# S57-R1 step 5c: restore decisions, batch A (C01 to C08)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (reader A, gaps
A-C01-* to A-C08-*), and `<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml` for C01 to
C08. The restore lists are in `restore-lists/S57-R1-C0n.txt`, and each restored line is commented
with the gap it closes. The outputs are `S57-R1-C0n-final-prose.yml`, built by
`check/compress/restore.py` and checked by `check/compress/validate.py`. The tools were not
changed. Holes are listed for the fixer in `HOLES-A.md` (item numbers given below as H-n).

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means it could not be closed here: the original does not fill it either, it is
an error or contradiction, or the only closing sentence would have raised the mean sentence
length. **not a defect** means nothing to do.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → cut → final | Validate |
|---|---|---|---|---|---|---|
| C01 | 1363 | 706 | 856 | +150 | 12.05 → 11.78 → 11.97 | OK |
| C02 | 966 | 496 | 591 | +95 | 13.14 → 12.87 → 12.70 | OK |
| C03 | 793 | 419 | 494 | +75 | 13.44 → 13.09 → 13.35 | OK |
| C04 | 845 | 479 | 521 | +42 | 14.32 → 14.09 → 14.08 | OK |
| C05 | 782 | 388 | 451 | +63 | 12.22 → 12.12 → 12.19 | OK |
| C06 | 1206 | 692 | 728 | +36 | 14.02 → 13.84 → 14.00 | OK |
| C07 | 927 | 396 | 546 | +150 | 13.84 → 11.65 → 13.00 | OK |
| C08 | 878 | 442 | 514 | +72 | 14.39 → 13.81 → 14.28 | OK |
| **Total** | 7760 | 4018 | 4701 | +683 | | 8 OK |

`python check/build.py --check` / `--subject S57-R1` was not run: it needs the final text written
back into the records, which is outside this step's brief.

## The mean-length ceiling: restorations tried and dropped

The first build restored everything the gaps earned, and five sections (C01, C03, C05, C06, C08)
failed validation because the mean sentence length rose above the original's. The restored
sentences were long ones. These were then taken back out, least necessary first, until each
section passed:

- C01: the Definition's "In Deslauriers and colleagues' experiment (2019), physics students were
  allocated at random ..." (26 words). A-C01-5 is closed by the shorter Must-know sentence instead.
- C03: "Of the 49 effect sizes they could compute ..." (25 words; A-C03-2 becomes a hole, H-10) and
  "Drop any one of the three ..." (17 words; A-C03-5 is closed by the A-C03-1 line instead).
- C05: "Over half, 55%, named it the one they used most ..." (A-C05-5 is closed by the 84% line alone).
- C06: "In a survey of 114 academics ... Newton and Miah (2017) found that 58% agreed ..." (28 words)
  and its follow-on "They cite a 2012 study ... 93% of 137 UK schoolteachers ..." (A-C06-5 becomes a
  hole, H-26); "Searching a literature of several thousand articles ..." (24 words; A-C06-2 is closed by
  the shorter "Studies with the right design ..."); "The best method varies with the content ..."
  (A-C06-3 is judged not a defect).
- C08: "Intrinsic load comes from the complexity of the material ..." (27 words; A-C08-1 is closed by
  the plain-terms "Some of the load comes from the material itself ...").

## Side effects of the tool, noted rather than fixed

- C01 illustration: restoring "Now read the second column." brings back, by `restore.py`'s rule, the
  fenced block after that paragraph ("61 minus 40 = 21"). The first block ("83 minus 71 = 12") stays
  cut. Both numbers are in the kept sentence after them, so nothing is lost; the asymmetry is the
  tool's rule, not a choice.
- C06 definition: with "Searching a literature ..." still cut, "They conclude that applying learning
  styles ... is unwarranted" now follows "Studies with the right design found no support ...", so
  "They" can be read as the studies rather than Pashler and colleagues. Restoring "Searching ..."
  would fix it but breaks the mean ceiling. Listed as H-25 for the fixer.

## Gap by gap

### C01
- **A-C01-1** restored: "You have just taught a batch of third-year MBBS students ..." sets up the
  session that "At the end" refers to.
- **A-C01-2** restored: "Students learned one short prose passage." (what "it" is) and "Here are the
  percentages of the passage recalled on that final test." (what 83 and 40 are).
- **A-C01-3** restored: "Now read the second column." (brings the 61 − 40 working with it; see above).
- **A-C01-4** restored: "At the end of the first session, before any final test, each student filled
  in a short rating form." and "One question asked how well they would remember the passage in 1
  week, on a 7-point scale." The SSST value (4.2) is not in the C01 original; it is not needed to
  read 4.8 against 4.0 once the scale is given.
- **A-C01-5** restored: "In Deslauriers's experiment, a chance process decided who was taught
  actively." This is the antecedent of "Those students". The Definition's fuller sentence was tried
  and dropped for the mean ceiling.
- **A-C01-6** not a defect: with A-C01-5 restored, the evidence is on the page (the actively taught
  group rated its learning lower). The tension with C08's worked examples is recorded under A-C08-2
  (H-29).
