# Verifier brief · S36-R1 (Task 4b of PIPELINE.md)

Repository `/home/claude/obesity-course`. Do not commit. You did not draft, audit or fix these
records. Edit nothing except the defect files you are given (one line under each defect).

For each defect in `books/S36-R1/defects/<RECORD-ID>.md`, read the fixer's "Fixer:" line, then
read the record (`check/records/S36/<RECORD-ID>.yml`) and check the defect is actually gone:
recompute any number in Python, search the source file (`sources/INDEX.yml` maps citekeys to
files) for any quote, open any figure PNG the defect concerns (`check/figures/`). A "withdrawn"
must be justified by the source's words or by the fixer brief's book-wide decisions
(`books/S36-R1/FIX-BRIEF.md`); check it. Check nothing else. Under each defect write one line:
`Verifier: closed` or `Verifier: open, because …`. Also run `python check/build.py --check` and
report any blocking line naming your records.

Return at most 100 words: open count per record, and each open defect in one line.

**This book.** A defect whose only remaining action is for a person to check an OCR quote (from
`kitzinger_1995`, `britten_1995`, `pope_mays_1995`) against the scanned page image is marked
`Verifier: deferred, page image` — neither closed nor open; the conductor tracks those. A defect a
fixer marked open because the fix belonged in another record (labels restart in each interview;
"rung" explained): check whether that other record now carries it (C03 illustration 2 says the
labels restart in each made-up interview; the conductor replaced "rung" in reader text with "book"
or "next level of this subject") and close it if so.
