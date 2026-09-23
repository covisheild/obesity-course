# S01-R1-C05 · The accounting identity for a body

**Definition.** A person's body energy stores are a stock, in the sense Book 0 gives that word. Energy
intake and energy expenditure are flows that change that stock: intake adds to it, and
expenditure takes from it.

Draw the boundary at the mouth and skin, as `B0-R0-C33` shows for a person, and count intake
at the metabolisable line: the energy that crosses in after the losses in faeces, gas and
urine have already left, which `B0-R0-C32` defines. Then the balance line for a stock,
`B0-R0-C23`, gives the energy balance equation for a day.

The rate of change of body energy stores equals energy intake minus energy expenditure, both
counted over the same day.

The word "equals" here means "if and only if". Whenever the two sides are computed correctly
for the same boundary and the same interval, they match, with no exception and no remainder.
A day on which they appear not to match is a day on which a route was left off one side, not a
day on which the identity failed.

Because it is a balance line applied to one particular stock, the identity carries no
direction and no cause. It says what the numbers must do. It does not say why intake or
expenditure took the value it did.

**In plain terms.** A body holds energy the way a bank account holds money. What you eat and drink is a deposit.
Everything your body spends — moving, keeping warm, running your organs — is a withdrawal.

The balance changes only by deposits and withdrawals. Nothing else moves it.

So over one day, write it as a single line. How much your stores changed today equals what
went in today, minus what went out today.

```working
    the change in body energy stores over the day = energy intake for the day minus energy expenditure for the day
```

That line is not a guess about how bodies behave. It is what has to be true once you have
agreed where the boundary is — round the person, at the mouth and skin — and agreed that
"intake" means energy that actually crossed in, past the losses that never got absorbed.

Two things this line is not. It is not a promise that stores fall smoothly whenever intake is
below expenditure on average; day to day, food still sitting in the gut and water still moving
in the body can make one day's figure look wrong until you widen the interval. And it is not an
explanation of anything. It tells you the two sides must match. It never tells you why intake
or expenditure came out the way they did.

**Illustration.** Take a made-up week, seven days, to see the identity used forwards and then checked
backwards.

A person's energy stores are measured at the start of the week: 620 megajoules. Each day
their intake and expenditure, in megajoules, are recorded.

```table
day  intake (MJ)  expenditure (MJ)
1    9.1          8.6
2    8.4          8.7
3    9.6          8.5
4    8.0          9.0
5    9.3          8.4
6    8.8          8.8
7    9.9          8.3
```

Apply the identity one day at a time. The change on each day is intake minus expenditure.

```working
    day 1: 9.1 minus 8.6 = 0.5
    day 2: 8.4 minus 8.7 = -0.3
    day 3: 9.6 minus 8.5 = 1.1
    day 4: 8.0 minus 9.0 = -1.0
    day 5: 9.3 minus 8.4 = 0.9
    day 6: 8.8 minus 8.8 = 0
    day 7: 9.9 minus 8.3 = 1.6
```

Sum the seven daily changes to get the change over the week.

```working
    0.5 plus -0.3 plus 1.1 plus -1.0 plus 0.9 plus 0 plus 1.6 = 2.8
```

Stores rose by 2.8 megajoules over the week. Add that to the starting figure.

```working
    620 plus 2.8 = 622.8
```

Stores stand at 622.8 megajoules at the end of the week.

Now check it the other way, the way an auditor would: sum all seven days' intake, sum all
seven days' expenditure, and subtract the totals once, rather than day by day.

```working
    intake total: 9.1 plus 8.4 plus 9.6 plus 8.0 plus 9.3 plus 8.8 plus 9.9 = 63.1
    expenditure total: 8.6 plus 8.7 plus 8.5 plus 9.0 plus 8.4 plus 8.8 plus 8.3 = 60.3
    63.1 minus 60.3 = 2.8
```

Same 2.8 megajoules. It has to be: the identity holds on any interval, a day or a week, as
long as intake and expenditure are counted over exactly that interval and nothing else
changes the boundary.

Day 6 is worth a second look. Intake and expenditure matched exactly, and stores did not move
that day. That is not a day on which nothing was happening in the body — catabolism and
anabolism were both still running, as `B0-R0-C23`'s must-know points already warn. It is a
day on which the two flows through the stock happened to be equal.

