# Figures · S37-R1 · planner f2 (C10 to C18)

Done 2026-09-25 under `FIGURE-BRIEF.md`. Not committed. The figure specs changed (`figures:`,
`figure_note`, `derived`) and no prose did. `draw.py --book S37-R1` gives 29 figures and 0
problems. `build.py --check` blocks nothing in C10 to C18. At the time of the last run the only
blocks in the corpus were C09's, which belongs to the other planner. I opened and looked at every
PNG below.

## Per section

**C10: 3 figures**
- `s37-r1-c10-duty-landed-price.png` (drafter's): the landed price against the duty for a made-up
  Rs 100 before duty. Held by the `fit y = 100 + x` through 0/100, 5/105 and 10/110.
- `s37-r1-c10-rice-subsidy-share.png` (drafter's): the rice subsidy as a percentage of economic
  cost for 2021-22 to 2025-26, from the stated table values. The bars start at zero.
- **New** `s37-r1-c10-paddy-margin-base.png`: common paddy's cost of 1627, the gap of 814 and the
  MSP of 2441. The trap it shows is the base of a margin. Checks: `y[0]+y[1]=y[2]`, the gap is 50
  per cent of the cost, and the gap is 33 per cent of the MSP.

**C11: 2 figures**
- `s37-r1-c11-household-entitlement.png` (drafter's): kg a month against household size. Held by
  the fits `5x` and `35`, with a reference line at 7.
- **New** `s37-r1-c11-grain-per-person.png`: the same rule per person. The curve `y = 35/x` passes
  through 35, 5 and 3.5 and is checked like a fit. A flat 5 kg line is drawn beside it. The picture
  shows the section's point that the poorest households get less per head above 7 people.

**C12: 1 figure (new; it replaces the figure_note)**
- `s37-r1-c12-pm-poshan-food-norms.png`: PM POSHAN food norms in g per child per day, primary
  against upper primary. Grain is the heaviest item, every row is a floor, and salt and sugar have
  no bar. Checks: upper primary equals 1.5 times primary on all four rows. The 1.5 is `derived`
  (150/100).
- The drafter asked for a **flow diagram** that the tool cannot draw, so it is recorded here for
  the contract-change chat. It has four boxes: Parliament (NFSA Schedule II), then the WCD ministry
  (2022 guidelines), then the State (pays its share and sets the items, with the side arrow "to
  change the plate, go here"), then the anganwadi centre.

**C13: 2 figures**
- `s37-r1-c13-school-meal-energy.png` (drafter's): kJ from each food and the total, with a
  reference line at 1,881 kJ. Check: the parts sum to 1952.8.
- **New** `s37-r1-c13-ration-kj-trap.png`: the kJ-as-kcal misreading (2485) against the correct
  594.5, beside the reference woman's 1660 and the reference man's 2110. Checks: 2485/4.18 = 594.5,
  and the ratios 0.358 and 0.282.

**C14: 2 figures**
- `s37-r1-c14-grain-allocation.png`: **hole B-C14 is fixed.** The seven scheme bars add to
  605.88, but the text states 607.40 "with a small festival and calamity allocation". I added a
  bar for festival and calamity of 1.52, `derived` as 607.40 minus the seven rows. There is now a
  check that `sum(y) = 607.40`, and the caption and alt text state the total.
- **New** `s37-r1-c14-pm-poshan-lifted.png`: PM POSHAN grain, 22.31 allocated against 15.68
  lifted by December 2025. The section's point is that an allocation is not grain received.

**C15: 2 figures**
- `s37-r1-c15-double-burden-bars.png` (drafter's): six NFHS measures, NFHS-4 beside NFHS-5.
- **New** `s37-r1-c15-point-changes.png`: signed bars of the percentage-point changes (-2.9, -4.2,
  +3.4, +1.3). Each bar is checked against its stated subtraction.

**C16: 1 figure**
- `s37-r1-c16-oil-duty-bars.png` (drafter's; from_table block 0). The y-axis now reads "basic
  customs duty, as stated (%)" to match the table header.

**C17: figure_note kept.** The wanted diagram is a stage chain with each proposal pinned to its
stage, coloured by whether it acts upstream or on the person. The only number in the section is
15, so no data chart would teach anything.

**C18: figure_note kept.** The wanted diagram is the biscuit flow from crops to factory,
distributor and kirana, with a checked, seen or unknown mark on each link and the policy tools
hanging off each crop. The prices are on different bases, so a chart of them would compare
nothing.

## Caveats
- C14's 1.52 is a remainder. It could be one table row or several, and I did not check it against
  the DFPD table. The prose only says "a small festival and calamity allocation".
- C16's 2024 bar: the source says "import duty". The June 2025 release says the basic customs duty
  was 20% before its cut, so that supports the label. The auditor may still want to judge it.
- The labels on C11's per-person figure sit a little away from their points, so that they do not
  collide with the lines. They are readable.
