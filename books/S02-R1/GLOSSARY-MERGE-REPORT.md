# S02-R1 glossary merge report

CONDUCTOR step 8. Checked against the final text as built by `python check/build.py --subject S02-R1`
(`check/_build/S02-R1.md`, 24 September 2026), not against the draft notes. Section n is record
`S02-R1-C0n` or `S02-R1-Cn`. No record was edited. No existing row of `prose/GLOSSARY.md` was changed;
new rows were inserted in their alphabetical places, as the file's header asks.

## 1. Rows added to `prose/GLOSSARY.md` (69)

antiderivative (C06); average value (of a rate) (C05); baseline (C01); coefficients (C11); constant
multiple rule (C03); constant rule (C03); continuous (random variable) (C13); counter (of a sum) (C01);
critical point (C09); d/dx (C03); data matrix (C11); definition (kind of equation) (C17); derivation
(C16); differential equation (C07); discrete (random variable) (C13); dot product (C10); e (the number)
(C04); energy density (C01); entry (of a vector or matrix) (C10); equilibrium (steady state) (C08);
expected value (expectation), E[X] (C14); first derivative test (C09); first-order (differential
equation) (C07); fitted equation (C17); forward step (Euler's method) (C07); fundamental theorem of
calculus (evaluation theorem) (C06); half-time (C04); identity (kind of equation) (C17); initial value
(C07); initial-value problem (C07); integrand (C05); law of large numbers (C14); least squares (C09);
length (of a vector) (C10); limit (C02); limits of integration (C05); local maximum, local minimum
(C09); matrix (C11); matrix product (C11); model assumption (C17); move (in a derivation) (C16);
natural logarithm (ln) (C04); net change theorem (C05); net signed area (C05); notebook entry (C17);
overall maximum, overall minimum (C09); power rule (C03); predictor (C12); probability density (C13);
probability distribution (C13); quadratic (C09); random variable (C13); rate constant (k) (C04);
redundant (column) (C12); scalar (C10); second derivative (C03); second derivative test (C09); set
point model (C08); settling point model (C08); sigma (Σ) (C01); size (of a matrix) (C11); stable,
unstable (equilibrium) (C08); subscript (C01); sum and difference rules (C03); time constant (τ) (C08);
vector (C10); weighted sum (C10); weights (of a weighted sum) (C10); where-clause (C01).

## 2. Draft-note proposals not added (stale, or named but not taught)

- **linearization** (b1, b3): not in the final text.
- **indefinite integral** (b2): not in the final text. C06 keeps only "plus C", which the
  antiderivative row now carries.
- **collinearity, rank** (b5, C12): neither word is in the final text. C12 says only that a nearly
  redundant column "is a harder problem" for the next rung.
- **chain rule, product rule** (b1, C03), **covariance** (C15): named, not taught; each is routed to a
  later book. No row, as for covariance in b6.
- **capital delta, small delta, rho, epsilon** (b1): C01's table says "each paper decides what its
  letters mean". Only Σ, which is an operation, got a row. ρ's meaning is carried by the new
  "energy density" row. See §3.6 for δ.
- **trapezium** (b2): used as a shape, not defined. No row.
- **"where" clause** (b1): added as "where-clause", the spelling C16 and C17 use (see §4.3).
- **parameter** (b1), **solution (of a differential equation)** (b3), **variance** and
  **independent** (b6): not added because a row for the word already exists. See §3.

## 3. One word, two senses (existing rows unchanged; each needs a between-rounds decision)

1. **parameter.** Row (`B0-R0-C29`): "a number that describes the population, if every member of it
   could be measured". C01: "a parameter, a fixed number", and "a number the paper keeps the same for
   every person and every interval" (model sense). C14 uses the Book 0 sense ("a parameter in the
   sense of Book 0, D6"). So S02 uses both senses. Fix: C01 needs a note that this is a second sense,
   distinct from Book 0's, or it should say "model constant".
2. **variance.** Row (`B0-R0-C28`): computed from data, dividing by the count or one less. C15: "the
   expected value of the squared deviation of X from E[X]" (of a random variable). C09 uses the data
   sense ("sample variance"). C15 does contrast the two senses in its Definition. The row needs a
   sense (2). The **standard deviation** row ("the square root of the variance") then fits both.
3. **independent.** Row (`B0-R0-C25`), of events: "finding out one of them happened tells you nothing
   new about the other". C14 and C15 extend it to random variables (see §4.1). The row needs a sense
   (2).
4. **solution.** Row "solution (of a system)" (`B0-R0-C17`): "the pair of values that satisfies both
   equations". C07: a solution of a differential equation is a whole curve, a function that makes the
   two sides agree at every moment. C07 has no Definition sentence for it; the gloss is in "In plain
   terms" only. Fix: C07 should state the sense and note that it differs from Book 0, C3.
5. **rule.** Row (`B0-R0-C43`) has only the legal sense. S02 uses "rule" throughout in the function
   sense (C01 "a rule called f"; C07 "a rule that gives the rate from the state"), and for
   differentiation rules (C03). This is inherited from `B0-R0-C18`'s function row. No S02 fix is
   needed; the row needs a mathematical sense added.
6. **delta.** Row (`B0-R0-C34`): Δ, "the change in". C01's table adds small delta δ, also said
   "delta", for Polidori's physical activity parameter. C01 does keep them apart. Optional fix: an
   aside in C01 that "delta" names two symbols.

## 4. Drift inside S02-R1

1. **independent (random variables) glossed twice.** C14: "knowing one tells you nothing about the
   other, the idea of Book 0, D2 carried to random variables". C15: "every event about one is
   independent ... of every event about the other". The sense is the same. Fix: C15 should point back
   to C14 and give its wording as the precise form.
2. **limit, two senses in one book.** C02: the number the averages close in on as h shrinks. C05
   uses that sense ("the integral is the limit of the sum") and in the next paragraph introduces
   "limits of integration", the start and end times. Both rows were added. Fix: C05 needs a note that
   these limits are the ends of the interval, not C02's limit.
3. **where-clause spelling.** C01 says "a clause beginning 'where'" and "its own 'where' clause". C16
   and C17 write "where-clause". Fix: C01 should name it "the where-clause" once.
4. **state never glossed.** C07's title, Definition and plain terms use "state" as a technical term
   ("a rule in its state"; "an initial value, the state at one stated time") without saying what a
   state is. It can only be inferred that the state is the weight. No row was added because no
   record teaches it. Fix: C07 should give it plain words, for example "the state: the value the
   quantity has now, here the weight".
5. **Used before the defining section.** Derivation is used in C09 (Exercise 1, practice 13) and
   defined in C16. Fitted is used in C11 ("They were fitted to ...") and defined in C17. Both are
   everyday uses, so this is minor.
6. **No inconsistency** found for weighted sum and weights (C10 and C12), rate constant and time
   constant (C04 and C08, τ = 1/k in both), or equilibrium (C08's Definition and plain terms).

## 5. Cross-book notes (existing rows, same sense, no fix required)

- **derivative** (`B0-R0-C21`), **integral** (`B0-R0-C22`), **average rate of change**, **exponential**,
  **stock**, **running total**: used in their row senses. C02 and C05 refer back to Book 0 explicitly.
- **mean** (`B0-R0-C28`): C14 says E[X] equals the ordinary mean only when every case is equally
  likely. This is consistent with the row.
- **distribution** (`B0-R0-C27`, data) and the new **probability distribution** (model): C13
  contrasts them explicitly.
- **identity (kind of equation)** is consistent with **accounting identity (for a body)**
  (`S01-R1-C05`).
- **basal metabolic rate (BMR)** (`S01-R1-C03`: "the energy spent lying at rest after a fast"): C17
  re-glosses it as "the energy a body spends lying awake and at rest, after an overnight fast". The
  sense is the same, but the words differ. Optional fix: C17 should reuse the row's words.
- **energy density**: S01-R1 §5.5 recorded it as unglossed in S01-R1-C02 practice. Its first gloss
  is now C01 of this book ("energy per kilogram"), so the S01 uses still precede the row.

## 6. Build

`python check/build.py --check`: 0 blocking, 130 warnings, the same as before the merge.
