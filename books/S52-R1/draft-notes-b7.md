# Draft notes, b7 (C19, C20), 2 Oct 2026

## Records written

- `check/records/S52/S52-R1-C19.yml`, Checking the data in code. Derivable, quantitative, 13 practice problems,
  4 exercises (critique K02, design K01, retrieval, teaching), 5 retrieval items. One figure:
  `check/figures/s52-r1-c19-nhanes-row-counts.png` (+ `.spec.json`), rows after each step of the NHANES
  example (8860, 8860, 6064, 5970), from the record's table; checks `y[0] = y[1]` and `y[2] - y[3] = 94`.
- `check/records/S52/S52-R1-C20.yml`, Does shared code rerun? What studies found. Empirical, not quantitative,
  4 exercises (critique, interpretation, retrieval, teaching), 5 retrieval items. One figure:
  `check/figures/s52-r1-c20-reexecution-results.png`, Trisovic's RQ 4 table (success, error, time limit
  exceeded by run); checks the three row totals 7659, 7414, 8609.
- `books/S52-R1/numbers.yml`: added `nhanes_adults_rows` (6064), source C19 illustration 2. C20 uses the
  existing `trisovic_fail_initial_pct` and `trisovic_fail_cleaned_pct` in prose; C19 uses `bmx_rows`.

State at hand-back: `code_gate.py --check --no-cache` 0 failures on both; `build.py --check` =
`records 148 | clusters 9 | blocking 0 | warnings 253`, with no warning on C19 or C20 in `check_report.md`.
Figures drawn by `draw.py --book S52-R1 --out` scratch; only my two were copied in. I looked at both PNGs.

## Drill-set size (C19)

Thirteen. The technique has four moves (a `stopifnot()` test, a range, a key, a row count) and the
corrections after a failure. Each move has a trap that runs silently: `|` for `&`, limits taken from the
data's min and max, a missing value failing the check, a fix by row position, and a check deleted to let a
join through. Each trap gets its own diagnostic problem. The transfer band has two: a thesis sentence on the
NHANES data, and "the script ran without an error" said of the penguin file. Levels: 1, 2, 3, 3, 4, 5, 6, 7,
7, 8, 8, 9, 10.

## Sources and claims

- Every quote is in its source file and states the number it is cited for; the build's quote checks pass.
- C19's functions are cited to `rdocs_s52r1_base` (stopifnot) and `rdocs_s52r1_dplyr` (n_distinct, the
  join's `relationship` argument). The help page states stopifnot's NA rule only in code
  (`if(any(is.na(A)) || !all(A)) stop(...)`); the note says so. The gate outputs show the behaviour.
- The range limits (50 to 250 cm, 20 to 300 kg for adults; 1000 to 10,000 g for penguins) are stated in the
  text as decisions, not facts, set wide. No source is claimed for them. The NHANES codebook's "Range of
  Values" (79.1 to 200.7 cm) is quoted as describing the file, which agrees with C10's rule.
- C20: Trisovic's abstract (74%/56% failed) and table (25/40/56% success) are quoted separately with their
  own words, as the intake log and source header ask. The record shows by arithmetic that the table's rates
  equal success / (success + error) and says the held parts of the paper do not show how the abstract's
  figures were computed. It does not claim the abstract is wrong.
- "Commonest" claims were softened to what the text supports ("some of the most common execution errors,
  such as hard-coded path variables"; all setwd errors fixed; a significant jump from library errors).
- Peng is an author manuscript with fair-use terms; quoted in four short sentences only. Fig. 1 not held, so
  the spectrum is described from the body text.
- The RQ 10 three-package check is reported as Trisovic reports it, without a rate.
- Nothing unsourced that I know of. Nothing set `opened: false`.

## Unsure, for the conductor or auditor

1. C19 points to C13 (missing values) and C17 (joins) by description; both were not drafted when I wrote,
   so check the wording ("as the section on missing values taught", "as the section on reshaping and
   joining used them") matches what they do. C17 may not use the NHANES join in the same form.
2. C19 must-know: "dplyr warns only when IDs repeat in both tables" rests on the dplyr 1.1.4 help page
   (`relationship` default) and the gate output; newer dplyr may differ (not checked against
   `tidyverse_news_s52r1`).
3. C19's corrections use made-up dates (2026-10-02) in comments; the register story is said to be made up.
4. C20 `concept_deps` includes C19 (it is earlier); the prose does not lean on C19.
5. C20 says Trisovic's "most packages came from the social sciences": supported by the Background sentence
   and RQ 9's "most of the datasets are labeled 'social science'" (in a note).
