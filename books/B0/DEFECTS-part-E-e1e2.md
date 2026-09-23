# Book 0 · Part E · audit of E1 and E2

Records audited: `check/records/B0/B0-R0-C31.yml` (E1, atoms and bonds) and
`check/records/B0/B0-R0-C32.yml` (E2, chemical energy and the bomb calorimeter).

Audited 23 September 2026 against the files in `sources/`, by the method in `claude.md` §7b and
§8. Every `definition.references[].quote` and every `illustration.numbers[].quote` in both
records was located in the file `sources/INDEX.yml` maps its citekey to, and read in its
surrounding paragraph. All twelve of E2's practice answers were recomputed line by line rather
than read.

`python check/build.py --check` reports **blocking 0** and names neither record in its 75
warnings. Everything below is invisible to the build, which is why the audit is a step.

**Count: 16 defects — 1 critical, 5 major, 3 moderate, 7 minor.**

---

## Critical

### 1. E2 teaches "two steps and only two" and the report carries three

- **Concept** `B0-R0-C32`
- **Fields** `definition.text`; `simplified_explanation`; `illustration.body`;
  `must_know[1]` (the `trap` point); `retrieval_items[2]`

**The claim the record makes.** `definition.text`: *"What remains after those losses is
metabolizable energy. That is the whole cascade the Organization's 2003 report carries, and it
has no digestible-energy step in it."* `simplified_explanation`: *"Two steps, then, and only
two: gross energy, then metabolizable energy."* `illustration.body`: *"Two steps. Gross energy,
then metabolizable energy, with named losses in between."* And the `trap` point arms a refusal
on it: *"Its cascade runs gross or ingested energy straight to metabolizable energy... If
somebody offers you a three-way gross, digestible and metabolisable split and cites this report,
the citation does not hold. Say so."*

**What the source actually says.** FAO 77 §3.3, second paragraph, transcribed verbatim at
`sources/fao_food_energy.txt` line 56:

> Not all metabolizable energy is available for the production of ATP. Some energy is utilized
> during the metabolic processes associated with digestion, absorption and intermediary
> metabolism of food and can be measured as heat production; this is referred to as
> dietary-induced thermogenesis (DIT), or thermic effect of food... When the energy lost to
> microbial fermentation and obligatory thermogenesis are subtracted from ME, the result is an
> expression of the energy content of food, which is referred to as **net metabolizable energy
> (NME)**.

The same source file states the cascade in its own words at lines 70–72: *"The report's own
energy cascade runs gross/ingested energy (GE/IE) -> metabolizable energy (ME) -> net
metabolizable energy (NME)."*

So the drafter's true finding — that there is no *digestible-energy* step — was generalised into
a false one: that there is no third step at all. The report has a third step. It is NME, and it
sits below ME rather than between GE and ME.

**Why this is the worst defect in either record.** It is not a wrong sentence, it is a trained
refusal. The `trap` point tells the reader to say out loud, in public, that a three-step citation
of this report does not hold. A reader who deploys that against somebody correctly citing
GE → ME → NME is wrong in the one situation the whole course exists to make them right in. And
the error is upstream: `books/B0/READY-part-E.md` finding 4 and `books/B0/INVENTORY-part-E.md`
both state the two-step cascade, so fixing the record alone leaves the error in the gate document
for the next Part to inherit.

**Smallest change that fixes it.** Narrow every one of the five statements to the word
*digestible*, and add NME as what the third step actually is:

- `definition.text`: *"What remains after those losses is metabolizable energy. Below that the
  report carries one further step, net metabolizable energy, which takes off the energy spent on
  digesting and processing the food. What the report has no step for anywhere is digestible
  energy."*
- `simplified_explanation` and `illustration.body`: replace *"Two steps, then, and only two"*
  with *"Gross energy, then metabolizable energy. The report carries one more step below that and
  no step above it called digestible energy."*
