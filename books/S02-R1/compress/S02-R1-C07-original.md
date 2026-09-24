# S02-R1-C07 · A differential equation: a rule that gives the rate from the state

**Definition.** A differential equation is an equation involving an unknown function and one or more of
its derivatives. The equations in this book are first order: they hold the first
derivative and no higher one. Each gives the rate of change of a quantity at a moment as a
rule in the value the quantity has at that moment, its state, and sometimes in the time as
well. For body weight W in kilograms and time t in days, the form is dW/dt = f(W, t).

A solution is a function of time that makes the two sides equal at every time in the range
considered, when the function and its derivative are put into the equation. Such an
equation has many solutions. An initial value, the state at one stated time, picks out one
of them. The equation and the initial value together are an initial-value problem, and a
function solves it only if it satisfies both.

The energy balance identity in rate form says the rate of change of stored energy equals
energy intake EI minus energy expenditure EE, each in kilocalories a day. Take rho, written
ρ, as the energy stored or released per kilogram of weight change, in kilocalories per
kilogram. The identity becomes ρ × dW/dt = EI − EE. This is not yet a rule that can be run
forward, because it does not say what EE will be. It becomes a differential equation once
expenditure is written as a function of weight, EE(W), and intake is either fixed or also
written as a function of weight.

With expenditure a straight line in weight, rising by epsilon, written ε, kilocalories a day
for each kilogram, and a step change ΔEI in intake from a steady starting weight W0, the
equation is:

```working
ρ × dW/dt = ΔEI − ε × (W − W0),   with W = W0 at t = 0
```

This is Equation 1 of Polidori and colleagues (2016) with its physical activity and urinary
glucose terms set to zero, rearranged. The paper calls that equation a linearization, a
straight-line version, of a fuller model of body weight.

A forward step, which is Euler's method taken one step at a time, approximates a solution.
From the state at time t, compute the rate from the equation. Then take the state at t + h
to be about W(t) + h × (the rate at t). Each step holds the rate fixed across one interval
of length h, as one rectangle does in a running total.

**In plain terms.** Book 1 gave you the energy balance identity. Over a day, the change in the body's stored energy
is what came in minus what went out. The section on the derivative let you shrink that day to
a moment. Then it reads as rates.

```working
rate of change of stored energy = EI − EE
```

EI is energy intake and EE is energy expenditure, both in kilocalories a day.

Now turn stored energy into kilograms. Say each kilogram of weight gained or lost carries a
fixed amount of energy. Call it rho, written ρ, in kilocalories per kilogram. Then the rate of
change of stored energy is ρ times the rate of change of weight.

```working
ρ × dW/dt = EI − EE
```

That line is always true. It is still no use for predicting anything. To run it forward from
today, you need tomorrow's EE, and nobody hands you that. A smaller body spends less, so EE
depends on the weight itself.

So write EE as a rule in W. The simplest rule is a straight line. It says each kilogram of
weight adds a fixed number of kilocalories a day to expenditure. Call that number epsilon,
written ε.

Now the equation gives the rate from the weight. Tell it the weight today, and it tells you
how fast the weight is moving today. That is what a differential equation is: a rule that
gives the rate from the state.

Two things follow from that.

- An answer to it is not a number. It is a whole curve of weight against time. You check a
  curve by putting it into the equation. The two sides have to agree at every moment, not
  only at the start.
- Many curves obey the same rule. The starting weight picks out the one that is yours.

You can also walk the curve without a formula. Work out today's rate from today's weight.
Move one day at that rate. Work out the new rate from the new weight. Move again. That is the
running total of rectangles from an earlier section, run forwards one day at a time.

**Illustration.** Go back to Hall and colleagues' man from Book 1. He weighs 100 kilograms and cuts his energy
intake by 2 megajoules a day. The paper converts that for you: "2 MJ per day (480 kcal per
day)". So ΔEI, the change in intake, is minus 480 kilocalories a day. Book 1's static rule
predicted about 22.6 kilograms off in the first year, and the paper's own model predicted
about half that.

You now need a value for ρ. Use 7,716.18 kilocalories per kilogram, the static rule's own
figure from Book 1. It is a stand-in that makes the arithmetic comparable with Book 1. Book
1 showed it is the rule's assumption, not a measurement of what this man's weight is made
of.

For ε, Hall and Guo (2017) give expenditure rising with weight "with a slope of about 20–30
kcal/d per kg". Take the lower end, 20 kilocalories a day for each kilogram. The man's
equation is then:

```working
7716.18 × dW/dt = −480 − 20 × (W − 100),   with W = 100 at t = 0
```

