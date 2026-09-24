# Verifier brief · S02-R1 (Task 4b of PIPELINE.md)

Repository `/home/claude/obesity-course`. Do not commit. You did not draft, audit or fix these
records. Edit nothing except the defect files you are given (one line under each defect).

For each defect in `books/S02-R1/defects/<RECORD-ID>.md`, read the fixer's "Fixer:" line, then
read the record (`check/records/S02/<RECORD-ID>.yml`) and check the defect is actually gone:
recompute any number in Python, search the source file (`sources/INDEX.yml` maps citekeys to
files) for any quote, open any figure PNG the defect concerns (`check/figures/`). A "withdrawn"
must be justified by the source's words or by the fixer brief's book-wide decisions
(`books/S02-R1/FIX-BRIEF.md`); check it. Check nothing else. Under each defect write one line:
`Verifier: closed` or `Verifier: open, because …`. Also run `python check/build.py --check` and
report any blocking line naming your records.

Return at most 100 words: open count per record, and each open defect in one line.
