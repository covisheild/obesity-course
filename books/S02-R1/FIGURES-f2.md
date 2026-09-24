# Figures, batch f2 · S02-R1-C07 to C12

Drawn by `python check/figures/draw.py --book S02-R1` (45 drawn, 0 problems); `python check/build.py --check`
blocks on nothing (0 blocking; no figure warnings for C07–C12). Every PNG was opened and looked at.
Only `figures:` changed in each record; no prose was touched. No `figure_note` was needed.

## C07 · A differential equation

- `s02-r1-c07-three-rules.png` (drafter's spec, fixed). The illustration's table: static rule, ε = 20 and ε = 30,
  over 1095 days. Changed from a line chart with undrawn fits to points with each exact solution drawn through
  them. Check: three `curves` tied to their series (`100 - 480*x/7716.18`, `100 - 24*(1 - exp(-x/385.809))`,
  `100 - 16*(1 - exp(-x/257.206))`), each passing through every table point. The drafter's spec blocked on
  257.206; it and 16 are now under `derived` (7716.18/30, 480/30).
- `s02-r1-c07-forward-steps.png` (new). Practice problems 3–5: forward steps of size 1 for dy/dt = 6 − 0.5y
  from y = 4 (4, 8, 10, 11) against the exact 12 − 8e^(−0.5t) (9.06 at t = 2), plus the family member from
  y = 20, and a reference line at y = 12, where the rate is zero. Check: curves over [0, 3]. The step polyline
  is the Euler path.
- `s02-r1-c07-thirty-day-steps.png` (new). Practice problem at level 6: 30-day steps (98.13379, 96.41269,
  94.82542) against the curve formula (95.01 at day 90) and the static line (94.40). Check: both curves are
  the record's own formulas; 60 derived as 30 + 30.

## C08 · Equilibrium

- `s02-r1-c08-settling-point.png` (drafter's, unchanged). Flat intake meets expenditure 15 kg down for slope 20
  and 10 kg down for slope 30. Check: three `fit`s.
- `s02-r1-c08-approach.png` (drafter's, redrawn). Now points with exact curves `15*(1 - exp(-x/385.809))` and
  `2.5*(1 - exp(-x/64.3015))` through the table, a reference line at 15 kg, and lines at the halving times,
  day 44.57 and day 267.4. Check: curves tied to their series.
- `s02-r1-c08-rate-zero.png` (new). The right side of the man's equation against W: with ε = 20 it is 80 at
  72 kg, 0 at 76 and −80 at 80 (stability); with ε = 0 it stays at −480 (no equilibrium). Check: `fit`s
  `-480 - 20*(x - 100)` and `-480 - 0*(x - 100)`; reference lines at W* = 76 and at zero.
- `s02-r1-c08-set-point-crossing.png` (new). Set point model: intake −300 − 100x meets expenditure 20x at
  2.5 kg down. Check: two `fit`s, and `y1[1] = y2[1]` at x = −2.5; 200 and 50 derived.

## C09 · Critical points

- `s02-r1-c09-cubic-critical-points.png` (drafter's, unchanged). f(x) = x³ − 3x on [−2, 3]: a local maximum
  at −1, a local minimum at 1, the overall maximum 18 at the end. Check: `fit` through the table.
- `s02-r1-c09-least-squares-valley.png` (drafter's, unchanged). S(m) = 0.40 + 5(m − 70.6)² through the table.
- `s02-r1-c09-level-not-turning.png` (new). g = x³ and g′ = 3x² on [−2, 2]: the slope touches zero at 0 without
  changing sign. Check: curves tied to both series; 8 and 12 derived.
- `s02-r1-c09-valley-sharpness.png` (new). The rise in S against the step: 5h² (five readings, S″ = 10) against
  20h² (20 readings, S″ = 40). A 0.4 kg step costs 0.80 against 3.2. Check: curves tied to series. The
  five-reading points are taken from the table (1.20 − 0.40, 0.60 − 0.40), so the curve checks the table.

## C10 · Vectors

- `s02-r1-c10-energy-parts.png` (drafter's, unchanged). 12 + 81 + 60 = 153. Check: `sum(y) = 153`.
- `s02-r1-c10-meal-sum.png` (new). Snack, biscuit and meal energy by nutrient. Checks: sums 153, 133 and 286,
  and the meal's bars are exactly the snack's plus the biscuit's, one check per nutrient. The biscuit and
  meal products are derived.

## C11 · Matrices

- `s02-r1-c11-schofield-columns.png` (drafter's, unchanged). The XC table as two lines. Check: two `fit`s.
- `s02-r1-c11-column-view.png` (new). Bw column by column: 65 × slope plus 1 × intercept for each equation.
  Checks: `y1 = 65*15.057`, `y1 = 65*11.472`, and the sum equals each entry of Bw exactly.

## C12 · Redundant columns

- `s02-r1-c12-energy-weighted-sum.png` (drafter's; checks added). Energy against 4P + 9F + 4C on y = x. Four
  checks were added so that each x is recomputed from its item's grams.
- `s02-r1-c12-tee-not-weighted-sum.png` (drafter's; y-range added for label room). The weights from adults
  1 and 2 miss adult 3 by 3. Check: `y1[2] - y2[2] = 3`.
- `s02-r1-c12-three-weightings.png` (new). The three made-up scores (energy only; 4, 9, 4 on the grams; half
  and half) are equal on all four items. Checks: eight checks recompute each bar from the table's grams and
  energy.

## Caveats

- Point values not in any table (C07 steps; the C08 and C09 new figures) are literal `series` lists. Each one
  is stated in the prose or derived under `derived`, and the checker ties it to a drawn formula.
- An exact-identity `check` (`a = b`) is used rather than `a - b = 0`. A zero on the right is compared at
  integer precision (±0.5), which would hide small errors.
