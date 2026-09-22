# B3 · Dimensional analysis as an error check

**Definition.** Every measured quantity has a dimension, which is the kind of thing it is: a length, a mass, a
time, or a combination of these built by multiplication and division. The unit is how that
dimension is measured. Two quantities of the same dimension may be measured in different units.

An equation between physical quantities must carry the same dimension on both sides, and two
quantities may be added or subtracted only when they have the same dimension.

Multiplying quantities multiplies their units, and dividing them divides their units.

Matching dimensions on both sides cannot confirm a formula, because a wrong dimensionless
factor changes no unit.

**In plain terms.** You can often show that a formula is wrong without knowing the right formula. You do it by
looking at the units and ignoring the numbers.

Both sides of an equals sign have to carry the same kind of quantity. The word for the kind of
thing a quantity is, is its dimension.

You can only add or subtract quantities of the same dimension, and then only once both are
written in the same unit. Three metres plus four seconds is not seven of anything, because a
length and a time are different kinds of thing.

Multiplying and dividing behave the way they do with plain numbers. Metres times metres give the
unit m^2. You can cancel them the way you cancel a shared number in a ratio.

So here is the check, in four steps.

1. Throw the numbers away and keep the units.
2. Write the unit of every quantity on both sides.
3. Cancel anything that appears on the top and on the bottom.
4. Compare the two sides. Different units mean the formula is wrong.

Matching units do not make a formula right. Halving a quantity, doubling it, or multiplying it
by 3.14 leaves every unit exactly where it was.

**Illustration.** > The stretch is 12 km and the bus averages 40 kilometres an hour, so allow 480 minutes.

Take the numbers out and watch what the units do.

```working
    km times km per hour
    = km^2 per hour
```

A square kilometre per hour is an area divided by a time. It is not a time at all.

You want hours to be left standing at the end.

```working
    km divided by km per hour
    = km times hour over km
    = hours
```

Dividing does it. The kilometres cancel and the hours are left.

Put the numbers back.

```working
    12 divided by 40 = 0.3
```

That is 0.3 hours. Turn it into minutes with a conversion factor, as you did in the section
before this one.

```working
    0.3 h times 60 min over 1 h
    = 18 min
```

Eighteen minutes, not 480.

Section 3(1) of the National Food Security Act, 2013 entitles a person in a priority household
to five kilograms of foodgrains per person per month. Somebody proposes a way of working out a
household's grain for a year.

> yearly grain = 5, divided by the number of people, times 12

Strip the numbers out again and write only the units.

```working
    kilograms per person per month
    divided by persons
    times months
    = kilograms per person squared
```

The months cancelled, which is right. You are left with kilograms per person squared, and
there is no such quantity.

Ask what arrangement would leave kilograms standing instead.

```working
    kilograms per person per month
    times persons
    times months
    = kilograms
```

So you multiply by the number of people. You do not divide by it. Now put the numbers in, for a
household of four.

```working
    5 times 4 times 12 = 240
```

240 kilograms per household per year. The 240 is your arithmetic on it, and it is not a figure
the Act carries.

A unit check throws out wrong arrangements. It never hands you a right formula.

**Where this picture breaks.** This check catches a formula of the wrong shape. It cannot catch a formula of the right shape
and the wrong size.

Halving a quantity leaves every unit where it was. A formula can pass this check and still give
you an answer twice the truth.

It also says nothing about the quantities themselves. Kilograms of grain and kilograms of
anything else carry the same unit.

And the persons in the working above are not an SI unit.

**Must know points for you.**

- Run the check in four steps when a formula you did not write lands in front of you.
- Matching units never make a formula right.
- The same letters are not the same units. Read the powers before you agree that two units match.
- You can reject a formula in a paper, a protocol or a spreadsheet without being able to derive the right one.
- Read the unit that falls out of any calculated dose before you act on it.
- This check finds an error in the shape of a formula and never an error in a plain number multiplying it.
- Teach a trainee who cannot remember a formula to check the units of the one in front of them.

