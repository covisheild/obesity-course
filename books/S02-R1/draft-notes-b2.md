# Draft notes, batch b2 · S02-R1-C04, C05, C06

Drafter: Opus 5.5, 24 Sep 2026. Brief: `books/S02-R1/DRAFT-BRIEF.md`. Nothing committed.

## Records written

| Record | Name | Practice | Figure |
| --- | --- | --- | --- |
| `check/records/S02/S02-R1-C04.yml` | The number e, natural logarithms and change proportional to amount | 16 | `s02-r1-c04-two-exponentials.png` |
| `check/records/S02/S02-R1-C05.yml` | The integral of a rate is the change in the stock | 14 | `s02-r1-c05-net-rate-line.png` |
| `check/records/S02/S02-R1-C06.yml` | Undoing a derivative: antiderivatives and the fundamental theorem | 14 | `s02-r1-c06-steady-and-halving.png` |

`python check/build.py --check`: blocking 0 for these three. The only remaining warning on them is
that C04's illustration number 25 is derived (100 kg minus the 75 kg plateau), which the build
reports by design. The whole-build blocking count was 1 at hand-back, in `S02-R1-C17`, which is not
mine. All three figures pass `python check/figures/draw.py --book S02-R1`, and I looked at each PNG.
Every equation in the working and answers was recomputed in Python, including the lines with e and
ln that the build's checker skips (`/home/claude/scratch-b2/verify.py`). One rounding slip was found
and fixed (e^(-0.3465) is 0.7072, not 0.7071).

`concept_deps` names C01 to C03, as the brief says. They now exist, so the missing-record blocks seen
while drafting have cleared.

## Sources, and anything unsourced or unsure

- Every definition reference is to a held file, with a quote the build found. Textbook quotes are
  prose sentences. Two carry flattened letters from the extraction, and each note says so: "natural
  ee" (§1.5, the file doubles the italic e) and "*e*" (§3.9).
- **The defining sentence for e is not quoted.** In §3.9, e is the base b for which B′(0) = 1. That
  sentence is flattened, so the record quotes the plain sentence after it ("between 2.7 and 2.8").
  The value 2.71828 is checked on a calculator, not quoted.
- **Antiderivative is not quoted from its own section.** OpenStax defines it, and gives its power
  rule, in §4.10, which is not held. C06 quotes §5.3 and §5.4 (the evaluation theorem, the cancelled
  constant, the indefinite integral as a family). Each rule in C06's table is checked in the record by
  differentiating back. Because the concept is derivable, that is enough, but the auditor may want
  §4.10 taken at the next intake.
- **ln 20 divided by k** for the time to 95% is not in the book. It is derived in C04 by the same
  steps as the book's half-life. Its note says so.
- **The C04 flag is honoured.** The 1-year and 3-year figures from Hall 2011 and Hall 2012 are
  presented as rounded model outputs. The record shows that one exponential cannot give both: the
  ratio is 4.32 for any exponential and 3 for the papers. It says the rounded figures cannot tell you
  whether the curve is not exponential or the rounding is loose. It never claims either paper fits one
  exponential.
- **The shrinking deficits in C06 are made up.** One halves each year, one falls in a straight line.
  Each is labelled as made up and "not the paper's model" where it appears. The Hall 2011
  "about 100% greater" is quoted only for the direction of the gap and for the paper's own
  first-year figure. The halving deficit gives a smaller gap (526.6 MJ against 730), and the record
  says so instead of fitting it to the paper.
