# Book 0 · Part D concept inventory

Sections D1 to D7 of `check/book0/OUTLINE.md` — concepts `B0-R0-C24` to `B0-R0-C30`, sequence 24
to 30. Produced 23 September 2026 against frozen map `fc19c8bc-a216-4131-99fb-ebe3f19cec4a`, by
the method in the specification §5, adapted to Book 0 as Parts A to C were: Book 0 has no rung
outcomes of its own, so the terminal requirements are the outline's notes plus what the subject
rungs above Part D presuppose.

Written while the Part C chat runs its compression pass in parallel. Nothing here touches a Part C
file. See the end for which shared files Part D appends to.

---

## What makes Part D different, and it is the sourcing again — the other way round

Part B was hard to source because a unit is a decision somebody made. Part C needed no source
beyond its anchor, and its anchors were tables of contents: opened, never quoted, so every Part A
to C definition carries `claim_located: false`.

**Part D is the first Part whose anchor is held as text.** `sources/openstax_intro_stats_2e.txt`
holds ten sections of the textbook, so each definition can carry a `quote` the build checks. That
raises the bar for the drafters: the definition says what the book says, or the build blocks.

**And it is the first Part with a real dataset in it.** Every section of Part D computes with
numbers, and "real numbers, not invented ones, wherever a real one exists" has so far been met by
the National Food Security Act — which is a statute, not data. Probability, variation and sampling
need data. One open-access Indian paper is held whole, with its tables, and it carries almost
everything Part D wants to compute with:

> Kiran R, Harshitha, Bhargava M. *Mid-upper arm circumference and neck circumference to screen for
> overweight-obesity in young adults in South India.* Heliyon 2022;8:e12173.

282 medical students in Mangaluru. Weight, height, body-mass index, waist, arm and neck
circumference, and body fat by bioimpedance. Men and women tabulated separately. Sensitivity and
specificity for each cut-off. Means beside medians. A sample-size calculation. And — found by
reading it rather than assumed — **six places where the paper disagrees with itself**, listed in the
header of the source file. Those are real, reproducible diagnostic-band material of exactly the
kind §4 asks for: a reader can open the paper and find each one.

It is used as material to compute with, never as evidence about the world. Book 0 says nothing
about whether arm circumference is a good screen. It uses the paper's table to teach what a
screening table is.

---

## The terminal requirements, before regression

**1. The outline's own notes.** D3 "the table before the formula; carries most of S03 rung 1".
D7 "prerequisite for the whole of S08".

**2. What the subject rungs presuppose.**

- **S03 rung 1** — conditional probability, independence, Bayes' theorem; "compute and interpret a
  conditional probability, including the base-rate case that defeats most clinicians"; parameter
  against statistic against estimator. D1, D2, D3 and D6 discharge these.
- **S03 rung 2** — "the sampling distribution as the central object". D6 must leave the reader
  holding the idea that a sample's answer varies from sample to sample, and by how much, so that
  rung 2 has something to formalise.
- **S08 rung 1** — "every measurement contains error, and error is not the same as bias"; "random
  versus systematic error, illustrated on a weighing scale". D7 discharges this. It does the
  weighing scale and leaves the 24-hour recall to S08, because the recall needs dietary
  assessment, which Book 0 does not teach.
- **S02 rung 1** — "random variable, expectation and variance". D5 names *variance* as the square
  of the standard deviation. Random variable and expectation are left to S02, deliberately:
  Book 0 teaches the arithmetic, S02 the object.

