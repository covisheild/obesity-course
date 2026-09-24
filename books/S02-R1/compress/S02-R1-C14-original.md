# S02-R1-C14 · Expectation

**Definition.** Let X be a discrete random variable, as in `S02-R1-C13`, taking the values x1, x2, ..., xk.
Its expected value, or expectation, is written E[X]. It is each value times its probability,
all added up: x1 times P(X = x1), plus x2 times P(X = x2), and so on up to xk times
P(X = xk). In
the sigma notation of `S02-R1-C01`, E[X] = Σ x P(X = x), the sum running over every value x
that X can take. It carries the unit of X. It is also written with the Greek letter mu, μ.

E[X] is a probability-weighted average. It is the ordinary mean of `B0-R0-C28` only when all
the values are equally likely. It need not be a value X can take.

It is the long-run average. Repeat the chance process many times, and the average of the
values X takes settles towards E[X]. That is the law of large numbers. It is a property of the probability distribution, a
parameter in the sense of `B0-R0-C29`. The mean of a sample of observed values is a statistic.
It estimates E[X] and differs from it from one sample to the next.

Two rules follow from the definition. For fixed numbers a and b, E[aX + b] = aE[X] + b. For
any two random variables X and Y, E[X + Y] = E[X] + E[Y], whether or not X and Y are
independent. Together they give E[aX + bY] = aE[X] + bE[Y].

The first rule follows in three moves. Each value x of X becomes a times x, plus b, with the
same probability as before. So E[aX + b] is the sum of (a times x plus b) times P(X = x).
Multiply out the bracket, as in `B0-R0-C15`. That gives a times the sum of x times P(X = x),
plus b times the sum of P(X = x). The first sum is E[X], and the second is 1.

The second rule follows by working outcome by outcome. E[X] can also be found as the sum, over
every outcome in the sample space, of the value X gives that outcome times the probability of
that outcome. Grouping the outcomes that give the same value turns this back into the
value-by-value sum. Now X + Y gives each outcome the value X gives it plus the value Y gives
it. So the outcome-by-outcome sum for X + Y splits into the sum for X plus the sum for Y. No
step asks whether X and Y are independent.

Neither rule reaches products, ratios or squares. E[XY] is not in general E[X] times E[Y], and
E[X/Y] is not in general E[X] divided by E[Y]. For those, go back to the distribution.

For a continuous random variable the sum becomes an integral of x times the probability
density. This book works only the discrete case.

A clash of letters. In papers on energy balance, E with a label, as in EI, EE or ES, is energy.
E followed by square brackets around a random variable, E[X], is expectation. Some books write
E(X) with round brackets.

**In plain terms.** Take a chance process that gives a number, and imagine running it a very large number of
times. The average of all those numbers is the expected value.

To work it out, you do not need the long run. Multiply each value by its chance and add. A
value with a big chance counts for a lot, and a rare value counts for little.

Picture the values as weights hung along a ruler, each as heavy as its chance. The expected
value is where the ruler balances. It can sit between the weights, at a value that never
happens.

Two shortcuts save a lot of work. Double every value and the expected value doubles. Add 5 to
every value and it goes up by 5. And the expected value of a total is the total of the expected
values. That last one holds even when the parts are tied to each other.

**Illustration.** Start with the mistake. Suppose a person's energy surplus on a day, intake minus expenditure
as in `S01-R1-C05`, is a random variable X, in kilocalories a day. The distribution below is
made up.

```table
surplus x (kcal/day)  P(X = x)
-300                  0.2
0                     0.3
200                   0.4
500                   0.1
```

The move you will reach for first is to average the four values, as if each were equally
likely.

```working
-300 plus 0 plus 200 plus 500 = 400
400 divided by 4 = 100
```

That gives 100, and it is wrong. The values are not equally likely, and the ordinary mean
treats them as if they were. Weight each value by its probability instead.

```working
-300 times 0.2 = -60
0 times 0.3 = 0
200 times 0.4 = 80
500 times 0.1 = 50
-60 plus 0 plus 80 plus 50 = 70
```

E[X] is 70 kcal a day. You will never see a day with a surplus of 70 in this model. The 70 is the balance point
of the four values, pulled towards 200 by its 0.4 and held back by the 0.2 at minus 300.

Now a week. Let W be the surplus over seven days: X1 for day 1, plus X2 for day 2, and so on
to X7. If each day has this same distribution, each has expected value 70. The sum rule gives
the week.

```working
7 times 70 = 490
```

