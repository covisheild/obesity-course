# Draft notes, batch b3 (S52-R1 C07, C08, C09)

Drafter b3, 2 Oct 2026. Records written:

- `check/records/S52/S52-R1-C07.yml`: project folder, working directory, absolute and relative paths, `here()`.
- `check/records/S52/S52-R1-C08.yml`: data frame and tibble, the three tidy rules (Wickham 2014), Broman and Woo's
  data-entry rules, what one row of the penguin file stands for.
- `check/records/S52/S52-R1-C09.yml`: CSV as plain text, `read_csv()` and its column report, `na`, `col_types`,
  `problems()`, MD5 checksum to show reading leaves the file alone, `read_excel()`, `read_sav()`, `read_xpt()` on
  NHANES BMX_L, with one figure (missing values per body-measure column).

Every output block was filled by `check/code_gate.py --write`; `--check` passes on all three (0 failures).
`check/build.py --check`: blocking 0. The warnings left on these records are sentence-length ones, fixed where shown.
The figure `s52-r1-c09-nhanes-missing.png` was drawn by `draw.py --book S52-R1` and looked at: four bars, 106, 361,
389, 670, axis from zero.

## Drill sets

- C07: 10. Building a path is one move, so the mechanical band is short (3). The weight is on the diagnostic
  band (a `setwd()` that stops; a script that writes over `data-raw/` and changes the row count on the second run)
  and the transfer band (moving the project to a new folder; showing a cleaned file is disposable by checksum).
- C08: 10. Two moves (build and inspect a data frame; judge a layout against the rules), each applied to the
  penguin file, with diagnostics on backticked names and a text blood-pressure column, and transfers on counting
  units (344 rows, 190 IDs, 304 species-island-ID combinations).
- C09: 10. Several arguments compose (`na`, `col_types`, `range`, other readers), so every band has two or three.
  The two diagnostics are real traps: `.default = col_double()` wiping out IDs, and `na = "-99"` replacing the
  default list (the penguin file then shows 0 missing sexes instead of 11 and 15 text columns).

Non-code arithmetic in practice answers (C08 means 22.83333, 104, 66.5, 19.1; 110 + 114 + 120 = 344; C09
8860 − 106 = 8754) was recomputed in Python; each also matches the gate's R output.

## Unsourced, or sourced only by the code's own output

- Help pages not held, so what these functions do is shown by gate-filled output only, never cited: `tibble()`,
  `glimpse()` (used from tibble, not dplyr), `nrow()`, `ncol()`, `dim()`, `unique()`, `table()`, `paste()`,
  `sapply()`, `colSums()`, `getwd()`, `dir.create()`, `dir.exists()`, `list.files()`, `tools::md5sum()`,
  `readLines()`, `writeLines()`, `readxl_example()`, `cols()`/`col_double()` (readr vignette held, not quoted).
  The concepts are derivable, so this is a warning-level debt, not a block.
- KoboToolbox, ODK and REDCap are named in C09 only as field data tools taught at the next rung (map P5); no
  source is cited for what they do.
- The Excel and SPSS examples use files that ship inside readxl (`deaths.xlsx`) and haven (`iris.sav`), not
  penguins or NHANES: the project holds no .xlsx or .sav file. The record says they are package examples and not
  health data.
- `read_dta()` (Stata) from the inventory row is not taught: its help page is not held.

## Things I am unsure of

- **Code gate drops line breaks in cli messages.** readr's column report prints as
  `Rows: 3 Columns: 3── Column specification ──...` and `...to quiet this message.# A tibble: ...`; readxl's
  "New names" list runs into the tibble the same way. A real console puts each on its own line. This is in
  the gate (`check/code/run_chunks.R` message capture), not in the records; once fixed, `--write` refills the
  blocks and no prose changes. Reported in `notes-for-others-b3.md`.
- The parse error in C08 practice 7 prints in the gate's form (`Error: <text>:1:20: unexpected symbol`); an
  interactive console words it differently.
- C09 says `problems()` row 3 counts the header line as row 1. That is what readr 2.1.5 printed here; the held
  help page does not say it.
- In C08 the claim that `N1A1` names two different birds rests on the rows (an Adélie on Torgersen and a Gentoo
  on Biscoe carry it). How many birds the file covers is left open, as the help page does not say.
- C07 introduces the terminal, `cd` and `Rscript` in one paragraph, to show `here()` working from `code/`. If C02
  or C21 introduces the terminal more fully, the reconcile step may move or shorten this.
