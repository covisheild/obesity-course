# Book 0 · Part E · defect list for E3 and E4

Audit of `check/records/B0/B0-R0-C33.yml` (E3, conservation of energy and a system with a
boundary, `derivable`, eight practice problems) and `check/records/B0/B0-R0-C34.yml` (E4, heat
and temperature, eight practice problems). Checked against `claude.md` (§§2, 3, 5, 7a, 7b, 8, 9,
10), `books/B0/READY-part-E.md`, `books/B0/INVENTORY-part-E.md`, `sources/INDEX.yml`, the source
files in `sources/`, and `check/records/B0/B0-R0-C23.yml` (Book 0 C9) for consistency. Produced
23 September 2026. **No record was edited.**

Every quote in both records was searched for in the file `sources/INDEX.yml` maps its citekey to.
All sixteen practice answers were recomputed line by line. The arithmetic checker's tolerance rule
was tested against the build's own code rather than taken from the comment above it.

**Headline. Nineteen defects: five serious, six medium, eight low.** The most serious is defect 1.
E3 says twice that Book 0 C9 refuses to join the weight balance to the energy balance, and C9 does
not refuse — C9 makes body weight a stock in kilograms whose two flows are food energy in and
energy spent, in kilojoules, three times over. The refusal E3 claims to inherit exists only in E3.

The good news first, because it is load-bearing. **Every quote in both records is in its source
file, at the locator given.** `build.py --check` reports zero blocking failures and the quote check
returns clean. **No kilocalories-per-kilogram-of-body figure appears anywhere in either record** —
E3 refuses one in five separate places and E4 never reaches for one. **All sixteen practice answers
are arithmetically correct**, every line of them, and both ladders climb and reach all four bands.
The four items the drafter flagged are settled at the end of this file; three hold, one does not.

---

## Serious

## 1. E3 · `simplified_explanation` and `illustration.analogy_breaks_when` — the refusal is attributed to C9, and C9 does not make it

**The claim, in two places.** `simplified_explanation`: "It is the balance line from the section on
stocks and flows, with energy as the stock. **That section said a body gains or loses weight only
by mass crossing its edge.** This says the same thing about energy and a boundary."
`analogy_breaks_when`: "**The section on stocks and flows ran the weight balance and the energy
balance separately and refused to join them**, and this section refuses in the same place."

**What C9 actually says.** `B0-R0-C23.yml` contains no second balance, no mass flow, and not one
occurrence of the word *mass* or the word *edge*. It runs one balance for a person, and that
balance is the join:

> A person's body weight is a stock. Food energy taken in is a flow into that stock. Energy spent
> is a flow out of it. Both are rates and both carry a time on the bottom, in the kilojoules or
> the kilocalories you met in the section on energy units. (`illustration.body`)

The same join is made twice more: in the `teaching` exercise answer — "Body weight is the level.
Food energy coming in and energy being spent are the tap and the drain" — and in a
`retrieval_items` answer: "weight is a stock and the energy taken in and the energy spent are
flows."

So C9 attaches kilojoule-per-day flows to a kilogram stock. That is precisely the conversion E3
says the ground floor refuses, and it is also a breach of C9's own `must_know` point 3 ("Never add
or subtract a stock and a flow"), in the harder direction: not adding a stock to a flow, but
declaring a flow in one unit to be the inflow of a stock in another.

**Why this is the worst one here.** E3's whole treatment of the joules-to-kilograms question is
built on inheriting a refusal. A reader who follows the pointer back finds C9 doing the thing E3
says it refused, and either concludes E3 is confused or — worse, and more likely — takes C9's
version, which silently commits to a kilocalories-per-kilogram figure nobody has stated. No build
check can see this: both records pass, and the earlier C9 audit
(`books/B0/DEFECTS-part-C-c6c9.md`) did not catch the unit mismatch either.

**Smallest fix, in E3 only.** Both sentences describe C9 rather than energy, so both can be cut
back to what C9 does carry. In `simplified_explanation`, replace "That section said a body gains
or loses weight only by mass crossing its edge" with "That section gave you the line; this section
gives you the rule that makes it true of energy." In `analogy_breaks_when`, replace "The section on
stocks and flows ran the weight balance and the energy balance separately and refused to join them,
and this section refuses in the same place" with "Nothing in this course has given you that figure,
and nothing in this section can produce one."

**And raise C9 separately.** E3 cannot be made consistent with C9 by editing E3 alone if C9 is left
as it stands, because C9 will still be teaching a kilogram stock with kilojoule flows two hundred
pages earlier. That belongs in `DEFECTS.md` against `B0-R0-C23`, not in this list, but it should
not be left unrecorded: C9's body-weight passage needs either a mass balance with mass flows, or
an explicit second balance in energy units, and the choice affects what E3 may say about it.

---

## 2. E3 · `illustration.body` — the search that "finds nothing" is contradicted by the source pack's own file

**The claim.** "Widen the search and the same thing happens. The first-law section of the same book
does not define it. **Neither do two sections of University Physics Volume 1.** Four pages that use
the word, and **not one of them says what the word names**."

**What the source says.** `sources/openstax_college_physics_2e.txt` carries two labelled blocks from
other OpenStax titles. They are not two sections of University Physics Volume 1. One is University
Physics **Volume 2**, section 3.1 Thermodynamic Systems, and it defines the word in full, in the
first sentence of the block:

> A thermodynamic system includes anything whose thermodynamic properties are of interest. It is
> embedded in its surroundings or environment; it can exchange heat with, and do work on, its
> environment through a boundary, which is the imagined wall that separates the system and the
> environment.

`sources/INDEX.yml` says so explicitly, and says why the block is there: "College Physics 2e
nowhere defines a system and its boundary. Nothing cites that block."

Two further legs of the claim cannot be checked from files at all: College Physics 2e §15.1 (the
first-law section) and University Physics Volume 1 §8.1, both named in the record's
`verified.note`, are not in the pack. Only UP V1 §8.3 is, and it does not define the word.

