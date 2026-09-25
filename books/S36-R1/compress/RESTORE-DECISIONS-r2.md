# S36-R1 step 5c: restore decisions, batch r2 (C08 to C14)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (section 4, C08 to
C14, and the cross-cutting list in section 5 where it touches these sections), and
`<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml` for C08 to C14. Restore lists are in
`restore-lists/S36-R1-Cnn.txt`, each line commented with the gap it closes. Outputs are
`S36-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and checked by
`check/compress/validate.py`. The tools were not changed. C01 to C07 are batch r1.

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means it was not closable here; it is in `HOLES-r2.md` for the fixer and the
audit. **not a defect** means nothing to do, with the reason.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → final | Validate |
|---|---|---|---|---|---|---|
| C08 | 1003 | 501 | 562 | +61 (5 sentences) | 12.86 → 12.49 | OK |
| C09 | 933 | 487 | 519 | +32 (2) | 13.72 → 12.97 | OK |
| C10 | 1644 | 885 | 948 | +63 (5) | 12.48 → 11.76 | OK |
| C11 | 615 | 302 | 336 | +34 (3) | 11.83 → 11.59 | OK |
| C12 | 1421 | 777 | 804 | +27 (2) | 12.92 → 12.72 | OK |
| C13 | 716 | 359 | 394 | +35 (5) | 12.79 → 11.26 | OK |
| C14 | 1411 | 738 | 757 | +19 (2) | 11.53 → 10.25 | OK |
| **Total** | 7743 | 4049 | 4320 | +271 | | 7 OK |

`python check/build.py --check` / `--subject S36-R1` was not run: it needs the final text written
back into the records, which is outside this brief.

## Restores tried and dropped (mean sentence length)

Two restores the gaps justified failed validation because the original's sentences are longer
than the section's mean; they are recorded as holes, as S01-R1 C02 G3 was.

- C11 `definition.text`: "The respondent speaks more than the interviewer exactly when ..." and
  "That is the gate this rung sets." raise the mean 11.83 → 11.87 even with the other C11
  restores, 11.93 alone. The shorter `simplified_explanation` sentences were used instead.
- C12 `definition.text`: "Reading a transcript for analysis begins with reading the whole of it
  ..." and "That label is a code: ..." raise the mean to 12.96 (first alone, with C12-2) and 13.15
  (second, with C12-2). C12-2 was the sharper gap (a dangling "It"), so it kept the words.

## Gap by gap

### C08
- **C08-1** not a defect: `britten_1995` is on the section's reference list (record
  `definition.references`); the cold reader saw prose only. "Britten's point" is findable there.
- **C08-2** restored: must_know[5] "The recording keeps the words." It is the antecedent of "It
  does not keep the room".
- **C08-3** restored: must_know[1] '"Yes... okay..." keeps a person talking.' It sets acknowledging
  sounds against the kept "You are right, the diet is impossible", which is the line Ex 3 needs.
- **C08-4** restored: must_know[2] 'A probe made of their words, a pause, or "tell me more" adds
  nothing of yours.' It says "tell me more" and a pause are allowed, so Ex 2's rule is "no new
  content word". Ex 2's wording itself is an exercise and not touched.
- **C08-5** restored in part: must_know[4] "Then do come back to it: give them a name at the clinic
  to ask." (held-back medical questions). The rest (closing question, recorder off, upset
  respondent, what is said after) is a hole: the original does not cover it. HOLES-r2 H1.
- **C08-6** hole, H2: the original's definition of field notes says the same as the kept
  simplified sentence, and no example set of notes exists (cross-cutting "no worked field notes").
- **C08-7** restored: must_know[6] "Know your protocol's plan for this before the interview
  starts, and tell people at consent that confidentiality has limits." The clash with C09's
  promise is an error, recorded under C09-4 (H4).
- **C08-8** hole, H3: the original gives no criterion for when or how to steer back either.

### C09
- **C09-1** restored: definition "Britten (1995) states the general case." and 'Researchers "need to
  consider how they are perceived ..."'. The "wish to please" and "setting" quotations now follow
  a named source, and "None of these sources" has two named sources before it.
- **C09-2** not a defect: `mays_pope_2000` is on the reference list.
- **C09-3** hole, H5 (course-wide): "rung", "build", "S36-R2" are used the same way in the original
  and never glossed for the reader.
- **C09-4** hole (error), H4, **serious**: "Promise, truthfully, that nothing said will reach the
  clinic" is in the original and contradicts C07 and C08's disclosure duty.
- **C09-5** not a defect: "transcript" is ordinary English, defined in the next section (C10); the
  reader did Ex 2 and Ex 3 without it.

### C10
- **C10-1** hole, H6: the original does not teach minutes-to-hours or rounding a final 5 either.
- **C10-2** hole, H5.
- **C10-3** not a defect: `mcmullin_2023` is on the reference list (thirteen entries).
- **C10-4** hole (error), H7: the original's list of what the cleaned version dropped has the same
  five items.
- **C10-5** restored: analogy_breaks_when "A real recording would be in Chhattisgarhi.", "Putting it
  into English adds a second set of choices.", "This example does not show those.", "They do not
  tell you how long it takes to check a draft made by speech-to-text software ..."
- **C10-6** hole, H8: the original names translation and never teaches it.
- **C10-7** restored: must_know[1] "The point of a pilot is to hear your own interviewing, and
  cleaning takes out the fillers, interruptions and half-questions that show it."

### C11
- **C11-1** hole, H9: the original's word rule is the same.
- **C11-2** restored: simplified "This rung ends with a simple test." and "In your interview, did
  the respondent speak more than you did?" Together with the kept "If it is under 50 per cent, the
  respondent spoke more" and "The 50 per cent line is this course's gate", the gate is named early
  and 50.0 fails. The Definition's own statement of the gate could not come back (see above).
- **C11-3** hole, H10: the original also describes two excerpts it never shows.
- **C11-4** hole, H11, **sharpest practice-set hole**: the original never demonstrates working back
  from a share to a count.
- **C11-5** hole, H12: Ex 1 in the original also asks for a transcript the reader does not yet have.
- **C11-6** restored: must_know[3] "Report each interview's share, and open the transcript of any
  that sits near or above half.", with "In your interview ..." above.

### C12
- **C12-1** hole, H13: the original's sentences that close it ("Reading a transcript ... begins",
  "That label is a code: ...") fail validation (see above). The kept `simplified_explanation`
  carries both the first reading and "That label is a code."
- **C12-2** restored: analogy_breaks_when "A code here is your own label for finding and comparing
  passages." (antecedent of "It is not yet a finding") and "That does not tell you what share of
  the clinic's patients stop for that reason."
- **C12-3** hole, H5.
- **C12-4** hole, H14: no test for "bears on the study question" in the original.
- **C12-5** hole, H15: respondent labels reused for different people (also cross-cutting).

### C13
- **C13-1** restored: definition "A reader checks a quotation with the four acts used on any
  reference." and the four acts ("Find the transcript." ... "Read whether it says what it was quoted
  for."). "The last of those checks" now has its referent.
- **C13-2** hole (error), H16: the R3 "job with no day off" is in the original and appears nowhere.
- **C13-3** hole, H17: no model quotation in the original.
- **C13-4** hole, H18: output format for the one-page brief is not taught (same as C02-8, batch r1).

### C14
- **C14-1** hole (error), H19, **serious**: C14 Ex 1 "consent record, kept without names" is in the
  original. C07's side belongs to batch r1.
- **C14-2** hole (error), H20: forbidden or discouraged; same in the original.
- **C14-3** hole, H21: recruitment is not taught in the original.
- **C14-4** hole, H22: the original's seven steps also omit ethics review.
- **C14-5** hole, H23: nothing on the recorder or on judging the consent talk in the original.
- **C14-6** hole, H5.
- **C14-7** restored: illustration "Pilot 3 also had a question that fell flat." and '"What does the
  clinic do for you?" drew one-word answers.' It shows what "fell flat" means. (C06-1 is batch r1.)

### Cross-cutting (C08 to C14 side only)
- **Sources never referenced**: not a defect for Britten, Mays and Pope, McMullin (all on the
  record reference lists); the unattributed C09 quotations are closed by C09-1.
- **Dangling referents**: C08 (C08-2), C12 (C12-2), C13 (C13-1) restored.
- **Figures describing material not shown**: C11, hole H10.
- **Terms before home section**: transcript in C09 not a defect (C09-5); field notes (C08) H2; gate
  in C11 closed by C11-2.
- **No worked field notes, topic guide or consent script**: field notes H2 (topic guide and
  consent script are C06/C07, batch r1).
- **Respondent labels reused**: H15.

## Counts (C08 to C14, 42 gaps)

Restored 13 · hole 25 · not a defect 4 (13 + 25 + 4 = 42). C08-5 is counted as restored; its
unrestorable remainder is also hole H1, so HOLES-r2 has 23 entries (several gaps share H5).
