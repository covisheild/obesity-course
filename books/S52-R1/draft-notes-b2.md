# Draft notes, batch b2 (S52-R1 C04-C06), 2 Oct 2026

## Records written

- `check/records/S52/S52-R1-C04.yml` Vectors, types and NA (derivable, quantitative)
- `check/records/S52/S52-R1-C05.yml` Functions and arguments (derivable, quantitative)
- `check/records/S52/S52-R1-C06.yml` Packages: where they come from and which version you have (derivable, quantitative)

State at hand-back: `code_gate.py --check --record` 0 failures for each (13, 13 and 9 sessions);
schema-valid; `build.py --check` = `records 138 | clusters 9 | blocking 0 | warnings 251`, with no
warning naming C04, C05 or C06. Figures drawn to scratch and only my two PNGs + `.spec.json` copied
into `check/figures/` (`s52-r1-c04-body-mass-na.png`, `s52-r1-c05-three-averages.png`); I looked at
both images. C06 has a `figure_note`.

## Drill sets

- C04: 11 (levels 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10). Four moves (build/convert, type after mixing,
  NA spreading, is.na plus brackets), and three diagnostics because each trap (text compared as
  text, "NA" in quotes, `x == NA`) runs without an error.
- C05: 11 (1-7, 8, 8, 9, 10). Diagnostics cover the three ways a call goes wrong: silently by
  position (`mean(3750, 3800, 3250)` gives 3750, via `trim` taken as 0.5), by an error
  (`na.rm = true`), and by rounding too early.
- C06: 7 (1, 2, 3, 5, 7, 8, 9). Three simple moves; inventory asked for a small set.
- Prompts that ask the reader to predict output carry `norun` blocks so no output is printed in
  the prompt. Diagnostic prompts show the colleague's code with its gate-filled output, on purpose.

## Datasets and numbers

- Worked examples use the first ten values of `Body Mass (g)` and `Flipper Length (mm)` from
  `penguins_raw.csv`, typed into `c()` (data frames and `read_csv()` come later). I checked all
  ten of each against the file with readr (3750 3800 3250 NA 3450 3650 3625 4675 3475 4250;
  181 186 195 NA 193 190 181 195 193 190). Only 3750, 3800 and 344 have a quote in the source
  file (the CSV lines and the help page's "344 rows"); the other values are not quotable from
  `horst_2020_palmerpenguins.txt`. The auditor can recheck them by reading the file.
- Made-up material, each said to be made up in its sentence: the clinic register weights, the
  haemoglobin values, school heights, BMI lists, district names.
- C06 uses `{{n:r_version}}`, `{{n:dplyr_version}}`, `{{n:readr_version}}`. I did not add keys to
  `numbers.yml`. C06 states R 4.6.1 (June 2026) and dplyr 1.2.0 (February 2026) once each, quoted
  from `r_intro_manual` and `tidyverse_news_s52r1`. If C21 repeats them they should become keys.
- No NHANES used (not one of my sections).

## Sourcing

- Every definition reference is to a held file, with a quote the build finds. No `opened: false`.
- What I relied on but could not quote from a held source, and how I handled it:
  - Picking by position with `[ ]`: R-intro's positive-index passage is not held; the definition
    cites the general index-vector sentence and the code output shows the behaviour (noted in the
    reference).
  - `typeof()`, `length()`, `sum()`, `search()`, `nrow()`, `R.version.string`, `n_distinct()` are
    shown working; only `n_distinct`, `search` (R-intro) and `packageVersion` have held help text.
    No prose claim about them goes beyond what their output shows.
  - "R prints 19 rather than 19.0, because it drops a final zero" (C05 practice 4): an observation
    of the printed output, not cited.
  - "copy a block three times, write a function" (C05 must-know): stated as this book's advice,
    no source.
- Excluded on purpose: any claim about newer R shipping its own `penguins` (version not
  established, log-a finding 2); any description of what `stats::filter()` does (its help page is
  not held), so C06 says only that stats has its own, different `filter()`.

## Unsure of

- C04 says the fourth penguin's mass is NA "in the file" and that reading the file in a later
  section gives "the same ten numbers": true for readr's default `na` (checked), but C09 must not
  change the default in a way that alters this.
- C06 illustration 1 uses `here::here()`, `show_col_types = FALSE` and `nrow()` ahead of C07, C09
  and C08, each glossed in one clause and pointed forward. If the reconcile pass prefers no
  forward use, the call can be replaced by the `n_distinct()` example alone (practice 5 and 7 use
  the same call).
- Skill refs: C04 exercise uses K02 (keep raw untouched, changes in code), C05 and C06 use K01.
