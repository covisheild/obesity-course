# Triage of HOLES-part-D.md (Task 3 audit, 2026-09-23)

One line per hole. Defect IDs point to books/B0/defects/<RECORD-ID>-compression.md.

## D1 (C24)
- must_know[3] "is itself a ceiling": CONFIRMED-ERROR. The complement of a ceiling is a floor (C24-K1).
- whose rural population: CONFIRMED-GAP. The Act names no State or district, and s.9 leaves each State's share to the Centre. The P9 answer's "national" is not in the Act (C24-K2).
- "per cent." full stop: NEEDS-HARSH. The sentence is paraphrase, not a marked quotation, and it adds a comma the statute lacks. Suggest either quoting it exactly with [sic], or paraphrasing it without the stop.

## D2 (C25)
- must_know[4] "same at most / at least": CONFIRMED-ERROR. The direction flips at every "1 minus" step (C25-K1). A related error is in P13 (C25-K3).
- complement step assumes independent non-coverage; bounds unlabelled: CONFIRMED-GAP (C25-K2).
- independence check has no joint figure: CONFIRMED-GAP. A direct argument counts as the check, and the default is "dependent". The source quote is already held (C25-K4).
- household coverage asserted: CONFIRMED-GAP (support). Supported by nfsa s.3(1) and s.10, but not quoted (C25-K5).
- "cubed" undefined: CONFIRMED-GAP, minor (C25-K6).
- "fair" undefined: CONFIRMED-GAP, minor (C25-K7).

## D3 (C26)
- "cut-off" and "the tape" undefined: CONFIRMED-GAP (C26-K1).
- candidate step for 52 and 79 not shown: CONFIRMED-GAP (C26-K2).
- the 89 include the 10 obese men, so the PPV counts them as wrong: CONFIRMED-GAP. 61% is a floor for the "25 or more" question (C26-K3).
- sensitivity agreement is circular: NOT-A-DEFECT. The ABW says the table is rebuilt from two rounded percentages. 36 and 66 are the only whole numbers that fit on the 42/89 split, so the PPV and NPV inherit a unique inference, which is stated.
- 1,000 "whole people" sentence: NOT-A-DEFECT. The sentence is gone from the current text. P7 handles 36.08 by the divide-back method the illustration shows, and P12 uses 900, so its products come out whole.
- must_know[6] never demonstrated: CONFIRMED-GAP. P10's answer demonstrates it, but its prompt lacks 71, 114 and 97 (C26-K4).
- Exercise 2 blocked: CONFIRMED-GAP. The prompt omits Table 3. The answer's "no arithmetic check" is also wrong, because Table 1's quartile 28.1 against Table 2's 114 settles it (C26-K5).

## D4 (C27)
- "heavy tail" undefined: CONFIRMED-GAP. Change it to "long tail" (C27-K2).
- WHO not introduced; "not centred" uncheckable: CONFIRMED-GAP (C27-K3).
- "Two students landing in different bands is a real difference between people": CONFIRMED-ERROR (C27-K1).
- "inter-observer" undefined: CONFIRMED-GAP, minor (C27-K4).
- "underweight" undefined: CONFIRMED-GAP, minor (C27-K5). "average" in Exercise 1: NOT-A-DEFECT, because earlier Parts use it (A1, A3, A5, C4–C8).

## D5 (C28)
- P6 "the variance" ambiguous: CONFIRMED-GAP (C28-K6).
- "the line at 25": NOT-A-DEFECT. D4 (in concept_deps) sets 25 as the paper's cut-off, and this section's own previous paragraph counts the men "of 25 or more".
- "A smaller number of men ... pull the mean up": CONFIRMED-ERROR (overstatement), repeated in P14 (C28-K3).
- "Both rows fail the same way": CONFIRMED-ERROR. They fail in opposite directions (C28-K2).
- P10 operation not taught: CONFIRMED-GAP. Add one sentence to the definition (C28-K7).
- must_know[6] quartile distances not shown: CONFIRMED-GAP. The K3 fix closes it (C28-K4).
- P16 no quartiles given: CONFIRMED-GAP (C28-K5).
- must_know[0] reverse case not worked: NOT-A-DEFECT. must_know[0] is stated for either side, and P11 is its mirror application.

## D6 (C29)
- "likely" unquantified: NOT-A-DEFECT. No exercise asks for an interval. P7 asks only for the broken step, which the answer finds with no range rule.
- "would then say something concrete": CONFIRMED-GAP. The promise is unkept, and "a share is an average" is never said (C29-K1).
- "target" and sizing unexplained: NOT-A-DEFECT. "to size their study" in the same paragraph says what the target is, and sizing is outside D6's outcome.
- P9 "20% for young adults nationally": NOT-A-DEFECT. The line is part of the note under critique, and the answer flags it. The same holds for P10's newsletter line.
- P3 and P6 solving √n = k: NOT-A-DEFECT. D5's definition says "taking a square root undoes the squaring", and A6 and C2 supply the rest.

## D7 (C30)
- "Two stated scales are each weighed against it": CONFIRMED-ERROR (wording, minor) (C30-K3).
- 60.0 − 59.925 not shown: CONFIRMED-GAP, minor (C30-K4).
- no rule for "more systematic" against "more random": NOT-A-DEFECT. The SE defines systematic as "same direction by roughly the same amount" and random as unpredictable, which is the rule P3 and P5 apply.
- must_know[4] asserted without numbers: CONFIRMED-ERROR (overstatement). P12 supplies the numbers, but the claim that all of the difference is habit is too strong (C30-K2).
- resolution thread for derived BMI left open: NOT-A-DEFECT. Nothing asks for it, and propagation of error is outside D7's outcome.

## NEW (found in passing)
- C24-K3: the P9 answer cites s.9 with no refs.
- C26-K6: P9 needs 109 in the prompt.
- C26-K7: P2 uses an independence test D2 never states.
- C27-K6: pointer to D3's abdominal-obesity figures, which are not in concept_deps.
- C28-K1: P15's "a quarter or more ... at 25.6 or above" is wrong.
- C28-K8: EX1 says "more than half" where the median gives "at least half".
- C28-K9: P16 says "at most about half" between the quartiles.
- C29-K2: P7's false "used before" pointer.
- C29-K3: orphan simulated numbers.
- C30-K1: the VIM quotes in the definition have no jcgm_vim3 reference.
