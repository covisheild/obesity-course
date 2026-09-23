# Verification · Book 0 Part D fix pass, D4–D5 (`B0-R0-C27`, `B0-R0-C28`)

Audit of the fix pass, 2026-09-23. What was checked:

- The current records, against `DEFECTS-part-D-d4d5.md`, the fixer's appended "Resolution" section, and `DECISIONS-part-D-fix.md` (M4–M8, M13, M14).
- Every changed number, recomputed in python.
- Every quote, searched in its source with the build's normalisation.
- The figure, compared against its image, its caption and alt text, and `check/figures/draw.py`.
- `python check/build.py --check` was run. It regenerates `check/_build/check_report.md`.

No record was edited.

## Headline

**The fixer's "all 39 closed" is not true.** 28 of the original items are closed, 10 are partly
closed and 1 is not closed. There are 23 new or still-open defects, listed in section 3.

- **D5-7 is not closed.** It is the interquartile range used as an interval, which M6 forbids. That usage survives in eleven places.
- **The fixer's claim about warnings is false.** It says no build warning names C27 or C28. The build names them 21 times (12 for C27, 9 for C28): sentence length and reading grade.
- **The arithmetic is clean.** Every new working line recomputes correctly.

Most of what remains is in sourcing detail and in the new material itself.

---

## 1. Status of every original defect

| id | status | note |
| --- | --- | --- |
| D4-1 | closed | 243, in both places. |
| D4-2 | partly | The illustration and level 8 are fixed per M7. Level 9 still says "Most of the group sits clustered in the middle" (V4-6). |
| D4-3 | closed | 113/109 removed. The new lead has its own locator error (V4-1). |
| D4-4 | closed | The pointer back to C26 is valid: C26 still runs the 113 check (C26 line 703). |
| D4-5 | closed | The s.1.2 and s.2.7 quotes are present and support their claims. |
| D4-6 | partly | 98, 282 and 34.8 are registered. The derived quotes cover only the 83 cell, and the cut-off 25 is unregistered (V4-7). |
| D4-7 | closed | |
| D4-8 | closed | |
| D4-9 | closed | |
| D4-10 | closed | |
| D4-11 | closed | WHO is expanded and kg/m^2 is used. The new quote adds an unnamed ≥ (V4-8). |
| D4-12 | closed | Two problems were added. Both carry new defects (V4-4, V4-5). |
| D4-13 | closed | The new boundary point is right. The definition's wording is muddled (V4-9). |
| D4-14 | closed | |
| D4-15 | closed | |
| D4-16 | closed | Moot now. |
| D4-17 | partly | The content is fixed. Must-know 4 is now one 41-word sentence and must-know 6 one 34-word sentence (V4-10). |
| D5-1 | closed | The prompt now says "sample". |
| D5-2 | closed | Level 10 now argues from the quartiles 16.7 and 28.8. The argument is sound. |
| D5-3 | partly | 52, 39.7 and 1.8 are registered and the 42 and 10 quotes are widened. The derived quotes omit the cells they were counted from (V5-10). |
| D5-4 | closed | |
| D5-5 | closed | |
| D5-6 | partly | The retrieval item is fixed and "most papers" is used. The new text overstates what the textbook says (V5-4), and the new quote has a wrong locator (V5-3). |
| D5-7 | **not closed** | The interval sense survives in eleven places (V5-1). |
| D5-8 | closed | |
| D5-9 | closed | |
| D5-10 | closed | Moved to the women's figures. The limits named are right and attributed to the paper. |
| D5-11 | closed | |
| D5-12 | partly | The rule is shown with a one-line reason. It points back to "the section on counting", which in this working copy has no negative numbers (V5-9). |
| D5-13 | closed | M5's words are used exactly. |
| D5-14 | closed | |
| D5-15 | closed | The odd-count rule matches the anchor. The new problem gives Q1 5, Q2 9, Q3 15 and IQR 10, all correct. |
| D5-16 | closed | §9 is clear. |
| D5-17 | partly | Level 2 is new and level 9 now uses the women. Level 8 is now pre-answered by the illustration (V5-6). The new level 5 repeats level 4 (V5-7). Level 9 repeats C27's level 6 (V5-8). |
| D5-18 | closed | |
| D5-19 | partly | Level 4 is fixed. The new level 5 brings the overclaim back (V5-7). |
| D5-20 | closed | |
| D5-21 | partly | The illustration now hedges. The level 8 answer still states the swap as fact (V5-6). |
| D5-22 | partly | Mean and average are now tied together, which creates a new contradiction (V5-5). "Anchor textbook" reaches the reader (V5-4). Sentence warnings remain (V5-12). |

