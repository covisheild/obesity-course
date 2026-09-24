# S02-R1 draft notes · batch b3 (C07, C08)

Drafter: Opus 5.5, 24 Sep 2026. Brief: `books/S02-R1/DRAFT-BRIEF.md`. Nothing committed.

## Records written

- `check/records/S02/S02-R1-C07.yml`: A differential equation: a rule that gives the rate from the state. 16 practice problems, 2 exercises (K01 interpretation, K02 teaching), 1 figure.
- `check/records/S02/S02-R1-C08.yml`: Equilibrium: where the rate is zero. 17 practice problems, 2 exercises (K02 critique, K01 teaching), 2 figures.

`python check/build.py --check`: blocking 0 at hand-back (whole corpus). The only warnings on
these two records are the expected "derived rather than stated" notes on 7,716.18 (see below).
Every practice answer and every illustration line was recomputed in Python
(`/home/claude/scratch-b3/c07.py`, `c07p.py`, `c08p.py`). The build's quote check passes on every
quote. Each quote cited for a number states that number.

## Equations: what was used in place of the ones not held

- **Chow & Hall 2008 Equations 1-2 and the fixed-point equations: not used.** Only their prose is
  quoted: the "divide Equation 1 by some interval of time" sentence (C07), "ρM ... need not be a
  constant" (C07), and the fixed-point and stability sentences (C08).
- **The model equation in both records is Polidori 2016 Equation 1**, taken from the held MathML
  rendering. BW is written as W, and the Δδ and UGE terms are set to zero. The equation is then
  rearranged to ρ × dW/dt = ΔEI − ε × (W − W0). Hall 2012's words carry the rate form of the identity.
- **The C08 set point model adds Polidori Equation 4**, ΔEI = −kP × ΔBW. So the two slopes add:
  ρ × dW/dt = ΔEI − (ε + kP) × (W − W0).
- Thomas 2013 is used only for its "based on the first law" sentence and the 3500 kcal/lb quote.

## Things the auditor should look at (unsourced, or needing a decision)

1. **ρ = 7,716.18 kcal/kg is a stand-in.** It is the static rule's figure from Book 1, not a
   measured energy density of weight change. No held source gives the value of Polidori's ρ
   (Equation 2 gives only its form). Both records say in the prose that ρ is a stand-in, and that
   the timings it produces are illustrative. With ε = 20 it gives a half-time of about 267 days,
   against Hall's "roughly 1 year". The records say so and do not reconcile the two.
2. **Settling point and set point shifts (10-15 kg, 2.3-2.5 kg) and the C08 time table are my
   arithmetic** on Hall & Guo's stated slopes, with the stand-in ρ for the timings. Hall & Guo
   give the slopes and the 300 kcal/d cut, but no numeric result. The records say the numbers
   come from straight lines.
3. **Inventory wording corrected.** The C08 row says "with intake also falling as weight falls".
   The sources say intake *rises* as weight falls (Hall & Guo: slope about −100 kcal/d per kg;
   Polidori: eating rises ~100 kcal/day per kg lost). The record follows the sources. The slopes
   still add, because both flows push weight back.
4. **The Polidori check (350 ÷ 100 = 3.5 kg against "several kilograms lower")** uses only the
   intake side. The record says so. I did not attempt to reconcile the ~90 g/day UGE energy with
   the equilibrium. That would need a glucose energy factor that no held passage states for
   glucose itself.
5. **Polidori's β** (Equation 1) is not defined in any held passage. The C07 interpretation
   exercise tells the reader to write "not defined in what I read" rather than guess.
6. **C04 flag honoured.** C08 names Hall's "half in about 1 year, 95% in about 3" as the outputs
   of a model that is not a single exponential. It points to C04, which covers this. It fits no
   exponential to them.
7. **Hall 2011 rule-of-thumb forms differ by about 8%.** 100 kJ/d per kg is 23.90 kcal/d per kg,
   and 10 kcal/d per lb is 22.05 kcal/d per kg. C08 practice level 5 makes this the exercise,
   without calling either wrong.
