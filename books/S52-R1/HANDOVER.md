# S52-R1 handover (v1.0, 3 Oct 2026)

Book 6, *R, reproducibility engineering and data management · Rung 1*. 22 sections, 190 practice problems, 34
figures + 3 figure_notes (C06, C07, C21), 72 glossary rows (+4 second senses), PDF 322 pages (page_budget 240).
295 audit defects (30 errors; compression holes included), every one with a disposition and verified closed (two
closed by conductor decision: C10 terminal pointer, C22 journey heading). Build blocking 0. Source gate released
2 Oct 2026, `sources-provided` (Harsh supplied Herndon 2014, Bruford 2020, the NMC guideline, NHANES BMX_L/DEMO_L
with codebooks, and the typeset Broman & Woo). The first book with R code: every printed output is produced by the
code gate.

## Contract changes made in this book (Harsh's explicit instruction, 2 Oct 2026, "Add code support + code gate")
- ```` ```r ````, ```` ```output ````, ```` ```sh ```` fences (attributes `norun`, `error`, `file=`), verbatim
  monospace in HTML/docx/PDF, exempt from notation, caret, arithmetic, sentence and numbers-registry checks;
  compression tools treat a code block as one unit. `check/code_gate.py` + `check/code/run_chunks.R` rerun every
  block in a fresh Rscript per record and per practice item, inside a project built from `books/<ID>/code.yml`;
  `build.py --check` blocks on a mismatch (cached). Report: `books/S52-R1/TOOLING-CODE-GATE.md`.
- Shared sentence splitter (`build._sentences`) made code-aware (a sentence may open with a code span, a call, a
  picker or `!`; punctuation inside a code span never ends one); all 83 earlier compression files still validate.
- Notation layer pairs inline backticks left to right (the old pattern parked prose between two spans as code).
- CSS: ligatures off for all code (inline `<-` printed as an arrow); code block styles.
- Figure specs accept an opt-in `x_ticks` (figspec.py, draw.py, schema).
- Requires R in the sandbox: `apt-get install r-base-core r-cran-tidyverse r-cran-palmerpenguins` (CRAN is blocked;
  readxl, haven, here, renv come with the apt set). Without Rscript, records with code block the build.

## Decisions taken in this book
- Datasets (Harsh): palmerpenguins `penguins_raw.csv` (CC0) for examples and drills; NHANES 2021–2023 BMX_L joined
  to DEMO_L for C09, C17, C19, C22; every NHANES summary is unweighted and estimates nothing about the US population.
- Versions (Harsh): outputs from R 4.3.3, dplyr 1.1.4, tidyr 1.3.1, readr 2.1.5, ggplot2 3.4.4 etc.; newer
  behaviour only as `tidyverse_news_s52r1` states it.
- A penguin row is one bird's record in one nesting season; rows are counted as rows, never as penguins or nests.
- From C10 every session loads `library(dplyr, warn.conflicts = FALSE)` (glossed in C10; C06 teaches masking).
- C22 keeps the full `sessionInfo()` printout as the record of versions.
- C01 teaches three documented failures (the PHE statement never names Excel or a row limit; Herndon's journal
  article numbers are cited, not the working paper's: 71 country-years, "inappropriate weighting").
- Map amendment **S52-R2-A01** (iteration added to S52-R2 P1) accepted by Harsh and appended to
  `map/AMENDMENTS-v3.1.yml`; regular expressions refused.

## Not taught, and why
- How to open a terminal on the reader's computer: no held source (C07 says what a terminal is; C10, C21, C22 use one).
- RStudio's interface beyond what the held Carpentries/R4DS passages say (no pane positions or shortcut tables).
- Sample weights and survey design (S54); missing-data mechanisms (S15-R2); functions, Git, Quarto, DuckDB, form
  tools (S52-R2); renv and targets (S52-R3).

## Numbers and claims to re-check, with triggers
- Package versions and the "newer releases" list (C06, C21, front matter): at the next version, or when the sandbox R
  changes.
- Excel's date conversion of gene symbols "as reported in 2016" (C01, C15): if a current source on Excel's
  behaviour is held.
- NFHS-5 BMI cut-points (C12): when NFHS-6 reports are taken in.
- Excel for Mac's 1904 date system (C15): currency not checked.

## Series-wide notes for the handover (not this book's to fix)
- `check/figures/draw.py` checks specs before `{{n:}}` substitution while `build.py` checks after (S47-R1 used a
  book-local wrapper; here C14 avoided it with a `derived` entry). Fix the shared loader between rounds.
- The renderer mishandles LaTeX accents in `.bib` (`{\c{C}}`, ``{\`e}``): this book's entries were changed to UTF-8;
  `openintro_stats_4e` still carries `{\c{C}}etinkaya`.
- `check/compress/prepare.py` assemble leaves out `illustrations[]`, so cutters and cold readers never see worked
  examples held there; this book's cold read had them inserted by hand (v1 was void). Earlier books may have had
  the same blind spot.
- The Symbols page prints "10 ³" (superscript minus missing in the table face), every book.
- Subagents in this environment cannot write report files outside the repo; the conductor saved their reports.
