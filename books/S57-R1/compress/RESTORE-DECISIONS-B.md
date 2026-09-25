# S57-R1 step 5c: restore decisions, batch B (C09 to C16)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (reader B, gaps
B-C09-* to B-C16-* and B-TASK-*), and `<S>-original.md`, `<S>-prose.yml` and
`<S>-pass1-prose.yml` for C09 to C16. The restore lists are in `restore-lists/S57-R1-Cnn.txt`, and
each restored line is commented with the gap it closes. The outputs are
`S57-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and checked by
`check/compress/validate.py`. The tools were not changed, and no record was edited.

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means it was not closable here, and it is written up for the fixer in
`HOLES-B.md`. **not a defect** means nothing to do, with the reason given.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → final | Validate |
|---|---|---|---|---|---|---|
| C09 | 698 | 381 | 471 | +90 | 11.93 → 11.07 | OK |
| C10 | 921 | 494 | 494 | +0 | 13.75 → 13.72 | OK |
| C11 | 660 | 362 | 413 | +51 | 12.32 → 11.60 | OK |
| C12 | 1899 | 993 | 1193 | +200 | 11.17 → 10.94 | OK |
| C13 | 781 | 403 | 444 | +41 | 12.20 → 11.38 | OK |
| C14 | 1056 | 527 | 611 | +84 | 14.27 → 13.89 | OK |
| C15 | 1091 | 515 | 579 | +64 | 14.36 → 14.12 | OK |
| C16 | 1175 | 638 | 714 | +76 | 14.87 → 14.57 | OK |
| **Total** | 8281 | 4313 | 4919 | +606 | | 8 OK |

C10: the one sentence that would have been restored (for B-C10-4) took the mean from 13.75 to
14.0 and failed validation. The pass-1 text already answers the gap (see B-C10-4), so the list is
empty and the reason is written in the list file. That is not a tool conflict.

`python check/build.py --check` / `--subject S57-R1` was not run. It needs the final text written
back into the records, which is outside this brief.

Counts: 65 gaps (60 section gaps, 5 task-level). **28 restored, 25 hole, 12 not a defect.**

## Gap by gap

### C09
- **B-C09-1** hole (H1): the original has no worked objective either.
- **B-C09-2** restored: "Chatterjee and Corral name five of these parts ...". This is their first
  mention and says what they are the source of. The full citation is in the record's sources.
- **B-C09-3** restored: "Ask whether the learner meets a case they have not seen before, or
  repeats something they were shown." This gives a working test for "above remember". The
  original never glosses apply, analyse, evaluate or create either (residue in H2).
- **B-C09-4** restored: "\"Describe\" sits under both remember and understand ..." (one verb at
  two levels) and the "Ask whether ..." sentence above.
- **B-C09-5** restored: "For a skill like that, still write an action you can watch ..." and
  "Then judge it by watching, not by the verb list." Ex 1.2 can now be done.
- **B-C09-6** not a defect: the book's front matter (`book.yml` how_to_read) defines the build as
  "a single session, taught to real learners, with a written objective and a measure of what they
  learned". Ex 2 restates it. The cold reader's copy lacked the front matter.
- **B-C09-7** hole (H3): the original has the same "By when" wording. C10's model says "end of
  session" and C13 says "a week or more".
- **B-C09-8** hole (H1): the original gives no example standard either. Same fix as B-C09-1.

### C10
- **B-C10-1** hole (H4, contradiction): the model objective in Ex 1 has two actions ("weigh ... and
  record"). The exercises are not the compression pass's to change.
- **B-C10-2** hole (H5): the original also says every item is "marked against its standard".
- **B-C10-3** not a defect: the BMI example is a contrast (a test of the wrong thing). The reader
  does not have to classify BMI to see the mismatch.
- **B-C10-4** not a defect: the kept must_know[2] already says partner items ask for "the same
  action on different cases" (for an observed test, a different child). The reader got it right.
  The one fuller original sentence failed validation (see above).
- **B-C10-5** hole (H6): the original glosses only SH's testing consequence as well.
- **B-C10-6** hole (H7): the original never covers an odd-numbered group. The reason the
  difficulty cancels is in the caption, and the reader used it.
- **B-C10-7** not a defect: the sentence glosses internal assessment in its own words ("from
  day-to-day tests, and quizzes can count"), and its point (counted quiz marks are not
  low-stakes) is usable without more.

### C11
- **B-C11-1** restored. The cut had removed part 3's question-and-answer ("Each is followed by one
  question that every learner answers alone ...") and all of part 4 ("One question on material
  from an earlier session ..."). Both are back, so the list runs 1 to 7 and part 3 carries its
  retrieval.
- **B-C11-2** hole (H8, contradiction): the original has no plan table either, and its 40/18/2
  minutes leave no room for the pre-test, post-test or free recall.
- **B-C11-3** restored: "Then you count." dangled. The sentences before it are restored: "The
  earlier sections gave you the pieces." and "This section puts them in order on one page ...".
- **B-C11-4** hole (H9, contradiction across sections): the original also has only two forms and a
  delayed test "on a parallel form".
- **B-C11-5** hole (H10): the original also makes every retrieval written, and never says how to
  run retrieval for an SH skill.
- **B-C11-6** not a defect: C13 gives "a week or more after the session" and C04 gives the gap
  arithmetic. The reader did it from taught text.
- **B-C11-7** hole (H11): the original's free recall also has no answer shown after it.
- **B-C11-8** restored: "Spread them for other reasons: short teaching parts, attention, a turn
  for every learner."

### C12
- **B-C12-1** restored: "Hake (1998) defines the class form, 〈g〉, from class-average scores."
  This introduces Hake before first use. "Cited below" is not a defect: the record cites
  `hake_1998_normalized_gain`, so the rendered booklet prints the reference. The cold reader's
  copy lacked the reference list.
- **B-C12-2** restored: "Hake surveyed 62 physics courses." and the two sentences giving 0.23
  (SD 0.04, 14 courses) and 0.48 (SD 0.14, 48 courses). The averages are now stated before the
  analogy refers to them.
- **B-C12-3** restored: "It equals the mean post-test score minus the mean pre-test score." (so
  the mean raw gain is 29) and "Work out each, add them, and divide by 10: it comes to about
  0.59." The "different number" is now the mean of individual g. The wording "the mean of each
  learner's own gain" is still loose (residue in H12).
- **B-C12-4** restored: the original's worked SD ("Next, the spread." to "The SD of the gains is
  about 9.9 percentage points.", with its working block). It divides by 9 (n − 1), so Problem 3
  has one answer (7.91).
- **B-C12-5** hole (H13): the original also computes only the retained share at the delay, not a
  delayed g.
- **B-C12-6** hole (H14): "in points" is in the problem text, which the pass does not touch.
- **B-C12-7** restored: the "48 courses ... 0.48, with an SD of 0.14" sentence makes the SD a
  spread across courses.
- **B-C12-8** hole (H15): the original figure description has the same unexplained dotted line.
- **B-C12-9** restored: "Read the question again before you teach the topic again."
- **B-C12-10** restored: the "14 courses ... SD of 0.04" sentence gives the traditional courses'
  SD that Problem 13 needs.
- **B-C12-11** not a defect: the reader solved Problem 5 correctly with C2's rearrangement. Nothing
  stopped them.

### C13
- **B-C13-1** restored: "To evaluate teaching is to measure some outcome of it." This is the
  antecedent of "those outcomes".
- **B-C13-2** hole (H16): the original figure also has a single Level 4.
- **B-C13-3** hole (H17): "gate" is defined nowhere in the original or the front matter.
- **B-C13-4** hole (H18): the original has the same blend of Level 2B with timing.
- **B-C13-5** restored: "It tells you whether learners could hear, kept up, and would come back
  ..." and "Use the form for those questions and a test for learning."
- **B-C13-6** not a defect: the exercise tests judgement. The reader answered it from D5's
  already-taught habit of checking printed numbers against each other, which is the intended
  move.

### C14
- **B-C14-1** hole (H19): the original also never names the statute that created NMC or its
  power.
- **B-C14-2** restored: "They direct NMC's undergraduate board to publish the model curriculum
  ..." and "It calls itself guidelines, it was issued by letter, and it places itself under GMER
  2023." These put the guideline under the regulation. Whether a guideline binds is still never
  said (residue in H20).
- **B-C14-3** restored: "Lectures to a large group may take at most a third of a subject's hours."
  This reads "large group teaching" as lecturing. The group size is never given (residue in H21).
- **B-C14-4** restored: "Each mentor gets three students during the Foundation Course ..." and
  "Mentors are drawn from Assistant Professor upwards ...".
- **B-C14-5** hole (H22): the original never gives the curriculum's own reason for the cap.
- **B-C14-6** hole (H23): the original never names the 2019 regulation.
- **B-C14-7** not a defect: the reader answered Ex 2 fully. Naming an excluded specialty is not
  needed for it.

### C15
- **B-C15-1** restored: "Frich and colleagues' systematic review found 45 published studies ...".
  This is the antecedent of "All 45".
- **B-C15-2** hole (H24): the original also never gives the lineage's answer to "what happens to
  it the day you go?".
- **B-C15-3** hole (H25): the original has the same unsupported "mostly measured straight after the
  course".
- **B-C15-4** hole (H26): the original also says "four" without the four-or-five caveat that C13
  teaches.
- **B-C15-5** hole (H27): the original gives no reason for joining either.
- **B-C15-6** restored: "Kotter (1990) argued that leadership has nothing to do with charisma ...".
  This is the first mention, with a date and what he argued.
- **B-C15-7** restored: "You get three first-year students a year, and they stay with you until
  they finish internship."

### C16
- **B-C16-1** restored: "Role clarity means writing down, for each decision, who makes it ...".
  This is the antecedent of "that sheet".
- **B-C16-2** restored: "Last, two kinds of disagreement." (antecedent of "They") and "How to
  handle each is for the next book in this subject."
- **B-C16-3** not a defect: "three matching activities", with the two lists in parallel order,
  states the pairing. The reader's pairing is Kotter's.
- **B-C16-4** restored: "An order from the post does not reach a department you do not head." and
  "Trust built over time can reach people no post does." Ex 2 item 1 is now decidable
  (authority).
- **B-C16-5** restored: "It rests on your record, and on whether what you do matches what you
  say."
- **B-C16-6** not a defect: the record cites `kotter_1990_what_leaders_do`, so the rendered
  booklet prints the reference.

### Task-level
- **B-TASK-1** not a defect: how to measure waist circumference is anthropometry, taught in
  another subject's book. S57 teaches how to teach a session on a topic the reader chooses (C09
  Ex 2, C11 Ex 2). It does not teach the topic itself. The waist session was the cold-read
  brief's choice, not the book's.
- **B-TASK-2** not a defect, for the same reason: a measuring tolerance is subject content for the
  topic being taught. D7 already gives the error-against-reference idea.
- **B-TASK-3** restored in C12: "A learner's score on a test is written here as a percentage of the
  test's maximum, from 0 to 100%." A checklist score is then items met over items. Whether one
  item acts as a gate is the objective's standard (C09).
- **B-TASK-4** hole: this goes with B-C11-5 (H10). The book requires SH skills to be observed and
  puts pre-tests and post-tests inside a 60-minute session, but it never addresses observing each
  learner. It is the same fix.
- **B-TASK-5** restored in C09 with B-C09-5: for a skill Bloom cannot grade, "write an action you
  can watch ... judge it by watching". This works for any learner group.

### Outside scope
Reader B's three notes on C02 and C04 belong to batch A's sections. They are not decided here.
