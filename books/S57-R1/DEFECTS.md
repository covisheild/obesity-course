# S57-R1 defects

## Found by the compression pass

Holes the cold read found that the full-length original did not fill (or errors it exposed). Each goes through the audit and fix loop.

# S57-R1 compression-pass holes, batch A (C01 to C08)

For the fixer. These are holes the restore could not close, from reader A's cold read
(`COLD-READ-GAPS.md`) and `RESTORE-DECISIONS-A.md`. Either the original does not fill them either,
or they are errors or contradictions, or (marked **ceiling**) the original's closing sentence could
not come back without raising the mean sentence length. "Field" is the field in
`S57-R1-Cnn-final-prose.yml`, or the exercises, which the compression pass does not touch. Nothing
here was fixed; each needs new text or a correction, and goes back through the audit.

## Across sections

**H-2 · C01, C03, C05, C07, C08 · exercises (gaps A-C01-11, A-C03-8, A-C05-6, A-C07-8, A-C08-9).**
C01 has no exercises and no problems. C03, C05, C07 and C08 have one or two open exercises and no
numbered practice set. Wrong: nothing checks that the reader can do the quantitative steps (C01's
percentage-point reversal, C03's effect-size counts). Would close it: a practice set for each, per
`claude.md` §7a.

## C01

**H-1 · simplified_explanation (A-C01-10).** "You find out about learning by testing again, after a
gap, on something the learners have not just seen." Wrong: can be read as "different material",
which contradicts Must-know 3's "same objective". Would close it: "... with new questions on the same
objective".

**H-3 · simplified_explanation (A-C01-12).** "A session can go well and teach almost nothing that
lasts." Wrong: the only data shown has the worst group recalling 40% a week later. Would close it:
soften the claim ("teach much less than it seemed") or tie it to evidence that shows it.

## C02

**H-4 · simplified_explanation (A-C02-4).** "But marks go up after almost any teaching." Missing: why
(practice on the test, time, other teaching). The kept restore gives the trap but not the reason.
Would close it: one sentence on why marks rise, with a source.

**H-5 · definition.text (A-C02-5). Contradiction.** "Its sign says which group did better, so you
always state which group was subtracted from which." Wrong: false when a lower score is better, which
problem 10 (mistakes counted) tests. Would close it: "its sign says which group scored higher; whether
higher is better depends on the scale".

**H-6 · must_know[4].point (A-C02-7).** "Freeman and colleagues pooled 158 comparisons of active
learning against lecturing ..." Missing: what "active learning" is, and what "pooled" means. Would
close it: a one-line definition of each.

**H-7 · exercises, Exercise 1 (A-C02-8).** "Name the one number you will report first." Missing: the
text never says whether the MD or the SMD comes first. Would close it: state the rule in the
Definition or Must-know.

**H-8 · exercises, problem 6 (A-C02-9).** "... Say what the two SMDs tell you about the random
allocation." Missing: any guide to how large a baseline SMD is worrying; a description of
Deslauriers's groups A and B. "72.02%" has two decimals where every other figure has one. Would close
it: a threshold or a worked judgement; describe the groups; check the figure.

**H-9 · C02, several fields.**
- must_know[3].point (A-C02-10): "To turn it into marks, multiply it by the SD of the scores on your
  own test." Unflagged assumption that a pooled SMD carries over to your test and learners; Freeman's
  "6%" is ambiguous between points and per cent. Close: flag the assumption; say which.
- definition.text, last paragraph (A-C02-11): never says why a pre-to-post SMD cannot sit beside a
  between-group SMD (different SD, no comparison). Problem 12 depends on it. Close: one sentence.
- must_know[6].point (A-C02-12): "With a small batch, chance can still leave one group stronger."
  "Small" unquantified; D6's standard error never linked to the MD. Close: link to D6 with a worked
  size.
- exercises (A-C02-13): "ASHA workers are accredited social health activists: village health
  workers." appears twice; "growth chart" unexplained. Close: remove the repeat, gloss the term.
- whole section (A-C02-14): no Illustration and no "Where this picture breaks"; the only worked SMD
  is a figure caption, yet problems 8 and 9 test errors in that procedure. Close: an Illustration
  working one SMD.

## C03

**H-10 · definition.text / must_know[4].point (A-C03-2). Ceiling.** "None of the 50 classroom
experiments in that review was run in India." against the figure's "49 effect sizes" and Must-know
3's "46 of 49". The original's "Of the 49 effect sizes they could compute, each a Cohen's d, 28 were
above 0.50. 46 favoured ..." (25 words) reconciles them but raised the mean. Would close it: a shorter
sentence saying 49 of the 50 experiments gave a computable effect size.

**H-11 · definition.text (A-C03-4).** "Practice testing with feedback beats restudy ..." Missing: that
practice testing is Dunlosky's name for retrieval practice (C05 now says so; C03 does not). Would
close it: say so at first use in C03.

**H-12 · must_know[5].point (A-C03-6).** "When most of the room cannot answer, give the answer and
reteach ..." Missing: any threshold or evidence for "most". Would close it: a sourced rule of thumb,
or drop "most".

**H-13 · exercises, Exercise 1 (A-C03-7).** "Then write down when they will recall it a second time
..." Wrong order: the spacing rule is taught in C04. Would close it: a forward pointer to C04, or move
the part to C04.

**H-14 · figure caption and definition.text (A-C03-9, A-C05-4).** "3 favoured the comparison" never
says what the comparison was (restudy, or nothing). C05's "No experiment has tested rereading's effect
on learning in a real course ..." then sits in tension with it. Would close it: name the comparison
conditions in Agarwal's review and reconcile the two statements.

## C04

**H-15 · definition.text (A-C04-1). Error.** "The retention interval, from `S57-R1-C03`, is the time
from the last study session to the test." Wrong: it is defined in C01. Would close it: `S57-R1-C01`.

**H-16 · must_know[3].point (A-C04-2). Contradiction.** "The best gap grows as the test moves away,
but its share falls: 23 days, 7%, for a test 350 days away." Wrong: everywhere else, including problem
1's source and the figure, it is 21 days (6%). Would close it: check Cepeda 2008; correct to 21 days,
6%, or explain 23 as a fitted value and say so.

**H-17 · definition.text (A-C04-3). Contradiction.** "So the best gap grew with the retention
interval, but its share of the retention interval fell." Wrong: the section's own numbers rise from
14% (1/7) to 31% (11/35) before falling, and the gap does not grow from 70 to 350 days. Would close
it: state it for 35 days onward, or describe the rise then fall.

**H-18 · definition.text (A-C04-4, A-C04-5).** "It was about 20% to 30% for a test a few weeks away.
For a test a year away it was about 5% to 7%." and "At the best gap, final recall was 64% higher than
with no gap." Missing: where the 20% lower bound and the 5 to 7% range come from (the data give 31%,
30% and 6%); what to do for a test one week away (14%); at which interval the 64% applies and that it
is a relative increase. Would close it: source the ranges or give the per-interval values; say which
interval and "relative".

