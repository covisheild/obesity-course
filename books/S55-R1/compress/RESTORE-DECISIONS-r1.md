# S55-R1 step 5c, batch r1 (C01 to C04): restore decisions

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (C01 to C04 and the
"Across files" gaps that touch them), and `<S>-original.md`, `<S>-prose.yml` and
`<S>-pass1-prose.yml` for each section. The restore lists are in `restore-lists/S55-R1-Cnn.txt`, and
each restored line is commented with the gap it closes. The outputs are `S55-R1-Cnn-final-prose.yml`,
built by `check/compress/restore.py` and checked by `check/compress/validate.py`. The tools were not
changed. No record was edited and nothing was committed.

Key: **restored** means original sentences were put back because they let the reader do the thing.
**hole** means it was not closable here and is written up in `HOLES-r1.md` for the fixer.
**not a defect** means nothing to do. "Restored, residual" means the restored sentences close what
the reader could not do, and a remaining part of the gap goes to `HOLES-r1.md`.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → cut → final | Validate |
|---|---|---|---|---|---|---|
| C01 | 1236 | 664 | 744 | +80 | 12.27 → 12.09 → 12.24 | OK |
| C02 | 941 | 492 | 586 | +94 | 12.89 → 11.18 → 11.72 | OK |
| C03 | 1168 | 644 | 712 | +68 | 12.85 → 11.14 → 11.36 | OK |
| C04 | 920 | 501 | 545 | +44 | 11.72 → 11.51 → 11.47 | OK |
| **Total** | 4265 | 2301 | 2587 | +286 | | 4 OK |

`python check/build.py --check` / `--subject S55-R1` was not run: it needs the final text written
back into the records, which is outside this step's brief.

## Validation note (C01)

The first C01 build failed: mean sentence length 12.27 → 12.46. The cause was the list, not the
tool: the restored NCD expansion (A-C01-5) is 23 words. It was taken out of the list, and A-C01-5
went to the holes. The rebuild passed (12.24).

## Gap by gap

### C01
- **A-C01-1** restored: "The future-research line at the end of a paper is a good place to find a candidate." It is the
  antecedent of "It was written for the authors' own field".
- **A-C01-2** restored: "A careful sample and a correct analysis answer the question that was asked." It is the
  antecedent of "that question". With it back, "well done and still no use" reads as the original meant.
- **A-C01-3** restored: "You do not yet have the tests that decide between them; the rest of this book builds them."
  The reader now knows the tests come later.
- **A-C01-4** restored: "Knowing how a question arrived tells you only whether it was compared with others." and
  "It does not tell you whether the question is good." Together they let the reader name Ex 1's fault: having the data
  is a route, and a route does not make a question good.
- **A-C01-5** hole (H1): the original expands NCD in the illustration, but restoring that 23-word sentence raised the
  mean sentence length past the original's, and validation failed.
- **A-C01-6** not a defect: "guide" is inferable, and "community medicine" is only setting. No exercise needs it.
- **A-C01-7** restored: "You cannot plan a study from a topic." This is the sentence before "You can plan one", which was
  left dangling.
- **A-C01-8** not a defect: set-up, as the report itself says. The A-C01-3 sentence now says the criteria come later.

### C02
- **A-C02-1** hole (H2): the original has no illustration either. The figure describes one that does not exist.
- **A-C02-2** hole (H3): the original has no "Where this picture breaks" either.
- **A-C02-3** restored, residual (H4): "When they list several risk factors, ask which one they would keep if they could
  only keep one." This gives the reader the move Ex 2 needs: several risk factors, one exposure. The original never
  states the one-exposure rule or defines "risk factor".
- **A-C02-4** restored: "Without a comparison, "children who walk have obesity less often" has nothing to be less often
  than." This tells the reader that an implied "less" still needs something to be less than (Practice 2c).
- **A-C02-5** hole (H5): no cut-off for obesity or overweight in the original, and nothing for children.
- **A-C02-6** not a defect: Practice 9 asks the reader to fence the population, so choosing an age range is the task.
  "Block" is given as a place fence and is not needed to label the parts.
