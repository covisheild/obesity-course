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
REFDOC = os.path.join(ROOT, "references", "reference.docx")
FIGURES_DIR = os.path.join(ROOT, "figures")
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

# The drill set is a range, not a number. Ten began as a working figure and was briefly enforced
# as an equality, which made concepts pad to reach it and trim to avoid exceeding it - the count
# started driving the teaching instead of following it. What has to hold is that the ladder is
# climbed: the reader meets the technique mechanically, applies it, diagnoses a broken version of
# it, and carries it somewhere new. A concept with one move reaches that in four problems; a
# concept with several may need eighteen. Outside the range, `practice_note` must say why.
PRACTICE_MIN, PRACTICE_MAX = 3, 18
PRACTICE_BANDS = [(1, 3, "mechanical"), (4, 6, "applied"), (7, 8, "diagnostic"), (9, 10, "transfer")]


def BAND_OF(level: int) -> str:
    for lo, hi, name in PRACTICE_BANDS:
        if lo <= level <= hi:
            return name
    return "transfer" if level > 10 else "mechanical"

# Which Book 0 Parts teach technique. Read off book0/OUTLINE.md: A numbers, B units, C
# relationships and change, D uncertainty. E is the physical and living world and F is reading and
# reasoning, and neither teaches a calculation the reader must be able to perform. A record may
# override this either way with an explicit `quantitative`.
MATHEMATICAL_PARTS = {"A", "B", "C", "D"}

# Prose fields must be authored as literal blocks. A folded scalar (`>`) turns a blank line into a
# single newline, which silently destroys every paragraph break and every markdown table in the
# field, and the damage is invisible in the record and only shows up in the rendered booklet.
PROSE_KEYS = ("text", "simplified_explanation", "body", "analogy_breaks_when",
              "point", "prompt", "answer", "note")
FOLDED_RE = re.compile(r"^\s*(?:- )?(" + "|".join(PROSE_KEYS) + r"):\s*>[-+]?\s*$", re.M)

# Sequence-read and plain-language thresholds (the style sheet §10 and 11). Warnings, not errors:
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
# stays an editorial judgement (the style sheet §11a), not a measure.

# A grade computed over one bullet is noise: a single 30-word sentence with three long words
# spikes it, and the author learns to ignore the whole report. Score passages, not fragments.
GRADE_MIN_WORDS = 60
STACCATO_MIN_WORDS = 90
MAX_WARNINGS_PER_FIELD = 2

# The two passages at the top of the style sheet §11: the register the reader chose, and the sentence
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
    for p in (r.get("practice") or []):
        if isinstance(p, dict):
            lv = p.get("level")
            out += [(f"practice {lv} prompt", p.get("prompt")), (f"practice {lv} answer", p.get("answer"))]
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
                             "sentences and commoner words (the style sheet §11)")


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

# Every other check in this file is structural: is the field present, is the citekey in the
# bibliography, does the ladder reach both ends. None of them asks whether anything is *true*.
# For a book whose content is arithmetic that is the wrong place to stop - a worked answer with
# a slip in it passes every gate, reaches the reader, and teaches the slip.
#
# Two things make it checkable. The prose writes operators as words, consistently, because §1
# requires it; and the answers show every line, because §4 does. So most of the arithmetic in
# the corpus is machine-evaluable without anyone writing it twice.
#
# Two things make it subtle, and both are in the material by design:
#   - Levels 7 and 8 are diagnostic. Their prompts contain a *deliberately wrong* worked answer
#     for the reader to break. Checking those would flag the teaching as a defect.
#   - Answers round. `17 divided by 7 = 2.428571429` is right, and exact comparison says it is
#     not. Tolerance is set from the digits actually shown.

_OPS = [(r"\bdivided by\b", "/"), (r"\btimes\b", "*"), (r"\bplus\b", "+"),
        (r"\bminus\b", "-"), (r"\bover\b", "/")]
_ARITH_SAFE = re.compile(r"^[\d\s.+\-*/()]+$")


def _arith_value(expr: str):
    """Evaluate one side of an equation, or None if it is not plain arithmetic."""
    e = expr.strip()
    for word, sym in _OPS:
        e = re.sub(word, sym, e)
    e = e.replace("^", "**")
    e = re.sub(r"(?<=\d),(?=\d)", "", e)           # 1,00,000 and 1,000,000 alike
    e = re.sub(r"\s*\([^)]*\)\s*$", "", e).strip()  # a trailing parenthetical comment
    if not _ARITH_SAFE.match(e) or not re.search(r"\d", e):
        return None
    if re.search(r"\*\*\s*\(", e) or len(e) > 120:
        return None
    try:
        v = eval(e, {"__builtins__": {}}, {})       # noqa: S307 - guarded by _ARITH_SAFE
    except Exception:
        return None
    return v if isinstance(v, (int, float)) and abs(v) < 1e18 else None


def _decimals_shown(expr: str) -> int:
    return max((len(m.group(1)) for m in re.finditer(r"\.(\d+)", expr)), default=0)


