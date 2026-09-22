# Book 0 · Part B, sections B1–B3 — audit defect list

Records audited: `B0-R0-C09` (B1), `B0-R0-C10` (B2), `B0-R0-C11` (B3).
Sources opened: `sources/bipm_si.txt`, `sources/nfsa_2013.txt`, `sources/nist_sp811.txt`,
`sources/INDEX.yml`, `check/references/library.bib`, `books/B0/INVENTORY-part-B.md`.
Audited 22 September 2026. Report only; no record was edited.

Quote existence and prose arithmetic were taken as already checked and were not re-run. What
follows is claims the quotes do not carry, claims carrying no citekey at all, type and treatment
mismatches, staleness, and errors in the teaching itself.

**What is clean, said plainly.** Every worked answer in both drill sets was recomputed by hand and
every one is right — 8 problems in C10, 14 in C11, including the four-place cases (0.3 h → 18 min,
12,000 m² → 0.012 km², 45,000,000 ÷ 3,000,000 = 15, 2 × 5,000 mg → 10 g against the brochure's
0.0004 g). Both ladders reach the mechanical band and the transfer band and touch all four bands.
All three records carry a `boundary` must-know point that names a limit of the technique rather
than the scope of the section, which is the failure Part A shipped four of. C09's illustration is
genuinely reproducible: searching the held BIPM page for `J =` and for `299 792` both land exactly
where the text says they will. And B3 does deliver its promise in the direction that matters — the
480-minute note, the kilograms-per-person-squared formula, and levels 7, 8 and 10 all reject a
wrong formula without deriving the right one. The defect in B3 is the opposite claim, at item 1.

---

## 1. C11 · `illustration.body` — the closing sentence asserts the converse of the section's own boundary

**The claim.** Two sentences, both in the illustration:

> Dividing does it. The kilometres cancel and the hours are left. So the journey time is the
> distance divided by the speed, and the units told you so.

> Notice what you did there. You did not know the formula and you did not look one up. You wrote
> down what unit the answer had to have, and **the only arrangement that gives that unit is the
> right one.**

**Why it is wrong.** The second sentence is false, and it is false on the illustration's own second
worked case. `kilograms per person per month × persons × months = kilograms` is satisfied by
`5 × 4 × 12`, and equally by `5 × 4 × 30`, `5 × 4 × 6`, and `2 × 5 × 4 × 12`. The reader did not get
the 12 from the units. They got it from knowing that a year holds twelve months, which the units
cannot tell them. The unit check narrowed the *shape* to "rate times a count of people times a count
of months" and then stopped.

**What the rest of the record says.** Four other fields of this same record say the opposite.
`definition.text`: "It cannot confirm a formula, because a wrong dimensionless factor changes no
unit." `simplified_explanation`: "The check throws out wrong formulas. It never certifies a good
one." The `boundary` must-know point. And the `critique` exercise, whose whole answer is that a
colleague reporting "the units come out right, so the formula is correct" has established nothing.

This is the most serious item in the three sections because the illustration is the part the reader
*does*, it is where the claim is made last, and it hands them precisely the habit the section exists
to prevent — signing off a formula because the units worked out.

**Smallest fix.** Replace the two offending clauses. "So the journey time has the shape of a
distance divided by a speed, and the units told you that much" and "You wrote down what unit the
answer had to have, and that threw out every arrangement but one shape. It did not tell you the
twelve — you brought that." Nothing else in the illustration needs to move.

---

## 2. C09 · `definition.text`, `simplified_explanation`, `must_know` — the artefact contrast is unsupported by the only source cited, and is misdated by 36 years

**The claim**, in three reader-facing fields:

- `definition.text`: "Since 20 May 2019 every SI unit follows from those seven fixed values **rather
  than from any object kept anywhere**."
- `simplified_explanation`: "One of them is the speed of light in vacuum, fixed at 299 792 458 metres
  per second. **It is not measured any more.** … **So nobody keeps a master metre in a cupboard**,
  and nobody has to send you a copy of one."
