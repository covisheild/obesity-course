# Book 0 · F2 inventory — Reading a figure, and the ways a figure misleads

One section, record `B0-R0-C40`, sequence 40, between F1 (`B0-R0-C39`, reading a table) and F3
(`B0-R0-C41`, checking a reference). Produced 23 September 2026, after Parts A to C were released
and while Parts D and E are being written in other chats.

---

## Why this section, and why it is not C5 again

Every subject book above Book 0 argues from figures: prevalence trends across survey rounds,
dose-response curves, forest plots, maps of district burden. A reader who cannot read one — or who
reads the shape first and the axes second — is carried by whoever drew it.

**C5 (`B0-R0-C19`) already teaches the machinery of a graph**: what each axis is, that the scale was
chosen by someone, slope as a rate, the intercept, and that two drawings of the same points on
different scales are both honest. F2 does not repeat any of that. It points back to it.

**F2's own territory is two things.** First, reading a *published* figure end to end before
believing its shape — the figure-shaped version of F1's four questions. Second, the ways a figure
misleads while every number on it is correct, and the one idea underneath most of them: **a mark
carries its number by position, by length or by area, and each of those can be made to lie in its
own way.**

## Type and sources

`derivable`. Every claim is geometry or arithmetic the reader can check — a bar that starts at 400
instead of zero shows a difference of 350 as if it were 50, and a picture scaled in both directions
by 1.56 has 2.42 times the area. The anchors confirm; they are not the evidence.

Both anchors are held, so every quote is checked by the build:

| Citekey | File | What it carries |
| --- | --- | --- |
| `openstax_contemporary_math` | `sources/openstax_contemporary_math_8_2.txt` | The two primary manipulations (axis scales, areas of bars); non-zero vertical axes overemphasise differences in heights; area images distort because width changes with height; the eye reads area more easily than height; histogram bars must have equal widths |
| `openstax_business_stats_2e` | `sources/openstax_business_stats_2_1.txt` | Varying histogram category widths; a time axis whose spacing changes part way across; pie charts set side by side across years; shrinking or stretching the time axis |
| `nfsa_2013` | `sources/nfsa_2013.txt` | Schedule II's energy values per meal, the real numbers the figures are drawn from |

**Both OpenStax books are CC BY-NC-SA 4.0**, confirmed on their details pages; the excerpts are
held for non-commercial use under the same licence.

## What the section must establish

1. **Read before you look.** Before the shape: what is one mark, what does each axis measure and
   in what unit, where does each axis start and how is it spaced, and where did the numbers come
   from. This is F1's four questions turned to a figure, and it must say so; it must also agree
   with C5's reading order rather than invent a third one.
2. **How a mark carries a number** — position (a point on a line), length (a bar), area (a
   picture, a bubble, a slice). Length only carries a value if it is measured from zero. Area grows
   as the square of a scale factor (A6 powers), so a picture scaled up in both directions overstates.
3. **The catalogue**, each shown once and each with its check:
   - a bar chart whose value axis does not start at zero;
   - pictures or areas standing in for bars;
   - unequal spacing — bins of unequal width, or a time axis whose steps change part way;
   - a chosen window — the start and end of a time series picked to show a rise or a fall;
   - counts where rates are needed (A5): more cases in a bigger district is not a higher burden;
   - two vertical axes on one figure, where the crossing point is set by the two scales chosen.
4. **Line charts differ from bar charts on the zero question**, and this is where F2 must be exact
   rather than repeat a slogan. A bar's length is its value, so a bar must start at zero. A line
   carries its value by position; a line chart that does not start at zero can be honest, as C5
   says, provided the reader reads the scale. The anchor's warning is about bars. F2 must not
   contradict C5.

## Boundary — what F2 does not teach

- **Uncertainty.** Whiskers, error bars and confidence intervals belong to Part D, which is being
  written in parallel. F2 may say that a bar or whisker around a point shows some spread or some
  uncertainty and that which one is stated in the caption; it teaches nothing more and depends on
  nothing in Part D.
- **Distribution shapes** (skew, spread). A histogram's bins appear only as the unequal-width
  distortion.
- **Making charts.** The reader reads figures; the section is not a design guide.
- **Log axes** are taught in A7 and C6. F2 names them in one line and points back.
- **No body-mass-index threshold**, and no obesity prevalence figure that is not from a held
  source. Invented data is marked as made up in the sentence that introduces it.

## Drill set — `quantitative: true`, by explicit override

Part F is non-quantitative by default, and F1 carries no drill set. F2 is the exception and says
so in `practice_note`: reading a figure is a technique with a fixed order and several composing
checks, the square law is a calculation, and a reader who has only read about a truncated axis
has not yet caught one. **Eight to twelve problems.** Mechanical: read values off a described
figure, compute an area ratio. Applied: the same with real units. Diagnostic: a worked reading of
a figure that goes wrong at one step. Transfer: a figure described in a press line.

## Figures

The section is about pictures, so it earns them — but they are drawn by the main thread from the
record's own tables, as every Book 0 figure is. The drafter names each figure it wants and the
table it reads from. Expected:

- **Baseline** — Schedule II's six energy values as bars from zero, beside the same bars from 400.
- **Area** — two values as bars, beside the same two as pictures scaled in both directions.
- Possibly **window** — an invented, marked series, whole and then cut to a chosen stretch.

## Dependencies

| Needs | Why |
| --- | --- |
| C5 `B0-R0-C19` | Axes, scale, the chosen scale, both-drawings-are-honest |
| F1 `B0-R0-C39` | The four questions, which F2 turns to a figure |
| A5 `B0-R0-C05` | Rates, for counts-versus-rates |
| A6 `B0-R0-C06` | Powers, for the square law |
| A7 `B0-R0-C07` | Log axes, named and pointed back to |