def check_arithmetic(r: dict) -> list:
    """Evaluate both sides of every equation in a record's reader-facing prose."""
    out = []

    def scan(text, where):
        for line in str(text or "").split("\n"):
            t = line.strip()
            if t.count("=") < 1 or "==" in t:
                continue
            sides = [p for p in t.split("=") if p.strip()]
            if len(sides) < 2:
                continue
            vals = [_arith_value(p) for p in sides]
            if any(v is None for v in vals):
                continue
            # Compare at the precision the text itself displays.
            places = min(_decimals_shown(p) for p in sides)
            tol = max(10 ** -places, abs(vals[0]) * 1e-9) if places else abs(vals[0]) * 1e-9
            if max(vals) - min(vals) > tol + 1e-12:
                out.append((where, t, vals))

    d = r.get("definition") or {}
    scan(d.get("text"), "definition")
    scan(r.get("simplified_explanation"), "simplified_explanation")
    for ill in ([r.get("illustration")] if r.get("illustration") else []) + (r.get("illustrations") or []):
        if isinstance(ill, dict):
            scan(ill.get("body"), "illustration")
            scan(ill.get("analogy_breaks_when"), "illustration.analogy_breaks_when")
    for q in (r.get("must_know") or []):
        if isinstance(q, dict):
            scan(q.get("point"), "must_know")
    for i, ex in enumerate(r.get("exercises") or [], 1):
        scan(ex.get("prompt"), f"exercise {i} prompt")
        scan(ex.get("answer"), f"exercise {i} answer")
    for q in (r.get("practice") or []):
        if not isinstance(q, dict):
            continue
        lvl = q.get("level")
        # The diagnostic band's prompt is a wrong answer on purpose. Its worked answer is not.
        if BAND_OF(lvl) != "diagnostic":
            scan(q.get("prompt"), f"practice {lvl} prompt")
        scan(q.get("answer"), f"practice {lvl} answer")
    return out


def _source_text(citekey: str):
    """The text of the source file behind a citekey, if this repository holds one."""
    if not citekey:
        return None
    cache = getattr(_source_text, "_cache", None)
    if cache is None:
        cache = _source_text._cache = {}
    if citekey not in cache:
        src = os.path.join(os.path.dirname(ROOT), "sources")
        idx, text = {}, None
        ipath = os.path.join(src, "INDEX.yml")
        if os.path.exists(ipath):
            with open(ipath, encoding="utf-8") as fh:
                idx = _yaml().safe_load(fh) or {}
        entry = (idx.get("files") or {}).get(citekey)
        if entry:
            path = os.path.join(src, entry["file"])
            if os.path.exists(path):
                with open(path, encoding="utf-8", errors="replace") as fh:
                    text = " ".join(fh.read().split()).lower()
        cache[citekey] = text
    return cache[citekey]


def _do_not_cite() -> dict:
    """Files held in sources/ that must never back a claim."""
    ipath = os.path.join(os.path.dirname(ROOT), "sources", "INDEX.yml")
    if not os.path.exists(ipath):
        return {}
    with open(ipath, encoding="utf-8") as fh:
        return (_yaml().safe_load(fh) or {}).get("do_not_cite") or {}


def check_quotes(r: dict) -> tuple:
    """Search the source file for the words a record says it took from it.

    This is the only check in the build that reads a source. Until it existed the audit
    was a prompt handed to a subagent with nothing behind it: the instruction said to
    quote the exact words out of the file in sources/, and the quote went into the
    subagent's report and then nowhere. A claim that was never in the file passed exactly
    as cleanly as one that was, because the only artefact of the check was the checker's
    own assurance that it had checked.

    A quote that is present is a fact verified mechanically. A quote that is absent is
    precisely the failure the audit exists to catch - a claim that reads plausibly and is
    not in the source - and it blocks. Whitespace and case are normalised, because a
    passage copied out of a PDF rewraps; nothing else is relaxed.
    """
    block, warn = [], []

    def look(citekey, quote, where):
        text = _source_text(citekey)
        if text is None or not quote:
            return None
        if " ".join(str(quote).split()).lower() in text:
            return True
        block.append(f"{where}: the quoted words are not in sources/{citekey}.txt - "
                     f"\"{' '.join(str(quote).split())[:70]}\". Either the passage says "
                     "something else, or the claim did not come from it")
        return False

    for i, ref in enumerate((r.get("definition") or {}).get("references") or [], 1):
        if not isinstance(ref, dict):
            continue
        key, quote = ref.get("citekey"), ref.get("quote")
        banned = _do_not_cite()
        if key in banned:
            block.append(f"definition reference {i} cites '{key}', which sources/INDEX.yml "
                         f"marks do-not-cite: {' '.join(str(banned[key].get('why','')).split())}")
        look(key, quote, f"definition reference {i}")
        # A local source with no quote can be confirmed by nobody except whoever ticked
        # the box, so a located claim without one is an assurance rather than a check.
        # A reference to a source this repository holds must carry the words it relies on.
        # Without them the citation is an assurance, and an assurance is what the audit was
        # already producing before this check existed.
        if _source_text(key) is not None and not quote:
            block.append(f"definition reference {i} cites '{key}', which is held in sources/, "
                         "but carries no 'quote'. Copy the exact words the claim rests on so "
                         "the build can find them")

    for n, num in enumerate((r.get("illustration") or {}).get("numbers") or [], 1):
        if not isinstance(num, dict):
            continue
        where = f"illustration number {n} ({num.get('value')})"
        look(num.get("citekey"), num.get("quote"), where)
        if _source_text(num.get("citekey")) is not None and not num.get("quote"):
            block.append(f"{where} comes from a source held in sources/ but carries no "
                         "'quote'. A figure nobody can trace back to its words is the one "
                         "kind of error a reader cannot catch")
    return block, warn