- `must_know` (the `number` point, `refs: [bipm_si]`): "**No object has to be sent from anywhere.**"

**What the source actually says.** `sources/bipm_si.txt` contains no mention of an object, an
artefact, a prototype or a cupboard. The quoted sentence is "From 20 May 2019 all SI units are
defined in terms of constants that describe the natural world." The source's own account of what
preceded 2019 is the opposite of the record's: "Prior to the historic vote … the SI was defined in
terms of **seven base units and derived units defined as products of powers of the base units**."
So the record's contrast is not merely unsupported — it conflicts with how the instrument itself
describes the change.

**And it is factually wrong.** The metre stopped being an artefact in 1960 and has been defined from
a fixed value of the speed of light since the 17th CGPM in 1983. The speed of light has not been a
measured quantity since 1983 either. Both sentences attribute to the 2019 revision two things that
happened 36 years earlier. What 2019 actually changed was the kilogram, the ampere, the kelvin and
the mole — and the kilogram is the one that was an object in a cupboard, until 2019. The record has
attached the right story to the wrong unit.

The claim entered upstream, not here: `books/B0/INVENTORY-part-B.md` already states "the SI is
defined by seven exact constants **rather than by artefacts**, which is why a metre in Raipur is a
metre in Paris". So the fix belongs in the inventory too.

**Smallest fix.** Move the story to the kilogram and get a source for it, or delete the contrast.
The cheapest honest version keeps the Raipur-and-Paris line, which is true and needs no artefact:
"A metre in Raipur is a metre in Paris because both follow from the same fixed numbers." Then either
drop "nobody keeps a master metre in a cupboard" and "it is not measured any more", or put the
kilogram sentence in its place with a source that says so — which is not in `sources/` yet, so it
goes to the citation backlog with `opened: false` rather than being written from memory.

---

## 3. C11 · `illustration` — a statutory figure in reader-facing prose with no citekey, no quote, and no `numbers` entry

**The claim.** `illustration.body`: "Section 3(1) of the National Food Security Act, 2013 entitles a
person in a priority household to five kilograms of foodgrains per person per month."

**What backs it in this record.** Nothing. C11 has no `illustration.numbers` block at all. The
statutory sentence, the 5, the section number and the Act's name sit in prose with no `refs` and no
`citekey`. Practice levels 5 and 7 repeat the same figure and do carry `refs: [nfsa_2013]`, but
neither carries a quote.

**Why nothing catches it.** `check/build.py` builds the numbers register from
`illustration.numbers` only (line 1305). A number that never appears there is invisible to the
register, and a `refs` entry on a practice problem is checked for being a known citekey, not for
saying what the problem says. So the most load-bearing factual sentence in B3's second illustration
is checked by nobody.

**What the source says.** `sources/nfsa_2013.txt` supports the figure — "shall be entitled to
receive five kilograms of foodgrains per person per month" — so this is a missing audit trail, not a
wrong claim. C10 has already done the work: its `illustration.numbers` carries value, unit, citekey
and that exact quote.

**Smallest fix.** Copy C10's `illustration.numbers` entry into C11 verbatim, and add an `as_of`.

---

## 4. C10 · `practice` level 4 — the Antyodaya figure is stated more absolutely than the proviso allows

**The claim.** "The proviso to section 3(1) of the National Food Security Act, 2013 covers
households under the Antyodaya Anna Yojana. **It entitles such a household to 35 kilograms of
foodgrains per household per month.**"

**What the proviso actually says** (`sources/nfsa_2013.txt`, s.3(1) first proviso):

> Provided that the households covered under Antyodaya Anna Yojana shall, **to such extent as may be
> specified by the Central Government for each State in the said scheme**, be entitled to thirty-five
> kilograms of foodgrains per household per month **at the prices specified in Schedule I**

Two qualifiers are dropped. The 35 kg is not an unconditional entitlement of every AAY household —
its extent is specified by the Central Government, State by State, under the scheme. And the
entitlement is to receive at Schedule I prices, not to receive. The record turns a conditional,
priced entitlement into a flat quantity. This is the same shape of defect as the pilot's "laying
requirement described as a condition of validity" — a real clause, read one degree harder than it
reads.

