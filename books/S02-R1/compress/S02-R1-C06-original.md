# S02-R1-C06 · Undoing a derivative: antiderivatives and the fundamental theorem

**Definition.** An antiderivative of a function f is a function F whose derivative is f, so that dF/dt = f(t).
If F is one antiderivative, F plus any constant C is another, and on an interval every
antiderivative of f has that form. The family is written ∫ f(t) dt = F(t) plus C, with no
limits on the sign, and is called the indefinite integral.

Each of these is checked by differentiating back, with the rules of `S02-R1-C03` and
`S02-R1-C04`:

```table
the function f(t)             an antiderivative F(t)
a constant c                  c times t
t^(n), for n a whole number   t^(n plus 1) divided by (n plus 1)
e^(kt), for k not zero        e^(kt) divided by k
```

Sums and constant multiples are done term by term. The same form holds for most other powers
as well, but never for n = -1, where it would divide by zero. Checking it for powers that are
not whole numbers needs a power rule this book does not teach.

The fundamental theorem of calculus, in the part called the evaluation theorem, says this.
If f is continuous from a to b and F is any antiderivative of f, then ∫ from a to b of f(t) dt
= F(b) minus F(a). The constant C cancels in the subtraction, so any antiderivative gives the
same answer.

Put together with the net change theorem of `S02-R1-C05`, the change in a stock over an
interval is found from any function whose rate is the given rate, evaluated at the two ends.

For a deficit D(t) = D0 e^(-kt), with D0 its value at t = 0 and k above zero, the total from
0 to T is D0 times (1 minus e^(-kT)) divided by k. That is less than D0 times T, the total of
a deficit held at D0. However long T runs, it never exceeds D0 divided by k.

**In plain terms.** `S02-R1-C05` worked out integrals from shapes: rectangles, triangles, trapeziums. That works only
for a rate that is steady or changes in a straight line. Most rates bend. This section gives a
way that does not need a shape.

Start from what you already know. `S02-R1-C03` and `S02-R1-C04` take a function and give its
rate. Now run that backwards. Given a rate, find a function whose rate it is. That function is
called an antiderivative.

Say the rate is 2t. Which function has the rate 2t? The power rule says t^2 does. So t^2 is an
antiderivative of 2t.

So is t^2 plus 5, and t^2 plus any fixed number. A fixed number has a rate of zero, so adding
one changes nothing about the rate. That is why an antiderivative is written with plus C on the
end, where C is any constant.

You never have to trust an antiderivative. Differentiate it and see whether the rate comes back.
Three rules cover this book.

```table
the rate                  an antiderivative
a steady rate c           c times t
t^(n), n a whole number   t^(n plus 1) divided by (n plus 1)
e^(kt)                    e^(kt) divided by k
```

Check the middle one on t^2. Its antiderivative should be t^3 divided by 3. Differentiate that.
The power rule brings down the 3 and takes one off the power, giving 3 t^2 divided by 3, which
is t^2. It comes back.

Check the last one. The rate of e^(kt) is k times e^(kt) (`S02-R1-C04`). Divide by k and you
get e^(kt) back.

Now the step that makes this worth doing. The fundamental theorem of calculus says an integral
is the antiderivative at the end minus the antiderivative at the start.

```working
∫ from a to b of f(t) dt = F(b) minus F(a)
```

Here F is any antiderivative of f. The C cancels, because it is added at both ends and then
subtracted. So leave it out when you work out an integral.

Why is this true? `S02-R1-C05` said the integral of a rate is the change in the stock. An
antiderivative is a stock with that rate. Its change from a to b is F(b) minus F(a). That is
the whole idea.

**Illustration.** Hall and colleagues model a man who cuts his intake by 2 megajoules a day (*Lancet* 2011).
Keep the deficit at 2 megajoules a day, as the static rule of `S01-R1-C07` does. Then one year
of it is a rectangle.

```working
2 times 365 = 730
```

Seven hundred and thirty megajoules in the first year. So a deficit of 2 megajoules a day is
730 megajoules a year.

His expenditure falls as his weight falls, so his real deficit shrinks. Suppose, to see the
arithmetic, that it halves every year. This shape is made up here, and it is not the paper's
model. A half-time of 1 year means k = 0.693 per year (`S02-R1-C04`). With t in years, the
deficit in megajoules a year is this.

