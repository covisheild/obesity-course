# Figures · S02-R1 batch f1 (C01–C06)

Drawn by `python check/figures/draw.py --book S02-R1`, all verified by `figspec.verify` and the
build (`check/build.py --check`: 0 blocking). I looked at every PNG as an image. There are no
`figure_note`s in this batch, because every section has at least two figures.

## C01 · Reading the symbols in a methods section
The drafter's `s02-r1-c01-sigma-week.png` read a daily-balance table that the compression pass
removed. Its values (0.5, −0.3 … 1.6) are no longer in the text, so the figure could not be kept.
I deleted it and its `.spec.json`.
- `s02-r1-c01-sigma-terms.png`: Σ[i = 1 to 4] 2i and Σ[i = 1 to 4] 3i drawn as their terms,
  as grouped bars at i = 1…4. Checks: `sum(y1) = 20`, `sum(y2) = 30`.
- `s02-r1-c01-feedback-line.png`: Polidori Equation 4, ΔEI = −k_P × ΔBW, with k_P = 100. The
  line runs from ΔBW = −3 to 0, and there is a point at (−1, 100). Check: the curve
  `y = -100*x` is tied to the series and passes through both points.

## C02 · The derivative
- `s02-r1-c02-settling.png`: kept as drafted. It plots the average rate against step h, and
  the averages close in on 20. Check: fit `y = 20 + 5*x` at all 8 table rows.
- `s02-r1-c02-chord-tangent.png` (new): S(t) = 5t² on [1, 3], with the chord from 2 to 3
  (slope 25) and the tangent at 2 (slope 20). Check: the curve is tied to the points (2, 20)
  and (3, 45).
- `s02-r1-c02-weighings.png`: now also draws the one-day chord from day 12 to day 13 (0.6 kg a
  day, tied to the data) and the line between the five-day averages (80.0 at day 2 to 79.5 at
  day 12, −0.05 kg a day). Checks: both means, and `y[13] - y[12] = 0.6`. The value 0.7 is
  derived.

## C03 · Differentiation rules
- `s02-r1-c03-weight-curve.png`: now points plus the exact curve W(t) = 90 − 0.2t + 0.001t²
  (tied to the points), with tangents at day 0 (slope −0.2) and day 60 (slope −0.08, through
  81.6). Both slopes come from the W′ column.
- `s02-r1-c03-rate-line.png`: W′(t) = −0.2 + 0.002t, fit at all 6 rows, with a new reference
  line at 0.

## C04 · e, ln, proportional change
- `s02-r1-c04-base-e.png` (new): 2^t, e^t and 3^t on [−0.5, 0.5], all through (0, 1), with
  the line 1 + t touching e^t. The slopes 0.693, 1 and 1.099 appear in the key.
- `s02-r1-c04-two-exponentials.png`: kept. Two drawn fits are checked at all 6 rows.
- `s02-r1-c04-ratio-steps.png` (new): the yearly gains 50.0, 25.0 and 12.5 as bars. Checks:
  both ratios are 0.5, and the gains sum to 87.5.

## C05 · Integral of a rate
- `s02-r1-c05-net-rate-line.png`: rebuilt with `areas`. The area from 0 to 30 is +4500 and
  the area from 30 to 50 is −2000, each checked as a signed integral. The fit
  `y = 300 - 10*x` is checked, plus the two 2500 identities.
- `s02-r1-c05-average-rate.png` (new): the same line, with the average value of 50 as a
  reference line and the rectangle 50 × 50 shaded. Checks: its area equals 2500, and
  (300 + (−200))/2 = 50.

## C06 · Antiderivatives and the fundamental theorem
The drafter's figure read a table that compression removed. I rebuilt it from literal values
that the level-10 practice answer states (730/2190 and 526.6/921.7).
- `s02-r1-c06-plus-c.png` (new): t² and t² + 5 (tied curves), with parallel tangents of
  slope 4 at t = 2. Check: the gap is 5 at t = 0 and at t = 3.
- `s02-r1-c06-halving-deficit.png` (new): D(t) = 730e^(−0.693t) on [0, 2] against a steady
  730. The first-year area of 526.6 and the strip of 203.4 between the curve and 730 are both
  checked as integrals. The values 365.1, 182.6 and 203.4 are derived.
- `s02-r1-c06-steady-and-halving.png`: the totals 730x and 1053.4(1 − e^(−0.693x)), each tied
  to its points at years 0, 1 and 3, with a reference line at 1053.4.

## Judgement calls a reviewer may want to look at
- C01 feedback line: the range down to −3 kg is the model's straight line, not a range the
  paper reports. The 3 in "−3" is borrowed from the ΔF = −3 kg practice problem.
- C04 ratio-steps is close to a small table drawn as bars. I kept it because the halving is
  the section's point.
- Figures where two tangent or curve styles share a colour family are readable, but the
  palette cannot give two free curves the same style.
