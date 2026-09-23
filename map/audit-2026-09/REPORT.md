# Curriculum constitution audit, 23 September 2026

**Question (Harsh):** do the 61 subjects, 195 rungs and 196 books cover every competency and concept
needed to attack obesity at every level, from the clinic to policy?

**Answer:** no, but the map is not broken. The map has been checked only against the document it was
derived from. This audit is the first check against outside standards. About 56% of 879 external
framework items are fully covered, 31% partly, 1% routed away on purpose and 12% absent. The absent
and partial items reduce to about eleven verified themes. Nearly all of them can be closed by adding
bullets to rungs that have not been built yet. That needs no new books and changes no numbering.
The bigger finding is about shape, not coverage. The map was built for a methods-strong
researcher-adviser with a regulatory niche. The goal "from clinics to policy" is wider than that.
Three of the gaps are deliberate choices in the map, and only Harsh can decide on those.

Evidence: `claude/curriculum-audit-2026-09-verification.md` (verified, with map line numbers and
primary-source quotes) and `claude/curriculum-audit-2026-09-evidence.md` (the six raw audits, with
every framework item and URL).

---

## 1. Why the existing "coverage audit" does not answer the question

`map/subject-map-v3-FROZEN.md` line 45 ("Coverage audit") checks the map against the 58-item
checklist and 12-step causal spine of *Obesity Expertise: A First-Principles Curriculum*, the
document the map was derived from. That test shows nothing was lost in transcription. It cannot show
whether the source itself left anything out. That source document is not in the repository or the
project. S61, which routes adjacent fields, routes only the source's own "literate/aware" items
(line 4422). So any topic the source never considered is neither taught nor routed.

## 2. How this audit was run

- Six auditors worked in parallel. Each opened external frameworks and mapped every item onto the
  rungs as COVERED, PARTIAL, ROUTED or ABSENT, searching at least three synonyms before calling
  anything absent.
  - **A. Clinical:** OMEC competencies, the ABOM exam outline, the 2025 Lancet Commission on clinical
    obesity, the Canadian clinical practice guideline, Indian consensus statements.
  - **B. Policy:** the WHO Acceleration Plan, NOURISHING and MOVING, INFORMAS and Food-EPI, the Global
    Syndemic Commission, the WHO NCD best buys, the WHO GLP-1 guideline.
  - **C. Causes:** all 108 variables of the Foresight obesity system map, and the ANGELO framework.
  - **D. Professional public health:** WHO-ASPHER, Council on Linkages Tier 3, the NMC MD Community
    Medicine curriculum, WHO UHC competencies and EPHF, the Ottawa Charter.
  - **E. India:** programmes, regulations, data systems and institutions, each confirmed from an
    official or peer-reviewed page.
  - **F. Blind derivation:** a first-principles matrix of levels × verbs, written to disk *before*
    the map was opened, then compared with it.
- Two fresh verifiers then tried to refute the findings.
  - **V-map** searched the full map text, including the "Why this level" and "What it buys you"
    prose that the auditors' index left out. It also looked for text showing an exclusion was
    deliberate.
  - **V-facts** re-opened the primary source for eight external facts that drive decisions.
- Result: no gap was fully refuted, but several sub-claims were (§7).

