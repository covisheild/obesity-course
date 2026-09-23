# S01-R1-C07 · Sizing an imbalance, and the static rule

**Definition.** A kilogram of body fat is proposed to hold a fixed number of kilocalories, so that a
surplus or a deficit of energy intake, summed over time, converts into a change in fat
mass at that fixed rate. Every other quantity is held constant for the interval this is
applied to: the day's intake, the day's expenditure, and the energy content of a
kilogram of fat itself. This is the static rule.

Its common English form states the rate as 3,500 kilocalories removed or added for each
pound of body weight changed, a figure this subject's held sources trace to Wishnofsky
(1958) and describe as "derived by estimation of the energy content of weight lost".
Converting the pound to the unit this course uses, with the exact factor 1 pound equals
0.453 592 37 kilogram, gives the same rate per kilogram.

```working
    3500 divided by 0.45359237 = 7716.18
```

About 7,716 kilocalories per kilogram. This figure is arithmetic on the rule's own
number, converted from one unit to another; it is not a measurement of what a kilogram
of body fat, or of adipose tissue, actually holds. That measurement is a separate
question, taken up in this subject's C02.

Given a daily surplus or deficit of D kilocalories, held at the same size for n days, the
static rule predicts a change in fat mass of D times n, divided by 7,716, in kilograms.
Because D is held fixed, the predicted change is a straight line against time: the same
daily D always predicts the same rate of change, on day one and on day one thousand.

The rule fails for two separate reasons, and only the second is this concept's subject.
First, real tissue lost is not pure fat, so a single fixed kilocalories-per-kilogram
figure cannot hold for every kilogram lost; that is C02's territory. Second, and the
reason a straight line is the wrong shape, intake and expenditure are not constant
through a period of weight loss: both respond to the loss itself. A technique that holds
D fixed cannot represent a quantity that changes, so the straight line is the shape of
"nothing responds", not a shape anybody has measured. The next rung teaches what
actually happens when D is not held fixed.

**In plain terms.** Say a kilogram of fat is worth a fixed number of kilocalories. Eat that many fewer than
you burn, and a kilogram should come off. Eat that many more, and a kilogram should go on.
That is the whole idea, and the number everybody has heard is 3,500 kilocalories for a
pound.

A pound is not the unit this course uses, so turn it into kilograms first. One pound is
exactly 0.453 592 37 kilogram. Divide the 3,500 by that.

```working
    3500 divided by 0.45359237 = 7716.18
```

About 7,716 kilocalories for a kilogram. Keep hold of where that number came from: it is
the old rule, converted into a new unit. It is not a fact anybody measured about fat.

Now run the rule forward. Pick a daily surplus or deficit, and hold it the same size every
day. Multiply it by the number of days, and divide by 7,716.

```working
    change in kilograms = (daily amount times days) divided by 7716
```

Plot that against time and you get a straight line, because the daily amount never
changes in the sum. A straight line drawn from a rule like this is a warning sign rather
than a prediction, and the reason is in the words "held constant". Nobody's daily intake
and daily expenditure sit still while they lose weight. A smaller body spends less. A
body under a sustained deficit does not respond the way it did on day one. The straight
line is the picture you get from assuming none of that happens, and that assumption is
the trap.

**Illustration.** Take the scenario the *Lancet* paper by Hall and colleagues uses to make this point.
A sedentary man weighing 100 kilograms cuts his energy intake by 2 megajoules a day and
keeps it cut. Using the calorie the source itself says food energy is measured in, the
thermochemical kilocalorie at 4.184 kilojoules, turn the daily cut into kilocalories.

```working
    2 divided by 0.004184 = 478.01
```

About 478 kilocalories a day. Run the static rule forward for one year.

```working
    478.01 times 365 = 174473.65
    174473.65 divided by 7716.18 = 22.61
```

About 22.6 kilograms in the first year. The paper reports the same rule's own prediction
for this scenario as "22 kg lost in the first year" — close to what the arithmetic here
gives, the small gap being rounding in the megajoule-to-kilocalorie step and in the
paper's own figures.

Now the failure. The paper's own dynamic model, built from the first law of
thermodynamics rather than from a fixed rate, predicts something different for the same
100-kilogram man on the same cut: a bodyweight plateau at about 75 kilograms, reached
over about three years, "taking roughly 1 year to reach half of the maximum weight loss".
Put the two predictions for year one side by side.

```table
model                weight change after one year
the static rule       about 22.6 kg
the dynamic model      about half of 25 kg, so roughly 12 to 13 kg
```

The static rule is not merely optimistic here. It has the wrong shape. It says every
year should look like the first, for as long as the deficit is kept up. The dynamic
model says the loss slows and levels off, because the man's expenditure falls as his
body gets smaller, which shrinks the deficit that is actually driving further loss even
though intake has not changed again.

A second real case, in the other direction, sizes what "several days" of fat means.
Thomas and colleagues pooled 103 adults on supervised diets averaging a 1,439 kcal per
day deficit. Work out what the static rule predicts they should lose over their average
64.8 days on the diet.

