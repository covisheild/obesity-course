# S01-R1 step 5c: restore decisions

Restorer: not the cutter and not the cold reader. Inputs: `COLDREAD-REPORT.md`, and
`<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml` for C01 to C10. The restore lists
are in `restore-lists/S01-R1-Cnn.txt`, and each restored line is commented with the gap it
closes. The outputs are `S01-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and
checked by `check/compress/validate.py`. The tools were not changed.

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means it was not closable here and is recorded in `../DEFECTS.md` (item number
given). **not a defect** means nothing to do.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → final | Validate |
|---|---|---|---|---|---|---|
| C01 | 956 | 333 | 421 | +88 | 14.94 → 14.03 | OK |
| C02 | 1873 | 971 | 1090 | +119 | 18.97 → 18.67 | **FAIL** (see "Tool conflict") |
| C03 | 1425 | 724 | 855 | +131 | 22.27 → 21.38 | OK |
| C04 | 1267 | 625 | 706 | +81 | 19.80 → 16.42 | OK |
| C05 | 1229 | 552 | 627 | +75 | 17.13 → 16.16 | OK |
| C06 | 1228 | 553 | 591 | +38 | 19.56 → 18.58 | OK |
| C07 | 1484 | 756 | 908 | +152 | 19.90 → 18.44 | **FAIL** (see "Tool conflict") |
| C08 | 1466 | 739 | 779 | +40 | 19.79 → 19.46 | OK |
| C09 | 1125 | 469 | 625 | +156 | 20.45 → 18.94 | OK |
| C10 | 1116 | 451 | 507 | +56 | 16.91 → 16.90 | OK |
| **Total** | 13219 | 6173 | 7109 | +936 | | 8 OK, 2 FAIL |

`python check/build.py --check` / `--subject S01-R1` (PIPELINE step 5c's last line) was not run
here. It needs the final text written back into the records, which is outside this step's brief.

## Tool conflict (C02, C07): needs the conductor's decision

In two places the pass-1 cut kept only part of what `build._sentences` counts as one sentence:

- C02 `must_know[4].point`: "... is far lower than fat's. This record names the number ...". The
  splitter's abbreviation rule treats `'s.` as an abbreviation, so the two sentences count as one.
- C07 `illustration.body`: '... predicted by the 3500 kcal rule." A kilogram of fat is several days
  ...'. The splitter does not split after a closing quote.

`restore.py` can bring back only the whole unit, and `validate.py` then reports the cut's fragment
as "kept by the cut, missing after restore". The fragment's text is present in the final file
(checked by substring). An empty list fails as well: C02's field comes out empty, and C07 loses the
kept sentence. No list can pass. Each final file therefore carries the whole unit, which adds about
24 words (C02) and 30 words (C07) that no gap asked for. The fix belongs to the cut or to the
tools, not to the list. Either re-cut those two units on the splitter's boundaries, or have
`restore.py`/`validate.py` agree on the boundary. Tools were not touched.

## Gap by gap

### Global
- **GL-1** not a defect: the renderer fixed it (instruction).
- **GL-2** hole, DEFECTS 1: the original uses the same record/concept/rung/gate vocabulary.
- **GL-3** hole, DEFECTS 2. C05's restored "Because it is a balance line applied ..." ties
  "identity" to the balance line. "First law" is defined nowhere in the original.
- **GL-4** hole, DEFECTS 3: the practice sets are absent in the original too, and exercises are
  not the compression pass's to change.
- **GL-5** hole, recorded per section: DEFECTS 47 (C07) and 58 (C09).

### C01
- **G1** restored: "It does not say how much of adipose tissue's own weight is fat rather than
  water ..." This gives the "not pure fat" that C02 relies on. The unassigned compartment remains
  (DEFECTS 4).
- **G2** restored: "Read on, in the same paragraph." and the Hall and Guo quote "Fat-free mass is
  elevated in obesity, along with body fat ..." These are the source for "they carry more of
  both".
- **G3** hole, DEFECTS 5 and 8: the original never expands REE or explains "metabolically
  active".
- **G4** hole, DEFECTS 6: the original never explains body protein as a store.
- **G5** restored: "Pack enough fat cells together ..." and "That is the store." These give the
  antecedent of "It is a large store".
- **G6** hole, DEFECTS 7: the original says outright that it gives no method.
- **G7** hole, DEFECTS 4: the original uses the same three terms.

