# Defects — Part B, sections B4 to B6

Audit of `check/records/B0/B0-R0-C12.yml` (B4, energy units), `B0-R0-C13.yml` (B5,
concentration units) and `B0-R0-C14.yml` (B6, body-size units), against the files in
`sources/`. Most serious first.

Quote existence and prose arithmetic were not re-checked; the build already does both. Every
worked answer in all three drill sets was recomputed anyway and every result is right, so no
arithmetic defect is listed below. What follows is what reading the instruments turned up.

**The two deliberate boundaries both held.** B5 supplies no molar mass for cholesterol
anywhere — not in the illustration, not in a must-know point, not in any of the thirteen
practice answers — and refuses the conversion in four separate places. B6 names no BMI
threshold, no cut-point and no value at which anything becomes anything. Defect 8 is a leak
around the first of those and defect 10 a wording risk near the second; neither breaches it.

---

## 1. B0-R0-C12 — `must_know[7]` — the labelling requirement is not absolute

**The claim.** "An Indian food packet must carry its energy in kilocalories." The same
absolute form is in `definition.text`: "In India the energy on a pre-packaged food label is
declared in kilocalories."

**What the source says.** Regulation 5(3)(c) of the Food Safety and Standards (Labelling and
Display) Regulations, 2020 (compendium Version-VIII, 09.09.2025) opens: *"The following foods
are exempted from mandatory nutritional labelling:"* and then lists thirteen classes —
unprocessed single-ingredient products, drinking water, herbs and spices, salt and salt
substitutes, table-top sweeteners, coffee and chicory products, tea and herbal infusions,
vinegars, flavourings and additives and gelatine and yeast, chewing gum and bubble gum,
alcoholic beverages, and Foods for Special Dietary Uses and Special Medical Purposes.
Regulation 8(1) adds a second exemption: *"Where the surface area of the package is not more
than 100 square centimetres, the label of such package shall be exempted from the requirements
of list of ingredients, Lot Number ..., nutritional information ..."*

So a packet of salt, a bottle of water, a packet of tea, a bar of chewing gum and any packet
under 100 cm² carry no energy declaration at all. The record states as a universal duty a rule
that the regulation itself narrows twice, and a reader who repeats it in a committee is
contradicted by the next clause of the instrument they cited.

**Smallest fix.** Add the qualifier where the word "must" appears, in both places: *"An Indian
food packet that has to carry nutritional information must give its energy in kilocalories.
Regulation 5(3)(c) exempts thirteen classes of food from nutritional labelling altogether, and
regulation 8(1) exempts any package smaller than 100 square centimetres."* Add a reference
entry for regulation 5(3)(c) with the quote above.

---

## 2. B0-R0-C12 — `definition.text` and `must_know[7]` — the per-serve requirement is for the
   RDA percentage, not for a second energy figure

**The claim.** `definition.text`: "That figure is given for every 100 g or 100 ml, and again
per serve." `must_know[7]`: "It asks for the energy value in kcal, for every 100 g or 100 ml
and per serve."

**What the source says.** Regulation 5(3)(b), in full: *"Nutritional Information per 100g or
100ml or per single consumption pack of the product and per serve percentage (%) contribution
to Recommended Dietary Allowance calculated on the basis of 2000kcal energy, 67 g total fat, 22
g saturated fat, 2 g trans fat, 50 g added sugar and 2000 mg of sodium (5 g salt) requirement
for average adult per day, shall be given on the label containing the following: — (i) energy
value (kcal); ..."*

Two things are wrong. The thing required per serve is the **percentage contribution to the
RDA**, not the energy value in kilocalories; a search of the whole instrument finds "per serve"
only in this clause and in regulation 9(1) for restaurant menus. And the base is *"per 100g or
100ml **or per single consumption pack**"* — three alternatives, not two, so a single-
consumption pack need not carry a per-100 g figure at all. The record's own cited quote stops
one word before the word that carries the requirement.

**Smallest fix.** Replace both sentences with: *"That figure is given per 100 g, or per 100 ml,
or per single consumption pack. The same clause separately requires, per serve, the percentage
contribution to the Recommended Dietary Allowance."*

---

## 3. B0-R0-C14 — `definition.references[0].verified.opened` — set true on a source the
   record's own note says was not opened

