# S02-R1 step 5c: restore decisions, batch a (C01 to C09)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (Reader A), and
`<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml` for C01 to C09. The restore lists
are in `restore-lists/S02-R1-C0n.txt`, and each restored line is commented with the gap it
closes. The outputs are `S02-R1-C0n-final-prose.yml`, built by `check/compress/restore.py` and
checked by `check/compress/validate.py`. The tools were not changed, and no record was edited.

Key: **restored** means original sentences were put back because they let the reader do the
thing. **hole** means it is not closable here, and it is written up for the fixer in
`HOLES-a.md` (a restored gap with a part the original also leaves open has that part there too,
marked "residual"). **not a defect** means nothing to do.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → cut → final | Validate |
|---|---|---|---|---|---|---|
| C01 | 2658 | 1404 | 1609 | +205 | 11.55 → 11.46 → 11.27 | OK |
| C02 | 1757 | 1029 | 1157 | +128 | 11.43 → 11.01 → 11.22 | **FAIL** (tool conflict) |
| C03 | 1571 | 903 | 1036 | +133 | 11.54 → 11.06 → 11.36 | **FAIL** (tool conflict) |
| C04 | 2226 | 1170 | 1451 | +281 | 13.30 → 13.07 → 13.28 | OK |
| C05 | 1822 | 960 | 986 | +26 | 12.67 → 12.01 → 12.04 | OK |
| C06 | 1752 | 780 | 838 | +58 | 11.59 → 11.51 → 11.39 | OK |
| C07 | 2368 | 1321 | 1551 | +230 | 12.55 → 11.80 → 12.24 | OK |
| C08 | 2358 | 1365 | 1385 | +20 | 12.62 → 12.47 → 12.55 | OK |
| C09 | 2831 | 1646 | 1670 | +24 | 13.49 → 12.94 → 13.04 | OK |
| **Total** | 19343 | 10578 | 11683 | +1105 | | 7 OK, 2 FAIL |

C01's +205 includes the five sentences restored for A-C02-1, which C02 relies on but which sit in
C01. `python check/build.py --check` / `--subject S02-R1` was not run. It needs the final text
written back into the records, and this step's brief rules that out.

## Tool conflict (C02, C03): needs the conductor's decision

This is the same conflict as S01-R1 C02 and C07. In two places the pass-1 cut kept only part of
what `build._sentences` counts as one sentence. The splitter does not break before a sentence
that opens in lower case:

- C02 `simplified_explanation`: "Read the paper's equation again in these terms. dES/dt is the
  rate of change of stored energy, in kilocalories a day." The cut kept the part from "dES/dt".
- C03 `simplified_explanation`: "First, a symbol. d/dx, said "dee by dee x", means ...". The cut
  kept the part from "d/dx".

`restore.py` can bring back only the whole unit. `validate.py` then reports the cut's fragment as
"kept by the cut, missing after restore", although its text is in the final file. An empty list
fails in the same way, because the fragment is dropped. No list can pass. Each final file
therefore carries the whole unit, which adds 8 words (C02) and 3 words (C03) that no gap asked
for. The list lines are marked `TOOL CONFLICT`. Both sections pass every other check. The fix
belongs to the cut (re-cut on the splitter's boundaries) or to the tools (agree on the
boundary). The tools were not touched.

## Restores dropped because of the mean-sentence rule

`validate.py` fails a file whose mean sentence is longer than the original's. For four gaps, the
original sentence that closes the gap is long enough to break that rule. As in S01-R1 C02-G3,
these became holes, and each is written up with the exact sentence that would close it:

- A-C06-3 (34 words) and A-C06-5 (25 words): either one with A-C06-2 takes C06 to 11.60 or
  more, against 11.59.
- A-C04-9, second half ("A consensus statement the next year repeats it ...", 17 words): with it
  C04 goes to 13.32, against 13.30.
- A-C03-2, first sentence ("It took a page of shrinking steps ...", 25 words): with it C03 goes
  to 11.55, against 11.54. The check is still restored, using its short introduction and its
  closing line.

## Gap by gap

### C01
- **A-C01-1** restored: "E with I is energy intake (EI).", "E with O is energy output (EO).", "E with
  S is energy stored (ES)." and "This book writes these on the line, as EI and ES." These name I,
  O and S, and say the labels are printed flat. Once that is said, ρF and kP read the same way.
- **A-C01-2** restored: "Two symbols side by side are multiplied. f(x) is the output of a rule
  called f, not f times x (`B0-R0-C18`)." So ΔEI(t) reads as a function of t, and ε(...) as a
  product, because ε is a number.
- **A-C01-3** hole: the original has the same "interval i" gloss on an instantaneous-rate symbol,
  and P7's t is a length of time.
