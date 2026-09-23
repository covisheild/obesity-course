# C8 · Accumulation, a running total, without the machinery

**Definition.** An amount is a rate multiplied by the length of time over which that rate held.

A running total is the sum of those amounts across successive intervals.

Drawn with time along the bottom and the rate up the side, each amount is the area of a
rectangle whose width is the interval and whose height is the rate over it. The running total
up to any time is the area under the rate line up to that time.

The total is certain to be exact only where the rate held steady across each interval. Where
the rate moved inside an interval, the rectangle over-counts or under-counts. Take the largest gap between the
height used and the rate at any moment inside that interval. That gap, multiplied by the length
of the interval, is the most the rectangle can be wrong by. The error is an amount and carries
the quantity's unit.

Added across the intervals, those amounts are the most the total can be wrong by. That most is
zero only where the rate held steady inside every interval.

Take a rate that only falls, or only rises, with each height read at one end of its interval.
Halving the intervals then halves the most the total can be wrong by, and never raises the
actual error. Where the rate rises and falls, halving usually lowers the most, but not always.
The actual error can then grow or shrink, though it never passes the most for the intervals
used.

A rate and a total are different quantities with different units, and neither can be read off
the other without the time it applied over.

**In plain terms.** The section before this one took a quantity and got a rate out of it. This one goes the other
way. You start with a rate and you get an amount back.

A rate multiplied by a time gives an amount.

```working
    the amount = the rate, times the length of time the rate held for
```

Twenty kilograms a month, held for three months, gives sixty kilograms.

```working
    20 times 3 = 60
```

Check the unit, because the unit is what tells you the step was done the right way round.
Kilograms per month, multiplied by months, leaves kilograms. The months cancel, exactly as they
did in the section on dimensional analysis.

They cancel only when the two time units match. Say water is drawn at 40 litres a day for 2
months, both figures made up. Litres a day times months is not litres. So turn the months into
days first. Count a month as 30 days, and say that you did.

```working
    2 times 30 = 60
    40 times 60 = 2400
```

Sixty days at 40 litres a day is 2,400 litres. Now the days cancel.

Rates change. So you cut the time into intervals short enough that the rate can be treated as
steady inside each one. Work out the amount for each interval. Then add them up as you go.

That sum is called a running total.

Draw time along the bottom and the rate up the side. Mark the rate over each interval at the
height it reached. The line those marks make across the figure is the rate line, and everything
below it is what you are about to measure.

Now take one interval and draw a rectangle on it. Its height is the rate over that interval, so
its top sits on the rate line.

The area of that rectangle is its height times its width. The area of the rectangle is the
amount.

Stack the rectangles side by side across the whole stretch of time. The total area is the running
total.

A rectangle assumes the rate held steady across its whole width. Where the rate was falling, a
rectangle drawn at the starting rate counts too much. Where the rate was rising, it counts too
little.

Now cut each interval in half. Where the rate only falls, or only rises, the error does not grow,
and it usually shrinks. Where the rate rises and falls, the over-counts and under-counts can
partly cancel. Then halving can leave the error larger. Only a rate that held steady inside
every interval gives a total you know to be exact.

One name, so you recognise it on somebody else's page. The total under a rate line is called an
integral. It is written with the sign ∫, which is a stretched letter S for sum. That is all you
need. Nothing in this book asks you to work one out.

**Illustration.** A store issues grain. Somebody records the rate at which it goes out, month by month, for six
months.

```table
month  kilograms a month going out
1      20
2      20
3      15
4      10
5      10
6      5
```

A note on the file says this.

> The store issues 20 kilograms a month. Over six months that is 120 kilograms.

The multiplication is right.

The error is that 20 was the rate in two of the six months and not in the other four. One
month's rate was used as though it held for all six.

Do it properly. Each month is one interval, and each interval's amount is its rate times one
month.

Add them as a running total, which is the amount so far after each month.

```working
    20 plus 20 = 40
    40 plus 15 = 55
    55 plus 10 = 65
    65 plus 10 = 75
    75 plus 5 = 80
```

Eighty kilograms over the six months, against the 120 in the note. The note is out by half
again.

Now draw it, because the picture is how everybody else will show you this.

Put months along the bottom and kilograms a month up the side. Mark each month's rate at the
height it reached, and the six marks make one stepped line across the figure. That line is the
rate line.

Now over month one, draw a rectangle one month wide and 20 kilograms a month tall, so that its
top sits on the rate line. Its area is its height times its width.

