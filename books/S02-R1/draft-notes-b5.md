# Draft notes · S02-R1 batch b5 (C12, C13, C14)

Drafter: Opus 5.5, 24 Sep 2026. Brief: `books/S02-R1/DRAFT-BRIEF.md`. Nothing committed.

## Records written

| Record | Name | Practice | Figures |
| --- | --- | --- | --- |
| `check/records/S02/S02-R1-C12.yml` | A column that is a weighted sum of other columns | 14 (levels 1–10) | `s02-r1-c12-energy-weighted-sum.png`, `s02-r1-c12-tee-not-weighted-sum.png` |
| `check/records/S02/S02-R1-C13.yml` | A random variable and its distribution | 15 (levels 1–10) | `s02-r1-c13-village-distribution.png`, `s02-r1-c13-rounding-density.png` |
| `check/records/S02/S02-R1-C14.yml` | Expectation | 14 (levels 1–10) | `s02-r1-c14-surplus-balance.png`, `s02-r1-c14-week-expected.png` |

`python check/build.py --check`: blocking 0 across the book when last run, and no warning of any
kind against C12, C13 or C14. `python check/figures/draw.py --book S02-R1`: 24 figures, 0 problems.
Every practice and illustration answer was recomputed in Python
(`/home/claude/scratch-b5/recompute.py`); all agree. Every quote was machine-checked by the build
against its source file, and read by eye to confirm it carries the claim it is cited for.

## Sources, and anything unsourced

All references are to held files and are `opened: true`. Nothing is unsourced.

