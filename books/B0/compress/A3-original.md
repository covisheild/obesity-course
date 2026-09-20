### A3 · Decimals, rounding, and significant figures

*B0-R0-C03 · derivable*

**Definition.** A decimal continues place value to the right of a point. Each place to the right is worth one
tenth of the place on its left, so the places run tenths, hundredths, thousandths. A decimal is
therefore a fraction whose denominator is ten, a hundred, a thousand, and so on.

Rounding is choosing which place to stop at and adjusting the last kept digit for what follows
it. Look at the first digit being dropped: below five, the kept digit stands; five or above, it
goes up by one.

The significant figures of a number are the digits that carry information about the quantity,
counted from the first digit that is not zero. A quantity calculated from other quantities
cannot carry more significant figures than the least precise of them. A calculator has no way
to know this and will print as many digits as its display holds.

**In plain terms.** A decimal is the same place-value rule, carried on past the point. To the left of the point, each
step is ten times bigger. To the right, each step is ten times smaller: tenths, then hundredths,
then thousandths.

So 0.17 is seventeen hundredths. A decimal is just a fraction wearing different clothes, and the
denominator is always ten, or a hundred, or a thousand.

Rounding is deciding where to stop. Pick the place you want to stop at and look at the very next
digit. If it is four or less, leave your last digit alone. If it is five or more, push it up by
one. That is all there is to it.

Now the part that matters far more than the rule. A calculator will hand you ten digits whether
or not those digits mean anything. The digits it gives you are not evidence. They are what the
division happened to produce.

Your answer cannot be more exact than the numbers you put in. Divide something you know to two
digits by something you know to two digits, and you know the answer to about two digits. Writing
down eight of them does not make you more careful. It makes a claim about the world that nothing
you have supports. A reader who notices will stop trusting the rest of your numbers too.

The habit that follows is simple. Keep every digit while you are working. Round once, at the very
end, and round to what your weakest input earned.

**Illustration.** Open `sources/nfsa_2013.txt` again and search inside it for "five kilograms". Two hits, and both
are inside section 3. The first is section 3(1), which gives a person in a priority household
five kilograms of foodgrains per person per month.

Somebody now asks you the obvious follow-up. How much is that a day?

Type five, divide by thirty, and read what the calculator says.

```
    5 divided by 30 = 0.1666666667
```

Here is the mistake, and it goes into real documents. The figure is copied straight across, and
a report goes out saying each person receives 0.1666666667 kilograms of grain a day.

Count the digits after the point. Ten of them. A tenth decimal place in kilograms is a
ten-millionth of a gram. That last digit is claiming to pin the daily ration down that far.
Nothing you did could possibly support that.

Look at where the ten digits came from. Two numbers went in. The five is exact: it is not a
measurement, it is a figure written into an Act, and it is five and nothing else. The thirty is
not exact at all. You chose it. A month is twenty-eight days, or thirty, or thirty-one.

So work the two ends instead of one middle.

```
    5 divided by 31 = 0.16129...
    5 divided by 28 = 0.17857...
```

The honest answer sits somewhere between 0.16 and 0.18 kilograms a day. Two digits, not ten. And
even those two are only as good as your guess about the month.

Now round the middle case properly, so you can see the rule work. You have 0.1666666667 and you
want two places after the point. The two places give you 0.16. The next digit along is a 6,
which is five or more, so the 6 you are keeping goes up to 7.

```
    0.1666666667 rounds to 0.17
```

Last, the trap inside the habit. Suppose you round first and then carry on. Round to 0.17, then
multiply by 30 to get back to a month.

```
    0.17 times 30 = 5.1
```

You started with exactly 5 and came back with 5.1. The rounding leaked. That is why you round
once, at the end, and never in the middle of a chain.

The best answer to the original question is the one that does not round at all. Each person
gets 5 kilograms a month. If somebody needs a daily figure, give them 0.16 to 0.18 kilograms and
say where the spread came from.

**Where this picture breaks.** Significant figures are a rough guide to precision, not a measure of it. They tell you roughly
how many digits you have earned. They do not tell you how wrong the number might be. Two
numbers with the same three digits can be trustworthy to very different degrees. That is a
different question, and a later part of this book takes it up.