- **A-C01-4** hole: the original gives no grams-to-kcal figure for glucose either.
- **A-C01-5** restored: "For output it writes energy expenditure (EE), the name Book 1 used." and
  "EE and Hall's EO are the same quantity."
- **A-C01-6** restored: the Methods sentences, "The words are in the Methods." through "And "Δδ
  represents changes in physical activity"". The reader can now fill the words column from the
  paper's own sentences. The δ gloss is a residual hole, because the original says no more.
- **A-C01-7** hole: the original never teaches ×, * or > either.
- **A-C01-8** hole: "model" and "runs" are undefined in the original too. The restored "Then "The
  model parameter ρ ..."" now gives the sentence a context, but no definition.

### C02
- **A-C02-1** restored in C01's list: "This book keeps the two apart.", "ES is the store, in
  kilocalories.", "Its rate of change is dES/dt ...", "In this book's letters Hall's equation
  says this." and "The rate of change of stored energy equals energy intake minus energy
  expenditure.", with its `dES/dt = EI minus EE` block. C01 now settles ES as the store and
  dES/dt as its rate, which C02 and C05 rely on.
- **A-C02-2** hole: the original gives the same pointer to `B0-R0-C15` for a bracket times a
  bracket.
- **A-C02-3** restored: "Where the two sides do not settle on one number, f has no derivative at
  a." "Smooth" is a residual hole, because the original never defines it.
- **A-C02-4** restored: "Those intervals end at a instead of starting there." A negative divided
  by a negative is a residual hole, and belongs to Book 0.
- **A-C02-5** restored: "Test that against the body.", "Hall (2008) gives body fat 39.5 MJ a
  kilogram.", "The FAO/WHO/UNU report's worked example puts one woman's ... 8.26 MJ.", "Adding 0.6
  kg of fat in a day would take 23.7 MJ more than she spent." and "That is nearly three whole days
  of her expenditure.", with their working. The water claim can now be checked.
- **A-C02-6** hole: the original never defines "moving average". The 52 days against
  "neighbouring days" contradiction is in the exercise.
- **A-C02-7** hole (error): "shrink the interval the other way" is in the original, and so is the
  unexplained "middle day".
- **A-C02-8** hole: the original never quantifies "weeks" or the swing interval.
- **A-C02-9** restored: "Book 0 showed you the rate at an instant as the slope of a tangent, laid
  on a curve with a ruler." and "It named that rate the derivative (`B0-R0-C21`)." These also give
  the kept "no ruler needed" its antecedent.

### C03
- **A-C03-1** restored: "The constant multiple rule: ..." and "The sum and difference rules: ..."
  in the definition, so it now lists all four rules.
- **A-C03-2** restored: "Now use the rules.", with its working (S′(t) = 10t, S′(2) = 20), and "The
  same 20, in two lines." The 25-word opening was dropped for the mean-sentence rule, so "the same
  20" leans on C02 (residual).
- **A-C03-3** restored: "A derivative is itself a function, so you can take its derivative
  too."
- **A-C03-4** restored: "A rule applied to the output of another rule needs the chain rule." and
  "Both come in the rung-2 book of this subject." The two rules are now named, and "Until then"
  has its referent. C04's exponential rule is neither of them.
- **A-C03-5** restored: "Hall and colleagues (2012) write that "weight change will slow over time
  due to passive compensatory changes in energy expenditure"."
- **A-C03-6** hole: the original never defines passive compensation. It has only the Hall quote
  restored for A-C03-5.
- **A-C03-7** hole: P16 needs a rate of a rate from a table, and the original never teaches it.
- **A-C03-8** not a defect: the kept "Its sign says whether the rate is rising or falling" gives
  it directly. The reader worked it out, and was not stopped.

### C04
- **A-C04-1** restored: "Take y = e^(kt), where k is a fixed number ...", "Step forward a short
  time h.", "Multiplying two powers of the same base adds their exponents ...", with its working,
  and "As h shrinks, ... settles on k." through "... is the slope of e^(t) at the start, which is
  1." "So the rate of e^(kt) is k times e^(kt)" now follows from something.
- **A-C04-2** restored: "Take a base, say 2, ...", "Take a very short step, 0.0001, ...", with its
  working, then "The curve 2^(t) starts with a slope of 0.693." through "That base is e, and it is
  2.71828 ...". This gives the family of curves, and why e is the one with slope 1.
- **A-C04-3** hole: the original also states 1 minus e^(−kt) without deriving it.
- **A-C04-4** hole (error): the original has the same sentence. It is the gaps that are multiplied
  by the ratio, not the curve.
- **A-C04-5** hole (error): the original has the same must-know line.
- **A-C04-6** restored: "Start from 95% at 3 years and work out k, then the half-time.", with its
  working (2.996 ÷ 3 = 0.999).
