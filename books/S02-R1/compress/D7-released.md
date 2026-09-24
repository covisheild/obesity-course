# D7 · Random error and systematic error as different things

**Definition.** A measurement's error is the value it returns minus the value that is actually true, or, since
the true value is usually unknown, minus a trusted reference value it is checked against. The
International Vocabulary of Metrology (VIM), 3rd edition, 2012, entry 2.16, gives this in its
own words: a measurement error is "measured quantity value minus a reference quantity value".

An error can behave in two different ways when the same thing is measured again and again.

A systematic error is the part of the error that, in the VIM's own words (entry 2.17), "remains
constant or varies in a predictable manner". It pushes every reading the same way, by close to
the same amount, every time.

A measurement bias is, in the VIM's own words (entry 2.18), an "estimate of a systematic
measurement error". In plain words, it is an error that points one way and does not shrink when
you collect more.

A random error is the part that, in the VIM's own words (entry 2.19), "varies in an
unpredictable manner" from one reading to the next.

In plain words, accuracy is how close a measured value comes to the true value.

In plain words, trueness is how close the average of many repeated readings sits to the true
value. That makes trueness about the size of the systematic error alone.

Precision, in the VIM's sense, is how closely repeated readings agree with each other. That
makes it about the size of the random error alone. An instrument can be precise and wrong at the
same time.

Resolution (VIM 4.14) is a different thing again: the "smallest change in a quantity being
measured that causes a perceptible change in the corresponding indication". It says nothing
about whether those digits sit close to the truth.

**In plain terms.** Take any measurement. Its error is what it says minus what is actually true. If a scale says 61.2
kilograms and the true weight is 60.5, the error is 0.7 kilograms. An error can be positive or negative.
Stating it needs you to already know the true value, which in real life usually comes from a trusted
reference instrument, not from guessing.

A systematic error pushes every reading off in the same direction by roughly the same amount. Say a
kitchen scale reads 0.5 kilograms with nothing on the pan, instead of nothing. That is a systematic
error: everything you weigh on it afterward comes out half a kilogram heavy. Take a hundred readings on
this scale and average them. The half-kilogram is still there, because every single reading carried it.

A random error pushes readings around in a way that is not predictable from one reading to the next.
Take a hundred readings from an instrument with only random error, and average them. The average comes
out close to the truth.

Averaging more readings fixes random error. It does nothing at all for systematic error. A very careful,
very repeated measurement on an instrument with a systematic error is not a truer
measurement. It is a more confident wrong one.

A scale that reads 61.4, 61.4, 61.4 and 61.4 kilograms on the same object agrees with itself to the last
digit it shows. If the true weight is 60.0 kilograms, it is also wrong every time. Trueness is how close
the average of many repeated readings sits to the true value. Accuracy needs both: small scatter and no
push off target.

Resolution is the smallest step an instrument's display can move by. A scale reading to the nearest 100
grams has a resolution of 100 grams. It tells you nothing about whether those digits are close to being
true.

**Illustration.** Kiran and colleagues' methods section states a figure worth testing before it is used.

> Weight and height were recorded with accuracy of 100 g and 0.1 cm.

Read that sentence the way the definition above teaches you to. A hundred grams is the step the
weights were written down in. No reading can show a change smaller than that. That is a
statement about resolution: the "smallest change in a quantity being measured that causes a
perceptible change in the corresponding indication" (VIM 4.14). It is not a measured closeness
to a true value. That would need the readings checked against a known reference weight, and
nothing in the paper's methods reports such a check for this scale.

This mix-up is common enough to be worth seeing worked through with numbers on a stated case. No
real scale's repeated calibration readings are held in this book's sources. Say a calibration
weight — a weight already checked and trusted to be correct — is known to be exactly 60.0
kilograms. Each of two stated scales weighs it twenty times.

