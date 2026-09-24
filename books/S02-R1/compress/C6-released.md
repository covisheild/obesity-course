# C6 · Recognising shapes: linear, exponential, saturating

**Definition.** A relationship is linear when equal steps in the input add the same amount to the output every
time.

A relationship is exponential when equal steps in the input multiply the output by the same
factor every time.

A relationship is saturating when the output rises while the differences between successive
outputs shrink towards zero, approaching a value it does not pass. That value is the ceiling,
and the output may approach it without ever reaching it.

The tests are arithmetic, carried out on values taken at equal steps. Constant differences
between successive outputs mean linear. Constant ratios mean exponential.

Differences that shrink while the output climbs do not on their own mean saturating, because an
output can climb for ever by ever smaller amounts and approach no value at all. What settles it
is a ratio taken on the differences themselves rather than on the outputs. Divide each
difference by the difference before it. Three cases follow.

Where that ratio holds constant below one, each difference is a fixed share of the one before.
The ceiling can then be computed. The gap still left above any value is the next difference
divided by one minus the ratio.

Where the ratios vary but stay at or below some number under one, a ceiling exists. The
differences still sum to a finite amount. The same division, using that number, gives the most
the gap can be. It does not say exactly where the ceiling is.

Where the ratios creep up towards one, the test shows no ceiling. The differences may add up
without limit, as a logarithm's steps do, and the shape has not been named.

Each case reads the steps observed. It holds beyond them only if the ratios keep behaving the
same way.

**In plain terms.** Three shapes turn up over and over.

**Linear. Equal steps add.** Take one step along the bottom and the value goes up by the same
amount. Take another step and it goes up by that same amount again. Drawn out, it is a straight
line.

**Exponential. Equal steps multiply.** Take one step along the bottom and the value is multiplied
by the same number. Take another step and it is multiplied by that number again. Drawn out, it
starts off looking lazy and then, if it is rising, leaves everything else behind.

**Saturating. It rises, then flattens.** It climbs quickly at first, then less, then hardly at
all. It is heading for a level and it flattens against it. That level is called the ceiling.

Subtract each value from the next one. Are the differences all the same? Then it is linear.

Divide each value by the one before it. Are the ratios all the same? Then it is exponential.

A ratio below one is still exponential, and the values then fall towards zero. The test for
saturating, which comes next, applies only to values that rise.

Do the differences keep shrinking while the values keep climbing? That is not yet enough to say
saturating. A quantity can climb for ever by ever smaller amounts and head for no level at all.

A logarithm does exactly that. Take the multiplying ruler from the section on logarithms. Each
number sits a little further along it than the one before, and each of those steps is shorter
than the step before it. The ruler goes on for ever. Nothing on it is a level to flatten against.

So run one more division, and this time divide the differences rather than the values. Take each
difference and divide it by the difference before it. Then look at what those ratios do.

Do they hold at the same number, below one? Then each difference is a fixed share of the one
before it. The differences add up to a finite amount, and you can work out where the ceiling is.
That is saturating.

Do they wobble, but never go above some number below one, such as 0.5? Then the differences
still add up to a finite amount, and there is a ceiling. You can say the most it can lie above
where you stand. You cannot say exactly where it is.

Do they creep up towards one, say 0.5, then 0.75, then 0.83? Then the test has found you no
ceiling. The steps may be shrinking the way a logarithm's do, heading nowhere. Do not go looking
for a ceiling on the strength of the shrinking alone.

One more thing, and it is the one people get caught by. Look at the side axis before you name
anything. Some side axes multiply by ten at every step, which is the ruler you met in the section
on logarithms. On one of those, an exponential comes out as a straight line. So a straight line
on that kind of axis means multiplying, not adding.

And a warning about how much you need to see. Three points do not have a shape. Any three rising
points can be drawn as any of the three shapes here. You need enough values to see what the
steps are doing.

**Illustration.** Start with three numbers and a wrong answer, because naming a shape too early is the mistake
this section exists to stop.

Somebody shows you three values, taken one step apart: 10, 30, 42. They call the rise
exponential and say it is roughly doubling.

Divide each value by the one before it.

```working
    30 divided by 10 = 3
    42 divided by 30 = 1.4
```

The ratios are not the same, so nothing here is multiplying by a fixed factor. Exponential is
the wrong word.

Now carry on to six values, and put two other shapes beside them for comparison.

```table
step  linear  exponential  saturating
0     10      10           10
1     20      15           30
2     30      22.5         42
3     40      33.8         49.2
4     50      50.6         53.5
5     60      75.9         56.1
```

Work down each column with the two tests.

Take the first column by subtraction.

```working
    20 minus 10 = 10
    30 minus 20 = 10
    60 minus 50 = 10
```

The same amount is added at every step, so the first column is linear.

Take the second column by division.

```working
    15 divided by 10 = 1.5
    22.5 divided by 15 = 1.5
    75.9 divided by 50.6 = 1.5
```

The same factor multiplies at every step, so the second column is exponential.

Take the third column by subtraction, and watch what the differences do.

```working
    30 minus 10 = 20
    42 minus 30 = 12
    49.2 minus 42 = 7.2
    53.5 minus 49.2 = 4.3
    56.1 minus 53.5 = 2.6
```

The steps shrink while the values keep climbing. Now divide each of those differences by the
one before it, which is the test that says whether the shrinking is heading anywhere.

```working
    12 divided by 20 = 0.6
    7.2 divided by 12 = 0.6
```

The ratio holds at about 0.6 all the way down the column, and 0.6 is below one. So if the ratio
keeps holding, the shrinking differences add up to something finite, and a ceiling exists. Now
find where it is.

Call the distance still left between a value and the ceiling the gap. Before the first step,
the gap is the whole of what the differences will ever add up to.

