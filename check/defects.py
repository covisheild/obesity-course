"""Every audit defect gets a disposition, and every disposition a verifier's word.

    python check/defects.py S47-R1        # lists defects with no disposition or no verification

Added 28 Sep 2026 from the statistics book, where every one of 298 audit rows was logged
FIXED, PARTLY or REJECTED with a reason, and a fresh verifier checked each claim. Auditors can be
wrong (handover §7, "withdrawn defects"), so rejecting a defect is allowed, but only with a
reason a verifier has accepted.

The format, under each numbered defect in books/<ID>/defects/<RECORD-ID>.md:

    Fixed: <what changed>            (or)  Partly: <what changed, and who owns the rest>
                                     (or)  Rejected: <why the text was right>
    Verified: closed                 (or)  Verified: open, because <...>

`parallel.py ready` and the conductor run this before bundling a book that is not legacy.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
ITEM = re.compile(r"^(\d+)\.\s+\*\*", re.M)
DISPO = re.compile(r"^\s*(Fixed|Partly|Rejected):\s*\S", re.M)
VERIF = re.compile(r"^\s*Verified:\s*(closed|open\b.*)", re.M)


def problems(book_id):
    d = os.path.join(REPO, "books", book_id, "defects")
    out = []
    if not os.path.isdir(d):
        return out
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        text = open(os.path.join(d, fn), encoding="utf-8").read()
        starts = [m.start() for m in ITEM.finditer(text)] + [len(text)]
        for i in range(len(starts) - 1):
            chunk = text[starts[i]:starts[i + 1]]
            n = ITEM.match(chunk).group(1)
            dm, vm = DISPO.search(chunk), VERIF.search(chunk)
            if not dm:
                out.append(f"{fn} item {n}: no Fixed/Partly/Rejected line")
            if not vm:
                out.append(f"{fn} item {n}: not verified")
            elif vm.group(1).startswith("open"):
                out.append(f"{fn} item {n}: open ({vm.group(1)[:80]})")
    return out


if __name__ == "__main__":
    bid = sys.argv[1]
    p = problems(bid)
    for x in p:
        print(" ", x)
    print(f"{bid}: {len(p)} defect(s) without a closed disposition")
    sys.exit(1 if p else 0)
