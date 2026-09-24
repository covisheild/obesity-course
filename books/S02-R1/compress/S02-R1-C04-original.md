# S02-R1-C04 · The number e, natural logarithms and change proportional to amount

**Definition.** The number e is the base of the one exponential curve, e^(t), whose slope where it crosses the
vertical axis, at t = 0, is exactly 1. To five decimal places e = 2.71828. It is also the value
that (1 plus 1/m) raised to the power m approaches as m grows without limit.

The natural logarithm of a positive number x, written ln x, is the power to which e must be
raised to give x. So ln(e^(x)) = x for every x, and e^(ln x) = x for every x above zero. It is
defined only for numbers above zero, and ln 1 = 0. Like the logarithm to base ten, it turns
multiplication into addition: ln(ab) = ln a plus ln b, for a and b above zero.

For constants A and k, the function y = A e^(kt) has derivative dy/dt = k A e^(kt), which is
k times y. Its rate of change is proportional to its own value. The constant k is the rate
constant: the rate of change divided by the amount, with the unit one over time. A quantity
whose rate of change is always k times its own value follows this curve, with A its value at
t = 0.

Where the quantity shrinks, write y = A e^(-kt) with k above zero. The time it takes to fall
to half of any starting value is the half-time, ln 2 divided by k, which is about 0.693
divided by k. The time to fall to one twentieth, 5% of the start, is ln 20 divided by k, about
3.00 divided by k. For every such curve the second time is ln 20 divided by ln 2, about 4.32,
times the first.

A quantity W that approaches a level L in this way follows W = L plus (W0 minus L) times
e^(-kt), where W0 is its value at t = 0. The gap W minus L is the shrinking exponential. Its
rate of change is dW/dt = -k times (W minus L), and the share of the eventual change reached
by time t is 1 minus e^(-kt).

Read at equal steps of time h, the gap is multiplied by the same factor, e^(-kh), at every
step, and so is each successive change. That is the saturating pattern with a constant ratio
of differences taught in `B0-R0-C20`, and the ratio gives k back as minus ln(ratio) divided
by h.

**In plain terms.** Book 0 built powers and logarithms on ten (`B0-R0-C06`, `B0-R0-C07`). Papers on body weight use
a different base, a number written e. Here is where it comes from, and why it earns its place.

Take a base, say 2, and ask how steep the curve 2^(t) is where it starts, at t = 0. `S02-R1-C02`
gave you the way to ask. Take a very short step, 0.0001, and divide the change by the step.

```working
2^0.0001 = 1.0000693
(1.0000693 minus 1) divided by 0.0001 = 0.693
```

The curve 2^(t) starts with a slope of 0.693. Do the same with 3 and you get 1.099. So somewhere
between 2 and 3 is a base whose curve starts with a slope of exactly 1. That base is e, and it
is 2.71828 to five decimal places. Your calculator has a key for it, usually marked e^(x).

Now the property that makes e worth having. Take y = e^(kt), where k is a fixed number, and find
its rate at any time t. Step forward a short time h. Multiplying two powers of the same base adds
their exponents (`B0-R0-C06`), so read that rule backwards.

```working
e^(kt plus kh) = e^(kt) times e^(kh)
the change = e^(kt) times e^(kh) minus e^(kt)
the change = e^(kt) times (e^(kh) minus 1)
the change divided by h = e^(kt) times (e^(kh) minus 1) divided by h
```

As h shrinks, (e^(kh) minus 1) divided by h settles on k. Here is why. Call kh by one letter, u.
Then (e^(kh) minus 1) divided by h is k times (e^(u) minus 1) divided by u. And (e^(u) minus 1)
divided by u, for u close to zero, is the slope of e^(t) at the start, which is 1.

So the rate of e^(kt) is k times e^(kt). Put a constant A in front, and by the constant-multiple
rule (`S02-R1-C03`) the rate of A e^(kt) is k times A e^(kt).

Read that sentence again, because it is the whole point. The rate is k times the amount
itself. Double the amount and the rate doubles. The number k is the rate constant, the rate
divided by the amount. Its unit is one over time: per day, or per year.

