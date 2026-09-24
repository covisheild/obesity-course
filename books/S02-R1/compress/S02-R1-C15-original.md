# S02-R1-C15 · Variance, and why independent errors add as squares

**Definition.** This section stands on the last two. A random variable X gives a number to each outcome of a
chance process, and its expected value E[X] is the sum of its values, each weighted by its
probability.

The variance of X, written Var(X) and said "the variance of X", is the expected value of the
squared deviation of X from E[X]. In symbols:

```working
Var(X) = E[(X − E[X])²]
```

For a random variable with a list of values, that is the sum, over every value x, of
(x − E[X])² times the probability of x. The standard deviation of X, written with the Greek
letter sigma, σ, is the square root of Var(X). It carries the unit of X. The variance carries
that unit squared.

For fixed numbers a and b, the variance of aX + b is a² times the variance of X. Adding b
moves every value and leaves the spread alone. The standard deviation of aX + b is σ times
the size of a, whatever the sign of a.

```working
Var(aX + b) = a² Var(X)
```

Two random variables are independent when every event about one is independent, in the sense
of `B0-R0-C25`, of every event about the other. For independent X and Y, the variance of their sum
is the sum of their variances, and so is the variance of their difference.

```working
Var(X + Y) = Var(X) + Var(Y)
Var(X − Y) = Var(X) + Var(Y)
Var(aX + bY) = a² Var(X) + b² Var(Y)
```

Standard deviations do not add. For independent parts, the standard deviation of the sum is
the square root of the sum of the squared standard deviations.

For n independent random variables, each with variance σ², the sum has variance nσ² and
standard deviation σ times the square root of n. Their mean has standard deviation σ divided
by the square root of n, which is the square-root law of `B0-R0-C29`.

Without independence the adding rule fails. A correction term, the covariance, enters, and
S03-R1 teaches it.

**In plain terms.** The expected value says where a chancy quantity sits on average. The variance says how far it
strays from there.

Take each value's distance from the expected value and square it. Weight each square by that
value's probability, and add them up. Squaring does two jobs. A miss below counts the same as a
miss above, so the two cannot cancel. And a big miss counts for much more than a small one.

The answer is in squared units: square grams, if the quantity was in grams. Take its square root
and you are back in grams. That is the standard deviation, the figure you set beside a mean.

Now add two uncertain amounts whose errors have nothing to do with each other. The spread of the
total grows, but by less than the two spreads added. A high on one often meets a low on the other.

Subtract them instead, and the spread grows by exactly the same amount. Subtracting does not
cancel uncertainty. A difference between two measured amounts is less certain than either of
them. Energy intake minus energy expenditure is such a difference.

Add up many days whose errors are independent, and the spread of the total grows with the square
root of the number of days. An error that is the same every day does not behave like this. It
grows in step with the days.

**Illustration.** You weigh dal on a cheap kitchen scale, by difference. Weigh the empty katori. Put the dal in
and weigh again. The dal's weight is the second reading minus the first.

Suppose each reading is off by minus 10, 0 or plus 10 grams, with probabilities 0.25, 0.5 and
0.25. These numbers are made up. Suppose too that the error of one reading tells you nothing
about the error of the other, so the two are independent. Call the error of one reading X.

Find its expected value first: each value times its probability, added up.

```working
-10 times 0.25 plus 0 times 0.5 plus 10 times 0.25 = 0
```

Now the variance. Each value's deviation from 0 is the value itself. Square it, weight it by
its probability, and add.

```working
100 times 0.25 plus 0 times 0.5 plus 100 times 0.25 = 50
```

Var(X) is 50 square grams. The standard deviation is the square root of 50, about 7.07 grams.

The dal's error is the second reading's error minus the first's. Work out its distribution by
listing the pairs. Because the readings are independent, multiply to get each pair's
probability, the rule from `B0-R0-C25`. An error of minus 20 grams happens only when the second
reading is 10 low and the first is 10 high.

```working
0.25 times 0.25 = 0.0625
```

An error of minus 10 happens two ways: second 10 low and first right, or second right and
first 10 high. Add the two ways.

```working
0.25 times 0.5 plus 0.5 times 0.25 = 0.25
```

An error of 0 happens three ways: both low, both right, or both high.

```working
0.25 times 0.25 plus 0.5 times 0.5 plus 0.25 times 0.25 = 0.375
```

The positive errors mirror the negative ones. Set the two distributions side by side.

```table
error (g)  one reading  the dal, by difference
-20  0  0.0625
-10  0.25  0.25
0  0.5  0.375
10  0.25  0.25
20  0  0.0625
```