```working
    20 times 1 = 20
```

Twenty kilograms. Do the same for each month and you get six rectangles standing side by side.
Their heights are 20, 20, 15, 10, 10 and 5, and every width is one month. The whole shaded area
under the rate line is 80 kilograms, which is the answer you already have.

Check the unit before you go on.

```working
    kilograms per month, times months
    = kilograms
```

A total is in the unit of the quantity, never in the unit of the rate.

Those 80 kilograms went out of the store, so for the store itself they are subtracted. Say it
held 200 kilograms at the start and nothing came in. That 200 is made up for this line.

```working
    200 minus 80 = 120
```

One hundred and twenty kilograms left. Subtract month by month instead. The running total of
grain issued still rises, 20, 40, 55, 65, 75, 80. What falls is the stock left in the store.

```working
    200 minus 20 = 180
    180 minus 20 = 160
    160 minus 15 = 145
    145 minus 10 = 135
    135 minus 10 = 125
    125 minus 5 = 120
```

A flow out is an amount taken away rather than added.

Last, the part that decides how much your total is worth.

Take a rate that is falling steadily, from 20 kilograms a month down to nothing over four
months. Read it at the start of each month and you get 20, 15, 10 and 5.

This rate line is a different drawing from the one for the store. There we took each month's
rate as holding for the whole month, so the line was a staircase and the rectangles sat exactly
on it. Here the rate
falls all the time, so its line is a straight slope from 20 down to nothing. Rectangles always
make a staircase. The gap between that staircase and the slope is what the table below
measures.

Build the total from four rectangles, each one month wide.

```working
    20 plus 15 plus 10 plus 5 = 50
```

Fifty kilograms.

Now cut the intervals in half. Read the rate every half month and you get 20, 17.5, 15, 12.5,
10, 7.5, 5 and 2.5. Each rectangle is half a month wide, so add the eight heights and multiply
by half a month.

```working
    20 plus 17.5 plus 15 plus 12.5 plus 10 plus 7.5 plus 5 plus 2.5 = 90
    90 times 0.5 = 45
```

Forty-five kilograms.

The rate falls in a straight line from 20 to nothing, so its average over the four months is
halfway between the two ends.

```working
    20 plus 0 = 20
    20 divided by 2 = 10
```

Ten kilograms a month, for four months.

```working
    10 times 4 = 40
```

Forty kilograms, and that one is exact.

Put the three answers beside each other and watch the error close.

```table
how the total was built     answer     how far above the exact answer
four whole-month blocks     50 kg      10 kg
eight half-month blocks     45 kg      5 kg
the exact total             40 kg      none
```

Halving the interval halved the error, and it did that because this rate falls in a straight
line. On a rate like this one, halving again would halve the error again. Read that as a
property of a rate that changes steadily, not as a rule about intervals.

Where a rate bends but keeps falling, halving the intervals still shrinks the error, but by no
fixed share you can count on. Where a rate rises over part of the span and falls over the rest,
two rectangle errors can point opposite ways and partly cancel. Halving can then leave the
total error larger than it was. It still never passes the most from the definition: each
interval's largest gap times its width, added across the intervals.

In this worked case the error never reaches zero, and every rectangle counts too much, because
the rate was falling inside each one of them.

So a total is not one number. It is one number and one assumption, and the assumption is that
the rate held across each interval you used.

**Where this picture breaks.** The six monthly rates in the first table are bare numbers.

Area is a total only when time is along the bottom and a rate is up the side. Read both axis labels
before you shade anything.

A rectangle built on the rate at the start of an interval counts too much while the rate is falling.
While it keeps falling, halving the intervals shrinks that error and never removes it. Where the
rate rises and falls, halving can leave the error larger.

And every amount here is an amount going one way. A flow out of something is an amount subtracted
rather than added, and the amount left then falls.

**Figure.** Each rectangle is one month's rate multiplied by one month, so its area is that month's amount. Stacking them is the running total, and the total is the area under the whole rate line.

*What the figure shows:* Six rectangles of equal width standing on an axis of months, labelled 20, 20, 15, 10, 10 and 5 kilograms a month. Their tops make one stepped line across the figure, which is the rate line. The heights fall in stages with a flat pair at the 20 level and another at the 10 level. The six areas add to 80 kilograms.

**Must know points for you.**

