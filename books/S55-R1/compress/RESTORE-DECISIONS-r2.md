# S55-R1 step 5c, batch r2: restore decisions (C05 to C08)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (C05 to C08, plus
the "Across files" gaps that touch these sections), and `<S>-original.md`, `<S>-prose.yml` and
`<S>-pass1-prose.yml` for each section. Restore lists: `restore-lists/S55-R1-C05.txt` to
`S55-R1-C08.txt`, each line commented with its gap id. Outputs: `S55-R1-Cnn-final-prose.yml`,
built by `check/compress/restore.py` and checked by `check/compress/validate.py`. The tools were
not changed. Holes are written up for the fixer in `HOLES-r2.md`.

Key: **restored** = original sentences put back because they let the reader do the thing.
**hole** = the original does not fill it either, or it is an error; goes to the audit.
**not a defect** = nothing to do.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → final | Validate |
|---|---|---|---|---|---|---|
| C05 | 1107 | 352 | 368 | +16 (1 sentence) | 14.34 → 13.52 | OK |
| C06 | 1586 | 737 | 1010 | +273 (17 sentences) | 13.42 → 12.75 | OK |
| C07 | 1785 | 1030 | 1125 | +95 (6 sentences) | 11.46 → 11.38 | OK |
| C08 | 1072 | 666 | 718 | +52 (3 sentences) | 12.51 → 11.67 | OK |
| **Total** | 5550 | 2785 | 3221 | +436 | | 4 OK |

`python check/build.py --check` was not run: it needs the final text written back into the
records, which is outside this step's brief.

## Gap by gap

### C05
- **A-C05-1** restored in part: must_know[2] "Ask the programme what it already counts, and look for
  reviews that have gathered earlier studies." This names where to look. How to search, when to
  stop and what "answered well" means are in no version: hole H1.
- **A-C05-2** hole H2: the original only gives the reason ("under pressure to find that result"),
  never a demonstration.
- **A-C05-3** hole H3: sequencing; the original also states test 3 before C07 supplies the tool.
- **A-C05-4** hole H4: "Book 0" is in the original exercise too.
- **A-C05-5** hole H5 (with A-X-1): the original has no Illustration either.
- **A-C05-6** hole H6 (merged with A-C08-2): the scoring sheet has no "in doubt" item in the original.

### C06
- **A-C06-1** restored: the Heneberg check ("In one check, a biologist named Heneberg ..." to "The
  rest had been cited, and the database had missed it."). 0.3% is the "under 1%" end.
- **A-C06-2** restored: "Web of Science, owned by Clarivate, is the database behind most of the
  figures below; Scopus is another." and the Nicolaisen and Frandsen Scopus count ("counted in
  Scopus", the document types and window, "uncitedness ratio ... fraction of 1", "0.18 ... 0.64").
  The 1990 report's database is named nowhere: hole H7.
- **A-C06-3** hole H8: no fuller references, no gloss of Science/Nature, "peer-reviewed" undefined,
  in the original too.
- **A-C06-4** hole H9: "held" is in the original.
- **A-C06-5** restored: must_know[3] "But it leaves out many regional-language journals ..." and
  "Before concluding that a department's work goes unread ...". This gives the use. The fact itself
  is still unsourced: hole H10.
- **A-C06-6** restored: must_know[6] "Most of them, it finds, have some chance of being cited given
  enough time."
- **A-C06-7** restored: "They sorted them into seven designs ...", "They counted each article's
  citations to the end of the second year ...", "Meta-analyses, which combine earlier studies ..."
  and "Case reports, on one patient or a few ...". Defines both designs and what the medians count.
- **A-C06-8** hole H11: stating confidence is taught nowhere.
- **A-C06-9** hole H12 (error): "never cited" against a 5-year window is in the original.
- **A-C06-10** restored in part: must_know[4] "Test a question by who needs its answer and what they
  would do with it, as the last section began to do." The missing Illustration is hole H5.

### C07
- **A-C07-1** restored: "A funder is one kind of party that can be waiting." ties money to the
  test. Who holds which kind is left to the next book in the original too (no further hole).
- **A-C07-2** hole H13 (error): the original's camp also measures only weight and height.
- **A-C07-3** hole H14: the original never says why BMI misses people whom waist catches.
- **A-C07-4** restored: the Jhangiani, Ratan and Ioannidis sentences in definition.text name the
  guides.
- **A-C07-5** restored in part: analogy_breaks_when "Ioannidis counts research as useful when it
  changes a decision 'either by itself or when integrated with other studies'." "Guideline group"
  stays undefined: hole H15.
- **A-C07-6** restored in part: must_know[6] "The screen for this comes with the kinds of money in
  the next book." No concrete action here in any version: hole H16.
- **A-C07-7** hole H17 (with A-C02-5): overweight against obesity is never taught.
- **A-C07-8** not a defect: "write up" is plain English for writing the study's report, and the
  instruction (ask again before it) is usable as it stands.

### C08
- **A-C08-1** hole H18 (contradiction): the original table carries the same rows.
- **A-C08-2** hole H6: the original sheet also drops the in-doubt test, the design match and two
  feasibility lines.
- **A-C08-3** hole H19: the ten candidates are only in the figure in the original too.
- **A-C08-4** hole H20 (contradiction): same table rows in the original.
- **A-C08-5** hole H1 (merged with A-C05-1).
- **A-C08-6** hole H21: no rule for rank rejections in any version.
- **A-C08-7** hole H22.
- **A-C08-8** hole H23: the original says only "The scores put judgements in order", which the cut
  already carries in definition.text.
- **A-C08-9** restored: "The earlier sections of this book each gave you one check on a question."
  (antecedent of "them"). "This book's build" is in the original: hole H24.
- **A-C08-10** hole H25.

### Across files (the parts that touch C05 to C08)
- **A-X-1** hole H5.
- **A-X-2** restored in C08: "The question you keep is the seed of the one question you will own."
  and "The next book in this subject builds on it: a body of work, the data, a unit that houses them,
  and a three-year plan." The protocol and approval steps are in no version (in H1's neighbour, H26).
- **A-X-3** hole H1.

## Counts (37 gaps)

Restored (wholly or in part): 13. Hole: 23. Not a defect: 1. Four partial restores (A-C05-1,
A-C06-2, A-C06-5, A-C07-5/6) also leave a hole, listed in `HOLES-r2.md`.