- **A-C01-7** restored: "Deslauriers found that ratings tracked test scores more closely in students
  who already knew more physics."
- **A-C01-8** not a defect: "transmission" is defined here for C11, whose title and text use it
  ("retrieval rather than transmission").
- **A-C01-9** restored: "Both premises can be true." This is what "still" answers.
- **A-C01-10** hole, H-1: the original has the same ambiguous sentence.
- **A-C01-11** hole, H-2: no exercises in the original either; exercises are not the compression
  pass's to change.
- **A-C01-12** hole, H-3: "almost nothing that lasts" against 40% recall is in the original.
- Also restored in C01 for **A-C03-3**: "In Roediger and Karpicke's first experiment (2006), each
  student read two short prose passages." and "They then read one passage again and took a recall
  test on the other." C03's restored sentence says the first experiment was described in C01; this
  keeps that true.

### C02
- **A-C02-1** restored: "Both groups learn the same content, in the same time, and sit the same test
  after the same delay." This is the antecedent of "That delay".
- **A-C02-2** restored: "Anything else that affects the score is what OpenStax calls a lurking
  variable."
- **A-C02-3** restored: "The SMD the Cochrane Handbook uses, Hedges' adjusted g, divides by an SD
  pooled from both groups."
- **A-C02-4** restored: "You try a new method with a batch.", "Their marks go up." and "It feels like
  proof." These state the trap that "But marks go up" answers. Why marks rise after almost any
  teaching is asserted in the original too (H-4).
- **A-C02-5** hole (error), H-5: "Its sign says which group did better" is in the original.
- **A-C02-6** restored: "Papers often report an SMD as an "effect size", and some name the version,
  such as Hedges' g or Cohen's d."
- **A-C02-7** restored: "It came from volunteer teachers in university science courses." This says
  who Freeman's comparisons came from (problem 11). "Active learning" and "pooled" are undefined in
  the original too (H-6).
- **A-C02-8** hole, H-7: the original never says which number to report first.
- **A-C02-9** hole, H-8: no baseline threshold, no description of Deslauriers's A/B groups, and 72.02
  in the original's problem.
- **A-C02-10** hole, H-9: the transfer assumption and the "6%" are unflagged in the original too.
- **A-C02-11** hole, H-9: the original never says why a pre-to-post SMD and a between-group SMD
  cannot be compared.
- **A-C02-12** hole, H-9: "small" is unquantified and D6's standard error is unlinked in the
  original too.
- **A-C02-13** hole, H-9: the duplicated ASHA sentence and "growth chart" are in the exercises,
  which this step does not touch.
- **A-C02-14** hole, H-9: the original has no Illustration.

### C03
- **A-C03-1** restored: "In classrooms, Agarwal, Nunes and Blunt (2021) screened nearly 2,000
  abstracts and kept 50 experiments ..." (Definition) and "The classroom evidence is large and mostly
  from the United States and Europe." (the sentence before "Ten of the experiments" in plain terms).
- **A-C03-2** hole, H-10: the closing sentence ("Of the 49 effect sizes they could compute ...") was
  tried and dropped: it raised the mean sentence length from 13.44 to above the ceiling.
- **A-C03-3** restored: "Roediger and Karpicke's (2006) first experiment, which `S57-R1-C01`
  described, shows both halves." and "Each student reread one passage and tried to recall the other,
  with no feedback." This gives the within-student design. The 2-day point is given as a test time in
  the figure itself and needs nothing more.