- Multiply a rate by the time it held for before you quote any total.
- Check the unit of every total. If the unit of your answer still has a time on the bottom, you have added rates instead of accumulating them.
- Taking one measurement of a rate and multiplying it by a whole year is the commonest way a total goes wrong.
- The area under a rate line is a total and not a rate.
- A total carries its interval assumption with it. Halving the intervals usually shrinks the error, but where the rate rises and falls it can make it larger. Only a rate that held steady inside every interval gives a total you know to be exact.
- Before accepting an annual figure built from one measurement, ask how many times the rate was measured and when. A yearly total from a single reading is a forecast wearing the clothes of a count.
- A total says how much has piled up, a rate says how fast it is piling up now, and the two answer different questions.
- Teach a trainee to draw the rectangles before reaching for a formula.

**Exercise 1** (interpretation). A figure has months along the bottom and litres a day up the side. The line starts high, falls
for six months, and then runs flat for six more.

Say what the area under the line stands for, and give its unit. Then say what the figure does
not tell you.

**Exercise 2** (critique). A district file carries this line.

> The depot issued 400 bags in the first week of April. That is 400 a week, so it will issue
> about 20,800 bags this year.

Take a year as 52 weeks.

Say what has been assumed, say what you would ask for, and say what you would write in its
place.

**Exercise 3** (teaching). A health secretary has one page and three minutes. Two reports have reached them about the same
programme. One gives a monthly rate and one gives a yearly total, and the two do not look like
they can both be true.

Write what you would put on that page.

**1.** A quantity grows at a steady rate of 7 for each unit of time.

Work out how much is added over 9 units of time, over 20 units of time, and over half a unit of
time.

**2.** A quantity changes at different rates over three successive stretches of time.

```table
stretch  the rate  how long it held
first    12        4 units of time
second   5         6 units of time
third    20        2 units of time
```

Work out the amount over each stretch, and the total over all three.

**3.** A quantity is added at these rates over six successive intervals, each one unit of time long:
9, 9, 4, 4, 4, 2.

Write the running total after each interval.

**4.** A quantity accumulates over three stretches. Over the first it grows at 10 for 5 units of time.
Over the second it grows at 6 for 5 units of time. Over the third it grows at 6 for 10 units of
time.

Work out the total. Then work out the average rate over the whole twenty units of time.

**5.** Section 3(1) of the National Food Security Act, 2013 entitles a person in a priority household
to five kilograms of foodgrains per person per month.

Work out the grain a household of seven is counted for over a full year. Show the rate you used
and the time you multiplied it by, and give the unit at every line. Then say which figure in
your working comes from the Act and which are yours.

**6.** A rate is recorded once a month for six months, in litres a month: 300, 300, 450, 450, 200,
100.

Work out the running total after each month, and the total over the six months. Then state the
assumption the total rests on.

**7.** A rate is measured every three months and comes out at 40 units a month, then 60, then 60, then
20. Each reading is the rate for the three months that start on the day it was taken, and the
four together cover the year.

Work out the total across the year. Then work out what you would get by adding the four
readings, and say what unit that sum is in.

**8.** A quantity accumulates over 8 months and the total comes to 96 kilograms. Over the first 2 months
the rate was 18 kilograms a month.

Work out the average rate over the whole 8 months. Then work out the total over the remaining 6
months, and the average rate over those 6 months.

**9.** Here is a worked answer. Find the step that broke.

```working
    a tank is filling and the rate is measured at four times
    the readings are 12, 9, 6 and 3 litres a minute
    the total is 12 plus 9 plus 6 plus 3
    12 plus 9 plus 6 plus 3 = 30
    so 30 litres went in
```

**10.** Here is a worked answer. Find the step that broke.

```working
    a figure has months along the bottom and kilograms in the store up the side
    the line runs at about 300 kilograms for all twelve months
    the area under the line is 300 times 12
    300 times 12 = 3600
    so 3,600 kilograms passed through the store during the year
```

**11.** A note reaches you from a block office.

> Our vehicle used 8 litres of fuel an hour on the day we measured it. It runs about 6 hours a
> day. So budget for about 17,500 litres this year.

The office, the vehicle and all three figures are made up for this problem. No real service is
being described.

Decide what to compute, compute it, and say what your answer does not establish.

**12.** A line in a review meeting goes like this.

> The scheme distributed 24 lakh kilograms of grain last year. The year before it was 20
> lakh. It is clearly reaching more people than ever.

The scheme and both figures are made up for this problem. No real scheme is being described.

Decide what to compute, compute it, and say what your answer does not establish.

