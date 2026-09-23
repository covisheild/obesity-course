# Holes in Part D the original did not fill (compression pass, step 5c)

Source: COLDREAD-REPORT-part-D.md. Each item below is a gap the cold reader found where the full-length original is also silent or wrong, so nothing could be restored. These go to DEFECTS.md and back through the audit (claude.md §12, "The second output").

## D1
- D1 must_know[3]: "Every probability, complement and odds you compute from a ceiling is itself a ceiling." — wrong: 1 minus a ceiling is a floor. The section's own analogy_breaks_when (now restored) says 0.25 is "the smallest the chance of not being covered could be", so the section contradicts itself. Affects D1 P4, and carries into D2 P13 through D2 must_know[4].
- D1 illustration.body: "It shall extend up to seventy-five per cent. of the rural population, and up to fifty per cent. of the urban population." — never says whose rural population (national, state or district). Affects D1 P9 ("rural people here"): the reader cannot say whether a local figure is bounded by it.
- D1 illustration.body: "It shall extend up to seventy-five per cent. of the rural population" — the full stop after "per cent" is the statute's own punctuation, but it reads as a typo. Needs Harsh's decision on whether to mark it [sic] or explain it. No exercise blocked.

## D2
- D2 must_know[4]: "Carry the same "at most" or "at least" through every step." — wrong across any "1 minus" step, where the direction flips. Affects D2 P13, where following the rule gives "at most 0.25" and points the conclusion the wrong way.
- D2 illustration.body: "Go by the complement instead: work out the probability that none of the three is covered, and subtract that from 1." — the step assumes the three "not covered" events are independent because the "covered" events were, and never says so. The working never labels where the bound turns from a ceiling to a floor and back. Affects P3, P8, P11.
- D2 definition.text: "Independence is checked, not assumed: A and B are independent exactly when P(A and B) — the probability that A and B both happen — equals P(A) times P(B), and dependent otherwise." — the illustration has no joint figure, so this check cannot be run there. The text never shows what evidence counts when all you have is a ceiling. Only the informal question "does knowing one change the other?" is offered. Affects Exercise 1 and P12. (must_know[0]'s "If you have not tested it and cannot argue for it directly, assume the events are dependent" goes part of the way. Restoring it pushed the mean sentence length above the original's, so it was withdrawn.)
- D2 illustration.body: "If the household is covered, every person belonging to it is covered along with it." — asserted, and nothing quoted from the Act anywhere in A to D says that coverage is decided per household. Affects P7, P10, P13.
- D2 simplified_explanation: "Two tosses give 2 squared outcomes, three tosses give 2 cubed, and n tosses give 2 to the power n." — "cubed" is never named before this, and A6 names only "squared". Minor. Affects P1.
- D2 practice P5: "Two fair coins are tossed" — "fair" is never defined, and the counting method depends on equally likely outcomes. Affects P5.

