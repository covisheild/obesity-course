# Fixer brief, rendered-page round · S58-R1 (3 Oct 2026)

Follow `books/S58-R1/FIX-BRIEF.md` (its rules and book-wide decisions still bind), with these
changes. Only the items under "## Found in the rendered pages" at the end of your defect file are
open; every earlier item is closed and verified, do not touch their lines. The built PDF is
`check/_build/S58-R1.pdf` (read the pages named with the Read tool's `pages` parameter) and its
markdown source `check/_build/S58-R1.md`. Many of these faults come from how the renderer reads a
prose field (a line beginning "(a)" or "1." or "- " becomes a list; a record id at the start of a
sentence prints lower-case): find the record text that produced the fault and rewrite it so it
renders as intended, with the fewest words. Never edit `check/` code. Do NOT run
`python check/build.py --subject` (twelve other fixers are working; the conductor rebuilds the PDF
afterwards); run `python check/build.py --check` until blocking is zero for your record, and if you
change a figure spec run `python check/figures/draw.py --book S58-R1` and look at the PNG. To see
how a field will render, you may run pandoc on a scratch copy of the field in
`/home/claude/scratch-s58-rfix-<RECORD-ID>/`. Write the `Fixed:`/`Partly:`/`Rejected:` line under each
open item. Return at most 80 words.
