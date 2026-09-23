# Cold-read report: Part D, pass 1 (D1 to D7)

Reader: an intelligent adult with no background, who has read A1 to A8, B1 to B6 and C1 to C9 (released) once, in order, then D1 to D7. Only /tmp/coldread/ was read. Already known and not reported: there is no answer appendix, and the source files the sections point to are not available.

Gap counts: D1 10 · D2 9 · D3 10 · D4 12 · D5 12 · D6 9 · D7 9 (73 in all).

The three most serious:
1. **The bound direction is taught wrong (D1, carried into D2).** "Every probability, complement and odds you compute from a ceiling is itself a ceiling." This is false for the complement: 1 minus a ceiling is a floor. It contradicts D1 P4, which asks for "the smallest" the not-covered probability can be. D2 then says "Carry the same 'at most' or 'at least' through every step", and a reader who follows that gets the direction wrong on D2 P13.
2. **Prevalence is never named in the D3 worked example.** "Table 2 already gives it directly: 42 of 131." Here "it" points back at specificity. The figure is actually prevalence, which is the hinge of the whole positive-predictive-value lesson. The rebuilt table also quietly counts the 10 men at 30 or more as "not in the band". So a tape flag on an obese man becomes a false positive, and nobody says so.
3. **The square-root law is taught for averages only, never for a percentage, and never turned into a range (D6).** The worked example promises that "the square-root law would then say something concrete" about the 34.8 per cent, and then never says it. A reader cannot give an interval for the true mean in P7, cannot put a number on P9 to P11, and has no way to get the spread of a yes/no share.

---

## D1 · What a probability is

### Exercises

**Exercise 1 (teaching, journalist).** "The seventy-five per cent is not odds, and it is not how many people are covered. It is a ceiling written into section 3(2): coverage can reach *up to* three in four rural people. As a probability, a randomly picked rural person has at most a 0.75 chance of being covered. As odds, that is at most three to one: three covered for every one not covered. The law does not say how many are actually covered."
Printable sentence: "The law lets food-security coverage reach at most three in every four rural people. That is a cap, not a count of who is covered."

**Exercise 2 (critique).** "Odds of 60%" mixes two scales. Odds are a ratio (p divided by 1 minus p) and are not stated in per cent. If 0.6 was meant as a probability, the odds are 0.6 / 0.4 = 1.5, which is "three to two". If 0.6 was meant as odds, the probability is 0.6 / 1.6 = 0.375. Rewrite: "The probability of coverage in this block is 0.6 (six in ten), which is odds of three to two." That wording holds only if 0.6 is a measured block figure. If it came from a legal ceiling, say "at most".

### Practice
1. Red is 5/8 = 0.625 and blue is 3/8 = 0.375. They add to 1.
2. Probability 0.2 gives odds of 0.2 / 0.8 = 0.25. Odds of 1.5 give a probability of 1.5 / 2.5 = 0.6.
3. The complement is 1 − 0.4 = 0.6. The odds are 0.4 / 0.6 = 0.667 (two to three).
4. The probability of being covered is at most 0.75. The probability of not being covered is at least 1 − 0.75 = 0.25. *The text's own must-know says this complement is "itself a ceiling". I had to overrule it by reasoning from "the two add to 1". See gap D1-6.*
5. The odds are at most 0.75 / 0.25 = 3, that is three to one.
6. For urban coverage the odds are at most 0.5 / 0.5 = 1 (evens). The rural probability is 1.5 times the urban one, but the rural odds are 3 times the urban odds. Above one half, odds pull away from probability.
7. The broken step is "odds of 0.25 mean a probability of 0.25". The probability is 0.25 / 1.25 = 0.2, so one in five households, not a quarter.
8. The broken step is "divided by 1 plus probability". The divisor should be 1 minus the probability: 0.6 / 0.4 = 1.5.
9. Compute: 0.75 is a ceiling on the probability, and the odds are at most 3 to 1. The note turns a legal cap into a count ("are covered"). It does not establish how many are actually covered. It also does not establish whether the 75 per cent applies to "here" at all, because the text never says which population the ceiling is measured over (see D1-9).

### What D1 taught me that changes what I do
- I will convert between odds and probability before speaking. Odds of x mean a probability of x/(1+x).
- I will refuse "odds of N%" as a phrase and ask which scale was meant.
- I will say "at most" in the same sentence whenever a figure comes from a statutory "up to".
- I will not apply a group probability to the one person in front of me.
- To a journalist I will say "three in four", not "three to one".

