# S02-R1-C16 · Following a derivation without skipping

**Definition.** A derivation is a chain of equations in which each line follows from the line before it by
one move that can be named. The moves this book uses are these.

- Substitute: replace a symbol by something stated to be equal to it.
- Rearrange: do the same thing to both sides, by the four operations of `B0-R0-C16`.
- Divide by a time interval and shrink it: turn a change over an interval into a rate at an
  instant, the derivative of `S02-R1-C02`.
- Differentiate both sides, or integrate both sides over an interval, as `S02-R1-C03` and
  `S02-R1-C05` do.
- Assume: bring in a new premise.

The first four moves carry the truth of the line before them to the line after. An assumed
line carries nothing from above. It is a new premise, in the sense of `B0-R0-C42`, and every
line below it holds only as far as it does.

A where-clause fixes each symbol's meaning, its unit and its sign. The same printed equation
can say opposite things under two readings of its where-clause.

Following a derivation means three things. Write the move beside every line. Fill in any line
the author skipped, one move at a time. And find any line that no named move produces, or that
rests on an assumption nobody stated.

**In plain terms.** A derivation is a staircase. Each step down is one small move you could make yourself. You put
one thing in place of another, or do the same to both sides. Or you turn a change into a rate, or
a rate into a change. If you can name the move, the step is safe, and the line below is as true as the line
above.

Some steps are not moves at all. The author brings in something new: "suppose expenditure stays
fixed". That line is a premise. Everything below it depends on it, however careful the steps that
follow.

So read a derivation with a pencil. Beside every line, write the move that got you there. When
you cannot name one, stop. Either the author skipped steps, and you fill them in, or the author
slipped in a premise, and you write it down as one.

**Illustration.** Start with the rule Book 1 called the static rule, as Thomas and colleagues print it (Thomas
2013). They write W(t) for the expected weight, in pounds, on day t, and W0, said "W nought",
for the weight at the start. They write ΔEB for "the change in energy balance in kcal/d". Their
equation says: the weight on day t is the starting weight minus ΔEB times t, divided by 3,500.

```working
W(t) = W0 − ΔEB × t / 3500
```

Rebuild it from the identity, one move per line. Write the move beside each line as you go.

Line 1 is the identity as a rate. Hall and colleagues state it this way (Hall 2012). The rate
of change of the body's energy stores ES equals the rate of energy intake (EI) minus the rate
of energy expenditure (EE). They write it ES = EI − EO. As `S02-R1-C01` showed, this book
writes the rate of change of ES as dES/dt, and expenditure as EE.

```working
dES/dt = EI − EE (line 1: the identity, taken as given)
```

Line 2 brings in something new. The rule assumes every 3,500 kcal of stored energy gained or
lost is one pound of body weight. So the rate of change of stored energy is 3,500 times the
rate of change of weight, W in pounds a day. Check the unit: kcal a pound times pounds a day
is kcal a day, the unit of dES/dt.

```working
dES/dt = 3500 × dW/dt (line 2: assumed, 3,500 kcal in every pound)
```

Line 3 puts line 2 in place of dES/dt in line 1.

```working
3500 × dW/dt = EI − EE (line 3: substitute)
```

Line 4 is a second assumption. Intake minus expenditure stays the same number on every day.
Call that number ΔEB.

```working
3500 × dW/dt = ΔEB (line 4: assumed, the gap never changes)
```

Line 5 divides both sides by 3,500.

```working
dW/dt = ΔEB / 3500 (line 5: rearrange)
```

Line 6 integrates both sides from day 0 to day t. The rate is the same every day, so the area
under it is a rectangle, rate times time, as in `S02-R1-C05`. The left side becomes the change
in weight.

```working
W(t) − W0 = ΔEB × t / 3500 (line 6: integrate both sides from 0 to t)
```

Line 7 adds W0 to both sides.

```working
W(t) = W0 + ΔEB × t / 3500 (line 7: rearrange)
```

Now set your line 7 beside the printed equation. Yours has a plus where theirs has a minus. No
line of yours is wrong. The difference sits in the where-clause. Thomas and colleagues define
ΔEB as "the difference between the rate of energy intake and the rate of energy expenditure".
That phrase does not say which is taken from which.

Your line 4 took intake minus expenditure. On that reading a deficit makes ΔEB negative, and
the printed minus sign would make weight rise. The printed equation predicts a fall only if
ΔEB is expenditure minus intake: the deficit, written as a positive number.

Test both readings on made-up numbers. Start at 180 pounds, with a deficit of 500 kcal a day.
At day 70, the change is:

```working
500 times 70 divided by 3500 = 10
```

```table
day  ΔEB read as expenditure minus intake (lb)  ΔEB read as intake minus expenditure (lb)
0  180  180
35  175  185
70  170  190
105  165  195
140  160  200
```

