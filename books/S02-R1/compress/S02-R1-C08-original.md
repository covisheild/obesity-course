# S02-R1-C08 · Equilibrium: where the rate is zero

**Definition.** An equilibrium, or steady state, of a differential equation dW/dt = f(W) is a constant value
of the state at which the rule gives a rate of zero. It is written W*, read "W star", so
f(W*) = 0. The constant function W(t) = W* is then a solution, because its derivative is
zero and the rule also gives zero. To find the equilibria, set the right-hand side equal to
zero and solve for the state.

Take the equation of the last section, ρ × dW/dt = ΔEI − ε × (W − W0). Setting its right
side to zero gives ε × (W* − W0) = ΔEI. So W* − W0 = ΔEI ÷ ε. On a graph of kilocalories a day
against weight, W* is where the line for intake crosses the line for expenditure. When
intake does not depend on weight, as in Hall and Guo's settling point model, the shift in
the equilibrium is the change in intake divided by the slope of expenditure.

When intake also depends on weight, it rises by a fixed number of kilocalories a day for
each kilogram lost. Polidori and colleagues write that number kP, k with a P for
proportional. The model is then ρ × dW/dt = ΔEI − (ε + kP) × (W − W0). The two slopes add, and the shift
becomes ΔEI ÷ (ε + kP). Hall and Guo call a model with feedback on both intake and
expenditure a set point model. The name is theirs; the equilibrium still moves when intake
is shifted.

In either model, a weight that starts away from the equilibrium approaches it along an
exponential. The gap W − W* is multiplied by the same factor in every equal step of time.
Its time constant, written tau (τ), is ρ divided by the total slope, in days. The gap
halves every τ × ln 2 days.

An equilibrium is stable if a state pushed a little away from it returns to it, and
unstable if the state moves further away. With every slope positive, the rate is negative
above W* and positive below it, so W* here is stable. Classifying equilibria in general is
the work of the second book of this subject.

At an equilibrium the rate of change of stored energy is zero. Intake and expenditure are
equal. Neither is zero.

**In plain terms.** The last section ended with curves that fall and then flatten. This section finds the level
they flatten at, without walking the curve to get there.

The idea is short. A weight stops moving when its rate of change is zero. So take the
equation, put zero where the rate is, and solve for the weight. That weight is the
equilibrium.

Picture it as two lines on one graph, with weight along the bottom and kilocalories a day up
the side.

- Expenditure rises as weight rises. A bigger body costs more to run.
- Intake is a flat line, if it ignores weight.

Where the two lines cross, intake equals expenditure, and the weight stops moving. Cut
intake, and the flat line drops. The crossing slides to a lower weight. How far it slides is
the cut divided by the slope of the expenditure line. A steep line means a short slide.

Now let intake rise as weight falls, which is what appetite does. Then the intake line tilts
too, and it tilts against the change. The two slopes add, and the crossing slides a much
shorter way.

Three more things are worth carrying out of this section.

- The weight does not arrive at the crossing on a date. It closes the gap by the same
  fraction every day, fast at first and then ever more slowly.
- Push the weight a little either side of the crossing, and the rate sends it back. That is
  what stable means here.
- At the crossing, intake and expenditure are equal. Both are still large. A steady weight is
  busy, not idle, as Book 0 said of any steady stock.

**Illustration.** Start with the model that has no sensible equilibrium: the static rule. Its expenditure
ignores weight, so ε is 0. Hall and colleagues' man cuts 480 kilocalories a day. Set the
rate to zero in his equation and see what is left.

```working
0 = −480 − 0 × (W* − 100)
0 = −480
```

That is false for every weight. There is no equilibrium, so the weight falls for ever,
which is the static rule's straight line. Now let him go back to his old intake, so ΔEI is
0.

```working
0 = 0 − 0 × (W* − 100)
```

This is true for every weight. Every weight is an equilibrium, so whatever he weighs, he
stays there. Hall and Guo name the consequence: in the static model, "the same baseline
energy intake allows for maintenance of the reduced weight." No equilibrium, or every weight an equilibrium: that is what the
static rule says. Neither is what bodies are observed to do.

Now use the equation of the last section, with ε = 20 kilocalories a day per kilogram.

```working
0 = −480 − 20 × (W* − 100)
20 × (W* − 100) = −480
W* − 100 = −480 ÷ 20 = −24
W* = 76
```

