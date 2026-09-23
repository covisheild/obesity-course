# S01-R1 figure plan, C06 to C10

Run 23 September 2026 (PIPELINE.md, "Figure plan"). Only the `figures:` / `figure_note` fields of
C06 to C10 were added, at the end of each record. No prose was changed. The specs pass
`figspec.verify`. `draw.py --book S01-R1` draws all 10 book figures with 0 problems (checked in a
scratch directory, so the C01 to C05 PNGs were left alone). `build.py --check` shows 0 blocking. I
looked at each PNG and fixed its layout through the spec.

| Section | Figures | File |
| --- | --- | --- |
| C06 | none. `figure_note`: the section states no numbers, so a drawn case would need invented values | - |
| C07 | static rule vs Hall's dynamic model, 100 kg man, years 0, 1 and 3 | `check/figures/s01-r1-c07-static-vs-dynamic.png` |
| C07 | Thomas cohort: the static-rule line over 64.8 days vs the measured loss | `check/figures/s01-r1-c07-thomas-shortfall.png` |
| C08 | daily deficit each claim needs if all fat, vs the cohort's average deficit of 1,439 | `check/figures/s01-r1-c08-claims-vs-deficit.png` |
| C09 | the appetite slope, 100 kcal/day per kg lost, reaching 800 at 8 kg | `check/figures/s01-r1-c09-appetite-slope.png` |
| C10 | none. `figure_note`: an argument laid out as premises, whose only numbers are C09's | - |

## Known errors kept out of the figures (DEFECTS.md)

- **Item 42 (C07).** The text says 20.1 lb measured, but 27.6 − 7.4 = 20.2. The figure plots the
  measured point as `derived 27.6 - 7.4` = 20.2 and checks `y2[-1] = 27.6 - 7.4`. It prints neither
  20.1 nor 20.2: the label says "7.4 lb short of the paper's 27.6 lb". If the audit finds that the
  paper reports 20.1, the spec needs a look.
- **Item 48 (C08).** The text calls 1,439 "the largest" deficit. The figure labels it "cohort's
  average deficit, supervised" and checks `7000 / 1439 = 4.864489229`.
- **Item 56 (C09).** The text says appetite outweighs expenditure "more than three times". The
  figure draws only Polidori's slope (`fit y = 100*x`). It does not set the 800 kcal (at 8 kg lost)
  against the 300 to 400 kcal (at a 10% loss) as bars, because those two match only at 80 kg. The
  correct ratios are declared as checks: `y[-1] / 400 = 2` and `y[-1] / 300 = 8/3`, so 2 to 2.7
  times. The caption keeps the two bases apart.
- **Item 61 (C09).** The y-axis says "extra eating", not "wanting to eat".
- **Items 64 to 68 (C10 contradicts C06).** Neither section has a figure, so nothing encodes the
  contradiction.

## Layout fixes made after viewing

- C07 static vs dynamic: the dynamic series and the drawn static relation were both red. I
  reordered the series so the dynamic model is blue and the static rule is red throughout, and
  moved the plateau label off the line.
- C07 Thomas: the label crossed the dashed line twice. I moved it below the line, beside the
  measured point.

## Open

- C07 static vs dynamic joins the dynamic model's three stated points with straight segments. The
  paper's curve between them is not held here, and the legend says "points the paper states".
- C08 does not show glycogen's energy per kilogram, because no sourced figure exists (item 52).
  The 3 kg bar is labelled "mostly glycogen and water".
