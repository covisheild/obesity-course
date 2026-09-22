"""Check one cut prose file against the original it was cut from.

Run:  python books/B0/compress/validate.py A4-pass1-prose.yml
"""
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "..", "..", "check"))
import build  # noqa: E402


def measure(texts):
    sents = [s for t in texts for p in build._paragraphs(t) for s in build._sentences(p)]
    lens = [len(s.split()) for s in sents]
    return (sum(len(t.split()) for t in texts),
            round(sum(lens) / len(lens), 2) if lens else 0.0,
            max(lens) if lens else 0)


def main(cut_name):
    sec = os.path.basename(cut_name).split("-")[0]
    cut = yaml.safe_load(open(os.path.join(HERE, os.path.basename(cut_name)), encoding="utf-8"))
    orig = yaml.safe_load(open(os.path.join(HERE, f"{sec}-prose.yml"), encoding="utf-8"))

    bad = []
    if set(cut) != set(orig):
        bad.append(f"keys differ. missing {sorted(set(orig) - set(cut))}, "
                   f"extra {sorted(set(cut) - set(orig))}")
    for k in sorted(set(cut) & set(orig)):
        if not str(cut[k]).strip():
            bad.append(f"{k} is empty; every field must survive")

    # every surviving sentence must appear, word for word, in the original: deletion only
    def norm(s):
        return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", s)).strip().lower()

    for k in sorted(set(cut) & set(orig)):
        o = norm(str(orig[k]))
        for para in build._paragraphs(str(cut[k])):
            for s in build._sentences(para):
                if norm(s) and norm(s) not in o:
                    bad.append(f"{k}: this sentence is not in the original word for word, so it "
                               f"was rewritten rather than kept: \"{' '.join(s.split()[:12])}...\"")

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
    print("\nOK: deletion only, every field survives, sentence length did not rise.")


if __name__ == "__main__":
    main(sys.argv[1])
