# B0-R0-C28 (D5) — compression-pass holes, audit triage

1. **C28-K1** — CONFIRMED-ERROR — `practice[14]` (P15 answer)
   - Quoted: "About a quarter of the women sit at or above the third quartile. So about a quarter or more of the 151 women are at 25.6 or above, even though the mean is 23.0."
   - Wrong: about a quarter are at or above 25.6. "Or more" applies to the share at **25** or above, because 25 < 25.6. As written, the sentence draws a stronger claim than the quartile allows and misses the point about the cut-off.
   - Fix: "About a quarter of the women sit at or above 25.6. Since 25.6 is above 25, at least about a quarter of the 151 women are at 25 or above, even though the mean is 23.0."
   - Support: Table 1 women's BMI "22.7 (20.5, 25.6)". Consistent with Table 2: 41 + 5 = 46 of 151 = 30.5 per cent at 25 or more.
   - Fix: P15 answer now reads "About a quarter of the women sit at or above 25.6. Since 25.6 is above 25, at least about a quarter of the 151 women are at 25 or above", as proposed.
   - Verify: closed

2. **C28-K2** — CONFIRMED-ERROR — `illustration.body`; P13
   - Quoted: "Both rows fail the same way, and each one passes against the other row's numbers."
   - Wrong: they fail in opposite directions. The weight median (70.9) sits below both of its printed numbers (167.7, 177.8). The height median (173) sits above both of its (62.6, 80.9). The text itself says "below both" and then "above both".
   - Fix: "Both rows fail, in opposite directions, and each passes against the other row's numbers: 70.9 sits between 62.6 and 80.9, and 173 between 167.7 and 177.8."
   - Support: kiran_2022_muac_nc Table 1 (quoted in the record). Also the source header: "the interquartile ranges are exchanged between the two rows".
   - Fix: illustration sentence replaced with "Both rows fail, in opposite directions, and each passes against the other row's numbers: 70.9 sits between 62.6 and 80.9, and 173 between 167.7 and 177.8."
   - Verify: closed

3. **C28-K3** — CONFIRMED-ERROR (overstatement) — `illustration.body`, repeated in `practice[13]` (P14 answer); affects P7, P16
   - Quoted: "A smaller number of men, with a much higher body fat percentage, pull the mean up past them." (P14: "Most men sit near or below the median.")
   - Wrong: a mean above the median shows only that the values above the median reach further than those below it. It does not show that the men above are fewer, or that their values are "much higher". "Most men sit ... below the median" is false by definition: at most half do.
   - Fix (illustration, replacing the quoted sentence and the next one): "The men above the median must reach far enough up to pull the mean past it. The quartiles printed beside the median show it: 16.7 sits 3.6 below 20.3, and 28.8 sits 8.5 above it. The upper quarter stretches more than twice as far, which is a longer tail upward." P14: "Most men sit near or below the median" → "At least half sit at or below the median."
   - Support: Table 1 men's body fat "20.3 (16.7, 28.8)" (already quoted in the record's numbers). Arithmetic: 20.3 − 16.7 = 3.6; 28.8 − 20.3 = 8.5.
   - Fix: illustration now says the men above the median must reach far enough up to pull the mean past it, prints the quartiles 16.7 and 28.8 with a working block (20.3 minus 16.7 = 3.6; 28.8 minus 20.3 = 8.5, checked in Python), and says the quarter just above the median stretches more than twice as far as the quarter just below. P14: "At least half sit at or below the median"; "A few readings" -> "Some readings". Same overstatement also removed from P16 ("The men above it reach far enough up..."), P12 (mean below median now explained by the lower values reaching further down) and exercise 1 ("The patients above the median reach far enough up...").
   - Verify: closed

4. **C28-K4** — CONFIRMED-GAP — `must_know[6]`; P9
   - Quoted: "Where the mean and median disagree by much, look at the quartiles instead of trusting a single standard deviation to describe both sides."
   - Gap: the text never shows how to read the two quartile distances as a sign of a tail, and P9 asks exactly that.
   - Fix: the K3 fix closes this. It works the two distances on the body fat row.
   - Support: as K3.
   - Fix: closed by the K3 illustration fix, which works both quartile distances on the body fat row.
   - Verify: closed

5. **C28-K5** — CONFIRMED-GAP — `practice[15]` (P16)
   - Quoted (answer): "Men's body fat is printed as a median of 20.3 per cent, with quartiles of 16.7 and 28.8."
   - Gap: the quartiles 16.7 and 28.8 are not in the prompt or the prose (they appear only in `illustration.numbers`), so the reader cannot test "20 to 24".
   - Fix: the K3 fix puts them in the illustration. Alternatively, add them to the P16 prompt.
   - Support: as K3.
   - Fix: closed by the K3 fix; 16.7 and 28.8 now appear in the illustration prose before P16.
   - Verify: closed

6. **C28-K6** — CONFIRMED-GAP — `practice[5]` (P6)
   - Quoted: "Give the variance and the sample standard deviation of a set whose deviations from its own mean are the five values below."
   - Gap: the definition gives two variances (divide by 5 or by 4). The prompt does not say "sample" for the variance, or that the set is a sample. The answer divides by 4.
   - Fix: "Give the sample variance and the sample standard deviation of a sample whose deviations ..."
   - Support: none needed.
   - Fix: P6 prompt now reads "Give the sample variance and the sample standard deviation of a sample whose deviations ...".
   - Verify: closed

7. **C28-K7** — CONFIRMED-GAP — `practice[9]` (P10); definition
   - Quoted: "Work out how many standard deviations above the mean his reading would sit."
   - Gap: the operation (deviation divided by the SD) is used only in the answer.
   - Fix (definition, after the standard-deviation sentence): "To say how far one value sits from the mean in standard deviations, divide its deviation by the standard deviation."
   - Support: arithmetic (definition of a unit). No source needed.
   - Fix: definition now adds, after the standard-deviation sentence, "To say how far one value sits from the mean in standard deviations, divide its deviation by the standard deviation."
   - Verify: closed

8. **C28-K8** — NEW (minor) — `exercises[0]` answer
   - Quoted: "More than half of all patients walk at or below 4,100 steps"
   - Wrong: the median gives "at least half", not "more than half". The section's own wording elsewhere is "at least half".
   - Fix: "At least half of all patients walk at or below 4,100 steps".
   - Support: the definition of the median.
   - Fix: exercise 1 answer now says "At least half of all patients walk at or below 4,100 steps".
   - Verify: closed

9. **C28-K9** — NEW (minor) — `practice[15]` (P16 answer)
   - Quoted: "So at most about half of the men can lie anywhere between 16.7 and 28.8. The colleague's "20 to 24" is a narrower band sitting inside that half."
   - Wrong: about half (not "at most about half") lie between the quartiles. The bound that matters is on 20 to 24: at most about half can lie there.
   - Fix: "So about half the men lie between 16.7 and 28.8. The colleague's 20 to 24 sits inside that stretch, so at most about half can lie in it."
   - Support: the definition of the quartiles.
   - Fix: P16 answer now reads "So about half the men lie between 16.7 and 28.8. The colleague's 20 to 24 sits inside that stretch, so at most about half can lie in it."
   - Verify: closed
