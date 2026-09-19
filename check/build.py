"""Course build: concept records -> Book 0 and per-subject booklets.

Assembly emits plain markdown and is independent of the renderer, so swapping
Quarto for pandoc (or back) touches only `render()`. Run from the repo root:

    python course/build.py --check          # validation and reports only
    python course/build.py --subject S01    # assemble + render one booklet
    python course/build.py --all

The checks are the point. Writing 61 booklets without them produces a corpus
whose internal consistency nobody can verify.
"""
from __future__ import annotations
import argparse, json, os, re, shutil, subprocess, sys, datetime as dt
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
RECORDS, OUT = os.path.join(ROOT, "records"), os.path.join(ROOT, "_build")
SCHEMA = os.path.join(ROOT, "schema", "concept.schema.json")
BIB = os.path.join(ROOT, "references", "library.bib")
LEVELS = ["Introductory", "Intermediate", "Advanced", "Expert"]

KIND_FOR_TYPE = {
    "derivable":     {"textbook"},
    "empirical":     {"primary", "systematic_review"},
    "institutional": {"instrument", "guideline", "consensus_statement"},
}
STABILITY_FOR_TYPE = {"derivable": "long", "empirical": "medium", "institutional": "short"}

# Must-know points are a flexible list, not five fixed slots: a concept carries as many as it
# demands and no more. `bearing` is what keeps them pointed at the expertise being built rather
# than at general interest - every point has to change something the reader would do, say, accept
# or refuse in one of these five capacities.
MUST_KNOW_BEARINGS = ["clinical", "methodological", "policy", "teaching", "public"]
MUST_KNOW_SOFT_CAP = 9

# Prose fields must be authored as literal blocks. A folded scalar (`>`) turns a blank line into a
# single newline, which silently destroys every paragraph break and every markdown table in the
# field, and the damage is invisible in the record and only shows up in the rendered booklet.
PROSE_KEYS = ("text", "simplified_explanation", "body", "analogy_breaks_when",
              "point", "prompt", "answer", "note")
FOLDED_RE = re.compile(r"^\s*(?:- )?(" + "|".join(PROSE_KEYS) + r"):\s*>[-+]?\s*$", re.M)

# Sequence-read and plain-language thresholds (STYLE.md 10 and 11). Warnings, not errors:
# they mark places to look. The numbers are pinned by CALIBRATION below, so they cannot be
# quietly loosened until everything passes.
LONG_SENTENCE_WORDS = 25        # reader-facing prose
LONG_SENTENCE_WORDS_DEF = 35    # definition.text is allowed to be exact, so it is allowed to be long
READING_GRADE_MAX = 9.0
READING_GRADE_MAX_DEF = 14.0
LONG_PARAGRAPH_SENTENCES = 7

# There is a second defect the grade cannot see: prose chopped into fragments scores beautifully
# and reads worse. A floor was tried and withdrawn - the draft the reader chose has a procedural
# passage at mean 9.9 words, below any floor that would catch real choppiness elsewhere. Rhythm
# stays an editorial judgement (STYLE.md 11a), not a measure.

# A grade computed over one bullet is noise: a single 30-word sentence with three long words
# spikes it, and the author learns to ignore the whole report. Score passages, not fragments.
GRADE_MIN_WORDS = 60
STACCATO_MIN_WORDS = 90
MAX_WARNINGS_PER_FIELD = 2

# The two passages at the top of STYLE.md 11: the register the reader chose, and the sentence
# that made them stop. If a threshold change stops separating these two, the build says so.
CALIBRATION = {
    "standard": "Here is the trap with Indian law online. One Act can exist in several copies, "
                "made at different times, all sitting on the same government website. None of "
                "them says \"this one is old\". So you do it yourself: open the copy, find the "
                "list of amendments, look at the newest date. If that date is older than the "
                "thing you are checking, you have the wrong copy.",
    "rejected": "Indian statutes are frequently republished in consolidated editions of differing "
                "vintage, and official repositories host several at once without making the "
                "currency obvious. Checking the latest amendment a text mentions is a cheap and "
                "necessary habit.",
}


# ---------------------------------------------------------------- loading

def _yaml():
    try:
        import yaml
        return yaml
    except ModuleNotFoundError:
        sys.exit("pyyaml is required: run in the course-build environment.")


def load_subjects() -> dict:
    with open(os.path.join(ROOT, "subjects.json"), encoding="utf-8") as fh:
        return json.load(fh)


def load_clusters() -> dict:
    with open(os.path.join(ROOT, "clusters.yml"), encoding="utf-8") as fh:
        raw = _yaml().safe_load(fh)
    out = {}
    for group in ("primary", "overlay"):
        for key, val in (raw.get(group) or {}).items():
            out[key] = {**val, "group": group}
    return out


