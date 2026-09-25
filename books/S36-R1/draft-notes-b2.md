# Draft notes · S36-R1 · batch b2 (C04, C05, C06)

## Records written

- `check/records/S36/S36-R1-C04.yml`: The focus group, and choosing between it and the interview (empirical, Kitzinger 1995 only)
- `check/records/S36/S36-R1-C05.yml`: Open, closed and leading questions (derivable, quantitative, 10 practice problems)
- `check/records/S36/S36-R1-C06.yml`: The topic guide (derivable)

`python check/build.py --check`: blocking 0 for the whole build at hand-back. None of the warnings are in these three records. Quotes were checked by script against `sources/` (normalised as the build does). Every tally in the prompts, answers and figures was recounted in Python from the record's own tables (scratch-b2/recount.py).

## For the conductor to decide

1. **Reference kind (corrected on the coordinator's instruction).** Every journal article is now `kind: primary`. Blackstone 2012 (*Principles of Sociological Inquiry*, Saylor) is the `textbook` anchor.
   - **C05:** four references, all from section 9.2: open-ended questions defined; open against closed-ended; leading questions; "why" as a follow-up.
   - **C06:** three references, all from section 9.2: the interview guide defined as "not set in stone"; sensitive questions not at the start; an over-detailed guide.
   - **C04:** three references, all from section 12.1: interaction as the aim; one or two participants dominating; no promise of confidentiality.
   - Blackstone carries the core claim of each concept. No prose changed.
2. **Group size.** The inventory said about six to ten. Kitzinger says between four and eight. Blackstone 12.1 differs from both: it prefers 3–5 for heated topics, and reports 6–10 from Morgan and 3–12 from Adler & Clark. C04's prose attributes four to eight to Kitzinger by name, so it is not wrong, and I left it unchanged. You could add one sentence saying the recommendations differ. The note on C04's Blackstone reference records the conflict. Focus groups are in Blackstone section 12.1, not 9.4.
3. **Overlap with C08.** C05 teaches the clash between the two meanings of "leading": a leading question, and the "Leading" row of DeJonckheere & Vaughn's Table 6, which is a probe. C08 teaches the same clash again. Since C05 comes first, C08 could point back to it or drop the point.

## Unsourced or reasoned, not quoted

- **C05, "why" heard as blame.** Now sourced. Blackstone 9.2 says "why" as a follow-up "can come off as confrontational, even if that is not how you intend it".
- **C05, double questions.** No held source names them. The point is derivable: an answer cannot be assigned to one of the two questions.
- **C06, the closing question** ("Is there anything I have not asked about that I should have?"). No held source gives it. It is presented as a design choice. The follow-up "anything you want to ask me" rests on Britten's line that the respondent's questions can be answered at the end.
- **C06, the time plan** (5+5+10+10+10+5+5 = 50 minutes). This is a made-up plan, and the prose says "your own choice, not a rule". No source gives durations.
- **C06, keeping dated versions of the guide.** Derived from DeJonckheere & Vaughn's point that the guide changes during a study. This is not a quote.
- All transcripts, guides and draft questions are made up. Each is labelled as made up the first time in each illustration. No line is attributed to a real study.

## Practice set (C05): 10 problems, why

The technique has three checks (form, premise, count) and a rewrite. The rewrite interacts with the premise check, which is where readers go wrong. So the set is built like this:

- one mechanical problem per check (L1–L3);
- three applied problems on clinic lines, including a transcript turn and a count over a whole draft (L4–L6);
- one diagnostic on the form check ("Tell me, do you...") and one on a rewrite that keeps its premise (L7–L8);
- two transfer problems, from a protocol line and from a "they all start with how" claim (L9–L10).

Fewer than ten would drop either a diagnostic or the counting problem.

## Figures

- `s36-r1-c04-who-answers-whom.png`: a bar chart of respondent turns in the two made-up groups (6/0 against 2/6), drawn from the record's table.
- `s36-r1-c05-draft-labels.png`: a bar chart of the eight-question draft before and after rewriting (open 3→7, closed 5→1, leading 5→0, double 2→0). It checks that open plus closed is 8 in both drafts.
- `s36-r1-c06-time-plan.png`: a bar chart of the planned minutes per part of the guide, which checks that they add up to 50. This is the weakest of the three. It is close to a table drawn as a picture. If the figure planner disagrees, replace it with `figure_note: "A topic guide is a list of questions; a picture of it would repeat the table."`

All three were drawn with `draw.py` with no problems and looked at as images.

## OCR quotes (check each against the page image)

Kitzinger 1995 (`kitzinger_1995`), C04:

| Page | Quote as in the OCR layer |
| --- | --- |
| 299 | Focusgroupsareaformofgroupinterviewthat capitalisesoncommunicationbetweenresearchparti- cipantsinordertogeneratedata. |
| 299 | insteadoftheresearcheraskingeachpersontorespond toaquestioninturn,peopleareencouragedtotalkto oneanother:askingquestions,exchanginganecdotes andcommentingoneachothers'experiencesand pointsofview. |
| 299 | Groupworkalsohelpsresearcherstapintothemany differentformsofcommunicationthatpeopleusein daytodayinteraction,includingjokes,anecdotes, teasing,andarguing. |
| 299 | toexploretheissuesofimportance tothem,intheirownvocabulary,generatingtheirown questionsandpursuingtheirownpriorities. |
| 299 | theydonotdiscriminateagainstpeople whocannotreadorwrite |
| 300 | Thedownsideofsuchgroupdynamicsisthatthe articulationofgroupnorms may silenceindividual voicesofdissent.Thepresenceofotherresearch participantsalsocompromisestheconfidentialityof theresearchsession. |
| 300 | Groupworkcan activelyfacilitatethediscussionoftabootopicsbecause thelessinhibitedmembersofthegroupbreaktheice forshyerparticipants. |
| 300 | groupdynamicscanallowforashiftfrom personal,selfblamingpsychologicalexplanations |
| 300 | itisimportanttobeaware ofhow hierarchywithinthegroup may affectthedata |
| 301 | Thefacilitatorshouldexplainthatthe aimoffocusgroupsistoencouragepeopletotalkto eachotherratherthantoaddressthemselvestothe researcher. |
| 301 | Theidealgroupsizeis betweenfourandeightpeople.Sessionsmaylastoneto twohours (also used, shortened, for the numbers 4 and 8, marked `derived` because the unspaced OCR hides the words from the number check) |
| 301 | A commonexerciseconsistsofpresenting thegroupwithaseriesofstatementsonlargecards. |
| 301 | Ideallythegroupdiscussionsshouldbe tape recordedandtranscribed. |
| 301 | Ingeneral,itisnotappropriatetogive percentagesinreportsoffocusgroupdata,anditis importanttotrytodistinguishbetweenindividual opinionsexpressedinspiteofthegroupfromtheactual groupconsensus. |
| 302 | Interviews maybemoreappropriatefortappingintoindividual biographies,27butfocusgroupsaremoresuitablefor examininghowknowledge,andmoreimportantly, ideas,developandoperatewithinagivencultural context. |
| 302 | Questionnairesaremoreappropriatefor obtainingquantitativeinformationandexplaininghow manypeopleholdacertain(pre-defined)opinion; focusgroupsarebetterforexploringexactlyhowthose opinionsareconstructed. |
| 302 | Groupdataareneithermorenorlessauthenticthan datacollectedbyothermethods |

Page numbers for the 300/301 split were inferred from where the OCR layer prints the page footers "BMJ VOLUME 311 29JuLY1995" and "301". A person checking against the image should confirm them.

Britten 1995 (`britten_1995`), C05 and C06:

| Page | Quote as in the OCR layer | Record |
| --- | --- | --- |
| 251 | interviewersaretrained toaskquestions(mostlyfixedchoice)inastandardised manner.Forexample,intervieweesmightbeasked: "Isyourhealth:excellent,good,fair,orpoor?" | C05 |
| 251 | suchas:"Whatdoyouthinkgoodhealthis?","How doyouconsideryourownhealth?" | C05 |
| 252 | Pattonsaidthatgoodquestionsinqualitativeinter- viewsshouldbeopen ended,neutral,sensitive,and clearto theinterviewee. | C05 |
| 252 | Thenoviceresearchinterviewerneedstonoticehow directiveheorsheisbeing,whetherleadingquestions are beingasked | C05 |
| 252 | Itisusuallybesttostartwithquestionsthatthe intervieweecan answer easilyandthenproceedto more difficultor sensitivetopics. | C06 |
| 252 | highlystructuredquestionnaires,theorderinwhich questionsareaskedwillvary | C06 |
| 252 | Wordingscannotbestandardisedbecausetheinter- viewerwilltryto use theperson'sown vocabulary whenframingsupplementaryquestions. | C06 |
| 252 | Onesolutionistosaythatsuch questionscanbeansweredattheendoftheinterview | C06 |

## Glossary rows (proposed; none of these terms is in `prose/GLOSSARY.md`)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| closed question | a question whose possible answers are fixed before the respondent speaks: yes or no, a number, or one of the options given | `S36-R1-C05` |
| double question | a question that asks two things in one sentence, so an answer cannot be assigned to either | `S36-R1-C05` |
| focus group | a group of people who talk with each other about a topic under a moderator, where the talk between them is the data | `S36-R1-C04` |
| group interview | several people interviewed together, each answering the researcher in turn | `S36-R1-C04` |
| leading question | a question that shows the answer the asker expects, or takes for granted part of what it asks about; it can be open or closed | `S36-R1-C05` |
| main question | one of the questions a topic guide turns on, usually asked of every respondent (DeJonckheere and Vaughn's "core question") | `S36-R1-C06` |
| moderator | the person who runs a focus group and keeps the talk going without taking it over (Kitzinger's "facilitator") | `S36-R1-C04` |
| open question | a question the respondent answers in their own words (C03 uses it first in plain words; C05 gives the definition) | `S36-R1-C03`, `S36-R1-C05` |
| prompt (in a topic guide) | a short note under a main question of what you hope the answer covers, used only if the respondent does not get there on their own | `S36-R1-C06` |
| topic guide | the written list of areas and questions an interviewer takes into a semi-structured interview; a guide, not a script | `S36-R1-C06` |
| warm-up question | an easy first question on something the respondent knows well, to start them talking (DeJonckheere and Vaughn's "grand tour" question) | `S36-R1-C06` |

The glossary already has "premise" as "a reason offered" (`B0-R0-C42`). C05 uses it in that sense: "a statement that an argument rests on".
