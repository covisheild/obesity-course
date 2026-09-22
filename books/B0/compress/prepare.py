"""Set a Part up for the compression pass, and assemble the cut sections afterwards.

    python books/B0/compress/prepare.py extract C15 C16 C17 ...
    python books/B0/compress/prepare.py assemble C1 C2 C3 ...
    python books/B0/compress/prepare.py release A B          # earlier Parts, uncut

`extract` writes, for each record:

  <label>-prose.yml     the prose fields alone, which is all a cutter may touch
  <label>-original.md   the whole section as a reader meets it, for the record

`assemble` builds `<label>-pass1.md` from the cutter's `<label>-pass1-prose.yml` **plus the
exercises and practice prompts read straight out of the record**. The test set is then
identical to the original's by construction rather than by instruction, which is the whole
reason the assembly is a script and not a copy-paste. Practice *answers* are left out: the
cold reader is supposed to work the problems.

`release` writes `<label>-released.md` for every section of an earlier Part, uncut. Those go
into the scratch directory beside the cut sections, because a reader who has reached Part C
has read Parts A and B, and withholding them turns every legitimate backward dependency into
a reported hole. That mistake cost roughly half of Part B's gap report.

The first two commands existed as hand-typed steps through Parts A and B. Writing them down
is not tidiness: the hand-assembled version is how a cut section can end up with an edited
exercise, which invalidates step 2 silently.
"""
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.normpath(os.path.join(HERE, "..", "..", "..", "check"))
sys.path.insert(0, CHECK)
import build  # noqa: E402

RECORDS = os.path.join(CHECK, "records", "B0")

HEADS = {"definition.text": "**Definition.**",
         "simplified_explanation": "**In plain terms.**",
         "illustration.body": "**Illustration.**",
         "illustration.analogy_breaks_when": "**Where this picture breaks.**"}


def labels():
    """{record sequence: outline label}, e.g. 15 -> C1. The outline is the one source."""
    out = {}
    for part in build.load_book0_outline():
        for s in part["sections"]:
            out[s["index"]] = s["id"]
    return out


