# Book 0 · Part B concept inventory

Sections B1 to B6 of `check/book0/OUTLINE.md`. Produced 22 September 2026 against frozen map
`fc19c8bc-a216-4131-99fb-ebe3f19cec4a`, by the method in the specification §5, adapted to Book 0
as Part A's inventory was: Book 0 has no rung outcomes of its own, so the terminal requirements are
the outline's own notes plus what the sections and subject records above Part B presuppose.

---

## What makes Part B different from Part A, and it is not difficulty

Every Part A section was `derivable`. The reader rebuilds arithmetic from the floor, so an
unopened source blocked a label and not the teaching.

**A unit is not derivable.** The metre is what it is because the CGPM decided so; the calorie is
4.184 joules by definition and not by measurement; a label carries kilocalories because a
regulation says it must. These are `institutional`, and §4 is explicit about the treatment: cite
the instrument, stamp an as-of date, never present as a fact of nature. There is no calculator
check behind any of it.

That changes what the inventory has to decide, so each section below carries its type and its
source, and two sections are held back because their source is not in hand.

---

## The terminal requirements, before regression

**1. The outline's own notes.** B3 "catches a wrong formula without knowing the right one";
B4 "direct dependency of S01"; B5 "needed before any clinical or biochemical number"; B6 "needed
before BMI can be discussed at all".

**2. What Part A leaves unfinished.** A5 teaches ratios and rates as pure numbers. Every rate the
course actually uses carries units — per person per month, per 100 g, per litre — and nothing yet
teaches what happens to a unit when you divide by it.

**3. What the subject books presuppose.** S01 needs energy in both joule and calorie families
before it can discuss intake. Any clinical rung needs mg/dL and mmol/L before a laboratory value
means anything. Every obesity subject needs kg/m² before BMI is discussable at all.

---

## The sections

| § | Concept | Type | Source | Quantitative | Drill set |
| --- | --- | --- | --- | --- | --- |
| B1 | What a unit is; the SI base and derived units | mixed | `bipm_si` — in hand | **false** | none |
| B2 | Converting units as multiplication by one | derivable | OpenStax anchor | true | 6–8 |
| B3 | Dimensional analysis as an error check | derivable | OpenStax anchor | true | 12–16 |
| B4 | Energy units: joule, kilojoule, calorie, kilocalorie | institutional | `bipm_si`, `nist_sp811` — in hand | true | 8–12 |
| B5 | Concentration units: mg/dL, mmol/L, interconversion | empirical | `pubchem_molar_masses` — in hand | true | 12–14 |
| B6 | Body-size units: kg, m, cm, kg/m² | derivable | `bipm_si` for the base units | true | 6–8 |

### B1 · What a unit is; the SI base and derived units — `quantitative: false`

The only Part B section that teaches no technique the reader must carry out, and the default for a
mathematical Part would have made it carry a drill set. Set `quantitative: false` explicitly.

What it must establish: a measurement is a number **and** a unit, and the number alone means
nothing; the SI is defined by seven exact constants rather than by artefacts, which is why a metre
in Raipur is a metre in Paris; and a derived unit is built from base units by multiplication and
division, so `J = kg m² s⁻²` is not a fact to memorise but a statement about what energy *is*.

The last of those is the bridge to B3, and B3 does not work without it.

Cite `bipm_si` with the quote requirement: the constants are stated exactly on that page.

### B2 · Converting units as multiplication by one — `derivable`

One move, applied repeatedly. A conversion factor is a fraction whose top and bottom are the same
quantity written two ways, so it equals one, and multiplying by one changes the name and not the
amount. Rests directly on **A2** (fractions) and **A5** (ratios). Both are declared `concept_deps`.

The failure to inoculate: inverting the factor. A reader who multiplies when they should divide
gets an answer wrong by the square of the factor, and nothing about the number looks wrong.

Six to eight problems: one move, so the ladder is climbed quickly, and the diagnostic band carries
the inversion.

### B3 · Dimensional analysis as an error check — `derivable`

**The section that pays for the Part.** The outline's note is the requirement: it catches a wrong
formula without knowing the right one. A reader who can check that both sides of an equation carry
the same units can reject a wrong formula without being able to derive the right one, which is a
disproportionate return for one technique.

Several moves that compose — strip the numbers, carry the units through multiplication and
division, cancel, compare. **Twelve to sixteen problems**, and this is the section of Part B most
worth over-drilling. Rests on **A5** and on B1's derived-unit construction.