- `must_know[1]`: the refusal must bite on the word, not on the count — *"If somebody offers you
  a gross, **digestible** and metabolisable split and cites this report, the citation does not
  hold, because the phrase digestible energy does not occur in it."*
- Correct `READY-part-E.md` finding 4 and the E2 line of `INVENTORY-part-E.md` in the same pass.

---

## Major

### 2. E2's Atwater paragraph states the fibre rule the source it stands on denies

- **Concept** `B0-R0-C32`
- **Field** `definition.text`, the paragraph on the Atwater general factors

**The claim the record makes.** One paragraph carries, in sequence: the FAO description of the
general factor system, the FAO values, and then *"The carbohydrate amount is discounted a certain
amount for the fibre content, which is indigestible carbohydrate."* The reader gets one account
of one system.

**What the source actually says.** The fibre sentence is genuine — OpenStax Chemistry 2e §5.2,
transcribed at `sources/openstax_chemistry_2e.txt` line 262 — and it is cited correctly as
`definition.references[12]`. But FAO 77 §3.5.1, in the same paragraph the record takes its
factors from (`sources/fao_food_energy.txt` line 87), says the opposite about the same system:

> As originally described by Atwater, carbohydrate is determined by difference, and thus includes
> fibre.

This is the defect class the audit is for: a quote that is genuinely in its source and does not
support the claim it has been attached to. Placed beside the FAO factors, the OpenStax sentence
makes a composite claim about the Atwater general factor system that FAO explicitly contradicts.
It matters because the record then teaches the reader to recompute a label, and the two rules give
different answers on any food with fibre in it.

**Smallest change that fixes it.** Move the fibre sentence out of the Atwater paragraph and label
whose practice it describes: *"One thing the general system does not do is take fibre out.
Atwater's carbohydrate is worked out by difference and includes the fibre. Label systems differ:
a US label discounts the carbohydrate for its fibre content, and an Indian label gives dietary
fibre its own factor of 2 kilocalories a gram under regulation 5(3)(e)(i)."* The Indian figure is
at `sources/fssai_labelling_2020.txt` line 483 and is already a cited source in this record.

### 3. Three of E2's practice problems carry invented calorimeter constants with no flag

- **Concept** `B0-R0-C32`
- **Fields** `practice[1]` (level 2), `practice[2]` (level 2), `practice[8]` (level 7)

**The claim the record makes.** `practice[1]`: *"A calorimeter's energy equivalent is 9,500 joules
for each degree."* `practice[2]`: *"A sample whose energy is known to be 44,000 joules is burned
in a calorimeter. The thermometer rises by 4.00 degrees"* — giving 11,000 joules per degree.
`practice[8]`: *"the calorimeter is worth 10,000 joules for each degree"*, with readings of 21.4
and 24.9 degrees. None of the three says the figures are made up, and none carries `refs`.