**The claim.** The record's only definition reference is `openstax_prealgebra_2e` with
`resolved_id: PENDING`, `claim_located: false` and `opened: true`. Its note reads: *"Not opened
from this authoring environment ... it stays in the citation backlog until somebody with
library access opens the chapter and fills in the locator."*

**What is wrong.** `opened: true` and the note contradict each other, and the note is the one
telling the truth. `claude.md` calls this the one rule that matters more than the others:
`verified.opened` "is set to true by whoever obtained the source and read the passage, and by
nobody else." The three other Book 0 records carrying an unreachable textbook anchor —
C39, C41, C42 — all write `opened: false` with `resolved_id: PENDING`, so the house convention
exists and this record departs from it. As it stands the record will pass to `verified` status
asserting a chain of provenance nobody built.

**Smallest fix.** `opened: false`. Nothing else changes; the note is already correct and the
concept is `derivable`, so an unopened anchor warns rather than blocks.

---

## 4. B0-R0-C12 — `practice[7].answer` (level 6) — the label-checking method breaks on the
   first real sugar-free or high-fibre product

**The claim.** "You can check any Indian label's energy figure from the grams printed beside
it, without any equipment at all."

**Why it breaks.** The factors in regulation 5(3)(e)(i) cover eight components: carbohydrate,
polyols other than erythritol, erythritol, protein, fat, alcohol, organic acid and dietary
fibre. The panel required by regulation 5(3)(b)(ii) lists only protein; carbohydrate, total
sugars and added sugars; total fat, saturated fat, trans fat and cholesterol; and sodium.
**Dietary fibre, polyols and organic acid are nowhere required on the panel.** So on a
high-fibre cereal or a sugar-free confection — exactly the products an obesity course sends a
reader to look at — the declared energy legitimately cannot be reproduced from the printed
grams, and a reader following this instruction will find a gap and conclude the label is wrong.
Regulation 5(3)(d) adds a second reason for a gap: *"The compliance to quantity of declared
nutrients on the label shall have the tolerance of maximum minus 10 percent of the value for
that nutrient declared on the label ..."*

The worked problem itself is fine — its food is carbohydrate, protein and fat only. It is the
generalisation in the closing paragraph that overreaches, and `must_know[8]` repeats it more
softly ("a gap you cannot explain is worth raising").

**Smallest fix.** Replace the sentence with: *"Where a label declares only carbohydrate,
protein and fat, you can reproduce its energy figure from the grams printed beside it. Where
the food carries dietary fibre, polyols or organic acid, the panel need not print those grams,
so your total will fall short of the declared figure and nothing is wrong."*

---

## 5. B0-R0-C14 — `illustration.body` and `illustration.numbers[0]` — a pre-2019 description
   of the SI quoted for how the SI is built now

**The claim.** "The metre and the kilogram are two of the seven base units of the SI. Every
other unit, this one included, is a product of powers of those base units." The registered
number cites `bipm_si` with the quote *"seven base units and derived units defined as products
of powers of the base units"*.

**What the source says.** That phrase is the tail of this sentence: *"**Prior to** the historic
vote by the BIPM's Member States on 16 November 2018 to revise the SI, the SI was defined in
terms of seven base units and derived units defined as products of powers of the base units."*
The page's own present-tense statement is the opposite one — *"From 20 May 2019 all SI units
are defined in terms of constants that describe the natural world"* — and what it says survives
is narrower: *"This role for the base units continues in the present SI even though the SI
itself is now defined in terms of the defining constants listed above."*

The quote is real and it is the wrong sentence: it describes the system the 2018 vote replaced,
and it is used to state how the SI is constituted today. B0-R0-C09 gets this right in the same
corpus — "Seven base units keep their role inside that system" — so B6 also drifts from the
wording the reader already met.

**Smallest fix.** Change the registered quote to *"This role for the base units continues in
the present SI even though the SI itself is now defined in terms of the defining constants
listed above"*, and rewrite the illustration line as: *"The metre and the kilogram are two of
the seven base units, which keep their role inside the SI. A unit like this one is built out of
them."*

---

## 6. B0-R0-C12 — `practice[7].answer` (level 6) — states two digits and then writes three

**The claim.** "Round it before you write it. The grams on the label carry two digits each, so
the last digits of 1,966.48 are not yours to keep. Report about 1,970 kilojoules for every
100 g."

