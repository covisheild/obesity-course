# S55-R1 figure plan, batch f1 (C01 to C08)

Drawn with `python check/figures/draw.py --book S55-R1` (6 figures, 0 problems); `check/build.py --check`: 0 blocking. Every PNG was opened and inspected. No prose was edited.

| Section | Figure or note | What it shows | What holds it |
|---|---|---|---|
| C01 | figure_note | No measured numbers. Wanted: a funnel of four candidates, one kept and three turned down with reasons. | none |
| C02 | `s55-r1-c02-parts-named.png` (kept, caption fixed, value labels added) | How many of the five made-up drafts and rewrites name each part: 1→5, 3→4, 0→4, 5→5 | `from_table` block 3 (the count table in illustration 2, which the text now holds); checks y1[3]=5, y2[0]=5, y2[3]=5. The caption no longer says "the fifth is a how-common question" (rewrite 5 is PICO) and now says rewrite 1. DEFECTS H2 is resolved: the second illustration is back in the text. |
| C03 | `s55-r1-c03-salsa-cases-controls.png` (new; replaces figure_note) | Hepatitis A outbreak, 2003: 94% of cases against 39% of controls ate salsa. The controls are what make the 94% mean anything. | Literal values, both stated in the text and table (as percentages, so they are not read from the table) |
| C04 | figure_note | No measured numbers. Wanted: a flow through test 1, test 2 and narrowing steps 0 to 3. | none |
| C05 | figure_note | No measured numbers. Wanted: a four-quadrant grid for Q1 to Q4. | none |
| C06 | `s55-r1-c06-medians-by-design.png` (kept) | Patsopoulos medians by design, 1991 and 2001 | `from_table` block 1 |
| C06 | `s55-r1-c06-uncited-shares.png` (new) | The six shares uncited (55, 4, 21, 12, 23, 18), each labelled with what was counted and when, with a reference line at half | Literal values; every number, year and window in the text; y=50 stated |
| C06 | `s55-r1-c06-heneberg-check.png` (new) | About 1.6% uncited at first glance, 0.3% after checking by hand | Literal values stated in the text |
| C07 | figure_note | Two questions answered in words; the one-in-ten threshold is a made-up remark. Wanted: a two-branch tree per candidate. | none |
| C08 | `s55-r1-c08-totals-and-item-5.png` (kept, value labels added so zeros show) | Totals and item 5 scores for candidates A to J. The rule's five rejections are the item-5 zeros. B and I tie at 9. | `from_table` block 1 (the score table, now in the text); checks y1[1]=9, y1[0]=8, y2[0]=0. DEFECTS H19 is resolved: the candidates and item 4 scores are now in the text. |

Housekeeping: I deleted the orphan `check/figures/s55-r1-c06-window.spec.json`, which had no PNG and no figure entry.
