# Fixer brief · S02-R1 (Task 4 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S02-R1`. Do not commit or push. Other fixers
are working on other sections at the same time: edit only your own record
(`check/records/S02/<RECORD-ID>.yml`), its figure specs/PNGs (`check/figures/s02-r1-cNN-*`), and
your defect file. Never edit `sources/`, `sources/INDEX.yml`, `check/references/library.bib`,
`prose/GLOSSARY.md`, `check/build.py` or any other record; never fetch from the web. If a fix needs a
source that is not held, or a change to a shared file, write that under the defect and leave it open.

Read `books/S02-R1/defects/<RECORD-ID>.md` and the record it names. Read the parts of `claude.md`
the defects cite (and "The one rule that matters"), and nothing else of it. For a defect that
depends on what a source says, open the held file in `sources/` and check it yourself: auditors
can be wrong — if one is, write "withdrawn: <reason, with the source's words>" and change nothing.

Apply every other item. Rules while fixing: a claim without an opened source is not written down
as a fact; every number's `quote` must state that number; keep the reader's second person; keep
sentences short (one idea each) — the compression pass is done, so do not re-grow the section: fix
with the fewest words that close the defect, and prefer deleting a false sentence to adding a
qualifying one. Never cite a Book 0 section by record id in a way that bypasses the renderer
(write `B0-R0-Cnn`, `S01-R1-Cnn` or `S02-R1-Cnn` in backticks; the build prints them as "Book 0, B4" /
"Book 1, section 3" / "section 3"). Expand every abbreviation at first use in the section. If a fix changes a number a
figure uses, update the figure's spec and run `python check/figures/draw.py --book S02-R1`, then
look at the PNG with the Read tool.

Then run `python check/build.py --check` and fix until blocking is zero for this record (the
arithmetic check evaluates every equation: a blocking failure from it is a real slip). Recompute
every practice/exercise answer you touched in Python. Then run
`python check/build.py --subject S02-R1` and read **your section only** in `check/_build/S02-R1.md`
(heading "### N · ..."). Every place you have to read a sentence twice is a defect: fix it.

Under each defect in the defects file, write one line starting "Fixer:": what you changed (or
"withdrawn: ..." / "open: needs ..."). Return at most 150 words: fixed / withdrawn / open counts,
and anything open.

**Book-wide decisions (conductor, 24 Sep 2026) — apply them wherever your defects touch them, so
seventeen fixers produce one book:**

1. **Stores and rates.** In this book `ES` is the energy stored (kcal) and `dES/dt` its rate
   (kcal a day). Hall and colleagues write `ES` for the rate: where their equation is quoted, say
   once that their ES is a rate, and write this book's form beside it.
2. **k is positive.** A rate constant `k` is always above zero; a shrinking curve is written
   `e^(-kt)`. Never "k is negative".
3. **Expenditure is `EE`.** Hall writes EO; say so once where Hall is quoted (C01), use EE elsewhere.
4. **Subscripts.** No underscores in prose. A label is written straight after the letter: `W0`,
   `EI0`, `BW0`, `kP`, `ρF`. C01 teaches this convention once ("a letter or digit written after a
   symbol is a label: W0 is the starting weight, not W times 0"); every other section follows it.
5. **ICMR-NIN.** The held source is the 2020 brief note. ICMR-NIN has issued a 2024 revised summary
   (a printed book; not held, not checked). Where a section uses the 2020 figures (BMR reduction,
   PAL), keep them, name the 2020 note as the source, and add nothing about 2024 beyond one line in
   the record's `review` (as_of 2020 note; re-check against the 2024 summary).
6. **Figures.** Raw carets in figure text are fixed in the tool (`^2` now prints as ²); a defect
   about a caret in a legend is closed by redrawing. Other figure faults are fixed in the spec.
7. **Polidori 2016** now holds the β, UGE (an energy loss, 360 kcal/d in Table 1; no per-gram
   factor stated) and kP = 95 passages (`sources/polidori_2016.txt`, blocks 14–17): quote them.

Scratch in `/home/claude/scratch-fix-<RECORD-ID>/`. Several fixers run `draw.py` and
`build.py --subject S02-R1` at the same time; if the rendered file looks truncated, re-run it.
