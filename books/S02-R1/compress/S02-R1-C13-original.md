# S02-R1-C13 · A random variable and its distribution

**Definition.** A random variable is a rule that gives a number to each outcome of a chance process. In the
language of `B0-R0-C18`, it is a function: its inputs are the outcomes in the sample space,
and its outputs are numbers. Two outcomes may share a number. A random variable is written as
a capital letter, such as X. A value it can take is written as the same letter in lower case,
x. P(X = x) is the probability that X takes the value x.

A random variable is discrete when the values it can take can be listed, one by one. Its
probability distribution is the list of every value it can take, each paired with its
probability. The values listed must not overlap. Each probability is between 0 and 1,
inclusive, and the probabilities add to 1.

For a discrete random variable, the probability that X lands in a range is the sum of P(X = x)
over the values in that range. Adding is allowed because two different values of X cannot
both happen, so the events are mutually exclusive, as in `B0-R0-C25`.

A random variable is continuous when it can take any value in an interval, like a weight
measured with perfect precision. The probability of any one exact value is then 0. Its
probability distribution is given instead by a probability density: a curve that never goes
below zero and has a total area of 1 beneath it. The probability that X lands between a and b
is the area under the probability density from a to b. That area is the integral from a to b
of the probability density, in the sense of `S02-R1-C05`. The height of a probability density
is a probability per unit of X, not a probability, and it can be larger than 1.

A probability distribution is a model. It states the probabilities themselves. A frequency
table of data, as in `B0-R0-C27`, gives relative frequencies from the cases actually counted.
Those estimate the probabilities, and differ from them from one sample to the next.

Families of distributions with names, such as the binomial, belong to the next subject,
probability and statistical inference. This section names none of them.

**In plain terms.** Toss two coins and count the heads. The count is 0, 1 or 2. That count is a random variable:
a rule that turns each way the tosses can land into a number. Both "heads then tails" and
"tails then heads" give the number 1, and that is allowed.

Its probability distribution lists each number beside its chance. Here that is 0.25 for no
heads, 0.5 for one and 0.25 for two. Check any such list two ways. Every chance must be from 0
to 1, and the chances must add to 1.

To get the chance of a range, such as "at least one head", add the chances inside it.

Some quantities can land anywhere in a range, like the tiny amount a scale is out by when it
rounds. Then no single exact value has any chance at all, and only ranges do. The chances are
areas under a curve, and the whole area is 1.

A list of chances is a model. A count of what happened in a survey is data. The data estimate
the chances. They do not equal them.

**Illustration.** Start with a mistake that is easy to make. A made-up village has ten households. A survey
visits four of them, picked at random, and finds households of 5, 9, 4 and 5 people. The note
reads: "The probability that a household here has 5 people is 0.5." Two of the four had 5
people, and 2 divided by 4 is 0.5. See why that is not the probability.

Here is the whole village. Its ten households hold 2, 3, 4, 4, 5, 5, 5, 6, 7 and 9 people.

The chance process is "pick one household at random", with each household equally likely, as
in `B0-R0-C29`. The outcome is which household you picked. The random variable X is the rule
"give the number of people in it". Three different households give the value 5. That is
allowed, because a function may give two inputs the same output.

Each household has a chance of 1 in 10.

```working
1 divided by 10 = 0.1
```

Three households hold 5 people, so P(X = 5) is 3 times 0.1.

```working
3 times 0.1 = 0.3
```

Do the same for every value. Here is the probability distribution of X, and beside it the
relative frequencies from the survey's four households.

```table
household size (x)  households  P(X = x)  relative frequency in the survey
2                   1           0.1       0
3                   1           0.1       0
4                   2           0.2       0.25
5                   3           0.3       0.5
6                   1           0.1       0
7                   1           0.1       0
9                   1           0.1       0.25
```

Check the two rules. Every probability is between 0 and 1. Then add them.

```working
0.1 plus 0.1 plus 0.2 plus 0.3 plus 0.1 plus 0.1 plus 0.1 = 1.0
```

They add to 1. The values do not overlap, because no household has two sizes.

Now the chance of a range. The probability of a household of 6 or more is the sum over 6, 7
and 9.

```working
0.1 plus 0.1 plus 0.1 = 0.3
```