A logarithm undoes a power. The natural logarithm, written ln, undoes a power of e. Ask "e to
what power gives this number?" and ln answers. So ln(e^3) = 3, ln e = 1 and ln 1 = 0. It works
only for numbers above zero, like log10.

It turns multiplication into addition, for the same reason log10 does. Multiplying powers of e
adds their exponents, and the exponents are the logarithms.

```working
ln(ab) = ln a plus ln b
ln 2 plus ln(1/2) = ln 1 = 0, so ln(1/2) = -ln 2
```

Now a quantity that shrinks, y = A e^(-kt), with k above zero. When has it fallen to half? Set
the curve equal to half its start, and divide both sides by A.

```working
A e^(-kt) = A divided by 2
e^(-kt) = 1/2
```

Both sides are the same number, so their natural logarithms are the same number.

```working
-kt = ln(1/2) = -ln 2
t = ln 2 divided by k
```

That time is the half-time. It does not depend on A, so the quantity halves in the same time
from any starting point. Put one twentieth in place of one half and the same steps work. They
give the time to fall to 5% of the start, which is 95% of the way to zero.

```working
ln 2 = 0.693
ln 20 = 2.996
2.996 divided by 0.693 = 4.32
```

So the time to 95% is always about 4.32 half-times, for any curve of this kind.

**Illustration.** Here is a claim you will meet, and a test it fails.

Hall and colleagues modelled a man weighing 100 kilograms who cuts his intake by 2 megajoules
a day and keeps it cut (*Lancet* 2011). Their model has his weight level off at about 75
kilograms. It takes "roughly 1 year to reach half of the maximum weight loss", and reaches "95%
of this value after about 3 years". The same paper turns this into a rule of thumb. Half the
change comes "in about 1 year and 95% of the weight change in about 3 years". A consensus statement
the next year repeats it (Hall and colleagues, *American Journal of Clinical Nutrition* 2012).
It gives nearly one year to 50%, and about three years to 95%.

The tempting reading is that the weight closes its gap as one exponential with a half-time of
one year. Test it. Start from the half-time and work out k.

```working
0.693 divided by 1 = 0.693
```

So k is 0.693 per year. Now the time to 95%.

```working
2.996 divided by 0.693 = 4.32
```

About 4.3 years, not 3.

Go the other way. Start from 95% at 3 years and work out k, then the half-time.

```working
2.996 divided by 3 = 0.999
0.693 divided by 0.999 = 0.694
```

A half-time of 0.694 years, about 8 months, not 1 year.

Now put the two curves side by side. The share of the eventual change reached by time t is 1
minus e^(-kt). Work each row out on your calculator, times 100 for a percentage.

```table
| years | half-time 1 year (k = 0.693) | 95% at 3 years (k = 0.999) | the papers' rounded figures |
| 0 | 0.0 | 0.0 | |
| 1 | 50.0 | 63.2 | about 50 |
| 2 | 75.0 | 86.4 | |
| 3 | 87.5 | 95.0 | about 95 |
| 4 | 93.7 | 98.2 | |
| 5 | 96.9 | 99.3 | |
```

Neither column passes through both figures. One exponential cannot give both, because for one
exponential the time to 95% is always 4.32 half-times. The papers' figures give 3 divided by
1, which is 3.

The papers never said the curve was one exponential. The two figures are rounded outputs of
their model. So two readings are left. The model's curve may not be a single exponential. Or
"roughly 1 year" may be rounding something shorter, near 8 months. From the rounded figures
alone you cannot tell which.

What you must not do is pick one of these curves and read months off it as if the paper had
said them. At one year the two columns differ by this much.

```working
63.2 minus 50.0 = 13.2
```

That is 13.2 percentage points. On the man's eventual loss of about 25 kilograms, it is 3.3
kilograms.

```working
100 minus 75 = 25
0.132 times 25 = 3.3
```

