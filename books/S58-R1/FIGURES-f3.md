# Figure plan, batch f3 (S58-R1-C13 to C18)

Drawn by `python check/figures/draw.py --book S58-R1` (29 figures drawn, 0 problems);
`python check/build.py --check` ends `blocking 0` (no item for C13-C18; C18's caption block is
closed). Every PNG below was opened and looked at, and converted to greyscale (PIL
`convert("L")`; colour-over-grey copies `cmp-*.png` in `/home/claude/scratch-s58-fig-f3/`).
Only `figures:` entries were edited; no prose touched. Record backups from before the edits are
in the same scratch folder.

**Greyscale, every two-series figure.** Primary and secondary merge in grey exactly as RECONCILE
says (both bars render the same mid-grey). Each two-series figure now reads without colour:
labels drawn directly on the bars or at the line ends via `labels`, plus the marker shape where
the kind has markers. The legend that draw.py always adds for n > 1 stays and is useless in
grey; the direct labels carry the series. Looked at in grey: all readable.

## C13 · The one-pass test
- figure_note kept: a procedure and a two-sentence comparison already set out as a table; no
  numbers to draw.

## C14 · A figure makes one claim
- `s58-r1-c14-urban-rural.png` (bars from zero, value labels): NFHS-5 urban vs rural, women
  33.2/19.7, men 29.8/19.3. Added the direct labels "urban"/"rural" above all four bars. Alt text
  now says where each bar sits in its pair. Grey: readable from the labels.
- H-14-2 (indicator numbering) left alone: the illustration now quotes the rows as "88." and
  "89." and the caption matches the text's own "after" caption.

## C15 · Choosing the mark
- `s58-r1-c15-large-errors.png` (bars from zero): first experiment, judgments 60/40, large
  errors 22/78. Checks `sum = 100` for each series and the per-judgment ratio 5.3. Added the
  direct labels "judgments"/"large errors" over all four bars. Grey: readable.
- New: `s58-r1-c15-pie-errors.png` (single series, bars from zero): second experiment, large
  errors on position 12%, on angle (pie) 88%. Checks `sum(y) = 100` and `y[1]/y[0] = 7.33`.
  Every number is in illustration 2's working; 88% being angle is confirmed by the record's
  Cleveland-McGill quote ("Eighty-eight percent of the large errors occurred for the angle
  judgments").

## C16 · Show the data
- `s58-r1-c16-equal-bars.png` (bars from zero, from table 1): three means of 30. Caption now
  opens with the finding.
- `s58-r1-c16-every-value.png`, redrawn (H-16-3, H-16-2): was three joined line series over
  adult 1-8, which joined unrelated people and let ward 1 and ward 3 dots overlap (45/44,
  15/16). Now one unjoined scatter series of all 24 values, ward by ward (x 1-8, 9-16, 17-24),
  each ward lowest first, labels "ward 1/2/3" over the blocks, dashed mean line at 30. Checks:
  each ward's slice sums to 240, mean 30. x positions 9, 12, 13, 14, 18, 20 are under `derived`
  (8 + 1 and so on). Single colour, so nothing merges in grey. Caption says "fairly evenly" (as
  the text now does) and that the dots are unjoined because the adults are not pairs.
- **For the conductor:** the text says each ward's adults are "numbered 1 to 8". The figure
  keeps that order inside each ward, but its x ticks run 0-25 because x is numeric. A true strip
  chart (one jittered column per ward) still needs categorical x for scatter (RECONCILE b6).

## C17 · Honest axes
- New: `s58-r1-c17-fuel-economy-change.png` (single series, bars from zero): Tufte's fuel-economy
  chart, 52.8% change in the data against 783% as drawn. Check `y[1]/y[0] = 14.8`.
- `s58-r1-c17-lie-factor-by-start.png` (points on a log axis plus the drawn fit
  y = 20.6/(20.6 - x), ref 1.05): added value labels, because draw.py prints log ticks as 10^0
  and 10^1. Caption now opens with the finding. Grey: dots and the dashed fit differ by form.
- `s58-r1-c17-bars-from-zero.png`: added the direct labels "NFHS-4"/"NFHS-5" over all four bars.
  Checks: differences 3.4 and 4.0.
- `s58-r1-c17-line-from-18.png`: added "women"/"men" labels at the line ends (circle and square
  markers). The axis starts at 18, and the caption says so.
- New: `s58-r1-c17-change-bars.png` (single series, bars from zero): the rise itself, 3.4 and
  4.0 percentage points, the text's "third" honest redraw. Checks `y[0] = 24.0 - 20.6`,
  `y[1] = 22.9 - 18.9`.
- Not drawn: the "fourth" redraw (ratio bars from 1 on a log axis, 1.685 and 0.593). draw.py
  has no bars from 1, and dots need numeric x. Also not drawn: C17's own truncated-axis figure
  (RECONCILE b7), which `verify` blocks by design.

## C18 · Decoration that does no work
- `s58-r1-c18-where-they-looked.png` (paired bars from zero): Bateman eye-tracking shares,
  Holmes 40/27/13/20 and plain 78/0/0/22. **The block is fixed**: "2010" is gone from the caption
  because the text never gives the year. The caption now opens with the finding ("The pictures
  took looking time") and says why the plain bars are 0. Direct labels "Holmes"/"plain" sit on
  the first and last pairs. Grey: readable.
- No second figure. The cleaned-up NFHS-5 bar the illustration describes would need 24.0 and
  22.9, and those are only `{{n:}}` keys in C18.