### Gaps
- **D1-1.** "Read on to section 3(2), which sets a ceiling on how many people that entitlement can reach." The illustration never names the Act, and D1 contains no "entitlement" for "that" to point to. "Read on" assumes a document is already open. A reader has to reach back to C9 or A4 to know this is the National Food Security Act, 2013, and that the entitlement is section 3(1)'s 5 kg. It blocks nothing, because the problems name the Act.
- **D1-2.** "Pick one rural person, anywhere the Act covers, entirely at random." The definition gives a probability as a long-run frequency. The plain-terms part says "A probability is a proportion", and counting works only "when every outcome is exactly as likely". The text never makes the bridge: a random pick makes every person equally likely, so P(A) equals the share of the population covered. "At random" is not defined until D6. I supplied the link. This affects Exercise 1 and P4, P5 and P9.
- **D1-3.** "So work with 0.75 as a ceiling on P(A), not a measured figure". The line before this "So" only introduces the P(A) notation. The reason (the statute says "up to", and a legal cap is not a count) is left for the reader to assemble.
- **D1-4.** "Now the trap." No trap is named or shown. The next lines just compute odds correctly. I guessed that the trap is mistaking odds for probability.
- **D1-5.** "Watch it stop." Nothing stops: the urban case works out cleanly to odds of 1. The phrase points at nothing. I read it twice.
- **D1-6 (serious).** "Every probability, complement and odds you compute from a ceiling is itself a ceiling." This is false for the complement: if P(covered) is at most 0.75, then P(not covered) is *at least* 0.25. It contradicts P4 ("the smallest that the probability they are not covered can be"). It also sets up the wrong rule that D2 repeats. This blocks P4, since the text and the problem disagree, and it misleads D2 P13.
- **D1-7.** "Near 0, odds and probability are almost the same number. Above one half they pull apart, and near 1 they pull apart fast: 0.99 to 0.999 multiplies the odds by ten." This is asserted, not worked (99 against 999). I checked it myself. It is partly needed for P6's "what the comparison shows".
- **D1-8.** "A probability describes a group, or a process repeated many times. It does not describe the one person in front of you." The whole illustration, though, is about "one rural person" and their P(A). The text never reconciles the two, so the reader cannot tell how to word Exercise 1 without contradicting one of them.
- **D1-9.** "It shall extend up to seventy-five per cent. of the rural population". It never says whose rural population: national, state or district. A4 P5 applied it to a district without comment. This blocks the "what it does not establish" part of P9 ("rural people *here*"), because I cannot say whether a local figure is bounded by it.
- **D1-10.** "seventy-five per cent. of the rural population" has a stray full stop in the quoted statutory style. I read it twice.

---

## D2 · Counting outcomes; independence

### Exercises

**Exercise 1 (critique).** The claim is missing whether the two residents' coverage is independent. It needs to say whether they come from different, unrelated households, and that 0.75 is a ceiling, so the answer is "at most". If they live in the same household, coverage goes with the household, so P(both) is at most 0.75, not 0.5625.

**Exercise 2 (teaching).** "And" is not a licence to multiply. First ask: does knowing A happened change the chance of B? If yes, the events are dependent and you do not multiply. The formal test is P(A and B) = P(A) × P(B). Example: two coins, where P(HH) = 1/4 = 1/2 × 1/2, so they are independent. Two people in one household: if one is covered, the other is certainly covered, so knowing one changes the other, and you do not multiply. The same caution applies to "or": you add only when the two events cannot both happen.

### Practice
1. HHH, HHT, HTH, HTT, THH, THT, TTH, TTT: that is 8 = 2^3.
2. P(A and B) = 0.6 × 0.5 = 0.3. P(C or D) = 0.3 + 0.4 = 0.7.
3. P(neither) = 0.8 × 0.8 = 0.64, so P(at least one) = 0.36. *This assumes the "not" events are also independent, which is never stated. See D2-4.*
4. 0.5 × 0.4 = 0.2, which equals P(A and B), so A and B are independent.
5. The sample space is HH, HT, TH, TT. P(A) = 2/4, P(B) = 2/4, and P(A and B) = 1/4 = 1/2 × 1/2, so they are independent. *This needs "fair" to mean equally likely, which is never defined. See D2-6.*
6. At most 0.75 × 0.75 = 0.5625.
7. At most 0.75, because the household is covered or not as one unit. That is higher than 0.5625, since the two people are one draw counted twice.
8. P(none) is at least 0.25^3 = 0.015625, so P(at least one) is at most 0.984, about 98.4 per cent.
9. The broken step is adding the probabilities of events that are not mutually exclusive (independent events with non-zero probabilities can both happen). The 1.3 is also impossible, since it is above 1. Correct: 1 − 0.3 × 0.4 = 0.88.
10. The broken step is multiplying for a same-household pair. The answer is at most 0.75.
11. The broken step is adding for "at least one". A probability of 2.25 is impossible. Correct: at most 1 − 0.25^3 = 0.984.
12. For 0.5625 to hold, the two must be independent (different, unrelated households) and each must be covered with probability exactly 0.75. Since 0.75 is a ceiling, the figure is really "at most 0.5625". It does not establish actual coverage.
13. Coverage goes by household (as the text asserts), so "at least one of the four not covered" is the same as "the household not covered". That has probability *at least* 0.25. If you wrongly treat the four as independent, you get 1 − 0.75^4 = 0.684. Neither figure supports "high": all that is known is a floor of 0.25. *If I apply D1's and D2's must-know rules literally ("carry the same at most"), I get "at most 0.25", which points the conclusion the wrong way. See D1-6 and D2-9.*

