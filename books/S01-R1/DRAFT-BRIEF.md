# Drafter brief · S01-R1 (Task 2 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S01-R1`. Do not commit, push, fetch from the
web, or use GitHub tools. Write only the files named for you.

Read `claude.md`: "The one rule that matters", the whole authoring style sheet (§1–§11a), and
specification §1 and §4. Skip §12 and the rest of the specification. Read the two exemplar records
you are given before writing a word — they are the standard, and matching them matters more than
following the rules in the abstract.

Read `books/S01-R1/INVENTORY.md` (your concepts' rows: what each must cover, its Book 0 sections,
its sources, whether it is quantitative) and `books/S01-R1/READY.md` + `sources/INDEX.yml` (which
source files and citekeys are held). This is **a subject book**: its reader has read Book 0. Do not
re-teach what a Book 0 section in your row teaches; name it where the reader needs it (as the
exemplars do for earlier sections) and list it in `ground_floor_deps`. To see what a Book 0 section
actually says, read only its `definition` and `must_know` in `check/records/B0/<id>.yml`.

Write one YAML file per concept at `check/records/S01/<concept id>.yml` (subject `S01`, rung `1`,
`sequence` = the concept number), using `check/schema/example.concept.yml` as the template and
`check/schema/concept.schema.json` as the schema. `concept_deps` may name only earlier S01-R1
concepts.

For every concept the inventory marks quantitative, write `practice[]` on the ladder in `claude.md`
§7a — levels 1-3 mechanical on bare numbers, 4-6 applied to a real quantity with its unit, 7-8
diagnostic on a worked answer that is wrong, 9-10 transfer from a claim in words. How many is your
judgement, between three and eighteen, chosen from the technique. The set must reach both ends of
the ladder, and say in one line in your notes why you chose the number. Prompts carry no hint of
the answer. Answers show every line. A problem quoting a real figure names its citekey in `refs`;
where no real figure exists, use bare numbers rather than inventing one.

For every factual claim, quote the exact words from the file in `sources/` that carry it, and put
the file and section in the locator. The quote must state the number it is cited for. If no held
file carries it, set `opened: false`, say in `verified.note` which instrument is needed, and write
the concept so it does not depend on the unopened claim. Two papers are **not held** yet: Hall 2008
(*Int J Obes* 32:573, energy content of adipose and lean tissue) and Hall et al. 2012 (*AJCN* 95:989).
Use the held papers (Hall 2011 Lancet, Hall & Guo 2017, Thomas 2013, Rosenbaum & Leibel 2010,
Polidori 2016, FAO/WHO/UNU 2004, ICMR-NIN 2020 brief note, NSS Report 594, FTC Gut Check) wherever
they carry the claim. The source files mark which passages are verbatim; never quote a `[NOTE]` line
or a header. Several are NIH author manuscripts: cite the paper, quote the held text.

Never tell the reader to open a file in `sources/`. Name the instrument by its own title and give
the public URL from `check/references/library.bib`.

A `boundary` must-know point names a limit of the technique — when the tool stops being trustworthy
and what the reader should do then. Never a table-of-contents entry ("This section gets you...").

Prose fields are literal blocks (`|`), never folded (`>`). Columns go in a ```` ```table ```` block.
Display arithmetic goes in a ```` ```working ```` block, never indented. Write exponents as `10^7`
and logarithms as `log10`; no markup. Introduce an operator in words beside its symbol the first
time. Use `illustrations` (a list) where one illustration does not do the teaching. A figure you
would want: name it in your notes with its numbers; do not draw it.

**Glossary:** do not edit `prose/GLOSSARY.md`. Put every new term's proposed row (same columns as
that file; read its header and a few rows) in your notes file under "Glossary rows". Check that the
term is not already glossed there; if it is, use the existing sense.

Before you hand back, check your own work as the auditor will. Run `python check/build.py --check`
until blocking is zero for your records (other drafters are writing other S01 records at the same
time; ignore failures in files that are not yours). Recompute every practice answer in Python, not
by reading it. For every quote, confirm it is in the source file and states the number it is cited
for. Check each item of `check/SELFCHECK.md`.

Write your notes to `books/S01-R1/draft-notes-<your batch>.md`: records written, anything
unsourced, why each practice-set size, figures wanted, glossary rows. Then return at most 150 words.