Read it in words. On the left, the rate at which his stored energy changes. On the right,
the cut in intake, plus the fall in expenditure since the start. When W is below 100,
W − 100 is negative. So minus 20 times it is positive, and it eats into the deficit.

Start with the curve that fails. The static rule says his weight falls in a straight line.

```working
480 divided by 7716.18 = 0.06221
W(t) = 100 − 0.06221 × t
```

Put that line into the equation a year in, at t = 365. The line's slope is −0.06221
kilograms a day on every day, so the left side is this.

```working
7716.18 times 0.06221 = 480.02
```

About minus 480. The small gap is rounding. Now the right side needs the weight at day 365.

```working
0.06221 times 365 = 22.71
100 minus 22.71 = 77.29
```

His weight on the line is 77.29 kilograms, 22.71 below the start.

```working
20 times 22.71 = 454.2
480 minus 454.2 = 25.8
```

The right side is about minus 25.8. The left side is minus 480. The two sides disagree by
more than 450 kilocalories a day. The straight line starts at the right weight and is not a
solution. It solves the equation only when ε is 0, that is, when expenditure ignores weight.
That is the static rule, written as a differential equation.

Now the curve that works. Here it is, handed to you. Finding it from the equation takes more
than the antiderivatives of the last section. That is the work of the second book of this
subject.

```working
W(t) = 100 − 24 × (1 − e^(-t/385.809))
```

Where do 24 and 385.809 come from? Each is a ratio of the equation's own numbers.

```working
480 divided by 20 = 24
7716.18 divided by 20 = 385.809
```

Check it the way any candidate is checked: the start, then both sides. At t = 0, e^(0) is 1.
So 1 − 1 is 0, and W is 100. The initial value holds.

For the rate, use the rule from the section on e: the derivative of e^(kt) is k times
e^(kt). Here k is minus 1 divided by 385.809. The derivative of W is then this.

```working
dW/dt = −24 × (1 divided by 385.809) × e^(-t/385.809)
24 divided by 385.809 = 0.06221
```

So dW/dt is −0.06221 × e^(-t/385.809). Take t = 365 again.

```working
365 divided by 385.809 = 0.9461
e^(-0.9461) = 0.3883
```

The left side, rounded:

```working
0.06221 times 0.3883 = 0.024156
7716.18 times 0.024156 = 186.39
```

About minus 186.4. The right side needs the weight at day 365.

```working
1 minus 0.3883 = 0.6117
24 times 0.6117 = 14.68
100 minus 14.68 = 85.32
20 times 14.68 = 293.6
480 minus 293.6 = 186.4
```

The right side is minus 186.4 as well. The two sides agree, and they would at any t you
tried. In symbols the check is two lines, both using the rule for e^(kt):

```working
left:  7716.18 × dW/dt = −480 × e^(-t/385.809)
right: −480 − 20 × (−24) × (1 − e^(-t/385.809)) = −480 + 480 − 480 × e^(-t/385.809)
```

Both come to minus 480 times e^(-t/385.809). The deficit starts at 480 kilocalories a day and
shrinks towards nothing as the weight falls.

Now walk it without the formula, one day at a time. On day 0 the weight is 100, so the
bracket is 0 and the rate is the static rule's.

```working
480 divided by 7716.18 = 0.062207
100 minus 0.062207 = 99.937793
```

On day 1 the weight is 99.937793, which is 0.062207 below the start.

```working
20 times 0.062207 = 1.24414
480 minus 1.24414 = 478.75586
478.75586 divided by 7716.18 = 0.062046
99.937793 minus 0.062046 = 99.875747
```

About 99.8757 on day 2. The formula gives 99.8759. The steps drift a little from the curve,
because each one holds the rate fixed for a whole day while the true rate keeps falling. A
smaller step drifts less. How small is small enough is also the second book's work.

Run the formula for three years and put the static line beside it. A second curve uses the
top of Hall and Guo's range, ε = 30. Its two numbers come the same way: 480 divided by 30 is
16, and 7,716.18 divided by 30 is 257.206.

```table
day   static rule, ε = 0  ε = 20 kcal/day per kg  ε = 30 kcal/day per kg
0     100                 100                     100
90    94.40               95.01                   95.28
180   88.80               91.05                   91.95
365   77.29               85.32                   87.87
545   66.10               81.84                   85.92
730   54.59               79.62                   84.94
1095  31.88               77.40                   84.23
```

All three columns come from one equation. Only ε differs. With ε at 0, the loss never
slows. With any ε above 0, the loss slows and flattens. The next section finds the level
each curve flattens at, without walking to it.

