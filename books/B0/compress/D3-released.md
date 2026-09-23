# D3 · Conditional probability through the two-way table

**Definition.** P(A given B), written P(A|B), is the count of people who are both A and B, divided by the
count of people who are B. P(A|B) and P(B|A) divide the same top count by two different totals
and are not generally equal.

Sensitivity is the share of people with the condition that the test catches, written P(test
positive given condition present).

Specificity is the share of people without the condition that the test correctly clears,
written P(test negative given condition absent).

The positive predictive value is the share of positive results that are right, written
P(condition present given test positive).

Prevalence is how many people in a group have the condition, written P(condition present),
with no test involved.

**In plain terms.** Given a positive result, how likely is the condition actually there?

A two-way table sorts the same people twice. Sort them one way down the columns, by whether they truly
have the thing you care about. Sort them the other way across the rows, by what a quick measurement says.
Where a row meets a column is a count of people who are both — that count is a cell.

Add up everything and you get the grand total.

A conditional probability is the same move with a chosen denominator. "Of those who test positive, how
many truly have it" divides by the row of positive results. "Of those who truly have it, how many test
positive" divides by the column of people who truly have it. Ask which one you have been handed before
you read anything into it.

The positive predictive value is the share of positive results that are right. Its mirror is the negative
predictive value, the share of negative results that are right. Prevalence — how many people in a group
have the condition — needs no test at all. It is a fact about the group before anyone is measured.

The positive predictive value belongs to the room the test is used in, not to the test by itself.

**Illustration.** Kiran, Harshitha and Bhargava measured 282 medical students in Mangaluru, including their
body-mass index and the circumference of the upper arm. This section uses only the 131 men.

The study's Table 3 reports a 31.3 centimetre arm cut-off for men, labelled "overweight,
body-mass index 25 or more". It gives sensitivity 86 per cent and specificity 74 per cent.
Table 2 gives 42 men with an index from 25 to 29.9, and 10 more at 30 or more.

```working
    42 plus 10 = 52
```

```working
    131 minus 52 = 79
```

Try to rebuild the table the label describes: 52 men against 79. Sensitivity of 86 per cent
should mean some whole number of the 52 caught by the tape. Try the nearest candidates.

```working
    44 divided by 52 = 0.8461...
    45 divided by 52 = 0.8653...
```

Rounded, 44 gives 85 per cent and 45 gives 87 per cent. Neither is 86. No whole number of 52
rounds to exactly 86 per cent. Try the 79 the same way, against the specificity of 74 per
cent.

```working
    58 divided by 79 = 0.7341...
    59 divided by 79 = 0.7468...
```

Neither is 74 either. The label's own group sizes, 52 and 79, cannot have produced the
paper's printed percentages.

This is a denominator question, the kind this whole section teaches. Somewhere else in Table
2 is a group of men that does divide back cleanly. Try the 42 men in the 25-to-29.9 band on
their own, against the other 89 men in the study.

```working
    131 minus 42 = 89
```

```working
    0.86 times 42 = 36.12
    36 divided by 42 = 0.8571...
```

Thirty-six of the 42 rounds to exactly 86 per cent.

```working
    0.74 times 89 = 65.86
    66 divided by 89 = 0.7415...
```

Sixty-six of the 89 rounds to exactly 74 per cent. Both round back to the printed figure.

On that rounding this row fits the 42 and not the 52.

The rest of each row and column follow by subtraction.

```working
    42 minus 36 = 6
    89 minus 66 = 23
    36 plus 23 = 59
    6 plus 66 = 72
```

```table
|  | in the 25-29.9 band | not in the band | total |
| arm 31.3 cm or more | 36 | 23 | 59 |
| arm under 31.3 cm | 6 | 66 | 72 |
| total | 42 | 89 | 131 |
```

This table is rebuilt, not printed by the paper in this form.

Take the row of men the tape flags — arm 31.3 centimetres or more — 59 of them in total.

```working
    36 divided by 59 = 0.6101...
```

About 61 per cent. This is the positive predictive value: of the men the arm measurement
flags, the share who are actually in the 25-to-29.9 band.

Now reverse the question. Take the column of men in the 25-to-29.9 band — 42 of them.

```working
    36 divided by 42 = 0.8571...
```

About 86 per cent. This second ratio is the sensitivity, and it is the number the paper
itself reports. P(in the band given arm 31.3 or more) is not P(arm 31.3 or more given in the
band).

Specificity is the share of the 89 men outside the band whom the measurement correctly
clears.

```working
    66 divided by 89 = 0.7415...
```

Prevalence is how many of the 131 men are in the band in the first place, no measurement
involved. Table 2 already gives it directly: 42 of 131.

```working
    42 divided by 131 = 0.3206...
```

About 32 per cent, among these 131 men.

Keep the same cut-off, the same 86 per cent sensitivity and the same 74 per cent specificity.
Apply them to a stated group instead: 1,000 young men in which one in five is in the band.

```working
    0.20 times 1,000 = 200
    1,000 minus 200 = 800
```

```working
    0.86 times 200 = 172
    0.74 times 800 = 592
```

```working
    200 minus 172 = 28
    800 minus 592 = 208
    172 plus 208 = 380
```

```table
|  | in the band | not in the band | total |
| arm 31.3 cm or more | 172 | 208 | 380 |
| arm under 31.3 cm | 28 | 592 | 620 |
| total | 200 | 800 | 1,000 |
```

```working
    172 divided by 380 = 0.4526...
```