**Counts** (the auditors' own tallies; frameworks overlap, so this measures breadth, not independence):

| Audit | Items | Covered | Partial | Routed | Absent |
| --- | --- | --- | --- | --- | --- |
| A Clinical | 142 | 76 | 48 | 1 | 17 |
| B Policy | 122 | 45 | 59 | 1 | 17 |
| C Causal system | 153 | 73 | 38 | 5 | 37 |
| D Professional | 216 | 134 | 59 | 1 | 22 |
| E India | 49 | 21 | 26 | 0 | 2 |
| F Blind derivation | 197 | 140 | 42 | 1 | 14 |
| **Total** | **879** | **489 (56%)** | **272 (31%)** | **9 (1%)** | **109 (12%)** |

Policy (B) has the lowest covered share. The map teaches the *evidence* on a policy lever much more
often than the *design* of the instrument.

## 3. What the map is built to produce

This is the most important finding, and it is a design choice, not an oversight. The map says so itself:

- Front matter, line 37: "The cap is as load-bearing as the spike."
- Line 39: the Expert targets "cluster … measurement, causal inference, nutritional epidemiology, the
  Indian phenotype, circadian biology, Indian data and Indian regulation."
- S55-R2, line 4013: of the four assets of recognition, institutional position is "manufactured by
  the first three" (papers, data custody, a teaching lineage).
- S55-R3, line 4034: "administrative capture" and "awareness-poster capture" are named as failure modes.
- S51-R3, line 3745: influence comes from "years being reliably useful … making officials look competent".

Verified structure (V-map recomputed it from the register):

- **Research methods take 57–68 of 195 rungs** (29–35%), depending on definition. The range is 57–89
  if research craft and modelling are counted. By Part, *Implementation and health-systems delivery*
  is the smallest, with 6 rungs.
- **Expert targets:** 8 of 19 are strictly methods, measurement or computation (11 if S18, S54 and S55
  are counted), 5 are biology, 2 are stigma/ethics, and **1 (S48) is a change-making lever**.
  S34, S37, S39, S41, S47, S50 and S51 stop at Advanced; S43 and S49 at Intermediate.
- **No subject is organised around the family or household, the settings where prevention is
  delivered (anganwadis, schools, workplaces), or the physical-activity environment.**
- About 58 of 195 build targets are publications and about 55 are real-world artefacts. That is a
  keyword estimate by audit F.

In short, the map produces a methods-strong academic public-health physician, with district and state
implementation skills and a regulatory specialism. That is a credible route to influence, but it is
one route. "Attack obesity at every level" also needs whoever designs the school or anganwadi
programme, drafts the marketing rule and runs the unit that lasts. Whether the persona should widen is
**Decision 2** (§9).

## 4. Verified gaps

"Where it goes" is V-map's recommended rung. **Build #** is the book's position in `map/BOOKS.yml`
(Book 1 is S01-R1), which shows how soon a decision is needed.

### Tier 1: the map argues for these but never builds them (internal inconsistencies)

| # | Gap | Evidence the map wants it | Where it goes | Build # |
| --- | --- | --- | --- | --- |
| 1.1 | **Settings.** Designing anganwadi/ICDS nutrition, school food standards and PE, and workplace programmes. RBSK/RKSK as platforms. | S26 prose, line 1995: prevention belongs "inside the machinery … ICDS, school health"; also lines 1245 and 2041. Searches for "anganwadi", "canteen" and "physical education" return 0 hits. | S26-R3, S51-R3, S34-R3 | 153–174 |
| 1.2 | **Designing availability and marketing restrictions** (including digital and packaging), public food-procurement standards, double-duty standards for PDS, PM POSHAN and ICDS, and a *government* Food-EPI. Menu labelling. | S34-R3, line 2613: the lever hierarchy puts "availability and marketing restriction" above labelling as "the strategic heart of the whole curriculum". The map teaches design for levers 1, 2 and 4, but not 3. | S47-R3, S48-R3, S37-R2/R3, S39-R3, S38-R3 | 65–165 |
| 1.3 | **Early life.** Infant and young child feeding, breastfeeding promotion and protection (IMS Act), rapid infant weight gain, parental feeding, growth monitoring, paediatric complications. | Lines 1993, 2004 and 3912: "India's obesity problem is arriving through its children". Searches for "infant", "IYCF" and "IMS Act" return 0 hits. Breastfeeding appears only as a confounding problem (line 1295). | S26-R2/R3, S48-R2 | 76–169 |
| 1.4 | **Clinical care to its endpoint.** (a) Cardiorenal criteria: HFpEF, HFrEF, AF, pulmonary hypertension, DVT/PE, microalbuminuria with reduced eGFR (Rubino 2025, Table 2). (b) Treating complications and deprescribing as weight falls, and switching to weight-neutral drugs. (c) Older adults, sarcopenic obesity, menopause. (d) Opening the conversation: asking permission, the 5As, shared decision-making. (e) Clinic design: MDT, recall, chronic-care model. (f) Weight recurrence after bariatric surgery, adjunct drugs, dumping. (g) Counselling on supplements and commercial products. | S20-R3 and S22-R3 cite the Lancet Commission's organ-dysfunction requirement (lines 1603, 1775) but name no cardiorenal criterion. S22-R3's build is "a weekly obesity or metabolic clinic slot, running" (1785) with no team specified. | S22-R1/R2/R3, S24-R2, S25-R2/R3, S23-R1, S26 | 34–169 (S22-R1 is #34) |

### Tier 2: blind spots (outside the source document's scope; nothing in the map argues against them)

| # | Gap | Where it goes | Build # |
| --- | --- | --- | --- |
| 2.1 | **Physical-activity environment**: built environment, walkability, active transport, municipal governance, the activity transition (Time Use Survey). Foresight: 11 of 13 PA-environment variables absent. S30 says activity is weak *for weight* (2273, 2313) but that "the health argument stands". | S30-R2/R3; extend S38-R2 GIS to activity; route urban/transport planning in S61 | 11 (S61), 84–142 |
| 2.2 | **Equity lenses**: gender (women's time use, intra-household food allocation), tribal populations (0 hits, yet the map names "rural Chhattisgarh", line 942), cultural norms (fasting, festivals, hospitality feeding, body-size ideals), language. | S17-R2/R3, S23-R2, S35-R3, S58-R3 | 103–164 |
| 2.3 | **Other determinants**: smoking and cessation-related weight gain, alcohol as intake (0 hits for both), ACEs and job strain. No causal-system map to locate any cause on; the HLPE food-systems framework is named (2815), Foresight and ANGELO are not. | S22-R2, S32-R2 or S17-R2, S44-R2 | 75–103 |
| 2.4 | **Named Indian entities**: CDSCO, the FSS school regulations 2020, Poshan Tracker, NNMB, the Time Use Survey, NFHS-6, RBSK/RKSK, the 2025 Indian obesity definition, NITI Aayog, NHSRC, the private sector as the main provider, AYUSH (recognise and route). | S54-R1/R2, S48-R2, S20-R3, S51-R1, S26-R3, S61 | 11 (S61), 58–169 |
| 2.5 | **Health literacy and label comprehension**. The live FOPL question at S48-R3 (line 3537) turns on this; the word appears only in that line. | S48-R3 or S29-R3 | 136, 151 |

### Tier 3: deliberate exclusions (Harsh decides)

| # | Gap | The map's own reason | Options |
| --- | --- | --- | --- |
| 3.1 | **Leadership and management**: running people, projects and budgets; building institutions; negotiating with ministries and industry; community mobilisation; sustaining oneself over decades. "Leader/leadership" has 0 hits. The map's own builds (a multi-district trial, an owned cohort, a state PIP activity) assume these skills. | Institutional position is a by-product (4013); "administrative capture" is a failure mode (4034). | (a) route explicitly in S61; (b) add project, team and budget skills to the rungs whose builds need them, plus a leadership thread in S57; (c) a new subject (+2–3 books) |
| 3.2 | **Campaign and social-marketing craft.** WHO lists mass-media campaigns among the best buys; the map ranks them the weakest lever. | S34 (2568, 2578, 2622), S55 (4034) | (a) route in S61 and keep "argue them toward structural levers"; (b) add campaign design at S34-R3 |
| 3.3 | **Overall shape**: methods-heavy; change-making capped at Advanced. | Front matter, lines 34, 37 and 39 | Keep the design (V-map: "no action"), or act through 3.1. Raising caps is the wrong lever. |

## 5. Two verified facts that change what a rung can ask of Harsh

1. **GLP-1 prescribers.** On 24 March 2026, MoHFW (press release 2244252) said: "the drug has been
   approved in India with condition of prescription by Endocrinologists and Internal Medicine
   Specialist and for some indications by Cardiologists only."
   - This is a CDSCO approval condition on retail sale. The PIB Research backgrounder of
     1 April 2026 repeats it. The CDSCO committee minutes show the same condition for tirzepatide
     (2023) and, for Wegovy in adolescents, "Endocrinologist or pediatrician" (23 March 2026).
   - Community Medicine is not on the list.
   - S24-R2 trains Harsh to initiate GLP-1s, and S22-R3's build is his own running clinic.
   - Not verified: whether the December 2025 generic semaglutide approvals carry the condition. Their
     committee minutes list none.
   - This is a regulatory condition, not an NMC scope-of-practice rule. Whether it bars him from
     prescribing is a legal question. Nothing here is legal advice.
   - **Decision 3.**
2. **The FSS school-children regulations 2020 are only partly in force.**
   - The title is *Food Safety and Standards (Safe food and balanced diets for children in school)
     Regulations, 2020*.
   - The campus sale ban (reg 3(5)) and the 50-metre rule (reg 5(1)) wait for a commencement
     notification. None was found, and FSSAI's CEO called the 50-metre curb a proposal on
     3 September 2026 (ANI, a secondary source).
   - A 7 August 2026 draft would take its HFSS thresholds from the Dietary Guidelines for Indians 2024.
   - This bears on Tier 1.2 and S48-R3.

Currency, verified: NFHS-6 was released on 29 May 2026 (PIB); the release has no adult obesity figure.
Semaglutide compound patent IN 262697 expired on 20 March 2026 (Delhi High Court, 9 March 2026).
The map's dated statements, such as its NFHS-3 to NFHS-5 comparisons, are scaffolding. They don't
reach the books unless a source opened at intake supports them, so the one rule already guards this.

## 6. What the audit did *not* find

- Nothing is wrong with the ground floor. Book 0 is untouched by every gap.
- **Book 1 (S01-R1, in flight) is unaffected.** No amendment touches S01.
- The biology, measurement, causal-inference, nutrition, sleep and circadian, commercial-determinants,
  fiscal and regulatory spine is strong in every framework it was compared with.
- The map's routing list (S61) is sound for what it routes. The problem is what it never considered.

## 7. Auditor claims the verifiers refuted or corrected

- **Supplements "absent":** wrong. S23 prose (1797) and S58-R3 (4255) cover them. What is missing is
  clinical counselling and the regulation of remedies.
- **"No health-promotion theory":** wrong. PRECEDE-PROCEED is at S50-R2 (3656), and COM-B, SCT, SDT
  and MRC are at S34-R2 (2596). Only the Ottawa settings approach and health literacy are missing.
- **"No determinants framework anywhere":** overstated. HLPE is named at S37-R2 (2815).
- **"Implementation to district scale only":** wrong. A state PIP is a build target (3753), and
  vertical scale-up is taught (3676). What is missing is running a *national* programme.
- **"11 of 19 Expert subjects are methods":** true only under a broad definition. The strict count is 8.
- Auditor E called the FSS 2020 school rules "the only statutory HFSS restriction in force"; that is
  wrong for the 50 m rule and the sale ban (§5). The Misra 2025 Indian definition is in *Diabetes &
  Metabolic Syndrome*, not Lancet D&E. The Rubino renal criterion is "microalbuminuria with reduced
  eGFR", not "CKD".

## 8. Recommended fix: amend, don't renumber

1. Keep `subject-map-v3-FROZEN.md` frozen. Add `map/AMENDMENTS-v3.1.md` holding one line per
   rung-level addition from Tiers 1–2, plus whatever Harsh decides for Tier 3.
2. Change one line of the inventory rule (`claude.md` line 541: "Collect the terminal requirements. From
   frozen v3 …") so that it also reads any amendment for that rung. The conductor then picks the
   additions up automatically, book by book.
3. The book count stays at 196, every ID and position stays the same, and `series.py` is untouched.
   The rungs get somewhat fuller.
4. **Timing:** the routing additions to S61-R1 fall at Book #11. The first clinical additions are
   S22-R1 (#34) and S23-R1 (#45). If Decision 2(b) puts a leadership thread into S57-R1, that one is
   #8. So the amendments file should land before about Book 8.
5. Deliver it as a small bundle *after* Book 1's bundle has been pulled, because bundles chain.
6. Only if Harsh wants it later: a second, narrower audit per subject at inventory time, against that
   subject's own external framework. The raw audits here already list the items.

## 9. Decisions for Harsh — taken 23 Sep 2026

**Outcome:** Harsh approved everything. Decision 1: all Tier 1 and 2 gaps closed. Decision 2: persona
widened inside existing rungs, no new books (leadership thread in S57; management, negotiation,
institution building and community mobilisation where builds need them; campaign design in S34-R3,
structural levers still first). Decision 3: GLP-1 hands-on builds are a clinic co-run with an
eligible physician who holds the prescription. Implemented as `map/AMENDMENTS-v3.1.yml` (113
entries, 50 rungs), enforced by `check/amendments.py` and the build. The questions as they were put:


1. **Approve Tiers 1 and 2 as amendments?** Recommended: yes. They are cheap now and expensive once
   the rungs are built.
2. **Persona (Tier 3.1 and 3.2):** keep the researcher-adviser design and route leadership and
   campaigns explicitly in S61, or add leadership and management skills (within existing rungs, or
   as a new subject)?
3. **GLP-1 prescribing (§5.1):** how should S24-R2 and S22-R3 frame hands-on prescribing? For example,
   as a clinic co-run with an eligible physician, as a knowledge-and-protocol target, or after getting
   his own legal clarity.

## 10. Caveats

- Several framework texts could not be opened in full:
  - Lancet Global Syndemic Commission (403).
  - WHO Acceleration Plan PDF.
  - Final 2024 best-buys edition (the 2023 draft was used).
  - MOVING sub-policies.
  - WHO GLP-1 guideline PDF.
  - Kushner 2019 and the Indian consensus papers: abstracts only.
  - WHO EPHF: domains only.
  - EASO has no published syllabus.
  - The official NMC PDF returned 404 (a university-hosted copy was used).
  - informas.org now serves unrelated content and must not be cited.
- Most auditor quotes passed through a summarising fetch tool. The eight facts in V-facts were
  re-read in full text. Everything else should be spot-checked before it is cited in a book.
- PARTIAL versus COVERED is a judgement against Harsh's goal, not a framework rule. The structural
  counts (§3) depend on category definitions, which are stated in the verification doc.
- The source document the map was derived from was not found, so the map could not be checked against
  anything it may have deliberately left out.
