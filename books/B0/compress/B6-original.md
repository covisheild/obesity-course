# B6 · Body-size units: kg, m, cm and kg/m^2

**Definition.** The kilogram, written kg, is the SI base unit of mass. The metre, written m, is the SI base
unit of length. A centimetre, written cm, is one hundredth of a metre, so one metre is 100 cm.

Dividing a mass in kilograms by the square of a length in metres gives a quantity whose unit is
the kilogram per metre squared, written kg/m^2. This is a derived unit: it is built from base
units by division and by raising a base unit to a power.

Because the length in the denominator is squared, the numerical value of the index depends on
the unit chosen for that length, by the square of the conversion factor between the two units.
A length entered in centimetres rather than metres therefore divides the value by 10^4.

The index is a number together with its unit. Nothing in its construction states which values
are high or low. That is a separate decision, made by a body rather than by the arithmetic.


**In plain terms.** Two units first, and you have met the idea behind both.

Mass is measured in kilograms, written kg. Length is measured in metres, written m. A centimetre,
written cm, is one hundredth of a metre. So 100 cm make one metre, and any height in centimetres
becomes metres when you divide by 100.

Now the index. Take a mass in kilograms. Take a height in metres and multiply it by itself, which
is the squaring you met in the section on powers. Divide the first by the second.

The answer is not a bare number. It carries a unit, and the unit comes out of the division:
kilograms on top, metres times metres underneath. You write it kg/m^2 and you say it kilograms
per metre squared.

That is a derived unit. It was not handed down. It was built out of two base units by dividing
one by the other and squaring one of them on the way.

Two warnings come with it, and the first is the expensive one.

The height must be in metres. Put centimetres in and the answer is not slightly off. It is ten
thousand times too small, because the squaring squares the mistake as well.

And the number this gives you does not mean anything on its own. It is an amount with a unit,
like a price or a distance. Where the line falls between one value and another is a decision
somebody made, and this section does not make it.


**Illustration.** Work the wrong one first. You will meet it in a spreadsheet long before you meet it in a book.

A person weighs 70 kg and stands 168 cm tall. The height is in centimetres, which is how a
clinic form usually collects it. Square it as it stands and divide.

```working
    168 times 168 = 28,224
```

Now divide the 70 by that. The answer is 0.00248, and the unit that falls out of the division is
kilograms per centimetre squared, not kilograms per metre squared.

Now do it properly. Put the height into metres first.

```working
    168 divided by 100 = 1.68
    1.68 times 1.68 = 2.8224
    70 divided by 2.8224 = 24.8
```

24.8 kg/m^2. Say it out loud as kilograms per metre squared, because the unit is what tells you
the first answer was not an answer at all.

Put the two denominators side by side and the size of the error stops being a surprise.

```working
    28,224 divided by 2.8224 = 10,000
    24.8 divided by 10,000 = 0.00248
```

One hundred centimetres in a metre, and the denominator is squared, so the mistake is squared
too.

```working
    100 times 100 = 10,000
```

An error of ten thousand times is so large that it does not look like an arithmetic slip. It
looks like a different quantity altogether, which is exactly why it survives a read-through.

Now the second thing the square does, and it is not a mistake this time. Take a shape and make
every length twice as long, keeping everything else the same. Mass goes with volume, and volume
has three lengths in it, so the mass goes up by 2 times 2 times 2.

```working
    2 times 2 times 2 = 8
```

The denominator has only two lengths in it.

```working
    2 times 2 = 4
```

So the index itself goes up.

```working
    8 divided by 4 = 2
```

Twice the index, from the same shape at a different size. Dividing by the square of a height
does not remove size from the number. It removes some of it, and a squared denominator is a
choice somebody made rather than a law you can check.

One line of grounding for the units themselves. The metre and the kilogram are two of the seven
base units, which keep their role inside the SI. A unit like this one is built out of them.


**Where this picture breaks.** The doubling argument holds only while the shape and the density stay the same. Real bodies are
not scaled copies of each other. The factor of 2 is what the geometry alone gives you, and not
a prediction about any person.

The ten-thousand check holds only for centimetres against metres. A height in inches, or a mass
in pounds, carries a different factor. Work that one out the same way rather than reusing this
one.

And the arithmetic here is exact while the two numbers going in are not. A weight taken with
shoes on, or a height measured without a wall, moves the answer more than any rounding in the
sum does.


**Must know points for you.**

- A height in centimetres does not give a slightly wrong index. It gives one ten thousand times too small, because the denominator squares the error. If a value lands in the thousandths, stop and look at the height column rather than at the person.
- Convert the height to metres before anything else, by dividing by 100. Do it as a separate written line, not inside the same keystroke as the division, so you can see it was done.
- Say the unit with the number: 24.8 kilograms per metre squared. The unit is what catches the centimetre error, and a figure quoted without it cannot be checked by anybody who hears it.
- In a dataset, find out which unit height was collected in before you compute a single row. A column holding some heights in metres and some in centimetres gives two groups of values ten thousand apart. An average taken across both is a number about nothing.
- Dividing by the square of a height does not take size out of the number. Scale a shape up and the index rises with it. So the index is not a shape measurement that happens to be written in kilograms per metre squared.
- The arithmetic stops at the number and its unit. What counts as a high value is not in it. Somebody decided that, and decisions like that get revised. Quote a cut-off only with whose it is and when it was set.

**Exercise 1** (calculation). A person weighs 64 kg and is 155 cm tall. Work out the index, showing the height conversion as
its own line, and state the unit. Then write one sentence saying what your answer does not tell
you.


**Exercise 2** (teaching). A first-year resident has ten minutes and a whiteboard. They ask why the height is squared and
why it matters that the answer is in kilograms per metre squared. Explain it so they could
reconstruct it afterwards, and give them one error to watch for.


**1.** Work each of these out. Square the second number, then divide the first by it.

```working
    72 and 1.8
    81 and 1.5
    45 and 1.5
```


**2.** Turn each of these lengths into metres.

```working
    168 cm      155 cm      180 cm      96 cm
```


**3.** A quantity is divided by the square of a length. Somebody supplies the length in centimetres
when metres were wanted. By what factor is the answer wrong, and in which direction? Show the
step that produces the factor.


**4.** A person weighs 58 kg and is 1.52 m tall. Work out the index and give it with its unit, showing
every line.


**5.** A record gives an index of 27.0 kg/m^2 and a height of 1.60 m, but the mass is missing. Work out
the mass in kilograms, showing every line.


**6.** Here is a worked answer. Find the step that broke.

```working
    a person weighs 65 kg and is 170 cm tall
    170 divided by 100 = 1.7
    65 divided by 1.7 = 38.2
    so the index is 38.2 kg/m^2
```


**7.** Here is a worked answer. Find the step that broke.

```working
    a person weighs 62 kg and is 158 cm tall
    158 times 158 = 24,964
    62 divided by 24,964 = 0.00248
    that is far too small, so multiply by 100
    the index is 0.248 kg/m^2
```


**8.** A colleague sends you this line about a survey.

> Our height column turned out to be in centimetres, and the index column looks wrong because
> of it. It is only a scaling problem, so we can multiply the whole column by 100 and move on.

Decide what to compute, compute it, and say what your answer does not establish.

