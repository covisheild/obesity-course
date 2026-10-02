# Draft notes, batch b6 (S58-R1-C14, C15, C16)

Task 2 drafter, 2 Oct 2026. Exemplars followed: S57-R1-C03 (empirical), S57-R1-C10 (derivable).

## Records written

| Record | Name | Type | Figures |
| --- | --- | --- | --- |
| `check/records/S58/S58-R1-C14.yml` | A figure makes one claim | derivable | `s58-r1-c14-urban-rural.png` (grouped bars, NFHS-5 urban v rural, women and men) |
| `check/records/S58/S58-R1-C15.yml` | Choosing the mark: what the eye reads accurately, and the shape of the data | empirical | `s58-r1-c15-large-errors.png` (Cleveland & McGill exp. 1: share of judgments v share of large errors, position and length; checks the 5.3) |
| `check/records/S58/S58-R1-C16.yml` | Show the data: when a bar of means hides what the points would show | empirical | `s58-r1-c16-equal-bars.png` (three equal bars of means), `s58-r1-c16-every-value.png` (the 24 values, each ward's dots in order) |

Each record has a `retrieval` exercise, `common_misreading`, and (C14, C16) `reporting_sentence`. None is
quantitative, so none carries `practice[]` (the inventory marks only C09, C11, C17).

## Sourcing

- Every factual claim is quoted from a held file; all 21 + 51 + 18 quotes were confirmed as
  whitespace-normalised substrings of their files by script, and each number's quote states it.
- No `[NOTE]` line or header is quoted. Where the Cleveland & McGill text layer is garbled ("I0",
  "5 .", "2.97", "4-"), the quote stops before the garble or uses the clean summary passage (§4.5)
  instead; the garbled points are explained in `verified.note`.
- The Heer & Bostock quotes keep the file's "ﬁ" ligature so the build can find them.
- ICMJE is quoted in short sentences only and linked; Wilke is quoted, never adapted (CC BY-NC-ND).
  The mark-by-shape table in C15 illustration 3 is the book's own wording of Wilke ch. 5's five
  headings; no Wilke figure or table is reproduced.
- **Nothing unsourced.** Three things are the book's own reasoning, labelled as such or built from
  quoted parts: the sentence / table / figure decision table in C14 (from ICMJE §3.e, §3.h and
  Rougier Rule 2); the C14 boundary that one claim never licenses cutting data that would weaken it
  (resting on Rougier Rule 7); the C16 box-plot quartiles of ward 3 (Book 0's method on made-up data).
- C15 rebuilds Cleveland & McGill's 5.3 from "Seventy-eight percent" and "three position judgments for
  each two length judgments", and their 7.3 from 88 per cent with equal numbers of judgments ("each
  set was encoded by a bar chart and a pie chart"). Recomputed in Python: 39 / 7.333 = 5.318;
  88 / 12 = 7.333.
- C15 deliberately does not compare the 5.3 (length) with the 7.3 (angle): different experiments.
  Heer & Bostock found angle no worse than length; C15 says so.
- C16's three wards and two hostels are **made up** and say so in the sentence that introduces them.
  Recomputed: each ward sums to 240, mean 30; SDs 14.29, 14.28, 14.25 (all 14.3 to 1 dp); medians 30,
  25.5, 30; ward 3 quartiles 16.5 and 43.5. Hostels: both means 7.25; medians 7.25 and 5.75.

## Practice-set size

Not applicable: C14-C16 are not quantitative.

## Figures

All four specs pass `python check/figures/draw.py --book S58-R1` (19 drawn, 0 problems at my last
run) and were looked at as images.

- NFHS numbers in C14's figure: `draw.py` reads the raw record, without `{{n:}}` substitution, so a
  figure's values must appear literally in the reader text. C14's illustration 1 therefore quotes
  fact-sheet rows 88 and 89 verbatim as a blockquote (quotes are the source's words, not retyped
  numbers); all prose uses `{{n:key}}`. **Worth telling the conductor:** any figure that plots a
  `numbers.yml` value needs either a literal source quote in the body or a `draw.py` that substitutes
  first.
- **Wanted, not drawable:** (1) a true strip chart for C16 (one column of jittered dots per ward):
  `scatter` needs numeric x, so the wards sat at x = 1, 2, 3 with ticks at 1.25, 1.50 ... I replaced it
  with each ward's dots set out in order (x = 1 to 8, joined), which shows the three shapes clearly.
  (2) A line over the two NFHS rounds for C15: numeric x of 4 and 5 printed ticks at 4.2, 4.4 ...,
  meaningless for survey rounds. Dropped; the line is described in prose instead. A `x_ticks` option
  (or categorical x for line/scatter) in `figspec.py`/`draw.py` would allow both.
- **Orphan files to delete** (I did not `rm` in the repository, per the brief): my superseded drafts
  `check/figures/s58-r1-c15-two-rounds.png` and `check/figures/s58-r1-c16-strip-chart.png`, each with
  its `.spec.json`. No record refers to them now.

## numbers.yml

No keys added. Used: `nfhs5_women_ow_ob_pct`, `nfhs4_women_ow_ob_pct`, `nfhs5_men_ow_ob_pct`,
`nfhs4_men_ow_ob_pct`, the four urban/rural keys, and both `_change_pp` keys.

Candidates for the reconciler if another section reuses them (all literal in my records now):

| Value | Meaning | Source |
| --- | --- | --- |
| 5.3 | large errors per judgment, length over position | `cleveland_mcgill_1984_graphical_perception` p. 542 |
| 7.3 | large errors per judgment, angle over position | same, p. 542 |
| 1.4 to 2.5 | factors by which position beat length | same, §4.5 |
| 1.96 | times as accurate, position over angle | same, §4.5 |
| 3 of 40 | cases where the pie beat the bar chart | same, p. 540 |
| 703; 85.6%; 13.4% | papers reviewed; with a bar graph; with a univariate scatterplot | `weissgerber_2015_beyond_bar_graphs` |

## Notation rows needed

None new. The records print ≥ (in the quoted NFHS rows; glossed in words in C14), ≈ (C15's working,
glossed in words where first used) and ± (only inside a reference quote). All three already have rows
in `check/notation.yml`.

## Build-level notes

- The NFHS fact sheet is cited as `kind: instrument`: the build rejects `dataset`, although the schema
  lists it.
- The arithmetic gate is exact when the left side shows no decimals ("22 divided by 3 = 7.333"
  blocks), so C15's two inexact steps are written with ≈. The same rule is what blocked several
  C09 and C11 lines in an earlier run of the build.
- `python check/build.py --check`, filtered to C14-C16 by a scratch runner over the same
  `build.check`: 0 blocking; only sentence-length warnings (26-27 words) remain.

## Glossary rows

Checked against `prose/GLOSSARY.md`: "mark", "pie chart", "value axis", "distribution", "median",
"quartile", "standard deviation", "standard error of the mean" already exist and are used in their
senses. "continuous (random variable)" exists from S02-R1-C13; C16 uses "continuous data" only as
Weissgerber's term for a measured quantity, in the same sense (any value in a range).

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| bimodal | having two clusters of values, two peaks | `S58-R1-C16` |
| box plot | a box around the middle half of the values, a line at the median, whiskers beyond, far values as single dots | `S58-R1-C16` |
| caption | the text printed with a figure; journals call it the figure legend | `S58-R1-C14` |
| common scale | one axis that every mark being compared is read against | `S58-R1-C15` |
| elementary perceptual task | the judgment the eye makes to read a number back from a mark: position, length, angle, area and others | `S58-R1-C15` |
| jittering | spreading dots a little sideways at random so that equal values do not hide each other | `S58-R1-C16` |
| measured quantity | a value such as minutes or kilograms that can take any value in a range (continuous data) | `S58-R1-C16` |
| strip chart | every value drawn as a dot along the value axis, one column per group; also called a univariate scatterplot | `S58-R1-C16` |

## Notes for others

- **C03 drafter:** C14 points to "the one message you wrote for it (`S58-R1-C03`)" and calls a
  figure's single statement its "claim". If C03 names it differently, C14's wording should follow.
- **C17 (honest axes):** C15 says the value axis of a line or dot chart may start above zero ("at 15
  per cent, a little below the lowest point"), citing Book 0 F2 (`B0-R0-C40`), and that on a log axis
  amounts take dots, not bars (Wilke §17.2). C17 should build on this, not contradict it. C14's figure
  is a bar chart from 0.
- **C18 (decoration):** C15 already cites Cleveland & McGill's conclusion that pies and divided bar
  charts "should not be used". C18 need not repeat it.
- **C20 (words on a figure):** C14 introduces "caption" (= the journal's "legend") and the rule that its
  first sentence states the finding, and that titles go in the caption, not on the drawing (ICMJE
  §3.i). C20 owns the rest of the caption (n, what an error bar is). C16 names standard deviation and
  standard error error bars only in passing, pointing to `B0-R0-C29`; it does not teach their
  difference.
- **C21 (tables):** C14 states the sentence / table / figure decision and ICMJE's "do not duplicate
  data in graphs and tables". C21 should use the same three-way rule.
- **C22 (making the plot):** C14 says a slide figure is made again, not lifted from the paper (Rougier
  Rule 3).
- **C23 journey:** C14 makes the urban-rural gap the figure's claim and puts the NFHS-4 to NFHS-5 rise
  in a sentence; it also notes the India fact sheet gives NFHS-4 only as a total, so an urban-rural
  trend cannot be checked from it.
- **Terms chosen:** "strip chart" (Wilke) rather than "dot plot" or "univariate scatterplot"; "box
  plot" as two words; "bar chart" throughout (Book 0's term), never "bar graph" outside quotes.