**Why it matters.** The illustration's turn — "A physics book can tell you about things in the
world. It cannot tell you where you decided to draw your line" — rests on four pages failing. One
of them does not fail, and it is in this repository, one file away from the record. A hostile
checker finds it in under a minute, and the reader who reproduces the search finds it too, which is
the outcome §4's "real material, real dead ends" is meant to survive.

**Smallest fix.** Narrow the claim to what is true and keep the point, which survives intact. Replace
the sentence with: "Widen the search and College Physics 2e still does not define it. The book that
does is University Physics Volume 2, in its thermodynamics chapter — section 3.1, Thermodynamic
Systems, which says a system is embedded in its environment and exchanges heat with it through a
boundary." The next paragraph of the record already draws the right conclusion from that — "It is
defined in chapters about setting up a measurement, not in chapters about stating the law" — so
nothing downstream has to change. Correct the `verified.note` on definition reference 1 to name
only what was opened.

---

## 3. E3 · `simplified_explanation`, derivation steps three and four — the derivation skips, and E3 is the Part's only `derivable` concept

`claude.md` §3: "derivable — build it. The reader should be able to reconstruct it from the floor.
**A derivation that skips is worse than no derivation.**" §2 rule 4: "Every algebraic move is either
taught in Book 0 or shown in full."

Worked through as a reader holding Book 0 A to D and nothing else, two steps skip.

**Step three.** The record shows the line before:

```
    the amount inside at the end, plus the amount outside at the end
    = the amount inside at the start, plus the amount outside at the start
```

and the line after:

```
    the change inside, plus the change outside = 0
```

with nothing between them except "This is the move from the section on rearranging an equation,
done twice. Take away 'the amount inside at the start', then take away 'the amount outside at the
start'. What is left on the left-hand side is two changes, because a change is an end value minus
a start value."

Doing what the reader is told to do produces a four-term left-hand side:

```
    the amount inside at the end, plus the amount outside at the end,
    minus the amount inside at the start, minus the amount outside at the start = 0
```

Getting from there to two changes needs the four terms **regrouped** into two pairs. That move is
not shown, and it is not taught anywhere in Book 0. C16, *Rearranging an equation*, teaches exactly
two things — do the same to both sides, and a side that is a sum is treated whole — and nothing
about reordering or bracketing the terms of a sum. C15, *Variables and algebra*, is not even in
E3's `concept_deps`. A reader with no remembered mathematics is shown a two-term line, told to
subtract twice, and shown a different two-term line.

**Step four, which is the larger skip.** The record writes:

> **Step four. Name where it went.** Energy that left the outside and arrived inside crossed the
> line inwards. Energy that went the other way crossed it outwards. There is no third possibility,
> because step one used up the whole world in two pieces.
>
> ```
>     the change inside = the total that crossed in, minus the total that crossed out
> ```

There is no working line between step three's result and this one. The missing link is the
statement that the outside's change is the total that crossed out minus the total that crossed in —

```
    the change outside = the total that crossed out, minus the total that crossed in
```

