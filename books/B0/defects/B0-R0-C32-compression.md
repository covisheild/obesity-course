# Compression-pass holes, triaged · B0-R0-C32 (E2)

Auditor: Task 3, fresh context. Full per-hole verdicts: `books/B0/compress/TRIAGE-part-E.md`.

---

**C32-K1** · CONFIRMED-ERROR
- **Field:** `illustration.body`, `must_know[1]`, `retrieval_items[2]`, `simplified_explanation`
- **Sentences:** "The digestible-energy step is nowhere in the report at all." / "Object to the word digestible, which is not in it anywhere." / "the phrase does not occur in the report" / "What the report has no step for anywhere is digestible energy."
- **What is wrong:** the claims are made about the whole report, but the held evidence covers two chapters only. The held file says: "Checked https://www.fao.org/4/y5022e/y5022e04.htm (Chapter 3 …) and …y5022e05.htm (Chapter 4)." Its "does not occur in this report" is a [NOTE] line, not source text. Nothing held shows the phrase is absent from chapters 1, 2 or the annexes.
- **Fix:** narrow every instance to what was checked: "is not in chapter 3, where the report sets out its energy cascade, or in chapter 4." must_know[1] becomes: "The report's cascade has no digestible-energy step … Object to the word digestible when it is credited to this cascade." The cascade claim is fully supported and is what the lesson needs.
- **Support:** `sources/fao_food_energy.txt`, the NOT OBTAINED VERBATIM record under §2. Alternatively, check the full report and keep the wider claim, but that needs a fetch, which was out of scope here.

Fix: narrowed every whole-report claim to chapters 3 and 4 (definition.text, simplified_explanation, illustration.body, must_know[1] per the suggested wording, retrieval_items[2]); also exercise 1 answer now says "not in the report's cascade".

**C32-K2** · CONFIRMED-ERROR
- **Field:** `illustration.body`. The same pattern is in `practice` L5, L8 and L10.
- **Sentences:** "Round it to three figures and you have 0.114. Multiply by a hundred…" and "340 divided by 2,928.8 = 0.116" (the rounded value is written as an equality). The same happens in L5 ("0.107"), L8 ("0.254") and L10 ("0.114").
- **What is wrong:** every one rounds in the middle of the working, which contradicts A3's rule: "Keep full precision while you work and round once, at the end, to what your weakest input earned." The final figures do not change.
- **Fix:** carry full precision and round once. For example: `80 divided by 700 = 0.1142857143`, then `0.1142857143 times 100 = 11.42857143`, then "Round once, at the end: 11.4." For kJ: `340 divided by 2,928.8 = 0.1160885…`, then `times 100 = 11.60885…`, then 11.6. Checked: 11.43, 11.61, 10.67, 25.40 and 11.43 all round to the printed figures.
- **Support:** A3-released.md, must-know points.

Fix: illustration (kcal and kJ sums), L5, L8 and L10 now carry full precision (0.1142857143, 0.1160885004, 0.1066666667, 0.253968254) through the ×100 line and round once at the end; recomputed in Python, printed figures 11.4, 11.6, 10.7, 25.4 unchanged.

**C32-K3** · CONFIRMED-GAP
- **Field:** `definition.text`
- **Sentence:** "Atwater's carbohydrate is determined by difference, and thus includes fibre."
- **What is wrong:** "by difference" is never explained, so the "thus" cannot be followed.
- **Fix:** add "that is, not measured directly but taken as whatever is left of the food's weight once the other measured parts are subtracted". This needs a source: the held FAO excerpt uses the phrase without defining it. If no source is added, cut the sentence and keep "One thing the general system does not do is take fibre out", which the held FAO sentence ("…and thus includes fibre") carries.
- **Support:** needs a source that is not held.

Fix: no source defining "by difference" is held, so cut the sentence; kept "does not take fibre out" and added a definition reference to FAO s.3.5.1 quoting "carbohydrate is determined by difference, and thus includes fibre" to carry it.

**C32-K4** · CONFIRMED-GAP (support)
- **Field:** `illustration.analogy_breaks_when`
- **Sentence:** "Fat's precise value is 37.4 kilojoules a gram"
- **What is wrong:** the reader is given no source for 37.4, and it has no `illustration.numbers` entry (SELFCHECK 3).
- **Fix:** "The same footnote gives fat's precise value as 37.4 kilojoules a gram". Add a numbers entry: value 37.4, citekey fao_food_energy_2003.
- **Support:** held. FAO footnote 9: "The precise values for protein, fat, total carbohydrate and alcohol are, respectively, 16.7, 37.4, 16.7 and 28.9 kJ/g."

Fix: analogy_breaks_when now reads "The footnote that gave protein's 16.7 gives fat's precise value as 37.4 kilojoules a gram"; added illustration.numbers entry 37.4, fao_food_energy_2003, footnote 9 quote.

**C32-N1** · NEW · CONFIRMED-ERROR
- **Field:** `practice` L5 answer
- **Sentence:** "Taken as plain calories it would be a meal of 450 calories, which is under half a kilojoule, and no meal is that."
- **What is wrong:** 450 × 4.184 J = 1,882.8 J = 1.88 kJ. That is almost four times half a kilojoule.
- **Fix:** "…a meal of 450 calories, which is under two kilojoules (450 times 4.184 = 1,882.8 joules), and no meal is that."
- **Support:** arithmetic, using nist_sp811's 4.184.

Fix: L5 now gives a working line 450 times 4.184 = 1,882.8 (joules) and says "under two kilojoules".

**C32-N2** · NEW · CONFIRMED-ERROR (minor, support)
- **Field:** `definition.references`
- **What is wrong:** two references now stand behind nothing in the text. The fssai_labelling_2020 entry says it carries "The definition's fibre factor of 2 kilocalories a gram", and the definition no longer says it. The OpenStax 5.2 fibre-discount quote ("The carbohydrate amount is discounted a certain amount for the fiber content") reads against the definition's "One thing the general system does not do is take fibre out". A reader who opens 5.2 finds the opposite, with no explanation that the two describe different systems.
- **Fix:** either restore one sentence ("An Indian label counts dietary fibre separately, at 2 kilocalories a gram.") or drop the fssai reference and its note. Then either drop the OpenStax fibre quote or add: "Some labelling systems do discount fibre, as OpenStax describes; Atwater's general system does not."
- **Support:** held. fssai_labelling_2020 "(H)Dietary fibre 2kcal/g"; FAO §3.5.1.

Fix: restored "The Indian labelling regulations give dietary fibre its own factor, 2 kilocalories a gram" (fssai ref now backed) and added "Some labelling systems do discount fibre, as OpenStax Chemistry describes. Atwater's general system does not."; note added to the OpenStax fibre reference.
