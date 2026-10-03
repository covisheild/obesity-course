# S58-R1 step 5c: restore decisions, batch r3 (C13 to C18)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (Reader B, gaps
B-13-* to B-18-*), and `<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml` for C13 to
C18. The restore lists are in `restore-lists/S58-R1-Cnn.txt`, each line commented with the gap it
closes. The outputs are `S58-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and
checked by `check/compress/validate.py`. The tools were not changed. No record was edited.

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means it was not closable here and is written up in `HOLES-r3.md`. **not a
defect** means nothing to do. Where a restore closes only part of a gap, the rest is in
`HOLES-r3.md` as well, and the line says so.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → cut → final | Validate |
|---|---|---|---|---|---|---|
| C13 | 1174 | 616 | 621 | +5 | 13.20 → 12.78 → 12.60 | OK |
| C14 | 682 | 364 | 422 | +58 | 13.64 → 13.48 → 13.61 | OK |
| C15 | 861 | 390 | 473 | +83 | 14.35 → 13.45 → 13.91 | OK |
| C16 | 791 | 374 | 395 | +21 | 15.21 → 14.96 → 15.19 | OK |
| C17 | 763 | 428 | 475 | +47 | 14.37 → 14.21 → 14.34 | OK |
| C18 | 761 | 399 | 466 | +67 | 13.81 → 13.30 → 13.71 | OK |
| **Total** | 5032 | 2571 | 2852 | +281 | | 6 OK |

Exercises, problems and figure captions are not in the prose files: the cut did not touch them,
and this step cannot either. Every gap that sits only in one of them is a hole.

`python check/build.py --check` / `--subject S58-R1` was not run here: it needs the final text
written back into the records, which is outside this step's brief.

## The mean-sentence limit cost four restores

Restored sentences in C14, C16 and C18 were longer than the section's mean, and the first lists
failed validation (C14 13.64 → 14.07, C16 15.21 → 15.82, C18 13.81 → 14.03). No list was padded
with short sentences to pull the mean down. Instead, where a shorter original sentence did the
same job it was used (C14, B-14-4), and otherwise the lowest-value restore was dropped and its gap
moved to the holes:

- C14 B-14-4: the must-know's own reason, "Make the slide version again, with fewer elements,
  thicker lines and bigger text ..." (25 words), dropped; the definition's three short sentences
  on print against slide restored instead. What to change on the slide remains a hole.
- C16 B-16-1 ("It usually adds an error bar for ...", 19 words) and B-16-4 ("With more values, a
  box plot shows the median ...", 29 words): the section has room for one of the three restores,
  and B-16-5 was kept.
- C18 B-18-2 ("Bateman and colleagues (2010) showed 20 people charts by the graphic artist Nigel
  Holmes ...", 25 words): dropped, because the figure caption already names Bateman (2010) and
  Holmes charts.

## Gap by gap

### C13
- **B-13-1** restored, partly: "The wording need not match." Paraphrase passes, so "the two surveys" for
  NFHS-4 and NFHS-5 is fine. The second reader dropping "India" while the first reader's lost age
  range is a failure is the original's own inconsistency: hole H-13-1.
- **B-13-2** hole H-13-2: the original's table is the same ("Indian women" flags only the age
  range; "increasing" marked kept).
- **B-13-3** hole H-13-3: the original never defines "how far it reaches" either.
- **B-13-4** hole H-13-4: Exercise 2 step 4; the original names no program here or in C11.

### C14
- **B-14-1** not a defect (artifact 1, `{{n:key}}` placeholders in the caption).
- **B-14-2** hole H-14-2: the figure caption; the original never explains indicator numbers.
- **B-14-3** hole H-14-3: Exercise 4's "all eight NFHS bars" against a four-bar figure, in the original too.
- **B-14-4** restored, partly: "A figure on a printed page can be studied ...", "A figure on a slide is
  seen for a few seconds ...", "The two are made separately." The reason is back; what to change
  is not (see above): hole H-14-4.
- **B-14-5** restored: "Wilke recommends three to six figures for a scientific paper ..." The limit is on the
  number of figures.

### C15
- **B-15-1** not a defect (artifact 2, record id `B0-R0-C40` printed raw).
- **B-15-2** restored: "They are position along a common scale, position along scales that are not lined up,
  ..." The ten are named.
- **B-15-3** hole H-15-3: the tie at third place makes "the first four places" ambiguous in the original;
  no chart shows judging direction.
- **B-15-4** hole H-15-4: the original never illustrates scales not lined up.
- **B-15-5** restored: "Many values from one group take a chart of how they spread, which the next section is
  about." The original names no chart here either; the pointer is what it has.
- **B-15-6** restored: "Avoid making the reader compare pieces stacked inside bars, or slices of a pie." and
  "Those are lengths without a shared start, and angles." This gives the reason, tied to the order.
- **B-15-7** hole H-15-7: Exercise 3's "the table in this section"; there is no table in the original.
- **B-15-8** hole H-15-8: dots on a log axis here against bars from 1 in C17; a contradiction in the original.
- **B-15-9** restored, partly: "Neither are conditions a person can have together, such as stunting and underweight
  in the same child." The overlap is now stated. Stunted, wasted and underweight are still undefined: hole H-15-9.

### C16
- **B-16-1** hole H-16-1: the original's sentence says what an error bar stands for, not what it is,
  and was dropped for the mean (see above).
- **B-16-2** hole H-16-2: the 14.3 is right for the record's figure data (sample SD 14.29, 14.28,
  14.25, checked here), but the values are in the spec only, and "climbs evenly" is approximate.
- **B-16-3** hole H-16-3: the second figure is a dot-and-line chart by rank, not a strip chart, in the original.
- **B-16-4** hole H-16-4: the box-plot description exists in the original but was dropped for the mean.
- **B-16-5** restored: "A share of people with a condition is one number per group, and a bar or dot is right
  for it."
- **B-16-6** hole H-16-6: the original never names the review's authors or has Weissgerber recommend anything.
  The "why not a box plot" half of Exercise 1 is answerable from the kept must-know.

### C17
- **B-17-1** not a defect (artifact 1).
- **B-17-2** hole H-17-2: the original states LF = a ÷ (a − s) "as the second illustration shows", and no
  illustration derives it.
- **B-17-3** hole H-17-3: the shortcut fails for a fall; this is an error in the original.
- **B-17-4** hole H-17-2 (same): the original never connects the drawn and data ratios to the LF.
- **B-17-5** restored, partly: "Then "twice" and "half" have the same length, pointing opposite ways, ..."
  Why bars start at 1 is not in the original: hole H-17-5.
- **B-17-6** hole H-17-6: log10 is not taught in the original either.
- **B-17-7** hole H-17-7: "ink" is used before C18 defines it, in the original too.
- **B-17-8** restored: "The range you pick for a line chart still sets how big the change feels." It is the
  antecedent of "So".
- **B-17-9** restored: "In Correll's experiments the exaggeration stayed even when readers reported the
  numbers accurately." The source is named before P13. What "the critics cannot claim" points at is
  part of the problem's own reasoning.
- **B-17-10** not a defect: P13 is a "decide what to compute" problem. Working out that 4.6% is
  points from the 1.13 ratio is the task, and the reader did it.
- **B-17-11** hole H-17-11: P7 assumes equal bar widths and does not say so, in the original too.

### C18
- **B-18-1** restored: "He gives no one-sentence definition of chartjunk." and "He introduces it as decoration
  that "does not tell the viewer anything new"."
- **B-18-2** hole H-18-2: the original sentence was dropped for the mean (see above). The caption names
  Bateman (2010) and Holmes charts. The original never ties the title "Useful junk?" to Bateman in words.
- **B-18-3** hole H-18-3: the original never identifies Wilke (C14's restored line shows only that he is
  an author).
- **B-18-4** restored, partly: "The third dimension carries no data and it bends the bars: ..." This gives the reason.
  "Flat data" is undefined in the original: hole H-18-4.
- **B-18-5** hole H-18-5: the original teaches no order beyond "Do this before you change anything else".
- **B-18-6** restored: "So is a direct label: ... in place of a legend, the key that says which colour is
  which." Here, legend means the key. That C14 calls the caption "the figure legend" is a book-wide
  double meaning: hole H-18-6.

## Totals

41 gaps: 14 restored (6 of them partly, with the remainder in `HOLES-r3.md`), 23 holes, 4 not a
defect (3 artifacts, B-17-10).
