# D7 · Random error and systematic error as different things

**Definition.** Some error has nothing to do with how a sample was drawn. A faulty instrument is one source:
the statistics textbook this book follows calls this a nonsampling error. This section is about
that kind, on a single instrument measuring one thing.

A measurement's error is the value it returns minus the value that is actually true, or, since
the true value is usually unknown, minus a trusted reference value it is checked against. The
International Vocabulary of Metrology (VIM), 3rd edition, 2012, entry 2.16, gives this in
its own words: a measurement error is "measured quantity value minus a reference quantity
value".

An error can behave in two different ways when the same thing is measured again and again.

A systematic error is the part of the error that, in the VIM's own words (entry 2.17),
"remains constant or varies in a predictable manner". It pushes every reading the same way, by
close to the same amount, every time. Averaging repeated readings does not remove it, because
every reading it touches is wrong in the same direction.

A measurement bias is, in the VIM's own words (entry 2.18), an "estimate of a systematic
measurement error". In plain words, it is an error that points one way and does not shrink when
you collect more. The section before this one met sampling bias: a sample in which some members
were more likely to be chosen than others. Measurement bias is the same word for the same shape
of problem.

A random error is the part that, in the VIM's own words (entry 2.19), "varies in an
unpredictable manner" from one reading to the next. It pushes readings both above and below the
true value, so it partly cancels when readings are averaged, in the same way a sample average
settles down as the sample grows.

Three further words describe how good a set of measurements is, and the VIM keeps them apart on
purpose. Its definitions of them use one more term of its own, the measurand: the quantity
being measured.

Measurement accuracy (VIM 2.13) is "closeness of agreement between a measured quantity value and
a true quantity value of a measurand". In plain words, accuracy is how close a measured value
comes to the true value.

Measurement trueness (VIM 2.14) is "closeness of agreement between the average of an infinite
number of replicate measured quantity values and a reference quantity value". In plain words,
trueness is how close the average of many repeated readings sits to the true value. That makes
trueness about the size of the systematic error alone.

A set of readings is called true on average when this closeness is good, which the VIM keeps
apart from calling it accurate.

The section on significant figures already used the word precision, for how many digits a
figure can defend. This book's glossary calls precision, more loosely, how tightly a
measurement pins the number down. Measurement precision (VIM 2.15) narrows that further:
"closeness of agreement between indications or measured quantity values obtained by replicate
measurements on the same or similar objects under specified conditions". Precision, in the
VIM's sense, is how closely repeated readings agree with each other. That makes it about the
size of the random error alone. It says nothing about whether the readings are close to the
truth. An instrument can be precise and wrong at the same time.

Resolution (VIM 4.14) is a different thing again: the "smallest change in a quantity being
measured that causes a perceptible change in the corresponding indication". For a digital
display, that is in practice the step of its last digit. A fine resolution says how many digits
an instrument can print. It says nothing about whether those digits sit close to the truth.

**In plain terms.** The section before this one was about a sample's answer bouncing around from one draw to the
next. This section is about a different kind of wobble: the one a single instrument shows when it
measures the same thing more than once.

Take any measurement. Its error is what it says minus what is actually true. If a scale says
61.2 kilograms and the true weight is 60.5, the error is 0.7 kilograms. An error can be positive
or negative. Stating it needs you to already know the true value, which in real life usually
comes from a trusted reference instrument, not from guessing.

Measure the same thing over and over on the same instrument. The errors you get behave in one of
two ways, or some mixture of both.

A systematic error pushes every reading off in the same direction by roughly the same amount.
Say a kitchen scale reads 0.5 kilograms with nothing on the pan, instead of nothing. That is a
systematic error: everything you weigh on it afterward comes out half a kilogram heavy. This
particular case, an instrument reading something other than zero when it should read zero, has
its own name: a zero error (VIM 4.28). Take a hundred readings on this scale and average them.
The half-kilogram is still there, because every single reading carried it.

Once a systematic error's size is known, though, it can be taken back out: subtract it from
every reading. The VIM calls this a correction (2.53). Finding the size of the error needs an
independent check against a known value. More readings from the same scale cannot supply it.

