# S36-R1 figure plan, batch f2 (C08 to C14)

`python check/figures/draw.py --book S36-R1`: 0 problems. `python check/build.py --check`: 0 blocking in C08 to C14. I looked at every PNG as an image.

| Section | Figures or figure_note | What the figure shows | Check that holds it |
| --- | --- | --- | --- |
| C08 | figure_note | No chart. The diagram a reader would want is a flow of the interview's parts. | n/a |
| C09 | figure_note | No chart, because the effect is unmeasured. The diagram a reader would want shows direction: interviews that all lean one way beside ones that scatter. | n/a |
| C10 | `s36-r1-c10-transcribing-hours.png` (rebuilt) | Hours of typing against hours of audio at 3 and 8 hours per recorded hour. It marks the 47-minute pilot (2.35 and 6.27 hours) and five one-hour pilots (15 and 40 hours). | `fit y = 3*x` and `y = 8*x` through every point; a ref at x = 0.7833; every number is in the prose |
| C11 | `s36-r1-c11-five-shares.png` (drafter's) | The five pilot shares, with the gate at 50 and the mean at 27.2. Interview 3 is over the gate. | `from_table` block 3; `check` that the mean is 27.2 |
| C11 | `s36-r1-c11-turns-and-words.png` (drafter's) | The same three turns each, but 15 against 108 words and 104 against 8. | `from_table` block 2 |
| C11 | `s36-r1-c11-share-and-ratio.png` (new) | Share = 100/(1 + ratio), through the section's worked cases: 0.0769→92.9, 1→50, 1.78→36, 3→25, 7.2→12.2. A ratio of 1 is the gate. | `fit` plus a `curves` entry tied to the series |
| C12 | figure_note | A tally of codes is the counting the section warns against. The diagram a reader would want is the read, code, memo, next-interview loop. | n/a |
| C13 | figure_note | The check reads words against words. The diagram a reader would want is the four acts as a checklist. | n/a |
| C14 | `s36-r1-c14-talk-share.png` (drafter's) | The section's pilots: 46, 38, 26, 20, 43 under the 50 line. | `from_table` block 0 |
| C14 | `s36-r1-c14-moving-and-flat.png` (new) | The section's pilots beside the trainee's flat 45, 44, 47, 46, 45. Both meet the gate, and only the first moves. | Literal data; every value is stated in the critique exercise |

C10 fix: the compression removed the hours table, so `from_table` block 3 no longer existed. The spec now lists its data and uses the 47-minute worked exercise together with the illustration's five-pilot sum.
