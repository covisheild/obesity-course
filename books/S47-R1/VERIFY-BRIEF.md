# Verifier brief · S47-R1 (Task 4b of PIPELINE.md)

Repository `/home/claude/obesity-course`. Do not commit. You did not draft, audit or fix these
records. Edit nothing except the defect files you are given. No `rm` in the repository.

For each numbered defect in `books/S47-R1/defects/<RECORD-ID>.md`, read the fixer's `Fixed:` /
`Partly:` / `Rejected:` line, then read the record (`check/records/S47/<RECORD-ID>.yml`) and check
the defect is actually gone: re-derive any answer, search the source file (`sources/INDEX.yml` maps
citekeys to files) for any quote, open any figure PNG the defect concerns (`check/figures/`). A
`Rejected:` must be justified by the source's words or by the book-wide decisions in
`books/S47-R1/FIX-BRIEF.md`; check it. A `Partly:` is closed only if what remains is genuinely outside
this record (a source not held, another section's text) and is named. Check nothing else, except: if
a fix introduced a new false statement in the sentence it touched, say so.

Under each defect write exactly one line: `Verified: closed` or `Verified: open, because …`
(`check/defects.py` reads it).

Conductor rulings (2 Oct 2026) the verifier applies: (a) a PIB release is kind `instrument` where an
institutional record uses it for what the government decided, and `primary` where an empirical record
uses it as a text whose framing is studied — both are correct; (b) the 40% is "the special de-merit
rate of 40%" as PIB 2163555 states; a record need not call it "combined", and must not say the Union
levies it or that States notify it under their own Acts; (c) figure notes naming wanted diagrams are
not defects; (d) the 01/2026 copy is CBIC's pre-Gazette copy and 19/2025 is not held: a record that
dates the rate "as amended by 01/2026-CT(Rate), in force 1 May 2026" and says 19/2025 was not read is
closed.

Run `python check/build.py --check` and report any blocking line naming your records. Return at most
100 words: open count per record, and each open defect in one line.