The second line adds 20 × (W* − 100) to both sides. The third divides both sides by 20. The
equilibrium is 76 kilograms. Look back at the last section's table and you will find the
ε = 20 column at 77.40 on day 1095, still closing on 76. With ε = 30 the same steps give this.

```working
480 divided by 30 = 16
100 minus 16 = 84
```

84 kilograms, and the table's ε = 30 column reads 84.23 at day 1095. Hall and colleagues'
own model, which is richer than this one, predicted "a bodyweight plateau at about 75 kg".

You can check that 76 is stable. Put the man 4 kilograms above it, at 80, and 4 below it,
at 72.

```working
at 80:  −480 − 20 × (80 − 100) = −480 + 400 = −80
at 72:  −480 − 20 × (72 − 100) = −480 + 560 = 80
```

Above 76 the rate is negative, so the weight falls back. Below 76 it is positive, so the
weight rises back. Either way it returns.

Now the two models Hall and Guo (2017) draw side by side. Both start from a cut of 300
kilocalories a day: "When the same 300 kcal/d is cut from the diet".

In the settling point model, intake is flat and expenditure rises "with a slope of about
20–30 kcal/d per kg". The shift in the equilibrium is the cut divided by the slope.

```working
300 divided by 20 = 15
300 divided by 30 = 10
```

Ten to 15 kilograms lower. That is where the flat intake line, 300 below its old level,
crosses the expenditure line. At 5 kilograms down, the expenditure line with slope 20 is
100 below its old level. So there is still a gap of 200 between the two lines, and the
weight is still falling.

In the set point model, intake also depends on weight, "with a slope of about -100 kcal/d
per kg". Polidori and colleagues (2016) measured the same feedback as their kP: eating
rose "by ~100 kcal/day per kg of lost weight". Write the model with both slopes.

```working
ρ × dW/dt = −300 − 100 × (W − W0) − ε × (W − W0)
         = −300 − (100 + ε) × (W − W0)
```

The two slopes add, because both push the same way. Losing weight lowers what goes out and
raises what comes in. Set the rate to zero.

```working
300 divided by 120 = 2.5
300 divided by 130 = 2.307692308
```

About 2.3 to 2.5 kilograms, against 10 to 15. The same cut moves the equilibrium about a
sixth to a quarter as far.

Polidori's trial gives a check on the arithmetic of this model. The drug made people lose
glucose in their urine. The paper finds that "energy intake was calculated to have
increased by ~350 kcal/day at steady state". Equation 4 of the paper says the rise in intake
is kP times the weight lost. Divide to get the weight lost.

```working
350 divided by 100 = 3.5
```

About 3.5 kilograms. The paper reports that weight "reached a new equilibrium several
kilograms lower". The two agree in size.

Now the approach. The last section's solution can be written as a gap that shrinks.

```working
W(t) − W* = (W0 − W*) × e^(-t/τ),   with τ = ρ ÷ (total slope)
```

Take ρ = 7,716.18 kilocalories per kilogram, the stand-in of the last section. For the
settling point model with slope 20 the total slope is 20. For the set point model it is
100 + 20 = 120.

```working
7716.18 divided by 20 = 385.809
7716.18 divided by 120 = 64.3015
```

Time constants of about 386 and 64 days. Each gap halves every τ × ln 2 days. From the
section on e, ln 2 is 0.6931.

```working
385.809 times 0.6931 = 267.4
64.3015 times 0.6931 = 44.57
```

And each reaches 95% of its shift at τ × ln 20, where ln 20 is 2.9957.

```working
385.809 times 2.9957 = 1155.8
64.3015 times 2.9957 = 192.63
```

About 3.2 years against about 6 months. Here is the loss, in kilograms, with each model.

```table
day   settling point, slope 20  set point, slopes 100 + 20
0     0                         0
30    1.12                      0.93
60    2.16                      1.52
90    3.12                      1.88
180   5.59                      2.35
365   9.18                      2.49
730   12.74                     2.50
1095  14.12                     2.50
```

Each column is the shift times (1 − e^(-t/τ)), with its own shift and its own τ. The set
point curve flattens sooner and lower. Hall and Guo say the settling point model "takes
years to equilibrate". This column agrees.

