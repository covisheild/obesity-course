# B0-R0-C27 (D4) — compression-pass holes, audit triage

1. **C27-K1** — CONFIRMED-ERROR — `illustration.body`
   - Quoted: "Two students landing in different bands is a real difference between people."
   - Wrong: this contradicts the section's own third source of difference, and it contradicts the next sentence ("It cannot tell you which of the three you would be looking at"). Two students either side of 25.0 can land in different bands through measurement alone. It also misleads P4(a) and P7.
   - Fix: "Two students landing in different bands need not be a real difference between people. Two students either side of 25.0 can be separated by the measurement alone."
   - Support: the record's own definition ("a difference between repeated measurements of the same person ... at the same moment").
   - Fix: replaced the sentence with the proposed two sentences ("need not be a real difference ... by the measurement alone").
   - Verify: closed

2. **C27-K2** — CONFIRMED-GAP (terminology) — `simplified_explanation`
   - Quoted: "A set that is perfectly symmetric can be made to look like it has a heavy tail just by moving the bands."
   - Gap: only "long tail" is defined. The text uses two words for one thing (SELFCHECK item 7).
   - Fix: "heavy tail" → "long tail".
   - Support: none needed.
   - Fix: changed "heavy tail" to "long tail" in simplified_explanation.
   - Verify: closed

3. **C27-K3** — CONFIRMED-GAP — `illustration.body`; P10
   - Quoted: "These four bands are the ones the World Health Organization drew, for its own reasons. They are not centred on where these 282 students' body-mass index actually sits."
   - Gap: this is the WHO's first appearance in A–D, with no introduction. The reader cannot check "not centred" from anything given.
   - Fix: "These four bands are the World Health Organization's (WHO), which the paper adopted. They were not drawn around these students, and they are not equally wide: 18.5 to 24.9 spans about 6.5 units, 25 to 29.9 about 5, and the two outer bands have no outer edge."
   - Support: kiran_2022_muac_nc: "Overweight was defined using the WHO cut-offs (BMI ≥25 kg/m2)"; band edges from Table 2. The widths are arithmetic.
   - Fix: replaced the two sentences with the proposed text (WHO introduced, bands adopted by the paper, unequal widths, open outer bands). Supported by the WHO cut-offs quote already in illustration.numbers and Table 2's heading "BMI (WHO criteria)" in the held source; no new number entry needed (widths are arithmetic).
   - Verify: closed

4. **C27-K4** — CONFIRMED-GAP (minor) — `practice[6]` (P7)
   - Quoted: "single observer measurements with minimum inter-observer variation"
   - Gap: "inter-observer" is never glossed, and the section's three sources never name observers.
   - Fix (prompt): add "Inter-observer means between different people taking the measurement."
   - Support: none needed. The quote is verified in the source.
   - Fix: added "Inter-observer means between different people taking the measurement." to the P7 prompt after the quote.
   - Verify: closed

5. **C27-K5** — CONFIRMED-GAP (minor) — `practice[10]` (P11)
   - Quoted: "ranges from underweight to 30 or more"
   - Gap: "underweight" is never defined. The illustration's table says only "under 18.5".
   - Fix: label the table row "under 18.5 (the paper's 'underweight')", or gloss it in the P11 prompt.
   - Support: kiran_2022_muac_nc Table 2: "Underweight (<18.5 kg/m2)". (The hole's second part, "average" in Exercise 1, is NOT-A-DEFECT: "average" is used in A1, A3, A5 and C4–C8.)
   - Fix: glossed in the P11 prompt ("Underweight is the paper's name for its band under 18.5."); table left unchanged to keep its columns aligned.
   - Verify: closed

6. **C27-K6** — NEW (pointer) — `illustration.body`
   - Quoted: "This is not two counts disagreeing with each other, the way the abdominal-obesity figures did."
   - Wrong: this points to D3's P9, a practice problem in a section that is not in concept_deps (C03, C05, C18). SELFCHECK item 8.
   - Fix: delete the clause ("This is not two counts disagreeing with each other. It is a label attached to the wrong slice of its own table."). Or add B0-R0-C26 to concept_deps and name the section.
   - Support: none needed.
   - Fix: deleted the clause ", the way the abdominal-obesity figures did"; concept_deps unchanged.
   - Verify: closed