— which, put into step three's line, gives step four in one move. The prose gestures at it ("there
is no third possibility") but that sentence establishes that crossings are exhaustive, not the
subtraction. As written, step four is asserted, and it is the step the whole balance line rests on.
A reader rebuilding this tomorrow, as the record explicitly asks them to ("so that you could put it
together again tomorrow without this page"), stops here.

**A third, smaller one.** The last line — "the energy inside at the end = the energy inside at the
start, plus everything that crossed in, minus everything that crossed out" — is introduced with
"Write that out with the start value put back". That is adding the start value to both sides, which
C16 does teach, but the line is not shown either.

**Smallest fix.** Add two working lines, both inside step three and four, and one sentence.

1. In step three, insert the intermediate line between the two existing ones: `the amount inside at
   the end, minus the amount inside at the start, plus the amount outside at the end, minus the
   amount outside at the start = 0`, with the sentence "The four pieces can be written in any
   order, so put each end value next to its own start value."
2. In step four, insert `the change outside = the total that crossed out, minus the total that
   crossed in` before the existing line, with the sentence "Put that into step three and take the
   change inside over to its own side."
3. Add `B0-R0-C15` to `concept_deps`, and check whether C16 should carry the reordering move; if it
   should, that is a defect against C16, not against E3.

---

## 4. E4 · `illustration.body` — the white-roof worked example is wrong, and it is the record's showcase of its own method

**The claim.** "Try it on a white roof, which is the book's own example. Colour acts on radiation,
so the roof reflects sunlight that would otherwise be absorbed. **Conduction through the roof slab
is untouched, because the slab is the same slab. Convection under the ceiling is untouched too.** So
'a white roof keeps the house cooler' is a claim about one route in three. Whether it is enough
depends on how much of the heat was arriving that way."

**What is wrong.** Conduction through the slab is not untouched, and it is the route the heat
actually takes into the house. Sunlight is absorbed at the outer surface, raising its temperature;
heat then conducts down through the slab; the ceiling then warms the room by convection and
radiation. A white roof lowers the absorbed radiation, which lowers the outer surface temperature,
which lowers the temperature difference across the slab, which lowers the conducted heat. That is
the entire mechanism by which a white roof works. The record has confused *which route a control
acts on* with *which routes are affected by it*, and then drawn a conclusion from the confusion:
"a claim about one route in three" and "how much of the heat was arriving that way" both understate
the effect, because essentially all of it was arriving that way.

The record is not rescued by `analogy_breaks_when`'s "A control that works on one route can be
undone by the two it left alone" — that sentence is about a control failing, and here the control
works, through the two routes the worked example says it leaves alone.

**Why it matters more than an ordinary slip.** The white roof is the last thing in the illustration,
it is offered as the reader's first run of the three-routes method ("So here is what to do with your
hands..."), and the next sentence calls it "the whole method". A reader who copies it will apply the
method wrongly the first time they use it.

**Smallest fix.** Replace the two sentences with: "Colour acts on radiation, so the roof absorbs
less of the sunlight falling on it. That is the only route the colour touches. The other two are
downstream of it — a cooler slab conducts less heat down into the ceiling, and a cooler ceiling
warms the air under it less. So naming the route tells you where the control bites, not which
routes end up different." Then the closing question — "how much was coming that way?" — still works.

---

## 5. E4 · `practice` 10 answer — 893 J/°C is called "the instrument's own constant" and then, correctly, said not to be

**The claim.** The answer opens: "What to compute: the energy behind each rise, **using the
instrument's own constant**, and then the ratio of the two." Four paragraphs later, in its own list
of what the answer does not establish: "It does not account for everything that absorbed the energy.
**The 893 joules per degree is the bomb itself.** A bomb calorimeter sits in water, and the water
takes up energy too."

**What the source says.** The figure is verified: `sources/openstax_chemistry_2e.txt`, §5.2, the
bomb-calorimetry worked example — "the calorimeter contains 775 g of water, and **the bomb itself
has a heat capacity of 893 J/°C**." The source makes the distinction the answer's last paragraph
makes: 893 J/°C is the bomb, and the water is separate.

**What is wrong.** E4's own `definition` says "The calibration constant of a bomb calorimeter is
that calorimeter's heat capacity", and E2 (`B0-R0-C32`) teaches the energy equivalent as the number
that converts a rise into the energy the reaction released. On both of those, "the instrument's own
constant" is the whole assembly, water included. 893 J/°C is not that number. So the answer's first
line names the wrong object, and its fourth caveat then contradicts the first line without saying
that it is doing so. A reader who takes the opening at face value will multiply a rise by a bomb's
heat capacity and call the product the energy the food released, which is the error E2 spent a
section preventing.

**Smallest fix.** Two words in the opening line: "using the bomb's own heat capacity" instead of
"using the instrument's own constant". Then, at the end of the first paragraph, add: "Note what that
figure is and is not — it is the bomb, not the whole calorimeter."

---

## Medium

## 6. E4 · `illustration.body` — the three controls are said to "line up one to one" with the three routes, and the quoted sentence does not say that

**The claim.** Immediately after the block quote about choosing materials, controlling air movement
and choice of colour: "Three controls, and they line up one to one with the three routes. **Choosing
the material acts on conduction.** Stopping the air moving acts on convection. Choosing the colour
acts on radiation."

**What the source says.** §14.4: "We can control rates of heat transfer by choosing materials (such
as thick wool clothing for the winter), controlling air movement (such as the use of weather
stripping around doors), or by choice of color (such as a white roof to reflect summer sunlight)."
That is a list of three controls. It does not pair them with the three methods, and nothing on the
page does.

The pairing is also shakiest exactly where the record states it most flatly. Thick wool clothing —
the book's own example for "choosing materials" — works largely by holding still air in the fibres,
which suppresses convection as much as conduction. So the quote is cited for a mapping it does not
make, and the mapping is wrong for the example the quote gives.

**Smallest fix.** Replace "and they line up one to one with the three routes" with "and each of them
bites on a route you can name". Replace "Choosing the material acts on conduction" with "Choosing
the material acts on how easily heat gets through it — thick wool works by holding still air in the
fibres, which slows conduction and convection at once." The three-routes checklist that follows is
unaffected.

---

## 7. E3 · `exercises` 2 (critique) answer — "round the whole kitchen and nothing crossed at all" is contradicted by the flue two sentences later

**The claim.** "Redraw the line and the sentence changes. Put the boundary round the food and the
third crossed out of it. **Put the boundary round the whole kitchen and nothing crossed at all.** The
third is in the air, in the steel of the pans, in the walls, and **in whatever went up the flue**."

**What is wrong.** A flue is a hole in the kitchen boundary. If some of the energy went up it, it
crossed the kitchen boundary, so the kitchen is not a closed system and the change inside it is not
zero. The two sentences cannot both be true. This is the exact error the record's own level-8
practice problem is built to catch — a route through the wall that is easy to miss because it is not
a door — and it is here in a worked answer.

The illustration's kitchen gets this right, by stipulation: "The kitchen door and window are shut for
the two minutes", and `analogy_breaks_when` then says the seal holds only for a stated stretch of
time. The exercise answer drops both guards.

**Smallest fix.** Replace the sentence with: "Draw it round the whole kitchen except the flue and
almost nothing crossed; draw it round the kitchen and the flue is a hole in your line, so say how
much went up it."

---

## 8. E4 · `definition` and `simplified_explanation` — synonym drift from E2's "energy equivalent" to "calibration constant"

**The claim.** E4 uses "calibration constant" three times as though the reader already holds it:
`definition` — "The calibration constant of a bomb calorimeter is that calorimeter's heat capacity";
`simplified_explanation` — "A calorimeter has one. That is exactly what its calibration constant is.
It is also why a calorimeter's degrees can be trusted."

**What E2 taught.** `B0-R0-C32.yml` uses **energy equivalent** twelve times and makes it the term:
"the calorimeter's energy equivalent, in joules for each degree… Doing this is called calibrating
the machine." "Calibration constant" appears once, in passing, in a practice answer.

`claude.md` §10 rule 2: "A term is introduced once, where the reader first meets it, and afterwards
used in the same words. Synonym drift … costs the reader a re-read every time." E4's sentence "That
is exactly what its calibration constant is" asks the reader to recognise a term they were not given.

**Smallest fix.** Use E2's words and bridge once. In `simplified_explanation`: "A calorimeter has
one. It is exactly the energy equivalent you met in the last section — the joules that instrument
needs for one degree — and heat capacity is its proper name." In `definition`: "A bomb calorimeter's
energy equivalent is that calorimeter's heat capacity." E4 `practice` 10's prompt keeps "heat
capacity", which is the source's word and is correct there.

