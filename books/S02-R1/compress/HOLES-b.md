**Conductor, 24 Sep 2026:** item 6 (C15, table of days 1, 4, 9, 16) is CLOSED: `restore.py` now restores a fence the list names, and the table is back in C15's final text. The C02/C03 tool conflict in batch a is also closed: `build._sentences` now splits before a lower-case symbol that opens a sentence, and both validate.

# S02-R1 compression pass, batch b (C10 to C17): holes for the audit

Each item below is a gap from Reader B's cold read that the full-length original does not fill
either, or that is an error or contradiction rather than missing text. It could not be fixed at
step 5c, which writes nothing new. "As it stands" quotes the final text
(`S02-R1-Cnn-final-prose.yml`), or the exercise where the gap is in one. Gap ids refer to
`COLD-READ-GAPS.md`, and decisions to `RESTORE-DECISIONS-b.md`.

## 1. C10, must_know[3].point (and illustration.analogy_breaks_when): the addability test lets through what it forbids (B-C10-3)
- **As it stands:** "Add or scale rows only when every entry means the same thing, in the same
  unit, in the same place. Food grams add. Two patients' rows do not."
- **What is wrong:** two patients' rows do pass that test, since each entry means the same thing
  in the same unit and place. The real reason is the original's: the sum "describes nobody".
  Adding is meaningful when the sum of the quantities is itself a quantity (grams of a meal),
  which a sum of ages or heights is not. The original's analogy paragraph has the same wording.
- **To close it:** restate the test so that it asks whether the entry-by-entry sum (or multiple)
  is itself a meaningful amount. Keep "Food grams add. Two patients' rows do not." as its
  examples.

## 2. C10, definition.text: dot product of unequal lengths (B-C10-5)
- **As it stands:** "The dot product of two vectors of the same length, written a · b and said
  "a dot b", is a single number." Only addition gets an explicit "Vectors of different lengths
  cannot be added."
- **What is missing:** a statement that no dot product exists for vectors of different lengths.
  P4(1) asks for exactly that.
- **To close it:** add a matching sentence after the dot-product definition.

## 3. C12, several fields: fitting, predictor, effect, model never taught (B-C12-1)
- **As it stands:** definition.text "the table no longer fixes the weights on a weighted sum of
  all of them together"; Exercise 1 "All four were entered together as predictors of weight
  change"; P13 "fat intake had no effect on weight gain"; must_know[5].point "found no effect of
  fat once calories were accounted for ... the model had no way to find an effect of fat".
- **What is missing:** what fitting a model means, what a predictor is, and what "an effect ...
  once X is accounted for" means (the weight on a column with the others held fixed). The
  original never teaches them. The restored score example gives the plain version: nobody can
  say whether the score "comes from" energy or from the grams.
- **To close it:** one short paragraph, or a pointer to where the book defines them, tying
  "predictor" to a column, "fitted model" to weights chosen from the rows, and "effect of X with
  the others accounted for" to X's weight. Or cut the exercise wording back to the section's own
  terms.

## 4. C12, P14: "ash" undefined (B-C12-7)
- **As it stands:** "That is 100 minus water, protein, fat and ash, all in grams."
- **What is missing:** "ash" (the mineral residue left after burning) is not defined in the
  original either.
- **To close it:** gloss it in the prompt.

## 5. C13, definition.text, illustration.analogy_breaks_when and P9: "model", "values overlap", "range" (B-C13-2, B-C13-3, B-C13-4)
- **As it stands:** "A probability distribution is a model." against "The village is made up,
  and the distribution is exact only because the whole village was listed." Also "The values
  listed must not overlap." P9 says "Work out the range of X".
- **What is wrong:** (a) a distribution computed from a complete list is called both a model and
  exact, and P10 asks which of two numbers is the model. (b) Single values cannot overlap; only
  bands can, as must_know[1] shows. (c) "Range" has already been used in this book for a
  function's outputs (C09); here it means the interval X can take.
- **To close it:** (a) say that a distribution is the model and a survey is data, and that the
  model can be known exactly when the whole population is listed. (b) Write "The values or bands
  listed must not overlap." (c) In P9, write "the interval of values X can take".