The same elision, smaller, sits in C10's illustration and C11's: "entitles a person in a priority
household to five kilograms" drops "at subsidised prices specified in Schedule I" and "identified
under sub-section (1) of section 10". For a units exercise that shortening is defensible; for the
proviso it is not, because the Central-Government qualifier is the operative limit.

**And there is no quote anywhere in the record for the 35.** `refs: [nfsa_2013]` is the whole audit
trail.

**Smallest fix.** Add ten words to the prompt — "to the extent the Central Government specifies for
each State, 35 kilograms per household per month" — and put the proviso's words in the record beside
the figure, as C10 already does for the 5.

---

## 5. C11 · `illustration.body` and `practice` level 7 — a derived annual figure presented as the statutory entitlement, which is the move C10 forbids two sections earlier

**The claim.** C11 practice level 7, worked answer: "**Sixty kilograms per person per year.**"
C11 illustration: "**240 kilograms per household per year.**"

**What C10 taught.** C10's `analogy_breaks_when`: "The Act gives a monthly entitlement. The daily
figure is yours, and you say so when you quote it. … '167 grams a day' on its own hands your choice
to the next person as though the Act had made it." And C10 carries a whole must-know point on it,
tagged `india_deviation`, bearing `policy`: "Say which number of days you used whenever you quote a
daily figure built from the five kilograms per person per month in the Act."

C11 then prints a bare annual figure, twice, with no such sentence anywhere in the record. There is
no 60 kg annual entitlement in the NFSA and no 240 kg household one; both are the reader's
arithmetic on a monthly figure. The section that follows the rule breaks it.

This is a defect no source check can see, because both numbers are arithmetically correct and the
statute is quoted correctly. It is a contradiction between two records, and it lands on the reader
as a licence to do in B3 what B2 told them not to.

**Smallest fix.** One clause in each place. "Sixty kilograms per person per year — your arithmetic,
not the Act's figure; the Act states a monthly entitlement." Same for the 240.

---

## 6. C09 · `definition.references[4]` — the quote carries the list of names and neither of the two claims attached to it

**The reference.** `locator: closing paragraph, on the seven base units and the 2018 vote`;
`quote: the metre, the kilogram, the second, the ampere, the kelvin, the mole, and the candela`.

**The claims that lean on it.**

- `definition.text`: "Seven base units **keep their role** inside that system."
- `analogy_breaks_when`: "The BIPM's member states **voted on 16 November 2018** to change how the
  SI is defined, and they can vote again."

Neither is in the quoted words. The quote is a list of seven nouns. It establishes that those seven
are the base units and nothing else — not that their role continues, and not that a vote happened on
a date.

**Both claims are true and both are in the file**, in the sentences on either side of the quoted
list: "the historic vote by the BIPM's Member States on 16 November 2018 to revise the SI" and
"This role for the base units continues in the present SI even though the SI itself is now defined
in terms of the defining constants listed above." So this is a quote that was chosen for the wrong
span. The machine check passes, because the words are in the file; the claims still stand on
nothing. §8 says numbering is per source-and-clause "so a number always names exactly what was
consulted", and one reference is doing three jobs here.

The 16 November 2018 date is also the record's only dated institutional claim in reader-facing
prose and, as it stands, carries no citekey in its own field at all.

**Smallest fix.** Split into two references against the same locator paragraph, quoting the two
sentences named above, and point `analogy_breaks_when` at the vote one.

---

## 7. C09 · `illustration.body` — the prefix table and the minute and hour are institutional decisions with no instrument behind them

**The claims, all uncited.**

> ```table
>     prefix  multiply the unit by  so
>     kilo    10^3                  one kilometre is 1,000 metres
>     centi   10^-2                 one centimetre is 0.01 metres
>     milli   10^-3                 one milligram is 0.001 grams
>     micro   10^-6                 one microgram is 0.000001 grams
> ```

