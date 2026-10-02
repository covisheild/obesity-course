# S58-R1 · Task 2 draft notes · batch b7 (C17, C18)

## Records written

- `check/records/S58/S58-R1-C17.yml` — Honest axes: where an axis starts, what range it shows, and
  measuring the distortion. `derivable`, `quantitative: true`, 14 practice problems, 4 illustrations,
  3 figures, `common_misreading`, `reporting_sentence`, 2 exercises (retrieval; design, K02).
- `check/records/S58/S58-R1-C18.yml` — Decoration that does no work. `empirical`, 2 illustrations,
  1 figure, `common_misreading`, 3 exercises (retrieval; critique, K02; teaching, first-year resident).

Both: every quote found in its source file by the build's own normalisation (`build._source_text`),
every illustration number passes `_states_value`, `check_arithmetic` empty, every figure spec passes
`figspec.verify` and was drawn by `python check/figures/draw.py --book S58-R1` (0 problems), and each
PNG was looked at. Every practice answer and working line was recomputed in Python. The full
`build.py --check` was slow under load from the other batches; see the end of this file.

## What C17 covers, and what it leaves to Book 0

Book 0 F2 (`B0-R0-C40`) already teaches "bars from zero, lines need not". C17 names that and builds
on it: the principle of proportional ink (Bergstrom & West, via Wilke ch. 17), shading counts as ink,
the drawn ratio against the data ratio, Tufte's Lie Factor from percentage changes, the derived
shortcut LF = a ÷ (a − s) for two bars (worked in full in illustration 2: the b − a cancels), the
line-axis range (Bergstrom & West: "not much larger than the range of the data values"), four honest
redraws (bars from zero; points on a stated range; bars of the change from zero, after Wilke §17.1;
ratios on a log axis with bars from 1), and Correll et al.'s measured effect on readers.

Illustrations: (1) Tufte's real newspaper fuel-economy chart, LF 14.8, failure first; (2) the NFHS
women's rows on a made-up slide from 20: LF 34.3, the shortcut derived, a table of LF by axis start;
(3) the redraws, with the urban/rural ratio on a log axis; (4) Correll: 0.36 rise in perceived
severity on a 1-5 scale for an axis at 25% against 0%; break marks did not help; persisted when
numbers were reported accurately.

## Anything unsourced or inferred