### C02
- **G1** restored in C01 (C01-G1). Once that is in, the back-reference holds.
- **G2** hole (error), DEFECTS 9: "9 kilocalories ... for each kilogram" is also in the original.
- **G3** hole (error), DEFECTS 10. The original's partial answer ("Close, not identical ...", 56
  words) was tried and dropped, because it raised the mean sentence length from 18.97 to 19.34
  and failed validation.
- **G4** hole, DEFECTS 11: the original also names the rule before stating it.
- **G5** hole (error), DEFECTS 12: the original has the same 7,830 against 7,700.
- **G6** hole (error), DEFECTS 13: the production artefact is in the original.
- **G7** hole (error), DEFECTS 14: the original has the same working and gloss.
- **G8** restored: "Lean tissue's own energy density is far lower than fat's. Hall (2008) gives
  17.6 and 19.7 ... once the water that moves with them is counted, of 7.6 ..." This gives the
  source and why lean is below protein (water). The missing quote remains (DEFECTS 15).
- **G9** restored: "Search on for the word variable." and the Hall quote "the change of body fat
  ... variable contribution of fluid and protein ..."
- **G10** hole (error), DEFECTS 41 (merged with C07-G3).
- **G11** hole, DEFECTS 1.
- **G12** restored: "It is the same 87% reappearing wherever the same rule is computed."
- Abbreviations (BIPM, FAO, MJ): hole, DEFECTS 16.

### C03
- **G1** restored: "Worked examples given for three populations put total energy expenditure at
  8.26 ... 9.86 ... 16.42 ..." This names the three groups. The "about ten" contradiction is in
  the original (DEFECTS 17).
- **G2** hole, DEFECTS 18: the original names the method's duration but not how it works.
- **G3** hole (error), DEFECTS 19: "measured" is also in the original.
- **G4** hole, DEFECTS 26: the original never expands PAL, BMR or TEE.
- **G5** hole, DEFECTS 20: the original has no column headings.
- **G6** restored: "India's National Sample Survey puts the all-India average acquisition at
  2,233 ... rural and 2,250 ... urban for 2022-23." This maps the columns. "Purchases" against
  "bought or grown" remains (DEFECTS 21).
- **G7** hole (error), DEFECTS 22: the original has the same contradiction.
- **G8** restored: "India's Indian Council of Medical Research and National Institute of
  Nutrition set ... rising to 3,470 and 2,720 for heavy work." This also expands ICMR and NIN.
- **G9** restored: "There is a fourth thing worth knowing before you trust any number a person
  tells you themselves." Source and direction remain (DEFECTS 23).
- **G10** hole, DEFECTS 24.
- **G11** hole, DEFECTS 25.

### C04
- **G1** restored: "This is the smallest of the three shares." Now the ranking is in the body
  before the Must-know. The ranking is still unsourced (DEFECTS 27).
- **G2** hole, DEFECTS 28.
- **G3** restored: "The heavier patient's resting expenditure, the largest of the three
  components, is expected to be higher ..." This answers the illustration's question.
- **G4** hole, DEFECTS 29: the original has the same sentence.
- **G5** hole, DEFECTS 31.
- **G6** restored: "So a maintenance requirement worked out for a person at one weight does not
  hold ..." This gives the referent of "the number".
- **G7** restored: "This record names the three components and says each depends on body size."
  This gives the referent of "it".
- **G8** hole, DEFECTS 30.
- **G9** not a defect here: it rests on C01-G2, which is now restored with its source.

### C05
- **G1** restored: "Draw the boundary at the mouth and skin, as B0-R0-C33 shows for a person, and
  count intake at the metabolisable line ..."
- **G2** restored: "Take a made-up week, seven days, ..." The verb "measured" remains (DEFECTS 32,
  error).
- **G3** hole (error), DEFECTS 33: the original makes the same energy/mass slide.
- **G4** restored: "Because it is a balance line applied to one particular stock, the identity
  carries no direction and no cause."
- **G5** not a defect: code mapping (GL-1).
- **G6** hole, DEFECTS 34.
- **G7** hole (error), DEFECTS 36.
- Abbreviations (FAO, WHO, UNU): hole, DEFECTS 35.

### C06
- **G1** hole, DEFECTS 37: "lever" is unexplained in the original.
- **G2** hole, DEFECTS 2.
- **G3** hole, DEFECTS 38.
- **G4** restored: "A trainee who has just learned this identity will reach for 'energy in, energy
  out' as an explanation ..." This says which sentence to watch for.
- **G5** restored: "Say what changed, in energy terms, if you know it." This gives the antecedent
  of "it changed".
- **G6** hole, DEFECTS 39.
- **G7** not a defect: F4's illustration does state the missing premise in a sentence ("Nobody ...
  says out loud that eating sits untouched by price"). The pointer is fair.

