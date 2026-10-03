# S58-R1 step 5c, batch r4: restore decisions (C19 to C23)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (reader B, sections
19 to 23, and reader B's symbol list as it touches these sections), and `<S>-original.md`,
`<S>-prose.yml` and `<S>-pass1-prose.yml` for C19 to C23. Exemplar:
`books/S01-R1/compress/RESTORE-DECISIONS.md`. The restore lists are in
`restore-lists/S58-R1-C19.txt` to `-C23.txt`, each line commented with the gap it closes. Outputs:
`S58-R1-C19-final-prose.yml` to `-C23-final-prose.yml`, built by `check/compress/restore.py` and
checked by `check/compress/validate.py`. The tools were not changed. No record was edited.

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means the original does not fill it either, or it is an error, or the original's
sentence cannot come back without raising the mean sentence length or tripping the tool conflict
below; each is in `HOLES-r4.md` (item number given). **not a defect** means nothing to do;
**artifact** is the "Two artifacts" section of `COLD-READ-GAPS.md` (raw `{{n:key}}` placeholders).

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → cut → final | Validate |
|---|---|---|---|---|---|---|
| C19 | 831 | 394 | 516 | +122 | 15.11 → 12.31 → 13.23 | OK |
| C20 | 778 | 403 | 474 | +71 | 14.96 → 14.39 → 14.81 | OK |
| C21 | 794 | 401 | 401 | +0 | 13.69 → 13.37 → 13.37 | OK |
| C22 | 2038 | 1112 | 1308 | +196 | 11.57 → 10.27 → 10.58 | OK |
| C23 | 777 | 455 | 487 | +32 | 14.49 → 14.39 → 14.48 | OK |
| **Total** | 5218 | 2765 | 3186 | +421 | | 5 OK |

The prose files hold the definition, plain terms, illustration (C22) and must-know fields. Figure
captions and exercises are not in them and were not touched; a gap that sits in a caption or an
exercise cannot be restored here and is a hole if real.

Trials that failed validation and were dropped (the restore list was changed, never the tool):
C20 with the 95% CI sentence (mean 15.10 with the legend sentences alone, 15.32 with the n
sentences too); C23 with "A fact sheet read online is not a journal article ..." (14.58).

## Tool conflict (C22): needs the conductor's decision