The derivation told you which reading the equation needs. It also shows you where the rule goes
wrong. Lines 1, 3, 5, 6 and 7 are safe moves. Lines 2 and 4 are assumptions. Hall and colleagues
reject line 4. In their words, "weight change will slow over time due to passive compensatory
changes in energy expenditure that occur with the weight change." Expenditure falls as weight
falls, so the gap in line 4 shrinks.

Now a derivation the paper leaves out. Polidori and colleagues work out the change in each
person's energy intake from their weights alone, with their Equation 1 (Polidori 2016). They
write body weight as BW; here it is W. Set aside, for now, two terms this book comes back to
below. The equation then says this. The change in intake since the start equals ρ times the
rate of change of weight, plus ε times the change in weight since the start.

```working
ΔEI = ρ × dW/dt + ε × (W − W0)
```

The Greek letter rho, ρ, is "the effective energy density associated with the body weight
change", in kcal per kg. The Greek letter epsilon, ε, sets "how energy expenditure depends on
body weight", in kcal a day per kg. The paper calls Equation 1 a linearization. Here that means
expenditure is drawn as a straight line in weight. Rebuild it.

Line 1 is the model of `S02-R1-C07`. That section wrote the result of this rebuild without the
steps between. Its model says that ρ times the rate of change of weight equals intake minus
expenditure, and that expenditure depends on weight.

```working
ρ × dW/dt = EI − EE(W) (line 1: the model, taken as given)
```

Line 2 assumes expenditure is a straight line in weight near the start. It is its starting
value, EE0, plus ε times the change in weight.

```working
EE(W) = EE0 + ε × (W − W0) (line 2: assumed, a straight line near the start)
```

Line 3 writes intake as its starting value, EI0, plus a change, ΔEI. This defines ΔEI. It
assumes nothing.

```working
EI = EI0 + ΔEI (line 3: definition)
```

Line 4 puts lines 2 and 3 into line 1.

```working
ρ × dW/dt = EI0 + ΔEI − EE0 − ε × (W − W0) (line 4: substitute)
```

Line 5 needs a premise. At the start, weight was steady, so its rate was zero. That is the
equilibrium of `S02-R1-C08`: intake equalled expenditure, and EI0 minus EE0 is zero.

```working
ρ × dW/dt = ΔEI − ε × (W − W0) (line 5: assumed, steady at the start)
```

Line 6 adds ε × (W − W0) to both sides and swaps the sides.

```working
ΔEI = ρ × dW/dt + ε × (W − W0) (line 6: rearrange)
```

The paper's full Equation 1 has two more terms. One is multiplied by Δδ, the change in
physical activity; δ is the Greek small letter delta. The paper says that without measurements this is
"often assumed to be zero", and then the term vanishes. The other, written UGE, is the energy
lost as glucose in the urine, which the drug in their trial increases. A practice problem adds
it.

Look at what your six lines show. The equation that turns weights into intake is the balance
of `S02-R1-C07` plus premises. Expenditure is a straight line, the start is steady, and the
activity change is assumed to be zero. Each premise is a place a reader can push.

**Where this picture breaks.** The 180 pounds and the 500 kcal a day are made up. The two straight lines in the table hold
only while lines 2 and 4 hold. Hall and colleagues say line 4 does not hold for long.

The rebuild of Polidori's Equation 1 shows its shape and the premises it needs. It is not the
paper's own route: the paper cites an earlier study for its method, which this book has not
opened. The rebuild also takes ρ and ε as given. The paper builds each from further quantities
in its Equations 2 and 3, and those steps are not checked here.

**Figure.** The printed equation W(t) = W0 − ΔEB × t / 3500 under two readings of ΔEB, for a made-up start of 180 pounds and a deficit of 500 kcal a day. Read as expenditure minus intake, weight falls to 160 by day 140; read the other way, the same equation makes it rise to 200. The weight axis does not start at zero.

*What the figure shows:* Two straight lines from 180 pounds at day 0. One falls through 170 at day 70 to 160 at day 140. The other rises through 190 at day 70 to 200 at day 140.

**Must know points for you.**