- **C12.** Austin §2.1 and §2.2 (weights, matrix times vector as a weighted sum of columns, the
  test as "is the linear system consistent"). FAO 77 §3.5.1 (the 4, 9, 4 factors; "carbohydrate
  is determined by difference, and thus includes fibre"). FAO/WHO/UNU 2004 glossary ("BMR times
  PAL is equal to TEE"). Hall 2012 (ES = EI − EO, for one practice problem). The inventory's
  planned anchors were Austin §2.2 and FAO 77; the last two are additions, both held and quoted.
- **C13 and C14.** OpenStax Introductory Statistics 2e §4.1–4.2 and OpenIntro 4e §3.1.5, §3.4 and
  §3.5 (both held since the intake, although the inventory marks them not held). Hall 2012 for the
  letter E as energy (notation-clash paragraph). FAO/WHO/UNU 2004 for PAL 1.40–2.40 (C13 level 10)
  and the 1.75 × 7.10 worked example (C14 level 4).
- **Derived, not quoted:** E[aX + b] = aE[X] + b (OpenIntro gives only aX + bY), and the
  outcome-by-outcome proof that E[X + Y] = E[X] + E[Y] needs no independence. OpenIntro's "always"
  carries the claim, and the record derives both from the floor.
- **Model assumptions, labelled in the text:** the flat density for a scale's rounding error is
  the record's own assumption. OpenIntro supplies only the rounding logic, and the text says so.
  All distributions and tables are made up and say so, except the FAO and Atwater figures.
- **Not used:** Chow & Hall 2008 and Hall 2008's equations. The inventory did not route either one
  to these concepts.

## Why each practice-set size

- **C12, 14.** The technique has several moves that compose: forming a weighted sum, a row that
  isolates one weight, elimination with two unknowns, the column of 1s, checking every leftover
  row, rows to spare, rounding, a product that fails the test, and the infinitely-many rewrite.
  Each move gets a mechanical problem and an applied or diagnostic one.
- **C13, 15.** It has two regimes, discrete sums and continuous areas (flat and triangular), plus
  the check of the two rules, ranges and complements, and the model-against-estimate distinction.
  That distinction is the concept's main trap, and it needs its own diagnostics.
- **C14, 14.** There is one core computation, then two linearity rules (the sum rule without
  independence is counter-intuitive), a reverse problem, scaling to a week, a fixed bias, sample
  mean against parameter, and the boundary at products and ratios (BMI).

## Things the conductor should know

1. **`illustrations` (plural) does not work in the build.** Its `numbers` items reject `quote`
   (schema), `check_quotes` reads only `illustration.numbers`, and the build blocks
   "illustration.analogy_breaks_when is empty" when only `illustrations` is present. I folded
   C12's two worked cases (the Atwater column, and TEE = BMR × PAL failing the test) into a single
   `illustration`. C04 (another batch) was hitting the same blocks when I last looked. Needs a
   build fix before the brief's advice to use `illustrations` can be followed.
2. **"parameter" clash.** `draft-notes-b1.md` proposes a glossary row "parameter: a number the
   model holds fixed while it runs" (C01). `prose/GLOSSARY.md` already has "parameter" from
   `B0-R0-C29` (a number describing the population). C14 uses the B0 sense and points to C29. Two
   senses of one word in one book needs a decision: number the senses, or rename one.
3. **Acronyms FAO, WHO, UNU** are expanded again in C12's illustration, because I could not rely
   on an earlier section's wording. If C01 already expands them, C12's expansion can go in the
   sequence read.
4. **EO against EE.** Hall 2012's equation is quoted with EO. C12 level 5 adds "which this book
   writes EE".
5. **Book 1 pointers.** C14 names `S01-R1-C04`, `C05` and `C07` in prose, and C12's exercise names
   no S01 record. The brief allows only S02-R1 ids in `concept_deps`, so none of these is listed
   there.
6. **Forward pointers.** C14's analogy says dependence matters "for the spread, in the next
   section" (C15). It is a pointer, not a dependence. Cut it if the sequence read objects.
7. **Two level-10 problems rest on interpretation**, which is flagged in the answers.
   - C13's reading of FAO/WHO/UNU's PAL range as about populations, not individuals: the answer
     only says the sentence speaks of populations and gives no distribution for individuals.
   - C12's "by difference" rule (100 minus water, protein, fat, ash): it is supplied by the
     problem as a table's own note and never attributed to FAO.

## Figures wanted that the tool cannot draw

- C13 rounding density: a **shaded strip** under the flat density from 0 to 0.02 kg. It is drawn
  now as a second step series outlining the strip.
- C14 surplus distribution: a **vertical marker at x = 70** (the expected value) under the label.
  At present the label floats above the bars. Also wanted: a wedge or triangle at the balance
  point, as in OpenIntro Figure 3.20.
- C12: none beyond what is drawn.

## Glossary rows (proposed; `prose/GLOSSARY.md` not edited)

Checked against the file. "distribution" (`B0-R0-C27`, data), "relative frequency", "sample
space", "outcome", "parameter" and "statistic" (`B0-R0-C29`), "mean", "systematic error" and "BMI"
are already glossed and used in their existing sense. "Probability distribution" is new and kept
distinct from B0's "distribution" of data. "Weighted sum", "weights" and "linear combination" are
C10's. They are left to that batch's rows.

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| collinearity | a column that is nearly, but not exactly, a weighted sum of other columns; named here, taught at rung 2 | `S02-R1-C12` |
| continuous (random variable) | can take any value in an interval, so any one exact value has probability 0 | `S02-R1-C13` |
| discrete (random variable) | the values it can take can be listed, one by one | `S02-R1-C13` |
| expected value (expectation), E[X] | each value times its probability, all added up; the long-run average; also written μ | `S02-R1-C14` |
| law of large numbers | repeat a chance process many times and the average of the results settles towards the expected value | `S02-R1-C14` |
| predictor | a column that a model uses to predict an outcome, with one weight for each | `S02-R1-C12` (unless C11 glosses it first) |
| probability density | a curve, never below zero, with total area 1 under it; the area over a range is the probability of that range; its height is probability per unit, not a probability | `S02-R1-C13` |
| probability distribution | every value a random variable can take, each paired with its probability; a model, where a frequency table is data | `S02-R1-C13` |
| random variable | a rule that gives a number to each outcome of a chance process; written with a capital letter, X | `S02-R1-C13` |
| rank | how many of a table's columns are not redundant; named here, taught at rung 2 | `S02-R1-C12` |
| redundant (column) | a column that is a weighted sum of other columns in the table, so it says nothing about any row that they do not | `S02-R1-C12` |
