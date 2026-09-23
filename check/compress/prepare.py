"""Set a book up for the compression pass, and assemble the cut sections afterwards.

    python check/compress/prepare.py --subject B0 extract B0-R0-C15 B0-R0-C16 ...
    python check/compress/prepare.py --subject B0 assemble B0-R0-C15 ...
    python check/compress/prepare.py --subject B0 release A B      # earlier Parts, uncut
    python check/compress/prepare.py --subject B0 writeback B0-R0-C15 ...

    python check/compress/prepare.py --subject S01-R1 extract       # no ids: the whole rung
    python check/compress/prepare.py --subject S01-R1 release       # Book 0 deps + earlier rungs

`--subject` picks the book (see `_book.py`): Book 0, or one rung of a subject. The working
folder is `books/<ID>/compress/`. Book 0's sections are labelled from its outline (C7); a rung
book's sections by their own concept_id (S01-R1-C03), which is also the file stem.

`extract` writes, for each record:

  <label>-prose.yml     the prose fields alone, which is all a cutter may touch
  <label>-original.md   the whole section as a reader meets it, for the record

`assemble` builds `<label>-pass1.md` from the cutter's `<label>-pass1-prose.yml` **plus the
exercises and practice prompts read straight out of the record**. The test set is then
identical to the original's by construction rather than by instruction, which is the whole
reason the assembly is a script and not a copy-paste. Practice *answers* are left out: the
cold reader is supposed to work the problems.

`release` writes `<label>-released.md` for every section the cold reader has already read,
uncut. Those go into the scratch directory beside the cut sections, because a reader who has
reached Part C has read Parts A and B, and withholding them turns every legitimate backward
dependency into a reported hole. That mistake cost roughly half of Part B's gap report.
For Book 0 that is the Parts named. For a rung book it is every Book 0 section the rung's
records list in `ground_floor_deps` (PIPELINE.md Task 5), every section of the subject's
earlier rungs, and any whole Book 0 Parts named as well.

The first two commands existed as hand-typed steps through Parts A and B. Writing them down
is not tidiness: the hand-assembled version is how a cut section can end up with an edited
exercise, which invalidates step 2 silently.
"""
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _book import Book, take_opts  # noqa: E402

BOOK = None     # set in main()

HEADS = {"definition.text": "**Definition.**",
         "simplified_explanation": "**In plain terms.**",
         "illustration.body": "**Illustration.**",
         "illustration.analogy_breaks_when": "**Where this picture breaks.**"}


def load(cid):
    return BOOK.load(cid)


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


def _ids(cids):
    """The ids named, or every record of the book when none are."""
    return list(cids) or [cid for cid, _ in BOOK.mine()]


def extract(cids):
    os.makedirs(BOOK.work, exist_ok=True)
    for cid in _ids(cids):
        r = load(cid)
        label = BOOK.label(cid, r)
        prose = prose_only(r)
        _dump(BOOK.f(f"{label}-prose.yml"), prose)
        with open(BOOK.f(f"{label}-original.md"), "w",
                  encoding="utf-8", newline="") as fh:
            fh.write(section_md(r, label, prose))
        words = sum(len(v.split()) for v in prose.values())
        print(f"  {cid} -> {label}: {len(prose)} prose fields, {words} words")


def assemble(cids):
    by_label = {}
    for cid in _ids(cids):
        r = load(cid)
        by_label[BOOK.label(cid, r)] = r
    for label, r in by_label.items():
        cut_path = BOOK.f(f"{label}-pass1-prose.yml")
        if not os.path.exists(cut_path):
            print(f"  {label}: no {os.path.basename(cut_path)} - skipped")
            continue
        with open(cut_path, encoding="utf-8") as fh:
            cut = yaml.safe_load(fh)
        out = BOOK.f(f"{label}-pass1.md")
        with open(out, "w", encoding="utf-8", newline="") as fh:
            fh.write(section_md(r, label, cut))
        print(f"  {label}: {os.path.basename(out)}")


def _write_released(label, r):
    prose = prose_only(r)
    with open(BOOK.f(f"{label}-released.md"), "w", encoding="utf-8", newline="") as fh:
        fh.write(section_md(r, label, prose))


def release(letters):
    """Uncut text of everything the cold reader has already read, for the scratch directory.

    Book 0: whole Parts, by letter. A rung book: the Book 0 sections its records list in
    `ground_floor_deps`, every section of the subject's earlier rungs, and any Book 0 Parts
    named. Book 0 text is always read from check/records/B0 and labelled from its outline.
    """
    os.makedirs(BOOK.work, exist_ok=True)
    outline = BOOK.outline()
    b0_label = {s["index"]: s["id"] for p in outline for s in p["sections"]}
    want = {s["index"]: s["id"] for p in outline if p["letter"] in letters
            for s in p["sections"]}
    deps, earlier = set(), []
    if not BOOK.is_b0:
        mine = BOOK.mine()
        deps = {d for _, r in mine for d in (r.get("ground_floor_deps") or [])}
        rung = int(BOOK.id.split("-R")[1])
        for fn in sorted(os.listdir(BOOK.records_dir)) if os.path.isdir(BOOK.records_dir) else []:
            if not fn.endswith((".yml", ".yaml")):
                continue
            with open(os.path.join(BOOK.records_dir, fn), encoding="utf-8") as fh:
                r = yaml.safe_load(fh) or {}
            if r.get("subject") == BOOK.subject and 0 < (r.get("rung") or 0) < rung:
                earlier.append(r)
    made, found = 0, set()
    b0 = BOOK.b0_records_dir
    for fn in sorted(os.listdir(b0)):
        if not fn.endswith(".yml"):
            continue
        with open(os.path.join(b0, fn), encoding="utf-8") as fh:
            r = yaml.safe_load(fh)
        label = want.get(r.get("sequence"))
        if not label and r.get("concept_id") in deps:
            label = b0_label.get(r.get("sequence"), r.get("concept_id"))
        if not label:
            continue
        found.add(r.get("concept_id"))
        _write_released(label, r)
        made += 1
    for r in sorted(earlier, key=lambda r: (r.get("rung", 0), r.get("sequence", 0))):
        _write_released(r["concept_id"], r)
        made += 1
    if BOOK.is_b0:
        print(f"  {made} released sections for Part(s) {', '.join(letters)}")
    else:
        missing = sorted(deps - found)
        print(f"  {made} released sections: {len(found)} from Book 0"
              + (f" (Parts {', '.join(letters)} and ground-floor deps)" if letters
                 else " (ground-floor deps)")
              + f", {len(earlier)} from earlier rungs of {BOOK.subject}")
        if missing:
            print(f"  MISSING - ground_floor_deps with no Book 0 record: {', '.join(missing)}")


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
    for cid in _ids(cids):
        r = load(cid)
        label = BOOK.label(cid, r)
        path = BOOK.f(f"{label}-final-prose.yml")
        if not os.path.exists(path):
            print(f"  {label}: no final prose - skipped")
            continue
        with open(path, encoding="utf-8") as fh:
            final = yaml.safe_load(fh)
        target = BOOK.path_of(cid)
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


def main(argv):
    global BOOK
    opts, args = take_opts(argv)
    if not args:
        sys.exit(__doc__)
    BOOK = Book.from_opts(opts)
    cmd, rest = args[0], args[1:]
    {"extract": extract, "assemble": assemble, "release": release,
     "writeback": writeback}[cmd](rest)


if __name__ == "__main__":
    main(sys.argv[1:])
