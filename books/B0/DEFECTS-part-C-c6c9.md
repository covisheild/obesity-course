# Book 0 · Part C · defect list for C6 to C9

Audit of `check/records/B0/B0-R0-C20.yml` (C6), `-C21.yml` (C7), `-C22.yml` (C8) and
`-C23.yml` (C9), against `books/B0/INVENTORY-part-C.md` (especially "Where C7 and C8 stop"),
`claude.md`, and `B0-R0-C19.yml` (C5) for the chain. Produced 23 September 2026. No record was
edited.

Quoted passages and prose arithmetic were already checked mechanically and are not re-checked
here. Everything below is mathematics, boundary, sourcing, chain, antecedents or figures.

**Headline.** Seventeen defects. Three are mathematics that is wrong as written; one of those sits
in a must-know point and is contradicted by the record's own exercise answer. The C7/C8 boundary
holds, with two notes. C9 is clean of invented physiological numbers, but carries one
unattributed physiological claim.

---

## 1. C7 · `must_know` (point 2) and `simplified_explanation` — "it can match the rate at no moment" is false

**The claim.** `must_know` point 2: "So it can match the rate at no moment inside the stretch."
`simplified_explanation`: "An average across the whole of it can match its steepness at no point
of it at all."

**What is wrong.** For any quantity that changes continuously and smoothly — every quantity in
this section and every quantity in the subject books — the average rate over an interval equals
the instantaneous rate at at least one moment strictly inside it. That is the mean value theorem,
and it is not a technicality: it is why the average is a *representative* of the interval at all.
The record states the opposite as a flat fact, in the one field designed to survive after the
section is forgotten.

The record already contradicts itself. The `interpretation` exercise answer says "Its steepness
passes through the average somewhere in the middle. At either end it sits nowhere near it." That
sentence is correct and it is what the point should have said.

The real lesson — which the `definition` field gets right — is not that the average matches
nowhere, but that it tells you nothing about *where* it matched, and can be far from the rate at
either end.