def load_records() -> dict:
    yaml = _yaml()
    recs = {}
    for dirpath, _, files in os.walk(RECORDS):
        for fn in sorted(files):
            if not fn.endswith((".yml", ".yaml")):
                continue
            with open(os.path.join(dirpath, fn), encoding="utf-8") as fh:
                raw = fh.read()
            r = yaml.safe_load(raw)
            if not r:
                continue
            r["_path"] = os.path.relpath(os.path.join(dirpath, fn), ROOT)
            r["_raw"] = raw
            recs[r["concept_id"]] = r
    return recs


def load_book0_outline() -> list[dict]:
    """Book 0's part structure, read from OUTLINE.md.

    The outline is the single source of truth for what Book 0 contains and in what order. Parsing
    it here means the booklet's part headings and its "n of N sections" line cannot drift from the
    plan, which is the failure this corpus has already had once with a hand-copied count.
    """
    path = os.path.join(ROOT, "book0", "OUTLINE.md")
    if not os.path.exists(path):
        return []
    parts, cur, idx = [], None, 0
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            h = re.match(r"^##\s+Part\s+([A-Z])\s+[·\-]\s+(.+?)\s*$", line)
            if h:
                cur = {"letter": h.group(1), "title": h.group(2), "sections": []}
                parts.append(cur)
                continue
            m = re.match(r"^\|\s*([A-Z]\d+)\s*\|\s*([^|]+?)\s*\|", line)
            if m and cur and m.group(1).startswith(cur["letter"]):
                idx += 1
                cur["sections"].append({"id": m.group(1), "name": m.group(2), "index": idx})
    return parts


def load_bib_keys() -> set:
    if not os.path.exists(BIB):
        return set()
    with open(BIB, encoding="utf-8") as fh:
        return set(re.findall(r"^@\w+\{([^,]+),", fh.read(), re.M))


# ------------------------------------------------- the sequence read

def prose_fields(r) -> list[tuple[str, str]]:
    """Every field a reader actually reads, in the order they meet it."""
    out = [("definition.text", (r.get("definition") or {}).get("text")),
           ("simplified_explanation", r.get("simplified_explanation")),
           ("illustration.body", (r.get("illustration") or {}).get("body")),
           ("illustration.analogy_breaks_when", (r.get("illustration") or {}).get("analogy_breaks_when"))]
    mk = r.get("must_know")
    if isinstance(mk, list):
        out += [(f"must_know[{i+1}]", p.get("point")) for i, p in enumerate(mk) if isinstance(p, dict)]
    for i, ex in enumerate(r.get("exercises") or []):
        out += [(f"exercise {i+1} prompt", ex.get("prompt")), (f"exercise {i+1} answer", ex.get("answer"))]
    return [(k, v) for k, v in out if isinstance(v, str) and v.strip()]


BULLET = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")


def _paragraphs(text: str) -> list[str]:
    """Prose paragraphs only.

    Table rows and headings are not prose and are not measured. A list is measured item by item,
    because three bullets are three thoughts however they are punctuated.
    """
    out = []
    for block in re.split(r"\n\s*\n", text):
        b = block.strip()
        if not b or b.lstrip().startswith(("|", "#", "```")):
            continue
        if BULLET.match(b):
            items = []
            for line in b.splitlines():
                if BULLET.match(line):
                    items.append(BULLET.sub("", line).strip())
                elif items and line.strip():
                    items[-1] += " " + line.strip()
            out += items
        else:
            out.append(b)
    return out


def _sentences(para: str) -> list[str]:
    flat = re.sub(r"\s+", " ", re.sub(r"[*_`]", "", para)).strip()
    flat = re.sub(r"\b(e\.g|i\.e|etc|vs|No|Dr|Mr|Ms|Art|s|ss)\.", r"\1<dot>", flat)
    parts = re.split(r"(?<=[.?!])\s+(?=[A-Z\"'(])", flat)
    return [p.replace("<dot>", ".").strip() for p in parts if p.strip()]


def _syllables(word: str) -> int:
    """Vowel-group count with the usual silent-e correction. Approximate on purpose.

    An exact syllabifier needs a pronunciation dictionary. The grade score here is used to
    compare one passage against another inside one corpus, and for that a consistent
    approximation is worth more than an accurate one that needs a dependency.
    """
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and groups > 1:
        groups -= 1
    return max(1, groups)


