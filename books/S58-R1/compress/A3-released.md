# A3 · Decimals, rounding, and significant figures

**Definition.** A decimal continues place value to the right of a point. Each place to the right is worth one
tenth of the place on its left, so the places run tenths, hundredths, thousandths.

Rounding is choosing which place to stop at and adjusting the last kept digit for what follows
it.

The significant figures of a number are the digits that carry information about the quantity,
counted from the first digit that is not zero. A quantity calculated from other quantities
cannot carry more significant figures than the least precise of them.

**In plain terms.** A decimal is the same place-value rule, carried on past the point. To the right, each step is
ten times smaller: tenths, then hundredths, then thousandths.

Rounding is deciding where to stop. Pick the place you want to stop at and look at the very next
digit. If it is four or less, leave your last digit alone. If it is five or more, push it up by
one.

Significant figures are the digits that carry the information. Start counting at the first digit
that is not a zero. Stop at the last digit written down. Everything in between counts, zeros
included.

So 0.00420 has three of them: the four, the two and the final zero. The zeros in front are only
holding the place. The zero at the end is holding nothing, so somebody put it there on purpose,
and it says the measurement reached that far.

Whole numbers ending in zeros are the awkward case. Write 4,200 and nobody can tell whether you
counted to the nearest hundred or to the nearest one. The digits cannot tell you. The person, the
table heading or the document has to. If none of them does, you do not know how precise the
number is. Do not treat it as exact until somebody tells you it is.

Your answer cannot be more exact than the numbers you put in. Divide something you know to two
digits by something you know to two digits, and you know the answer to about two digits.

**Illustration.** Open the National Food Security Act, 2013 again and search inside it for "five kilograms". The first is section
3(1), which gives a person in a priority household five kilograms of foodgrains per person per
month.

How much is that a day?

Type five, divide by thirty, and read what the calculator says.

```working
    5 divided by 30 = 0.1666666667
```

Here is the mistake, and it goes into real documents. The figure is copied straight across, and
a report goes out saying each person receives 0.1666666667 kilograms of grain a day.

Count the digits after the point. Ten of them. Nothing you did could possibly support that.

The five is exact: it is not a measurement, it is a figure written into an Act, and it is five
and nothing else. The thirty is not exact at all. You chose it. A month is twenty-eight days, or
thirty, or thirty-one.

So work the two ends instead of one middle.

```working
    5 divided by 31 = 0.16129...
    5 divided by 28 = 0.17857...
```

The honest answer sits somewhere between 0.16 and 0.18 kilograms a day. Two digits, not ten.

Now round the middle case properly, so you can see the rule work. You have 0.1666666667 and you
want two places after the point. The next digit along is a 6, which is five or more, so the 6
you are keeping goes up to 7.

```working
    0.1666666667 rounds to 0.17
```

Round to 0.17, then multiply by 30 to get back to a month.

```working
    0.17 times 30 = 5.1
```

You started with exactly 5 and came back with 5.1. The rounding leaked.

If somebody needs a daily figure, give them 0.16 to 0.18 kilograms and say where the spread came
from.

**Where this picture breaks.** Significant figures are a rough guide to precision, not a measure of it. They do not tell you
how wrong the number might be.

The rounding rule itself has an edge. When the digit you are dropping is exactly five and
nothing follows it, the rule above always pushes up. That nudges a long column of numbers
slightly high. It rarely matters. It matters when you are rounding thousands of values and then
adding them.

**Must know points for you.**

- The digits on a calculator display are not precision. They are what the division produced.
- Keep full precision while you work and round once, at the end, to what your weakest input earned.
- Five kilograms in an Act is exactly five. Five kilograms on a scale is not. Ask which kind you are holding before you decide how to round it.
- Indian entitlements are commonly written per month while reporting wants a daily figure. That one division is where false precision enters.
- When a number you are given carries more digits than its source could support, say so at the time.
- Do not quote a spuriously precise figure in public even when it is the one you were handed.

**Exercise 1** (calculation). A household of six people is in a priority household under section 3(1) of the National Food
Security Act, 2013. Work out the household's monthly entitlement, then its daily entitlement.
Give the daily figure to a precision you can defend, and say in one line why you stopped there.

**Exercise 2** (critique). A district report reads: "Average grain lifted per beneficiary was 4.8732 kg per month against
an entitlement of 5 kg." Nothing here is arithmetically wrong. Name what you would ask about the
figure 4.8732, and say what you expect the answer to be.

**1.** In the number 0.408, say what each digit after the point is worth. Then put these four numbers
in order, smallest first.

```working
    0.7      0.65      0.089      0.7000
```

**2.** Round each of these to two places after the point.

```working
    0.3849      12.0761      0.0955      7.2950
```working

**3.** How many significant figures does each of these carry?

```working
    450      0.0072      6.030      1,200
```working

**4.** Work out 17 divided by 7. Write the calculator's full display, then give the answer to three
significant figures.

**5.** Section 3(1) of the National Food Security Act, 2013 gives five kilograms of foodgrains per
person per month. Work out the figure per week, using 4 weeks in a month, and give it to a
precision you can defend.

**6.** A hot cooked meal is set at 450 calories by the second schedule of the National Food Security
Act, 2013. A child attends on 196 of the year's school days. Work out the year's calories from
the meal, and say how many significant figures the answer deserves.

**7.** A store issues 1,850 kilograms of grain to 387 households in a month. Work out the average per
household and report it to a precision you can defend. Say in one line what fixed the
precision.

**8.** Here is a worked answer. Find the step that broke.

```working
    2.4 times 3.6 = 8.64
    8.64 rounded to 2 significant figures = 8.6
    8.6 divided by 4 = 2.15
    final answer, to 2 significant figures = 2.2
```

**9.** A district report reads: "Coverage stands at 64.8135 per cent."

It was computed from a count of covered households and a count of total households, both taken
from a register. Find what is wrong with the figure as reported.

**10.** Somebody sends you a one-line finding and asks whether to publish it.

> Mean intake fell from 2,014.6 to 1,987.3 calories a day, a fall of 1.36 per cent.

Decide what to compute, compute it, and say what your answer does not establish.

