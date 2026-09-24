# Cold-read gap reports · S02-R1 (Task 5b), condensed by the conductor

Two cold readers, 24 Sep 2026: A read C01–C09, B read C10–C17 (each with the released Book 0 and Book 1
text, B also with C01–C09 cut). Subagents could not write files, so the conductor transcribed the gap
lists from their replies; the readers' worked answers are omitted. A's 68 gaps, B's 44 plus 6 exposed.

**Artifacts of the cold-read set, not defects (conductor):** G0 — raw ids like `B0-R0-C11` and
`S01-R1-C03` in the pass-1 text (the renderer prints "Book 0, B4" / "Book 1, section 3", so the reader
of the book can follow them); `S01-R1-C03` absent from the set (not in any record's concept_deps; the
book's reader has Book 1). Everything else below goes to 5c triage.

## Reader A

**C01.** 1 Hall's subscripts printed flat: "Hall and colleagues write E for energy and set a small I, O
or S after it" then "ES = EI minus EO" — reads as E times S; I and O never named; "ρF", "kP>0" too (read
twice). 2 Two brackets look alike: `ε(BW_i − BW_0)` multiplies, `ΔEI(t)` is "at time t"; no way to tell.
3 dBW_i/dt glossed "rate of change of body weight, interval i" though the d-notation is an instant;
P7 "t = (N−1)*T" is an interval length. 4 "Before you put 90 into this equation, find that conversion"
— no paper; nothing says glucose takes 4 kcal/g. 5 Caption "Σ[i = 1 to 7] (EI_i − EE_i)": EE undefined
(text used EO). 6 Reader sent to a paper they lack ("Fill the 'words' column from the paper's own
sentences", "Search the Methods … β"); δ glossed only as "a physical activity quantity". 7 "×", "*",
">" never taught (only ≥). 8 "A parameter is a number the model holds fixed while it runs": model and
runs undefined.

**C02.** 1 ES changes meaning: C01 "ES is the rate of change in the body's macronutrient stores", C02
"dES/dt is the rate of change of stored energy … not the stored energy itself" (read twice; reconciled
only in C05). 2 "Multiply out the bracket with the rule from B0-R0-C15" — a bracket times a bracket was
never taught. 3 "If both lists close in on the same number" — what if they don't; "smooth" undefined.
4 "with h below zero" — why, and negative ÷ negative never taught. 5 "The one-day rate is measuring
water, not stores" asserted for made-up data. 6 "moving average" undefined; Exercise 1 says "weighings
were 52 days apart" then asks about "weighings made on neighbouring days" (read twice). 7 "Shrink the
interval the other way" widens it; "Each average belongs to its middle day" unexplained (read twice).
8 "averages over weeks", "the interval over which water swings" never quantified. 9 Limit never tied to
Book 0 C7's tangent.

**C03.** 1 Definition's "Four rules" ≠ plain-terms list. 2 Rules asserted, never checked (C02's 5t²
would confirm the power rule). 3 "**The second derivative.** The result is the second derivative" —
the instruction to differentiate again is missing; d²y/dx² unexplained (read twice). 4 "Two rules are
not in this book" names one; "Until then" contradicts; C04 then gives an exponential rule. 5 "a made-up
curve with that shape" — no antecedent (read twice). 6 "passive compensation" undefined. 7 P16 needs a
rate of a rate from a data table; only formulas taught. 8 Negative f″ while falling left to inference.

**C04.** 1 "So the rate of e^(kt) is k times e^(kt)" follows nothing; C06–C08 rest on it (read twice;
most serious). 2 Family of exponential curves never introduced ("the one exponential curve"). 3 "1 minus
e^(−kt)" not derived from W = L + (W0 − L)e^(−kt). 4 "The ratio is what the curve is multiplied by over
one step" — true of the gaps, not the curve 0, 50, 75, 87.5. 5 Must-know "divide its rate by its value"
fails for a curve approaching a level (it is the gap). 6 k = 0.999 never derived (ln 20 ÷ 3). 7 Unit of
k asserted; P5's half-time "14" has no unit. 8 "rate divided by the amount" gives −k for e^(−kt), yet k
declared positive. 9 "log10" notation, "W0" underscore, "the papers'" plural for one paper.

**C05.** 1 "the rectangles' areas" — no rectangles introduced; where heights are read not said.
2 Reversed limits never taught; P6 asks "∫ from 10 to 4". 3 Doubly labelled water points to S01-R1-C03.
4 "Two cases can be done exactly with no limit" asserted.

**C06.** 1 "continuous" undefined. 2 "Most rates bend. This section gives a way that does not need a
shape." (read twice). 3 "As T grows" — T not introduced. 4 "For a shrinking curve, where k is negative"
contradicts C04's "e^(−kt) with k above zero" (read twice). 5 "Where this picture breaks" states no
limitation: "Every total here is energy, in megajoules."

**C07.** 1 "initial value" used before defined. 2 "Then take the state at t + h" — "Then" follows
nothing; h never introduced (read twice). 3 From "ρ × dW/dt = EI − EE" to "ΔEI − ε × (W − W0)" never
shown; EE = EE0 + ε(W − W0) never written; starting in balance never stated (most serious). 4 "That line
is always true" holds only if ρ fixed; later "need not be a constant". 5 "disagree by more than 450"
without working (454). 6 W(t) = 100 − 24(1 − e^(−t/385.809)) not linked to C04's form. 7 "Book 1" never
mapped to S01. 8 P14 "the Polidori-style problem at level 5" is Problem 8; "level" unused elsewhere (read
twice). 9 "A smaller step drifts less" asserted. 10 "f(W, t)" untaught; "ΔEIi", "BW0" drop underscores.

