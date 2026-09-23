# S01-R1 glossary merge report

CONDUCTOR step 7. Checked against the final text as built by `python check/build.py --subject S01-R1`
(`check/_build/S01-R1.md`, 23 September 2026), not against the draft notes. Section n is record
`S01-R1-C0n`. No record was edited. No existing row of `prose/GLOSSARY.md` was changed.

## 1. Rows added to `prose/GLOSSARY.md` (32)

accounting identity (for a body) (C05); adaptive part (of the fall in expenditure) (C09); adipocyte
(C01); adopted requirement (C03); basal metabolic rate (BMR) (C03); breaks conservation (of a claim)
(C08); consumer unit (C03); conversion table (C03); doubly labelled water (C03); dynamic model (C07);
energy expenditure (C03); energy intake (C03); fat mass (C01); fat-free mass (C01); first law of
thermodynamics (C06); implausible (of a weight-loss claim) (C08); impossible (of a weight-loss claim)
(C08); lean body mass (C01); lever (C06); lipid fraction (C02); maintenance requirement (C04);
megajoule (C02); metabolically active tissue (C01); physical activity expenditure (C04); physical
activity level (PAL) (C03); pound (C07); regulated system (C09); resting energy expenditure (REE)
(C01); static rule (C07); thermic effect of food (C04); total energy expenditure (TEE) (C03); type 2
diabetes (C09).

## 2. Draft-note proposals not added (stale)

- **adaptive thermogenesis, set point, settling point** (b4, C09): none of the three terms appears in
  the final text. C09 now says "the adaptive part"; that is the row added.
- **energy density** (b5, C02): the prose never glosses it. It says "energy per gram". The term
  appears only in Hall's quoted words and, without a gloss, in C02 practice problems 3 and 6. See §4.
- **physical activity level, doubly labelled water** and the other b1 proposals were added, using the
  final text's words.

## 3. Terms already glossed: mismatches against the existing rows

1. **metabolizable energy.** The row, C02 and C04 all spell it "metabolizable". C05 writes
   "metabolisable" four times (Definition, a must-know point, practice 3 and 4). Fix: respell C05.
2. **glycogen.** Book 0 (`B0-R0-C36`) glosses it as "a great many glucose molecules strung together,
   kept in the liver and the muscles". C08 glosses it again in different words: "a form of
   carbohydrate" (Definition) and "a starch-like fuel called glycogen" (In plain terms). Fix: drop the
   second gloss, or use the Book 0 words.
3. **conservation of energy** (minor). C06 has "never made or destroyed, only changed in form". The row
   has "never made and never destroyed; it changes form and it moves". The sense is the same.
   Optional fix.
4. **adipose tissue** (minor). The row has "the tissue whose cells hold triglyceride until it is
   needed". C01 has "fat cells ... together make up adipose tissue", plus "the fatty layer and the
   pockets of fat". The sense is the same and no fix is needed.
5. No mismatch for kilojoule, kilocalorie, Atwater general factors, triglyceride, gross energy,
   catabolism and anabolism, stock, boundary, energy balance, premise, inference or conclusion.

## 4. Drift inside S01-R1 (§10 rule 2)

1. **REE glossed twice.** C01 says "the energy spent at rest". C04 says "the energy spent keeping the
   body alive and running while it does no physical work". Fix: C04 should refer back to C01.
2. **BMR glossed twice.** C03 says "the energy spent lying at rest after a fast". C04 says "measured
   fasting, at rest and in a neutral temperature". Fix: C04 should refer back to C03, adding the
   temperature condition as a detail.
3. **fat-free mass / lean body mass / lean mass.** C01 introduces fat-free mass and gives lean body
   mass as the other name. C02 (prose, table and a must-know point) and C09 then say "lean mass",
   which is never introduced. Fix: C02 and C09 should say "fat-free mass", or C01 should name "lean
   mass" too. Hall's ρL is for lean body mass, so check that the change of name is safe.
4. **classic rule / static rule.** C02 calls it "the classic rule" (prose, a figure caption, a
   must-know point and practice 8). C07 introduces the same thing as "the static rule". Fix: C07
   should say that the static rule is C02's classic rule, or C02 should use one name.

