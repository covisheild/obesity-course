# C07 blind drafter comparison: correctness audit and counts

What was checked (PIPELINE.md Task 3; claude.md "The one rule that matters", §7a, §7b, §10):

- Every `quote` in each record was searched for in the file `sources/INDEX.yml` maps its citekey to, with whitespace normalised. For every `numbers[]` entry, the quote was checked to state the value.
- Every worked equation in reader-facing prose (`a times/divided by/minus/plus b = c`) was recomputed in Python, at the tolerance the build uses (the digits shown).
- Each practice set was checked for a climb from the mechanical band to the transfer band.
- Reader-facing claims were checked against the held source text. `books/S01-R1/READY.md` was read for the C07 source gate.

Tags: **error** means false, contradicts a source or the record itself, or would block the build. **gap** means unsourced, or a source is held but not used. **style** means the reader has to read it twice, or it breaks a rule in §7a/§10 without being false.

---

## X

**Size:** about 5,970 words of reader-facing prose (definition, simplified explanation, illustration and its limits, must-know points, exercises, practice, retrieval items; about 5,350 without the `working` blocks). **12 practice problems**, at levels 1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10.

**Quotes:** 10 of 10 reference quotes and 14 of 14 number quotes are in the source file. 13 of the 14 number quotes state their value. The 14th is 0.45359237, which carries a correct `derived` field (4.535 923 7 E-01).

**Arithmetic:** 67 equations recomputed. 66 are correct; the one slip is error 1 below.

**Climb:** mechanical (1, 2, 2, 3), then applied (4, 5, 6, using ICMR-NIN Indian figures at level 5), then diagnostic (7, 7, 8), then transfer (9, 10). Each problem varies the move, and level 2b reverses the direction.

| # | Tag | Field | Reason |
|---|---|---|---|
| 1 | error | practice[level 9].answer | `10.42857143 times 5 = 52.14285714`: the product is 52.14285715. It is a last-digit slip, but at the digits shown it fails the build's arithmetic check. |
| 2 | gap | exercises[*] | No exercise carries `skill_ref`, although `provenance.outcome_refs` claims S01-R1-S2. No other S01-R1 record carries it either, so §7's rung check would fail. |
| 3 | gap | definition.references (fao, hall_2011 `verified.note`) | The notes say Hall 2008 is "not held". It is held (`hall_2008_ijo`), and READY.md says "C07: the rule's derivation is now sourced (Hall 2008, block 3)". The rule's derivation (87% fat) is left unused. |
| 4 | gap | must_know[5] (policy) | The draft says Hall "name exactly that use", meaning multiply by 365 and divide by 3,500. Hall 2011 only says the rule was "misapplied at the population level to predict the effect of policy interventions", and does not describe that formula. |
| 5 | style | definition.text | "kcal" and "MJ" are used without being expanded at first use (§10 rule 3). |
| 6 | style | practice[level 5].answer | "the whole requirement, which is what a person would need to eat nothing at all to cover" has to be read twice. |
| 7 | style | exercises[critique].answer | "over-predicted loss by about a quarter" is ambiguous. The shortfall is 27% of the prediction, but the prediction is 37% above the actual loss. |

**X totals: error 1, gap 3, style 3 (7 defects).**

---

## Y

**Size:** about 3,240 words of reader-facing prose (about 2,980 without the `working` blocks). **8 practice problems**, at levels 1, 2, 4, 5, 7, 8, 9, 10.

**Quotes:** 4 of 4 reference quotes and 4 of 4 number quotes are in the source file. 3 of the 4 number quotes state their value. The 4th is 7716.18, which is `derived`; see gap 1.

**Arithmetic:** 27 equations recomputed, and all are correct.

**Climb:** the set reaches all four bands (1–2, 4–5, 7–8, 9–10). Level 1, a division by 0.45359237, is harder than level 2 (3,500 × 5). Levels 9 and 10 test the same move (see style 5). There is no Indian material in the applied band (gap 6).