**C08.** 1 τ never tied to k (τ = 1/k); P5 has no ρ. 2 "The two slopes add" beside a slope of "−100":
literally −80, exactly P12's error. 3 "settling point model" undefined (only "set point"). 4 "Set the
rate to zero." straight to "300 divided by 120", sign dropped. 5 "water shifts can hide the true rate for
weeks" new and unsupported. 6 "kP" ≠ C01's k_P.

**C09.** 1 "or does not exist" never explained. 2 "range" third meaning ("inside the range" = allowed
inputs; C4 defined range as outputs) (read twice). 3 Negative root never taught ("x = 1 or x = −1").
4 Σ without a counter; m out of the sum and Σm² = nm² asserted. 5 "A rate held at zero marks a settling
point" clashes with C08's model name. 6 P8 (fencing) needs building a function from a constraint.
7 P10 needs matching coefficients. 8 Median never named (P16); x^2 → x² drift.

## Reader B

**C10.** 1 (M) "A weighted sum of vectors v and w … is the vector cv + dw" vs "Each factor is a weight":
never says a dot product is a weighted sum of entries (read twice). 2 (L) Subtraction and negative
weights never shown; P2 needs both. 3 (M) "Add or scale rows only when every entry means the same thing
… Two patients' rows do not." — two patients' rows pass the stated test. 4 (L) "Many different gram
vectors give the same total energy" asserted; P14 relies on it. 5 (L) Dot product of unequal lengths only
implied undefined; P4(1) needs it.

**C11.** 1 (L) "scalar" undefined. 2 (M) "The same result is a weighted sum of the columns of A"
asserted, never shown; P3 asks for it. 3 (M) "ICMR-NIN's 2020 brief note…" never expanded here;
"reference woman" (P7) undefined. 4 (L) "Book 1 met the basal metabolic rate" (S01-R1-C03). 5 (L)
Vector as one-column matrix / 1×1 product as a number never said (P6). 6 (L) P14's "10 to 12%" not in
C11. 7 (L) P15 gives nothing to compute.

**C12.** 1 (H) "the table no longer fixes the weights…", "entered together as predictors" (Ex 1), "had
no effect" (P13), "accounted for" (must-know) depend on fitting, predictor, effect, model — none taught.
2 (M) "Find the weights from as many rows as there are weights" needs k equations in k unknowns; Book 0
C3 taught two; P11 announces a three-unknown solution. 3 (M) "If the equations have no solution, or a
single leftover row fails, it is not." omits infinitely many solutions. 4 (M) "Weight can be moved … in
proportion" never demonstrated; P9 depends on it. 5 (L) "the next rung's collinearity" undefined.
6 (L) "The report defines…" no antecedent. 7 (L) "almost" in "almost any column fits"; "ash" (P14)
undefined.

**C13.** 1 (M) "X can be any number from −0.05 to 0.05": half-step rule asserted; P9 needs it.
2 (M) "A probability distribution is a model" vs "exact only because the whole village was listed"; P10
(read twice). 3 (L) "The values listed must not overlap" — for bands, not values. 4 (L) P9 "range of X"
ambiguous.

**C14.** 1 (H) "Two rules follow from the definition … E[X + Y] = E[X] + E[Y], whether or not X and Y
are independent." never shown; X + Y and joint distribution undefined; must-know acts on it. 2 (M) "the
ordinary mean … only when all the values are equally likely" contradicted by the village (E[X] = 5.0 =
ordinary mean) (read twice). 3 (L) Defined only for discrete. 4 (L) Caption "balance point" not in text.
5 (M) P14 — by the text's own surplus definition the claim is true; answer route unclear.

**C15.** 1 (H) Title promises "why … add as squares"; adding rule and a² rule asserted; only check is
a figure caption; D6's √n law rests on it. 2 (H) "Over 9 days … 900 … 300 divided by the square root of
16 is 75": example switches 9 days → 16. 3 (M) Dependence only described as making a spread "much less";
P18's 784 > 747. 4 (M) Probability-weighted Var(X) never related to D5's n−1 rule. 5 (L) "removes an
error shared by both readings" asserted. 6 (L) P17 "within 50": SD or bound? 7 (L) P8 "precision of 5%"
undefined as relative.

**C16.** 1 (M) "The moves this book uses are these" — P8 needs "take the limit", not listed; others need
evaluate/collect. 2 (L) Ex 1 "the consensus panel dropped it" not in text. 3 (L) "infinitesimal",
"passive" undefined. 4 (L) Line 2 folds a differentiation into an "assumed" line.

**C17.** 1 (M) No practice set (concept is not quantitative: not a defect). 2 (H) Ex 1 candidate 9
(Polidori Equation 5, "adds an integral term") and the Chow & Hall / Hall 2008 equations are not printed;
the reader cannot finish. 3 (M) Identity and definition overlap; candidates 3 and 5 unsortable.
4 (L) "Schofield", "the consultation" unexplained; "fitted on" count given only for men. 5 (L) "use
ICMR-NIN's figures" — no figures given.

**Exposed in earlier text.** 1 (M) Book 0 C3 limited to two unknowns. 2 (L) Book 0 D2 independence only
for events; C14/C15 apply it to random variables. 3 (M) D6's √n law underived. 4 (L) C03 "passive"
undefined. 5 (L) S01-R1-C03 (artifact). 6 (L) C11 uses ICMR-NIN before C17 defines it.

**Reader B's worked answers flagged:** C11 P14 — "the correction factor is 1/1.10 to 1/1.12, which is
0.909 to 0.893, not 0.90 to 0.88"; C16 P13 — "26.6 against 27.6; a mean of products isn't a product of
means" (check the record's own answer); C14 P14 — see C14 gap 5.