def load(cid):
    with open(os.path.join(RECORDS, f"{cid}.yml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def prose_only(r):
    """The fields a cutter may touch, keyed as validate.py expects."""
    out = {}
    for k in ("definition.text", "simplified_explanation",
              "illustration.body", "illustration.analogy_breaks_when"):
        a, _, b = k.partition(".")
        v = (r.get(a) or {}).get(b) if b else r.get(a)
        if isinstance(v, str) and v.strip():
            out[k] = v
    for i, p in enumerate(r.get("must_know") or []):
        if isinstance(p, dict) and isinstance(p.get("point"), str):
            out[f"must_know[{i}].point"] = p["point"]
    return out


def _dump(path, mapping):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        yaml.safe_dump(mapping, fh, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, width=10 ** 6)


def _tail(r, label, prose):
    """Everything after the prose: must-knows, exercises, practice prompts.

    Read out of the record every time. Nothing here is ever the cutter's copy.
    """
    md = []
    points = [v for k, v in prose.items() if k.startswith("must_know")]
    if points:
        md += ["**Must know points for you.**", ""]
        md += [f"- {' '.join(p.split())}" for p in points] + [""]
    for i, ex in enumerate(r.get("exercises") or [], 1):
        kind = f" ({ex.get('type')})" if ex.get("type") else ""
        md += [f"**Exercise {i}**{kind}. {ex.get('prompt', '').strip()}", ""]
    prac = sorted((p for p in (r.get("practice") or []) if isinstance(p, dict)),
                  key=lambda q: q.get("level", 0))
    for i, q in enumerate(prac, 1):
        md += [f"**{i}.** {q.get('prompt', '').strip()}", ""]
    return md


def section_md(r, label, prose):
    md = [f"# {label} · {r['name']}", ""]
    for k, head in HEADS.items():
        if k in prose:
            md += [f"{head} {prose[k].strip()}", ""]
    # Figures go in as caption plus alt text. The first Part C pass left them out, and the cold
    # reader reported - correctly, for what it had been given - that four sections argue from
    # drawings that do not exist. Half of C5's gap list was that one omission. A reader who has
    # reached this page has seen the picture, so the test has to show them something for it.
    for f in (r.get("figures") or []):
        cap = " ".join((f.get("caption") or "").split())
        alt = " ".join((f.get("alt") or "").split())
        md += [f"**Figure.** {cap}", "", f"*What the figure shows:* {alt}", ""]
    return "\n".join(md + _tail(r, label, prose)) + "\n"


def extract(cids):
    lab = labels()
    for cid in cids:
        r = load(cid)
        label = lab.get(r["sequence"], cid)
        prose = prose_only(r)
        _dump(os.path.join(HERE, f"{label}-prose.yml"), prose)
        with open(os.path.join(HERE, f"{label}-original.md"), "w",
                  encoding="utf-8", newline="") as fh:
            fh.write(section_md(r, label, prose))
        words = sum(len(v.split()) for v in prose.values())
        print(f"  {cid} -> {label}: {len(prose)} prose fields, {words} words")


def assemble(cids):
    lab = labels()
    by_label = {}
    for cid in cids:
        r = load(cid)
        by_label[lab.get(r["sequence"], cid)] = r
    for label, r in by_label.items():
        cut_path = os.path.join(HERE, f"{label}-pass1-prose.yml")
        if not os.path.exists(cut_path):
            print(f"  {label}: no {os.path.basename(cut_path)} - skipped")
            continue
        with open(cut_path, encoding="utf-8") as fh:
            cut = yaml.safe_load(fh)
        out = os.path.join(HERE, f"{label}-pass1.md")
        with open(out, "w", encoding="utf-8", newline="") as fh:
            fh.write(section_md(r, label, cut))
        print(f"  {label}: {os.path.basename(out)}")


def release(letters):
    """Uncut text for a whole Part, for the cold reader's scratch directory."""
    lab = labels()
    want = {s["index"]: s["id"] for p in build.load_book0_outline() if p["letter"] in letters
            for s in p["sections"]}
    made = 0
    for fn in sorted(os.listdir(RECORDS)):
        if not fn.endswith(".yml"):
            continue
        r = load(fn[:-4])
        label = want.get(r.get("sequence"))
        if not label:
            continue
        prose = prose_only(r)
        with open(os.path.join(HERE, f"{label}-released.md"), "w",
                  encoding="utf-8", newline="") as fh:
            fh.write(section_md(r, label, prose))
        made += 1
    print(f"  {made} released sections for Part(s) {', '.join(letters)}")


def _replace_block(raw, key, body, occurrence=0):
    """Swap one block scalar's body in the raw file text, touching nothing else.

    Raw surgery rather than load-edit-dump, and that is not fussiness. Rebuilding a record
    through yaml.safe_dump is how an earlier compression run silently destroyed every
    must-know `kind` and `bearing`, and it is also how a long line ends up wrapped across
    two physical lines and stops being valid YAML. Replacing the body of a named block and
    leaving every other byte alone cannot do either.
    """
    lines = raw.splitlines(keepends=True)
    pat = re.compile(rf"^(\s*)(?:- )?{re.escape(key)}:\s*\|-?\s*$")
    seen = -1
    for i, line in enumerate(lines):
        m = pat.match(line)
        if not m:
            continue
        seen += 1
        if seen != occurrence:
            continue
        indent = len(m.group(1)) + (2 if line.lstrip().startswith("- ") else 0) + 2
        j = i + 1
        while j < len(lines) and (not lines[j].strip() or
                                  len(lines[j]) - len(lines[j].lstrip()) >= indent):
            j += 1
        new = "".join(" " * indent + l + "\n" if l.strip() else "\n"
                      for l in body.rstrip("\n").split("\n"))
        return "".join(lines[:i + 1]) + new + "".join(lines[j:]), True
    return raw, False


def writeback(cids):
    """Put each section's final prose back into its record. Prose fields only."""
    lab = labels()
    for cid in cids:
        r = load(cid)
        label = lab.get(r["sequence"], cid)
        path = os.path.join(HERE, f"{label}-final-prose.yml")
        if not os.path.exists(path):
            print(f"  {label}: no final prose - skipped")
            continue
        with open(path, encoding="utf-8") as fh:
            final = yaml.safe_load(fh)
        target = os.path.join(RECORDS, f"{cid}.yml")
        with open(target, encoding="utf-8", newline="") as fh:
            raw = fh.read()
        done, missed = 0, []
        mk = 0
        for k, body in final.items():
            if k.startswith("must_know"):
                idx = int(re.search(r"\[(\d+)\]", k).group(1))
                raw, ok = _replace_block(raw, "point", body, idx)
            else:
                raw, ok = _replace_block(raw, k.split(".")[-1], body)
            done += ok
            if not ok:
                missed.append(k)
        yaml.safe_load(raw)          # refuse to write anything that is not valid YAML
        with open(target, "w", encoding="utf-8", newline="") as fh:
            fh.write(raw)
        print(f"  {label} -> {cid}: {done} prose fields replaced"
              + (f"; MISSED {missed}" if missed else ""))


if __name__ == "__main__":
    cmd, rest = sys.argv[1], sys.argv[2:]
    {"extract": extract, "assemble": assemble, "release": release,
     "writeback": writeback}[cmd](rest)
