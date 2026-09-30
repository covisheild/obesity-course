# Verification of the health-economics and AI/ML amendments (30 Sep 2026)

Two independent verifier rounds, kept as written. Every finding was applied (see `map/audit-2026-09/ADDENDUM-HE-AI.md` §4a).

## Verification R1: HE/AI addition of 30 Sep 2026 (17 entries, drafter HEAI)

Verifier: independent, adversarial. No repository file was edited.
What I did: read the brief rules, map front matter and every touched rung (via check/amendments.py). I checked
the 5 revise targets against the frozen map (lines 613, 749, 2616, 3149 and 3816 all match exactly), grepped the
map and the earlier amendments for duplicates, and re-opened the sources myself: PubMed abstracts and full text for
TRIPOD+AI, PROBAST+AI, CONSORT-AI, SPIRIT-AI, Obermeyer, Ho, Li, Fridolfsson, Gupta, Wiegand, Saumure, Noh, Singh,
the joint AI statement (PMC full text), Sharma 2023 (PMC full text) and Prinja 2021. I also opened the CDSCO PDF
and the ICMJE page with WebFetch.

Severity counts: error 3, should-fix 7, minor 7.

---

## Findings

### F1. S42-R2-A01 (and its `why`/`note`), severity: ERROR
**Problem.** The `why` says the reference case "defers a BIA method to a separate future document, so its status must be
read at intake", and the note says HTAIn BIA guidance "was not checked". Both are wrong. Sharma 2023 itself says that India's BIA
guidelines have already been published: the national methodological BIA guidelines (Prinja, Chugh, Rajsekar,
Muraleedharan, Appl Health Econ Health Policy 2021;19(6):811-823, reviewed by HTAIn's Technical Appraisal Committee).
The line therefore points the reader to the wrong document ("what India's reference case ... says about budget
impact"). The instrument that actually governs BIA in India is left out.
**Evidence.**
- Sharma 2023, PMC10485782 (doi 10.1016/j.lansea.2023.100241): "separate documents should be prepared on three important
  aspects including modelling, budget impact analysis (BIA) and cost-effectiveness thresholds (CET), in near future.
  In this context, the BIA guidelines for India have already been published." Also: "guidance documents such as the
  HTAIn process manual, the handbook for health system costing, and budget impact analysis (BIA) guidelines have also
  been developed."
- Prinja 2021, PMID 34184237, https://doi.org/10.1007/s40258-021-00668-y: "Our paper aims to present Budget Impact Analysis
  (BIA) guidelines for health technology assessment (HTA) in India ... A time horizon of 1-4 years is recommended ...
  BIA should be used along with evidence from economic evaluation for decision making, and not as a substitute".
**Proposed replacement.**
text: 'Budget impact analysis as the companion to cost-effectiveness, never its substitute: the eligible population,
the current treatment mix and how uptake changes it, the costs displaced, and a short horizon from one named payer''s
perspective, built to published good-practice principles and to India''s national methodological guidelines for
budget impact analysis; and the newer obesity drugs as the standing example of how a treatment judged cost-effective
over a lifetime can still cost more at population uptake than a payer can fund.'
why: '... Budget impact is absent from the map although S43-R2 asks how generic semaglutide could reach population
scale (3219). India has national BIA guidelines (Prinja 2021, reviewed by HTAIn''s Technical Appraisal Committee);
the reference case (Sharma 2023) says they "have already been published".'
sources: add https://doi.org/10.1007/s40258-021-00668-y. verify_at_intake: true can stay, to check for any later HTAIn revision.
note: delete "whether HTAIn has since issued budget-impact guidance was not checked".
Also correct ADDENDUM-HE-AI.md, which never mentions the Indian BIA guidelines.

### F2. S09-R3-A01, severity: ERROR
**Problem.** "mixed and culturally specific dishes, which most Indian meals are, are recognised worst" has two faults.
(a) "which most Indian meals are" is a factual claim that no opened source supports. Li 2024 is an Australian app study
and does not mention India, and the intake notes themselves say no Indian validation was found. (b) "recognised worst" is a
ranking that Li 2024 does not report. Li says only that AI recognition needs improving "especially for" these foods.
**Evidence.** Li 2024, PMID 39125452, https://doi.org/10.3390/nu16152573: "automatic energy estimations from AI-enabled
food image recognition were inaccurate ... training AI models are needed to improve AI-enabled food recognition,
especially for mixed dishes and culturally diverse foods." The apps were drawn from "Australia's Apple App and Google Play stores".
**Proposed replacement.**
text: 'AI-assisted dietary assessment as a new instrument to be validated, not trusted: food recognition, portion
estimation and nutrient lookup each add error; mixed dishes and culturally diverse foods, common in Indian diets, are
where recognition is reported to be weakest, and no validation against a reference method for Indian foods has been
found; a recognition score on a benchmark image set is not validity against weighed records or doubly labelled water;
and where food is served from a common pot the plate photographed is itself an uncertain exposure.'
If the drafter wants no descriptive claim about India, cut "common in Indian diets" as well. Also change the `why`
from "name mixed and culturally diverse dishes as the weak point" to "say recognition must improve especially for mixed
dishes and culturally diverse foods (Li 2024)".

### F3. ADDENDUM-HE-AI.md §4 "Which books pick them up", severity: ERROR
**Problem.** The list of the earliest affected book per subject is wrong in two places and out of order.
- S38: S38-R3-A03 sits at R3, so the book that bridges to it is S38-R2 (#109), not S38-R1 (#49). S38-R1 is not affected.
- S09: S09-R2-A01 revises an R2 line, so S09-R1 (#38) carries it as its bridge. The addendum names S09-R2 (#98) as the
  earliest and leaves S09-R1 out.
- The order claims to run by book number, but S42-R1 (#57) is placed before S38 and S34-R2 (#97) before S09-R2 (#98).
Evidence: BOOKS.yml gives S48-R1 #16, S06-R1 #29, S07-R1 #30, S09-R1 #38, S38-R1 #49, S42-R1 #57, S60-R1 #60, S52-R2 #67,
S34-R2 #97, S09-R2 #98, S38-R2 #109. All are "not started". The claim "Book #6 (S52-R1) is not affected" is correct,
because the S52 change is at R3 and reaches only S52-R2 and S52-R3.
**Proposed replacement.** "The earliest affected book is S48-R1 (#16, bridge to S48-R2), then S06-R1 (#29), S07-R1 (#30),
S09-R1 (#38, bridge to S09-R2), S42-R1 (#57), S60-R1 (#60), S52-R2 (#67, bridge to S52-R3), S34-R2 (#97, bridge to
S34-R3) and S38-R2 (#109, bridge to S38-R3). Book #6 (S52-R1) is not affected."

### F4. S48-R2-A05, severity: SHOULD-FIX (volatile legal status; overstates what the source is)
**Problem.** The line states a current legal status: CDSCO's regulation "reaches AI/ML-based software and apps ... and
excludes general-wellness software". The brief forbids stating legal status in a line. The source is also a guidance
document that calls itself non-binding, issued in 2026 after a 2025 draft. The line's inference that the question
"turns on its intended purpose and claims" is well supported. The status sentence should become a thing to read at intake.
**Evidence.** CDSCO PDF (doc CDSCO/MD/GD/MDSW/01/2026): "Mobile apps, AI/ML-based software and Cloud/Network-based software
that meet the definition ... are considered as MDSW". Wellness software "should not be making any reference to diseases or
disorders or pathological conditions". And: "This guidance document is aimed only for creating public awareness about
Regulations of Medical Device Software and is not meant to be used for legal or professional purposes."
**Proposed replacement.**
text: 'Governance of AI and digital health tools in India: how the Medical Devices Rules, 2017 and CDSCO''s guidance
on medical device software draw the line between regulated software — including AI/ML-based software and apps — and
general-wellness software, read at intake, so that whether a weight-loss app is a regulated device is decided from its
intended purpose and its claims (a reference to obesity as a disease is a claim); ICMR''s ethical guidelines for AI in
biomedical research and healthcare as the standard an ethics committee applies; and the Digital Personal Data
Protection Act for the data such tools collect.'
Also add to the note: "The CDSCO guidance says it is for public awareness and not for legal purposes; the binding
text is MDR-2017."

### F5. S42-R2-A01, obesity-drug example, severity: SHOULD-FIX (overclaim; folded into F1)
**Problem.** "the obesity drugs as the standing example of treatments judged cost-effective over a lifetime whose total
cost at population uptake a payer still cannot absorb" makes a general claim about every obesity drug and every payer.
The support is US-only (Pearson 2025; Ramachandran 2026), and one opened source (Hennessy 2026, in SOURCES-HE-AI §5)
found semaglutide *not* cost-effective at net price. Whether a drug is cost-effective depends on its price, which
changes, and no Indian analysis exists.
**Proposed replacement.** The F1 wording ("the newer obesity drugs as the standing example of how a treatment judged
cost-effective over a lifetime can still cost more at population uptake than a payer can fund") states the mechanism
rather than a universal verdict.

### F6. S60-R2-A01, severity: SHOULD-FIX (the cited evidence shows the opposite of one clause)
**Problem.** "stereotyped depictions of people with high body weight in AI-generated images". Saumure 2025 supports
stereotyping, but only when images are made "funnier". Wiegand 2025, the second source cited, found that people with high
body weight were *under-represented*: generators defaulted to normal weight. That is erasure, not stereotyping.
**Evidence.** Wiegand, PMID 40683994: "we observed an over-representation of White and normal weight individuals." Saumure,
PMID 39779743: "When ChatGPT updates images to make them 'funnier' ... people with high body weight groups are more
likely to be represented."
**Proposed replacement.** "... consent and secondary use of patient data for training; and how AI image generators
misrepresent people with high body weight — leaving them out of neutral depictions of patients and adding them as the
joke when asked for humour — so an AI tool is appraised for stigma and for whom it fails, as any other intervention is."

### F7. S52-R3-A01, severity: SHOULD-FIX (placement; near-duplicate of an existing home line)
**Problem.** The map already teaches ICMJE authorship at S56-R2 O5 (line 4102: "Authorship and collaboration: ICMJE
criteria, CRediT ..."). Why a chatbot cannot be an author is an ICMJE authorship criterion, so it belongs in that line.
Putting it in S52-R3 (Advanced R tooling) splits the ICMJE teaching across two subjects and delays it to R3, although
every resident who writes an R2 paper needs it. The fact itself is correct.
**Evidence.** ICMJE page: "Chatbots (such as ChatGPT) should not be listed as authors because they cannot be
responsible for the accuracy, integrity, and originality of the work"; "Authors who use such technology should
describe, in both the cover letter and the submitted work ... how they used it."
**Proposed replacement.** Keep S52-R3-A01 but trim it to the use and disclosure duty: "... Disclose how you used them,
as the ICMJE recommendations and journal policies require." Add a revise of S56-R2 O5 (line 4102, target quoted exactly
from the frozen map): "Authorship and collaboration: ICMJE criteria — including why an AI tool cannot be an author and
how its use is disclosed — CRediT, negotiating author order before the work starts, and being an excellent collaborator
by delivering early and making the senior author's life easier."
The alternative is to leave it as drafted and record the S56 overlap in the note.

### F8. Addendum §2 AI2 and S07-R2-A01, severity: SHOULD-FIX (missed existing line, inconsistency)
**Problem.** The gap check says "TRIPOD only", but S56-R2 O3 (line 4100) also lists "CONSORT and SPIRIT, ... PRISMA,
TRIPOD, CHEERS ...". After S07-R2-A01 the map says at S07-R2 that the 2015 TRIPOD "should no longer be used", while
S56-R2 O3 still tells readers to use TRIPOD.
**Evidence.** TRIPOD+AI, PMID 38626948: "The new checklist supersedes the TRIPOD 2015 checklist, which should no longer be used."
**Proposed replacement.** Add a revise of S56-R2 O3 (line 4100): "Reporting guidelines used at the design stage: CONSORT
and SPIRIT (with their AI extensions), STROBE and STROBE-nut, PRISMA, TRIPOD+AI, CHEERS, COREQ, ISPOR-SMDM." Or at least
record the dependency in the S07-R2-A01 note and correct the addendum row to "TRIPOD only (S07-R2 O3, S56-R2 O3)".

### F9. S06-R2-A01, severity: SHOULD-FIX (a clause no opened source supports, and a mild overclaim in `why`)
**Problem.** (a) "the recall of an automated screen is checked before it replaces a human screener" is not in the joint
statement, and RAISE was not opened. The statement says to pilot or calibrate a tool to validate its performance, and it
presents AI as a *second* reviewer, not a replacement. (b) The `why` says the organisations "endors[e] the RAISE
recommendations". The statement says they "support the aims of" RAISE.
**Evidence.** Joint statement, PMC12603384: "they may need to pilot (or calibrate) the AI system or tool to validate its
performance within their evidence synthesis"; "Using AI as a second 'reviewer' could help reduce this risk"; "The group
officially supports the aims of RAISE". PRISMA and "fully and transparently reported" are correct.
**Proposed replacement.** text: '... PRISMA 2020 asks which automation tools were used, and a tool''s performance —
for screening, its recall — is validated within the review before it is relied on.' why: '... issued a joint position
statement on AI in evidence synthesis in 2025, supporting the aims of the RAISE recommendations.'

### F10. S38-R3-A03, severity: SHOULD-FIX (strength of claim; one listed technique not in the source)
**Problem.** "are often used to promote less healthy foods" uses the review's own word, but the finding rests on 7 of
16 included studies, most of them outside India. As a line it reads as settled fact. "Ranking" is not among the
techniques Gupta lists; the review lists sorting and filtering features and search-engine optimisation.
**Evidence.** Gupta 2025, PMID 41366445: "we found that they were often deployed to preferentially promote nutrient-poor
foods. Specifically, seven studies highlighted the use of these marketing techniques to promote foods of poor nutritional
quality"; the techniques named include "algorithmic personalisation, push notifications, membership-based models,
interactive tools such as sorting and filtering features".
**Proposed replacement.** "Platform algorithms as part of the digital food environment: personalised ranking and
recommendation, push notifications and membership offers decide what each user is shown, and studies of delivery and
grocery platforms find them used to promote less healthy foods, so a user's exposure differs from the menu and cannot
be read from a menu scrape alone — which matters both for measuring the environment and for drafting marketing
restrictions that reach it."

### F11. S07-R2-A01 / S07-R2-A03, severity: MINOR (missing LLM standard)
**Problem.** S07-R1-A01 introduces LLMs, and S07-R2-A03 asks the reader to appraise "a chatbot ... against its reporting
standard". But the revised O3 names no standard for LLM studies. TRIPOD-LLM, an extension of TRIPOD+AI, exists.
**Evidence.** PMID 39779929, https://doi.org/10.1038/s41591-024-03425-5: "We present ... TRIPOD-LLM, an extension of the
TRIPOD + artificial intelligence statement, addressing the unique challenges of LLMs".
**Proposed replacement.** In S07-R2-A01 text, after "machine learning", insert "(with TRIPOD-LLM for studies of large
language models)". Add the DOI to sources and set verify_at_intake: true, because it calls itself "a living document".

### F12. S42-R2-A03, severity: MINOR
**Problem.** "the cost-effectiveness threshold it tells analysts to use" overstates the source, which says "may use". The `why` gives
Chugh as 2025, but the journal issue is 2026 (e-pub Oct 2025).
**Evidence.** Sharma 2023: "researchers may use one-time gross domestic product (GDP) per-capita until a CET is determined for India."
**Proposed replacement.** "... India's HTA reference case — including the interim cost-effectiveness threshold it allows
analysts to use, whether India has formally adopted one, and what the estimates of Indian willingness to pay per QALY
imply, all checked at intake." In the why, write "Chugh 2026 (e-pub 2025)".

### F13. S42-R2-A02, severity: MINOR (level and sources)
**Problem.** "Build a budget impact model" is execution at an R2 (read-critique-commission) rung. S42-R2 already asks
the reader to "Build a Markov cohort model in heemod", so this is consistent with the rung, but it goes further than the
rubric allows. The sources omit the Indian BIA guideline that the skill has to follow.
**Proposed replacement.** "Build a budget impact model for one obesity intervention for a named Indian payer — a state
scheme or PM-JAY — to India's budget impact analysis guidelines, and present it beside the intervention's
cost-effectiveness result, with uptake treated as the main uncertainty." Add https://doi.org/10.1007/s40258-021-00668-y to sources.

### F14. S34-R3-A05, severity: MINOR
**Problem.** The revision re-asserts the inherited "severe attrition". Neither new source reports attrition, and the
intake notes say so. The phrase is not the drafter's, but a revision is the chance to fix it.
**Proposed replacement.** Keep the line as drafted but change "severe attrition" to "high attrition", or record in the
note that the attrition claim is inherited and unverified.

### F15. S42-R3-A01, severity: MINOR
**Problem.** The `why` claim "Uptake is the largest uncertainty in the S42-R2 budget impact skill and in the S42-R3
microsimulation" is the drafter's judgement, not sourced. Bridges 2011 is a conjoint-analysis checklist, and the ISPOR
DCE-specific task-force reports were not consulted. The line text itself is fine.
**Proposed replacement.** why: "... Uptake is a main uncertainty in the S42-R2 budget impact skill ..." Add to the note:
"ISPOR DCE experimental-design and analysis task-force reports to be added at intake."

### F16. S09-R3-A01, severity: MINOR (partial overlap)
**Problem.** The clause "where food is served from a common pot" repeats S09-R3 O3 ("food is shared from a common pot").
It adds the photo angle, so it is acceptable, but it could be shortened to "and the common-pot problem (O3) makes the
plate photographed an uncertain exposure".

### F17. S48-R2-A05 placement, severity: MINOR
**Problem.** ICMR's research-ethics guidelines already sit at S56-R2 O4 ("ICMR national ethical guidelines"). The ICMR AI
guidelines "as the standard an ethics committee applies" fit there more naturally than in the regulatory-lever rung.
S48-R2 now carries 5 additions (the note says so). Suggestion: move the ICMR-AI clause to a revise of S56-R2 O4, or leave
it and cross-reference.

---

## Entries passed (no defect found beyond any minor noted above)
- S42-R1-A01: supported by YHEC, Robinson 1993 and Sullivan 2014. R1 recognise level; no volatile fact. PASS.
- S07-R1-A01: R1 recognise level, definitional, does not raise S07's Intermediate cap. PASS.
- S07-R2-A01: TRIPOD+AI supersedes TRIPOD 2015, PROBAST+AI "may replace" PROBAST ("successor" is fair), and CONSORT-AI and
  SPIRIT-AI cover trials and protocols; all verified. The target matches line 613 exactly. PASS, with minor F11.
- S07-R2-A02: the Obermeyer mechanism is correctly stated ("predicts health care costs rather than illness, but unequal
  access to care means that we spend less money caring for Black patients"). R2 level. PASS.
- S07-R2-A03: observable R2 appraise-and-decide skill. PASS.
- S09-R2-A01: target matches line 749. Ho 2020 supports under-reporting that is largest against doubly labelled water
  (-448 kcal) and "serious measurement errors". PASS.
- S34-R3-A05: target matches line 2616. Singh 2023 (74% low quality) and Noh 2023 (quality "low") support the `why`. PASS, with minor F14.
- S42-R3-A01: R3 concept. PASS, with minor F15.
- S52-R3-A01: target matches line 3816 and the ICMJE text is verified. Factually PASS; placement should-fix F7.
- Fridolfsson 2025 is verified: "All models exhibited systematic underestimation that increased with portion size".
- Cofre 2025 and Leslie 2023 were not re-opened; their intake quotes are PubMed abstracts and are plausible.
- The addendum's counts are verified: 17 entries = 12 new + 5 revisions across 13 rungs; the O-numbers and line numbers are
  correct; "Book #6 S52-R1 not affected" is correct.

## Verification R2: HE/AI addition of 30 Sep 2026 (20 entries, drafter HEAI)

Verifier: fresh, independent. No repository file was edited.
Checks run: `python3 check/amendments.py --check` gives amendments 133 | rungs touched 61 | problems 0.
`python3 check/build.py --check` gives records 126 | clusters 9 | blocking 0 | warnings 199, which equals the baseline.
All 8 revise targets were compared with the frozen map (613, 749, 2616, 3149, 3816, 4100, 4101, 4102). All match exactly, and the
O-numbers quoted in the addendum are correct (S07-R2 O3, S09-R2 O4, S34-R3 O4, S42-R2 O3, S52-R3 O5, S56-R2 O3/O4/O5).
Re-opened: the ICMR AI guidelines page (WebFetch), the ICMJE authors page (WebFetch), and PubMed metadata for Prinja 2021 (PMID 34184237)
and TRIPOD-LLM (PMID 39779929).

## 1. Round-1 findings

| F | Disposition | Evidence |
|---|---|---|
| F1 | Fixed | S42-R2-A01 text now names "India's national methodological guidelines for budget impact analysis". The why cites Prinja 2021, reviewed by HTAIn's TAC, and Sharma's words "have already been published". The Prinja DOI is in sources. The note keeps verify_at_intake for any later revision. Addendum HE1 names Prinja 2021. |
| F2 | Fixed | "which most Indian meals are" and "recognised worst" are gone. The line now reads "where recognition is reported to need most improvement". The why quotes Li's "especially for mixed dishes and culturally diverse foods" and flags that the apps are Australian. |
| F3 | Fixed | The list is in book order and matches BOOKS.yml: #16, #29, #30, #38, #52, #57, #60, #67, #97, #109. S38-R2 and S09-R1 are correct. S56-R1 (#52) was correctly added for the new S56-R2 revisions. All these books are "not started". "#6 not affected" is correct. |
| F4 | Fixed | The status is now "read at intake" and decided from "intended purpose and claims". The note says the guidance is for public awareness only and that MDR-2017 binds. Addendum AI7 says it is non-binding. |
| F5 | Fixed | The line now says "can still cost more at population uptake than a payer can fund". The note adds that cost-effectiveness depends on price. |
| F6 | Fixed | "leaving them out of neutral depictions … adding them as the joke when asked for humour". The why attributes each half correctly (Wiegand, Saumure). |
| F7 | Fixed | S52-R3-A01 is trimmed to the disclosure duty. S56-R2-A03 revises line 4102 and its target matches exactly. The ICMJE quote was re-verified (below). |
| F8 | Fixed | S56-R2-A01 revises line 4100 to TRIPOD+AI and the AI extensions, and its target matches. Addendum AI2 now cites "(S07-R2 O3, S56-R2 O3)". |
| F9 | Fixed | The line now says performance "is validated within the review before it is relied on". The why says "supporting the aims of the RAISE recommendations". |
| F10 | Fixed | The line uses "studies … find them used to promote less healthy foods". The why gives 7 of 16 studies, mostly outside India. |
| F11 | Fixed | TRIPOD-LLM is in the S07-R2-A01 text and sources, with verify_at_intake true and a living-document note. |
| F12 | Partly | The YAML is fixed ("allows analysts to use"; "Chugh 2026 (e-pub 2025)"). **Addendum §2 HE2 still says "Chugh 2025 proposes one."** |
| F13 | Fixed | S42-R2-A02 names India's BIA guidelines and has the Prinja DOI. The why justifies execution at R2 by the heemod skill. |
| F14 | Fixed | The line reads "high attrition", and the note says so. |
| F15 | Partly | The YAML why reads "a main uncertainty", and the note adds the ISPOR task-force reports. **Addendum §2 HE3 still says "Uptake is the main uncertainty in budget impact and in microsimulation."** |
| F16 | Fixed | The line reads "the common-pot problem makes the plate photographed an uncertain exposure". |
| F17 | Fixed | The ICMR AI clause moved to S56-R2-A02 (revise of line 4101), and the S48-R2-A05 note records the move. |

Totals: 15 Fixed, 2 Partly, 0 Not fixed.

Proposed fixes for the two partial fixes (ADDENDUM-HE-AI.md §2 table):
- HE2 cell: replace "Chugh 2025 proposes one." with "Chugh 2026 (e-pub 2025) proposes a range from a willingness-to-pay study."
- HE3 cell: replace "Uptake is the main uncertainty in budget impact and in microsimulation." with "Uptake is a main uncertainty in budget impact and in microsimulation."

## 2. The three S56-R2 revisions

- **S56-R2-A01** (line 4100). The target matches exactly. The claim "TRIPOD 2015 'should no longer be used'" was verified in R1 (TRIPOD+AI, PMID 38626948). "CONSORT and SPIRIT (with their AI extensions)" is supported by bmj.m3164 and bmj.m3210. The line holds no volatile fact. PASS.
- **S56-R2-A02** (line 4101). The target matches exactly. ICMR page re-opened: the title is "Ethical guidelines for application of Artificial Intelligence in Biomedical Research and Healthcare, 2023". The guidelines are addressed to "… clinicians, ethics committees, institutions, sponsors, and funding organizations". Their purpose is "to ensure ethical conduct and address emerging ethical challenges". The line's wording ("ICMR's ethical guidelines for the application of AI in biomedical research and healthcare") matches the title and leaves out the year. The year appears only in the why, which the rules allow. verify_at_intake: true. A PDF link (308.97 KB, ISBN 978-93-5811-343-3) is now present on the page, so the note "read the guideline PDF at intake" still applies. PASS.
- **S56-R2-A03** (line 4102). The target matches exactly. ICMJE page re-opened. It says "Chatbots (such as ChatGPT) should not be listed as authors because they cannot be responsible for the accuracy, integrity, and originality of the work". It also says "Authors should not list AI and AI-assisted technologies as an author or co-author". On disclosure, the page says authors should describe their use (acknowledgments for writing assistance, methods for data work). "Why an AI tool cannot be an author and how its use is disclosed" is supported. PASS.

New sources:
- **Prinja 2021** (PMID 34184237, doi 10.1007/s40258-021-00668-y), "National Methodological Guidelines to Conduct Budget Impact Analysis for Health Technology Assessment in India", Appl Health Econ Health Policy 2021;19(6):811-823. It was reviewed by the HTAIn TAC, which verifies the why. "BIA should be used along with evidence from economic evaluation … and not as a substitute", which supports "companion … never its substitute". "A time horizon of 1-4 years" supports "short horizon". The paper recommends "a payer's perspective, which will include both a multi-payer … and a single-payer scenario". See N2.
- **TRIPOD-LLM** (PMID 39779929, doi 10.1038/s41591-024-03425-5), Nat Med 2025;31(1):60-69. It is "an extension of the TRIPOD + artificial intelligence statement" and calls itself "a living document". The why's "TRIPOD-LLM (2025)" is correct, since publication was 8 Jan 2025.

## 3. New defects (cold read of all 20 entries plus the addendum)

### N1. MINOR: SOURCES-HE-AI.md has no intake record for the two new sources
Prinja 2021 and TRIPOD-LLM are now cited in YAML sources (S42-R2-A01, S42-R2-A02, S07-R2-A01), but SOURCES-HE-AI.md has no entry for either. Grep finds "40258", "03425" and "TRIPOD-LLM" 0 times. Every other cited source has one.
**Fix:** append to SOURCES-HE-AI.md:
```
### 13. Added at round-1 verification — OPENED (PubMed abstracts)
- Prinja S, Chugh Y, Rajsekar K, Muraleedharan VR. National Methodological Guidelines to Conduct Budget Impact Analysis for Health Technology Assessment in India. Appl Health Econ Health Policy 2021;19(6):811-823. PMID 34184237. https://doi.org/10.1007/s40258-021-00668-y
  - "These were reviewed by Technical Appraisal Committee (TAC) of Health Technology Assessment in India (HTAIn)"
  - "A time horizon of 1-4 years is recommended."
  - "We recommend a payer's perspective, which will include both a multi-payer (depicting the current situation in India) and a single-payer scenario"
  - "BIA should be used along with evidence from economic evaluation for decision making, and not as a substitute to evidence on value for money."
- Gallifant J, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med 2025;31(1):60-69. PMID 39779929. https://doi.org/10.1038/s41591-024-03425-5
  - "TRIPOD-LLM, an extension of the TRIPOD + artificial intelligence statement, addressing the unique challenges of LLMs"
  - "As a living document, TRIPOD-LLM will evolve with the field"
```

### N2. MINOR: S42-R2-A01 "one named payer's perspective" narrows what the Indian guideline recommends
The line says the analysis is built "to India's national methodological guidelines" but specifies "one named payer's perspective". Prinja 2021 recommends a payer's perspective that includes both a multi-payer scenario (India's current situation) and a single-payer scenario.
**Fix:** in S42-R2-A01 text, replace "and a short horizon from one named payer''s perspective," with "and a short horizon from the payer''s perspective — in India both the current multi-payer and a single-payer scenario —,". A shorter alternative is "and a short horizon from the payer''s perspective,". S42-R2-A02 ("for a named Indian payer") is an exercise and can stay.

### N3. MINOR: the disclosure duty is taught twice (S52-R3-A01 and S56-R2-A03)
S56-R2-A03 now teaches "how its use is disclosed" under ICMJE. S52-R3-A01 adds "Disclose how you used them, as the ICMJE recommendations … require". The overlap is defensible, because S52 has no prerequisites (map line 110), so S52-R3 cannot presuppose S56-R2. But the overlap is not recorded.
**Fix:** set the S52-R3-A01 note to: 'The disclosure duty is also taught with ICMJE authorship at S56-R2 (S56-R2-A03); it is repeated here because S56 is not a prerequisite of S52.'

### N4. MINOR: Addendum §4a asserts round 2 before it ran
"A second verifier checked the fixed entries." was written before this check. After this round it should state the result.
**Fix:** replace that sentence with "A second verifier confirmed 15 of the 17 fixes in full and 2 in the YAML only (the addendum's HE2 and HE3 cells, since corrected), and found 4 minor defects, all applied." (Adjust the wording to whatever is actually applied.)

### Checked and passed
- Counts: 20 entries = 12 new + 8 revisions across 14 rungs, which matches the YAML. The table rows, kinds, gaps and line numbers are all correct.
- Level fit: the R1 lines (S42-R1-A01, S07-R1-A01) only recognise. The R2 skills are appraise and build, which fits the heemod precedent. The R3 DCE line is a concept only.
- Chain: S07-R1-A01 anchors LLMs for TRIPOD-LLM at R2. S09-R2-A01 anchors S09-R3-A01. S42-R1-A01 anchors the budget impact and CBA lines.
- Volatile facts: none in any line text. The years appear only in why fields. "The 2015 TRIPOD checklist" names an edition, not a volatile fact.
- Duplicates: grep of the map and the earlier amendments finds no other TRIPOD, PROBAST, ICMJE, budget-impact or chatbot line.

## 4. Build
`python3 check/build.py --check`: blocking 0, warnings 199 (baseline unchanged). `check/amendments.py --check`: 0 problems.