def reading_grade(text: str) -> float:
    """Flesch-Kincaid grade level. Roughly: the school year needed to read this cold."""
    sents = [s for p in _paragraphs(text) for s in _sentences(p)]
    words = [w for s in sents for w in s.split() if re.search(r"[A-Za-z]", w)]
    if not sents or not words:
        return 0.0
    syl = sum(_syllables(w) for w in words)
    return 0.39 * (len(words) / len(sents)) + 11.8 * (syl / len(words)) - 15.59


def load_hardwords() -> dict:
    path = os.path.join(ROOT, "prose", "hardwords.yml")
    if not os.path.exists(path):
        return {"replace": [], "teach_once": []}
    with open(path, encoding="utf-8") as fh:
        raw = _yaml().safe_load(fh) or {}
    for e in raw.get("replace") or []:
        e["_re"] = re.compile(r"\b(?:" + e["word"] + r")\b", re.I)
    for e in raw.get("teach_once") or []:
        e["_re"] = re.compile(r"\b(?:" + e["word"] + r")s?\b", re.I)
    return {"replace": raw.get("replace") or [], "teach_once": raw.get("teach_once") or []}


def readability(rid: str, r: dict, W, hard=None) -> None:
    """Warn where a cold sequential read would stumble. Every warning has a rewrite."""
    for field, text in prose_fields(r):
        is_def = field == "definition.text"
        max_words = LONG_SENTENCE_WORDS_DEF if is_def else LONG_SENTENCE_WORDS
        found = []
        sents = [s for p in _paragraphs(text) for s in _sentences(p)]
        n_words = len(text.split())

        for para in _paragraphs(text):
            ps = _sentences(para)
            if len(ps) > LONG_PARAGRAPH_SENTENCES:
                found.append(f"paragraph of {len(ps)} sentences - split it")
        worst = max(sents, key=lambda s: len(s.split()), default="")
        if worst and len(worst.split()) > max_words:
            found.append(f"{len(worst.split())}-word sentence carries too much - one idea per "
                         f"sentence (\"{' '.join(worst.split()[:8])}...\")")

        # grade and rhythm are measured on passages only; on a single bullet they are noise
        if n_words >= GRADE_MIN_WORDS:
            grade = reading_grade(text)
            limit = READING_GRADE_MAX_DEF if is_def else READING_GRADE_MAX
            if grade > limit:
                found.append(f"reading grade {grade:.1f} against a limit of {limit:.0f} - shorter "
                             "sentences and commoner words (STYLE.md 11)")


        # a hyphenated word wrapped across two lines renders with a space inside it
        if re.search(r"[A-Za-z]-\n[A-Za-z]", text):
            found.append("a hyphenated word is split across two lines and will render with a "
                         "space in the middle of it - rejoin it")

        # the definition is the one field allowed exact legal language, quoted as the law has it
        if not is_def:
            for e in (hard or {}).get("replace", []):
                m = e["_re"].search(text)
                if m:
                    found.append(f"\"{m.group(0)}\" is on the hard-word list - use {e['use']}"
                                 + (f" ({e['note']})" if e.get("note") else ""))

        for msg in found[:MAX_WARNINGS_PER_FIELD]:
            W(rid, f"{field}: {msg}")
        if len(found) > MAX_WARNINGS_PER_FIELD:
            W(rid, f"{field}: and {len(found) - MAX_WARNINGS_PER_FIELD} more")
    body = ((r.get("illustration") or {}).get("body") or "")
    if body and not re.search(r"\byou(r|rself)?\b", body, re.I):
        W(rid, "illustration.body never addresses the reader - check it shows the reader something "
               "to do rather than reporting work already done")


def acronym_defects(text: str) -> list[str]:
    """Acronyms used in the assembled booklet before anything expands them."""
    bad, seen_expansion = [], set()
    known = {"GST", "BMI", "NFHS", "ICMR", "RDA", "WHO", "DNA", "UK", "US", "UPF", "PDF", "HTML"}
    for m in re.finditer(r"\(([A-Z]{2,6})\)|\b([A-Z]{2,6})\b", text):
        if m.group(1):
            seen_expansion.add(m.group(1))
            continue
        a = m.group(2)
        if a in known or a in seen_expansion or a in bad:
            continue
        bad.append(a)
    return bad


# ---------------------------------------------------------------- checks

