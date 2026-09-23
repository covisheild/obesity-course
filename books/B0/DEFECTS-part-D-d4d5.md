# Defects · Book 0 Part D, D4–D5 (`B0-R0-C27`, `B0-R0-C28`)

Audit step 3, 2026-09-23. I checked the records against `sources/kiran_2022_muac_nc.txt` and
`sources/openstax_intro_stats_2e.txt`, which `sources/INDEX.yml` maps to the two citekeys. I also
checked them against the earlier records C01–C26, C29 and C30 and against `prose/GLOSSARY.md`.
I recomputed every figure in python. No record was edited.

I searched for every `quote` with the build's own normalisation (whitespace and case). All 22
quotes are present in their files, so the build's current check passes. The defects below are the
ones that check cannot see.

Severity: **error** means a wrong statement, wrong arithmetic, wrong sourcing or a claim with no
source. **floor** means a breach of claude.md §2, spec §1 or §10 sequence. **style** covers
everything else.

---

## Recomputation summary

I ran every working line in both records through python.

- **C27:** every line is right except one number in the level 8 answer (D4-1). Checked: L1 0.2 / 0.5 / 0.2 / 0.1, sum 1. L2 39. L3 40 and 40. L4 5.319. L5 131 and 7.634. L6 30.464. L7 14.894 and 32.061. Also 109/282 = 38.652, 113/282 = 40.071, 24+160+83+15 = 282, and 98/24 = 4.08.
- **C28:** every line is right. Checked: mean 16.667 and median 13.5. Quartiles 4, 7, 9 and IQR 5. SD example: sum of squares 32, variance 6.4, SD 2.5298. L1 49, 7, 7. L2q 5, 10, 13 and IQR 8. L3 variance 8, SD 2.8284. L3b squares sum to 46, variance 11.5, SD 3.3912. L4 0.4. L5 1.8. L5b 5.6. L6 1.4872. L7 variance 22.5 and SD 4.7434 (18 and 4.2426 with n). Also 52/131 = 39.695, 72.0 ± 13.1 = 58.9 / 85.1, and 22.1 ± 7.3 = 14.8 / 29.4.
- **The C28 errors are in reasoning, not arithmetic** (D5-1, D5-2).
- **Quartile method.** Both records use the median of each half, which is the method the anchor teaches (s.2.3: "the middle value of the lower half of the data"). It is stated only partly (D5-15).

## Numbers register under the stricter rule

**All 15 entries state their number in the quote.** None relies on a heading, a clause number or
a same-digit cell elsewhere. Every Table cell quote is the right row, the right column and the
right sex. I checked each against the flattened table.

These entries still have problems:

| Record | Entry | Problem |
| --- | --- | --- |
| C27 | 113 | The quote is right, but `unit` says "results text". The sentence is in the **abstract** (source line 43). See D4-3. |
| C27 | 109 | The quote is from the results text (line 251), but `unit` says "Table 2". See D4-3. |
| C28 | 10 | `10 (7.6)` occurs twice in the file. The first hit is the right cell (Table 2, men, obese). The second is Table 4, MUAC, men, "not preferred" (line 623). The quote does not say which is meant. See D5-3. |
| C27 | *missing* | 98 (83 plus 15) is computed and not registered as derived. See D4-6. |
| C28 | *missing* | 52 (42 plus 10) and 39.7 % (52 ÷ 131) are computed and not registered as derived. They carry the section's title claim, and the paper states neither. Also missing: 58.9, 85.1 and 1.8, all derived. See D5-3. |

---

## D4 · `B0-R0-C27` Variation: what differs and by how much

### Arithmetic and sourcing

**D4-1**
- **Field:** `practice[level 8].answer`, last sentence (line 504).
- **Claim:** "It never looks at where the other 267 students, out of 282, actually are."
- **Arithmetic:** the colleague compared the two outer bands, which hold 24 plus 15 = 39 students. So 282 minus 39 = **243** are left over. The 267 is 24 plus 160 plus 83, which is the wrong subset.
- **Severity:** error.
- **Fix:** replace 267 with 243.

**D4-2**
- **Field:** `illustration.body`, the shape paragraph (lines 155–164). Also `practice[level 8].answer` (lines 491–500) and `must_know` 5 by implication.
- **Claim:** 98 students above the middle band against 24 below shows "its tail stretches further upward than downward". Level 8 says "a heavy tail on the high side", which "stays invisible if you only compare the two outer bands".
- **What the data say:** counting people above and below a band shows shape only if the band sits centred on the data. This one does not.
  - Table 1 puts the medians at 23.8 (men) and 22.7 (women), near the top of the 18.5–24.9 band.
  - The band's upper edge is about 1.4 kg/m² above the pooled mean of 23.6. Its lower edge is about 5.1 below.
  - A perfectly symmetric bell curve with the paper's own means and SDs (men 24.2, 3.9; women 23.0, 3.7) predicts about 26 / 156 / 100 people in the three groups. The table shows 24 / 160 / 98.
  - The paper also says its Kolmogorov-Smirnov test was run "to confirm normal distribution" (line 134).
- **Conclusion:** the 98-to-24 split comes from where the WHO cut-points sit. It is not evidence of a tail. `analogy_breaks_when` itself says this table cannot say how far anyone sits from the middle. The level 8 answer replaces the colleague's bad argument with a second bad argument.
- **Severity:** error.
- **Fix:**
  - Illustration: say the four bands are uneven. The middle one is not centred on this group. So more people above it than below it says nothing about shape. Shape needs the individual values, or bands of equal width placed round the middle.
  - Level 8 answer: the flaw is that band counts depend on where the band edges fall. The two outer bands are open-ended and cover different distances from the middle, so neither comparison tests symmetry.
  - Drop "tail stretches further upward" and "heavy tail on the high side".

