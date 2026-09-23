# B0-R0-C26 (D3) — compression-pass holes, audit triage

1. **C26-K1** — CONFIRMED-GAP — `illustration.body`
   - Quoted: "The study's Table 3 reports a 31.3 centimetre arm cut-off for men, labelled "overweight, body-mass index 25 or more"."
   - Gap: "the tape" is used ("caught by the tape", "the men the tape flags") and never introduced. "Cut-off" is used without saying which side counts as a positive. B6 uses the word but never says which side.
   - Fix (after the quoted sentence): "The arm is measured with a tape, and a man whose arm measures 31.3 centimetres or more counts as a positive result."
   - Support: kiran_2022_muac_nc, methods: "Mid-upper arm circumference was measured with the calibrated plastic tape". The "or more" direction is the one the record's own table already uses.
   - Fix: added after the Table 3 sentence: "The arm is measured with a tape, and a man whose arm measures 31.3 centimetres or more counts as a positive result." (tape quote confirmed in the held source).

2. **C26-K2** — CONFIRMED-GAP — `illustration.body`; affects P6, P11
   - Quoted: "Sensitivity of 86 per cent should mean some whole number of the 52 caught by the tape. Try the nearest candidates."
   - Gap: the step that picks 44 and 45 (and 58 and 59) is not shown. It first appears later, for the 42 ("0.86 times 42 = 36.12"). P11's trap is exactly the choice of candidate.
   - Fix: add working before each pair: "0.86 times 52 = 44.72, so try 44 and 45" and "0.74 times 79 = 58.46, so try 58 and 59".
   - Support: arithmetic (0.86 × 52 = 44.72; 0.74 × 79 = 58.46).
   - Fix: added "0.86 times 52 = 44.72" and "0.74 times 79 = 58.46" as first lines of the two candidate working blocks; prose now says to work out 0.86 times 52 and try the whole numbers either side.

3. **C26-K3** — CONFIRMED-GAP (changes the meaning of the headline figure) — `illustration.body`; affects P7, P8, P12, P13, Exercise 1
   - Quoted: "Try the 42 men in the 25-to-29.9 band on their own, against the other 89 men in the study."
   - Gap: the 89 include the 10 men at 30 or more. On this reading, an obese man the tape flags counts as a wrong result. The 23 "false positives" probably include most of those 10 men, whose arms are the largest. The text never says so. A reader will take 61 per cent as the chance that a flag means an index of 25 or more. For that question, 61 per cent is only a floor.
   - Fix (after the rebuilt table): "The 89 include the 10 men at 30 or more, so a flagged man at 30 or more counts here as a wrong result. For the question 'is his index 25 or more?', 61 per cent is the least the share could be."
   - Support: logic. If k of the 10 are among the 59 flagged, then PPV for "25 or more" = (36 + k)/59 ≥ 36/59. Table 2: "Obese (≥30 kg/m2) 15 (5.3) 10 (7.6)".
   - Fix: added the suggested two sentences, placed after the 61 per cent paragraph (not straight after the table) so the 61 is already on the page when it is qualified.

4. **C26-K4** — CONFIRMED-GAP — `practice[9]` (P10) prompt; `must_know[6]`
   - Quoted (answer): "Table 2 gives 71 men and 114 women with high PBF, and they add to 185, not 186." / "The normal-range row, 97, plus the high row, 185..."
   - Gap: the answer uses 71, 114 and 97, and none of them is in the prompt or anywhere earlier in the text. The reader cannot do the check that must_know[6] asks for. (P10 is the section's only demonstration of must_know[6]. That is enough once the numbers are given.)
   - Fix (prompt): add "Table 2 also gives 71 men and 114 women in the high row, and 97 students in the normal-range row."
   - Support: kiran_2022_muac_nc Table 2: "Normal 97 (34.4) ... Overweight (≥20% in men; ≥ 28% in women) 185 (65.6) 71 (54.2) 114 (75.5)".
   - Fix: P10 prompt now adds "Table 2 also gives 71 men and 114 women in the high row, and 97 students in the normal-range row." (confirmed in Table 2).

5. **C26-K5** — CONFIRMED-GAP + NEW error — `exercises[1]` (Exercise 2)
   - Quoted (answer): "There is no arithmetic check here of the kind that settles a count against a percentage." and "The methods section, Table 2 and Table 3 all give the women's cut-off as 28 per cent."
   - Gap: the prompt gives only two places for 28 (methods, Table 2). The answer counts three, and Table 3 is never given to the reader.
   - Error: an arithmetic check does exist in the paper. Table 1 gives women's body fat a first quartile of 28.1. At least a quarter of 151 women, so at least 38, sit at or below 28.1, which leaves at most 113 above it. Table 2 puts 114 women in the high row. A 30 per cent cut-off cannot produce 114, and a 28 per cent cut-off can. This needs D5's quartiles, which D3's reader does not yet have.
   - Fix: prompt: "Its methods section, Table 2 and Table 3 all use '≥28' per cent for women instead." Answer, first sentence: "Nothing taught so far settles it by arithmetic, though the section on average and spread will give a way." (Or drop the claim.)
   - Support: kiran_2022_muac_nc Table 3 "High percent Body fat Women (≥28%)"; Table 1 women's body fat "34.0 (28.1, 39.2)"; Table 2 "114 (75.5)". Arithmetic: 0.25 × 151 = 37.75 → at least 38 at or below Q1, so at most 113 above it. Caveat: quartile conventions vary, so the check is strong but not airtight at a margin of one woman.
   - Fix: prompt now names methods, Table 2 and Table 3; answer's opening replaced with "Nothing taught so far settles it by arithmetic. A later section will give a way." (dropped the "definition, not a total" sentence; later section left unnamed).

6. **C26-K6** — NEW (gap) — `practice[8]` (P9)
   - Quoted (answer): "Try the paper's other count for the same measurement, 109, from its own results text and Table 2."
   - Wrong: 109 appears nowhere in the prompt or in the text before it, so the reader cannot reach the correction.
   - Fix (prompt): add "The results text and Table 2 give the same group as 109."
   - Support: kiran_2022_muac_nc: "109 participants (38.7%) with abdominal obesity".
   - Fix: P9 prompt adds "The results text and Table 2 give the same group as 109." (confirmed in results text).

7. **C26-K7** — NEW (consistency, minor) — `practice[1]` (P2 answer)
   - Quoted: "check whether the test and the condition are independent, using last section's test. Does P(test positive) equal P(test positive given condition present)?"
   - Wrong: the last section's test is "P(A and B) equals P(A) times P(B)". The conditional form is never stated there (SELFCHECK items 5 and 8).
   - Fix: use D2's form: "P(test positive and condition present) is 15/100 = 0.15. P(test positive) times P(condition present) is 0.25 × 0.2 = 0.05. They do not match."
   - Support: arithmetic.
   - Fix: P2 answer now uses the product form: working 15/100 = 0.15, 25/100 = 0.25, 20/100 = 0.2, 0.25 × 0.2 = 0.05; prose compares 0.15 with 0.05.
