# S37-R1 compression-pass holes, batch r2 (C07 to C12)

These are for the fixer and the audit. Each is a gap that the cold read found and that the
original either does not fill, or fills only with a sentence the validation rule would not allow
back. "As it stands" quotes `S37-R1-Cnn-final-prose.yml`, or the record where the field is not
prose (figures, problems). Numbers match `RESTORE-DECISIONS-r2.md`. "Residual" marks what is left
after a partial restore.

## C07

**1. A-C07-1 (definition.text).** As it stands: "Its headline figure is the monthly per capita
consumption expenditure (MPCE): ..." Missing: "Its" has no antecedent, and "HCES" (used in the
figure and exercises) is never expanded. The original's first sentence names it ("India's Household
Consumption Expenditure Survey (HCES), run by the Ministry of Statistics and Programme
Implementation (MoSPI), records what ..."), but at 31 words it raises the mean sentence length and
fails validation. To close it, split that sentence in the record (for example, name the survey and
its body in one sentence and what it records in another), then restore it.

**2. A-C07-2 (simplified_explanation).** As it stands: "Across the same years its average hardly
moved: about 2,200 kilocalories a person a day." Wrong: the calorie years are 2011-12 and 2023-24,
and the spending years are 2011-12 and 2022-23. The same error is in the original. To close it,
state the calorie years ("Between 2011-12 and 2023-24 ...").

**3. A-C07-3 (simplified_explanation; definition.text).** As it stands: "Two government surveys
tell you ..." / "The second survey takes the food each household said it used." / "The National
Sample Survey's Report 594 converts the food each household recorded as consumed ..." Missing:
which survey's consumption records Report 594 uses, and whether the two are independent. The fixer
should check the report: if it is built on HCES quantities, "two surveys" is wrong and must say
"two uses of one survey".

**4. A-C07-4, residual (must_know[5].point).** As it stands: "Before you set two rounds side by side,
check that they measured the same way. The surveys before 2009-10 used a different reference
period ..." Missing: whether the 2011-12 and 2022-23 rounds, which the section itself compares
throughout, did measure the same way. To close it, add one sourced sentence on the comparability of
HCES 2022-23 with the 2011-12 round.

**5. A-C07-7 (must_know[2].point).** As it stands: "Beverages, refreshments and processed food is the
largest food group in Indian household spending." Missing: the other groups' shares, so the reader
cannot check "largest". It is also unclear which year the claim is for, since the 2023-24 figures
(9.84/11.09) were cut. To close it, give the next-largest group's share (for example milk) with the
year.

**6. A-C07-8 (must_know[0].point).** As it stands: "Cereals' share of rural MPCE halved between
2011-12 and 2022-23 while the rupees spent on them rose." Missing: the rupees are nominal, and no
price change is given, so a real rise cannot be judged. To close it, say "rose in rupees of each
year" and give a food price index change, or drop the claim that spending rose.

**7. A-C07-10 (must_know[2].point).** As it stands: "It includes purchased cooked meals." Missing:
the other contents and any split within the group, so Ex 2, P11 and a sugar-drink question cannot
say what share is packaged snacks or sweet drinks. The original lists the contents ("drinks,
snacks, packaged food and meals bought ready to eat") but no split. To close it, give the item-level
split from the HCES tables, or state that none is published.

## C08

**11. A-C08-1 (definition.text).** As it stands: "The measure these institutions are judged by is
also a quantity. For 2022-23 it gives net imports of cereals of minus 30,352 thousand tonnes ..."
Missing: the antecedent of "it" (the Economic Survey table). The original's sentence "The Economic
Survey 2025-26's table of foodgrain availability counts production, net imports and stocks in
thousand tonnes, and availability per person in grams a day." could not be restored with the other
C08 restores without failing the mean-length rule. To close it, change "it" to "the Economic Survey
2025-26's Table 1.19". Also, "judged by" is the author's framing and should be marked as such.

**12. A-C08-3, residual (must_know[4].point).** As it stands: "The PDS was never meant to be a whole
diet." Missing: "ration" is never defined, and nothing says the ration is rice and wheat (Ex 1
assumes it). The link from procurement to ration comes only in C09. To close it, add one sentence
on what the PDS issues, or point forward to C09 and C11.

