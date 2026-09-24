# S02-R1-C02 · The derivative: the rate at an instant, computed

**Definition.** Let f be a function and a an input it accepts. The average rate of change of f over the
interval from a to a + h is f(a + h) minus f(a), divided by h, for h not zero.

The derivative of f at a is the single number these averages settle on as h is made smaller
and smaller, through positive values and through negative values alike. Where the two sides
do not settle on one number, f has no derivative at a. The number the averages settle on is
called the limit, written lim with h → 0 beneath it.

The derivative at a is written f′(a), said "f prime of a". For a quantity S that changes
with time t it is also written dS/dt, said "dee S by dee t", the rate of change of S with
respect to t. Found at every input, the derivatives make a new function, f′.

The derivative carries the unit of f divided by the unit of the input. A positive derivative
means f is rising at a, a negative one that it is falling, and zero that at that instant it
is doing neither.

The derivative belongs to a smooth curve. Repeated measurements are separate points with
error in them. A rate taken from them is an average over an interval, and an interval
shorter than the error can resolve makes the estimate worse, not better.

**In plain terms.** Book 0 showed you the rate at an instant as the slope of a tangent, laid on a curve with a
ruler. It named that rate the derivative (`B0-R0-C21`). The last section read the symbol dES/dt in
a paper. This section works the number out with arithmetic, no ruler needed.

The idea is one you already have. A shorter interval gives a closer answer. So take the
average rate over shorter and shorter intervals, all starting at the moment you care about.
Watch the answers. They settle on one number. That number is the rate at that instant.

Here is the procedure for a function f at an input a.

1. Pick a small step, h. Work out f(a + h) minus f(a), and divide by h. That is the average
   rate over the interval from a to a + h.
2. Make h smaller: 1, then 0.1, then 0.01, then 0.001. Work the average out each time.
3. Do the same with h below zero: minus 1, minus 0.1, and so on. Those intervals end at a
   instead of starting there.
4. If both lists close in on the same number, that number is the derivative at a.

You never set h to zero. At zero the interval has no length, and dividing by zero is not
allowed (`B0-R0-C16`). You only let h shrink, and watch where the answers go. The number they
close in on is called the limit.

The derivative has three names you will meet. f′(a), said "f prime of a". dS/dt, said "dee S
by dee t". And in words, the rate of change of S with respect to t. All three mean the same
thing.

Its unit comes from the division, as in Book 0. A weight in kilograms against time in days
gives kilograms per day.

Its sign tells you the direction. Positive means rising at that instant. Negative means
falling. Zero means neither, at that instant.

Read the paper's equation again in these terms. dES/dt is the rate of change of stored
energy, in kilocalories a day. It is not the stored energy itself.

**Illustration.** Start with a claim that uses the wrong interval. A quantity follows the rule S(t) = 5 t^2,
which is 5 times t times t. The rule is made up for this example, and there are no units. A
note says this.

> S went from 20 at t = 2 to 45 at t = 3. So at t = 2 it is rising at 25 a unit of time.

Check the two values first.

```working
    S(2) = 5 times 2 times 2 = 20
    S(3) = 5 times 3 times 3 = 45
```

The 25 is the average over a whole unit of time, from t = 2 to t = 3. That is a chord.
The note calls it the rate at t = 2. Test that by shrinking the interval.

Each row takes a step h from t = 2. Work out S(2 + h), subtract S(2), and divide by h.

```table
| step h | S(2 + h) | S(2 + h) minus S(2) | average rate |
| 1 | 45 | 25 | 25 |
| 0.1 | 22.05 | 2.05 | 20.5 |
| 0.01 | 20.2005 | 0.2005 | 20.05 |
| 0.001 | 20.020005 | 0.020005 | 20.005 |
| -0.001 | 19.980005 | -0.019995 | 19.995 |
| -0.01 | 19.8005 | -0.1995 | 19.95 |
| -0.1 | 18.05 | -1.95 | 19.5 |
| -1 | 5 | -15 | 15 |
```

Here is one row in full, h = 0.1.

```working
    S(2.1) = 5 times 2.1 times 2.1 = 22.05
    22.05 minus 20 = 2.05
    2.05 divided by 0.1 = 20.5
```

Read down the last column. From above, 25, then 20.5, 20.05, 20.005. From below, 15, 19.5,
19.95, 19.995. Both lists close in on 20. So the rate at t = 2 is 20 a unit of time, not 25.

```working
    S′(2) = 20
```

