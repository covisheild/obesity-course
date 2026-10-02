# Drafter brief · S52-R1 (Task 2 of PIPELINE.md)

Repository `/home/claude/work/obesity-course`, branch `book/S52-R1`. Use ABSOLUTE paths. Do not commit,
push, fetch from the web, or use GitHub tools. Never `rm` anything in the repository. Write only the
files named for you. Scratch work goes under `/tmp/claude-0/draft-<your batch>/` with your own names.

Read `claude.md`: "The one rule that matters", the whole authoring style sheet (§1–§11a, including the new
paragraph on code fences next to the ```working/```table rules), and specification §1 and §4. Skip §12 and the
rest of the specification. Read `books/S52-R1/TOOLING-CODE-GATE.md` (how code blocks and the code gate work).
Read the two exemplar records before writing a word: `check/records/S55/S55-R1-C02.yml` (a derivable
concept with a drill set) and `check/records/S55/S55-R1-C06.yml` (an empirical concept). They are the
standard for structure, voice and density; matching them matters more than following rules in the abstract.
Neither contains code: this book is the first that does.

Read `books/S52-R1/INVENTORY.md` (your concepts' rows: what each must cover, Book 0 sections, sources,
quantitative or not), `books/S52-R1/SOURCE-GATE.md` (what is held, Harsh's decisions), the intake logs
`books/S52-R1/intake/log-a.md`, `log-b.md`, `log-c.md`, `log-d.md` (findings that override the inventory), and
`sources/INDEX.yml`. Read the header of every source file you cite. To see what a Book 0 section says, read
only its `definition` and `must_know` in `check/records/B0/<id>.yml`; name it where the reader needs it and
list it in `ground_floor_deps`; do not re-teach it.

**The reader** is a medical graduate training in community medicine in India who has never programmed and
has read Book 0 only. Examples come from that world (a survey of school children's heights, a clinic
register, a thesis dataset) and from obesity and nutrition, the series' subject.

Write one YAML file per concept at `check/records/S52/<concept id>.yml` (subject `S52`, rung `1`,
`sequence` = the concept number), from `check/schema/example.concept.yml`, valid against
`check/schema/concept.schema.json`. `concept_deps` may name only earlier S52-R1 concepts.

## Code: the rules every batch follows (so the book reads as one)

- Code goes in ```` ```r ```` blocks; its printed result in the ```` ```output ```` block that follows; a shell
  command in ```` ```sh ````. Attributes: `norun` (shown, never run: `install.packages()`, a personal path),
  `error` (the chunk is meant to stop with an error), `file=code/analysis.R` (the block is a script file the
  reader saves). **Never type an output block.** Write the r blocks, then run
  `python /home/claude/work/obesity-course/check/code_gate.py --write --record <your file>` to fill every output,
  then `--check` to confirm. Read the filled output and make your prose agree with it, number for number.
- Each record's prose fields run as ONE fresh R session in render order: load packages and read data in the
  record itself before using them (a fresh session knows nothing from an earlier section). Each `practice[]`
  item runs as its OWN fresh session, prompt then answer: a prompt that shows code must contain every line its
  answer needs (library calls, reading the file).
- The reader's project, as the gate builds it (`books/S52-R1/code.yml`): `data-raw/penguins_raw.csv`,
  `data-raw/BMX_L.xpt`, `data-raw/DEMO_L.xpt` at the project root. Read data with
  `read_csv(here::here("data-raw", "penguins_raw.csv"))` (or `haven::read_xpt(...)`). Folders: `data-raw/`
  (never written to), `code/`, `output/`; the script is `code/analysis.R`; the one command is
  `Rscript code/analysis.R`, run from the project root. Write outputs only to `output/`.
- **Datasets (Harsh's decision):** worked examples and drill problems use `penguins_raw.csv` (the raw file, read
  from `data-raw/`; never the `palmerpenguins::penguins` object, since newer base R ships its own `penguins`).
  NHANES 2021–2023 (`BMX_L` body measures joined to `DEMO_L` demographics on `SEQN`) is used in C09 (reading
  a .xpt with haven), C17 (the join), C19 (checks) and C22 (the build); any summary of it is unweighted and
  estimates nothing about the US population (survey weights are another book's subject, S54): say so
  wherever an NHANES summary appears. Small made-up tibbles are fine for one-line drills (say they are made up).
- Style: the native pipe `|>`; `<-` for assignment; snake_case names; one verb per line in a pipe; spaces
  round operators; the tidyverse style guide (`tidyverse_style`). Load packages with `library(readr)`,
  `library(dplyr)` etc. rather than `library(tidyverse)` unless the section is about the tidyverse itself.
- Versions: outputs come from R `{{n:r_version}}` and the packages in `books/S52-R1/numbers.yml`; newer releases
  exist. Do not claim how a newer version behaves unless `tidyverse_news_s52r1` says so.
- Code is not prose: it is exempt from the notation layer and sentence checks, and `{{n:key}}` is never
  substituted inside code. Numbers you state in PROSE that come from a code output must match the output
  exactly; a number reused in another section goes in `numbers.yml` as a key (add it, with `source:` naming the
  record and chunk that prints it) and is written `{{n:key}}` in prose.
- Units in prose: height in cm, weight in kg, BMI in kg/m^2 (written that way; the build typesets it).

## Sources and claims

For every factual claim, quote the exact words from the file in `sources/` that carry it (never a `[NOTE]`
line or a header) and put the file and section in the locator; the quote must state the number it is cited
for. What a function does is cited to the version-matched help pages (`rdocs_s52r1_<package>`), not to R4DS or
a website. R4DS 2e and the typeset Broman & Woo article are CC BY-NC-ND: quote briefly, never adapt their text,
code, tables or figures; write your own examples. Prefer `broman_woo_2018_tas` (version of record) to the
manuscript `broman_woo_2018`; prefer `herndon_2014_cje` to the working paper. If no held file carries a claim,
set `opened: false`, say which instrument is needed, and write the concept so it does not depend on it.
Known traps (from intake): the PHE statement never names Excel or a row limit; Bruford 2020 names SEPT1 and
MARCH1 and Excel, not SEPT2 and not "spreadsheet"; Herndon's journal article says "inappropriate weighting"
and differs from the working paper in two numbers (log-d.md); Trisovic's 74%/56% "failed" and its table's
success rates are on different bases; R4DS's third tidy rule differs from Wickham 2014's (cite Wickham 2014);
Data Carpentry and Broman & Woo differ on how to store dates (do not merge them into one rule).

## Practice, retrieval, figures

For every quantitative concept, write `practice[]` on the ladder in `claude.md` §7a: levels 1-3 mechanical
(one line on a toy vector or a three-row tibble), 4-6 applied to the book's dataset with units and labels kept,
7-8 diagnostic on worked code that is wrong (it runs and gives a plausible number, or it stops with an error:
use the `error` attribute), 9-10 transfer from a claim in words (a sentence from a thesis or meeting turned into
code, run, and followed by what the result does not establish). Between three and eighteen, chosen from the
technique; reach both ends of the ladder; say in one line in your notes why that number. Prompts carry no hint
of the answer. Answers show the code and its gate-filled output. A problem quoting a real figure names its
citekey in `refs`.

Every section carries at least one `retrieval` item. Every section gets at least one figure (drawn only by
`check/figures/draw.py` from a `spec` reading your own ```table block, never by hand and never a ggplot
screenshot), or one line in `figure_note` saying why a figure would teach nothing the prose does not. A
section on plotting may draw, via the figure system, the same data its code plots (the table of counts or
values copied from a gate-filled output). A `boundary` must-know point names a limit of the technique.

If another batch's section needs a change, do not edit it: write the note to
`books/S52-R1/notes-for-others-<your batch>.md` (section, what, why).

## Before you hand back

Run `python check/code_gate.py --check --record <file>` for each record (0 failures), and
`python check/build.py --check` (takes about 2 minutes; use a timeout of at least 600 s) until blocking is zero
for your records. Recompute every non-code practice answer in Python or R, not by reading it. For every quote,
confirm it is in the source file and states the number it is cited for. Check each item of `check/SELFCHECK.md`.
Write `books/S52-R1/draft-notes-<your batch>.md` (records written, drill-set sizes and why, anything unsourced,
anything you are unsure of). Then return at most 150 words.