def check_doc_paths() -> list:
    """Every repository path the instruction documents name must exist.

    The documents rot silently and in a particular way: a file is renamed or merged, the
    prompts that point at it keep pointing, and the next chat to follow one improvises. A
    drafting prompt was found citing two template paths that had not existed for weeks,
    alongside error messages sending readers to a STYLE.md that had been folded into
    claude.md. Nothing catches that except looking, so this looks.

    Per-subject files (READY.md, DEFECTS.md, INVENTORY.md and the like) are named
    generically in the documents and are skipped; they exist once a subject exists.
    """
    repo = os.path.dirname(ROOT)
    generic = {"READY.md", "DEFECTS.md", "INVENTORY.md", "HANDOVER.md", "SOURCES.md",
               "CLAUDE.md", "OUTLINE.md"}
    out, pat = [], re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_./-]*\.(?:md|py|yml|yaml|json|bib|docx))`")
    for doc in ("claude.md", "PIPELINE.md", "PARALLEL.md", "MEASUREMENTS.md"):
        full = os.path.join(repo, doc)
        if not os.path.exists(full):
            continue
        with open(full, encoding="utf-8") as fh:
            text = fh.read()
        seen = set()
        for m in pat.finditer(text):
            p = m.group(1)
            if p in seen or os.path.basename(p) in generic or "<" in p or "SUBJECT" in p:
                continue
            seen.add(p)
            if p.startswith("books/"):
                continue
            if not (os.path.exists(os.path.join(repo, p)) or os.path.exists(os.path.join(ROOT, p))):
                out.append(f"{doc} names `{p}`, which does not exist - a chat following this "
                           "document will improvise")
    return out


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

    # the plain-language thresholds must still separate the two passages in the style sheet §11
    hard = load_hardwords()
    g_ok, g_bad = reading_grade(CALIBRATION["standard"]), reading_grade(CALIBRATION["rejected"])
    if not (g_ok <= READING_GRADE_MAX < g_bad):
        block.append(f"prose thresholds no longer discriminate: the chosen register scores "
                     f"{g_ok:.1f} and the rejected sentence {g_bad:.1f} against a limit of "
                     f"{READING_GRADE_MAX:.0f} (the style sheet §11)")
    if not any(e["_re"].search(CALIBRATION["rejected"]) for e in hard["replace"]):
        block.append("hard-word list no longer catches the sentence it was built from")

    order = {rid: (r.get("rung", 0), r.get("sequence", 0)) for rid, r in recs.items()}
    outline = load_book0_outline()
    b0_index = {s["index"] for p in outline for s in p["sections"]}
    b0_part = {s["index"]: p["letter"] for p in outline for s in p["sections"]}
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
            # How bad an unopened source is depends entirely on the concept type, and treating
            # every one as a warning is what let eleven of them sit for days.
            #
            # A `derivable` concept can be checked without its source: the reader rebuilds it
            # from the floor, and the textbook is a canonical anchor rather than the evidence.
            # An unopened anchor there is a debt, so it warns.
            #
            # An `empirical` or `institutional` concept cannot be checked that way at all. Its
            # content is true because a study measured it or a body decided it, and with the
            # source unopened there is nothing standing behind the claim except whoever drafted
            # it - which, for a record drafted by a model, means nothing stands behind it. That
            # is how a confidently-worded invention reaches a reader who has no way to catch it,
            # and it is the failure that scales badly into the clinical and policy subjects. It
            # blocks.
            v = ref.get("verified") or {}
            uncheckable = ctype in ("empirical", "institutional")
            if not v.get("opened"):
                (E if uncheckable else W)(rid, f"reference '{ref.get('citekey')}' not yet opened"
                                   + (f" - a {ctype} claim cannot rest on an unopened source, "
                                      "because nothing else can check it" if uncheckable else ""))
            elif not v.get("claim_located"):
                (E if uncheckable else W)(rid, f"reference '{ref.get('citekey')}' opened but the claim "
                                   "was not located in it"
                                   + (" - find the passage or change the claim" if uncheckable else ""))

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

        # The drill set. Ten was a working figure, not a law, and enforcing it as an
        # equality forced concepts to pad or to cut. What actually has to hold is that the
        # ladder is climbed: mechanical, applied, diagnostic and transfer bands all
        # represented, in rising order, with enough repetition to make the technique
        # automatic. A concept with one move needs fewer; a concept with several needs more.
        quant = r.get("quantitative")
        if quant is None:
            quant = (r.get("subject") == "B0"
                     and b0_part.get(r.get("sequence")) in MATHEMATICAL_PARTS)
        prac = [p for p in (r.get("practice") or []) if isinstance(p, dict)]
        if quant:
            excused = (r.get("practice_note") or "").strip()
            if not PRACTICE_MIN <= len(prac) <= PRACTICE_MAX and not excused:
                E(rid, f"quantitative concept carries {len(prac)} practice problems; the range is "
                       f"{PRACTICE_MIN} to {PRACTICE_MAX} (the style sheet §7a). Judge it by the technique: "
                       "one move needs few, several moves need many. Outside this range, say why "
                       "in 'practice_note' and the build will accept it.")
            levels = [p.get("level") for p in prac if isinstance(p.get("level"), int)]
            if len(levels) != len(prac):
                E(rid, "every practice problem needs an integer 'level' from 1 to 10")
            elif levels != sorted(levels):
                E(rid, "practice problems must be stored in rising order of level")
            elif prac:
                bands = {BAND_OF(l) for l in levels}
                if not {"mechanical", "transfer"} <= bands:
                    missing = sorted({"mechanical", "transfer"} - bands)
                    E(rid, f"practice ladder never reaches: {', '.join(missing)}. A drill set that "
                           "is all mechanical does not test understanding, and one that is all "
                           "transfer does not build fluency.")
                elif len(bands) < 3:
                    W(rid, f"practice covers only {len(bands)} of the four difficulty bands; the "
                           "middle of the ladder is where most readers actually fall off")
        elif prac:
            W(rid, f"{len(prac)} practice problems on a concept not marked quantitative - either "
                   "set 'quantitative: true' or move these to exercises")
        qblock, qwarn = check_quotes(r)
        for m in qblock:
            E(rid, m)
        for m in qwarn:
            W(rid, m)

        for where, line, vals in check_arithmetic(r):
            E(rid, f"arithmetic does not hold in {where}: \"{line[:66]}\" evaluates to "
                   f"{' and '.join(f'{v:g}' for v in vals)}")

        # A boundary point that describes the section instead of the technique. Four shipped
        # in Part A: "This section gets you the arithmetic of a percentage" is a contents entry
        # sitting in the one part of the record meant to outlive the section. Narrow on purpose -
        # it catches the section-scope shape and leaves every real limit alone.
        for q in (r.get("must_know") or []):
            if not isinstance(q, dict) or q.get("kind") != "boundary":
                continue
            first = " ".join((q.get("point") or "").split())
            # One sentence only. A point that opens on scope and then names a real limit and
            # what to do about it is doing its job - C39 and C42 both do - and flagging those
            # would teach the author to ignore the warning. Pure scope is a single sentence.
            sentences = [x for x in re.split(r"(?<=[.!?]) +", first) if x.strip()]
            if len(sentences) == 1 and re.match(r"^This (section |)(gets|gives|takes) you\b", first):
                W(rid, f"boundary point describes the section, not a limit of the technique: "
                       f"\"{first[:60]}...\" - say when the tool stops being trustworthy, or cut it "
                       "(the style sheet 5)")

        # Columns set with spaces inside a working block cannot line up: the Working style
        # is proportional, so the whole point of the alignment is lost between the record
        # and the page. Before this check the book contained one real table and about
        # sixteen that had been written as aligned text and arrived as ragged prose.
        # A fence toggles. Reading a closing fence as if it opened a block - which is what
        # a naive `inside = tag != "table"` does - makes the prose after a table look like
        # a block of its own, and it reported the table it had just correctly skipped.
        raw, inside, tag, body = r.get("_raw") or "", False, "", []
        for ln in raw.split("\n"):
            m = re.match(r"^\s*```+\s*(\S*)\s*$", ln)
            if m:
                if inside and tag != "table" and _looks_tabular(body):
                    W(rid, "a working block has columns in it - tag it ```table so it "
                           "renders as a table, or the columns arrive as ragged text")
                inside, tag, body = not inside, ("" if inside else m.group(1)), []
                continue
            if inside:
                body.append(ln)

        # A figure whose file is absent renders as a broken-image placeholder in Word and
        # as nothing at all in print, and neither failure is visible from the record.
        for f in (r.get("figures") or []):
            if not isinstance(f, dict):
                continue
            if not os.path.exists(os.path.join(FIGURES_DIR, f.get("file", ""))):
                E(rid, f"figure '{f.get('file')}' is not in check/figures/ - run "
                       "check/figures/draw.py, or remove the entry")
            elif not os.path.exists(os.path.join(FIGURES_DIR, f.get("source", ""))):
                W(rid, f"figure '{f.get('file')}' names source script '{f.get('source')}', "
                       "which is not in check/figures/ - the picture cannot be redrawn")
        for p in prac:
            if not (p.get("answer") or "").strip():
                E(rid, f"practice {p.get('level')} has no worked answer")
            for ck in p.get("refs") or []:
                if bibkeys and ck not in bibkeys:
                    E(rid, f"practice {p.get('level')} cites '{ck}', which is not in library.bib")

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

    warn += check_doc_paths()

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

