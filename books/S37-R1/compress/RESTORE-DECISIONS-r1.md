# S37-R1 step 5c: restore decisions, batch r1 (C01 to C06)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (gaps A-C01-* to
A-C06-*), and `<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml` for S37-R1-C01 to C06.
Restore lists are in `restore-lists/S37-R1-C0n.txt`, each line commented with the gap it closes.
Outputs are `S37-R1-C0n-final-prose.yml`, built by `check/compress/restore.py` and checked by
`check/compress/validate.py`. The tools were not changed. No record was edited.

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means the original does not fill it either, or it is an error or contradiction, or
(marked) the original fills it but the restore could not pass validation; each is in
`HOLES-r1.md`. **not a defect** means nothing to do. Where a restore closes only part of a gap, the
rest is carried to `HOLES-r1.md` as a residual.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → final | Longest orig → final | Validate |
|---|---|---|---|---|---|---|---|
| C01 | 777 | 444 | 552 | +108 | 13.63 → 13.46 | 39 → 39 | OK |
| C02 | 928 | 531 | 635 | +104 | 14.50 → 14.43 | 32 → 28 | OK |
| C03 | 861 | 420 | 472 | +52 | 14.11 → 13.88 | 31 → 31 | OK |
| C04 | 841 | 419 | 487 | +68 | 14.75 → 14.32 | 32 → 29 | OK |
| C05 | 789 | 420 | 483 | +63 | 12.52 → 11.78 | 29 → 26 | OK |
| C06 | 800 | 434 | 493 | +59 | 13.56 → 12.64 | 33 → 33 | OK |
| **Total** | 4996 | 2668 | 3122 | +454 | | | 6 OK |

Decisions: 55 gaps. Restored 20, hole 35, not a defect 0.

`python check/build.py --check` / `--subject S37-R1` was not run: the final text is not yet
written back into the records, which is outside this brief.

## The mean-sentence constraint bit twice

In C01 and C02 the cut's mean sentence length sat close to the original's, and the sentences the
gaps call for are long. Every candidate list was measured before building; where a sentence would
have pushed the mean over the original's, it was left out and its gap sent to the holes file with
the original sentence quoted, so the fixer can decide. No sentence was restored to pull the mean
down.

- C01: "Which stages, places and flows count as inside is fixed by a boundary ..." (24 words, closes
  A-C01-7). With the two dangling-antecedent restores (A-C01-1, A-C01-3) it cannot fit under 13.63
  in any combination.
- C02: "For India, a study by the consultancy NABCONS for the Ministry of Food Processing Industries
  ..." (32 words, closes A-C02-2). With the RBI source sentence (A-C02-1) it cannot fit under 14.50.
  The shorter must-know sentence "That is the NABCONS study for 2020-22, as the ministry reported it
  in 2025." was restored instead; it gives the years and release year, not who NABCONS is or which
  ministry.

## Gap by gap

### C01
- **A-C01-1** restored: "Inside the system, HLPE names the food supply chain ..." (antecedent of
  "It lists the chain's steps"), and must-know "Cooking and eating sit in the food system as
  consumer behaviour." (why the kitchen is in the system but not in the chain's steps).
- **A-C01-2** restored: "The list is this book's reading of HLPE's sentences, not a list HLPE
  prints." Residual hole (H1): the original never says why eight, why this order, or why waste is a
  stage.
- **A-C01-3** restored: "Each step is done by somebody, such as a farmer, a trader, a mill owner, a
  shopkeeper or the person who cooks." (the cut left "Call each of them an actor" with no
  antecedent) and "Each stage is an activity carried out by actors." Residual hole (H2): no actor
  at the waste stage, and the state's status as actor, anywhere in the original.
- **A-C01-4** hole (H3): the original names no kind of source that could check a stage either.
- **A-C01-5** hole (H4): the original never gives the reason for "food system" over "diet".
- **A-C01-6** restored: "Perhaps it was stored in a warehouse, or milled and packed in a factory."
  and "And after the meal, what is left over goes somewhere too." (the walk's storage, processing
  and waste steps). Residual hole (H5): no Illustration and no practice set, in the original too.
- **A-C01-7** hole, restore blocked by validation (H6): the original's boundary sentence answers it
  but raises the mean.

### C02
- **A-C02-1** restored: "The Reserve Bank of India (RBI) working paper on tomato, onion and potato
  (Working Paper 08 of 2024) describes the onion route ..." Sources the mandi account and the
  secondary-mandi quotation.
- **A-C02-2** hole, partly restored (H7): must-know "That is the NABCONS study for 2020-22, as the
  ministry reported it in 2025." The sentence that names NABCONS and the ministry was blocked by the
  mean (see above).
- **A-C02-3** hole (H8): the original never states the base of the loss percentages.
- **A-C02-4** hole (H9): the original never places "market level" against UNEP's retail line.
- **A-C02-5** hole (H10): the original gives no reason not to add the two percentages.
- **A-C02-6** restored: must-know "It is built from seven city studies scaled to the national
  population." (what "modelled" means). Residual hole (H11): "medium confidence" never explained.
