# Compression-pass holes, triaged · B0-R0-C36 (E6)

Auditor: Task 3, fresh context. Full per-hole verdicts: `books/B0/compress/TRIAGE-part-E.md`.

---

**C36-K1** · CONFIRMED-ERROR (internal inconsistency)
- **Field:** `definition.text` (paragraphs 5, 6 and 7), `simplified_explanation` (closing paragraph)
- **Sentences:** "Excess glucose is either stored as an energy reserve in the liver and skeletal muscles as the complex polymer glycogen, or converted into fat" against "When a person eats more glucose or carbohydrate than the body needs, that excess is turned into fat." and "when catabolism lets go of more than anabolism is using, the extra is built into fat and put away."
- **What is wrong:** the same word "excess" is given two different fates, glycogen-or-fat and fat only, two sentences apart. must_know[6] ("Spare energy goes to glycogen and to fat") and the illustration ("Some goes into the near store … Some goes into the far store") follow the first. Each sentence is in a held source (A&P 24.1 line "Excess glucose is either stored … as the complex polymer glycogen, or it is converted into fat (triglyceride) in adipose cells"; A&P 24.3 "When you eat more glucose or carbohydrates than your body needs, your system uses acetyl CoA to turn the excess into fat"). The source does not reconcile them, and the record has to.
- **Fix:** paragraph 6: "A triglyceride is the molecular form that fat takes both in food and in the body. Glucose beyond what the body needs can be turned into fat, as well as stored as glycogen." The plain-terms closing sentence becomes "the extra is put away, in the near store and the far one." Leave the 24.1 net-energy sentence (paragraph 8) as the source words it ("building fat molecules for long-term storage").
- **Support:** held, the A&P 24.1 sentence quoted above.
Fix: definition paragraph 6 now reads "Glucose beyond what the body needs can be turned into fat, as well as stored as glycogen." The plain-terms closing now reads "the extra is put away, in the near store and the far one." Paragraph 8 is unchanged.
Verify: closed

**C36-K2** · CONFIRMED-GAP (minor)
- **Field:** `definition.text`, `simplified_explanation`
- **Sentence:** "A living cell cannot store significant amounts of free energy." / plain: "A cell cannot hold a useful amount of loose energy."
- **What is wrong:** "free energy" reads as a technical term and is never linked to "loose energy".
- **Fix:** plain terms: "A cell cannot hold a useful amount of loose energy, which the textbooks call free energy: energy ready to do a job."
- **Support:** "ready to do a job" is a gloss, and no held sentence defines free energy. If a source is required, drop the gloss and keep only the link: "…loose energy (the book's phrase is free energy)."
Fix: plain terms now read "A cell cannot hold a useful amount of loose energy, which the textbooks call free energy." Used the link-only fallback; the "ready to do a job" gloss was dropped because no held source defines free energy.
Verify: closed


**C36-K3** · CONFIRMED-GAP
- **Field:** `definition.text`
- **Sentences:** "All carbohydrates are absorbed in the form of monosaccharides." / "fibrous polysaccharides, such as cellulose" / "large organic molecules"
- **What is wrong:** monosaccharide and polysaccharide are never defined. The plain terms say "single sugar molecules" and "a long chain of sugar molecules" but never attach the words.
- **Fix:** plain terms, at the starch paragraph: "…you get single sugar molecules, called monosaccharides. A chain of them, such as starch, is a polysaccharide." "Organic molecules" is covered by C35-K1.
- **Support:** held. A&P 24.1: "complex carbohydrates, polysaccharides like starch and glycogen, or simple sugars (monosaccharides) like glucose and fructose."
Fix: plain terms now read "…single sugar molecules, called monosaccharides. A chain of them, such as starch, is a polysaccharide." Added a 24.1 reference quoting "polysaccharides like starch and glycogen, or simple sugars (monosaccharides) like glucose and fructose".
Verify: closed


**C36-N1** · NEW · CONFIRMED-ERROR (unsourced claim about food)
- **Field:** `illustration.body`
- **Sentence:** "Now the dal. Dal is largely protein, and protein is a chain too, made of amino acids."
- **What is wrong:** there is no source for it, and it is false as generally stated. Pulses carry more carbohydrate than protein by weight. This is domain knowledge, not checked against a held source, because no food-composition source is held.
- **Fix:** "Now the dal. Dal carries a good deal of protein as well as starch; follow the protein. Protein is a chain too, made of amino acids."
- **Support:** needs a food-composition source if any quantity is kept. The fix makes no quantitative claim.
Fix: now reads "Now the dal, and follow the protein in it." I left out the suggested "a good deal of protein as well as starch" because no food-composition source is held, so the sentence makes no claim about how much.
Verify: closed