Now see why it is exactly 20, with algebra. Write S(2 + h) out. Multiply out the bracket
with the rule from `B0-R0-C15`, once for each term.

```working
    (2 + h) times (2 + h) = 2 times (2 + h) + h times (2 + h)
    = 4 + 2h + 2h + h^2
    = 4 + 4h + h^2
    S(2 + h) = 5 times (4 + 4h + h^2) = 20 + 20h + 5 h^2
```

Subtract S(2), which is 20. Then divide by h. That is allowed, because h is never zero.

```working
    S(2 + h) minus S(2) = 20h + 5 h^2
    (20h + 5 h^2) divided by h = 20 + 5h
```

The average rate over a step h is 20 + 5h, for any h. Check it against the table: h = 0.1
gives 20.5. As h shrinks, 5h shrinks with it, and what is left is 20.

Now the same move on real measurements, where it breaks. A person weighs themselves each
morning for fifteen days. The weights below are made up, but day-to-day swings of this size
are normal. Hall and colleagues (2012) warn that "weight change may not directly represent
energy imbalances, particularly over the short term", because body water moves.

```table
day  weight (kg)
0    80.3
1    79.8
2    80.1
3    79.6
4    80.2
5    79.5
6    79.9
7    79.4
8    79.9
9    79.2
10   79.6
11   79.5
12   79.0
13   79.6
14   79.8
```

Shrink the interval to one day, as you did for S. Take the last two days, then the two days
before them.

```working
    79.8 minus 79.6 = 0.2, over 1 day: 0.2 kg a day
    79.6 minus 79.0 = 0.6, over 1 day: 0.6 kg a day
```

Rising at 0.6 kg a day. Test that against the body. Hall (2008) gives body fat 39.5 MJ a
kilogram. The FAO/WHO/UNU report's worked example puts one woman's whole day's expenditure
at 8.26 MJ.

```working
    0.6 times 39.5 = 23.7
    23.7 divided by 8.26 = 2.87
```

Adding 0.6 kg of fat in a day would take 23.7 MJ more than she spent. That is nearly three
whole days of her expenditure. The one-day rate is measuring water, not stores.

So with weighings, shrink the interval the other way. Polidori and colleagues (2016) did
this. They used "the moving average of the measured body weight time course" to get the rate
over each interval. Their weighings were 52 days apart. Try a small version. Average the
first five days and the last five. Each average belongs to its middle day.

```working
    80.3 plus 79.8 plus 80.1 plus 79.6 plus 80.2 = 400.0
    400.0 divided by 5 = 80.0, the average weight at day 2
    79.6 plus 79.5 plus 79.0 plus 79.6 plus 79.8 = 397.5
    397.5 divided by 5 = 79.5, the average weight at day 12
    79.5 minus 80.0 = -0.5
    -0.5 divided by 10 = -0.05
```

Falling at about 0.05 kg a day over those ten days. Even this is still an average over an
interval. It is the best a scale can give you. The derivative itself belongs to a smooth
curve that nobody measured.

**Where this picture breaks.** The rule S(t) = 5 t^2 is smooth all the way down, so its averages keep settling as h shrinks.
Real weighings are not. Below the interval over which water swings, a shorter interval gives
a worse rate, not a better one.

The fifteen weights are made up. They show the size of day-to-day swings, not any person's
trend. The 0.05 kg a day holds for these ten days only.

**Figure.** The average rate of S(t) = 5 t^2 from t = 2 over a step h, for steps from -1 to 1. Every average lies on the line 20 + 5h. As the step shrinks towards zero from either side, the averages close in on 20, the derivative at t = 2; the point h = 0 itself is never computed.

*What the figure shows:* Points on a rising straight line, with the step h along the bottom from -1 to 1 and the average rate up the side from 15 to 25. Points at h = -1, -0.1, -0.01 and -0.001 sit at 15, 19.5, 19.95 and 19.995; points at 0.001, 0.01, 0.1 and 1 sit at 20.005, 20.05, 20.5 and 25. The line passes through 20 at h = 0, where there is no point.

**Figure.** Fifteen made-up morning weighings. Day to day the weight jumps by as much as 0.7 kg, while the average of days 0 to 4, 80.0 kg, and of days 10 to 14, 79.5 kg, fall by 0.5 kg over ten days. The side axis does not start at zero, so the swings look larger than they are.

*What the figure shows:* Fifteen points from day 0 to day 14, zigzagging between 79.0 and 80.3 kilograms, drifting slowly downwards.

**Must know points for you.**

