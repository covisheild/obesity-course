# Restorer brief · S52-R1 (Task 5, step 5c)

Repository `/home/claude/work/obesity-course`. Do not commit, and do not edit any record. You are neither
the cutter nor the cold reader. Read `claude.md` §12 and `PIPELINE.md` "Step 5c". Read
`books/S52-R1/compress/COLDREAD-REPORT-A.md` (C01–C11) or `COLDREAD-REPORT-B.md` (C12–C22), the gaps for your sections. For each of your sections read `<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml`
in `books/S52-R1/compress/`, and `books/S01-R1/compress/RESTORE-DECISIONS.md` as the format exemplar.

For each gap decide one of: **restored** (the original holds sentences that let the reader do the
thing: name them, word for word, in `books/S52-R1/compress/restore-lists/<S>.txt`, one sentence
opening per line, each commented with the gap id, e.g. `# A-C04-1`); **hole** (the original does not
fill it either, or it is an error or contradiction rather than missing text: it goes to the audit);
**not a defect** (say why in one line). Restore only where the reader was actually unable to do
something; never because a passage reads well. Write nothing new. A pass-1 sentence left dangling by
the cut ("Then take the state at t + h" with nothing before it) is closed by restoring the original's
sentence before it.

Build each section with `python check/compress/restore.py --subject S52-R1 <S> restore-lists/<S>.txt`
(a section with nothing to restore still gets an empty list, so every section has a
`-final-prose.yml`), then `python check/compress/validate.py --subject S52-R1 <S>-final-prose.yml`
until it passes. If validation fails, find why (your list, or a tool bug); never loosen the tool, and
report a tool conflict instead of working round it.

Write `books/S52-R1/compress/RESTORE-DECISIONS-<batch>.md` (word-count table and gap-by-gap
decisions) and `books/S52-R1/compress/HOLES-<batch>.md`: each hole with section and field, the
sentence as it stands, what is wrong or missing, and what would close it (for the fixer). Scratch in
`/tmp/claude-0/scratch-restore-<batch>/`. Return at most 150 words: per section words original → cut →
final and validate result; counts restored / hole / not a defect.

**S52-R1 specifics.** The cut touched only prose fields. Gaps in practice problems, exercises and illustrations
(code examples) cannot be closed by restoring; they are holes for the fixer unless a cut prose sentence answers
them. Many cold-reader gaps are a function or symbol used before it is taught: if the original prose taught it
and the cut removed it, restore; if the original never taught it, it is a hole (say what would close it: a
one-line gloss, a pointer, a code line in an illustration, or a changed problem). A gap whose fix needs a new
or changed code block is always a hole (code must go through the code gate). The cold reader could not run
code: "values unpredictable without running" is not a defect when the problem asks the reader to run it.
"Book 0" as a name is the series convention (the reader of this book has read Book 0): not a defect.
