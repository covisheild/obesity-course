# S58-R1 step 5c, batch r1: restore decisions (C01 to C06)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (reader A, sections
01 to 06, and A-02-4's recurrences in 03, 04 and 06), and `<S>-original.md`, `<S>-prose.yml` and
`<S>-pass1-prose.yml` for C01 to C06. Exemplar: `books/S01-R1/compress/RESTORE-DECISIONS.md`.
The restore lists are in `restore-lists/S58-R1-C0n.txt`, each line commented with the gap it
closes. Outputs: `S58-R1-C0n-final-prose.yml`, built by `check/compress/restore.py` and checked by
`check/compress/validate.py`. The tools were not changed. No record was edited.

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means the original does not fill it either, or it is an error, or the original's
sentence cannot come back without raising the mean sentence length; each is in `HOLES-r1.md`
(item number given). **not a defect** means nothing to do.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → cut → final | Validate |
|---|---|---|---|---|---|---|
| C01 | 755 | 395 | 457 | +62 | 14.52 → 13.62 → 14.28 | OK |
| C02 | 551 | 307 | 355 | +48 | 14.89 → 13.95 → 13.65 | OK |
| C03 | 582 | 289 | 313 | +24 | 14.55 → 13.76 → 14.23 | OK |
| C04 | 832 | 392 | 421 | +29 | 15.13 → 14.52 → 15.04 | OK |
| C05 | 1112 | 575 | 685 | +110 | 13.73 → 13.37 → 13.70 | OK |
| C06 | 714 | 380 | 437 | +57 | 11.70 → 11.18 → 11.50 | OK |
| **Total** | 4546 | 2338 | 2668 | +330 | | 6 OK |

The prose files hold the definition, plain terms and must-know fields only. The figure caption and
the exercises are not in them and were not touched; a gap that sits in a caption or an exercise
cannot be restored here and is a hole if real.

**Restorations dropped for the mean sentence length.** Four candidates were in the original and
would have helped, but each raised the section's mean above the original's and failed
`validate.py`: C04 the definition's methods and results sentences (A-04-3), C04 "They hold only
what was known when the plan or protocol was written." (A-04-5; it also dangles without the
27-word methods sentence before it, and with that sentence the mean went 15.13 → 15.37), C05 the
"et al." sentence (A-05-S1), C06 the past-participle sentence (A-06-2). They are recorded as holes
(or, for A-04-3, not a defect), with the original sentence named so the fixer can weigh them.

`python check/build.py --check` / `--subject S58-R1` was not run: it needs the final text written
back into the records, which is outside this step's brief.

## Gap by gap

### Artifacts (not restored)
- **A-03-1, placeholder half** not a defect (artifact 1): `{{n:key}}` printed raw in the cold-read
  files. The conductor confirms the build substitutes the keys. The real half is below.

### C01
- **A-01-1** hole, HOLES 1: the original has the same sentence; ambiguity of wording, not missing text.
- **A-01-2** restored: "IMRAD is a convention that editors adopted, not a fixed law of science." and
  "In four leading general medical journals it was absent from original articles in 1935, ...
  (Sollaci and Pereira, 2004)." This names the source behind the figure and the must-know. The
  first sentence is there as the antecedent of "it" in the second. The four journals are not named
  in the original either (HOLES 2).
- **A-01-3** hole, HOLES 3: the original never defines the article types.
- **A-01-4** hole, HOLES 4: the original lists three or four types too; the exercise asks for "the one case".
- **A-01-5** hole, HOLES 5: the original never says to split a sentence that holds a result and its reading.
- **A-01-6** hole, HOLES 6: "protocol" is used, never defined, in the original (see also A-04-5).
- Dangling cut (brief rule, no gap id): restored "The four-part shape has a name, IMRAD, from the
  first letters of the parts." as the antecedent of the kept "It is a habit that editors spread ...".

### C02
- **A-02-1** hole, HOLES 7: the original says "Book 0" too, and Book 0 never names itself (A-00-2).
- **A-02-2** restored in part: "In one study that Chalmers and Glasziou cite, only around 60 per cent
  of trial reports described the treatment adequately.", "The information existed for 90 per cent."
  and "The difference was lost in the writing." These state the figure's link to the claim.
  "Clinical trial" and "adequate" stay undefined (HOLES 8).
- **A-02-3** hole, HOLES 9: the original does not name the study either.
- **A-02-4** hole, HOLES 10: the original carries the same instruction-less "the section you chose".
- **A-02-5** restored in part: "Finish the step: print the result of the comparison and say what it
  shows." This is the rule for a step sentence (turn it into evidence). No worked diary-to-argument
  rewrite exists in the original (HOLES 11).

