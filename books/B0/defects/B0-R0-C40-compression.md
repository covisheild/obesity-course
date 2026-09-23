# B0-R0-C40 (F2, Reading a figure): compression-pass holes, audit triage

Auditor: Opus, Task 3. I recomputed all 13 practice answers, the illustration and the exercises. All the arithmetic is correct. (1.556² = 2.42; (14/9)² = 2.4198; sqrt(1.6) = 1.2649; 18/5.5 = 3.27; 300/7400 = 0.0405; 30/440 = 0.068.)
"Recurring" means the kind is on check/SELFCHECK.md.

1. **C40-K1**. Class: CONFIRMED-ERROR (it contradicts an earlier section), **recurring** (SELFCHECK 7). Fields: simplified_explanation, must_know[0], and definition.references[2].verified.note.
   Sentences: "So a bar chart must start at zero, and a line chart need not." "'Every chart must start at zero' is the error." The note: "This record applies the warning to bars and not to line charts, which agrees with B0-R0-C19."
   What is wrong: C5 (B0-R0-C19), as released, tells the reader two things about any figure, lines included. "A side axis that does not start at zero makes every small wiggle on it look like a cliff." And "When a figure alarms you, redraw it with the side axis starting at zero before you repeat it to a journalist." F2 never names that advice. A reader who holds both gets opposite instructions about a line chart, which blocks a confident answer to P11 and Ex 3. The note's "agrees with B0-R0-C19" is true of C5's figure caption ("neither is dishonest") but not of its must-knows.
   Fix (on the F2 side, after "a line chart need not"): "The section on graphs told you to redraw an alarming line from zero before repeating it. Keep doing that, as a check on the impression a slope gives. It does not mean the first drawing was dishonest. A line on a printed non-zero axis is honest; a bar on one is not." Change the note to "agrees with the figure caption of B0-R0-C19; that section's advice to redraw from zero is a check on impression, not a rule of honesty."
   Alternative: reword C5's must-know to scope it to impressions. C5 is released, so which side changes is Harsh's call.
   Support: C5-released line 209 ("neither is dishonest"), and lines 221 and 224.
   Fix: Not applied: awaits Harsh (which side of the C5/F2 zero-baseline conflict changes).
   Fix: applied in round 2 under Harsh's decision (reword F2, not C5); see C40-R2a.

2. **C40-K2**. Class: CONFIRMED-ERROR. Fields: illustration.body; also practice level 2 answer and practice level 7 (first) answer.
   Sentences: "The page a plate covers is its height times its width." "Area is height times width, and both were multiplied by the same number." (P2) "Area is height times width, and the working added them." (P7)
   What is wrong: this is true only of a rectangle. A round plate of diameter d covers (π/4)·d², not d². The ratio 2.42 still holds, because any shape scaled by k both ways covers k² as much: (π/4)(kd)² ÷ (π/4)d² = k². But the sentence as written is false. The held source's "area (height × width)" is about rectangular bars.
   Fix, in the illustration: "Whatever its shape, a plate made 1.556 times as tall and 1.556 times as wide covers 1.556 times 1.556 as much of the page." In P2 and P7: "Whatever the shape, its area is multiplied by the height's factor times the width's factor."
   Support: the arithmetic above.
   Fix: illustration now says "Whatever its shape, a plate made 1.556 times as tall and 1.556 times as wide covers 1.556 times 1.556 as much of the page."; P2 and first P7 answers now say "Whatever the shape, its area is multiplied by the height's factor times the width's factor". Arithmetic unchanged.
   Verify: closed

3. **C40-K3**. Class: CONFIRMED-GAP (a term is never defined). Field: definition.text.
   Sentences: "So the value axis of a bar chart must start at zero." "A bar chart's value axis may start above zero."
   What is wrong: "value axis" appears only here. Everything after it, and C5, says "side axis". Bars lying flat are not covered.
   Fix: "…so the value axis (the one a bar's length is read against: the side axis when bars stand up, the bottom axis when they lie flat) must start at zero."
   Source: none needed.
   Fix: definition.text now adds "The value axis is the one a bar's length is read against: the side axis when bars stand up, the bottom axis when they lie flat."
   Verify: closed

4. **C40-K4**. Class: CONFIRMED-GAP. Field: simplified_explanation, which Ex 2 depends on.
   Sentence: "Two pie charts drawn the same size for two years hide any change in the total."
   What is wrong: a pie chart is never explained, here or in A to E. Ex 2 turns on the fact that a slice shows a share of a whole, and that fact appears only in Ex 2's answer.
   Fix, under "By area": "A pie chart is a circle standing for a whole. Each slice's share of the circle is its share of the total, so a slice shows a share, not an amount."
   Source: none needed. The held openstax_business_stats_2e pie paragraph is consistent with it.
   Fix: added the pie-chart sentences (circle for a whole; slice shows a share, not an amount) at the end of the "By area" paragraph.
   Verify: closed

