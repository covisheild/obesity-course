# Fixer brief · S37-R1 (Task 4 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S37-R1`. Do not commit or push. Other fixers
are working on other sections at the same time: edit only your own record
(`check/records/S37/<RECORD-ID>.yml`), its figure specs/PNGs (`check/figures/s37-r1-cNN-*`), and
your defect file. Never edit `sources/`, `sources/INDEX.yml`, `check/references/library.bib`,
`prose/GLOSSARY.md`, `check/build.py` or any other record; never fetch from the web. If a fix needs a
source that is not held, or a change to a shared file, write that under the defect and leave it open.

Read `books/S37-R1/defects/<RECORD-ID>.md` and the record it names. Read the parts of `claude.md`
the defects cite (and "The one rule that matters"), and nothing else of it. For a defect that
depends on what a source says, open the held file in `sources/` and check it yourself: auditors
can be wrong — if one is, write "withdrawn: <reason, with the source's words>" and change nothing.

Apply every other item. Rules while fixing: a claim without an opened source is not written down
as a fact; every number's `quote` must state that number; keep the reader's second person; keep
sentences short (one idea each) — the compression pass is done, so do not re-grow the section: fix
with the fewest words that close the defect, and prefer deleting a false sentence to adding a
qualifying one. Never cite a Book 0 section by record id in a way that bypasses the renderer
(write `B0-R0-Cnn`, `S01-R1-Cnn` or `S37-R1-Cnn` in backticks; the build prints them as "Book 0, B4" /
"Book 1, section 3" / "section 3"). Expand every abbreviation at first use in the section. If a fix changes a number a
figure uses, update the figure's spec and run `python check/figures/draw.py --book S37-R1`, then
look at the PNG with the Read tool.

Then run `python check/build.py --check` and fix until blocking is zero for this record (the
arithmetic check evaluates every equation: a blocking failure from it is a real slip). Recompute
every practice/exercise answer you touched in Python. Then run
`python check/build.py --subject S37-R1` and read **your section only** in `check/_build/S37-R1.md`
(heading "### N · ..."). Every place you have to read a sentence twice is a defect: fix it.

Under each defect in the defects file, write one line starting "Fixer:": what you changed (or
"withdrawn: ..." / "open: needs ..."). Return at most 150 words: fixed / withdrawn / open counts,
and anything open.

**Book-wide decisions (conductor, 25 Sep 2026) — apply them wherever your defects touch them, so
eighteen fixers produce one book:**

1. **Stages.** C01's eight stages are the book's only stage names: production, storage, processing,
   distribution, retail, preparation, consumption, waste. C16's map, C17's method and C18's sketch
   place each instrument or proposal at one or more of those stages, by those names. "Trade",
   "tax", "provision", "safety and labelling" are kinds of instrument, not stages: keep them as a
   separate column or word ("an import duty, a trade instrument, acting on what reaches
   distribution"), never as extra stages.
2. **Food environment.** C05's definition is canonical and includes promotion, advertising and
   information. An awareness campaign or a label moves the information element; it does not move
   availability or price. C17 says exactly that; it must not say a campaign moves no element.
3. **Anganwadi norms revision.** Only what `pib_2251769` says: the supplementary-nutrition norms of
   NFSA Schedule II for children 6 months to 6 years, pregnant women, lactating mothers and
   adolescent girls "have been revised in January 2023"; the revised numbers are not held; the held
   2022 guidelines' table is marked "under revision". Nothing about PM POSHAN's school-meal norms
   being revised. C12 and C13 use this same scope and wording.
4. **Not held, nothing rests on them:** `eca_1955`, `food_corporations_act_1964` (withdrawn), Hawkes
   2020, PM POSHAN 2023 guidelines (cost sharing), CACP "About us" (the 1965 date). A fact the audit
   asks for that no held file carries (e.g. a paddy-to-rice ratio, the lower/upper primary class
   split, the components of an effective duty) is either found in a held file and quoted, or the
   sentence is cut or reworded so it does not need it. Never from memory.
5. **Currency.** Every scheme, price and rate carries the date or period the held text gives. Where
   the held text says a scheme was approved to March 2026, or a stock limit ran to April 2026, say so
   in the past or with its end date; do not assert it continues. The next event goes in the record's
   `review` trigger.
6. **Duty wording.** Use the words each release uses: "basic customs duty" only where the release
   says it; the 2024 figure is "import duty, as the release states". Figures follow the same rule.
7. **Illustrations.** `build.py` does not check quotes in `illustrations[]`; check any you touch by hand.

Scratch in `/home/claude/scratch-fix-<RECORD-ID>/`. Several fixers run `draw.py` and
`build.py --subject S37-R1` at the same time; if the rendered file looks truncated, re-run it.