**13. A-C08-4 (illustration.body).** As it stands: "The system built to end a grain shortage now runs
a grain surplus." Wrong: a net export is equated with "surplus" without a definition, in a section
that warns that availability is not intake. To close it, define "surplus" here as net exports plus
stocks above the buffer norm, or say "exports more grain than it imports".

**14. A-C08-6 (structure).** There is no practice set. The only arithmetic is the net-import sum.
This is for the drafter or fixer, not the compression pass.

## C09

**21. A-C09-2, residual (must_know[6].point).** As it stands: "The cost in the MSP releases is the
CACP's all-India weighted average, including imputed family labour." Missing: what the average is
weighted by, and what "imputed" means. The original's "The cost counts paid-out costs and the
imputed value of family labour" does not define it either. To close it, define both in one or two
short sentences.

**22. A-C09-3 (exercise 2 / table).** As it stands: "margin over cost (%)". Wrong: C04 defined margin as
mark-up minus handling costs, and here it is (MSP − cost)/cost. The clash is not flagged. To close
it, add a line saying the word is used differently here, or use "excess over cost".

**23. A-C09-5, residual (must_know[1].point).** As it stands: "MSP is announced for many crops.
Procurement is concentrated in one." Wrong: the evidence is kharif only, and the definition says
wheat is bought at MSP too, with no wheat volume given. To close it, say "Among kharif crops,
procurement is concentrated in one", or add the wheat figure.

**24. A-C09-6, residual (must_know[1].point; figure).** As it stands: "8,746 lakh tonnes". Missing:
"lakh" is defined nowhere in the book or in Book 0, and C06 and C08 use thousand tonnes. To close
it, define "a lakh is 100,000" at first use and give the figure in million tonnes as well.

**25. A-C09-7 / B-C10-13, residual (C09 figures; C10 must_know[2], [5]).** As it stands (C10): "It raises
the economic cost, and so the subsidy." / "Paddy is milled before it becomes rice." Missing: a
paddy-to-rice conversion (outturn ratio), so procurement in paddy cannot be linked to rice in C08
and C11, and the MSP effect on the economic cost cannot be sized. To close it, give the official
outturn ratio with its source.

**26. A-C09-9 (figure).** As it stands: "Paddy (common): floor 2440.5, MSP 2441." Missing: the paddy
cost (Rs 1,627) and its source release. The reader has to work it back from the floor. To close it,
print the cost with the kharif 2026-27 release.

**27. A-C09-10 (structure).** There is no Illustration and no practice set. The chain from MSP to
procurement to ration, the section's main point, is never worked with numbers. For the drafter or
fixer.

## C10

**31. B-C10-1, residual (definition.text).** As it stands: "The central issue price is the price at
which the Union government issues the grain to the States." Missing: that this was the Schedule I
price (Rs 3 a kg for rice, C11), and that the figure's "Rs 300 a quintal" is that price. To close
it, add the link in one sentence.

**32. B-C10-5 (H; must_know[4].point).** As it stands: "Government releases on edible oil use two terms,
'basic customs duty' and 'effective customs duty', and they are not the same charge." Missing: what
the difference is, with one worked example. Without it, problems 9, 11 and 14 and C16's figure
cannot tell whether the landed-price rule gives the real landed price. To close it, source and state
the components of the effective duty (for example the cess on top of basic duty).

**33. B-C10-6 (problem 5).** As it stands: "Compare your answer with the margin the release prints."
Missing: the printed moong margin is given nowhere. To close it, print it in the problem, or drop the
instruction.