## 6. C15, illustration.body: 9 days becomes 16 without a word (B-C15-2; tool conflict)
- **As it stands:** "Over 9 days the square root of 9 is 3." [900] ... [2700] "Divide by the
  days to get the error in the average day. In the first case it shrinks: 300 divided by the
  square root of 16 is 75 kcal a day."
- **What is wrong:** the example switches from 9 days to 16. In the original, the 16 comes from
  a table of days 1, 4, 9 and 16. That table follows a fenced block directly, so `restore.py`
  cannot bring it back (see the tool conflict in `RESTORE-DECISIONS-b.md`).
- **To close it:** re-admit the original's table (fixer or conductor), or make the sentence
  consistent with 9 days: 900 divided by 9, which is 100, that is 300 divided by the square root
  of 9. The figure caption already refers to 16 days, so the table is the smaller change.

## 7. C14, definition.text: "ordinary mean only when all the values are equally likely" (B-C14-2)
- **As it stands:** "It is the ordinary mean of `B0-R0-C28` only when all the values are equally
  likely."
- **What is wrong:** in the village, the values are not equally likely (5 has 0.3), yet E[X] =
  5.0, the ordinary mean of the ten households. What must be equally likely is each case
  (household), not each distinct value. The original's cut sentence even says so: "because every
  household was equally likely". must_know[1] ("Averaging the possible values ... only when every
  value is equally likely") is correct, because it averages the distinct values.
- **To close it:** make the definition say "the ordinary mean of the listed cases when every case
  is equally likely", or "the ordinary mean of the distinct values only when all the values are
  equally likely", and keep the two senses apart.

## 8. C15, must_know[4].point: dependence said only to shrink the spread (B-C15-3 residue)
- **As it stands:** "A before-and-after change, or a predicted-minus-actual difference, can then
  spread much less than the adding rule says. Do not call a reported spread wrong only because it
  fails the rule on paired figures."
- **What is missing:** that dependence can also make a spread larger than the rule says. For a
  difference, it is larger when the two parts move in opposite directions. P18 needs this: its
  784 is above the rule's 747.
- **To close it:** "can then spread much less, or more, than the adding rule says", with the
  direction for a difference stated once.

## 9. C15, definition.text: Var(X) never related to Book 0's n − 1 rule (B-C15-4)
- **As it stands:** Var(X) is defined only as a probability-weighted sum. Book 0's D5 computes a
  sample's standard deviation with n − 1.
- **What is missing:** one sentence saying that the n − 1 figure is a statistic that estimates σ,
  as a sample mean estimates E[X] (the pattern of C14).
- **To close it:** add that sentence, pointing to D5.

## 10. C15, P8 and P17: "precision of 5%" and "within 50" (B-C15-6, B-C15-7)
- **As it stands:** P8 "give doubly labelled water 'a precision of' about 5%"; P17 "accurate to
  within 50 kcal per item".
- **What is wrong:** P8 needs "precision" read as a percentage of the expenditure (relative),
  and the text never says so. P17 does not say whether 50 is a standard deviation or a maximum
  error, and the answer turns on it.
