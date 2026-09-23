# Curriculum audit, 23 Sep 2026: verification layer

Two fresh verifiers. V-map searched the full frozen map (line numbers refer to map/subject-map-v3-FROZEN.md at main 4b06079). V-facts re-opened primary sources for eight decision-driving facts. Summary and decisions: claude/curriculum-audit-2026-09.md.

# V-map: adversarial verification of G1–G11 against the full map

Verifier V. Source: `/home/claude/obesity-course/map/subject-map-v3-FROZEN.md` (4,456 lines). I read the whole file top to bottom, including the front matter and every "Why this level" and "What it buys you" paragraph. Then I grepped it case-insensitively with a helper that tags each hit with its subject and rung (Sxx-Rn, Sxx-WHY, Sxx-BUYS, FRONT). All line numbers below are line numbers in the FROZEN map.

Verdict key: **REFUTED** = the content is in the map. **PARTIAL** = some of it is there. **CONFIRMED** = absent.

## Summary

| Gap | Verdict | Deliberate-exclusion evidence? | Recommended classification |
|---|---|---|---|
| G1 Settings | PARTIAL | No. The map says prevention belongs *inside* ICDS and school health (1995, 2041) | deepen existing rung |
| G2 Built environment / PA environment | CONFIRMED | Indirect only: S30 says activity is weak for weight (2273, 2313) | deepen existing rung (+ route urban planning in S61) |
| G3 Early life | PARTIAL | No | deepen existing rung |
| G4a Complications and deprescribing | PARTIAL | Depth cap only (1730) | deepen existing rung |
| G4b Cardiorenal | CONFIRMED | No | deepen existing rung |
| G4c Older adults, sarcopenic obesity, menopause | CONFIRMED (lean-mass content nearby) | No | deepen existing rung |
| G4d Opening the conversation | PARTIAL | No | deepen existing rung |
| G4e MDT clinic / chronic-care design | PARTIAL | Depth cap only (1730) | deepen existing rung |
| G4f Post-bariatric recurrence | PARTIAL | No | deepen existing rung |
| G4g Supplements, commercial products | PARTIAL (the auditors' "ABSENT" is wrong) | No | deepen existing rung |
| G4h Drug-induced weight gain beyond psychotropics | PARTIAL | No | deepen existing rung (merge with G4a) |
| G5 Leadership, management, mobilisation | PARTIAL | **Yes, a stance** (4013, 4034, 3745, 4454) | route in S61 (deliberate) + deepen for project/team management |
| G6 Designing policy instruments | PARTIAL | No. The map's own lever hierarchy argues *for* it (2613) | deepen existing rung |
| G7 Equity blind spots | PARTIAL (tribal, cultural norms and language are absent) | No | deepen existing rung |
| G8 India landscape | PARTIAL (item by item below) | No | deepen existing rung (named-entity updates) |
| G9 Health promotion, literacy, campaigns | PARTIAL | **Yes, for campaigns** (2568, 2578, 2613, 2622, 3539, 4034) | route in S61 (deliberate) for campaign craft; deepen for health literacy |
| G10 Other determinants | PARTIAL (smoking and alcohol confirmed absent) | Climate depth already routed (4434) | deepen existing rung |
| G11 Structure | PARTIAL (the numbers depend on definitions; "district only" is overstated) | **Yes, explicit** (37, 39, 34, 2920, 3190) | no action (decision for Harsh) |

**Nothing is fully refuted.** These sub-claims are refuted or overstated:

- G4g "supplements ABSENT". S23-BUYS names the supplement market (1797). S58-R3 covers detox and fad-diet misinformation (4255).
- G9 "no health-promotion theory". S50-R2 names PRECEDE-PROCEED (3656). S34-R2 teaches COM-B, SCT, SDT and the MRC framework (2596).
- G10 "no named determinants framework anywhere". S37-R2 names the HLPE food systems framework (2815). The front matter maps the source's "twelve-step causal spine" (47).
- G11 "implementation taught to district scale only". The state PIP is a build target (3753). S50-R3 teaches vertical scale-up and institutionalisation (3676).
- F's statement that "ICDS, school health" appears once is wrong. It appears three times (1995, 2041, 3743).

**A cross-cutting point that changes how every gap reads.** The map is derived from a source curriculum. Its coverage audit is against that source's checklist and causal spine (line 47). S61 routes only that source's "literate/aware" items (4422). None of G1–G10 is routed in S61, except planetary health (part of G10) and marketing science (4434). So most of these gaps are outside the source's scope, not rejected by it. Only G5, G9 (campaigns) and G11 have text in the map arguing for the exclusion.

---

## G1. Settings as delivery platforms — PARTIAL

**What exists**
- Schools as a design target, at Advanced:
  - S26-R3 skill: "Design a school or adolescent programme whose messaging has been tested for stigma and disordered-eating risk before deployment" (2045).
  - S26-R3 build: "A school or adolescent intervention designed, delivered and evaluated with harm outcomes measured alongside weight outcomes" (2049).
  - S26-R3 gate: "…a school principal would each sign off your design" (2051).
  - S26-R3: "Argue the school screening question in both directions" (2046).
  - S26-WHY: "Anything you design for schools or adolescents can do harm, so this must be executable" (1993).
- School food environment:
  - S38-R2: "school neighbourhood audits" (2881) and "Design a school neighbourhood audit a resident can execute in a term" (2890).
  - School-food governance in S48-R1 (3502) and S48-R2, "school food with the Ministry of Education, CBSE and states under PM POSHAN" (3519).
  - S48-R3: "reduced oil in PM POSHAN mid-day meals, sugar and oil awareness boards in CBSE schools" (3538).
- ICDS and maternal-child machinery as the vehicle:
  - S26-BUYS: "It places obesity prevention inside the machinery Indian public health already runs — maternal and child health, ICDS, school health" (1995; this prose is not in the index).
  - The same idea as an S26-R3 concept (2041).
  - S16-BUYS: an obesity programme "delivered through maternal and child health rather than competing with it" (1245).
  - S51-R3: "Convergence: ICDS and Poshan Abhiyaan, school education, urban development, Panchayati Raj" (3743).
- Workplace, only obliquely:
  - S30-R2: "Explain the occupational paradox to a programme designer proposing a workplace steps campaign" (2296).
  - S33 treats shift workers as a trial population, with "occupational health protection" (2526) and "from molecular clock to occupational policy" (2544).

**Missing**
- Searched "anganwadi" (0), "canteen" (0), "hostel" (0), "faith|temple|mosque|church|religio" (0 relevant), "physical education|sport" (0).
- There are no school food standards (only governance and an audit).
- There is no workplace-wellness setting and no health facility as a food setting ("hospital" appears only at 3706 and 3795).
- No subject is organised around settings. ICDS is named but never designed for.

**Deliberate?** No. The map argues the opposite: prevention *should* run through these platforms (1995, 1245, 2041). It then never builds the competency. That is an internal inconsistency, not an exclusion.

**Recommendation: deepen existing rung.** Add settings design (anganwadi/ICDS, school food standards, workplace) to S26-R3 and S51-R3. A new subject is not needed, because the design-deliver-evaluate build already exists at S26-R3.

---

## G2. Physical-activity environment — CONFIRMED

**What exists (adjacent only)**
- S51-R3 names "urban development, Panchayati Raj" as convergence partners (3743).
- S38-R2's audit build is "published or lodged with the municipality" (2892).
- S38 has GIS and outlet mapping, for food only (2881, 2889).
- S30-R2 covers the occupational PA paradox (2291) and "Design a population activity intervention targeted at the least-active" (2297).
- S01-R4 covers the biomechanics of locomotion (195).

**Missing.** Searched with 0 relevant hits:
- "built environment", "walkab", "park|open space|green", "zoning|licens", "motor|vehicle", "cycl" (only biochemical cycles, PDSA and PIP), "planning" (none urban), "labour-saving|technolog".
- "time use", "domestic".
- "transport" (only locomotion, transportability and transport workers).

**Deliberate?** There is no explicit exclusion. There is an implicit de-prioritisation of activity as a *weight* lever:
- S30-R1: "That activity is weak for weight loss and strong for health — the single most important honest message in this subject" (2273).
- S30-R3: "Tell a health minister that an activity programme will not move prevalence and should still be funded" (2313), and "why the population weight argument fails while the health argument stands" (2309).
- S19-R3 calls constrained TDEE "the most policy-relevant finding in metabolic physiology of the last decade" (1534).
- The S34-R3 lever hierarchy is entirely food-side (2613).

This weakens the case for a whole subject. It does not justify having zero content, because S30 itself says the health case stands and should be funded.

**Recommendation: deepen existing rung.** Add the built environment and active transport as activity exposures in S30-R2/R3, and extend S38-R2's GIS audit to the activity environment. Add "urban planning / transport planner" to S61's routing list.

---

## G3. Early life — PARTIAL

**What exists**
- S16 DOHaD:
  - "fetal programming versus postnatal catch-up growth as separate mechanisms" (1274).
  - The capacity-load model (1291).
  - Indian birth cohorts: "low birthweight followed by childhood or adolescent BMI gain" (1290).
  - "Maternal obesity, gestational diabetes and the intergenerational cycle; the confounding problems in the breastfeeding literature" (1295).
  - S16-R1 gate: ask about "birthweight and childhood growth as routinely as you ask about diet" (1264).
- S26-R1: growth references (2003); "Plot and interpret a child's growth trajectory correctly" (2009); "A growth-charting audit" (2012).
- S26-R2: IAP versus WHO references (2020); "family as the unit of intervention" (2027); pregnancy and preconception care (2023, 2028).

**Missing.** Searched with 0 hits:
- "infant", "IYCF|complementary feed|weaning", "IMS Act|breast-milk substitut|formula" (all "formula" hits are reformulation or g-formula).
- "parent", "toddler|under-5|preschool|early childhood|first 1000".
- "puberty", "complication" (paediatric).
- "growth monitor".

Breastfeeding appears once, as a confounding problem (1295). There is nothing on paediatric complications.

**Deliberate?** No. S16-WHY chooses *adolescent and maternal* nutrition as the policy emphasis (1243, 1312, 1317), but it does not argue against infancy.

**Recommendation: deepen existing rung.** In S26-R2/R3, add IYCF, rapid infant weight gain, parental feeding practices and paediatric complications. Name the IMS Act in S48-R2.

---

## G4. Clinical

Deliberate-scope evidence for the whole cluster:
- S22-WHY: "Advanced means you run the consultation independently — not that you are a bariatric physician" (1730).
- S25-WHY: "The operation itself is Introductory for you — recognise, route, and never opine on technique" (1927).
- S32-WHY: "You screen and co-manage; you do not run a sleep laboratory" (2412).
- S22-BUYS frames clinical skill as instrumental: "Credibility with clinicians" (1732).

These cap *depth*. None of them excludes the topics below, and none of the topics is routed in S61.

### G4a. Treating complications and deprescribing — PARTIAL
**Exists**
- Complications are assessed in the S22-R2 comorbidity list: "dysglycaemia, dyslipidaemia, hypertension, MASLD with fibrosis staging, OSA, PCOS, osteoarthritis, GERD, depression, subfertility, obesity-associated cancers" (1759).
- MASLD is acted on: "Stage MASLD fibrosis non-invasively and act on the result" (1764).
- Remission is covered: DiRECT (1823); "Total diet replacement and remission programmes" (1842); bariatric "diabetes remission" (1954).
- S22-R3: "problem list, plan" (1781).

**Missing.** Searched "deprescri|dose reduc|taper|step down" (0) and "statin|antihypertens" (0). The only hypoglycaemia content is post-bariatric (1955, 1979). There is no treat-to-target management of T2D, HTN, lipids, PCOS, OA or GERD, and no medication reduction as weight falls.

**Recommendation: deepen existing rung** (an S22-R3 or S24-R2 skill).

### G4b. Cardiorenal — CONFIRMED
Searched "heart failure|HFpEF|atrial|AF|CKD|kidney|renal|albumin" and got 0 relevant hits. The only cardiovascular content is "SELECT cardiovascular benefit" (1888). S20-R3/S22-R3 cite the Lancet Commission's requirement of "organ dysfunction" (1603, 1775), but no organ-specific cardiorenal criteria are named.

**Recommendation: deepen existing rung** (the S22-R2 comorbidity list and the S20-R3 criteria).

### G4c. Older adults, sarcopenic obesity, menopause — CONFIRMED (adjacent content exists)
- Searched "elderly|geriatric|sarcopen|frail|menopaus" (0) and "older" (only "LASI older ages only", 3928).
- "ageing" appears only as "demographic ageing" in microsimulation (3167).
- Adjacent: GLP-1 "loss of lean mass" (1890); "protect lean mass with concurrent resistance training and protein targets" (1896); low South Asian muscle mass (1567, 1586, 1825, 1536).
- S26 defines its life stages as "paediatric, adolescent and pregnancy" (1989). Older age is simply not a stage in the map.

**Recommendation: deepen existing rung.** Add an older-adult and menopause bullet to S26, or an S22-R3 concept tied to the S24-R2 lean-mass skill.

### G4d. Opening the conversation — PARTIAL
**Exists**
- MI: "Deliver motivational interviewing competently" (1830).
- Stigma-free consultation: "Conduct a consultation without stigmatising language" (2650), with the gate "respectful without being asked" (2655).
- Expectation setting: "State to a patient what weight change is realistic, before starting" (1812).
- Options counselling: "Explain the options to a patient at the level of what each involves and commits them to" (1943); "Select between agents for a specific patient and defend the choice" (1897); "Counsel a patient on what a GLP-1 agonist will and will not do" (1877).

**Missing.** Searched "permission" (0), "5 ?As|Ask, Assess" (0), "shared decision|decision aid" (0) and "raise the topic|broach" (0).

**Recommendation: deepen existing rung.** One S22-R1 or S35-R1 bullet on asking permission, the 5As and SDM.

### G4e. Multidisciplinary clinic and chronic-care design — PARTIAL
**Exists**
- S22-R3 build: "A weekly obesity or metabolic clinic slot, running, with staged patients" (1785).
- S24-R2: "prescribing and monitoring protocol… documented discontinuation pathway" (1899).
- S25-R2: "post-bariatric surveillance protocol… with a patient register" (1965).
- S25-R3 gate: "physician on a multidisciplinary bariatric team" (1985).
- S26-R2 family-based pathway (2031). S32-R3: "Co-manage OSA… and audit the pathway" (2466).
- S51-R2 task-shifting and non-physician NCD care (3726). S50-R2 QI and PDSA (3659, 3664).

**Missing.** Searched "multidisciplinary|MDT|team" (only 1985), "recall" (none clinical), "chronic care|telemedicine" (0) and "dietitian" (only 2120). There is no team composition, recall system or chronic care model for the obesity clinic itself.

**Recommendation: deepen existing rung** (the S22-R3 build specification).

### G4f. Post-bariatric weight recurrence — PARTIAL
**Exists:** "revisional surgery" (1955); "revisional decisions as contested areas" (1974); "Recognise late complications and act" (1963); "Co-manage complex post-operative patients… hypoglycaemia and nutritional failure" (1979). Regain is treated thoroughly for lifestyle and drugs (1822, 1853, 1872, 1891).

**Missing:** "dumping" (0). Post-surgical weight recurrence and adjunct pharmacotherapy after surgery are not mentioned (no "regain" hit in S25).

**Recommendation: deepen existing rung** (S25-R2/R3).

### G4g. Supplements and commercial weight-loss products — PARTIAL (A's "ABSENT" is wrong)
**Exists**
- S23-BUYS: the difference "between a patient who returns and one who disappears into the supplement market" (1797). This is prose; A's own table quotes it.
- S58-R3: "Countering misinformation, dominant in Indian diet discourse: fad diets, detox claims, influencer nutrition" (4255).
- The regulator is mapped in S48-R2: "misleading advertisement action with the Central Consumer Protection Authority" (3519).

**Missing:** "ayurved|AYUSH|herbal|slimming|nutraceutical|remed" (0; the only hits are "Ayushman"). There is no clinical counselling on supplements and no regulation of nutraceuticals or remedy advertising.

**Recommendation: deepen existing rung** (S23-R1 counselling and S48-R2 regulation).

### G4h. Drug-induced weight gain beyond psychotropics — PARTIAL
**Exists:** identification is fully covered:
- "the common drug causes of weight gain" (1741).
- "List the drugs in a patient's chart that promote weight gain" (1747).
- S22-R2 names "antipsychotics, insulin and sulfonylureas, steroids, some antiepileptics, beta blockers" (1757).
- Management is covered for psychotropics only: "Manage a patient whose weight gain is psychotropic in origin" (2671).

**Missing:** switching to weight-neutral alternatives for non-psychotropic drugs ("weight-neutral|switch" 0).

**Recommendation: deepen existing rung.** Merge this with G4a as one S22-R2/R3 prescribing skill.

---

## G5. Leadership, management, negotiation, institution building, community mobilisation, sustaining oneself — PARTIAL

**Exists**
- Leading, as a verb:
  - "Lead a randomised early-TRE trial" (S33-R4, 2551).
  - "an ethics standard adopted by a group you lead" (S60-R4, 4414).
  - "Set the ethical standard for a group or a national programme" (4411).
- Management:
  - "Budgeting, procurement and the practical mechanics of getting an activity approved and paid for" (S51-R3, 3744).
  - PIP costing (3735). "Cost an intervention including frontline worker opportunity cost" (3683).
  - "Set and enforce a data management standard for a cohort or a department" (3840).
  - Dataset governance with "access policy, authorship policy" (3965).
- People:
  - "deliberate training of juniors who become the network" (4188).
  - "Supervise others' question selection" (4057).
  - "not reproducing extraction downward with people you supervise" (4119, 4406).
  - "Train others to facilitate the protocol" (3363).
- Negotiation: "Negotiate and execute a data use agreement" (3952); "Negotiate authorship before work begins" (4108).
- Institution building:
  - "Reproducibility as an institutional practice… make it the default for a group" (3833).
  - "What it takes for a dataset to outlive you" (3966).
  - A surveillance system that "survives a change of district officer" (1380, 1390).
  - "institutionalisation in policy and budget is what lasts" (3676).
- Coalitions and convening:
  - S47-R3: "Assemble and brief a coalition around one instrument" (3479).
  - S51-R3: "Convene across departments at district level — a genuinely scarce skill" (3750).
  - S57-R2/R3: professional bodies and civil society (4171, 4177, 4195).
  - S45 facilitation, including "Handle a workshop in which the senior official disagrees" (3345).
- Community: "Intervention co-design and participatory methods" (2767); "co-design workshop with patients or frontline workers" (2773); "community involvement, returning results" (4101).
- Sustaining oneself:
  - S55-R3 stopping rules and failure modes (4034–4035).
  - S60-R3 personal hazards: the "empathy gap" and the "saviour frame" (4388).
  - S59 calibration.

**Missing**
- Searched "leader|leadership" (**0**) and "partner" (0).
- "negotiat" appears only for DUAs and authorship.
- "hire|hiring" (0), "mobilis|empower|SHG" (0) and "burnout|wellbeing" (0).
- Missing skills: team, HR and financial management of a unit; negotiation with ministries or industry; community mobilisation and public demand; burnout prevention.

**Deliberate?** Yes, as a stance, though not as an explicit exclusion:
- S55-R2 (4013): "The four assets recognition is made of: a citable body of work…; custody of data or a cohort; a teaching lineage; institutional position and committee membership — **with the fourth manufactured by the first three**." Institutional position is treated as a by-product, not a skill to be trained.
- S55-R3 (4034) lists failure modes: "advocacy capture, awareness-poster capture, **administrative capture**". S55-R3 (4039): "Decline invitations that do not serve the one question you own".
- S51-R3 (3745) gives the map's theory of influence: "the researchers who get things implemented are those who have spent years being reliably useful — answering questions, producing reports on time, making officials look competent."
- S47-R2 (3462) and S48-R4 (3558) maintain a researcher-versus-advocate identity: "what a researcher can say that an advocate cannot".
- The closing note (4454): the career that becomes nationally consequential is "the one that spent 2027 doing unglamorous work on a chrononutrition instrument in Raipur".
- S43-WHY uses the same logic for another field: "building health financing policy is a separate career" (3190).

**Recommendation: route in S61 (deliberate)** for organisational leadership and administration, for example "health management/administration: partner with a programme manager". Also **deepen existing rungs** for the project, team and budget management that the map's own builds already require (the S33-R4 trial, the S54-R4 cohort, the S50-R3 hybrid study). This is Harsh's decision, because it changes the persona.

---

## G6. Designing policy instruments — PARTIAL

**Exists: instrument design where the map chose to teach it**
- Tax: "Design a tiered threshold tax on a nutrient of concern" (S41-R2, 3088); "Construct a tax proposal that could survive the GST Council" (3107).
- FOP thresholds: "Derive candidate India-specific nutrient profiling thresholds" (S29-R3, 2247; S48-R3, 3545).
- Rule-type choice: "Advise a regulator on the choice between processing-based and nutrient-based rules" (2180).
- Reformulation: "Advise a reformulation programme on which nutrient changes are worth mandating" (2115).
- Drafting: "Write a regulatory comment that a technical panel would take seriously" (3478); a four-page brief "with the legal mechanism" (3461); "Name the three regulatory levers that would most change a product's consumption, and who would fight each one" (2840).
- Marketing: the evidence "on food marketing to children" (2882); the mechanism, with the S21-R3 gate "advertising restriction is a biologically motivated intervention" (1702); the regulators CCPA and MIB (3519); the Chilean package (3603).
- Double burden: "State the double burden of malnutrition as one problem rather than two" (S16-R1, 1260); "the double burden within the same household" (2221); "Explain why the PDS and the obesity problem are the same policy conversation" (2824); "Indian food policy was built to end calorie deficiency, not calorie excess" (2800); S16-BUYS "India's undernutrition machinery" (1245).
- Benchmarking: industry via "Run an India-specific benchmarking exercise using INFORMAS or ATNI instruments" (2972); INFORMAS for food environments (2883).

**Missing**
- "procure" appears only in the S51 administrative sense (3744). "menu labelling" (0). "zoning" (0).
- No rung designs a marketing restriction, a school-food rule, a procurement standard, a double-duty programme standard (PDS, PM POSHAN, ICDS) or a government Food-EPI.
- B's statement that "undernutrition appears in no rung" is literally true, because the word appears only in S16-BUYS prose. But the double burden *is* in the S16-R1 and S29-R2 rungs.

**Deliberate?** No. The map's own lever hierarchy argues for this:
- S34-R3 (2613): "reformulation mandates, then price instruments, then **availability and marketing restriction**, then front-of-pack labelling… — the strategic heart of the whole curriculum."
- The map teaches design for levers 1 (partly), 2 and 4, but not 3. That is an internal inconsistency.
- S47-WHY: "Vague advocacy is ignored and specific drafting is not" (3425).

**Recommendation: deepen existing rung.**
- Add marketing-restriction and procurement-standard design to S47-R3 and S48-R3.
- Add double-duty design to S37-R2/R3.
- Add a government Food-EPI to S39-R3.

---

## G7. Equity blind spots — PARTIAL (mostly absent)

**Exists**
- Sex as a stratifier: "Describe an outcome by wealth quintile, urban-rural and sex" (1347).
- "caste and class as distinct constructs" (1358).
- "the double burden within the same household" (2221).
- The Indian common pot as a measurement problem (768). "Indian household food architecture" (1811, 1829).
- "Indian vegetarian diets" (2073). Regional dietary patterns (2205).
- "Intervention-generated inequality as a design consideration" (1378).
- S60-R2: "the ethics of imposing dietary change on people with little discretionary income or time" (4368).
- "rural Chhattisgarh" transportability (942).

**Missing.** Searched with 0 relevant hits:
- "gender", "women's", "intra-household", "allocation" (in the food sense), "mobility".
- "tribal|adivasi|scheduled tribe|indigenous". The only "tribal" hit is "the field's tribal positions" at 2063.
- "festiv|hospitality|wedding|ritual", "body size ideal|prosperity|beauty", "fasting" (only as a diet regimen, 1823).
- "linguistic|vernacular|Hindi".

**Deliberate?** No.

**Recommendation: deepen existing rung.** Add gender and tribal equity to S17-R2/R3, cultural norms to S23-R2 and S35-R3, and language to S58-R3.

---

## G8. India landscape, named and current — PARTIAL (item by item)

| Item | Verdict | Evidence |
|---|---|---|
| CDSCO and GLP-1 prescriber rules | CONFIRMED | "CDSCO|DCGI|Drugs and Cosmetics|prescriber" 0 hits. S24-R3 has "non-prescription share" and "Pharmacovigilance" (1907, 1909) |
| FSS (school children) Regs 2020 | PARTIAL | School food is assigned to "Ministry of Education, CBSE and states under PM POSHAN" (3502, 3519); the regulation is not named ("Safe food|fifty|50 m" 0) |
| NFHS-6 | CONFIRMED | The map is pinned to NFHS-3 to NFHS-5 (1993, 2004, 3912); a currency update, not a competency gap |
| Poshan Tracker | CONFIRMED | "Tracker" 0; Poshan appears only as PM POSHAN or Poshan Abhiyaan (3519, 3538, 3743) |
| 2025 Indian obesity definition | PARTIAL | The 2025 Lancet Commission is covered (1603, 1775, 4369); Indian action points 23/25 (1567, 1602); S20-R4 "authorship on an Indian consensus statement on obesity definitions" (1631); the Indian 2025 scheme is not named |
| NNMB | CONFIRMED | S54 lists "NNMS" (3911, 3928), which is a different survey; "NNMB|What India Eats" 0 |
| RBSK / RKSK | CONFIRMED | 0 hits; only the generic "school health" (1995, 2041) |
| NITI Aayog, ICMR-NIN, NHSRC | PARTIAL | ICMR-NIN appears only as the RDA author (2203); ICMR as funder and ethics body (4016, 4101); NITI, NHSRC and PHFI 0 |
| Time Use Survey | CONFIRMED | 0 hits; MoSPI appears only for unit-level access (3930) |
| AYUSH | CONFIRMED | 0 hits (the only matches are "Ayushman") |
| Private sector as main provider | PARTIAL | S43-R1 "out-of-pocket, PM-JAY, state schemes, private insurance" (3200); S25-R2 "Indian practice landscape" (1956); unsupervised GLP-1 use (1878); S51 treats delivery as public only (3706–3708) |

**Deliberate?** No. S54-R2's dataset list is presented as "what each dataset can and cannot answer" (3928), not as an exhaustive list.

**Recommendation: deepen existing rung.**
- Named-entity additions: S54-R1/R2 (Poshan Tracker, NNMB, TUS); S48-R2 (CDSCO, FSS 2020 school regulations); S26-R3 (RBSK/RKSK); S20-R3 (the Indian 2025 definition); S51-R1 (private sector).
- Add AYUSH to S61 as recognise-and-route.
- I did not verify E's external facts, such as the PIB prescriber restriction or the NFHS-6 release.

---

## G9. Health-promotion theory, health literacy, social marketing, campaign design — PARTIAL

**Exists**
- Behaviour-change theory at Intermediate and Advanced: "COM-B and the Behaviour Change Wheel; the BCT taxonomy…; self-determination theory; social cognitive theory; the MRC framework" (2596).
- **PRECEDE-PROCEED**, the canonical health-promotion planning model, "for planning" (S50-R2, 3656).
- Message design and testing:
  - "Test every message, poster, brief and abstract you produce for stigma" (2688).
  - "Set the communication standard for a national or state programme" (2708).
  - "messaging has been tested for stigma" (2045).
- Risk communication (4237). Media, inoculation and pre-bunking (4254–4255).
- "Adjudicate whether a proposed campaign is ethically deliverable" (2707).

**Missing**
- "health promotion|Ottawa" (0). "social marketing|mass media" (0).
- "literacy" appears only in the Court's "nutrition literacy" question (3537) and in "low-literacy settings" consent (4101).
- There is no health literacy or label-comprehension competency and no campaign-design craft.

**Deliberate?** Yes, for campaigns:
- S34-R1: "That information campaigns are the weakest lever and the most popular one" (2578).
- S34-BUYS: "the skill that keeps you from becoming an awareness-poster researcher. Every time you are asked to design a campaign, this is what lets you say what the campaign will achieve and what would achieve more" (2568).
- S34-R3 skill: "Decline to run an awareness intervention and win the argument on evidence" (2622). Gate: "argued a programme away from awareness toward a structural lever" (2626).
- S48-R3: "The risk that the window closes having produced only awareness measures" (3539).
- S55-R3 failure mode: "awareness-poster capture" (4034).

There is no such argument against health literacy.

**Recommendation: route in S61 (deliberate)** for campaign and social-marketing craft. The map expects campaign requests and equips him to appraise and redirect them. **Deepen existing rung** for health literacy and label comprehension in S48-R3 or S29-R3, since the live FOPL case turns on it (3537).

---

## G10. Other determinants — PARTIAL

| Item | Verdict | Evidence |
|---|---|---|
| Psychosocial stress | PARTIAL | S32-R2 "Stress, cortisol and emotional eating" (2443); S19-R3 HPA axis and cortisol (1535); depression (2663); shift work (2526) |
| ACEs, job strain | CONFIRMED | "adverse childhood|trauma|job strain" 0 relevant |
| Smoking and cessation | CONFIRMED | "smok|cessation|nicotine" 0; tobacco appears only as a policy analogy (2966, 3453) |
| Alcohol as an intake determinant | CONFIRMED | Only "alcohol use disorder" after bariatric surgery (1955) |
| Heat and climate | PARTIAL; climate depth already ROUTED | S37-R3 "Planetary health and the diet-climate-land use link" (2836, 2842); EAT-Lancet (2241); S61 routes "planetary health… (sustainability scientist)" (4434); heat acting on activity appears nowhere |
| Named determinants framework | PARTIAL (the claim of "none anywhere" is overstated) | "Foresight|ANGELO|syndemic|socio-ecological" 0; but the HLPE food systems framework is named "as a formal reference, learned well enough to locate any intervention within it" (2815), and the map is organised on the source's "twelve-step causal spine" (47) |

**Deliberate?** Only the climate routing (4434).

**Recommendation: deepen existing rung.**
- Smoking and alcohol history and counselling in S22-R2 (they are also confounders for S11/S18).
- ACEs and job strain in S32-R2 or S17-R2.
- One S44-R2 bullet: locate any cause on the Foresight or ANGELO map.

---

## G11. Structure — PARTIAL (numbers reproduce only under stated definitions; deliberate)

The recompute script parsed the register at lines 57–119 and cross-checked it against the `### Sxx · Rung` headings in the body. Both give 195 rungs, and the target level matches the rung count for all 61 subjects. By level: Introductory 61, Intermediate 60, Advanced 55, Expert 19, which matches the front matter (line 11). Targets: 1 Introductory, 5 Intermediate, 36 Advanced, 19 Expert.

**Rungs per Part**

| Part | Rungs | Part | Rungs |
|---|---|---|---|
| 1 Physical and mathematical foundations | 7 | 10 Behavioural and psychological | 10 |
| 2 Statistical inference and modelling | 16 | 11 Food systems and commercial determinants | 9 |
| 3 Measurement science | 8 | 12 Economics and decision modelling | 11 |
| 4 Causal inference | 17 | 13 Systems and complexity | 8 |
| 5 Epidemiology | 14 | 14 Policy, law and political economy | 9 |
| 6 Metabolic and appetite biology | 11 | 15 Implementation and health systems delivery | **6** |
| 7 Clinical obesity medicine | 15 | 16 Computation and data | 10 |
| 8 Nutrition science | 9 | 17 Research craft | 7 |
| 9 Movement, sleep and circadian | 14 | 18 Teaching, communication and integrity | 14 |

**"~67 of 195 are research methods".** F's 67 reproduces exactly. It uses S02–S14 (44 rungs) plus S31 (4), S36 (3), S52 (4), S53 (2), S55 (4), S56 (3) and S59 (3). The figure depends on the definition:

| Definition | Subjects | Rungs |
|---|---|---|
| Strict methods (stats, measurement, causal, computation, qualitative) | S02–S14, S31, S36, S52, S53 | **57** |
| + study design, nutritional-epidemiology critique, survey data | + S15, S18, S54 | **68** |
| + research craft and epistemics | + S55, S56, S59 | **78** |
| + modelling | + S42, S44, S45, S46 | **89** |

F's set counts S55 (question selection and career strategy), S56 and S59 (epistemics) as methods, and leaves out S15, S18 and S54. The honest range is about 57 to 89. "About a third" holds under the most natural definitions (57–68).

**Remaining rungs (my partition)**

| Category | Subjects | Rungs |
|---|---|---|
| Biology, nutrition, movement | S01, S16, S19–S21, S27–S30, S32, S33 | 38 |
| Clinical | S22–S26 | 15 |
| Change-making (behaviour/intervention design, food systems, economics instruments, policy, implementation, health system, plus S17 equity/surveillance) | S17, S34, S37–S41, S43, S47–S51 | 38 |
| Communication, teaching, ethics, stigma | S35, S57, S58, S60 | 14 |
| Routing | S61 | 1 |

Total with the broadest methods set: 89 + 38 + 15 + 38 + 14 + 1 = 195.

**"11 of 19 Expert subjects are methods"**

| Group | Subjects | Count |
|---|---|---|
| Strict methods, measurement, computation | S03, S04, S08, S09, S10, S11, S31, S52 | **8** |
| Epidemiology and data | S18, S54 | +2 |
| Research craft | S55 | +1 = **11** |
| Biology | S01, S16, S20, S21, S33 | 5 |
| Change-making | S48 | 1 |
| Stigma and ethics | S35, S60 | 2 |

So 11 holds only if S18, S54 and S55 count as methods; the strict count is 8. S01 is itself dynamic ODE modelling, so it could also be counted as methods.

**"The change-making subjects stop at Advanced; S43 at Intermediate".** Confirmed from the register: S34, S37, S39, S41, S47, S50 and S51 are all Advanced (lines 92, 95, 97, 99, 105, 108, 109). S43 is Intermediate (101) and S49 is Intermediate (107). S48 is the only Expert change lever.

**"Implementation taught to district scale only".** Overstated.
- Hands-on delivery is district-anchored:
  - S51-R3 skill: "adapt it for a district… get it approved, deliver it" (3749).
  - S50-R3 gate: "adapted by another district" (3688).
- But state and national scale appear as build targets:
  - S50-R3: "horizontal scale versus vertical scale, and why institutionalisation in policy and budget is what lasts" (3676).
  - S51-R2: the state PIP cycle (3724). S51-R3 build: "An activity you designed appearing in a **state** PIP and being delivered" (3753).
  - S17-R3: "adopted by a district or state programme" (1388). S42-R3 gate: "A state health department asks you" (3182).
  - S35-R4: "Set the communication standard for a national or state programme" (2708).
- What is missing is running a *national* programme.

**Deliberate?** Yes, explicitly:
- Front matter (37): "Ladders stop at the target… That is deliberate: machine learning, agent-based modelling, comparative policy, health financing, Python and the adjacent specialist domains are places where going deeper is available, interesting and wrong… The cap is as load-bearing as the spike."
- Front matter (39): "19 subjects carry an Expert target, and they cluster rather than scatter: measurement, causal inference, nutritional epidemiology, the Indian phenotype, circadian biology, Indian data and Indian regulation." Its depth-first advice is S08, S11, S33 and S54 (three methods and one biology).
- The rubric itself (34): Advanced is "the working standard for anything you will publish, prescribe or implement". Expert (35) is "derive it from first principles… settle a dispute… publish work that changes how others do theirs". Under this rubric, capping change-making at Advanced is by design: Advanced is the implementation standard.
- S39-WHY: "Expert would mean developing commercial-determinants theory, which is not where your differentiation lies" (2920).
- S43-WHY: "building health financing policy is a separate career" (3190). S49-WHY: "do not specialise in it" (3576).

**Recommendation: no action.** The structure is an explicit, argued choice, not an oversight. Whether the persona should move from researcher-adviser towards programme leader is Harsh's decision. If he wants that, the lever is G5, not raising caps.

---

## The two text checks

1. **"India's obesity problem is arriving through its children".** It appears in three places:
   - S26 "Why this level" prose (1993): "India's obesity problem is arriving through its children — the NFHS-3 to NFHS-5 comparison shows a 288% relative rise in adolescent boys against a 91% rise in adult women…"
   - S26-R1 concept (2004).
   - S54-R1 concept (3912).

   F's attribution to "S26 R1 and S54 R1" is correct; the S26-WHY copy is additional.
2. **"leader appears nowhere".** True as a string: "leader" and "leadership" have 0 hits. The line 3519 hit is "misleading". But the verb is present:
   - "**Lead** a randomised early-TRE trial" (S33-R4, 2551).
   - "an ethics standard adopted by a group you **lead**" (S60-R4, 4414).

   So D's "Leadership is never named" is accurate. "The map produces a trusted adviser, not a leader" is a fair reading, but the map does assume he will lead a trial and a group.

## Caveats

- Verdicts are about whether the content is in the map text. I did not re-verify the auditors' external facts: the PIB GLP-1 prescriber restriction, the NFHS-6 release, the FSS 2020 regulation clauses, the Misra 2025 definition, RBSK 2.0, or the WHO best-buy status of mass-media campaigns.
- The category boundaries in G11 are my own and are stated explicitly. Other reasonable partitions move the methods count between 57 and 89.
- "Deliberate" evidence ranges from explicit statements (G11: front matter 37 and 39, rubric 34) to an inferred stance (G5: 4013, 4034, 3745). Harsh should read G5 and G9 as design choices open to his decision, not as settled exclusions.

---

# V-facts: fresh verification of 8 external claims

Verifier V. Date: 23 Sep 2026. Every quote below was copied from a primary source opened in this session. PDFs and web pages were read with a full-text extractor (TinyFish fetch_content), not a summarising tool. Journal text came from PubMed/PMC, and the Delhi High Court judgment came from the court's own PDF via Legal Data Hunter. WebFetch's summary of the Rubino table was thrown away and replaced with the raw PMC XML text. Direct curl to .gov.in and ncbi hosts is blocked by this session's egress proxy (403), so it was not used.

Verdicts: **CONFIRMED** = the source says it (any nuance is in the note). **CORRECTED** = the source says something materially different. **UNVERIFIABLE** = no primary source could be opened.

| # | Claim | Verdict | Exact quote from primary source | URL | Note |
|---|---|---|---|---|---|
| 1 | Official statement (PIB backgrounder, Apr 2026) says GLP-1 RAs may be prescribed only by endocrinologists, internal medicine specialists and cardiologists. Who issued it, what is its legal status, and does it restrict an MD Community Medicine? | **CONFIRMED (wording); CORRECTED on source and scope** | (a) PIB backgrounder: "In India, GLP-1 drugs can only be prescribed by endocrinologists, internal medicine specialists, and cardiologists - they cannot be purchased over the counter." Also: "In India, the drug can be prescribed only by endocrinologists, internal medicine specialists and cardiologists." (b) The underlying MoHFW release (24 Mar 2026): "It is important to reiterate here that the drug has been approved in India with condition of prescription by Endocrinologists and Internal Medicine Specialist and for some indications by Cardiologists only." (c) CDSCO SEC, 20–21 Apr 2023, tirzepatide: "The drug should be sold by retail under prescription of Endocrinologist or internal medicine specialists only." (d) CDSCO SEC, 23 Mar 2026, Wegovy in adolescents 12+: "the drug shall be prescribed by registered Endocrinologist or pediatrician." | (a) https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/apr/doc202641837401.pdf (b) https://www.pib.gov.in/PressReleasePage.aspx?PRID=2244252&reg=3&lang=1 (c) https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2018/UploadCommitteeFiles/Recommendations%20Endocrinology%20&%20%20Metabolism%2020.04.2023%20&%2021.04.2023.pdf (d) https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2018/UploadCommitteeFiles/Recommendations%20Endocrinology%20Metabolism%2023.03.2026%20(1)%20(2).pdf | **Issuer:** the backgrounder "GLP-1 Drugs: Use, Risks, and Regulation" (1 Apr 2026) is by "PIB Research". Its only source for this line is MoHFW press release 2244252 (24 Mar 2026). The backgrounder drops the MoHFW qualifier "for some indications" from the cardiologist part, and it speaks of GLP-1 drugs generally, not obesity use only. **Legal status:** the backgrounder is an explainer with no legal force. The rule itself is a CDSCO marketing-approval condition, recommended by the Subject Expert Committee and imposed by the DCGI under the drug-approval process. It is worded as a condition on retail sale, and it is enforced against manufacturers, sellers and clinics ("cancellation of licenses, penalties, and prosecution"). It is not an NMC rule on doctors' scope of practice. **Unverified:** the 9 Dec 2025 SEC minutes approving generic semaglutide for weight management (Sun, Alkem, Zydus) list only a PMS-study condition and **no prescriber condition**. I did not open the final permission letters, so I cannot confirm that the generics carry the restriction beyond MoHFW's general statement. **MD Community Medicine:** that specialty is not on the list, so on the face of the condition a pharmacy may not lawfully dispense these products on his prescription. Whether that bars him from prescribing is a legal interpretation for Harsh to decide (or to get advice on). |
| 2 | NFHS-6 (2023–24 round) national results released 29 May 2026 | **CONFIRMED** | "Posted On: 29 MAY 2026 3:55PM by PIB Delhi … The Ministry of Health and Family Welfare (MoHFW) released the National Family Health Survey – 6, here today. The NFHS-6 was conducted during 2023-24 by MoHFW with the International Institute for Population Sciences (IIPS), Mumbai as the nodal agency. Covering nearly 6.79 lakh households across 715 districts" | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2266600&reg=3&lang=1 | The release gives national headline indicators (stunting 35.5→29.3%, and others) but **no adult overweight or obesity figure**. It only says "the dual burden of undernutrition and rising overweight/obesity among adults". NFHS-6 obesity prevalence figures are still unverified. The fact sheets are on the MoHFW publications page linked in the release, which I did not open. |
| 3 | FSSAI "(Safe and Wholesome Food for School Children) Regulations, 2020": no HFSS sale to schoolchildren on school premises or within 50 m of the gate, plus advertising restrictions; wording, and whether in force | **CORRECTED** | Title: "Food Safety and Standards (Safe food and balanced diets for children in school) Regulations, 2020." Reg 3(5): "School Authority shall ensure that no person shall sell or offer for sale including free sale, or permit sale, of food products high in saturated fat or trans-fat or added sugar or sodium in school premises or campus." Reg 5(1): "No person shall advertise or market or sell or offer for sale including free sale, or permit sale of, food products high in saturated fat or trans-fat or added sugar or sodium in school campus or to school children in an area within fifty meters from the school gate in any direction." Commencement, Reg 1(2): "They shall come into force on the date of their publication in the Official Gazette and food business operator shall comply with all the provisions of these regulations with effect from 1st July, 2021, except sub-regulation (5) of regulations 3 and sub-regulation (1) of regulations 5 which shall come into force only from such date as the Food Authority may, by notification in the Official Gazette, appoint." Draft amendment (notification dated 7 Aug 2026, Gazette 10 Aug 2026) inserts reg 7: "'high in added fat or added sugar or sodium' shall be as per the Dietary Guidelines for Indians-2024, ICMR" (fat >4.2 g/100 g solid or >1.5 g/100 ml liquid; sugar >3 g/100 g or >2 g/100 ml; salt >0.625 g/100 g or >0.175 g/100 ml). | https://fssai.gov.in/upload/uploadfiles/files/Gazette_Notification_Safe_Food_Children_07_09_2020.pdf ; draft: https://fssai.gov.in/docs/food-law/notice-comment/Draft%20Food%20Safety%20and%20Standards%20(Safe%20food%20and%20balanced%20diets%20for%20children%20in%20school)%20Regulations,%202026.pdf ; FSSAI list: https://fssai.gov.in/food-law/notifications | (1) The title in the claim is wrong. (2) The regulation says "high in saturated fat or trans-fat or added sugar or sodium", not "fat, salt or sugar", and it gave no thresholds; the 2026 draft is the first attempt to define them. (3) **The two core provisions, the campus sale ban 3(5) and the 50 m rule 5(1), were deferred to a date FSSAI must notify.** I found no such notification. On 3 Sep 2026 FSSAI's CEO called the campus-plus-50 m curb "a draft regulation" and "a proposal that we have submitted before the Honourable Supreme Court" (ANI, a secondary source: https://www.aninews.in/news/business/fssai-plans-curbs-on-high-fat-food-sales-within-50-metres-of-schools-ceo-rajit-punhani-says20260903192457/). Treat those two provisions as **not in force nationally**. (4) Some provisions are in force from 1 Jul 2021 on the text: the warning board at the gate 3(6); no HFSS ad banners or wallpaper on school computers 3(7); premiums, incentives and sponsorship only with non-HFSS food 5(2); and 5(3), under which FBOs must not "market, sell, or give away" HFSS food "anywhere on school campuses" via logos, vending machines, materials, "direct sale", free samples or fundraising. Without a definition of "high", enforcement is weak. (5) Maharashtra FDA issued a state order on 28 Jul 2026 enforcing the 50 m rule. This is from news only (FPJ, 21 Aug 2026), not verified from the order. Auditor E's row 18, which calls these "India's only statutory HFSS availability and marketing restriction currently in force", is wrong for the 50 m and sale-ban parts. |
| 4 | 2024 Food-EPI of India's government policies (Lancet Reg Health SE Asia 2024) rated India's restriction of food marketing to children weak | **CONFIRMED (with scope correction)** | "A discrepancy was noted in India regarding the implementation of marketing restrictions on unhealthy food products to children, which was reported as fully implemented by WHO but rated as weak in our study. This difference may arise from the narrower definition used by the Food-EPI tool which asks specifically about media and school marketing restrictions of unhealthy foods whereas in the WHO report it is related to a set of 12 guidelines on food marketing." India overall: "43% of the indicators were rated as weak and 57% as moderate" | https://pmc.ncbi.nlm.nih.gov/articles/PMC11260855/ (Pineda E et al., Lancet Reg Health Southeast Asia 2024;26:100428, doi:10.1016/j.lansea.2024.100428, PMID 39040122) | This is a **four-country South Asia comparison** (Bangladesh, India, Pakistan, Sri Lanka) covering policies from 2020–2022, not an India-only Food-EPI. The India paragraph also lists as *moderate* an indicator justified "as the promotion of foods high in fat, sugar and salt is prohibited in schools". The indicator codes are stripped from the PMC text, so it cannot be seen which PROMO indicators were weak. Safe wording: "rated weak overall; the school-promotion item was moderate". |
| 5 | 2025 definition of obesity for Asian Indians (Misra et al., reported as Lancet Diabetes & Endocrinology 2025) with Stage 1 / Stage 2 | **CORRECTED (journal)** | "In Stage 1 Obesity, individuals exhibit increased adiposity (BMI>23 kg/m) without discernible effects on organ functions or daily activities. Stage 2 Obesity denotes a more advanced state … The criteria for Stage 2 Obesity include a mandatory BMI exceeding 23 kg/mand at least one of the following: excess waist circumference or waist-to-height ratio." | https://pubmed.ncbi.nlm.nih.gov/39814628/ (doi:10.1016/j.dsx.2024.102989) | Published in **Diabetes & Metabolic Syndrome: Clinical Research & Reviews** 2025;19(1):102989 (Misra A, Vikram NK, Ghosh A, Ranjan P, Gulati S et al.), not Lancet D&E. It is a Delphi-based definition. The two-stage scheme is confirmed from the abstract only; the full text was not opened. A likely cause of the mix-up is that Misra is a co-author of the Rubino Lancet D&E Commission (claim 6). A PubMed search for Misra in Lancet D&E from 2024 on found no obesity-definition paper. |
| 6 | Rubino et al. 2025 Lancet D&E Commission: 18 adult diagnostic criteria for clinical obesity, incl. HFpEF, AF, and CKD or albuminuria | **CORRECTED (renal item)** | Table 2, adults. 4: "Reduced Left Ventricular systolic function - Heart Failure with Reduced Ejection Fraction - HFrEF". 5: "Chronic/recurrent atrial fibrillation". 6: "Pulmonary artery hypertension". 7: "Chronic fatigue, lower limb edema due to impaired diastolic dysfunction- Heart Failure with Preserved Ejection Fraction - HFpEF". 8: "Recurrent DVT and/or pulmonary thromboembolic disease". 9: "Raised arterial blood pressure". 12 (Renal): "Microalbuminuria with reduced eGFR". Also 11 (Liver): "NAFLD with hepatic fibrosis". | https://pmc.ncbi.nlm.nih.gov/articles/PMC11870235/ (Table 2; Lancet Diabetes Endocrinol 2025;13(3):221-262, doi:10.1016/S2213-8587(24)00316-4, PMID 39824205) | There are 18 adult criteria (and 13 for children and adolescents). HFpEF and AF are confirmed. **There is no "CKD" item and no stand-alone "albuminuria" item: the renal criterion needs microalbuminuria *with* reduced eGFR.** The Commission says it deliberately uses "individual alterations of organ function, not diseases in their own right" as criteria. The cardiorenal set is items 4–9 plus 12. Corrections to auditor A's row 79: the liver item reads "NAFLD with hepatic fibrosis", not "MASLD", and "LV dysfunction" is specifically HFrEF. The PMC copy is the NIH author manuscript. |
| 7 | Poshan Tracker records growth measurements of about 6.3 crore under-5 children and codes overweight | **CONFIRMED** | "The tracker also enabled growth monitoring for over 6.3 crore children aged 0–5 years, covering nearly 94% of registered beneficiaries as of May 2026. The application tracks stunting, underweight, wasting (SAM/MAM), and overweight/obesity indicators." Also: "Poshan Calculator: Uses WHO Child Growth Standards … classifying children across stunting, underweight, wasting, SAM/MAM and overweight/obesity" | https://www.pib.gov.in/FactsheetDetails.aspx?id=150744&NoteId=150744&ModuleId=16&reg=6&lang=1 (PIB Research factsheet, 8 Jul 2026) | Precise wording: "over 6.3 crore", "aged 0–5 years", as of May 2026. Not verified: whether overweight counts or rates from the Tracker are published or accessible to researchers. |
| 8 | Semaglutide's Indian patent expired March 2026 and generic semaglutide launched in India | **CONFIRMED (with precision)** | Delhi HC Division Bench, 9 Mar 2026: "this appeal has been preferred when the suit patent itself is to expire on 20 March 2026 … after 20 March 2026, the appellant would no longer be able to enforce the suit patent, and it would be open to exploitation by the world at large." The suit patent is Indian Patent 262697, "ACYLATED GLP-1 ANALOGS COMPRISING NON-PROTEOGENIC AMINO ACID RESIDUE", priority date 18 Mar 2005. MoHFW, 24 Mar 2026: "With the recent introduction of multiple generic variants of GLP-1-based weight loss drugs in the Indian market". | https://s3.ap-south-1.amazonaws.com/indian-high-court-judgments/data/pdf/year=2026/court=7_26/bench=dhcdb/DLHC011006272025_1_2026-03-09.pdf (Novo Nordisk v Dr Reddy's, FAO(OS)(COMM) 204/2025) ; https://www.pib.gov.in/PressReleasePage.aspx?PRID=2244252&reg=3&lang=1 ; CDSCO generic approvals: https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2018/UploadCommitteeFiles/Recommendations%20Endocrinology%20Metabolism%2009.12.2025(1).pdf | The expiry is of the **compound patent IN 262697 (injection), on 20 Mar 2026**. Other semaglutide patents remain, such as the oral-tablet SNAC patent IN 325669, which was in litigation in March 2026 (SpicyIP, a secondary source). "Launched" is supported by MoHFW's "recent introduction of multiple generic variants". Specific brands, launch dates and the "50–60% cheaper" price claim were **not** verified from primary sources. |

## Sources that failed or were not used
- curl to static.pib.gov.in, fssai.gov.in, ebi.ac.uk and eutils.ncbi.nlm.nih.gov was blocked by the egress proxy (403). The same URLs were read through TinyFish.
- The Lancet HTML for Rubino was bot-blocked, so the PMC XML via NCBI efetch was used instead. The indiankanoon mirror was bot-blocked, so the court PDF was used instead.
- Not opened: the CDSCO final permission letters for the generic semaglutide products, the original adult Wegovy approval minutes, the NFHS-6 fact sheets, any FSSAI commencement notification for regs 3(5) and 5(1) (none found), and the Maharashtra FDA order of 28 Jul 2026.