E[W] is 490 kcal. The week itself could land anywhere from seven days at minus 300 to seven
days at 500.

```working
7 times -300 = -2100
7 times 500 = 3500
```

So 490 is the long-run average of weeks. It is not what any one week will show.

Does the sum rule need the days to be independent? Try a pair that is as tied together as
possible. Say that on day 2 this person's surplus is always 140 minus day 1's. A big day is
followed by a small one. Call day 2's surplus Y. Each value of X fixes Y.

```table
x (kcal/day)  y (kcal/day)  probability
-300          440           0.2
0             140           0.3
200           -60           0.4
500           -360          0.1
```

Work out E[Y] from its own values and probabilities.

```working
440 times 0.2 plus 140 times 0.3 plus -60 times 0.4 plus -360 times 0.1 = 70
```

E[Y] is 70 too. On every row, X plus Y is 140, so E[X + Y] is 140. The sum rule gives the same.

```working
70 plus 70 = 140
```

The two days could hardly be more dependent, and the rule still holds.

Now a fixed shift. Say an app adds a fixed 120 kcal to every day's logged intake, a
systematic error as in `B0-R0-C30`. The logged surplus is X + 120. By the first rule its
expected value is E[X] + 120.

```working
70 plus 120 = 190
7 times 190 = 1330
```

Over a week the log expects 1,330 kcal against a true 490. Logging more weeks will not close
that gap. The shift moves the expected value itself.

Last, the expected value set beside a sample's mean. Go back to the made-up village of
`S02-R1-C13`: ten households of 2, 3, 4, 4, 5, 5, 5, 6, 7 and 9 people. Pick one at random,
and let X be its size. Each household has probability 0.1, so E[X] is 0.1 times the sum of
the sizes.

```working
2 plus 3 plus 4 plus 4 plus 5 plus 5 plus 5 plus 6 plus 7 plus 9 = 50
0.1 times 50 = 5.0
```

E[X] is 5.0 people, the same as the village's ordinary mean, because every household was
equally likely. The survey's four households held 5, 9, 4 and 5 people.

```working
5 plus 9 plus 4 plus 5 = 23
23 divided by 4 = 5.75
```

The sample mean is 5.75. It is a statistic that estimates E[X], and it misses by 0.75. A
bigger random sample would tend to land closer. E[X] itself does not move.

**Where this picture breaks.** The surplus distribution is made up, and it is the same on every day only because this model
says so. A real person's daily surplus has no known distribution. It also drifts as their
weight and habits change, and then "7 times 70" no longer describes the week. The sum rule
still holds with seven different expectations. It is the "same every day" that fails.

The day-2 rule, 140 minus day 1, is invented to show that dependence does not matter for the
expected value. It will matter a great deal for the spread, in the next section.

The village is made up. Its E[X] equals its mean only because each household was equally
likely to be picked.

**Figure.** The made-up distribution of a day's energy surplus, in kilocalories a day. The expected value, 70, is the balance point of the four bars. No bar sits at 70, and averaging the four values without their probabilities gives 100.

*What the figure shows:* Four bars: 0.2 at minus 300, 0.3 at 0, 0.4 at 200 and 0.1 at 500 kilocalories a day, with a label at 70 marking the expected value.

**Figure.** The expected running total of surplus over a week grows by 70 kilocalories a day, to 490 by day 7. The possible totals fan out much wider, from seven days at minus 300 (minus 2,100) to seven days at 500 (3,500).

*What the figure shows:* Three lines from zero at day 0: the expected total rising to 490 at day 7, the highest possible total rising to 3,500 and the lowest falling to minus 2,100.

**Must know points for you.**

- The expected value is not what any one person or day will show. It is the long-run average, and it may be a value that never happens. Never tell a patient "you can expect to lose 4 kg" as if it were their outcome. Say what happened on average, and how widely people differed.
- Averaging the possible values without their probabilities gives the expected value only when every value is equally likely. Otherwise it is wrong, sometimes badly. Weight each value by its probability, every time.
- The expected value of a sum is the sum of the expected values, with no condition of independence. So a week's expected surplus is seven times a day's, when every day has the same expected value, however the days are tied together. Do not refuse the sum because the days are dependent. Keep that objection for the spread, where it matters.
- The rules stop at sums and fixed multiples. The expected BMI is not the expected weight divided by the square of the expected height. The expected TEE is not the expected PAL times the expected BMR when the two vary together. For a product, a ratio or a square, go back to the distribution and work value by value.
- A fixed error of b in every reading moves the expected value by exactly b. Averaging more readings does not remove it; it only pins down the shifted value more closely. Find the size of the shift against a known reference, as in `B0-R0-C30`, and subtract it.
- E[X] belongs to the model. A sample mean is a statistic that estimates it, and misses by an amount that changes from sample to sample. Before you quote a paper's "expected value", ask whether it was computed from a stated distribution or averaged from data.
- In an energy-balance paper, check which E you are reading. E with a label, such as EI or ES, is energy. E with square or round brackets around a random variable is an expected value.

