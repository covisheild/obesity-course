# Book 0 · Part C — what the independent verification of the fix pass found

Two subagents audited Part C and two more applied the 34 defects they raised. Both fix agents
reported every defect closed and a clean build. This file records what checking that claim found,
because an agent's summary describes what it meant to do and not necessarily what it did.

The mechanical checks all held. `blocking 0`, warnings back to the 23 baseline, and a structural
diff of every record against its parent showed no `kind`, `bearing`, `level`, `citekey` or `quote`
path destroyed — the failure mode that silently wiped every must-know `kind` on an earlier run. The
two gates were re-proved live rather than assumed: a tampered quote blocked, and a tampered sum
blocked.

Seven things survived the fix pass and were fixed here.

## 1. `check/figures/draw.py`, `c7_chords` — the third chord was invisible

The new figure drew three averages, all ending at the last reading. Two of them start within one
month of each other and therefore lie almost on the curve, so the one-month chord could not be
seen at all and the two-month one barely read as straight. The caption promised three lines and
the page showed two.

This is not a drawing fault so much as the section's own point arriving as a problem: a shorter
span gives an average nearer the rate at a moment, which is exactly why its chord hugs the curve.
So the fix keeps the geometry and makes the lines separable another way — each chord is extended
a little past the last reading so the three fan out on the right, each starts at a marked square,
and the three labels go into a key whose text is coloured and whose line samples carry the dash
patterns. The first attempt put labels beside each line and they collided; the second used leader
lines and the leaders read as a fourth data line. The key is the third attempt and the right one.

**Found by rendering the figure and looking at it.** Nothing in the build could have caught it.

## 2. `B0-R0-C22`, `definition.text` — an error bound that fails on a rate that turns

The fix pass added a bound: the rectangle is wrong "by at most the change in the rate across that
interval multiplied by the length of the interval". For a rate that moves one way across the
interval that is correct. For a rate that rises and then falls inside the interval, the change
across it can be nil while the rectangle is badly wrong, and the bound claims an error of zero.

Rewritten to the quantity that always bounds it: the largest gap between the height used and the
rate at any moment inside the interval, multiplied by the length of the interval. The retrieval
item carrying the same sentence was rewritten with it.

## 3. `B0-R0-C18` — "domain" and "range" were cut rather than taught

Defect 12 of the C1–C5 list was correct that both words were asserted in `definition.text` and
built nowhere, and it offered two fixes: cut the sentence, or give the words a paragraph in
`simplified_explanation` and a practice problem. The fix pass took the cut.

The second option is taken here instead. A reader heading for epidemiology meets both words in
week one of any paper, and *range* collides with a different meaning in statistics — the largest
measurement minus the smallest — which is a trap worth one sentence. So: the definition sentence
is restored, `simplified_explanation` names both words in the register the book uses for naming
("two names, so you recognise them on somebody else's page"), the statistical collision is stated,
a level-4 problem asks for the domain and range of the entitlement rule and then asks what an
office has done wrong with an input of 4.5 people, and a retrieval item carries the collision.
Eight problems now, still inside the inventory's 6–8.

## 4. `B0-R0-C16`, `practice[5]` — the worked answer broke the section's own rule

The replacement level-6 problem guards the multiplication ("a packet does not weigh nothing") and
then divides both sides by a letter with no guard at all, two paragraphs after the section says
never to do that. One clause added.

## 5. `B0-R0-C23`, `practice[4]` — 3.6 called "about three and a half"

In a book that spends a Part A section on rounding, 3.6 does not get reported as three and a half.
Now "three point six times over", and the sentence below it says "more than three times its own
contents".

## 6. `check/build.py` — section headings were skipping the notation pass

`concept_md` builds its heading straight from the record's `name`, and `_prose` never touches it,
so B6 — whose title is "Body-size units: kg, m, cm and kg/m^2" — printed a raw caret in its
heading and again in the appendix. The heading now runs through `_notation`.

This is the same defect class as the one that produced `m^2` in B6's body text earlier, found the
same way: by rendering a page and reading it.

## 7. `check/build.py`, `_SUP` — a bracketed exponent left a live caret on the page

The pattern accepted a numeric exponent and a fraction in brackets, and nothing else. Part A writes
its exponent arithmetic in words:

    1,00,000 times 100 = 10^5 times 10^2 = 10^(5 plus 2) = 10^7

The first, second and fourth became superscripts. The third did not, so the line rendered with two
proper superscripts, a raw caret, and then a third superscript — the exact defect the whole
notation layer was built to prevent, sitting in Part A since Part A shipped. Fourteen places in the
book.

The exponent alternative now accepts a bracketed expression, and because pandoc will not set a
superscript containing an unescaped space, the spaces inside it are escaped before the substitution
is parked. Verified by stripping all tags from the rendered HTML and counting literal carets and
tildes in what is left: fourteen before, nought after.

**That check is worth keeping as a standing one.** It is three lines, it runs on the built HTML,
and it catches every failure of this layer at once rather than one section at a time.

## What was checked and held

- Every mathematical fix re-derived independently: C16's 59.4–60.4 kg interval, including that
  most of the kilogram comes from the height rather than from the index; C20's 0.6 ratio down the
  saturating column and the ceiling of 60 that follows from it; C22's halving table and its
  correct new scoping to a rate that falls in a straight line; C23's 21,600 litres and 3.6
  turnovers; C21's three chord slopes against the record's own table.
- C21's mean-value claim. It is stated without naming the theorem, hedged to a quantity that
  changes without jumping, and justified in one plain sentence that is the right justification.
  Its converse is not claimed anywhere, and C20's "where no such ratio holds" wording is
  epistemic rather than mathematical, which is the correct shape.
- The C7/C8 boundary. `dy/dx` appears once in teaching prose and `∫` once. No limit, no rule of
  differentiation, no antiderivative.
- No BMI threshold anywhere in Part C, and none in Parts A or B either.
- Part B's debt to C2 is discharged: the rearrangement that recovers a mass from an index and a
  height is C16's level-10 problem. The level-6 problem the fix pass replaced was recovering a
  *height*, which needs a square root C2 does not teach; replacing it was right.
- Practice counts now run 6, 8, 10, 11, 12, 13 and 14 across the book, against the uniform ten
  that started this.
- Figures regenerate byte-identically from the records, so no figure holds a second copy of a
  number.
