# Book 0 · Ground floor

**Scope and ordering. Not written yet.** This is the inventory of what has to exist below every subject booklet, given the reader floor in `SPEC.md` §1: literacy, a calculator, nothing else.

Book 0 exists so that the ground floor is taught **once, properly**, instead of 61 times inconsistently. Each subject booklet then opens with a short micro-refresher covering only the Book 0 sections it actually uses, generated from the union of its concepts' `ground_floor_deps`. A reader can therefore pick up any single booklet and work through it unaided, which is the requirement, without Book 0 becoming a compulsory gate in front of everything.

**Status of this list.** A working scope, deliberately produced before the pilots rather than after, so the pilots can test the Book 0 → refresher → chapter chain end to end. It is revised in the plan's final phase once the pilots show what was missing and what was dead weight. Section count is not a commitment.

**Forty-three sections** across six parts: A 8, B 6, C 9, D 7, E 8, F 5. Counted from the tables below rather than stated from memory.

---

## Part A · Numbers you can trust

| # | Section | Notes |
| --- | --- | --- |
| A1 | Counting, place value, and what a calculator is actually doing | Starts below fractions. Deliberately. |
| A2 | Fractions | |
| A3 | Decimals, rounding, and significant figures | Where false precision begins. |
| A4 | Percentages, and the percentage of a percentage | The single commonest error in health reporting. |
| A5 | Ratios, rates and proportions | Prepares every "per 1,000" and "per person-year" in the course. |
| A6 | Powers, roots and scientific notation | |
| A7 | Logarithms — what they are for before how they work | Needed for odds, pH, log scales on every dose-response figure. |
| A8 | Orders of magnitude and the back-of-envelope sanity check | The habit that makes S01's competency test possible. |

## Part B · Units and dimensions

| # | Section | Notes |
| --- | --- | --- |
| B1 | What a unit is; the SI base units and derived units | |
| B2 | Converting units as multiplication by one | |
| B3 | Dimensional analysis as an error check | Catches a wrong formula without knowing the right one. |
| B4 | Energy units: joule, kilojoule, calorie, kilocalorie | Direct dependency of S01. |
| B5 | Concentration units: mg/dL, mmol/L, and interconversion | Needed before any clinical or biochemical number. |
| B6 | Body-size units: kg, m, cm, kg/m² | Needed before BMI can be discussed at all. |

## Part C · Relationships and change

| # | Section | Notes |
| --- | --- | --- |
| C1 | Variables and algebra: what a letter stands for | |
| C2 | Rearranging an equation | |
| C3 | Two equations at once | |
| C4 | Functions: input, rule, output | |
| C5 | Graphs: axes, scale, slope, intercept | |
| C6 | Recognising shapes: linear, exponential, saturating | Lets a reader read a curve before differentiating one. |
| C7 | Rate of change — average and instantaneous, without the machinery | The derivative, taught as a rate. |
| C8 | Accumulation — a running total, without the machinery | The integral, taught as a total. |
| C9 | Stocks and flows as the physical reading of C7 and C8 | Shared by S01 and S44; promoted here by the §5 step-4 rule. |

## Part D · Uncertainty

| # | Section | Notes |
| --- | --- | --- |
| D1 | What a probability is | |
| D2 | Counting outcomes; independence | |
| D3 | Conditional probability through the two-way table | The table before the formula. Carries most of S03 rung 1. |
| D4 | Variation: what differs and by how much | |
| D5 | Average and spread, and why the average is not the person | |
| D6 | Sampling: how a part can tell you about a whole | |
| D7 | Random error and systematic error as different things | Prerequisite for the whole of S08. |

## Part E · The physical and living world

| # | Section | Notes |
| --- | --- | --- |
| E1 | Atoms, molecules and bonds — enough to see where energy is stored | |
| E2 | Chemical energy, combustion, and the bomb calorimeter | Direct dependency of S01. |
| E3 | Conservation of energy, and a system with a boundary | Direct dependency of S01. |
| E4 | Heat and temperature; how heat moves | |
| E5 | The cell, membranes, proteins and receptors | Floor for every drug and hormone concept later. |
| E6 | Metabolism as chemistry happening in a body | |
| E7 | Genes, DNA and inheritance in outline | Floor for S16. |
| E8 | Organs and systems that matter for metabolism | Replaces the MBBS assumption that has been removed. |

## Part F · Reading and reasoning

| # | Section | Notes |
| --- | --- | --- |
| F1 | Reading a table | |
| F2 | Reading a figure, and the ways a figure misleads | |
| F3 | What a scientific reference is, and how to check one | Makes the reader able to audit the course's own citations. |
| F4 | Argument: premise, inference, conclusion, and what makes one invalid | |
| F5 | How government works, in the shape needed to read a regulation | Ministry, regulator, statute, rule, notification, court. Floor for S48. |

---

## What the two pilot chapters depend on

Stated in advance so the pilots test the chain rather than assume it.

*Updated after the inventories were enumerated. The lists below are the union of the `ground_floor_deps` on each subject's concept records in `INVENTORY-PILOT.md`, not an estimate — an earlier draft of this file guessed contiguous ranges (`B1–B4`, `C5–C9`, `E1–E3`) and guessed wrong in both directions, pulling in B3, C6, C7 and C8, which nothing needs, and missing A4, A5, B6 and E6, which four concepts do.*

**S01 Energy balance** — a derivable subject, and the heaviest realistic Book 0 load: **A4, A5, A8, B1, B2, B4, B6, C5, C9, E1, E2, E3, E6** — thirteen of the forty-three sections. The pilot writes these.

**S48 Indian regulatory architecture** — an institutional subject with, notably, **almost no mathematical dependency at all: F1, F3, F4, F5** — four sections. This asymmetry is itself a finding worth confirming: if it holds, the institutional and policy booklets can be written and released long before Parts A–E of Book 0 are finished, which changes the rollout order materially.