def check(recs: dict, subjects: dict, clusters: dict, bibkeys: set):
    """Returns (blocking, warnings). Blocking failures stop a render."""
    block, warn = [], []
    subj = subjects["subjects"]
    today = dt.date.today().isoformat()

    def E(rid, msg): block.append(f"{rid}: {msg}")
    def W(rid, msg): warn.append(f"{rid}: {msg}")

    # schema validation, if available
    try:
        import jsonschema
        with open(SCHEMA, encoding="utf-8") as fh:
            sch = json.load(fh)
        validator = jsonschema.Draft202012Validator(sch)
        for rid, r in recs.items():
            body = {k: v for k, v in r.items() if not k.startswith("_")}
            for err in validator.iter_errors(body):
                E(rid, "schema: " + "/".join(str(p) for p in err.path) + ": " + err.message)
    except ModuleNotFoundError:
        warn.append("jsonschema not installed - structural validation skipped")

    # the plain-language thresholds must still separate the two passages in STYLE.md 11
    hard = load_hardwords()
    g_ok, g_bad = reading_grade(CALIBRATION["standard"]), reading_grade(CALIBRATION["rejected"])
    if not (g_ok <= READING_GRADE_MAX < g_bad):
        block.append(f"prose thresholds no longer discriminate: the chosen register scores "
                     f"{g_ok:.1f} and the rejected sentence {g_bad:.1f} against a limit of "
                     f"{READING_GRADE_MAX:.0f} (STYLE.md 11)")
    if not any(e["_re"].search(CALIBRATION["rejected"]) for e in hard["replace"]):
        block.append("hard-word list no longer catches the sentence it was built from")

    order = {rid: (r.get("rung", 0), r.get("sequence", 0)) for rid, r in recs.items()}
    b0_index = {s["index"] for p in load_book0_outline() for s in p["sections"]}
    for rid, r in recs.items():
        ctype = r.get("concept_type")

        # Book 0 sequence numbers are positions in the outline, not free integers
        if r.get("subject") == "B0" and b0_index and r.get("sequence") not in b0_index:
            W(rid, f"sequence {r.get('sequence')} is not a section position in book0/OUTLINE.md")

        # reference kind must match concept type; locator mandatory
        for ref in (r.get("definition", {}) or {}).get("references", []) or []:
            if ctype and ref.get("kind") not in KIND_FOR_TYPE.get(ctype, set()):
                E(rid, f"reference kind '{ref.get('kind')}' invalid for concept_type '{ctype}'")
            if not (ref.get("locator") or "").strip():
                E(rid, f"reference '{ref.get('citekey')}' has no locator")
            if bibkeys and ref.get("citekey") not in bibkeys:
                E(rid, f"citekey '{ref.get('citekey')}' not in library.bib")
            v = ref.get("verified") or {}
            if not v.get("opened"):
                W(rid, f"reference '{ref.get('citekey')}' not yet opened")
            elif not v.get("claim_located"):
                W(rid, f"reference '{ref.get('citekey')}' opened but claim not located")

        # review clock consistency
        rev = r.get("review") or {}
        want = STABILITY_FOR_TYPE.get(ctype)
        if want and rev.get("stability") != want:
            E(rid, f"review.stability '{rev.get('stability')}' inconsistent with concept_type '{ctype}'")
        if ctype == "institutional" and not rev.get("as_of"):
            W(rid, "institutional concept has no review.as_of")
        trig = str(rev.get("trigger") or "")
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", trig) and trig < today:
            W(rid, f"review overdue (trigger {trig})")

        # must-know points: as many as the concept demands, each one load-bearing
        mk = r.get("must_know")
        if isinstance(mk, dict):
            E(rid, "must_know is a mapping - the five fixed slots were retired. Write a list of "
                   "points, each with 'point' and 'bearing'.")
        else:
            pts = [p for p in (mk or []) if isinstance(p, dict)]
            if not pts:
                E(rid, "must_know has no points")
            if len(pts) > MUST_KNOW_SOFT_CAP:
                W(rid, f"{len(pts)} must-know points against a soft cap of {MUST_KNOW_SOFT_CAP} - "
                       "check whether some belong in the illustration or an exercise instead")
            kinds = {p.get("kind") for p in pts}
            if not ({"misconception", "trap"} & kinds):
                W(rid, "no must-know point tagged 'misconception' or 'trap' - what does a reader "
                       "who half-knows this get wrong?")
            for i, p in enumerate(pts):
                if re.search(r"\n\s*\n", p.get("point") or ""):
                    W(rid, f"must_know[{i+1}] runs to more than one paragraph - a point is one point")
                for ck in p.get("refs") or []:
                    if bibkeys and ck not in bibkeys:
                        E(rid, f"must_know[{i+1}] cites '{ck}', which is not in library.bib")

        # prose fields authored as folded scalars lose their paragraph breaks and tables
        for key in sorted(set(FOLDED_RE.findall(r.get("_raw") or ""))):
            E(rid, f"'{key}' is authored with a folded scalar '>': paragraph breaks and tables are "
                   "silently destroyed. Use a literal block '|'.")

        readability(rid, r, W, hard)

        # illustration failure boundary
        ill = r.get("illustration") or {}
        if not (ill.get("analogy_breaks_when") or "").strip():
            E(rid, "illustration.analogy_breaks_when is empty")

        # scope gate
        if not ((r.get("provenance") or {}).get("outcome_refs") or []):
            E(rid, "no provenance.outcome_refs - serves no outcome, so out of scope")

        # clusters must exist
        for ck in r.get("clusters") or []:
            if ck not in clusters:
                E(rid, f"unknown cluster '{ck}'")

        # dependency integrity: no forward references inside a subject
        for dep in r.get("concept_deps") or []:
            if dep not in recs:
                E(rid, f"concept_deps references missing record '{dep}'")
            elif recs[dep].get("subject") == r.get("subject") and order[dep] >= order[rid]:
                E(rid, f"forward reference to '{dep}' in the same subject")
        for dep in r.get("ground_floor_deps") or []:
            if dep not in recs:
                W(rid, f"ground_floor_deps references missing Book 0 record '{dep}' (write it or drop it)")

        # answers must exist for every exercise; integrative belongs elsewhere
        for i, ex in enumerate(r.get("exercises") or []):
            if not (ex.get("answer") or "").strip():
                E(rid, f"exercise {i+1} has no worked answer")
            if ex.get("type") == "integrative":
                E(rid, f"exercise {i+1} is 'integrative' - reserved for the interleaving sets, "
                       "which are composed from concept records rather than authored inside them")

    # skill coverage per subject-rung, against the frozen map
    covered = defaultdict(set)
    for r in recs.values():
        for ex in r.get("exercises") or []:
            if ex.get("skill_ref"):
                covered[(r.get("subject"), r.get("rung"))].add(ex["skill_ref"])
    present = {(r.get("subject"), r.get("rung")) for r in recs.values()}
    for sid, rung in sorted(present):
        if sid == "B0":
            continue
        key = "rung1" if rung == 1 else ("rung2" if rung == 2 else None)
        skills = ((subj.get(sid) or {}).get(key) or {}).get("skills") or []
        for n in range(len(skills)):
            if f"{sid}-R{rung}-K{n+1:02d}" not in covered[(sid, rung)]:
                warn.append(f"{sid} rung {rung}: skill K{n+1:02d} has no exercise")

    # bridge sufficiency, where a rung above exists
    for sid, rung in sorted(present):
        if sid == "B0" or rung != 1:
            continue
        if not (subj.get(sid) or {}).get("rung2"):
            continue  # S61: terminal rung, scoped against its gate instead
        discharged = set()
        for r in recs.values():
            if r.get("subject") == sid and r.get("rung") == 1:
                discharged |= set((r.get("provenance") or {}).get("bridge_ref") or [])
        n_pre = len((subj[sid]["rung2"].get("concepts") or []))
        missing = [f"{sid}-R2-P{i+1:02d}" for i in range(n_pre)
                   if f"{sid}-R2-P{i+1:02d}" not in discharged]
        if missing:
            warn.append(f"{sid}: bridge test - {len(missing)}/{n_pre} rung-2 presuppositions undischarged")
    return block, warn


