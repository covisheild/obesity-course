# S57-R1 figures, batch f1 (C01 to C05)

All drawn by `python check/figures/draw.py --book S57-R1`; `python check/build.py --check` shows no
blocking item in C01 to C05. Every PNG was opened and looked at after the last redraw.

## C01 · Learning is what lasts
- `s57-r1-c01-reversal.png` (drafter's, kept). Grouped bars, Roediger and Karpicke Experiment 2:
  recall after 5 minutes (83, 78, 71) against after 1 week (40, 56, 61) for SSSS, SSST, STTT. Data
  from the illustration's table; check `y[0] - y[2] = 12` (the 12-point lead at 5 minutes).

## C02 · Testing a teaching method
- `s57-r1-c02-md-and-sd.png` (drafter's, kept). Invented numbers, labelled as such: bars 58 and 66,
  band 58 to 74 = one SD of 16 above the comparison mean. Checks `y[1] - y[0] = 8`,
  `(y[1] - y[0]) / 16 = 0.5`.
- `s57-r1-c02-smd-and-spread.png` (new). The worked relationship SMD = 8 ÷ SD drawn as a curve from
  SD 8 to 16, through the text's two cases (SD 16 → 0.5, SD 8 → 1). Curve tied to the series, so
  it is checked through both points.

## C03 · Retrieval practice
- `s57-r1-c03-d-by-delay.png` (drafter's, kept). Signed d by delay: -0.52, 0.95, 0.83, from the
  table in the first illustration.
- `s57-r1-c03-classroom-effect-sizes.png` (drafter's; y axis set to 0 to 25 so ticks are whole
  counts). Agarwal 2021 counts 3, 18, 12, 16; check `sum(y) = 49`.

## C04 · Spacing
- `s57-r1-c04-best-gap.png` (drafter's; label moved beside the 350-day point). Cepeda's best tested
  gaps 1, 11, 21, 21 at 7, 35, 70, 350 days, with the lines gap = 0.2 × RI and gap = 0.05 × RI.
- `s57-r1-c04-review-window.png` (new). The calendar worked example: 42 days split into gap and
  retention interval as the gap's share goes from 20% to 30%. Curves `y = 42*x/(100 + x)` and
  `y = 42*100/(100 + x)`, each tied to its series (7 → 9.69, 35 → 32.3); check `y1[0] + y2[0] = 42`;
  reference line at 11 days (best gap tested for a 35-day retention interval). The 28-day self-study
  example is not drawn: its printed values (4.66, 6.45) come from rounded intermediates and miss the
  exact curve at two decimals.

## C05 · Rereading and highlighting
- `s57-r1-c05-sure-and-kept.png` (drafter's, kept). Rating expected against recall after 1 week:
  (4.8, 40), (4.2, 56), (4.0, 61). Caption says the x axis shows only part of the 1-to-7 scale.
  No second figure: Table 4 is letters, Fowler and Barker give no group numbers in the text.

No figure_notes needed. Deslauriers 2019 is not drawn anywhere in this batch.
