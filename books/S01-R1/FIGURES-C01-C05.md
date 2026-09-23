# S01-R1 figure plan, C01 to C05

Run 23 September 2026, PIPELINE.md "Figure plan". Only `figures:` / `figure_note` were added to
the five records. No prose was changed. `draw.py --book S01-R1` drew all figures with 0 problems,
and `build.py --check` shows 0 blocking. I looked at every PNG and fixed the label placement
(C02 lipid line, C05 stores) through the spec.

| Section | Figures | File(s) in `check/figures/` |
| --- | --- | --- |
| C01 | 0, `figure_note` | the only number is the 90 kg total, and the section deliberately does not split it |
| C02 | 2 | `s01-r1-c02-energy-density-bars.png`: 37 / 39.5 / 32.2 / 7.6 MJ/kg, with check 39.5/7.6 ≈ 5.2 · `s01-r1-c02-lipid-fraction-line.png`: fit y = 37x, the rule's assumed point 0.87 → 32.19 |
| C03 | 1 | `s01-r1-c03-icmr-requirement-bars.png`: ICMR-NIN 2020, sedentary and heavy work × men and women |
| C04 | 1 | `s01-r1-c04-activity-cost-line.png`: fit y = x/55 at 55, 85 and 95 kg (1, 1.55, 1.73) |
| C05 | 2 | `s01-r1-c05-daily-flows.png`: intake and expenditure from the table, check sum difference = 2.8 · `s01-r1-c05-stores-week.png`: the stock 620 → 622.8, each step derived |

## Known defects kept out of the figures (DEFECTS.md)

- C02 items 9, 10 and 12: the figures use MJ/kg only. No kcal-per-kilogram value appears, and
  neither does the 0.87 × 9.0 kcal route. The two pure-fat values are shown as separate bars, not
  as a range, and Hall's figure is not called "physiological".
- C03 items 17 and 19: no FAO/WHO/UNU total energy expenditure figure is drawn. A second C03
  figure, placing the three kinds of number on one axis, would need those worked examples. **It
  depends on the audit** relabelling them (not "measured") and settling the "about ten" range.
- C03 item 22: the caption calls the ICMR figures a committee's figure for a group, not "the one
  to use".
- C05 items 32 and 36: the captions say "made-up week" and "start at", never "measured". The
  8.26 practice problems are not drawn.

## For the auditor

- C04 draws Hall and Guo's "in proportion to overall body weight" as strict proportionality
  (y = x/55). Check that this reading is fair. The caption says "if".
- C02's lipid line counts only the fat in adipose tissue, which is how the section's "fraction ×
  fat's energy per gram" works. The caption says so. It is not a model of whole-tissue energy
  (lean change is 7.6, not 0).
- C05's stores chart has a y axis starting at 619.5, not 0. This is a line chart, and the
  caption gives the 2.8 on 620.
- `draw.py --book S01-R1` also redraws C06–C10's figures from their unchanged specs, which
  touches the other planner's PNGs and sidecars. Their content is identical.
