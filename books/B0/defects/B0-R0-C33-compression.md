# Compression-pass holes, triaged · B0-R0-C33 (E3)

Auditor: Task 3, fresh context. Full per-hole verdicts: `books/B0/compress/TRIAGE-part-E.md`.
Practice numbering follows the list order: P3 = level 4 (lamp), P6 = level 8 (fan), P7 = level 9, P8 = level 10.

---

**C33-K1** · CONFIRMED-ERROR
- **Field:** `illustration.body` (line three). The same pattern is in `practice` level 4 (a) and (b).
- **Sentence:** "At the start, inside, there are 60,000 joules sitting in the gas. At the end … what is inside instead is the 42,000 in the water and the 11,000 in the steel." then `53000 minus 60000 = -7000`.
- **What is wrong:** it states an amount inside the boundary that is not the amount inside. The water, the pan and the burner already held energy at the start. What is being subtracted are changes, but they are presented as totals, and lines one and two worked by crossings, not totals. The answer is right only because the unstated starting amounts cancel.
- **Fix:** work by crossings, as lines one and two did: "Nothing crosses in. The 7,000 joules that reached the kitchen air crossed out. So the energy inside went down by 7,000 joules." Keep the check as changes: "the gas gave up 60,000; the water gained 42,000 and the steel 11,000: 42000 plus 11000 minus 60000 = -7000." In L4, change "At the start the kerosene holds 900,000 joules" to "Over the hour the kerosene gives up 900,000 joules of chemical energy", and describe (b) the same way.
- **Support:** logic. The record's own balance line is inside at end = inside at start + in − out.

Fix: applied. Line three now works by crossings (nothing in, 7,000 out: `0 minus 7000 = -7000`), then checks as changes (`42000 plus 11000 minus 60000 = -7000`). L4 (a) now says the kerosene gives up 900,000 J over the hour; L4 (b) works by crossing (`0 minus 60000 = -60000`) and checks as changes (`840000 minus 900000 = -60000`); the old totals line and `840000 plus 60000` check removed. Recomputed in Python.

**C33-K2** · CONFIRMED-GAP (support)
- **Field:** `illustration.body`, `analogy_breaks_when`
- **Sentence:** "> One joule is not a large amount of energy; it would lift a small 100-gram apple…" / "Only the size of the joule comes from a source."
- **What is wrong:** the reader is shown a quotation with no source named.
- **Fix:** introduce the quote with "OpenStax College Physics 2e, section 7.1, puts it like this." In analogy_breaks_when: "Only the size of the joule comes from a source, College Physics 2e section 7.1."
- **Support:** held. `openstax_college_physics_2e` §7.1, exact sentence present.

Fix: applied. Quote now introduced with "OpenStax College Physics 2e, section 7.1, puts it like this."; analogy_breaks_when now names "College Physics 2e section 7.1".

**C33-K3** · CONFIRMED-GAP
- **Field:** `must_know[5]`, `practice` L9 answer
- **Sentence:** "It crosses outwards as heat, as work done on things around them…"
- **What is wrong:** "work" is undefined in A1–E3.
- **Fix:** closed by C31-K2 (define work in E1). No change here once that lands.
- **Support:** held. College Physics 2e §7.1.

Not applied: the triage's own fix is no change here; it closes when C31-K2 (define work in E1) lands. Released E1 does not yet define work, so this stays open until that fix is in.

**C33-K4** · CONFIRMED-ERROR (internal contradiction)
- **Field:** `must_know[5]` and `practice` L9 against `practice` L10. It also bears on E6 and E8.
- **Sentences:** must_know[5]: "Energy crosses a person's line inwards in food and drink. It crosses outwards … in what leaves the body unabsorbed." L9: "9,000 kilojoules crosses in with food, 1,000 kilojoules leaves unabsorbed". L10: "What crosses in is not what the sample holds. It is what the sample holds, minus whatever leaves the person without being absorbed."
- **What is wrong:** L9 and must_know[5] draw the person's line at the mouth, where unabsorbed food crosses in and back out. L10 draws it at the gut wall, where unabsorbed food never crosses in. E6 ("it never became part of you") and E8 ("Until a molecule passes through the wall of the tube…") also use the gut wall. The section's own lesson is that two lines give two answers and you must say which, and it switches lines without saying so.
- **Fix:** add one sentence to `must_know[5]`: "Two lines are both in use: one at the mouth and skin, where unabsorbed food crosses in and back out, and one at the gut wall, where it never crosses in. Say which one you mean." In L10, write "The colleague's line, drawn at the mouth: 1,200 crosses in and U crosses back out unabsorbed, so the net crossing is 1200 minus U. Draw it at the gut wall instead and the same 1200 minus U is simply what crosses in." No source needed.
- **Support:** logic, from the section's own definition.

Fix: applied. must_know[5] gains the two-lines sentence (mouth and skin vs gut wall, say which). L9 now says its line is drawn at the mouth and skin. L10 now shows both lines give the same net crossing (merged with N1, so the unknown is D rather than U).

**C33-K5** · CONFIRMED-GAP
- **Field:** `practice` L8 answer (P6)
- **Sentence:** "The fan turned it into moving air and the moving air turned it into warmth, and all of it stayed inside. The room got warmer."
- **What is wrong:** the balance gives +300,000 J inside, and nothing up to E3 teaches that it ends up as warmth. E4, the next section, is where heat and temperature are introduced. The section itself says the balance "does not tell you which way energy went", and the answer asserts the form.
- **Fix:** "The energy inside the room went up by 300,000 joules. The balance does not say what form it ends in. It does remove the only support for 'cannot have got warmer', and the next section shows where such energy shows up." Alternatively, add a sourced line such as "Electrical energy is a common form that is converted to many other forms" (College Physics 2e §7.6, held), but that still does not give warmth, so prefer the rewording.
- **Support:** logic, and the record's own `definition.text` ("It does not say by which route…").

Fix: applied, with the triage's wording. The answer now says the balance does not say what form the 300,000 J ends in, that it removes the only support for "cannot have got warmer", and that the next section takes up where such energy ends up. No warmth asserted.

**C33-N1** · NEW · CONFIRMED-ERROR (contradicts E2)
- **Field:** `practice` L10 answer
- **Sentence:** "The label's line. A food's energy figure is measured, or calculated, for the food burnt completely. The boundary is drawn round the food sample, and what crosses out is everything the sample holds."
- **What is wrong:** E2 (C32) teaches the opposite for a calculated figure: "Those factors already have the losses taken out of them … So the figure on the packet is an estimate of metabolizable energy for an average". A label figure is not gross energy, so "1200 minus U" double-counts the average losses.
- **Fix:** "The label's figure was calculated with the Atwater factors, which already take off average losses (the section on the bomb calorimeter). So 1,200 is an estimate of what an average person gets from the packet. The colleague's sentence is about this person. Call the gap between this person's losses and the average D, and nobody in the room has a figure for D." Keep the rest of the argument.
- **Support:** C32 simplified_explanation; FAO §3.5.1 (held): "based on the heats of combustion … which are corrected for losses in digestion, absorption and urinary excretion of urea."
Fix: applied. L10 prompt now stipulates the label figure was calculated with the Atwater general factors (part of the made-up scenario). The answer says the section before showed those factors already take off average losses, so 1,200 is an estimate for an average person; the unknown is now D, this person's losses minus the average; 'what to say in the meeting' reworded to match. Added B0-R0-C32 to concept_deps for the pointer. Caveat: the fact that the factors carry average losses rests on E2's FAO citation, not on a source cited in this record; it is stated as a recall of the earlier section, not re-cited here.
