# S02-R1-C03 · The few rules that do the differentiating

**Definition.** Four rules give the derivative of any sum of constant multiples of whole-number powers of
the input, without the shrinking-interval calculation.

The constant rule: the derivative of a constant is zero.

The power rule: for a positive whole number n, the derivative of x^(n) is n times x^(n minus 1).

The constant multiple rule: the derivative of k times a function is k times the derivative
of the function.

The sum and difference rules: the derivative of a sum or difference of two functions is the
sum or difference of their derivatives.

Together these give the derivative of a straight line, y = a + bx, as b at every x. The
derivative of a straight line is its slope.

The derivative of the derivative is the second derivative, written f″(x), said "f double
prime of x", or d^2y/dx^2. It is the rate of change of the rate. Where it is positive the
rate is rising, and where it is negative the rate is falling. So for a quantity that is
falling, a positive second derivative means the fall is slowing.

The derivative of a product of two functions is not the product of their derivatives. It
needs the product rule. A function of a function needs the chain rule. The power rule does
not apply to a constant raised to a power that varies, such as 2^(t).

**In plain terms.** The last section found a derivative by shrinking an interval. It worked, and it took a page.
Four rules do the same job in a line, for any rule made of powers of the input.

First, a symbol. d/dx, said "dee by dee x", means "the derivative with respect to x of what
follows". So d/dx (x^3) is the derivative of x cubed. The input can have any letter: d/dt for
time, d/dW for weight.

**The constant rule.** A constant has derivative zero. A number that never changes has a rate
of change of zero.

```working
    d/dx (7) = 0
```

**The power rule.** For x raised to a whole number n, bring the n down in front and take one
off the power.

```working
    d/dx (x^(n)) = n times x^(n minus 1)
    d/dx (x^3) = 3 x^2
    d/dx (x^2) = 2x
    d/dx (x) = 1 times x^0 = 1
```

The last line uses x^0 = 1, from `B0-R0-C06`. So x on its own has derivative 1.

**The constant multiple rule.** A number multiplying a function stays where it is. Take the
derivative of the function, then multiply.

```working
    d/dx (5 x^2) = 5 times 2x = 10x
```

**The sum and difference rules.** Take each term's derivative on its own, then add or
subtract.

```working
    d/dx (x^3 + 5 x^2 minus 4) = 3 x^2 + 10x minus 0 = 3 x^2 + 10x
```

Put the rules together on a straight line, y = a + bx. The constant a goes to zero. The term bx
becomes b times 1. So the derivative is b, the slope, at every x. That matches Book 0: a
straight line has one steepness everywhere (`B0-R0-C21`).

**The second derivative.** A derivative is itself a function, so you can take its derivative
too. The result is the second derivative, the rate of change of the rate. It is written f″(x),
said "f double prime of x", or d^2y/dx^2, said "dee two y by dee x squared".

Its sign says whether the rate is rising or falling. Here is the trap. When a quantity is
falling, its rate is below zero. A positive second derivative then means the rate is rising
towards zero. The quantity is still falling, only more slowly.

Two rules are not in this book. The derivative of a product is not the product of the
derivatives: it needs the product rule. A rule applied to the output of another rule needs the
chain rule. Both come in the rung-2 book of this subject. Until then, multiply a product out
before you differentiate.

**Illustration.** Start with the cost of the last section. It took a page of shrinking steps to find that
S(t) = 5 t^2 changes at 20 a unit of time when t = 2. Now use the rules.

```working
    S′(t) = 5 times 2t = 10t
    S′(2) = 10 times 2 = 20
    S′(3) = 10 times 3 = 30
```

The same 20, in two lines. And you now have the rate at every t at once. At t = 3 it is 30.

Next, a line from a real paper. Hall and Guo (2017) describe expenditure rising with body
weight "with a slope of about 20–30 kcal/d per kg". Take the low end and write it as a rule.
W is body weight in kilograms, and EE is energy expenditure in kilocalories a day.

```working
    EE(W) = a + 20W
```

Here a is where the line meets the side axis. The quoted sentence does not give it. That
looks like a problem. It is not. Differentiate term by term with respect to W.

```working
    d/dW (a) = 0, by the constant rule
    d/dW (20W) = 20 times 1 = 20, by the constant multiple and power rules
    dEE/dW = 0 + 20 = 20
```