| # | Tag | Field | Reason |
|---|---|---|---|
| 1 | error | definition.text (also simplified_explanation, illustration) | The draft states the rule as fat: "predicts a change in fat mass" and "a kilogram of fat is worth…". The sources state it per pound of *weight* (Thomas: "one pound of weight loss"; Hall: "energy content of weight lost"). This contradicts the record's own second paragraph. |
| 2 | error | illustration.body | "the calorie the source itself says food energy is measured in, the thermochemical kilocalorie": no held Hall 2011 text says this. The paper gives 480 kcal itself, but the draft uses 478. |
| 3 | error | illustration.body (last paragraph) | "A kilogram of fat is several days of a person's whole daily expenditure" has no expenditure figure anywhere in the record, and it calls the rule's figure fat, against the draft's own caveat. "which is why… takes over two months" is a false causal link: the study durations were set by design. |
| 4 | error | must_know[4] (number) | "takes months to move a double-digit number of kilograms", cited to Thomas. Thomas's 20.1 lb is 9.12 kg, a single-digit figure. The "several days of expenditure" claim is unsourced (same problem as error 3). |
| 5 | error | must_know[3] (consequence) | It calls "roughly a kilogram every two weeks, for the first few months" "a claim you can defend". No deficit or source is given, and the record's own Thomas data show the rule over-predicting within about 65 days. |
| 6 | error | exercises[teaching].answer | It says the rule is "roughly correct" over the first weeks and fails only "past the first year". Thomas says it "significantly overestimates" in 31–93-day studies and warns against it "even as a convenient estimate". Hall says the first-year figure is about 100% too high. |
| 7 | error | practice[level 7].answer | It puts the break at the student's "forever", which implies the one-year line holds. The record's own Hall figures put the first-year line about 2× too high, so the break is already at the textbook's "at that rate". |
| 8 | error | definition.references[3], must_know[5].refs, practice[level 7].refs | It cites `openstax_anatphys_2e` §24.7 as a reference. The source file's note says DO NOT CITE it "for any figure… nor for its reasoning", and READY.md allows it "only as a specimen to diagnose". |
| 9 | gap | illustration.numbers[1] (7716.18) | The derivation rests on the exact NIST factor, but the entry is cited to Thomas, whose quote gives only "about 0.45 kilogram". |
| 10 | gap | illustration.numbers | The illustration uses figures with no `numbers[]` entry, so the build cannot check them: 100 kg, 2 MJ, 75 kg, 103 adults, 64.8 days, 20.1 lb, 27.6 lb, 7.4 lb. All are in the sources. |
| 11 | gap | illustration.body | The dynamic model is "built from the first law of thermodynamics". The held Hall 2011 text does not say this; the wording is Thomas's description of dynamic models in general. |
| 12 | gap | definition.text | "intake and expenditure… both respond to the loss": only expenditure is sourced in the record. `hall_guo_2017`, which says so, is not cited. |
| 13 | gap | definition.text | It traces the rule to "Wishnofsky (1958)" without a reference carrying it. Hall 2008 (held; READY.md names it for C07's derivation) is not used. |
| 14 | gap | practice[4–5] | The applied band has no Indian material, which §7a makes the default. `icmr_nin_2020_brief` is held, and Y uses no requirement figure anywhere. |
| 15 | style | definition.text | It names concept IDs in reader prose ("this subject's C02", "C02's territory"), against §10 rule 5. |
| 16 | style | illustration.body, practice | "kcal" is used without being expanded. |
| 17 | style | illustration.body (last paragraph) | "in the other direction" and "It is not several hours, and it is not… quite as many days as the static line predicts either" do not make sense as written. |
| 18 | style | practice[level 1].prompt | "3,500 removes one unit of weight for every 0.45359237 of a different unit" is garbled. The problem is also harder than level 2. |
| 19 | style | practice[levels 9, 10] | Both are the same 500 kcal → a pound a week claim, with the same move (§7a says to vary the move). Level 10 computes only 500 × 7. |
| 20 | style | definition.references[3].verified.note | It says the do-not-cite marking is in `sources/INDEX.yml`. It is not: the marking is in the source file and READY.md. |

**Y totals: error 8, gap 6, style 6 (20 defects).**

---

## Summary

| Draft | error | gap | style | total | words (reader-facing) | practice problems |
|---|---|---|---|---|---|---|
| X | 1 | 3 | 3 | 7 | ~5,970 | 12 |
| Y | 8 | 6 | 6 | 20 | ~3,240 | 8 |

Not checked: figures (neither record names any), and currency beyond noting that the ICMR-NIN 2020 values match the held Brief Note. Hall 2008 was checked only to confirm that it is held and names the derivation. Its quotes were not audited, because neither draft cites it.

---

Label mapping: X = `C07-opus.yml`, Y = `C07-sonnet.yml`.
