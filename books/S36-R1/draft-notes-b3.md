# Draft notes · S36-R1 batch b3 (C07, C08, C09)

## Records written

- `check/records/S36/S36-R1-C07.yml`: Consent, recording and privacy before you switch on the recorder. Institutional. 28 references (27 ICMR 2017 as `guideline`, 1 DeJonckheere & Vaughn as an off-type `primary`), all quoted, `review.as_of` 2026-09-24, trigger: the next ICMR revision of the guidelines.
- `check/records/S36/S36-R1-C08.yml`: Running the interview without leading it. Derivable. Its textbook anchor is Blackstone 2012 (9.2, 9.4). It also rests on DeJonckheere & Vaughn 2019 (`primary`), with off-type Britten 1995 (OCR) and ICMR 9.2.8 for the boundary point.
- `check/records/S36/S36-R1-C09.yml`: The interviewer is part of the data. Empirical. It rests on Britten 1995 (OCR), DeJonckheere & Vaughn 2019 and Mays & Pope 2000, with off-type ICMR Box 9.4 and Box 9.2.

`python check/build.py --check` gives 0 blocking. A filtered run of `build.check()` shows no blocking failures and no warnings for these three records. Every quote was checked by script against the `[TEXT]` runs only, never against headers or `[NOTE]` lines: 69 of 69 are present.

## Decisions for the conductor or Harsh

1. **C08's textbook anchor (corrected after the coordinator's message).** DeJonckheere & Vaughn are back to `kind: primary`. C08 now carries four `blackstone_2012` (`textbook`) references: 9.2, that what the participant says shapes the interview after the opening question, and the skill of listening and following up; 9.4, the probe as "a request for more information", and not judging. Blackstone carries the core (following the respondent, probing, not judging). The specific probe kinds, field notes and deferring questions rest on DeJonckheere & Vaughn and Britten. C09 also cites Blackstone 9.4 on the power differential and on letting the respondent choose the place. C07 stays on ICMR. In C07 the stand-in for a name is now a "label" (R1), not a "code", to match C12.
2. **C07 and review of a learner's pilot.** The record does not assert either way. It teaches Table 2.1 (routine questioning is minimal risk), Table 4.2 (exemption only with "no linked identifiers"), 4.8.3 (the researcher cannot decide the category) and 9.2.12 (preliminary observation notes need not go to the committee, but ethical issues in that phase should). It then routes the reader to their institution's committee. 3.5.1 (course research) is about authorship, so it is not used. The Digital Personal Data Protection Act is not named. The boundary point says only that ICMR 2017 is "not the whole of the law on recordings or personal information".
3. **C07 simplified_explanation** defines an ethics committee in plain words ("a group of people at a hospital, college or research body"). That definition is general description and no held passage states it. The held sections describe what the committee does, not what it is.
4. **C09 left out on purpose.** The term "social desirability" and any list of cues ("we" instead of "I", answers that are all positive) are left out, because only Bergen & Labonté 2020 carries them and it is not held. C09 describes the pull only in Britten's words ("wish to please the doctor"). If Harsh obtains Bergen & Labonté, both could be added.
5. **C09 has no effect size.** The record says so plainly, and states what would overturn the claim.
6. **"Probe" is used in C05 before C08 defines it.** C05 speaks of "a probe called leading". C08 is where the inventory puts probes, and it defines the term. C05's drafter or the audit should either point forward in plain words or define it there. I removed my own point on Table 6's "Leading" label, because C05 already teaches it.
7. **Terms kept consistent with siblings.** I use "topic guide" (C06), whose closing question C08's illustration uses. "Field notes" means notes written straight after the interview, as in C14 step 3. I avoided "memo", because C12 defines it. C08 defines the "probe" as a follow-up while interviewing. That is distinct from C06's "prompts", the notes written under each main question.

## Unsourced or soft

- C07: the example script sentences ("I am not your doctor", codes such as R1 on file names, keeping the code-to-name list apart) are practice built on 2.3, 2.3.2, 5.3.10 and 9.2.12. They are not quoted rules, and the record frames them as "how you honour" the duty.
- C09 illustration 1's "a respondent may tell a stranger a harsher story" (in analogy_breaks_when) is reasoning, not sourced.

## Practice sets