---

## 9. E4 · `simplified_explanation` and `illustration.body` — "the last section" is used three times to mean E2, and the last section is E3

**The claim.** `simplified_explanation` opens: "You have just spent a section watching a thermometer
go up and calling the rise a measurement of energy." Later: "One more word, because **the last
section** used it without naming it." `illustration.body` opens: "Start with the belief **the last
section** may have left you with."

**What is wrong.** In reading order E4 follows E3 (conservation of energy and a boundary), not E2
(the calorimeter). E3 has no thermometer in it. The record itself gets it right once — `practice` 9's
answer says "The balance from **the previous section** says the numbers must add up across the
boundary", which is E3 — so the same phrase points at two different sections inside one record.

`claude.md` §10 rule 5: "A section that stands on the previous one says so in its first sentence, in
ordinary words." E4 does stand on E2, and the ordering was a known constraint — `INVENTORY-part-E.md`
sets it out at length — so the fix is to say which section, not to pretend it is adjacent.

**Smallest fix.** Name it. `simplified_explanation` first sentence: "Two sections back you watched a
thermometer go up and called the rise a measurement of energy." Later: "because the section on the
calorimeter used it without naming it." `illustration.body`: "Start with the belief the calorimeter
section may have left you with."

---

## 10. E4 · `illustration.analogy_breaks_when` — the cause given for the 4186/4184 gap is not what either source says

**The claim.** "College Physics 2e Table 14.1 gives 4186 joules per kilogram per degree Celsius.
Chemistry 2e section 5.1 gives 4.184 joules per gram per degree Celsius, which is 4184 joules per
kilogram per degree. The gap is under one part in two thousand and **comes from the temperature at
which the measurement is made.**"

**What the sources say.** The arithmetic is right — 4186 − 4184 = 2, and 2 ÷ 4186 is one part in
2,093, so "under one part in two thousand" holds. The cause is not in either source. Chemistry §5.1
gives a different origin for 4.184 outright: "A calorie is the amount of energy required to raise
one gram of water by 1 degree C… **To standardize its definition, 1 calorie has been set to equal
4.184 joules.**" That is a defined conversion, not a measurement at a different temperature. College
Physics' 4186 is tied to a temperature — Table 14.1 labels the row "Water (15.0 °C)" — but the pair
of figures differs because one book quotes a measured value at 15 °C and the other quotes the
standardised thermochemical calorie, and no source in the pack states that comparison.

`claude.md` §7b: never write a claim from what the model knows and attach it to sourced material.
The sentence sits inside a paragraph that is otherwise carefully cited.

**Smallest fix.** Delete the causal clause and stop at the size of the gap: "The gap is under one
part in two thousand, and neither book explains the other's figure. Use one book's figure all the
way through a calculation, and say which one you used."

---

## 11. E4 · `practice` 9 answer — uses College Physics' 4186 and then 4,184 joules per kilocalorie in the same calculation, against the record's own rule

**The claim.** The answer computes 4 × 4186 × 32 = 535,808 joules, then: "Now put it in the unit food
labels use. **One kilocalorie is 4,184 joules**, from the section on energy units."

**What is wrong.** Both numbers are correct and traceable — 4186 J/(kg·°C) is College Physics Table
14.1, and 4,184 J per kilocalorie is the exact calorie of C12 and NIST — and they are different
physical quantities, so this is not literally a mixture of two specific heats. But it reads as one,
and it breaks the instruction this record gives three fields earlier: "**Use one book's figure all
the way through a calculation, and say which one you used.**" A reader who has just been told the two
books disagree about water by two joules, and then watches an answer use 4186 and 4184 in the same
sum without comment, has to stop and work out whether that is the disagreement being ignored.

**Smallest fix, and it is cleaner arithmetic too.** Table 14.1's second column gives water as 1.000
kcal/(kg·°C), which is College Physics' own kilocalorie. Then 4 × 1.000 × 32 = 128 kilocalories
exactly, from one book, in one line, and the bracketing against 4,184 is not needed. If the joule
route is kept, add one sentence: "The 4,184 here is the calorie's definition, not water's specific
heat — the two are different quantities and they are not the disagreement described above."

---

## Low

## 12. E4 · `practice` 6 answer — "starts cooling faster" is a rate claim this section says it cannot make

**The claim.** "Every joule that goes into warming the tumbler came out of the chai, so the glass
tumbler takes about 1.86 times as much energy out of it. **The chai in the glass starts cooling
faster for that reason alone.**"

**What is wrong.** The calculation is about a total quantity of energy, not a rate. How fast the chai
cools at the start depends on how fast heat conducts into the wall, which this section gives no way
to compute. The record says so twice — in the same answer's closing paragraph ("How fast the chai
then goes on cooling depends on the routes out of the tumbler") and in `analogy_breaks_when` ("This
section gives no rates").

**Smallest fix.** "The chai in the glass ends up cooler once both tumblers have warmed, for that
reason alone."

---

## 13. E3 · `concept_deps` — negative numbers are used in four answers and never pointed at

`practice` 1 produces −160, `practice` 3 produces −900,000 and −60,000, and the illustration produces
−7,000, all as reader-facing results with the sign carrying meaning. Negative numbers are taught in
`B0-R0-C01`. E3's `concept_deps` are C04, C12, C16 and C23; C01 is not among them, and no field in
the record tells the reader where they met the sign. E4 does this properly — "you have already met
negative numbers in the section on counting" — and lists C01.

**Smallest fix.** Add `B0-R0-C01` to `concept_deps`, and one clause at the first negative answer in
`practice` 1: "It is negative, in the way the section on counting showed you."

---

## 14. E3 · `illustration.body` summary table — the third row's label leaves out the two things that make its answer right