**D4-3**
- **Field:** `illustration.body` (lines 96–104); `illustration.numbers[0].unit` and `numbers[1].unit`.
- **Claim:** "Read its results section first" (then the 113 sentence is quoted). "A few paragraphs later, introducing the same finding through its table…" (then the 109 sentence). The units say 113 comes from the "results text" and 109 from "Table 2".
- **Source:**
  - The 113 sentence is the **abstract's** Results paragraph (line 43). The file header lists it as "abstract '113 (38.7%)'".
  - The 109 sentence is in the main Results, about 200 lines later (line 251).
  - The quoted words for 109 are running text. Table 2 separately prints "109 (38.7)".
- **Severity:** error (locator).
- **Fix:**
  - "Read its abstract first."
  - "Further on, in the results section, introducing Table 2, the paper says this instead."
  - Units: "abstract, Results paragraph", and "results text introducing Table 2".

**D4-4**
- **Field:** `illustration.body`, the whole abdominal-obesity block (lines 99–131).
- **Claim:** this is the section's lead failure case. `draft-notes-part-D-D4D5.md` item 2 says C26 used the neck-circumference conflict instead.
- **Source:** C26 already works this exact check **twice**:
  - `exercises[1]` (C26 lines 364–392);
  - `practice[level 7]` (C26 lines 605–629).
  - Both use the same 109 ÷ 282 and 113 ÷ 282 divisions and the same conclusion. `draft-notes-part-D-D1D3.md` says C26's diagnostic band uses all three real inconsistencies. The D4–D5 notes are wrong on this point.
