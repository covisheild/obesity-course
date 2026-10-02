# Draft notes, batch b8 (C21, C22), 2 Oct 2026

## Records written

- `check/records/S52/S52-R1-C21.yml`: Top to bottom in a fresh session, with one command (derivable,
  quantitative). Two illustrations: (1) a script that runs in the session and stops under `Rscript`
  with "object 'penguins_raw' not found" because the reading line lived only in the console, then the
  fixed script; (2) `rm(list = ls())` leaves packages attached (`search()`), `source()` runs in the
  current workspace, `set.seed()` shown with `sample(344, 5)`, and a whole script that writes two files
  to `output/` and ends with `sessionInfo()`. `figure_note` instead of a figure (the evidence is two
  runs' printed outputs).
- `check/records/S52/S52-R1-C22.yml`: One dataset, end to end (`journey: true`, quantitative false).
  NHANES 2021-2023 BMX_L joined to DEMO_L. Four illustrations: question, terms (NCHS Data User
  Agreement quoted), MD5s, dictionary table, README; building the steps in the session, leading with
  the real failure met while drafting (`filter(RIDEXPRG != 1)` kept 1093 of 6064 adults because
  RIDEXPRG is NA for 4930; fixed with `is.na(RIDEXPRG) | RIDEXPRG != 1`, 6023); the full
  `file=code/analysis.R` script and `sh` `Rscript code/analysis.R`; the rerun from nothing (`rm -r
  output`, rerun, `cmp` of the CSV: identical), what it does not show, what S52-R2 adds. Figure:
  `s52-r1-c22-bmi-quartiles.png` (scatter of the three quartiles by gender, from the illustration's
  table; checks on the two interquartile widths 10.3 and 7.5). Exercises: retrieval, build (K01),
  critique (K02), teaching (health secretary). `common_misreading` set.

## Drill set

- C21: ten problems (levels 1-10, one each). The technique is one test (a fresh run) with three parts
  (seed, empty workspace, attached packages), which the mechanical band covers once each; the weight
  is on diagnostic (hidden object giving a plausible wrong mean, 4716 g vs 4202 g; `source()` as a
  false test) and transfer (a thesis "fully reproducible" claim; "same table every time" tested by two
  fresh runs and `cmp`). Stated in `practice_note`.
- C22: none (journey; quantitative false per the inventory).

## Checks run

- `code_gate.py --write` then `--check` on both: 0 failures (12 sessions). Every output block is
  gate-written; prose numbers were read from the filled outputs.
- `build.py --check`: blocking 0 overall at the last run (records 148); C21 and C22 have no blocking
  and, after fixes, no sentence or grade warnings.
- Non-code arithmetic recomputed: 152 + 68 + 124 = 344; 165 + 168 + 11 = 344; 2680 + 3249 = 5929;
  6064 - 41 = 6023; 6064 - 1093 = 4971; 6023 - 5929 = 94; 34.7 - 24.4 = 10.3; 32.4 - 24.9 = 7.5.
- Every definition quote is found by the build; the five C22 illustration-number quotes and the four
  NHANES phrases quoted in prose, plus Trisovic's "often related to missing files or incomplete code",
  were checked as substrings of the source files by script (the build does not check quotes under
  `illustrations[]`, only under `illustration`).
- Figure drawn with `draw.py --book S52-R1 --out` into scratch, and only my PNG and `.spec.json` copied
  to `check/figures/` (so other batches' figures were not touched). Looked at as an image.

## Consistency choices

- Script conventions match C17/C19: `left_join(..., relationship = "one-to-one")`; named `stopifnot()`
  range checks with C19's limits (height 50-250 cm, weight 20-300 kg). Numbers keys used:
  `bmx_rows`, `demo_rows`, `nhanes_adults_rows`, `trisovic_fail_initial_pct`, `penguins_rows`,
  `r_version`, `dplyr_version`, `readr_version`, `here_version`. No key added to `numbers.yml`.
- Column name `gender` (the codebook's label for RIAGENDR, codes 1 Male, 2 Female).
- C21's Trisovic wording follows C20 ("failed to complete without error").
- README in C22 follows C10's form (blockquote) and names the dictionary `data-raw/nhanes_dictionary.csv`
  and both outputs, as b4 asked.

## Unsure / for the auditor

1. `sessionInfo()` output in C21 and C22 prints the sandbox's platform lines ("Running under: Ubuntu
   24.04.5 LTS", BLAS paths, locale C.utf8, time zone UTC). The prose reads only the R and package
   versions from it and says a reader's own lines will differ.
2. The C22 rerun compares only the CSV byte for byte; the prose says a figure is compared by looking,
   because image bytes can differ with nothing visible changed. That sentence is general, not sourced.
3. Excluding the 41 pregnant participants is framed as the question's choice, with no biological claim.
4. A figure I drew first (`s52-r1-c22-row-counts`) duplicated C19's row-count figure; I moved its PNG and
   spec out of `check/figures/` into my scratch dir (I had created them minutes earlier) and replaced it
   with the quartile figure.
5. C22 lists `S52-R1-C18` in `concept_deps`; it blocked once while C18 was not yet on disk and passes now.
6. `sample()` has no held help page; its job is cited through the Random help page's See Also line
   ("'sample' for random sampling with and without replacement"), in a reference note.
