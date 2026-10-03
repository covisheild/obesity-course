# S47-R1 figure plan, batch f1 (C01–C09)

Drawn with `python check/figures/draw.py --book S47-R1`. `python check/build.py --check`: no block in C01–C09. Every PNG was opened and looked at.

| Section | Figure or figure_note | What it shows | Check that holds it |
| --- | --- | --- | --- |
| C01 | figure_note (unchanged) | No measured number. Wanted diagram: four-stage cycle with the arrow back from evaluation and the proposal marked at agenda setting | — |
| C02 | figure_note (unchanged) | No measured number. Wanted diagram: four job boxes with the food-regulation bodies under each and a Union/State line | — |
| C03 | figure_note (unchanged) | Only dates. Wanted diagram: the ladder of instruments with an executive-power branch (Articles 73, 162) | A commencement step chart was considered. It needs 0 and 12 months, which the text does not state (it says "one year"), so it was not drawn |
| C04 | figure_note (rewritten to name a diagram) | Wanted diagram: Union/State/Concurrent circles with each proposal on its entries, and panchayats/municipalities below | — |
| C05 | figure_note (rewritten to name a diagram) | Wanted diagram: a tree from Council of Ministers and Cabinet to departments, each proposal's part on its Second Schedule item | — |
| C06 | `s47-r1-c06-private-members-bills.png` (caption reworded to the text's "the term running in 2012") | Private Members' Bills, introduced and discussed: Lok Sabha 264/14, Rajya Sabha 160/11 | `264 + 160 = 424`, `14 + 11 = 25` |
| C07 | `s47-r1-c07-packaging-path.png` (replaced) | Days from the draft's date (19 March 2018): copies reach the public on day 14, objections close on day 44, final notification on day 280. A dashed line at 30 shows where a count from 19 March would stop | derived `44 = 14 + 30`. Checks `12 + 2 = 14`, `44 − 30 = 14`, `12 + 244 + 24 = 280` |
| C08 | `s47-r1-c08-poshan-shares.png` (kept; caption now says "general components") | Centre's share by category and component, from the record's table | from_table block 0 |
| C08 | `s47-r1-c08-poshan-split.png` (new) | States with a legislature: Centre and State share of each component, 60/40, 25/75, 50/50 | each pair sums to 100 (three checks) |
| C09 | `s47-r1-c09-gst-votes.png` (fixed and extended) | Centre alone 33.3, States alone 66.7, Centre plus 41.7 from the States reaches 75 | derived `75 = 3/4×100`, `33.3 = 100/3`, `66.7 = 200/3`, `41.7 = 75 − 33.3`. Checks `y[0] + y[1] = 100`, `y[0] + 41.7 = 75` |

## Caveats
- **C09 was not being drawn.** `draw.py` checks the raw text and does not substitute `{{n:…}}`, while `build.py` does. The old PNG was stale but still passed the build. It is fixed with `derived` entries worked from the literal 3, 4, 100 and 200 in the working block.
- **No C09 rate figure.** A figure of 28 → 40 against the central 20 cannot pass `draw.py`, because 40 appears in C09 only as `{{n:gst_demerit_rate_pct}}`. The brief's "central 20 within the combined 40" would also show a State half that the section explicitly does not show.