```table
scale A readings (kg), tight and shifted
60.5  60.5  60.5  60.5  60.5  60.4  60.5  60.5  60.5  60.5
60.5  60.6  60.5  60.5  60.5  60.4  60.5  60.6  60.5  60.5
```

```table
scale B readings (kg), centred and wide
59.7  60.2  60.2  60.4  60.0  59.6  59.4  60.6  58.7  59.7
59.4  60.0  59.7  59.7  60.4  59.7  59.4  60.5  60.5  60.7
```

Scale A's twenty readings barely move: they sit within a tenth of a kilogram of their own
average. That is precision: how closely repeated readings agree with each other. Average them.

```working
    604.9 plus 605.1 = 1210.0
    1210.0 divided by 20 = 60.5
```

Against the known 60.0 kilograms, every reading is 0.4 to 0.6 kilograms high, and the average is
0.5 high.

```working
    60.5 minus 60.0 = 0.5
```

No amount of repeating the weighing removes it, because this part of the error does not vary
from reading to reading. It is systematic.

Scale B's twenty readings scatter far more widely, from 58.7 up to 60.7, including two readings
of exactly 60.0. That is wide, so this scale is much less precise than scale A. Average them
anyway.

```working
    598.5 plus 600.0 = 1198.5
    1198.5 divided by 20 = 59.925
    60.0 minus 59.925 = 0.075
```

Its average sits 0.075 kilograms below the truth.

This scale's error is random: it wobbles both above and below the truth from reading to reading.
The wobbles partly cancel when averaged, and a few more readings would tend to bring the average
closer still.

Scale A looks better reading by reading: tighter, more repeatable, a more confident-looking
number each time. Yet its average sits further from the truth than scale B's average does: half
a kilogram out against seven and a half hundredths. Precision and trueness are not the same
property, and a fine resolution tells you about neither one.

**Where this picture breaks.** In most real measurement, the true value is exactly what you are trying to find out, so you
cannot compute an error this way. Instead, you check an instrument's trueness once, in advance,
against a trusted reference standard, using exactly this arithmetic.

An instrument that reads true at 60 kilograms can drift at 120.

**Figure.** Twenty readings from each scale against a weight known to be 60.0 kilograms, the dashed line. Scale A's readings sit in a tight pile, about half a kilogram too high. Scale B's scatter widely on both sides of the truth, and their average lands close to it. How closely repeated readings agree with each other and how close they sit to the truth are two different things.

*What the figure shows:* A dot plot with readings in kilograms from 58.5 to 61. The upper row, scale A, is a tall narrow stack at 60.5 with a few dots at 60.4 and 60.6, all to the right of a dashed line at 60.0. The lower row, scale B, is spread from 58.7 to 60.7 on both sides of the dashed line, with its average marked just below 60.0.

**Must know points for you.**

- Averaging more readings on a biased instrument does not get you a truer answer.
- Measurement bias is the VIM's own word (entry 2.18) for the same shape of problem as a biased sample. It is an error that points one way and does not shrink when you collect more.
- An instrument's stated "accuracy" is often a number of grams, millimetres or decimal places. It is not a closeness to a known true value. Check which one a paper means.
- Knowing an instrument's precision (VIM 2.15), how closely repeated readings agree with each other, tells you nothing about whether they agree with the truth.
- Part of the difference between observers is each observer's own systematic habit. Mixed across many observers, those habits scatter like random error. A single observer taking every measurement removes that scatter, but not the one observer's own habit. That habit then reaches every reading in the study, and no amount of data from that study alone can reveal it.
- Once a systematic error's size is known, subtract it. Finding the size needs an independent check against a known value, not simply more readings from the same instrument.
- Teach a trainee to ask two separate questions of any instrument. How closely do repeated readings agree with each other? That is precision. How close does the average of many repeated readings sit to the true value? That is trueness. Accuracy needs both together.