`restore.py`'s docstring says a fenced block comes back if "the prose paragraph immediately before
it got a sentence restored". The code (`rebuild`, `prev_restored = restored_here`) tests the whole
run of prose between two fences, not the last paragraph. In C22's illustration, restoring B-22-5's
two sentences ("The fact sheet's rows for non-pregnant and pregnant women rose too." / "They are
left out because the row for all women contains them ...") sits three paragraphs above the Lie
Factor ```` ```working ```` block (22.7 minus 20 = 2.7 ...), yet brought that block back without its
introduction ("See what it was doing ..." / "Work out the Lie Factor ..."). `validate.py` passed it.
That is text neither version said in that form, so B-22-5 was taken out of the list and recorded as
a hole (HOLES 12). If the tool is made to match its docstring, the two sentences can be added back
to `restore-lists/S58-R1-C22.txt` (they are named there in a comment).

## Gap by gap

### C19
- **B-19-1** hole, HOLES 1: the original names no scale for the third job (picking out against grey)
  either; Ex 1 asks for one.
- **B-19-2** hole, HOLES 2: ordered groups (Ex 2's age groups) are not covered in the original.
- **B-19-3** restored: "A colour scale shows values fairly when it is perceptually uniform ...",
  "Its lightness should also change in one direction only ...", "The rainbow scale fails both." and
  "Crameri, Shephard and Heron (2020) report ...". The reason the rainbow fails, needed for Ex 2.
- **B-19-4** restored in part: the Crameri sentence above gives the source. "Colour bar" and "heat
  map" are undefined in the original too: HOLES 3.
- **B-19-5** restored: "Wilke shows colours are harder to tell apart there, and harder still under
  colour-vision deficiency." The why behind thin lines, which Ex 2's Figure 5 needs.
- **B-19-6** restored in part: "A grey copy keeps only how light or dark each colour is." and "So two
  colours of the same lightness turn into the same grey ...". Lightness is now said in words.
  "Equally strong" and lightness against hue are not in the original: HOLES 4.

### C20
- **B-20-1** restored: "It then says what is shown, in whom, where and when; how many independent
  people or units were measured, written n; ..." and "In n, independent means separate people or
  units." n is named before the SE formula uses it.
- **B-20-2** hole, HOLES 5: the original's "A 95% CI is a range worked out from the sample so that,
  if the study were repeated many times, ..." fills it but raised the mean sentence length (see
  trials). Not restored.
- **B-20-3** hole, HOLES 6: the original also gives 4 SE for n = 3 and 2 SE for n of 10 or more, and
  nothing between.
- **B-20-4** hole, HOLES 7: "Cumming's Rule 8" and the per-person interval are as opaque in the
  original.
- **B-20-5** not a defect (artifact): placeholder width.
- **B-20-6** hole, HOLES 8: the P value and the asterisk convention are not taught in the original.

### C21
- **B-21-1** not a defect (artifact): placeholder count in Ex 3.
- **B-21-2** hole, HOLES 9: the original also gives right alignment and decimal-point alignment with
  no rule for which wins.
- **B-21-3** restored, in C22: rows 95 ("All women age 15-49 years ... 57.0") and the column note
  now come back in C22's illustration, so 57.0 reads as all women and 57.2 (C21's heading) as
  non-pregnant women.
- **B-21-4** hole, HOLES 10: litre and deci- are not taught in the original either.
- **B-21-5** hole, HOLES 11: no list of standard abbreviations in the original.

### C22
- **B-22-1** hole, HOLES 13: the original also says nine decisions and shows a ten-row sheet.
- **B-22-2** hole, HOLES 14: the original's step 5 renames the legend and its step 6 labels the
  rounds directly; the conflict with section 18 is the original's.
- **B-22-3** restored: "An image is saved either as a bitmap, a grid of coloured dots called pixels,
  or as a vector graphic ..." and "Never use a jpeg for a chart: Wilke says to avoid it for 'images
  containing line drawings or text'." The reason Ex 2's "jpeg, so the file is small" is wrong. Jpeg,
  png and pdf are never named as kinds of file in the original (part of HOLES 15).
- **B-22-4** not a defect (artifact): placeholder widths.
- **B-22-5** hole, HOLES 12: the first half is restorable but blocked by the tool conflict above; the
  second half (a rise of 29.2 to 31.1 against sampling variation) is not in the original.
- **B-22-6** restored in part: "The fact sheet counts a person as anaemic when it is below a cut-off
  for their group.", "Five of its rows are these.", the five quoted rows 92 and 95 to 98, "The four
  columns are NFHS-5 (2019-21) urban, rural and total, ..." (which also closes pass 1's dangling
  "Take the two totals for each group"), and "Each group has its own cut-off for haemoglobin, so the
  bars compare shares, not haemoglobin levels." The rows give the children's (11.0) and men's (13.0
  g/dl) cut-offs. The women's cut-offs are not in the original: HOLES 15.

### C23
- **B-23-1** hole, HOLES 16: the original also never shows the three drafts or a worked journey.
- **B-23-2** not a defect (artifact): placeholders.
- **B-23-3** restored in part: "Where you have only an example to work from, say the entry is
  modelled on it." "A fact sheet read online is not a journal article: it follows the chapter on
  titles on the Internet." raised the mean sentence length and was dropped; no format other than
  the journal article is shown in the original: HOLES 17.
- **B-23-4** hole, HOLES 18: no tool for "how sure you are" in the original.
- **B-23-5** restored: "NFHS-5's {{n:nfhs5_women_interviewed}} women are those it gathered
  information from, not the women weighed for this row." The reason the multiplication is wrong.
- **B-23-6** hole (error), HOLES 19: "Indian adults" for ages 15 to 49 is in the original.
- **B-23-7** hole, HOLES 20: the original never prints the finding's numbers either.

### Reader B's symbol list (as it touches C19 to C23)
- **n** (20): restored, B-20-1. Section 09 belongs to batch r2.
- **CI and "95%"**: hole, HOLES 5 (B-20-2).
- **"±" glossed once; "<" never glossed**: hole, HOLES 21.
- **"*" on a p value, and p**: hole, HOLES 8 (B-20-6).
- **g/dl**: hole, HOLES 10 (B-21-4).
- **SE and SEM, SEM defined only in an exercise**: hole, HOLES 22.
- **legend** (caption in 14 and 20, colour key in 18, 19, 22): restored in C20 ("To a journal, the
  figure legend is the caption ..." / "On the figure itself, a legend is the key to the colours.",
  which close pass 1's dangling "'Legend' means two things."). C22's legend against direct labels
  stays HOLES 14.
- **title** (caption opening in 20, text across the drawing in 22, table heading in 21): hole,
  HOLES 23.
- **decoration and ornament**: hole, HOLES 24 (C19's "ornament"; section 18's side is batch r3's).
- **value axis and side axis** (22, 20 Ex 3): hole, HOLES 25.
- **57.2 and 57.0**: restored, B-21-3.
- **"17%"** (a relative rise of 16.5%): not a defect. Working out that 17 is a relative rise is what
  C23's Ex 2 asks.
- **"adults" for 15-49**: hole, HOLES 19 (B-23-6).
- **two nine-step lists (22 and 23)**: not a defect. They are two named procedures, the nine
  decisions for a figure and the nine steps of a finding's journey. The ten-row sheet is B-22-1.
- **placeholder lines**: not a defect (artifact).
- log10, s, a, "4.6%", "ten" tasks, bars on a log axis: sections 15 and 17, other batches.

## Counts

Gaps B-19-* to B-23-* (30): restored 10 (five of them in part, with the rest in HOLES), hole 16,
not a defect 4 (all artifacts). Symbol list (14 items in these sections): restored 3, hole 9 (5 new,
4 duplicating a gap), not a defect 2; placeholder lines artifacts.