Now look at the same curve another way. Book 0 gave you a test for a shape that flattens
against a ceiling (`B0-R0-C20`). Take values
at equal steps, subtract each from the next, then divide each difference by the one before. A
ratio that holds steady below one means a ceiling you can work out. This is that test, run on
a curve you already know.

Take the first column of the table above, the curve with a one-year half-time. Read it once a
year: 0.0, 50.0, 75.0, 87.5. Subtract each from the next.

```working
50.0 minus 0.0 = 50.0
75.0 minus 50.0 = 25.0
87.5 minus 75.0 = 12.5
```

Now divide each difference by the one before.

```working
25.0 divided by 50.0 = 0.5
12.5 divided by 25.0 = 0.5
```

A steady ratio of 0.5. Book 0's rule says the gap still left above any value is the next
difference divided by one minus the ratio. The next difference is half of 12.5.

```working
12.5 times 0.5 = 6.25
6.25 divided by (1 minus 0.5) = 12.5
87.5 plus 12.5 = 100
```

The ceiling is 100%, as it must be. Book 0's steady ratio and this section's e^(-kt) are the
same shape, seen at equal steps. The ratio is what the curve is multiplied by over one step, so
it is e^(-k) for a step of one year. Take ln of both sides to get k back.

```working
e^(-k) = 0.5
-k = ln 0.5 = -0.693
k = 0.693 per year
```

That is the k you started from. So a set of weights taken at equal intervals, whose
differences shrink by a steady ratio, gives you the rate constant without any curve-fitting.
Divide minus ln of the ratio by the length of the step.

**Where this picture breaks.** Both columns are what one exponential would give. Neither is the model's own curve, which the
papers do not print as a formula. The 25 kilograms is a rounded plateau for one modelled man,
with a spread of about 4 kilograms either way that the paper itself shows. Nothing here says a
real person follows either column.

The ratio holds steady only if the curve really is one exponential and the readings are
exact. Rounded or noisy readings make the ratios wobble, and one wobbling ratio is not evidence
of any shape. Three readings give only two ratios, which is too few to call anything steady.

**Figure.** Two exponentials, each matching one of Hall's rounded figures. The one with a half-time of 1 year reaches 50% at 1 year and only 87.5% at 3. The one that reaches 95% at 3 years is already at 63.2% after 1. No single exponential passes through both figures.

*What the figure shows:* Two rising curves of the share of the eventual change reached, from 0 at year 0 towards 100 by year 5. The upper curve passes 63.2 at year 1 and 95.0 at year 3. The lower passes 50.0 at year 1 and 87.5 at year 3. Labels mark the paper's figures at 1 year and 3 years.

**Must know points for you.**

- For any single exponential, the time to 95% of the way is 4.32 half-times, because ln 20 divided by ln 2 is 4.32. Hall's "about 1 year" and "about 3 years" are in another ratio. So either the curve is not one exponential, or the figures are loosely rounded. Stop there. Do not fill in the months between with an exponential you chose yourself.
- Use ln, not log10, in a half-time. The calculator key marked log is log10, and log10 2 divided by k gives 0.301 divided by k, less than half the right answer. The rate constant k was defined with e, so only ln undoes it.
- Write the unit beside k every time. A k of 0.693 per year used with t in days gives an answer 365 times too fast. The fix is a conversion before the calculation, never after it.
- To test whether a claimed curve is exponential, divide its rate by its value at two or more times. The answer must be the same constant every time. With readings at equal steps, divide each difference by the one before; the ratio must hold steady.
- "Exponential" is not a synonym for fast or for runaway. A gap closing exponentially closes fastest at the start and ever more slowly, because its rate is k times what is left.
- A patient may ask how long a change in intake takes to show in full. Give the model's figures as rough figures. Roughly a year to half, and about three years to most of it, for the model's average adult (Hall 2011). Do not give month-by-month figures from one exponential. Those are yours, not the paper's. Pick a different exponential and they move by kilograms.

**Exercise 1** (calculation). A quantity falls as y = A e^(-kt), with k above zero. Derive the time at which it has fallen
to 5% of its starting value. Write the move you make beside every line, as a word or two: for
example "divide both sides by A". Then say why the answer does not depend on A.

