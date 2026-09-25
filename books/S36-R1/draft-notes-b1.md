# Draft notes · S36-R1 · batch b1

Drafter, Task 2, 2026-09-24. Concepts S36-R1-C01, C02, C03.

## Records written

- `check/records/S36/S36-R1-C01.yml`: Two kinds of question: how many, and why and how
- `check/records/S36/S36-R1-C02.yml`: Who you talk to, and what the answers can claim
- `check/records/S36/S36-R1-C03.yml`: The interview: structured, semi-structured, in-depth

All three are `derivable`, `quantitative: false`, status `drafted`. `python check/build.py --check`
shows zero blocking and zero warnings for these three (whole build: blocking 0 at hand-back). The
records were generated from scripts in `/home/claude/scratch-b1/` (c01.py to c03.py), so every prose
field is a literal block.

C01 introduces the running setting (the made-up Chhattisgarh district hospital NCD clinic) and
expands NCD. C02 defines "respondent" in its definition; C03 introduces the speaker labels I and R1.

## Unsourced, or resting on a judgement the auditor should check

1. **The evidence hierarchy (C01).** No held source lays the hierarchy out as a ranked list. The
   record says only that evidence-based medicine gives most weight, for a treatment question, to the
   randomised controlled trial and the pooled result of several trials, and that the ranking is for
   that question. The support is indirect: Green & Britten's "good 'evidence' goes further than the
   results of meta-analysis of randomised controlled trials" and Pope & Mays calling the trial "the
   epitome of the quantitative method". This is noted in that reference's `verified.note`. If the
   auditor finds it too thin, cut the sentence about the pooled result and keep only the trial.