# Reader-facing prose is authored in plain words, and two things it cannot express are
# supplied here rather than pushed onto the author. Section 11 makes plain language the
# core obligation of the book, so every piece of notation an author has to remember is a
# tax on the one rule that matters most.
#
#   1. Display working. A calculation set out line by line used to be indented four
#      spaces, which markdown reads as a code block and Word then typesets as computer
#      source. Arithmetic is not source code. Authors fence it as ```working and it
#      renders in a Working paragraph style. Legacy indents are still converted, and
#      warned about, so nothing silently regresses to monospace.
#   2. Notation. Authors write 10^7 and log10; they are typeset here as real
#      superscripts and subscripts. The book can therefore show standard notation
#      without anyone having to write LaTeX inside a YAML field.

WORKING_OPEN = '::: {custom-style="Working"}'

_SUP = re.compile(r"(?<![\w^~])(\d[\d,.]*)\s*\^\s*"
                  r"(\(\s*-?\d+\s*/\s*\d+\s*\)|-?\d+(?:\.\d+)?)(?!\^)")
_LOGB = re.compile(r"\blog\s?(10|2|e)\b")
_FENCE = re.compile(r"^\s*```+\s*(working|calc|table)?\s*$")


def _notation(text: str) -> str:
    """10^7 and 9^(1/2) -> superscript, log10 -> subscript.

    Every caret and tilde this does not itself use is escaped afterwards, and that is not
    housekeeping. Pandoc marks a superscript by pairing two carets, so a line reading
    `9^(1/2)   144^(1/2)` has its two stray carets paired across the gap between them and
    sets `(1/2)   144` as a superscript on the 9. The fix cannot be a tidier regex: any
    unpaired caret left in the text is a live pairing hazard for the next one anywhere in
    the same paragraph. So the substitutions are parked behind placeholders, everything
    still carrying a caret or tilde is escaped, and the placeholders are restored.
    """
    subs = []

    def park(fmt):
        def go(m):
            subs.append(fmt.format(*m.groups()))
            return f"\x00{len(subs) - 1}\x01"
        return go

    text = _SUP.sub(park("{0}^{1}^"), text)
    text = _LOGB.sub(park("log~{0}~"), text)
    text = text.replace("^", r"\^").replace("~", r"\~")
    return re.sub(r"\x00(\d+)\x01", lambda m: subs[int(m.group(1))], text)