### B4 · Energy units: joule, kilojoule, calorie, kilocalorie — `institutional`

Both sources are in hand and both are quotable. The joule is defined by the SI (`bipm_si`:
`J = kg m² s⁻²`). The calorie is not an SI unit and is fixed by convention — `nist_sp811` states
`calth = 4.184 J exactly`, and separately that the International Table calorie is 4.1868 J, which
is the fact that a reader comparing two papers needs and will not find stated anywhere they look.
NIST also records that "the kilogram calorie or large calorie is an obsolete term used for the
kilocalorie, which is the calorie used to express the energy content of foods".

**Added after the first draft.** The FSSAI labelling compendium is now in `sources/` as
`fssai_labelling_2020.txt`, so the Indian label requirement is written rather than held back.
Regulation 5(3)(b) requires `energy value (kcal)` per 100 g or 100 ml and per serve, with the
share of the Recommended Dietary Allowance worked out on 2000 kcal a day, and requires no
kilojoule figure at all. Regulation 5(3)(e)(i) fixes the factors by which the declared energy is
calculated rather than measured — carbohydrate 4 kcal/g, protein 4 kcal/g, fat 9 kcal/g, alcohol
7 kcal/g and four more. A reader can now recompute a label's energy from its grams and check the
printed figure, and one practice problem makes them do it.

### B5 · Concentration units — **written; molar mass source now in hand**

The distinction is derivable from `bipm_si`: mg/dL is a mass in a volume, mmol/L is an amount of
substance in a volume, and the mole is an SI base unit fixed by the Avogadro constant. The two are
not interchangeable without knowing **what the substance is**, which is the whole teaching point
and the reason a glucose conversion factor does not work for cholesterol.

The interconversion needs a molar mass, which is measured, not decided — an `empirical` claim, so
the record is typed `empirical` and cites `pubchem_molar_masses` as `primary`.

`sources/pubchem_molar_masses.txt` now holds the PubChem records, read in a browser because
PubChem is CAPTCHA-gated. It carries D-glucose's molecular weight, 180.16 g/mol (CID 5793), and it
carries cholesterol's formula, C27H46O (CID 5997), **without** cholesterol's molecular weight,
which was below the fold when the page was captured.

That gap is used rather than filled. The section works the glucose conversion in full and then
stops dead on cholesterol: the reader knows the substance, knows the formula and knows the method,
and still cannot finish without looking the molar mass up. No cholesterol molar mass is supplied
from anywhere, and the section says in as many words why supplying one would be the failure the
source gate exists to stop.

### B6 · Body-size units: kg, m, cm, kg/m² — `derivable`

**Scope discipline is the whole job here.** The outline scopes B6 as units, and that scope holds:
the section teaches that kg/m² is a derived unit like any other, that computing it requires height
in metres and not centimetres, and that the squaring in the denominator is what makes the index
scale-dependent in the first place.

**It does not teach what any value means.** Thresholds are institutional, they differ for Indian
populations, and the 2025 India Obesity Commission statement has moved the definition away from
BMI alone to a staged one. Book 0 must not teach something the subject books then have to unteach —
that is the ground floor failing at its one job. Compute the number, name the unit, and say that
what counts as high is a decision some body has made, is under revision, and is where the subject
books begin.

The must-know point that earns its place here is the unit-mismatch trap: a height entered in
centimetres gives a BMI ten thousand times too small, and the error is so large it looks like a
different kind of mistake.

---

## Dependencies on Part A, declared

| Part B section | Needs | Why |
| --- | --- | --- |
| B2 | A2 fractions, A5 ratios | A conversion factor is a fraction equal to one |
| B3 | A5 ratios | Units cancel the way numbers in a ratio cancel |
| B4 | A3 significant figures, A6 scientific notation | A converted energy value must not gain precision; kJ figures run large |
| B5 | A3, A6 | Same, and lab values are small decimals |
| B6 | A6 powers | The square in the denominator |

## What is being built now, and what is not

All six sections are drafted. **B5 was held at the source gate** and was released when
`pubchem_molar_masses.txt` arrived; **B4** was written without the labelling regulation and was
extended when `fssai_labelling_2020.txt` arrived. Both gaps closed the same way, by somebody
opening a browser, and neither was closed by writing round it.