# ---------------------------------------------------------------- assembly

def _refs(r):
    out = []
    for ref in (r.get("definition", {}) or {}).get("references", []) or []:
        v = ref.get("verified") or {}
        flag = "" if v.get("claim_located") else " *[unverified]*"
        out.append(f"[@{ref['citekey']}, {ref['locator']}]{flag}")
    return " ".join(out)


def concept_md(r, label=None) -> list[str]:
    md = [f"### {label + ' · ' if label else ''}{r['name']}", ""]
    md += [f"*{r['concept_id']} · {r['concept_type']}"
           + (f" · as of {r['review'].get('as_of')}" if r.get("review", {}).get("as_of") else "") + "*", ""]
    md += ["**Definition.** " + r["definition"]["text"] + " " + _refs(r), ""]
    md += ["**In plain terms.** " + r["simplified_explanation"], ""]
    ill = r["illustration"]
    md += ["**Illustration.** " + ill["body"], "",
           "**Where this picture breaks.** " + ill["analogy_breaks_when"], ""]
    mk = r.get("must_know") if isinstance(r.get("must_know"), list) else []
    rows = [f"- {' '.join((p.get('point') or '').split())}" for p in mk
            if isinstance(p, dict) and (p.get("point") or "").strip()]
    if rows:
        md += ["**Must know points for you.**", ""] + rows + [""]
    return md


