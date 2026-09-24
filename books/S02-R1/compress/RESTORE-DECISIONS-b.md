# S02-R1 step 5c, batch b: restore decisions (C10 to C17)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (Reader B, the
"Exposed in earlier text" items and the flagged worked answers), and `<S>-original.md`,
`<S>-prose.yml` and `<S>-pass1-prose.yml` for C10 to C17. The restore lists are in
`restore-lists/S02-R1-Cnn.txt`, and each restored line is commented with the gap it closes. The
outputs are `S02-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and checked by
`check/compress/validate.py`. The tools were not changed. Batch a (C01 to C09) was not touched.

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means it was not closable here and is written up in `HOLES-b.md` (item number
given). **not a defect** means nothing to do. Where a restore closes most of a gap and leaves a
residue the original never filled, the residue is a hole and is numbered too.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → final | Validate |
|---|---|---|---|---|---|---|
| C10 | 1743 | 883 | 1020 | +137 | 12.02 → 11.53 | OK |
| C11 | 1823 | 1047 | 1137 | +90 | 13.02 → 12.86 | OK |
| C12 | 2114 | 1146 | 1362 | +216 | 13.77 → 12.53 | OK |
| C13 | 1570 | 924 | 941 | +17 | 12.58 → 12.58 | OK |
| C14 | 1797 | 971 | 1144 | +173 | 12.21 → 11.70 | OK |
| C15 | 2396 | 1283 | 1791 | +508 | 12.53 → 12.20 | OK |
| C16 | 1941 | 1048 | 1073 | +25 | 12.64 → 11.75 | OK |
| C17 | 1539 | 843 | 918 | +75 | 11.98 → 11.07 | OK |
| **Total** | 14923 | 8145 | 9386 | +1241 | | 8 OK |

The longest sentence did not rise anywhere. In C17 it went from 24 in the cut back to 32, the
original's own longest, because "One printed equation can mix kinds ..." was restored (C17-3).
C15 takes the largest share (+508). Its gap 1 was one of the reader's two highest-severity gaps,
and the original's two demonstrations of the section's title claim are long.

`python check/build.py --check` / `--subject S02-R1` (PIPELINE step 5c's last line) was not run
here. It needs the final text written back into the records, and that is outside this brief.

## Tool conflict (C15): needs the conductor's decision

`restore.py` brings back a fenced block only if the cut kept it, or if the prose paragraph
immediately before it had a sentence restored. In C15 `illustration.body`, the original's table
of error against days (rows 1, 4, 9 and 16) comes straight after the `300 times 9 = 2700` fenced
block, with no prose between them. So no restore list can bring it back. That table is the only
place the original gets from "Over 9 days" to "300 divided by the square root of 16" (gap
B-C15-2). The list was not worked round. The gap is carried to `HOLES-b.md` (item 6) so that
the fixer can re-admit the table or make the text consistent.

## C14: a restore dropped because it failed validation

For B-C14-1, the original's general proof of E[X + Y] = E[X] + E[Y] ("The second rule follows by
working outcome by outcome ...", six sentences, one of 28 words) was tried first. It raised the
mean sentence length to 12.42, above the original's 12.21, and `validate.py` failed it. The list
now restores the original's worked case of two dependent days instead ("Does the sum rule need
the days to be independent? ..."). That case also shows X + Y row by row. It passes at 11.70.

## Gap by gap

### C10
- **B-C10-1** restored: "The dot product is a weighted sum of the entries of one vector, with
  the entries of the other as the weights."
- **B-C10-2** restored: the patient rows and "Take the same patient a year later ... Subtract
  entry by entry." with its working, and "The change vector y − x is (1, −3, 0, −4)." This is the
  only place the original shows subtraction. With scaling, that is enough to work 2u − 3v in P2.
- **B-C10-3** hole, HOLES 1. The original gives the same rule and the same counterexample. The
  test as worded does not exclude two patients' rows, so it is an error in the rule, not missing
  text.
- **B-C10-4** not a defect. P14 is the demonstration (find two gram vectors that both give 510
  kcal). The kept statement and the dot product are all it needs. The original only adds a
  second assertion ("So two foods ... can differ in every nutrient").
- **B-C10-5** hole, HOLES 2. The original, like the cut, defines the dot product only for equal
  lengths and never says it has no meaning otherwise.

### C11
- **B-C11-1** restored in C10: "A single number used this way is called a scalar." The cut had
  removed the definition from C10, and C11 uses the word.
- **B-C11-2** restored: "Column by column, 65 lots of the slope column plus 1 lot of the
  intercept column:" with its working, and "The same vector comes out." This shows the column
  reading that P3 asks for.
- **B-C11-3** restored: "That is the reference man of the Indian Council of Medical Research and
  National Institute of Nutrition (ICMR-NIN), in its 2020 requirements." This expands ICMR-NIN
  and says what a reference man is (P7's reference woman follows).
- **B-C11-4** not a defect: artifact G0 of the cold-read set (the book's reader has Book 1).
- **B-C11-5** not a defect. P6 asks only whether each product exists and its size. The kept rule
  "If A is m × r and B is r × n, then AB is m × n" answers all four parts.
- **B-C11-6** restored: "They were fitted to a large international set of measurements, and
  ICMR-NIN's note says that for Indians they can overestimate BMR by 10 to 12%." (analogy). The
  cut had removed both of the original's statements of the 10 to 12%.
- **B-C11-7** restored by the same sentence. The record's answer to P15 computes 10 to 12% of a
  prediction, so the problem does have something to compute once the figure is in the text.

### C12
- **B-C12-1** hole, HOLES 3. The original never teaches fitting, predictor, effect or model
  either. The sentence restored for B-C12-4 ("Handed only the table and the scores, nobody can
  say whether the score 'comes from' energy or from the grams.") gives the plain meaning of "no
  longer fixes the weights". The terms themselves remain.
- **B-C12-2** restored: "With more, look for rows in which every column but one is zero, because
  each such row gives one weight on its own." This is the original's method beyond two weights,
  and the illustration uses it. Residue: solving k equations in k unknowns in general is taught
  nowhere (Exposed-1, HOLES 17).
- **B-C12-3** restored: "If the rows you picked repeat each other, so that their equations have
  infinitely many solutions, pick another row."
- **B-C12-4** restored: the score example, from "Here is what that does to any sum built from all
  four columns." to "All three give 460 on row 3, and they agree on every other row too." with
  its three workings, then "Handed only the table and the scores ...". This demonstrates moving
  weight in proportion, which P9 asks the reader to do.
- **B-C12-5** restored: "A column that is nearly, but not exactly, a weighted sum of others is the
  problem called collinearity."
- **B-C12-6** restored: "Three United Nations bodies wrote the report *Human energy requirements*
  together in 2004." This is the antecedent of "The report defines ...".
- **B-C12-7** hole, HOLES 4 ("ash" in P14 is undefined in the original too). "Almost" in "almost
  any column fits exactly" is correct as it stands (degenerate rows), and is not a defect.

### C13
- **B-C13-1** restored: "A person whose true weight is anywhere from 69.95 kg to 70.05 kg sees
  70.0 on it." This shows where the half-step comes from, so P9's 0.2 kg step can be done.
- **B-C13-2** hole, HOLES 5. The original says the same two things ("is a model"; "exact only
  because the whole village was listed"). The tension is in the wording, not in missing text.
- **B-C13-3** hole, HOLES 5 ("The values listed must not overlap" is the original's wording too).
- **B-C13-4** hole, HOLES 5. This is exercise wording, which the pass does not touch.

### C14
- **B-C14-1** restored: the dependent-days case, from "Does the sum rule need the days to be
  independent?" to "The two days could hardly be more dependent, and the rule still holds." with
  its table and workings. It shows the sum rule holding without independence, and X + Y worked
  row by row. The general proof failed validation (see above).
- **B-C14-2** hole (error), HOLES 7. The original has the same definition sentence, and it
  conflicts with the village.
- **B-C14-3** not a defect. No exercise, and no later section of this book, takes the expected
  value of a continuous variable. The original's two scope sentences would inform the reader but
  would not enable anything.
- **B-C14-4** not a defect for this step. The phrase is in the figure caption. PIPELINE's figure
  plan runs next on the compressed text, and a figure that relies on something the cut removed
  is a spec to fix, never a sentence to restore. For the figure planner: the caption and the
  label "E[X] = 70, the balance point" of `s02-r1-c14-surplus-balance.png` have no antecedent in
  the final text.
- **B-C14-5** restored: "A real person's daily surplus has no known distribution." and "It also
  drifts as their weight and habits change, and then '7 times 70' no longer describes the week."
  This gives the route of the record's answer to P14: the per-day expectation does not stay at
  100 as weight rises.

### C15
- **B-C15-1** restored, in two parts. (a) The pair-listing check of the adding rule, from "Work
  out its distribution by listing the pairs." to "It agrees.", with its workings and table. (b)
  The derivation of Var(aX + b) = a² Var(X), from "Why does the standard deviation scale by 4.184
  ..." to "The standard deviation, its square root, is 4.184 times the standard deviation in
  kcal." These are the original's two demonstrations of the section's title claim. Residue: the
  adding rule is checked on one example, never derived in general (with Exposed-3, HOLES 19).
- **B-C15-2** hole, HOLES 6. The original bridges 9 days to 16 only through a table that
  `restore.py` cannot restore (see "Tool conflict").
- **B-C15-3** restored: "A correction term, the covariance, enters, and S03-R1 teaches it." and
  "Do not call a reported spread wrong only because it fails the rule on paired figures." This
  second sentence is the route for P18. Residue: the original says dependence makes the spread
  "much less" and never says it can make it more, as P18's 784 > 747 needs (HOLES 8).
- **B-C15-4** hole, HOLES 9. The original never relates Var(X) to Book 0's n − 1 sample rule.
- **B-C15-5** restored: "A real scale also has systematic error, the kind `B0-R0-C30` separates
  from random error." and "If the scale reads 5 grams heavy every time, that 5 grams sits in both
  readings and cancels in the difference." Together they show the shared error cancelling, which
  P15 turns on.
- **B-C15-6** hole, HOLES 10 (exercise wording).
- **B-C15-7** hole, HOLES 10 (exercise wording; the original never explains relative precision).
- **Exposed-2** restored here: "Two random variables are independent when every event about one
  is independent, in the sense of `B0-R0-C25`, of every event about the other." This is the
  original's extension of Book 0's event independence to random variables. C14 uses the word
  first, but only to say that the rule does not need it.

### C16
- **B-C16-1** restored: "Divide by a time interval and shrink it: turn a change over an interval
  into a rate at an instant, the derivative of `S02-R1-C02`." This is the move P8 needs. Residue:
  "evaluate" and "collect terms" are not named moves in the original either (HOLES 11).
- **B-C16-2** not a defect. C15's kept text says "Hall and colleagues wrote a consensus statement
  on energy balance", and C16's kept text says "Hall and colleagues reject line 4". The panel and
  its rejection are both in the reader's text.
- **B-C16-3** hole, HOLES 12. The original never defines "infinitesimal" (it appears only in P8's
  quote) or "passive" (with Exposed-4).
- **B-C16-4** hole (error), HOLES 13. The original labels the same line "assumed".

### C17
- **B-C17-1** not a defect (the reader's own note: the concept is not quantitative).
- **B-C17-2** hole, HOLES 14. The original prints none of the three equations either.
- **B-C17-3** restored: "One printed equation can mix kinds: a model assumption with a fitted
  constant, or a definition rearranged and then used to estimate a quantity from inputs that are
  themselves fitted or adopted." and "Each part is then checked by its own kind." (candidate 3).
  Also "Take the Atwater factors of `S02-R1-C10`: 4, 9 and 4 kcal a gram.", "They are averages of
  measurements, rounded, and then adopted by agreement." and "So they are fitted and then fixed
  by a body." (candidate 5). Residue: the identity's "because of how its quantities are defined"
  still overlaps the definition (HOLES 15).
- **B-C17-4** hole, HOLES 16. The original explains neither "the consultation" nor the women's
  fitted-on count. "Schofield" is not a defect: "They come from Schofield" is all a notebook
  entry needs.
- **B-C17-5** not a defect. "Use ICMR-NIN's figures" is clinical advice that points to ICMR-NIN's
  own tables. The book's text gives the two 5% cuts (C11) and the PAL change from 1.53 to 1.40
  (C17 must-know). No exercise needs more.

### Exposed in earlier text
- **Exposed-1** hole, HOLES 17 (Book 0; see also B-C12-2).
- **Exposed-2** restored in C15 (see above).
- **Exposed-3** hole, HOLES 19 (Book 0 D6; C15's restored check covers one example only).
- **Exposed-4** hole, HOLES 18 (C03, batch a's section; also C16).
- **Exposed-5** not a defect: artifact G0.
- **Exposed-6** restored by B-C11-3: C11 now expands ICMR-NIN at its first use.

### Flagged worked answers
- **C11 P14** not a defect. The record's answer already says that dividing by 1.10 is multiplying
  by about 0.909, not 0.90, and it names both readings. Reader B agrees with it.
- **C16 P13** not a defect. The record's answer says the colleague's 26.6 is right arithmetic
  and that a mean of products is not a product of means. Reader B agrees with it.
- **C14 P14** counted under B-C14-5 (restored).

## Tally

52 items: 44 of Reader B's gaps, 6 exposed items, and 2 flagged answers (C14 P14 is counted
under B-C14-5).

- Restored: 22 (C10 2, C11 5, C12 5, C13 1, C14 2, C15 3, C16 1, C17 1, Exposed 2).
- Hole: 19 (C10 2, C12 2, C13 3, C14 1, C15 4, C16 2, C17 2, Exposed 3), plus 5 residues left by
  partial restores (HOLES 8, 11, 15, and the residues of B-C12-2 and B-C15-1 folded into HOLES 17
  and 19).
- Not a defect: 11 (C10 1, C11 2, C14 2, C16 1, C17 2, Exposed 1, flagged 2).
