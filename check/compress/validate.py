"""Check one cut or restored prose file against the original it was cut from.

    python check/compress/validate.py --subject B0 A4-pass1-prose.yml
    python check/compress/validate.py --subject B0 A4-final-prose.yml
    python check/compress/validate.py --subject S01-R1 S01-R1-C02-final-prose.yml

The file is read from the book's working folder (`books/<ID>/compress/`), and so is the
original, `<label>-prose.yml`.

Every file, cut or restored: same fields, none empty; every sentence word for word in the
original (deletion only: nothing new in); mean and longest sentence not risen.

A restored file (`-final-prose.yml`), when its `-pass1-prose.yml` is beside it, is also checked
the other way: every sentence, list item, quote, table row, heading and fenced block the cut
kept must still be there (nothing kept lost). That is the check that would have caught the
restore bug of 23 September 2026, which silently dropped every kept bullet, quote and table row.
"""
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _book import Book, build, section_of, take_opts  # noqa: E402


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", s)).strip().lower()


def measure(texts):
    sents = [s for t in texts for p in build._paragraphs(t) for s in build._sentences(p)]
    lens = [len(s.split()) for s in sents]
    return (sum(len(t.split()) for t in texts),
            round(sum(lens) / len(lens), 2) if lens else 0.0,
            max(lens) if lens else 0)


def _fences(text):
    return re.findall(r"^[ \t]*```.*?^[ \t]*```[^\n]*$", text, re.M | re.S)


def _structural_lines(text):
    """Table rows and headings outside fences: build._paragraphs does not measure them, so the
    sentence check cannot see them go missing. Compared line by line."""
    body = re.sub(r"^[ \t]*```.*?^[ \t]*```[^\n]*$", "", text, flags=re.M | re.S)
    return [l for l in body.splitlines() if l.lstrip().startswith(("|", "#"))]


def survival(cut, final):
    """Everything the cut kept, still present after the restore."""
    lost = []
    for k in sorted(set(cut) & set(final)):
        have = {norm(s) for p in build._paragraphs(str(final[k])) for s in build._sentences(p)}
        for p in build._paragraphs(str(cut[k])):
            for s in build._sentences(p):
                if norm(s) and norm(s) not in have:
                    lost.append(f"{k}: kept by the cut, missing after restore: "
                                f"\"{' '.join(s.split()[:12])}...\"")
        lines = {norm(l) for l in str(final[k]).splitlines()}
        for l in _structural_lines(str(cut[k])):
            if norm(l) not in lines:
                lost.append(f"{k}: kept row or heading missing after restore: \"{l.strip()[:60]}\"")
        fences = {norm(f) for f in _fences(str(final[k]))}
        for f in _fences(str(cut[k])):
            if norm(f) not in fences:
                lost.append(f"{k}: kept fenced block missing after restore: "
                            f"\"{' '.join(f.split()[:8])}...\"")
    return lost


def main(argv):
    opts, args = take_opts(argv)
    if len(args) != 1:
        sys.exit(__doc__)
    book = Book.from_opts(opts)
    cut_name = os.path.basename(args[0])
    sec = section_of(cut_name)
    with open(book.f(cut_name), encoding="utf-8") as fh:
        cut = yaml.safe_load(fh)
    with open(book.f(f"{sec}-prose.yml"), encoding="utf-8") as fh:
        orig = yaml.safe_load(fh)

    bad = []
    if set(cut) != set(orig):
        bad.append(f"keys differ. missing {sorted(set(orig) - set(cut))}, "
                   f"extra {sorted(set(cut) - set(orig))}")
    for k in sorted(set(cut) & set(orig)):
        if not str(cut[k]).strip():
            bad.append(f"{k} is empty; every field must survive")

    # every surviving sentence must appear, word for word, in the original: deletion only
    for k in sorted(set(cut) & set(orig)):
        o = norm(str(orig[k]))
        for para in build._paragraphs(str(cut[k])):
            for s in build._sentences(para):
                if norm(s) and norm(s) not in o:
                    bad.append(f"{k}: this sentence is not in the original word for word, so it "
                               f"was rewritten rather than kept: \"{' '.join(s.split()[:12])}...\"")

    # a restore must not lose anything the cut kept
    pass1 = book.f(f"{sec}-pass1-prose.yml")
    if cut_name.endswith("-final-prose.yml") and os.path.exists(pass1):
        with open(pass1, encoding="utf-8") as fh:
            bad += survival(yaml.safe_load(fh), cut)
        print(f"{sec}: survival checked against {os.path.basename(pass1)}")

    ow, om, ol = measure([str(v) for v in orig.values()])
    cw, cm, cl = measure([str(v) for v in cut.values()])
    print(f"{sec}: words {ow} -> {cw}  ({100 * (ow - cw) / ow:.0f}% cut)")
    print(f"{sec}: mean sentence {om} -> {cm}   longest {ol} -> {cl}")
    if cm > om + 0.001:
        bad.append(f"mean sentence length rose, {om} -> {cm}. Something was compressed rather "
                   "than deleted. claude.md 12 calls that a failure whatever the word count says")
    if cl > ol:
        bad.append(f"longest sentence rose, {ol} -> {cl}")

    if bad:
        print("\nFAIL")
        for b in bad:
            print(" -", b)
        sys.exit(1)
    print("\nOK: deletion only, every field survives, sentence length did not rise"
          + (", nothing the cut kept was lost." if cut_name.endswith("-final-prose.yml")
             and os.path.exists(pass1) else "."))


if __name__ == "__main__":
    main(sys.argv[1:])