### C07
- **G1** restored: "First, real tissue lost is not pure fat, so a single fixed
  kilocalories-per-kilogram figure cannot hold ...; that is C02's territory." The brief listed
  this under (b), but the original fills it word for word, so it is a cut-made hole and was
  restored. No defect was recorded.
- **G2** hole (error), DEFECTS 40.
- **G3** hole (error), DEFECTS 41.
- **G4** restored: "About 26.6 pounds predicted, close to the 27.6 pounds the rule in fact
  predicted for this cohort in the paper." The 20.1 against 20.2 remains (DEFECTS 42).
- **G5** hole, DEFECTS 43.
- **G6** restored: "The dynamic model says the loss slows and levels off, because the man's
  expenditure falls as his body gets smaller ..." The source details remain (DEFECTS 47).
- **G7** restored: "Because D is held fixed, the predicted change is a straight line against time
  ..."
- **G8** restored by the same G6 sentence ("... even though intake has not changed again").
- **G9** hole, DEFECTS 44: the original gives no interval that fits the Thomas data.
- **G10** hole (error), DEFECTS 45.
- **G11** hole (error), DEFECTS 46.
- **G12** restored: "The static rule is not merely optimistic here."
- Tool-forced: "What they actually lost, measured, ..." brings back the rest of the same unit, "A
  kilogram of fat is several days ... to move 20 pounds." See "Tool conflict".

### C08
- **G1** hole (error), DEFECTS 48.
- **G2** hole (error), DEFECTS 49.
- **G3** hole, DEFECTS 50.
- **G4** hole, DEFECTS 51.
- **G5** restored: "The body stores some energy as glycogen, and Hall and colleagues note ...
  'intracellular water associated with stored glycogen and protein'." This sources "stored with
  water". There is still no figure (DEFECTS 52).
- **G6** hole (error, wording only), DEFECTS 53. The code-mapping half is not a defect (GL-1).
- **G7** hole, DEFECTS 54.
- **G8** hole (error), DEFECTS 55.

### C09
- **G1** hole (error), DEFECTS 56: the original repeats "more than three times".
- **G2** restored: "After a person sustains a loss of 10% or more of body weight, 24-hour energy
  expenditure falls by about 20% to 25%, and that fall runs about 10% to 15% below what ...
  would predict."
- **G3** restored: "The extra fall is the adaptive part: ... roughly 300 to 400 fewer calories
  ..." The illustration's mislabel remains (DEFECTS 57, error).
- **G4** restored: "The researchers measured body weight week by week and worked back ..." This
  gives the antecedent of "They" and the method. The citation remains (DEFECTS 58). The
  "Polidori's own comparison" sentence was not restored, because it repeats the G1 error.
- **G5** hole, DEFECTS 59.
- **G6** restored: "Rosenbaum and Leibel's patients, after losing a tenth of their body weight
  ..." This names the source for the expenditure figure. The sensing claim is still unsourced
  (DEFECTS 60).
- **G7** hole (error), DEFECTS 61.
- **G8** hole (error), DEFECTS 62.
- **G9** restored: "Energy intake and energy expenditure are not two independent dials a person
  sets and then leaves alone."
- **G10** hole, DEFECTS 63.

### C10
- **G1** hole (error), DEFECTS 64: the original is the same, and more pointed.
- **G2** hole (error), DEFECTS 65.
- **G3** hole (error), DEFECTS 66. The original's "A person can cut intake exactly as instructed
  and still see the scale stall ..." was not restored, because it repeats the flaw.
- **G4** restored: "Written out in full it runs: ... (premise one).", "Cutting intake, with
  expenditure held fixed, therefore reduces stored energy (premise two, ...)." and "Conclusion:
  ..." Premise two is now laid out before it is cited. The definition/illustration mismatch and
  the unnamed "earlier concept" remain (DEFECTS 65).
- **G5** hole, DEFECTS 1.
- **G6** hole (error), DEFECTS 67.
- **G7** hole, DEFECTS 68.

## Holes by section

| Section | Errors | Gaps |
|---|---|---|
| Global | 0 | 3 |
| C01 | 0 | 5 |
| C02 | 5 | 3 |
| C03 | 4 | 6 |
| C04 | 0 | 5 |
| C05 | 3 | 2 |
| C06 | 0 | 3 |
| C07 | 5 | 3 |
| C08 | 4 | 4 |
| C09 | 4 | 4 |
| C10 | 4 | 1 |
| **Total** | **29** | **39** |
