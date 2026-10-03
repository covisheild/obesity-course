# Fixer brief · S52-R1 (Task 4 of PIPELINE.md)

Repository `/home/claude/work/obesity-course`, branch `book/S52-R1`. Absolute paths. Do not commit or push;
never `rm` in the repository. Other fixers work on other sections at the same time: edit only your own records
(`check/records/S52/<RECORD-ID>.yml`), their figure specs/PNGs (`check/figures/s52-r1-cNN-*`), and their defect
files. Never edit `sources/`, `sources/INDEX.yml`, `check/references/library.bib`, `prose/GLOSSARY.md`,
`books/S52-R1/numbers.yml` (write a needed key under the defect as "Partly: conductor adds key ...") or anything
under `check/` other than your records and figures; never fetch from the web. If a fix needs a source that is
not held, or a change to a shared file, write that under the defect.

Read `books/S52-R1/defects/<RECORD-ID>.md` and the record it names. Read the parts of `claude.md` the defects
cite (and "The one rule that matters"), `books/S52-R1/DRAFT-BRIEF.md` ("Code") and
`books/S52-R1/TOOLING-CODE-GATE.md`. For a defect that depends on what a source says, open the held file and
check it yourself: auditors can be wrong.

Under each numbered defect write exactly one line beginning **Fixed:** (what you changed), **Partly:** (what you
changed and who owns the rest) or **Rejected:** (why the text was right, with the source's words). Leave the
`Verified:` line to the verifier.

Rules while fixing: a claim without an opened source is not written down as a fact; every number's `quote`
must state that number; second person; one idea a sentence. **The book is over its page budget (342 pages
rendered against 240), so no fix may grow a section beyond what closing the defect needs.** Prefer deleting a
false sentence to qualifying it; act on the auditor's "style" items that remove material without loss (a long
tibble print where `nrow()` or `print(n = 3)` shows the point; a duplicate drill at one level), and on gaps
choose the shortest closure: a one-line gloss plus a pointer to the section that teaches the thing, rather than
teaching it again. Cite another section with its record id in backticks (`S52-R1-C09`, `B0-R0-C28`); the
renderer prints it as "section 9" / "Book 0, D5". Expand every abbreviation at first use in the section.

**Code.** Any change to an r/sh block, or a new one: run
`python check/code_gate.py --write --record <file>` then `--check --record <file>` (0 failures), and make the
prose agree with every changed output. Never type an output block. A practice item runs as its own fresh
session: its prompt must hold every line its answer needs. Inline code goes in backticks; a unit like kg/m^2 is
prose, never inside backticks, and never between two backticked names on one line if avoidable.

**Book-wide decisions (conductor, 3 Oct 2026), so twenty-two fixers produce one book:**
1. In `penguins_raw.csv` one row is one bird's record in one nesting season (a "nesting observation"); the
   same bird can appear in more than one row and a nest has two birds. Never call rows "penguins" or "nests"
   when counting; say "rows". Where a count of birds or nests is needed and not computed, do not state it.
2. `penguins_raw` is the data as read; `penguins` is a cleaned copy (C06–C09 were renamed at reconcile).
3. The NHANES sex variable is `RIAGENDR` (1 male, 2 female per the DEMO_L codebook, held in
   `nchs_nhanes_2021_2023_bmx_demo`); quote the codebook when a section first uses it. Every NHANES summary
   says it is unweighted and estimates nothing about the US population.
4. Functions used before the section that teaches them: one-line gloss and pointer (e.g. "`count()` counts
   rows per value; `S52-R1-C14` teaches it"). Do not re-teach.
5. Amendment S52-R2-A01 (S52-R2 P1 now includes iteration): C05 and C22 add `S52-R2-A01` to `bridge_ref`
   where they point to S52-R2's functions; say only what the amendment says.
6. Behaviour of the installed versions is what the code gate prints; behaviour of newer versions only as
   `tidyverse_news_s52r1` states it.
7. "Book 0" is the series' name for the ground floor (the reader has read it): not a defect.

If a fix changes a number a figure uses, update the spec, run `python check/figures/draw.py --book S52-R1`, and
look at the PNG. Then run `python check/build.py --check` (about 2.5 minutes; timeout ≥ 900 s) until blocking is
zero for your records. Recompute every practice/exercise answer you touched. Do not render the book (other
fixers run at the same time); reread your records' prose directly. The conductor renders after all fixers finish.

Return at most 150 words: fixed / partly / rejected counts per section, and anything left for the conductor.