- Before you call a rate "the rate now", ask how long the interval was. A rate over a long interval is an average across it. The rate at an instant is what those averages settle on as the interval shrinks.
- A rate of weight change taken from two weighings a day apart is mostly water. It can come out as a gain of 0.6 kg a day in a person who is losing weight. Take a rate from averages over weeks, not from neighbouring readings.
- A shorter interval is better only for a smooth curve. For measurements with error, shrinking the interval below the size of the swings makes the rate worse. So the derivative in a paper's equation is always estimated, from an interval the Methods should state.
- Never set h to zero to get the derivative. The average has h on the bottom. Let h shrink and watch where the answers go.
- Read dW/dt as a rate with a unit, kilograms per day, and read its sign first. A figure of minus 0.05 means weight is falling by 0.05 kg a day at that instant. It says nothing about how much has been lost so far.
- When a trial reports a rate of weight change, look in the Methods for the interval and the averaging used. Polidori's rates came from moving averages over 52-day intervals. A rate from single weighings a week apart is a different, noisier number.

**Exercise 1** (interpretation). Polidori and colleagues (2016) describe how they got one of their inputs. Here is their
sentence.

> the moving average of the measured body weight time course was used to calculate the rate
> of change of body weight over each interval

They call that rate dBWi/dt.

Their weighings were 52 days apart.

Say what dBWi/dt denotes and what unit it carries. Then say why the authors did not take the
rate from two weighings made on neighbouring days, and what their choice gives up.

**1.** A function has f(4) = 30 and f(4.5) = 33.5.

Work out the average rate of change of f from 4 to 4.5.

**2.** Take f(t) = t^2, which is t times t, and the input t = 3.

Work out the average rate from t = 3 to t = 3 + h for h = 1, 0.1 and 0.01. Do the same for
h = -0.1 and h = -0.01. Then give the derivative at t = 3.

**3.** Say each of these aloud in words, and give its unit.

```working
    dW/dt, where W is body weight in kg and t is time in days
    f′(10) = -3, where f is in kcal a day and its input is body weight in kg
```

**4.** Take f(t) = 3 t^2 and the input t = 1.

Write out f(1 + h) minus f(1), divided by h, using algebra. Then find the derivative at
t = 1.

**5.** Here are four values of a derivative. For each, say whether the function is rising, falling
or neither at that input.

```working
    f′(0) = 4
    f′(2) = 0
    f′(5) = -0.3
    f′(7) = -12
```

**6.** In the trial reported by Polidori and colleagues (2016), weighings were 52 days apart. Take a
made-up participant who weighs 94.6 kg at one weighing and 92.0 kg at the next.

Work out the average rate of weight change over the interval, with its unit. Then give it in
kilograms a week.

**7.** The FAO/WHO/UNU report (2004) gives a woman's total energy expenditure as 8.26 MJ a day. Take
a made-up day on which her metabolizable intake is 7.80 MJ.

Work out dES/dt, the rate of change of her energy stores, in MJ a day and then in kcal a day.
Use 1 kcal = 4.184 kJ. Say what the sign means.

**8.** A patient weighs 92.0 kg today. Their weight is falling at 0.05 kg a day. Both figures are
made up.

Estimate their weight 10 days from now, using the rate. Then do the same for 300 days from
now, and say which of the two estimates you would trust less, and why.

**9.** Here is a worked answer. Find the step that broke.

```working
    f(t) = t^2, find the derivative at t = 3
    f(3 + h) = (3 + h) times (3 + h) = 9 + h^2
    f(3 + h) minus f(3) = h^2
    h^2 divided by h = h
    as h shrinks, h shrinks to 0
    so the derivative at t = 3 is 0, and f is not changing there
```

**10.** Here is a worked answer. Find the step that broke.

```working
    a patient weighed 79.0 kg on Monday morning and 79.6 kg on Tuesday morning
    the rate of weight change is 79.6 minus 79.0, over 1 day, = 0.6 kg a day
    a shorter interval gives a closer rate, so this is close to the rate at an instant
    so the patient is gaining 0.6 kg of body fat a day
```

**11.** A newspaper report says this about a new diet.

> In the first week, people on the diet lost 2 kg. Kept up, that is over 100 kg in a year.

The report and its 2 kg are made up for this problem. Decide what to compute, compute it, and
say what your answer does not establish.

**12.** A clinic note reads as follows.

> Weighed 76.2 kg yesterday and 76.2 kg today. dW/dt = 0. Her weight has stopped changing, so
> her intake now matches her expenditure.

The weights are made up for this problem. Decide what to compute, compute it, and say what
your answer does not establish.

