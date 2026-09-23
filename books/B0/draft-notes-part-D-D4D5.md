# Draft notes · Book 0 Part D, D4–D5 (concepts C27–C28)

Written by the Sonnet chat that drafted `B0-R0-C27.yml` (D4, *Variation: what differs and by how
much*) and `B0-R0-C28.yml` (D5, *Average and spread, and why the average is not the person*)
against `books/B0/INVENTORY-part-D.md` and `books/B0/READY-part-D.md`. D1–D3 and D6–D7 are being
drafted in parallel by other chats. Build run against all records currently present:
`python check/build.py --check` reports 0 blocking lines, and no blocking or warning line names
C27 or C28. (One unrelated blocking line names C29, from the D6–D7 batch's own file, and one
booklet-level warning is discussed below under "flag for reconciliation".)

## Drill-set counts, and why

| Concept | Count | Inventory's expectation | Why this count |
| --- | --- | --- | --- |
| C27 (D4) | 9 | 8–10 | D4's technique is thin on its own: relative frequency is division, already taught as A5's proportion, and range is a straight recall of C18. What earns the extra weight is the *habit* the section adds on top — check a table's count against its own printed percentage before trusting either — which needed its own mechanical, applied and diagnostic coverage. Landed at 9: three mechanical (relative frequency on bare counts, range on a bare list, the same-range-different-shape pair), three applied (three different slices of the real Kiran table, each varying which total is divided by which), two diagnostic (a wrong-denominator slip; a shape claim that only compares the two outer bands) and one transfer. A tenth problem would have repeated a move already drilled rather than adding a new failure mode. |
| C28 (D5) | 15 | 14–16 | D5 composes four sub-skills that each need their own mechanical drill before the real material arrives: mean, median, quartiles/interquartile range, and the standard deviation's five hand-steps (deviation, square, sum, divide by n−1, square root) with variance named as the stop before the last step. Five mechanical problems give each sub-skill its own bare-number pass (including a second, isolated one on the variance-then-root step, since the course owner specifically asked for variance to be seen as its own move). Five applied problems carry the real Kiran figures: the mean-median gap on body-mass index, the same gap on body fat, a real interquartile range that *does* pass the sanity check, a "how many standard deviations away" reading, and the women's combined band. Three diagnostic problems, because three distinct failures needed separate treatment: the classic divide-by-n slip, the real printed interquartile range that cannot contain its own median (the weight/height swap), and a directional logic error about which side of the mean most of a group sits on. Two transfer problems close it, both built on the section's own title claim. |

Both reach every band (mechanical, applied, diagnostic, transfer) per
`check/_build/check_report.md`'s practice-sets table.

## New glossary terms introduced

Per `claude.md` §7 note 7, `prose/GLOSSARY.md` was not written to. These go to the main thread for
reconciliation against `prose/glossary-inbox-D.md` and the D1–D3 / D6–D7 batches.

| Term | Plain words at first use | Concept |
| --- | --- | --- |
| distribution | "the set of values a quantity takes ... together with how often each value turns up" | B0-R0-C27 |
| frequency table | "lists each value, or each band of values, against the count of times it occurred" | B0-R0-C27 |
| relative frequency | "what fraction of the whole that value or band accounts for" — tied explicitly to A5's *proportion* | B0-R0-C27 |
| shape (of a distribution) | "bunched together near the middle... or thinning out slowly on one side and quickly on the other, which is a long tail" | B0-R0-C27 |
| mean | "their sum divided by how many there are" | B0-R0-C28 |
| median | "the middle value of the same set once it is ordered" | B0-R0-C28 |
| quartile | "one of three values that divide an ordered set into four equal-sized parts" | B0-R0-C28 |
| interquartile range | "the third quartile minus the first" — describes "the spread of the middle half of the values" | B0-R0-C28 |
| deviation | "that value minus the mean" | B0-R0-C28 |
| variance | "the average of the squared deviations" | B0-R0-C28 |
| standard deviation | "the square root of the variance" | B0-R0-C28 |

`range` is reused unchanged from C18, exactly as the inventory instructed, and is not a new row.

**Flag for reconciliation.** `B0-R0-C24` (D1) quotes the anchor's own phrase "the long-term
relative frequency of that outcome" inside its definition reference, but does not itself teach
*relative frequency* in plain words — it is quoted, not glossed. C27 is therefore the first place
in document order that actually defines the term for the reader. If the main thread reorders
sections or if D1 is later edited to gloss the phrase, check which one now comes first and drop
the duplicate.

## Figure proposals

The inventory names one candidate figure for each section. Both are drawn from numbers already in
the record's own prose, per the rule that a figure reads its numbers out of its record.

**D4 — dot plot with the range marked.** The inventory expects this to show "a distribution is a
thing the reader has to see once." Rather than draw it from the real Kiran table (which is grouped
into bands, not individual values — the record's own point is that a banded table cannot give you
a dot plot), I would draw it from the two bare six-number sets used in practice level 3, since
they carry the section's sharpest single idea: the same range, two different shapes.