Now the note. P(X = 5) is 0.3. The survey's 0.5 is a relative frequency from four households.
It estimates 0.3, and misses it. A second survey of four would give different numbers. Neither
changes the village. The value 8 has probability 0, because no household holds 8, and nothing
in any survey can move that.

Now a variable that is not a list. A clinic scale shows weight to 0.1 kg. A person whose true
weight is anywhere from 69.95 kg to 70.05 kg sees 70.0 on it. Let X be the displayed weight
minus the true weight, in kilograms. That is the error the rounding makes. X can be any number
from −0.05 to 0.05, so it is continuous.

Say nothing makes one part of that range more likely than another. That is an assumption you
are choosing, not a fact about the scale. Then the probability density is flat across a width
of 0.1 kg, and zero outside it. At −0.1 kg or at 0.1 kg, for instance, the density is 0. Its
total area must be 1, so its height is 1 divided by the width.

```working
1 divided by 0.1 = 10
```

The height is 10 per kilogram. It is bigger than 1, and that is fine, because it is not a
probability. It is probability per kilogram of error.

The probability that the error lies between 0 and 0.02 kg is the area of a rectangle, 0.02 kg
wide and 10 per kilogram high. It is the integral of a constant, which `S02-R1-C05` computes
exactly.

```working
0.02 times 10 = 0.2
```

The kilograms cancel, and a probability is left: 0.2. Now ask for the probability that the
error is exactly 0.02. That rectangle has no width, so its area is 0. Only ranges carry
probability here.

**Where this picture breaks.** The village is made up, and the distribution is exact only because the whole village was
listed. For a real place you never have the list; you have a survey, and the survey only
estimates the distribution.

The flat density is a model chosen for want of anything better. It describes only the
rounding. A scale that reads 0.3 kg heavy every time has a systematic error, as in
`B0-R0-C30`. That error shifts every reading by the same amount and is no part of this X at
all. The model holds only for errors between −0.05 and 0.05 kg on a scale that rounds to the
nearest 0.1 kg.

**Figure.** The made-up village's household sizes. The first bar of each pair is the probability for one household picked at random; the second is the relative frequency in a survey of four. The survey puts 0.5 on 5 people where the probability is 0.3, and sees none of five other sizes.

*What the figure shows:* Paired bars for household sizes 2 to 9. Probabilities are 0.1 for sizes 2, 3, 6, 7 and 9, 0.2 for size 4 and 0.3 for size 5. The survey bars are 0.25 at size 4, 0.5 at size 5, 0.25 at size 9 and zero elsewhere.

**Figure.** The flat probability density for a scale's rounding error, 10 per kilogram from -0.05 to 0.05 kg and zero outside. The probability of an error between 0 and 0.02 kg is the area of the strip over that range, 0.02 times 10, which is 0.2.

*What the figure shows:* A step line at zero from -0.1 to -0.05, at height 10 from -0.05 to 0.05, and at zero again up to 0.1. A second line outlines the strip from 0 to 0.02 under the top of the step.

**Must know points for you.**

- A relative frequency from data is not the probability. It is an estimate of it. When a paper says "the probability was 0.3" and the 0.3 came from counting a sample, read "a sample gave 0.3". Then ask how big the sample was.
- Before you use a table that a paper calls a distribution, check it. Every probability is between 0 and 1, and they add to 1. No two rows overlap: bands of "under 60 kg" and "50 to 70 kg" count the same people twice. A table that fails any of these is not a probability distribution, however it is labelled.
- For a continuous measurement, the chance of any single exact value is zero. A probability density's height is not a probability and can be larger than 1. Ask for the chance of a range, such as 69.95 to 70.05 kg, never of "exactly 70 kg".
- Every probability you work out from a distribution is only as good as the distribution. If its shape was assumed, such as a flat density "for want of anything better", every answer carries that assumption. Say so in the same sentence, or get data that shows the shape.
- A zero in a small sample does not make a value impossible. Four households with no 3-person household do not show that the village has none. Say "not seen in this sample", never "probability zero", unless you hold the whole list.
- When you give a journalist a chance, say which kind it is. "One in three, in our model" and "one in three of the people we counted" are different claims, and only the second is a count.

**Exercise 1** (teaching). A journalist has three minutes. They have read "the probability that a household has five
members is 0.5" in a survey report of four households, and want to print it.