**34. B-C10-7 (problem 6; C09 simplified_explanation).** As it stands: "Rabi crops are the ones sown
after the monsoon, in winter." Missing: kharif is defined nowhere, and rabi only here, after C09
used both. To close it, define both in C09 at first use.

**35. B-C10-8 (problem 12).** As it stands: "Paddy farmers now get a 50 per cent profit, guaranteed."
Missing: no paddy MSP or cost is in the problem or in C10. To close it, give MSP Rs 2,441 and cost
Rs 1,627 in the problem (with HOLES 26).

**36. B-C10-9 (problem 8).** As it stands: "a second category, which it calls 'tide over', for rice
issued at Rs 830 a quintal." Missing: who gets tide-over grain and why, here and in C14. To close it,
add one sourced sentence.

**37. B-C10-10 (number; figure).** As it stands: "It was 91.6 and 91.9 per cent while the issue price
was Rs 300 a quintal. It has been 100.0 since the issue price became zero on 1 January 2023." Wrong
or unexplained: January to March 2023 falls in 2022-23, yet that bar is 91.9. The fixer must check
the bulletin's year basis and either state it or correct the bars.

**38. B-C10-11 (exercise 2; definition.text).** As it stands: "The full cost of buying, storing and
moving the grain is called the economic cost." Missing: any split of the economic cost (the MSP
share, and the costs of storage and movement), so "where does that money go?" cannot be answered
beyond three words. To close it, give the bulletin's components of the economic cost.

**39. B-C10-12 (figure).** As it stands: "Rs 110 at 10 per cent, Rs 105 at 5 per cent, Rs 100 at
nil." Missing: which oil the nil rate applies to (C16 gives it for crude sunflower only). To close
it, name the oil, or mark nil as the zero point of the line only.

## C11

**41. B-C11-5 (cross-file; figure).** As it stands: "an Antyodaya household gets 35 kg whatever its
size." Wrong against Book 0 A5 and B2. Those carry the section 3(1) proviso, "to the extent the
Central Government specifies for each State", which this drops. To close it, add the proviso or
cross-reference it.

**42. B-C11-6 (structure).** There is no practice set. The entitlement arithmetic (the crossing at 7
people, the per-person Antyodaya share) is untested. For the drafter or fixer.

## C12

**51. B-C12-2 (table; exercise 1).** As it stands: table rows "lower primary classes" / "upper
primary classes"; Ex 1.3 "A child in class VI". Missing: which classes are lower and which are upper
primary (C13's problems depend on it too). To close it, add "lower primary is classes I to V, upper
primary VI to VIII" with its source.

**52. B-C12-4 (must_know[1].point).** As it stands: "Every norm in Schedule II and in the school-meal
table is an amount to reach." Wrong: there is no separate school-meal table in C12. The PM POSHAN
food norms appear only in C13's figure and problem 5. To close it, reword to "in Schedule II and in
the PM POSHAN food norms (C13)", or drop "school-meal table".

**53. B-C12-5 (number; must_know[4].point).** As it stands: "Mothers, children under three and
severely malnourished children get a take-home ration." Wrong: the table's row says "children, 6
months to 6 years, who are malnourished", with no "severely". The fixer must check the guidelines
and make the two agree.

**54. B-C12-6 (H; must_know[0].point, against C13).** As it stands: "The government says the Schedule II
norms were revised in January 2023, and the revised figures are not in the documents this book
holds." C13 says: "The anganwadi take-home-ration norms in the Act's Schedule II were revised in
January 2023". Wrong: the scope differs between the two (all norms, anganwadi norms, or THR only),
so the reader cannot tell whether the 450/700 school norms are current. It is also not explained
how a Schedule is revised by government rather than Parliament (F5), presumably under a section of
the Act that lets the Central Government amend Schedules by notification. To close it, find the
January 2023 notification and state its scope and legal basis once, the same way in both sections.

**55. B-C12-8 (structure).** There is no practice set. For the drafter or fixer.