**H-19 · simplified_explanation and must_know[2].point (A-C04-6). Largest demonstration gap.** "Then
make the gap before the review about 20% to 30% as long as the wait from the review to the test."
Missing: when only the total span T is known, the gap solves g = k(T − g), giving g = kT ÷ (1 + k);
this is never worked, and the tempting "20 to 30% of the whole span" is never warned against. Problem
5 depends on it. Would close it: an Illustration or working block solving one case (T = 60 days gives
day 10 to 14).

**H-20 · exercises, Exercise 2 (A-C04-8).** "Explain the mechanism and the evidence ..." Missing: no
mechanism for spacing is taught anywhere. Would close it: a sourced sentence on the proposed mechanism,
or drop "mechanism" from the exercise.

**H-21 · must_know[5].point (A-C04-10).** "Test often and lightly ..." Missing: the section works with
one review; nothing says how to place a second or third. Would close it: a sourced rule for expanding
or repeated reviews, or state that the evidence covers one review.

## C05

**H-22 · definition.text (A-C05-1).** "... rereading has consistently done worse than practice testing
and than two techniques of explaining." Missing: the two techniques are named only in C07, unmarked.
Would close it: name them with a pointer to `S57-R1-C07`.

**H-23 · definition.text and exercises (A-C05-7).** "Highlighting, in most situations studied and
with most learners, did little to boost performance." Missing: study counts, effect sizes or
populations, which Exercise 1 ("say how sure the evidence lets you be") needs. Would close it: give
Dunlosky's evidence base for highlighting.

