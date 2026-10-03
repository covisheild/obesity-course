# S52-R1 intake group d: checks the four NMC quotations in books/S52-R1/COVERAGE.md (lines 15-18) against
# the NMC raw text, and prints what the printed sentence continues with after each quotation. Run from the
# repository root.
import re

norm = lambda s: " ".join(s.split())
raw = norm(open("books/S52-R1/intake/raw/nmc_pg_md_community_medicine-pdftotext.txt", encoding="utf-8").read())
lines = open("books/S52-R1/COVERAGE.md", encoding="utf-8").read().splitlines()[14:18]
for n, line in enumerate(lines, start=15):
    for q in re.findall(r"“([^”]+)”|\"([^\"]+)\"", line):
        q = norm(q[0] or q[1])
        k = raw.find(q)
        if k == -1:
            print(f"line {n}: NOT FOUND: {q!r}")
            continue
        before = raw[max(0, k - 60):k]
        after = raw[k + len(q):k + len(q) + 60]
        print(f"line {n}: FOUND: {q!r}\n    printed before: ...{before!r}\n    printed after:  {after!r}...")