## D3
- D3 illustration.body: "The study's Table 3 reports a 31.3 centimetre arm cut-off for men, labelled "overweight, body-mass index 25 or more"." — "cut-off" is never defined, and "the tape" is never introduced. Affects every problem that uses the arm measurement.
- D3 illustration.body: "Sensitivity of 86 per cent should mean some whole number of the 52 caught by the tape." — the step that picks the candidates (0.86 × 52 = 44.72, then take the whole numbers on either side) appears only later, for the 42. Affects P6 and P11 (P11's trap is exactly the choice of candidate).
- D3 illustration.body: "Try the 42 men in the 25-to-29.9 band on their own, against the other 89 men in the study." — the 89 includes the 10 men at 30 or more, who then count as "not in the band". An obese man flagged by the tape becomes a false positive, and the 61 per cent PPV counts him as a wrong result. The text never says so. Affects P7, P8, P12, P13 and the meaning of the section's headline figure.
- D3 illustration.body: "This second ratio is the sensitivity, and it is the number the paper itself reports." — this agreement is circular, because 36 was chosen to reproduce 86 per cent. The text never says that the PPV of 61 and the NPV inherit that inference. Affects P7, P8.
- D3 illustration.body: "The figure of 1,000 keeps the arithmetic in whole people." — never says what to do when the products do not come out whole (36.08, 286.7). Affects P7, P12.
- D3 must_know[6]: "When two published figures for the same measurement disagree, check whether either one conflicts with something else printed alongside it." — never demonstrated in D3. Affects P10 and Exercise 2.
- D3 Exercise 2: "Say how you would check which of the two women's figures, 30 or 28 per cent, the paper's own numbers are actually built on." — no women's body-fat count, percentage or distribution appears before D5. Blocks Exercise 2 at the "which numbers" step.

## D4
- D4 simplified_explanation: "A set that is perfectly symmetric can be made to look like it has a heavy tail just by moving the bands." — "heavy tail" is never defined. Only "long tail" is. Minor.
- D4 illustration.body: "These four bands are the ones the World Health Organization drew, for its own reasons." — the WHO is never introduced, and the reader cannot check "not centred on where these 282 students' body-mass index actually sits". Affects P10.
- D4 illustration.body: "Two students landing in different bands is a real difference between people." — contradicts the section's own third source: two students on either side of 25.0 can differ by measurement alone. Affects P4(a), P7.
- D4 practice P7: "minimum inter-observer variation" — "inter-observer" is never defined, and the three sources never mention observers. Affects P7.
- D4 practice P11: "ranges from underweight to 30 or more" — "underweight" is never defined. Exercise 1 also uses "average" before D5 defines the mean. Affects P11, Exercise 1.

## D5
- D5 practice P6: "Give the variance and the sample standard deviation" — "the variance" is ambiguous between the sample form (divide by 4) and the population form (divide by 5). Affects P6.
- D5 illustration.body: "The mean of the group, 24.2, sits under the line at 25." — "the line at 25" is a cut-off the section never sets up. Minor.
- D5 illustration.body: "A smaller number of men, with a much higher body fat percentage, pull the mean up past them." — states as fact what mean > median only suggests. Affects how P7 and P16 are worded.
- D5 illustration.body: "Both rows fail the same way, and each one passes against the other row's numbers." — wrong: they fail in opposite directions (the weight median is below both quartiles, the height median above both). Affects P13.
- D5 practice P10: "Work out how many standard deviations above the mean his reading would sit." — the operation (the difference divided by the SD) is never taught. Blocks P10.
- D5 must_know[6]: "Where the mean and median disagree by much, look at the quartiles instead of trusting a single standard deviation to describe both sides." — the text never shows how to read the two quartile distances as a sign of a tail. Affects P9.
- D5 practice P16: "most men have a body fat percentage somewhere between 20 and 24" — no SD or quartiles for men's body fat appear anywhere, so the claim cannot be tested with numbers. Affects P16.
- D5 must_know[0]: "A long tail on one side of a distribution pulls the mean toward it." — only the mean-above-median case is worked. The reverse, which P11 asks for, is never shown. Affects P11.

## D6
- D6 definition.text: "The square-root law describes how far a random sample's average is likely to sit from the average of the population it was actually drawn from." — "likely" is never quantified, and no rule turns a standard error into a range. Affects P7 (the correct interval) and P11 ("reliable").
- D6 illustration.body: "The square-root law would then say something concrete." — never shown. The law is taught only for the average of numeric values, and the spread of a yes/no share (34.8 per cent) is never given. Blocks the numbers in P9, P10, P11.
- D6 illustration.body: "Before recruiting anyone, they set their target using a figure from the National Family Health Survey, NFHS-4, run in 2015-16." — "target", and how a prevalence sizes a study, are never explained. No exercise blocked.
- D6 practice P9: "20% for young adults nationally" — the text never says this. It says only that the figures are "NFHS-4's figures for India" and does not say which ages or which people. The problem's wording goes beyond the section. Affects P9, P10.
- D6 practice P3, P6: solving √n = k by squaring is never shown in D6 (it can be put together from A6 and C2). Affects P3, P6.

## D7
- D7 illustration.body: "Two stated scales are each weighed against it twenty times." — the scales are not what is weighed. The wording is backwards. Read twice, and no exercise is blocked.
- D7 illustration.body: "Yet its average sits further from the truth than scale B's average does: half a kilogram out against seven and a half hundredths." — the subtraction 60.0 − 59.925 = 0.075 is never shown. Minor.
- D7 (whole section): no sentence says how to judge "more systematic" against "more random" from a list of errors (the average error against the spread of the errors). It is only illustrated. Affects P3, P5.
- D7 must_know[4]: "Differences between observers are each observer's own systematic habit." — asserted, and never shown with numbers. Affects P12.
- D7 illustration.body: "> Weight and height were recorded with accuracy of 100 g and 0.1 cm." — the text never says what this resolution means for the study's own derived figures (for example BMI). The thread is left open. No exercise blocked.
