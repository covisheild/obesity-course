# S02-R1-C05 · The integral of a rate is the change in the stock

**Definition.** Let f(t) be a rate that depends on time t. The definite integral of f from a to b is written ∫
from a to b of f(t) dt. Cover the time from a to b with thin intervals of width Δt. Over each,
draw a rectangle whose height is the rate in that interval. The integral is the limit of the
sum of the rectangles' areas as the widths shrink towards zero.

The sign ∫ is a stretched S, for sum. The numbers a and b are the limits of integration: a is
where the interval starts and b where it ends. The function f(t) is the integrand. The dt
names the variable that runs from a to b and stands for the width of the thin intervals.

Where f(t) is below zero, each rectangle's height times width is negative. So the integral is
the net signed area: the area between the rate line and the time axis above the axis, minus
the area between them below the axis.

If f is the rate of change of a quantity Q, then ∫ from a to b of f(t) dt equals Q(b) minus
Q(a). This is the net change theorem: the integral of a rate over an interval is the change in
the stock over that interval. Its unit is the rate's unit times the unit of time, which is the
stock's unit.

Two cases can be done exactly with no limit. A constant rate c gives a rectangle, c times (b
minus a). A rate that changes along a straight line gives a trapezium, the average of the two
end rates times (b minus a). The trapezium rule holds with the signs kept, including when the
line crosses zero. A triangle is the case where one end rate is zero.

The average value of f from a to b is the integral divided by (b minus a). It is the height of
the one rectangle over the same interval with the same net signed area. For a straight-line
rate it is halfway between the two end rates.

Applied to a body, with stored energy ES, energy intake EI and energy expenditure EE, the
identity of `S01-R1-C05` written as rates is dES/dt = EI minus EE. So ES(b) minus ES(a) = ∫ from
a to b of (EI minus EE) dt. A sum of daily differences is the rectangle version of that
integral, with each rectangle one day wide. It is exact when each day's figures are that day's
totals. It is an estimate, with the error bound of `B0-R0-C22`, when each is a rate read at one
moment and applied to the whole day.

**In plain terms.** Book 0 drew rectangles under a rate line and added them up (`B0-R0-C22`). It called the total
under the line an integral, and said nothing in that book would ask you to work one out. This
section asks you to.

Here is how a paper writes one.

```working
∫ from a to b of f(t) dt
```

Read it from left to right. The ∫ is a stretched S, for sum. The a at its foot is where the time
starts, and the b at its top is where it stops. Those two are the limits of integration.

Next comes f(t), the rate being added up. Its name is the integrand. Last, dt says the adding
runs over time t. It stands for the width of each thin slice, the Δt of `S02-R1-C01`, made very
small.

Say it aloud as "the integral from a to b of f of t, d t". It means this. Cut the time from a
to b into thin slices. Multiply the rate in each slice by its width. Add them all. Then let the
slices get thinner, until the total stops changing.

One thing is new since Book 0. There, every rate was above zero. Here a rate can drop below
zero, because a stock can lose as well as gain. A rectangle below the time axis has a negative
height, so its area counts as negative. Area below the axis is subtracted. The result is called
the net signed area.

Why bother with any of this? Because of one fact. The integral of a rate over an interval equals
the change in the stock over that interval. This is called the net change theorem.

```working
the stock at b minus the stock at a = ∫ from a to b of the rate dt
```

For a body's energy stores, the rate is intake minus expenditure (`S01-R1-C05`). Write the stores
as ES, intake as EI and expenditure as EE. In words: the rate of change of ES with respect to t
equals EI minus EE.

```working
dES/dt = EI minus EE
ES(b) minus ES(a) = ∫ from a to b of (EI minus EE) dt
```

Two shapes can be done exactly, with no slices at all. A steady rate gives a rectangle: the rate
times the time. A rate that changes along a straight line gives a trapezium, a four-sided shape
with two parallel sides. Its area is the average of the two end rates, times the time. A
triangle is the case where one end is zero.

The average value of a rate over an interval is its integral divided by the length of the
interval. It is the one steady rate that would have given the same change.

**Illustration.** Take a made-up case, with numbers chosen so that the rate is a straight line. A person's net
rate, intake minus expenditure, is 300 kilocalories a day on day 0. It falls by 10
kilocalories a day, every day, for 50 days.

