# Draft notes · S57-R1 · batch b3 (C05, C06)

Resumed run, 2026-09-25. The C05 record from the interrupted run was lost, so C05 was written again
from scratch. C06 was an unchecked partial draft built on Pashler's abstract only. It has been
reworked against the whole article, now held, and every check was run again on both records as if
they were new.

## Records written

- `check/records/S57/S57-R1-C05.yml`: What does not work: rereading and highlighting (empirical, not
  quantitative). 39 definition references (Dunlosky 2013, Pashler 2008, Deslauriers 2019), 3
  illustrations, 6 must-know points, 1 teaching exercise, 3 retrieval items, 1 figure.
- `check/records/S57/S57-R1-C06.yml`: Learning styles: a popular claim that fails its own test
  (empirical, quantitative). 37 definition references (Pashler 2008 whole body, Newton & Miah
  2017), 3 illustrations, 8 must-know points, 10 practice problems, 1 design exercise, 3 retrieval
  items, 3 figures.

`python check/build.py --check`: blocking 0 overall, and no warnings on either record. Every
quote was checked by script against its source file with the build's own normalisation, and each
number's quote was checked to state that number: 103 of 103. The C06 practice answers and
illustration arithmetic were recomputed in Python (`/home/claude/scratch-b3/c06_check.py`). All
agree.

## What changed in C06 now that Pashler is held in full

- **A correction to the partial draft.** It listed "a crossover the wrong way round" (each group
  best with the unmatched method) as a pattern that *fails* the test. The body says otherwise.
  Pashler's criterion is deliberately liberal: it "does not require that the optimal method for
  each group would somehow match … each group's learning style". The learning-styles hypothesis
  "could be true without the meshing hypothesis being true". So that pattern would support
  learning styles in the broad sense and contradict meshing. The definition, practice 6 and the
  design exercise now say this.
- **A second correction.** The partial draft treated "one style group scores higher on both
  methods" as a failing pattern. Figure 1B shows a crossover can exist even when every subject in
  one group outscores the other group. Practice 4 now tests exactly this move, replacing the old
  problem, whose two MDs were equal.
- **Added from the body:**
  - the four criteria, including "if the tests are different, no support can be provided";
  - "plotted on the horizontal axis";
  - Figure 1C (both groups equal on one method);
  - Figures 1D to 1I (same method best for all, even if significant);
  - Figure 2's warning that the choice of horizontal axis decides whether a pattern "appears to
    cross over". This now sources the column-reading trap, which the partial draft had argued
    unaided.
  - the findings: Sternberg 1999 as the one arguable study (112 of 324, 35%; tenuous), Cook 2009
    with 123 internal medicine residents, and Constantinidou & Baker 2002;
  - the conclusion ("unwarranted") and the refutation caution;
  - the method varying by discipline, prior knowledge, and the cost argument.
- The Figure 1 and Figure 2 panels are not held. The section uses only the captions and the body's
  words, and says every table is invented.

## Anything unsourced or second-hand (for the auditor)

- Nothing is written as fact without a held quote. Three findings are second-hand, and the text
  names the reporter each time:
  - Karpicke et al. 2009 (84%, 55%), reported by Dunlosky;
  - Cook et al. 2009 and Sternberg et al. 1999, reported by Pashler;
  - the 2012 study of 93% of 137 schoolteachers (Dekker), reported by Newton & Miah.
- C06 illustration 2 calls Constantinidou & Baker "close to" the same-sign pattern. No cell means
  are held, only Pashler's words.
- C05 illustration 3 goes back to the Roediger & Karpicke Experiment 2 numbers that `S57-R1-C01`
  already teaches (14.2 read-throughs; ratings 4.8/4.2/4.0; 1-week recall 40/56/61). It is framed,
  as C03 frames Experiment 1, as a new question put to a known result: the group that only
  reread. The compression pass may judge it duplicative. If it is cut, the C05 figure goes with
  it, and C05 then needs a `figure_note`.
- "Fluency" is the section's word. Pashler's words are "ease or sense of familiarity". Deslauriers
  (cited in C01) uses "cognitive fluency" for lectures only.

## Practice-set size

C06 has 10 problems. The inventory estimated 3 to 6. I kept 10 because each problem adds a move
the others do not:

- sign-reading with both outcomes (L1, L2);
- the reverse, finding a missing cell (L3);
- the group-difference distractor of Figure 1B (L4);
- a gap that differs in size but not in sign (L5);
- a wrong-way crossover, broad hypothesis against meshing (L6);
- the column-reading trap of Figure 2 (L7);
- the half-empty table (L8);
- two transfer claims (L9, L10).

The set reaches all four bands. C05 is not quantitative and has no practice set.

## Figures

All specs pass `figspec.verify`. They were drawn with `draw.draw_spec`, the function `draw.py
--book` calls, from a helper (`/home/claude/scratch-b3/draw_mine.py`) that draws only my two
records. That kept me from rewriting other drafters' PNGs while they work. `draw.py` and
`figspec.py` were not edited. I looked at every PNG.

- `s57-r1-c05-sure-and-kept.png` (scatter): each group's mean rating against its 1-week recall.
  The x axis runs only from 4.0 to 4.8 because the spec has no `x_range`, and the caption says
  so. **Wanted:** an `x_range` option so the axis can show the whole 1-to-7 scale.
- `s57-r1-c06-crossover-means.png` and `s57-r1-c06-md-signs.png`: kept from the partial draft;
  their numbers are unchanged.
- `s57-r1-c06-lessons-along-bottom.png` (new): the second made-up table drawn with the lessons
  along the bottom, which is Pashler's Figure 2 point. Series colours follow series order, so
  magenta is "diagram lesson" in the first C06 figure and "visual group" in this one. The legends
  say which is which. The figure planner may want a fixed colour per series name.

## Choices the conductor may want to revisit

- The C05 title reads "rereading", not the inventory's "re-reading", to match C03, C04 and
  Dunlosky.
- C05 `concept_deps` adds C02 and C04, and C06 adds C03. Each is pointed to in the text; none of
  them is a forward reference.
- C05 is quoted from the Dunlosky PDF text layer. Several quotes keep the line-end hyphen breaks
  exactly as the file has them ("under - lined", "ques- tions", "educa- tional"). The reader-facing
  blockquotes are clean.

## Glossary rows (proposed; none of these terms is in prose/GLOSSARY.md)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| fluency | the ease with which a text reads or a fact comes to mind; it can come from things unrelated to understanding | `S57-R1-C05` |
| highlighting | marking the parts of a text that seem important while reading it; underlining counts as the same technique | `S57-R1-C05` |
| rereading | studying a text again after a first reading: the restudy of `S57-R1-C03`, done with a text | `S57-R1-C05` |
| utility (of a study technique) | Dunlosky and colleagues' overall rating, low, moderate or high: how widely a technique's benefit holds, and how it compares with the others | `S57-R1-C05` |
| criterion task | Dunlosky and colleagues' name for the final test used to measure what was learned | `S57-R1-C05` |
| learning styles | the idea that people differ in which mode of teaching or study works best for them | `S57-R1-C06` |
| learning-styles hypothesis | the claim that teaching fitted to a learner's style gives a better learning outcome | `S57-R1-C06` |
| meshing hypothesis | the commonest version: teaching works best in the format that matches the learner's preference | `S57-R1-C06` |
| crossover (interaction) | the method that gives one style group its best score is not the one that gives another group its best; in a 2 × 2 table, the two row MDs have opposite signs | `S57-R1-C06` |
| 2 × 2 table | a table of two rows and two columns, read "two by two" | `S57-R1-C06` |