The rounding rule itself has an edge. When the digit you are dropping is exactly five and
nothing follows it, the rule above always pushes up. That nudges a long column of numbers
slightly high. It rarely matters. It matters when you are rounding thousands of values and then
adding them.

And notice the asymmetry in the worked example. The five was exact because an Act said so. A
figure that came off a weighing scale or out of a survey is never exact in that way. So the
precision question is sharper there, not softer. Treating a legal figure and a measured figure
the same way is the mistake this section is really guarding against.

**Must know points for you.**

- The digits on a calculator display are not precision. They are what the division produced. Copying them into a report claims an exactness nothing you did supports, and the first reader who notices will discount every other number you brought.

- Keep full precision while you work and round once, at the end, to what your weakest input earned. Rounding in the middle of a chain leaks, and the leak grows with every further step.

- A figure fixed by law and a figure read off an instrument look identical on the page and are not the same kind of number. Five kilograms in an Act is exactly five. Five kilograms on a scale is not. Ask which kind you are holding before you decide how to round it.

- Indian entitlements are commonly written per month while reporting wants a daily figure. That one division is where false precision enters. The number of days is a choice you made, and the decimal places hide that you made it.

- When a number you are given carries more digits than its source could support, say so at the time. It is the cheapest possible challenge and it needs no data of your own. Very often nobody in the room knew where the figure came from.

- Do not quote a spuriously precise figure in public even when it is the one you were handed. It invites a question about the last digit that you cannot answer, and losing that exchange costs you the point you were actually making.


**Exercise B0-R0-C03-E1** (calculation). A household of six people is in a priority household under section 3(1) of the National Food
Security Act, 2013. Work out the household's monthly entitlement, then its daily entitlement.
Give the daily figure to a precision you can defend, and say in one line why you stopped there.

*Record your confidence as a percentage before turning to the answer.*

**Exercise B0-R0-C03-E2** (critique). A district report reads: "Average grain lifted per beneficiary was 4.8732 kg per month against
an entitlement of 5 kg." Nothing here is arithmetically wrong. Name what you would ask about the
figure 4.8732, and say what you expect the answer to be.

**Practice.** Ten problems on this technique, easiest first. Work them on paper. The answers are in the appendix at the back, under these numbers.

**B0-R0-C03-P01.** Round each of these to two places after the point.

```
    0.3849      12.0761      0.0955      7.2950
```

**B0-R0-C03-P02.** How many significant figures does each of these carry?

```
    450      0.0072      6.030      1,200
```

**B0-R0-C03-P03.** Work out 17 divided by 7. Write the calculator's full display, then give the answer to three
significant figures.

**B0-R0-C03-P04.** Section 3(1) of the National Food Security Act, 2013 gives five kilograms of foodgrains per
person per month. Work out the figure per week, using 4 weeks in a month, and give it to a
precision you can defend.

**B0-R0-C03-P05.** A hot cooked meal is set at 450 calories by the second schedule of the National Food Security
Act, 2013. A child attends on 196 of the year's school days. Work out the year's calories from
the meal, and say how many significant figures the answer deserves.

**B0-R0-C03-P06.** A store issues 1,850 kilograms of grain to 387 households in a month. Work out the average per
household and report it to a precision you can defend. Say in one line what fixed the
precision.

**B0-R0-C03-P07.** Here is a worked answer. Find the step that broke.

```
    2.4 times 3.6 = 8.64
    8.64 rounded to 2 significant figures = 8.6
    8.6 divided by 4 = 2.15
    final answer, to 2 significant figures = 2.2
```

**B0-R0-C03-P08.** A district report reads: "Coverage stands at 64.8135 per cent."

It was computed from a count of covered households and a count of total households, both taken
from a register. Find what is wrong with the figure as reported.

**B0-R0-C03-P09.** Here is a line from a note.

> Average household grain offtake was 4.8732 kg against an entitlement of 5 kg, a shortfall of
> 2.536 per cent.

Decide what to compute, compute it, and say what your answer does not establish.

**B0-R0-C03-P10.** Somebody sends you a one-line finding and asks whether to publish it.

> Mean intake fell from 2,014.6 to 1,987.3 calories a day, a fall of 1.36 per cent.

Decide what to compute, compute it, and say what your answer does not establish.
