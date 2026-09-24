# S02-R1 compression pass: holes, batch a (C01 to C09)

Found by the cold read (Reader A) and not closable at step 5c. Either the original never filled
them, or they are an error or contradiction, or the original's own sentence could not come back
without breaking the mean-sentence rule. They are for the fixer and the audit. Sentences are
quoted as they stand in `S02-R1-C0n-final-prose.yml`. Exercises and practice problems are
outside the prose files, and are quoted from `S02-R1-C0n-pass1.md`. "Residual" marks the part of
a gap that was otherwise restored.

## C01

**A-C01-3**: `illustration.body`, the symbol table row "| dBW_i/dt | ... | rate of change of body
weight, interval i | kg a day |", and practice P7, "The interval length was t = (N−1)*T". What is
wrong: the d-notation was taught as a rate at an instant, but the gloss (Polidori's own) is an
average over an interval. P7's t is a length of time, while t everywhere else is a moment. To
close it: say once that Polidori's dBW_i/dt is estimated as an average over each interval, which
is the same point C02 makes. In P7, say that this t is a length of time, not the time variable.

**A-C01-4**: `illustration.body`, "Before you put 90 into this equation, find that conversion."
What is missing: the reader has no paper, and no figure for the energy in glucose. To close it:
either give the conversion with its source (for example, the kcal per gram of glucose that
Polidori used), or reword this as something the reader should look for in the paper, so that it
does not read as something they can do now.

**A-C01-6, residual**: `simplified_explanation` table row "| δ | small delta | "delta" | a
physical activity quantity (Polidori) |". What is missing: nowhere does the text say what δ
measures, or what its unit is before the unit working. To close it: quote Polidori's definition
of δ, if the paper gives one, or say that the paper does not define it.

**A-C01-7**: the exercises, "− k_P × ΔBW(t)", "kP>0" (Exercise 1) and "(N−1)*T" (P7). What is
missing: ×, * and > are never taught. The text teaches only multiplication by writing symbols
side by side, and Book 0 taught ≥. To close it: add one line on ×, * and > as they appear in
papers.

**A-C01-8**: `illustration.body`, "A parameter is a number the model holds fixed while it runs."
What is missing: "model" and "runs" are undefined at this point. To close it: define a model as
an equation that gives an output from inputs, and "runs" as working it out for each interval, or
reword without them.

## C02

**A-C02-2**: `illustration.body`, "Multiply out the bracket with the rule from `B0-R0-C15`, once
for each term." What is missing: `B0-R0-C15` teaches a number times a bracket, not a bracket
times a bracket, and the working does the second. To close it: say in one sentence that each
term of the first bracket multiplies the whole second bracket, as the first working line shows.
C09 needs the same step.

**A-C02-3, residual**: `definition.text`, "The derivative belongs to a smooth curve." What is
missing: "smooth" is never defined. To close it: give a one-line meaning, such as no jumps or
corners, so that the averages settle.

**A-C02-4, residual**: the table rows with negative h, for example "| -0.001 | 19.980005 |
-0.019995 | 19.995 |". What is missing: the text never teaches that a negative divided by a
negative is positive. To close it: add one line at the h below zero step, or cite the Book 0
section that teaches it, if one does.

**A-C02-6**: the term "moving average" (Exercise 1's quote), and Exercise 1, "Their weighings
were 52 days apart." then "why the authors did not take the rate from two weighings made on
neighbouring days". What is wrong: "moving average" is never defined. The exercise says the
weighings were 52 days apart, and then asks about weighings on neighbouring days, which did not
exist. To close it: define a moving average from the five-day example. Reword the exercise
(which is the fixer's job, not the compression pass's) so that the two statements agree, for
example "rather than from single weighings".

**A-C02-7 (error)**: `illustration.body`, "So with weighings, shrink the interval the other way."
and "Each average belongs to its middle day." What is wrong: the averaging widens the interval,
and does not shrink it. Why an average belongs to its middle day is never said. To close it:
"widen the interval". Add that a five-day average is placed at the middle day because that is
the centre of the days it covers.

**A-C02-8**: `must_know[1].point`, "Take a rate from averages over weeks, not from neighbouring
readings.", and `illustration.analogy_breaks_when`, "Below the interval over which water swings,
a shorter interval gives a worse rate, not a better one." What is missing: no length is given,
either for "weeks" or for the water-swing interval. To close it: give a sourced figure, or say
that it is not known and that the Methods should state it.

## C03

**A-C03-2, residual**: `illustration.body`, "Now use the rules." and its working, then "The same
20, in two lines." What is missing: without the original's opening sentence, "the same 20"
refers to C02's result, and S(t) = 5t² is not restated in C03. The opening was dropped because
restoring it breaks the mean-sentence rule. To close it: a short sentence naming S(t) = 5t² and
C02's answer of 20 at t = 2.

**A-C03-6**: `must_know[2].point`, "Slowing weight loss is what passive compensation predicts,
even with no change in the treatment." What is missing: "passive compensation" is never
defined. The restored Hall quote says only "passive compensatory changes in energy
expenditure". To close it: one line saying that expenditure falls as weight falls, with no
action by the person, so the deficit shrinks (C07's mechanism).

**A-C03-7**: practice P16, the monthly weights table. What is missing: the text teaches second
derivatives of formulas only. P16 needs a rate of a rate from data, which is differences of
differences. To close it: a worked line in the text, or drop the demand from P16.

## C04

**A-C04-3**: `illustration.body`, "The share of the eventual change reached by time t is 1 minus
e^(-kt)." What is missing: it is not derived from W = L plus (W0 minus L) times e^(-kt). To close
it: two lines. The change so far is W0 − W = (W0 − L)(1 − e^(−kt)), and dividing by the whole
change W0 − L leaves 1 − e^(−kt).

**A-C04-4 (error)**: `illustration.body`, "The ratio is what the curve is multiplied by over one
step, so it is e^(-k) for a step of one year." What is wrong: the curve 0, 50, 75, 87.5 is not
multiplied by 0.5. The gaps to the ceiling, and the successive differences, are. To close it:
"The ratio is what the gap to the ceiling (and each difference) is multiplied by over one step".
The original's cut definition sentence, "Read at equal steps of time h, the gap is multiplied by
the same factor, e^(-kh), at every step, and so is each successive change.", states it
correctly.

**A-C04-5 (error)**: `must_know[3].point`, "To test whether a claimed curve is exponential, divide
its rate by its value at two or more times." What is wrong: for a curve approaching a level L, it
is the rate divided by the gap (W − L) that is constant, not the rate divided by the value. To
close it: "divide its rate by its value (or, for a curve levelling off, by its gap to the
level)".

**A-C04-7**: `simplified_explanation`, "Its unit is one over time: per day, or per year.", and
practice P5, "A quantity falls exponentially with a half-time of 14." What is missing: the unit
of k is asserted, not derived from rate ÷ amount. P5 gives no unit. To close it: one line
deriving it ((amount per time) ÷ amount = per time). Give P5 a unit (the fixer's job).

**A-C04-8 (error)**: `simplified_explanation`, "The number k is the rate constant, the rate
divided by the amount.", against `definition.text`, "Where the quantity shrinks, write y = A
e^(-kt) with k above zero." What is wrong: for A e^(−kt), the rate divided by the amount is −k,
so the stated test gives a negative number, while k is declared positive. To close it: say that
the rate divided by the amount is k for growth and −k for decay, written with k above zero.

**A-C04-9, residual**: `illustration.body`, the table header "the papers' rounded figures" and
"The papers' figures give 3 divided by 1, which is 3.", and `definition.text`, "W0". What is
wrong: only one paper (Hall, *Lancet* 2011) is left in the text, so the plural has no
antecedent. W0 is printed without the underscore that C01 uses for counting subscripts. To close
it: the original's "A consensus statement the next year repeats it (Hall and colleagues,
*American Journal of Clinical Nutrition* 2012)." (17 words, left out because it breaks the
mean-sentence rule), or "the paper's". For the other, make W0 / W_0 consistent across the
book.

## C05

**A-C05-2**: practice P6, "∫ from 10 to 4 of f(t) dt". What is missing: reversed limits are
never taught. To close it: one line saying that swapping the limits changes the sign, which
follows from F(a) − F(b) = −(F(b) − F(a)) in C06. Alternatively, move the item to C06.

**A-C05-4**: `definition.text`, "Two cases can be done exactly with no limit." What is missing:
why these two need no limit is never said. To close it: add that the rate is constant, or
straight, across each slice, so every slicing gives the same total and the limit adds nothing.

## C06

**A-C06-1**: `definition.text`, "If f is continuous from a to b and F is any antiderivative of f,
then ...". What is missing: "continuous" is undefined. To close it: a one-line meaning (no
jumps), or say that every rate in this book meets it.

