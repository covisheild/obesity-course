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
