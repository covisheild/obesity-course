# Fixer brief · S01-R1 (Task 4 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S01-R1`. Do not commit or push. Other fixers
are working on other sections at the same time: edit only your own record
(`check/records/S01/<RECORD-ID>.yml`), its figure specs/PNGs (`check/figures/s01-r1-cNN-*`), and
your defect file. Never edit `sources/`, `sources/INDEX.yml`, `check/references/library.bib`,
`prose/GLOSSARY.md`, `check/build.py` or any other record; never fetch from the web. If a fix needs a
source that is not held, or a change to a shared file, write that under the defect and leave it open.

Read `books/S01-R1/defects/<RECORD-ID>.md` and the record it names. Read the parts of `claude.md`
the defects cite (and "The one rule that matters"), and nothing else of it. For a defect that
depends on what a source says, open the held file in `sources/` and check it yourself: auditors
can be wrong — if one is, write "withdrawn: <reason, with the source's words>" and change nothing.

Apply every other item. Rules while fixing: a claim without an opened source is not written down
as a fact; every number's `quote` must state that number; keep the reader's second person; keep
sentences short (one idea each) — the compression pass is done, so do not re-grow the section: fix
with the fewest words that close the defect, and prefer deleting a false sentence to adding a
qualifying one. Never cite a Book 0 section by record id in a way that bypasses the renderer
(write `B0-R0-Cnn` or `S01-R1-Cnn` in backticks; the build prints them as "Book 0, B4" /
"section 3"). Expand every abbreviation at first use in the section. If a fix changes a number a
figure uses, update the figure's spec and run `python check/figures/draw.py --book S01-R1`, then
look at the PNG with the Read tool.

Then run `python check/build.py --check` and fix until blocking is zero for this record (the
arithmetic check evaluates every equation: a blocking failure from it is a real slip). Recompute
every practice/exercise answer you touched in Python. Then run
`python check/build.py --subject S01-R1` and read **your section only** in `check/_build/S01-R1.md`
(heading "### N · ..."). Every place you have to read a sentence twice is a defect: fix it.

Under each defect in the defects file, write one line starting "Fixer:": what you changed (or
"withdrawn: ..." / "open: needs ..."). Return at most 150 words: fixed / withdrawn / open counts,
and anything open.
