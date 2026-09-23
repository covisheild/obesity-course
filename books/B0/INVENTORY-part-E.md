# Book 0 · Part E concept inventory

Sections E1 to E8 of `check/book0/OUTLINE.md`, which are sequence positions 31 to 38 and therefore
records `B0-R0-C31` to `B0-R0-C38`. Produced 23 September 2026 against frozen map
`fc19c8bc-a216-4131-99fb-ebe3f19cec4a`, by the method in the specification §5.

---

## What makes Part E different, and this time it is the subject matter

Parts A to D are mathematics. Part F is reading and reasoning. Every section written so far has
been either something the reader can rebuild from the floor with a calculator, or something a body
decided and wrote down. **Part E is the first Part that is neither.** A reader cannot derive the
plasma membrane from arithmetic, and no Act established it.

That is not a presentational difficulty. It broke the concept-type taxonomy, and the taxonomy is
enforced by the build. Before this Part, `empirical` accepted only `primary` and
`systematic_review` — so marking "a cell has a plasma membrane" empirical would have demanded a
research paper for the existence of the cell. Marking it `derivable` would have made that word mean
two different things in one corpus.

`empirical` now accepts a `textbook` anchor, changed at the reader's direction on 23 September 2026.
The rule that replaces the machine check is in `claude.md` §4 and it is a rule of judgement:
**a claim with a number attached to it is not settled science.** An effect size, a risk, a
dose-response, a prevalence, a measured rate — those still need primary evidence. The audit is what
enforces that now, because no check can.

**This Part is where that gets tested**, so the type column below is not routine. Three of the
eight sections carry all three types between them.

## The second thing that makes it different: nothing here is a chain, and two things are gates

Part C was a chain — nine sections where nothing stood alone. Part E is closer to Part A: mostly
independent sections, with two real dependencies inside the Part and one awkward ordering problem.

```
E1 atoms and bonds ─── E2 chemical energy and the calorimeter
                  └─── E6 metabolism
E3 conservation and the boundary   (stands on Book 0 section C9, record B0-R0-C23)
E4 heat and temperature            (stands on E2, and repairs it)
E5 the cell ─── E6 metabolism ─── E8 organs
E7 genes                           (stands on E5)
```

**The ordering problem, and it is real.** E2 teaches the bomb calorimeter, which measures energy by
a temperature rise. Specific heat capacity — the thing that turns a temperature rise into an energy
— is E4, two sections later. `claude.md` §10 rule 1 forbids a forward reference, and the concept
ids are fixed by the outline and may never be renumbered, so E2 and E4 cannot be swapped.

**The resolution, and it happens to be how the instrument really works.** A bomb calorimeter is
*calibrated*: a substance of known energy is burnt in it, the temperature rise is measured, and the
ratio gives the calorimeter's energy equivalent in joules per degree. Thereafter a temperature rise
converts to an energy by that one constant. E2 teaches it that way and needs no specific heat at
all. E4 then defines heat capacity properly, and opens on the misconception E2's reader may have
picked up — that a bigger temperature rise means more heat. That is `claude.md` §4's "lead with the
failure" arriving for free, and it is a better section than the one that would have been written
without the constraint.

E2 uses *temperature* as an everyday word — a thermometer reading goes up — which §11 rule 1
permits. E4 is where the word becomes technical.

---

## The inventory

Type is `d` derivable, `e` empirical, `i` institutional. **Q** is whether the concept is
quantitative and therefore owes a drill set.

| # | Record | Concept | Type | Q | Book 0 deps | Source it needs | Serves |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | `B0-R0-C31` | Atoms, molecules and bonds, and that a bond is where chemical energy sits | e | no | A6, B1 | `openstax_chemistry_2e` 2.3, 2.4, 7.2, 7.5 | S01 C03, C05 |
| E2 | `B0-R0-C32` | Burning a food releases its chemical energy; a calibrated bomb calorimeter measures how much; and not all of it reaches a person | e | **yes** | A4, A5, B2, B4, C9 (`B0-R0-C23`), E1 | `openstax_chemistry_2e` 5.2, 5.3; `fao_food_energy_2003` 3.2, 3.3, 3.5.1; `nist_sp811`; `nfsa_2013` Sch II | S01 C05, C06, C07 |
| E3 | `B0-R0-C33` | Energy is conserved; drawing a boundary is what makes that countable | d | **yes** | A4, C9 (`B0-R0-C23`) | `openstax_college_physics_2e` 7.6; `openstax_chemistry_2e` 5.2 | S01 C09, C10 |
| E4 | `B0-R0-C34` | Heat is not temperature; heat capacity relates them; heat moves three ways | e | **yes** | A5, B1, B2, E2 | `openstax_college_physics_2e` 14.1, 14.2, 14.4 | E2's calibration constant; S01 later rungs |
| E5 | `B0-R0-C35` | A cell, its membrane, the proteins in it, and what a receptor does | e | no | — | `openstax_biology_2e` 4.1, 4.3, 5.1, 5.3, 3.4, 9.1 | floor for every drug and hormone concept |
| E6 | `B0-R0-C36` | Metabolism is chemistry happening in a body: catabolism releases, anabolism builds, ATP carries | e | no | E1, E5 | `openstax_anatphys_2e` 24.1, 24.2, 24.3; `openstax_biology_2e` 7.1 | S01 C07 |
| E7 | `B0-R0-C37` | Genes, DNA and inheritance, in outline and no further | e | no | E5 | `openstax_biology_2e` 14.2, 12.2 | floor for S16 |
| E8 | `B0-R0-C38` | The organs that matter for metabolism, and what each one does | e | no | E5, E6 | `openstax_anatphys_2e` 23.6, 23.7, 17.1, 17.9 | replaces the removed MBBS assumption |