def booklet_md(sid, recs, subjects, clusters) -> tuple[str, list[str]]:
    subj = subjects["subjects"]
    mine = sorted([r for r in recs.values() if r.get("subject") == sid],
                  key=lambda r: (r.get("rung", 0), r.get("sequence", 0)))
    if sid == "B0":
        title, status, target, nr = "Book 0 · Ground floor", "foundations", "-", 0
    else:
        s = subj[sid]
        title, target, nr = f"{sid} · {s['title']}", s["target"], s["n_rungs"]
        done = sorted({r["rung"] for r in mine})
        rng = (f"Rung {done[0]}" if len(done) == 1 else f"Rungs {done[0]}\u2013{done[-1]}") if done else "nothing"
        rest = [str(k) for k in range(1, nr + 1) if k not in done]
        status = f"{rng} released" + (f" · rung{'s' if len(rest) > 1 else ''} {', '.join(rest)} in preparation" if rest else " · complete")

    md = [f"# {title}", ""]
    outline = load_book0_outline() if sid == "B0" else []
    where = {s["index"]: (p, s) for p in outline for s in p["sections"]}
    if sid == "B0" and outline:
        total = len(where)
        md += [f"**Edition 0.1 (draft)** · {len(mine)} of {total} sections written", "",
               "This book teaches the ground floor once, so that every other booklet can stand on "
               "it. It assumes you can read English and use a calculator. It assumes nothing else: "
               "no medicine, no biology, no remembered mathematics.", "",
               "Read it in order. Each section assumes everything before it and nothing after it. "
               "If a section looks easy, read it anyway and read it quickly — it is here because "
               "something later needs it.", "",
               f"Sections keep the numbering of the full plan of {total}, so a gap in the numbers "
               "is a section not yet written rather than one you have missed.", ""]
    if sid != "B0":
        md += [f"**Target level: {target}** · {status} · edition 0.1 (draft)", "",
               f"*Ground floor: see Book 0. Derived against subject map `{subjects['source_map_version_id']}`.*", ""]
        gf = sorted({d for r in mine for d in (r.get("ground_floor_deps") or [])})
        if gf:
            md += ["## Before you start", "",
                   "This booklet uses the following Book 0 sections. Each is summarised where it is first "
                   "needed; work through Book 0 itself if a summary is not enough.", ""]
            md += [f"- `{d}`" + (f" — {recs[d]['name']}" if d in recs else "") for d in gf] + [""]
    answers, seen_part = [], None
    for rung in sorted({r.get("rung", 0) for r in mine}):
        band = [r for r in mine if r.get("rung", 0) == rung]
        if sid != "B0":
            md += [f"## Rung {rung} — {LEVELS[rung-1]}", ""]
        for r in band:
            label = None
            if sid == "B0":
                part, sec = where.get(r.get("sequence"), (None, None))
                if part and part["letter"] != seen_part:
                    seen_part = part["letter"]
                    md += [f"## Part {part['letter']} · {part['title']}", ""]
                label = sec["id"] if sec else None
            md += concept_md(r, label)
            for i, ex in enumerate(r.get("exercises") or []):
                tag = f"{r['concept_id']}-E{i+1}"
                md += [f"**Exercise {tag}** ({ex['type']}). {ex['prompt']}"
                       + ("  \n*Record your confidence as a percentage before turning to the answer.*"
                          if ex.get("confidence_first") else ""), ""]
                answers += [f"**{tag}.** {ex['answer']}", ""]
    if answers:
        md += ["\\newpage", "", "# Appendix · Worked answers", ""] + answers
    return "\n".join(md), [r["concept_id"] for r in mine]


# ---------------------------------------------------------------- reports

