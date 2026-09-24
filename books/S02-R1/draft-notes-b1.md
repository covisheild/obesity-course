# Draft notes · S02-R1 · batch b1 (C01–C03)

Task 2 of `PIPELINE.md`, per `books/S02-R1/DRAFT-BRIEF.md`. Not committed.

## Records written

- `check/records/S02/S02-R1-C01.yml`: Reading the symbols in a methods section (11 practice problems, 1 exercise with skill_ref S02-R1-K01, 1 figure)
- `check/records/S02/S02-R1-C02.yml`: The derivative: the rate at an instant, computed (12 practice, 1 exercise with K01, 2 figures)
- `check/records/S02/S02-R1-C03.yml`: The few rules that do the differentiating (16 practice, 1 teaching exercise, 2 figures)

Build: `python check/build.py --check` shows 0 blocking for C01–C03. One warning remains: in C02, exercise 1 prompt, a 26-word sentence that is a verbatim Polidori quote, so it is not shortened. `python check/figures/draw.py --book S02-R1` draws all five b1 figures with 0 problems. I looked at each PNG. Every practice and illustration number was recomputed in Python (`/home/claude/scratch-b1/verify.py`, 111 checks, 0 failures). Every quote in the definition references and in `illustration.numbers` passes the build's check. Every quoted phrase in reader prose was also checked against `sources/` by script (`/home/claude/scratch-b1/quotes.py`): all source quotes were found. Acronyms are expanded before first use across the three records in order (checked with `build.acronym_defects`).

## Practice-set sizes: why each number

- **C01, 11.** Five moves, each drilled once or twice with a reversal: reading a subscript, writing Σ out and back, a unit worked out from the terms beside it, the "where" clause, and a unit hidden inside a term. Fewer would leave one move undrilled. More would repeat the Σ drill.
- **C02, 12.** One technique (shrink h, from both sides), plus its algebra, its notation and unit, its sign, rate × time, and the noisy-data limit. The limit needs its own diagnostic and transfer problems.
- **C03, 16.** Four rules that compose, the second derivative, and two traps that must each be broken once: a product, and a constant base raised to a varying power. Applied problems use three real slopes (Hall & Guo, Table 5.2, PAL × Table 5.2). The hardest concept of the three, so the largest set.

## Sources, and anything unsourced or unsure

- All three are `derivable`. Every reference is opened and its passage located in a held file (`opened: true`, `claim_located: true`). Hall 2012, Hall & Guo 2017 and Polidori 2016 are off-type (`primary`) with quotes. The chain rule is only **named** in C03; OpenStax §3.6 is not held, so no claim about it is quoted, and it is never used.
- **Not used, as the brief requires:** the Hall 2008 and Chow & Hall 2008 equations. C01 uses Hall 2008's *prose* definition "ρF = 39.5 MJ/kg" and ΔF only. The product ρF × ΔF in C01 practice 5 is built from the definitions (energy per kg times kg). It is not presented as Hall's equation. The equation taught in C01 is Polidori's Equation 1 (held as MathML), with Equation 4 in the exercise.
- **Polidori's β and α** are not defined in the held text. C01 tells the reader to search the Methods for β and to write "not found" if they cannot find it. It never claims the paper leaves β undefined. **UGE** is not expanded next to Equation 1 in the held text. The expansion is taken from the abstract's words "increases urinary glucose excretion" and presented that way.
- **Polidori's "t = (N−1)*T"**: the file has the markdown-escaped `\*`, and the file's NOTE says the XML reads `*`. The C01 practice 6 prompt prints `*`.
- **Hall 2012's ES**: the paper uses ES for the stores and, in the equation, for their rate of change. C01 teaches this switch as the lead failure. **Decision for the conductor:** this book writes ES for the store and dES/dt for its rate, so Hall's equation reads dES/dt = EI − EE. The brief says "ES as in Hall 2012", which could be read either way. C04–C17 drafters (C05 in particular, ∫(EI − EE) dt) should use the same reading.
- **EE vs Hall's EO**: C01 says outright that they are one quantity. The book uses EE throughout.
- C02 builds its short-interval failure on made-up daily weighings, labelled as made up. The only real anchors are Hall 2012's short-term water warning, Hall 2008's 39.5 MJ/kg, FAO's 8.26 MJ/day and Polidori's 52-day interval.
- The C03 note that dTEE/dW = 1.75 × 15.057 ≈ 26.35 falls inside Hall & Guo's 20–30 is arithmetic only. The answer says it confirms neither figure.

## Notation this batch introduced (for the other batches to match)

- **Subscripts that count** are written after an underscore: BW_i, BW_0, EI_i. **Label subscripts** go on the line: EI, EE, ES.
- **Σ on one line**: `Σ[i = 1 to 7] (EI_i − EE_i)`, with the counter and its range in square brackets.
- **d/dx**, said "dee by dee x", is introduced in C03. f′(a) is said "f prime of a". The second derivative is written f″ or d^2y/dx^2.
- **Limit** is introduced in C02 as the number the averages close in on, with "lim with h → 0" named once.

