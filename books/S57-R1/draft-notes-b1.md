# Draft notes · S57-R1 · batch b1 (C01, C02)

Drafter, 2026-09-25. This run resumed an earlier run that had been cut off. That run had written C01
and its figure. C02, the notes and the scratch files did not exist. C01 was re-checked from
scratch and corrected. C02 was written new.

## Records written

- `check/records/S57/S57-R1-C01.yml`: empirical. Corrections to the earlier draft:
  - Experiment 2's test periods were 10 minutes long, not 5. Added the quote "Each test lasted 10 min".
  - Experiment 1 was within-subjects: each student restudied one passage and was tested on the
    other. The definition now says so; the earlier wording read as two separate groups.
  - "American university students" became "undergraduates at one university". The source says
    only "Washington University undergraduates".
  - The 20-minute talk in must_know now has a quote behind it.
  - B0-R0-C04 added to `ground_floor_deps`, because the record uses percentage points.
  - Four readability warnings fixed.
- `check/records/S57/S57-R1-C02.yml`: derivable, quantitative. Textbook anchors are OpenStax §1.4
  (the one-difference rule, lurking variables, random assignment, control group) and the Cochrane
  Handbook §6.5.1.1-6.5.1.2 (MD, SMD in words, pooled SD / Hedges' adjusted g, Glass's delta,
  scale direction, "effect size"). Off-type references carry quotes: Freeman 2014 (0.47 from 158
  comparisons, Table 1, volunteers, test timing varied, "about 6%"), Deslauriers 2019 (Table 1
  baseline midterm means and SDs of the randomised groups; the test was at the end of class),
  Roediger & Karpicke 2006 (Experiment 2 means and d = 1.22 and 1.26), and Agarwal 2021 (only
  for the name "Cohen's d").
- Figure `s57-r1-c02-md-and-sd.png`: bars at 58 and 66 (made-up), with a band from 58 to 74
  marking one SD of 16. I looked at it and at the redrawn `s57-r1-c01-reversal.png`.
  `draw.py --book S57-R1` redrew all 12 of the book's figures from their own specs. It reported
  0 problems.

`build.py --check`: blocking 0 for the whole corpus at the last run. My two records have no
warnings. Every quote in both records (32 and 49) was found in its source file by script, whitespace
normalised. Every practice and worked line was recomputed in Python
(`/home/claude/scratch-b1/verify.py`).

## Unsourced, or needing a decision

- The SMD formula is derived from the Cochrane Handbook's definitions in words ("relative to the
  between-participant variability"; "the same proportion of the standard deviation"). The image
  formula is not held. The record says published SMDs use an exact formula this book does not
  work through.
- Practice L6 works back from Roediger's d to an implied SD, treating d as MD ÷ SD. The paper does
  not give its SDs or how it computed d. The answer says the SDs are implied and rough.
- Practice L9 applies Freeman's 0.47 to an SD of 13.4 taken from Deslauriers's Table 1. The
  prompt says this is a supposition about "your course", not Freeman's data. The held text does
  not say whether Freeman's "about 6%" means percentage points or a per cent of the score. The
  answer says so.
- ASHA is expanded as "accredited social health activists: village health workers". No held
  source defines it. I dropped a clause about the National Health Mission for that reason.
- Made-up numbers are marked as made up where they appear: the before-after batch, the
  two-group delayed test, the L7 and L8 worked answers, the L10 colleague's claim and the
  journalist exercise's company claim.
- Sibling C03 calls Agarwal's effect sizes "Cohen's d" and points to C02. C02 now names Cohen's d
  and Hedges' g as other names papers use for an SMD, citing Agarwal and Freeman.

## Practice-set size (C02): 12

The technique has four moves: the MD with a stated direction, the division by an SD, the two
reversals (MD from an SMD, and SD from both), and reading the sign when the scale runs the other
way. Twelve problems give each move one bare-number rep. They apply it to three real sources, break
it three ways (dividing by the mean, subtracting the wrong way round, a scale where fewer is
better), and carry it into two claims in words. Levels are 1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9 and 10.

## Figures wanted

None beyond those drawn. A later figure could plot SMD against MD for two SDs (lines y = x/16 and
y = x/8), to show the same MD giving two SMDs. The `curves` option can already draw it. I chose
the bar-and-band figure because it shows the one worked case.

## Glossary rows

None of these terms is in `prose/GLOSSARY.md` now. "at random" (B0-R0-C24) is there, and C02 uses
it in that sense.

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| comparison group | the group taught the usual way, against which the new method is compared; OpenStax calls it the control group | `S57-R1-C02` |
| effect size | a name papers often give an SMD; also used loosely for any measure of an effect | `S57-R1-C02` |
| feeling of learning | the learner's own judgement of how much they learned, usually given as a rating | `S57-R1-C01` |
| learning (in S57) | a lasting change in what a person can do, measured by a test after a delay | `S57-R1-C01` |
| lurking variable | anything other than the method that affects the score | `S57-R1-C02` |
| mean difference (MD) | the mean of one group minus the mean of the other, in the test's own unit, with the order stated | `S57-R1-C02` |
| performance (in S57) | what a learner can do during a session or within minutes of it | `S57-R1-C01` |
| random allocation | a chance process decides which group each learner goes into, not the teacher or the learners | `S57-R1-C02` |
| retention interval | the time between study and the test | `S57-R1-C01` |
| standardised mean difference (SMD) | the mean difference divided by the standard deviation of the scores: the gap in standard deviations | `S57-R1-C02` |
| transmission | teaching by telling: the teacher explains, the learners listen and take notes | `S57-R1-C01` |