- **To close it:** gloss each in its prompt (P8 "5% of the expenditure"; P17 "read 50 as a
  standard deviation" or "as a worst case").

## 11. C16, definition.text: evaluate and collect are not named moves (B-C16-1 residue)
- **As it stands:** the list of moves is substitute, rearrange, divide by a time interval and
  shrink it, differentiate or integrate, assume.
- **What is missing:** putting a number in (P5, P7) and collecting like terms (P3) are not
  named. Substitute and rearrange can be stretched to cover them, but the text does not say so.
- **To close it:** say that putting in a value is a substitution and collecting terms is a
  rearrangement, or list them.

## 12. C16: "infinitesimal" and "passive" undefined (B-C16-3)
- **As it stands:** P8 quotes Chow and Hall's "take the limit of infinitesimal change";
  must_know[4].point "as the passive fall in expenditure is for the 3500 kcal rule".
- **What is missing:** neither word is defined in the original. "Passive" is the same gap as
  Exposed-4 (item 18).
- **To close it:** gloss "infinitesimal" as "shrinking towards zero" (the limit of C02). Define
  "passive" once, in C03 (item 18), and point there.

## 13. C16, illustration.body, line 2: a differentiation labelled as an assumption (B-C16-4)
- **As it stands:** "dES/dt = 3500 × dW/dt (line 2: assumed, 3,500 kcal in every pound)".
- **What is wrong:** the premise is that stored energy changes by 3,500 kcal per pound, ΔES =
  3500 × ΔW. The rate form follows from it by a named move (differentiate, or divide by the
  interval and shrink it). A section that teaches "name every move" hides one here.
- **To close it:** split line 2 into "ES change = 3500 × W change (assumed)" and "dES/dt = 3500 ×
  dW/dt (differentiate both sides)", and renumber the lines, or say in the where-clause that the
  line folds the two together.

## 14. C17, Exercise 1: three equations the reader cannot see (B-C17-2)
- **As it stands:** candidate 9 "Equation 5 of Polidori and colleagues 2016, which adds an
  integral term"; "Equations 1 and 2 of Chow and Hall 2008" and "Hall's 2008 equation for the
  energy density of weight loss".
- **What is wrong:** none of the three is printed in the book, the original included. "Choose any
  ten" out of ten candidates forces candidate 9 unless the reader brings one from outside.
- **To close it:** print Polidori's Equation 5 in the prompt (checked against the paper), or
  offer eleven or more printed candidates. Mark the other two as optional and outside the
  book's text.

## 15. C17, definition.text: identity and definition overlap (B-C17-3 residue)
- **As it stands:** "An identity holds for every value of its symbols, because of how its
  quantities are defined or because a conservation law requires it." and "A definition brings in
  a new quantity as a combination of others."
- **What is wrong:** "because of how its quantities are defined" also describes a definition, so
  TEE = BMR × PAL can be sorted either way. The restored "a definition rearranged and then used
  to estimate ..." helps with candidate 3 but does not remove the overlap.
- **To close it:** keep "identity" for the conservation case (and for equations that hold
  whatever each quantity's definition). Say that a definition rearranged is still a definition.

## 16. C17, illustration.body: "the consultation" and the women's fitted-on count (B-C17-4)
- **As it stands:** "They come from Schofield, and the consultation "decided to retain" them."
  Later, "Assumes, or fitted on: Schofield's measured men, 2,879 in this band."
- **What is missing:** "the consultation" (the FAO/WHO/UNU expert consultation behind the 2004
  report) is never named as such. Only the men's count for ages 18 to 30 is given, so a reader
  who picks candidate 4 (women, 18 to 30) cannot fill in "fitted on".
- **To close it:** name the consultation once. Give the Table 5.2 count for women aged 18 to 30,
  checked against the source.

## 17. Book 0 C3 (cited in C12 as `B0-R0-C17`): only two unknowns (Exposed-1; residue of B-C12-2)
- **As it stands:** Book 0 teaches two equations in two unknowns. C12's "Find the weights from as
  many rows as there are weights" needs k in k. The restored "With more, look for rows in which
  every column but one is zero ..." covers only that special case.
- **To close it:** C12 could say outright that this book solves more than two only in that
  special case, or Book 0 could extend elimination to three unknowns. This is for the audit of
  Book 0 and C12 together.

## 18. S02-R1-C03 (batch a) and C16: "passive" undefined (Exposed-4)
- **As it stands:** C03 "passive compensation"; C16 "the passive fall in expenditure".
- **What is missing:** a definition: the change in expenditure that follows a change in weight
  without the person doing anything differently.
- **To close it:** define it at first use in C03, and point to it from C16.

## 19. Book 0 D6 and C15: the square-root law is never derived (Exposed-3; residue of B-C15-1)
- **As it stands:** D6 states the √n law. C15's "Their mean has standard deviation σ divided by
  the square root of n, which is the square-root law of `B0-R0-C29`" rests on the adding rule.
  That rule is now checked on one example (the dal pairs) but is derived nowhere.
- **To close it:** either a general derivation of Var(X + Y) = Var(X) + Var(Y) for independent X
  and Y in C15 (the √n law then follows in two lines from the a² rule, which is derived), or a
  sentence saying that the book checks the rule and does not prove it.
