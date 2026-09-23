# Compression-pass holes, triaged · B0-R0-C35 (E5)

Auditor: Task 3, fresh context. Full per-hole verdicts: `books/B0/compress/TRIAGE-part-E.md`.

---

**C35-K1** · CONFIRMED-GAP
- **Field:** `definition.text`, `simplified_explanation`
- **Sentences:** "The plasma membrane controls the passage of organic molecules, ions, water and oxygen…" / "Internal receptors sit in the cytoplasm…" / "A cell is a bag of watery jelly with a skin round it."
- **What is wrong:** "cytoplasm" is never tied to the "watery jelly" the reader is given. Exercise 1's answer says "waiting in the jelly", so a reader cannot connect the definition's "cytoplasm" to it. "Organic molecules" is never glossed. "Ions" is covered by C31-K1.
- **Fix:** "A cell is a bag of watery jelly, called the cytoplasm, with a skin round it." Add after the membrane sentence in plain terms: "Organic molecules are the carbon-based molecules living things are built from and run on: sugars, amino acids, fats and proteins among them."
- **Support:** held. Biology 2e §4.3: "The cytoplasm is the cell's entire region between the plasma membrane and the nuclear envelope … Even though the cytoplasm consists of 70 to 80 percent water, it has a semi-solid consistency". The same paragraph says "proteins are not the only organic molecules in the cytoplasm. Glucose and other simple sugars, polysaccharides, amino acids, nucleic acids, fatty acids…" That gives examples, not a definition, so "carbon-based" needs a source or should be dropped. Glossing by example alone is supported.
- Fix: simplified explanation now reads "A cell is a bag of watery jelly, called the cytoplasm, with a skin round it." Definition adds "Sugars, amino acids, fatty acids and proteins are among those organic molecules." (by example only; "carbon-based" dropped, no held source) and "The cytoplasm is the cell's whole region between the plasma membrane and the nucleus. It is mostly water but semi-solid." Three Biology 2e §4.3 references added with quotes.
Verify: closed

**C35-K2** · CONFIRMED-GAP
- **Field:** `exercises[2]` (teaching)
- **Sentence:** prompt: "They can recite that insulin acts on cells … so that they leave able to place a drug they have never met." The answer never places insulin.
- **What is wrong:** the prompt names insulin, and nothing in E5 says where insulin's receptor sits. A reader following the answer's own "place it" move stops at insulin.
- **Fix:** add one line to the answer, before the close: "Place the one they came in with. Insulin's receptors sit on the cell membrane, so insulin is a signal of the second kind: it lands outside and never needs to enter." Add a reference.
- **Support:** held. OpenStax A&P 2e §17.9 speaks of "insulin receptors on their cell membranes" (the sentence quoted in C38).
- Fix: added to exercise 3 answer before the close: "Place the one they came in with. Insulin's receptors sit on the cell membrane, so insulin is a signal of the second kind: it lands outside and never needs to enter." Added definition reference openstax_anatphys_2e §17.9 quoting "do not have insulin receptors on their cell membranes and do not require insulin for glucose uptake" (held source, already in the library, but new to this record).
Verify: closed