Now look at the differences after the first one: 12, then 7.2, and so on. Each is 0.6 of the
one before it in the full list. So together they add up to 0.6 of the full list's total. That
means the first step leaves 0.6 of the gap still to go. It has closed the other 0.4.

The first step closed 20. So 20 is 0.4 of the gap, and the gap is 20 divided by 0.4. Add the
gap to the starting value of 10.

```working
    1 minus 0.6 = 0.4
    20 divided by 0.4 = 50
    10 plus 50 = 60
```

If the ratio keeps holding, the ceiling is 60. Check it from a later value. At 42 the next
difference is 7.2.

```working
    7.2 divided by 0.4 = 18
    42 plus 18 = 60
```

The same ceiling. So the rule, in words: divide the next difference by one minus the ratio, and
add the answer to the value you are standing on.

Now look at step one and step five, because that is where the trap is. At step one the
exponential column is the lowest of the three. At step five it is the highest, and it has
passed the ceiling the saturating column will never reach.

That is why you get more values before you name anything.

A rising exponential eventually passes any linear.

**Where this picture breaks.** These three shapes are a starting kit and not a list of everything.

The two tests need equal steps along the bottom. Values taken at uneven intervals give
differences and ratios that mean nothing. A table that does not say its step size cannot be
tested at all.

Rounding hides small changes. A ratio that reads 1.5 three times running may be drifting in the
digits you were not shown.

**Figure.** The three shapes on one pair of axes, which is the only way the difference between them can be practised. All three start at the same place; by the last of the six readings they are nowhere near each other.

*What the figure shows:* Three curves from a common starting point. One rises as a straight line, one curves upward ever more steeply, and one rises quickly then flattens toward a ceiling.

**Must know points for you.**

- Run two tests on any set of values taken at equal steps. Subtract each from the next for a constant difference, and divide each by the one before for a constant ratio.
- Shrinking differences do not on their own mean a ceiling. A quantity can climb for ever by ever smaller amounts, as a logarithm does. So run one more test before you say saturating. Divide each difference by the difference before it. A ratio that holds below one lets you work out the ceiling. Ratios that vary but stay at or below some number under one show that a ceiling exists, and not exactly where. Ratios creeping up towards one show you no ceiling, so say you have none to quote rather than estimate one.
- Exponential does not mean fast. It means each equal step multiplies by the same factor.
- Three points have no shape. Ask for more values before you name anything.
- Read the side axis before you call a line linear. On an axis where each step multiplies by ten, a straight line is an exponential.
- Where a curve has flattened, a further equal step in the input buys much less than the step before it did.
- Naming a shape names a pattern and never a mechanism.
- When a journalist uses the word exponential, ask what the values were at equal times and whether the ratio held.

**Exercise 1** (interpretation). A figure shows one curve, with time along the bottom and a count up the side. The curve rises
steeply for the first part, then bends over and runs nearly flat for the rest.

Say which of the three shapes it is. Say what the flat part means in the arithmetic. Then say
what the figure does not tell you.

**Exercise 2** (teaching). A journalist has three minutes and no jargon. They have a chart and a press line saying the
numbers are rising exponentially. They ask you whether that is right.

Say what you would tell them, and give them one quotable sentence.

**1.** Each of these is a set of values taken one step apart. Name the shape of each where the tests
allow one, and say which test told you.

```table
A  4   8    12    16    20
B  4   8    16    32    64
C  4   12   16    19    21.5
```

**2.** Each of these is a set of values taken one step apart. Name the shape of each.

```table
D  100  50   25    12.5   6.25
E  100  130  160   190    220
F  2    6    18    54     162
```

**3.** Start at 8 and write five values for each of these rules, taking one step at a time.

```working
    add 6 at every step
    multiply by 3 at every step
```

Then say which of the two is which shape.

**4.** Under section 3(1) of the National Food Security Act, 2013, a person in a priority household is
entitled to five kilograms of foodgrains a month.

Write the total grain a household of four is counted for after one, two, three and four months.
Name the shape. Give the slope of the line with its unit. Then say what would have to be true
for this quantity to be exponential.

**5.** A quantity is measured at equal steps and comes out as 20, 44, 56.0, 62.0, 65.0, 66.5.

Name the shape, show the working that names it, and estimate the ceiling it is heading for.

**6.** Two quantities are recorded at equal steps.

```table
G  5    35    65    95    125
H  5    10    20    40    80
```

Say which of the two will be the larger at step 12, and show the working that decides it.

**7.** Here is a worked answer. Find the step that broke.

```working
    the values at equal steps are 10, 30, 42, 49.2, 53.5, 56.1
    the first step rose by 20, which is a big jump
    the curve is clearly rising fast
    a curve that rises fast is exponential
    so the quantity is growing exponentially and will keep doing so
```

**8.** Here is a worked answer. Find the step that broke.

```working
    the figure has a side axis marked 10, 100, 1,000, 10,000
    the points lie on a straight line across the figure
    a straight line is the picture of a linear relationship
    so the quantity is rising by a fixed amount each month
    the rise from the first month to the last is steady and needs no further comment
```

**9.** A line in a meeting note says this.

> Registrations are growing exponentially. We had 200 in the first month, 400 in the second and
> 600 in the third.

The programme and all three figures are made up for this problem. No real programme is being
described.

Decide what to compute, compute it, and say what your answer does not establish.

**10.** A district officer writes this in a review note.

> The programme is running out of steam. Coverage went up 12 points in the first year, then 6,
> then 3, then 1.5. The gains are collapsing and we should move the money elsewhere.

The programme and all four figures are made up for this problem. No real programme is being
described.

Decide what to compute, compute it, and say what your answer does not establish.