def _looks_tabular(body: list[str]):
    """Rows of a genuine table, or None.

    Columns in these records are separated by runs of spaces, which a proportional font
    cannot preserve - so anything with real columns has to become a real table or it
    arrives as ragged prose. The thing that must not be swept up is a list of equations:
    `one lakh = 1 times 10^5` splits into two columns on whitespace and is not a table,
    it is a calculation, and it belongs in a working block. An `=` anywhere in a row is
    the signal, and it is deliberately blunt - a table wrongly left as working still
    reads; an equation forced into a grid does not.
    """
    live = [l for l in body if l.strip()]
    # Columns are found by whitespace, which cannot express an empty leading cell - a
    # header sitting over the third and fourth columns comes out in the first and second.
    # Where that matters the author writes the row with pipes and says exactly what they
    # mean; one pipe row makes the whole block explicit.
    if live and all("|" in l for l in live):
        return [[c.strip() for c in l.strip().strip("|").split("|")] for l in live]
    rows = [re.split(r" {2,}", l.strip()) for l in live]
    if len(rows) < 2 or any("=" in l for l in body):
        return None
    multi = [r for r in rows if len(r) >= 2]
    # Most rows must actually have columns. A block of running text with one
    # incidentally-spaced line in it is prose, and forcing it into a grid destroys it.
    if len(multi) < 2 or len(multi) < 0.75 * len(rows):
        return None
    return rows


def _grid_table(rows: list[list[str]]) -> list[str]:
    """A pandoc grid table. Headerless unless the first row reads like labels.

    Grid tables are used rather than pipe tables because most of these have no header -
    a place-value breakdown is two columns of data - and a pipe table cannot express
    that without an empty header row, which prints as a blank banded strip.
    """
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    # A first row carrying no digits, above rows that do, is a header.
    head = (len(rows) > 2
            and not any(ch.isdigit() for ch in " ".join(rows[0]))
            and any(ch.isdigit() for ch in " ".join(rows[1])))
    w = [max(4, max(len(r[c]) for r in rows) + 2) for c in range(n)]
    rule = lambda ch: "+" + "+".join(ch * x for x in w) + "+"
    out = [rule("-")]
    for i, r in enumerate(rows):
        out.append("|" + "|".join(" " + c.ljust(x - 1) for c, x in zip(r, w)) + "|")
        out.append(rule("=") if (head and i == 0) else rule("-"))
    return ["", *out, ""]


def _working_div(body: list[str]) -> list[str]:
    body = [b for b in (x.strip() for x in body) if b]
    if not body:
        # A run of spaces is how these blocks set two quantities side by side for
        # comparison. Markdown collapses them, so they become non-breaking spaces and the
        # columns survive without needing a table for two numbers.
        return []
    body = [re.sub(r" {3,}", "\\\\ " * 4, b) for b in body]
    return ["", WORKING_OPEN, *[b + "\\" for b in body[:-1]], body[-1], ":::", ""]