**What the source actually says.** Nothing. No whole-instrument energy equivalent exists anywhere
in `sources/`. The drafter is right that every such figure in E2 is invented, and right that it
is flagged in three places — `illustration.body`, `illustration.analogy_breaks_when`, and
`practice[5]` (*"Every figure in this problem is made up"*) — plus `practice[7]` (*"All the
figures are made up for this problem"*), `practice[9]`, `practice[11]` and the `critique`
exercise. The flag is on seven of the ten places it is needed. These three are the gap.

`claude.md` §7a names this exactly: *"Never invent a statistic to make a problem feel applied...
it is worse, because the reader is about to do arithmetic on it and remember the result."* The
three figures are plausible magnitudes for a real bomb calorimeter, which is what makes them
stick.

**Smallest change that fixes it.** One sentence at the end of each of the three prompts: *"The
figures in this problem are made up."*

### 4. The "each column rounded separately" rule the reader is given is false for fat

- **Concept** `B0-R0-C32`
- **Fields** `illustration.body`; `practice[4]` (level 4) answer;
  `illustration.analogy_breaks_when` (by omission)

**The drafter's first flagged item, settled: both halves of it are true.** Checked against
`sources/fao_food_energy.txt` lines 87 and 91.

```
17   divided by 4.184 = 4.063    printed beside it: 4.0
16.7 divided by 4.184 = 3.991    rounds to 4.0
37   divided by 4.184 = 8.843    printed beside it: 9.0
37.4 divided by 4.184 = 8.940    rounds to 8.9, not 9.0
9.0  times   4.184 = 37.66       neither 37 nor 37.4
```

**The claim the record makes.** The record's handling of protein is correct and is well taught —
the illustration walks the reader into the discrepancy through a real sum and then resolves it,
and `practice[4]` drills it. But `practice[4]`'s answer then generalises: *"The kilojoule column
has been rounded to whole numbers and the kilocalorie column to one decimal place, separately."*

**What the source actually says.** Footnote 9 gives the precise values as *"16.7, 37.4, 16.7 and
28.9 kJ/g"* — so for protein and carbohydrate the printed kilocalorie figure is the rounded
conversion of the precise kilojoule figure, and for fat it is not, in either direction. The rule
the reader is handed breaks on one of the three factors the same section prints, and the record
has just taught them the habit of converting to check.

**Should the fat case be in the reader-facing text? Yes** — but as a boundary, not as a second
worked example, which would cost a page and teach the same move twice.

**Smallest change that fixes it.** Two sentences in `illustration.analogy_breaks_when`: *"The
pairing holds for protein and for carbohydrate and not for fat. 37.4 divided by 4.184 is 8.94,
and the report prints 9.0, so fat's two figures are not conversions of one another at all. Read
each column as its own set of numbers and do not derive one from the other."* And soften
`practice[4]`'s closing generalisation to *"The two columns were set down separately, and for
protein the precise kilojoule figure does round to the printed kilocalorie one."*

### 5. FAO 77 carries half of E2 and never reaches the reader's reference list

- **Concept** `B0-R0-C32`
- **Field** `definition.references` (absence), and `check/build.py` `Cites.mark`

**The drafter's second flagged item, settled: the diagnosis is right, the workaround is honest,
and it is not sufficient.**

**What the record does.** The `AUDIT NOTE` on `definition.references[13]` states the problem
plainly and in the right place: `fao_food_energy_2003` is a `consensus_statement`, `KIND_FOR_TYPE`
(`check/build.py` line 38) allows only `textbook`, `primary` or `systematic_review` on an
`empirical` concept, so the source is carried on `must_know[].refs` and on
`illustration.numbers[].citekey` instead, where the build does check its quotes. That is honest.
Nothing is smoothed over.

**Why it is not sufficient.** Two things follow that the note does not reckon with.

First, `definition.text` now contains a large block of claims with **no reference of any kind
behind it**: the FAO naming of ingested and gross energy, the four named losses, metabolizable
energy, the negative claim about the digestible-energy step, the six Atwater values, and *"based
on the heats of combustion of protein, fat and carbohydrate, corrected for losses in digestion,
absorption and urinary excretion of urea."* All fourteen listed references are OpenStax, and
OpenStax §5.2 contains none of that material. `claude.md` §8's minimum of one reference of the
right kind is met, and the rule it was written to enforce is not.

Second, and this is the part no note can fix: `Cites.mark` (`check/build.py` line 1107) builds the
reader's numbered reference list from `definition.references` and from nowhere else. So FAO 77
gets no bracketed number anywhere in Part E, no entry in the Part's bibliography, and not even a
line in the outstanding list underneath it. The reader meets it only as a URL inside the
illustration's prose, which `claude.md` §4 permits for an illustration but which was never meant
to be the only route to a source the section's second half rests on.

**This needs a decision above the record level**, because no edit inside the record can reach it.
Three routes, in order of preference:

- **(b) is the one the specification has already chosen.** `claude.md` §4 says, verbatim:
  *"Atwater's 4/9/4 is `institutional`, because a body adopted those rounded values and can
  revise them."* The specification already classifies this material. E2 has been drafted as one
  `empirical` concept carrying institutional content, which is what produced the collision. Split
  the Atwater and cascade material into its own `institutional` concept, or set E2's
  `concept_type` to `institutional` and take the bomb calorimeter from a textbook on the other
  side. Either way `consensus_statement` becomes legal and the citation renders.
- **(a) is the cheap repair.** Let `Cites.mark` also draw numbered entries from `must_know[].refs`
  and `illustration.numbers[].citekey`. This gets the reader a reference they can open without
  reclassifying anything, and it fixes the same hole for every future record.
- **(c) is the one to refuse.** Widening `KIND_FOR_TYPE["empirical"]` to admit
  `consensus_statement` would let a WHO or professional-body statement stand behind any empirical
  claim in the corpus, which is the distinction §4 exists to hold.

### 6. E2's institutional content runs on an empirical review clock with no as-of date

- **Concept** `B0-R0-C32`
- **Fields** `review`; `illustration.numbers[5]` and `[6]`

**The claim the record makes.** `review.stability: medium`, `review.trigger: '2029-09-23'`, no
`review.as_of`. `illustration.numbers` stamps `as_of: '2026-09-23'` on the FAO entries, the
footnote-9 entry and the NIST entry, and stamps nothing on the two Schedule II figures.

**What the sources actually are.** Two of E2's four sources are live instruments.
`sources/fssai_labelling_2020.txt` is compendium **Version-VIII, dated 09.09.2025** — amended
within the last twelve months, and the record cites regulation 5(3)(e)(i) from it in
`must_know[5]` and `practice[10]`. `sources/nfsa_2013.txt` line 1159 carries section 37, *"Power
to amend Schedules"*: *"If the Central Government is satisfied that it is necessary or expedient
so to do, it may, by notification, amend Schedule I or Schedule II..."* So 700 and 20 are exactly
the figures that can change without anything about the world changing, and they are the only two
in the record with no as-of stamp. `claude.md` §4 requires an **event** trigger on institutional
content, not a date.

**Smallest change that fixes it.** Add `review.as_of: '2026-09-23'`; add `as_of: '2026-09-23'` to
the two `nfsa_2013` numbers; and add an event line to `review.trigger` naming *next notification
amending NFSA Schedule II under section 37* and *next amendment of the FSS (Labelling and Display)
Regulations 2020*. If defect 5 is settled by splitting the concept, the institutional half takes
`stability: short` and this resolves with it.

---

## Moderate

### 7. E2's calibration note asserts an identity the source does not state

- **Concept** `B0-R0-C32`
- **Field** `definition.references[6].verified.note`

**The claim the record makes.** *"The book's name for what the calibration finds is the heat
capacity of the calorimeter. This record calls the same quantity the calorimeter's energy
equivalent, in joules for each degree... **The quantity is identical; only the name differs.**"*

**What the source actually says.** The quote cited is genuine — *"Bomb calorimeters require
calibration to determine the heat capacity of the calorimeter and ensure accurate results"*
(`sources/openstax_chemistry_2e.txt` line 249) — and it does not establish the identity. The
book's own worked example, two lines later at line 251, uses the phrase the other way:

> When 3.12 g of glucose... is burned in a bomb calorimeter... **The calorimeter contains 775 g
> of water, and the bomb itself has a heat capacity of 893 J/°C.**

There the heat capacity is the bomb alone and the water is accounted for separately, whereas the
record's energy equivalent is the whole assembly, water included. The book uses the phrase both
ways on one page. The record's note flattens that into an identity and hands the flattened version
forward to whoever writes E4.

Nothing reader-facing is wrong: the instrument as E2 teaches it — calibrate the whole thing once,
then multiply — is how a bomb calorimeter is actually used, and the ordering resolution in
`INVENTORY-part-E.md` stands.

**Smallest change that fixes it.** Replace the last sentence of the note with: *"The book uses the
phrase both ways on the same page — for the calibrated whole in the calibration sentence, and for
the bomb alone in Example 5.7, where 893 J/°C sits beside 775 g of water counted separately.
Whoever writes E4 has to say which one the phrase means there."*

### 8. E2 names four losses in some places and three in others, and claims the report names three

- **Concept** `B0-R0-C32`
- **Fields** `simplified_explanation`; `must_know[0]`; `exercises[1].answer`;
  `exercises[2].answer`; `practice[11].answer`

**The claim the record makes.** `definition.text` and `illustration.body` name four losses —
faecal, gaseous, urinary and surface. `simplified_explanation` says *"Three things happen to that
energy on the way through"* and names three. `must_know[0]` says *"losses in the faeces, in gas
from the large intestine, and in the urine. The Food and Agriculture Organization's 2003 report
**names all three**."*

**What the source actually says.** `sources/fao_food_energy.txt` line 51: *"A small amount of
energy is also lost from the body surface (surface energy [SE])."* The report names four. The
must-know point's claim about the source understates it, and `claude.md` §10 rule 2 is breached
by the drifting count.

**Smallest change that fixes it.** In `must_know[0]`, *"names all three"* → *"names those three
and a small surface loss besides"*. In `simplified_explanation`, *"Three things happen"* →
*"Several things happen"*, and add the surface loss to the list as one clause.

### 9. E2's made-up disclaimer covers the real figures that follow it

- **Concept** `B0-R0-C32`
- **Field** `illustration.body`

**The claim the record makes.** *"All the numbers from here to the end of this part are made up
for the example. No real calorimeter and no real food is being described."*

**What follows it in the same illustration.** The real 4.184 from NIST, the real Atwater factors
from FAO 77, and the real 700 and 20 from Schedule II of the National Food Security Act — with
their URLs given to the reader and their citekeys in `illustration.numbers`.
`illustration.analogy_breaks_when` gets the scope exactly right: *"Only the 4.184, the Atwater
factors and the two Schedule II figures come from a source."* The two fields contradict each
other, and the reader meets the wrong one first.

**Smallest change that fixes it.** *"Every figure in this calorimeter example is made up."*

---

## Minor

### 10. Four practice problems quote real figures with no `refs`

`B0-R0-C32`, `practice[0]` (4.184), `practice[3]` (4.0, 9.0, 4.0), `practice[7]` (4.0, 9.0, 4.0
and 4.184), `practice[9]` (4 and 9). `claude.md` §7a: *"A problem quoting a real number names its
`citekey` in `refs`."* Levels 4, 5, 9 and 10 do it; these four do not, so the set is inconsistent
with itself. Fix: add `refs: [nist_sp811]` or `[fao_food_energy_2003]` as applicable.

### 11. E2 uses stocks and flows and does not declare it

`B0-R0-C32`, `concept_deps`. `practice[11]`'s answer says *"The section on stocks and flows says
why you cannot assume that. The balance line holds whatever the flows do."* That is `B0-R0-C23`
(Part C section 9; Part A is eight sections and Part B six, so C9 is sequence 23). `concept_deps`
lists `C04`, `C05`, `C10`, `C12` and `C31` only. The reference is backward, so the build does not
block, but the dependency graph is wrong and any micro-refresher generated from it will be short.
Fix: add `B0-R0-C23` to `concept_deps`, and to E2's Book 0 deps column in `INVENTORY-part-E.md`.

### 12. A `number` must-know point carrying six figures

`B0-R0-C32`, `must_know[3]`. `claude.md` §5: *"`number` points carry one figure with its unit and
source, not a list."* The point lists 17, 4.0, 37, 9.0, 17 and 4.0. It passes the admission test
on its last sentence and is worth keeping. Fix: drop the `kind: number` tag, or keep the tag and
cut the point to the one figure it turns on.

### 13. One working line missing from E2's illustration

`B0-R0-C32`, `illustration.body`. The kilocalorie route shows `0.114 times 100 = 11.4`; the
kilojoule route goes from `340 divided by 2,928.8 = 0.116` straight to *"Eleven point six per
cent"* with no multiplication line. `claude.md` §4: a reader who cannot follow line three cannot
skip to line four, and the whole point of the passage is that the two routes are parallel. Fix:
add `0.116 times 100 = 11.6`.

### 14. E1 says the page gives three numbers in kilojoules; it gives them in kilojoules per mole

`B0-R0-C31`, `illustration.body`. The record writes *"The page gives you all three numbers, in
kilojoules"* over a table headed *"energy in kilojoules"*. OpenStax 7.5
(`sources/openstax_chemistry_2e.txt` lines 104 and 128) gives 436 kJ/mol, 243 kJ/mol and 432
kJ/mol; only the −185 kJ is a plain kilojoule figure. The record's own `illustration.numbers`
units say *"per mole of bonds broken"*, so the audit trail is right and the reader-facing sentence
is not. The next paragraph mitigates well — *"Each one is the energy for a fixed, standard amount
of the substance, and it is the same fixed amount in all three"* — and the mole-free treatment is
the right call under the inventory's scope cut. Fix: *"The page gives you all three numbers, in
kilojoules for a fixed standard amount of each"*, and head the table column *"energy in
kilojoules, per fixed standard amount"*.

### 15. E1's endothermic sentence has no quote behind it

`B0-R0-C31`, `definition.text` and `definition.references[12]`. The reference quotes only the
exothermic sentence. The record also asserts *"Where the bonds in the products are weaker, the
reaction absorbs heat and is called endothermic."* The source states it in the very next sentence
— *"An endothermic reaction (ΔH positive, heat absorbed) results when the bonds in the products
are weaker than those in the reactants"* (`sources/openstax_chemistry_2e.txt` line 113) — and it
is not in the `quote`, so the build checks only half of what the record claims. Fix: extend the
quote to both sentences.

### 16. Two unsourced claims in E1's reader-facing prose

`B0-R0-C31`, `simplified_explanation` and `retrieval_items[4]`: *"Table salt is held together this
way"* (ionic) and *"Most of what is in a food is held together this way"* (covalent). Neither is
in any quoted passage. The salt claim is inferable from 7.2's metallic/nonmetallic sentence plus
2.4's *"sodium and chlorine can react to form table salt"*, and the claim about food is nowhere in
the source pack. Both are small and both are the shape §7b warns about — written from what the
model knows, sitting next to citations that cover the sentences around them. Fix: locate the food
claim in `openstax_chemistry_2e` or `openstax_biology_2e` and add a reference, or reword to
*"covalent bonds are the ones this course will keep meeting"*, which claims nothing about the
world.

---

## What was checked and held

A clean finding stated is worth as much as a defect. These were opened, searched and recomputed,
and nothing was wrong with them.

**Every quote is in its file, and every quote behind a number states that number.** All fifteen
`definition.references` quotes in E1, all fourteen in E2, and all thirteen
`illustration.numbers` quotes across both records were located as exact substrings in the file
`sources/INDEX.yml` maps their citekey to, and read in their surrounding paragraph. No citekey
resolves to a `do_not_cite` file. On the specific failure mode named in the brief — a citation
that passes by containing the value's digits somewhere without stating the figure — **there are
no instances in either record.** Each of the thirteen quotes states its value as a figure: 436,
243, 432 and 864 are each printed with their bond in E1; −185 is the source's own arithmetic line
`[436+243]−2(432)=−185kJ`; 17, 4.0, 37 and 9.0 are all in the one FAO sentence that assigns them
to their substrates; 16.7 is in footnote 9's `respectively` list; 700 and 20 are the Schedule II
row `Upper primary classes Hot Cooked Meal 700 20` at `sources/nfsa_2013.txt` line 1480; and
4.184 is `calth = 4.184 J exactly` in the NIST footnote. **No `derived` declaration is missing**,
because no figure in either record is counted or worked out from a passage rather than stated in
it. There is no `derived` field in `check/schema/concept.schema.json`; none is needed here, and
the convention will first be needed elsewhere.

**All twelve of E2's practice answers are arithmetically correct.** Recomputed line by line, not
read. `2,092 ÷ 4.184 = 500` exactly. `9,500 × 3.4 = 32,300`; `÷1,000 = 32.3`. `44,000 ÷ 4.00 =
11,000`. `12×4 = 48`, `8×9 = 72`, `40×4 = 160`, sum `280`; and the aside checks —
8 g is a fifth of 40 g, and 72 is 45 per cent of 160, which is *"almost half"*. `17 ÷ 4.184 =
4.0631` shown as 4.063; `16.7 ÷ 4.184 = 3.99139` shown as 3.991. `52,500 ÷ 3.50 = 15,000`;
`×2.80 = 42,000`; `÷1,000 = 42`; `÷2.00 = 21`. `12×4.0 = 48`; `48÷450 = 0.1066666667`; `0.107×100
= 10.7`. `8,000×2.50 = 20,000`; `÷1,000 = 20`; `÷1.25 = 16`; `16 ÷ 4.184 = 3.82409` shown as
3.824; `0.10×4.0 = 0.4`, `0.05×9.0 = 0.45`, `0.70×4.0 = 2.8`, sum `3.65`; `3.824 − 3.65 = 0.174`.
`24.9 − 21.4 = 3.5`; `10,000×3.5 = 35,000`; `÷1,000 = 35` — and the deliberately wrong prompt is
internally consistent at `10,000 × 24.9 = 249,000`, which is what makes it diagnosable.
`30×4=120`, `6×4=24`, `5×9=45`, sum `189`; the wrong total `237` is right for the wrong method;
`237−189 = 48`; `48÷189 = 0.253968254`; `0.254×100 = 25.4`; and the weights check, `30+12+6+5 =
53` against a 30 g carbohydrate total. `250 × 4.184 = 1,046` exactly. `20×4.0 = 80`; `80÷700 =
0.1142857143`; `0.114×100 = 11.4`, with *"the other eighty-nine per cent"* right for 88.6. The
illustration's own eleven lines were recomputed too and are all correct, including `26,400 ÷ 2.2
= 12,000`, `14.8 ÷ 4.184 = 3.5373` and `700 × 4.184 = 2,928.8`.

**The drill set climbs and reaches both ends.** Levels run 1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10 —
four mechanical, four applied, two diagnostic, two transfer. All four bands are touched, so the
build's ladder check passes on substance and not only on count. The set is not twelve problems at
one difficulty with different numbers: `practice[2]` deliberately reverses `practice[1]` (given
the constant find the energy, then given the energy find the constant), `practice[7]` sets the two
methods against each other, the diagnostic pair breaks in two different ways (a reading used as a
rise; a nested label line double-counted), and the transfer pair asks two different refusals. One
soft mismatch worth noting rather than fixing: `practice[3]` is tagged level 3, which is the
mechanical band — *"bare numbers, one step, no context, no unit"* — and it carries grams, a food
and three multiplications. It reads as an applied problem sitting a band low. The set still
reaches the mechanical band through levels 1 and 2, so nothing breaks.

**The scope cuts held.** The mole and Avogadro's number do not appear in any reader-facing field
of either record. The word *mole* occurs only in E1's `illustration.numbers[].unit` and `quote`
fields and in one audit note in E2 — and `check/build.py` renders `illustration.numbers` to
`numbers_register.csv`, never into the booklet, so the audit trail keeps the honest unit while
the reader never meets it. *Avogadro* occurs nowhere. No chemical equation is balanced anywhere
in either record. **No kilocalories-per-kilogram-of-body figure appears**, and the refusal is not
merely passive: `illustration.body` says *"you have nothing at all about what any one child
spends, or about what a change in anybody's body would be made of. This book does not carry
either number, and you should not supply one from memory"*, and `practice[10]`'s answer repeats
it — *"You would need to know what a kilogram of that change is made of. This book does not give
you that number... Do not supply it from memory."* Book 0 C9's refusal is intact and E2 actively
defends it.

**§9 holds in both records.** No moral vocabulary for eating or weight anywhere: no *cheating*,
*being good*, *indulgence*, *guilt* or *bad foods*; no *obese person* construction; no
before-and-after framing. **No example turns on a person's willpower.** The one place the pull
exists is `practice[11]`, where a school meal might displace food eaten at home — and it is
written as a measurable behavioural question with a named remedy (*"Whether a school meal
displaces food at home is a question about behaviour, and it has to be measured, not assumed"*),
not as anybody's failure. Neither record carries prevalence or risk framing at all.

**§5's admission test holds on all fourteen must-know points.** Every point in both records
changes something the reader would do, say, accept or refuse. In particular, **neither `boundary`
point describes the scope of its section.** E1's — *"Bond energies give you the size of an energy
change and nothing else. They cannot tell you whether the reaction happens, or how fast, or what
starts it"* — is a limit of the technique. So is E2's — *"a figure worked out from them can tell
two foods apart only by their grams. It cannot show that one food is taken up better than another.
It is the wrong tool for that question, and no amount of precision fixes it."* Both name when to
stop trusting the tool. Neither has *this section* as its subject. E1 carries six points, E2
eight, both under the soft cap of nine, and both carry a `misconception` and a `trap`. Bearings
are spread across all five capacities in E2 and four of five in E1.

**Currency, beyond what defect 6 names.** `nist_sp811` needs no review clock at all: the file's
own last line reads *"Defined (not measured) value"*, and `calth = 4.184 J exactly` is a
definition, not a measurement. The four OpenStax texts are stable and the excerpt-only caveat in
`sources/INDEX.yml` did not bite — every quote was found. One item for the next reviewer that is
not a defect today: **FAO Food and Nutrition Paper 77 is twenty-three years old**, and the same
report recommends moving toward net metabolizable energy for some purposes. If a successor
conversion-factor report appears, E2's whole second half is the first thing to re-read. That
belongs in the event trigger defect 6 asks for.

**E1's sign convention is consistent everywhere, which was worth checking.** `definition.text`,
`simplified_explanation`, the illustration's `679 minus 864 = -185`, the retrieval exercise's
*"Take the second away from the first"* and `retrieval_items[2]`'s *"subtract the second from the
first"* all give bonds-broken minus bonds-formed, and all pair a negative answer with heat
released. A half-sum or a flipped sign in any one of the five would have read as plausible prose.
There is none.

**The dependency declarations match the inventory.** E1's `concept_deps` `C06` and `C09` are A6
and B1; E2's `C04`, `C05`, `C10`, `C12` and `C31` are A4, A5, B2, B4 and E1 — exactly the Book 0
deps columns of `INVENTORY-part-E.md`, once the outline's part sizes are counted (A 8, B 6, C 9).
The single omission is at defect 11. No forward reference exists in either record. E1's
`quantitative: false` follows the inventory's judgement and survives inspection: its illustration
does arithmetic, but none of its exercises or retrieval items requires the reader to carry a
calculation out.

**Both records pass `python check/build.py --check` with zero blocking failures and appear in
none of its 75 warnings.** Every defect above is one the build cannot see.