Explain the difference between a probability and a relative frequency from a survey. Give
them one sentence they can quote.

**1.** X takes the values 0, 1, 2 and 3, with probabilities 0.1, 0.3, 0.4 and 0.2.

Is this a probability distribution?

**2.** X takes the values 1, 2, 3 and 4. P(X = 1) is 0.25, P(X = 2) is 0.35 and P(X = 4) is 0.15.

Work out P(X = 3).

**3.** Toss two fair coins. Let X be the number of heads.

List the outcomes, and write out the probability distribution of X.

**4.** X takes the values 0, 1, 2, 3 and 4, with probabilities 0.1, 0.2, 0.4, 0.2 and 0.1.

Work out P(X ≥ 3), the probability that X is 3 or more. Then work out P(1 ≤ X ≤ 3), the
probability that X is from 1 to 3. Then work out P(X = 0) by the complement.

**5.** Three tables are offered as probability distributions for a variable taking the values 1, 2
and 3.

```table
table  P(X = 1)  P(X = 2)  P(X = 3)
a      0.3       0.3       0.3
b      0.5       -0.1      0.6
c      0.2       0.5       0.3
```

Which are probability distributions? For each that is not, name the rule it breaks.

**6.** A continuous random variable X has a flat probability density from 0 to 4, and zero density
outside that range.

Work out the height of the density. Then work out P(1 ≤ X ≤ 2.5) and P(X = 3).

**7.** A continuous random variable X has a probability density that is zero outside the range from
0 to 2. Inside it, the density rises in a straight line, from 0 at x = 0 to 1 at x = 2.

Check that the total area is 1. Then work out P(X ≤ 1).

**8.** A made-up ward has 20 patients. Eight stayed 2 days, six stayed 3 days, four stayed 4 days
and two stayed 7 days. Pick one patient at random. Let X be their length of stay, in days.

Write out the probability distribution of X. Then work out the probability of a stay of 4
days or more.

**9.** A scale shows weight to the nearest 0.2 kg. Let X be the displayed weight minus the true
weight, in kilograms. Model X as spread evenly, with a flat probability density, across its
whole range.

Work out the range of X and the height of the density, with its unit. Then work out the
probability that the error is more than 0.05 kg away from zero, in either direction.

**10.** Go back to the made-up ward of 20 patients: eight stayed 2 days, six 3 days, four 4 days and
two 7 days. A student picks five patients at random and finds stays of 2, 2, 7, 3 and 2 days.

Work out the relative frequency of a 2-day stay in the student's five. Set it beside P(X = 2)
for the ward, and say which is the model and which is the estimate.

**11.** Here is a worked answer. Find the step that broke.

```working
a scale rounds to the nearest 0.1 kg; the error X is modelled as flat from −0.05 to 0.05 kg
height of the density = 1 divided by 0.1 = 10
so P(X = 0.02) = 10
that is, an error of exactly 0.02 kg is very likely
```

**12.** Here is a worked answer. Find the step that broke.

```working
the made-up ward: 8 patients stayed 2 days, 6 stayed 3 days, 4 stayed 4 days, 2 stayed 7 days
a student samples five patients at random: stays 2, 2, 7, 3, 2
no patient in the sample stayed 4 days
so P(X = 4) = 0 for this ward: a 4-day stay does not happen here
```

**13.** Here is a worked answer. Find the step that broke.

```working
a report gives weights in three bands: under 60 kg, 0.3; 50 to 70 kg, 0.5; over 70 kg, 0.3
P(under 70 kg) = P(under 60 kg) plus P(50 to 70 kg)
0.3 plus 0.5 = 0.8
so the probability of weighing under 70 kg is 0.8
```

**14.** A clinic note says this. The counts are made up.

> In our survey, 12 of 40 patients weighed between 80 and 90 kg. So the probability that the
> next patient weighs between 80 and 90 kg is 0.3.

Decide what to compute, compute it, and say what your answer does not establish.

**15.** PAL is the physical activity level: total energy expenditure divided by basal metabolic rate.
The FAO/WHO/UNU report on energy needs says this about it.

> The PAL values that can be sustained for a long period of time by free-living adult
> populations range from about 1.40 to 2.40.

A slide then says:

> So a randomly chosen adult has a 50 per cent chance of a PAL above 1.90.

Decide what to compute, compute it, and say what your answer does not establish.

