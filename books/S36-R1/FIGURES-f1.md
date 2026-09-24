# Figure plan · S36-R1 · batch f1 (C01–C07)

Drawn with `python check/figures/draw.py --book S36-R1`; `python check/build.py --check` shows no block in C01–C07. Every PNG below was opened and looked at.

| Section | Figure or note | What it shows | The check that holds it |
| --- | --- | --- | --- |
| C01 | figure_note | Names the diagram a reader would want: a loop (asking finds what to count, counting says how common, a trial tests the fix). No quantity in the section. | — |
| C02 | `s36-r1-c02-share-follows-choice.png` (new) | Two bars: 7 of 12 chosen = 58.33333333 %, 7 of 14 chosen = 50 %. The same seven respondents give a different share when the choice changes, so the share describes the choice, not the clinic. | `y[0] = 7/12*100`, `y[1] = 7/14*100`; 50 derived from the prose's `7 divided by 14 = 0.5`. Replaces the old note. |
| C03 | figure_note | Names a spectrum: structured, semi-structured and in-depth as points on one line of how much is fixed in advance. | — |
| C04 | `s36-r1-c04-who-answers-whom.png` (kept) | Respondent turns answering the moderator or another participant: first group 6 and 0, second group 2 and 6. | Recounted by hand from both exchanges; all numbers stated in the prose's own counts table. |
| C05 | `s36-r1-c05-draft-labels.png` (kept) | The eight questions by label, first draft against rewrite: open 3→7, closed 5→1, leading 5→0, double 2→0. | `y1[0] + y1[1] = 8`, `y2[0] + y2[1] = 8`; labels recounted from both question tables. |
| C06 | `s36-r1-c06-time-plan.png` (kept) | Planned minutes for the seven parts of the guide, 50 in all, most on main 2 to 4. | `sum(y) = 50`. |
| C07 | figure_note | Names a flow of the consent steps in order, ending with a spoken label, not a name. No quantity in the section. | — |

Not drawn, on purpose: word counts of R1's turns in C03's two exchanges. They are not stated in the text and cannot be derived by arithmetic, and a chart of them would decorate a point the prose already makes.