A random error pushes readings around in a way that is not predictable from one reading to the
next. Sometimes it is a little high, sometimes a little low, for reasons too small and too
tangled to track down. Take a hundred readings from an instrument with only random error, and
average them.
The average comes out close to the truth. The reason is the same one behind a sample's average
settling down as the sample grows: the too-high readings and the too-low readings partly cancel.

This is the one fact worth carrying out of the whole section. Averaging more readings fixes random
error. It does nothing at all for systematic error. Calibration is measuring a machine against
something already known, so its readings mean something. A very careful, very repeated
measurement on a badly calibrated instrument is not a truer measurement. It is a more confident
wrong one.

That is the same mistake the section before this one made about a biased sample. Sampling bias
and measurement bias are the same word for the same shape of problem. Each is an error that
points one way and does not shrink when you collect more. No amount of repeating the same flawed process
will fix that.

Two more words are easy to mix up, and papers sometimes mix them up, as the VIM itself notes
(2.15). The section on significant figures already used precision for how many digits a figure
can defend. This book's glossary calls precision, more loosely, how tightly a measurement pins the
number down. The exact sense meant here is narrower still: how closely repeated readings agree
with each other. It says nothing about whether they agree with the truth.

A scale that reads 61.4, 61.4, 61.4 and 61.4 kilograms on the same object agrees with itself to
the last digit it shows. If the true weight is 60.0 kilograms, it is also wrong every time.
Trueness is how close the average of many repeated readings sits to the true value. Accuracy needs
both: small scatter and no push off target. An instrument can be precise without being true on
average, or true on average without being especially precise.

A third word gets mistaken for both of these. Resolution is the smallest step an instrument's
display can move by. A scale reading to the nearest 100 grams has a resolution of 100 grams.
That tells you how many digits it can show you. It tells you nothing about whether those digits
are close to being true.

**Illustration.** Kiran and colleagues' methods section states a figure worth testing before it is used.

> Weight and height were recorded with accuracy of 100 g and 0.1 cm.

Read that sentence the way the definition above teaches you to. A hundred grams is the step the
weights were written down in. No reading can show a change smaller than that. That is a
statement about resolution: the "smallest change in a quantity being measured that causes a
perceptible change in the corresponding indication" (VIM 4.14). It is not a measured closeness
to a true value. That would need the readings checked against a known reference weight, and
nothing in the paper's methods reports such a check for this scale.

Was the scale also true on average, against a correctly calibrated reference? That is a separate
question. The paper's own wording does not answer it, however natural it is to read "accuracy"
and believe it has been.

This mix-up is common enough to be worth seeing worked through with numbers on a stated case.
No real scale's repeated calibration readings are held in this book's sources. Say a
calibration weight — a weight already checked and trusted to be correct — is known to be
exactly 60.0 kilograms. Two stated scales are each weighed against it twenty times.

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

Sixty and a half kilograms, and no single reading is more than a tenth of a kilogram from it.
Against the known 60.0 kilograms, every reading is 0.4 to 0.6 kilograms high, and the average
is 0.5 high.

```working
    60.5 minus 60.0 = 0.5
```

Say the cause is a zero error, so that with nothing on it the scale already reads 0.5
kilograms. These twenty readings, all at one weight, could not show that by themselves. A zero
error and an error that grows with load would look the same at a single weight. Either way,
the half-kilogram gets added to every reading here. No amount of repeating the weighing removes
it, because this part of the error does not vary from reading to reading. It is systematic.

Scale B's twenty readings scatter far more widely, from 58.7 up to 60.7, including two readings
of exactly 60.0. That is wide, so this scale is much less precise than scale A. Average them
anyway.

```working
    598.5 plus 600.0 = 1198.5
    1198.5 divided by 20 = 59.925
```

Fifty-nine point nine two five kilograms, within a tenth of a kilogram of the true 60.0, even
though most single readings landed further away. This scale's error is random: it wobbles both
above and below the truth from reading to reading. The wobbles partly cancel when averaged, and
a few more readings would tend to bring the average closer still.