The dal's expected error is 0, by the same symmetry. Its variance, from the squared errors:

```working
400 times 0.0625 plus 100 times 0.25 plus 0 times 0.375 plus 100 times 0.25 plus 400 times 0.0625 = 100
```

Now check the rule. The variance of a difference of independent errors is the sum of their
variances.

```working
50 plus 50 = 100
```

It agrees. The dal's standard deviation is the square root of 100, which is 10 grams. Each
reading alone had about 7.07. You subtracted, and the error grew.

Notice what did not happen. Adding the two standard deviations gives about 14.14 grams, and
that is wrong. Variances add; standard deviations do not.

Now carry the rule from grams to energy. Hall and colleagues wrote a consensus statement on
energy balance. It puts the uncertainty of expenditure measured by doubly labelled water at
more than 100 kilocalories (kcal) a day. It gives the same figure as 420 kilojoules (kJ) a
day. Doubly labelled water is Book 1's method
for measuring what a person actually spent.

Converting kcal to kJ multiplies every value by 4.184, the factor in `B0-R0-C12`. So a spread in kJ is a
spread in kcal times 4.184. Take 100 kcal a day as the floor of the standard deviation.

```working
100 times 4.184 = 418.4
```

The paper rounds this to 420. Why does the standard deviation scale by 4.184 and the variance
by 4.184 times 4.184? Derive it, naming each move. Call the error in kcal X, and the same
error in kJ aX + b, with a = 4.184 and b = 0. Keep b in, because the same steps show what an
added constant does.

First, the expected value of aX + b is a times E[X] plus b. The last section showed that.

Second, subtract it from aX + b. Substitute, then collect terms.

```working
(aX + b) − (aE[X] + b) = aX − aE[X] = a(X − E[X])
```

The b has gone. Adding a constant moves every value and its expected value together.

Third, square both sides.

```working
((aX + b) − E[aX + b])² = a² (X − E[X])²
```

Fourth, take the expected value of both sides. The a² is a fixed number, so it comes outside,
by the rule for E[aX] from the last section. The left side is now the variance of aX + b. The
right is a² times the variance of X.

```working
Var(aX + b) = a² Var(X)
```

With a = 4.184, the variance in kJ is 4.184 times 4.184, about 17.5, times the variance in
kcal. The standard deviation, its square root, is 4.184 times the standard deviation in kcal.

Now the difference that matters most in this subject. The energy imbalance of a day is energy
intake (EI) minus energy expenditure (EE). If you work it out from a measured intake and a
measured expenditure, it is a difference of two uncertain amounts.

Take the expenditure error's standard deviation as 100 kcal a day, the floor from above. Hall and colleagues give no figure for intake measured by self-report. They say
only that its accuracy and precision "are much worse". So suppose, as a made-up figure, that
the intake error has a standard deviation of 300 kcal a day. Suppose too that the two errors
are independent. The variance of the imbalance is the sum of the two variances.

```working
100 times 100 plus 300 times 300 = 100000
```

The standard deviation of the imbalance is the square root of 100,000, about 316.2 kcal a day.
It is at least that, because 100 was a floor. Even with intake measured perfectly, the
imbalance could be no more certain than the expenditure: at least 100 kcal a day.

Now add up days. Take two made-up cases, each with an intake error of 300 kcal on a single
day. In the first, each day's error is independent of every other day's. In the second, the
record under-counts by the same 300 kcal every day.

In the first case the variance of an n-day total is n times the variance of one day. So its
standard deviation is 300 times the square root of n. Over 9 days the square root of 9 is 3.

```working
300 times 3 = 900
```

In the second case nothing varies. The total error is 300 times n.

```working
300 times 9 = 2700
```

```table
days  independent daily errors (kcal)  same under-count every day (kcal)
1  300  300
4  600  1200
9  900  2700
16  1200  4800
```

Divide by the days to get the error in the average day. In the first case it shrinks: 300
divided by the square root of 16 is 75 kcal a day. That is the square-root law of `B0-R0-C29`. In the
second case it stays at 300 kcal a day however long you record. That is the systematic error
of `B0-R0-C30`, which more readings do not shrink.

**Where this picture breaks.** The three-value error is made up so that you can list every pair by hand. A real scale's
reading error takes many values, and the rule still holds as long as the two readings'
errors are independent.

A real scale also has systematic error, the kind `B0-R0-C30` separates from random error. If the
scale reads 5 grams heavy every time, that 5 grams sits in both readings and cancels in the
difference. Weighing by difference removes an error shared by both readings and adds up the
variances of the parts that are not shared.

