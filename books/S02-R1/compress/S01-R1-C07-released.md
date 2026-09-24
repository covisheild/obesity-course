# S01-R1-C07 · Sizing an imbalance, and the static rule

**Definition.** A kilogram of body fat is proposed to hold a fixed number of kilocalories. A surplus or a
deficit of energy intake, summed over time, then converts into a change in fat mass at
that fixed rate. Every other quantity is held constant for the interval this is
applied to: the day's intake, the day's expenditure, and the energy content of a
kilogram of fat itself. This is the static rule.

Its common English form is 3,500 kilocalories removed or added for each pound of body
weight changed. The rule is stated for body weight, and it assumes every kilogram of that
weight is fat tissue. The sources this book cites trace it to Wishnofsky (1958), cited by
Thomas (2013) and Hall (2008). Hall and colleagues (2011) say it was "derived by estimation
of the energy content of weight lost". Wishnofsky's estimate is the calculation
`S01-R1-C02` describes: tissue taken to be 87% fat, times fat's energy per gram.

```working
    3500 divided by 0.45359237 = 7716.18
```

About 7,716 kilocalories per kilogram.

Given a daily surplus or deficit of D kilocalories, held at the same size for n days, the
static rule predicts a change in fat mass of D times n, divided by 7,716, in kilograms.
Because D is held fixed, the predicted change is a straight line against time: the same
daily D always predicts the same rate of change, on day one and on day one thousand.

The rule fails for two separate reasons, and this section covers the second. First, real
tissue lost is not all fat tissue, so no single kilocalories-per-kilogram figure holds for
every kilogram lost; `S01-R1-C02` covers that. Second, and the
reason a straight line is the wrong shape, intake and expenditure are not constant
through a period of weight loss: both respond to the loss itself.

**In plain terms.** Say a kilogram of fat is worth a fixed number of kilocalories. Eat that many fewer than
you burn, and a kilogram should come off. That is the whole idea, and the number everybody
has heard is 3,500 kilocalories for a pound.

A pound is not the unit this course uses, so turn it into kilograms first. One pound is
exactly 0.453 592 37 kilogram. Divide the 3,500 by that.

```working
    3500 divided by 0.45359237 = 7716.18
```

About 7,716 kilocalories for a kilogram. It is a calculation, not something anybody measured.

Pick a daily surplus or deficit, and hold it the same size every day. Multiply it by the
number of days, and divide by 7,716.

Plot that against time and you get a straight line, because the daily amount never changes
in the sum. Nobody's daily intake and daily expenditure sit still while they lose weight.
A smaller body spends less.

**Illustration.** Take the scenario Hall and colleagues (2011) use in the *Lancet* to make this point. A
sedentary man weighing 100 kilograms cuts his energy intake by 2 megajoules a day and
keeps it cut. One kilocalorie is 0.004184 megajoules, so divide by that.

```working
    2 divided by 0.004184 = 478.01
```

About 478 kilocalories a day. Run the static rule forward for one year.

```working
    478.01 times 365 = 174473.65
    174473.65 divided by 7716.18 = 22.61
```

About 22.6 kilograms in the first year.

Now the failure. The paper's own dynamic model is built on energy balance, with
expenditure allowed to change. For the same man on the same cut, it predicts weight
levelling off towards about 75 kilograms. The model takes "roughly 1 year to reach half of the
maximum weight loss". It is 95% of the way there after about three years.

```table
model                weight change after one year
the static rule       about 22.6 kg
the dynamic model      roughly 11 to 12.5 kg (the paper: the static rule's 22 kg is about double)
```

The static rule is not merely optimistic here. It has the wrong shape. It says every
year should look like the first, for as long as the deficit is kept up. The dynamic
model says the loss slows and levels off. The man's expenditure falls as his body gets
smaller. That shrinks the real deficit, even though his intake has not changed again.

Thomas and colleagues (2013) pooled 103 adults whose diets were supervised or whose
intake was measured. Their prescribed deficit averaged 1,439 kcal a day. Work out what
the static rule predicts they should lose over their average 64.8 days on the diet.