5. **C40-K5**. Class: CONFIRMED-GAP, **recurring** (SELFCHECK 7). Field: practice level 3, prompt and answer.
   Sentences: "with a mark every 20"; "Point A sits level with the third mark above the bottom."
   What is wrong: the section defines "a mark" as the thing drawn for a data value ("A mark is anything drawn that stands for one number: a bar, a point…"). P3 uses the word for an axis tick. One word is doing two jobs in one section.
   Fix: in P3, use "a numbered line every 20" and "the third numbered line above the bottom" in the prompt and in the answer ("List the numbered lines first…").
   Source: none needed.
   Fix: P3 prompt and answer now say "numbered line" for every axis tick; "mark" is left only for a drawn data value.
   Verify: closed

6. **C40-K6**. Class: CONFIRMED-GAP, **recurring** (SELFCHECK 9: derivations do not skip). Field: simplified_explanation (Unequal spacing); P9 answer.
   Sentence: "Either way it cannot be compared with the others."
   What is wrong: the P9 answer puts the wide bin on a fair footing by dividing its count by the number of standard spans it covers (18 ÷ 5.5). The text never teaches that step. It says only that the bar cannot be compared.
   Fix: add: "To compare it fairly, divide its count by how many of the ordinary spans it covers. That gives the count for each ordinary span, on average."
   Source: none needed (arithmetic).
   Fix: Unequal spacing now ends "...cannot be compared with the others as it stands. To compare it fairly, divide its count by how many of the ordinary spans it covers. That gives the count for each ordinary span, on average."
   Verify: closed

7. **C40-K7**. Class: CONFIRMED-GAP. Field: illustration.body, which Ex 1 depends on.
   Sentence: Ex 1 prompt: "Then describe two honest ways to redraw it."
   What is wrong: only one redraw (from zero) is shown. The second, used in the answer (dots with no bars), is never named.
   Fix: after "Redraw the chart with the side axis starting at zero. Each bar is now as long as its value.", add: "Or keep the axis from 400 and draw each value as a dot with no bar under it. A dot carries its value by position."
   Source: none needed.
   Fix: illustration adds, after the zero redraw, "Or keep the axis from 400 and draw each value as a dot with no bar under it. A dot carries its value by position."
   Verify: closed

8. **C40-K8**. Class: NEW (a minor inconsistency), **recurring** (SELFCHECK 5 and 7). Fields: simplified_explanation compared with Ex 1, Ex 3, P11 and retrieval_items[1].
   Sentence: simplified: "a printed axis starting at 400 tells you where they are". Elsewhere the condition is "printed on the axis and stated in the caption".
   What is wrong: the condition under which a non-zero line axis is honest is stated two ways. A reader cannot tell whether the caption is required.
   Fix: in simplified_explanation, "a printed axis starting at 400, stated in the caption, tells you where they are". Or drop the caption condition everywhere.
   Fix: simplified_explanation now reads "a printed axis starting at 400, stated in the caption, tells you where they are", matching Ex 1, Ex 3, P11 and retrieval_items[1].
   Verify: closed


## Round 2 (23 Sep 2026)

- **C40-R2a** · HARSH DECISION on C40-K1 (23 Sep): reword F2, not C5. After 'a line chart need not' add, in the section's register, that the earlier section's advice to redraw an alarming line from zero is a check on the impression a slope gives, not a rule of honesty; a line on a printed non-zero axis is honest, a bar on one is not. Change the reference note that says F2 'agrees with B0-R0-C19' to say it agrees with that section's figure caption, and that the redraw-from-zero advice is a check on impression. Make P11 and Ex 3 answers consistent.
  Fix: simplified_explanation, after "a line chart need not.", adds "The section on graphs told you to redraw an alarming line from zero before you repeat it. Keep doing that. It is a check on the impression a slope gives, not a rule of honesty. A line on a printed non-zero axis is honest; a bar on one is not." definition.references[2] note now says it "agrees with the figure caption of B0-R0-C19. That section's advice to redraw an alarming line from zero is a check on impression, not a rule of honesty."; the openstax_business_stats_2e note now says it follows "the figure caption of B0-R0-C19". P11 (first level-9) answer adds "Redrawing it from zero, as that section advised, checks the impression. It does not make the first drawing dishonest." Ex 3 answer adds "If the line looks alarming, redraw it from zero to check the impression. That is a check, not a sign that the first drawing was dishonest." C5 unchanged.