The boundary is set up as "**Line three, round the burner, the unburnt gas, the pan and the water.**"
The table then labels the row "the burner and the pan". The gas is what carries the 60,000 joules
that start inside, and the water is what holds 42,000 of them at the end; without both, −7,000 looks
arbitrary. A reader checking the table against the working has to go back.

**Smallest fix.** `the burner, the gas, the pan and the water   minus 7,000 joules`.

---

## 15. E4 · `practice` 7 answer — cites a section that is not in `concept_deps`

"Two answers three orders of magnitude apart is the kind of gap **the section on orders of magnitude**
exists to make visible." That is `B0-R0-C08`. E4's `concept_deps` are C01, C09, C10, C12, C15, C16
and C32. C08 is not listed, so the `ground_floor_deps` and dependency reports do not see it.

**Smallest fix.** Add `B0-R0-C08` to `concept_deps`.

---

## 16. E3 · `practice` 3 prompt — "all three figures are made up" and only two figures are given

The prompt gives 900,000 joules released and 840,000 joules into the air and walls, then says "The
lamp, the room and **all three figures** are made up for this problem." The third figure, 60,000
joules of light, is what the reader is about to compute in part one. Telling them there are three
gives away that the answer is a third number before they have found it, and it miscounts what was
stipulated.

**Smallest fix.** "The lamp, the room and both figures are made up for this problem."

---

## 17. E3 · `must_know` point 5 — the sentence's subject is the section

"**This section gives you no way** to turn joules into kilograms of a body. That is a limit of the
tool, not a gap to be filled from somewhere handy."

The point passes the admission test — it changes what the reader refuses, and the rest of it is
excellent. But `claude.md` §5 warns that "a sentence whose subject is *this section* almost never
passes it", and a must-know point is the field meant to survive after the section is forgotten, at
which time "this section" names nothing. The point is tagged `trap` rather than `boundary`, so the
hard rule about boundary points does not bite; this is the soft version of the same problem.

**Smallest fix.** "Nothing turns joules into kilograms of a body. That is a limit of the tool, not a
gap to be filled from somewhere handy."

---

## 18. E4 · `must_know` point 4 — a `number` point carrying two figures

"Water needs 4186 joules for each kilogram and each degree Celsius, at 15.0 °C. Iron and steel need
452." `claude.md` §5: "`number` points carry **one** figure with its unit and source, not a list."

This is the softest item in the list, because the two figures are a comparison and the point says so
("Carry that one pair of numbers"). Recorded because the rule is explicit and because the point's
work is done by the ratio, which is a third figure again.

**Smallest fix.** Either accept it and note the exception, or lead on the ratio: "Water needs more
than nine times the energy that iron or steel needs for the same rise in the same mass — 4186 joules
per kilogram per degree Celsius at 15.0 °C against 452."

---

## 19. `books/B0/READY-part-E.md` · the E4 gate line does not list OpenStax Chemistry 2e §5.1

**The gate line as it stands.** "E4 — heat against temperature, specific heat, the three ways heat
moves | OpenStax College Physics 2e, §§14.1, 14.2, 14.4 | textbook | `openstax_college_physics_2e.txt`
| **yes**".

**What E4 actually needs.** Two of E4's eleven definition references are to OpenStax Chemistry 2e
§5.1 — the definition of heat capacity, and the sentence fixing the sign of q. The heat-capacity one
is not optional: College Physics 2e does not define heat capacity at all (see the verdicts below), so
E4's third definitional paragraph has no other source. `illustration.numbers` carries a fifth entry
citing Chemistry 2e as well.

The file is in the pack, because E2's gate line pulls in Chemistry §§5.1, 5.2 and 5.3, so nothing
blocked and nothing was missed at draft time. But the gate is the artefact that says which source
each concept rests on, and for E4 it is now wrong. If E2 were ever rescoped, E4's line would still
say yes.

**Smallest fix.** Add a row: "E4 — heat capacity, and the sign of a heat quantity | OpenStax
Chemistry 2e, §5.1 | textbook | `openstax_chemistry_2e.txt` | **yes**, already held for E2". Add it
to the "Four things found by opening the sources" list as a fifth item, since it is exactly that
kind of finding.

---

# What was checked and held

## Every quote, against its source

**All eighteen quotes are in their files, at their locators, and every one of them supports the
claim it is attached to.** Six definition references and one `illustration.numbers` quote in E3;
twelve definition references and five `illustration.numbers` quotes in E4. `build.py`'s
`check_quotes` returns clean, and each was also read in context to see whether the surrounding
sentences say what the record says they say. Spot notes:

- E3 definition reference 1 (`§ 7.6`, the law) — the note's central observation is right: §7.6 states
  the law, refers to "the system of interest", and nowhere says what a system is. Verified against
  the transcribed block.
- E3 definition reference 5 (`§ 5.2 Calorimetry`) — the note's reading of "requires the definition of
  a system" is exactly what the sentence says, and the record's whole section turns on that word
  correctly.
- E4 definition reference 5 (`§ 5.1`, heat capacity) — matches character for character, and the
  note's claim about the following paragraph ("proportional to the amount of the substance") is
  verified.
- E4 definition reference 9 (`§ 14.4`) — the note's claim about §§14.5, 14.6 and 14.7 is verified
  against those blocks, including that §14.7 contains no "Radiation is…" sentence.
- E4's convection claims about blood flow to the skin are supported by §14.6 verbatim, and
  `analogy_breaks_when`'s claim that sweating is mentioned there but not treated as a fourth method
  is accurate.

**Every number stands on a quote that states it.** E3's one figure is the joule, whose quote says
"One joule… would lift a small 100-gram apple a distance of about 1 meter" — 1, 100 and 1 all
stated. E4's five are 4186, 840 and 452 (each quoted from its own row of Table 14.1), 3 (quoted as
"only three methods", stated in words) and 4.184 (quoted from the sentence that states it twice).
**No figure in either record is counted or worked out from a passage rather than stated in it**, so
no `derived` declaration is owed.