**Why it is wrong.** 1,970 carries three significant figures, not two. The record contradicts
itself inside one paragraph, and it contradicts `practice[3]` (level 4), which reasons
identically from 450 and correctly writes 1,900. One of the three inputs, the 8 g of protein,
carries a single digit. On the record's own rule the answer is 2,000 kJ, or 1,900 kJ if the
8 g is read as two digits.

This is the one place in the three sections where a converted figure gains a digit against the
record's own stated discipline, and it sits in the drill set, where a reader will copy it.

**Smallest fix.** "Report about 2,000 kilojoules for every 100 g" — or keep 1,970 and change
the sentence before it to say which input justifies three digits.

---

## 7. B0-R0-C13 — illustration against `practice[4]` — the same rule is applied two ways

**The claim.** Illustration: "The laboratory gave you 100, to the nearest whole milligram. That
is three digits you can stand behind. Write 5.55 mmol/L." Practice level 4: "The laboratory
gave 92, which carries two digits you can trust. Writing 5.1066 claims five. Write 5.1 mmol/L."

**Why it matters.** Both values come off the same instrument to the nearest whole milligram per
decilitre, so both carry the same resolution — about half a part in two hundred. The
illustration derives three digits from that fact and names the reasoning. The practice problem
derives two digits from the same fact and names no reasoning at all. A reader who works the
illustration and then the drill cannot tell which rule they are being taught, and the drill's
answer silently throws away resolution the laboratory supplied.

Nothing here gains significant figures — the precision discipline errs safe in every one of the
thirteen answers, and level 8 is an excellent treatment of the 5.550621670 failure. The defect
is the inconsistency, not a false number.

**Smallest fix.** Give level 4 the illustration's sentence: *"The laboratory gave 92 to the
nearest whole milligram, which is two digits. Write 5.1 mmol/L."* Or, better, carry the
illustration's reasoning through and write 5.11.

---

## 8. B0-R0-C13 — `practice[12].prompt` (level 10) — the two figures encode cholesterol's molar
   mass

**The claim.** "The trial reports mean total cholesterol as 5.2 mmol/L. Our audit reports it as
200 mg/dL. Those are the same figure, near enough, so the two groups are comparable on this."

**Why it is a problem.** The section's whole teaching point is that the course does not hold
cholesterol's molar mass and will not supply it. But a reader who takes the prompt's two
figures at face value and runs the section's own method backwards recovers it: 200 divided by
0.52 is about 385 g/mol, which is cholesterol's molar mass to three digits. The two numbers
cannot both have been chosen without that value in hand, and the source file says in its own
words it does not carry it.

The answer is not defective — it stops at M, refuses the divisor, and sends the reader to
PubChem 5997. The boundary holds in everything the record asserts. What leaks is the prompt,
and it leaks the one number the section exists to withhold.

**Smallest fix.** Change one of the two figures so the pair no longer implies a molar mass —
for example make the audit figure 210 mg/dL and the claim "near enough" a claim the reader
cannot evaluate at all. The problem gets harder in the right way: the reader must say they
cannot check it even approximately.

---

## 9. B0-R0-C12 — `must_know[7]` — silence read as prohibition

**The claim.** "It asks for no kilojoule figure at all. So the SI unit of energy is the one
Indian law does not want."

**What the source says.** Searching the whole instrument for "joule", "kilojoule" and "kJ"
returns nothing, so the first sentence is right: no kilojoule figure is required anywhere in
these regulations. The second sentence turns that silence into a preference and almost into a
ban. The regulations neither require a kilojoule figure nor forbid one, and regulation 5(3)(b)
is a floor — it says what the label shall contain, not what it may not contain.

**Smallest fix.** "It asks for no kilojoule figure at all. The SI unit of energy is simply not
the unit Indian labelling law works in, which is why you have to be able to convert."

---

## 10. B0-R0-C14 — `must_know[5]` — a live scientific and institutional dispute, with no citekey

**The claim.** "Whether the same line should be drawn for Indian populations is a live
question. The subject books take it up with the statements in hand."

**Why it needs one.** This is an assertion about the state of the world — that a dispute exists,
that it is current, and that it concerns Indian populations specifically. The point carries no
`refs` and the record cites nothing but `openstax_prealgebra_2e` and, in the numbers register,
`bipm_si`. Neither says anything about cut-points or about India. As drafted it is exactly the
pattern `claude.md` §7b names: a claim written from what the model knows, sitting in the one
field designed to survive after the section is forgotten.