**C36-N2** · NEW · CONFIRMED-ERROR (contradicts a held source and E2)
- **Field:** `illustration.body`, `must_know[0]`, `exercises[1]` answer
- **Sentences:** "A lot of a raw onion is fibre." / "But it never became part of you, and it handed you no energy." / "Add it in, and you have counted energy that never crossed."
- **What is wrong:** (a) raw onion is mostly water, and "a lot … is fibre" is unsourced and overstated (domain knowledge, not held). (b) "handed you no energy" contradicts the held FAO text: "fermentation of unabsorbed carbohydrate in the colon … Short-chain (volatile) fatty acids are also formed in the process, some of which are absorbed and available as energy." It also sits badly with the Indian fibre factor that C32 cites (fssai "(H)Dietary fibre 2kcal/g"). (c) A food table's onion figure is not mainly fibre energy.
- **Fix:** "Raw onion carries some fibre. Your body makes no enzyme that can break most plant fibre down, so it is not absorbed as it stands. Bacteria in the large intestine ferment part of it, and a little of what they make is absorbed. So fibre hands you far less than a food table's carbohydrate line might suggest, and the rest leaves." Drop "Add it in, and you have counted energy that never crossed." and keep "Your total is a number about the plate."
- **Support:** held. FAO §3.3 paragraph 1 (quoted above); A&P 23.7 "Your bodies do not produce enzymes that can break down most fibrous polysaccharides".
Fix: the onion paragraph now reads "Now the onion, and follow the fibre in it. Your body makes no enzyme … so it is not absorbed as it stands. It travels on down the gut … helps move everything else along. Whether any energy reaches you from it further down, this section does not say." I dropped "handed you no energy" and "Add it in, and you have counted energy that never crossed", and "The table gives a figure for each of the four, onion included." I did not assert fermentation or absorbed fatty acids, because FAO is not cited by this record (A&P 23.7 does not say it). must_know[0] was not changed: it is still true of the fibre itself.
Verify: closed (note: the Fix line says "The table gives a figure for each of the four, onion included" was dropped; it is still in illustration.body, and is harmless)


**C36-N3** · NEW · CONFIRMED-ERROR (contradicts E2)
- **Field:** `exercises[1]` answer (critique)
- **Sentence:** "A food table gives the energy in the food. It does not give the energy that crossed anybody's gut wall."
- **What is wrong:** E2 teaches that table and label figures computed with Atwater factors "already have the losses taken out of them … an estimate of metabolizable energy for an average". The table figure is an average estimate of what crosses, not gross energy in the food. This is the same slip as C33-N1.
- **Fix:** "A food table gives an average estimate: its factors already take off average losses. It does not give what crossed these women's gut walls, and nothing in the note measured that."
- **Support:** C32 simplified_explanation; FAO §3.5.1 (held).
Fix: the critique now reads "A food table gives an average estimate for a food. It does not give what crossed these women's gut walls, and nothing in the note measured that." The later line now reads "It is a table estimate for the food recorded, not a measure of energy absorbed". I left out "its factors already take off average losses" because FAO §3.5.1 and C32 are not cited or in concept_deps here.
Verify: closed


**C36-H1** · NEEDS-HARSH
- **Field:** `simplified_explanation`, `analogy_breaks_when` (and C38 "It is also the near store")
- **Sentence:** "Near store and far store describe the size of the two and nothing else."
- **Issue:** "near" and "far" suggest place or order of use, but the text says they mean size, and no rule settles it. Options: (a) rename to "small store" and "large store" everywhere (E6, E8); (b) keep the names and add "The names are only labels. The section gives no rule about which is drawn on first." Either is sourced as it stands. It is an editorial choice.
Not applied: NEEDS-HARSH (store names), awaiting his decision.


## Round 2 (23 Sep 2026)

- **C36-R2a** · HARSH DECISION on C36-H1 (23 Sep): rename 'near store' → 'small store' and 'far store' → 'large store' everywhere in this record (prose, exercises, answers, practice, retrieval, notes). Keep capitalisation and grammar right. Remove any sentence whose only job was to say the names mean size only, if it now says nothing.
Fix: renamed everywhere it appeared (definition plain terms, illustration, analogy_breaks_when, exercise answer): 'near store' → 'small store', 'far store' → 'large store', 'the far one' → 'the large one'. Dropped "One is near and small. One is far and large." and "Near store and far store describe the size of the two and nothing else.", which now said nothing; kept "This section gives no rule about which store is drawn on first, or how fast either fills or empties." Grep finds no 'near store' or 'far store' left.
Verify: closed