**A-C06-3**: `illustration.body`, "As T grows, e^(-0.693T) shrinks towards zero, so its total
creeps up towards 1053.4 megajoules and never passes it." What is missing: T is never
introduced. To close it: the original's "For a deficit D(t) = D0 e^(-kt), with D0 its value at t
= 0 and k above zero, the total from 0 to T is D0 times (1 minus e^(-kT)) divided by k." It was
left out because, at 34 words, it breaks the mean-sentence rule. A shorter sentence that
introduces T as the end of the interval would do it.

**A-C06-4 (contradiction)**: `must_know[1].point`, "For a shrinking curve, where k is negative,
it also gives the wrong sign." What is wrong: C04 writes a shrinking curve as e^(−kt) with k
above zero. To close it: "For a shrinking curve, e^(−kt), dropping the k also gives the wrong
sign".

**A-C06-5**: `illustration.analogy_breaks_when`, "Every total here is energy, in megajoules."
What is missing: under "Where this picture breaks" no limitation is stated. To close it: the
original's "Turning it into kilograms needs to know what tissue was lost (`S01-R1-C02`), and that
is part of why Hall's model differs from the static rule." It was left out because, at 25 words
together with A-C06-2's restore, it breaks the mean-sentence rule. Or a shorter version of it.

## C07