- Beside every line of a derivation, write the move that produced it. If you cannot name one, the line is a skipped step or a premise. Fill in the step, or write the premise down as one.
- A result derived from the first law is not thereby proved. The 3500 kcal rule follows correctly from the energy-balance identity plus two assumptions, and it fails because of one of them. When someone says an equation "comes from physics", ask which lines are physics and which are assumptions.
- A where-clause fixes signs, and "the difference between A and B" does not say which is taken from which. Test a printed equation on a case whose answer you know. A deficit must lower weight. If your reading makes it raise weight, your reading is wrong.
- Check the unit of every term on every line. A line whose terms carry different units did not follow from the line above, however tidy it looks.
- Following a derivation tells you whether each line follows. It cannot tell you whether an assumed line is true; that needs evidence, as the passive fall in expenditure is for the 3500 kcal rule. Where a paper cites another paper for its steps, say you could not rebuild them, rather than trusting them because the result looks tidy.
- When you teach a derivation, have the trainee mark assumed lines differently from derived ones, before they say anything about the result. A trainee who can point to the assumed lines can say what a model's prediction rests on.
- When a press line says a diet "must" produce a steady loss "because of physics", the accurate reply is short. The physics gives one line. The steady loss needs a second line, that expenditure stays fixed, and it does not.

**Exercise 1** (teaching). A first-year resident asks where the rule "3,500 kcal a pound" comes from and why the
consensus panel dropped it. You have ten minutes and a whiteboard. Plan what you will write,
line by line.

**Exercise 2** (critique). A trainee's journal-club slide says: "Polidori and colleagues derive Equation 1 from the first
law of thermodynamics, so the intake changes it gives are exact."

Find the specific flaw.

**1.** Write the move that produced each line from the line above it.

```working
4x + 6 = 26
4x = 20
x = 5
```

**2.** Write the move that produced the third line.

```working
y = 3x
x = 5
y = 15
```

**3.** The author went from the first line to the last in one step. Fill in the skipped lines, one
move each, and name each move.

```working
5x − 4 = 2x + 11
x = 5
```

**4.** Name the move from the first line to the second, and the rule it uses.

```working
y = 4t + 3
dy/dt = 4
```

**5.** A quantity W is 80 at t = 0 and its rate of change is dW/dt = −0.2 at every t. Write the lines
that give W at t = 10, with the move beside each.

**6.** Find the line that does not follow from the one above it, and say what it should be.

```working
4x + 8 = 20
x + 8 = 5
x = -3
```

**7.** Use the equation W(t) = W0 − ΔEB × t / 3500, with W in pounds and ΔEB in kcal a day (Thomas 2013).
Take the reading that makes a deficit lower weight. A person starts at 200 pounds with a deficit
of 700 kcal a day, figures made up for this problem.

Work out W(28), and say which reading of ΔEB you used.

**8.** Chow and Hall describe one step in words (Chow and Hall 2008). They "divide Equation 1 by some
interval of time and take the limit of infinitesimal change".

Apply that step to Book 1's identity over an interval of Δt days. Write ES for body energy
stores in kcal.

```working
ΔES = (energy taken in over the interval) − (energy spent over the interval)
```

Write the lines that take it to Hall's rate form, naming each move, and give the unit of each
side at each line.

**9.** In Polidori and colleagues' trial the drug makes the body lose extra glucose in the urine,
which the paper calls UGE (urinary glucose excretion). Write it U, energy lost a day, zero
before the drug starts. The balance becomes:

```working
ρ × dW/dt = EI − EE(W) − U
```

Using the same premises as the section's rebuild, derive an equation for ΔEI, naming each
move. Then compare it with the paper's Equation 1 with Δδ = 0 (Polidori 2016).

**10.** Here is a worked answer, with made-up intake and expenditure. Find the step that broke.

```working
3500 × dW/dt = EI − EE
dW/dt = EI − EE / 3500
with EI = 2000 and EE = 2500, dW/dt = 2000 − 0.714 = 1999.3 pounds a day
```

**11.** Here is a worked answer. Find the step that broke.

```working
ρ × dW/dt = EI − EE(W)
EE(W) = EE0 + ε × (W − W0), and EI = EI0 + ΔEI
ρ × dW/dt = EI0 + ΔEI − EE0 − ε × (W − W0)
so ΔEI = ρ × dW/dt + ε × (W − W0)
```

**12.** Here is a worked answer. Find the step that broke.

```working
a made-up rate of change of weight: dW/dt = −0.1 plus 0.001 t, in kg a day, t in days
integrate both sides from 0 to 60: the change is the rate times the time
at t = 60 the rate is −0.1 plus 0.06 = −0.04
change = −0.04 times 60 = −2.4 kg
```

**13.** Thomas and colleagues report a mean deficit of 1439 kcal a day over a mean of 64.8 days
(Thomas 2013). The mean loss the 3500 kcal rule predicted was 27.6 pounds.

A colleague says: "1439 times 64.8 divided by 3500 is 26.6, not 27.6, so their prediction has an
arithmetic slip."

Decide what to compute, compute it, and say what your answer does not establish.

**14.** A health column says: "Physics proves that cutting 500 kcal a day loses a pound a week, for as
long as you keep it up."

Decide what to compute, compute it, and say what your answer does not establish.