- **A-C02-7** hole (H6): the original has the same definition ("age, and any other trait"). It does not say whether a
  trait alone completes the person fence.
- **A-C02-8** restored, residual (H7): "Morgan and colleagues report, from an earlier review they cite, ..." and "This
  course has not read that review." These are the premises of the dangling "So when you read a paper". The loose "short
  names made from their first letters" is also in the original and goes to H7.
- **A-C02-9** hole (H8): the singular prompt in Practice 6 is in the original. Exercises are not this step's to change.

### C03
- **A-C03-1** restored: "For a relational question it can show an association, but it usually cannot show which of the
  two came first." This explains why a cross-sectional study measures an exposure.
- **A-C03-2** hole (H9): the original has the same describe/relate boundary. Whether a trait like age group counts as an
  exposure is never said.
- **A-C03-3** restored: "So it can find that they go together." (before "It cannot tell you which came first"), plus the
  A-C03-1 sentence. A one-visit survey can show association but not time order.
- **A-C03-4** hole (H10): the original gives no design for a cause question whose exposure cannot be assigned.
- **A-C03-5** restored, residual (H11): "Chance does the deciding, not anything about the people." It is the step
  before "So no third thing can decide who is exposed". The original never says whether chance itself can leave the
  groups unequal.
- **A-C03-6** restored, residual (H12): "It collects and combines the results of all the studies already done on one
  question." This says what a systematic review does. Which kind of question it answers, and its link to C05's
  "reviews" and C06's "meta-analysis", are not in the original.
- **A-C03-7** restored: "When a trainee proposes a trial for a how-common question, ask them what chance would decide."
  This is the subject of the must-know point, which misread as a general rule without it.
- **A-C03-8** hole (H13): the original also says prevalence is "how many people", but every example asks for a share
  (error).
- **A-C03-9** hole (H14): the original has no illustration and no "Where this picture breaks". It never says that a
  cohort starts with people free of the outcome.

### C04
- **A-C04-1** hole (H15): the original's citation is no fuller ("Aslam and Emmanuel credit it to Hulley and colleagues",
  no work, no year). I, N and R are never explained. No exercise uses FINER, so nothing was restored.
- **A-C04-2** restored: "Nobody could answer it in one study." It is the missing premise for "So you narrow it".
- **A-C04-3** restored: "That can be the right move." It is the contrast before "But the study now answers", and it
  presents narrowing to a relate question as a choice, not a forced step.
- **A-C04-4** hole (H16): "enough number" is not quantified in the original either.
- **A-C04-5** hole (H17): the original's feasibility list also omits measuring the exposure.
- **A-C04-6** hole (H18): "small trial" is the original's wording. A pilot is never named.
- **A-C04-7** restored, residual (H19): "That is a group of people at a hospital, college or research body." and "It
  reads a researcher's plan before any research starts, and can say yes, no, or change this first." These define the
  ethics committee. "Protocol" and "health secretary" are undefined in the original too. The missing illustration is
  covered by A-X-1.

### Across files (the parts that touch C01 to C04)
- **A-X-1** hole (H20, and H2, H3, H14): C02, C03 and C04 have no worked illustration in the original either.
- **A-X-2** hole (H21): no original sentence in C01 to C04 assembles what follows the kept question. The batch holding
  C08 may record it too.
- **A-X-3** restored in part, residual (H22): C02's "Writing the question this way has a second use, later." and "When
  you search for what others have already found, you build the search from these same parts." These give task (a) a
  start: build the search from the four parts. No original sentence here gives a search method.

## Counts (C01 to C04 plus A-X-1 to A-X-3)

| | Restored | Hole | Not a defect |
|---|---|---|---|
| C01 | 5 | 1 | 2 |
| C02 | 3 | 5 | 1 |
| C03 | 5 | 4 | 0 |
| C04 | 3 | 4 | 0 |
| Across files | 1 | 2 | 0 |
| **Total** | **17** | **16** | **3** |

Six of the 17 restorations leave a residual that is also written up in `HOLES-r1.md`.
