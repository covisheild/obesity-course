# C7 · Rate of change, average and instantaneous, without the machinery

**Definition.** A rate of change is a change in a quantity divided by the time that change took. Its unit is
the unit of the quantity divided by the unit of time.

The average rate of change over an interval is the change between the two ends of the interval
divided by the length of the interval. Drawn on a graph with time along the bottom, it is the
slope of the straight line joining the two end points. That joining line is a chord.

The rate at an instant is the rate of change at one moment rather than over a stretch of time.
On a graph it is the steepness of the curve at that one point, which is the slope of the
straight line that touches the curve there. That touching line is a tangent.

For a straight line the average rate over every interval is the same number, and it equals the
rate at every instant on the line. For a curve the two differ, and an average over an interval
fixes nothing about where inside that interval the change happened.

An average rate over an interval is exact as a statement about that interval. It becomes a
claim about a moment only when somebody quotes it as one.

For a quantity that changes without jumping, there is at least one moment inside the interval
at which the rate equals the average over it. Which moment that is, the average does not say.

**In plain terms.** A slope is a rate. You met that in the section on graphs. This section is about the rate you will
meet most often, which is how fast a quantity changes as time passes.

A rate of change is a change divided by the time it took. Take the quantity at the start. Take it
at the end. Subtract to get the change. Divide by how long it took.

```working
    the rate of change = the change in the quantity, divided by the time it took
```

The unit falls out of the division, exactly as it did for a slope. Kilograms divided by months is
kilograms per month. A rate of change is never in kilograms on its own, and a rate quoted without
its unit is a number you cannot check.

Now the part people get wrong, and it is the whole of this section.

A rate can be worked out over a stretch of time, or asked for at a single moment. Those are two
different quantities and they usually have two different values.

**The average rate over an interval.** It uses the value at the start and the value at the end. It
uses nothing in between. So it can tell you nothing about what happened in between.

**The rate at one moment.** This is how fast the quantity is changing right now. Its name is the
instantaneous rate. On a graph it is the steepness of the line at that single point.

For a straight line the two are the same number. A straight line has one steepness and it has it
everywhere. Pick any two points on it and you get the same answer.

For a curve they come apart. A curve is steep in some places and nearly flat in others. An
average across the whole of it can sit far from its steepness at both ends.

Somewhere in between, though, the curve is exactly as steep as the average. It has to be. A
curve that stayed steeper than the average all the way across would finish higher than it does.
One that stayed flatter would finish lower. So the steepness passes through the average on the
way. What the average will not tell you is where it passed. Nor will it tell you how far the
curve got from the average on either side of that point.

Here is how you get each one off a drawn curve, with a ruler.

For the average rate between two points, lay the ruler across those two points. Read its slope,
which is the rise divided by the run. The line you have laid down has a name: it is a chord.

For the rate at one point, lay the ruler so that it touches the curve at that point and runs
along it. Read its slope the same way. That touching line has a name too: it is a tangent.

A shorter interval gives you a closer answer. Take the average over a month and you get the
month. Take it over a day around the same moment and you get much nearer to the moment itself.

One more thing, so that you recognise it on somebody else's page. The rate at a moment has a
name in mathematics: the derivative. It is written dy/dx, said "dee y by dee x". The two letters
d each mean "a change in". The whole symbol is the steepness at one point, which is what you
have just been reading off a curve with a ruler. That is all you need. Nothing in this book asks
you to work one out.

Last, run the unit check from the section on dimensional analysis before you believe any rate.
A quantity in kilograms, changing over months, gives a rate in kilograms per month. If somebody
hands you a rate whose unit is not the quantity divided by a time, it is not a rate of change.

**Illustration.** Start with a sentence that is two thirds right, because the true part is what carries the false
part past a reader.

Take the saturating column from the section before this one. A quantity was recorded six times,
one month apart.

```table
months from the start  the quantity
0                      10
1                      30
2                      42
3                      49.2
4                      53.5
5                      56.1
```

A note about it says this.

> It rose by about 46 over five months. That is about 9 a month. Two more months take it past
> 70.

Test the first claim. Subtract the first value from the last.

```working
    56.1 minus 10 = 46.1
```

Test the second. Divide that change by the time it took.

```working
    46.1 divided by 5 = 9.22
```

About 9.22 a month. So the first two sentences hold. That number is the average rate of change
over the five months, and it is correct.

Now work out the rate over each single month. Each one is a change divided by one month.

