# Draft notes · S57-R1 · batch b4 (C07, C08)

Drafter, 2026-09-25. This run resumed an interrupted earlier run. That run had left unchecked
drafts of C07 and C08 and their two figures. Both records were re-checked from scratch. C07 was
reworked so that the full Rozenblit and Keil 2002 text, now held, carries the illusion claims.
C08 needed only small fixes.

## Records written

- `check/records/S57/S57-R1-C07.yml` (empirical, not quantitative). Changes from the earlier draft:
  - **Rozenblit and Keil now carry the claims they made.** The rate, explain, re-rate procedure,
    Study 1 (16 graduate students, a 1-7 scale, 48 items, four devices explained), the drop (Fig. 3
    caption), the students' surprise, Study 2 (33 undergraduates, same pattern), Study 6 (a warning
    made the drop smaller, not absent) and the domain results (large for devices and natural
    processes, small for facts, none for procedures and film plots) are all quoted from the 2002
    text. Fisher and Keil 2015 is kept only for "people with more education show it on their own
    subject", which is their finding, not the 2002 one.
  - **No mean rating is given.** The paper plots the means and does not print them. The definition
    and the illustration's `analogy_breaks_when` both say so.
  - **New boundary from the domain results.** People judge their knowledge of procedures about
    right, so asking for steps will not show the illusion; ask why each step is there. The earlier
    draft's worked cases (explain how to measure waist circumference; explain how to work out a
    BMI) were procedures, which is exactly where the 2002 paper found no drop. The illustration and
    the exercise now use the reasons behind the steps of measuring height instead. The record does
    not list those steps itself, so it asserts no clinical method.
  - Illustration 1 now uses the paper's own 1-7 scale and sends the reader to the PMC page to find
    three quoted sentences ("genuine surprise", "extreme warning", "cookbook").
  - The self-explanation evidence is split correctly. Self-explanation: materials, ages, and
    memory, comprehension and transfer. Elaborative interrogation: firmly shown only on memory
    after short delays. The earlier draft had merged the two.
  - Added: "below the high utility of practice testing" (Dunlosky Summary quote), and a pointer to
    C01's feeling of learning (C01 added to `concept_deps`).
  - The word "significant" is kept out of reader text. "The drop did not go away" stands for "still
    significant" (noted in the reference).
- `check/records/S57/S57-R1-C08.yml` (empirical, not quantitative). Fixes: a 49-word exercise prompt
  and two long sentences split; a quote added for "effects generally increase as prior knowledge
  increases" (Dunlosky 1.2b); "the review reports the direction, not the size" narrowed to the
  passages quoted, since the whole review is not held; a pointer back to C07 where the "why"
  questions come in.

Both records: `python check/build.py --check` gives blocking 0 overall and no warning for C07 or
C08. `draw.py --book S57-R1` drew 14 figures with 0 problems. I looked at both of mine. Every
definition quote, number quote and illustration block quote was confirmed in its source file by
script (`/home/claude/scratch-b4/qcheck2.py`), and each number quote states its number. The
Rozenblit file has no ligatures in the passages quoted. Arithmetic was recomputed in Python:
76 - 69 = 7; 32 - 28 = 4; 26/40, 18/24, 31/50 = 65%, 75%, 62%; 24/12 = 2.

## Decisions an auditor should look at

- **C07, "rated 48 things taken from books on how things work".** The 48 include 40 distracters.
  Only the eight test items are named in the text. The four each student explained were devices.
- **C07, the height example.** Nobody tested the reasons behind a clinical method. The record says
  so in `analogy_breaks_when` and offers it as a place to look, not a measured case.
- **C07, Fisher and Keil's "same laboratory".** Fisher and Keil 2015 is from Keil's laboratory;
  this rests on the bib entry's author list and the Keil-lab URL.
- **C08, the Woloshyn 24% and 12%.** Dunlosky does not say whether these are percentage points or
  relative increases. The record says so and draws only the ratio (2).
- **C08, the figure.** It shows the knowledge-moderation result, not working memory. No held source
  gives a number for working-memory capacity or load, so a figure of the section's core idea would
  have to invent one.

## Anything unsourced

Nothing reader-facing that I know of. The percentage problems in C08 illustration 1 and the ASHA
session plan in C08's exercise are made up and are labelled or plainly hypothetical.

## Practice-set size

Neither concept is quantitative (inventory: no), so neither has a practice set.

## Figures

- `s57-r1-c07-why-prompts.png`: Smith et al. 2010 (through Dunlosky), 76% against 69% correct.
- `s57-r1-c08-knowledge-and-why.png`: Woloshyn et al. 1992 (through Dunlosky), 24% against 12%.
- Wanted, not drawable from held data: Rozenblit and Keil's T1-T5 mean ratings for devices,
  facts and procedures, side by side. The means are only plotted in the paper. If a later intake
  reads them off Figs. 3 and 6 (marked as read from a graph), a line figure of the drop by domain
  would teach C07's boundary better than any prose.

## Glossary rows

None of these is in `prose/GLOSSARY.md` or in another batch's proposed rows.

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| cognitive load | the demand a learning task makes on working memory | `S57-R1-C08` |
| elaborative interrogation | a study technique: the learner works out why a stated fact is true | `S57-R1-C07` |
| extraneous load | cognitive load that comes from how material is presented and what the learner is made to do; the teacher can change it | `S57-R1-C08` |
| illusion of explanatory depth | people feel they understand how things work in more detail than they do; shown when their rating falls after they try to explain | `S57-R1-C07` |
| interleaving | mixing different problem types in one session instead of doing one type in a block | `S57-R1-C08` |
| intrinsic load | cognitive load that comes from the material's complexity for this learner; it changes only if the material or the learner's knowledge changes | `S57-R1-C08` |
| long-term memory | where learned things are kept; it has no known limit, and what comes back from it arrives as one piece | `S57-R1-C08` |
| self-explanation | a study technique: the learner explains how new information relates to what they know, or explains the steps they take in solving a problem | `S57-R1-C07` |
| worked example | a problem shown with its full solution, for the learner to study | `S57-R1-C08` |
| working memory | the part of the mind that holds what you are thinking about now; it holds only a few new elements at a time, and only briefly | `S57-R1-C08` |