**Totals:** 28 closed, 10 partly, 1 not closed.

---

## 2. Re-audit of what changed

**Arithmetic.** Every new line was recomputed in python and is correct.

- **C27:**
  - The bands on the numbers 1 to 11 hold 3 / 5 / 3 and then 1 / 7 / 3.
  - 98 ÷ 282 = 34.75.
  - 71 − 58 = 13, and 70.6 − 70.4 = 0.2.
  - 282 − 39 = 243.
- **C28:**
  - Level 2 gives 108, 18 and 12.5.
  - The odd-count quartiles are 5, 9 and 15, with IQR 10, by the anchor's method of leaving the median out of both halves.
  - The women's body-mass index gap is 0.3.
  - The women's body-fat IQR is 11.1.
  - Level 7 gives 22.5 and 4.743.
  - The women's swap checks all come out as the record says.
  - Level 9 gives 30.46. Level 10 gives 12.1 and 1.8.

**Quotes.** All present. Two have locator errors (V5-2, V5-3). One also matches the source file's own header note (V4-7).

**States-the-number rule.**

- Every non-derived entry states its number.
- Every derived entry names its derivation.
- The derived entries' quotes cite only part of the passage they were counted from (V4-7, V5-10).

**Figure.** `d5-mean-median.png` shows dots at 5, 8, 12, 15, 20 and 40, a solid median line at 13.5 and a dashed mean line at 16.7.

- The image matches the alt text.
- `draw.py` reads the six numbers from the record and stops with an error if the mean or median drifts from 16.7 and 13.5.
- One caption clause overstates (V5-13).

**§9.** No breach in either record.

---

## 3. New or still-open defects

### C27

**V4-1**
- **Field:** `illustration.body`, the new lead.
- **Problem:** the text says the paper "defines its own terms before it uses them" and quotes the Methods sentence. It then says "A few pages later, the paper reports… '83 (29.4%) were overweight'". That sentence is in the **abstract** (source line 48), which comes **before** the Methods. The abstract also carries its own definition: "to screen overweight (BMI ≥25 kg/m2)". The results text itself labels 83 as "(BMI: 25–29.9 kg/m2)" (line 255).
- **Smallest fix:**
  - Quote the abstract's own definition and its own count.
  - Say "In its abstract, the paper defines… and then reports…".
  - Add one line: the results section labels the same 83 correctly as the 25 to 29.9 band.
- **Severity:** error.

**V4-2**
- **Field:** `illustration.body`.
- **Problem:** the text says "Run the check a frequency table always deserves", and later "the fix is the same move either way: divide the count by the total". But 83 ÷ 282 = 29.43, which matches the printed 29.4. The division check that must-know 2 and retrieval item 2 teach **passes** here. What catches the error is a different check: does the label's definition match the band the count sits in? As written, the illustration credits the section's check with a catch it did not make.
- **Smallest fix:**
  - Say the division check passes here.
  - Name the second check: "match each label to the band it covers".
  - Add it as a sentence in must-know 2.
- **Severity:** error.

**V4-3**
- **Field:** `simplified_explanation`, shape lesson.
- **Problem:** "three bands centred on the middle number, each reaching three either side of it" does not describe the table. The bands 1–3, 4–8 and 9–11 have a middle band reaching **two** either side of 6, and outer bands **three numbers wide**. The "band" labelled "1 to 1" is a single value.
- **Smallest fix:**
  - Say: "a middle band from 4 to 8, two either side of 6, with three numbers left on each side".
  - Label the single value as "1".
- **Severity:** error.