**3. What earlier Parts leave owed.** A5 taught *proportion* ("a part out of the whole it came
from, never more than one"). A probability is a proportion looked at before the draw, and D1 must
say so in those words. C18 already taught *range* in its statistical sense and warned about the
clash; D4 uses it and must not re-teach it differently. C39 (Part F) holds *precision* in the
glossary as "how tightly a measurement pins the number down"; D7 must use those words and then
sharpen them against the VIM.

**4. A sequence trap.** Reading a table is taught in F1 (`B0-R0-C39`), which comes *after* Part D
in document order. D3 teaches a two-way table and may not lean on F1. It teaches the rows,
columns and totals it needs itself.

---

## The sections

All seven are `derivable`, anchored to `openstax_intro_stats_2e` with quotes. All seven are
quantitative. Drill-set sizes are expectations to test, not targets.

| § | Concept | Needs | Must cover, in one line | Drill set | Real material |
| --- | --- | --- | --- | --- | --- |
| D1 | `C24` What a probability is | A2, A3, A4, A5 | A number from 0 to 1 saying how often, in the long run, an outcome turns up; counting equally likely outcomes; the complement; odds as a different number from probability | 8–10 | NFSA s.3(2), "up to seventy-five per cent. of the rural population" |
| D2 | `C25` Counting outcomes; independence | D1, A2, A6 | Listing outcomes; multiply for *and* when events are independent; add for *or* when they cannot happen together; *at least one* through the complement; the independence assumption checked, never assumed | 12–14 | NFSA s.3(1): coverage is decided per household, so two people from one house are not independent |
| D3 | `C26` Conditional probability through the two-way table | D1, D2, A4, A5 | Build the table; divide by the row or column that matches the condition; P(A given B) is not P(B given A); sensitivity, specificity, positive predictive value; the same test on a different prevalence | 14–16 | Kiran 2022 Tables 2–3: arm circumference against body-mass index in 131 men |
| D4 | `C27` Variation: what differs and by how much | A5, A3, C18 | A distribution; frequency and relative frequency tables; range; shape — symmetric or with a long tail; three sources of difference: between people, within a person, between measurements | 8–10 | Kiran 2022 Table 2 as a frequency table |
| D5 | `C28` Average and spread, and why the average is not the person | D4, A6, A3 | Mean, median; which one a long tail moves; quartiles and the interquartile range; standard deviation computed by hand on a small set; variance named; a mean says nothing about any one person | 14–16 | Kiran 2022 Table 1: men's mean body-mass index below 25 while 52 of 131 are at 25 or over |
| D6 | `C29` Sampling: how a part can tell you about a whole | D5, D1, A6 | Population and sample; parameter and statistic; random against convenience samples; a sample's answer varies from sample to sample; that variation shrinks with the square root of the sample size; bias does not shrink at all | 10–12 | Kiran 2022: 282 volunteers from one college, planned on a 20 per cent prevalence, finding 34.8 |
| D7 | `C30` Random error and systematic error as different things | D6, D5, A3, B1 | Error is a measured value minus a true one; systematic error pushes every reading the same way and averaging does not remove it; random error scatters and averaging does; accuracy, trueness, precision and resolution as the VIM defines them | 10–12 | VIM3 entries; Kiran 2022's scale "with accuracy of 100 g", its single observer, and bioimpedance against the method it names as the gold standard |

### D1 · What a probability is

A probability is a proportion you work out *before* the draw. That sentence carries the whole
bridge from A5 and must be said. Then: the scale from 0 to 1 and the percentage form of it; the
long-run reading (the anchor's own "long-term relative frequency"); counting equally likely
outcomes; the complement, 1 minus p.

**Odds go here**, as a named trap and not as a technique. Book 0 has no other home for them, and
every case-control paper and every logistic regression the reader will meet reports odds. A reader
who has only ever met probability reads "odds of 0.25" as a one-in-four chance and is wrong. D1
teaches odds as p divided by 1 minus p, drills the conversion both ways, and stops.

The NFSA illustration: s.3(2) says coverage "shall extend up to seventy-five per cent. of the rural
population". Pick one rural person at random and the probability they are covered is *at most*
0.75. The words "up to" make it a ceiling, and "at random" is doing work the reader must see.

### D2 · Counting outcomes; independence

The move that composes: list, then multiply or add. Twelve to fourteen problems, because the moves
combine and the diagnostic band has two distinct errors to carry — adding when you should multiply,
and multiplying when the events are not independent.

**Independence is taught as a check, not a label.** Two events are independent when knowing one
tells you nothing about the other. In D2 that is tested by counting: does P(A and B) equal P(A)
times P(B)? D3 then restates it with a condition, which is where the anchor defines it.

The NFSA case is the trap, and it is real. Coverage under s.3(1) is decided *per eligible
household*. Pick two rural people at random from different households and the chance both are
covered is at most 0.75 times 0.75. Pick two from the same household and it is at most 0.75, not
0.5625, because if one is covered the other is. Nothing in the arithmetic warns you.

### D3 · Conditional probability through the two-way table — the section the Part is built to reach

The outline's note is the design: the table first, the formula after, and the formula written
once, as a compression of what the reader has already done.

The sequence:

1. **Build the table.** Two ways of sorting the same people, rows one way and columns the other,
   with totals. Taught from nothing, since F1 comes later.
2. **Condition means: change the denominator.** "Of those who…" picks a row or a column, and that
   row's total goes under the line. A4 already taught that a percentage is only as good as its
   denominator; this is the same idea with a name.
3. **Reverse it.** P(positive, given overweight) is not P(overweight, given positive). The two
   share a top and have different bottoms.
4. **Name the screening words.** Sensitivity, specificity, positive predictive value, prevalence —
   each as "which cell over which total".
5. **Move the prevalence.** The same test, the same sensitivity and specificity, on a population
   where the condition is rarer. The positive predictive value falls, and the reader computes why.

The real table, from Kiran 2022. In men, 52 of 131 had a body-mass index of 25 or more (Table 2:
42 overweight plus 10 obese). At an arm circumference of 31.3 cm the paper reports sensitivity 86%
and specificity 74% (Table 3). Rebuilt to whole people:

```table
                        index 25 or more   under 25   total
arm 31.3 cm or more     45                 21         66
arm under 31.3 cm       7                  58         65
total                   52                 79         131
```

Positive predictive value in this room: 45 of 66, about 68%. Now apply the same two percentages to
1,000 young men where one in five has an index of 25 or more — the paper's own planning figure,
taken from NFHS-4 — and it falls to 172 of 380, about 45%. **Same tape, same cut-off, and a positive
result is right less than half the time.** That is the base-rate case S03 names, arrived at by
arithmetic the reader has already done twice.

**One boundary the rebuild must state.** Sensitivity and specificity were printed rounded to whole
percentages, so the counts are rebuilt to the nearest person and two of them are not unique. The
illustration says so. It is a real lesson in its own right: you cannot always get the counts back
from a rounded percentage, and a table rebuilt from one is an estimate of the table.

Bayes' theorem is named at the end, once, as the formula that does what the table just did. It is
not taught as a formula. S03 rung 1 owns that.

### D4 · Variation: what differs and by how much

This section is about the *spread of values*, before any number summarises it. A distribution is
the list of values and how often each turns up. Kiran 2022 Table 2 is a real frequency table — 282
students sorted into four body-mass-index bands — and relative frequency is A5's proportion again.

Three sources of difference, which D7 depends on and nothing before it names:

- **between people** — two students differ;
- **within a person** — one student differs from morning to evening;
- **between measurements** — the same student, the same moment, two readings.

A reader who cannot say which of the three a spread comes from cannot reason about error at all.
That is the section's must-know core.

Range stays as C18 taught it. Shape is taught in words — bunched in the middle, or with a long
tail to one side — and drawn. Histograms and dot plots are the figure, not a technique to drill.

### D5 · Average and spread, and why the average is not the person

The mean and the median, each computed by hand; which one a long tail drags; quartiles and the
interquartile range; the standard deviation, computed step by step on five or six numbers — each
value's distance from the mean, squared, averaged, square-rooted — and variance named as the step
before the square root.

**The sample standard deviation divides by n minus 1.** The anchor does, and so will every paper.
D5 shows the step and says in one sentence why it exists, without deriving it. A reader who
divides by n will get a slightly different answer from every paper they check, and should know
that is not their error.

The real case that gives the section its title. Kiran 2022 Table 1: men's mean body-mass index is
24.2 kg/m², under 25. Table 2: 52 of those same 131 men — two in five — are at 25 or over. **The
average of the group is under the line, and two in five of the people in it are above it.** Men's
body fat: mean 22.1, median 20.3. The mean is higher, so the tail is on the high side.

And a real diagnostic problem: Table 1 prints the men's weight as a median of 70.9 kg with an
interquartile range of 167.7 to 177.8 — which cannot contain its own median. The weight and height
rows have their ranges swapped. A reader who knows what an interquartile range is sees it in five
seconds; one who does not reads straight past it, as the paper's reviewers did.

### D6 · Sampling: how a part can tell you about a whole

Population, sample, parameter, statistic — with S03's three-way distinction in mind, so *estimate*
is named here. Random sampling as every member having an equal chance, and the convenience sample
as the thing it is contrasted with. Sampling variation: draw again and you get a different answer.

**The square-root law, stated and shown, not derived.** The spread of a sample's average is the
spread of the individuals divided by the square root of the sample size. So four times the sample
halves the spread. The anchor states it in one plain sentence (s.7.1), which is quoted. The section
shows it with a figure rather than a derivation.

**Then the half that matters more: size fixes random error and does nothing for bias.** A bigger
convenience sample is a more confident wrong answer. That is where D6 hands to D7.

The real case: the paper planned 282 students on an expected 20 per cent from NFHS-4. It found 98
of 282 at a body-mass index of 25 or more — 34.8 per cent. The transfer problem hands the reader
the sentence "medical students are far more overweight than India's young adults" and asks what the
sample can and cannot say. Volunteers, from one college, answering an invitation. Standard error
beyond naming it, confidence intervals and the normal curve are S03's, and D6 stops short of them.

### D7 · Random error and systematic error as different things

Error is the measured value minus the true value. The VIM's own definition (2.16) and its two parts
— systematic error "remains constant or varies in a predictable manner"; random error "varies in an
unpredictable manner" — are quoted, because they are what the words mean in every metrology and
epidemiology text the reader will open.

The weighing scale, as S08 rung 1 asks. A scale that reads 0.5 kg with nothing on it — the VIM's
*zero error* — adds 0.5 kg to everyone. Average twenty readings and the half-kilogram is still
there. A scale whose reading wobbles by a few hundred grams averages towards the right answer.
Stated conditions, marked as such; there is no real scale in the sources.

The vocabulary that most Indian papers get wrong, and Kiran 2022 does in its methods: "Weight and
height were recorded with accuracy of 100 g and 0.1 cm". That is **resolution** (VIM 4.14), the
smallest step the display can show. A scale can show 100 g steps and be a kilogram out.

Accuracy, trueness and precision are taught as the VIM defines them. Precision is introduced in
the glossary's existing words — how tightly a measurement pins the number down — and then made
exact: how closely repeated readings agree with each other, which says nothing about whether they
agree with the truth.

**Where D7 stops.** Classical and Berkson error, attenuation, differential error — all S08 rung 2.
The single observer in the paper is where D7 ends: one person measuring everyone removes the
differences between observers, and it also means that observer's own habit, if they have one,
reaches every reading. Nothing in the data can show it.

---

## Figures

The bar is unchanged. Candidates, for the main thread to decide once the records exist:

- **D4** — a dot plot of one small set of values, with the range marked. Probably earns its place:
  "a distribution" is a thing the reader has to see once.
- **D5** — a distribution with a tail to one side and the mean and median marked on it, so the
  reader watches the mean get dragged. Earns it.
- **D6** — sample averages from many samples of 10 against many samples of 40, drawn from one
  stated population, showing the second spread at half the first. Earns it: it is the square-root
  law as a picture, and the section explicitly does not derive it. Must be drawn from a seeded draw
  whose numbers are written into the record, per the rule that a figure reads its numbers out of
  its record.
- **D7** — two scales, twenty readings each, against the true weight: one tight and shifted, one
  centred and wide. Earns it. It is the section.
- **D3** — none. The table *is* the picture, and it is a table.

Four at most, which is inside the 6–10 a Part budget.

---

## Dependencies, declared

| Section | Needs | Why |
| --- | --- | --- |
| D1 | A2, A3, A4, A5 | A probability is a fraction, a decimal, a percentage and a proportion |
| D2 | D1, A2, A6 | Multiplying probabilities is multiplying fractions; listing outcomes of n coin tosses is 2 to the power n |
| D3 | D1, D2, A4, A5 | A conditional is a proportion with a chosen denominator |
| D4 | A3, A5, C18 | Relative frequency is a proportion; range as C18 taught it |
| D5 | D4, A3, A6 | The standard deviation takes a square root; a mean is rounded to what the data can carry |
| D6 | D1, D5, A6 | The square-root law; a sample average is D5's mean |
| D7 | D5, D6, A3, B1 | A measurement is a number and a unit; averaging is D5; bias not shrinking with size is D6 |

## Bridges to record in `provenance.bridge_ref`

| Subject rung presupposition | Discharged by |
| --- | --- |
| S03 r1 — conditional probability, the base-rate case | D3 |
| S03 r1 — independence | D2, D3 |
| S03 r1 — parameter, statistic, estimate | D6 |
| S03 r2 — a sampling distribution, as something the reader has seen | D6 |
| S08 r1 — error is not bias; random against systematic on a weighing scale | D7 |
| S02 r1 — variance as a quantity | D5 (named, computed) |

## Glossary terms Part D will introduce

Expected, to be reconciled once the batches report back: probability, outcome, complement, odds,
independent, conditional probability, two-way table, sensitivity, specificity, positive predictive
value, prevalence, distribution, frequency, relative frequency, mean, median, quartile,
interquartile range, standard deviation, variance, population, sample, parameter, statistic,
random sample, sampling variation, bias, measurement error, systematic error, random error,
accuracy, trueness, resolution.

Already held and to be used in their recorded words: proportion, rate, ratio, denominator,
precision, range (C18).

Because the Part C chat is running in parallel, these go to `prose/glossary-inbox-D.md`, not
`prose/GLOSSARY.md`.

---

## Risks specific to this Part

- **Model knowledge dressed as a quote.** Statistics is the subject a drafting model knows best,
  which is exactly when §7b bites. Every definition quotes the held anchor or the build blocks.
- **Rebuilt counts presented as the paper's counts.** D3's table is rebuilt from rounded
  percentages. It must say so in the illustration and in `analogy_breaks_when`.
- **The paper as evidence.** No record may say what arm circumference *is good for*. The paper is
  material, and §3's empirical treatment would apply the moment a record leaned on its findings.
- **§9 on weight.** A Part about "overweight" counts in real tables is where people-first language
  slips. "52 men with an index of 25 or more", never "52 overweight men" in the prose. The paper's
  own category labels may be quoted as labels.
- **Two meanings of *bias*.** Measurement bias (VIM 2.18) and sampling bias (the anchor, s.1.2) are
  both "systematic", and D6 meets one before D7 names the other. The glossary row must cover both
  or D7 must say plainly that it is the same word for the same shape of problem.
- **Sensitivity collides.** VIM 4.12 has "sensitivity of a measuring system", a different thing.
  Not held and not needed; D3's sense is the only one taught.

## Shared files Part D touches, and how

The Part C chat is mid-flight, so Part D writes only its own files and appends to shared ones,
each addition in a clearly headed block at the end so a merge is mechanical:

| File | What Part D does |
| --- | --- |
| `check/records/B0/B0-R0-C24.yml` … `C30.yml` | new files |
| `books/B0/*-part-D*.md` | new files |
| `sources/*.txt` (three) | new files |
| `sources/INDEX.yml`, `sources/SOURCES.md`, `check/references/library.bib` | append a Part D block at the end |
| `check/figures/draw.py` | append Part D functions at the end, if figures are drawn |
| `prose/glossary-inbox-D.md` | new file, for Harsh to merge |
| `claude.md`, `PIPELINE.md`, `check/build.py`, `prose/GLOSSARY.md` | **not touched** |