- **A-C03-4** hole, H-11: the original never says practice testing and retrieval practice are the
  same thing (C05's restored line now says so, for C05).
- **A-C03-5** restored, by the A-C03-1 line: it says the classroom experiments were ones "in which
  each student retrieved alone, closed-book". That is the reason given. The original's direct
  sentence ("Drop any one of the three ...") was dropped for the mean ceiling.
- **A-C03-6** restored: "Classroom studies without feedback showed mostly small or very small
  effects." There is no numeric threshold in the original (H-12).
- **A-C03-7** hole, H-13: the exercise asks for a spacing date before C04; the original is the same.
- **A-C03-8** hole, H-2.
- **A-C03-9** hole, H-14: the comparison condition in Agarwal's review is not given in the original.

### C04
- **A-C04-1** hole (error), H-15: the wrong cross-reference is in the original.
- **A-C04-2** hole (error), H-16: 23 against 21 days is in the original.
- **A-C04-3** hole (error), H-17: "its share ... fell" is in the original.
- **A-C04-4** hole, H-18: the original gives the same ranges without explanation.
- **A-C04-5** hole, H-18: the original never says at which interval the 64% applies.
- **A-C04-6** hole, H-19: the original never demonstrates g = k(T − g). The largest demonstration
  gap in batch A.
- **A-C04-7** restored: "Dunlosky and colleagues give that fixed share, and Cepeda's own data bend
  away from it."
- **A-C04-8** hole, H-20: no mechanism anywhere in the original.
- **A-C04-9** restored: "In one study, when tests came only every 3 weeks, students left their study
  until just before each test." and "With daily tests, their study was spread out."
- **A-C04-10** hole, H-21: the original works with one review only.

### C05
- **A-C05-1** hole, H-22: the forward reference is unmarked in the original too.
- **A-C05-2** restored: "The rating asks two things.", "How widely does the benefit hold, across
  learners, kinds of material, kinds of final test and real classrooms?", "And how does the technique
  compare with the others?" and "Practice testing, the retrieval practice of `S57-R1-C03`, and
  distributed practice, the spacing of `S57-R1-C04`, were rated high." The other six techniques are
  not named in the original either; not needed to place "low".
- **A-C05-3** not a defect here: closed in C01 by A-C01-4.
- **A-C05-4** hole, H-14 (tension with C03's unstated comparison condition).
- **A-C05-5** restored: "At one highly selective university, 84% of students listed it among their
  study methods."
- **A-C05-6** hole, H-2.
- **A-C05-7** hole, H-23: the original gives no counts or effect sizes for highlighting.

### C06
- **A-C06-1** hole, H-24: "the broad sense" is undefined in the original.
- **A-C06-2** restored: "Studies with the right design found no support, one of them with 123
  internal medicine residents." "Searching a literature of several thousand articles ..." was
  dropped for the mean ceiling; see H-25 on the "They" it leaves.
- **A-C06-3** not a defect: the kept Must-know sentence "Choose methods for the material and the
  level." states the content argument, and the reader inferred it correctly from it.
- **A-C06-4** hole, H-27: the original gives no way to tell a real crossover from chance.
- **A-C06-5** hole, H-26: the closing sentences (Newton and Miah's statement, and the 93% of 137
  schoolteachers) were tried and dropped for the mean ceiling.
- **A-C06-6** restored, by the A-C06-2 line: the residents' study is one of the "studies with the
  right design".
- **A-C06-7** restored: "They call that last pattern a crossover interaction, drawn with the style
  groups along the bottom axis of a graph." This is Pashler's own link that the caption relies on.

### C07
- **A-C07-1** restored: "In a second study, 33 undergraduates showed the same pattern."
- **A-C07-2** restored: "When students were warned at the start that they would have to write
  explanations, the drop was smaller, but it did not go away." (the negative "either" follows) and
  "A later study from the same laboratory found that people with more education show it on topics
  from their own subject." (the evidence).
- **A-C07-3** restored: "Ask people to list the steps of a procedure, like the steps for weighing a
  child, and they judge what they know about right." and "Ask them why each step is there, and you
  are asking how something works." These draw the procedure/mechanism line.
- **A-C07-4** restored: "When you ask learners to explain, have them check the explanation against
  the text or against you." This says whose explanation. How a wrong one hurts is unexplained in the
  original too (H-28).
- **A-C07-5** hole, H-28: the figure's study is unnamed and chance at 50% is unmentioned in the
  original.
- **A-C07-6** restored: "A 2013 review by Dunlosky and colleagues rated both of moderate utility,
  below the high utility of practice testing." and "Self-explanation has helped across different
  materials, a wide range of ages, and tests of memory, understanding and transfer to new problems."
- **A-C07-7** hole, H-28: "anthropometry" is in the exercise, undefined in the original.
- **A-C07-8** hole, H-2.

### C08
- **A-C08-1** restored: "Cognitive load theory, set out by Sweller and colleagues, separates two
  sources of it." and "Some of the load comes from the material itself, and you cannot remove it
  without changing what is taught." The Definition's intrinsic-load sentence was dropped for the mean
  ceiling; the term "intrinsic" is therefore not on the page (not needed for any exercise).
- **A-C08-2** hole, H-29: no novice criterion, and the tension with C01 and C03, are in the original.
- **A-C08-3** hole, H-30: the original does not say what form the lasting steps take beside a
  diagram.
- **A-C08-4** hole, H-31: the figure is the same in the original.
- **A-C08-5** restored: "Interleaving, mixing different problem types in one session instead of doing
  one type in a block, gave college students better test results a week later."
- **A-C08-6** hole, H-31: asserted without data in the original too.
- **A-C08-7** hole, H-31: no number, elements/pieces and "transfer" are the same in the original.
- **A-C08-8** restored: "Then give a problem with part of the solution done, then a whole problem."
- **A-C08-9** hole, H-2.

## Counts

| | Restored | Hole | Not a defect | Total |
|---|---|---|---|---|
| C01 | 7 | 3 | 2 | 12 |
| C02 | 6 | 8 | 0 | 14 |
| C03 | 4 | 5 | 0 | 9 |
| C04 | 2 | 8 | 0 | 10 |
| C05 | 2 | 4 | 1 | 7 |
| C06 | 3 | 3 | 1 | 7 |
| C07 | 5 | 3 | 0 | 8 |
| C08 | 3 | 6 | 0 | 9 |
| **Total** | **32** | **40** | **4** | **76** |