### What D2 taught me that changes what I do
- I will refuse to multiply just because a sentence says "and". I will ask whether knowing one event changes the other.
- I will treat people from one household (one decision unit) as one draw.
- I will answer "at least one" questions through the complement.
- I will reject any probability above 1 as a sign that something was added that should not have been.

### Gaps
- **D2-1.** "Section 3(2) caps how far that entitlement reaches". As in D1-1, there is no antecedent and the Act is not named in the illustration.
- **D2-2 (serious).** "Independence is checked, not assumed" is followed by "Pick two rural people entirely at random, from two different, unrelated households. Multiply." The illustration multiplies without running the check the definition demands. The check (does P(A and B) equal P(A) × P(B)?) cannot be run here anyway, because no joint figure exists. The text never shows how to "check" independence when all you have is a ceiling: only the informal "does knowing one change the other?" is offered. This blocks Exercise 1 and P12 ("decide what has to be true") at the point of saying what evidence would count.
- **D2-3.** "If the household is covered, every person belonging to it is covered along with it." This is asserted. Nothing quoted from the Act in A to D says coverage is decided per household. C4 and C9 quote only "a person in a priority household". I supplied it. It is needed for P7, P10 and P13.
- **D2-4.** "Go by the complement instead: work out the probability that none of the three is covered". The step silently assumes that the three "not covered" events are independent because the "covered" events were, and that is never stated. The bound's direction also flips twice (0.25 is a floor, and 1 minus a floor is a ceiling), yet the working labels nothing until "At most". A reader cannot see why the answer is "at most". This affects P3, P8 and P11.
- **D2-5.** "three tosses give 2 cubed". "Cubed" is never named before this (A6 names only "squared"). Minor.
- **D2-6.** P5, "Two fair coins are tossed". "Fair" is never defined. The counting method in D1 needs equally likely outcomes, and "fair" is where that comes from. I supplied "heads and tails equally likely".
- **D2-7.** "When A and B cannot both happen … P(A or B) … equals P(A) plus P(B): add." No rule is given for "or" when the events can both happen. P9 wants the step found, which I can do, but the correct value, 0.88, needs the complement route plus the unstated independence of the complements.
- **D2-8.** "Two people drawn from the same unit that a decision is made about are almost never independent." The phrase "unit that a decision is made about" is jargon that is never explained. I read it twice.
- **D2-9 (serious, with D1-6).** "A number built by multiplying several ceilings together is a smaller ceiling. Carry the same 'at most' or 'at least' through every step." This is wrong across any "1 minus" step, where the direction flips. It misleads P13.

---

## D3 · Conditional probability through the two-way table

### Exercises

**Exercise 1 (health secretary page).** The answer first: "86 per cent accurate" is the test's *sensitivity*. Of the men in the overweight band, the tape flags 86 in 100. It is not the chance that a man the tape flags is overweight. Among the study's 131 medical students, only about 61 per cent of flagged men were in the band. In a group where one in five men is in the band, that falls to about 45 per cent. The test also wrongly flags about 26 per cent of men who are not in the band (specificity 74 per cent). The paper's own label ("25 or more") does not match its numbers: they fit the 25-to-29.9 band only. So ask for the prevalence in the population you intend to screen before judging how often a positive result will be right.