```working
    1439 times 64.8 = 93247.2
    93247.2 divided by 3500 = 26.64
```

About 26.6 pounds predicted, close to the 27.6 pounds the rule in fact predicted for
this cohort in the paper. What they actually lost, measured, was 20.1 pounds: "7.4±12.6
lb less than the 27.6±16.0 lbs predicted by the 3500 kcal rule." A kilogram of fat is
several days of a person's whole daily expenditure, which is why even a supervised,
fully controlled deficit takes over two months to move 20 pounds. It is not several
hours, and it is not, on the rule's own numbers here, quite as many days as the static
line predicts either.

**Where this picture breaks.** The 7,716 kilocalories per kilogram figure is arithmetic on the rule's stated rate, not a
measured property of fat or of adipose tissue; do not carry it into a claim about what a
kilogram of body fat actually contains. The straight-line projection is reliable only
over an interval short enough that intake and expenditure have not yet responded to the
loss, and both sources here agree that response starts working against the deficit
within the first year, not after several years. Beyond that interval the rule
overstates the loss, and by how much grows with time, not by a fixed margin.

**Must know points for you.**

- Convert the unit before you argue about the number. "3,500 kcal a pound" and "7,716 kcal a kilogram" are the same rule; a mismatch between the unit you compute in and the unit you were given is a silent source of a two-fold error, since a pound is not half a kilogram, it is under half.
- A rule that holds a daily amount fixed and multiplies it by time always draws a straight line, whatever the real quantity does. Seeing a straight-line prediction is itself information: it tells you the model held something constant, and the question to ask next is whether that thing actually stays constant.
- The straight line from the static rule is not wrong on day one. It is wrong about how long day one's numbers keep applying, because it never says when to stop trusting itself.
- When you tell a patient a target using this rule, say over what interval it holds. "Roughly a kilogram every two weeks, for the first few months" is a claim you can defend. "A kilogram every two weeks, indefinitely" is not, on the same evidence.
- A kilogram of fat is several days of a person's total daily expenditure, not a few hours of it. This is why even a large, fully supervised deficit takes months to move a double-digit number of kilograms, and why a claimed weekly loss should be checked against how many days of expenditure it would actually cost.
- A figure like 3,500 kcal per pound being widely printed, including in textbooks, does not make it a measured property of fat. It is a rate proposed for one purpose, arithmetic, not a finding about physiology; teach the two as separate claims.

**Exercise 1** (calculation). A person keeps to a deficit of 600 kcal a day for 40 days. Using the static rule,
work out the predicted loss in kilograms.

**Exercise 2** (teaching). A health secretary has one page and wants an answer first. They have asked: "Is the
3,500-calorie rule good enough to put in a public information leaflet?"

**1.** A rule states that 3,500 removes one unit of weight for every 0.45359237 of a
different unit that measures the same thing. Work out the rate per whole unit of the
second measure.

**2.** Using a rate of 3,500 for one unit, work out the total for 5 units, and separately for
12 units.

**3.** Thomas and colleagues' pooled dieters were prescribed a target intake giving them an
average deficit of 1,439 kcal a day, over an average of 64.8 days on the diet. Using
the static rule's rate of 3,500 kcal a pound, work out the predicted loss in pounds,
then convert it to kilograms using the exact factor 1 pound equals 0.45359237 kg.

**4.** Hall and colleagues model a 100 kg sedentary man cutting his intake by 2 megajoules a
day and holding that cut for a year. Using the thermochemical kilocalorie, 1 kcal
equals 0.004184 megajoules, convert the daily cut to kilocalories. Then run the static
rule forward for 365 days using 7,716.18 kcal per kilogram, and compare your figure
with the paper's own reported prediction for the static rule of "22 kg lost in the
first year".

**5.** A textbook states: "The accumulation of an extra 3500 calories adds one pound of
weight. If an excess of 200 calories per day is ingested, one extra pound of body
weight will be gained every 18 days. At that rate, an extra 20 pounds can be gained
over the course of a year." A student extends the reasoning: "So anyone eating 200
calories over their needs, every day, for the rest of their life, will gain 20 pounds
a year, every year, forever." Find the step that broke.

**6.** Here is a worked answer. Find the step that broke.

```working
    a clinic wants a target for 8 kilograms of fat loss
    the static rule gives 3,500 for a unit of weight change
    8 times 3500 = 28,000
    so the patient needs a total deficit of 28,000 kcal
```

**7.** A slimming programme's leaflet says: "Cut 500 calories a day and you will lose about a
pound a week — in six months, that is 26 pounds off." Decide what to compute, compute
it, and say what your answer does not establish.

**8.** A dietitian tells a patient: "Keep to 500 kcal under your target and you'll reliably
lose a pound a week — do the maths yourself if you don't believe me." Decide what to
compute, compute it, and say what your answer does not establish.

