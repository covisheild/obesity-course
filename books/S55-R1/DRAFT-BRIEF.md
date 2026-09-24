# Drafter brief · S55-R1 (Task 2 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S55-R1`. Do not commit, push, fetch from the
web, or use GitHub tools. Write only the files named for you.

Read `claude.md`: "The one rule that matters", the whole authoring style sheet (§1–§11a), and
specification §1 and §4. Skip §12 and the rest of the specification. Read the two exemplar records
you are given before writing a word — they are the standard, and matching them matters more than
following the rules in the abstract.

Read `books/S55-R1/INVENTORY.md` (your concepts' rows: what each must cover, its Book 0 sections,
its sources, whether it is quantitative) and `books/S55-R1/READY.md` + `sources/INDEX.yml` (which
source files and citekeys are held). This is **a subject book**: its reader has read Book 0 (and Books 1-3, which this book does not need). Do not
re-teach what a Book 0 section in your row teaches; name it where the reader needs it (as the
exemplars do for earlier sections) and list it in `ground_floor_deps`. To see what a Book 0 section
actually says, read only its `definition` and `must_know` in `check/records/B0/<id>.yml`.

Write one YAML file per concept at `check/records/S55/<concept id>.yml` (subject `S55`, rung `1`,
`sequence` = the concept number), using `check/schema/example.concept.yml` as the template and
`check/schema/concept.schema.json` as the schema. `concept_deps` may name only earlier S55-R1
concepts.

For every concept the inventory marks quantitative, write `practice[]` on the ladder in `claude.md`
§7a — levels 1-3 mechanical on bare numbers, 4-6 applied to a real quantity with its unit, 7-8
diagnostic on a worked answer that is wrong, 9-10 transfer from a claim in words. How many is your
judgement, **between three and eighteen** (claude.md §7a), chosen from the technique and the number
of moves that compose in it. In this book the "numbers" of the ladder are mostly research questions: for C02,
levels 1-3 mark the population, exposure and outcome in a bare question, 4-6 write a one-sentence
question from an obesity topic in the running setting, 7-8 break a worked one-sentence question that is
wrong, 9-10 turn a line from a protocol or a meeting into one sentence and say what it still cannot
answer; for C08, levels 1-3 score a bare candidate on each item of the sheet, 4-6 total and rank a short
list, 7-8 the diagnostic where a high total hides a zero on the who-is-waiting item, 9-10 a candidate
proposed in words to score, rank and reject in one line. The inventory row suggests sizes. The set must reach both ends of
the ladder, and say in one line in your notes why you chose the number. Prompts carry no hint of
the answer. Answers show every line. A problem quoting a real figure names its citekey in `refs`;
where no real figure exists, use bare numbers rather than inventing one.

For every factual claim, quote the exact words from the file in `sources/` that carry it, and put
the file and section in the locator. A quote that carries a number must state that number. If no
held file carries a claim, set `opened: false`, say in `verified.note` which instrument is needed,
and write the concept so it does not depend on the unopened claim — or leave the claim out.
Held for this book (`READY.md`, `INTAKE.md`, `sources/INDEX.yml`; read each file's header first):
`blackstone_2012` (chapter 4 is blocks 13-18; the earlier blocks are S36's), `jhangiani_2019_methods`,
`cdc_ss1978_lesson1`, `aslam_emmanuel_2010`, `morgan_peco_2018`, `ratan_2019`, `ioannidis_2016_useful`,
`ioannidis_2014_waste`, `van_noorden_2017`, `golosovsky_lariviere_2021`, and the optional
`farrugia_2010` (its running text has spaces inside words and fails the quote check: quote its boxes
only, or not at all) and `nowroozzadeh_2019`. Van Noorden 2017 is all rights reserved and Ioannidis
2014, Morgan 2018, Farrugia and Nowroozzadeh carry no open licence: short phrases for audit, never a
table, box or chart reproduced. Never quote a `[NOTE]` line or a header.

**Reference kinds.** Derivable concepts need at least one reference of kind `textbook`; the held
textbooks are `blackstone_2012`, `jhangiani_2019_methods` and `cdc_ss1978_lesson1`. Journal methods
papers are `primary`. **Never relabel a source's kind to satisfy the build** (handover §7, Book 3): if a
concept has no textbook that carries it, say so in your notes and the conductor decides.

**Not held, so not stated as fact:** the NMC postgraduate regulations (whether an MD thesis is
required, who assigns it); the Companies Act and CSR rules (C07 names company CSR funds only as a
word, with no statement about the law); Chalmers & Glasziou 2009 and the "85% of research is wasted"
figure (do not state it, even though Ioannidis 2016 repeats it; you may say Ioannidis argues much
clinical research is not useful, in his words); Patsopoulos 2005 and any claim about citation by study
design. **The map's O3 sentence** ("most descriptive cross-sectional studies are never cited") is not
supported by the held sources and is never written as fact: C06 teaches what the measurements show,
with every figure carrying its database, cohort year and citation window, quoted, and says the
Larivière–Sugimoto figures reach us through a news feature and a book not held. O1's "most are made
by accident" is not a measured share either: C01 names the routes and asserts no proportion.

**Examples in this book.** Every candidate question, protocol line, meeting remark, scoring sheet
and person in an example is an **illustration you made up**, and the prose says so the first time in
each section ("suppose...", "a made-up list"). Never attribute an illustrative question to a real
study, and never invent a statistic, a prevalence or a citation count; where a number is needed for a
drill, use a score on the sheet, not a fact about the world. One running setting, shared by every
batch so the book reads as one: **you are a postgraduate in community medicine at a medical college
in Chhattisgarh, and you must propose a first research question on obesity; your guide, your
department and a district NCD programme officer are the people around you.** Topics for candidates
come from that setting (school children, NCD clinic patients, urban slum households, a district
screening camp, college students' meal timing), stated as made-up.

**Scope.** Anything the inventory routes to S55-R2 (the four assets, the portfolio ladder and its
costs, documented systematic searching, the funding sequence, grant writing) or S55-R3 is named and
routed in one line, not taught. The reader's final build is the list of ten scored questions (C08).

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
as in `check/schema/example.concept.yml` (file names `s55-r1-cNN-<what>.png`). Run
`python check/figures/draw.py --book S55-R1` to see that each spec passes; never draw by hand. **Do not edit
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
until blocking is zero for your records (other drafters are writing other S55 records at the same
time; ignore failures in files that are not yours). Recompute every practice answer in Python, not
by reading it. For every quote, confirm it is in the source file and states the number it is cited
for. Check each item of `check/SELFCHECK.md`.

Write your notes to `books/S55-R1/draft-notes-<your batch>.md`: records written, anything
unsourced, why each practice-set size, figures wanted, glossary rows. Then return at most 150 words.