One structural note while this is fresh: **`schema/concept.schema.json` has no `derived` field**, and
`illustration.numbers` is `additionalProperties: false`. A future record that does owe one cannot
carry it without a schema change. Separately, the `illustrations` (plural) branch of the schema
defines `numbers` items **without a `quote` property at all**, so a record using multiple
illustrations can carry figures the quote check cannot see. Neither bites here — both records use the
singular `illustration` — but both are worth fixing before a record needs them.

## All sixteen practice answers, recomputed

Every line of every answer was evaluated independently, not read. **All sixteen are correct.** So is
every working block in both illustrations, both simplified explanations and all six exercise answers.

E3: 1,200 + 450 = 1,650 and − 610 = 1,040 with a net of −160; the four table rows at 1,100, 150, 450
and 900; 900,000 − 840,000 = 60,000 with boundary changes of −900,000, −60,000 and 0; 5,000,000 −
4,100,000 = 900,000 at 18 per cent, checked forwards; 60,000 − 42,000 = 18,000; 0 + 300,000 − 0 =
300,000; 1,000 + 7,600 = 8,600 and 9,000 − 8,600 = 400.

E4: 2 × 500 × 30 = 30,000 and both reversals; 100 − 28 = 72, 2 × 4,186 = 8,372, × 72 = 602,784,
1.2 × 452 = 542.4, × 72 = 39,052.8, total 641,836.8, and the "about fifteen times" ratio (15.4);
0.18 × 840 = 151.2, × 55 = 8,316, 0.18 × 452 = 81.36, × 55 = 4,474.8, ratio 1.8584 and the
multiply-back 452 × 1.858 = 839.816; 500 ÷ 1,000 = 0.5 and 0.5 × 4,186 × 50 = 104,650, with the
"three orders of magnitude" claim exactly right; 39.3 − 30.0 = 9.3 giving 4,203.6 against 4,186, a
gap of 17.6 which is 0.42 per cent; 37 − 5 = 32, 4 × 4,186 = 16,744, × 32 = 535,808, 4,184 × 128 =
535,552, short by 256; 893 × 4.2 = 3,750.6, 893 × 2.1 = 1,875.3, ratio exactly 2.

The illustrations' figures also check: 42,000 + 11,000 + 7,000 = 60,000 and the four boundary
answers; 4,186 ÷ 452 = 9.2611 so "9.26" and "a little over nine" are right, 452 × 9 = 4,068 and
452 × 10 = 4,520 bracket it correctly, 4,520 − 4,186 = 334 and 334 ÷ 4,186 = 7.98 per cent so "about
eight per cent" holds; 30 − 95 = −65, 0.2 × 4,186 = 837.2, × −65 = −54,418.

## Both ladders

**E3: levels 1, 2, 4, 5, 7, 8, 9, 10.** Climbs, and reaches all four bands — mechanical (1, 2),
applied (4, 5), diagnostic (7, 8), transfer (9, 10). Eight is inside the three-to-eighteen range and
matches `INVENTORY-part-E.md`'s stated count.

**E4: levels 1, 2, 4, 6, 7, 8, 9, 10.** Same, all four bands, eight problems.

## E3's variety — the one specifically asked about

**It is real.** Six of the eight problems turn on where the line is drawn, and they are genuinely
different lines, not the same line with different digits:

- Level 4 (kerosene lamp) sets **three** boundaries over one event — round the fuel, round the room's
  contents with the window as a hole, round the room plus everything the light reaches — and gets
  −900,000, −60,000 and 0. This is the illustration's kitchen move, done on a different event, with
  the sign flipped.
- Level 5 (solar heater) runs a **single** boundary **backwards**, which is §7a's "reverse the
  direction at least once".
- Level 7 diagnoses **two numbers measured round two different lines** and subtracted as though they
  were one.
- Level 8 diagnoses **a route through a boundary that is not a door** — a mains cable.
- Level 9 draws the line **round a person** and enumerates four crossings.
- Level 10 sets **the food sample's line against the person's line** and shows the answer is a
  quantity nobody has.

Levels 1 and 2 are bare-number and boundary-free, which is what §7a's mechanical band requires
("no context, no unit, nothing to interpret"). So the set is not eight boundaries, but it is six, and
the two that are not are the two that are not supposed to be.

## The kilocalories-per-kilogram refusal

