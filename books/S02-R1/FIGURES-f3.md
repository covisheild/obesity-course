# Figures, batch f3 · S02-R1-C13 to C17

Drawn by `python check/figures/draw.py --book S02-R1` (45 drawn, 0 problems); `python check/build.py
--check` blocks nothing (0 blocking; no warning names C13–C17). Every PNG below was opened and looked at.
Only `figures:`, `figure_note` and `derived` entries were edited; no prose changed.

## C13 · A random variable and its distribution

- `s02-r1-c13-village-distribution.png`: paired bars from the illustration's table. P(X = x) next to
  the survey's relative frequency for each household size. Checks: `sum(y1) = 1.0`, `sum(y2) = 1.0`,
  and P(X ≥ 6) = `y1[4] + y1[5] + y1[6] = 0.3`. Caption corrected: the drafter's "sees none of five
  other sizes" was wrong. The survey misses four sizes (2, 3, 6, 7).
- `s02-r1-c13-rounding-density.png`: **redrawn**. The drafter's step chart drew the strip as a second
  line lying on the density, with its markers scattered along zero. Now: the flat density drawn as a
  bare line. Two `areas`: the whole rectangle (`equals: 1`) and the strip from 0 to 0.02
  (`equals: 0.2`). A `ref` at exactly 0.02 is labelled "no width, area 0".

## C14 · Expectation

- `s02-r1-c14-surplus-balance.png`: the four bars of the surplus distribution, with dashed lines at
  E[X] = 70 and at the wrong unweighted average 100. Checks: sum 1, the weighted sum = 70,
  `mean(x) = 100`. The drafter's label floated at no line and was offset 60 pt from its point.
- `s02-r1-c14-week-expected.png`: expected running total 70·x beside the highest (500·x) and lowest
  (−300·x) possible totals. It was **blocked** because 3,500 and 2,100 were not stated. It now has
  `derived` 3500 = 7×500 and 2100 = 7×300. The bound lines have `marker: none`. Fits check all
  three series.
- `s02-r1-c14-dependent-days.png` (new): the table of dependent days. Its fit, `y = 140 − x`, is
  drawn. `refs` at E[X] = 70 and E[Y] = 70 cross on the line. Both expectations are checked by
  weighted sums.
- `s02-r1-c14-logged-shift.png` (new): the true (70·x) and logged (190·x) expected totals. Checks:
  `y2[2] − y1[2] = 840` and `= 7*120`. Derived 840 = 1330 − 490.

## C15 · Variance

- `s02-r1-c15-difference.png`: the two error distributions from the table. Added checks that the
  weighted squares give Var = 50 for one reading and 100 for the dal.
- `s02-r1-c15-variance-parts.png` (new): each error's square times its probability, the parts of the
  weighted sum. Checks: `sum(y1) = 50`, `sum(y2) = 100`, and `sum(y2) = sum(y1) + sum(y1)`. Derived
  25 = 100×0.25 = 400×0.0625.
- `s02-r1-c15-days.png`: the fits 300·√n and 300·n are now **drawn**. The old picture joined the
  √n points with straight segments, which hid the curve. The y axis now starts at 0.
- `s02-r1-c15-average-day.png` (new): the error in the average day. Fits 300/√n (points 300, 150,
  100, 75) and a flat 300. Derived 150 = 600/4, 100 = 900/9 and 75 = 1200/16.

## C16 · Following a derivation

- `s02-r1-c16-two-readings.png`: the table's two readings of ΔEB. Both fits are now drawn and
  labelled as the printed equation with ΔEB = 500 and ΔEB = −500. The caption already says the
  weight axis does not start at zero.
- `s02-r1-c16-line-six.png` (new): line 5's constant rate, −500/3500 lb a day (fit checked against
  the plotted −0.143). The area from day 0 to day 140 is shaded, with `equals: −20` for the change
  from 180 to 160. Derived 20 = 180 − 160.

## C17 · Four kinds of equation

- No figure. The `figure_note` is reworded: the section sorts equations and sets out an entry. It
  works no relationship of its own, and a plot of one equation would teach that equation, not the
  sorting. A Schofield-line figure was considered and rejected: the record states no weight at
  which to draw it, and ICMR-NIN's "overestimate by 10–12%" does not say which base the percentage
  is taken on.

## Caveats

- In `dependent-days` and `two-readings`, the legend names are the table headers ("y (kcal/day)",
  "… (lb)"), because `from_table` takes them from there. They are accurate but terse. Changing them
  would mean changing the prose table.
