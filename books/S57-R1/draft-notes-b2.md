# Draft notes · S57-R1 · batch b2 (C03, C04)

Drafter, 2026-09-25. This run resumed an interrupted earlier run of this batch. That run had written
C03, its figure `s57-r1-c03-reversal-bars.png`, and two scratch scripts. C04 and this notes file did
not exist. C03 was re-checked from scratch and partly rewritten. C04 was written new.

## Records written

- `check/records/S57/S57-R1-C03.yml` (empirical, not quantitative). Changes to the earlier draft:
  - **Overlap with C01 removed.** C01 (batch b1) already walks through Roediger and Karpicke's
    Experiment 1 numbers (81/75, 68/54, 56/42) and Experiment 2 (SSSS/STTT, 14.2 vs 3.4 readings,
    confidence ratings). The old illustration 1 re-taught all of that. It now points back to C01
    and asks a new question of the same result: the size of the benefit as d, with a sign
    (-0.52, 0.95, 0.83), and why the same 14-point gap gives two d values (C02's point that an SMD
    divides by a spread). Experiment 2 and the confidence quote are gone from C03. The old must-know
    "never judge a method by an end-of-session check" duplicated C01's and was cut.
  - Definition: Experiment 1 is described as within-subjects (one passage each way), not as two
    groups; d = 0.83 added with its quote.
  - "Retention interval" is no longer re-defined in C03; C01 teaches it.
  - Added quotes: Agarwal "we derived 49 effect sizes (Cohen's d)" (backs "could compute") and
    "too varied for a meta-analytic approach" (backs "chose not to average them").
  - "Western Europe" became "Europe" (Denmark, Netherlands, Sweden).
  - Readability warnings fixed.
  - Figures replaced: `s57-r1-c03-d-by-delay.png` (signed d at three delays, from the illustration's
    table) and `s57-r1-c03-classroom-effect-sizes.png` (Agarwal's 49 effect sizes counted by size:
    3, 18, 12, 16; `check: sum(y) = 49`). The old `s57-r1-c03-reversal-bars.png` and its
    `.spec.json` (this batch's own files, now unreferenced) were deleted by exact path.
- `check/records/S57/S57-R1-C04.yml` (empirical, quantitative, 10 practice problems). Sources:
  Cepeda 2008 (authors' manuscript; the record says so), Dunlosky 2013 section 9, Weinstein 2018
  "Spaced practice". Figure `s57-r1-c04-best-gap.png`: the four best tested gaps (1, 11, 21, 21 days
  at retention intervals 7, 35, 70, 350) as points, with drawn lines for a gap of 20% and of 5% of
  the retention interval, and a label for the fitted optimum (23 days, 7%). Points are not joined,
  because they are the best of six or seven gaps tried and nothing was measured between them.

Both records: `python check/build.py --check` gives blocking 0 overall and no warning for C03 or
C04. `draw.py --book S57-R1` drew 13 figures, 0 problems; I looked at all three of mine. Every quote
was confirmed present by script, and each number quote was checked to state its number (C04's "30%"
comes from Cepeda's "0.3" and carries a `derived` line). Every practice line and every date was
recomputed in Python (`/home/claude/scratch-b2/recompute_c04.py`). Weekdays were computed, not
assumed.

## Decisions an auditor should look at

- **The planning range "20% to 30%".** Cepeda's abstract says "about 20%" for tests a few weeks
  away. The best tested gaps at 35 and 70 days work out to 31% and 30%, and the design aimed at
  gap/RI ratios "near 0.1, 0.2, and 0.3". So the record teaches a window, 20% to 30%, and tells the
  reader to take the later end because Cepeda says a too-long gap costs "much less" than a too-short
  one. The 30% end is derived, not stated as a recommendation by the authors.
- **Dunlosky's "10-20%" against Cepeda's falling ratio.** Dunlosky summarises Cepeda as a fixed
  10-20% and extrapolates to 5 years (6-12 months). Cepeda's own text says the ratio "must decline"
  as the retention interval grows (7% at 350 days). The record treats Dunlosky's 5-year example as
  an extrapolation past 350 days (must-know 4, practice 9). Worth a check that this is fair to
  Dunlosky.
- **The fitted surface.** My own recomputation of Cepeda's fitted function (parameters in the
  Discussion) puts the optimum near 24 days at 350 (paper: 23) but 5 days at a 7-day retention
  interval, where the best tested gap was 1 day. The record uses only the paper's stated 23 days
  and does not quote the function. No reader-facing number rests on my recomputation.
- **Bahrick 1979** is reported only through Dunlosky's words; its figure values are an image and
  are not held, so no scores are quoted.
- **Cepeda 2006** (47% vs 37%, 254 studies) is reported through Dunlosky; the record says so.
- Practice 7 uses a made-up 40% baseline, labelled as made up in the prompt.
- Practice 10's "a per cent change and a d can rank the same results differently" rests on Cepeda's
  26% (d = 1.5) for recognition against 64% (d = 1.1) for recall.

## Anything unsourced

Nothing reader-facing that I know of. The dates in illustration 2 and the practice set are a
worked schedule, not data. "Laying review dates on a calendar for yourself before teaching within a
month" (inventory) is done in illustration 2 with the same 20-30% window; no source measures that
case directly, and the analogy_breaks_when says the window is a starting point.

## Practice-set size (C04): 10

Ten, the inventory's top. The technique has several moves that compose: a ratio as a percentage,
a share of a quantity, splitting a total into gap and retention interval (a rearrangement), the
reverse (retention interval from a fixed gap), date arithmetic across month ends, per cent change
against percentage points, and the limit of a fixed ratio outside the data. Each move gets a
problem, two diagnostic errors are ones teachers actually make (reviewing just before the exam;
adding a per cent change to a percentage), and both transfer problems start from a real claim.

## Figures wanted

None beyond those drawn. A curve of the fitted retention surface's optimum against retention
interval would be nicer than the two straight reference lines, but it needs the paper's
exponential-and-log function, which I chose not to put in front of the reader.

## Glossary rows

Checked against `prose/GLOSSARY.md` and the rows batches b1, b5 and b6 propose. "Retention
interval" is b1's (C01) and is used, not re-taught. Proposed new rows:

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| feedback (in S57) | showing the learner the correct answer after their attempt | `S57-R1-C03` |
| low-stakes test | a test whose score counts for little or nothing | `S57-R1-C03` |
| restudy | reading or hearing the same material again, for the same time | `S57-R1-C03` |
| retrieval practice | an attempt by a learner, during learning, to bring material back to mind from memory without looking at it | `S57-R1-C03` |
| testing effect | a retrieval attempt improves memory on a later test more than restudy does; it shows on a delayed test, not always minutes later | `S57-R1-C03` |
| WEIRD | Agarwal and colleagues' short form: western, educated, industrialized, rich and democratic countries | `S57-R1-C03` |
| gap (between study sessions) | the time between two study sessions of the same material | `S57-R1-C04` |
| massed practice | the same study occasions put back to back; often called cramming | `S57-R1-C04` |
| spacing (distributed practice) | studying or retrieving the same material on two or more occasions spread out in time | `S57-R1-C04` |
| spacing effect | for the same total study time, spaced practice gives better long-term retention than massed practice | `S57-R1-C04` |