2. **Reference kinds (corrected on the coordinator's instruction).** Every journal article
   (Pope & Mays 1995, Britten 1995, Mays & Pope 2000, Pope, Ziebland & Mays 2000, Green & Britten
   1998, DeJonckheere & Vaughn 2019) is now `kind: primary`. Each record's `textbook` anchor is
   `blackstone_2012` (Principles of Sociological Inquiry, Saylor 2012), quoted from the section named
   in the locator: C01 from 1.2 (qualitative and quantitative methods defined; "complementary rather
   than competing", "different goals, strengths, and weaknesses"); C02 from 7.2 (representing the
   population "is not the goal"; the purposive sample covering "that full range of perspectives";
   caution in generalising from convenience samples); C03 from 9.2 (semistructured, open-ended
   questions, order and wording varied; the in-depth opening question). **Gap:** the held Blackstone
   sections do not describe the structured interview (9.3 is not held) or the contrast between a
   research interview and a clinical consultation, so those parts of C03 rest on Britten 1995 alone.
   Blackstone also treats in-depth and semi-structured as the same thing. That supports C03's point
   that the labels overlap, and it does not contradict the prose. No prose was changed.
3. **NCD gloss (C01).** "Long-lasting conditions that do not pass from person to person, such as
   diabetes and high blood pressure" is a plain-words label with no source. It is not a claim the
   section rests on.
4. **C02 illustration table ("Because..." column)** and C02/C03 exercise answers hold hypotheses
   about why patients might stop coming (fare, a day's wage, the first visit). Every one is worded
   as "may" and the setting is declared made-up; none is presented as a finding.
5. **C03, "a structured form may end with one open question"** (analogy_breaks_when): general
   knowledge, stated as a possibility, not sourced.
6. **C03, "sugar can be high without any symptoms"**: said by the interviewer in a made-up exchange
   as an example of correcting; it is not taught as a fact.
7. **DeJonckheere & Vaughn's "individual, face-to-face, in-depth interviews"** is used in C03 both as
   the source for "most common form is semi-structured, one person, face to face" and as the
   example of the labels overlapping. The same sentence carries both, which is the point.
8. **Britten on not correcting (C03)** comes from her paragraph on interviewing one's own patients.
   The reference note says it is cited only for the rule that a respondent is not corrected.

Every quote was confirmed in its file by the build's own normalisation (whitespace and case only).
No quote carries a number the record relies on except the must-know point "8 to 12" (C02), whose
quote states "8–12"; must-know points are not quote-checked, so the reference is in the definition
list and `refs` names the citekey.

No `[NOTE]` line or header was quoted. No box or table was reproduced: three single items from
boxes are quoted (Pope & Mays Box 1 purposive-sampling phrase, Box 3 stage heading; Britten Box 5
one item; Mays & Pope's quality-questions box, one sentence).

## OCR quotes (to check against the page images)

Copied exactly as the OCR layer has them; a space marks a line break in the layer.

**pope_mays_1995** (BMJ 1995;311:42-5, PMC2550091)
- p. 43: `Qualitativestudiesareconcernedwithanswering questionssuchas'WhatisX andhowdoesXvaryin differentcircumstances,andwhy?"ratherthan"How manyXsarethere?"` (C01)
- p. 43: `Therandomisedcontrolledtrial,withitsfocuson hypothesistestingthroughexperimentcontrolledby meansofrandomisation,canbeseenastheepitomeof thequantitativemethod.` (C01)
- p. 43: `Answeringthe"whatisX" question,though,isthefoundationofquantification: untilsomethingisclassifieditcannotbemeasured.` (C01)
- p. 43: `ageneralpractitioner,knowingthatintensiveinsulin therapyworksmaybesecondarytoknowingwhether thepatientwillcomplywiththetreatment.` (C01)
- p. 43, Box 1: `Purposiveorsystematicsampling-deliberatechoiceofrespondents,subjects,or settings,asopposedtostatisticalsampling` (C02)
- p. 44: `qualitativeworkcanbe conductedasanessentialpreliminarytoquantitative research.` (C01)
- p. 44: `Attheirmostbasic,these techniquescanbeusedsimplytodiscoverthemost comprehensibletermsorwordstouseinasubsequent surveyquestionnaire.` (C01)
- p. 44, Box 3: `IISociologicalstudy-explaininghowandwhy variationscomeabout` (C01)
- p. 45: `Itisnotthatqualitativemethods aresomehowsuperiortoquantitativeones` (C01)

**britten_1995** (BMJ 1995;311:251-3, PMC2550292)
- p. 251: `Therearethreemaintypes: structured,semistructured,andindepthinterviews` (C03)
- p. 251: `Structuredinterviewsconsistofadministering structuredquestionnaires,andinterviewersaretrained toaskquestions(mostlyfixedchoice)inastandardised manner.` (C03)
- p. 251: `theterm "unstructured"ismisleadingasnointerviewiscom- pletelydevoidofstructure` (C03)
- p. 251: `Semistructuredinterviewsareconductedonthe basisofaloosestructureconsistingofopenended questionsthatdefinetheareatobeexplored,at leastinitially,andfromwhichtheintervieweror intervieweemaydivergeinordertopursueanideain moredetail.` (C03)
- p. 251: `Indepthinterviewsarelessstructuredthanthis,and maycoveronlyoneortwoissues,butinmuchgreater detail.` (C03)
- p. 251: `Furtherquestionsfromtheinter- viewerwouldbebasedonwhattheintervieweesaid andwouldconsistmostlyofclarificationandprobing fordetails.` (C03)
- p. 251: `theclinicaltaskistofitthatprobleminto anappropriatemedicalcategoryinordertochoosean appropriateformofmanagement.` (C03)
- p. 251: `Inaqualitative researchinterviewtheaimistodiscovertheinter- viewee'sownframeworkofmeaningsandtheresearch taskistoavoidimposingtheresearcher'sstructures andassumptionsasfaraspossible.` (C03)
- p. 252: `Anintervieweewhoisalreadya patientorlikelyto becomeonemay wishtopleasethedoctorbygivingthe responsesheorshethinksthedoctorwants.` (C03)
- p. 252: `theyshouldnotbecorrectediftheysaythingsthat doctorsthinkarewrong` (C03)
- p. 252: `Onesolutionistosaythatsuch questionscanbeansweredattheendoftheinterview` (C03)
- p. 252: `criticallyappraisingtaperecordingsoftheir interviewsandaskingothersfortheircomments.` (C03)
- p. 253, Box 5: `Teaching(forexample,givingintervieweemedical advice)` (C03)
- p. 253: `Statisticalrepresentativeness isnotnormallysoughtinqualitativeresearch` (C02)

## Practice sets

None. The inventory marks none of C01-C03 quantitative, and each record sets `quantitative: false`.
C02 has a little arithmetic (7 of 12, 7 of 14, 9 of 15, 14 of 20), recomputed in Python; it is
there to show a share that means nothing, not a technique to drill.

## Figures

All three carry a `figure_note` instead of a figure; the tool draws only quantities.
Wanted, if the planner adds a diagram kind:

- **C03** (most useful): one horizontal line labelled "fixed in advance", from "everything" at the
  left to "almost nothing" at the right, with three marks: structured (questions, order, wording and
  answer options fixed), semi-structured (areas and a few open questions fixed; order, wording and
  follow-ups free), in-depth (one or two issues and an opening question fixed). No numbers.
- **C01**: two columns, "how many / how much" and "what / how / why", with arrows between them:
  asking finds what to count, counting says how common, a trial says whether a fix works. No numbers.
- **C02**: none wanted; any chart of respondent counts invites the misreading the section exists to
  prevent.

## Glossary rows

Checked against `prose/GLOSSARY.md`: none of these is glossed there. Existing senses used
unchanged: convenience sample, random sample, population, sample, premise, inference, conclusion.
"Instrument" is avoided for the interview (the glossary holds its legal sense), and "prevalence" is
avoided (C26 is not a dependency here).

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| conceptual generalisation | an idea, a reason and how it works, that a reader can test in another setting, as against a rate carried to a population | `S36-R1-C02` |
| evidence-based medicine | the practice of basing treatment decisions on the results of research | `S36-R1-C01` |
| evidence hierarchy | a ranking of study designs for one question: does this treatment work, and by how much | `S36-R1-C01` |
| in-depth interview | one or two issues in great detail; after an opening question, what is asked comes from what the respondent said | `S36-R1-C03` |
| mixed methods | studies that combine counting and asking by design (taught in S36-R3) | `S36-R1-C01` |
| NCD (non-communicable disease) | a long-lasting condition that does not pass from person to person, such as diabetes or high blood pressure | `S36-R1-C01` |
| open question | a question the person answers in their own words, not by picking from a list (taught fully in C05) | `S36-R1-C03` |
| power calculation | the sum a survey or trial does to decide how many people it needs | `S36-R1-C02` |
| qualitative research | research that gathers people's own words and actions and analyses them without turning them into counts | `S36-R1-C01` |
| quantitative research | research that counts and measures | `S36-R1-C01` |
| randomised controlled trial | a study in which chance decides who receives the treatment, and the groups are then compared | `S36-R1-C01` |
| research interview | a conversation in which a researcher asks a respondent about a topic to gather the respondent's own account of it | `S36-R1-C03` |
| respondent | a person who answers in a qualitative study | `S36-R1-C02` |
| semi-structured interview | a short guide of open questions fixes the areas; order, wording and follow-up questions are left to the interviewer | `S36-R1-C03` |
| statistically representative | a group whose make-up matches the whole population's in known proportions | `S36-R1-C02` |
| structured interview | a questionnaire read out: questions, order, wording and answer options all fixed | `S36-R1-C03` |

Coordination: "open question" is glossed briefly in C03 because C03 needs it; C05's drafter should
keep the same plain words or the conductor should pick one. "Respondent" is first defined in C02,
so C03 onward can use it bare.