```table
day  EI minus EE (kcal/day)
0    300
10   200
20   100
30   0
40   -100
50   -200
```

A trainee is asked how much the person's energy stores changed over the 50 days. They draw
the line and shade everything between it and the time axis. There are two triangles, and a
triangle's area is half its base times its height. They work out both and add them.

```working
0.5 times 30 times 300 = 4500
0.5 times 20 times 200 = 2000
4500 plus 2000 = 6500
```

They report a gain of 6,500 kilocalories. Find the flaw before you read on.

From day 30 to day 50 the rate is below zero. Expenditure is higher than intake on each of
those days, so the stores fall. The 2,000 kilocalories under the axis is energy taken out, not
put in. It has to be subtracted.

```working
4500 minus 2000 = 2500
```

The stores rose by 2,500 kilocalories over the 50 days. The trainee's 6,500 is correct
arithmetic on a real area. It answers a question nobody asked: how much energy moved in either
direction.

Now the one-line way. The rate is a straight line, so the whole shape counts as one trapezium.
Take the average of the two end rates, keeping the minus sign, and multiply by the time.

```working
300 plus -200 = 100
100 divided by 2 = 50
50 times 50 = 2500
```

The same 2,500 kilocalories. The minus sign did the subtraction for you. The middle number, 50
kilocalories a day, is the average value of the rate. A steady 50 a day for 50 days would have
changed the stores by the same amount.

Now write what you did the way a paper would. The rate is 300 minus 10t, with t in days.

```working
∫ from 0 to 50 of (300 minus 10t) dt = 2500
```

Read it aloud: the integral from 0 to 50 of 300 minus 10t, d t, is 2,500. Check its unit. It
is kilocalories a day times days, which is kilocalories. A change in a stock carries the
stock's unit.

The same idea runs through a record you already have. The week in `S01-R1-C05` added seven
daily differences to get 2.8 megajoules. Each day was a rectangle one day wide, with height
that day's intake minus expenditure. The week's sum was the rectangle version of this
integral.

```working
ES(day 7) minus ES(day 0) = ∫ from 0 to 7 of (EI minus EE) dt
```

There, each day's figure was that day's total. So each rectangle was exact, whatever happened
between meals. Suppose instead each figure had been a rate read at one moment and stretched
across 24 hours. Then each rectangle would carry the error `B0-R0-C22` taught you to bound.

One trap waits when you read where this equation comes from. Hall and colleagues' consensus
statement (*American Journal of Clinical Nutrition* 2012) writes it as ES = EI minus EO. The
O stands for output, which this book writes EE. They say "all of these terms are expressed as
energy per unit of time". So in their equation ES is the rate of change of the stores, not the
stores. The stores themselves come only from the integral.

**Where this picture breaks.** The straight-line rate is made up. It was chosen so that the trapezium is exact. A real
person's net rate does not change in a straight line and is never measured at every moment.
Two readings joined by a straight line give an estimate, not the integral.

Stored energy is not body weight. Turning 2,500 kilocalories into kilograms needs to know what
tissue was gained or lost, which `S01-R1-C02` covers and this section does not.

**Figure.** A made-up net rate falling in a straight line from 300 to minus 200 kilocalories a day over 50 days. The triangle above the axis is 4500 kilocalories gained, the one below is 2000 lost, and the change in stores is 2500.

*What the figure shows:* A straight line falling from 300 at day 0 to minus 200 at day 50, crossing zero at day 30, with the gain above the axis and the loss below it labelled.

**Must know points for you.**

- Area below the time axis is subtracted. A total that adds it instead answers "how much energy moved either way", not "how much did the stores change". Before you accept a change in stores, check that the days of loss were taken away.
- A shrinking surplus is still a surplus. While intake minus expenditure stays above zero, the stores rise, however fast the surplus is shrinking. They start to fall only once the rate crosses zero.
- The trapezium is exact only for a rate that changes in a straight line between the two readings. For any other rate it is an estimate. Readings far apart can hide a bend, so ask how often the rate was measured before you trust an exact-looking total.
- Hall's ES = EI minus EO is an equation between rates. Before you quote any figure called ES, ask whether its unit is kilocalories or kilocalories a day. The first is a change in stores, the second is how fast they are changing.
- Check the unit of every integral: the rate's unit times the time's unit. If your answer still carries "per day", you have a rate or an average, not a change in the stock.
- A small error in a daily rate grows in the integral. Hall and colleagues put the uncertainty of doubly labelled water at more than 100 kilocalories a day. Held in one direction for a year, 100 a day is 36,500 kilocalories. So a stores change built from measured rates can be far less certain than each rate looks.

