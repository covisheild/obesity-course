# Draft notes · S02-R1 batch b4 (C09, C10, C11)

Drafter, Task 2 of `PIPELINE.md`, 2026-09-24. Nothing committed.

## Records written

- `check/records/S02/S02-R1-C09.yml`: Highest and lowest points: slope zero and curvature. 16 practice problems.
- `check/records/S02/S02-R1-C10.yml`: Vectors as data rows, and the weighted sum. 14 practice problems.
- `check/records/S02/S02-R1-C11.yml`: A matrix, and what multiplying by one does. 15 practice problems.

`python check/build.py --check`: blocking 0 for the whole build at hand-back (records 70), and no
warning on any of the three records. `python check/figures/draw.py --book S02-R1`: 24 figures, 0
problems. Every practice answer and every illustration value was recomputed in Python
(`/home/claude/scratch-b4/recompute.py`), and every quote was tested against the normalised
source text (`/home/claude/scratch-b4/q.py`).

## Why each drill-set size

- **C09, 16.** Several moves compose here: differentiate, solve f′ = 0, sort with f″ or with the
  sign of f′, check the ends of a range, then the Σ derivation of the mean, the curvature rule, and
  the difference between a turning point and an equilibrium. Each move needs its own rung on the
  ladder and one broken version.
- **C10, 14.** There are fewer moves (add, scale, dot, read a weight), but each has a trap: order,
  length, scaling twice, and "others held fixed". Several problems reverse the direction (find a
  missing gram count from a total).
- **C11, 15.** Size rules, the two readings of Ax, the matrix product and its order, scalar
  multiples, and y = Xb all need drilling. Three diagnostics cover the three commonest slips:
  the swapped (1, 65), multiplying entry by entry, and scaling only the slope.

## Sources: what is sourced, what is derived, what is unsourced

- **C09.** Definitions of local and overall extrema, critical points, both derivative tests and
  "extrema can sit at an end" are quoted from OpenStax Calculus Vol 1 §4.3 and §4.5. The mean and
  the deviation are quoted from Introductory Statistics 2e §2.5 and §2.7. **No held source states
  that the mean minimises Σ (x − m)², or the exact rule that a quadratic rises by half of f″ times
  h² from its level point.** Both are derived on the page, line by line (the record's note says
  so). The concept is `derivable`, so nothing depends on a source for them.