**V4-4**
- **Field:** `practice[level 3, three sources]`.
- **Problems:**
  - The prompt asks "which of the three sources … produced the gap", and (b)'s answer gives "Within a person" alone. The definition says a spread comes from "one or more of three sources". A 1.2 kg gap four days apart also contains whatever the scale contributes, so the problem teaches that each gap has one source, which D7 will contradict.
  - The answer adds an unsourced physiological premise: food, drink and time of day "can each move a weight reading by more than a kilogram" (spec §1 test 6).
  - The problem has units and patients, so it is not the level 1–3 band (bare numbers).
- **Smallest fix:**
  - (b): "Mostly within a person. Part of the 1.2 kg could still come from the scale, and nothing here separates the two."
  - Drop "by more than a kilogram".
  - Relabel it level 4.
- **Severity:** error.

**V4-5**
- **Field:** `practice[level 5, single observer].prompt`.
- **Problem:** "The same paper, describing its own limitations, says this." The quoted sentence is the paper's stated **strength**: "The strength of the study was…", line 740, under "Strengths and limitations".
- **Smallest fix:** "describing what it counts as its own strength".
- **Severity:** error.

**V4-6**
- **Field:** `practice[level 9].answer`.
- **Problems:**
  - "Most of the group sits clustered in the middle" is a shape claim read off the WHO bands. The illustration and level 8 of the same record now say those bands cannot support one.
  - "98 students … are above it" appears with no working line.
- **Smallest fix:**
  - Say "160 of the 282 sit in the one band from 18.5 to 24.9".
  - Add the working `83 plus 15 = 98`.
- **Severity:** style.

**V4-7**
- **Field:** `illustration.numbers`.
- **Problems:**
  - Derived `98` and `34.8` quote only `Overweight (25–29.9 kg/m2) 83 (29.4)`. They were counted from the 83 row **and** the 15 row (M13: "the passage it was counted from").
  - The cut-off 25, used in the illustration, is unregistered.
  - The abstract `83` quote, `83 (29.4%) were overweight`, now also matches the source file's own header note (line 20). The build can be satisfied by the curator's note instead of the paper.
- **Smallest fix** (every quote below passes the normalised search once):
  - For 98 and 34.8, quote `Overweight (25–29.9 kg/m2) 83 (29.4) 42 (32.1) 41 (27.2) Obese (≥30 kg/m2) 15 (5.3)`.
  - Register 25 with the quote `Overweight was defined using the WHO cut-offs (BMI ≥25 kg/m2)`.
  - Widen the 83 quote to `Of the 282 participants, 83 (29.4%) were overweight`, which matches the abstract only.
- **Severity:** error (sourcing).

**V4-8**
- **Field:** `illustration.body`, the quoted definition.
- **Problem:** "(BMI ≥25 kg/m2)" puts the symbol ≥ in front of the reader unnamed. No record before C27 names it (C26 uses it only inside quotes). This is spec §1 test 1.
- **Smallest fix:** after the quote, add "The sign ≥ means 'at or above'." Better still, make that addition at its first use in C26.
- **Severity:** floor.

**V4-9**
- **Field:** `definition.text`, paragraph 6.
- **Problems:**
  - "That last kind … can hide completely": a *difference* cannot hide. What hides is an error that produces no difference.
  - The sentence is 50 words long (build warning).
- **Smallest fix:** split it. "That last kind comes from the instrument and the act of measuring, not from any change in what was measured. An instrument can also be wrong without producing any difference: …"
- **Severity:** style.

**V4-10**
- **Field:** throughout.
- **Problem:** the build now names C27 twelve times: sentence length, and reading grade 10.3 and 10.6 on the new level 3 prompt and level 5 answer. The fixer reported none.
- **Smallest fix:** split at natural joints, as M15 did for C24–C26.
- **Severity:** style.

### C28

**V5-1**
- **Field:** several (D5-7 not closed).
- **Problem:** M6 forbids calling the interval "the interquartile range" or "the range". It survives in eleven places:
  - the illustration table header "median (interquartile range)";
  - "Stop on the weight row's interquartile range";
  - "swapping the two printed ranges";
  - "had their interquartile ranges printed in each other's places";
  - `analogy_breaks_when`: "catches a range that sits nowhere near the median … inside the range by chance";
  - level 5b: "interquartile range of 21.2 to 26.8";
  - level 8 answer: "printed range of 51.3 to 63.9", "ranges are swapped back", "had their interquartile ranges swapped";
  - level 10: "interquartile range of 16.7 to 28.8".