The same equation can also be run backwards. Polidori and colleagues (2016) had weights and
no reliable intake. So they worked out "the rate of change of body weight over each
interval, dBWi/dt", from the weighings. The weighings were 52 days apart: "T = 52 was the
number of days between measurements". Then they put the weight and its rate into their Equation 1 and read off
ΔEI. The intake change they report is an output of the equation, not a measurement.

**Where this picture breaks.** The value of ρ here is the static rule's 7,716.18 kilocalories per kilogram, borrowed as a
stand-in. For a real body, ρ "need not be a constant", as Chow and Hall (2008) put it. It
changes with what the weight lost is made of. So the curves in the table have the right
shape and not Hall's timing. Hall's model takes "roughly 1 year to reach half of the
maximum weight loss". The ε = 20 curve here gets halfway, 12 of its 24 kilograms, sooner.
Its half-time, from the section on e, is 385.809 times ln 2.

```working
385.809 times 0.6931 = 267.4
```

About 267 days.

The straight line for expenditure is an approximation. Polidori and colleagues call their
Equation 1 "a linearization" of a fuller model. It is safest for changes small enough that
one slope describes them. It says nothing about intake rising as weight falls, which the
next section adds.

**Figure.** Hall's 100 kg man cutting 480 kcal a day, from one equation with ρ = 7,716.18: the static rule (ε = 0) falls in a straight line to 31.88 kg by day 1095. With ε = 20 or 30 the loss slows, to 77.40 and 84.23 kg.

*What the figure shows:* Body weight against days, 0 to 1095. A straight line falls from 100 through 77.29 at day 365 to 31.88 at day 1095. Two curves fall from 100 and flatten: one through 85.32 and 79.62 to 77.40, the other through 87.87 and 84.94 to 84.23.

**Must know points for you.**

- The energy balance identity predicts nothing on its own. A prediction appears only when someone writes expenditure, and perhaps intake, as a rule in weight. When you read a projection built "on energy balance", find that rule. The prediction lives in it, and so does every assumption worth arguing about.
- A curve that starts at the right weight is not thereby a solution. The static rule's straight line starts at the right weight. A year later it is wrong by more than 450 kilocalories a day, once expenditure falls with weight. Check a claimed solution at the start and at a later time, on both sides of the equation.
- "Cut 480 kilocalories and you run a 480 deficit every day" is the static rule. In the equation the deficit is the whole right side, and it shrinks as the weight falls, because expenditure falls with it. Correct a trainee who carries the day-one deficit forward: the cut stays the same; the deficit does not.
- When you step an equation forward, work the rate out again from the new state at every step. A rate worked out once and multiplied by the whole time is the static rule again, however the working is dressed.
- Keep the units in step: ρ in kilocalories per kilogram and intake in kilocalories a day give kilograms a day. Put intake in megajoules against ρ in kilocalories and the rate comes out about 240 times too small, which no reader would catch by eye.
- This equation has one ρ and one straight-line slope. Polidori and colleagues call it a linearization, and Chow and Hall warn that ρ changes with body composition. Use it for the shape of a response and for modest changes. For one person's timetable over years, use a validated model, and say in writing which one you used.
- When a paper reports intake "calculated" from repeated weighings, read it as the output of an equation. It moves with the ρ and the ε put in. Do not quote it as though someone measured what people ate.

**Exercise 1** (interpretation). Polidori and colleagues (2016) calculate a change in energy intake from repeated
weighings with their Equation 1. The paper writes it with BW for body weight, and an i
after a symbol marks the interval.

```working
ΔEIi = ρ × (dBWi/dt) + ε × (BWi − BW0) + (Δδ divided by (1 − β)) × BW0 + UGE
```

For each symbol, say what it stands for and its unit, as far as the paper tells you. Then
say which two terms this section set to zero, and what setting each to zero assumes.

**Exercise 2** (teaching). A first-year resident has ten minutes and a whiteboard. They ask: "If energy in minus
energy out is always true, why does the same diet give smaller losses each month?"
Explain, with the equation, and expect them to want the mechanism.

**1.** A rule gives the rate of change of y as dy/dt = 6 − 0.5 × y. Work out the rate when y is
4, when y is 12, and when y is 20.

**2.** Say which of these are differential equations. For each one that is, say whether the rate
depends on the state y, or on the time t alone.

```working
(a)  y = 3t + 2
(b)  dy/dt = 3t + 2
(c)  dy/dt = −0.2 × y
(d)  E = 4P + 9F + 4C
```

**3.** Take dy/dt = 6 − 0.5 × y with y = 4 at t = 0. Take three forward steps of size 1. Give y at
t = 1, 2 and 3.

**4.** Take the initial-value problem dy/dt = 6 − 0.5 × y, with y = 4 at t = 0. Check whether
y = 12 − 8 × e^(-0.5t) solves it. Then compare its value at t = 2 with the forward steps you would get
from step size 1.

