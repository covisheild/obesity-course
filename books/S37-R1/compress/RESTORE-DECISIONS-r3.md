# S37-R1 step 5c: restore decisions, batch r3 (C13 to C18)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (gaps B-C13-* to
B-C18-*), and `<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml` for C13 to C18. The
restore lists are in `restore-lists/S37-R1-Cnn.txt`, each restored line commented with the gap it
closes. The outputs are `S37-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and
checked by `check/compress/validate.py`. The tools were not changed. The holes are in
`HOLES-r3.md`, numbered H1 onwards.

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means the original does not fill it either, or it is an error or contradiction:
it goes to the audit. **not a defect** means nothing to do. "Restored, residual hole" means the
original closed part of the gap and the rest is in `HOLES-r3.md`.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → cut → final | Validate |
|---|---|---|---|---|---|---|
| C13 | 978 | 500 | 573 | +73 | 13.40 → 13.16 → 13.02 | OK |
| C14 | 870 | 473 | 548 | +75 | 15.26 → 15.26 → 15.22 | OK |
| C15 | 1064 | 571 | 604 | +33 | 14.78 → 14.64 → 14.73 | OK |
| C16 | 1349 | 785 | 785 | 0 | 13.65 → 13.52 → 13.52 | OK |
| C17 | 726 | 481 | 481 | 0 | 13.20 → 12.66 → 12.66 | OK |
| C18 | 1351 | 876 | 934 | +58 | 11.87 → 11.14 → 11.01 | OK |
| **Total** | 6338 | 3686 | 3925 | +239 | | 6 OK |

C16 and C17 have a comment-only list, so each still has a `-final-prose.yml`.

`python check/build.py --check` / `--subject S37-R1` was not run. It needs the final text written
back into the records, which is outside this brief.

**One restoration dropped for sentence length (C14).** With the fair-price-shop sentence that
expands DFPD (B-C14-5), C14's mean sentence rose from 15.26 to 15.28 and validation failed. That
sentence was taken out and B-C14-5 became a hole (H13). No tool conflict arose.

## Tally

| | Restored | Hole | Not a defect |
|---|---|---|---|
| C13 | 4 (2 with a residual hole) | 3 | 1 |
| C14 | 4 (2 with a residual hole) | 4 | 0 |
| C15 | 1 | 4 | 0 |
| C16 | 0 | 7 | 1 |
| C17 | 0 | 5 | 0 |
| C18 | 1 | 7 | 0 |
| **Total (42 gaps)** | **10** | **30** | **2** |

## Gap by gap

### C13
- **B-C13-1** restored, residual hole H1. Restored in `definition.text`: "The contents per 100 grams
  come from a food composition table.", "India's is the Indian Food Composition Tables 2017 (IFCT)
  ...", "IFCT prints energy in kilojoules only.", "The figures are physiologically available
  energy, worked out by the Atwater system." and "IFCT converts them to kilocalories with 1 kcal =
  4.18 kJ." The reader now knows 4.18 is the tables' own stated factor. The original never says
  whether 4.18 is a rounding of 4.184, or whether the 450 kcal norm uses the same calorie (H1).
- **B-C13-2** restored, residual hole H2. The IFCT sentence above expands ICMR-NIN. "Sedentary" and
  "reference" are undefined in the original too (H2).
- **B-C13-3** hole H3. The original also gives the primary gram norms only in the figure, and never
  says whether they are raw weights.
- **B-C13-4** restored by the same IFCT sentences. The tables' energy is now stated as Atwater
  (physiologically available), the same system as the 37 kJ/g fat factor. Adding them is
  consistent, and the "never mix factors" warning concerns 4.18 against 4.184.
- **B-C13-5** hole H4. The original is identical: it gives no reason for "at most" or for leaving the
  vegetables out.
- **B-C13-6** hole H5. The original says "the 2017 tables' average" with no more.
- **B-C13-7** restored: "The Department of Food and Public Distribution itself calls the ration
  supplemental." (`must_know[5].point`). This is the original's sentence immediately before the
  orphan "So", and it gives the "So" its premise.
- **B-C13-8** not a defect. The problem asks what the answer does not establish, and the reader
  answered it fully, including the missing children's figures.

### C14
- **B-C14-1** restored, residual hole H6. Restored "The report's text says 595.05."
  (`must_know[2].point`), so "when text and table disagree" now has both numbers. The figure's
  seven bars sum to 605.88, not the 607.40 total. The original has the same bars (H6).
- **B-C14-2** restored, residual hole H7. Restored "The DFPD allocates grain to welfare
  institutions and hostels, 5.83 lakh tonnes for 2025-26.", which explains the hostels bar. The
  "tide over" and "adolescent girls" bars are unexplained in the original too (H7).
- **B-C14-3** hole H8. The original C14 never names PM POSHAN's ministry either. Its "The DFPD
  allocated it" misleads the reader in the same way.
- **B-C14-4** restored: "The earlier sections showed what each scheme promises one person ..." and
  "This one steps back and asks how big the whole thing is." Together they give "It is very big"
  its antecedent. The second alone would have left "This one" dangling.
- **B-C14-5** hole H13. The original expands DFPD in "The grain goes out through fair price shops,
  of which the Department of Food and Public Distribution (DFPD) counts 5.51 lakh". Restoring it
  raised the mean sentence length (15.26 → 15.28), so it failed validation and was dropped.
- **B-C14-6** hole H9. The original never says how WBNP wheat becomes a prepared ration.
- **B-C14-7** restored: "As on March 2026 the mission's tracking system followed nearly 14,03,170
  ..." It names the source Exercise 1 asks for.
- **B-C14-8** hole H10. The original has no practice set either, and exercises are not this pass's
  to change.

### C15
- **B-C15-1** restored: "The child is wasted when weight-for-height is more than two standard
  deviations below it, and underweight when weight-for-age is." and "The child is overweight when
  weight-for-height is more than two standard deviations above it." Every child bar in the figure
  now has its yardstick.
- **B-C15-2** hole H11. The original's two words and three WHO levels are the same, still with no
  label for "checked, passes, one burden" and no mapping. "A calorie norm with nothing else is a
  single-duty design" was not restored, because it does not settle Ex 1(b).
- **B-C15-3** hole H12. The original asserts the rule without evidence or a named population.
- **B-C15-4** hole H14. The original has the same "adult aged 15 to 49" and does not name whose
  BMI cut-offs they are.
- **B-C15-5** hole H10 (practice set) and H15 (no WHO source or link).

### C16
- **B-C16-1** hole H16. The original's Stage column and its plain-terms walk ("At the farm ... At
  the plate ... across all of it sits tax") also depart from C01's eight stages. It is a mismatch
  between sections, not missing text.
- **B-C16-2** hole H17. The original's map also leaves out the APMC mandi.
- **B-C16-3** hole H18. The original also calls the 2024 value "the duty on edible oils", with
  basic or effective unstated.
- **B-C16-4** hole H19. The original never quotes the 24 September 2026 release either.
- **B-C16-5** not a defect. The table's descriptions ("two national cooperative federations", "a
  price support scheme") are enough for every exercise. Naming them would not let the reader do
  anything they could not do already.
- **B-C16-6** hole H20. The original says "two Poshan 2.0 awareness campaigns in 2025", but it does
  not name them either, or tie them to C17's.
- **B-C16-7** hole H21. MSP "rests on a decision" in C16, but C09 cites NFSA s. 2(10). The original
  is the same, so this is a contradiction between sections.
- **B-C16-8** hole H10.

### C17
- **B-C17-1** hole H22. The contradiction with C05 (information is an element) is in the original
  word for word.
- **B-C17-2** hole H23. Poshan Maah, the jaggery rule and nutrition gardens are unintroduced in the
  original too. The exercise text is untouchable.
- **B-C17-3** hole H24. The original gives no stage or actor for a tax, and no teaching on who bears
  it.
- **B-C17-4** hole H25. "Dietary guidelines" is introduced nowhere in the original.
- **B-C17-5** hole H10.

### C18
- **B-C18-1** restored:
  - "You take one packaged food you eat often." and "You write down where it came from ..." say
    what "the book's build" is.
  - "Start with the label." and "Its ingredient list is in order of weight, heaviest first" give
    the orphan "So the first few names ..." its premise.
  - "In this sketch the tools on each crop are checked." and "The brand and the shop are seen."
    give the worked sketch its own tally.

  The other blank runs the reader saw were left by deleted sentences. In the final file they
  close up once a paragraph is rewrapped, and no kept sentence around them lacks a premise.
- **B-C18-2** hole H26. The original also skips invert sugar syrup, and Exercise 1 asks for four
  ingredients.
- **B-C18-3** hole H27. The original also marks the crude palm oil duty "checked" for refined oil
  of unknown form.
- **B-C18-4** hole H28. The original never defines "recovery". Its "sugar season that starts on 1
  October 2026" was not restored, because it would not let the reader interpret the 10.25%.
- **B-C18-5** hole H29. The original never says whether a licence number makes the maker checked.
- **B-C18-6** hole H30. The C18 definitions are correct where they stand. The defect is that
  kirana (C05) and quintal (C09, C10) are used earlier without them.
- **B-C18-7** hole H31. The original also asserts the MSP link to a miller's wheat without showing
  it.
- **B-C18-8** hole H32. The original also leaves FSSAI labelling and GST off the sketch, and gives
  no GST rate.