- **Why it matters:** the reader meets the same move a third time in D4. The illustration asks them to do nothing new (§4).
- **Severity:** error (duplicated material, and a false claim in the drafter's notes).
- **Fix:** cut the block to one pointing-back sentence ("you ran this check on the abdominal-obesity counts in the section on conditional probability"). Then lead with a failure C26 has not used. The same abstract sentence has one:
  - The abstract defines overweight as "BMI ≥25 kg/m2" (line 31).
  - It then reports "83 (29.4%) were overweight" (line 43).
  - But 83 is only the 25–29.9 band. At 25 or more the count is 83 plus 15 = 98, which is 34.8 %.
  - That is a real case of a label and its count not matching. Check that C29 (which computes 98) is not also using it as a failure.

**D4-5**
- **Field:** `definition.references[0].quote`, with `claim_located: true`.
- **Claim:** the quote "An important characteristic of any set of data is the variation in the data" stands under a definition of distribution, shape, and the three sources of difference.
- **Source:** the sentence (s.2.7, line 2353) says only that data vary. It does not carry:
  - what a distribution is;
  - the shape of a distribution;
  - the three sources.
- **The anchor has prose that does** (all pass the build's normalised search):
  - s.1.2 "Variation in Data": "Measurements of the amount of beverage in a 16-ounce can may vary because different people make the measurements or because the exact amount, 16 ounces of liquid, was not put into the cans." This separates differences between things from differences between measurements.
  - s.2.7: "The reason is that the two sides of a skewed distribution have different spreads." This supports the shape claim.
- **Severity:** error (sourcing: `claim_located` is asserted and not true).
- **Fix:** add the s.1.2 quote under the three-sources paragraph, with locator "s.1.2 Variation in Data". Add the s.2.7 skew sentence for shape. Keep the frequency-table quote, which does support its sentence.

**D4-6**
- **Field:** `illustration.numbers`.
- **Claim:** the list is meant to hold every number the illustration uses.
- **Missing:**
  - 98 (83 plus 15), which is computed. Under the stricter rule it must be marked derived and say how.
  - 40.1 (113 ÷ 282), also derived.
  - 282, stated in "Of the 282 participants", but not registered on its own.
- **Severity:** error (sourcing, minor).
- **Fix:** add 98, `unit`: "derived: 83 plus 15, Table 2 N column, BMI 25 or more", with the two cell quotes. Add 282 with quote "Of the 282 participants".

**D4-7**
- **Field:** `simplified_explanation`, paragraph 4 (lines 71–74).
- **Claims:**
  - "The slow side is called a long tail, and it always points toward the values that turn up least often."
  - "Most distributions bunch up somewhere in the middle."
- **What is true:** the values at both ends turn up rarely, so "points toward the values that turn up least often" does not pick out one side. A long tail is the side where values stretch **far from the middle**. "Most distributions bunch up in the middle" is a claim about the world with no source. Counts, waiting times and mixtures often do not.
- **Severity:** error.
- **Fix:** "The side that thins out slowly is called a long tail. It points toward the values that sit farthest from the middle." Delete the "most distributions" sentence or say "Many".

**D4-8**
- **Field:** `exercises[0]`, prompt and answer.
- **Claim:** the prompt says "The range of waiting times is 2 minutes to 340 minutes". The answer says "Every value in the set has to fall inside its own range."
- **Conflict:** C18 teaches the statistical range as "the largest value in a set of measurements minus the smallest". C27's own definition matches: range is one number, here 338 minutes. The exercise uses range as an interval, so the term is taught twice in two senses.
- **Severity:** error (terminology).
- **Fix:**
  - Prompt: "The shortest wait was 2 minutes and the longest 340, a range of 338 minutes."
  - Answer: "Every value lies between the smallest and the largest."

**D4-9**
- **Field:** `practice[level 9].answer`.
- **Claim:** the note says "body-mass index ranges from underweight to 30 or more. So weight varies enormously". The answer never challenges the switch from body-mass index to weight.
- **What is true:** a spread of body-mass index bands is not a spread of weight, because height varies too (C14). The transfer band exists to say what the computation does not establish, and this is the first thing it does not establish.
- **Severity:** error (omission in a transfer answer).
- **Fix:** add a sentence under "What this does not establish": "The table sorts body-mass index, not weight. Two students with the same index can differ in weight by many kilograms if their heights differ."

### Floor

**D4-10**
- **Field:** `exercises[0].answer`, last paragraph.
- **Claim:** "Or ask for the median and the interquartile range."
- **Problem:** both are taught in D5 (C28), after this section (§10 rule 1).
- **Severity:** floor.
- **Fix:** ask instead for a frequency table in useful bands, or for how many patients waited more than an hour.

**D4-11**
- **Field:** `illustration.body` (quote at line 106); table header (line 137).
- **Problems:**
  - "WHO" first appears unexpanded inside the quoted sentence. No record from C01 to C26 expands it. BMI is expanded in C14, so it is fine.
  - The table header writes "kg/m2". C14 taught the unit as kg/m^2, which the build typesets. "m2" reaches the reader as "m two".
- **Severity:** floor.
- **Fix:** add "the World Health Organization (WHO)" in the sentence before the quote. Write `kg/m^2` in record prose and tables, and leave the paper's own flattened form inside quotes.

**D4-12**
- **Field:** `practice` (whole set).
- **Claim:** the simplified explanation calls the three sources of difference "the part that matters more than any of the words above". The inventory calls them "the section's must-know core".
- **Problem:** not one of the nine problems drills them. All nine are on relative frequency, range or band shape.
- **On the drafter's question (keeping "between measurements" without numbers):**
  - Keeping invented numbers out of the illustration was right.
  - But the reader can only do the teaching exercise from words, and never practises sorting a difference into one of the three.
  - A labelled stated-conditions pair is allowed (§7a: "use bare numbers and say nothing about the world"). C30 already does this with 61.2 against 60.5 kg.
  - The paper also supplies real words: "The strength of the study was single observer measurements with minimum inter-observer variation" (line 736), and "Weight and height were recorded with accuracy of 100 g and 0.1 cm" (line 111).
- **Severity:** floor (the reader cannot yet carry out the core move).
- **Fix:** add two problems.
  - A mechanical one: three pairs of readings under stated conditions; say which source each difference comes from.
  - An applied one on the paper's single-observer sentence: which of the three sources does one observer reduce, and which two does it not touch?

**D4-13**
- **Field:** `definition.text`, paragraph 5, and `must_know` 4.
- **Claim:** differences between repeated measurements are "produced by the instrument and the act of measuring".
- **The gap:** a measurement error that is the same on every reading produces **no** difference between readings. A scale 0.5 kg heavy gives two identical wrong readings. As written, the lens lets a reader conclude "the two readings agree, so the measurement is fine". D7 has to undo that.
- **Is D7 affected?** C30 re-teaches repeated readings from scratch and never points back to D4. So nothing breaks. But D4 is teaching, by omission, the misconception D7 exists to correct.
- **Severity:** floor.
- **Fix:** add a `boundary` point: "Measuring twice shows you only the part of measurement error that changes between readings. An instrument that is wrong by the same amount every time gives two matching readings, and both are wrong." Kind `boundary`, bearing `methodological`.

### Style

**D4-14**
- **Field:** `practice[level 7].prompt`.
- **Claim:** "42 of the 282 total students (not just the men) are said to be in the band".
- **Problems:**
  - The parenthesis gives the error away. §7a: no hint.
  - The framing misstates the table: 83 of the 282 are in that band, and 42 of the 131 men.
- **Severity:** style.
- **Fix:** "Here is a worked answer to: what share of the men in Table 2 are in the band from 25 to 29.9?" Then keep the working as it is.

**D4-15**
- **Field:** `definition.text` paragraph 3; `simplified_explanation` paragraph 3.
- **Claim:** range "exactly as the section on functions taught it".
- **Problem:** C18 taught a rule's range and only *warned* about the statistical one. The pointer can send the reader to the wrong meaning.
- **Severity:** style.
- **Fix:** "the statistical meaning the section on functions warned about, not a rule's range of outputs".

**D4-16**
- **Field:** `illustration.body`, the first quote.
- **Problem:** the quoted abstract sentence also uses "overweight" in two senses (see D4-4). It also carries the 186 / 185 body-fat conflict. Neither is flagged. A reader who runs the section's own check on "overweight" gets 98, not 83, and is left unsure.
- **Severity:** style.
- **Fix:** either use this as the new lead case (D4-4), or cut the quote to the abdominal-obesity clause.

**D4-17**
- **Fields:** `must_know` 4 and 5; section opening; §10 rule 4.
- **Problems:**
  - Must-know 4 ends "treating one as another wastes it". The consequence is not stated (§5).
  - Must-know 5 barely passes the admission test. Say what the reader refuses, for example "do not quote the share in the top band as the group's weight".
  - The first sentence of the section does not say which earlier section it stands on (§10 rule 5).
  - Simplified paragraph 2 introduces two terms of art at once (§10 rule 4).
  - "Distribution" also appears in C22 in the grain-handout sense. One clause would separate the two, as C18 does for range.
- **Severity:** style.

---

## D5 · `B0-R0-C28` Average and spread, and why the average is not the person

### Arithmetic and sourcing

**D5-1**
- **Field:** `practice[level 7]`, prompt and answer.
- **Claim:** the worked answer's division by 5 is "the step that broke". The answer says "This is a sample of five values."
- **Problem:** the prompt never says the five numbers are a sample, or that a sample SD was asked for. For a whole group, dividing by 5 is correct: variance 18, SD 4.2426. Worse, the section's own simplified explanation (lines 214–216) says dividing by the full count "is not a mistake in their arithmetic. It is a different, and less usual, convention." The level 7 answer calls the same thing the broken step.
- **Severity:** error (the worked answer is not wrong as posed, and the answer contradicts the section).
- **Fix:**
  - Prompt: "Five patients were picked from a clinic's list. Here is someone's worked sample standard deviation."
  - Answer: "divided by the count, which is the convention for a whole group, where the question asked for a sample".

**D5-2**
- **Field:** `practice[level 10].answer`.
- **Claim:** "One standard deviation either side of the mean already covers 14.8 to 29.4". Then: "The spread being at least 14.8 to 29.4 already makes 'most men between 20 and 24' an unsupported guess". And: "Neither the mean nor the standard deviation tells you what fraction… That needs a frequency table."
- **What the source and the section allow:**
  - A standard deviation does not say where the values lie unless you assume a bell curve. Part D excludes that assumption (READY: "The normal distribution… belongs to S03"). "The spread being at least 14.8 to 29.4" is not a statement the SD supports.
  - The decisive computation is available from the section's own technique and the same table row: men's body fat, "20.3 (16.7, 28.8)".
  - About a quarter of the men are at or below 16.7, and about a quarter at or above 28.8 (anchor s.2.3: "About one-fourth of the data falls on or below the first quartile").
  - So at most about half lie between 16.7 and 28.8. "Most" cannot lie between 20 and 24.
  - The anchor also warns, s.2.7 line 2825: "in skewed distributions, the standard deviation may not be much help… it is better to look at the first quartile, the median…".
- **Severity:** error.
- **Fix:** replace the compute step with the quartile argument and the working `28.8 minus 16.7 = 12.1`. Keep the mean-above-median point. Make "does not establish" say: the quartiles bound the share in 20–24 from above, but do not give it.

**D5-3**
- **Field:** `illustration.numbers`.
- **Problems:**
  - **52** (42 plus 10) and **39.7 %** (52 ÷ 131) carry the section's title claim. The paper states neither. Both are computed and neither is registered, let alone marked derived.
  - Also derived and not registered: 58.9 and 85.1 (72.0 ∓ 13.1), and 1.8.
  - Stated in a quote but not registered as values: 131, 13.1, 6.8, 3.9, 167.7, 177.8.
  - `10 (7.6)` also occurs in Table 4 (line 623).
- **Severity:** error (sourcing).
- **Fix:**
  - Add 52, `unit`: "derived: 42 plus 10, Table 2 men's column, BMI 25 or more". Quotes for both cells.
  - Add 39.7 as "derived: 52 divided by 131".
  - Widen the 10 quote to `Obese (≥30 kg/m2) 15 (5.3) 10 (7.6)` and the 42 quote to `Overweight (25–29.9 kg/m2) 83 (29.4) 42 (32.1)`, as C26 already does. Both pass the normalised search.

**D5-4**
- **Field:** `exercises[0].prompt`.
- **Claim:** "the 5,000-step benchmark most guidelines use".
- **Problem:** this is a statement about the world's guidelines with no source (claude.md: "A claim without a source you have opened is not written down as a fact"). The 6,200 and 4,100 are also unlabelled invented figures.
- **Severity:** error (sourcing).
- **Fix:** "the report's own target of 5,000 steps", and add "(the figures are made up for this exercise)", as C21 does.

**D5-5**
- **Field:** `must_know` 1.
- **Claim:** "…is the single most common error made with these two numbers together."
- **Problem:** an empirical claim with no source.
- **Severity:** error (sourcing).
- **Fix:** delete the clause. The point stands without it: "Reading this backwards… is an error."

**D5-6**
- **Field:** `simplified_explanation` (lines 208–216); `definition.text` paragraph 4; `must_know` 4; `retrieval_items[1]`.
- **The reason given for n minus 1:** "The mean itself was already built from these same numbers. So measuring each value's distance from its own sample's mean slightly understates the wider population's true spread. Dividing by a smaller number pushes the answer back up to correct for that."
- **Is it true?** In direction, and **for the variance, on average**, yes. Squared distances from the sample's own mean are never larger than distances from the population mean would be, so dividing by n runs low on average.
- **Where it overclaims:**
  - (a) "understates" holds on average, not in every sample.
  - (b) Dividing by n minus 1 makes the **variance** right on average. The square root still runs slightly low. So the retrieval answer, which says the SD division "corrects the estimate back upward", is false as stated for the standard deviation.
  - (c) The passage is billed as "one sentence" and is three.
  - (d) "Every paper the reader will ever open does the same" and "every published table uses" (simplified). "The convention this book and every paper the reader will meet both follow" (definition). "Every paper you read will have done the same" (must-know 4). None of these can be checked, and papers often do not say which divisor they used.
- **The anchor's own reason is available and is more modest:** "The sample variance is an estimate of the population variance… dividing by (n – 1) gives a better estimate of the population variance" (s.2.7, lines 2807–2809).
- **Severity:** error (retrieval item false, and overclaims elsewhere).
- **Fix:**
  - "Distances from the sample's own mean come out a little small on average, because that mean sits in the middle of these particular numbers. Dividing by one less than the count makes the variance come out right on average."
  - Retrieval: say "the variance".
  - Replace "every paper" with "most papers, and the textbook this book follows".
  - Add the anchor sentence as a quote: `gives a better estimate of the population variance`.

**D5-7**
- **Fields:** `definition.text` paragraph 2; `illustration.body` (lines 230–233, "the printed range is 167.7 to 177.8"); `practice[level 5 (IQR)]`; `practice[level 8]`; `must_know` 6.
- **The conflict:** the definition makes the interquartile range one number, the third quartile minus the first. The illustration, level 8 and must-know 6 treat it as an interval that "has to contain its own median". Level 5 asks for it "as a single number" and never explains the switch. "The printed range" also uses *range* as an interval, against C18. The paper's "Median (IQR)" column prints the two quartiles, not the IQR.
- **Severity:** error (terminology; one term taught in two senses).
- **Fix:**
  - Before the table: "Papers usually print the first and third quartiles in brackets after the median and label the pair IQR. The interquartile range itself is the difference between them."
  - Restate every check as "the median must sit between the two quartiles printed beside it".

**D5-8**
- **Field:** `practice[level 6]`, the second one (women, 41 plus 5 over 151).
- **Problem:** this is word for word C27 `practice[level 6]`, prompt and answer. It drills D4's relative frequency, not any D5 technique.
- **Severity:** error (duplicate, and it does not exercise the section).
- **Fix:** replace it with women's body fat, Table 1: `33.8 (7.8) 34.0 (28.1, 39.2)`.
  - Compute the IQR: 39.2 minus 28.1 = 11.1.
  - Check the median sits between the quartiles.
  - The mean is *below* the median. Say which way that points.
  - This also meets "reverse the direction at least once" (§7a), which the set currently never does for mean against median.

**D5-9**
- **Field:** `practice[level 6]`, the first one.
- **Claim:** "A man in the study has a body-mass index of 30 kg/m2."
- **Problem:** the paper reports no individual values (Table 2: 10 men at 30 or more). This is an invented datum presented as real ("real figures or none").
- **Severity:** error.
- **Fix:** "Suppose a man in this group had a body-mass index of 30."

**D5-10**
- **Field:** `practice[level 9].answer`, "What this does not establish".
- **Problems:**
  - The first sentence, "It does not establish that no student in the group has a body-mass index of 25 or more", rebuts the note. It does not name a limit of the computation.
  - The answer misses what 39.7 % does not establish:
    - anything about any one man's body fat or health. The paper's own introduction says BMI "does not distinguish between fat mass and lean body mass", line 72.
    - that 25 is a natural line. It is the WHO cut-off the paper chose, and the same introduction notes risk "at lower levels of BMI" in Asians.
- **Severity:** error (the transfer band's "does not establish" is not met).
- **Fix:** replace the first sentence with those two limits. Keep the "one college, one year" sentence.

### Floor

**D5-11**
- **Field:** `illustration.body` (lines 235–242).
- **Claim:** "A men's weight roughly one standard deviation either side of the mean sits around 59 to 85 kilograms… which is the sanity check worth keeping as a habit."
- **Problem:** this relies on an untaught rule, that most values lie within one SD of the mean. That is the bell-curve rule. READY puts it outside Part D, and the anchor states it only for "BELL-SHAPED and SYMMETRIC" data (line 3135).
- **On the drafter's question 4:** no, a reader holding only this record cannot follow why the band is a fair test.
- **Severity:** floor.
- **Fix:** use the check the section does teach. "A first quartile of 167.7 would mean about three in four men weigh 167.7 kg or more. The median says half weigh 70.9 kg or less. Both cannot be true." Then note that 62.6 to 80.9, printed in the height row, fits the weight median.

**D5-12**
- **Field:** `simplified_explanation` (lines 168–178); `practice[level 3]` and `[level 3b]`.
- **Claim:** "Squaring removes the sign", then "-1 times -1 = 1", "-3 times -3 = 9".
- **Problem:** that a negative times a negative gives a positive is not taught anywhere in C01–C26.
  - C01 teaches whole numbers and place value, and contains no negative numbers. The brief's premise that A1 teaches them does not hold.
  - Negatives appear only as results of subtraction (C16 `-236`, C21 `-600 divided by 12 = -50`). They are never multiplied together.
- **Severity:** floor (an algebraic move not taught, spec §1 test 5).
- **Fix, smallest:** square the distance without its sign. "A deviation of −3 means 3 below the mean. Square the distance: 3 times 3 = 9." Or show the rule in two lines before it is used.

**D5-13**
- **Fields:** `definition.text` paragraph 4; the n minus 1 passage; `practice[level 3]` ("sample standard deviation"); `practice[level 7].answer`; retrieval item 2.
- **Problem:** *sample*, *population* and *estimate* are used without definition. They are first taught in C29 (D6), after this section. The only earlier "sample" is C24's "sample space", which is a different thing and invites confusion.
- **Severity:** floor (§10 rule 1).
- **Fix:** gloss inline in C29's own words, so the term is not taught twice in different words. "A sample is the part of a group whose members are actually measured; the population is the entire group the question is about." Then have C29 point back to it.

**D5-14**
- **Field:** `illustration.body`, table header "mean (SD)".
- **Problem:** the acronym SD is never expanded. The prose says "standard deviation" but never ties SD to it, and every paper uses SD.
- **Severity:** floor (acronym).
- **Fix:** add a sentence before the table: "Papers write the standard deviation as SD."

**D5-15**
- **Field:** `definition.text` paragraph 2.
- **Claim:** "The first quartile is the median of the lower half of the ordered values."
- **What is right:** this matches the anchor for an even count.
- **What is missing:**
  - The anchor leaves the median out of both halves when the count is odd. Its 13-price example gives Q1 = (230,500 + 387,000) ÷ 2. The record says nothing about this case.
  - Every quartile problem uses eight values, so the odd case is never met.
  - Nothing says that software computes quartiles by other rules. The paper used SPSS, so a reader who recomputes a published quartile may disagree with it. The section gives exactly this reassurance for n minus 1, and not for quartiles.
- **Severity:** floor.
- **Fix:**
  - Add "When the count is odd, leave the median out of both halves."
  - Add one mechanical problem with seven values.
  - Add one sentence that software uses other quartile rules, so small differences from a paper are not the reader's error.

### Style

**D5-16**
- **Fields:** `must_know` 5; `exercises[1].prompt`; `exercises[1].answer`.
- **Claims:** "A mean sitting on the safe side of a line…". Also: "a cut-off of 25… Both come from a real study of 131 men."
- **Problems:**
  - "Safe side" frames a body-mass index under 25 as safe and the people above it as unsafe (§9, risk framing).
  - 25 is the WHO cut-off the paper used, an institutional line, not a fact of nature (§3).
  - It does not come from the study's data.
- **Severity:** style, but §9 makes it must-fix.
- **Fix:** replace "safe side of a line" with "below a cut-off". Write "the WHO cut-off of 25 that the paper used".

**D5-17**
- **Field:** `practice`.
- **Problem:** four of the fifteen problems are already fully worked in the section (§7a: "If the prompt contains the shape of the answer, it is a worked example").
  - Level 2 (5, 8, 12, 15, 20, 40) is the simplified explanation's own worked set.
  - Level 5 (body fat 22.1 against 20.3) is worked in the illustration.
  - Level 8a (the IQR swap) is worked in the illustration.
  - Level 9 (52 of 131) is worked in the illustration and again in the teaching exercise answer.
- **Separate gap:** the applied band never applies a mean, median or SD computation to real data. It only subtracts printed summaries.
- **Severity:** style.
- **Fix:**
  - Level 2: new numbers.
  - Level 8a: the **women's** rows, `57.4 (155.0, 163.0)` and `159 (51.3, 63.9)`. The same exchange happens there, and the illustration does not mention it.
  - Level 9: the women's version. Mean 23.0 is under 25, and 46 of 151 women, 30.5 %, are at 25 or more.

**D5-18**
- **Field:** `must_know` 6.
- **Problems:**
  - It is tagged `boundary`, but it is a data-checking move. It names no limit of the interquartile range.
  - The section has no boundary for the standard deviation, which is the limit level 10 fell into.
- **Severity:** style.
- **Fix:**
  - Retag 6 as `move`.
  - Add a boundary: "In a lopsided distribution the standard deviation hides that the two sides differ. Use the quartiles." Quote the anchor: `The reason is that the two sides of a skewed distribution have different spreads.`

**D5-19**
- **Field:** `practice[level 4].answer`.
- **Claim:** "The tail is on the high side", from a gap of 0.4 kg/m².
- **Problems:**
  - 0.4 is about a tenth of an SD, between medians printed to one decimal.
  - The paper reports a normality check.
  - The prompt itself said "likely".
- **Severity:** style.
- **Fix:**
  - Say "a slight sign of a tail on the high side".
  - Or add the quartile check: 23.8 minus 21.2 = 2.6 below, and 26.8 minus 23.8 = 3.0 above.

**D5-20**
- **Fields:** `practice[level 3b].prompt`; `practice[level 5].prompt`.
- **Problems:**
  - Level 3b restates the method: "Square them, add the squares, divide by one less than the count" (§7a: "no restatement of the method").
  - Level 5 hints at the answer: "where more than half the men actually sit".
- **Severity:** style.
- **Fix:**
  - Level 3b: "Give the variance and the standard deviation of a sample whose deviations are…"
  - Level 5: "say what it tells you about the men relative to the mean".

**D5-21**
- **Field:** `illustration.body` (lines 244–251); `practice[level 8].answer`.
- **Problems:**
  - "The two rows have had their interquartile ranges swapped" is stated as fact. It is well supported: I verified it in the file for both sexes, since women's 57.4 sits in 51.3–63.9 and 159 in 155.0–163.0. But it is an inference. The paper never says it.
  - "sits almost exactly inside 167.7 to 177.8" is unclear. Is it the mean or the band?
- **Severity:** style.
- **Fix:**
  - "The numbers fit if the two rows' quartiles were printed in each other's places, and the women's columns show the same pattern."
  - Say "the mean, 172.2, sits inside 167.7 to 177.8".

**D5-22**
- **Fields:** throughout.
- **Problems:**
  - "average" and "mean" are used interchangeably and never tied (§10 rule 2). The anchor gives the words: "The words 'mean' and 'average' are often used interchangeably."
  - "kg/m2" appears in prose. It should be `kg/m^2`, and C29 writes kg/m².
  - "body-mass index" differs from C14's "body mass index".
  - Reader-facing prose uses the third person: "A reader who divides…", "Every paper the reader will ever open". It should say "you" (§1).
  - The first sentence does not say it stands on D4 (§10 rule 5).
- **Severity:** style.

---

## Notes on the brief and the drafter's notes

These are not record defects. They were found while checking the notes' claims.

- **Glossary inbox missing.** `prose/glossary-inbox-D.md` does not exist. The inventory says Part D's new terms go there. The D4–D5 notes list eleven new terms, but no file records them.
- **Non-existent rule cited.** The notes cite "claude.md §7 note 7". There is no such note.
- **"range" is not a GLOSSARY row.** The inventory lists it as "already held" as range (C18), but `prose/GLOSSARY.md` has no row for it. C18's own words are the only record, and C27 matches their formula.
- **Seventh inconsistency.** The Kiran header lists six internal inconsistencies. The abstract's two senses of "overweight" (BMI ≥25 in the aims; 83, which is the 25–29.9 count, in the results) look like a seventh (D4-4).
- **Build outputs rewritten.** Running `python check/build.py --check` to confirm the drafter's "0 blocking" rewrote the generated `check/_build/check_report.md` and `check/_build/numbers_register.csv`. Blocking is 0; no warning names C27 or C28.

---

## Verdicts

**B0-R0-C27 (D4).**
- **Sources and arithmetic:** the Table 2 figures are right, and every division checks.
- **Lead illustration:** the abdominal-obesity case is misplaced (it is the abstract, not the results section) and duplicated (C26 works the same check twice). The reader does nothing new.
- **Shape:** the section's one real lesson on shape is wrong. The 98-above against 24-below split comes from where the WHO cut-points sit, not from a tail. A symmetric curve with the paper's own means and SDs reproduces the table almost exactly. Level 8 teaches the same error as its correction and also miscounts: 267, not 243.
- **Core skill:** the three sources of difference, which the section calls its core, are never drilled. The third source omits the one fact D7 most needs: an error the same on every reading shows no spread.
- **Minor sourcing:** the definition quote does not carry most of what it is attached to. Better anchor sentences exist and pass the build's search.
- **Verdict:** needs a real fix pass, not a polish. D4-1 to D4-5, D4-7 to D4-9 and D4-12 to D4-13 must be done before compression.

**B0-R0-C28 (D5).**
- **Arithmetic and cells:** every one of its roughly seventy working lines recomputes correctly. Every table cell is the right cell. The weight/height interquartile-range exchange is real and holds in both sexes.
- **Reasoning:** the defects are in reasoning, and they sit where the course's purpose sits.
  - The level 7 "wrong" answer is not wrong as posed, and it contradicts the section's own statement that dividing by n is a convention.
  - The level 10 answer argues from the standard deviation, which cannot bound the share, while the quartiles printed in the same row settle the question directly.
  - The illustration's sanity check smuggles in the bell-curve rule Part D excludes.
  - The interquartile range is taught as a number and then used as an interval, the same number-against-interval conflict as with *range*.
- **The n minus 1 reason:** directionally true for the variance on average. It overclaims when applied to the standard deviation, and the "every paper" lines overclaim throughout.
- **Floor:** negative times negative is never taught, and neither is *sample*.
- **Title claim:** the 52 of 131 claim is sound but unregistered as a derived number.
- **§9:** the "safe side" framing needs to go.
- **Verdict:** a strong draft that needs about a dozen targeted repairs. None of them requires restructuring.

---

## Resolution (fix pass)

Task 4, 2026-09-23. Applied to `B0-R0-C27` and `B0-R0-C28` against this audit and
`books/B0/DECISIONS-part-D-fix.md` (M1-M15), which overrides this audit where the two differ.
`python check/build.py --check` runs clean for both records: blocking 0, no warning names C27 or
C28. Final practice counts: C27 eleven problems (was nine; added two to drill the three sources of
difference, M7's decisions note plus the audit's D4-12), C28 sixteen problems (was fifteen; added
one mechanical odd-count quartile problem for D5-15). Both stay within three to eighteen and touch
all four bands.

- **D4-1** — fixed. Level 8's "267" is now "243" (24 plus 15 = 39 outer-band students; 282 minus 39
  leaves 243 in the two middle bands untouched by the comparison).
- **D4-2** — fixed. The shape lesson no longer claims a tail from Table 2's bands. It says plainly
  that band counts depend on where the edges fall and that the WHO bands are not centred on this
  group, and shape is taught instead on bare-number sets in `simplified_explanation` (see the
  figures at the end of this section). Level 8's answer states only the band-edge flaw, with no
  substitute shape claim.
- **D4-3** — fixed differently. Rather than relabelling the 113/results-text and 109/abstract
  locators, the whole 113-versus-109 lead was removed (M7 decision plus the brief's instruction not
  to reuse it, since C26 already runs it and may drop it). The locator problem is moot: those two
  numbers no longer appear in C27.
- **D4-4** — fixed differently. Instead of cutting the abdominal-obesity block to one sentence and
  leading with the abstract's overweight/PBF sentence, the lead is now the seventh inconsistency in
  the source header: the abstract's "83 (29.4%) were overweight" against the WHO-cut-off definition,
  resolved by adding the 30-or-more band to get 98 of 282 (34.8%). This tests relative frequency
  directly and Table 2 is introduced as the frequency table in the same breath. A one-sentence
  pointer to the section on conditional probability (C26) opens the illustration instead.
- **D4-5** — fixed. Added the anchor's s.1.2 "Variation in Data" quote (supports the three sources)
  and its s.2.7 skewed-distribution quote (supports shape); kept the original frequency-table quote.
- **D4-6** — fixed. `98` and `282` are registered in `illustration.numbers`, with `98` carrying a
  `derived` field. `34.8` (98 divided by 282) is also registered as derived, since it is now the
  section's own headline check.
- **D4-7** — fixed. "Most distributions bunch up" softened to "Many"; "points toward the values
  that turn up least often" replaced with "points toward the values that sit farthest from the
  middle".
- **D4-8** — fixed. The exercise no longer calls an interval "the range". Prompt: "a range of 338
  minutes"; answer: "every value lies between the smallest and the largest".
- **D4-9** — fixed. Level 9's answer adds the BMI-versus-weight limit: two students with the same
  index can differ in weight by many kilograms if their heights differ.
- **D4-10** — fixed. The exercise no longer asks for D5's median and interquartile range. It now
  asks for a frequency table in useful bands, or how many patients waited more than an hour.
- **D4-11** — fixed. "The World Health Organization, written WHO for short" is introduced in the
  sentence before its first quoted use. Table header and prose write `kg/m^2`; quoted text keeps the
  paper's own flattened form.
- **D4-12** — fixed. Two new practice problems drill the three sources of difference: a mechanical
  one sorting three stated-condition reading pairs, and an applied one on the paper's own
  single-observer sentence.
- **D4-13** — fixed. `definition.text` and `simplified_explanation` both state that an error the
  same on every reading produces no difference between readings, and a new `boundary` must-know
  point says the same thing for D7 to build on.
- **D4-14** — fixed. The prompt no longer names the flaw in parenthesis; it asks a plain question
  ("what share of the men are in the band from 25 to 29.9?") and keeps the same worked lines.
- **D4-15** — fixed. "Exactly as the section on functions taught it" is now "the statistical meaning
  the section on functions warned about, not a rule's range of outputs", in both `definition.text`
  and `simplified_explanation`.
- **D4-16** — fixed differently. The abstract quote used is now the narrow fragment "83 (29.4%) were
  overweight" alone, not the full sentence carrying the body-fat clause, so the second-sense and
  186/185 problems it raised do not arise here.
- **D4-17** — fixed. Must-know 4 states its consequence explicitly; must-know 5 ties the trap to
  band edges; the section's first sentence now points back to the section on ratios, rates and
  proportions in plain words; the frequency-table paragraph in `simplified_explanation` is split so
  each paragraph introduces one term; "distribution" is marked as the statistics meaning, distinct
  from C22's grain-handout sense.

- **D5-1** — fixed. The prompt now says the five values are a sample picked from a clinic's larger
  list and that the sample standard deviation was asked for, so dividing by the count is genuinely
  the step that broke.
- **D5-2** — fixed. Level 10 now argues from the body-fat quartiles printed in the same row (16.7,
  28.8; interquartile range 12.1) to show at most about half the men can lie in any band that width,
  and drops the one-SD-either-side/bell-curve step entirely.
- **D5-3** — fixed, with one exception. `52` and `39.7` (its relative frequency) are registered as
  derived numbers; `1.8` (22.1 minus 20.3) is registered as derived; the `42` and `10` quotes are
  widened with row context so they are unique in the file (the `10` collision with Table 4 is
  resolved). `58.9` and `85.1` are **not** registered: fixing D5-11 removed the mean-plus-or-minus-SD
  "sanity check" that computed them, so they no longer appear anywhere in the record.
- **D5-4** — fixed. The exercise now cites "the report's own target of 5,000 steps" and flags the
  6,200/4,100 figures as made up for the exercise.
- **D5-5** — fixed. Must-know 1's unsourced "single most common error" clause is cut; the point
  stands on "is an error" alone.
- **D5-6** — fixed. The explanation now states the correction holds for the variance on average, not
  for every sample and not exactly for the standard deviation after the square root; "every paper"
  is replaced with "most papers" and the anchor textbook; the anchor's own sentence is quoted; the
  retrieval item is corrected to talk about the variance, not the standard deviation's correction.
- **D5-7** — fixed. The interquartile range is stated and used as one number throughout; every check
  is restated as "the median must sit between the two quartiles printed beside it"; "the printed
  range" language is gone from the illustration.
- **D5-8** — fixed. The duplicate of C27's women's-band practice problem is replaced with the
  women's body-fat interquartile-range problem, which also reverses the mean-versus-median direction
  (mean below median here) as required elsewhere in this list.
- **D5-9** — fixed. "A man in the study has a body-mass index of 30" is now "Suppose a man in this
  group had a body-mass index of 30", in both the practice prompt and its answer.
- **D5-10** — fixed. The "does not establish" paragraph now names the real limits: body-mass index
  does not measure fat mass against lean mass, and 25 is the WHO's chosen cut-off, not a natural
  line, with the paper's own note on Asian risk at lower BMI. The problem is also now posed on the
  women's figures, per D5-17.
- **D5-11** — fixed. The illustration's swap check now runs entirely on the section's own technique:
  checking each row's median against the other row's printed quartiles, and again after swapping
  the ranges back. No bell-curve or one-SD-either-side reasoning remains.
- **D5-12** — fixed (M4). The first time a deviation below the mean is squared, `-1 times -1 = 1` is
  shown on its own with the one-line reason (multiplying by a negative flips a value across zero,
  twice), and the deviation step points back to "the section on counting" for negative numbers.
- **D5-13** — fixed (M5). *Population* and *sample* are defined at first use in `definition.text`,
  in the exact words the decision gives, before either word is used anywhere else in the record.
- **D5-14** — fixed. "Papers write the standard deviation as SD" is added before the first table
  that uses the abbreviation.
- **D5-15** — fixed. `definition.text` states the odd-count rule and the software-variation caveat;
  a new mechanical practice problem (seven ordered values) drills the odd-count case.
- **D5-16** — fixed (§9). "Safe side of a line" is replaced with "below a cut-off" in the must-know
  point and the teaching exercise; the exercise now states plainly that 25 is the WHO cut-off the
  paper used, not a figure that comes from the study's own data.
- **D5-17** — fixed. Level 2's numbers are new. The interquartile-range-swap diagnostic problem
  (formerly duplicating the illustration exactly) now uses the women's rows. The transfer problem
  now uses the women's 46-of-151 figure instead of the men's 52-of-131, which the illustration and
  the teaching exercise both already work through.
- **D5-18** — fixed. Must-know 6 is retagged from `boundary` to `move` and restated as a check
  rather than an interval claim; a new `boundary` point on the standard deviation hiding skew is
  added, quoting the anchor.
- **D5-19** — fixed. Level 4's answer now calls the 0.4 kg/m^2 gap "only a slight sign of a tail on
  the high side, not a firm one".
- **D5-20** — fixed. Level 3b no longer restates the method in the prompt; level 5's hint ("where
  more than half the men actually sit") is removed.
- **D5-21** — fixed. The illustration no longer states the interquartile-range swap as a fact about
  the paper. It shows that the technique itself (median against the other row's quartiles) finds the
  swap, and says the women's columns show the identical pattern rather than asserting it as given.
  The ambiguous "sits almost exactly inside" sentence is gone along with the mean/SD check it was
  attached to.
- **D5-22** — fixed. "Mean" and "average" are tied together with the anchor's own sentence quoted;
  every reader-facing `kg/m2` is now `kg/m^2`; "a reader who..." is rewritten as "you"; the opening
  sentence of `definition.text` now says the section stands on the section on variation.

**M13 (derived numbers), M14 (transfer-band scope) and M6 (range/interquartile range as single
numbers)** are applied throughout both records as part of the item-by-item fixes above, not as a
separate pass.

**Figures for the main thread.**

(a) D4 — the bare-number sets the record uses to teach shape (`simplified_explanation`), printed
exactly as the record gives them:

```
1   2   3   4   5   6   7   8   9   10   11
```

split once as

```
band          count
1 to 3        3
4 to 8        5
9 to 11       3
```

and again, on the same eleven numbers, as

```
band          count
1 to 1        1
2 to 8        7
9 to 11       3
```

(b) D5 — the bare-number set with a tail (`simplified_explanation`'s mean/median demonstration), its
mean and its median, printed exactly as the record gives them:

```
5, 8, 12, 15, 20, 40
```

mean: about 16.7 (`100 divided by 6 = 16.6666666667...`)
median: 13.5 (`12 plus 15 = 27`, `27 divided by 2 = 13.5`)