- **Smallest fix:**
  - Header: "median (first and third quartiles)".
  - Elsewhere: "the two quartiles printed beside it".
  - Add one sentence once, before the table: "The paper labels this pair IQR; the interquartile range itself is the difference between them."
- **Severity:** error.

**V5-2**
- **Field:** `definition.references[0]`.
- **Problem:** the quote `The words "mean" and "average" are often used interchangeably.` has straight quotation marks. It matches only **s.1.1** (source line 158). The s.2.5 sentence the locator names has curly marks (line 1708) and would not match.
- **Smallest fix:** locator "s. 1.1 Definitions of Statistics, Probability, and Key Terms".
- **Severity:** error (sourcing).

**V5-3**
- **Field:** `definition.references[6].locator`.
- **Problem:** "The Sample Variance and Standard Deviation" is not a heading in the source. The quoted sentence (line 2809) sits under "Explanation of the standard deviation calculation shown in the table" (line 2791).
- **Smallest fix:** correct the locator.
- **Severity:** error (sourcing).

**V5-4**
- **Field:** `simplified_explanation`, the n minus 1 passage.
- **Problems:**
  - "…which is the same reason the anchor textbook this book follows gives for the rule" is not true. The anchor gives no mechanism. It says only that "The sample variance is an estimate of the population variance" and that "dividing by (n – 1) gives a better estimate", "based on the theoretical mathematics".
  - "Anchor textbook" is internal jargon reaching the reader.
- **Smallest fix:** "The textbook this book follows puts it briefly: dividing by one less 'gives a better estimate of the population variance'."
- **Severity:** error.

**V5-5**
- **Field:** `definition.text`, paragraphs 2, 5 and 6.
- **Problem:** the definition now makes "average" mean exactly "mean": sum divided by count. It then says "The variance is the average of the squared deviations", and then that for a sample it divides by one less than the count. By the definition just given, that is not an average. `definition.text` has to be technically exact.
- **Smallest fix:** "The variance is worked out from the squared deviations: add them, then divide by the count for a whole population, or by one less than the count for a sample."
- **Severity:** error.

**V5-6**
- **Field:** `illustration.body`; `practice[level 8, women]`.
- **Problems:**
  - The illustration now says "the paper's own table for the 151 women shows the identical pattern in the same two rows". The level 8 diagnostic asks the reader to find exactly that, so the problem is pre-answered.
  - The level 8 answer states the swap as fact ("have had their interquartile ranges swapped in the paper's own table"). That is the D5-21 defect again.
- **Smallest fix:**
  - Delete the women sentence from the illustration.
  - In level 8, say "the numbers fit if the two rows' quartiles were printed in each other's places".
- **Severity:** style.

**V5-7**
- **Field:** `practice[level 5, women's body-mass index]`.
- **Problems:**
  - It is level 4's move with other numbers ("vary the move, not just the numbers").
  - Its answer brings back the certainty D5-19 removed. From a 0.3 gap, about a twelfth of an SD, it says "A smaller number of women … pull the mean up past where most of the group sits".
  - Level 6b's low-side tail from a 0.2 gap is hedged and fine.
- **Smallest fix:** make it a new move. Read the tail from quartile spacing on men's body-mass index: 23.8 − 21.2 = 2.6 below the median, and 26.8 − 23.8 = 3.0 above. Or at least hedge the answer as level 4 does.
- **Severity:** style.

**V5-8**
- **Field:** `practice[level 9]`.
- **Problem:** the computation (41 + 5 = 46, and 46 ÷ 151 = 30.5 per cent) is word for word C27's level 6. The transfer problem drills D4's move, not D5's. M14 is met, but only formally.
- **Smallest fix:** compute from D5's technique instead. Table 1 prints the women's body-mass index as `22.7 (20.5, 25.6)`. The third quartile, 25.6, is above 25, so about a quarter or more of the women are at 25.6 or above even though the mean is 23.0. This quote passes the search. Keep the current "does not establish" paragraph.
- **Severity:** style.