Last, the equilibrium is not a place where nothing happens. At 76 kilograms, Hall's man eats
what a 76 kilogram man of his habits spends. Book 1 showed that a day's expenditure runs to
thousands of kilocalories for most adults. Both flows are that large, and they are equal. Hall and colleagues
(2012) describe a weight held over the long term in the same way: "average E S approaches
zero". The net rate is zero. Neither flow is.

And if the man goes back to his old intake, the equilibrium goes back to 100. The weight
follows it, along the same kind of curve. Hall and Guo: "weight regain ensues with an
exponential time course mirroring the weight loss phase." Regain here is the equation
working, not a person failing.

**Where this picture breaks.** Every equilibrium here comes from straight lines. Polidori and colleagues are frank about
their own feedback term. They "do not yet know" whether it holds "for a range of weight
losses". The slopes are group
averages, and Hall and Guo expect "a wide degree of individual variation". So an
equilibrium worked out here is a model's figure for an average person, not a prediction
for the one in front of you.

The time constants use the static rule's ρ as a stand-in, so their sizes are illustrative.
Hall's own model reaches half its loss in about a year and 95% in about three. The section
on e showed those two outputs do not come from one exponential. This straight-line model
is simpler than Hall's.

A scale does not show an equilibrium over a few weeks. Hall and colleagues (2012) warn that
"changes in body weight also include changes in body water, which may be variable".

**Figure.** Hall and Guo's settling point model after a 300 kcal a day cut. Flat intake crosses expenditure 15 kg down when the slope is 20 kcal a day per kg, and 10 kg down when it is 30.

*What the figure shows:* Change from the start in kcal a day against change in weight in kg, from minus 15 to 0. A flat line at minus 300. Two lines through the origin, with slopes 20 and 30, meet it at minus 15 and minus 10.

**Figure.** Loss after the same 300 kcal a day cut, with ρ = 7,716.18: the settling point model (slope 20) is still closing on 15 kg at day 1095. With intake also responding (slopes 100 + 20) the loss flattens at 2.5 kg within months.

*What the figure shows:* Kilograms lost against days, 0 to 1095. One curve rises through 3.12 at day 90 and 9.18 at day 365 to 14.12 at day 1095. The other rises steeply through 0.93 at day 30 and 1.88 at day 90, and is flat at 2.50 from day 730.

**Must know points for you.**

- To find where a model says weight will settle, set the rate to zero and solve for the weight. Do not run the model forward and read off where it seems to stop. The algebra gives the level exactly, and it shows which numbers the level depends on.
- In the settling point model, a lasting cut of 300 kilocalories a day moves the equilibrium down 10 to 15 kilograms. It takes years to get there. Now let eating rise by about 100 kilocalories a day for each kilogram lost. The same cut then moves it only 2.3 to 2.5 kilograms. Before you give a patient a target from a cut in food, say which model it came from.
- "Keep eating what got you to the new weight and you will stay there" is the static model. In it, every weight is an equilibrium. When expenditure falls with weight, going back to the old intake moves the equilibrium back to the old weight. Tell a patient that regain is this equation at work. Never call it a lapse.
- A steady weight means intake equals expenditure, not that either is small. Say it that way to a journalist who calls a stable weight a sign that "nothing is going on".
- A weight that stops falling for a few weeks is not thereby at an equilibrium. The rate is zero at an equilibrium and stays zero. It can pass through zero for a moment while intake is still moving, and water shifts can hide the true rate for weeks. In the programme Polidori and colleagues describe, average weight was lowest at about 8 months. Intake was already back within 100 kilocalories a day of where it began, and slow regain followed.
- An equilibrium worked out from straight lines is only as good as the lines. They hold where the slopes were measured, and for the average person. Polidori and colleagues do not yet know if their slope for eating holds for larger losses. So quote such a figure as the model's answer for a group, and name the slopes. Never give it to one person as the weight they will end at.
- When a trainee adds up the slopes, check the signs first. As weight falls, intake goes up and expenditure goes down. Both push the weight back, so their slopes add. Subtract them, and the pull looks weaker and the shift looks larger.

**Exercise 1** (critique). A policy note says this.

> A population-wide cut of 100 kcal a day, sustained, will lower average weight every
> year. The loss is 100 × 365 ÷ 7,700 = 4.7 kg a year.

Say what is wrong, using the idea of an equilibrium. Then give the figure you would put
in its place, with the source of every number in it.

**Exercise 2** (teaching). A journalist has three minutes and no jargon. They ask: "Why do people who lose weight so
often put it back on?" Give them the idea of an equilibrium without the word, and one
quotable sentence.