def reports(recs, subjects, clusters, block, warn):
    os.makedirs(OUT, exist_ok=True)
    today = dt.date.today().isoformat()

    nums = [["concept_id", "value", "unit", "citekey", "as_of"]]
    due = [["concept_id", "type", "stability", "trigger", "as_of", "last_reviewed"]]
    retr = []
    for rid in sorted(recs):
        r = recs[rid]
        for n in ((r.get("illustration") or {}).get("numbers") or []):
            nums.append([rid, str(n.get("value", "")), n.get("unit", ""), n.get("citekey", ""), n.get("as_of", "")])
        rev = r.get("review") or {}
        trig = str(rev.get("trigger") or "")
        overdue = re.fullmatch(r"\d{4}-\d{2}-\d{2}", trig) and trig < today
        if overdue or rev.get("stability") == "short":
            due.append([rid, r.get("concept_type", ""), rev.get("stability", ""), trig,
                        rev.get("as_of", ""), rev.get("last_reviewed", "")])
        for it in r.get("retrieval_items") or []:
            retr.append({"concept_id": rid, "subject": r.get("subject"), "rung": r.get("rung"),
                         "clusters": r.get("clusters"), "q": it["q"], "a": it["a"]})

    def csv(path, rows):
        with open(os.path.join(OUT, path), "w", encoding="utf-8") as fh:
            fh.write("\n".join(",".join('"' + str(c).replace('"', '""') + '"' for c in row) for row in rows))

    csv("numbers_register.csv", nums)
    csv("review_due.csv", due)
    with open(os.path.join(OUT, "retrieval_items.json"), "w", encoding="utf-8") as fh:
        json.dump(retr, fh, indent=1)
    bearings = defaultdict(int)
    for r in recs.values():
        mk = r.get("must_know") if isinstance(r.get("must_know"), list) else []
        for p in mk:
            if isinstance(p, dict):
                bearings[p.get("bearing") or "untagged"] += 1

    hard = load_hardwords()
    ordered = sorted(recs.values(), key=lambda r: (r.get("subject", ""), r.get("rung", 0),
                                                   r.get("sequence", 0)))
    grades = []
    for r in ordered:
        for field, text in prose_fields(r):
            if field != "definition.text" and len(text.split()) >= GRADE_MIN_WORDS:
                grades.append((reading_grade(text), r["concept_id"], field))
    first_use = {}
    for r in ordered:
        blob = "\n".join(t for _, t in prose_fields(r))
        for e in hard["teach_once"]:
            if e["word"] not in first_use and e["_re"].search(blob):
                first_use[e["word"]] = (r["concept_id"], e.get("gloss_hint", ""))

    with open(os.path.join(OUT, "check_report.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# Build check report\n\n{today} · {len(recs)} records\n\n")
        if grades:
            worst = sorted(grades, reverse=True)[:8]
            fh.write("## Plain language\n\n"
                     f"Reading grade, worst {len(worst)} reader-facing fields. "
                     f"Limit {READING_GRADE_MAX:.0f}; `definition.text` is exempt and held to "
                     f"{READING_GRADE_MAX_DEF:.0f} (STYLE.md §11).\n\n"
                     "| Grade | Concept | Field |\n| --- | --- | --- |\n")
            for g, cid, field in worst:
                fh.write(f"| {g:.1f}{' ⚠' if g > READING_GRADE_MAX else ''} | {cid} | {field} |\n")
            fh.write("\n")
        if first_use:
            fh.write("## Terms of art, first use\n\n"
                     "Each of these survives because the subject needs it. Check that the section "
                     "named here gives it in plain words.\n\n"
                     "| Term | First used in | Plain words it needs |\n| --- | --- | --- |\n")
            for w, (cid, hint) in first_use.items():
                fh.write(f"| {w} | {cid} | {hint} |\n")
            fh.write("\n")
        fh.write("## Must-know points by bearing\n\n"
                 "What each point changes for the reader. A corpus tilted entirely one way is not "
                 "wrong, but it should be a decision rather than a habit.\n\n"
                 "| Bearing | Points |\n| --- | --- |\n")
        for b in MUST_KNOW_BEARINGS + ["untagged"]:
            if bearings.get(b):
                fh.write(f"| {b} | {bearings[b]} |\n")
        fh.write("\n")
        fh.write(f"## Blocking ({len(block)})\n\n" + ("\n".join(f"- {b}" for b in block) or "- none") + "\n\n")
        fh.write(f"## Warnings ({len(warn)})\n\n" + ("\n".join(f"- {w}" for w in warn) or "- none") + "\n")
    return {"numbers": len(nums) - 1, "review_due": len(due) - 1, "retrieval": len(retr)}


# ---------------------------------------------------------------- render

def _launch(exe):
    """Windows ships quarto as a .CMD wrapper, which subprocess cannot exec directly."""
    if exe and exe.lower().endswith((".cmd", ".bat")):
        return ["cmd", "/c", exe]
    return [exe]


def _works(exe, probe=("--version",)):
    """Runtime capability probe, not a path check.

    A launcher can be on PATH and still be unusable - the conda quarto package on
    Windows ships quarto.cmd plus quarto.js with no runtime, so which() finds it and
    every invocation fails. Probe once, believe the result.
    """
    if not exe:
        return False
    try:
        p = subprocess.run(_launch(exe) + list(probe), capture_output=True, text=True, timeout=120)
        return p.returncode == 0 and bool((p.stdout or "").strip())
    except Exception:
        return False


def _pdf_engine_ok():
    """True only if some engine can actually compile, not merely report a version."""
    if getattr(_pdf_engine_ok, "_cached", None) is not None:
        return _pdf_engine_ok._cached
    ok = False
    for eng in ("xelatex", "pdflatex", "lualatex", "tectonic"):
        exe = shutil.which(eng)
        if not exe:
            continue
        probe = os.path.join(OUT, "_pdfprobe")
        os.makedirs(probe, exist_ok=True)
        tex = os.path.join(probe, "p.tex")
        with open(tex, "w", encoding="utf-8") as fh:
            fh.write("\\documentclass{article}\\begin{document}x\\end{document}\n")
        env = dict(os.environ, TECTONIC_CACHE_DIR=probe, XDG_CACHE_HOME=probe)
        args = ["-X", "compile", tex, "--outdir", probe] if eng == "tectonic" else \
               ["-interaction=nonstopmode", "-output-directory", probe, tex]
        try:
            p = subprocess.run(_launch(exe) + args, capture_output=True, text=True, timeout=300, env=env)
            ok = p.returncode == 0 and os.path.exists(os.path.join(probe, "p.pdf"))
        except Exception:
            ok = False
        shutil.rmtree(probe, ignore_errors=True)
        if ok:
            break
    _pdf_engine_ok._cached = ok
    return ok


def render(md_path, stem):
    """Quarto where usable, pandoc otherwise. Content is renderer-agnostic."""
    made, pandoc = [], shutil.which("pandoc")
    quarto = shutil.which("quarto")
    quarto = quarto if _works(quarto) else None
    formats = [("docx", "docx"), ("html", "html")]
    if _pdf_engine_ok():
        formats.append(("pdf", "pdf"))
    elif not getattr(render, "_pdf_warned", False):
        render._pdf_warned = True
        print("  [pdf] skipped: no working PDF engine. tectonic runs but cannot resolve Windows "
              "platform directories inside the sandbox; install a LaTeX engine or convert from docx.")
    args_common = ["--citeproc", f"--bibliography={os.path.abspath(BIB)}"] if os.path.exists(BIB) else []
    for fmt, ext in formats:
        target = os.path.join(OUT, f"{stem}.{ext}")
        if quarto:
            cmd = _launch(quarto) + ["render", os.path.basename(md_path),
                                     "--to", fmt, "--output", f"{stem}.{ext}"]
            cwd = OUT
        else:
            engine = ["--pdf-engine=tectonic"] if fmt == "pdf" and shutil.which("tectonic") else []
            cmd = _launch(pandoc or "pandoc") + [md_path, "-o", target, "--from",
                   "markdown-yaml_metadata_block", "--toc", "--toc-depth=3"] + args_common + engine
            cwd = None
        env = dict(os.environ)
        if fmt == "pdf":
            # tectonic cannot locate platform cache dirs inside the sandbox
            cache = os.path.join(ROOT, "_build", ".tectonic-cache")
            os.makedirs(cache, exist_ok=True)
            env["TECTONIC_CACHE_DIR"] = cache
            env.setdefault("XDG_CACHE_HOME", cache)
        p = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd, env=env)
        if p.returncode == 0 and os.path.exists(target):
            made.append(f"{stem}.{ext}")
        else:
            tail = (p.stderr or p.stdout or "").strip().splitlines()
            print(f"  [{fmt}] not produced: {tail[-1] if tail else 'unknown error'}")
    return made


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject", action="append", default=[])
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    subjects, clusters, recs = load_subjects(), load_clusters(), load_records()
    bibkeys = load_bib_keys()
    block, warn = check(recs, subjects, clusters, bibkeys)
    counts = reports(recs, subjects, clusters, block, warn)

    print(f"records {len(recs)} | clusters {len(clusters)} | blocking {len(block)} | warnings {len(warn)}")
    print(f"reports: numbers {counts['numbers']}, review-due {counts['review_due']}, retrieval {counts['retrieval']}")
    for b in block[:15]:
        print("  BLOCK", b)
    if a.check:
        return 1 if block else 0
    if block:
        print("blocking failures - not rendering")
        return 1

    os.makedirs(OUT, exist_ok=True)
    todo = a.subject or (sorted({r.get("subject") for r in recs.values()}) if a.all else [])
    for sid in todo:
        md, ids = booklet_md(sid, recs, subjects, clusters)
        path = os.path.join(OUT, f"{sid}.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(md + "\n")
        stumbles = acronym_defects(md)
        if stumbles:
            print(f"  [{sid}] used before anything expands them: {', '.join(stumbles)}")
        print(f"{sid}: {len(ids)} concepts ->", ", ".join(render(path, sid)) or "markdown only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