About 45 per cent, against about 61 per cent among the medical students themselves.

**Where this picture breaks.** The 36-23-6-66 table is rebuilt, not measured. It was built by applying two rounded percentages to two
counts. Of the two group sizes tried, only one rounds back to both 86 and 74. Wherever you see a
sensitivity and a specificity with no counts behind them, run the same check before you trust which
group they describe.

The positive predictive value of 61 per cent describes these 131 medical students and nobody else.
Sensitivity and specificity stayed the same. Never quote a positive predictive value without saying
whose prevalence produced it.

Whether the measurement is worth taking in a clinic is a separate question.

**Must know points for you.**

- P(A given B) is not P(B given A). Sensitivity and the positive predictive value are built from the same top count. They divide it by different totals.
- Run the same test where the condition is common, and most positive results are right. Run it where the condition is rare, and most positive results are wrong.
- Before dividing anything, say out loud which row or column you are dividing by.
- Carrying sensitivity and specificity forward to a new group is itself an assumption. Say so whenever you do it.
- Divide back. Try every whole number of the stated group. A row's own label is not proof that it matches the count behind it.
- A headline that reports a test as some per cent "accurate" tells you nothing on its own. It names none of the sensitivity, the specificity or the positive predictive value. Ask which one was meant, then ask for the prevalence the third one needs.
- When two published figures for the same measurement disagree, check whether either one conflicts with something else printed alongside it. A shared total, or rows that must add up, can settle which figure the paper actually computed from. Do this before you assume the more prominent figure is correct.

**Exercise 1** (teaching). A health secretary has one page and wants an answer first. The briefing says an
arm-measurement test for a weight-related condition is "86 per cent accurate". Write the page.

**Exercise 2** (critique). The paper defines higher percent body fat (PBF) separately for men and women. It measures
body fat with a machine that passes a small current through the body. Its abstract states the cut-off in one place as
"(men: ≥20%; women: ≥30%)". Its own methods section and Table 2 both use "≥28" per cent for
women instead.

Say how you would check which of the two women's figures, 30 or 28 per cent, the paper's own
numbers are actually built on.

**1.** Of 100 people, 20 truly have a condition and 80 do not. A test is positive for 15 of the 20
who have it, and positive for 10 of the 80 who do not.

Build the two-way table, with row and column totals.

**2.** Using the table you built in the previous problem, work out P(test positive given condition
present) and P(condition present given test positive). Say which total each one divides by.

**3.** Using the same invented table, work out P(test negative given condition absent).

**4.** Still using the invented table, name which cell and which total each of these divides by:
sensitivity, specificity, and the positive predictive value. Give the value of each.

**5.** Kiran, Harshitha and Bhargava's 2022 study found that 52 of 131 men had a body-mass index of
25 or more. Work out this share as a percentage, and the percentage of men under 25.

**6.** Table 3 also reports a women's arm-circumference cut-off. Sensitivity is 88 per cent and
specificity 83 per cent, labelled "body-mass index 25 or more" the same way the men's row
was. Table 2 gives 41 women in the 25-to-29.9 band and 5 more at 30 or more. Together that
is 46 women carrying the label, out of 151 women in the study.

Try to reproduce 88 per cent from whole numbers of 46, and 83 per cent from whole numbers of
105 (151 minus 46). Say what the check shows.

**7.** Table 2's own women's row gives 41 women in the 25-to-29.9 band on its own, and 151 minus 41
women outside it. Use these two totals with the same 88 per cent sensitivity and 83 per cent
specificity, and work out the positive predictive value.

**8.** Using the men's rebuilt table — 36, 6, 23 and 66 — work out the negative predictive value.
Of the men the arm measurement clears, what share truly are outside the 25-to-29.9 band?

**9.** Here is a worked answer. Find the step that broke.

```working
    the abstract says 113 had abdominal obesity — the paper's label for a waist of 90
    centimetres or more in men and 80 or more in women
    113 divided by 282 = 0.4007...
    0.4007 rounds to 40.1 per cent, close enough to the abstract's own 38.7 per cent
    so 113 is confirmed as the paper's count for abdominal obesity
```

**10.** Here is a worked answer. Find the step that broke.

```working
    the abstract reports 186 (66%) had higher percent body fat (PBF), out of 282
    Table 2 reports the same measure as 185 (65.6%)
    185 divided by 282 = 0.6560..., which rounds to 66 per cent
    186 divided by 282 = 0.6596..., which also rounds to 66 per cent
    both numbers are consistent with their own printed percentages, so nothing in the paper
    can decide which count is right
```

**11.** Here is a worked answer. Find the step that broke.

```working
    Table 3 gives its 31.2 cm arm cut-off's sensitivity as 85 per cent for spotting the 41 men
    whose waist is 90 centimetres or more (Table 2)
    0.85 times 41 = 34.85
    so 34 of the 41 men were caught by the tape
    34 divided by 41 rounds to 85 per cent, matching the paper
```

**12.** A district officer says: "The tape correctly identified men in the 25-to-29.9 body-mass-index
band most of the time among these medical students. It will be right about as often wherever
I use it."

Suppose one in three men in the district were in the band. Decide what to compute, compute
it, and say what your answer does not establish.

**13.** A note says: "Neck circumference correctly identifies men with a body-mass index of 25 or
more, most of the time. It should replace body-mass index screening everywhere."

Table 3 gives a neck-circumference cut-off for men: sensitivity 81 per cent, specificity 71
per cent.

Decide what to compute, compute it, and say what the claim does not show.

