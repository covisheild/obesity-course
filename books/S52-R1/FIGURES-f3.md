# Figures, batch f3 · S52-R1-C16 to C22

All figures drawn by `python check/figures/draw.py --book S52-R1`; `python check/build.py --check --subject S52`
reports blocking 0. Every PNG was opened and looked at. Only `figures:` entries were edited; no prose changed.
Captions that cited "the first illustration" (C16, C18) or "the example" (C19) now name what they show.

## C16 Summaries by group
- `s52-r1-c16-mass-by-species.png` (kept, caption fixed): mean body mass by species from the summary table. Bars from zero.
- `s52-r1-c16-share-grouped-vs-all.png` (new): the eight species x sex counts as percentages two ways, still grouped by species (48.0 ...) and via `.by` (21.2 ...). Checks: each species' within-shares sum to 100; all eight ungrouped shares sum to 100 (to rounding).
- `s52-r1-c16-iqr-by-method.png` (new, from table block 1): IQR of the nine heights by Book 0 / type 7 / type 6: 10, 7, 10. Checks: 136 - 126, 134 - 127, type 6 = Book 0.

## C17 Reshaping and joining
- `s52-r1-c17-nhanes-join-rows.png` (kept): row counts of the two NHANES files and the join. Checks: 11933 - 8860 = 3073; joined = BMX rows.
- `s52-r1-c17-visit-means.png` (new): patients 101 and 102 fall at every visit while the mean of the weights recorded rises at visit 2 (84.8, 87.1, 82.4). Checks: each mean recomputed from the listed weights (3, 2, 3 values). Patient 103 (no visit 2) is not drawn; caption and alt say so.

## C18 Plotting with the grammar of graphics
- `s52-r1-c18-mass-histogram.png` (kept, caption fixed): the eight bin counts. Check: they sum to 342.
- `s52-r1-c18-quartiles-by-species.png` (new): Q1, median, Q3 per species as quantile() prints them (x = 0.25, 0.5, 0.75); the numbers each box is drawn from. Non-zero axis is correct for positions. Label marks the shared 3700 median.

## C19 Checking the data in code
- `s52-r1-c19-nhanes-row-counts.png` (kept, caption fixed): rows after each step. Checks: join kept 8860; 6064 - 5970 = 94.
- `s52-r1-c19-median-before-after.png` (new): clinic median BMI 26.2 as typed vs 23.7 after the two corrections. Derived 2.5 = 26.2 - 23.7.
- `s52-r1-c19-missing-measures.png` (new): adults with no height 67, no weight 81, either 94. Checks: 94 = 6064 - 5970; derived 54 = 67 + 81 - 94 lacking both (inclusion-exclusion, printed in the caption).

## C20 Does shared code rerun?
- `s52-r1-c20-reexecution-results.png` (kept): Trisovic table counts. Checks: row totals 7659, 7414, 8609.
- `s52-r1-c20-success-share-two-bases.png` (new): success share over finished files (0.2486, 0.3984, 0.5608, the table's basis) vs over all files with a result (derived 0.1243, 0.1985, 0.1836). Checks: each ratio recomputed from the table's counts.

## C21 Top to bottom in a fresh session
- figure_note kept: the evidence is two printed runs of one script; the only counts (island counts) are already C14's figure.

## C22 One dataset, end to end
- `s52-r1-c22-bmi-quartiles.png` (kept): BMI quartiles by gender. Checks: widths 10.3 and 7.5.
- `s52-r1-c22-pregnancy-filter.png` (new): 6064 adults; first try `RIDEXPRG != 1` keeps 1093; `is.na(...) | != 1` keeps 6023. Checks: 6064 - 6023 = 41; 1093 = 1065 + 28; 6064 - 1093 = 41 + 4930; 41 + 1065 + 28 + 4930 = 6064.
- `s52-r1-c22-rows-per-step.png` (new, from table block 1): 8860, 8860, 6064, 6023, 5929. Checks: join kept rows; drops of 41 and 94.

## Outside this batch
- `draw.py --book S52-R1` reports C14 as NOT DRAWN: its `check: "sum(y) = 344"` uses 344, which appears only as `{{n:penguins_rows}}`. draw.py verifies the raw record, before number substitution; build.py verifies after it, so the build passes and the existing C14 PNG is not redrawn. The C14 planner, or a fix in draw.py (apply numbers before verifying), should handle it.
