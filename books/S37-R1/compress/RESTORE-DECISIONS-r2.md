# S37-R1 step 5c: restore decisions, batch r2 (C07 to C12)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (gaps A-C07-* to
A-C09-* and B-C10-* to B-C12-*), and `<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml`
for C07 to C12. Restore lists are in `restore-lists/S37-R1-Cnn.txt`, each line commented with the
gap it closes. Outputs are `S37-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and
checked by `check/compress/validate.py`. The tools were not changed. Nothing was committed.

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means not closable here; it is written up for the fixer in `HOLES-r2.md`.
**not a defect** means nothing to do. Where a restore closes only part of a gap, the rest is also
in `HOLES-r2.md`, marked "residual".

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → final | Validate |
|---|---|---|---|---|---|---|
| C07 | 926 | 476 | 563 | +87 | 14.47 → 14.44 | OK |
| C08 | 1216 | 675 | 735 | +60 | 12.66 → 12.60 | OK |
| C09 | 1029 | 496 | 633 | +137 | 14.10 → 13.47 | OK |
| C10 | 731 | 407 | 463 | +56 | 14.33 → 13.62 | OK |
| C11 | 717 | 365 | 429 | +64 | 13.53 → 13.00 | OK |
| C12 | 930 | 570 | 639 | +69 | 14.21 → 13.67 | OK |
| **Total** | 5549 | 2989 | 3462 | +473 | | 6 OK |

Tally: 53 gaps. Restored 22, hole 28, not a defect 3.

## Validation constraint (C07, C08): two gaps left open by the mean-sentence rule

Two gaps had a filling sentence in the original that could not be restored without raising the mean
sentence length above the original's, which `validate.py` fails. They are recorded as holes, not
worked round:

- C07, A-C07-1: "India's Household Consumption Expenditure Survey (HCES), run by ..." (31 words).
  Alone it takes the mean from 14.42 to 14.91 against the original's 14.47.
- C08, A-C08-1: "The Economic Survey 2025-26's table of foodgrain availability ..." (25 words). It passes
  alone (12.65), but not with the restores for A-C08-2/3/5 (12.69 to 12.75). Those restores close
  three gaps against one, so they were kept.

This is the rule working as written, not a tool bug. The fixer can close both by splitting the
sentence in the record (HOLES-r2 items 1 and 11).

## Gap by gap

### C07
- **A-C07-1** hole (validation constraint above; HOLES 1). The original names and expands HCES in
  its first sentence. Restoring it fails validation.
- **A-C07-2** hole (error; HOLES 2). The original also says "Across the same years" over
  2011-12/2023-24 calorie years against 2011-12/2022-23 spending years.
- **A-C07-3** hole (HOLES 3). The original never says which survey Report 594's consumption data
  come from, or whether the "two surveys" are independent.
- **A-C07-4** restored: "The surveys before 2009-10 used a different reference period for some
  foods." and "Report 594 used a conversion table from a committee set up in 2025." Together they
  show what the caution means and that both calorie years share one table. Residual: whether the
  2011-12 and 2022-23 spending rounds match (HOLES 4).
- **A-C07-5** restored: "Rung 2 reads these changes against the nutrition transition." and "That is
  Popkin and colleagues' name for a shift ...". This is the definition; the first sentence is its
  antecedent.
- **A-C07-6** restored: "The headline shares leave out the value of food received free ..." and
  "From 2022-23 the survey records that food separately and reports a second set of estimates that
  includes it." They tie the section's shares to the headline set and say what imputing adds.
- **A-C07-7** hole (HOLES 5). The original never lists the other food groups either.
- **A-C07-8** hole (HOLES 6). No price change is given in the original.
- **A-C07-9** not a defect. Ex 1 prints the shares and asks what they show, not to recompute them.
- **A-C07-10** hole (HOLES 7). The original names the group's contents but gives no split within
  it, which is what Ex 2 and P11 would need.

### C08
- **A-C08-1** hole (validation constraint above; HOLES 11). The antecedent sentence exists in the
  original.
- **A-C08-2** restored: "A Food Department was set up in 1942, in the war, because of acute food
  shortage." and "The ration shops of the public distribution system started in the 1960s to manage
  scarcity." With the kept FCI 1965 sentence, "Each time" now covers three institutions.
- **A-C08-3** restored in part by the same "ration shops of the public distribution system"
  sentence, which ties PDS to ration shops. Residual: "ration" and its rice-and-wheat content are
  never stated in the original (HOLES 12).
- **A-C08-4** hole (HOLES 13). The original also calls a net export a "surplus" without defining it.
- **A-C08-5** restored: "Read how the Department describes the Food Corporation today." and "It is
  the main instrument for buying and distributing wheat, rice and coarse grains, the cereals other
  than those two." This defines coarse grains; the first sentence is the antecedent of "It".
- **A-C08-6** hole (structure; HOLES 14). The original has no practice set either, and exercises are
  not the compression pass's to change.

### C09
- **A-C09-1** restored: "As of 24 September 2026: MSP for common paddy ... a quintal being 100
  kilograms (CCEA, 13 May 2026)." This defines the quintal, which also serves C10 (B-C10-2).
- **A-C09-2** restored: "It says nothing about one farm, one state, or what the crop fetched." This
  gives the reason the margin is not profit. Residual: "weighted" and "imputed" stay undefined
  (HOLES 21).
- **A-C09-3** hole (HOLES 22). The original also uses "margin" differently from C04 without
  flagging it.
- **A-C09-4** restored: "Pulses, oilseeds and copra are procured under the Price Support Scheme of
  PM-AASHA ..." and "Cotton and jute are procured through the Cotton Corporation of India and the
  Jute Corporation of India."
- **A-C09-5** restored: "From 2014-15 to 2025-26, 8,746 lakh tonnes were bought across the 14 kharif
  crops." and "Paddy was 8,418 of them ...". These show that "one" is among kharif crops. Residual:
  the claim still sits badly with wheat procurement (HOLES 23).
- **A-C09-6** restored by the same two sentences, which make the figure a 12-year total. Residual:
  "lakh" is undefined in the original too (HOLES 24).
- **A-C09-7** hole (HOLES 25). C10's restored "Paddy is milled before it becomes rice." gives the
  relation, but no conversion ratio exists in either section.
- **A-C09-8** restored: "The Union Government fixes a fair and remunerative price (FRP), also on
  CACP's recommendation, ...". This settles "the same way". The rabi count follows once the 14 kharif
  crops are restored (22 − 14 = 8), and "Sugarcane has no MSP" keeps it out of the 22.
- **A-C09-9** hole (HOLES 26). The paddy MSP and its release now come back with A-C09-1. The cost
  (Rs 1,627) is printed nowhere in the original.
- **A-C09-10** hole (structure; HOLES 27). The original has no Illustration or practice set either.

### C10
- **B-C10-1** restored: "The central issue price is the price at which the Union government issues
  the grain to the States." Residual: its link to the Schedule I price is not stated (HOLES 31).
- **B-C10-2** restored in C09 (A-C09-1): the quintal is defined there, one section earlier.
- **B-C10-3** restored: "Second, it sells grain to ration-card holders for less than the grain cost
  it." and "The gap between the two is the subsidy." This closes a sentence left dangling by the cut.
- **B-C10-4** restored: "Three wedges are computed here, each by one rule." It says which tools are
  wedges.
- **B-C10-5** hole (HOLES 32). The original never explains basic against effective duty.
- **B-C10-6** hole (HOLES 33). The printed moong margin is in no version.
- **B-C10-7** hole (HOLES 34). Kharif is defined nowhere, and rabi only in a problem.
- **B-C10-8** hole (HOLES 35). Problem 12 carries no paddy data, and the paddy cost is printed
  nowhere.
- **B-C10-9** hole (HOLES 36). "Tide over" is unexplained in the original.
- **B-C10-10** hole (number; HOLES 37). The 2022-23 bar conflicts with free grain from 1 January 2023.
- **B-C10-11** hole (HOLES 38). The original gives only the same three words, "buy, store and move".
- **B-C10-12** hole (HOLES 39). The original does not say which oil "nil" is.
- **B-C10-13** restored: "Paddy is milled before it becomes rice." Residual: there is no conversion
  ratio, so the size of the effect cannot be estimated (HOLES 25).

### C11
- **B-C11-1** restored: "Since 1 January 2023 the grain has been issued free, by decision of the
  Union government under the Pradhan Mantri Garib Kalyan Anna Yojana." and "That decision was
  extended on 29 November 2023 for five years from 1 January 2024."
- **B-C11-2** not a defect. No exercise or later section needs the wheat or coarse-grain Schedule I
  price. The rice price is kept.
- **B-C11-3** restored: "Section 3(2) extends the entitlement to up to seventy-five per cent of the
  rural population and up to fifty per cent of the urban population."
- **B-C11-4** not a defect. The reader could check "most" from the text (about 58 per cent), and it
  holds.
- **B-C11-5** hole (cross-file; HOLES 41). The original also states the Antyodaya 35 kg without the
  Central Government proviso.
- **B-C11-6** hole (structure; HOLES 42). There is no practice set in the original.

### C12
- **B-C12-1** restored: "Pradhan Mantri Poshan Shakti Nirman (PM POSHAN), earlier the Mid-Day Meal
  Scheme, is run by the Ministry of Education."
- **B-C12-2** hole (HOLES 51). The original never says which classes are lower or upper primary.
- **B-C12-3** restored: "Section 6 adds meals for children who suffer from malnutrition."
- **B-C12-4** hole (HOLES 52). "The school-meal table" is also the original's wording, and it points at
  no separate table.
- **B-C12-5** hole (number; HOLES 53). The original has the same "severely" against the table's
  "malnourished".
- **B-C12-6** hole (H; HOLES 54). The scope of the January 2023 revision differs between C12 and C13
  in the originals too.
- **B-C12-7** restored: "The 2022 guidelines set the Centre's share of supplementary nutrition at 50
  per cent ..." and "It is 90 per cent in the north-eastern and Himalayan States ...". These are the
  split that the kept "No document held gives PM POSHAN's split" is set against.
- **B-C12-8** hole (structure; HOLES 55). There is no practice set in the original.

`python check/build.py --check` / `--subject S37-R1` was not run. It needs the final text written
back into the records, which is outside this brief.