**Smallest fix.** In `must_know` point 2, replace the last sentence with: "So it can sit far from
the rate at both ends of the stretch, and it never tells you where inside the stretch it was
matched." Make the same substitution in `simplified_explanation`. This aligns both fields with
`definition.text` ("an average over an interval fixes nothing about where inside that interval the
change happened") and with the exercise answer.

## 2. C7 · `figures[0]` and `check/figures/draw.py` — the figure labels a chord as a tangent

**The claim.** `draw.py:302-308` computes `last = (ys[-1] - ys[-2]) / (xs[-1] - xs[-2])` — that is
(56.1 − 53.5) ÷ 1 = 2.6, the average rate over the fifth month — and draws a dashed straight line
through the final point with that slope, annotated "steepness at the end: 2.6 a month". The
`caption` reads "The rate at the end is the steepness of the curve where it finishes", and the
`alt` reads "A dashed line lies along the curve at its final point". So the drawing, the caption
and the alt text all present a chord slope as the tangent slope.

**What is wrong.** This is exactly the error the section's own level-8 practice problem exists to
catch: "A rise divided by a run between two points is the average rate over the interval between
them. The answer has labelled it as the rate at one of the ends." The curve is decelerating, so
the true steepness at month 5 is strictly less than 2.6 — the dashed line as drawn is too steep.
The one figure in the section demonstrates the defect the section teaches against.

**Smallest fix.** Relabel, do not redraw. Change the annotation in `draw.py` to "average over the
last month: 2.6 a month", and the caption to "The second line is the average across the final
month alone, which is the closest the table's readings can get to the rate at the end." Keep the
level-8 problem as it is.

## 3. C7 · `illustration.body` and `practice` (level 7, second) — the same conflation in prose

**The claim.** `illustration.body`: "Use the rate now instead, which is 2.6 a month." Level-7
answer: "Two point six a month. That is the rate now." The `critique` exercise answer: "The rate
now is the gain in the fourth year, which is 1.5 points a year."

**What is wrong.** 2.6 is the average over the fifth month — the slope of a chord one month wide.
It is not the rate now, and the section spends a level-8 problem saying so. Because the quantity
is decelerating, the rate now is below 2.6, so the projection "56.1 plus 5.2 = 61.3" is itself an
over-estimate by the section's own argument. Related: `illustration.body` says of 9.22 "It was
never 9.22", which is true of the five monthly block rates but false of the underlying quantity —
9.22 lies between the second month's 12 and the third month's 7.2.

**Smallest fix.** Write "the most recent month's rate" wherever the text now writes "the rate now",
and change "It was never 9.22" to "No single month ran at 9.22."

## 4. C6 · `simplified_explanation` and `retrieval_items` — the saturating test does not exclude unbounded growth

**The claim.** The hand test: "Do the differences keep shrinking while the values keep climbing
towards some level? Then it is saturating." `retrieval_items`: "Differences that shrink while the
values climb towards a level mean saturating."

**What is wrong.** Shrinking differences and climbing values are not enough. A curve can rise ever
more slowly forever with no ceiling at all. A logarithm is the counterexample, and it is the one
curve the reader has already met (C07). Ten times log10 of the input, read at steps 1 to 8, gives
10.00, 13.01, 14.77, 16.02, 16.99, 17.78, 18.45, 19.03 — differences 3.01, 1.76, 1.25, 0.97, 0.79,
0.67, 0.58, shrinking every step, values climbing every step, and no ceiling anywhere. A reader
running the stated test names it saturating and then goes looking for a ceiling that is not there.
The test as written also has "towards some level" inside it, which asks the reader to assume the
answer.

The illustration already uses the correct diagnostic — "Each step closes about the same share of
whatever distance is left to 60" — and so do the level-5 and level-10 answers, which divide each
difference by the one before it and get a constant 0.5. That rule appears in no definition, no
must-know point and no retrieval item.

**Smallest fix.** Add the third division the worked answers already perform. After "Do the
differences keep shrinking", add: "Now divide each difference by the one before it. If that ratio
holds at some number below one, the differences are being cut by a fixed share each time, they add
up to a finite amount, and there is a ceiling. Differences that shrink without holding a ratio may
be heading nowhere in particular." Mirror the addition in the retrieval item.

## 5. C8 · `illustration.body` — "halving the interval halves the error" is true only of this rate

**The claim.** "Halving the interval halved the error. Halving it again would halve it again."

**What is wrong.** The demonstration is correct — 50, then 45, against an exact 40 — but it is
correct *because the rate falls in a straight line*, which this one does and which the text does
not say is doing the work. For a rate that is not linear, halving the interval only halves the
error approximately, and only once the intervals are already small. For a rate that rises over
part of the span and falls over the rest, the two rectangle errors partly cancel and halving the
interval can change the total error by any factor at all, including increasing it. Stated
unqualified in the one worked passage on error, this becomes a rule the reader will apply to
curves it does not hold for.

**Smallest fix.** One clause: "Halving the interval halved the error, and it did so exactly
because this rate falls in a straight line. For a rate that bends, narrower intervals shrink the
error without halving it to order."

## 6. C8 · `simplified_explanation`, `definition.text`, `figures[0]` — "the rate line" has no antecedent

**The claim.** `simplified_explanation`: "So the area under a rate line, up to any time, is the
total accumulated up to that time." `illustration.body`: "The whole shaded area under the rate
line is 80 kilograms." `definition.text`: "The running total up to any time is the area under the
rate line."

**What is wrong.** No rate line is ever drawn. The reader is told to draw axes and then to draw
rectangles: "Over one interval, draw a rectangle... Stack the rectangles side by side." The phrase
"a rate line" arrives with nothing to refer back to, and it arrives carrying the section's central
idea. The figure does not supply it either — `draw.py:327` plots the step outline with
`linewidth=0`, so nothing is visible, and the `alt` text describes only rectangles. So the
sentence that names the whole concept points at an object the reader has neither drawn nor seen.

**Smallest fix.** One sentence before the rectangles, in `simplified_explanation`: "First plot the
rate itself against time and join the points. That is the rate line, and everything below it is
what you are about to measure." Then set the step outline in `draw.py` to a visible width so the
figure shows the line the caption names.

## 7. C8 · `definition.text` — the error is given in the wrong kind of unit

**The claim.** "Where the rate moved inside an interval, the rectangle over-counts or under-counts
by as much as the rate moved."

**What is wrong.** The error is an amount; the rate's movement is a rate. In the section's own
worked case the rate moves 5 kilograms a month across each one-month interval, and the error per
rectangle is 2.5 kilograms — not 5 of anything. The two quantities cannot be equated, and this is
the one section whose whole discipline is that a rate and an amount are different kinds of thing.
`definition.text` is the field held to technical exactness.

**Smallest fix.** "…over-counts or under-counts by at most the change in the rate multiplied by
the length of the interval."

## 8. C7 · `simplified_explanation` — "so short that it may as well be a point"

**The claim.** "It means a change in y divided by a change in x. The stretch it is taken over is so
short that it may as well be a point." Repeated in `retrieval_items`: "taken over a stretch so
short it may as well be a point."

**What is wrong.** A stretch of positive length is never a point, and the rate over a very short
stretch is not in general the rate at a point. The sentence sells the reader the infinitesimal
that mathematics spent two centuries removing, and it is the one description in the section a
mathematician would call false rather than merely loose. It is also the nearest the section comes
to the limit process the inventory rules out — which the preceding paragraph, "A shorter interval
gives you a closer answer… take it over a day around the same moment and you get much nearer to
the moment itself", already describes in words. Keeping the false gloss buys nothing the true one
does not.

**Smallest fix.** "The two letters d each mean 'a change in'. The whole symbol is the steepness at
one point, which is what you have just been reading off a curve." Drop "may as well be a point"
from both fields. This also pulls C7 further from the boundary rather than nearer it.

## 9. C9 · `analogy_breaks_when` and `practice` (level 10) — an unattributed physiological claim

**The claim.** `analogy_breaks_when`: "A body is not a store room in one way that matters. The two
flows in a person are not independent of each other, and neither is independent of the stock."
Level-10 answer: "In a person the two flows and the stock affect one another."

**What is wrong.** This is physiological compensation, asserted as fact, with no `refs` and no
`citekey`, in a record whose only reference is an OpenStax calculus anchor. `check/references/library.bib`
holds no physiological source at all, so nothing stands behind the sentence except whoever drafted
it. `claude.md` §3 names this exact claim as the one that is *not* derivable — "physiological
compensation was not deducible" — so it cannot ride on the concept being typed `derivable`.
C9 is the section S01 builds on directly, which is where the damage lands.

It is worth recording what C9 got right, because it is the harder half. The section refuses a
number for either flow, says so out loud ("This section gives you no figure for either flow and
you should not take one from here"), builds its level-10 problem on bare units, and makes the
teaching exercise end on "What not to offer: a figure for either flow." **No invented
physiological number is present anywhere in C9.** The defect is a qualitative claim, not a
quantitative one.

**Smallest fix.** Attribute it forward rather than asserting it: "A body is not a store room in one
way that matters, and the booklet on energy balance is where the evidence for it is set out: there
the two flows are not independent of each other, and neither is independent of the stock." Same
change in the level-10 answer.

## 10. C9 · `definition.text` — contradicts what C7 established about rates

**The claim.** "A flow is a rate that changes a stock, and it is measured over a stretch of time
rather than at a moment."

**What is wrong.** C7 spends its whole length establishing that a rate can be asked for at a
moment as well as over a stretch, and that the rate at a moment is a real quantity with a name
and a picture. C9 then tells the reader that a rate is measured over a stretch "rather than at a
moment". A reader who took C7 seriously has to stop and reconcile the two, which is the §10 defect
this Part was warned about: the chain breaks when a later section uses different words for
something the earlier one settled.

**Smallest fix.** "…and, like any rate, it is quoted over a stretch of time or at a moment. A
stock is measured at a moment by looking at it; a flow is measured by watching it for a while."

## 11. C6 · `illustration.body` and `must_know` (point 2) — "the flattest of the three at the start"

**The claim.** `illustration.body`: "An exponential is the flattest of the three at the start and
the steepest of the three at the end." `must_know` point 2: "An exponential curve is the flattest
of the three at the start, so calling a steep early rise exponential gets it backwards."

**What is wrong.** True of this table, not true in general. It depends entirely on how the three
curves have been scaled against each other. Start all three at 10 and let the exponential multiply
by 3 a step against a linear adding 10, and the exponential is the steepest from the first step.
What is always true is the second half: an exponential eventually passes any linear. Stated as a
general property in a must-know point, it will be applied to curves it is false of.

The correction the point is reaching for — exponential is a claim about the ratio, not about
steepness — is right and worth keeping.

**Smallest fix.** "An exponential rise can be the gentlest-looking of the three at the start, so a
steep early rise is no evidence for the word."

## 12. C8 · `figures[0].alt` — the alt text does not match the record's table

**The claim.** "Six rectangles of equal width and decreasing height standing on a horizontal axis
of months, each labelled with its rate. Together they form a descending staircase."

**What is wrong.** The record's table reads 20, 20, 15, 10, 10, 5. Two pairs are equal, so the
heights do not decrease and the staircase has two flat treads — which is visible in the figure and
is part of what makes it a real record rather than a tidy one. The alt text also says each
rectangle is "labelled with its rate" and then gives none of the six rates, so a reader who cannot
see the figure gets no numbers, cannot check the 80, and cannot follow the section from the alt
text alone.

**Smallest fix.** "Six rectangles of equal width standing on an axis of months, labelled 20, 20,
15, 10, 10 and 5 kilograms a month. The heights fall in two steps with a flat pair at each level.
The six areas add to 80 kilograms."

## 13. C7 · `figures[0].alt` and `caption` — no numbers in the alt, and a rate described as a line

**The claim.** `caption`: "The average rate across the whole span is the straight line joining the
first point to the last… The two numbers differ by more than three times." `alt`: no numbers at
all.

**What is wrong.** Two things. First, an average rate is the *slope* of that line, not the line —
and C5 spent a section establishing that distinction, in these words. Second, the caption refers
the reader to "the two numbers" and the alt text supplies neither, so the reader who cannot see
the figure cannot check the ratio the caption asserts. The two numbers are 9.22 and 2.6 (`draw.py`
computes both from the record's own table), and 9.22 ÷ 2.6 is 3.55, so "more than three times"
is right.

**Smallest fix.** Caption: "The average rate across the whole span is the *slope* of the straight
line joining the first point to the last, 9.22 a month." Alt: name both numbers and say which line
carries which.

## 14. C8 · `exercises[1].answer` — two unattributed claims about how depots behave

**The claim.** "Issue rates move with the season, with the month of the entitlement cycle, and
with whatever else the depot is doing." And: "A cycle that starts at the beginning of the month
makes the first week the busiest one there is."

**What is wrong.** Both are assertions about how the public distribution system actually runs,
stated flatly, with no `refs` and no `citekey`. The second is the stronger one — it names a cause
and a consequence about real depots, and the argument of the whole exercise leans on it.

**Smallest fix.** Turn both into the questions the exercise is teaching the reader to ask: "Ask
whether issue rates move with the season or with the month of the entitlement cycle, and get the
weekly figures that would show it." And: "Ask whether the first week of April is a typical week,
or whether the entitlement cycle makes it the busiest."

## 15. C6 · `must_know` (point 7) — "most rises called exponential in public are not"

**The claim.** "Most rises that are called exponential in public are not, and the honest sentence
is that it grew and here is by how much."

**What is wrong.** "Most" is a quantified claim about the world with nothing behind it. The move
the point teaches — ask for the values at equal times and check the ratio — stands without it.

**Smallest fix.** "A rise called exponential in public may well not be one, and the honest sentence
is that it grew and here is by how much." Same treatment for C7 `practice` level 9, "A list often
clears its easy cases first", which is the same kind of claim in the same kind of place.

## 16. C6 · `definition.text` — "increments grow" excludes the record's own decaying exponential

**The claim.** "A relationship is exponential when equal steps in the input multiply the output by
the same factor every time. Its increments grow in proportion to the output itself."

**What is wrong.** The first sentence is right and it is the definition. The second contradicts the
first for any factor below one: practice level 2 item D runs 100, 50, 25, 12.5, 6.25, is taught as
exponential, and its increments shrink rather than grow. The answer to that problem makes the
point explicitly — "Exponential describes the multiplying, not the direction" — so the definition
is out of step with the drill set.

**Smallest fix.** "Its increments are proportional to the output itself."

## 17. Smaller defects, each with its fix

- **C6 `figures[0].caption`** — "by the sixth step they are nowhere near each other". The table
  runs step 0 to step 5, so the sixth *row* is the fifth *step*. Write "by the last of the six
  readings".
- **C6 `illustration.body`** — "Now look at the first two rows of the table again, because that is
  where the trap is", followed immediately by a sentence about step five. The pointer names rows
  the argument does not use. Write "Now look at step one and step five".
- **C7 `exercises[1].answer`** — "It is falling, and it is falling by half a year at a time" reads
  twice before it parses. Write "It is falling, and it halves every year."
- **C8 `illustration.body`** — "One month's rate was used as though it held all year", of a table
  covering six months. Write "as though it held for all six".
- **C9 `must_know` (point 1)** — "Equal flows leave a stock exactly where equal-sized nothing would
  leave it" is a phrase the reader has to decode. Write "Two flows that match leave the stock
  exactly where no flows at all would leave it."
- **C9 `practice` (level 5)** — the answer calls 3.6 "about three and a half times over" and the
  next sentence says "more than three times"; make both "about three and a half". The prompt's "a
  tank holds 6,000 litres and holds the same 6,000 litres a day later" reads as the same water,
  which is the opposite of the section's point. Write "and holds 6,000 litres again a day later".
- **C8 `concept_deps`** — the `interpretation` answer sends the reader to "the section on
  converting units" (B0-R0-C10), which is not in `concept_deps`. Add it.

---

## The boundary: held, with two notes

**C7 does not teach limits or any rule of differentiation.** No derivative of anything is taken
anywhere in the record, and no rule is stated. The reader finishes able to say what a derivative is
for and unable to compute one, which is the inventory's stated test.

**C8 does not teach antiderivatives or any rule of integration.** Every total in the record is
built by multiplying a rate by a time and adding. The one exact answer — the 40 kilograms — is
reached by averaging a linearly falling rate and multiplying, not by integrating.

Two notes, neither a breach:

1. **The nearest approach is C7's "so short that it may as well be a point"** (defect 8 above),
   together with "A shorter interval gives you a closer answer… take it over a day around the same
   moment and you get much nearer to the moment itself." That pair is a limit process described in
   words without the word. It is within the inventory's permission to teach "how to read a rate off
   a curve by looking at its steepness", and the second sentence is defensible. The first is not,
   because it is false; fixing defect 8 also puts more air between the section and the line.
2. **Symbol naming runs past "once".** The inventory allows `dy/dx` and `∫` "beyond naming it once
   so the reader recognises it". `dy/dx` appears in C7's `definition`, in `simplified_explanation`,
   and in a `retrieval_item` question and answer; "derivative" also appears in the `teaching`
   exercise answer. `∫` appears in C8's `definition`, `simplified_explanation` and a
   `retrieval_item`. A retrieval item asks the reader to produce the thing from memory, which is
   more than recognising it on somebody else's page. No content crosses the line — nothing is
   computed with either symbol — but if the boundary is to mean what it says, the two retrieval
   items are the ones to drop.

---

## The chain

**C7 against C5.** Consistent. C5 establishes slope as "the change up, divided by the change
across", names rise and run, and says "a slope is a rate" with unit the y unit over the x unit. C7
opens "A slope is a rate. You met that in the section on graphs", and uses rise, run, slope and
steepness in C5's senses throughout. `chord` and `tangent` are new and are both defined at first
use. No synonym drift found.

**C8 against C7.** Consistent on rate, average rate and unit discipline. The one break is defect 6:
"the rate line" is C8's own term and C8 never introduces it.

**C9 against C7 and C8.** Consistent on totals — "which is the running total of the previous
section" — and on units. The one break is defect 10: C9's definition of a flow contradicts C7's
finding that a rate can be asked for at a moment.

## C9's central claim

**It lands, and it is demonstrated rather than asserted.** The inspection example gives a stock of
2,000 kilograms and a flow of 10,000 kilograms a month in each direction, shows the turnover
explicitly (10,000 ÷ 2,000 = 5, so five times the contents of the room passed through it in the
month), and then writes the balance line out so the reader watches the two flows cancel:
2,000 + 10,000 − 10,000 = 2,000. The three-month table then makes the stock move and return, so
the reader sees that the first and last rows alone would say nothing happened. The level-7,
level-9 and level-10 problems each set two cases that produce identical measurements and different
worlds. Every figure checks: 5 × 4 = 20; 20 × 500 = 10,000; the six-month store problem's 54,000
in and out, and its 8,500-a-month variant landing the July count at 1,000, a shortfall of under
six per cent of the flow emptying three quarters of the store; the tank's 15 × 1,440 = 21,600
litres and 3.6 turnovers.

The arithmetic in the central example is right and the example does the work the inventory asked
of it.
