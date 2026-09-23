# V-amend: adversarial verification of merged-draft.yml (108 entries)

Verifier: fresh session, 23 Sep 2026. Everything below was checked against the files themselves, not against drafters' notes.
- **Check 1:** scripted. Each `target` was compared with the text at `map_line`, and each revise was diffed word by word against its target to find dropped words.
- **Check 2:** each new line was grepped against the full frozen map (4,456 lines) and against every other entry.
- **Check 4:** used the register (lines 57–119) and the real build order in `map/BOOKS.yml`. Book numbers are the `number:` field.
- **Check 5:** every source URL was traced to an audit file, and every fact was checked against V-facts. For Misra 2025, the PubMed abstract (PMID 39814628) was also re-read.

**Result:** 26 of 108 entries are defective (8 serious, the rest minor). 82 entries pass all eight checks.

## 1. Defective entries

Check numbers: 1 revise/target · 2 duplicate · 3 level · 4 chain · 5 one rule/facts · 6 Decision 3 · 7 coverage · 8 load.

| id | check | defect | concrete fix |
| --- | --- | --- | --- |
| **S22-R3-A02** | 6 | **Decision-3 hole.** The skill says to "switch weight-promoting drugs to … weight-reducing alternatives". For a diabetic patient, the obvious weight-reducing alternative is a GLP-1 RA or tirzepatide, and that is a restricted drug. The only safeguard the line has, "agreeing … with whichever prescriber owns the drug when it is not you", covers stopping *someone else's* drug. It does not cover Harsh starting a restricted one. | Append: "…and record the reason for every change; where the alternative is a drug whose approval restricts the prescriber, the eligible physician who co-runs the clinic holds that prescription." |
| **S24-R2-A04** | 1, 5 (form) | **Silent drop.** The original gate tested that Harsh runs the conversations "equally well". The new text drops that test, although the entry's `why` claims it "keeps the original test that both conversations are run well". It also turns the gate into a two-part test (the physician adopts the protocol AND leaves the conversations to him) that measures delegation, not quality. The target leaves out the `**Gate to the next rung.**` label. | Target: `**Gate to the next rung.** You run initiation and discontinuation conversations equally well.` Text: `**Gate to the next rung.** You run initiation and discontinuation conversations equally well, as judged by the eligible physician who co-runs the clinic and has adopted your protocol.` |
| **S29-R3-A01** | 4, 7 | **Gap 2.5 is misplaced.**<br>• The note says S48-R3 "stays lean" because this line exists. But S48-R3 is Book #136 and S29-R3 is Book #151, and S29 is not a prerequisite of S48 (S48's are S47 and S37).<br>• So the live FOPL book whose question "turns on" health literacy (line 3537) is written 15 books before literacy is taught, and it can never presuppose it.<br>• Nothing in the merged draft adds health literacy to S48. | Keep this line. Add a new **S48-R3 concept** (gap 2.5): "Label comprehension as the test a front-of-pack scheme must pass: a warning mark changes purchases only if shoppers with low literacy, reading in their own language in the seconds spent at a shelf, notice it, understand it and act on it — and what comprehension evidence a regulator or a court can be shown." |
| **S48-R3-A01** | 5 | **Two problems:**<br>• "what no Indian instrument yet reaches — digital, influencer and in-app marketing, child-appealing packaging, and promotion of breast-milk substitutes online" asserts a current legal status. The note admits it is an unchecked gap claim, and it may be wrong: the IMS Act's promotion ban is not limited by channel.<br>• "'high in' fat, sugar or sodium" misquotes the regulation, which says "saturated fat or trans-fat or added sugar or sodium" (V-facts 3).<br>The line handles commencement of regs 3(5) and 5(1) correctly. | Replace from "whether and how": "…whether and how 'high in saturated fat or trans-fat or added sugar or sodium' has been defined, which the 2020 text left open; and which channels — digital, influencer and in-app marketing, child-appealing packaging, online promotion of breast-milk substitutes — any Indian instrument currently reaches, established at intake." |
| **S48-R2-A01** | 5, 7 | **Two problems:**<br>• "Regulations, 2020, which make FSSAI a school-food regulator" states a legal status for a regulation whose two core provisions have not commenced.<br>• **Dropped handoffs.** S23-R2-A01's note passes "remedy advertising and nutraceutical regulation" to S48-R2, and this entry's own note assumes "A4 adds CDSCO … to S48-R2". No entry does either. So CDSCO is missing from the regulatory-architecture subject, and the regulation half of 1.4g (audit §7: "what is missing is clinical counselling and the regulation of remedies") is not closed. | Replace the FSS clause: "…Regulations, 2020, which bring FSSAI into school food alongside the Ministry of Education and CBSE, the commencement of each provision checked at intake;"<br>Append: "; and the regulation of weight-loss products outside food law and advertising codes: CDSCO as drug regulator, whose approval conditions govern obesity drugs; FSSAI's rules for health supplements and nutraceuticals; and the Drugs and Magic Remedies (Objectionable Advertisements) Act for advertised slimming remedies."<br>Add `gap: 1.4g` and keep `verify_at_intake: true`. |
| **S54-R2-A01** | 5, 2 | **Two problems:**<br>• "the only repeated intake data India has" is an asserted, contestable claim. `verify_at_intake` does not license stating it in the line.<br>• It is a new concept beside map line 3928 ("What each dataset can and cannot answer…"), which is the existing home for exactly this. The brief says to prefer a revise. | Make it a `revise` of 3928. Append to the existing line, before the final full stop: "; the Poshan Tracker, routine anganwadi growth monitoring of under-fives that codes overweight, with administrative-data caveats and researcher access to be established; ICMR-NIN's NNMB diet and anthropometry surveys, repeated rounds in a subset of states, and what those rounds can and cannot say about trends in intake; MoSPI's Time Use Survey, national 24-hour time diaries of activity, sedentary time, domestic work and travel." |
| **S51-R3-A03** | 5 | **Two problems:**<br>• It names Kayakalp and NQAS with no source and `verify_at_intake: false`.<br>• It calls them the facility's "procurement and quality route". They are quality and hygiene assessment and certification schemes, not procurement routes. | Text: "Write a food standard for one health facility's canteen, patient kitchen and campus vendors, build it into the canteen contract and the facility's quality assessment (NQAS or Kayakalp), and measure what changed on the counter." Set `verify_at_intake: true`. |
| **S26-R3-A04** | 7 | **Build and gate no longer match.**<br>• The revised build now allows an anganwadi or ICDS intervention with undernutrition outcomes.<br>• The unchanged gate (2051) still requires sign-off by "a school principal", which does not fit an anganwadi design.<br>• The note leaves this to "the conductor may wish". | Add a revise of line 2051. Target: `**Gate to the next rung.** A paediatrician, a psychiatrist and a school principal would each sign off your design.` Text: `**Gate to the next rung.** A paediatrician, a psychiatrist and the head of the platform that delivers it — a school principal or an ICDS supervisor — would each sign off your design.` This brings S26-R3 to 4.0 (at cap). |
| S37-R2-A01 | 2 | Repeats S37-R1-A01 almost word for word ("the state as food buyer and provider — PDS, PM POSHAN, ICDS supplementary nutrition and take-home rations"). The map's chain requirement says no rung repeats the rung below. | Text: "Public food provision beyond rations — meals served in public hospitals, hostels and government canteens — as a lever government controls directly; and double-duty actions, from the Global Syndemic framing of obesity, undernutrition and climate change as interacting problems with shared drivers, that reduce undernutrition and obesity together rather than fixing one while feeding the other." |
| S37-R3-A01 | 2 | Duplicates S51-R3-A03. Both have Harsh write the food standard for a hospital canteen. | Change "…or a hospital, hostel or government canteen…" to "…or a hostel or government canteen…". The hospital case then lives at S51-R3, where the health department controls it. |
| S39-R3-A02 | 2, 7 | **Two problems:**<br>• Near-duplicate of map 2972, "Run an India-specific benchmarking exercise using INFORMAS or ATNI instruments". The Food-EPI *is* an INFORMAS instrument.<br>• The build (2976) is still limited to "food industry practice". | Convert to a revise of 2972: "- Run an India-specific benchmarking exercise using INFORMAS or ATNI instruments — of food industry practice, or of government policy through a Food-EPI for India or one state: evidence document, briefed expert panel, implementation ratings and ranked actions."<br>Also revise 2976: "**Build target.** A published India benchmarking study of food industry practice or of government food-environment policy — publishable and politically useful in equal measure." |
| S51-R3-A04 | 2 | Repeats S50-R3-A01 ("expenditure accounting … utilisation statements and audit trail"). S50 is S51's prerequisite, and S50-R3 (#167) is built before S51-R3 (#174). | Text: "- Budgeting, procurement and the practical mechanics of getting an activity approved, paid for and accounted for inside the National Health Mission — fund flow and utilisation certificates — since an activity that cannot account for its spending rarely survives the next PIP cycle." |
| S26-R2-A03 | 4, form | "…as S16-R3 warns". S16-R3 is Book #158 and S26-R2 is Book #113, so the book cannot lean on a rung 45 books later. Map lines also never cite rung IDs. | Replace the tail: "…rapid infant weight gain and early adiposity rebound as risk markers — with the evidence read as largely observational and confounded by maternal education, income and body size." |
| S25-R2-A01 | 4 | "adjunct obesity pharmacotherapy" presupposes S24, which is not a prerequisite of S25 (S25's only prerequisite is S22). S25-R3-A01 then co-manages these drugs. The bridge is left to a note. | Put the bridge in the line: "…and its management with behavioural support, adjunct obesity pharmacotherapy (the agents, what each adds after surgery and who may prescribe them, taught here to the depth co-management needs) or revisional surgery." |
| S29-R3-A02 | 4 | Running a comprehension test needs sampling and randomised exposure to formats, which is study design (S15). S15 is not in S29's chain; S29's only prerequisite is S27. | "Design, with a survey or trial methodologist fixing the sampling and randomisation, and run a comprehension test of candidate front-of-pack formats…" (rest unchanged) |
| S33-R4-A02 | 4 | "hiring and supervising the trial team" is not taught in S33's chain (S19, S21, S32). S33-R4-A01 covers roles and the delegation log, not hiring. | Add to S33-R4-A01 after "the trial team's roles": "hiring to written roles," |
| S47-R3-A03 | 4 | Harsh conducts a negotiation with "an industry body" at S47-R3, but the conflict-of-interest rules (S60) are outside S47's chain; S47 has no prerequisites. Industry negotiation is already placed at S48-R4-A01, at a table the regulator convenes. | Delete "or an industry body". Industry negotiation then stays at S48-R4. |
| S51-R3-A05 | 4, form | **Two problems:**<br>• It is two skills in one: workforce planning, and designing and delivering training.<br>• Designing training whose effect is field-checked presupposes teaching and assessment craft (S57), which is outside S51's chain (S50 → S15, S36). | "Plan the obesity-care workforce for one district — which tasks sit with ASHAs, ANMs, community health officers, medical officers, dietitians and counsellors, how many of each the plan needs, and how they will be trained and supervised — and check one training's effect in the field months later rather than by a post-test on the day." |
| S57-R3-A03 | 4 | "a technical-support cell for a district" and "a funding line" presuppose district health-system and budgeting content. S57 has no prerequisites, although the note says "self-contained". | "Set up a standing group that does not depend on you — a working group or a teaching network — with written terms of reference, a plan, named roles and a named successor, and show that it has met and delivered without you in the room." |
| S20-R3-A02 | 5 | **Misra wording.** The line describes Stage 2 simply as adiposity "with" organ or functional effects. The PubMed abstract requires BMI plus excess waist circumference or waist-to-height ratio, **plus** functional limitation or obesity-related disease. The journal is correctly given as *Diabetes & Metabolic Syndrome*. | "…with its two stages: adiposity without discernible effects on organ function or daily activity, and generalised with abdominal adiposity accompanied by functional limitation or obesity-related disease, set beside…" (no cut-offs in the line) |
| S24-R1-A01 | 5 (low) | **Prescriber-condition wording.**<br>• The sources word the condition two ways: "sold by retail under prescription of" (SEC 2023) and "shall be prescribed by" (SEC 2026, MoHFW).<br>• V-facts stresses that it is a condition on retail sale enforced against sellers.<br>• The line says only "conditions on who may prescribe them". | "…approved with conditions, attached to the marketing approval and worded either as who may prescribe them or as on whose prescription they may be sold at retail, set by CDSCO on its Subject Expert Committee's advice; …" (rest unchanged) |
| S37-R2-A02 | 5 (low) | Names PM POSHAN and take-home rations with no source and `verify_at_intake: false`. | Copy S37-R1-A01's two PIB URLs into `sources`. |
| S22-R3-A03 | 1 (low) | The target is a substring of line 1785 and leaves out `**Build target.**`. A whole-line apply fails; a substring apply works but the convention is inconsistent with S26-R3-A04 and S55-R3-A03. | Prefix both `target` and `text` with `**Build target.** ` |
| S22-R3-A04 | 1 (low) | Same problem: `**Gate to the next rung.**` is missing (line 1787). | Prefix both with `**Gate to the next rung.** ` |
| S24-R2-A03 | 1 (low) | Same problem: `**Build target.**` is missing (line 1899). | Prefix both. |
| S38-R2-A02 | 1 (low) | Same problem: `**Build target.**` is missing (line 2892). | Prefix both. |

**Check 1 in full.**
- All 28 targets exist verbatim, and each occurs once in the map.
- 21 match the full line, either exactly or after its "- " bullet.
- 5 match only as substrings, because the bold label is missing (the rows above).
- Scripted word diff of every revise against its target:
  - Content dropped silently: only S24-R2-A04.
  - Content dropped with a stated reason:
    - S54-R1-A02 drops the 288%/91% figures, under the one rule.
    - S51-R3-A01 drops "Poshan Abhiyaan" because it is now inside Poshan 2.0 (E-india row 4).
    - S22-R3-A03 drops "slot".
    - S24-R2-A01 changes "initiate/escalate" to "escalation plan … initiation conversation" (Decision 3).
    - S34-R3-A04 narrows the skill.
  - All of these are acceptable.

**Check 3 (level).** No defects.
- No R1 line executes anything.
- Several R2 clinical lines execute: S23-R2-A01/A03, S26-R2-A04 and S35-R2-A01. The map's own clinical R2 rungs already do the same ("Deliver motivational interviewing competently" 1830, "Manage a patient…" 2671, "Initiate … a GLP-1" 1895), so these fit the rung as written.
- Both R4 lines are placed where the map already puts leading and negotiating: S33-R4-A01 next to "Lead a randomised … trial", and S48-R4-A01 at the seat at the table.

**Not defects, noted.**
- **S20-R3-A01 and S22-R2-A02** list the same cardiorenal criteria. This is justified: S22-R2 (#94) is built before S20-R3 (#139), and S20 cannot presuppose S22.
- **S22-R3-A01 and S24-R1-A01** both cover prescriber conditions. This is justified: S24 is not a prerequisite of S22.
- **S23-R2-A02 and S35-R3-A01** overlap on body-size and prosperity norms. The two subjects are not linked in the chain, and the framing differs (treatment planning versus stigma).
- All 80 source URLs were traced to an audit file. None cites informas.org.
- The Rubino wording ("microalbuminuria with reduced eGFR", items 4–9 and 12) is correct in S20-R3-A01 and S22-R2-A02.
- The FSS title and the non-commencement of regs 3(5) and 5(1) are handled correctly everywhere except the two S48 rows above.
- "ICMR-NINE (formerly NCDIR)" is confirmed by E-india row 45.

**Defect outside any entry (consistency).** S54-R1-A02 removes the NFHS 288%/91% figures, but the same figures stand at S26-R1 line 2004. S26-R1 is Book #53, so it is built first. Add a revise of 2004: "- That India's obesity problem is arriving through its children, a claim tested against each NFHS round, NFHS-6 included, by the relative rise in adolescents against adults recomputed rather than quoted." (gap 2.4; source: the NFHS-6 PIB URL.)

## 2. Coverage

| gap | closed by ids | status |
| --- | --- | --- |
| 1.1 anganwadi/ICDS design | S26-R1-A01/A02, S26-R3-A01/A02/A04, S51-R3-A01 | CLOSED (gate fix on S26-R3-A04 needed) |
| 1.1 school food standards and PE | S26-R3-A02 | CLOSED |
| 1.1 workplace | S34-R2-A01, S34-R3-A01 | CLOSED |
| 1.1 RBSK/RKSK as platforms | S26-R1-A01, S26-R3-A01/A04, S51-R3-A01 | CLOSED |
| 1.2 availability restriction design | S47-R3-A01, S48-R3-A01/A02, S38-R3-A01/A02, S26-R3-A02 | CLOSED |
| 1.2 marketing restriction incl. digital and packaging | S48-R3-A02 (S48-R3-A01 needs its fix) | CLOSED |
| 1.2 public procurement standards | S37-R3-A01, S51-R3-A02/A03 | CLOSED (de-duplicate) |
| 1.2 double-duty for PDS, PM POSHAN, ICDS | S37-R1-A01, S37-R2-A01/A02, S37-R3-A01 | CLOSED |
| 1.2 government Food-EPI | S39-R3-A01/A02 | CLOSED (convert A02 to revise) |
| 1.2 menu labelling | S38-R3-A01/A02 | CLOSED |
| 1.3 IYCF, breastfeeding, IMS Act | S26-R2-A03, S26-R3-A03, S48-R2-A01 | CLOSED |
| 1.3 rapid infant weight gain, parental feeding | S26-R2-A03/A04 | CLOSED |
| 1.3 growth monitoring | S26-R1-A01, S26-R2-A04, S26-R3-A01 | CLOSED |
| 1.3 paediatric complications | S26-R2-A01/A02 | CLOSED |
| 1.4a cardiorenal | S20-R3-A01, S22-R2-A02 | CLOSED |
| 1.4b complications, deprescribing, switching (+ G4h) | S22-R2-A03, S22-R3-A02 | CLOSED (Decision-3 fix needed) |
| 1.4c older adults, sarcopenic obesity, menopause | S22-R2-A04, S24-R2-A02 | CLOSED |
| 1.4d permission, 5As, shared decision-making | S22-R1-A01, S35-R2-A01 | CLOSED |
| 1.4e clinic design (team, recall, chronic-care model) | S22-R3-A01/A03/A04 | CLOSED |
| 1.4f recurrence after surgery, adjunct drugs, dumping | S25-R2-A01, S25-R3-A01 | CLOSED (bridge fix needed) |
| 1.4g supplement and commercial-product counselling | S23-R2-A01, S22-R2-A01 | CLOSED |
| 1.4g regulation of remedies and nutraceuticals (V-map G4g, audit §7) | none; the handoff to S48-R2 was never written | **NOT CLOSED**; fix via S48-R2-A01 row |
| 2.1 built environment, walkability, active transport | S30-R2-A02/A03, S30-R3-A01 | CLOSED |
| 2.1 municipal governance | S30-R2-A02, S30-R3-A01 | CLOSED |
| 2.1 activity transition (TUS) | S30-R2-A01 | CLOSED |
| 2.1 S38 GIS extended to activity | S38-R2-A01/A02 | CLOSED |
| 2.1 route urban and transport planning | S61-R1-A01 | CLOSED |
| 2.2 gender (time use, intra-household allocation) | S17-R2-A01/A02, S30-R2-A02 | CLOSED |
| 2.2 tribal | S17-R2-A01/A02, S17-R3-A01, S58-R3-A02 | CLOSED |
| 2.2 cultural norms (fasting, festivals, hospitality, body size) | S23-R2-A02/A03, S35-R3-A01 | CLOSED |
| 2.2 language | S58-R3-A01/A02 | CLOSED |
| 2.3 smoking and cessation weight gain | S22-R2-A01 | CLOSED |
| 2.3 alcohol as intake | S22-R2-A01 | CLOSED |
| 2.3 ACEs, job strain | S32-R2-A01 | CLOSED |
| 2.3 Foresight / ANGELO system map | S44-R2-A01/A02 | CLOSED |
| 2.4 CDSCO | S24-R1-A01, S22-R3-A01 | CLOSED for clinical; absent from S48 regulatory architecture (fix via S48-R2-A01) |
| 2.4 FSS school regulations 2020 | S48-R2-A01, S48-R3-A01 | CLOSED (wording fixes) |
| 2.4 Poshan Tracker | S17-R2-A03, S26-R1-A01, S26-R3-A01, S54-R1-A01, S54-R2-A01 | CLOSED |
| 2.4 NNMB | S48-R2-A02, S54-R1-A01, S54-R2-A01 | CLOSED |
| 2.4 Time Use Survey | S17-R2-A01, S30-R2-A01, S54-R1-A01, S54-R2-A01 | CLOSED |
| 2.4 NFHS-6 | S17-R2-A03, S54-R1-A01/A02 | CLOSED (S26-R1 2004 still carries the old figures) |
| 2.4 RBSK/RKSK | S26-R1-A01, S51-R3-A01 | CLOSED |
| 2.4 2025 Indian obesity definition | S20-R3-A02 | CLOSED (wording fix) |
| 2.4 NITI Aayog, NHSRC (+ ICMR-NIN, ICMR-NINE, PHFI) | S48-R2-A02 | CLOSED |
| 2.4 private sector as main provider | S51-R1-A01/A02 | CLOSED |
| 2.4 AYUSH recognise and route | S61-R1-A01, S51-R1-A01, S22-R2-A01, S23-R2-A01 | CLOSED |
| 2.5 health literacy and label comprehension | S29-R3-A01/A02 | **PARTIAL**: absent from S48-R3, which is built earlier (#136 vs #151) and has no chain link; fix = new S48-R3 concept |
| 3.1 people and team management | S57-R2-A01/A02, S57-R3-A01/A02, S50-R3-A01/A02, S51-R3-A05, S33-R4-A01/A02 | CLOSED |
| 3.1 project management | S50-R3-A01/A02, S33-R4-A01 | CLOSED |
| 3.1 budget management | S50-R3-A01/A02, S51-R3-A04, S54-R4-A01/A02, S55-R2-A02 | CLOSED |
| 3.1 institution building | S55-R2-A01, S55-R3-A01, S57-R3-A03, S54-R4-A01 | CLOSED; caution at 4034 kept |
| 3.1 negotiation with ministries, states, industry | S47-R3-A02/A03, S48-R4-A01 | CLOSED |
| 3.1 community engagement and mobilisation | S36-R3-A01, S50-R2-A01, S50-R3-A03, S51-R2-A01, S47-R3-A04 | CLOSED |
| 3.1 sustaining oneself over decades | S55-R3-A02/A03 | CLOSED |
| 3.1 leadership thread through S57 | S57-R1-A01, S57-R2-A01/A02, S57-R3-A01–A03 | CLOSED |
| 3.1 route institutional administration | S61-R1-A02 | CLOSED |
| 3.1 (extra, not asked) crisis communication | S58-R3-A03/A04 | added |
| 3.2 campaign and social-marketing design at S34-R3 | S34-R3-A02/A03/A04, S47-R3-A04 | CLOSED; lever hierarchy intact |
| 3.2 route production and media buying | S61-R1-A03 | CLOSED |
| Decision 3 regulatory-literacy item | S24-R1-A01 (+ S22-R3-A01 for the S22 chain) | CLOSED (wording fix) |

**Not closed:**
- 1.4g, the regulation-of-remedies half.
- 2.5, which is closed only at S29 and does not reach S48-R3.

## 3. Decision 3: lines in S22, S24, S25 and S26 that still have Harsh initiate or prescribe a GLP-1 or obesity drug

| line | where | status |
| --- | --- | --- |
| S22-R3-A02 (amendment) "switch weight-promoting drugs to … weight-reducing alternatives" | S22-R3 | **Still requires it** in the diabetic case, where the alternative is a GLP-1 RA or tirzepatide. Fix in §1. |
| Map 1897 "Select between agents for a specific patient and defend the choice" | S24-R2 | Ambiguous. Left unchanged deliberately (the drafter calls it a judgement). It does not require holding the prescription. Optional tightening: "Recommend an agent for a specific patient to the prescribing physician and defend the choice." |
| Map 1882 gate "No patient of yours starts one of these drugs believing it is a course" | S24-R1 | Compatible: it tests counselling, not prescribing. No change. |
| Map 1915 "Teach GLP-1 prescribing to physicians"; 2047 "Advise on adolescent pharmacotherapy" | S24-R3, S26-R3 | Compatible: teaching and advising. No change. |
| S24-R2-A01/A03/A04, S22-R3-A03/A04, S25-R3-A01 | | Fixed by the amendments: the co-run clinic in which the eligible physician holds the prescription. |

No line in S25 or S26, in the map or the amendments, requires Harsh to prescribe once the above are applied.

## 4. Load (new lines count 1, revises ½)

| rung | load | note |
| --- | --- | --- |
| S47-R3 | 4.0 | At cap. Coherent (policy craft), but the rung now has 6 skills. |
| S51-R3 | 4.0 | At cap. The most heterogeneous rung: convergence, NHM accounting, health-facility food setting and district workforce. A05 is a double skill (fix in §1). |
| S58-R3 | 4.0 | At cap. Coherent. |
| S26-R3 | 3.5, or 4.0 with the gate fix | At cap after the fix. |
| S26-R2, S34-R3 | 3.5 | |
| S22-R2, S22-R3, S23-R2, S30-R2, S50-R3, S57-R3, S61-R1 | 3.0 | S48-R3 also reaches 3.0 if the recommended 2.5 concept is added. |
| all others | ≤ 2.5 | |

No rung exceeds 4. The drafters' per-rung counts in `note` fields were re-counted and are correct.


---

# Round 2

# V-amend-r2: round-2 verification of AMENDMENTS-v3.1.yml (113 entries)

Verifier: fresh session, 23 Sep 2026. Everything was checked against the files, not against FIX-LOG.
- Every entry in `merged-draft.yml` was diffed field by field against `AMENDMENTS-v3.1.yml` (script).
  - No entry was dropped.
  - No text or target changed outside the V-amend rows, except for the stripping of "- " and labels.
  - The only changes to sources or verify flags are the two V-amend asked for (S37-R2-A02 sources, S51-R3-A03 verify).
- `check_amendments.py` was re-run and passes. All 33 revise targets match their map lines, and no two revises target the same line (checked separately).
- The Misra abstract was re-read on PubMed (PMID 39814628, doi:10.1016/j.dsx.2024.102989).
- V-facts claims 1, 2, 3, 5, 6 and 7 were re-read.

**Result:**
- 0 of the 26 V-amend defect rows are open. The S26-R1 consistency defect and both unclosed gaps are also closed.
- The new entries and the spot check found no serious defect, but they did find minor problems (§2, §5) that round 1 missed.

## 1. V-amend defect rows

| id | verdict | reason |
| --- | --- | --- |
| S22-R3-A02 | CLOSED | The Decision-3 clause is appended verbatim. The co-run clinic it refers to is on the same rung (A01, A03). |
| S24-R2-A04 | CLOSED | "equally well" is restored, and the co-running physician is the single judge. `why` is corrected. |
| S29-R3-A01 | CLOSED | Text kept; note rewritten. The S48 form is now S48-R2-A04, one rung lower than V-amend proposed, which still satisfies the chain rule for S48-R3 (line 3537). |
| S48-R3-A01 | CLOSED | The regulation's nutrient wording matches V-facts 3 exactly. The channel reach is "established at intake", so no status is asserted. |
| S48-R2-A01 | CLOSED | The FSS clause no longer states a legal status. The regulator half was moved to new entry S48-R2-A03 rather than appended here; that is acceptable. |
| S54-R2-A01 | CLOSED | Now a revise of 3928, with the target matching verbatim. The "only repeated intake data" claim is gone. |
| S51-R3-A03 | CLOSED | NQAS/Kayakalp are described as quality assessment, the canteen contract is the procurement lever, and `verify_at_intake` is true. |
| S26-R3-A04 | CLOSED | Paired with the gate revise S26-R3-A05 (but see §2 on A05). |
| S37-R2-A01 | CLOSED | Rewritten. It no longer repeats S37-R1-A01. |
| S37-R3-A01 | CLOSED | "a hospital" removed. |
| S39-R3-A02 | CLOSED | Now a revise of 2972, with the build revise S39-R3-A03 of 2976. |
| S51-R3-A04 | CLOSED | Limited to NHM fund flow and utilisation certificates, so there is no repeat of S50-R3-A01. |
| S26-R2-A03 | CLOSED | The forward reference to S16-R3 is removed. The confounding caution is in the line. |
| S25-R2-A01 | CLOSED | The pharmacotherapy bridge is in the line. |
| S29-R3-A02 | CLOSED | Sampling and randomisation are commissioned from a methodologist. |
| S33-R4-A02 (via A01) | CLOSED | "hiring to written roles" added to A01. |
| S47-R3-A03 | CLOSED | "or an industry body" deleted. |
| S51-R3-A05 | CLOSED | V-amend's text, adopted verbatim. |
| S57-R3-A03 | CLOSED | The district cell and the funding line are removed. |
| S20-R3-A02 | CLOSED | Checked against the PubMed abstract. The line's Stage 2 wording ("generalised with abdominal adiposity accompanied by functional limitation or obesity-related disease") matches the abstract: BMI >23, plus excess waist circumference or waist-to-height ratio, plus a limitation or comorbidity. No cut-offs are in the line. |
| S24-R1-A01 | CLOSED | Both wordings of the condition are covered: the prescription condition and the retail-sale condition. |
| S37-R2-A02 | CLOSED | Two PIB URLs added. |
| S22-R3-A03, S22-R3-A04, S24-R2-A03, S38-R2-A02 | CLOSED (by a different fix) | V-amend asked for the label to be prefixed to `target` and `text`. The fixer instead stripped every label and bullet and added `field: build/gate`. This is consistent across all 33 revises and passes a machine check. **Caveat:** BRIEF says `target` is the line "quoted exactly", and the `field` key is not in BRIEF. The inventory step that applies amendments must be told that it reattaches the label named by `field`. |
| S26-R1 line 2004 (consistency) | CLOSED | Closed by S26-R1-A03. Line 1993 is prose and still carries the 288%/91% figures. It cannot be amended and is left to the S26 book's intake, as FIX-LOG says. |

**OPEN: 0.**

## 2. The five new entries against BRIEF

| id | form / level | chain | duplicate | one rule | verdict |
| --- | --- | --- | --- | --- | --- |
| S48-R2-A03 | concept at R2 (recognise which body acts): fits | Teaches CDSCO itself, since S24 is not in S48's chain (S47, S37). The S48-R1 bridge must carry the vocabulary. | Overlaps S24-R1-A01 and S22-R3-A01 on prescriber conditions, which is justified because the chains are unlinked. "Magic Remedies", "nutraceut" and "CDSCO" get 0 hits in the map. | CDSCO is sourced to V-facts 1. "Enforcement reaches manufacturers, sellers and clinics" matches V-facts 1. The DMR Act, the FSSAI nutraceutical regulations and AYUSH licensing are unsourced but `verify_at_intake: true`. | PASS, with one low caveat: "FSSAI's regulations … which govern slimming products sold as food and the claims they may carry" is a statement of legal scope that no auditor verified. It is structural rather than dated, but the book must confirm it at intake. |
| S48-R2-A04 | concept at R2 (read and critique comprehension evidence): fits | R2 sits below R3, so S48-R3 (3537) reaches it. | Near-verbatim twin of S29-R3-A01. This is justified: S29 (prerequisite S27 only) and S48 (prerequisites S47, S37) are unlinked, and the precedent is S20-R3-A01 and S22-R2-A02. | Names no instrument. | PASS. S48-R2 is now at load 4.0 (cap), with 4 concepts. |
| S26-R3-A05 | gate, one pass/fail test: fits | fine | none | **Names ICDS with `sources: []` and `verify_at_intake: false`**, which breaks the letter of the one rule. S26-R3-A04 carries the ICDS/PM POSHAN URLs, which could simply be copied. | **MINOR DEFECT.** (1) Copy A04's sources. (2) The build explicitly allows delivery through RBSK or RKSK, but the gate's examples name only a principal or an ICDS supervisor. Fix: "— a school principal, an ICDS child development project officer or supervisor, or the RBSK/RKSK programme lead —". |
| S39-R3-A03 | build revise; target matches 2976 | fine | none | Names no instrument. | PASS |
| S26-R1-A03 | revise at R1: a "That …" concept. The recomputation is the book's job, not an act asked of the reader, so there is no R1 execution. | fine | Mirrors S54-R1-A02 by design. | NFHS-6 is sourced (PIB 2266600). | PASS, with one advisory point: V-facts 2 says NFHS-6 obesity figures are unverified (fact sheets not opened), yet the line presupposes that NFHS-6 carries adolescent and adult figures. Consider `verify_at_intake: true` here and on S54-R1-A02. |

## 3. Coverage (audit §4)

Every item below was re-checked against entry text, not against `gap` labels (see §5 for why the labels can't be trusted).

| item | closed by |
| --- | --- |
| 1.1 anganwadi/ICDS design; school food and PE; workplace; RBSK/RKSK platforms | S26-R3-A02/A04/A05, S26-R1-A01, S26-R3-A01, S34-R3-A01, S51-R3-A01/A03 |
| 1.2 availability and marketing restriction incl. digital and packaging; procurement standards; double-duty PDS/PM POSHAN/ICDS; government Food-EPI; menu labelling | S47-R3-A01, S48-R3-A01/A02; S37-R3-A01, S51-R3-A03; S37-R2-A01/A02, S37-R3-A01; S39-R3-A01/A02/A03; S38-R3-A01/A02 |
| 1.3 IYCF, breastfeeding, IMS Act; rapid infant weight gain; parental feeding; growth monitoring; paediatric complications | S26-R2-A03, S26-R3-A03, S48-R2-A01; S26-R2-A03/A04; S26-R2-A04, S26-R3-A01; S26-R2-A01/A02 |
| 1.4a cardiorenal | S20-R3-A01, S22-R2-A02 |
| 1.4b complications, deprescribing, switching | S22-R2-A03, S22-R3-A02 |
| 1.4c older adults, sarcopenic obesity, menopause | S22-R2-A04, S24-R2-A02 |
| 1.4d permission, 5As, shared decision-making | S22-R1-A01, S35-R2-A01 |
| 1.4e clinic design | S22-R3-A01/A03/A04 |
| 1.4f recurrence, adjunct drugs, dumping | S25-R2-A01, S25-R3-A01 |
| 1.4g counselling | S23-R2-A01, S22-R2-A01 |
| 1.4g regulation of remedies | S48-R2-A03 (**now closed**) |
| 2.1 | S30-R2-A01/A02/A03, S30-R3-A01, S38-R2-A01/A02, S61-R1-A01 |
| 2.2 | S17-R2-A01/A02, S17-R3-A01, S23-R2-A02/A03, S35-R3-A01, S58-R3-A01/A02 |
| 2.3 smoking and alcohol (text confirmed in S22-R2-A01); ACEs and job strain; Foresight and ANGELO | S22-R2-A01, S32-R2-A01, S44-R2-A01/A02 |
| 2.4 CDSCO | S24-R1-A01, S22-R3-A01, S48-R2-A03 |
| 2.4 FSS 2020 | S48-R2-A01, S48-R3-A01 |
| 2.4 Poshan Tracker, NNMB, TUS | S54-R1-A01, S54-R2-A01 (+ others) |
| 2.4 NFHS-6 | S17-R2-A03, S54-R1-A01/A02, S26-R1-A03 |
| 2.4 RBSK/RKSK | S26-R1-A01, S51-R3-A01 |
| 2.4 2025 Indian definition | S20-R3-A02 |
| 2.4 NITI Aayog, NHSRC | S48-R2-A02 |
| 2.4 private sector | S51-R1-A01/A02 |
| 2.4 AYUSH | S51-R1-A01, S61-R1-A01 |
| 2.5 health literacy and label comprehension | S48-R2-A04 (reaches S48-R3), S29-R3-A01/A02 (**now closed**) |
| 3.1 people, project and budget management; institution building; negotiation; community mobilisation; sustaining oneself; S57 thread; routing | S57-R1/R2/R3 entries, S50-R3-A01/A02/A03, S33-R4-A01/A02, S51-R3-A04/A05, S54-R4-A01/A02, S55-R2/R3 entries, S47-R3-A02/A03/A04, S48-R4-A01, S36-R3-A01, S50-R2-A01, S51-R2-A01, S61-R1-A02 |
| 3.2 campaign design at S34-R3 (lever hierarchy kept); route production | S34-R3-A02/A03/A04, S47-R3-A04, S61-R1-A03 |

**Still open: none.**

## 4. Decision 3: S22, S24, S25 and S26 map lines and amendments

I grepped the map (lines 1726–2052) and all amendments for initiat*, prescri*, start*, titrat*, escalat*, dose, agent, drug and pharmaco*.

**Hard violations** (a requirement that Harsh himself initiate or prescribe an obesity drug, once amendments are applied): **none.**
- Map 1895, 1899 and 1901 are replaced by S24-R2-A01/A03/A04.
- Map 1785 and 1787 are replaced by S22-R3-A03/A04.
- Map 1979 is replaced by S25-R3-A01.
- S22-R3-A02 now carries the restricted-drug clause.

**Residual ambiguities** (not violations, but for Harsh to decide):
- **Map 1897 (S24-R2), "Select between agents for a specific patient and defend the choice".** It is unchanged. It does not require holding the prescription, but it is a de facto prescribing decision. An optional revise: "Recommend an agent … to the prescribing physician and defend the choice" (FIX-LOG leaves this open).
- **S24-R2-A02 / map 1896, "Manage GI adverse effects".** Management may mean dose holding or reduction. This is compatible because the physician holds the prescription under A01.
- **Map 1861 (S24 prose), "know this at prescribing depth"; 1889, "dosing and escalation schedules"; 1915, "Teach GLP-1 prescribing"; 2047, "Advise on adolescent pharmacotherapy"; the S25-R3 gate, "the physician on a multidisciplinary bariatric team".** All are knowledge, teaching or advising, and are compatible.

## 5. Spot check of 10 unchanged entries (random, seed 20260923), plus a whole-file scan

The entries checked were S44-R2-A02, S34-R3-A01, S36-R3-A01, S47-R3-A04, S61-R1-A02, S50-R3-A02, S54-R4-A02, S30-R2-A02, S17-R3-A01 and S20-R3-A01. None has a content, level or chain defect. I also scanned all 113 entries for named instruments without a source.

Three things round 1 missed:
1. **`gap` labels for 1.4 use V-map's G4 letters, not the audit's.** BRIEF says `gap` is the *audit* gap id. V-map's G4a is complications and G4b is cardiorenal, while the audit has 1.4a as cardiorenal and 1.4b as complications. The audit also has no "1.4h". Five entries are mislabelled:
   - S20-R3-A01 and S22-R2-A02: "1.4b", should be "1.4a".
   - S22-R2-A03 and S22-R3-A02: "1.4a, 1.4h", should be "1.4b".
   - S20-R3-A02: "2.4, 1.4b", should be "2.4" (the definition is not complications).

   This is metadata only; the content closes the right gaps. It would mislead any coverage script keyed on `gap`.
2. **Named instruments with no source and `verify_at_intake: false`:**
   - S44-R2-A02 (Foresight map, ANGELO grid): copy S44-R2-A01's 4 URLs.
   - S26-R3-A05 (ICDS): see §2.
   - S51-R1-A02 (AYUSH) and S51-R3-A05 (ASHAs) are trivial: the cadre and system names are sourced in sibling entries.
3. **Stale notes:**
   - S51-R1-A01 points to "S23-R1" for remedy counselling; it is S23-R2-A01.
   - S34-R3-A01 says "May overlap A3", which is drafter chatter.

   These are harmless but should be cleaned before the file lands.

## 6. Caveats

- I did not reopen any URL except PubMed 39814628. Source traceability relies on V-amend's round-1 trace plus V-facts.
- Load was re-checked only through the script: 5 rungs are at 4.0 and none is over.
- The `field` convention (§1) needs a matching line in the inventory rule when the amendments file is wired in.


---

# Fix log

# FIX-LOG: merged-draft.yml to AMENDMENTS-v3.1.yml

- **Input:** 108 entries and the V-amend defect list.
- **Output:** 113 entries: 108 kept, with ids stable, plus 5 new. No entry was withdrawn.
- **Build script:** scratchpad `fix.py`.
- **Check script:** `/home/claude/amend/check_amendments.py`. Result: ALL CHECKS PASSED.

**Revise convention.** It is applied to all 33 revises.
- **Bullet lines:** `target` is the map line without its leading "- ".
- **Build and gate lines:** `target` is the text after the "**Build target.**" or "**Gate to the next rung.**" label, and the entry sets `field: build` or `field: gate`.
- **`text`:** follows the same convention as `target`.

## Defects (V-amend §1)

| id | change |
| --- | --- |
| S22-R3-A02 | Appended the Decision-3 clause: "where the alternative is a drug whose approval restricts the prescriber, the eligible physician who co-runs the clinic holds that prescription." |
| S24-R2-A04 | Restored the "equally well" test. Text: "…equally well, as judged by the eligible physician who co-runs the clinic and has adopted your protocol." Set `field: gate` and corrected `why`. |
| S29-R3-A01 | Kept the text; rewrote the note. The line carries the concept for S29's own chain. The S48 form is new entry S48-R2-A04. |
| S48-R3-A01 | Replaced the "high in" misquote with the regulation's wording ("saturated fat or trans-fat or added sugar or sodium"). Replaced the unchecked "what no Indian instrument yet reaches" claim with "which channels … any Indian instrument currently reaches, established at intake". |
| S48-R2-A01 | Replaced the FSS clause with "bring FSSAI into school food alongside MoE and CBSE, the commencement of each provision checked at intake". The regulator content moved into new entry S48-R2-A03 instead of being appended here. |
| S54-R2-A01 | Converted to a `revise` of line 3928 that appends the Poshan Tracker, NNMB and TUS clauses. Dropped "the only repeated intake data India has". |
| S51-R3-A03 | New text: "build it into the canteen contract and the facility's quality assessment (NQAS or Kayakalp)". Set `verify_at_intake: true`. |
| S26-R3-A04 | Removed the label (`field: build`). Added gate revise S26-R3-A05 (school principal or ICDS supervisor). |
| S37-R2-A01 | New text on public food provision beyond rations plus double-duty. It no longer repeats S37-R1-A01. |
| S37-R3-A01 | Removed "a hospital"; that setting now lives only at S51-R3-A03. |
| S39-R3-A02 | Converted to a `revise` of 2972 (INFORMAS/ATNI, now including a government Food-EPI). Added build revise S39-R3-A03 of 2976. |
| S51-R3-A04 | New text limited to NHM mechanics: fund flow and utilisation certificates. It no longer repeats S50-R3-A01. |
| S26-R2-A03 | Replaced the "as S16-R3 warns" tail with "confounded by maternal education, income and body size". |
| S25-R2-A01 | Moved the S24 bridge into the line: "(the agents, what each adds after surgery and who may prescribe them, taught here to the depth co-management needs)". |
| S29-R3-A02 | Added "with a survey or trial methodologist fixing the sampling and randomisation". |
| S33-R4-A02 | Added "hiring to written roles," to S33-R4-A01 after "the trial team's roles". Removed the "- " from A02's target and text. |
| S47-R3-A03 | Deleted "or an industry body". Industry negotiation stays at S48-R4-A01. |
| S51-R3-A05 | Made it a single skill: district workforce plan plus a field check of one training's effect. Removed "design and deliver training" (S57 is outside this chain). |
| S57-R3-A03 | Removed "technical-support cell for a district" and "a funding line". |
| S20-R3-A02 | Stage wording now follows the Misra abstract: "excess adiposity without discernible effects on organ function or daily activities" and "generalised with abdominal adiposity accompanied by functional limitation or obesity-related disease". No cut-offs in the line. |
| S24-R1-A01 | Condition now "attached to the marketing approval and worded either as who may prescribe them or as on whose prescription they may be sold at retail". |
| S37-R2-A02 | Added S37-R1-A01's two PIB URLs to `sources`. |
| S22-R3-A03 | Label convention: `field: build`, label-free target and text. |
| S22-R3-A04 | Label convention: `field: gate`. |
| S24-R2-A03 | Label convention: `field: build`. |
| S38-R2-A02 | Label convention: `field: build`. |

Also normalised: S55-R3-A03 (`field: build`, label removed). The leading "- " was stripped from the target and text of every bullet revise.

## Unclosed gaps closed, and the consistency defect

| new id | closes |
| --- | --- |
| S48-R2-A03 | **1.4g regulation of remedies, and CDSCO in S48.** Covers CDSCO approval conditions and enforcement, AYUSH medicine licensing, FSSAI health-supplement and nutraceutical regulations, and the DMR Act, whose schedule is read at intake. Sources are from V-facts claim 1, with `verify_at_intake: true`. |
| S48-R2-A04 | **2.5.** A health-literacy and label-comprehension concept at S48-R2, so that S48-R3 (line 3537 and the threshold skill) reaches it by the chain rule. The S29-R3 lines stay for S29's chain. |
| S26-R1-A03 | **V-amend consistency defect.** A revise of line 2004 that removes the NFHS 288%/91% figures, as S54-R1-A02 already does. |
| S26-R3-A05 | Gate revise of line 2051 (see S26-R3-A04). |
| S39-R3-A03 | Build revise of line 2976 (see S39-R3-A02). |

The following notes were updated to match these changes: S23-R2-A01, S48-R2-A02 and S54-R1-A02.

## Load

- Four rungs are at the cap of 4.0: S26-R3, S47-R3, S51-R3 and S58-R3. S48-R2 is also at 4.0, with 4 new concepts.
- No rung is over the cap.

## Left open (for Harsh)

- **Map line 1897 (S24-R2), "Select between agents … defend the choice".** It is unchanged; V-amend lists it as ambiguous and the change as optional. A revise to "Recommend an agent … to the prescribing physician" would remove the last ambiguity. It would bring S24-R2 to load 2.5.
- **S26 prose line 1993.** It still carries the 288%/91% figures. It is not an amendable line.
- **Unverified content in S48-R2-A03.** The DMR Act's schedule, the FSSAI nutraceutical regulations and AYUSH licensing were not verified by any auditor, so the entry depends on intake.
