# B6 · Body-size units: kg, m, cm and kg/m^2

**Definition.** A centimetre, written cm, is one hundredth of a metre, so one metre is 100 cm.

Dividing a mass in kilograms by the square of a length in metres gives a quantity whose unit is
the kilogram per metre squared, written kg/m^2.

A person's mass in kilograms divided by the square of their height in metres is the body mass
index, written BMI.

A height entered in centimetres rather than metres therefore divides the index by 10^4.

The index is a number together with its unit. Nothing in its construction states which values
are high or low. That is a separate decision, made by a body rather than by the arithmetic.

**In plain terms.** Mass is measured in kilograms, written kg. Length is measured in metres, written m. So 100 cm make one metre, and any height in centimetres
becomes metres when you divide by 100.

Take a mass in kilograms. Take a height in metres and multiply it by itself, which
is the squaring you met in the section on powers. Divide the first by the second.

What you get is called the body mass index, written BMI. It puts a mass and a height together
into one number, and the short name for it here is the index.

It carries a unit, and the unit comes out of the division:
kilograms on top, metres times metres underneath.

That is a derived unit.

The height must be in metres. Put centimetres in and the answer is not slightly off. It is ten
thousand times too small, because the squaring squares the mistake as well.

And the index does not mean anything on its own. Whether a value counts as high or low is a decision
somebody made, and this section does not make it.

**Illustration.** Do the calculation the wrong way first, because the mistake is the thing worth seeing.

A person weighs 70 kg and stands 168 cm tall. The height is in centimetres, which is how a
clinic form usually collects it. Square it as it stands, then divide the 70 by what you get.

```working
    168 times 168 = 28,224
    70 divided by 28,224 = 0.00248 kg/cm^2
```

Read the unit that fell out of that division. It is kilograms per centimetre squared, not
kilograms per metre squared.

Now do it properly. Put the height into metres first.

```working
    168 divided by 100 = 1.68
    1.68 times 1.68 = 2.8224
    70 divided by 2.8224 = 24.8
```

24.8 kg/m^2. Say it out loud as kilograms per metre squared, because the unit is what tells you
the first answer was not an answer at all.

One hundred centimetres in a metre, and the denominator is squared, so the mistake is squared
too.

```working
    100 times 100 = 10,000
```

Take a shape and make
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

Dividing by the square of a height
does not remove size from the number. It removes some of it, and a squared denominator is a
choice somebody made rather than a law you can check.

**Where this picture breaks.** The doubling argument holds only while the shape and the density stay the same. Real bodies are
not scaled copies of each other.

The ten-thousand check holds only for centimetres against metres.

**Must know points for you.**

- A height in centimetres does not give a slightly wrong index. It gives one ten thousand times too small, because the denominator squares the error.
- Convert the height to metres before anything else, by dividing by 100.
- Say the unit with the number: 24.8 kilograms per metre squared.
- In a dataset, find out which unit height was collected in before you compute a single row.
- Dividing by the square of a height does not take size out of the number. Scale a shape up and the index rises with it.
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

**5.** Two rows come out of a clinic register. The first records a mass of 61.5 kg and a height of
158 cm. The second records a mass of 73.4 kg and a height of 1.72 m.

Work out the index for each row, showing every line, and give each answer with its unit. Then
say which row needed a conversion first, and how the row itself told you.

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