The point is also the section's whole defence of the no-cut-points boundary, so it is the
sentence most likely to be quoted out of the section and the one least able to support being
quoted.

**Smallest fix.** Either cite the instrument — the 2025 India Obesity Commission statement is
the obvious anchor and is not in `sources/`, so it goes in `READY.md` and the citation backlog
first — or drop the empirical claim and keep only the methodological one: *"What counts as a
high value is not in the arithmetic. Somebody decided it, and decisions like that get revised.
Quote a cut-off only with whose it is and when it was set."*

---

## 11. B0-R0-C12 and B0-R0-C14 — `concept_deps` omit the sections they are built on

**The claim.** C12 declares `concept_deps: [B0-R0-C03, B0-R0-C06]`. C14 declares
`concept_deps: [B0-R0-C05, B0-R0-C06]`.

**What is missing.** C12's definition opens with "The joule is the SI unit of energy ...
J = kg m^2 s^-2", which is B0-R0-C09 ("What a unit is, and the SI base and derived units")
almost verbatim, and its whole drill set is unit conversion, which is B0-R0-C10. C14's
definition opens with "the SI base unit of mass ... the SI base unit of length" and turns on
what a derived unit is, all of which is C09. Neither declares C09. C13, by contrast, declares
C02, C03, C06, C09 and C10 and gets it right.

Nothing forward-references, so the build will not catch this. What it costs is the
micro-refresher, which is generated from the union of declared dependencies, and the audit
trail that shows the chain is unbroken rather than nominally unbroken.

**Smallest fix.** Add `B0-R0-C09` and `B0-R0-C10` to C12, and `B0-R0-C09` to C14.

---

## 12. B0-R0-C13 — `simplified_explanation` — "a fixed count of molecules"

**The claim.** "A mole is a fixed count of molecules, and it is one of the seven SI base units
you met a few sections back."

**Why it is loose.** `definition.text` in the same record has it right — the mole "counts
elementary entities rather than weighing them" — and B0-R0-C09, which the reader did meet four
sections back, says the mole "measures an amount of a substance". Molecules are one kind of
elementary entity. A reader who carries "count of molecules" forward will be wrong the first
time they meet a molar figure for an ion or an electron, and §10 rule 2 asks for the same words
each time a term reappears.

**Smallest fix.** "A mole is a fixed count of things — molecules here — and it is one of the
seven SI base units you met a few sections back."

---

## Notes that are not defects

**B5's handling of the missing molar mass is the strongest teaching in the three sections.**
The illustration names both wrong moves explicitly — summing atomic weights from memory, and
reusing glucose's divisor because both values came off one report — and level 7's first problem
makes the reader diagnose the second of them in someone else's working. That is the section
doing its job.

**B6's scaling argument is right.** Doubling every length multiplies mass by 8 and the squared
height by 4, so the index doubles, and `analogy_breaks_when` correctly restricts it to constant
shape and constant density. It is also the honest answer to "why squared", which most material
skips.

**B6 never names the index.** The record calls it "the index" throughout and never writes "body
mass index" or "BMI". That is consistent with the no-cut-points boundary and may well be
deliberate, but naming the quantity is not the same as naming a threshold, and a reader who
finishes B6 may not connect it to the term every subsequent booklet will use. Worth a decision
rather than a silent default.

**B5's mixture boundary sits awkwardly against its own worked example.** `must_know[4]` says a
figure that is a mixture reported as a single total has no molar mass, and the illustration's
worked-and-refused case is "total cholesterol" — a figure whose name says total. It is in fact
reported as cholesterol equivalents after the esters are hydrolysed, so a single molar mass is
the right instrument, but nothing in the record tells the reader that, and the word "total"
points the other way. One clause would settle it.

**B4's institutional treatment is correct and unusually well done.** The calorie is presented as
two committee decisions with dates, the `as_of` is stamped, the event trigger names three
instruments rather than a date, and the critique exercise makes the reader find the word
"measurement" and replace it. Defects 1, 2, 4, 6 and 9 are all in how the FSSAI regulation is
described, not in how the section treats its type.