**Exercise 1** (critique). mmHg means millimetres of mercury. It is the unit blood pressure is read in. A device maker
says: "Our new blood-pressure monitor is accurate to within 1 mmHg." Here is where that number
comes from. Used again and again on the same person inside one minute, the monitor gives the
same reading each time, to within 1 mmHg.

Say what word this number really describes. Say what question it leaves unanswered.

**Exercise 2** (teaching). A trainee says a colleague's instrument "must be fine because it gives the same number every
time." You have ten minutes and a whiteboard.

Teach them why that is not enough.

**1.** A device is checked against a known true value of 200. On one occasion it reads 194. Work out
the error, and say what its sign tells you.

**2.** A device is checked five times against a known true value of 75. It reads 78, 77, 79, 76 and 80.
Work out the error for each reading.

**3.** Two instruments are each checked five times against a known true value. Their errors are
listed below. For each set, work out the average error and the range of the errors. Say which
set looks more systematic and which looks more random.

```working
    set P: 3, 2, 4, 1, 5
    set Q: -3, 4, -5, 2, -1
```

**4.** A scale is checked against a calibration weight of 20.0 kg. It gives five readings: 20.3, 20.2,
20.4, 20.3 and 20.3 kg. Work out the error for each reading and the average error, with its
unit.

**5.** A thermometer is checked against a reference temperature of 37.0 °C (degrees Celsius). It gives
five readings: 36.4, 37.6, 36.9, 37.3 and 37.0 °C. Work out the error for each reading, the
average error, and the range of the errors. Say whether this instrument looks more like the
scale in the previous problem or not.

**6.** Kiran and colleagues' scale recorded weight in steps of 100 g. Suppose one student's weight is
recorded as 68.3 kg on this scale. A reference scale, checked against a known weight, gives
68.0 kg for the same student. Work out the error. Can knowing how the scale records its
weights tell you whether this error is systematic or random?

**7.** Here is a worked answer. Find the step that broke.

```working
    a thermometer has a zero error: with its probe in melting ice, it reads 0.3 °C instead of 0.0
    twenty readings of a pan of boiling water are taken and averaged, giving 100.3 °C
    averaging twenty readings reduces error, since averaging is how error is reduced
    so 100.3 °C can be treated as an accurate reading
```

**8.** Here is a worked answer. Find the step that broke.

```working
    a scale is checked twenty times against a known 40.0 kg weight
    the readings average to 40.05 kg
    the average is close to the true weight, so the scale is accurate
    each individual reading is therefore also close to the true weight
```

**9.** Here is a worked answer. Find the step that broke.

```working
    a paper states: neck circumference was measured with 1 mm precision
    precision means how closely repeated readings agree with each other
    so the paper has shown its neck-circumference readings agree with each other to within 1 mm
    this supports treating the reported neck-circumference figures as free of measurement error
```

**10.** Here is a worked answer. Find the step that broke.

```working
    a scale has a known zero error: with nothing on it, it reads 0.4 kg
    a reading of 62.1 kg is taken on this scale
    to correct for the zero error, add it back: 62.1 plus 0.4 = 62.5
    so the corrected weight is 62.5 kg
```

**11.** A colleague says: "Our new digital scale must be more accurate than the old one — it shows an
extra decimal place."

Here are five readings from each scale, weighing the same known 50.00 kg calibration weight.

```table
old scale (kg)   50.1   49.9   50.2   49.9   50.0
new scale (kg)   50.63  50.57  50.71  50.55  50.64
```

Decide what to compute, compute it, and say what your answer does not establish.

**12.** A methods section says: "One trained observer took every measurement, so this study has no
measurement error to consider."

Kiran and colleagues also used one observer. They call it a strength: no two people's readings
can then differ.

Now say a second person also measures the necks of the same five people. Each writes down the
size round the neck in cm.

```table
observer 1 (cm)   34.2   35.6   33.8   36.1   34.9
observer 2 (cm)   34.6   36.0   34.3   36.4   35.2
```

Decide what to compute, compute it, and say what the claim does not establish.

