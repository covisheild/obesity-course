# Book 0 · Part C, sections C1–C5 — audit defect list

Records audited: `B0-R0-C15` (C1, variables), `B0-R0-C16` (C2, rearranging), `B0-R0-C17` (C3, two
equations), `B0-R0-C18` (C4, functions), `B0-R0-C19` (C5, graphs). Audited 23 September 2026
against `claude.md`, `books/B0/INVENTORY-part-C.md`, `B0-R0-C06`, `B0-R0-C14` and
`check/figures/draw.py`.

Quoted passages and prose arithmetic were taken as already checked and were not re-verified. Every
practice answer was recomputed anyway; the arithmetic holds everywhere. What follows is about
method, boundaries, sourcing and the chain.

**C1 (`B0-R0-C15`) is clean.** Six problems, all four bands, every conversion factor in the numbers
register with its quote and citekey, no unsourced claim, no orphan pronoun, and the boundary
must-know ("the algebra will hand you a negative mass without complaining") is a real boundary. It
carries nothing on this list.

Drill-set counts are all inside the inventory's bands: C1 six (5–7), C2 twelve (10–12), C3 ten
(8–10), C4 seven (6–8), C5 twelve (10–14). Every set reaches the mechanical band and the transfer
band.

**The Part B debt is discharged.** `B0-R0-C16` practice level 4 recovers a missing mass from a body
mass index of 27.0 kg/m^2 and a height of 1.60 m, giving 69.12 kg. It uses `B0-R0-C14`'s exact
words — "body mass index", then "the index", the index being "the mass in kilograms divided by the
square of the height in metres" — and it states no threshold. Nor does any other problem in the five
records: levels 6, 7 and 9 of C2 carry index values of 24.0, 25.0 and 22.0 and say nothing about
what any of them means. Level 4's closing line is the right one and holds the boundary explicitly:
"What any value of it means is a separate decision. Some body took that decision, on some date, for
some population." Confirmed clean.

---

## 1. `B0-R0-C16`, `practice[8]` (level 9), answer — the stated interval for the recovered mass is false

The answer propagates the rounding of the index and not the rounding of the height, then states a
result as a range: "The recovered mass is somewhere between about 59.8 and 60.0 kilograms. A
quarter of a kilogram of uncertainty was created by dropping a column that had been measured."

The height is given as 1.65 m, which is rounded to two decimal places just as 22.0 is rounded to
one. A height anywhere in 1.645 to 1.655 squares to 2.706 to 2.739, and that spread is larger in
its effect than the index's. Taking both ends of both inputs:

- 21.95 × 1.645^2 = 21.95 × 2.706 = 59.40 kg
- 22.05 × 1.655^2 = 22.05 × 2.739 = 60.40 kg

The recovered mass is somewhere between about 59.4 and 60.4 kg — about one kilogram of
uncertainty, not a quarter. The answer understates it roughly fourfold, and it does so by picking
the smaller of the two contributions while presenting the result as the whole of it. It also
contradicts this record's own must-know point, which says "A recovered number carries the rounding
of everything you put in". This is a worked answer in the appendix, where the reader who disagrees
assumes they are the one who erred.

**Fix.** After the two index lines, add the height's own rounding as two further lines — square
1.645 and 1.655, multiply each by the matching end of the index — and restate the range as about
59.4 to 60.4 kg, about a kilogram. One paragraph, no change to the prompt.

## 2. `B0-R0-C16`, `definition.text` — "four operations leave the solutions unchanged" is false for one of the four

The definition says: "If two expressions stand for the same number, then applying the same
operation to both of them gives two expressions that still stand for the same number. Four
operations therefore leave the solutions of an equation unchanged" — then lists adding,
subtracting, multiplying, and "dividing both sides by the same quantity that is not zero".

The guard is on division only. Multiplying both sides by zero turns `x = 1` into `0 = 0`, which
every number satisfies; multiplying both sides by an expression holding the letter does the same
thing less visibly (`x = 3` times `(x − 1)` gives `x(x − 1) = 3(x − 1)`, which is also satisfied by
x = 1). Multiplication preserves *truth* for a given value but does not preserve *the solutions*,
which is what the sentence claims. The section then relies on the move: practice level 4 multiplies
both sides by h^2, and level 6 by h^2 again.

