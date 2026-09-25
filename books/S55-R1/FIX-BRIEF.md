# Fixer brief · S55-R1 (Task 4 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S55-R1`. Do not commit or push. Other fixers
are working on other sections at the same time: edit only your own record
(`check/records/S55/<RECORD-ID>.yml`), its figure specs/PNGs (`check/figures/s55-r1-cNN-*`), and
your defect file. Never edit `sources/`, `sources/INDEX.yml`, `check/references/library.bib`,
`prose/GLOSSARY.md`, `check/build.py` or any other record; never fetch from the web. If a fix needs a
source that is not held, or a change to a shared file, write that under the defect and leave it open.

Read `books/S55-R1/defects/<RECORD-ID>.md` and the record it names. Read the parts of `claude.md`
the defects cite (and "The one rule that matters"), and nothing else of it. For a defect that
depends on what a source says, open the held file in `sources/` and check it yourself: auditors
can be wrong — if one is, write "withdrawn: <reason, with the source's words>" and change nothing.

Apply every other item. Rules while fixing: a claim without an opened source is not written down
as a fact; every number's `quote` must state that number; keep the reader's second person; keep
sentences short (one idea each) — the compression pass is done, so do not re-grow the section: fix
with the fewest words that close the defect, and prefer deleting a false sentence to adding a
qualifying one. Never cite a Book 0 section by record id in a way that bypasses the renderer
(write `B0-R0-Cnn`, `S01-R1-Cnn` or `S55-R1-Cnn` in backticks; the build prints them as "Book 0, B4" /
"Book 1, section 3" / "section 3"). Expand every abbreviation at first use in the section. If a fix changes a number a
figure uses, update the figure's spec and run `python check/figures/draw.py --book S55-R1`, then
look at the PNG with the Read tool.

Then run `python check/build.py --check` and fix until blocking is zero for this record (the
arithmetic check evaluates every equation: a blocking failure from it is a real slip). Recompute
every practice/exercise answer you touched in Python. Then run
`python check/build.py --subject S55-R1` and read **your section only** in `check/_build/S55-R1.md`
(heading "### N · ..."). Every place you have to read a sentence twice is a defect: fix it.

Under each defect in the defects file, write one line starting "Fixer:": what you changed (or
"withdrawn: ..." / "open: needs ..."). Return at most 150 words: fixed / withdrawn / open counts,
and anything open.

**Book-wide decisions (conductor, 25 Sep 2026) — apply them wherever your defects touch them, so
eight fixers produce one book:**

1. **C07 binds; C08 implements it.** The who-is-waiting test in `S55-R1-C07` is the book's rule. C08's
   sheet scores item 4 (who is waiting) **0** when the waiting party is vague ("policy makers", "the
   literature", "future researchers") or is a body the reader cannot name and reach, and item 5 (what
   they would do differently) **0** when the actions for the possible answers are guessed or are the
   same. A zero on item 4 or on item 5 rejects the question whatever its total. Scores of 1 are kept
   for a named, reachable party whose decision is real but not yet confirmed with them. C08's
   candidates, rejections, practice answers and figure follow this; C07's examples must fail or pass
   by the same wording.
2. **One name for the first kind of question.** C02 introduces the "how-common question" (a question
   with no exposure). C03's three kinds are describe, relate and cause; C03 says once that a describe
   question is what C02 called a how-common question, and no third name is used anywhere.
3. **Prevalence** is a share (a proportion, people with the condition divided by people in the
   population at that time), never a count — and only as a held source states it; otherwise say "how
   common" without the term.
4. **A population has a boundary of place, age and time** (C02). Every practice answer and example
   applies this rule the same way: a population without an age band is faulted, everywhere.
5. **No obesity cut-offs** are held. No example or answer may depend on one: write the outcome as the
   measurement ("measured waist circumference", "body mass index measured at the camp") or "obesity as
   the protocol defines it", never a number. C07's camp example must not need data the camp does not
   collect: make its question one the camp could answer, or say the camp would have to start measuring.
6. **Abbreviations** expanded at first use in each section: non-communicable disease (NCD),
   population–intervention–comparison–outcome (PICO) and its exposure form (PECO), Centers for Disease
   Control and Prevention (CDC), FINER as the source expands it. Credit FINER only as the held sources
   do (check `ratan_2019`, `aslam_emmanuel_2010`, `farrugia_2010`); no author or year they do not give.
7. **Not held, never stated as fact:** NMC thesis rules; the Companies Act or CSR rules (CSR named as a
   word only); obesity cut-offs; any per-stage waste percentage from Chalmers & Glasziou 2009 (only its
   85% and "roughly 50%" text, with its basis); citation of cross-sectional studies as a design.
8. **Second-hand figures are attributed as reported:** the 1990 *Science* 55% ("reported by Van Noorden
   2017"; Nicolaisen & Frandsen report the same reports differently — say the figures differ by
   source), the Larivière–Sugimoto figures, Morgan's 54% ("from a review they cite"). Dated counts carry
   their year ("in 2017, Web of Science indexed about ...").
9. **Unsourced claims** are deleted or softened to what a held source says; the book's own reasoning
   reads as reasoning ("because..."), not as a finding. Prompts carry no hint of the answer.
10. **References:** a needed reference to a source already in `check/references/library.bib` may be
    added to your own record; a source not held stays open. `kind`: `blackstone_2012`,
    `jhangiani_2019_methods`, `cdc_ss1978_lesson1` are `textbook`; journal papers `primary`.
11. **Figures from non-open sources** (C06's Patsopoulos medians): a chart the course draws from a few
    stated numbers is kept; no table is reproduced in prose as a table copied from the source.