## Build and renderer defects found (not fixed; shared files)

1. **`illustrations:` (the list) blocks.** `check/build.py` around line 829 requires `illustration.analogy_breaks_when`, so a record with only `illustrations` blocks. The schema also forbids `quote` in `illustrations[].numbers`, and `check_quotes` reads only `illustration.numbers`. b1 therefore uses one `illustration` whose body has three parts in sequence. C04 and C12 were blocking on the same defect when I checked.
2. **Bar charts clip negative values.** `draw.py` calls `ax.set_ylim(bottom=0)` for every bar chart, so the negative days vanished from C01's first draft. C01 now uses `scatter` with `value_labels`. Signed bars need a zero baseline, not a zero floor.
3. **Superscripts miss a coefficient glued to a letter.** `_SUP` in `build.py` leaves `5t^2`, `3x^2` and `(3 + h)^2` as raw carets. It also leaves a letter exponent, `x^n` or `2^t`. b1 writes `5 t^2` with a space, and `x^(n)` and `2^(t)` in brackets, and multiplies brackets out rather than squaring them. Worth widening the pattern once. Other S02 drafters will hit this.
4. The arithmetic check takes its tolerance from the side with the fewest decimals, so `2 divided by 7 = 0.2857` blocks. b1 writes "is about" for rounded divisions of whole numbers.

## Figures

Drawn: `s02-r1-c01-sigma-week.png` (Σ's seven signed terms), `s02-r1-c02-settling.png` (average rate against step h on the line 20 + 5h), `s02-r1-c02-weighings.png` (15 made-up weighings), `s02-r1-c03-weight-curve.png` (W(t)) and `s02-r1-c03-rate-line.png` (W′(t)).

Wanted, if the figure planner extends the tool:

- **C02:** the curve S(t) = 5t² for t from 1 to 3, with three chords from t = 2 (slopes 25, 20.5, 20.05) and the tangent at t = 2 (slope 20, the line 20t − 20). This needs lines drawn over their own x ranges.
- **C03:** W(t) and W′(t) in two stacked panels sharing the day axis, so the falling curve and its below-zero, rising rate read together.
- **C01:** the week's terms as signed bars from a zero baseline (defect 2).

## Glossary rows (proposed; not added to `prose/GLOSSARY.md`)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| baseline (value) | the value at the start, before anything changed; written with a subscript 0 | `S02-R1-C01` |
| capital delta (Δ), small delta (δ) | two different symbols: Δ means "the change in" whatever follows; δ is whatever the paper says it is | `S02-R1-C01` |
| chain rule | the rule for the derivative of a rule applied to the output of another rule; named here, taught at rung 2 | `S02-R1-C03` |
| constant multiple rule | a number multiplying a function stays where it is; take the derivative, then multiply | `S02-R1-C03` |
| constant rule | a constant has derivative zero | `S02-R1-C03` |
| counter (of a sum) | the letter under the Σ that keeps track of which term you are on; it does not appear in the answer | `S02-R1-C01` |
| d/dx | "dee by dee x": the derivative with respect to x of what follows | `S02-R1-C03` |
| epsilon (ε) | a Greek letter, said "ep-sih-lon"; the paper says what it stands for | `S02-R1-C01` |
| f prime (f′) | the derivative of f; f′(a) is its value at the input a | `S02-R1-C02` |
| limit | the number the averages close in on as the step h shrinks towards zero, without h ever being zero | `S02-R1-C02` |
| linearization | a straight-line stand-in for a curved model, close only for small changes | `S02-R1-C01` |
| parameter | a number the model holds fixed while it runs | `S02-R1-C01` |
| power rule | for x to a whole number n, bring the n down in front and take one off the power | `S02-R1-C03` |
| product rule | the rule for the derivative of a product, which is not the product of the derivatives; named here, taught at rung 2 | `S02-R1-C03` |
| rho (ρ) | a Greek letter, said "roe"; in these papers an energy density, energy per kilogram | `S02-R1-C01` |
| second derivative | the rate of change of the rate; its sign says whether the rate is rising or falling | `S02-R1-C03` |
| sigma (Σ) | add up: put each value of the counter into what follows, and add the results | `S02-R1-C01` |
| subscript | a small letter or number set low after a symbol; part of its name, and never a multiplication | `S02-R1-C01` |
| sum rule | take each term's derivative on its own, then add | `S02-R1-C03` |
| "where" clause | the sentence near an equation that says in words what each symbol stands for | `S02-R1-C01` |

The existing "rule" row (`B0-R0-C43`) has the legal sense. The rule names above are compound terms in the mathematical sense and do not change that row. The existing "derivative", "chord", "tangent", "instantaneous rate", "delta", "energy intake" and "energy expenditure" rows are used in their glossed senses.