Expenditure changes by 20 kcal a day for each kilogram of weight, at the low end of their
range. At the high end it is 30. You found the rate without knowing a, because a constant
contributes nothing to a rate.

Read the unit off the division. Kilocalories a day divided by kilograms is kcal a day per kg.
This rate is not against time. It says how expenditure moves as weight moves.

Now the second derivative, and a misreading of it. Hall and colleagues (2012) write that
"weight change will slow over time due to passive compensatory changes in energy
expenditure". Here is a made-up curve with that shape, for 100 days of weight loss. Its
numbers stand for nobody.

```working
    W(t) = 90 minus 0.2t + 0.001 t^2
```

W is in kilograms and t is in days. A note on this curve says this.

> The second derivative is positive, so her weight is going back up.

Differentiate once, term by term.

```working
    W′(t) = 0 minus 0.2 + 0.001 times 2t
    W′(t) = -0.2 + 0.002t
```

Differentiate again.

```working
    W″(t) = 0 + 0.002 = 0.002
```

Now put in some days.

```table
| day t | W(t) (kg) | W′(t) (kg a day) |
| 0 | 90 | -0.2 |
| 20 | 86.4 | -0.16 |
| 40 | 83.6 | -0.12 |
| 60 | 81.6 | -0.08 |
| 80 | 80.4 | -0.04 |
| 100 | 80 | 0 |
```

Here is one row in full, day 20.

```working
    W(20) = 90 minus 0.2 times 20 + 0.001 times 20 times 20 = 86.4
    W′(20) = -0.2 + 0.002 times 20 = -0.16
```

The first derivative is below zero on every row until day 100. Weight is falling the whole
time. The second derivative is positive, 0.002 kg a day per day. That says the rate is
rising: from minus 0.2 towards zero. The fall is slowing. Weight is not going back up.

The note read the sign of the second derivative as if it were the sign of the first.

**Where this picture breaks.** The straight line EE = a + 20W holds only over the range of weights the slope was measured
on. Hall and Guo give it as "about 20–30", a range, not one person's value.

The curve W(t) is made up to fall and slow for 100 days, and holds nowhere else. Run it past
day 100 and it turns. At day 150 it gives a rate of plus 0.1 kg a day, and weight climbing
back to 82.5 kg. That is a property of this made-up curve, not a prediction about anyone. A
curve with two powers of t has no reason to follow a body beyond the days it was made for.

**Figure.** The made-up curve W(t) = 90 minus 0.2t + 0.001 t^2 over 100 days. Weight falls from 90 kg to 80 kg, and the fall slows as it goes: the curve flattens because its second derivative, 0.002, is positive.

*What the figure shows:* Six points from day 0 to day 100 on a falling curve that flattens: 90, 86.4, 83.6, 81.6, 80.4 and 80 kilograms.

**Figure.** The same curve's first derivative, W′(t) = -0.2 + 0.002t. It is below zero on every day before day 100, so weight is falling throughout. It climbs towards zero at 0.002 kg a day per day, the second derivative, so the fall is slowing.

*What the figure shows:* A rising straight line of six points from minus 0.2 kilograms a day at day 0 to 0 at day 100, passing minus 0.16, minus 0.12, minus 0.08 and minus 0.04.

**Must know points for you.**

- The derivative of a straight line is its slope, and the constant drops out. So you can read how fast expenditure changes with weight, 20 to 30 kcal a day per kg, without knowing where the line starts.
- A positive second derivative does not mean the quantity is rising. When weight is falling, a positive second derivative means the fall is slowing. Read the sign of the first derivative for the direction, and the second for whether it is speeding up or slowing down.
- Slowing weight loss is what passive compensation predicts, even with no change in the treatment. A positive second derivative is not by itself evidence that a treatment has stopped working.
- The derivative of a product is not the product of the derivatives. Multiply the product out first, or wait for the product rule. The same care applies to a power with the variable up in the exponent, such as 2^(t): the power rule does not reach it.
- These rules differentiate a formula exactly. They say nothing about whether the formula fits the body. Fit a curve with t^2 in it to 100 days, and it will turn round after that. The turn comes from its form, not from anything in the patient.
- Check a derivative you worked out by rule with the shrinking-interval method at one point. One row of that table catches a wrong rule faster than rereading the algebra.