**Exercise 2 (critique, women's PBF 30 vs 28).** Method: find a count and a percentage in the paper that depend on the women's cut-off (for example, the number of women with higher body fat), and divide back. See whether it matches a cut-off of 28 or of 30, using any distribution figures for women's body fat that are printed. *At D3 I have no women's body-fat numbers at all, so I can describe the check but not start it. See D3-10.* (D5 later prints women's body-fat quartiles of 28.1 and 39.2. That would put about three quarters of 151 women at or above 28, but that information arrives two sections later.)

### Practice
1. The table:

   | | condition present | absent | total |
   |---|---|---|---|
   | test + | 15 | 10 | 25 |
   | test − | 5 | 70 | 75 |
   | total | 20 | 80 | 100 |

2. P(+ given present) = 15/20 = 0.75, which divides by the "present" column. P(present given +) = 15/25 = 0.60, which divides by the "+" row.
3. P(− given absent) = 70/80 = 0.875.
4. Sensitivity is the cell 15 over the column total 20: 0.75. Specificity is the cell 70 over the column total 80: 0.875. The positive predictive value is the cell 15 over the row total 25: 0.60.
5. 52/131 = 39.7 per cent at 25 or more, and 60.3 per cent under 25.
6. 0.88 × 46 = 40.48. 40/46 = 87.0 and 41/46 = 89.1, so no whole number gives 88 per cent. 0.83 × 105 = 87.15, and 87/105 = 82.86 rounds to 83 per cent, so specificity *does* fit 105. The result is mixed: sensitivity rules out the "25 or more" group of 46. Against 41 and 110: 36/41 = 87.8, which rounds to 88, and 91/110 = 82.7, which rounds to 83. Both fit. So, like the men's row, the women's row fits the 25-to-29.9 band.
7. True positives are 36 (0.88 × 41 = 36.08). True negatives are 91 (0.83 × 110 = 91.3), so false positives are 19. PPV = 36/55 = 65.5 per cent. Without rounding to whole people it is 36.08/54.78 = 65.9 per cent. *The text never says whether to round to whole people. See D3-8.*
8. NPV = 66/72 = 91.7 per cent.
9. The broken step is "close enough". 113/282 = 40.1 per cent, which does not match 38.7 per cent. Dividing back: 0.387 × 282 = 109.1, so 109 fits the abstract's percentage and 113 does not.
10. The broken step is rounding Table 2's 65.6 to a whole per cent before comparing. At the precision printed, 185/282 = 65.6 matches, while 186/282 = 66.0 does not match 65.6. 185 is consistent with both prints (65.6, which rounds to 66), and 186 is not. So the paper does decide it: 185.
11. The broken step is "so 34". 34/41 = 82.9, which rounds to 83, not 85. 35/41 = 85.4, which rounds to 85. The candidate should be 35, the nearest whole number to 34.85, not the number truncated down.
12. With a third of men in the band, per 1,000 men: 333 in the band and 667 not. True positives 0.86 × 333 = 286.7 and false positives 0.26 × 667 = 173.4, so PPV is about 62 per cent. That is close to the students' 61 per cent, but only because a third is close to the students' 32 per cent. "Right most of the time" in the officer's sense (sensitivity) is not the same as "right when it flags" (PPV). This does not establish that 86 and 74 carry over from medical students to district men, or that the band label is right (see the check), and it says nothing about the men at 30 or more.
13. Neck circumference has sensitivity 81 and specificity 71. At the students' prevalence (42/131, if the row fits that band): true positives 0.81 × 42 = 34.0 and false positives 0.29 × 89 = 25.8, so PPV is about 57 per cent. "Most of the time" is only the sensitivity, and 29 per cent of men outside the band are flagged. The screening test is measured *against* body-mass index, so it cannot replace the reference that defines it. "Everywhere" ignores that PPV changes with prevalence. The claim does not show that the label matches the row (not checked), or that the figures hold outside these students.

### What D3 taught me that changes what I do
- Before dividing, I will say which row or column I am dividing by.
- I will never quote a PPV without the prevalence that produced it.
- I will refuse "X per cent accurate" until I know which figure is meant.
- I will divide printed percentages back into whole numbers of the stated group, and suspect the label when none fits.
- I will treat carrying sensitivity and specificity into a new group as an assumption.

### Gaps
- **D3-1.** "Its mirror is the negative predictive value". In the plain-terms passage the positive predictive value has not been mentioned before this sentence (the previous paragraph is about conditional probability in general). "Its" has no antecedent. I read it twice.
- **D3-2.** "The study's Table 3 reports a 31.3 centimetre arm cut-off for men". "Cut-off" is never defined. I inferred that a reading at or above it counts as a positive. "The tape" first appears as "caught by the tape", with no measuring tape introduced. This is needed for everything that follows.
- **D3-3.** "Sensitivity of 86 per cent should mean some whole number of the 52 caught by the tape." Only 44 and 45 are then tried. The step that picks them (0.86 × 52 = 44.72, then take the whole numbers either side) is skipped here and appears only later for the 42. The must-know says "Try every whole number of the stated group", and no method for choosing is taught. This affects P6 and P11 (P11's trap is exactly the choice of candidate).
- **D3-4 (serious).** "Try the 42 men in the 25-to-29.9 band on their own, against the other 89 men in the study." No reason is given for trying this hypothesis. The 89 includes the 10 men at 30 or more, who then count as "not in the band". So an obese man flagged by the tape becomes one of the 23 "false positives", and the 61 per cent PPV counts him as a wrong result. This is never addressed. I cannot tell what the 61 per cent means clinically. It affects P7, P8, P12 and P13.
- **D3-5.** "This second ratio is the sensitivity, and it is the number the paper itself reports." The 36 was chosen *so that* it reproduces 86 per cent, so the agreement is circular. The text says the table is "rebuilt", but it does not warn that every cell after it (PPV 61, NPV) inherits that inference.
- **D3-6 (serious).** "Table 2 already gives it directly: 42 of 131." "It" points back at specificity, but 42/131 is the *prevalence*, and the illustration never uses that word. I had to guess what the 32 per cent is. It is the hinge of the 61-against-45 comparison, and of P12.
- **D3-7.** "Apply them to a stated group instead: 1,000 young men in which one in five is in the band." In the worked case the products come out whole (172 and 592). The text never says whether to round to whole people when they do not (P7: 36.08; P12: 286.7).
- **D3-8.** "Ask which one was meant, then ask for the prevalence the third one needs." "Which one" and "the third one" refer to an unnamed list, and "accurate" is never defined. I inferred "sensitivity or specificity", with PPV as the third. This affects Exercise 1.
- **D3-9.** "When two published figures for the same measurement disagree, check whether either one conflicts with something else printed alongside it." This is never demonstrated in D3. P10 and Exercise 2 rely on it.
- **D3-10.** Exercise 2: "Say how you would check which of the two women's figures, 30 or 28 per cent, the paper's own numbers are actually built on." No women's body-fat count, percentage or distribution has been given by this point. I can state a method, but no number can be checked. This blocks Exercise 2 at the "which numbers" step.

---

## D4 · Variation: what differs and by how much

### Exercises

**Exercise 1 (critique).** Every patient waits between 2 and 340 minutes by definition, so the conclusion is empty. It says nothing about where *most* sit. The range uses only the two extremes. A mean of 45 set against a maximum of 340 suggests a long tail on the high side. I would ask for the frequency table (waits in bands, with counts), or the raw values.

**Exercise 2 (teaching).** A gap between two readings has three possible sources. (1) Between people: two different patients really differ. (2) Within a person: the same patient really changes between occasions (morning against evening). (3) Between measurements: the instrument, the tape or the hand produced the gap. The next question for each: are these the same person? Was time allowed to pass? Was it the same instrument and the same observer, at the same moment? Warning: two readings that agree can both be wrong.

### Practice
1. 0.2, 0.5, 0.2, 0.1, which add to 1.
2. 42 − 3 = 39.
3. A: 50 − 10 = 40. B: 50 − 10 = 40. The ranges are the same, but A is bunched from 10 to 14 with one far value, while B is spread evenly. The range cannot show this.
4. (a) between people; (b) within a person; (c) between measurements.
5. 15/282 = 5.3 per cent.
6. 5 + 74 + 42 + 10 = 131, and 10/131 = 7.6 per cent.
7. It reduces the part of between-measurement difference that comes from different observers ("inter-observer", which I inferred means between observers). It leaves the between-people and within-person sources untouched. It also leaves the one observer's own repeat error and any constant bias.
8. 46/151 = 30.5 per cent.
9. The broken step is dividing by 282 (everyone). It should be 131 (the men): 42/131 = 32.1 per cent.
10. The two outer bands are set by the World Health Organization's edges, not by where these students sit. Their sizes depend on where the edges fall, as the 11-number demonstration showed. The inner bands (56.7 against 29.4) are very unequal. Equal-looking tails do not show symmetry.
11. The range cannot be computed from bands. All that is known is that the lowest value is under 18.5 and the highest is 30 or more, so the range is more than 11.5. "Enormously" has no benchmark: 65 per cent sit under 25 and 57 per cent in one band. The answer does not establish how much of the spread is between people rather than measurement, or the actual extremes. *"Underweight" is never defined; I took it to mean the band under 18.5.*

### What D4 taught me that changes what I do
- I will divide each count back to its printed percentage, and then check the label against the band it covers.
- I will refuse to read shape off banded tables whose edges were set by someone else.
- I will ask which of the three sources produced a spread before explaining it.
- I will not accept agreement between two readings as proof that either is right.

### Gaps
- **D4-1 (serious).** "Watch that fail on eleven bare numbers". "That" has no antecedent. The paragraph before it only describes long tails. The claim being tested (that a banded frequency table shows a distribution's shape or tail) is never stated. I read it twice to reconstruct the lesson.
- **D4-2.** "can be made to look like it has a heavy tail just by moving the bands". "Heavy tail" is not defined; only "long tail" is.
- **D4-3 (serious).** "Otherwise it tells you about the band." This sentence is an orphan: "Otherwise" refers to a condition that is not in the text. I cannot recover when a banded table *does* show shape. This affects P10.
- **D4-4.** "It is a label attached to the wrong slice of its own table. Only matching the label to the band it covers did." "Did" what? The sentence it completes (the division check did not catch it) is missing. I read it twice.
- **D4-5.** "Table 2 also tempts a claim about shape. Resist calling that a tail." The claim is never stated, and "that" points at nothing.
- **D4-6.** "These four bands are the ones the World Health Organization drew, for its own reasons. They are not centred on where these 282 students' body-mass index actually sits." Both parts are asserted. The WHO is never introduced, and the reader has no way to check "not centred". This affects P10.
- **D4-7.** "those two individual numbers are gone" / "Both are lost the moment individual numbers are grouped." "Those two" and "Both" refer to the largest and smallest values, which neither sentence names. This affects P11.
- **D4-8.** "Two students landing in different bands is a real difference between people." This is asserted, and it contradicts the section's own third source: two students either side of 25.0 can differ by measurement alone. It confuses P4(a) and P7.
- **D4-9.** "Table 2 gives you only one reading per student." The conclusion (so within-person and between-measurement variation cannot be seen) is left unsaid.
- **D4-10.** "The edge itself may not sit where you assume it does." "The edge" is undefined (a band edge? a cut-off?). This must-know is an orphan.
- **D4-11.** P7: "minimum inter-observer variation". "Inter-observer" is never defined. The three sources mention "the hand holding it" but never observers.
- **D4-12.** P11: "ranges from underweight to 30 or more". "Underweight" is never defined. Exercise 1's "average" is also used before D5 defines the mean. It is recoverable from A1 P11.

---

## D5 · Average and spread

### Exercises

**Exercise 1 (critique).** A mean of 6,200 far above a median of 4,100 shows a long high tail: a few very active patients pull the mean up. Half the patients walk under 4,100 steps, which is below the 5,000 target. So inactivity may well be a major concern. I would ask for the share of patients under 5,000, and for the quartiles or a frequency table.

**Exercise 2 (teaching).** A mean is one number for the whole group. It can sit below a cut-off while a large share sits above. In Kiran et al.'s men, the mean BMI of 24.2 is under 25, yet 52 of 131 (39.7 per cent, about two in five) are at 25 or more. To say how many are above a line, you need counts, or the median and quartiles.

### Practice
1. The sum is 49, so the mean is 7. Ordered: 2, 3, 4, 7, 9, 9, 15, so the median is 7.
2. The sum is 108, so the mean is 18. The median is (11 + 14)/2 = 12.5.
3. Q2 = (9 + 11)/2 = 10. Q1 = median of 3, 5, 5, 9 = 5. Q3 = median of 11, 11, 15, 19 = 13. IQR = 8.
4. Q2 = 9. Leaving the 9 out: Q1 = median of 2, 5, 7 = 5, and Q3 = median of 12, 15, 20 = 15. IQR = 10.
5. The mean is 8. Deviations: 0, −2, 2, −4, 4, 0. Squares: 0, 4, 4, 16, 16, 0, summing to 40. 40/5 = 8, and √8 = 2.83.
6. Squares: 4, 16, 1, 9, 16, summing to 46. Sample variance 46/4 = 11.5, so SD = 3.39. *"The variance" is ambiguous: 46/5 = 9.2 if it means the population variance. See D5-1.*
7. The gap is 0.4 kg/m². The mean is above the median, so the tail is likely on the high side.
8. IQR = 26.8 − 21.2 = 5.6. The median of 23.8 does sit between them.
9. 23.8 − 21.2 = 2.6 and 26.8 − 23.8 = 3.0. The upper quartile is further out, which suggests a longer high-side tail. *This method is never demonstrated. See D5-8.*
10. (30 − 24.2)/3.9 = 5.8/3.9, which is about 1.5 SDs above the mean. *"How many standard deviations above" is never taught. See D5-7.*
11. IQR = 39.2 − 28.1 = 11.1, and the median of 34.0 sits between. The mean (33.8) is below the median, which points to a longer low-side tail (a few very low values).
12. The broken step is "variance = 90 divided by 5". Five patients from a larger list is a sample, so divide by 4: 22.5, and SD = √22.5 = 4.74.
13. 57.4 is not between 155.0 and 163.0. Those look like height quartiles in cm, printed in the weight row, just as the men's rows were swapped. Before quoting, check that each median sits between its own quartiles, and check the units.
14. The error is reading "the mean is higher" backwards. The median of 20.3 means half the men are at or below 20.3, so more than half are *below* 22.1, not above it.
15. Mean 23.0 < 25, but 46/151 = 30.5 per cent of the women are at 25 or more (from D4 P8). The mean below a cut-off says nothing about the share above it. It does not establish whether 30 per cent is a "concern", which is a cut-off judgement by some body (B6).
16. The median is 20.3, so half the men are at or below 20.3. The mean of 22.1 sits above the median, which suggests a high tail. "Most between 20 and 24" needs the quartiles or SD for men's body fat, and *none are printed in the text*. I can refute the reasoning but not the claim. See D5-9.

### What D5 taught me that changes what I do
- I will compare the mean and the median before quoting either.
- I will refuse "the mean is below the cut-off, so the group is fine".
- I will check each printed median against its own quartiles.
- I will use n − 1 for a sample SD.
- I will look at the quartiles when the mean and median disagree.

### Gaps
- **D5-1.** "Divide that by one less than the count of values, which is five here, not six." The six bare numbers were never called a sample, and no reason for n − 1 is given anywhere. This makes P6 ("Give the variance and the sample standard deviation") ambiguous: 46/4 or 46/5.
- **D5-2.** "The variance is 6.4, and it is in the wrong unit." The unit of the variance (the square of the original unit) is never stated, and the numbers are bare anyway. I read it twice.
- **D5-3.** "The mean of the group, 24.2, sits under the line at 25. The mean describes the group." The lesson sentence (yet two in five are at or above 25) is missing, and "the line at 25" is an undefined cut-off. I supplied the point, which is the section's title claim.
- **D5-4.** "A smaller number of men, with a much higher body fat percentage, pull the mean up past them." "Them" has no antecedent (the majority is never mentioned). The inference is also stated as fact, when mean > median only suggests a high-side tail.
- **D5-5.** "It says nothing about any other group." This orphan in "Where this picture breaks" follows a sentence about a quartile check, and I cannot identify what "It" is.
- **D5-6.** "Both rows fail the same way". They fail in opposite directions (weight median below both quartiles, height median above both). I read it twice.
- **D5-7 (blocks P10).** P10: "Work out how many standard deviations above the mean his reading would sit." The operation (the difference divided by the SD) is never taught. I supplied it.
- **D5-8.** Must-know: "look at the quartiles instead of trusting a single standard deviation to describe both sides". Reading quartile distances as a sign of a tail is never demonstrated. P9 needs it.
- **D5-9.** P16: "most men have a body fat percentage somewhere between 20 and 24". No SD and no quartiles for men's body fat appear anywhere in the text, so the claim cannot be tested numerically.
- **D5-10.** P11: "say which way the mean sitting below the median points". Only the mean-above-median case is taught. I inferred the reverse by symmetry.
- **D5-11.** "Compare the two before you quote either one on its own." "The two" is not named in that bullet (the previous bullet speaks only of the mean).
- **D5-12.** The illustration table prints "height (cm) … 173 (62.6, 80.9)", and the check is performed in prose only ("It sits above both of them"). "It" here is the median, which I resolved on a second read.

---

## D6 · Sampling

### Exercises

**Exercise 1 (critique).** Right: a large sample shrinks sampling variation. Left out: 4,000 followers is a convenience sample of people who follow the hospital and chose to answer. Its population is those followers, not patients or the public. Enlarging it does not fix who is in it.

**Exercise 2 (teaching).** Size fights only sampling variation: the bounce from one random sample to another, which falls as one over the square root of n. Randomness decides which population the sample describes. A huge volunteer sample estimates the volunteers very precisely. Example: Kiran's 282 volunteers at one college.

### Practice
1. 10/√4 = 5.
2. 8/4 = 2 and 8/8 = 1. Four times the sample halves the spread.
3. √n = 15/3 = 5, so n = 25.
4. 3.9/√25 = 0.78 kg/m².
5. 3.9/√131 = 0.34 kg/m². For 524 = 4 × 131 it is 0.17 kg/m².
6. √n = 3.9/0.1 = 39, so n = 1,521.
7. The broken step is using the SD of individuals (3.9) as if it were the uncertainty in the mean. If the sample were random, the spread of the mean would be 3.9/√131 = 0.34. The sample is not random, so the law does not locate the young-adult mean at all. *I can find the break, but the text never says how to turn a standard error into a range, so I cannot give the correct interval. See D6-2.*
8. The broken step is "doubling should halve". Halving needs four times the sample. 50/√200 = 3.54.
9. The broken step is the last line. A bigger sample from the same volunteer source would pull the estimate closer to *that source's* value, not to the national 20 per cent. The "20% for young adults nationally" is also a rounded planning figure from 2015-16. *The text never says whom NFHS-4's figure describes. See D6-5.*
10. 34.8 per cent (98/282) against a planning figure of 20 per cent (19 men / 21 women) is a gap of 14.8 points. Among men, 52/131 = 39.7 per cent against 19 per cent. The comparison does not establish that medical students differ: the sample is one college of volunteers, the survey is years older, and the definitions and populations are not stated as matching. Size cannot sort these out.
11. The law's formula contains the sample size, not the population size. At n = 2,000 the spread is the individual spread divided by 44.7. At several million it is divided by about 2,000, which is better but hardly needed. So a random 2,000 can be informative. This does not establish that the sample is random, how "reliable" is to be judged (no rule for turning spread into a range), or the spread of a percentage. *See D6-3.*

### What D6 taught me that changes what I do
- I will ask how a sample was drawn before asking how big it was.
- I will refuse "the sample was huge, so it's reliable".
- I will remember that halving the scatter costs four times the people.
- I will not use an SD of individuals as the uncertainty of a mean.

### Gaps
- **D6-1.** "The square-root law states that this spread equals the spread of the individual values in the population, divided by the square root of the sample size." "This spread" points at sampling variation, which was defined as a mismatch, not as a number. Which measure of spread (SD? IQR? range?) is not said until P1's "(standard deviation)".
- **D6-2 (serious).** "The square-root law describes how far a random sample's average is likely to sit from the average of the population". "Likely" is never quantified, and no rule turns a standard error into a range. This blocks the repair in P7 and the "reliable" judgement in P11.
- **D6-3 (serious).** "The square-root law would then say something concrete." This is never shown. The law is taught only for the average of numeric values with a known population spread. Nothing tells the reader the spread of a yes/no share (34.8 per cent), so the one real application the section sets up cannot be computed. This blocks the quantitative parts of P9, P10 and P11.
- **D6-4.** "they set their target using a figure from the National Family Health Survey … to size their study". The "target" (a sample size?) and how a prevalence sizes a study are never explained.
- **D6-5.** "The paper gives the prevalence of overweight as 19 per cent in men and 21 per cent in women." Whose prevalence (all adults? young adults? national?) and which definition of overweight are never stated. P9 then asserts "20% for young adults nationally", which the text never said. This affects P10.
- **D6-6.** "Now its spread, the same way: each value's distance from 5, squared, then averaged, then square-rooted." "The same way" as D5, yet D5's worked SD divided by one less than the count, while here it divides by the count. The reason (a whole population) sits only in D5's definition. I read it twice.
- **D6-7.** "It is an estimate of it, a number made from part of the group". The two "it"s are ambiguous (the statistic, and the parameter).
- **D6-8.** P3 and P6 need √n = k, then squaring. This is never shown in D6, though it can be assembled from A6 and C2.
- **D6-9.** Nowhere does the text say that the size of the population does not enter the law. P11 turns on it, and it is only implied by the formula and the without-replacement remark.

---

## D7 · Random and systematic error

### Exercises

**Exercise 1 (critique).** "Within 1 mmHg" on repeated readings of the same person describes *precision* (repeatability), not accuracy. It leaves unanswered how close the readings sit to the true pressure (trueness), which needs a check against a trusted reference.

**Exercise 2 (teaching).** "Same number every time" means high precision, which is small random error. A scale reading 0.5 kg with nothing on it gives the same wrong number every time. Two questions: how closely do repeated readings agree (precision)? How close is their average to a known true value (trueness)? Scale A in the section is tight but half a kilogram high.

### Practice
1. 194 − 200 = −6. It reads low.
2. The errors are 3, 2, 4, 1, 5.
3. P: average error 15/5 = 3, range 5 − 1 = 4. Q: average error −3/5 = −0.6, range 4 − (−5) = 9. P is more systematic (all one way) and Q more random.
4. The errors are 0.3, 0.2, 0.4, 0.3, 0.3. The average is 1.5/5 = 0.3 kg high.
5. The errors are −0.6, +0.6, −0.1, +0.3, 0.0. The average is 0.2/5 = +0.04 °C and the range is 1.2 °C. This is unlike P4's scale: mostly random, with little push.
6. 68.3 − 68.0 = +0.3 kg. No: the 100 g step is resolution and says nothing about which kind of error this is. One reading cannot separate systematic from random, and the reference scale's own error also matters.
7. The broken step is "averaging … reduces error". Averaging reduces random error, not a zero error. Corrected: 100.3 − 0.3 = 100.0 °C, assuming the offset holds at 100 °C.
8. The broken step is the last line. An average close to the truth (trueness) says nothing about the scatter of individual readings (precision).
9. The broken step is "1 mm precision" being taken as shown repeatability: it is likely resolution. Even real precision leaves systematic error, so "free of measurement error" does not follow.
10. The broken step is "add it back". A scale that reads 0.4 with nothing on it reads 0.4 high, so subtract: 62.1 − 0.4 = 61.7 kg.
11. Old scale: mean 50.02 kg, errors +0.1, −0.1, +0.2, −0.1, 0.0, range 0.3. New scale: mean 50.62 kg, average error +0.62 kg, range 0.16. The new scale is more precise and finer in resolution, but biased by about 0.6 kg. The old scale is truer. This does not establish behaviour at other weights (drift), or anything from more than five readings.
12. Observer 2 minus observer 1: +0.4, +0.4, +0.5, +0.3, +0.3, an average of +0.38 cm, all in one direction. That is a systematic difference between observers. One observer removes this between-observer difference but not their own habit or random error. It does not establish which observer is right (no reference), so "no measurement error" is false.

### What D7 taught me that changes what I do
- I will ask two questions of any instrument: how closely repeats agree, and how close the average is to a reference.
- I will read a paper's "accuracy of 100 g" as resolution.
- I will refuse "more decimal places, so more accurate".
- I will subtract a known offset.
- I will not treat a single observer as the absence of measurement error.

### Gaps
- **D7-1 (serious).** "in the VIM's own words (entry 2.17)". The VIM is never expanded, introduced or placed. The reader does not know what document is being quoted, or why its words settle anything. The same applies to 2.15, 2.18, 2.19 and 4.14.
- **D7-2.** "Its error is what it says minus what is actually true." This opens the plain-terms part, and "Its" has no antecedent. I read it twice.
- **D7-3.** "A systematic error is the part of the error that …". The idea that an error splits into a systematic part and a random part is used but never stated.
- **D7-4.** "Two stated scales are each weighed against it twenty times." "Stated" means nothing here, and scales are not weighed. I read it twice.
- **D7-5.** "That is wide, so this scale is much less precise than scale A." "That" has no antecedent. The sentence that introduces scale B's spread (58.7 to 60.7, about 2 kg) is missing, so a reader meets scale B's conclusion before its description.
- **D7-6.** "half a kilogram out against seven and a half hundredths". The subtraction 60.0 − 59.925 = 0.075 is never shown.
- **D7-7.** The text never states how to judge "more systematic" against "more random" from a list of errors (the average error against the spread of the errors). It is only illustrated. P3 and P5 ask for exactly this.
- **D7-8.** "Differences between observers are each observer's own systematic habit." This is asserted, never shown. P12 relies on it.
- **D7-9.** The illustration opens on "Weight and height were recorded with accuracy of 100 g and 0.1 cm" and then drops it. The text never says what this means for the study's own figures (for example, BMI). The thread is left hanging.
