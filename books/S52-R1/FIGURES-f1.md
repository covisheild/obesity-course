# Figures, batch f1 · S52-R1-C01 to C08

All PNGs drawn by `python check/figures/draw.py --book S52-R1`; `figspec.verify` clean for every figure
below; `python check/build.py --check --subject S52` shows no block in C01–C08 (the five blocks it
reports are stale PNGs in C16–C22, the other planner's range, mid-run). Each PNG opened and looked at.

## C01 · When data change silently (3 figures)
- `s52-r1-c01-phe-missing-results.png` (kept): PHE's missing results by day, from table block 1.
  Checks `sum(y) = 15841`, `y[5]+y[6]+y[7] = 11968`.
- `s52-r1-c01-years-counted.png` (new): Reinhart–Rogoff high-debt years counted, 110 → 96 → 71
  (table block 0's values; categories shortened as literal x because the table's long step names
  overlapped). Check `y[0] - y[2] = 39`, derived 39 = 110 − 71.
- `s52-r1-c01-growth-three-ways.png` (new): average growth 2.2 (all data), 1.9 (spreadsheet error
  alone), −0.1 (all problems, published); negative bar from a zero line. Check `y[0] - y[1] = 0.3`.

## C02 · Installing R; console and script (1 figure, figure_note removed)
- `s52-r1-c02-three-bmi-answers.png` (new): the three printed BMI answers, 0.0028125 / 72 / 28.125,
  as bars labelled with what was typed; the first is too small to show. Check `y[2] / y[0] = 10000`
  (the prose's "factor of 10,000"). A log scale was tried and dropped: bars on a log axis block,
  and a scatter gave fractional x ticks.

## C03 · Objects and names (1 figure, figure_note removed)
- `s52-r1-c03-bmi-stored-value.png` (new): bmi at each print, 28.125 / 28.125 / 28.90625, showing the
  stored value not following the changed weight until the line is rerun. Checks `y[1] = y[0]`,
  `y[2] = 74 / 1.6^2`.

## C04 · Vectors, types and NA (1 figure, kept)
- `s52-r1-c04-body-mass-na.png`: first ten body masses in kg, gap at penguin 4 (NA); table block 0.
  Check `y[6] = 4.675`.

## C05 · Functions and arguments (1 figure, kept)
- `s52-r1-c05-three-averages.png`: 3392.5 / 3769.444 / 3650 g, table block 0. Check `y[0]*10 = 33925`.

## C06 · Packages — figure_note kept
Outputs are messages, one count and version strings; a chart would redraw text.

## C07 · Project folder and paths — figure_note kept
The only quantities are 344 rows when a path works; a failed read is an error, not 0 rows, so a
rows-per-attempt chart would be false.

## C08 · Tidy data and the data frame (2 figures, figure_note removed)
- `s52-r1-c08-visit-weights.png` (new): the six rows of the tidy `visits` table as bars, dashed mean
  line at 22.36667 kg. Checks `sum(y) = 134.2`, `sum(y) / 6 = 22.36667`. Value labels left off
  (they collided with the mean line); the caption lists the six weights.
- `s52-r1-c08-rows-and-ids.png` (new): 344 rows against 190 distinct Individual IDs. Check
  `y[0] - y[1] = 154`, derived 154 = 344 − 190.

No prose was edited. Changes per record: `figures:` entries added (C01, C02, C03, C08) and
`figure_note` removed where a figure now exists (C02, C03, C08).
