# B0-R0-C25 (D2) — compression-pass holes, audit triage

1. **C25-K1** — CONFIRMED-ERROR — `must_know[4]`
   - Quoted: "A number built by multiplying several ceilings together is a smaller ceiling. Carry the same "at most" or "at least" through every step."
   - Wrong: every "1 minus" step turns the direction round. The section's own P8 working goes ceiling 0.75 → floor 0.25 → floor 0.015625 → ceiling 0.984375. Following the rule as written gives "at most 0.25" in P13 and points that conclusion the wrong way. This comes from C24-K1.
   - Fix: "Multiplying ceilings gives a ceiling, and multiplying floors gives a floor. Every '1 minus' step turns one into the other. Label each line 'at most' or 'at least' as you go."
   - Support: logic. For non-negative numbers, a ≤ A and b ≤ B give ab ≤ AB. And x ≤ c gives 1 − x ≥ 1 − c.
   - Fix: must_know[4] replaced with the suggested three sentences (ceilings give a ceiling, floors a floor, each "1 minus" swaps them; label each line).
   - Verify: closed

2. **C25-K2** — CONFIRMED-GAP — `illustration.body` (the three-people complement working); affects P3, P8, P11
   - Quoted: "Go by the complement instead: work out the probability that none of the three is covered, and subtract that from 1."
   - Gap: (a) The text never says that if the "covered" events are independent, so are the "not covered" events, and the working multiplies the not-covered probabilities. (b) The working never labels where the bound turns from a ceiling to a floor and back.
   - Fix: add "If the three 'covered' events are independent, the three 'not covered' events are too." Label the working lines: "P(not covered) is at least 0.25", "P(none covered) is at least 0.015625", "P(at least one covered) is at most 0.984375".
   - Support: logic. The standard result that complements of independent events are independent is not quoted anywhere in the record. If Harsh wants a citation, openstax_intro_stats_2e s.3.2 is the place to look. Not checked here.
   - Fix: illustration now says complements of independent events are independent, that each "1 minus" swaps ceiling and floor, and labels the lines at least 0.25, at least 0.015625, at most 0.984375. Stated as logic; no openstax quote added (not checked, as the defect notes).
   - Verify: closed

3. **C25-K3** — CONFIRMED-ERROR — `practice[12]` (P13 answer)
   - Quoted: "It gives no figure for households of four in particular, so the report's 'high' has nothing under it." and "The 75 per cent is national."
   - Wrong: (a) The problem says "Decide what to compute, compute it", but the answer never computes the correct figure. There is one. The person is picked at random, and every member shares the household's status. So P(some member not covered) = P(this person not covered), which is **at least 0.25**. That is a floor. It neither supports "high" nor leaves it with "nothing under it". (b) "National" is not in the held Act (see C24-K2).
   - Fix: replace the quoted paragraph's last two sentences with: "So the chance is the chance this one person is not covered: at least 0.25, a floor. That does not make it 'high', and it does not rule 'high' out." Replace "The 75 per cent is national." with "Section 3(2) names no State or district."
   - Support: logic, plus nfsa_2013 s.9 as in C24-K2.
   - Fix: P13 now says the chance is this one person's, with a new `1 minus 0.75 = 0.25` working, "At least 0.25, a floor", neither makes nor rules out 'high'; "The 75 per cent is national." replaced with "Section 3(2) names no State or district." Recomputed in Python.
   - Verify: open, because the new 'at least 0.25, a floor' is not supported: the prompt tells us this person lives in a household of four, and the 75 per cent ceiling is on the rural population as a whole (the answer itself says 'a ceiling on all rural people together'), so it puts no floor on non-coverage within a subgroup such as households of four; the removed 'no figure for households of four in particular' was right on that point. The 'national' half of the fix is closed.

4. **C25-K4** — CONFIRMED-GAP — `definition.text`; affects Exercise 1, P12, illustration
   - Quoted: "Independence is checked, not assumed: A and B are independent exactly when P(A and B) ... equals P(A) times P(B), and dependent otherwise."
   - Gap: the illustration has no joint figure, so the check cannot be run there. The illustration then "treats" two households as independent by argument alone. The text never says that a direct argument counts as the check, or what to do when neither is available. The definition's reference quote "assume they are dependent until you can show otherwise" backs a sentence that the compression removed. As things stand, that quote supports nothing in the prose.
   - Fix (definition, after the first sentence of that paragraph): "Where no joint figure exists, the check is an argument that knowing one tells you nothing about the other. If you can make neither, treat them as dependent."
   - Support: openstax_intro_stats_2e, already in the record: "if the knowledge that one occurred does not affect the chance the other occurs" and "assume they are dependent until you can show otherwise". Mean sentence length may rise. Harsh's rule takes the correctness fix first.
   - Fix: definition gains the two suggested sentences after the P(A)P(B) test sentence (now backed by the existing "assume they are dependent" quote).
   - Verify: closed

5. **C25-K5** — CONFIRMED-GAP (support) — `illustration.body`; affects P7, P10, P13, Exercise 1
   - Quoted: "If the household is covered, every person belonging to it is covered along with it."
   - Gap: nothing quoted in the record shows the Act works per household. The held Act does support it. The entitlement belongs to "every person belonging to priority households", and it is households that the State identifies (s.10).
   - Fix: add to the sentence: "the Act gives the entitlement to 'every person belonging to priority households', and it is households that the State Government identifies". Add both quotes to `illustration.numbers` or the references.
   - Support: nfsa_2013 s.3(1): "Every person belonging to priority households, identified under sub-section (1) of section 10, shall be entitled"; s.10(1)(b): "the remaining households as priority households to be covered under the Targeted Public Distribution System". Caveat: this is legal entitlement. It is not proof that ration cards list every member in practice, and P13's last paragraph already says so.
   - Fix: illustration sentence extended as suggested; the '5' number's quote widened to the full s.3(1) words, and a non-numeric numbers entry added quoting s.10(1)(b). Both quotes confirmed in sources/nfsa_2013.txt.
   - Verify: closed

6. **C25-K6** — CONFIRMED-GAP (minor) — `simplified_explanation`; P1
   - Quoted: "Two tosses give 2 squared outcomes, three tosses give 2 cubed, and n tosses give 2 to the power n."
   - Gap: "cubed" appears in no earlier released section (checked A1–C9 released text). A6 names only "squared".
   - Fix: "three tosses give 2 cubed, which is 2 to the power 3,".
   - Support: none needed.
   - Fix: simplified_explanation now reads "three tosses give 2 cubed, which is 2 to the power 3,".
   - Verify: closed

7. **C25-K7** — CONFIRMED-GAP (minor) — `practice[4]` (P5)
   - Quoted: "Two fair coins are tossed."
   - Gap: "fair" is not defined anywhere in A–D. The counting method needs equally likely outcomes, and D1 defines "equally likely" but not "fair".
   - Fix: "Two fair coins, each equally likely to land heads or tails, are tossed."
   - Support: none needed. D1 already cites "Equally likely means that each outcome of an experiment occurs with equal probability."
   - Fix: P5 prompt now reads "Two fair coins, each equally likely to land heads or tails, are tossed."
   - Verify: closed


## Round 2 (23 Sep 2026)

- **C25-R2a** · reopens C25-K3 (verifier): the P13 answer's new 'at least 0.25, a floor' does not follow. The prompt's person is in a household of four; the 75 per cent ceiling is for the rural population as a whole, not that subgroup. Make the answer say only what follows from the section (e.g. the ceiling for the whole rural population gives no bound for this subgroup, or state the bound for a person drawn from the whole rural population, if that is what P13 asks). Recompute any number.
