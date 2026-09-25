# Drafter brief · S36-R1 (Task 2 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S36-R1`. Do not commit, push, fetch from the
web, or use GitHub tools. Write only the files named for you.

Read `claude.md`: "The one rule that matters", the whole authoring style sheet (§1–§11a), and
specification §1 and §4. Skip §12 and the rest of the specification. Read the two exemplar records
you are given before writing a word — they are the standard, and matching them matters more than
following the rules in the abstract.

Read `books/S36-R1/INVENTORY.md` (your concepts' rows: what each must cover, its Book 0 sections,
its sources, whether it is quantitative) and `books/S36-R1/READY.md` + `sources/INDEX.yml` (which
source files and citekeys are held). This is **a subject book**: its reader has read Book 0 (and Books 1-2, which this book does not need). Do not
re-teach what a Book 0 section in your row teaches; name it where the reader needs it (as the
exemplars do for earlier sections) and list it in `ground_floor_deps`. To see what a Book 0 section
actually says, read only its `definition` and `must_know` in `check/records/B0/<id>.yml`.

Write one YAML file per concept at `check/records/S36/<concept id>.yml` (subject `S36`, rung `1`,
`sequence` = the concept number), using `check/schema/example.concept.yml` as the template and
`check/schema/concept.schema.json` as the schema. `concept_deps` may name only earlier S36-R1
concepts.

For every concept the inventory marks quantitative, write `practice[]` on the ladder in `claude.md`
§7a — levels 1-3 mechanical on bare numbers, 4-6 applied to a real quantity with its unit, 7-8
diagnostic on a worked answer that is wrong, 9-10 transfer from a claim in words. How many is your
judgement, **between three and eighteen** (claude.md §7a), chosen from the technique and the number
of moves that compose in it. In this book the "numbers" of the ladder are mostly questions and
transcript lines: levels 1-3 classify a bare question or count bare words, 4-6 work on a line from
the running example's topic guide or transcript, 7-8 break a worked answer that is wrong, 9-10 turn
a claim in words into a guide question or test it against a transcript. The set must reach both ends of
the ladder, and say in one line in your notes why you chose the number. Prompts carry no hint of
the answer. Answers show every line. A problem quoting a real figure names its citekey in `refs`;
where no real figure exists, use bare numbers rather than inventing one.

For every factual claim, quote the exact words from the file in `sources/` that carry it, and put
the file and section in the locator. A quote that carries a number must state that number. If no
held file carries a claim, set `opened: false`, say in `verified.note` which instrument is needed,
and write the concept so it does not depend on the unopened claim — or leave the claim out.
Held for this book (`READY.md`, `INTAKE.md`, `sources/INDEX.yml`): `dejonckheere_vaughn_2019`,
`pope_ziebland_mays_2000`, `mays_pope_2000`, `green_britten_1998`, `mcmullin_2023`,
`icmr_ethical_guidelines_2017`, and three **OCR text layers** of scanned 1995 BMJ papers:
`kitzinger_1995`, `britten_1995`, `pope_mays_1995`. Read those three files' headers: the OCR dropped
the spaces between words, so a `quote` from them must be copied exactly as it stands in the file
(unspaced, OCR errors and all), and in the record's prose you write the words normally. List every
quote you take from an OCR file in your notes under "OCR quotes", with the page, so a person can
check it against the page image. Prefer the HTML-text sources where both carry a claim. BMJ papers
are free to read, not openly licensed: quote short phrases for audit, never reproduce a box or table.
Never quote a `[NOTE]` line or a header.

**Examples in this book.** Qualitative research has no numbers to invent, but it has quotations,
and an invented quotation presented as real data is exactly the fabrication this course forbids.
So: every interview exchange, topic guide or transcript excerpt you write is an **illustration you
made up**, and the prose says so the first time in each section ("a made-up exchange", "suppose you
are interviewing..."). Never attribute an illustrative line to a real study, and never quote a real
study's participants unless the line is in a held source file. One running setting, shared by
every batch so the book reads as one: **a district hospital NCD clinic in Chhattisgarh whose adult
patients with obesity stop coming back for follow-up; you want to know why.** Respondents speak
Hindi or Chhattisgarhi; the book writes their words in English and may say they were translated.
Speaker labels in transcripts: `I` for interviewer, `R1`, `R2`... for respondents (in a focus group
`R1`–`R8` plus `M` for moderator). A transcript excerpt is a ```` ```table ```` block (Speaker |
Words) or a quoted block, never aligned with spaces.

**Consent section (C07).** Teach the ICMR 2017 guidelines as they are stated in the held file. Do not
assert whether a learner's practice interview needs ethics committee review; state what the
guidelines say and route the reader to their own institutional ethics committee. Do not name the
Digital Personal Data Protection Act 2023 (not held; decision pending with Harsh).

**Scope.** Anything the inventory routes to S36-R2 (sampling strategies, saturation, thematic and
framework analysis, coding frameworks, COREQ, interviewer effects in hierarchy) or S36-R3 (mixed
methods designs) is named and routed in one line, not taught.

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
as in `check/schema/example.concept.yml` (file names `s36-r1-cNN-<what>.png`). Run
`python check/figures/draw.py --book S36-R1` to see that each spec passes; never draw by hand. **Do not edit
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
until blocking is zero for your records (other drafters are writing other S36 records at the same
time; ignore failures in files that are not yours). Recompute every practice answer in Python, not
by reading it. For every quote, confirm it is in the source file and states the number it is cited
for. Check each item of `check/SELFCHECK.md`.

Write your notes to `books/S36-R1/draft-notes-<your batch>.md`: records written, anything
unsourced, why each practice-set size, figures wanted, glossary rows. Then return at most 150 words.