def _working(text: str, flag=None) -> str:
    """Fenced blocks and legacy four-space indents become display arithmetic.

    An untagged fence counts. The corpus contains no code, so a fenced block is always a
    calculation, and treating an untagged one as code is what put 186 paragraphs of
    arithmetic into a monospace face. Authors should tag them ```working; untagged ones
    are converted and flagged so the habit is visible rather than silently absorbed.
    """
    lines, out, i = text.split("\n"), [], 0
    while i < len(lines):
        m = _FENCE.match(lines[i])
        if m:
            if not m.group(1) and flag:
                flag("fence")
            tag, (i, body) = m.group(1), (i + 1, [])
            while i < len(lines) and not _FENCE.match(lines[i]):
                body.append(lines[i])
                i += 1
            if tag == "table":
                rows = _looks_tabular(body)
                out += _grid_table(rows) if rows else _working_div(body)
                i += 1
                continue
            if _looks_tabular(body) and flag:
                flag("table")
            out += _working_div(body)
            i += 1
            continue
        if lines[i].startswith("    ") and lines[i].strip():
            body = []
            while i < len(lines) and lines[i].startswith("    ") and lines[i].strip():
                body.append(lines[i])
                i += 1
            if flag:
                flag("indent")
            out += _working_div(body)
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def _prose(text, flag=None) -> str:
    """Every reader-facing prose field passes through here on its way to the page.

    Notation runs first and the order is load-bearing. A grid table is parsed by column
    position, so turning `10^1` into a superscript *after* the grid was drawn added a
    character to a cell and shifted every boundary to its right, and pandoc then read the
    wreckage as merged cells. Widths have to be computed on the final text.
    """
    return _working(_notation(str(text or "")), flag)


def _block(prefix, text, trail="", flag=None) -> list[str]:
    """A labelled passage that may contain display arithmetic.

    Prose fields can expand into block-level markdown, so a label cannot simply be
    concatenated in front of one: `"**Definition.** " + prose` puts the opening fence of a
    working block in the middle of a paragraph, where it stops being a fence and the
    arithmetic silently falls back to a code block. The label goes on the first line of
    prose and any citation mark on the last, and the blocks in between are left alone.
    """
    lines = _prose(text, flag).split("\n")
    first = next((i for i, l in enumerate(lines) if l.strip()), None)
    if first is None:
        return [prefix.strip(), ""] if prefix.strip() else []
    if lines[first].startswith(":::"):
        lines = [prefix.rstrip(), ""] + lines[first:]
    else:
        lines[first] = prefix + lines[first]
    if trail:
        last = max(i for i, l in enumerate(lines) if l.strip())
        lines[last] = lines[last] + trail if not lines[last].startswith(":::") else lines[last]
        if lines[last].startswith(":::"):
            lines += ["", trail.strip()]
    return lines + [""]


_NUMBERS = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen", "twenty"]


def _count_word(n: int) -> str:
    return _NUMBERS[n] if 0 <= n < len(_NUMBERS) else str(n)


# References are numbered in the text and listed at the end of the Part they appear in.
# Numbering is per (source, clause) pair rather than per source, so a number always names
# exactly what was consulted and the reader never carries a locator through the prose.
# Reader-facing text therefore contains no repository paths: the bibliography carries a
# resolvable URL, which is what someone who does not have this repository can actually use.

def _bib_entries() -> dict:
    """Parse library.bib into {citekey: {field: value}}, brace-aware."""
    if not os.path.exists(BIB):
        return {}
    with open(BIB, encoding="utf-8") as fh:
        src = fh.read()
    out = {}
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", src):
        depth, j = 1, src.index("{", m.start()) + 1
        while j < len(src) and depth:
            depth += (src[j] == "{") - (src[j] == "}")
            j += 1
        body, fields = src[m.end():j - 1], {}
        for fm in re.finditer(r"(\w+)\s*=\s*", body):
            p = fm.end()
            if p < len(body) and body[p] in "{\"":
                close, d, q = body[p], 1, p + 1
                while q < len(body) and d:
                    if close == "{":
                        d += (body[q] == "{") - (body[q] == "}")
                    else:
                        d -= body[q] == '"'
                    q += 1
                val = body[p + 1:q - 1]
            else:
                q = p
                while q < len(body) and body[q] not in ",\n":
                    q += 1
                val = body[p:q]
            fields[fm.group(1).lower()] = " ".join(val.replace("{", "").replace("}", "").split())
        out[m.group(2)] = fields
    return out


