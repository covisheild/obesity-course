# Draft notes, batch b1 (S52-R1 C01-C03), 2 Oct 2026

## Records written

- `check/records/S52/S52-R1-C01.yml` (empirical, not quantitative). One figure:
  `check/figures/s52-r1-c01-phe-missing-results.png` (+ `.spec.json`), drawn by `draw.py` from the
  record's PHE table (block 1); checks `sum(y) = 15841` and the last three days = 11968.
- `check/records/S52/S52-R1-C02.yml` (derivable, quantitative, 10 problems). `figure_note`.
- `check/records/S52/S52-R1-C03.yml` (derivable, quantitative, 10 problems). `figure_note`.

Code gate `--check`: 0 failures on all three. `build.py --check`: blocking 0 overall at my last run;
one warning left on my records (a 28-word sentence inside a quoted model sentence, C01 exercise 3).

## Drill-set sizes

- C02, 10: the technique has several moves (operators, order of operations, brackets, comments,
  reading an error, units in code), each needs its own mechanical problem, and the diagnostic band
  needs one silent-wrong case (107.3 kg) and one error case (missing `#`).
- C03, 10: assignment, overwriting, stale objects, naming rules and units in names are separate
  moves; L7 (name reused) and L8 (case) are the two diagnostics; L9-L10 are corrections and a unit
  mislabelled in a name.

## Decisions and deviations the conductor should check

1. **C01 name changed** from "When analysis is done by hand: four documented failures" to "When
   data change silently: three documented failures". The inventory row lists only three cases
   (gene names, Reinhart-Rogoff, PHE); no fourth held source carries a documented failure. And
   "done by hand" is false for PHE: the statement calls it an "automated process". The shared
   thread is written as "the change was silent and came to light only later", which all three
   sources support.
2. C01 cites `herndon_2014_cje` (article) for all figures and "inappropriate"; the "reproducible
   code" sentence is cited to `herndon_2013_wp322` only, as log-d requires. The record says the
   spreadsheet slip alone moved 2.2% to 1.9% (Table 5) so the case is not overstated.
3. C01 never says Excel or row limit for PHE; Bruford is cited for SEPT1/MARCH1 only; SEPT2 is
   Ziemann's.
4. Practice problems use made-up clinic numbers (said to be made up) and the first three rows of
   `penguins_raw.csv` (3750/3800/3250 g; flippers 181/186/195 mm), cited to
   `horst_2020_palmerpenguins`. No data file is read yet (reading arrives in C09).
5. C02's script is a plain r block named `bmi_arithmetic.R` in the prose, not a `file=` block and
   not `code/analysis.R`: the project folder is not taught until C07. `source()` was avoided
   because `source(echo = TRUE)` deparses the code and drops comments.
6. `{{n:ziemann_affected_pct}}` and `{{n:r_version}}` used in prose.

## Unsourced or unsure

- Statements that the RStudio console prints parse errors as `Error: unexpected input in "72 ÷"` /
  `unexpected symbol in "BMI of"` were verified by piping the lines into an interactive
  `R --vanilla -q` session (R 4.3.3), not from a held source. The gate prints these errors in a
  different layout (`Error: <text>:1:4: unexpected input` plus the caret lines), so the prose
  mentions both. See notes-for-others-b1.md.
- C03 "heights between roughly 1 m and 2 m" for adults is a stated plausibility range, not sourced.
- Nothing set `opened: false`; every quote was found in the held file and states its number.