8. `concept_deps`: C07 lists C01-C06, and C08 lists C01, C02, C04 and C07. These rely on the
   inventory's descriptions: C04 derivative of e^(kt) and ln 2 / ln 20; C05 rectangles; C06
   antiderivatives. The records also assume that C01 introduces EE in place of Hall 2012's EO.
   The Hall 2012 reference note says so. Check this against the C01 draft when it lands.
9. `python check/figures/draw.py --book S02-R1` redraws every S02-R1 figure, including other
   drafters' figures. One run coincided with another drafter's, and C12's sidecar was briefly
   unreadable. A later run cleared it. No other drafter's record was touched.

## Why each practice-set size

- **C07, 16.** Four moves compose: rate from state, forward step, checking a candidate on both
  sides and at the start, and running the equation backwards for ΔEI. Each needs a
  bare-number problem and an applied one. The four diagnostics are distinct errors: a stale
  rate, a sign flip, MJ against kcal, and change since the last weighing against change since
  baseline.
- **C08, 17.** The moves are: set the rate to zero and solve; find the crossing of two lines;
  add slopes when both flows respond; use the time constant and half-time; read the sign on
  each side for stability. There are four distinct diagnostics: subtracted slopes, τ inverted,
  a turning point taken for an equilibrium, and τ taken as the arrival time.

## Figures

- `s02-r1-c07-three-rules.png`: weight against day for ε = 0, 20 and 30, from the illustration's table.
- `s02-r1-c08-settling-point.png`: flat intake line against expenditure lines of slope 20 and 30,
  crossing 15 and 10 kg down.
- `s02-r1-c08-approach.png`: kg lost against day, settling point (τ = 385.809 d) against set
  point (τ = 64.3015 d), from the illustration's table.

Wanted, if the figure planner extends the tool:

- C07: a forward-step staircase over the exact curve for Hall's man. Use 30-day steps: 98.13,
  96.41 and 94.83 kg against the exact 95.01 kg at day 90. This needs a step series and a
  formula curve on one axis, in two styles.
- C08: the set point crossing. Intake line −300 − 100 × x against expenditure 20 × x, meeting at
  x = −2.5. It needs its own axes because the intake line is steep. Declaring it as a line
  figure is possible now if the conductor wants it.

## Glossary rows (proposed; not added to `prose/GLOSSARY.md`)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| differential equation | an equation that gives the rate of change of a quantity from the value it has now, and sometimes from the time | `S02-R1-C07` |
| equilibrium (of a differential equation) | a constant value of the state at which the rule gives a rate of zero; also called a steady state | `S02-R1-C08` |
| forward step (Euler's method) | work out the rate from the current state, move one step at that rate, then work the rate out again from the new state | `S02-R1-C07` |
| initial value | the state at one stated time, which picks one solution out of many | `S02-R1-C07` |
| initial-value problem | a differential equation together with an initial value; a function solves it only if it satisfies both | `S02-R1-C07` |
| linearization | a straight-line version of a fuller model | `S02-R1-C07` |
| set point model | Hall and Guo's model in which intake and expenditure both push back as weight changes; its equilibrium still moves when intake is shifted | `S02-R1-C08` |
| settling point model | Hall and Guo's model with intake flat and expenditure rising with weight; weight settles where the two lines cross | `S02-R1-C08` |
| solution (of a differential equation) | a function that makes both sides of the equation equal at every time; a second sense beside "solution (of a system)", `B0-R0-C17` | `S02-R1-C07` |
| stable (equilibrium) | a state pushed a little away from it returns to it | `S02-R1-C08` |
| state | the value a quantity has at a moment, from which a differential equation gives its rate | `S02-R1-C07` |
| time constant (τ) | ρ divided by the total slope, in days; the time in which the gap to the equilibrium shrinks by a factor of e | `S02-R1-C08` |