class Cites:
    """Numbered references, restarting at each Part, listed where that Part ends."""

    def __init__(self, entries):
        self.entries, self.order, self.num, self.unverified = entries, [], {}, set()

    def mark(self, r) -> str:
        marks = []
        for ref in (r.get("definition", {}) or {}).get("references", []) or []:
            key, loc = ref.get("citekey"), (ref.get("locator") or "").strip()
            if not key:
                continue
            # A source that has not been obtained gets one entry however many clauses cite
            # it. Numbering per clause is precision the reader can act on only when the
            # source is reachable; on a placeholder it produces eight identical entries.
            if not (self.entries.get(key) or {}).get("url"):
                loc = ""
            ident = (key, loc)
            if ident not in self.num:
                self.order.append(ident)
                self.num[ident] = len(self.order)
            if not (ref.get("verified") or {}).get("claim_located"):
                self.unverified.add(ident)
            marks.append(str(self.num[ident]))
        return f"[{', '.join(marks)}]" if marks else ""

    def _format(self, ident) -> str:
        key, loc = ident
        e = self.entries.get(key)
        if not e:
            return f"`{key}` — no entry in the reference library."
        bits = [e.get("author", "").rstrip("."), e.get("title", "").rstrip(".")]
        # A bib `note` is where the build keeps its own working commentary, and several of
        # them run to a paragraph of internal reasoning about why a source is still
        # missing. That belongs in the retrieval report, not under the reader's eye, so
        # only a note short enough to be a genuine citation detail is printed.
        note = (e.get("note") or "").strip()
        if note and len(note) <= 120:
            bits.append(note.rstrip("."))
        elif e.get("year") and e["year"].lower() not in ("n.d.", "nd", "none"):
            bits.append(e["year"])
        if loc:
            bits.append(loc)
        if e.get("howpublished"):
            bits.append(e["howpublished"])
        out = ". ".join(b.strip().rstrip(".").strip() for b in bits if b and b.strip()) + "."
        if e.get("url"):
            out += f" <{e['url']}>"
            if e.get("urldate"):
                out += f" (accessed {e['urldate']})"
            out += "."
        if ident in self.unverified:
            out += " *Outstanding — see the note below.*"
        return out

    UNVERIFIED_NOTE = (
        "*An entry marked outstanding has not yet been checked against the source itself. "
        "Nothing in these sections rests on one: the reasoning is a derivation you can "
        "check with a calculator, and the entry records an anchor still to be supplied.*")

    def flush(self, heading) -> list[str]:
        """Emit and reset. Called at each Part boundary and once at the end."""
        if not self.order:
            return []
        md, any_open = [f"### {heading}", ""], bool(self.unverified)
        for ident in self.order:
            md += [f"{self.num[ident]}. {self._format(ident)}", ""]
        if any_open:
            md += [self.UNVERIFIED_NOTE, ""]
        self.order, self.num, self.unverified = [], {}, set()
        return md


def _illustrations(r) -> list:
    """One illustration or several. A concept carries as many as earn their place."""
    many = r.get("illustrations")
    if isinstance(many, list) and many:
        return [i for i in many if isinstance(i, dict) and (i.get("body") or "").strip()]
    one = r.get("illustration")
    return [one] if isinstance(one, dict) and (one.get("body") or "").strip() else []


def _figures(r, sid) -> list[str]:
    """Figures live beside the records and are referenced by file name."""
    md = []
    for f in (r.get("figures") or []):
        if not isinstance(f, dict) or not f.get("file"):
            continue
        path = os.path.join("figures", f["file"]).replace("\\", "/")
        # Pandoc turns an image's bracket text into the figure's caption, so the caption
        # goes there and nothing else does. Putting the alt text in the brackets and the
        # caption on a line below printed both, one above the other, under every figure.
        # `alt` stays in the record: it is the accessible description, not a second caption.
        cap = " ".join((f.get("caption") or "").split())
        md += [f"![{cap}]({path}){{width=6in}}", ""]
    return md


def concept_md(r, cites, label=None, sid=None) -> list[str]:
    flagged = []
    p = lambda t: _prose(t, flagged.append)
    md = [f"### {label + ' · ' if label else ''}{r['name']}", ""]
    # The concept id and type are build metadata and are not shown: the heading already
    # names the section. Currency is shown, because a reader of statutory material needs
    # to know how old it is.
    asof = (r.get("review") or {}).get("as_of")
    if asof and r.get("concept_type") != "derivable":
        md += [f"*Checked against the sources as they stood on {asof}.*", ""]
    mark = cites.mark(r)
    flg = flagged.append
    md += _block("**Definition.** ", r["definition"]["text"], f" {mark}" if mark else "", flg)
    md += _block("**In plain terms.** ", r["simplified_explanation"], flag=flg)
    md += _figures(r, sid)
    ills = _illustrations(r)
    for n, ill in enumerate(ills, 1):
        head = "**Illustration.** " if len(ills) == 1 else f"**Illustration {n}.** "
        md += _block(head, ill["body"], flag=flg)
        if (ill.get("analogy_breaks_when") or "").strip():
            md += _block("**Where this picture breaks.** ", ill["analogy_breaks_when"], flag=flg)
    mk = r.get("must_know") if isinstance(r.get("must_know"), list) else []
    rows = [f"- {p(' '.join((q.get('point') or '').split()))}" for q in mk
            if isinstance(q, dict) and (q.get("point") or "").strip()]
    if rows:
        md += ["**Must know points for you.**", ""] + rows + [""]
    if flagged:
        LEGACY_INDENT.add(r["concept_id"])
    return md