**Exercise 1** (teaching). A journalist has three minutes. A press release says weight loss on a drug "slowed after six
months, showing its effect wears off". The press release is made up for this exercise.

Explain, without any symbols, what slowing weight loss does and does not tell you. Give them
one sentence they could quote.

**1.** Find each derivative.

```working
    d/dx (9)
    d/dx (x^6)
    d/dx (x)
```

**2.** Find each derivative.

```working
    d/dx (4 x^3)
    d/dt (-2 t^5)
```

**3.** Find the derivative of f(x) = 3 x^4 minus 2x + 6.

**4.** Take f(t) = 2 t^3 minus t. Find f′(t), then its value at t = 2.

**5.** Take f(t) = t^3 minus 6 t^2 + 4.

Find f′(t) and f″(t). Then work out both at t = 1 and at t = 3, and say in words what f is
doing at each.

**6.** Take the straight line y = 7 minus 0.4x. Find its first and second derivatives.

**7.** Hall and Guo (2017) give expenditure rising with body weight at "a slope of about 20–30
kcal/d per kg". Treat expenditure as a straight line in weight with that slope.

A person loses 8 kg. Work out how much their expenditure changes along the line, at each end
of the range. Give the unit.

**8.** Table 5.2 of the FAO/WHO/UNU report (2004) estimates basal metabolic rate from body weight.
For men aged 18 to 30 it is 15.057 times weight in kg, plus 692.2, in kcal a day.

Find dBMR/dW with its unit. Then work out BMR at 60 kg and at 70 kg, and check the difference
against the derivative.

**9.** The same FAO/WHO/UNU report multiplies BMR by the physical activity level, PAL, to get total
energy expenditure, TEE. Its worked example uses a PAL of 1.75.

Using the Table 5.2 line for men aged 18 to 30, BMR = 15.057W + 692.2, find dTEE/dW at a PAL of
1.75. Compare it with Hall and Guo's slope of "about 20–30 kcal/d per kg" for expenditure. Say
what the comparison does and does not show.

**10.** A made-up weight curve is W(t) = 84 minus 0.15t + 0.0005 t^2, with W in kg and t in days.

Find W′(60) and W″(t), with units. Say what W is doing at day 60. Then find the day on which
W′ reaches zero.

**11.** Here is a worked answer. Find the step that broke.

```working
    f(x) = 3 x^2 + 5
    d/dx (3 x^2) = 6x
    d/dx (5) = 5
    f′(x) = 6x + 5
    so f′(0) = 5
```

**12.** Here is a worked answer. Find the step that broke.

```working
    g(t) = 2^(t)
    by the power rule, g′(t) = t times 2^(t minus 1)
    so g′(1) = 1 times 2^0 = 1
```

**13.** Here is a worked answer. Find the step that broke.

```working
    h(t) = t^2 times t^3
    d/dt (t^2) = 2t and d/dt (t^3) = 3 t^2
    the derivative of a product is the product of the derivatives
    h′(t) = 2t times 3 t^2 = 6 t^3
    so h′(1) = 6
```

**14.** Here is a worked answer. Find the step that broke.

```working
    a patient's weight follows W(t) = 95 minus 0.3t + 0.002 t^2 over 60 days
    W″(t) = 0.004, which is positive
    a positive derivative means rising
    so from day 1 the patient's weight has been going up
```

The curve is made up for this problem.

**15.** A colleague says this at a case meeting.

> Each kilo she loses cuts her expenditure by 20 to 30 kcal a day. She has lost 10 kg. So she
> only needs to eat 200 to 300 kcal less than when she started to keep losing at the same
> speed.

The patient is made up. The slope is Hall and Guo's (2017). Decide what to compute, compute
it, and say what your answer does not establish.

**16.** A news report on a weight-loss medicine says this.

> Patients lost weight quickly at first, but loss slowed after month 6, which suggests the
> medicine stopped working.

The report is made up, and so are these monthly average weights for the group.

```table
month  weight (kg)
0      100
1      97
2      94.5
3      92.5
4      91
5      90
6      89.3
7      88.8
8      88.5
```

Decide what to compute, compute it, and say what your answer does not establish.