**Held, and thoroughly.** A search of both records for any per-kilogram energy figure for a body
finds none. E3 refuses one in five places — `simplified_explanation`, `analogy_breaks_when`,
`must_know` point 5, the `teaching` exercise's "What not to offer", and a `retrieval_items` answer —
and the transfer problems at levels 9 and 10 both close on it. E4 contains no such figure and its
`must_know` point 6 forbids the adjacent error ("never read a patient's temperature as a statement
about energy gained or lost"). The 128 kilocalories in E4's level-9 answer is the energy to warm four
litres of water, which is a different quantity and is labelled as one. **What fails is the
attribution to C9, defect 1, not the refusal itself.**

## §9, and the admission test

**No example turns on willpower and no moral vocabulary survives.** Searched for *willpower, cheat,
indulge, guilt, bad food, discipline, lazy, lapse, shed, burn off, before and after, obese person,
the obese* — nothing in either record. E4's level-9 gym poster is the one place the pull exists, and
the answer handles it as arithmetic with a ceiling on the effect, closing with "it stops the claim
being either dismissed or believed without a figure". E3's level-10 meeting exchange is neutral
throughout, and its `teaching` exercise refuses the physics-to-weight step on evidential grounds
rather than exhortative ones.

**Every must-know point passes the admission test.** Sixteen points across the two records, each one
changing something the reader would do, say, accept or refuse. Both `boundary` points name a limit of
the technique, not the scope of the section: E3's point 4 ("no ledger has ever explained a purchase")
and E4's point 5 ("It breaks at every boiling point, every melting point and every chemical
reaction"). Both records carry a `misconception` and a `trap`. Both sit at eight points, under the
soft cap of nine. Two soft items are recorded above as defects 17 and 18; one more is taste rather
than defect — E3's point 3 is tagged `bearing: clinical` and reads methodological.

## Currency, §9's other half, and the review clocks

**Nothing in either record carries a date or a cut-point that will go stale on a calendar.** Every
figure is a physical constant or an invented illustrative number declared as invented. The review
clocks are right: E3 `derivable`/`long`/2031-09-23 and E4 `empirical`/`medium`/2029-09-23, both
matching the specification §4 table.

**One item to re-check on an event rather than a date.** Both records' locators are OpenStax 2e
section numbers, and E4's three core figures are one row each of Table 14.1. A third edition would
renumber the sections and could revise the table. That is an edition event, not a five-year clock,
and it is worth naming in `review.trigger` alongside the date the way §4 names event triggers for
institutional content. Recorded here rather than as a defect because §4 does not currently ask for it
on a textbook anchor.

**One judgement call, recorded because Part E is where this line is first tested.** E4 is `empirical`
resting on `textbook` anchors, and §4 says "a claim with a number attached to it is not settled
science… a measured rate still needs `primary` or `systematic_review`". A specific heat is a measured
quantity, and the record itself says so ("Specific heat is not truly a constant. The book says it
varies with temperature"). It is also a physical constant of a material, not an effect size, a risk,
a dose-response or a prevalence — which is what §4's list is aimed at. **The textbook anchor is
right here**, and the reason is worth writing down for the next author: the test is whether somebody
would have to have run a study on people to get the number, not whether the number came from a
measurement. Almost every number in physics came from a measurement.

---

# The four items the drafter flagged

**1. Table 14.1 against the body text of §14.2 — E4 gets it right and does not overstate it.**
The body text says "the specific heat of water is five times that of glass and ten times that of
iron"; the table gives 4186, 840 and 452, so the two ratios are 4.98 and 9.26. E4 works the second
one out in the open, in the reader's hands: 452 × 9 = 4,068, 452 × 10 = 4,520, so the rise lands
between nine and ten; then 4,520 − 4,186 = 334, "about eight per cent of water's figure" (7.98 per
cent — correct), "the true ratio is a little over nine" (9.26 — correct). Every figure checks. It
then closes with "The sentence and the table are not in conflict; the sentence rounded", which is the
opposite of overstating — if anything it is generous, since rounding 9.26 to "ten" is a one-figure
rounding while the glass comparison it sits beside is accurate to 0.3 per cent. **No defect.** One
optional improvement: E4 never checks the glass ratio, and doing so (4,186 ÷ 840 ≈ 5.0) would show
the reader that the book rounded hard in one place and barely at all in the other, which is a better
lesson about round comparison figures than the one currently drawn.

**2. The two books' different specific heats for water — handled, and no calculation mixes them.**
`analogy_breaks_when` names both figures, converts 4.184 J/(g·°C) to 4184 J/(kg·°C) correctly, sizes
the gap correctly at under one part in two thousand, and gives the right instruction: use one book's
figure all the way through and say which. Every specific-heat calculation in the record uses 4186;
4.184 appears only in `illustration.numbers`, declared there as quoted "only to name the disagreement
with Table 14.1", and in the paragraph that names it. **No specific heat is mixed.** Two smaller
things came out of checking it, both listed above: the stated *cause* of the gap is not in either
source (defect 10), and the level-9 answer uses 4,184 joules per kilocalorie alongside 4186, which is
a different quantity but reads like the disagreement being ignored (defect 11).

**3. Heat capacity is not defined in College Physics 2e — verified, and the substitution is right.**
The source file records the check itself, under a `NOT OBTAINED VERBATIM` heading: "The phrase 'heat
capacity' occurs on section 14.2 exactly twice: in the section title ('Temperature Change and Heat
Capacity') and in a lab instruction ('To study differences in heat capacity:'). The section's body
text defines only specific heat… There is no sentence in the section defining heat capacity itself."
E4 takes the definition from OpenStax Chemistry 2e §5.1, quotes it exactly, and says so in the
reference note. **Correct, and correctly declared.** And the drafter is right that
`READY-part-E.md`'s E4 gate line does not mention Chemistry §5.1 — **that is defect 19 above.**

**4. 893 J/°C in E4 practice 10 — verified by hand, and correct.** `sources/openstax_chemistry_2e.txt`
carries the OpenStax Chemistry 2e §5.2 worked example: "When 3.12 g of glucose, C6H12O6, is burned in
a bomb calorimeter, the temperature of the calorimeter increases from 23.8 °C to 35.6 °C. The
calorimeter contains 775 g of water, and **the bomb itself has a heat capacity of 893 J/°C.**" The
figure, the unit and the citekey all check. Two notes: the passage is in §5.2, and E4's only Chemistry
references are to §5.1, so the record carries no locator anywhere for 893 — a practice problem's `refs`
list has no `locator` field, so the audit trail for this figure is this file. And the answer's opening
line mislabels what 893 is (**defect 5**), which its own fourth caveat then corrects.

---

# The arithmetic checker's tolerance — the claim, tested

**The drafter's claim holds in both named cases, and the mechanism is not what the drafter (or
`build.py`'s own comment, or `claude.md` §7a) says it is. The difference matters, and the next
author will hit it.**

Tested by running `build.check_arithmetic`'s own helpers over a set of equations:

```
BLOCK  4186 divided by 452 = 9.26           places=0  tol=9.26e-09  diff=1.06e-03
pass   17 divided by 7 = 2.428571429        places=0  tol=2.43e-09  diff=4.29e-10
BLOCK  17 divided by 7 = 2.4285714          places=0  tol=2.43e-09  diff=2.86e-08
pass   8316 divided by 4474.8 = 1.858       places=1  tol=1.0e-01   diff=4.07e-04
pass   452 times 1.858 = 839.816            places=3  tol=1.0e-03   diff=0
```

**What the code actually does.** `check_arithmetic` sets `places = min(_decimals_shown(p) for p in
sides)` — the minimum number of decimal places across **both** sides — and then
`tol = max(10 ** -places, abs(vals[0]) * 1e-9) if places else abs(vals[0]) * 1e-9`. Three consequences
the comment above it does not mention:

1. **When either side is written without a decimal point, `places` is 0 and the tolerance collapses
   to a relative 1e-9 — effectively exact.** `4186 divided by 452` is integers, so the right-hand
   side's two decimals buy nothing. That is why `= 9.26` blocks. The block is correct, but not for
   the stated reason.
2. **`17 divided by 7 = 2.428571429` passes only because nine decimals happens to land inside 1e-9
   relative.** Write eight — `= 2.4285714` — and the same division blocks. So §7a's "tolerance is set
   from the digits the text itself shows, so `17 divided by 7 = 2.428571429` passes **and does not
   have to be written to full precision to do so**" is wrong in the general case. It does have to be
   written to roughly ten significant figures, which is full precision for practical purposes. The
   working rule for an author is: **an inexact division with integers on the left may not be written
   as an equation at all** unless you are willing to print ten digits.
3. **The reverse failure is worse and nobody has noticed it.** If the left side carries a decimal,
   `places` becomes that count and the tolerance becomes `10 ** -places` **absolute**, which on a
   small quotient is enormous. E4 `practice` 6 contains `8316 divided by 4474.8 = 1.858`. `places` is
   1, so the tolerance is 0.1 — a five per cent band on an answer of 1.86. That line would pass with
   `= 1.9`, and it would pass with `= 1.95`. **On that line the checker is not checking anything.**

**So the drafter's second claim — that every inexact division in E4 was rewritten as bracketing or a
multiply-back check — is false.** The illustration does it properly: 4186 ÷ 452 is never written as an
equation, the value 9.26 is given in prose ("A calculator puts it at 9.26 degrees Celsius"), and the
bracketing 452 × 9 = 4,068 and 452 × 10 = 4,520 does the work. `practice` 6 does not: it writes the
inexact division out, and then adds the multiply-back check (452 × 1.858 = 839.816) on top. It passes
the build only through consequence 3, not through the discipline the drafter describes. It is not a
defect — the answer is right to three decimals and the multiply-back is genuinely there — but the
record should not be cited as evidence that the discipline was applied uniformly.

**What to record for the next author, in `claude.md` §7a.** Three lines:

- Tolerance comes from the **minimum** decimals across both sides, not from the answer's precision.
- An inexact division written with integer inputs is compared exactly. Bracket it, or multiply back,
  or put the value in prose. Do not print six or eight decimals and expect it to pass.
- A decimal on the **left** loosens the tolerance to `10^-places` absolute, which on a small quotient
  can be a several-per-cent band. Where that happens the arithmetic check is not protecting the line,
  and a multiply-back check is the only thing that is. Consider changing the tolerance to
  `max(10 ** -places, abs(v) * 1e-9)` computed from the **right-hand side's** decimals, or to a
  relative band, so that the check is neither exact-by-accident nor blind-by-accident.

---

# Out of scope for this fix: a defect against `B0-R0-C23`, for whoever owns Part C

Recorded here by the E3/E4 fix pass on 23 September 2026 and **not acted on**. `B0-R0-C23`,
*Stocks and flows*, is the ninth section of Part C and belongs to another Part and another chat.
No edit was made to it.

**What was checked.** The file was opened and read in full. It contains no occurrence of the word
*mass* and none of the word *edge*. It runs one balance, not two. In three separate places it
makes body weight a stock in kilograms whose two flows are energy:

- `illustration.body` — "A person's body weight is a stock. Food energy taken in is a flow into
  that stock. Energy spent is a flow out of it. Both are rates and both carry a time on the bottom,
  in the kilojoules or the kilocalories you met in the section on energy units."
- the `teaching` exercise answer — "Body weight is the level. Food energy coming in and energy
  being spent are the tap and the drain."
- a `retrieval_items` answer — "weight is a stock and the energy taken in and the energy spent are
  flows."

So a stock in kilograms is given flows in kilojoules per day. That is the defect. It is also a
breach of C23's own `must_know` point 3, "Never add or subtract a stock and a flow", in the harder
direction: not adding a stock to a flow, but declaring a flow in one unit to be the inflow of a
stock in another. Nothing in the build can see it, and the C23 audit
(`books/B0/DEFECTS-part-C-c6c9.md`) did not catch it either.

**What the owner has to choose between.** Either a mass balance for body weight, with mass flows
in kilograms, or an explicit second balance run in energy units and kept visibly separate from the
weight one. The choice is not cosmetic: it decides what any later section may say about C23.

**What E3 no longer depends on.** E3 previously claimed to inherit from C23 a refusal to join the
weight balance to the energy balance. C23 makes no such refusal, so the claim was false and has
been removed. E3 now makes the point in its own right in three places — `simplified_explanation`,
`illustration.analogy_breaks_when` and `must_know` point 5 — and attributes it to nothing. **E3 is
therefore correct whichever way C23 is fixed**, and no second pass on E3 is owed.

## Also out of scope: a possible defect against `B0-R0-C16`

Defect 3 above notes that C16, *Rearranging an equation*, teaches two moves — do the same to both
sides, and a side that is a sum is treated whole — and nothing about reordering the terms of a
sum. E3's step three needs that move. Rather than assume it, E3 now shows it in full, with a
concrete demonstration on numbers, so E3 stands on its own. Whether C16 should carry the move is a
question for whoever owns Part C.