**5.** Three people offer a solution to dy/dt = 6 − 0.5 × y with y = 20 at t = 0.

```working
(a)  y = 12 + 8 × e^(-0.5t)
(b)  y = 20 − 4t
(c)  y = 12 + 4 × e^(-0.5t)
```

Which one solves the initial-value problem? Say what is wrong with each of the other two.

**6.** Hall and Guo (2017) use a cut of 300 kilocalories a day from the diet. On the first day of
the cut, the weight has not yet moved, so the whole cut is the deficit. With ρ = 7,716.18
kilocalories per kilogram, the static rule's figure, work out dW/dt in kilograms a day and
in kilograms a week.

**7.** Same cut of 300 kilocalories a day, same ρ = 7,716.18 kilocalories per kilogram. Hall and
Guo put the slope of expenditure against weight at 20 to 30 kilocalories a day per
kilogram. A person, made up for this problem, is now 4 kilograms below their starting
weight. Work out dW/dt at each end of that range.

**8.** Polidori and colleagues computed dW/dt from weighings 52 days apart. A person, made up for
this problem, weighed 98.0 kilograms at the start. They weighed 96.4 kilograms at one
weighing and 95.8 kilograms at the next, 52 days later.

Use ρ = 7,716.18 kilocalories per kilogram and ε = 30 kilocalories a day per kilogram,
Polidori's round figure for the change in expenditure. Take W − W0 at the later weighing.
Work out ΔEI with ρ × dW/dt = ΔEI − ε × (W − W0).

**9.** Polidori and colleagues describe a commercial weight-loss programme. "After 1 year, the
average energy intake was practically at baseline levels while body weight was still
reduced by ~5 kg."

Take ΔEI = 0 and W − W0 = −5 kilograms. Use ρ = 7,716.18 kilocalories per kilogram and ε at
each end of Hall and Guo's 20 to 30 kilocalories a day per kilogram. Work out dW/dt, and
the change over the next 30 days if it held. Say which way the weight is heading.

**10.** Hall and colleagues' 100 kg man cuts intake by 480 kilocalories a day. Use ρ = 7,716.18
kilocalories per kilogram and ε = 20 kilocalories a day per kilogram. Take three forward
steps of 30 days each, and give his weight at day 90. Then give the static rule's weight
at day 90, which is 100 − 480 × 90 / 7,716.18.

**11.** Here is a worked answer. Find the step that broke.

```working
the man's equation is 7716.18 × dW/dt = −480 − 20 × (W − 100), starting at 100 kg
on day 0, W − 100 is 0, so dW/dt = −480 / 7716.18 = −0.062207 kg a day
over 90 days: 0.062207 × 90 = 5.5986 kg
so the equation predicts 100 − 5.5986 = 94.40 kg at day 90
```

**12.** Here is a worked answer. Find the step that broke.

```working
a person cuts intake by 300 kcal a day; ρ = 7716.18 kcal/kg; ε = 20
model: ρ × dW/dt = ΔEI + ε × (W − W0)
4 kg below the start: −300 + 20 × (−4) = −380
dW/dt = −380 / 7716.18 = −0.04925 kg a day
so at 4 kg down the loss has sped up from 0.0389 to 0.0492 kg a day
```

**13.** Here is a worked answer. Find the step that broke.

```working
Hall's man cuts intake by 2 MJ a day
ρ = 7716.18 kcal per kg
day one: dW/dt = −2 / 7716.18 = −0.000259 kg a day
over a year: 0.000259 × 365 = 0.0946 kg
so the cut barely moves his weight
```

**14.** Here is a worked answer to the Polidori-style problem at level 5. The person weighed 98.0
kilograms at the start, then 96.4 and 95.8 kilograms at weighings 52 days apart. Take
ρ = 7,716.18 and ε = 30. Find the step that broke.

```working
dW/dt = (95.8 − 96.4) / 52 = −0.011538 kg a day
W − W0 = 95.8 − 96.4 = −0.6 kg
ΔEI = 7716.18 × (−0.011538) + 30 × (−0.6) = −89.03 − 18 = −107.03 kcal a day
```

**15.** A commentator writes: "Energy balance is only an accounting identity. Any weight
prediction built on it is circular, because it just restates that calories in minus
calories out equals the change in stores." The commentator is made up for this problem.

Decide what to compute, compute it, and say what your answer does not establish.

**16.** A review sentence reads: "Polidori and colleagues measured how much people's eating
changed, using weights taken 52 days apart." The review is made up for this problem; the
paper is real.

Decide what to compute, compute it, and say what your answer does not establish.