LEGACY_INDENT = set()


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
    # Exercises and practice problems are numbered within their own section rather than
    # tagged with the record id. The id was build plumbing leaking onto the page; the
    # appendix groups answers under the section heading, which keeps them unambiguous
    # without making the reader parse an identifier to find question three.
    cites, answers, seen_part = Cites(_bib_entries()), [], None
    for rung in sorted({r.get("rung", 0) for r in mine}):
        band = [r for r in mine if r.get("rung", 0) == rung]
        if sid != "B0":
            md += [f"## Rung {rung} — {LEVELS[rung-1]}", ""]
        for r in band:
            label = None
            if sid == "B0":
                part, sec = where.get(r.get("sequence"), (None, None))
                if part and part["letter"] != seen_part:
                    if seen_part:
                        md += cites.flush(f"References · Part {seen_part}")
                    seen_part = part["letter"]
                    md += [f"## Part {part['letter']} · {part['title']}", ""]
                label = sec["id"] if sec else None
            md += concept_md(r, cites, label, sid)
            here = f"{label + ' · ' if label else ''}{r['name']}"
            block = []
            for i, ex in enumerate(r.get("exercises") or [], 1):
                md += _block(f"**Exercise {i}** ({ex['type']}). ", ex["prompt"])
                if ex.get("confidence_first"):
                    md += ["*Record your confidence as a percentage before turning to the answer.*", ""]
                block += _block(f"**Exercise {i}.** ", ex["answer"])
            prac = sorted([q for q in (r.get("practice") or []) if isinstance(q, dict)],
                          key=lambda q: q.get("level", 0))
            if prac:
                md += [f"**Practice.** {_count_word(len(prac)).capitalize()} problems on this "
                       "technique, easiest first. Work them on paper before turning to the "
                       "answers, which are in the appendix at the back under this section's name.", ""]
                for i, q in enumerate(prac, 1):
                    md += _block(f"**{i}.** ", q["prompt"])
                    block += _block(f"**{i}.** ", q["answer"])
            if block:
                answers += [f"### {here}", ""] + block
    if seen_part:
        md += cites.flush(f"References · Part {seen_part}")
    elif sid != "B0":
        md += cites.flush("References")
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
                     f"{READING_GRADE_MAX_DEF:.0f} (the style sheet §11).\n\n"
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
        drills = [(r["concept_id"], len([p for p in (r.get("practice") or []) if isinstance(p, dict)]))
                  for r in ordered]
        drills = [(cid, n) for cid, n in drills if n]
        if drills:
            fh.write("## Practice sets\n\n"
                     f"Problems per quantitative concept. The range is {PRACTICE_MIN} to "
                     f"{PRACTICE_MAX} (the style sheet §7a), judged by how many moves the technique has, "
                     "with the bands each drill set reaches shown so that a set which never leaves "
                     "the mechanical end is visible here rather than only on a careful read.\n\n"
                     "| Concept | Problems | Bands reached |\n| --- | --- | --- |\n")
            byid = {r["concept_id"]: r for r in ordered}
            for cid, n in drills:
                lv = [p.get("level") for p in (byid[cid].get("practice") or [])
                      if isinstance(p, dict) and isinstance(p.get("level"), int)]
                seen = [b for _, _, b in PRACTICE_BANDS if b in {BAND_OF(x) for x in lv}]
                fh.write(f"| {cid} | {n} | {', '.join(seen) or '—'} |\n")
            fh.write(f"\n**{sum(n for _, n in drills)} practice problems across "
                     f"{len(drills)} concepts.**\n\n")
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
    # Citations are numbered and listed per Part during assembly, so citeproc is not used.
    # A reference document carries the styles: Working for display arithmetic, a table
    # style that renders as a table, and spacing that does not leave gaps between every
    # paragraph. Without it pandoc's default template typesets arithmetic as source code.
    args_common = []
    figs = os.path.join(ROOT, "figures")
    if os.path.isdir(figs):
        shutil.copytree(figs, os.path.join(OUT, "figures"), dirs_exist_ok=True)
    for fmt, ext in formats:
        target = os.path.join(OUT, f"{stem}.{ext}")
        if quarto:
            cmd = _launch(quarto) + ["render", os.path.basename(md_path),
                                     "--to", fmt, "--output", f"{stem}.{ext}"]
            cwd = OUT
        else:
            engine = ["--pdf-engine=tectonic"] if fmt == "pdf" and shutil.which("tectonic") else []
            ref = [f"--reference-doc={os.path.abspath(REFDOC)}"] \
                if fmt == "docx" and os.path.exists(REFDOC) else []
            cmd = _launch(pandoc or "pandoc") + [md_path, "-o", target, "--from",
                   "markdown-yaml_metadata_block", "--toc", "--toc-depth=3",
                   f"--resource-path={OUT}"] + args_common + ref + engine
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
        # Headings are labels, not teaching. Section 10 asks that a term be introduced where
        # the reader first meets it in prose, and a heading naming the topic arrives before
        # that by construction - "B1 · What a unit is, and the SI base units" reported SI as
        # unexpanded even though the first sentence underneath expands it properly.
        # Scan teaching prose only. Headings are labels that arrive before the sentence which
        # introduces the term, and a reference list is bibliographic data where an acronym sits
        # beside the full name it abbreviates. Both reported terms that the prose does explain.
        body, in_refs = [], False
        for l in md.split("\n"):
            if l.startswith("### References ·"):
                in_refs = True
            elif l.startswith("#"):
                in_refs = False
            if not in_refs and not l.lstrip().startswith("#"):
                body.append(l)
        stumbles = [s for s in acronym_defects("\n".join(body))
                    if not re.fullmatch(r"[IVXLC]+", s)]   # Schedule II is a numeral
        if stumbles:
            print(f"  [{sid}] used before anything expands them: {', '.join(stumbles)}")
        print(f"{sid}: {len(ids)} concepts ->", ", ".join(render(path, sid)) or "markdown only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