```working
D(t) = 730 e^(-0.693t)
```

A trainee works out the first year's total. They remember that e^(t) is its own rate, so they
take the antiderivative of 730 e^(-0.693t) to be 730 e^(-0.693t) itself. At the end of the
year that is 730 times 0.5.

```working
730 times 0.5 = 365
365 minus 730 = -365
```

Minus 365 megajoules. But the deficit stayed above zero all year. A rate that never drops
below zero cannot add up to a total below zero.

Find the break by differentiating back. The rate of 730 e^(-0.693t) is -0.693 times 730
e^(-0.693t). That is not the deficit. It is -0.693 times the deficit. So divide by -0.693 to
cancel that factor.

```working
730 divided by 0.693 = 1053.4
F(t) = -1053.4 e^(-0.693t)
```

Check it. The rate of F is -0.693 times -1053.4 e^(-0.693t), which is 730 e^(-0.693t). It
comes back. Now take F at the end of the year minus F at the start. On the calculator,
e^(-0.693) is 0.5001, and e^0 is 1.

```working
F(1) minus F(0) = -1053.4 times 0.5001 plus 1053.4
1053.4 times (1 minus 0.5001) = 1053.4 times 0.4999
1053.4 times 0.4999 = 526.6
```

About 526.6 megajoules in the first year, against 730 for the steady deficit. Run the same
sum at other times and set the two side by side.

```table
| years | steady deficit, total so far (MJ) | halving deficit, total so far (MJ) |
| 0 | 0 | 0.0 |
| 0.5 | 365 | 308.5 |
| 1 | 730 | 526.6 |
| 1.5 | 1095 | 680.9 |
| 2 | 1460 | 790.0 |
| 2.5 | 1825 | 867.1 |
| 3 | 2190 | 921.7 |
```

The steady deficit's total climbs in a straight line, 730 more every year for ever. The
halving deficit's total bends. As T grows, e^(-0.693T) shrinks towards zero, so its total
creeps up towards 1053.4 megajoules and never passes it.

Hall and colleagues' own model puts the static rule's first-year loss at "about 100% greater
weight loss than our model prediction". This made-up halving deficit gives a smaller gap:
526.6 against 730. It is not their model. What it shows is the direction and the reason. A
deficit that shrinks adds up to less. How much less depends on how fast it shrinks, and working
that out is the model's job, in `S02-R1-C07`.

Last, a check that the theorem agrees with the shapes you already trust. Take a different
made-up deficit that falls in a straight line, from 730 to 365 megajoules a year over the first
year.

```working
D(t) = 730 minus 365t
```

Use the power rule term by term. The steady 730 gives 730t. The 365t gives 365 times t^2
divided by 2.

```working
365 divided by 2 = 182.5
F(t) = 730t minus 182.5 t^2
```

Differentiate back: 730 minus 2 times 182.5t, which is 730 minus 365t. It comes back. Now the
first year.

```working
730 times 1 minus 182.5 times 1 = 547.5
```

Now the trapezium from `S02-R1-C05`.

```working
730 plus 365 = 1095
1095 divided by 2 = 547.5
```

Both give 547.5 megajoules. The theorem does what the trapezium did. It also works where no
shape has an area formula, as the halving deficit showed.

**Where this picture breaks.** Both shrinking deficits are made up, one halving each year and one falling in a straight line.
They show how an integral treats a shrinking rate. They do not say how a real person's
deficit shrinks. The straight line would reach zero at two years and then go below it, so it
means nothing beyond the first year.

Every total here is energy, in megajoules. Turning it into kilograms needs to know what tissue
was lost (`S01-R1-C02`), and that is part of why Hall's model differs from the static rule.

**Figure.** The total of a steady deficit of 730 megajoules a year climbs in a straight line. A made-up deficit that halves each year adds up to 526.6 in the first year and levels off towards 1053.4 megajoules, which it never passes.

*What the figure shows:* Two lines over 0 to 3 years. A straight line rises from 0 to 2190. A curve rises from 0 through 526.6 at year 1 to 921.7 at year 3, bending under a dashed level at 1053.4.

**Must know points for you.**