Set the two scales side by side and the trap in the paper's sentence is easy to see. Scale A
looks better reading by reading: tighter, more repeatable, a more confident-looking number
each time. Yet its average sits further from the truth than scale B's average does: half a
kilogram out against seven and a half hundredths. Scale B's own worst reading, 58.7 kilograms,
sits 1.3 kilograms from the truth, further off than any single reading scale A ever gives.
Precision and trueness are not the same property, and a fine resolution tells you about
neither one.

One more real detail from the same paper closes the section. Its authors name the study's
strength this way: "was single observer measurements with minimum inter-observer variation."

That is a genuine strength. Differences between observers are each observer's own systematic
habit: one measures a fraction of a centimetre long, another rounds down, and so on. Mixed
across many observers, those habits scatter like random error. One observer taking every
measurement removes that scatter. It buys nothing against that one observer's own habit. Say
this person's technique ran a fraction of a centimetre long on every neck measurement. Then
every reading in the study carries it, and nothing in a single-observer dataset can show that
it happened.

**Where this picture breaks.** The two stated scales were built to show one shape each, on purpose. One has almost no random
error. One has almost no systematic error. A real instrument usually carries some of both at
once, and untangling the mixture from twenty readings alone is harder than either clean case
here.

Both scales were checked against a stated true weight known in advance. That is what let their
errors be computed directly. In most real measurement, the true value is exactly what you are
trying to find out, so you cannot compute an error this way. Instead, you check an instrument's
trueness once, in advance, against a trusted reference standard, using exactly this arithmetic.
Then you trust that check for the ordinary readings that follow.

Neither scale's error was shown to be the same at every weight it might read. An instrument
that reads true at 60 kilograms can drift at 120. Twenty readings taken at one weight say
nothing about its behaviour at another.

**Figure.** Twenty readings from each scale against a weight known to be 60.0 kilograms, the dashed line. Scale A's readings sit in a tight pile, about half a kilogram too high. Scale B's scatter widely on both sides of the truth, and their average lands close to it. How closely repeated readings agree with each other and how close they sit to the truth are two different things.

*What the figure shows:* A dot plot with readings in kilograms from 58.5 to 61. The upper row, scale A, is a tall narrow stack at 60.5 with a few dots at 60.4 and 60.6, all to the right of a dashed line at 60.0. The lower row, scale B, is spread from 58.7 to 60.7 on both sides of the dashed line, with its average marked just below 60.0.

**Must know points for you.**

- Averaging more readings on a biased instrument does not get you a truer answer. It gets you a more confident wrong one, because every reading it averages carries the same systematic error.
- The section before this one taught sampling bias: a sample in which some members were more likely to be chosen than others. Measurement bias is the VIM's own word (entry 2.18) for the same shape of problem. It is an error that points one way and does not shrink when you collect more. Repeating the same flawed process cannot fix it. Recognise the shape once and you recognise it in both places.
- An instrument's stated "accuracy" is often a number of grams, millimetres or decimal places. Often that is really its resolution (VIM 4.14): the "smallest change in a quantity being measured that causes a perceptible change in the corresponding indication". It is not a closeness to a known true value. Check which one a paper means.
- Knowing an instrument's precision (VIM 2.15), how closely repeated readings agree with each other, tells you nothing about whether they agree with the truth. That needs a separate comparison against a known correct value, which repetition on the instrument alone cannot supply.
- Differences between observers are each observer's own systematic habit. Mixed across many observers, those habits scatter like random error. A single observer taking every measurement removes that scatter, but not the one observer's own habit. That habit then reaches every reading in the study, and no amount of data from that study alone can reveal it.
- Once a systematic error's size is known, subtract it. The VIM calls this a correction (2.53). Finding the size needs an independent check against a known value, not simply more readings from the same instrument.
- Teach a trainee to ask two separate questions of any instrument. How closely do repeated readings agree with each other? That is precision. How close does the average of many repeated readings sit to the true value? That is trueness. Accuracy needs both together. A trainee who checks only the first question will trust a precise, biased instrument completely.

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