**V5-9**
- **Field:** `simplified_explanation`: "the kind of number the section on counting introduced".
- **Problem:** in this working copy, `B0-R0-C01` (unchanged since 2026-09-22) contains no negative numbers. M4 makes the pointer true only after the Part C close-out merges.
- **Smallest fix:** none in C28. Block the Part D commit on that merge, and re-grep C01 for negative numbers after it.
- **Severity:** floor (conditional).

**V5-10**
- **Field:** `illustration.numbers`, derived entries.
- **Problems:**
  - `52` quotes only the 42 cell. It was counted from 42 and 10.
  - `39.7` quotes neither 52's cells nor 131.
  - `1.8` quotes only `22.1 (7.3)`, not 20.3.
  - Still unregistered: the cut-off 25, n = 131, and 2019 (in `analogy_breaks_when`).
- **Smallest fix** (every quote below passes the search once):
  - For 52 and 39.7, quote `Overweight (25–29.9 kg/m2) 83 (29.4) 42 (32.1) 41 (27.2) Obese (≥30 kg/m2) 15 (5.3) 10 (7.6)`, plus the derivation text for 131.
  - For 1.8, quote `22.1 (7.3) 20.3 (16.7, 28.8)`.
  - Register 25 (quote `Overweight was defined using the WHO cut-offs (BMI ≥25 kg/m2)`) and 2019 (quote `July–September 2019`).
- **Severity:** error (sourcing).

**V5-11**
- **Field:** `illustration.body`.
- **Problem:** "Both rows fail the same way, and each one fails against the other row's numbers" is backwards. Each row fails against its *own* quartiles and **passes** against the other row's.
- **Smallest fix:** "and each one passes against the other row's numbers."
- **Severity:** style.

**V5-12**
- **Field:** throughout.
- **Problems:**
  - The build names C28 nine times. It includes a 49-word sentence on the n minus 1 caveat, a 42-word sentence and reading grade 11.2 in the level 9 answer, and a 36-word sentence in the teaching answer. The fixer reported none.
  - "The same shape shows up again in body fat" points back to nothing, since the passage before it is about a cut-off, not a shape.
- **Smallest fix:**
  - Split the long sentences.
  - Say "Body fat shows the tail directly."
- **Severity:** style.

**V5-13**
- **Field:** `figures[0].caption`.
- **Problem:** "…the single value of 40, which is the only thing that moved it there". Without the 40, the mean of the other five values is 12 and so is their median. The 40 moves the median too, from 12 to 13.5. The caption implies the median was untouched. The simplified text correctly says "almost where it would have been". Image, alt text and record otherwise agree.
- **Smallest fix:** "The mean, 16.7, has been pulled towards the single value of 40. Without it, both would be 12."
- **Severity:** style.

---

## Counts

**Original 39:** 28 closed, 10 partly, 1 not closed.

**New or still-open items:** 23, as the numbered list above.

| severity | count | items |
| --- | --- | --- |
| error | 12 | V4-1, V4-2, V4-3, V4-4, V4-5, V4-7; V5-1, V5-2, V5-3, V5-4, V5-5, V5-10 |
| floor | 2 | V4-8, V5-9 |
| style | 9 | V4-6, V4-9, V4-10; V5-6, V5-7, V5-8, V5-11, V5-12, V5-13 |

## Verdicts

**B0-R0-C27:** the big defects are fixed: the shape inference, 267, the duplicate lead and the undrilled three sources. But the new lead misplaces its quote and credits the division check with a catch it did not make. The shape lesson misdescribes its own bands. Both new practice problems carry an error each. It needs one more short fix pass.

**B0-R0-C28:** the reasoning defects are fixed: level 7, level 10, the bell-curve check and n minus 1 on the standard deviation. The "interquartile range as interval" problem the fixer reported closed is still in eleven places. Two new locators are wrong, and the definition now contradicts itself on "average". It needs one more short fix pass, and it waits on the C01 merge for its pointer about negative numbers.