**1.** Find the equilibrium of dy/dt = 12 − 0.4 × y.

**2.** Find the equilibrium of dy/dt = −0.05 × (y − 70). Then work out the rate at y = 60 and at
y = 80, and say what each tells you.

**3.** Intake is a flat line at 2,000 units. Expenditure is 500 + 25 × W. Find the W where they
cross. Then drop intake to 1,800 and find the new crossing. How far did it move?

**4.** Intake is 5,700 − 60 × W and expenditure is 500 + 20 × W. Find the crossing. Then lower
intake by 400 at every W and find the new crossing.

**5.** Take dy/dt = −0.02 × (y − 50), with y = 60 at t = 0. Give the time constant, the half-time,
and y at t = 50. Use ln 2 = 0.6931 and e^(-1) = 0.3679.

**6.** A flat intake line is lowered by 300. The equilibrium moves by 12. What is the slope of
the expenditure line?

**7.** Hall and Guo (2017) cut 300 kilocalories a day from the diet in their settling point
model. Expenditure rises with weight at about 20 to 30 kilocalories a day per kilogram.
Work out how far the equilibrium weight moves at each end of that range.

**8.** Now Hall and Guo's set point model. The same 300 kilocalories a day is cut, and intake
also changes with weight, with a slope of about −100 kilocalories a day per kilogram.
Work out the shift in the equilibrium at each end of the 20 to 30 range for expenditure.
Compare with the settling point model.

**9.** Hall and colleagues (2011) give a rule of thumb. Every change of intake of 100 kJ a day
leads to "an eventual bodyweight change of about 1 kg". The paper adds "(equivalently, 10
kcal per day per pound of weight change)". Turn each form into kilocalories a day per kilogram.
Then give the equilibrium shift each form predicts for a cut of 300 kilocalories a day.
One kilocalorie is 4.184 kilojoules. One pound is 0.45359237 kilograms.

**10.** Polidori and colleagues ran a drug trial. At steady state, "energy intake was calculated
to have increased by ~350 kcal/day". Their Equation 4 says the change in intake is minus kP
times the change in weight. kP is about 100 kilocalories a day per kilogram. Work out the
weight change at steady state. Compare it with the paper's "new equilibrium several
kilograms lower".

**11.** Hall and colleagues' 100 kg man cuts 480 kilocalories a day. Their model predicts a
plateau "at about 75 kg". Their rule of thumb, 100 kilojoules a day per kilogram, is 23.90
kilocalories a day per kilogram. Work out the plateau the rule of thumb gives him. Then say
why the two might differ. The paper's summary helps: "adults with greater adiposity have a
larger expected weight loss for the same change of energy intake". Adiposity means how
much body fat a person carries.

**12.** Here is a worked answer. Find the step that broke.

```working
set point model: 300 kcal/day cut, intake slope −100, expenditure slope 20
combined slope = 100 − 20 = 80
shift = 300 ÷ 80 = 3.75 kg
```

**13.** Here is a worked answer. Find the step that broke.

```working
settling point model: ρ = 7716.18 kcal per kg, ε = 20 kcal/day per kg
time constant τ = ε ÷ ρ = 20 ÷ 7716.18 = 0.00259
so the weight is essentially at its new equilibrium within a day
```

**14.** Here is a worked answer. Find the step that broke.

```working
Polidori's programme: weight lowest at about 8 months, with intake within 100 kcal/day of baseline
at the lowest point, weight stopped falling, so dW/dt = 0
dW/dt = 0 is the definition of an equilibrium
so the lowest weight was the new equilibrium, and the group could hold it on that intake
```

**15.** Here is a worked answer. Find the step that broke.

```working
Hall's man, ε = 20, ρ = 7716.18: equilibrium 76 kg, time constant 385.809 days
the time constant is how long it takes to reach equilibrium
so on day 386 he weighs 76 kg
```

**16.** A newspaper headline reads: "Cut 300 calories a day and lose 15 kg, says top weight
scientist." The headline is made up for this problem.

Decide what to compute, compute it, and say what your answer does not establish.

**17.** A colleague says of a patient: "Her weight has been flat at 82 kg for two months. She's hit
her set point, so no change in what she eats will move it." The patient and her weight are
made up for this problem.

Decide what to compute, compute it, and say what your answer does not establish.