- Check every antiderivative by differentiating it. If the rate you started with does not come back, the antiderivative is wrong, however reasonable it looks. It takes one line.
- The antiderivative of e^(kt) is e^(kt) divided by k, not e^(kt). Dropping the k gives the wrong size. For a shrinking curve, where k is negative, it also gives the wrong sign. The unit is a second check. Dividing by a rate constant in per year multiplies by years, which turns a rate into an amount.
- "The deficit never quite reaches zero, so the loss keeps going for ever" is wrong as arithmetic. A deficit D0 e^(-kt) adds up to at most D0 divided by k, however long it runs. A rate that never reaches zero can still have a total that stops growing.
- These rules cover steady rates, whole-number powers of t, e^(kt), and sums and multiples of them. A model's real rate is often none of these. When no antiderivative is at hand, go back to rectangles and bound the error as `B0-R0-C22` does. Do not force a formula that does not fit. The other techniques belong to the next rung.
- A figure made by multiplying a daily deficit by 365, and then by a number of years, is a steady-deficit total. It grows in a straight line for as long as you let it. Any deficit that shrinks adds up to less. In a committee, call such a figure an upper limit that holds only if the deficit never shrinks.
- Take F at the upper limit minus F at the lower limit, in that order. The reverse gives the right size with the wrong sign. A positive rate must give a positive total, so check the sign before the number leaves your page.

**Exercise 1** (calculation). A deficit shrinks as D(t) = D0 e^(-kt), where D0 is its size at t = 0 and k is above zero.
Derive the total from t = 0 to t = T. Write beside each line the move you made. Then say what
the total approaches as T grows, and why.

**1.** Write an antiderivative of each: 6, 4t, 3 t^2, and t^3 plus 2t. Check each by differentiating
it.

**2.** Work out ∫ from 1 to 3 of 3 t^2 dt.

**3.** Work out ∫ from 0 to 2 of e^(3t) dt, to two decimal places.

**4.** Work out ∫ from 0 to 4 of 10 e^(-0.5t) dt, to two decimal places.

**5.** Work out ∫ from 2 to 5 of 2t dt twice: once with the antiderivative t^2, and once with t^2
plus 5. Say what happened to the 5.

**6.** A rate is 10 e^(-0.5t). Work out its total from t = 0 onwards, over all time. Then work out
how long it takes to add up to 95% of that.

**7.** Hall and colleagues (*Lancet* 2011) model a cut in intake of 480 kilocalories a day. Suppose
a person's net deficit starts at 480 and falls by 0.5 kilocalories a day every day. That fall
is made up for this problem. Use an antiderivative to work out the total deficit over 200 days.
Then check it with the trapezium.

**8.** Take the same deficit of 480 kilocalories a day (*Lancet* 2011). Over the first 90 days,
compare two totals. In the first, the deficit holds steady. In the second, it halves every
365 days, which is made up for this problem. Give the second as a share of the first.

**9.** A deficit shrinks as D0 e^(-0.693t), with t in years, so it halves every year. Over the first
year it adds up to 400 megajoules. Work out D0, in megajoules a year and then in megajoules a
day.

**10.** Here is a worked answer. Find the step that broke.

```working
∫ from 0 to 3 of (12 minus 2t) dt
an antiderivative is F(t) = 12t minus t^2
the integral = F(0) minus F(3)
F(0) = 0 and F(3) = 36 minus 9 = 27
0 minus 27 = -27
```

**11.** Here is a worked answer. Find the step that broke.

```working
∫ from 0 to 3 of t^2 dt
raise the power by one: an antiderivative is t^3
3^3 minus 0^3 = 27
```

**12.** Here is a worked answer. Find the step that broke.

```working
a deficit of 480 kcal/day halves every year, so k = 0.693
the total over the first 30 days = 480 times (1 minus e^(-0.693 times 30)) divided by 0.693
e^(-20.79) is almost 0
480 divided by 0.693 = 692.6
so the deficit adds up to about 693 kcal over the month
```

**13.** A patient information leaflet says this. The wording is made up for this problem.

> Your deficit gets smaller as you lose weight, but it never reaches zero. So the weight loss
> keeps going for ever, and in the end you lose what the old calorie rule said you would.

Decide what to compute, compute it, and say what your answer does not establish.

**14.** A journalist tells you this.

> A modelling paper says the old rule overstates first-year weight loss by about 100%. So to
> correct any figure from the old rule, just halve it.

Hall and colleagues (*Lancet* 2011) do say the static rule's first-year loss is "about 100%
greater" than their model's. Decide what to compute, compute it, and say what your answer does
not establish.