The derivation of Var(aX + b) needs a and b to be fixed numbers. A conversion factor is fixed by agreement,
so it qualifies. A factor that is itself measured, and so uncertain, is not a fixed number,
and the rule does not apply to it as it stands.

The 100 kcal a day is a floor: the paper says more than 100. It also does not say which
measure of spread its uncertainty is. Reading it as a standard deviation is your assumption.

The 300 kcal a day is made up, and so is the choice between the two cases. A real food record
carries both kinds of error at once, and nobody can split them from the record alone.

The adding rule also needs the intake and expenditure errors to be independent. That is an
argument you make, not a fact the numbers give you. And one measurement by doubly labelled
water is already an average over many days. Its error is not a new, independent draw each
day.

**Figure.** The error of one made-up reading (minus 10, 0 or 10 grams) and of the dal weighed by difference. The difference spreads from minus 20 to 20 grams: its variance is 100, the sum of the two readings' 50 and 50.

*What the figure shows:* Paired bars at errors of minus 20, minus 10, 0, 10 and 20 grams. One reading has bars 0.25, 0.5 and 0.25 at the middle three errors. The difference has 0.0625, 0.25, 0.375, 0.25 and 0.0625, lower in the middle and reaching both ends.

**Figure.** The error in a total of n days, from made-up daily errors of 300 kcal. Independent errors grow as 300 times the square root of n, reaching 1200 at 16 days. The same under-count every day grows as 300 times n, reaching 4800.

*What the figure shows:* Two lines over 1, 4, 9 and 16 days. The independent-error line rises 300, 600, 900, 1200. The repeated under-count line rises 300, 1200, 2700, 4800, pulling far above it.

**Must know points for you.**

- Subtracting one measured amount from another does not cancel their errors. When the errors are independent their variances add, so a difference such as intake minus expenditure is less certain than either figure it came from. Treat a small difference between two large measured amounts as the least trustworthy number on the page.
- Hall and colleagues say expenditure measured by doubly labelled water can be off by more than 100 kcal a day. Take measured intake minus that expenditure. The gap you get is at least as uncertain. That holds however well intake is measured. So do not accept one person's measured imbalance quoted as if it were known to within 50 kcal a day.
- Standard deviations do not add. Square each one, add the squares, and take the square root of the total. Adding the standard deviations of independent parts overstates the spread of their sum.
- The adding rule, and the square-root growth over days, hold only for independent errors. An under-count repeated every day grows in step with the days, and averaging does not shrink it. Before you use the rule, make the independence argument `B0-R0-C25` asks for. If you cannot make it, do not quote a spread built on the rule. Look for an independent check of the bias instead.
- Two measurements of the same person are rarely independent. A before-and-after change, or a predicted-minus-actual difference, can then spread much less than the adding rule says. Do not call a reported spread wrong only because it fails the rule on paired figures.
- When a paper subtracts a baseline, ask whether the baseline was a fixed number or a measurement. Taking away a fixed number leaves the spread alone. Taking away a measured baseline adds that baseline's variance to the change.
- Suppose a patient's food diary shows a deficit of a few hundred kcal a day and their weight has not moved. Do not treat the diary as the fixed truth and their body as the puzzle. Hall and colleagues say the combined error of a measured imbalance can easily reach 1000 kcal a day. That is far more than the diary's deficit.
- Teach a trainee to convert a variance to a standard deviation before setting it beside a mean. A variance is in squared units, such as square grams. Set beside a mean, it looks far larger or smaller than the spread really is.

**Exercise 1** (interpretation). Here is a line from a methods section about the error in an energy imbalance. X is the error
in measured intake, and Y the error in measured expenditure, both in kcal a day.

```working
Var(X − Y) = Var(X) + Var(Y)
```

Say what each symbol denotes, and what unit each term carries. Say what condition the line
needs, and why the minus sign on the left becomes a plus on the right.

**Exercise 2** (teaching). A journalist asks why a study cannot simply measure whether a new snack changes a person's
energy balance by 50 kcal a day. You have three minutes and no jargon. Give one quotable
sentence.

**1.** A random variable takes the values 2, 4 and 6 with probabilities 0.25, 0.5 and 0.25.

Work out its expected value, its variance and its standard deviation.

**2.** A random variable takes the value 0 with probability 0.8 and the value 10 with probability
0.2.

Work out its expected value, its variance and its standard deviation.