**Exercise 1** (interpretation). Hall and colleagues' consensus statement (*American Journal of Clinical Nutrition* 2012) says
this about the energy balance equation.

> the rate of change in body ES is equal to the difference between the rates of EI and EO.

They add that every term is energy per unit of time.

Write the sentence first as an equation between rates, in this book's notation. Then write it
as an integral that gives the change in stores between day a and day b. Say what each symbol
stands for and give its unit.

**1.** Look at ∫ from 2 to 7 of (3t plus 1) dt. Name the lower limit, the upper limit, the integrand
and the variable. Then work out the integral.

**2.** Work out ∫ from 0 to 6 of 4 dt, and ∫ from 0 to 6 of -4 dt.

**3.** Work out ∫ from 0 to 8 of 5t dt.

**4.** Work out ∫ from 0 to 10 of (6 minus t) dt. Then work out the total area between the line and
the axis, counting all of it as positive, and say why the two differ.

**5.** Work out the average value of 2t plus 4 from t = 1 to t = 5.

**6.** A rate f(t) has ∫ from 0 to 10 of f(t) dt = 50 and ∫ from 0 to 4 of f(t) dt = 18. Work out ∫
from 4 to 10 of f(t) dt, and ∫ from 10 to 4 of f(t) dt.

**7.** Doubly labelled water measures what a person spends (`S01-R1-C03`). Hall and colleagues say
its figure for expenditure can be off by more than 100 kilocalories a day (*American Journal
of Clinical Nutrition* 2012). Take a measuring period of 14 days. That is the upper end of the
range in `S01-R1-C03`. Suppose the error runs the same way on every day. Work out the smallest
error this gives in the total spent over the 14 days.

**8.** Hall and colleagues (*Lancet* 2011) model a cut in intake of 480 kilocalories a day. First
suppose the person's net deficit stays at 480 a day for 365 days. Then suppose instead that it
falls in a straight line from 480 to 240 a day over the same 365 days. That second shape is
made up for this problem. Work out the total deficit each way, and the average daily deficit
in the second case.

**9.** A person's energy stores fall by 9,000 kilocalories over 30 days. Work out their average net
rate. Then suppose the rate changed along a straight line and started at minus 500 kilocalories
a day. Work out where it ended.

**10.** Here is a worked answer. Find the step that broke.

```working
the net rate starts at -400 kcal/day and rises in a straight line to 200 kcal/day over 30 days
it crosses zero at day 20
area below the axis = 0.5 times 20 times 400 = 4000
area above the axis = 0.5 times 10 times 200 = 1000
total = 4000 plus 1000 = 5000
so the stores fell by 5000 kcal
```

**11.** Here is a worked answer. Find the step that broke.

```working
a surplus of 300 kcal/day is held for 4 weeks
the change in stores = ∫ from 0 to 4 of 300 dt
300 times 4 = 1200
so the stores rose by 1200 kcal
```

**12.** Here is a worked answer. Find the step that broke.

```working
the net deficit was read three times: 400 kcal/day on day 0, 300 on day 10, 0 on day 40
take the rate as a straight line between readings
average rate = (400 plus 300 plus 0) divided by 3 = 233.3
total = 233.3 times 40 = 9333
```

**13.** A trial report says this. The trial and its figures are made up for this problem.

> Participants' average energy imbalance was minus 150 kcal a day over 12 weeks, so each lost
> 12,600 kcal from their stores.

Hall and colleagues (*American Journal of Clinical Nutrition* 2012) say the combined error in
measuring energy imbalance "can easily reach 1000 kcal/d".

Decide what to compute, compute it, and say what your answer does not establish.

**14.** A colleague says this about a patient. The patient and the figures are made up for this
problem.

> Her surplus has been falling for two months, from 400 kcal a day to zero. So she has been
> losing weight.

Decide what to compute, compute it, and say what your answer does not establish.