None. The inventory marks none of C07, C08 and C09 as quantitative. They are taught through exercises instead: C07 has design, critique and teaching; C08 has critique, design and teaching (skill_ref S36-R1-K01); C09 has interpretation, design (K01) and teaching.

## Figures

Each record has a `figure_note` instead of a figure:
- C07: a sequence of spoken steps, with no quantity. The only diagram available would be ICMR's Table 4.2 redrawn.
- C08: conduct inside a conversation. Any count of turns or probes would be invented.
- C09: a figure would need a size for the interviewer effect, and no held source gives one.

No figure is wanted from the planner for these three.

## OCR quotes (Britten 1995, `britten_1995`: check each against the page image)

| Record | Page | Quote as in the OCR layer |
| --- | --- | --- |
| C08 | 251 | Semistructuredinterviewsareconductedonthe basisofaloosestructureconsistingofopenended questionsthatdefinetheareatobeexplored,at leastinitially,andfromwhichtheintervieweror intervieweemaydivergeinordertopursueanideain moredetail. |
| C08 | 252 | Itisvital thatinterviewerscheckthattheyhaveunderstood respondents'meaningsinsteadofrelyingon theirown assumptions. |
| C08 | 252 | theyshouldnotbecorrectediftheysaythingsthat doctorsthinkarewrong |
| C08 | 252 | Onesolutionistosaythatsuch questionscanbeansweredattheendoftheinterview, althoughthisisnotalwaysasatisfactoryresponse. |
| C08 | 252 | Thenoviceresearchinterviewerneedstonoticehow directiveheorsheisbeing,whetherleadingquestions are beingasked,whethercues are pickedup or ignored,andwhetherintervieweesaregivenenough timetoexplainwhattheymean. |
| C08 | 252 | pointisnotthatnon-directivenessisalwaysbest,but thattheamountofdirectivenessshouldbeappropriate. |
| C08 | 253 (Box 5) | Teaching(forexample,givingintervieweemedical advice) |
| C08 | 253 (Box 5) | Counselling(forexample,summarisingresponses tooearly) |
| C09 | 252 | Allqualitativeresearchersneedtoconsiderhowthey areperceivedbyintervieweesandtheeffectsofcharac- teristicssuchasclass,race,sex,andsocialdistanceon theinterview. |
| C09 | 252 | Thisquestionbecomesmore acuteifthe intervieweeknowsthat'theinterviewerisalsoadoctor. (the OCR has a stray apostrophe) |
| C09 | 252 | Anintervieweewhoisalreadya patientorlikelyto becomeonemay wishtopleasethedoctorbygivingthe responsesheorshethinksthedoctorwants. |
| C09 | 252 | Itisbest not to interviewone'sown patientsforresearch purposes,butifthiscannotbeavoided,patientsshould begivenpermissiontosaywhattheyreallythink |
| C09 | 253 | Thesettingofaninterviewaffectsthe content,anditisusuallypreferabletointerviewpeople athome. |
| C09 | 253 (Box 5) | Presentingone'sownperspective,thuspotentially biasingtheinterview |

I took the page numbers from the page footers in the OCR run. Box 5 comes after the "252" footer, so it is on page 253. The single spaces inside the quotes are the layer's own line breaks and gaps. Only short phrases were taken from the Box 5 items for audit, and no box is reproduced.

## Glossary rows (proposed; none of these terms is in `prose/GLOSSARY.md`)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| confidentiality | the researcher's duty to keep safe what a person told them (ICMR 2017, 2.3) | `S36-R1-C07` |
| ethics committee | a group at a hospital, college or research body that reads a research plan before it starts and decides its kind of review; ICMR shortens it to EC | `S36-R1-C07` |
| field notes | notes written the same day, straight after an interview: how it went, where, who could hear, what the interviewer noticed and did | `S36-R1-C08` |
| informed consent | agreement to take part given after being told about the study, understanding it, and being free to say no (ICMR 2017, 2.2) | `S36-R1-C07` |
| privacy | a person's right to decide what is collected about them and who sees it (ICMR 2017, 2.3) | `S36-R1-C07` |
| probe | a short follow-up that asks for more of what the respondent just said without suggesting what that should be (a pause, an echo, "tell me more") | `S36-R1-C08` |
| reflexivity | showing how the researcher and the research process may have shaped the data (Mays and Pope 2000) | `S36-R1-C09` |