**Exercise 1** (interpretation). A methods section contains these two lines.

> E(X) = Σ x_i P(X = x_i), where X is the daily energy surplus in kcal/day.
>
> Mean EI was 2,400 kcal/day.

Read the first line aloud in words, symbol by symbol, with units. Then say which E in the two
lines is energy and which is expectation, and how you can tell.

**1.** X takes the values 1, 2 and 3, with probabilities 0.2, 0.5 and 0.3.

Work out E[X].

**2.** X takes the values −2, 1 and 4, with probabilities 0.5, 0.25 and 0.25.

Work out E[X]. Is it a value X can take?

**3.** E[X] is 3.

Work out E[2X + 5], E[−X] and E[X − 3].

**4.** E[X] is 4 and E[Y] is −1. Nothing is known about whether X and Y are independent.

Work out E[X + Y], E[X − Y] and E[3X − 2Y].

**5.** X takes only the values 0 and 10. E[X] is 2.5.

Work out P(X = 10).

**6.** The FAO/WHO/UNU report on human energy requirements gives this example. A man has a PAL of
1.75 and a mean BMR of 7.10 MJ/day. The report multiplies them to get his mean energy
requirement.

Treat BMR as a random variable with expected value 7.10 MJ/day, and PAL as fixed at 1.75.
TEE is PAL times BMR. Work out E[TEE], and compare it with the report's figure of 12.42
MJ/day.

**7.** In a made-up model, a person's daily energy surplus has expected value −150 kcal/day on every
day. Their days are not independent: a low day tends to be followed by a high one.

Work out the expected surplus over 7 days and over 28 days.

**8.** In a made-up model, a person's true daily surplus has expected value 30 kcal/day. Their food
app adds a fixed 120 kcal to every day's logged intake.

Work out the expected logged surplus for a day and for a week. Then work out how far the
week's expected logged surplus is from the true one.

**9.** Go back to the made-up village of ten households with 2, 3, 4, 4, 5, 5, 5, 6, 7 and 9 people.
Its E[X] for one household picked at random is 5.0 people. A second survey picks five
households at random and finds 4, 7, 5, 5 and 9 people.

Work out the second survey's mean. Say which number is the parameter and which the statistic,
and what would tend to happen to the statistic with a much bigger sample.

**10.** Here is a worked answer. Find the step that broke.

```working
a day's surplus X is -300, 0, 200 or 500 kcal, with probabilities 0.2, 0.3, 0.4 and 0.1
E[X] = (-300 plus 0 plus 200 plus 500) divided by 4
= 400 divided by 4 = 100
so the expected surplus is 100 kcal a day
```

**11.** Here is a worked answer. Find the step that broke.

```working
each day's surplus has expected value 70 kcal a day
the week's expected surplus is the average of the seven days' expected values
(70 plus 70 plus 70 plus 70 plus 70 plus 70 plus 70) divided by 7 = 70
so the expected surplus for the week is 70 kcal
```

**12.** Here is a worked answer. Find the step that broke. BMI, from `B0-R0-C14`, is weight in
kilograms divided by the square of height in metres.

```working
two made-up adults, each picked with probability 0.5: 50 kg and 1.5 m, or 90 kg and 1.8 m
E[weight] = 0.5 times 50 plus 0.5 times 90 = 70
E[height] = 0.5 times 1.5 plus 0.5 times 1.8 = 1.65
E[BMI] = E[weight] divided by E[height] squared = 70 divided by 2.7225 = 25.7
```

**13.** A programme leaflet says this.

> The expected weight loss on our programme is 4 kg. So you will lose 4 kg.

Here is the leaflet's model, which is made up. The loss is 0 kg with probability 0.3, 4 kg
with probability 0.4, and 8 kg with probability 0.3. Decide what to compute, compute it, and
say what your answer does not establish.

**14.** A health talk says this.

> A surplus of just 100 kcal a day adds up to 36,500 kcal in a year, and all of it is stored.

Decide what to compute, compute it, and say what your answer does not establish.

