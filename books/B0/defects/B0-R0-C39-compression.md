# B0-R0-C39 (F1, Reading a table): compression-pass holes, audit triage

Auditor: Opus, Task 3. Checked against the current record (compressed text) and the released text of earlier Parts.
"Recurring" means the kind is on check/SELFCHECK.md, which lists only kinds found more than once in earlier audits.

1. **C39-K1**. Class: CONFIRMED-ERROR. Field: illustration.body.
   Sentence: "Run your finger along the top row. It is one state, not one woman."
   What is wrong: the top row of the table is the heading row (State | Women surveyed | Overweight or obese (%) | Year). It is not a state.
   Fix: "Run your finger along the first row under the headings. It is one state, not one woman."
   Support: the table as printed in the same field.
   Fix: illustration.body now reads "Run your finger along the first row under the headings. It is one state, not one woman."

2. **C39-K2**. Class: CONFIRMED-ERROR, **recurring** (SELFCHECK 3). Field: illustration.body (the table), and illustration.numbers.
   Sentence: the table rows "| A | 42,100 | 24.1 | 2019-21 |" and "| B | 18,750 | 39.6 | 2019-21 |".
   What is wrong: four figures about the world (42,100, 18,750, 24.1 and 39.6) are not said to be made up, and they carry no citekey. `numbers: []`. Every earlier Part, and F2, says when figures are made up.
   Fix: add straight after the table: "States A and B and all four figures in this table are made up for this section." If Harsh wants real survey figures instead, that needs a source. None is held: there is no NFHS file in sources/INDEX.yml.
   Support: SELFCHECK 3.
   Fix: added "States A and B and all four figures in this table are made up for this section." straight after the table; numbers left [] as no figure is a real-world illustration number.

3. **C39-K3**. Class: CONFIRMED-GAP. Field: illustration.body, which Ex 1 and Ex 2 depend on.
   Sentence: "Overweight or obese (%)". Ex 2 answer: "'obesity' and 'overweight or obese' are different categories".
   What is wrong: neither term is defined in F1 or in A to E. Ex 2's third point needs the reader to know that the heading's category is the wider one. The section on BMI (B6) said to quote a cut-off only with whose it is, and the table gives no cut-off.
   Fix: in the paragraph on columns, add: "'Overweight or obese' is one category, made by cutting a measurement at chosen values. It counts the overweight and the obese together, so it is larger than 'obese' alone. The heading does not say whose cut-offs were used, and that is a question to ask." Add B0-R0-C14 to concept_deps.
   Source: none needed. B6-released: "Quote a cut-off only with whose it is and when it was set."
   Fix: added the three suggested sentences on 'Overweight or obese' after the columns paragraph; added B0-R0-C14 to concept_deps.

4. **C39-K4**. Class: CONFIRMED-GAP. Field: must_know[0].
   Sentence: "Twenty-four per cent of 42,100 women and twenty-four per cent of two hundred women are not the same evidence."
   What is wrong: this is asserted with no link to the section that explains it (D6, the square-root law). It is also silent on D6's own limit. must_know[5] then puts precision out of scope, so the reader cannot tell where the reason lives.
   Fix: add: "The section on sampling says why: for a random sample, the typical error shrinks with the square root of the count. For a sample that was not random, no count rescues it." Add B0-R0-C29 to concept_deps.
   Source: none needed. D6-released, line 17 (the square-root law) and line 47: "It buys you nothing against a sample that was never random to begin".
   Fix: appended the two suggested sentences (square-root law, non-random sample) to must_know[0]; added B0-R0-C29 to concept_deps.

5. **C39-K5**. Class: CONFIRMED-GAP, unsupported claim, **recurring** (SELFCHECK 3). Field: must_know[2] (india_deviation).
   Sentence: "Expect an Indian survey table to report a fieldwork span rather than one year. Expect state sample sizes to differ several-fold within the same table."
   What is wrong: these are two claims about Indian surveys with no citekey, and no source is held for either. "Several-fold" is a quantitative claim.
   Fix: either cite a national survey report that shows state sample sizes and the fieldwork span (not held; would need fetching), or reword so it asks for a check rather than stating a fact: "In a national survey table, check the count in every row: states need not have been sampled equally."
   Source: none held.
   Fix: took the reword route (no source held, none fetched). must_know[2] now reads "In an Indian national survey table, check the count in every row: states need not have been sampled equally." It asserts no fact about Indian surveys; the fieldwork-span and several-fold claims are removed.
