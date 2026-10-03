# Verifier brief · S52-R1 (Task 4b of PIPELINE.md)

Repository `/home/claude/work/obesity-course`, branch `book/S52-R1`. Absolute paths. Do not commit; never `rm`.
You did not draft, audit or fix these records. Edit nothing except the defect files you are given.

For each numbered defect in `books/S52-R1/defects/<RECORD-ID>.md`, read its **Fixed:** / **Partly:** /
**Rejected:** line, then read the record (`check/records/S52/<RECORD-ID>.yml`) and check the defect is actually
gone: recompute any number in Python or R, search the source file (`sources/INDEX.yml` maps citekeys to files)
for any quote, open any figure PNG the defect concerns (`check/figures/`), and for code run
`python check/code_gate.py --check --no-cache --record <file>` once per record (0 failures) and read the output
blocks the defect concerns. A **Rejected:** must be justified by the source's words, by the auditor's own
withdrawal, or by the book-wide decisions in `books/S52-R1/FIX-BRIEF.md` (and the conductor's notes: from C10 on
every session loads `library(dplyr, warn.conflicts = FALSE)`, glossed in C10; C22 keeps the full
`sessionInfo()` printout). A **Partly:** is closed only if the part left is owned elsewhere and named; otherwise
open. Check nothing else.

Under each defect write exactly one line: `Verified: closed` or `Verified: open, because <...>`. Then run
`python check/defects.py S52-R1` and confirm none of your defects lacks a line.

Return at most 100 words: open count per record, and each open defect in one line.
