# Draft notes, batch b6 · S02-R1-C15, C16, C17

Drafter: Opus 5.5, 24 Sep 2026. Brief: `books/S02-R1/DRAFT-BRIEF.md`. Nothing committed.

## Records written

| Record | Name | Practice | Figure |
| --- | --- | --- | --- |
| `check/records/S02/S02-R1-C15.yml` | Variance, and why independent errors add as squares | 18 | `s02-r1-c15-difference.png`, `s02-r1-c15-days.png` |
| `check/records/S02/S02-R1-C16.yml` | Following a derivation without skipping | 14 | `s02-r1-c16-two-readings.png` |
| `check/records/S02/S02-R1-C17.yml` | Four kinds of equation, and the notebook entry | none (not quantitative) | `figure_note` |

`python check/build.py --check`: blocking 0 for the whole build at hand-back (70 records). Warnings
left on these three: two sentences of 26 and 28 words that state an equation in words (C16, C17
illustrations), and C15's illustration number 100 reported as derived (the text layer prints
">100" as ".100"; the `derived` field says so). `python check/figures/draw.py --book S02-R1`: 0
problems; I looked at all three PNGs. Every number in working, answers and prose was recomputed in
Python (`/home/claude/scratch-b6/`). Every definition quote and `illustration.numbers` quote passes
the build's check; every quoted phrase in reader prose was also searched for in `sources/` by
script (`scratch-b6/q2.py`). The only misses are the reader's own quoted claims (made-up press lines)
and two phrases Hall 2012's text layer breaks with a line-end hyphen ("best- case", "per- son").

## Practice-set sizes

- **C15, 18.** Variance composes many moves: the weighted sum, the root, scaling (a² and the sign),
  sum, difference, n days, the mean of n days, a unit conversion, and the independence judgement.
  Each is met forwards and once in reverse (days from a total's spread; intake SD from Hall's
  1000) before the diagnostics. Two diagnostics per band because there are two classic breaks
  (subtracting spreads; a systematic error given the square-root law). Two transfers use real
  Thomas 2013 figures, where the adding rule does *not* apply (paired data; a deficit column that
  is not baseline minus target).