```working
    30 minus 10 = 20
    42 minus 30 = 12
    49.2 minus 42 = 7.2
    53.5 minus 49.2 = 4.3
    56.1 minus 53.5 = 2.6
```

Put them beside the months they belong to.

```table
the month       the rate over it
first           20 a month
second          12 a month
third           7.2 a month
fourth          4.3 a month
fifth           2.6 a month
```

The rate over the first month was 20 a month and over the fifth it was 2.6 a month. No single
month ran at 9.22. The average is a true statement about the five months together and a false
statement about any one of them.

That is why the third sentence of the note fails. It takes an average over the past and uses it
as the rate now. Use the most recent month's rate instead, which is 2.6 a month.

```working
    2.6 times 2 = 5.2
    56.1 plus 5.2 = 61.3
```

About 61.3, not past 70. Treat that figure as a ceiling on what to expect rather than as a
forecast. The monthly rate has fallen at every step so far, and nothing in the six readings
says it has stopped. The note is not wrong about its arithmetic. It is wrong about which
interval its arithmetic describes.

Now the easy case, so that you can feel the difference.

Section 3(1) of the National Food Security Act, 2013 entitles a person in a priority household
to five kilograms of foodgrains per person per month. A household of four is counted for twenty
kilograms a month.

```working
    5 times 4 = 20
```

Say the house starts with 10 kilograms in it and nothing is taken out. Here is the grain in the
house, month by month.

```table
months from today  kilograms in the house
0                  10
1                  30
2                  50
3                  70
4                  90
```

Take the average rate over the whole four months.

```working
    90 minus 10 = 80
    80 divided by 4 = 20
```

Twenty kilograms a month. Now take it over the third month alone.

```working
    70 minus 50 = 20
    20 divided by 1 = 20
```

Twenty again. Take any interval you like and you will get twenty, because the points sit on a
straight line and a straight line has one steepness. Here the average rate and the rate at any
moment are the same number, and there is nothing to argue about.

So the question to carry away is not "what is the rate". It is "over what interval".

Finish with the unit, because a rate without one is not checkable. Kilograms up the side,
months along the bottom.

```working
    kilograms divided by months
    = kilograms per month
```

Twenty kilograms a month. Not twenty.

**Where this picture breaks.** The six values in the first table are bare numbers. They are the ones from the section before
this one and they describe nothing in the world.

An average rate over an interval is exact for that interval. It stops being true the moment
somebody quotes it as the rate now, and that is the only way it goes wrong.

A rate read off a drawn curve with a ruler is an estimate. How good it is depends on how well
the curve was drawn and how steadily you held the ruler.

A quantity measured once a month has no rate you can check between the measurements. The five
monthly rates above describe five whole months. What happened inside any one of them is not in
the table.

And time is not the only thing a quantity can change against. A change in an outcome for each
extra unit of a dose works the same way, and every word of this section applies to it. Time is
used throughout only because it is the case you will meet most.

**Must know points for you.**

- Ask "over what interval" every time somebody hands you a rate. A rate with no interval attached is not yet a number you can use, and the interval is usually the whole of the disagreement.
- An average rate over a stretch of time is not the rate now. It is built from the first value and the last value alone. It uses nothing that happened in between. So it can sit far from the rate at both ends of the stretch. Somewhere inside the stretch the quantity was changing at exactly the average rate, and the average never tells you where.
- Quote a rate with its unit, taken from the quantity divided by the time. Twenty kilograms a month is a claim somebody can check. Twenty is not, and it is the form in which wrong rates travel.
- Two quantities can share an average rate and have nothing else in common. One may have risen steadily and the other may have risen fast and then stopped. Ask for the values in between before you accept that two things are behaving alike.
- A rate you read off a curve by eye is an estimate and not a measurement. It is only as good as the drawing under your ruler. Use it to say which part of the curve is steeper, and go back to the numbers before you quote a figure.
- Where gains are slowing, an average over the whole programme is the number most flattering to it. Ask for the rate over the most recent interval before you agree to continue on the strength of the average.
- When a press line says a quantity is rising at some figure a month, ask which months were used. A rise averaged over a year and a rise over last month are different claims, and only one of them is about now.
- Teach a trainee to write the interval down beside every rate they compute, before the number leaves their page. A rate that loses its interval on the way to a slide cannot be got back.

