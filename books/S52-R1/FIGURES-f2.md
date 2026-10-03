# Figure plan, batch f2 · S52-R1 C09–C15

All figures drawn by `python check/figures/draw.py --book S52-R1` (0 problems); `python check/build.py --check`
blocks on nothing. I looked at every PNG listed here. No prose was edited. Only `figures:`, `figure_note` and `derived` changed.

| Section | File | What it shows | Check that holds it |
|---|---|---|---|
| C09 | s52-r1-c09-nhanes-missing.png (kept) | NA counts in BMXWT/BMXHT/BMXBMI/BMXWAIST: 106, 361, 389, 670 | from_table block 0; `y[2] = 389` |
| C09 | s52-r1-c09-camp-minus-99.png (new) | Camp heights as read with no `na` declared: 128, -99 (a bar below zero), 131 | `min(y) = -99`; `min(y[0], y[2]) = 128` (the shortest measured child once -99 is NA) |
| C10 | s52-r1-c10-ids-vs-rows.png (new; replaces figure_note) | 344 rows, 190 distinct Individual IDs, 344 distinct Species + Sample Number pairs | `y[0] = y[2]` (the pair picks out one row each) |
| C11 | s52-r1-c11-rows-left.png (respecified) | Rows left at each filter step: 344, 176, 85 | Literal data now, so the first bar reads "all rows", not "all penguins" (reconciler note). The caption no longer says "the second example's pipe" |
| C11 | s52-r1-c11-na-test.png (new) | `== NA` returns 0 rows and `is.na()` returns 2 | numbers from the two printed tibbles (0 × 17, 2 × 4) |
| C12 | s52-r1-c12-bmi-cut-points.png (kept) | BMI to 1 dp against the 18.5 and 25.0 cut-points | from_table block 1; refs |
| C12 | s52-r1-c12-cm-vs-m.png (new) | BMI from cm against BMI from m for the four patients | drawn `fit: y = 10000*x` passes all four points |
| C13 | s52-r1-c13-rows-kept.png (kept) | Rows kept: 344, 342, 333, 34 | from_table block 0 |
| C13 | s52-r1-c13-missing-by-column.png (new) | colSums(is.na()) for the columns with gaps; Comments 290 dominates | numbers from the printed colSums output |
| C13 | s52-r1-c13-code-999.png (new) | Register weights 62, 999, 71, 58, 999, with dashed lines at 437.8 and 63.7 | `mean(y) = 437.8`; `(y[0]+y[2]+y[3])/3 = 63.7` |
| C14 | s52-r1-c14-island-counts.png (fixed) | fct_infreq() order: 168, 124, 52 | `sum(y) = 344`, plus a `derived` 344 = 168+124+52 (draw.py does not substitute `{{n:}}`, so it refused this figure before) |
| C14 | s52-r1-c14-species-by-island.png (new) | Grouped bars of the species × island two-way table, zeros visible | from_table block 1; the sum of all cells = 344 (derived) |
| C15 | s52-r1-c15-days-after-first.png (new; replaces figure_note) | Days after the first visit: 0, 12, -34 (signed bars) | numbers from the printed time difference |
| C15 | s52-r1-c15-age-days-years.png (new) | age_days against age_years for the three patients; patient 1 labelled 31.0 printed, 30 completed years | drawn `fit: y = x/365.25` passes 31.0, 36.6, 20.1 at 1 dp |

No figure_notes remain in C09–C15.

Caveat for the conductor: `draw.py` checks numbers against the record text without the `{{n:key}}`
substitution that `build.py` applies, so a number stated only through a key fails in draw.py and passes in the build.
C14's derived entry works around this. The proper fix belongs in `figspec.reader_text`.