## C06

**H-24 · definition.text (A-C06-1).** "So a crossover the wrong way round ... supports learning styles
in the broad sense and contradicts meshing." Missing: "broad sense" is undefined, and the Definition's
"teaching fitted to a learner's style" does not obviously cover a wrong-way crossover. Problem 6
depends on it. Would close it: define the broad sense (the best method differs by style group,
whichever way).

**H-25 · definition.text (compression side effect).** "Studies with the right design found no
support, one of them with 123 internal medicine residents. They conclude that applying learning styles
in classrooms is unwarranted." Wrong: "They" now reads as the studies, not Pashler and colleagues,
because "Searching a literature ..." (24 words) could not come back under the mean ceiling. Would
close it: "Pashler and colleagues conclude ..."

**H-26 · definition.text / exercises, problem 10 (A-C06-5). Ceiling.** Problem 10: "Newton and Miah
found 58% of 114 UK academics agreed ..." Missing: agreed with what (preference or matching), and
whether the 137 schoolteachers answered the same statement. The original's Definition sentences ("...
58% agreed that individuals learn better when taught in their preferred learning style" and "They
cite a 2012 study in which 93% of 137 UK schoolteachers agreed with the same statement") answer it but
raised the mean. Would close it: a shorter sentence naming the statement.

**H-27 · must_know[7].point (A-C06-4).** "A crossover in one small table can also arise by chance: the
MD check reads the pattern, not whether it is real." Missing: how to tell, or how many learners a
study needs. Exercise 1 asks for "the study that could settle it". Would close it: link to D6's
standard error, or say plainly that sizing is outside this book.

## C07

**H-28 · C07, several fields.**
- must_know[2].point (A-C07-4): "A fluent explanation that is wrong can hurt learning." Missing: how
  it hurts, and the evidence. Close: a sourced sentence.
- figure caption (A-C07-5): "76% of 105 true-or-false questions right ... 69%." Missing: the study
  is unnamed; chance on true-or-false is 50%, which changes how the 7-point gap reads. Close: name the
  study; state chance.
- exercises, Exercise 1 (A-C07-7): "the chapter on anthropometry" is undefined anywhere. Close: gloss
  it ("body measurement").

## C08

**H-29 · simplified_explanation and must_know[1-2] (A-C08-2, A-C01-6).** "For a beginner, a problem
shown worked out ... often teaches more than being made to solve it cold." and "Once the basics are
held, effort helps." Missing: any criterion for when a learner stops being a novice; the section is in
unreconciled tension with C01 ("ask learners to work problems ... effort is part of how it works") and
C03 (retrieval for everyone). Would close it: a criterion, and a sentence reconciling worked examples
with retrieval and active work.

**H-30 · must_know[0].point and definition.text (A-C08-3).** "Put the steps where they stay: on the
board, a chart on the wall, a handout." against "A diagram alone has taught more than the same diagram
with text that repeats it." Missing: whether written steps beside a diagram are the harmful
redundancy. Exercise 1 depends on it. Would close it: say what form the lasting steps take (steps that
add to the diagram, not repeat it).