- **A-C02-7** restored: must-know "The eggs row of the ministry's loss table sits under 'million
  tonnes' and cannot be tonnes." (the incident the rule points at).
- **A-C02-8** hole (H12): the original gives no population either; Ex 2's 78 cannot be checked in C02.
- **A-C02-9** restored: "Retailers buy there and sell in neighbourhood markets." and "The trader
  pays a fee to the mandi and a commission to the agent." Residual hole (H13): the commission's base.
- **A-C02-10** hole, partly restored (H14): "Potatoes often sit for months in a cold store on the
  way." shows a storage stage; the original never maps the route onto C01's eight stages.
- **A-C02-11** hole (H5): no Illustration or practice set in the original.

### C03
- **A-C03-1** restored: "The Food Safety and Standards (Labelling and Display) Regulations, 2020,
  made by the Food Safety and Standards Authority of India (FSSAI), govern ..."
- **A-C03-2** restored: "The list therefore ranks the ingredients." ("It" is the list). Residual
  hole (H15): "for example" leaves the 5(2)(g) triggers open, in the original too.
- **A-C03-3** hole (H16): "with the source optional" is the same in the original.
- **A-C03-4** hole (H17): invert sugar syrup undefined in the original.
- **A-C03-5** restored: "If the manufacturer is someone else, only the manufacturer's licence
  number must appear (regulation 5(7)(b))." Residual hole (H18): licences never introduced.
- **A-C03-6** hole (H19): the original's Definition sentence also leaves "compound ingredient"
  undefined and gives no regulation number; restoring it would not let the reader do more.
- **A-C03-7** hole (H20): contradiction ("weight or volume" against "heaviest first") is in the
  original.
- **A-C03-8** hole (H21): the original names no class title beyond Sugar and Milk solids.
- **A-C03-9** hole (H5): never shown with numbers in the original.

### C04
- **A-C04-1** hole, partly restored (H22): "A fee at the market yard, a commission, a lorry, a mill,
  a packet, a wholesaler and the shopkeeper each added something." gives the hands in order in
  words; the figure's ten stages are unnamed in the original too.
- **A-C04-2** hole (H23): no base, no cost breakdown, in the original too; it breaks the section's
  own rule.
- **A-C04-3** hole (H24): the original never says which base the table prints.
- **A-C04-4** hole (H25): milk 70 against 35/49 = 71.4, unexplained in the original.
- **A-C04-5** restored: must-know "The RBI papers tie the low farmer's share of vegetables to
  perishability." (the source of the pattern, and the antecedent of the cut's "Suppose a proposal
  raises it"). Residual hole (H26): "spoil" undefined; milk on the "keep" side.
- **A-C04-6** hole (H27): no worked split of a mark-up into cost and margin in the original.
- **A-C04-7** hole (H28): origin per pulse and mandi price = farm-gate price, not in the original.
- **A-C04-8** restored: "Six rupees added to a price of 65 is about 9 per cent of 65.", "The same
  six rupees is about 8 per cent of the 71 the shopkeeper sells at." and "Both are true." (the trap
  itself).
- **A-C04-9** hole (H29): exercise wording; exercises are not this step's to change.
- **A-C04-10** hole (H30): "stage" used for two things, in the original too.
- **A-C04-11** hole (H31): three of four papers and the poultry figure's source unidentified in the
  original.

### C05
- **A-C05-1** restored: "In the Indian chains the Reserve Bank of India (RBI) studied in 2024, these
  decisions are observable."
- **A-C05-2** restored: "Processors and aggregators contract for crops before harvest."
- **A-C05-3** restored: must-know "APMCs fix mandi fees and commission charges, and on the RBI's
  onion route to Delhi these were 1 and 4 per cent." ("part of the price" is the fee).
- **A-C05-4** restored: "Processors spend on brand promotion." (promotion) and "A trader decided
  which grade of onion went to which city." (quality). Residual hole (H32): no actor for safety.
- **A-C05-5** hole (H33): not mapped onto the eight stages in the original.
- **A-C05-6** hole (H5): no Illustration or practice set in the original.
- **A-C05-7** hole (H34): taxes absent from the original.

### C06
- **A-C06-1** restored: "India's official series of per capita net availability of foodgrains,
  published in the Economic Survey's Statistical Appendix Table 1.19, applies the same identity
  with two further subtractions."
- **A-C06-2** restored: "A net imports figure, imports minus exports, is enough for the SSR and not
  enough for the IDR." Residual hole (H35): "net production" is named only in the figure and
  exercises.
- **A-C06-3** hole (H36): gross or net production in the SSR, not said in the original.
- **A-C06-4** restored: must-know "The FAO's handbook says so in as many words, and India's table
  follows it." (the table's stock sign).
- **A-C06-5** hole (H37): the wheat row misses by 2 and no tolerance is given, in the original too.
- **A-C06-6** hole (H38): 43.75 against 43.74.
- **A-C06-7** hole (H39): "supply" in the 56.25 claim is not the Definition's supply.
- **A-C06-8** hole (H40): PIB "consumption" not placed as availability or intake.
- **A-C06-9** hole (H41): 2021-22 row and stock changes not given.
- **A-C06-10** hole (H42): "exports left out": zero or unknown, not said.
