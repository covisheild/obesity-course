# B0-R0-C30 (D7) — compression-pass holes, audit triage

1. **C30-K1** — NEW (support) — `definition.references`
   - Quoted: "a measurement error is "measured quantity value minus a reference quantity value"" (and the quoted VIM 2.17, 2.18, 2.19 and 4.14 entries)
   - Wrong: the definition quotes five VIM entries, but its references list only two openstax quotes about sampling and nonsampling errors, which carry none of these claims (SELFCHECK items 1 and 3). jcgm_vim3 appears only in practice refs.
   - Fix: add jcgm_vim3 references with these quotes: 2.16 "measured quantity value minus a reference quantity value"; 2.17 "remains constant or varies in a predictable manner"; 2.18 "estimate of a systematic measurement error"; 2.19 "varies in an unpredictable manner"; 4.14 "smallest change in a quantity being measured that causes a perceptible change in the corresponding". For trueness and precision, add 2.14 and 2.15 as well.
   - Support: all five strings were found in sources/jcgm_vim3.txt (entries 2.16–2.19 and 4.14).
   - Fix: added eight jcgm_vim3 definition references (kind instrument, held source, quotes confirmed in sources/jcgm_vim3.txt): 2.13, 2.14, 2.15, 2.16, 2.17, 2.18, 2.19, 4.14; updated the openstax note that said the VIM could not sit there.

2. **C30-K2** — CONFIRMED-ERROR (overstatement) — `must_know[4]`; P12
   - Quoted: "Differences between observers are each observer's own systematic habit."
   - Wrong: the differences between two observers include a random part as well as each observer's habit. The section's own P12 shows a consistent offset (all five differences positive) plus a spread (0.3 to 0.5). The sentence says all of the difference is habit.
   - Fix: "Part of the difference between observers is each observer's own systematic habit."
   - Support: arithmetic on P12's own table (differences 0.4, 0.4, 0.5, 0.3, 0.3: all positive, but not constant).
   - Fix: must_know[4] now opens "Part of the difference between observers is each observer's own systematic habit."

3. **C30-K3** — CONFIRMED-ERROR (wording, minor) — `illustration.body`
   - Quoted: "Two stated scales are each weighed against it twenty times."
   - Wrong: this is backwards. The scales weigh the calibration weight, not the other way round.
   - Fix: "Each of two stated scales weighs it twenty times."
   - Support: none needed.
   - Fix: sentence now reads "Each of two stated scales weighs it twenty times."

4. **C30-K4** — CONFIRMED-GAP (minor) — `illustration.body`
   - Quoted: "half a kilogram out against seven and a half hundredths."
   - Gap: 60.0 − 59.925 = 0.075 is never shown (SELFCHECK item 9).
   - Fix: add working "60.0 minus 59.925 = 0.075" after scale B's average.
   - Support: arithmetic, recomputed: scale B's rows sum to 598.5 and 600.0, and the mean is 59.925. The min 58.7, the max 60.7 and the two readings of 60.0 all check.
   - Fix: added "60.0 minus 59.925 = 0.075" to scale B's working block and the sentence "Its average sits 0.075 kilograms below the truth." (recomputed in Python).