- **C16, 14.** Five moves plus the assumed line, and three tasks (name the move, fill a gap, find
  the break). Each move is met on bare algebra (levels 1 to 3) before it meets a paper's equation
  (Thomas, Chow and Hall's words, Polidori). Fewer would leave "shrink the interval" or
  "integrate a non-constant rate" undrilled.

## Held equations used, as the brief requires

- C16's worked derivations use **Thomas 2013's Methods equation** (rebuilt in seven lines from Hall
  2012's identity) and **Polidori 2016's Equation 1** (its first two terms rebuilt from the model of
  C07 with three premises; UGE added in practice level 6). **Chow and Hall 2008** is used only for
  its prose naming the move ("divide Equation 1 by some interval of time and take the limit");
  practice level 5 applies that move to Book 1's identity. Neither Chow and Hall's nor Hall 2008's
  equations are written anywhere.
- C17's ten build candidates are all held: Hall 2012 identity and rule of thumb; FAO/WHO/UNU PAL =
  TEE/BMR, TEE = BMR × PAL, one Table 5.2 row; FAO FNP 77 general factors; Thomas 2013; Polidori
  Equations 1, 4, 5. Chow and Hall Equations 1–2 and Hall 2008's energy-density equation are named
  as "if you can get them", with the second-reader instruction.

## Unsourced, unsure, or for the auditor

1. **Thomas 2013's sign.** The printed W(t) = W0 − ΔEB t/3500 (read from the MathML) and the
   where-clause "the difference between the rate of energy intake and the rate of energy
   expenditure" agree only if ΔEB is expenditure minus intake. C16 says the phrase does not fix the
   order and the equation needs the deficit reading. It does not say the paper is wrong. An auditor
   should compare the record's line with the MathML, since the quote check cannot see it.
2. **Polidori rebuild.** C16 rebuilds the *shape* of Equation 1 and says so; the paper cites its
   reference 6 (not held) for the method. β and δ are not defined in the held text; C17's build
   answer tells the reader to find them before finishing that entry. kI = 1 kcal/kg/d² is called
   "set for the simulation": the held words do not say it was fitted.
3. **Hall 2012's uncertainty figures.** ">100 kcal/d" is used as a floor, and every answer labels
   results "at least". The paper does not say its uncertainty or its "combined error ... 1000
   kcal/d" is a standard deviation; C15 says reading them so is the reader's assumption, in the
   illustration and in practice levels 4 to 6.
4. **Thomas's ± in the Results sentence** is read as a standard deviation on the strength of the
   Methods paragraph's "(Mean±SD)"; the practice prompt says so.
5. **ICMR-NIN**: its PAL sentence writes "PA R" for figures (1.53, 1.40) that are sedentary PAL
   values; C17 calls them the sedentary physical activity level and the reference note records the
   wording. "Another 5 %" does not say from which base, so the two 5% cuts are never combined into
   one figure. The 8.5% in C17 is PAL alone (1.40/1.53), at the same BMR.
6. **Made-up figures**, each said to be made up where introduced: C15's scale errors (±10 g), the
   300 and 250 kcal/day intake errors, the app's 50 kcal per item; C16's 180 lb / 500 kcal/day,
   200 lb / 700 kcal/day, EI 2000 / EE 2500, the straight-line rate; C17's 60 kg man.
7. **"Paired figures spread less"** (C15 must-know 5, practice 9) is mathematics of the covariance,
   which is routed to S03-R1; no held textbook states it in those words. OpenIntro says only that
   without independence "a modification to this equation would be required".
8. **Acronym EO.** C16 writes "They write it ES = EI − EO" and relies on C01 having expanded EO
   (C01's notes say it treats EE and EO as one quantity). The booklet's acronym report does not list
   EO, so it is expanded earlier.

## Notation followed

C01's reading of Hall's ES (the store; its rate is dES/dt), EE for expenditure, and C07's "ρ × dW/dt
= ΔEI − ε × (W − W0)" with explicit ×. Polidori's interval subscript as BW_i (C01's convention).

## Build defect met (not fixed; shared file)

`illustrations:` (the list) blocks: `check/build.py` near line 829 requires
`illustration.analogy_breaks_when`, and the schema forbids `quote` in `illustrations[].numbers`,
which `check_quotes` never reads anyway. As in b1, each record uses one `illustration` whose body
runs in parts.

## Figures wanted

None beyond those drawn. C17 carries a `figure_note`: it sorts equations and sets out an entry, and
its one calculation is a single substitution.

## Glossary rows (proposed; `prose/GLOSSARY.md` not edited)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| definition (kind of equation) | an equation that brings in a new quantity as a combination of others; it cannot be false, only read in another sense | `S02-R1-C17` |
| derivation | a chain of equations in which each line follows from the one before by one move that can be named | `S02-R1-C16` |
| fitted equation | an equation whose form was chosen and whose constants were estimated from one set of measurements; it holds for people like those | `S02-R1-C17` |
| identity (kind of equation) | an equation true for every value of its symbols, because of how its quantities are defined or because a conservation law requires it | `S02-R1-C17` |
| model assumption | a claim, adopted by an author, about how a body or a population behaves; it could be false | `S02-R1-C17` |
| move (in a derivation) | one named step from a line to the next: substitute, rearrange, shrink the interval, differentiate or integrate both sides, or assume | `S02-R1-C16` |
| notebook entry | six things written for one equation: the equation, each symbol with its unit, the sentence in words, its kind, what it assumes, and where it was found | `S02-R1-C17` |

Two existing rows gain a second sense (a between-rounds change, per the glossary's header):

- **variance**: (2) of a random variable, the expected squared deviation from its expected value,
  `S02-R1-C15`. The Book 0 sense (data) is unchanged.
- **independent**: (2) of two random variables, every event about one is independent of every
  event about the other, `S02-R1-C15`.

Named but not taught, so no row: covariance (routed to S03-R1).