**A-C07-3, residual**: `definition.text`, the working "ρ × dW/dt = ΔEI − ε × (W − W0), with W = W0
at t = 0", after `simplified_explanation`'s "ρ × dW/dt = EI − EE". What is missing: the algebra
between them. EE = EE0 + ε(W − W0), EI = EI0 + ΔEI, and EI0 = EE0 at the steady start, so EI −
EE = ΔEI − ε(W − W0). To close it: those three lines, as working. This was the reader's most
serious gap in C07.

**A-C07-4 (contradiction)**: `simplified_explanation`, "That line is always true.", against
`illustration.analogy_breaks_when`, "For a real body, ρ "need not be a constant", as Chow and Hall
(2008) put it." What is wrong: ρ × dW/dt = EI − EE holds exactly only with a fixed ρ. To close
it: "That line is true whenever ρ is fixed", or say that it is exact only for a constant ρ.

**A-C07-6**: `illustration.body`, "W(t) = 100 − 24 × (1 − e^(-t/385.809))". What is missing: no
link to C04's W = L plus (W0 minus L) e^(−kt), with L = 76, W0 − L = 24 and k = 1/385.809. To
close it: one line making the match.

**A-C07-8**: practice P14, "Here is a worked answer to the Polidori-style problem at level 5."
What is wrong: the problem meant is P8, and "level" is used nowhere else. To close it: "to
problem 8" (the fixer's job).

