# B0-R0-C29 (D6) — compression-pass holes, audit triage

1. **C29-K1** — CONFIRMED-GAP — `illustration.body`; affects P9 (line 3), P10
   - Quoted: "Suppose the 282 had instead been drawn at random from young adults, the group the paper set out to study. The square-root law would then say something concrete."
   - Gap: the promise is never kept. The law is taught only for "the average of a random sample", and the text never says that a percentage such as 34.8 is an average. P9's note applies the law to a share.
   - Fix: replace the second sentence with: "A share is itself an average: count each yes as 1 and each no as 0. So the square-root law would then say how far 34.8 per cent was likely to sit from that group's own figure." Do not give the p(1 − p) spread formula unless a source is added (openstax_intro_stats_2e ch. 7 or 8 would be the one to add; not checked here).
   - Support: logic (the mean of 0/1 values is the share). No source needed for the fix as worded.
   - Fix: in `illustration.body`, replaced "The square-root law would then say something concrete." with the wording above (share = average of 1s and 0s; law would say how far 34.8 per cent was likely to sit from that group's figure). No spread formula for a share added; no new fact asserted.
   - Verify: closed

2. **C29-K2** — NEW (false pointer) — `practice[6]` (P7 answer)
   - Quoted: "Adding and subtracting a spread from a mean is exactly the move this section has used before."
   - Wrong: neither D6 nor D5 ever adds or subtracts a spread from a mean.
   - Fix: "Adding and subtracting a spread from a mean looks like a natural move."
   - Support: the record's own text.
   - Fix: P7 answer sentence now reads "Adding and subtracting a spread from a mean looks like a natural move."
   - Verify: closed

3. **C29-K3** — NEW (minor, record hygiene) — `illustration.numbers`
   - Quoted: "0.633 standard deviation of 5,000 simulated sample-of-10 means" / "0.317 ... sample-of-40 means"
   - Wrong: the simulation these numbers describe is no longer in the prose after compression. These entries point at nothing and cite an openstax quote for simulated values.
   - Fix: delete both entries.
   - Support: the record's own text.
   - Fix: deleted the 0.633 and 0.317 entries from `illustration.numbers`. Caveat: the figure caption (d6-sample-means.png) still states 0.317 and 0.633; the build does not flag this, but the caption's simulated values now have no numbers entry.
   - Verify: closed


## Round 2 (23 Sep 2026)

- **C29-R2a** · follows C29-K3 (verifier caveat): the figure d6-sample-means.png caption still states 0.317 and 0.633, but their illustration.numbers entries were deleted. Either restore those two numbers entries exactly as they were at commit 64547ef^ (git show 64547ef^:check/records/B0/B0-R0-C29.yml), marked as the record's own simulated values, or remove the values from the caption. Prefer restoring the entries; do not redraw the figure.
  Fix: restored the 0.633 and 0.317 illustration.numbers entries byte-for-byte from 64547ef^ (marked as simulation output, not source figures); re-ran the seed-110 simulation, both values reproduce; caption and figure unchanged.