- **A-C04-7** hole: the original also asserts the unit of k. P5's unitless 14 is in the exercise.
- **A-C04-8** hole (error): the same sign conflict is in the original.
- **A-C04-9** restored: "The calculator key marked log is log10, ...". This says what log10 is.
  The plural "the papers'" was dropped for the mean-sentence rule, and it and "W0" are residual
  holes.

### C05
- **A-C05-1** restored: "Cover the time from a to b with thin intervals of width Δt." and "Over
  each, draw a rectangle whose height is the rate in that interval."
- **A-C05-2** hole: the original never teaches reversed limits either. P6 asks for them.
- **A-C05-3** not a defect: this is the G0 artifact. S01-R1-C03 is in Book 1, which the book's
  reader has.
- **A-C05-4** hole: the original also asserts that the two cases are exact, and never shows why.

### C06
- **A-C06-1** hole: the original never defines "continuous".
- **A-C06-2** restored: "`S02-R1-C05` worked out integrals from shapes: rectangles, triangles,
  trapeziums." and "That works only for a rate that is steady or changes in a straight line."
- **A-C06-3** hole: the original's only introduction of T, "For a deficit D(t) = D0 e^(-kt), ...
  the total from 0 to T is ...", is 34 words. Restoring it breaks the mean-sentence rule.
- **A-C06-4** hole (contradiction): the original also has "where k is negative".
- **A-C06-5** hole: the original's limitation, "Turning it into kilograms needs to know what
  tissue was lost ...", is 25 words. Restoring it with A-C06-2 breaks the mean-sentence rule.

### C07
- **A-C07-1** restored: "Such an equation has many solutions." and "An initial value, the state
  at one stated time, picks out one of them."
- **A-C07-2** restored: "From the state at time t, compute the rate from the equation." before
  "Then take ...", and "Each step holds the rate fixed across one interval of length h, ...".
- **A-C07-3** restored: "With expenditure a straight line in weight, rising by epsilon, ... and a
  step change ΔEI in intake from a steady starting weight W0, the equation is:". This states the
  steady start and the straight-line EE. The algebra from EI − EE to ΔEI − ε(W − W0) is a
  residual hole, because the original does not show it either.
- **A-C07-4** hole (contradiction): the original also has "always true" beside "need not be a
  constant".
- **A-C07-5** restored: "The line's slope is −0.06221 ...", "About minus 480.", "Now the right
  side needs the weight at day 365.", "His weight on the line is 77.29 kilograms, ...", "The right
  side is about minus 25.8." and "The left side is minus 480.", with their working (480 − 25.8 =
  454).
- **A-C07-6** hole: the original never links this curve to C04's L + (W0 − L)e^(−kt).
- **A-C07-7** not a defect: this is the G0 artifact. The renderer prints "Book 1".
- **A-C07-8** hole: the problem is in P14, which is outside the prose.
- **A-C07-9** restored: "The steps drift a little from the curve, because each one holds the rate
  fixed for a whole day while the true rate keeps falling."
- **A-C07-10** restored: "Each gives the rate of change of a quantity at a moment as a rule in
  the value the quantity has at that moment, its state, and sometimes in the time as well." This
  says what f(W, t) means. The dropped underscores are in an exercise's quoted equation, and are a
  residual hole.

### C08
- **A-C08-1** hole: the original never says τ = 1/k. P5 is an exercise.
- **A-C08-2** hole: the original also puts "−100" beside "the two slopes add", and never
  reconciles the sign convention.
- **A-C08-3** not a defect: the first use in the cut text, "In the settling point model, intake is
  flat and expenditure rises ...", states the model. (The definition's 31-word version would also
  break the mean-sentence rule.)
- **A-C08-4** hole: the original also goes straight from "Set the rate to zero." to "300 divided
  by 120".
- **A-C08-5** restored: "Hall and colleagues (2012) warn that "changes in body weight also
  include changes in body water, which may be variable"." This is the source. "For weeks" is a
  residual hole.
- **A-C08-6** hole: the original has the same kP / k_P drift.

### C09
- **A-C09-1** restored: "That is the other kind of critical point, where the derivative does not
  exist, and setting a derivative to zero will never find it."
- **A-C09-2** hole: the original uses "range" in the same way.
- **A-C09-3** hole: the original never teaches the negative root either.
- **A-C09-4** hole: the original's Σ has no counter either, and it asserts the same moves.
- **A-C09-5** hole: the original uses the same "settling point" wording.
- **A-C09-6**, **A-C09-7** hole: these are in the exercises (P8, P10), and the original never
  teaches the skills they need.
- **A-C09-8** hole: "median" appears nowhere in the original, and the x^2 drift is in the exercise
  text.

## Counts

67 gaps are listed for Reader A in `COLD-READ-GAPS.md`, which gives the total as 68. Of the 67:
**28 restored**, **35 hole**, **4 not a defect**. Eight of the restored gaps leave a residual in
`HOLES-a.md`.