**A-C07-10, residual**: an exercise's quoted equation, "ΔEIi = ρ × (dBWi/dt) + ε × (BWi − BW0) +
...". What is wrong: the underscores C01 uses for counting subscripts are dropped (ΔEI_i, BW_0).
To close it: print the subscripts as C01 does.

## C08

**A-C08-1**: `definition.text`, "Its time constant, written tau (τ), is ρ divided by the total
slope, in days.", and practice P5, "Take dy/dt = −0.02 × (y − 50) ... Give the time constant".
What is missing: τ is never tied to C04's k (τ = 1/k). P5 has no ρ, so "ρ divided by the total
slope" cannot be applied. To close it: add "τ is 1/k, where k is the rate constant of C04".

**A-C08-2**: `illustration.body`, "In the set point model, intake also depends on weight, "with a
slope of about -100 kcal/d per kg"." followed by "The two slopes add, because both push the same
way.", with expenditure's slope +20. What is wrong: taken literally, −100 plus 20 is −80, which
is exactly P12's broken step. The text never says that the slopes add in size because they are
written against the change (W − W0) with opposite sign conventions. To close it: one line saying
that Hall and Guo's −100 is intake against weight, so a fall in weight raises intake by 100 a
kg, and in the equation it enters as −100 × (W − W0), the same sign as −ε × (W − W0).

**A-C08-4**: `illustration.body`, "Set the rate to zero." followed straight by "300 divided by 120
= 2.5". What is missing: the step 0 = −300 − 120 × (W* − W0), so W* − W0 = −2.5, which gives the
sign (2.5 kg lower). To close it: add that line to the working.

**A-C08-5, residual**: `must_know[4].point`, "... and water shifts can hide the true rate for
weeks." What is missing: the restored Hall quote supports water shifts, but not "for weeks". To
close it: source the duration, or drop "for weeks".

**A-C08-6**: `definition.text`, "Polidori and colleagues write that number kP, k with a P for
proportional.", against C01 Exercise 1's "k_P". What is wrong: the same symbol is printed two
ways. To close it: one form across the book.

## C09

**A-C09-2**: `definition.text`, "A critical point of f is an input c, inside the range, at which
...". What is wrong: "range" here means allowed inputs, but Book 0 C4 defined range as the
outputs. To close it: "inside the stretch of inputs considered" (or "domain", if Book 0 names
it).

**A-C09-3**: `illustration.body` working, "x² = 1" then "x = 1 or x = −1". What is missing: that
a square has two roots is never taught. To close it: one line saying that both 1 × 1 and (−1) ×
(−1) give 1.

**A-C09-4**: `illustration.body`, "S(m) = Σ (x − m)²", "The candidate m is the same number in
every term, so it comes outside the sum." and "And m² is added once for each reading, n times in
all." What is missing: C01 taught Σ with a counter and limits, but this Σ has neither. Taking m
outside the sum, and Σ m² = n m², are asserted. To close it: write the sum with a counter, Σ[i =
1 to n] (x_i − m)², and show the two moves on the five weighings.

**A-C09-5**: `illustration.body`, "A rate held at zero marks a settling point." What is wrong: C08
uses "settling point model" as the name of one model, and here "settling point" means any
equilibrium. To close it: "marks an equilibrium".

**A-C09-6**: practice P8 (fencing). What is missing: building a function from a constraint is
never taught. To close it: a worked line in the text, or a note in P8 giving the area as a
function of one side.

**A-C09-7**: practice P10, "S(m) = 4m² − 560m + 19,601". What is missing: matching coefficients to
Σx², Σx and n is never taught. To close it: a line in the text, or rework P10 so that it needs
only differentiation.

**A-C09-8**: practice P16 (it needs the median), and "x^2" beside "x²" in the practice set. What
is missing: the median is never named, and the notation drifts. To close it: name the median
where the text says "a different centre can come out best", and make the notation consistent.
