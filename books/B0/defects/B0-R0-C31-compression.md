# Compression-pass holes, triaged · B0-R0-C31 (E1)

Auditor: Task 3, fresh context. Source: `books/B0/compress/HOLES-part-E.md`, checked against the current record.
Only CONFIRMED and NEW items are listed; the full per-hole verdicts are in `books/B0/compress/TRIAGE-part-E.md`.

---

**C31-K1** · CONFIRMED-GAP
- **Field:** `definition.text`, `simplified_explanation`
- **Sentence:** "A chemical bond is an attraction between atoms or ions …" / "In an ionic bond, one atom hands an electron over to the other. One is left positive, the other negative, and opposite charges pull."
- **What is wrong:** the word "ion" is used (here, and as known in E5 and E8) and never defined in A1–E8.
- **Fix:** after "…opposite charges pull." add: "An atom left carrying a charge this way is called an ion."
- **Support:** held. OpenStax Chemistry 2e §7.2, already quoted in the record: "Ionic bonding results from the electrostatic attraction of oppositely charged ions that are typically produced by the transfer of electrons between metallic and nonmetallic atoms."
Fix: added "An atom left carrying a charge this way is called an ion." after "…opposite charges pull." in `simplified_explanation`; supported by the §7.2 quote already held.

**C31-K2** · CONFIRMED-GAP
- **Field:** `definition.text`
- **Sentence:** "Energy is the capacity to supply heat or do work."
- **What is wrong:** "work" in the physics sense is never defined, and E3 must_know[5] and E3 practice L9 ("heat and work") depend on it.
- **Fix:** add after the sentence: "Work, in this sense, is energy transferred by a force moving something through a distance; lifting a weight is work."
- **Support:** held. OpenStax College Physics 2e §7.1 (in `openstax_college_physics_2e`): "The work done on a system by a constant force is the product of the component of the force in the direction of motion times the distance through which the force acts." Add as a reference.
Fix: added to `definition.text` "Work, in this sense, is a force moving something through a distance; lifting a weight is work." (worded without "energy transferred", which the held quote does not say), and added the College Physics 2e §7.1 definition as a reference with its quote.

**C31-K3** · CONFIRMED-GAP
- **Field:** `illustration.body`
- **Sentence:** "The page gives you all three numbers, in kilojoules for a fixed standard amount of each."
- **What is wrong:** the amount is never named, so the reader cannot say what 185 kJ is per. The record's own `illustration.numbers` units say "per mole", and B5 has taught the mole.
- **Fix:** "…in kilojoules per mole of bonds: the fixed count of the section on concentration units (B5)." Also in `analogy_breaks_when` "a fixed counted amount of each substance" → "a mole of each". Add B0-R0-C13 (B5) to `concept_deps` (SELFCHECK 8).
- **Support:** held. Chemistry 2e §7.5: "436 kJ per mole of H–H bonds broken".
Fix: body now says "in kilojoules per mole of bonds. A mole is the fixed count of things from the section on concentration units (B5)." (B5's own wording); table header "per mole of bonds"; `analogy_breaks_when` "quoted for a mole of each"; B0-R0-C13 added to `concept_deps`.

**C31-K4** · CONFIRMED-GAP
- **Field:** `illustration.analogy_breaks_when`
- **Sentence:** "A mixture can sit on a shelf for years, unchanged, with a large release waiting inside it. Something has to start it."
- **What is wrong:** it never says what the mixture is. Straight after the hydrogen-and-chlorine example it reads as a claim about that mixture, and no source is held for it. What starts the reaction is never named either.
- **Fix:** "Sugar can sit in a jar, in air, for years, unchanged, though burning it releases a great deal. Something, such as a flame, has to start it." This is an everyday observation and needs no source.
- **Support:** logic. The point is that the size of a bond sum says nothing about whether a reaction starts, and must_know[3] already says so.
Fix: replaced with "Sugar can sit in a jar, in air, for years, unchanged, though burning it releases a great deal. Something, such as a flame, has to start it." No source asserted (everyday observation).