```
set A: 10, 11, 12, 13, 14, 50   (range 40)
set B: 10, 20, 30, 40, 45, 50   (range 40)
```

Two rows of dots, one above the other, same horizontal scale, with the shared range of 40 marked
once underneath both. Set A shows five dots bunched together with one far outlier; set B shows six
dots spread almost evenly. This is the picture that the prose currently only argues in words.

**D5 — a skewed distribution with mean and median marked.** The inventory expects a distribution
with a tail to one side, so the reader watches the mean get dragged. The record's own bare-number
teaching example already has this shape built in:

```
values: 5, 8, 12, 15, 20, 40
mean = 16.6666666667 (about 16.7)
median = 13.5
```

A dot plot of these six values, with a vertical line at 13.5 labelled "median" and a second at
16.7 labelled "mean," would show the single high value (40) pulling the mean to the right of where
five of the six values actually sit. This is the section's own worked example, not an invented
one, so the numbers the figure would use are already checked by the record's own arithmetic.

Neither figure is added to either record's YAML. Per the batch instructions, that decision belongs
to the main thread.

## Places I was unsure

1. **"Between measurements" in D4 has no real source, and I kept it wordless rather than inventing
   numbers.** The inventory asks for three sources of difference, and Kiran 2022 has no
   repeated-measures data — every student was measured once. I described the third source in the
   illustration and simplified explanation only in words ("a fraction of a kilogram apart," no
   specific figures), rather than inventing a pair of readings, on the reasoning that an invented
   number dressed as a worked example is the same defect as an invented number in prose. This makes
   that one paragraph weaker as teaching than the other two sources, which do have real numbers
   behind them (the abdominal-obesity check, the frequency table). Worth the audit's judgement on
   whether that is the right trade, or whether a clearly-labelled hypothetical pair of numbers
   (explicitly flagged as invented, the way C21's transfer problems flag "the figures are made up
   for this problem") would have taught it better.

2. **The abdominal-obesity discrepancy (113 vs 109) is one of the paper's own six documented
   inconsistencies, and I want to flag which one I used so the audit can check for overlap.** The
   D1–D3 handover (`draft-notes-part-D-D1D3.md`) records that C26 used the neck-circumference
   specificity conflict for its diagnostic band. I used the abdominal-obesity count conflict
   (113 vs 109, both printed against "38.7%") for D4's lead illustration, on the reasoning that
   only 109/282 actually reduces to 38.7%, which makes it a genuine test of the relative-frequency
   technique this section teaches, not just a spotted typo. I have not read C29 or C30 and do not
   know whether either of the remaining four inconsistencies (women's cut-off, high-body-fat count,
   or the two neck-circumference specificity conflicts) is used again there.

3. **The one-sentence reason for dividing by n − 1 is a simplification, not a derivation, and I
   want the audit to check it does not overclaim.** The course owner's instruction was explicit:
   name it, do not derive it. I wrote: a sample's own mean is built from the same numbers used to
   measure the spread, so distances from it slightly understate the population's true spread, and
   dividing by a smaller number corrects the estimate back up. That is the standard informal
   account (Bessel's correction) and I believe it is directionally honest, but it is not a proof,
   and a specialist reader could reasonably want a sharper caveat than the one sentence gives.

4. **The "one standard deviation either side of the mean" sanity check in D5's illustration is my
   own construction, not something quoted from the anchor.** The anchor's own worked example (Rosa
   and Binh's supermarket wait times) teaches exactly this move, but I did not quote or cite it,
   because the record's own definition of standard deviation is enough to justify the check without
   borrowing the anchor's illustration. I would like the audit to confirm that a reader who has only
   read this record's own definition block can actually follow why "mean plus or minus one standard
   deviation" is a reasonable band to check a suspicious range against, since the record never states
   that rule as a named technique — it is used once, as a diagnostic move, without being taught as
   its own numbered step.

5. **Cross-batch acronym ordering.** `B0-R0-C26` (D3, not mine) uses "PBF" unexpanded before my own
   first use in C27. I added an expansion ("percent body fat (PBF)") in C27 regardless, so the
   acronym is expanded by the time any Part-D-only reader reaches D4 even if C26 is never fixed, but
   the build's acronym check still flags PBF as used-before-expanded at the booklet level, because
   C26 comes first in sequence and its usage is bare. This is not a defect in either C27 or C28 on
   its own; it is a document-order coordination issue between this batch and the D1–D3 batch. The
   fix belongs in C26.

## Nothing in the inventory looks wrong to me

I did not find a place where the inventory's brief for D4 or D5 was mistaken or needed correcting.
The one place I made a judgement call beyond the letter of the brief is item 2 above: the inventory
does not assign a specific one of the six real inconsistencies to D4, and I chose the
abdominal-obesity one because it is the cleanest test of relative frequency specifically, not
because the inventory pointed at it.
