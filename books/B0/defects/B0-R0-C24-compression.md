# B0-R0-C24 (D1) — compression-pass holes, audit triage

Auditor: Opus, Task 3, fresh context. Record read as it now stands (compressed text).

1. **C24-K1** — CONFIRMED-ERROR — `must_know[3]`
   - Quoted: "Every probability, complement and odds you compute from a ceiling is itself a ceiling."
   - Wrong: 1 minus a ceiling is a floor. The record contradicts itself: `analogy_breaks_when` says "0.25 as the smallest the chance of not being covered could be", and P4 asks for "the smallest that the probability they are not covered can be". Carries into D2 (C25-K1, C25-K3).
   - Fix: "A probability or odds computed from a ceiling is itself a ceiling, but its complement is a floor: at most 0.75 covered means at least 0.25 not covered. Say which in the same sentence you quote the number, or the reader will treat it as a count."
   - Fix: must_know[3] replaced with the proposed wording (probability or odds from a ceiling is a ceiling; its complement is a floor). Also analogy_breaks_when "Every probability above is a ceiling" changed to "a bound", since it goes on to call 0.25 a floor.
   - Verify: closed

2. **C24-K2** — CONFIRMED-GAP — `illustration.body` (and `practice[8]` P9 answer, `exercises[0]` answer)
   - Quoted: "It shall extend up to seventy-five per cent. of the rural population, and up to fifty per cent. of the urban population."
   - Gap: the text never says whose rural population. The P9 answer then says "the 75 per cent is a national ceiling", and Exercise 1's answer says "India's rural population". The held Act does not say "national". Section 3(2) is silent, and section 9 has the Central Government set each State's percentage "subject to sub-section (2) of section 3". So P9 ("rural people here") cannot be answered from the text, and the answer's "national" goes further than the source.
   - Fix (illustration, one sentence after the ceiling): "Section 3(2) does not say it bounds any one State or district. Section 9 leaves 'the percentage coverage ... for each State' to the Central Government." In the P9 answer, replace "And the 75 per cent is a national ceiling." with "And section 3(2) names no State or district."
   - Support: nfsa_2013, s.9: "The percentage coverage under the Targeted Public Distribution System in rural and urban areas for each State shall, subject to sub-section (2) of section 3, be determined by the Central Government". Held source; add as a quote.
   - Fix: illustration gets the two proposed sentences after the ceiling; P9 answer "national ceiling" sentence replaced as proposed; Exercise 1 answer "India's rural population" changed to "the rural population". s.9 quote (confirmed in the held nfsa_2013.txt) added as a definition reference, kind instrument.
   - Verify: closed

3. **C24-K3** — NEW — `practice[8]` (P9), support
   - Quoted: "The Act leaves each State's share to the Central Government under section 9"
   - Wrong: this is a claim from the Act in a practice answer, but P9 has no `refs` field, contrary to SELFCHECK item 3.
   - Fix: add `refs: [nfsa_2013]` to P9 and quote s.9 as in K2.
   - Support: nfsa_2013 s.9 (quoted above).
   - Fix: added `refs: [nfsa_2013]` to P9; the s.9 quote is the definition reference added under K2.
   - Verify: closed


## Round 2 (23 Sep 2026)

- **C24-R2a** · HARSH DECISION (23 Sep): drop the statute's 'per cent.' full stop in the unquoted paraphrase; write 'per cent'. If the sentence is actually a marked quotation, leave it exactly as the Act has it.