### Why E3 is the only `derivable` one

The specification's own example list for `derivable` names conservation of energy. It is there
because the reader really can rebuild it: once a boundary is drawn, "what is inside changes by what
crossed in minus what crossed out" is an accounting identity, and Book 0 section C9, record `B0-R0-C23`, has already taught stocks and flows. E3 derives it and shows the steps. Everything else in the Part is a fact about
how the world turned out.

### Why three sections are quantitative when Part E derives to false

`claude.md` §7a derives a Part E record as not quantitative, and for five of the eight that is
right — the reader has to be able to *state* what a receptor does, not carry anything out. Three
teach a technique the reader must be able to perform, and are set `quantitative: true` explicitly:

- **E2** converts between kilojoules and kilocalories, turns a calibrated temperature rise into an
  energy, and applies the Atwater factors to a food. Three moves that compose.
- **E3** draws a boundary, lists what crosses it, and computes the change in the store. This is the
  move S01's whole accounting identity stands on.
- **E4** uses `Q = mc(Delta)T` in both directions, and converts a heat capacity into an energy.

§7a says the permissive error is the cheap one, and a technique shipped that nobody can perform is
the expensive one. E6 was the close call and is set to false: its job is to let the reader say what
catabolism and anabolism are, and the arithmetic a reader might do on it is E3's, already drilled.

### Drill-set sizes, and the reasoning for each

The count is three to eighteen, chosen from the technique, and the set must reach both the
mechanical and the transfer band.

| Record | Problems | Why that number |
| --- | ---: | --- |
| `B0-R0-C32` | 12 | Three moves that compose — unit conversion, calibration constant, Atwater factors — and the transfer band has real work to do, because "this food contains 250 kcal" is the commonest number in the whole subject and the reader must be able to say what it does not establish |
| `B0-R0-C33` | 8 | One move, applied to different boundaries. The variety is in *where the boundary is drawn*, not in the arithmetic, so a long set would repeat itself |
| `B0-R0-C34` | 8 | One formula used in both directions, plus the heat-against-temperature distinction, which the diagnostic band is the right place to test |

---

## What was regressed and then cut, so nobody re-derives it

Chains followed to the floor and cut under §5 step 5 as serving nothing:

- **The mole and Avogadro's number.** E1 can say where energy sits in a bond without it, and B5 has
  already given the reader molar mass for the one place the course needs it. Cutting it keeps E1
  from becoming a chemistry course.
- **Balancing chemical equations.** Nothing above it needs the reader to balance one.
- **Glycolysis, the citric acid cycle and the electron transport chain as named stages.** E6 needs
  the reader to know that glucose is broken down and ATP is made. Naming the three stages adds
  vocabulary and changes nothing the reader would do, say, accept or refuse — §5's admission test,
  applied to a whole topic.
- **Mendelian ratios as arithmetic.** E7 is inheritance *in outline*. The 3:1 ratio is in the
  source and stays out of the record: S16 is where it earns its place, if anywhere.
- **Enzyme kinetics.** E5 teaches that an enzyme speeds a reaction and that its shape is why.
  Everything past that serves no rung in the map.

## The one thing this Part must not do

`claude.md` §9 governs every example here, and Part E is the first Part where it has real work to
do. E6 and E8 are about fat storage, appetite and the organs involved, and the pull toward moral
vocabulary is strongest exactly where the biology is being explained. Adipose tissue stores
triglyceride; that is a function, not a failing. No example in this Part turns on a person's
willpower, and regain, when it is mentioned at all, is a physiological outcome with a mechanism.

---

## Two errors this document introduced, corrected after the audit

Recorded rather than quietly fixed, because both propagated into records before anyone caught
them and the propagation is the lesson.

**1. The FAO cascade.** This inventory and `READY-part-E.md` both said FAO 77 carries a two-step
cascade, gross or ingested energy to metabolizable energy. It carries three: §3.3 names **net
metabolizable energy** below ME. The real finding was only ever that the report has no
*digestible energy* step — one word absent from one source — and it was generalised into a claim
about the whole cascade. E2 then built a must-know point arming the reader to say in public that a
three-step citation of FAO "does not hold", which would have misfired against somebody citing the
report correctly. A reader armed to object is harder to correct than a reader merely misinformed.

**2. Outline labels against record ids.** This document wrote "C9" for the ninth section of Part C,
which is record `B0-R0-C23`. Book 0 also has a record `B0-R0-C09`, which is Part B's first section,
"What a unit is". Two drafters read the label as the record id, and E3 shipped a paragraph
attributing to C9 a refusal that lives in `B0-R0-C23` — and E6 inherited the same error.

The rule that follows, for every later Part: **an inventory names a record by its id the first time
it names it at all**, and a bare section label like "C9" or "A4" is only safe in a column whose
heading says it is an outline position. The two namespaces overlap for thirty-eight of the
forty-three sections and nothing in the build distinguishes them.