- **Chow & Hall 2008 and Hall 2008 equations: not used.** Neither was needed. C05 uses Hall 2012's
  sentence on the energy balance ("the rate of change in body ES is equal to the difference between
  the rates of EI and EO"). C05 also flags that Hall's ES in "ES = EI - EO" is a rate, while this book
  writes the store as ES and its rate as dES/dt.
- **One Book 1 pointer stands in for a figure.** C05 practice level 4 takes a 14-day
  doubly-labelled-water period from `S01-R1-C03` ("usually 10 to 14" days), not from a citekey.
  C05 practice level 9's trial is made up and labelled so. Its only real figure is Hall 2012's
  1000 kcal/d, which the record cites.
- Chain rule avoided. C03 routes it to S02-R2, so C04 derives d/dt of e^(kt) from the slope-1
  property and the rule for multiplying powers. C06 limits the power rule to whole-number n, matching
  C03, and names n = -1 as the exception.

## Why each practice-set size

- **C04, 16.** This is the hardest of the three. It has several moves that combine: calculator e and
  ln, the product rule for ln, the rate of A e^(kt), the half-time and 95% time both ways, solving
  for t, and the discrete ratio turned into k. Each move needed its own mechanical problem before
  the applied and transfer problems could mix them. There are two diagnostics per level, because
  the common slips differ in kind: log10 for ln, 95% reached for 95% left, the power rule on an
  exponential, and per-year k with t in days.
- **C05, 14.** The moves are reading the notation, the rectangle, the triangle, the signed trapezium,
  the average value, additivity and reversed limits, plus a reverse problem. The diagnostics cover
  sign, units and unequal spacing. That is fewer moves than C04, but more than a one-move technique.
- **C06, 14.** The moves are antiderivatives of powers and of e^(kt), checking by differentiating, F(b)
  minus F(a), the cancelling C, the total over all time, and running a total backwards. The
  diagnostics are the order of the limits, the missing division, and mixed units. The transfer
  problems test the "never reaches zero" and "just halve it" claims.

## Figures wanted, and tool gaps found

1. **`illustrations` (a list) is unusable in the current build.** `check/build.py` blocks every
   record without `illustration.analogy_breaks_when`, and so blocks any record that uses
   `illustrations`. The schema also forbids `quote` and `derived` on `illustrations[].numbers`. So
   C04's two illustrations (the Hall test, then Book 0's ratio test) are merged into one
   `illustration`, in that order. The conductor or figure planner may want the build fixed.
2. **Every drawn `fit` takes the same colour** (`pal["secondary"]`). In C04 the two exponential
   curves are both red and dashed, told apart only by their points and the legend labels "curve
   through the circles" and "curve through the squares". Wanted: one colour per fitted series.
3. **Shaded area under a line.** C05's figure should shade the triangle above the axis (4,500 kcal
   gained) and the one below (2,000 kcal lost), in two tints. At present they are only labelled.
   Data: net rate 300 - 10t kcal/day, t from 0 to 50 days, crossing zero at day 30.
4. **C06 could also shade** the area between the steady-deficit line (730t MJ) and the halving curve
   (730/0.693 times (1 - e^(-0.693t))), from 0 to 3 years, as the energy the steady rule
   over-counts. It would be optional once shading exists.

## Glossary rows (proposed; `prose/GLOSSARY.md` not edited)

Checked against the file: none of these is glossed yet. "integral", "rate of change", "running
total", "stock", "flow", "ceiling", "saturating" and "exponential" are glossed already and are used
in their existing sense.

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| antiderivative | a function whose rate is the given function; checked by differentiating it back | `S02-R1-C06` |
| average value (of a rate) | the integral divided by the length of the interval: the one steady rate that gives the same change | `S02-R1-C05` |
| e | the base whose exponential curve starts with a slope of exactly 1; about 2.71828 | `S02-R1-C04` |
| fundamental theorem of calculus (evaluation theorem) | an integral is the antiderivative at the end minus the antiderivative at the start | `S02-R1-C06` |
| half-time | the time a shrinking exponential takes to fall to half, from any starting value; ln 2 divided by k | `S02-R1-C04` |
| indefinite integral | the whole family of antiderivatives of a function, written with plus C and no limits | `S02-R1-C06` |
| integrand | the rate being added up inside an integral, written after the ∫ | `S02-R1-C05` |
| limits of integration | the two times at the foot and the top of the ∫ sign, where the adding starts and stops | `S02-R1-C05` |
| natural logarithm (ln) | the power you have to raise e to, to get the number | `S02-R1-C04` |
| net change theorem | the integral of a rate over an interval is the change in the stock over that interval | `S02-R1-C05` |
| net signed area | area above the time axis minus area below it | `S02-R1-C05` |
| rate constant (k) | the rate of change divided by the amount; its unit is one over time | `S02-R1-C04` |
| trapezium | a four-sided shape with two parallel sides; under a straight-line rate, its area is the average of the two end rates times the time | `S02-R1-C05` |

Consistency note: C07 and C08 (other batches) use "half-time" in the same sense, and C08 adds "time
constant", which is 1 divided by k. C04 does not use "time constant", so the two do not clash.