- **C10.** Vector entries, addition, scalar multiplication and "weights" are quoted from Austin
  §2.1. The multiply-and-add move is quoted from College Algebra 2e §7.5 (its row-by-column rule,
  flattened as "row i i of A A" in the held file; the note gives the page's wording). **The name
  "dot product" is in neither held section.** Austin defines it in a later chapter, which is not held.
  The factors 4.0/9.0/4.0 kcal/g and 17/37/17 kJ/g are from FAO FNP 77 §3.5.1. The alcohol factor
  7.0 kcal/g (practice only) comes from the same paragraph. The FSSAI factors 4/9/4 kcal/g are
  quoted from regulation 5(3)(e)(i) (compendium Version VIII, 09.09.2025). No Indian food
  composition table is held, so every food and gram figure is made up and says so.
- **C11.** The FAO/WHO/UNU Table 5.2 rows (men and women, 18–30 and 30–60) are quoted from block
  9 of the held file. The ≥ 60 rows, which extract as "³ 60", are not used. The ICMR-NIN 65.0 kg
  and 55.0 kg reference weights, the two 5% cuts and the "10 -12%" overestimate are quoted from the
  brief note. **ICMR-NIN's note does not say whether "another 5 %" makes a total factor of 0.90 or
  0.9025.** The record shows both (about 4 kcal/day apart at 65 kg) and says the note does not
  settle it. Nor does the note say whether "overestimate by 10 -12%" means a factor of 1/1.10 or
  0.90. Practice level 9 is built on exactly that and does not pick one. The note's BMR sentence
  about "DLW or HRM methods" is flagged wrong in the held file and is not used. The planned
  "Schofield matrix times (weight, 1)" uses the held Table 5.2, not the inventory's "not held".
- Chow & Hall 2008 and Hall 2008 equations: not used by this batch.

## Decisions a reviewer should know

- **"Dimension" is avoided.** Austin and College Algebra use "dimension(s)" for a vector's length
  and a matrix's size. `B0-R0-C11` has already glossed "dimension" as the kind of a quantity, so
  these records say **length** (vector) and **size** (matrix), and the reference notes say why.
- **"Entry"** for both vectors and matrices (College Algebra's word), not Austin's "component".
- **"Weights" vs body weight.** C10 says once that "weight" there means a multiplier and that the
  book writes "body weight" for the person. It also adds a teaching must-know on it. C11 names
  the weights of a formula **coefficients**, tied back to C10's weights in one sentence. The
  reason is that "weights" beside body weights in the Schofield rows would read as one word doing
  two jobs. C12's drafter also uses "weights" and "weighted sum", which is consistent.
- **Unicode superscripts in C09.** The build's notation step typesets `x^2` only when the base
  stands alone. `3x^2`, `4m^2` and `(c + h)^2` would put a raw caret on the page. So C09's
  reader text uses x², x³, (x − m)², kg² and so on. Figure `fit` strings keep `^` (they are not
  reader text). The renderer may want to learn a coefficient-attached base; the pattern is
  `_SUP` in `check/build.py`.
- **S01 records are named in words, not by ID**, because the brief limits `concept_deps` to
  earlier S02-R1 concepts ("Book 1 met the basal metabolic rate"). C09 lists `S02-R1-C08` as a
  dependency because it contrasts an extremum with an equilibrium. The inventory does not list
  it, but the section cannot draw that contrast without it.
- **One `illustration`, not `illustrations`.** Each record's illustration holds two or three
  worked cases in sequence: the trap first, then the payoff. `check/build.py` line ~828 checks
  only `illustration.analogy_breaks_when`, so a record using `illustrations:` alone would block.
  Worth a look by whoever owns the build.
- **Routing** (one line each, not taught). Likelihood, and a standard error from curvature, go to
  rung 2 of this subject (C09). The partial derivative is named and routed to rung 2 (C10).
  Fitting b in y = Xb goes to "the statistics books" (C11). Transpose is shown as "rows turned
  into columns" but not named.

## Figures

All drawn by `draw.py` from specs, and all looked at as images.

- `s02-r1-c09-cubic-critical-points.png`: x³ − 3x over −2..3, with the drawn curve (fit). It
  labels the local maximum 2, the local minimum −2 and the overall maximum 18 at the end.
- `s02-r1-c09-least-squares-valley.png`: S(m) at five candidate centres, with the drawn parabola
  0.40 + 5(m − 70.6)².
- `s02-r1-c10-energy-parts.png`: bars of 12, 81 and 60 kcal, the three terms of the dot product.
  It checks `sum(y) = 153`.
- `s02-r1-c11-schofield-columns.png`: the two columns of XC against body weight. Each line is
  checked by a `fit` with its equation's slope and intercept, not drawn separately. The side axis
  does not start at zero, and the caption says so.

No further figure is wanted.

## Glossary rows (proposed; not added to `prose/GLOSSARY.md`)

None of these terms is glossed there now. "Dimension" is glossed with another sense, hence
"length" and "size" below.

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| coefficients | the fixed numbers a formula multiplies by; the weights of a weighted sum | `S02-R1-C11` |
| critical point | an input where a function's slope is zero or does not exist: a candidate for a top or a bottom, not a guarantee | `S02-R1-C09` |
| data matrix | a matrix whose rows are cases, such as people, and whose columns are variables in a fixed order | `S02-R1-C11` |
| dot product | multiply the entries of two same-length vectors in matching positions, then add; written a · b | `S02-R1-C10` |
| entry (of a vector or matrix) | one number in the list or table, found by its position | `S02-R1-C10` |
| least squares | choosing a value by making the misses, each squared and then added up, as small as possible | `S02-R1-C09` |
| length (of a vector) | how many entries it has | `S02-R1-C10` |
| local maximum, local minimum | a value at least as high, or at least as low, as every value near it | `S02-R1-C09` |
| matrix | a rectangular table of numbers with the labels taken off, named by a capital letter | `S02-R1-C11` |
| matrix product | each row of the first matrix dotted with each column of the second; needs the first's columns to match the second's rows | `S02-R1-C11` |
| overall maximum, overall minimum | the largest, or smallest, value over a whole stated range of inputs; textbooks say absolute maximum and minimum | `S02-R1-C09` |
| quadratic | a function of the form px² + qx + r | `S02-R1-C09` |
| scalar | a single number, used to multiply every entry of a vector or a matrix | `S02-R1-C10` |
| second derivative test | at a level point, a positive second derivative means a minimum, a negative one a maximum, and zero decides nothing | `S02-R1-C09` |
| size (of a matrix) | rows by columns, written m × n and said "m by n" | `S02-R1-C11` |
| vector | an ordered list of numbers, one entry for each variable, written in round brackets and named by a lowercase letter | `S02-R1-C10` |
| weighted sum | numbers or vectors, each multiplied by its own number and then added; textbooks say linear combination | `S02-R1-C10` |
| weights (of a weighted sum) | the multipliers in a weighted sum, not body weight | `S02-R1-C10` |