**3.** 1. A variance is 9. What is the standard deviation?
2. A standard deviation is 0.5. What is the variance?
3. A variance is 0.49. What is the standard deviation?

**4.** Var(X) = 4. Work out the variance and the standard deviation of 3X + 7, and of −2X + 5.

**5.** X and Y are independent. Var(X) = 9 and Var(Y) = 16.

Work out the variance and standard deviation of X + Y, and of X − Y. Then add the two standard
deviations of X and Y, and compare.

**6.** Nine independent random variables each have standard deviation 2.

Work out the standard deviation of their sum, and the standard deviation of their mean.

**7.** A day's error has standard deviation 10. The errors on different days are independent. Over
how many days does the standard deviation of the total reach 30?

**8.** Hall and colleagues give doubly labelled water "a precision of" about 5% (Hall 2012). They say
this "translates to an uncertainty of energy expenditure of" more than 100 kcal a day, or 420
kJ a day.

1. At what daily expenditure is 5% exactly 100 kcal a day?
2. Take 100 kcal a day as a standard deviation. Convert it to kJ a day, using 4.184 kJ in a
   kcal, and compare with the paper's 420.
3. By what number is the variance multiplied in that conversion?

**9.** The error in a person's expenditure, measured by doubly labelled water, has a standard
deviation of at least 100 kcal a day (Hall 2012). Suppose the error in their reported intake
has a standard deviation of 250 kcal a day. That figure is made up. The two errors are
independent.

Work out the standard deviation of the error in their energy imbalance, and say whether your
answer is a ceiling or a floor.

**10.** Keep the imbalance error from the last problem, a standard deviation of about 269.3 kcal a
day. Suppose the errors on different days are independent.

Work out the standard deviation of the error in the total imbalance over 7 days, and in the
average daily imbalance over those 7 days.

**11.** Hall and colleagues write that "the combined error of assessing energy imbalance can easily
reach 1000 kcal/d" (Hall 2012). They put the expenditure error at more than 100 kcal a day.

Read the 1,000 as a standard deviation, and the expenditure part as exactly 100. Suppose the
intake and expenditure errors are independent. What standard deviation of the intake error
would give the 1,000?

**12.** Here is a worked answer. Find the step that broke.

```working
intake error: standard deviation 300 kcal a day
expenditure error: standard deviation 100 kcal a day, independent of the intake error
the imbalance is intake minus expenditure, so its error is 300 minus 100
standard deviation of the imbalance error = 200 kcal a day
```

**13.** Here is a worked answer. Find the step that broke.

```working
Var(X) = 4
Var(3X) = 3 times Var(X) = 12
standard deviation of 3X = the square root of 12, about 3.46
```

**14.** Here is a worked answer. Find the step that broke.

```working
in a made-up group, reported intake under-counts by 300 kcal on every day
over 30 days, the errors add up as the square root of the days
error in the 30-day total = 300 times the square root of 30, about 1643 kcal
```

**15.** Here is a worked answer. Find the step that broke.

```working
the error of one reading on a scale has standard deviation 7 grams
a portion is weighed by difference: full bowl minus empty bowl
the bowl's weight is subtracted, so its error is removed
error of the portion = 7 grams
```

**16.** Thomas and colleagues pooled seven weight-loss studies. They report that participants "lost
20.1±11.3 lbs, 7.4±12.6 lb less than the 27.6±16.0 lbs predicted by the 3500 kcal rule"
(Thomas 2013). Their methods paragraph writes figures in the form mean ± standard deviation.

A reader says: "The difference is predicted minus actual, so its standard deviation should be
the square root of 11.3 squared plus 16.0 squared. That is about 19.6, not 12.6, so the 12.6
is a typo."

Decide what to compute, compute it, and say what your answer does not establish.

**17.** A calorie-counting app's advert says this.

> Our entries are accurate to within 50 kcal per item. So your daily log of 12 items is
> accurate to within 50 kcal.

The figures are the advert's own and are made up for this problem. Decide what to compute,
compute it, and say what your answer does not establish.

**18.** Thomas and colleagues report three figures for the same 103 adults (Thomas 2013). Baseline
energy intake was 2876±484 kcal a day. The prescribed target intake was 1409±569 kcal a day.
And they report "an average deficit of 1439±784 kcal/d". The figures after ± are standard
deviations.

A reviewer writes: "The deficit is baseline intake minus target intake. If those are
independent, its standard deviation must be the square root of 484 squared plus 569 squared.
That is about 747, so the reported 784 is too large."

Decide what to compute, compute it, and say what your answer does not establish.