## 5. Terms used before their plain-words introduction

1. **REE and metabolically active tissue.** C01 uses both in the Hall and Guo quotation before
   glossing them on the next line. The build also lists REE among the acronyms used before their
   expansion.
2. **The 3,500-kcal-a-pound rule (static rule).** It is used in C02 and named and defined only in
   C07.
3. **pound.** It is used as a unit from C02 onwards. It is converted and explained only in C07.
4. **deficit (and surplus).** Deficit is used from C02 (the title of the Hall paper, practice 7) and
   through C07 and C08, but never glossed, and it has no Book 0 row. Draft-notes b3 wrongly counted
   it as established in Book 0. Suggested fix: gloss it at first use in the prose, in C02 or C05, for
   example "a deficit: expenditure larger than intake". No row was added because no record teaches
   it.
5. **energy density.** It appears unglossed in C02 practice problems 3 and 6. Fix: say "energy per
   kilogram", as the prose does.
6. **dynamic model.** It appears in C07's figure caption before the prose glosses it (the same
   record).
7. **lever.** It appears in C06's heading before the gloss at the end of the Definition (the same
   record). This is acceptable because it is in the heading.
8. **energy intake and energy expenditure.** "Intake" is used alone in C01 ("when intake falls
   short"). Both terms get their plain words in C03's "In plain terms". C05 adds the deposit and
   withdrawal picture.

## 6. Other items from the build, not part of the glossary

The build also lists SI, NIN, FTC, PMID, NIH, CGPM and NIST as used before their expansion. Two
literal caret or tilde characters reach the rendered page: "kg/m^2" in the Before-you-start list,
and "~100 kcal" in a C09 retrieval or alt string.

## 7. Fixes applied (23 September 2026)

- Fixed: §3.1 metabolizable. C05's nine "metabolisable" respelled "metabolizable", matching the row; no quote touched.
- Fixed: §3.2 glycogen. C08 Definition now says "glycogen (`B0-R0-C36`)", pointing back to Book 0; the "starch-like fuel" gloss in In plain terms is dropped. `B0-R0-C36` added to C08's ground_floor_deps.
- Fixed: §4.1 and §5.1 REE. C01 glosses REE and metabolically active tissue before the Hall and Guo quotation, in the row's words. C04 now reuses them: "Resting energy expenditure (REE), from `S01-R1-C01`, is the energy spent at rest." REE no longer appears in the build's used-before-expansion list.
- Fixed: §4.2 BMR. C04 reuses C03's words and adds the temperature as a detail: "the energy spent lying at rest after a fast, also measured in a neutral temperature". `S01-R1-C03` added to C04's concept_deps.
- Fixed: §4.3 lean mass. C01 now says "Some papers call it lean body mass, or lean mass." The C02 and C09 uses are unchanged, so the C09 prose still matches Leibel's quoted "fat and lean mass". The S01-R1 fat-free mass row now adds "or lean mass".
- Fixed: §4.4 and §5.2 classic rule. C02 now calls it "the static rule" throughout (prose, caption, must-know, practice 8 and the retrieval answer). It is introduced where first used: "The static rule, named in full in `S01-R1-C07`, says a deficit of 3,500 kilocalories removes a pound of weight." Locators are unchanged. No figure text changed, so the figures were not redrawn.
- Fixed: §5.3 pound. C02 now gives "A pound is exactly 0.453 592 37 kilogram." at first use. It is backed by a new nist_sp811_pound reference in C02's Definition that quotes "The exact conversion factor is 4.535 923 7 E-01." The S01-R1 pound row's first-taught column is now `S01-R1-C02`.
- Fixed: §5.4 deficit. C02 glosses it at first use: "A deficit is expenditure larger than intake; a surplus is the reverse." New row added: "deficit (of energy)" (`S01-R1-C02`).
- Build: `python check/build.py --check`: 0 blocking, 103 warnings (54 S01-R1; these are sentence length, reading grade, "never addresses the reader" and two derived illustration numbers, none from these items). The §6 items (the SI/NIN/FTC/PMID/NIH/NIST/CGPM expansions and "kg/m^2" and "~100") were not in scope and remain open.