**Exercise 1** (critique). A colleague has checked somebody's formula and reports back in one line.

> The units come out right on both sides, so the formula is correct.

Say why that does not follow. Then give an example of a formula that passes a unit check and is
still wrong.

**Exercise 2** (teaching). A first-year resident says they can never remember formulas, and treats that as the end of the
matter. You have ten minutes and a whiteboard.

Teach them the unit check so that they leave able to use it on the next formula they meet.

**1.** Simplify each of these unit expressions.

```working
    m/s times s
    m times m times m
    kg divided by m^3, times m^3
```

**2.** Which of these pairs can be added together as they stand, which can be added after a
conversion, and which cannot be added at all?

```working
    3 m and 4 m
    3 m and 4 s
    3 kg and 4 g
    3 m^2 and 4 m
```

**3.** Work out the unit of each of these quantities from what it is built out of. Use metres,
kilograms and seconds.

```working
    a mass divided by a volume
    a length divided by a time
    a length divided by a time, and then divided by a time again
    a number of people divided by an area
```

**4.** Cancel each of these down as far as it will go.

```working
    kg m^2 s^-2 divided by kg
    kg m^2 s^-2 divided by s
    m^2 divided by m
```

**5.** The SI states that J = kg m^2 s^-2, where J is the joule. Write out the unit of each of these
in base units, cancelled as far as it will go.

```working
    J divided by kg
    J times s^2, divided by m^2
    J divided by s
```

**6.** A protocol works out a total amount of a drug like this.

> total amount = strength times volume

The strength is recorded in milligrams per millilitre. The volume is recorded in millilitres.

Check the units of the right-hand side and say what unit the total amount comes out in.

**7.** A district note plans grain for a priority household of six people. It says the household
should be counted for 360 kilograms of foodgrains in a year.

Work back to the rate for one person for one month, keeping the unit on the answer. Say which
units you cancelled to get there. Then say whether the rate you land on is the one section 3(1)
of the National Food Security Act, 2013 states.

**8.** A bus covers 18 kilometres in 30 minutes. A note says the speed is worked out as the time
divided by the distance.

Say what unit that gives and what it is not. Then write the arrangement whose units come out as
a speed, and work the speed out.

**9.** A block of material has a mass of 2,400 kilograms and a volume of 1.2 cubic metres. A note
works out its density as the volume divided by the mass.

A density is a mass in every unit of volume. Check the note's units against that, fix the
arrangement, and work the density out.

**10.** Here is a worked answer. Find the step that broke.

```working
    a rectangular plot measures 30 m by 20 m
    the fencing needed is 30 times 20 = 600
    so 600 m of fencing is needed
```

**11.** Here is a worked answer. Find the step that broke.

```working
    the entitlement is 5 kilograms per person per month
    a year is 365 days
    5 times 365 = 1,825
    so the entitlement is 1,825 kilograms per person per year
```

**12.** Here is a worked answer. Find the step that broke.

```working
    energy in the SI has the unit kg m^2 s^-2
    a note proposes that energy is a mass times a speed
    a mass is in kg and a speed is in m/s
    kg times m/s gives kg m/s
    kg m/s contains kg, m and s, and so does kg m^2 s^-2
    so the units match and the formula is fine
```

**13.** A press note crosses your desk with this line in it.

> The plant treats 4.5 crore litres a day, which works out at 135 litres a person for the
> city's 30 lakh people.

The plant, the city and both figures are made up for this problem. No real plant and no real
population is being described.

Decide what to compute, compute it, and say what your answer does not establish.

**14.** A supplier's brochure makes this claim about a water treatment unit for a village tank.

> It doses at 2 milligrams per litre. So a 5,000 litre tank needs 2 divided by 5,000, which
> is 0.0004 grams of chlorine a fill.

The brochure, the unit and both figures are made up for this problem. Do not carry the
2 milligrams per litre away as a chlorine dose. What a tank should be dosed at is set by
whoever sets the standard. This problem is about the arrangement of the units and nothing else.

Decide what to compute, compute it, and say what your answer does not establish.