**Exercise 1** (interpretation). A figure has months along the bottom and a count up the side. The curve climbs steeply for the
first three months, then bends over and runs almost flat for the next nine.

Say what the average rate over the twelve months describes, and what it does not. Then say
which two numbers you would ask for instead, and why those two.

**Exercise 2** (critique). A programme note contains this line.

> Coverage has grown at an average of 6 points a year for four years. On that trend we reach
> the target of 40 points above baseline in three more years.

The yearly gains were 12 points, then 6, then 3, then 1.5.

Say what is wrong with the second sentence, and say what you would put in its place.

**Exercise 3** (teaching). A first-year resident has ten minutes and a whiteboard. They keep saying "the rate" about a
quantity that is changing, and they mean whichever rate is nearest to hand.

Teach them the difference between an average rate and a rate at a moment. They should leave
asking the right question about the next figure they see.

**1.** A quantity is 14 at the start and 38 at the end. The change took 6 units of time.

Work out the average rate of change.

**2.** Work out the average rate of change for each of these.

```working
    from 50 to 90, over 8 units of time
    from 90 to 50, over 8 units of time
    from 7 to 7, over 5 units of time
```

**3.** A quantity is recorded at equal steps: 4, 10, 20, 34, 52.

Work out the rate over each single step. Then work out the average rate over the whole run.

**4.** A quantity changes at an average rate of 7 for each unit of time.

Work out the change over 9 units of time. Then work out how long it takes the quantity to
change by 91.

**5.** Work out the unit of the rate of change in each of these cases.

```table
the quantity        the time it is changing over
kilograms           months
kilocalories        days
number of people    years
rupees              weeks
```

**6.** Section 3(1) of the National Food Security Act, 2013 entitles a person in a priority household
to five kilograms of foodgrains per person per month.

A household of six collects its full entitlement every month and takes nothing out of the
house. The house holds 12 kilograms today.

Write the grain in the house at months one, two and three. Work out the average rate of change
over those three months, with its unit. Then work out the rate over the second month alone and
say why the two agree.

**7.** A quantity is recorded once a month for five months: 200, 320, 380, 410, 425.

Work out the average rate of change over the whole five months. Then work out the rate over the
first month and the rate over the last month. Say which of the three you would quote to
somebody who asks how fast it is growing now, and why.

**8.** A quantity falls from 900 to 300 over 12 months.

Work out the average rate of change, with its sign. Then say what the sign means, and say what
this number does not tell you about the twelve months.

**9.** Two quantities are recorded at the same five monthly times.

```table
month  quantity P  quantity Q
0      100         100
1      130         190
2      160         230
3      190         248
4      220         256
```

Work out the average rate of change of each over the four months. Then work out the rate over
the last month for each. Say what the pair of comparisons shows.

**10.** Here is a worked answer. Find the step that broke.

```working
    a quantity goes from 40 to 100 over 5 months
    the change is 100 minus 40, which is 60
    the rate is the time divided by the change
    5 divided by 60 = 0.083
    so the quantity is rising at 0.083 a month
```

**11.** Here is a worked answer. Find the step that broke.

```working
    the monthly values are 10, 30, 42, 49.2, 53.5, 56.1
    the total rise is 56.1 minus 10, which is 46.1
    that took 5 months, so the average rate is 46.1 divided by 5
    46.1 divided by 5 = 9.22
    so the quantity is currently rising at 9.22 a month
    and in five more months it will be about 56.1 plus 46.1
```

**12.** Here is a worked answer. Find the step that broke.

```working
    a curve is drawn with months along the bottom and kilograms up the side
    at month 2 the curve passes through 30 kilograms
    at month 8 the curve passes through 66 kilograms
    the rate at month 8 is the rise divided by the run
    66 minus 30 = 36
    36 divided by 6 = 6
    so at month 8 the quantity is rising at 6 kilograms a month
```

**13.** A district note crosses your desk with this line in it.

> The waiting list has come down from 900 to 300 over the last twelve months. That is a steady
> clearance rate, so the list will be empty in six more months.

The office, the list and both figures are made up for this problem. No real service is being
described.

Decide what to compute, compute it, and say what your answer does not establish.

**14.** A colleague sends a one-line summary of a programme review.

> Gains were 12 points, then 6, then 3, then 1.5, over four years. That averages about 5.6
> points a year, so budget for the same again next year.

The programme and all four figures are made up for this problem. No real programme is being
described.

Decide what to compute, compute it, and say what your answer does not establish.

