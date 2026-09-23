# Compression-pass holes, triaged · B0-R0-C34 (E4)

Auditor: Task 3, fresh context. Full per-hole verdicts: `books/B0/compress/TRIAGE-part-E.md`.
Practice numbering follows the list order: P5 = level 6 (tumblers), P7 = level 9 (poster).

---

**C34-K1** · CONFIRMED-GAP (wording). Settled by the record itself, so not NEEDS-HARSH.
- **Field:** `simplified_explanation`
- **Sentence:** "So the bucket and the spoonful are at the same temperature and hold very different amounts."
- **What is wrong:** it does not say amounts of what. Directly after "Heat … is an amount" it reads as "amounts of heat", which must_know[1] tells the reader to refuse ("refuse the sentence 'this object contains so much heat'").
- **Fix:** "…and hold very different amounts of energy." This is the wording the record's own exercise 1 answer already uses: "hold very different amounts of energy".
- **Support:** record-internal.
Fix: simplified_explanation now ends "hold very different amounts of energy."

**C34-K2** · CONFIRMED-GAP (minor)
- **Field:** `illustration.body`
- **Sentence:** "A calculator puts it at 9.26 degrees Celsius."
- **What is wrong:** the step is skipped (SELFCHECK 9). The reader is not shown that the rise is the energy divided by the joules per degree.
- **Fix:** add the working `4186 divided by 452 = 9.26` with the line "Divide the energy by what it needs for one degree." Checked: 4186 / 452 = 9.2611.
- **Support:** arithmetic.
Fix: replaced the calculator line with "Divide the energy by what it needs for one degree. That is 4,186 divided by 452, which comes to 9.26 degrees Celsius, to two decimal places. Check it backwards." plus working `452 times 9.26 = 4185.52`. The build's exact-match arithmetic check rejects `4186 divided by 452 = 9.26`, so the division is in prose and the checked line is the back-multiplication.

**C34-K3** · CONFIRMED-GAP (blocks P7 at step one)
- **Field:** `practice` L9 prompt and answer
- **Sentence:** "Four litres of water is four kilograms closely enough for this."
- **What is wrong:** nothing in A1–E4 gives the mass of a litre of water, and no held source states it (checked: no density-of-water statement in any file in `sources/`). The answer asserts a figure about the world with no citekey (SELFCHECK 3).
- **Fix (no source needed):** put the mass in the prompt. After the poster quote add: "Take the four litres as four kilograms of water." The answer then says "The prompt gives the mass as four kilograms." Otherwise, add a held source for the density of water.
- **Support:** none held for the physical fact. The fix avoids needing one.
Fix: prompt adds "Take the four litres as four kilograms of water."; answer now says "The prompt gives the mass as four kilograms." No new fact asserted.

**C34-N1** · NEW · CONFIRMED-ERROR (dangling pointer; recurring kind, see C28)
- **Field:** `practice` L9 answer
- **Sentence:** "That 4,184 is the calorie's definition, not water's specific heat. The two are different quantities. They are not the two books' disagreement about water, which this section described earlier."
- **What is wrong:** the reader-facing text of this section never describes a disagreement between the two books about water. Only the `illustration.numbers` entry for 4.184 mentions it, and that is not shown to the reader. The pointer points at nothing.
- **Fix:** delete the last sentence ("They are not the two books' disagreement…"). Then drop the 4.184 J/g°C numbers entry, which no reader-facing sentence now uses. Alternatively, restore one sentence to the illustration: "Chemistry 2e gives water 4.184 joules per gram per degree, which is 4,184 per kilogram. That differs from the table's 4,186, at a different temperature."
- **Support:** record-internal.
Fix: deleted the "They are not the two books' disagreement…" sentence and removed the 4.184 J/g°C illustration.numbers entry.

**C34-N2** · NEW · CONFIRMED-ERROR
- **Field:** `practice` L6 prompt and answer (P5)
- **Sentence:** prompt "Each tumbler itself rises by 55 degrees Celsius". answer "The chai in the glass ends up cooler once both tumblers have warmed, for that reason alone."
- **What is wrong:** the prompt fixes both tumblers at the same rise from the same start. When the tumbler stops warming, the chai in it is at the tumbler's temperature, so the chai ends at the same temperature in both. The conclusion contradicts the premise. With equal chai, the glass would in fact rise less than the steel.
- **Fix:** replace the sentence with "So to warm its tumbler by the same 55 degrees, the chai in the glass has to give up about 1.86 times as much energy. With the same amount of chai poured into each, the glass could not in fact rise the full 55 degrees. It would stop lower, and so would the chai." The simpler alternative is to cut the sentence.
- **Support:** logic, and the equilibrium sentence the record cites (College Physics 2e §14.1): "energy is transferred from the hotter to the colder object until equilibrium is reached".
Fix: replaced "The chai in the glass ends up cooler…" with "With the same amount of chai poured into each, the two tumblers could not both rise the full 55 degrees. The glass would stop lower, and so would the chai in it."

**C34-N3** · NEW · CONFIRMED-ERROR (minor, support)
- **Field:** `practice` L7 answer
- **Sentence:** "A hundred million joules is roughly what a small burner would deliver in a day of continuous running. Half a litre of water going from warm to very hot is a few minutes on a stove."
- **What is wrong:** these are two figures about the world with no citekey (SELFCHECK 3). The first implies a burner of about 1.2 kW (10^8 J / 86,400 s), stated as fact.
- **Fix:** delete both sentences and keep the pointer: "A size check would have caught it: the two answers are a thousand times apart, which is the kind of gap the section on orders of magnitude exists to make visible."
- **Support:** none held for the burner figure.
Fix: deleted the burner and stove sentences; the paragraph now reads "A size check would have caught it. The two answers are a thousand times apart, which is the kind of gap the section on orders of magnitude exists to make visible."