### C03
- **A-03-1** (real half) hole, HOLES 12: no NFHS-5 figure is given in the original sections 01 to 03.
- **A-03-2** hole, HOLES 13: the original never spells out NFHS-5 or gives its years and population.
- **A-03-3** hole, HOLES 14: the original gives no criterion or example for the "so what?" test.
- **A-03-4** restored: "The abstract is the message with its reasons: what was known, what was
  missing, what you did, what you found, and what it means." Five parts, matching Ex 3's five
  sentences. The definition's four-part list stays beside it (HOLES 15, for the fixer).
- **A-02-4 (recurrence, Ex 3)** hole, HOLES 10.

### C04
- **A-04-1** restored: "It ends on the study's specific purpose: the question it asks, its research
  objective, or the hypothesis it tests (a statement the study is designed to support or refute)."
  This defines hypothesis. No example of the label exists in the original (HOLES 16).
- **A-04-2** hole, HOLES 17: the original never teaches judging the direction a limitation pushes.
- **A-04-3** not a defect: the plain terms give the methods' and the results' jobs, and Ex 1 can be
  answered from them (the reader did, after a second read). The definition's two sentences were
  tried and dropped: they raised the mean from 15.13 to 15.65.
- **A-04-4** hole, HOLES 18: the exercise's paper has no question in the original either.
- **A-04-5** restored in part by the A-04-1 sentence, which shows question, objective and
  hypothesis as forms of one purpose. Whether "objective" and "question" are one term, and what a
  protocol is, stay open (HOLES 19).
- **A-02-4 (recurrence, Ex 3)** hole, HOLES 10.

### C05
- **A-05-1** restored: "This section follows two documents."
- **A-05-2** restored: "ICMJE asks you not to cite predatory or pseudo-journals, and the section does
  not define them.", "In this book, read the phrase as journals that present themselves as checking
  what they publish and do not." and "How to recognise one is taught at the next rung." The original
  defers spotting one to the next rung, so that is not a hole here.
- **A-05-3** restored: "If you read a preprint, a paper posted publicly before a journal has checked
  and accepted it, cite the preprint and say it is one."
- **A-05-4** hole, HOLES 20: the original shows no formatted NLM reference.
- **A-05-5** hole, HOLES 21: the original gives no access to the NLM Catalog abbreviation.
- **A-05-6** hole, HOLES 22: the original does not cover an article number in place of pages.
- **A-05-7** restored in part: "The authors must check each reference against a bibliographic
  database such as PubMed or against the original." and "A reference manager, a program that stores
  your references and types out the list, can do the typing." "[pt]" stays unexplained (HOLES 23).
- **A-05-8** hole, HOLES 24: "where you can" is unexplained in the original, and the book's own
  second-hand citations are a contradiction, not missing text.
- **A-05-S1** ("et al.") hole, HOLES 25: the original's "Citing Medicine gives all authors, and shows
  an optional limit of three or six followed by "et al." or "and others"; the journal decides."
  glosses it only by implication, and it raised the mean (13.73 → 13.90 with the full list).
- **A-05-S2** (P, Q, R, S as source names; "(1)" as a reference number) not a defect: each label is
  defined where it is used, in the exercise and in this section.

### C06
- **A-06-1** restored: "In the active voice, the subject performs the action of the verb." and "In
  the passive voice, the subject receives the action: the active sentence's object becomes the
  subject." These resolve "them".
- **A-06-2** hole, HOLES 26: the original's past-participle sentence ("The verb then takes a form of
  "to be" ... (measured, taken, given).", 31 words) would show endings other than -ed, but raised
  the mean (11.70 → 12.00). Whether "out" belongs to the verb is not covered in the original.
- **A-06-3** hole, HOLES 27: "there" sentences are not covered in the original.
- **A-06-4** restored: "A subordinate clause also has a subject and a verb." and "It opens with a
  word such as although, because, when, if, since or while, and it cannot stand alone."
- **A-06-5** hole, HOLES 28: the original asserts the test can mislead and gives no example.
- **A-02-4 (recurrence, Ex 3)** hole, HOLES 10.

## Counts

By gap id (A-01-* to A-06-*, the two section-05 symbol items, and A-02-4's three recurrences in
this batch; A-03-1 counted once, by its real half):

| Decision | Count | Gaps |
|---|---|---|
| restored (whole or in part) | 12 | A-01-2, A-02-2, A-02-5, A-03-4, A-04-1, A-04-5, A-05-1, A-05-2, A-05-3, A-05-7, A-06-1, A-06-4 |
| hole | 24 | A-01-1, -3, -4, -5, -6; A-02-1, -3, -4 (+3 recurrences); A-03-1, -2, -3; A-04-2, -4; A-05-4, -5, -6, -8, -S1; A-06-2, -3, -5 |
| not a defect | 2 | A-04-3, A-05-S2 (plus A-03-1's placeholder half, artifact) |

Five of the restored gaps leave a remainder that is also in `HOLES-r1.md`: A-02-2, A-02-5, A-04-1,
A-04-5, A-05-7. A-02-4's recurrences in sections 07, 08, 10 and 12 are outside this batch.