> The symbol for kilo is k, for centi is c and for milli is m. The symbol for micro is the Greek
> letter mu, written µ.

> Two more units you will meet every day are **not SI units at all**. They are used anyway, because
> each one has a fixed relation to the second. One minute is 60 seconds. One hour is 3,600 seconds.

**What the source says.** Nothing. `sources/bipm_si.txt` has no prefix table, no prefix symbols, and
no mention of the minute or the hour. `sources/nist_sp811.txt`, the only other SI file held, carries
the calorie definitions and a note on coherence — no prefixes either.

This matters more here than it would elsewhere because C09 is typed `institutional`, and §4 says an
institutional claim is true because a body decided it and must cite the instrument. The prefixes are
CGPM decisions. "Not SI units at all, but used anyway" is a statement about the SI Brochure's table
of non-SI units accepted for use with the SI. Both are presented as facts of the world with no body
named. Seven of the eight assertions in the paragraph above carry no citekey.

The downstream cost is real: C10 and C11 both compute with these prefixes throughout, and C10's
practice level 5 turns on µg and mg. The whole of B2 and B3 rests on a paragraph with no source.

**Smallest fix.** The SI Brochure is named in the held file ("The SI is defined by the SI Brochure,
published by the BIPM") but is not in `sources/`. So this goes to the citation backlog: add the
Brochure's prefix table and its Table 8 of accepted non-SI units as a reference with
`opened: false` and a `verified.note` naming what is needed, per §7b — rather than leaving eight
assertions with nothing behind them.

---

## 8. C10 and C11 · `review` — a five-year clock on records whose applied and transfer bands rest on a statute

**The state.** Both are `concept_type: derivable`, `review.stability: long`,
`review.trigger: '2031-09-22'`. Correct for the technique, per §4.

**Why it will go stale anyway.** Neither record's technique will change, but the material the reader
is drilled on will. C10's illustration and practice level 4 rest on NFSA s.3(1) and its proviso.
C11's second illustration and practice levels 5 and 7 rest on the same section. The proviso itself
says the extent "may be specified by the Central Government for each State in the said scheme" —
that is, it is designed to change without the Act changing. Nothing in either record will prompt a
re-check when it does, and a reader in 2029 quoting a 35 kg AAY figure out of a practice problem is
the exact failure §4's event triggers exist to prevent.

The same gap is visible in the smaller field: C09's two `illustration.numbers` entries both carry
`as_of: '2026-09-22'`; C10's single number, which is a statutory figure and the only one in the
record, carries none.

**Smallest fix.** Keep the five-year date and add a named event trigger beside it on both records:
*next amendment to NFSA section 3 or Schedule I, or next Central Government specification under the
Antyodaya Anna Yojana proviso.* And add `as_of: '2026-09-22'` to C10's `illustration.numbers` entry.

---

## 9. C09 · `must_know` — the policy point draws a conclusion the SI does not license, and pre-empts C13

**The point**, `kind: number`, `bearing: policy`, `refs: [bipm_si]`:

> The SI fixes every unit through seven constants with exact values. One of them is the speed of
> light in vacuum, at 299 792 458 metres per second. No object has to be sent from anywhere. **So
> when a result arrives from another country's laboratory, the units are not the thing to argue
> about.**

**What the quote establishes.** That the *size* of a unit is the same everywhere. That is all. It
says nothing about which unit a laboratory chooses to report in, which is the thing that actually
differs between countries and the thing that actually causes harm. The course knows this: C13,
three sections later, exists because mg/dL and mmol/L are both in daily use and a glucose value in
one is not a glucose value in the other.

So the point as written tells the reader to stop asking the question C13 is about to teach them to
ask. Under §5's admission test it changes what the reader does — in the wrong direction.

**Smallest fix.** Keep the first three sentences and rewrite the consequence to what the source
supports: "So a disagreement between two laboratories is never about the size of the unit. Check
which unit each one reported in — that is where the difference will be."

---

## 10. C11 · `definition.text` — the rule is stated on units, the section is named for dimensions, and the record's own practice contradicts it

**The claim.** Paragraph 1 draws the distinction: "Every measured quantity has a dimension, which is
the kind of thing it is … The unit is how that dimension is measured. **Two quantities of the same
dimension may be measured in different units.**" Paragraph 2 then states the rule: "An equation
between physical quantities must carry **the same units** on both sides. Two quantities may be added
or subtracted **only when their units are the same**."

**Why that is wrong by the record's own first paragraph.** 3 kg and 4 g have the same dimension and
different units. By paragraph 2 they may not be added. Practice level 1 has the reader add them —
"3 kg and 4 g — after converting" — which is right, and which paragraph 2 forbids. The equality that
has to hold across an equals sign is of dimension; equality of units is what you arrange by
converting first.

**And `dimension` is then abandoned.** The word appears in the concept name and twice in
`definition.text`, and never again in `simplified_explanation`, `illustration`, any must-know point,
either exercise, any of the fourteen practice problems, or any retrieval item. All of those say
"unit check". §10 rule 2 asks that a term be introduced once and then used in the same words; here it
is introduced once and then dropped, so a reader told they are learning dimensional analysis never
meets the idea again.

**Smallest fix.** Two sentences in `definition.text`: state the rule on dimensions, then say the
unit check is its practical form and requires converting to a common unit first. That makes
paragraph 2 consistent with paragraph 1 and with practice level 1, and it earns the word in the
title.

---

## 11. C09 · `quantitative: false` ships a constructive technique with no drill set

**The state.** `quantitative: false`, no `practice` block, no `practice_note`.
`books/B0/INVENTORY-part-B.md` justifies it: "The only Part B section that teaches no technique the
reader must carry out."

**Why that does not hold.** The record's own illustration says "Now build some units yourself" and
walks the reader through m/s, m², m³ and kg/m³. Its `retrieval` exercise asks them to "build two
derived units yourself from base units alone". §7a's test is whether the reader has to be able to
*carry something out* as against *state* something — assembling a derived unit is carrying something
out, and the record asks for it twice. §7a also says getting this wrong in the permissive direction
is cheap and getting it wrong the other way ships a technique nobody can perform.

**Smallest fix.** The technique *is* drilled — C11 levels 1 to 3 do exactly this, from a different
angle. So the honest and cheap fix is not to add problems but to add a `practice_note` saying the
construction of derived units is drilled in B3's mechanical band, which is true and which makes the
`false` a decision rather than an omission.

---

## 12. C10 and C11 · `definition.references` — `opened: true` on a passage the note says was not read, with `resolved_id: PENDING`

**The state**, identical in both records:

```
citekey: openstax_prealgebra_2e
verified:
  resolved_id: PENDING
  opened: true
  claim_located: false
  note: ... the named chapter located in its table of contents. The passage behind this
        definition has not been read yet ...
```

§8 is explicit: "`verified.opened` is set true only by the person who obtained and read the source."
The note says the passage was not read. `opened: true` therefore overstates what was done, on the
one flag the whole audit trail rests on, and it does so in the same field that honestly reports
`claim_located: false` — so the record contradicts itself in adjacent lines.

`resolved_id: PENDING` is separately wrong: `check/references/library.bib` already carries the
resolvable URL for this citekey, and its `note` records the chapter list as confirmed on 22 Sep 2026
— which is exactly the work the `verified.note` describes. The audit trail says PENDING for
something already done.

For a `derivable` concept this only warns, per §7b, and the teaching genuinely does not rest on the
anchor. That is why it sits at 12 rather than higher. But it is the flag that will be believed by
everyone downstream.

**Smallest fix.** Copy the bib URL into `resolved_id` in both records, and either set
`opened: false` keeping the note as it stands, or open the named section and set
`claim_located: true`.

---

## 13. C11 · `practice` level 5 is the second illustration with its answer already printed

**The state.** The illustration works the NFSA yearly-grain formula, establishes that you multiply
by persons and by months, and prints `5 times 4 times 12 = 240`. Practice level 5 then gives the
same statute sentence, the correct arrangement ("5, times the number of people, times 12"), the same
household of four, and asks for the same 240.

§7a: "The prompt is unsolved. No worked fragment, no hint, no restatement of the method. If the
prompt contains the shape of the answer, it is a worked example and belongs in the illustration."
Here the prompt hands over the arrangement that the illustration spent a page arriving at, and the
answer is already on the page above. It is the set's only applied problem on the statute, so the
applied band is thinner than the count suggests.

**Smallest fix.** Change what is given and what is asked. Give the yearly total and the household
size and ask for the monthly per-person rate, which drills the same cancelling backwards and cannot
be answered by looking up.

---

## 14. C11 · `practice` levels 9 and 10 present figures about the world with no citekey

**The claims.** Level 9: "The plant treats 4.5 crore litres a day, which works out at 135 litres a
person for the city's 30 lakh people." Level 10: "It doses at 2 milligrams per litre. So a 5,000
litre tank needs …"

A plant capacity, a city population and a chlorine dose, all presented as things somebody wrote in a
press note or a brochure, none with `refs`. §7a: "Real figures or none … Never invent a statistic to
make a problem feel applied — an invented prevalence in a practice problem is the same defect as an
invented one in the prose, and it is worse, because the reader is about to do arithmetic on it and
remember the result."

**In fairness, both answers hedge well.** Level 9's answer says "Both 15 and 135 are only numbers
until somebody names a standard and says who set it", and level 10's says "It says nothing about
whether 2 milligrams per litre is the right dose for that tank, which is a question for whoever sets
the standard." That containment is why this sits at 14 and not higher. The residue is that a reader
will still walk away with "2 mg/L" in their head as a chlorine dose.

**Smallest fix.** One clause in each prompt saying the figures are made up — or cite a real CPHEEO
or state water board figure, which would be better and costs a source.

---

## 15. C11 · `practice` level 5 (the bus) skips a line in the working

**The claim.** "Turn it over and the units come out as a speed."

```working
    kilometres divided by hours
    = km/h
```

Turning `min/km` over gives `km/min`, not `km/h`. The hour arrives from a conversion the working
never shows. §4: worked calculations show every line, and a reader who cannot follow line three
cannot skip to line four. A reader doing this literally gets km/min and stops.

**Smallest fix.** One line: `km/min`, then `× 60 min over 1 h`, then `km/h`.

---

## 16. C09 · `illustration.body` — "the metre comes from that speed" is one step short

**The claim.** "The second comes from that frequency and the metre comes from that speed. Fix the
numbers and you have fixed the units."

The metre follows from the fixed value of the speed of light *and* the second — a speed alone fixes
no length. The reader is being shown how the chain closes, and as printed it does not close. Small,
and worth the four words because this sentence is the one place the section shows the mechanism it
has been asserting.

**Smallest fix.** "…and the metre comes from that speed together with the second."

---

## Not defects, recorded so they are not re-raised

- C09 `review.stability: short` with an event trigger is correct for an `institutional` concept per
  §4, even though the SI is the most durable institutional object in the corpus.
- C09's `analogy_breaks_when` does the §3 `institutional` job properly: "all of this is decided, not
  discovered … Anything in this section that starts with 'the SI says' is true as of today, and is
  the kind of statement that carries a date." Apart from item 2, B1 does not present an SI decision
  as a fact of nature.
- C10 and C11 are genuinely derived, not asserted. C10 builds the conversion factor from "anything
  divided by itself is one" and shows the inverted case producing `kg²/g`; C11 builds the check from
  cancelling, which C05 supplies. Neither hides a step in the derivation itself.
- `books/B0/INVENTORY-part-B.md` types B1 as `mixed` where the record types it `institutional`. The
  record is right and the inventory's label is loose; nothing follows from it.
- Drill counts match the inventory's ranges: C10 has 8 against "6–8", C11 has 14 against "12–16".