```working
    1439 times 64.8 = 93247.2
    93247.2 divided by 3500 = 26.64
```

About 26.6 pounds. The paper's own figure is 27.6 pounds. The paper worked the rule out
person by person and averaged. Multiplying two averages gives a slightly different
number.

What they actually lost was 20.1 pounds: "Subjects lost 20.1±11.3 lbs, 7.4±12.6 lb less
than the 27.6±16.0 lbs predicted by the 3500 kcal rule." The number after ± shows how
widely people varied around the average. (27.6 minus 7.4 is 20.2. The 0.1 is rounding in
the paper's figures.)

**Where this picture breaks.** The straight line holds only until intake and expenditure respond to the loss. No source
here gives an interval over which it is safe. The Hall model puts half the eventual loss
in the first year. Thomas's dieters already fell about a quarter short of the rule within
about nine weeks.

**Figure.** Hall's 100 kg man cutting 2 MJ a day: the static rule's straight line loses about 22.61 kg every year. The dynamic model loses half of its 25 kg in year 1 and is 95% of the way to about 75 kg by year 3.

*What the figure shows:* Body weight against years. A dashed straight line falls from 100 kg through 77.39 at year 1 to 32.17 at year 3. A second line falls from 100 to 87.5 at year 1 and 76.25 at year 3, slowing as it goes.

**Figure.** Thomas's cohort: 1,439 kcal a day for 64.8 days gives 26.64 lb on the static rule. Measured loss was 20.1 lb, 7.4 lb less than the paper's own 27.6 lb prediction.

*What the figure shows:* Pounds lost against days on the diet. A dashed line rises from 0 to 26.64 lb at day 64.8. A single measured point at day 64.8 sits at 20.1 lb, below the line.

**Must know points for you.**

- Convert the unit before you argue about the number.
- A rule that holds a daily amount fixed and multiplies it by time always draws a straight line, whatever the real quantity does.
- The static rule's assumption that expenditure stays put is closest to true in the first days. Its assumption that the loss is fat is furthest from true then. Trust it for neither the first week nor the long run.
- When you tell a patient a target using this rule, say that it over-predicts from the first weeks.
- At the rule's 7,716 kcal, a kilogram of fat is two to four whole days of a person's total expenditure. That uses `S01-R1-C03`'s 8 to 16 megajoules a day.
- A figure like 3,500 kcal per pound being widely printed, including in textbooks, does not make it a measured property of fat.

**Exercise 1** (calculation). A person keeps to a deficit of 600 kcal a day for 40 days. Using the static rule,
work out the predicted loss in kilograms.

**Exercise 2** (teaching). A health secretary has one page and wants an answer first. They have asked: "Is the
3,500-calorie rule good enough to put in a public information leaflet?"

**1.** A rule says 3,500 kcal removes one pound. One pound is 0.45359237 kilogram. How many
kcal per kilogram is that?

**2.** Using a rate of 3,500 for one unit, work out the total for 5 units, and separately for
12 units.

**3.** Thomas and colleagues' pooled dieters were prescribed an average deficit of 1,439 kcal a
day. They were on the diet for an average of 64.8 days. Use the static rule's 3,500 kcal
a pound to work out the predicted loss in pounds. Then convert it to kilograms. One pound
is exactly 0.45359237 kg.

**4.** Hall and colleagues model a 100 kg sedentary man. He cuts his intake by 2 megajoules a
day and holds that cut for a year. One kilocalorie is 0.004184 megajoules. Use that to
turn the daily cut into kilocalories. Then run the static rule forward for 365 days at
7,716.18 kcal per kilogram. Compare your figure with the paper's static-rule prediction
of "22 kg lost in the first year".

**5.** A textbook states: "The accumulation of an extra 3500 calories adds one pound of
weight. If an excess of 200 calories per day is ingested, one extra pound of body
weight will be gained every 18 days. At that rate, an extra 20 pounds can be gained
over the course of a year." A student extends the reasoning. "So anyone eating 200
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