- **14.8** (Tufte's LF) is worked out from the quoted 783 and 53 and carries a `derived` field: the
  text layer garbles the printed fraction, so it is not quoted (brief: never quote the garbled text).
- **The LF formula and the data-ink ratio** are set in `working` blocks in our own notation; only the
  clean words ("size of effect shown in graphic", "size of effect in data", "proportion of a graphic
  that can be erased without loss of data-information") are quoted.
- **2016** as the year NFHS-4's fieldwork ended is read from the survey's own label "2015-16"; it is
  used only to place NFHS-4 on the x-axis of `s58-r1-c17-line-from-18.png`. NFHS-5's end, 30 April
  2021, is quoted from the fact sheet.
- **Bateman: when gaze was recorded.** The paper says both "throughout the description task" and
  "During the recall portion". The record says only "while the charts were on screen" (noted in the
  reference's `verified.note`).
- **Bateman effect sizes.** The held text reports t and p only; the means are in figures not held.
  The record says so ("not the size of the difference in score points") rather than inventing one.
- Nothing else rests on an unopened source. All references `opened: true`.

## Practice set (C17): why 14

The technique has several moves that compose: drawn heights from an axis start, drawn ratio against
data ratio, percentage changes into a Lie Factor, the shortcut a ÷ (a − s) and its reverse (find the
axis start from a picture), area scaling for pictures, and bars from 1 on a log axis. Fourteen lets
each move appear once on bare numbers and once on a real quantity, with a range choice, two
diagnostics (ratio-of-ratios instead of the LF; a break mark claimed to fix the LF) and two
transfers (the Fox News chart from Correll; a district officer's "almost doubled"). Levels: 1, 2, 2,
3, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10. Real figures name their citekeys (NFHS, Bergstrom & West, Tufte,
Correll, Wilke).

## Figures

Drawn and passing:
- `s58-r1-c17-lie-factor-by-start.png` — LF against axis start for the NFHS women's bars, from the
  illustration's table; fit y = 20.6/(20.6 − x); reference line at Tufte's 1.05; log side axis.
- `s58-r1-c17-bars-from-zero.png` — NFHS-4 and NFHS-5, women and men, bars from zero.
- `s58-r1-c17-line-from-18.png` — the same four values as points joined by lines, axis 18-26, each
  survey at the year its fieldwork ended (2016, 2021).
- `s58-r1-c18-where-they-looked.png` — Bateman et al.'s gaze split: Holmes charts 40/27/13/20 (data
  alone, data in a picture, picture alone, elsewhere; 40 and 20 derived from 67, 27, 13), plain
  78/0/0/22.

**Figure wanted and not drawable:** the brief's "same data with a zero and a truncated baseline".
The truncated *bar* chart cannot be drawn: `figspec.verify` blocks any bar chart whose axis does not
start at zero, by design. The wanted figure: NFHS women 20.6% and 24.0% as bars on an axis from 20
(drawn heights 0.6 and 4.0, second bar 6.67 times the first, LF 34.3), beside the same bars from
zero. If the conductor wants it, draw.py would need a deliberate "wrong on purpose" bar kind with a
mandatory label; I did not edit draw.py. The LF-by-start curve and the line from 18 carry the
lesson instead.

**Tool note for the conductor:** `check/figures/draw.py --book` does not run
`reader_checks.apply_numbers`, so a figure's `figspec.verify` there sees `{{n:key}}` unsubstituted.
I therefore kept every number a figure plots literal in the record's `table` and `working` blocks,
and in captions; prose sentences use `{{n:key}}`. Other batches drawing from NFHS numbers should do
the same, or the drawing step will report numbers "not stated".

## numbers.yml

No keys added (brief: do not edit). Keys used: `nfhs5_women_ow_ob_pct`, `nfhs4_women_ow_ob_pct`,
`nfhs5_men_ow_ob_pct`, `nfhs4_men_ow_ob_pct`, `nfhs5_women_ow_ob_urban_pct`,
`nfhs5_women_ow_ob_rural_pct`, `nfhs5_men_ow_ob_urban_pct`, `nfhs5_men_ow_ob_rural_pct`,
`nfhs5_women_ow_ob_change_pp`, `nfhs5_men_ow_ob_change_pp`.

Candidates for the reconciler (shared or likely to be):
- `nfhs5_women_urban_rural_ratio`: 1.685 — urban to rural, women overweight or obese, NFHS-5;
  33.2 ÷ 19.7. C09 computes the same value and reports it as 1.69; C17 does too.
- `tufte_lf_threshold`: 1.05 — Lie Factor above which Tufte calls distortion substantial;
  `tufte_1983_visual_display` p. 57. Likely reused by C22 (making the plot) and the C23 journey.
- `nfhs5_women_lf_axis20`: 34.3 — LF of the women's NFHS-4/NFHS-5 bars drawn from an axis at 20;
  20.6 ÷ (20.6 − 20). Only if C23 reuses the slide.

## Notation rows needed

None new. The records use ÷, −, × (rows exist). "log10" is written as text. Letters a, b, s and the
abbreviation LF are explained in words at first use; LF is expanded as "Lie Factor (LF)" in C17's
definition, so the booklet's acronym check is satisfied there.

## Glossary rows (proposed; not added)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| axis start | the value at which a figure's value axis begins, written s | `S58-R1-C17` |
| chartjunk | Tufte's word for decoration on a figure that "does not tell the viewer anything new" | `S58-R1-C18` |
| data-ink | the ink on a figure that changes when the data change: the bars, points and lines | `S58-R1-C18` |
| data-ink ratio | the data-ink divided by all the ink used to print the figure | `S58-R1-C18` |
| decoration (on a figure) | any element that tells the reader nothing about the data or about how to read them | `S58-R1-C18` |
| direct label | a group's name written beside its data, in place of a legend | `S58-R1-C18` |
| drawn ratio | how many times taller one bar is drawn than another: (b − s) ÷ (a − s) | `S58-R1-C17` |
| legend | the key that says which colour or mark stands for which group | `S58-R1-C18` |
| Lie Factor (LF) | the percentage change a figure draws divided by the percentage change in the data; 1 is honest | `S58-R1-C17` |
| non-data ink | everything on a figure that is not data-ink: frames, grids, labels, backgrounds | `S58-R1-C18` |
| principle of proportional ink | a shaded area in a figure must be in proportion to the value it stands for | `S58-R1-C17` |
| truncating an axis | starting a bar chart's value axis above zero | `S58-R1-C17` |
| value message | the opinion a chart carries, in Bateman and colleagues' sense | `S58-R1-C18` |

I avoided "baseline" for the axis start: the glossary already has "baseline" as the start of a
weight series (`S02-R1-C01`).

## Notes for others

- **C19, C20** already point back to "the direct labelling of `S58-R1-C18`". C18 now names and
  glosses *direct label* and *legend* in its definition ("a group's name written beside its data, in
  place of a legend, the key that says which colour is which") and teaches it as a must-know move.
  C20 re-glosses legend in the same sense: consistent.
- **C22 (making the plot)** should take its axis step from C17: bars from zero (LF 1); points on a
  stated range not much wider than the data; the change itself as bars from zero; ratios on a log
  axis with bars from 1; state any non-zero start in the caption. And its decoration step from C18:
  ask of each element what it tells the reader; keep axis titles, tick labels, light grid, direct
  labels.
- **C23 journey:** use "Lie Factor (LF)", "axis start", "a ÷ (a − s)" in those words. C17's
  `reporting_sentence` already drafts the caption sentence for the NFHS women's line chart from 18.
- **Tufte is the 1983 first edition**, cited with its page numbers (56, 57-58, 93, 96, 100, 107,
  113, 116). Wilke ch. 23 cites the data-ink ratio as "Tufte 2001"; do not copy that year.
  Rougier et al. Rule 8 misquotes Tufte ("Regardless of the cause"; Tufte p. 107 has "Regardless of
  its cause") and misspells him "Tutfe": quote Tufte from Tufte.
- **Correll et al.:** the Fig. 1 caption's "4.6% increase in tax rate (ratio of 1.13 to 1)" is a
  4.6 percentage-point rise, about 13 per cent; C09 may want it as a points-against-per-cent case
  (C17 uses it at practice level 9). Experiment 3 found trend estimates no worse on a cut axis but
  *more* error on individual values at a 25% start; say "reported the numbers accurately" (their
  Conclusion), not "read every value correctly". Many passages carry the "ﬁ" ligature; quote around
  it.
- **Bateman et al.:** do not use the word "recall" in reader prose for their memory measure (the
  book's rule reserves "recall" for pointing back); C18 says "remembered". Ten people per memory
  group, untimed viewing, spoken description; the authors "do not advocate this strategy as a
  general principle".
- **C17 does not contradict Book 0 F2**: it names the zero rule as Book 0's and does not re-teach it.
- The urban-rural ratio for women is computed as 1.685 and reported as about 1.69, matching C09's
  rounding lesson.

## Build

`python check/build.py --check` (2 Oct 2026, run while other batches were drafting): 0 blocking
and 0 warnings for S58-R1-C17 and S58-R1-C18 and their four figures; the build's printed list
shows only the first 15 blocks, so the full list was filtered by a script calling `build.check()`
directly. The 26 blocking items at that run were all in other batches' records (C09 and C11:
arithmetic written to four decimals against integer inputs, which the checker's tolerance rule
rejects; write "is about" for a rounded quotient of whole numbers). `draw.py --book S58-R1`: 0
problems. The only per-field acronym note is "LF" in C17's exercise answers, which is expanded as
"Lie Factor (LF)" earlier in the same section, so the booklet-level check passes.
