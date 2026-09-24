# S36-R1 step 5c: restore decisions, batch r1 (C01 to C07)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (sections 4 and 5),
and `<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml` for C01 to C07. Restore lists are
in `restore-lists/S36-R1-Cnn.txt`, each line commented with the gap it closes. Outputs are
`S36-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and checked by
`check/compress/validate.py`. Tools were not changed. Holes are written up for the fixer in
`HOLES-r1.md`.

Key: **restored** = original sentences put back because they let the reader do the thing.
**hole** = the original does not fill it either, or it is an error; goes to the audit.
**not a defect** = nothing to do. "Partial" means a restore closed part of the gap and the rest is
a hole.

## Word counts (as `validate.py` measures them)

| Section | Original | Cut (pass 1) | Final | Mean sentence orig → final | Validate |
|---|---|---|---|---|---|
| C01 | 1385 | 751 | 800 | 12.70 → 11.42 | OK |
| C02 | 866 | 435 | 603 | 14.68 → 13.11 | OK |
| C03 | 804 | 417 | 484 | 14.36 → 12.10 | OK |
| C04 | 1072 | 539 | 616 | 13.62 → 13.13 | OK |
| C05 | 929 | 490 | 570 | 12.06 → 11.63 | OK |
| C06 | 929 | 401 | 424 | 12.93 → 11.27 | OK |
| C07 | 1062 | 550 | 710 | 14.55 → 14.49 | OK |
| **Total** | 7047 | 3583 | 4207 | | 7 OK |

C07 first failed validation (mean 14.55 → 15.04): the restored consent sentences are long
quotations. Three restores were dropped, each because the pass-1 text already carries its point:
"The researcher must assure people that their decision ..." (pass-1 must-know: "saying no will not
change their treatment"), "Spoken consent without a signature ..." (written consent, witness and
thumb impression remain), and "Section 4.8.3 says a researcher cannot place ..." (pass-1 Definition:
"The committee, not the researcher, decides the kind of review"). It then passed at 14.49. No tool
conflict.

## Gap by gap

### C01
- **C01-1** restored: "You may have met a ladder of study designs, called the evidence hierarchy,
  with the randomised controlled trial near the top." Gives "That ladder" its referent.
- **C01-2** not a defect: "trial" is explained in the table ("chance decides who gets the message,
  then the groups are compared") before any exercise needs it, and the reader used it correctly.
- **C01-3** restored: "It is answered by qualitative research: research that gathers people's own
  words and actions ... without turning them into counts." The Definition now names and defines the
  second term.
- **C01-4** restored by the C01-1 sentence, which names the evidence hierarchy as that ladder.

### C02
- **C02-1** restored: "Book 0 taught you two ways to get a sample." "A random sample lets chance
  pick who is in it." "A convenience sample takes whoever is easy to reach."
- **C02-2** restored: "Because the people were chosen and not drawn, the findings describe the
  range of experiences ..." (antecedent of "They ... these").
- **C02-3** restored: "What the study can claim is different, and it is still worth having."
  (antecedent of "It can say").
- **C02-4** restored: "So a qualitative study is not judged by how many people it asked."
- **C02-5** restored: "When a trainee writes percentages into the results of an interview study,
  have them replace each one ..."
- **C02-6** restored: "The number of people interviewed is not the test, and there is no power
  calculation, the sum a survey or trial does to decide how many people it needs."
- **C02-7** restored, partial: "You choose some who live far away and some who live near, men and
  women, younger and older." Gives dimensions to choose along. How to decide which differences
  matter before the reasons are known is not in the original (deferred to the next book): hole H-3.
- **C02-8** hole H-1: the answer-first page is taught nowhere.
- Also restored (cross-cutting "dangling referents"): must-know 6 "It cannot tell you how common
  any reason is" had no antecedent; "A qualitative study tells you which reasons exist and how they
  work among the people you chose." restored.

### C03
- **C03-1** restored: "You open with one broad question about one or two issues."
- **C03-2** restored: "When a respondent mentions a symptom, you will feel pulled back into doctor
  mode." Gives "her" and "her health question" their case.
- **C03-3** restored: "A how-many question with known answer options takes a structured form ...",
  "A why or how question takes a semi-structured guide.", "One story told in full ... can take an
  in-depth interview."
- **C03-4** hole H-4 (terms before home: I/R labels). The original is the same, and the exercise
  table is not the pass's to change.
- **C03-5** hole H-5: the original C03 also has no positive interviewing skills.

### C04
- **C04-1** hole H-6: the two groups' talk is not in the original either.
- **C04-2** restored: "A group interview can be run simply as a quick way to hear several people
  at once, each answering the researcher in turn." and "A focus group is different in method:
  participants are asked to talk to one another." The figure's "group interview" now has its
  meaning.
- **C04-3** hole H-4 ("transcript", "turn" before C10/C11; original the same).
- **C04-4** hole H-2 (Kitzinger 1995 has no full reference in the original either).
- **C04-5** restored, partial: "Kitzinger calls this person the facilitator, and says the
  facilitator should explain that the aim is for people to talk to each other rather than to the
  researcher." and, for why "Everyone hears everything" is a weakness, "You cannot promise a person
  that what they say stays private." Running a group beyond that one move is not in the original:
  hole H-7.

### C05
- **C05-1** not a defect: the same sentence defines "premise", and a record code is the spec's
  allowed form of pointer (§1 test 3). How codes render is a renderer matter.
- **C05-2** restored: "It also asks the person to give reasons for what they did, as if they owed
  you an explanation." and "It carries the premise that they decided to stop."
- **C05-3** restored: "There it means asking someone to explain their reasoning, as in "Tell me how
  you came to that decision"." "Probe" still used before C08: hole H-4.
- **C05-4** restored, partial: '"Don't you find the diet hard?" is closed and leading.' and '"How
  hard is the diet for you?" is open in form and leading, because it takes for granted that the diet
  is hard.' This rules on "how hard" (open) for P2d and P8. "How much" / "how often" questions
  answerable by a degree word or a number (P10) still have no ruling: hole H-8.
- **C05-5** hole H-6 (draft and rewrite not in the original).
- **C05-6** hole H-4 ("topic guide" before C06).

### C06
- **C06-1** hole H-9 ("pilot" before C14; "fall flat" has no test in the original).
- **C06-2** restored, partial: "You use a prompt only if the respondent does not get there on their
  own." Settles when a prompt is spoken. Prompt versus leading probe, and an example prompt, are
  not in the original: hole H-10.
- **C06-3** restored, partial: "Tell me about a usual day for you." (the original's one example
  warm-up). No full worked guide exists in the original: hole H-11.
- **C06-4** hole H-12: the original does not say which three main questions carry the question.
- **C06-5** not a defect: the instruction can be followed without its reason, which C09 gives.
- **C06-6** hole H-13: demographic questions and their place are not covered in the original.
- **C06-7** hole H-14: deriving main questions from a study question is never shown.

### C07
- **C07-1** restored, partial: "The information given must include the person's "Freedom of the
  individual to participate and/or withdraw ..." (Box 5.1)." and "It must include how far
  confidentiality can be kept, and its limits (section 2.3.2)." Purpose, duration, recording, use of
  the words and contact are not listed in the original: hole H-15.
- **C07-2** restored: "The researcher "must obtain voluntary written informed consent from the
  prospective participant" (section 5.0).", "A person who cannot read gives consent in front of an
  impartial literate witness (section 5.4.3).", "A person who cannot sign gives a thumb impression
  (section 5.4.4)."
- **C07-3** restored, partial: "The guidelines warn that risks in social and behavioural research
  can be "misconstrued as no/minimum risk research" (Box 9.1)." Ex 2's "minimal risk" can now be
  refuted. The term itself stays undefined: hole H-16.
- **C07-4** hole H-17: what to send, to which committee, is not in the original.
- **C07-5** restored, partial: "The guidelines require you to say that it "may not be possible" to
  protect privacy in every circumstance (section 2.3.2)." What the concrete limits are is not
  stated: hole H-18 (tied to the C08/C09 contradiction).
- **C07-6** hole H-19: storage is named, not taught, in the original too.
- **C07-7** restored, partial: "An interview recording carries a voice, a name, a village, a
  family story." and "Raw data, audio-visual material included, is shared only after processing "to
  mask identifiers" (section 9.2.12)." Playing voices in a presentation can now be reasoned about;
  consent for secondary use is not in the original: hole H-20.
- Also restored (cross-cutting "dangling referents"): must-know 3 "Then take written notes
  instead" had nothing before it; "Someone may agree to talk and refuse to be recorded." restored.

### Cross-cutting (the parts touching C01 to C07)
- **Sources never referenced** (Kitzinger, DeJonckheere and Vaughn, Britten): hole H-2.
- **Dangling referents** (C02, C03): restored above, plus the two extra danglers in C02 and C07.
- **Figures of material not shown** (C04, C05): hole H-6.
- **Terms before their home section** (transcript, turn, probe, topic guide, pilot): holes H-4, H-9.
- **No worked topic guide or consent script**: holes H-11, H-15.
- **Respondent labels reused for different people** (C03, C04, C05): hole H-21.

## Counts (C01 to C07, 42 gaps)

Restored 25 (of which 9 partial, residue logged as holes), hole 14, not a defect 3.
Cross-cutting: 1 restored (dangling referents), 5 holes.
