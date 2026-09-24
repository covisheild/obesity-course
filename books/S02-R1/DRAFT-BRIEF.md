# Drafter brief · S02-R1 (Task 2 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S02-R1`. Do not commit, push, fetch from the
web, or use GitHub tools. Write only the files named for you.

Read `claude.md`: "The one rule that matters", the whole authoring style sheet (§1–§11a), and
specification §1 and §4. Skip §12 and the rest of the specification. Read the two exemplar records
you are given before writing a word — they are the standard, and matching them matters more than
following the rules in the abstract.

Read `books/S02-R1/INVENTORY.md` (your concepts' rows: what each must cover, its Book 0 sections,
its sources, whether it is quantitative) and `books/S02-R1/READY.md` + `sources/INDEX.yml` (which
source files and citekeys are held). This is **a subject book**: its reader has read Book 0 and Book 1 (S01-R1, energy balance; records in
`check/records/S01/`). Do not
re-teach what a Book 0 section in your row teaches; name it where the reader needs it (as the
exemplars do for earlier sections) and list it in `ground_floor_deps`. To see what a Book 0 section
actually says, read only its `definition` and `must_know` in `check/records/B0/<id>.yml`.

Write one YAML file per concept at `check/records/S02/<concept id>.yml` (subject `S02`, rung `1`,
`sequence` = the concept number), using `check/schema/example.concept.yml` as the template and
`check/schema/concept.schema.json` as the schema. `concept_deps` may name only earlier S02-R1
concepts.

For every concept the inventory marks quantitative, write `practice[]` on the ladder in `claude.md`
§7a — levels 1-3 mechanical on bare numbers, 4-6 applied to a real quantity with its unit, 7-8
diagnostic on a worked answer that is wrong, 9-10 transfer from a claim in words. How many is your
judgement, **between three and twenty-five in this book** (Harsh, 24 Sep 2026: easy concepts get
fewer problems, hard ones more; `practice_max: 25` is set in `books/S02-R1/book.yml`), chosen from
the technique and the number of moves that compose in it. The set must reach both ends of
the ladder, and say in one line in your notes why you chose the number. Prompts carry no hint of
the answer. Answers show every line. A problem quoting a real figure names its citekey in `refs`;
where no real figure exists, use bare numbers rather than inventing one.

For every factual claim, quote the exact words from the file in `sources/` that carry it, and put
the file and section in the locator. The quote must state the number it is cited for. If no held
file carries it, set `opened: false`, say in `verified.note` which instrument is needed, and write
the concept so it does not depend on the unopened claim. Held for this book (see `READY.md` and
`books/S02-R1/INTAKE.md`): OpenStax Calculus Vol 1 excerpts (`openstax_calculus_v1_s02`), Calculus
Vol 2 ch. 4 (`openstax_calculus_v2`), College Algebra 2e §7.5 (`openstax_college_algebra_2e_7_5`),
Austin *Understanding Linear Algebra* §2.1–2.2 (`austin_ula`), Introductory Statistics 2e incl. §4.1–4.2
(`openstax_intro_stats_2e`), OpenIntro Statistics 4e §3.4 (`openintro_stats_4e`), Chow & Hall 2008
prose only (`chow_hall_2008`), FAO/WHO/UNU 2004 incl. Table 5.2, Polidori 2016 incl. Equations 1–5
and Thomas 2013 incl. its Methods equation (both converted from MathML; the file header says how),
Hall 2011, Hall 2012, Hall & Guo 2017, Hall 2008 (text only), FAO FNP 77, ICMR-NIN 2020 brief note.
**Not held:** the typeset equations of Chow & Hall 2008 and of Hall 2008. Do not write either
equation from memory; where the inventory planned to use them, use a held equation instead
(Polidori 2016, Thomas 2013, Hall 2012's ES = EI - EO, FAO/WHO/UNU TEE = BMR x PAL and Table 5.2) and
say so in your notes. Textbook passages are for the definitions and rules; quote prose, since
formulas in those files are flattened by extraction. The source files mark which passages are
verbatim; never quote a `[NOTE]` or `[MATHML]` line or a header.

**Notation, shared by every batch so the book reads as one:** time `t` in days unless a source uses
years; body weight `W` in kg; energy intake `EI` and energy expenditure `EE` in kcal/day, with the
stored energy `ES` as in Hall 2012; a rate written `dW/dt` and said "the rate of change of W with
respect to t"; natural logarithm `ln`, and `log10` as in Book 0; vectors as bracketed lists of numbers
named by a lowercase letter, `x = (2, 5, 1)`; matrices by a capital letter; expectation `E[X]`,
variance `Var(X)`. The clash between `E` for energy and `E[X]` for expectation is real in papers:
the section that introduces `E[X]` says so once. Introduce every symbol in words at first use.

**Inventory flags you must honour:** C04 — Hall 2011 and Hall 2012 give about 1 year to half and
about 3 years to 95% of the eventual change; one exponential with a one-year half-time reaches 95%
at about 4.3 years. Present both as the model's rounded outputs and never claim one exponential fits
both. Anything the inventory routes to S02-R2 or S03 is named and routed in one line, not taught.

Never tell the reader to open a file in `sources/`. Name the instrument by its own title and give
the public URL from `check/references/library.bib`.

A `boundary` must-know point names a limit of the technique — when the tool stops being trustworthy
and what the reader should do then. Never a table-of-contents entry ("This section gets you...").

Prose fields are literal blocks (`|`), never folded (`>`). Columns go in a ```` ```table ```` block.
Display arithmetic goes in a ```` ```working ```` block, never indented. Write exponents as `10^7`
and logarithms as `log10`; no markup. Introduce an operator in words beside its symbol the first
time. Use `illustrations` (a list) where one illustration does not do the teaching. **Figures:** every section gets at least one, unless one line in `figure_note` says why a figure
would teach nothing the prose does not; a quantitative section gets a figure of its worked
relationship. Read `claude.md` §4, "Figures", and declare each as a `figures:` entry with a `spec`
as in `check/schema/example.concept.yml` (file names `s02-r1-cNN-<what>.png`). Run
`python check/figures/draw.py --book S02-R1` to see that each spec passes; never draw by hand. **Do not edit
`check/figures/draw.py` or `figspec.py`**: other drafters run it at the same time. If the figure you
want needs a kind the tool does not draw (a curve from a formula, a shaded area under a curve, a
tangent line), declare the nearest kind it does draw, or leave a `figure_note` and describe the
wanted figure with its numbers in your notes; the figure planner extends the tool once.

**Scratch:** any helper script or scratch file goes in `/home/claude/scratch-<your batch>/`, never a
shared name.

**Glossary:** do not edit `prose/GLOSSARY.md`. Put every new term's proposed row (same columns as
that file; read its header and a few rows) in your notes file under "Glossary rows". Check that the
term is not already glossed there; if it is, use the existing sense.

Before you hand back, check your own work as the auditor will. Run `python check/build.py --check`
until blocking is zero for your records (other drafters are writing other S02 records at the same
time; ignore failures in files that are not yours). Recompute every practice answer in Python, not
by reading it. For every quote, confirm it is in the source file and states the number it is cited
for. Check each item of `check/SELFCHECK.md`.

Write your notes to `books/S02-R1/draft-notes-<your batch>.md`: records written, anything
unsourced, why each practice-set size, figures wanted, glossary rows. Then return at most 150 words.