**1.** Use the e^(x) and ln keys of your calculator. Work out each of these to three decimal places:
e^1, e^2, e^(-1), ln 1, ln 10 and ln(e^3).

**2.** Show with numbers that ln 20 equals ln 4 plus ln 5. Then show that ln(1/2) equals minus ln 2.
Work to three decimal places.

**3.** A quantity follows y = 40 e^(0.05t). Work out its rate of change, dy/dt. Then work out y, dy/dt
and dy/dt divided by y at t = 0 and at t = 10.

**4.** A quantity follows y = 200 e^(-0.1t). Work out its half-time and the time it takes to fall to
5% of its starting value. Then work out y at each of those two times.

**5.** A quantity falls exponentially with a half-time of 14. Work out its rate constant k. Then work
out the share of the starting value left after 28, and after 10.

**6.** Solve 100 e^(-0.2t) = 30 for t.

**7.** A quantity is read at equal steps of 2 units of time: 60, 70, 75, 77.5. Find the level it is
approaching, its rate constant k, and its half-time.

**8.** Hall and colleagues (*Lancet* 2011) give a rule of thumb for an average adult with overweight. It
reads: "every change of energy intake of 100 kJ per day will lead to an eventual bodyweight
change of about 1 kg". Half of that change comes "in about 1 year".

A person cuts intake by 500 kJ a day and holds it. Work out the eventual change the rule of
thumb gives. Then suppose the change comes as one exponential with a half-time of exactly 1
year. Work out how much of it would have come by 6 months and by 2 years. Say which of your
figures are the paper's.

**9.** Hall and colleagues' modelled man starts at 100 kilograms and levels off at about 75 kilograms
(*Lancet* 2011). Suppose his weight closes the gap as one exponential that is 95% of the way
there at 3 years. Work out his weight at 1 year. Then work it out again for an exponential with
a half-time of 1 year, and give the difference.

**10.** Take the same man, with a gap of 25 kilograms, and suppose it closes as one exponential with a
half-time of 1 year. Work out the rate of change of his weight at the very start, in kilograms
a year and in grams a day. Then compare it with his average rate over the first year.

**11.** Here is a worked answer. Find the step that broke.

```working
a quantity falls exponentially with k = 0.1 per day
half-time = log10 2 divided by k
log10 2 = 0.301
0.301 divided by 0.1 = 3.01
so it halves every 3.01 days
```

**12.** Here is a worked answer. Find the step that broke.

```working
a change reaches its eventual size with k = 0.693 per year
95% of the way means e^(-kt) = 0.95
-kt = ln 0.95 = -0.0513
t = 0.0513 divided by 0.693 = 0.074
so 95% of the change comes in 0.074 years, about 27 days
```

**13.** Here is a worked answer. Find the step that broke.

```working
y = 40 e^(0.05t)
by the power rule, bring the power down and take one off it
dy/dt = 40 times 0.05t times e^(0.05t minus 1)
at t = 0, dy/dt = 0
so the curve is flat where it starts
```

**14.** Here is a worked answer. Find the step that broke.

```working
a gap closes exponentially with a half-time of 1 year, so k = 0.693
after 30 days the share left is e^(-0.693 times 30)
e^(-20.79) = 0.000000001
so the change is complete within a month
```

**15.** A colleague reads the rule of thumb in Hall and colleagues (*Lancet* 2011). It has "half of the
weight change being achieved in about 1 year and 95% of the weight change in about 3 years".
The colleague says this.

> That is an exponential with a one-year half-time. After three years it would be only 87.5%
> of the way, so the paper contradicts itself.

Decide what to compute, compute it, and say what your answer does not establish.

**16.** A health magazine prints this line. The patient and the 4 kilograms are made up for this
problem.

> Weight loss slows exponentially. So a patient who has lost 4 kg in the first three months
> will have lost 16 kg by the end of the year.

Decide what to compute, compute it, and say what your answer does not establish.