**H-31 · C08, several fields.**
- figure caption (A-C08-4): "they gained 24% on the facts they knew well and 12% on the facts they
  knew less." Missing: points or relative; the study is unnamed; no body sentence links a "why"
  question figure (C07's subject) to C08's claim. Close: name the study, say which, add the link or
  move the figure to C07.
- definition.text (A-C08-6): "These effects shrink, then vanish, and can reverse as learners gain
  expertise." Asserted with no data. Close: a sourced example.
- definition.text / simplified_explanation (A-C08-7): no number for "a limited number of new
  elements"; "elements" becomes "pieces" without comment; "transfer to new problems" undefined. Close:
  say no number is given (the original's cut Must-know sentence says so), align the terms, gloss
  "transfer".

# S57-R1 holes found by the compression pass, batch B (C09 to C16)

These are holes the restorer could not close, because the original did not fill them either, or
because the problem is an error or contradiction rather than missing text. They go to the fixer
and back through the audit. Gap ids refer to `COLD-READ-GAPS.md` (reader B). The quoted sentences
are as they stand in `S57-R1-Cnn-final-prose.yml`, or in the record's exercises and figures, which
the pass does not touch. "Residue" marks what is left of a gap that was partly restored.

## C09

**H1 · C09 definition.text / simplified_explanation (B-C09-1, B-C09-8).**
- As it stands: "It has six parts." … "5. The standard: how much, or how well, counts as done."
  … "Here is the test of a finished objective."
- Wrong or missing: the section never shows one finished objective with all six parts labelled,
  and never gives an example of a standard (a percentage, a checklist, a tolerance). Ex 1 and
  Ex 2 have no model to check against.
- To close it: add a short illustration with one complete objective, each part labelled. Include
  a standard of a checkable form. The objective should keep to one action (see H4).

**H2 · C09 definition.text (residue of B-C09-3).**
- As it stands: "remember, understand, apply, analyse, evaluate and create."
- Wrong or missing: only *understand* is glossed. The reader cannot tell an apply task from an
  analyse, evaluate or create task, and so cannot "write the objective at that level".
- To close it: add one line per level saying what the learner does, from the revised taxonomy's
  source.

**H3 · C09 definition.text, item 6 (B-C09-7).**
- As it stands: "6. By when: the point at which it will be checked."
- Wrong or missing: this is ambiguous between the end of the session and the delayed test. C10's
  model objective says "At the end of this session", while C13 says the gate test is "a week or
  more after the session".
- To close it: say which point the by-when names in this book's build, and square C10 and C13
  with it.

## C10

**H4 · C10 exercise 1, model objective (B-C10-1). Contradiction.**
- As it stands: "… will weigh the child and record the weight in the register, completing every
  step on the programme's checklist, observed by the trainer."
- Wrong or missing: this has two actions. C09 says "Each objective carries one action. Two actions
  make two objectives."
- To close it: cut "and record the weight in the register", or make recording a step on the
  checklist. Say so explicitly.

**H5 · C10 definition.text (B-C10-2).**
- As it stands: "A test matches a learning objective when every item … is marked against its
  standard."
- Wrong or missing: C12's standard is a whole-test threshold ("8 of the test's 10 questions
  right"), so a single item cannot be marked against it.
- To close it: distinguish the item's marking key from the objective's standard, which applies
  to the whole test.

**H6 · C10 must_know[5].point (B-C10-5).**
- As it stands: "Its tables give each skill a level: K (knows), KH (knows how), SH (shows how) or
  P (performs). A skill at SH cannot be tested on paper: the learner must show you."
- Wrong or missing: only SH's testing consequence is given. K against KH, and how P is assessed,
  are not.
- To close it: add one line each from the CBME Curriculum 2024 on how K, KH and P are assessed.

**H7 · C10 must_know[3].point (B-C10-6).**
- As it stands: "Give half the group each order of the two forms, with the halves the same size."
- Wrong or missing: nothing covers an odd-numbered group. The cancellation is shown only in a
  figure caption, and no problem practises it.
- To close it: add one line on an odd group (one learner over, whose gain is read with that in
  mind, or the group left unsplit), and a worked cancellation in the text.

## C11

**H8 · C11 simplified_explanation and figure (B-C11-2). Contradiction.**
- As it stands: "In this plan it is 40." Figure: "40 minutes with every learner answering in
  writing, 18 minutes of explaining, 2 minutes on the objective."
- Wrong or missing: the plan table is never shown. The 40 + 18 + 2 leaves no minutes for the
  pre-test, post-test or free recall unless they sit inside the 40, but must_know[2] says not to
  count the pre-test. The number and length of the teaching parts are not given, so the 40
  cannot be rebuilt.
- To close it: print the plan as the table the section tells the reader to write. Recount the 40
  so that the pre-test is excluded, and say whether the post-test and free recall count.

**H9 · C11 definition.text, parts 2, 6 and 7, with C12 (B-C11-4). Contradiction across sections.**
- As it stands: "A pre-test on one of two parallel forms." / "A post-test on the other form." /
  "A delayed test, booked before the session …". C12: "The delayed test is one week later, on a
  parallel form".
- Wrong or missing: with two forms, the delayed test repeats a form the learner has sat, which
  C10 warns can be answered from memory.
- To close it: name three parallel forms, or say which form the delayed test reuses and why that
  is acceptable.

**H10 · C11 definition.text (B-C11-5, B-TASK-4).**
- As it stands: "… bringing material back from memory, each alone and in writing …"; part 3:
  "… one question that every learner answers alone, in writing, without notes …".
- Wrong or missing: every retrieval is written, but C10 says an SH skill "cannot be tested on
  paper". Most of the book's own examples are hands-on (weighing a child). The book never says
  how to run retrieval, or observe each learner's pre-test and post-test, for a hands-on skill in
  a 60-minute session.
- To close it: add one line or must-know on retrieval for an SH skill (each learner performs,
  observed against the checklist). Say what observer ratio makes the pre-test and post-test
  feasible.

**H11 · C11 definition.text, part 5 (B-C11-7).**
- As it stands: "5. A closing free recall: notes away, each learner writes down all they can about
  the topic."
- Wrong or missing: unlike part 3, no correct answer follows, while C03 says feedback makes
  retrieval work more reliably. The reader cannot tell whether the omission is deliberate.
- To close it: add feedback to part 5, or say why none is given.

## C12

**H12 · C12 illustration.body and must_know[1].point (residue of B-C12-3).**
- As it stands: "The mean of the ten learners' own gains is a different number." / "The class gain
  worked out from the class means and the mean of each learner's own gain are different numbers."
- Wrong or missing: the definition calls "the mean of its learners' raw gains" the mean gain, and
  that equals the difference of the means (29). The sentence is true only of the mean of
  individual *normalised* gains. The restored "about 0.59" line now signals this, but the wording
  still says "gains".
- To close it: write "own normalised gains" / "own g" in both places.

**H13 · C12 practice problem 10 (B-C12-5).**
- As it stands: Problem 10 asks for "the class normalised gain at the delayed test".
- Wrong or missing: the illustration computes only the retained share (20/29) at the delay, never
  a delayed g, so the reader must decide that the room to gain still comes from the pre-test.
- To close it: show the delayed g in the illustration ((66 − 46)/(100 − 46)), or reword the
  problem.

**H14 · C12 practice problem 7 (B-C12-6).**
- As it stands: "What raw gain, in points, would equal Hake's interactive-course average of 0.48
  …"
- Wrong or missing: "points" could mean points out of 30 or percentage points.
- To close it: say "percentage points" (or "questions out of 30").

**H15 · C12 figure description (B-C12-8).**
- As it stands: "… the point at 80 and 100 sits on the dotted line across the top at 100."
- Wrong or missing: the caption never mentions a dotted line.
- To close it: add the ceiling line to the caption or the figure spec, or drop it from the
  description.

## C13

**H16 · C13 figure (B-C13-2).**
- As it stands: "Frich and colleagues split Levels 2, 3 and 4 by how the outcome is measured
  (2A, 3A, 4A) … (2B, 3B, 4B)." Figure: "Level 4, system results: 6".
- Wrong or missing: Level 4 is reported unsplit.
- To close it: split Level 4 as the source does, or say the source reports it unsplit.

**H17 · C13 must_know[2].point (B-C13-3).**
- As it stands: "This book's gate asks that your learners can do something they could not do
  before, and that you measured it."
- Wrong or missing: "gate" is defined in no section and not in the front matter (`book.yml`
  defines only the build).
- To close it: define the gate once (in the front matter or at first use) as the book's pass
  condition for the build.

**H18 · C13 must_know[2].point (B-C13-4).**
- As it stands: "That is Level 2B: a test you score, on the objective's action. Give it a week or
  more after the session …"
- Wrong or missing: Level 2B was defined by how the outcome is measured, not by timing. The
  sentence blends the two, so the reader cannot tell whether C12's end-of-session post-test is
  Level 2B.
- To close it: say that any scored test is 2B, and that the gate additionally asks for it to be
  delayed.

## C14

**H19 · C14 definition.text (B-C14-1).**
- As it stands: "The National Medical Commission (NMC) notified them in the Gazette on 2 June
  2023."
- Wrong or missing: F5's strong answer needs the statute that created the body and the section
  that grants the power. Neither is given (National Medical Commission Act, 2019, and its
  regulation-making section).
- To close it: add one sentence naming the Act and section, with its source.

**H20 · C14 simplified_explanation (residue of B-C14-2).**
- As it stands: "Under it sits the detail, in a guideline — a document NMC's undergraduate board
  sent out by letter and put on its website."
- Wrong or missing: F5's four levels have no slot for a guideline sent by letter. The restored
  lines put it under GMER 2023, but whether it binds is never said, while the must-know calls a
  timetable "out of line with the curriculum".
- To close it: state the guideline's legal standing (binding through GMER 2023's direction, or
  not), with its source.

**H21 · C14 definition.text (residue of B-C14-3).**
- As it stands: "It limits large group teaching to one third of a subject's allotted hours."
- Wrong or missing: "large group" is never sized.
- To close it: give the CBME Curriculum's definition of large-group teaching.

**H22 · C14 exercise 3 (B-C14-5).**
- As it stands: Ex 3 asks why the CBME Curriculum 2024 caps large group teaching at one third.
- Wrong or missing: the section never gives the curriculum's own reason, so the reader can only
  infer one from C01 and C03.
- To close it: quote the curriculum's stated rationale, or reword the exercise to ask for the
  learning-research argument.

**H23 · C14 definition.text (B-C14-6).**
- As it stands: "The 2019 regulation named the first five."
- Wrong or missing: the 2019 regulation is not named.
- To close it: name it (the Graduate Medical Education (Amendment) Regulations, 2019, if the
  source confirms).

## C15

**H24 · C15 simplified_explanation (B-C15-2).**
- As it stands: "To tell them apart, ask one question: what happens to it the day you go?"
- Wrong or missing: answers are given for a team ("it stops") and an institution ("keeps
  working"), never for a teaching lineage. Ex 1 asks for all three.
- To close it: add the lineage's answer (it carries on in the people you taught and those they
  teach).

**H25 · C15 simplified_explanation (B-C15-3).**
- As it stands: "Almost all of that success is what the doctors said about themselves, mostly
  measured straight after the course."
- Wrong or missing: "mostly straight after" is not supported by anything shown (C13's figure is by
  level, and C15's figure is after-only against before-and-after).
- To close it: source the timing claim from Frich, or cut "mostly measured straight after the
  course".

**H26 · C15 definition.text and must_know[1] (B-C15-4).**
- As it stands: "Four had a comparison group."
- Wrong or missing: C13 Ex 2 teaches that Frich says four in one place and five in another. C15
  states four without that caveat, which is the silent pick C13 warns against.
- To close it: write "four (the Results text says five)", or point to C13.

**H27 · C15 must_know[5].point (B-C15-5).**
- As it stands: "Join one professional body and one civil society organisation, and be useful to
  both."
- Wrong or missing: no reason is given, so the reader cannot defend or adapt the advice.
- To close it: add the reason in one line, with a source if it is claimed as a finding.
