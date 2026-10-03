# Figures, batch f2 (S58-R1-C07 to C12)

Figure planner, 3 Oct 2026. Only `figures:` entries edited; no prose touched. Every PNG drawn by
`check/figures/draw.py` from its spec, opened and looked at, and converted to greyscale (PIL
`convert("L")`) and looked at again. `draw.py --book S58-R1`: 29 drawn, 0 problems. `build.py
--check`: no record in C07-C12 blocks (the one block, C17, is another batch's stale PNG).

| Section | File | What it shows | Check that holds it | Greyscale |
| --- | --- | --- | --- | --- |
| C07 | `s58-r1-c07-subject-verb-gap.png` | Words in each of 4 sentences and words between subject and verb (table 0) | `y2[2] - y2[3] = 37` | Two series merged in grey. **Fixed:** direct labels on the first pair ("words in the sentence", "words between subject and verb"); readable in grey |
| C08 | `s58-r1-c08-acronyms-per-100-words.png` | Barnett and Doubleday: acronyms per 100 words, titles and abstracts, first year and 2019 (table 0) | ratios 10.25 and 3.43 | Merged in grey. **Fixed:** direct labels "first year counted" and "2019" on the first pair |
| C09 | `s58-r1-c09-one-person-step.png` | One person's worth, 100/n points, at 20, 40, 100, 200, 400; reference line at 1 point | curve `y = 100/x` through every point; `100 / x[1] = y[1]` | One series; fine. Unchanged |
| C10 | `s58-r1-c10-topics-before.png` (new) | Topic of each of 7 sentences before the rewrite: 6 changes | from table 0 column 1 | One series; fine |
| C10 | `s58-r1-c10-topics-after.png` (new) | The same after the rewrite: 2 changes, three flat runs | from table 0 column 2 | One series; fine |
| C11 | `s58-r1-c11-score-lines.png` | FRE against ASL: one line per version's ASW; the draft and Rewrite A on their lines; line at 60 | **added** checks: each point lies on its line (38.5, 71.0) | Solid mid-grey vs dashed dark line; distinguishable |
| C11 | `s58-r1-c11-counting-rule.png` | Draft and Rewrite A under the one-syllable and read-aloud rules (38.5/1.1, 71.0/8.3) | **added** four checks recomputing each score from the counts in the text | Merged in grey. **Fixed:** direct labels on the draft pair |
| C11 | `s58-r1-c11-three-scores.png` (new) | FRE of the draft, Rewrite A and Rewrite B (table 1) from zero, with lines at 60 and 100: B scores highest and is the worst | `206.835 - 1.015*24/7 - 84.6*29/24 = 101.1` | One series; fine |
| C12 | `s58-r1-c12-three-passes.png` | Words left after each pass: 161, 124, 69, 49 (table 0) | differences 37, 55, 20, total 112; derived 92 | One series; fine. Unchanged |

## Changes and fixes

- **C10.** The two-series step chart drew "before" and "after" as overlapping solid lines (they
  coincide at topic 1 for sentences 4-5) that merged in grey. Split into one figure per series,
  the same axes and size. `y_range` 0-4 gives whole-number ticks only (0-3.5 printed topic 0.5,
  1.5, 2.5, which do not exist). Old `s58-r1-c10-topic-changes.png` and its `.spec.json` moved
  (not deleted) to `books/S58-R1/superseded-figures/`.
- **C11 score-lines: alt text was wrong.** It put the draft on the lower line and Rewrite A on the
  upper. The draft's ASW (71/52) is smaller, so its line is the upper one, as the caption says.
  Alt corrected. The Rewrite A label crossed the draft's line; moved above it.
- **C11 new figure** for illustration 2's point (Rewrite B scores 101.1 and is the worst version).
  Ref lines carry no labels of their own; they are labelled at the left so the labels do not
  cross the Rewrite B bar.

## Not made (would need the prose or the tool changed)

- **C09** paired NFHS women/men bars (b4's wish): every value is `{{n:}}` in C09's text and
  draw.py does not substitute, so the figure would fail the number check.
- **C10** marked-up page with a margin column (b4's wish): not a chart; the tool cannot draw it.
- **C08** spread of acronym use (30 per cent once, 49 per cent two to ten times, 0.2 per cent over
  10,000): the middle band (11 to 10,000 uses) is not stated, and working it out from rounded
  shares would print false precision. Left to the prose.
- Two-series bar figures keep their colour legend (draw.py always draws one for two or more
  series); the direct labels repeat it so the figure reads without colour.