**Where this picture breaks.** The bank-account picture breaks where a bank account does not: a body cannot be read like a
balance printed on a statement. Body energy stores are not measured directly day to day; what
gets measured is body mass, and turning a mass change into an energy change needs a further
fact about what the mass is made of, which this record does not supply.

The week above is invented to show the arithmetic; none of its seven numbers is a real
measurement. A day's own intake and expenditure figures, in a real person, are not read off a
label. Intake is usually self-reported and runs low; expenditure is measured, when it is
measured at all, by doubly labelled water over a stretch of at least several days, not one.
Both of those facts belong to `S01-R1-C03`.

And the identity itself never says whether a particular day's imbalance came from eating more,
moving less, or the body's own expenditure shifting in response to the day before. It fixes
the arithmetic and leaves every question about cause exactly where it found it.

**Must know points for you.**

- Write the day down. "Energy in minus energy out" with no interval attached is not yet a claim you can check. State the day, or the stretch of days, before you accept or quote a figure built from this identity.
- Intake in this identity is metabolisable intake, the figure that survives the losses `B0-R0-C32` names, not the gross energy printed on a label or burned in a bomb calorimeter. Using a gross figure on the left of an "equals" sign that expects a metabolisable one is the commonest way this identity gets misquoted.
- A day where intake and expenditure match exactly is not a day of biological quiet. It is a day where two flows, both still running, happened to be equal. Do not read a flat scale reading as evidence that nothing is happening in the body.
- The identity holds on any interval you choose, provided intake and expenditure are both counted over exactly that interval. A day-to-day mismatch is usually a sign the interval is too short for food still in the gut and water shifts to average out, not a sign the identity has failed.
- This identity fixes the arithmetic and answers no question about cause. It cannot tell you whether a day's imbalance came from what was eaten, what was done, or how expenditure itself moved. `S01-R1-C06` is where that limit is made explicit and turned into a rule for what you may and may not infer from it.

**Exercise 1** (calculation). A patient's energy stores are 540 megajoules on the morning you first see them. Over the next
ten days their average daily intake is 8.9 megajoules and their average daily expenditure is
9.4 megajoules.

Work out their energy stores at the end of the ten days, and say in words what has to be true
of their body mass for that change to show up on a scale.

**1.** On a given day, energy intake is 380 and energy expenditure is 410, in the same units.

Work out the change in energy stores for that day.

**2.** Each row is one day. Two of the three numbers are given each time. Work out the missing one.

```table
| intake | expenditure | change in stores |
| 500 | 470 | |
| 500 | | -20 |
| | 460 | 35 |
| 500 | 500 | |
```

**3.** A reference sedentary or lightly active adult woman has a measured total energy expenditure
of 8.26 megajoules a day (FAO/WHO/UNU 2004).

On one made-up day, a woman matching that reference records a metabolisable intake of 8.80
megajoules. Work out the change in her energy stores for that day, in megajoules, and say
whether her stores rose or fell.

**4.** The same reference woman's total energy expenditure is 8.26 megajoules a day (FAO/WHO/UNU
2004). Over a made-up run of 14 days at that same expenditure, her energy stores fall by 9.8
megajoules in total.

Work out her average daily metabolisable intake over those 14 days.

**5.** Here is a worked answer. Find the step that broke.

```working
    a packet states it holds 1,800 kilojoules, worked out by burning a sample in a bomb calorimeter
    a person eats the whole packet, so 1,800 kilojoules crosses into their energy stores
    their expenditure that day is 9,500 kilojoules
    1,800 minus 9,500 = -7,700
    so their stores fell by 7,700 kilojoules that day
```

**6.** Here is a worked answer. Find the step that broke.

```working
    on Monday, a patient's stores change by -0.4 megajoules
    on Tuesday, their stores change by -0.6 megajoules
    change over the two days = -0.4 minus -0.6 = 0.2
    so their stores rose by 0.2 megajoules over the two days
```

**7.** A fitness app tells a user: "Your weight hasn't moved in three months, so your calories in and
calories out are perfectly matched every single day."

Decide what to compute, compute it, and say what your answer does not establish.

**8.** A colleague in a meeting says this.

> We put her on a diet supplying exactly 8.0 megajoules a day, and her measured expenditure is
> 8.5 megajoules a day. So her stores must be falling by 0.5 megajoules every single day of
> the diet.

The figures are made up for this problem. Decide what to compute, compute it, and say what
your answer does not establish.