**Fix.** Put the same guard on the multiplying bullet: "multiplying both sides by the same quantity
that is not zero". One clause.

## 3. `B0-R0-C16`, `practice[7]` (level 6), answer — a square root is taken of both sides as if it were one of the section's four moves

The answer reaches `h^2 = m divided by I`, then: "Take the square root of both sides, which is the
step the problem before it did not have." It then says "The square root of 2.25 is 1.5, because 1.5
multiplied by itself gives 2.25" and stops.

Three things are wrong with this, and they compound.

- The square root is not among the four operations the definition says are legal, and the record
  never adds it. §1 operational test 5 of the specification: a step requiring an algebraic move not
  taught is a floor violation.
- Minus 1.5 multiplied by itself also gives 2.25. Squaring is not reversible without choosing a
  branch, and neither `B0-R0-C06` (which defines a square root as "the number which, multiplied by
  itself…", singular) nor this record ever says so. The reader is left with "take the square root
  of both sides" as a move that returns one answer, which is the trap the prompt for this audit
  names and the one that will break the next time it is used on something that can be negative.
- Nothing says why the negative root is discarded here. The reason is that a height cannot be
  negative — a fact about the quantity, not about the algebra — and that is exactly the kind of
  reading-back this record's sibling `B0-R0-C15` already teaches in its boundary point.

**Fix.** Two sentences in the level 6 answer, after "Take the square root of both sides": say that
squaring loses the sign, so two numbers square to 2.25, 1.5 and minus 1.5; and that you keep 1.5
because a height cannot be negative. Add a fifth bullet to `definition.text` naming the square root
as a move that gives two answers unless the quantity rules one out, and a `boundary` must-know
point carrying the same thing.

## 4. `B0-R0-C18`, `must_know[2]` — "doubles back on itself" is the wrong test, and it forward-references C5

The point reads: "A drawn curve that doubles back on itself is giving one input two outputs. It is
not the picture of a function, whatever the caption calls it, and you can say so from the shape
alone."

A U-shaped curve — `y = x^2`, the shape `B0-R0-C20` is about to teach — doubles back in every
ordinary sense of the phrase, and is a function. The test that is actually meant is whether two
points sit directly above one another, which is a statement about the x direction, not about the
curve reversing. As written, the point trains the reader to reject good rules, which is precisely
what the must-know point directly above it warns against ("A resident who learns the test backwards
starts rejecting good rules").

It is also a forward reference. `B0-R0-C19` is the section that introduces axes and what "above"
means; §10 rule 1 says a section may assume everything before it and nothing after it. At C4 the
reader has no x-axis to reason with.

**Fix.** Either move the point into `B0-R0-C19`, where axes exist and it can be stated as the
vertical test, or rewrite it here without a drawing: "Two rows of a table with the same input and
different outputs, and two points of a drawing sitting one directly above the other, are the same
defect."

## 5. `B0-R0-C18` and `B0-R0-C19` — "range" is defined as a term of art in C4 and then used in C5 to mean something else

`B0-R0-C18` `definition.text`: "The collection of outputs it can return is its range."

`B0-R0-C19` `retrieval_items[3]`: "The range printed on the side axis. A shorter range makes the
same change fill more of the picture"; and `practice[11]` answer: "Zero people is outside the range
of every point that was fitted."

Same word, three meanings, one section apart: the outputs of a function, the span of an axis, the
span of the fitted data. §10 rule 2 — a term is introduced once and afterwards used in the same
words — is broken in the direction that costs most, because the technical sense is the one the
reader was told to remember.

**Fix.** C5 has no need of the word. Replace it with "the numbers printed on the side axis" in the
retrieval item and "outside every household size that was fitted" in the level 10 answer. See also
defect 12, which proposes cutting the C4 sentence entirely.

## 6. `B0-R0-C17`, `definition.text` — claims that hold for linear equations are asserted for equations in general

Three sentences assert more than is true:

- "It states a relation between them: every value given to one fixes a value of the other." Not in
  general. Give x the value 2 in `x + y^2 = 1` and y has two values; give it 5 and y has none.
- "A system of two such equations has exactly one solution, or none, or infinitely many." This is
  the trichotomy for *linear* systems. Two conics meet in up to four points.
- "It has infinitely many when one equation is a multiple of the other." Again linear-only, and
  again asserted flatly.

Nothing in the record ever says the word "linear" or restricts what kind of equation is meant, and
`concept_type: derivable` means the reader is invited to rebuild these from the floor. They cannot,
because as stated they are not rebuildable — they are false. The section's actual content is fine;
its statement of scope is missing.

**Fix.** One sentence at the head of `definition.text`: "Everything below concerns equations in
which each unknown appears on its own, multiplied by a number and added — the only kind this book
uses." Then the three claims are true as written.

## 7. `B0-R0-C19`, `practice[10]` (level 9), prompt — "The depot" has no antecedent

The prompt gives a press line about "the average bag", then says: "The depot and all four figures
are made up for this problem."

No depot appears anywhere in the prompt, in the press line, or in the record. The reader stops and
goes back looking for it, which §10 defines as a defect with a fix. "The average bag" is also
unanchored — a bag of what is never said, and the axis label is only implied by the unit.

**Fix.** Rewrite the sentence as "All four figures are made up for this problem", and name the
quantity in the press line: "the average bag of grain leaving the depot has shot up" — which
supplies the depot at the same time.

## 8. `B0-R0-C17`, `illustration.body` — an answer is announced and never shown

"One line, two unknowns. Here is the answer that comes back first, and it is not wrong arithmetic.
It is the belief that there is one answer to find."

Nothing follows. The two sections before this one use the identical construction — "Here is the
working that comes back first. It is wrong." — and both then print a `working` block. Here the
reader is promised a thing to look at and handed a sentence about a belief instead, and the two
"it"s in the second sentence point at an object that was never put on the page.

**Fix.** Rewrite the lead-in so it promises nothing: "One line, two unknowns. What comes back first
is not a wrong sum. It is the belief that there is one answer to find. There is not."

## 9. `B0-R0-C19`, `definition.text` — a slope is defined between "any two points", with no vertical line excluded

"The slope of a straight line is the change in the y quantity divided by the change in the x
quantity, measured between any two points on it."

Two points on an upright line have a run of zero, and the definition then asks the reader to divide
by it — one section after `B0-R0-C16` taught them never to divide by something that might be zero.
The record handles the flat case explicitly (practice level 2, slope zero) and never handles its
mirror. `analogy_breaks_when` names only the curve case.

**Fix.** Add to `analogy_breaks_when`: "Two points one directly above the other have no run at all.
An upright line has no slope, because the division has nothing to divide by." One sentence, and it
reuses C2's own rule.

## 10. `B0-R0-C19`, `definition.references[0].locator` — the chapter named does not cover half of what the definition asserts

The locator is "ch. 4, Linear Functions". Ch. 4 of *College Algebra 2e* is the plausible chapter for
slope, intercept and reading a straight line, and for those the anchor is right. But the definition
also fixes the origin, the x-axis and the y-axis, and the writing of a point as (x, y) — the
rectangular coordinate system, which in that book sits in ch. 2, not ch. 4. As the locator stands,
a reader sent to confirm the coordinate material will not find it where they were sent, and
`locator` is the field that makes a citation checkable at all.

**Fix.** Extend the locator to "ch. 2, on the rectangular coordinate system and graphs, and ch. 4,
Linear Functions", matching the two-chapter form `B0-R0-C15` already uses. `claim_located` stays
false either way. The other four anchors are plausible as named: ch. 1 and ch. 2 for variables and
substitution, ch. 2 for solving and for solving a formula for a named variable, ch. 7 for systems,
ch. 3 for functions including domain and range.

## 11. `B0-R0-C18`, `practice[4]` (level 6) — a statutory figure used with no `refs`

The prompt: "A household of five is counted for 25 kilograms of foodgrains a month under the rule
in the section above."

The 25 kg is the section 3(1) entitlement multiplied out, and the problem then does arithmetic on
it and asks the reader to remember the result. Level 5, immediately above, carries
`refs: [nfsa_2013]` for the same figure. This one carries none. §7a: a problem quoting a real number
names its citekey in `refs`. "The rule in the section above" is also doing the work a citation
should do, and in the appendix — where the answers are printed — "the section above" is nowhere
near.

**Fix.** Add `refs: [nfsa_2013]`, and replace "under the rule in the section above" with "under
section 3(1) of the National Food Security Act, 2013, which entitles a person in a priority
household to five kilograms of foodgrains a month".

## 12. `B0-R0-C18`, `definition.text` — "domain" and "range" are asserted and then built nowhere

"The collection of inputs the rule accepts is its domain. The collection of outputs it can return
is its range."

Neither word appears again in the record — not in `simplified_explanation`, not in the
illustration, not in a must-know point, not in an exercise, not in a practice problem, not in a
retrieval item. §11 rule 10 makes `definition.text` the one field allowed to stay technically
exact *because* `simplified_explanation` owes the reader the same content in the plain register
directly beneath it, and here it does not deliver it. For a `derivable` concept that is an
assertion from the floor's point of view rather than a thing built on it, and it is the sentence
that then collides with C5 (defect 5).

**Fix.** Cut the sentence. Nothing in Part C uses either word, and `B0-R0-C20`, which is next, does
not either. If they are wanted, they need a paragraph in `simplified_explanation` and a practice
problem that asks for the domain of something — which the drill count has room for.

## 13. `B0-R0-C16`, `practice[3]` (level 3), prompt — "make the subject" is a term of art the book never defines

The prompt says "Rearrange each of these to give the named letter on its own", which is clear, and
then the three bullets say "make W the subject", "make x the subject", "make t the subject". The
word *subject* in this sense appears nowhere else in `B0-R0-C16` or in any earlier record. The
definition gives the concept its own name — "to solve an equation for a letter" — and a second name
arrives one field later with no bridge. §2 rule 6, define or point; §10 rule 2, one term, one set of
words.

**Fix.** Either drop "the subject" from the three bullets, since the prompt line above already says
what is wanted, or teach it inline once in `simplified_explanation` in the dash form §11a rule 12
asks for: "getting one letter on its own is also called making it the subject".

## 14. `B0-R0-C19`, `figures[0]` — the caption calls exact points "readings", and the left axis does not run to what the prose says

Caption: "The same eight readings drawn twice."

The eight points are not readings. They are computed from section 3(1) — five kilograms a person, a
household of one to eight — and this record's own `analogy_breaks_when` makes the distinction
load-bearing: "These eight points come from an Act, so they are exact. Points that come from
measuring something are not, and nothing in this section tells you which kind you are looking at."
The caption then tells the reader the opposite of what the section wants them to hold.

Second, the numbers. `illustration.body` says "Draw it once with the side axis running from 0 to 40
kilograms". `check/figures/draw.py`, `c5_two_scales`, sets the two tops to `max(ys) * 1.1` and
`max(ys) * 5`, so the panels run 0–44 and 0–200. The right panel matches the prose and the 40 ÷ 200
= 0.2 the text computes; the left does not. The alt text is accurate to the figure ("stops just
above the highest point") and so contradicts the prose rather than the drawing.

Third, a smaller thing: the caption and alt say "vertical axis" where every line of the section's
prose says "side axis".

**Fix.** Caption: "The same eight entitlements drawn twice." Change the prose to "running a little
above 40 kilograms", or set the left top to exactly `max(ys)` in `draw.py` — the prose is the
cheaper of the two to change. Replace "vertical axis" with "side axis" in both captions and both
alt texts.

`figures[1]` is correct in every particular and needs nothing: seven points, a run of three months,
a rise of sixty kilograms, a slope of twenty kilograms a month and an intercept at ten all match
the record's second table and the annotations `c5_slope_intercept` draws from it. Its alt text
carries all four numbers, so a reader who cannot see it can still follow the section.

## 15. `B0-R0-C16` and `B0-R0-C17`, `illustration.numbers` — each register is missing a factor the illustration multiplies by

`B0-R0-C16` registers the carbohydrate factor (4) and the fat factor (9). Its illustration also
uses the protein factor: "4 times 12 = 48". No entry, no quote, no citekey.

`B0-R0-C17` registers the protein factor (4) and the fat factor (9). Its illustration also uses the
carbohydrate factor, in the table ("60 … 240") and in the working ("4 times 15 = 60"). No entry.

§4 requires every number in an illustration to be listed in `illustration.numbers` with its unit
and citekey so the numbers register can audit it without re-reading prose. `B0-R0-C15` lists all
three and is the model.

**Fix.** Copy the missing entry across from `B0-R0-C15`, which already carries all three with their
quotes: `(D) Protein 4 kcal/g` into C2, `(A) Carbohydrates 4 kcal/g` into C3.

## 16. `B0-R0-C16`, `practice[9]` and `practice[10]` answers — two claims about the world presented as ordinary fact, with no citekey

- Level 7 answer: "45 kilograms is an ordinary mass for a person, so nothing about the answer looks
  alarming."
- Level 8 answer: "80 grams of carbohydrate in 100 grams of a food is a perfectly ordinary figure,
  so nothing about it looks out of place."

Both are assertions about real distributions, used to carry the argument for why a wrong answer
reads as plausible, and neither carries `refs`. Neither is declared made up. They are small, but
they are the class the audit is specifically counting, and they sit in the diagnostic band, where
the reader is being trained to say what looks reasonable and why.

**Fix.** Neither claim needs a source, because neither needs to be about the world. Rewrite them to
be about the arithmetic: "45 is the right order of magnitude for the quantity asked for, so nothing
about the answer looks alarming" and "the figure that came out is the same size as the other
figures on the panel, so nothing about it looks out of place."

## 17. `B0-R0-C17`, `simplified_explanation` — "substitution" arrives in a second sense with no bridge

`B0-R0-C15` teaches the word: "Substituting a number for a letter replaces that letter, everywhere
it appears, with the number. The expression then becomes arithmetic." C3 then uses the same word
for putting an *expression* in place of a letter, which does not leave arithmetic behind: "The first
is substitution. Rearrange one equation so that one letter stands alone, then put that into the
other equation."

This is the right name for the move and the right place to widen it, but the widening is silent.
The reader is holding a definition that says substituting produces arithmetic, and the first
substitution here produces `10 minus y minus y = 4`, which is not arithmetic. §10 rule 2 is about
keeping one set of words for one thing; the mirror case, one set of words quietly covering two
things, costs the same re-read.

**Fix.** One sentence before the move: "You have substituted a number for a letter. This is the same
move with an expression in place of the number, and what it leaves behind is algebra rather than
arithmetic."

---

## What was checked and found sound

- **Every practice answer recomputed.** All arithmetic is correct in all five records, including the
  two diagnostic-band prompts per section whose working is deliberately wrong and whose corrections
  check out. Defect 1 is not an arithmetic slip; it is a correctly computed answer to the wrong
  question, stated as though it were the whole answer.
- **The chain holds at its joints.** C2 opens "This section stands on the one before it, where a
  letter became a number you do not know yet"; C3 opens "The section before this one solved
  equations with one letter in them"; C5 opens "You now have a rule that turns an input into one
  output". All three satisfy §10 rule 5. C4's `analogy_breaks_when` reaches back to `B0-R0-C14` in
  that record's own words ("The index you met in the section on body-size units").
- **The label rule `E = 4c + 4p + 9f` is the same object in all three of C1, C2 and C3**, introduced
  in C1 and named as already met in each of the next two.
- **No BMI threshold anywhere**, and no language that implies one. The boundary holds across all
  four problems that touch the index.
- **Weight language.** Nothing in the five records breaches §9. The index problems describe a
  register and a measurement and never a person's conduct; no example turns on willpower.
- **Figure files.** Both C5 figures exist in `check/figures/` and are generated by
  `check/figures/draw.py` from the record's own `table` blocks, so the second figure's numbers
  cannot drift. The first figure's axis top is computed rather than read, which is how defect 14
  became possible.
