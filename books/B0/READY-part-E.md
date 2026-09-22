# Source gate · Book 0 Part E (E1–E8)

Checked against `sources/` on 2026-09-23. The rule in `claude.md`: a book only enters the pipeline
when its source pack is complete, and a line saying **no** stops the pipeline.

Part E is the first Part where this gate has teeth. Seven of its eight concepts are `empirical`,
and `claude.md` §7b makes an unopened source on an empirical concept a **blocking** build failure,
not a warning. Part A ran with eight unopened anchors; Part E could not.

## The gate

| Needed for | Work | Kind | In `sources/`? | Obtained |
| --- | --- | --- | --- | --- |
| E1 — atoms, molecules, what a bond is, and bond energy | OpenStax Chemistry 2e, §§2.3, 2.4, 7.2, 7.5 | textbook | `openstax_chemistry_2e.txt` | **yes** |
| E2 — calorimetry, the bomb calorimeter and its calibration, enthalpy of combustion, system and surroundings | OpenStax Chemistry 2e, §§5.1, 5.2, 5.3 | textbook | `openstax_chemistry_2e.txt` | **yes** |
| E2 — the Atwater general factors, and the cascade from gross to metabolizable energy | FAO Food and Nutrition Paper 77 (2003), ch. 3 | consensus_statement | `fao_food_energy.txt` | **yes** |
| E2 — the calorie and the kilocalorie as exact conversions | NIST Guide to the SI, footnotes | instrument | `nist_sp811.txt` | **yes**, already held |
| E2 — a real Indian food-energy figure to work on | National Food Security Act 2013, Schedule II | instrument | `nfsa_2013.txt` | **yes**, already held |
| E3 — conservation of energy, and the forms energy takes | OpenStax College Physics 2e, §§7.1, 7.6 | textbook | `openstax_college_physics_2e.txt` | **yes** |
| E3 — a system and its surroundings | OpenStax Chemistry 2e, §5.2 | textbook | `openstax_chemistry_2e.txt` | **yes** |
| E4 — heat against temperature, specific heat, the three ways heat moves | OpenStax College Physics 2e, §§14.1, 14.2, 14.4 | textbook | `openstax_college_physics_2e.txt` | **yes** |
| E5 — the cell, the membrane, transport, proteins, receptors | OpenStax Biology 2e, §§4.1, 4.3, 5.1, 5.3, 3.4, 9.1 | textbook | `openstax_biology_2e.txt` | **yes** |
| E6 — metabolism, catabolism, anabolism, glucose and triglyceride, ATP | OpenStax Anatomy and Physiology 2e, §§24.1–24.3; OpenStax Biology 2e, §7.1 | textbook | `openstax_anatphys_2e.txt`, `openstax_biology_2e.txt` | **yes** |
| E7 — DNA, bases, the double helix, alleles | OpenStax Biology 2e, §§14.2, 12.2 | textbook | `openstax_biology_2e.txt` | **yes** |
| E8 — gut, liver, pancreas, insulin and glucagon, what a hormone is | OpenStax Anatomy and Physiology 2e, §§23.6, 23.7, 17.1, 17.9 | textbook | `openstax_anatphys_2e.txt` | **yes** |

**No line says no.** The gate is clear and the pipeline may start.

## Four things found by opening the sources rather than assuming them

Each of these would have produced a citation pointing at a page that does not contain the claim.
They are the reason the gate is a step and not a formality.

1. **OpenStax Chemistry's food-energy material is in §5.2, not §5.3.** A record citing the enthalpy
   section for the 4/4/9 figures would cite a page that does not carry them.
2. **System and surroundings is defined in Chemistry §5.2, not §5.1**, and **not in College Physics
   2e at all** — that book never defines a system's boundary. E3 therefore takes it from Chemistry.
3. **The three heat-transfer methods are defined together only in College Physics §14.4.** The
   individual sections 14.5, 14.6 and 14.7 do not each open with a definition, and 14.7 has no
   "radiation is…" sentence at all.
4. **FAO 77 has no concept of digestible energy.** The phrase does not occur in the report. Its
   cascade runs gross or ingested energy → metabolizable energy, with faecal, gaseous, urinary and
   surface losses named along the way. **Part E must not teach a three-way gross / digestible /
   metabolisable split and cite FAO for it**, and E2's inventory line is written to the two-step
   cascade the report actually carries.

## One source deliberately not used, and what replaces it

**No measured quantity in Part E rests on a textbook.** OpenStax Anatomy and Physiology states
every figure flat — no study named, no citation — and its obesity and diabetes prevalence figures
are a 2010 vintage. Under `claude.md` §4 as amended, a textbook anchor is for settled science and a
measured quantity needs primary evidence, so those numbers are unusable here.

What that means in practice: E6 and E8 are written qualitatively, and every real number the Part
works on comes from a source already opened and clause-located — Schedule II of the National Food
Security Act for a meal's energy, FAO 77 for the Atwater factors, NIST for the calorie, and
Chemistry 2e's own worked bond energies. Where a section would be better with a measured Indian
figure — a resting metabolic rate, an organ's share of energy expenditure — it is left out and
named in the handover as a citation backlog item, not filled with a textbook's flat assertion.

## What was checked and found not to be needed

Anticipated before the inventory and then dropped, so nobody goes looking:

- **NCBI Bookshelf / Endotext.** Reachable, and not needed: the chapters that would have been cited
  carry measured quantities, which Part E has been scoped to avoid. Worth knowing it is available
  when a subject booklet needs primary physiological evidence.
- **ICMR-NIN recommended dietary allowances.** A PDF, and not needed here. Schedule II of the NFSA
  carries statutory meal standards that are already opened and located.
- **PubChem.** Already held for B5's molar masses; E1 was scoped so that it does not re-teach them.
