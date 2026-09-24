# S02-R1-C17 · Four kinds of equation, and the notebook entry

**Definition.** An equation in a paper is one of four kinds, and each kind is checked a different way.

An identity holds for every value of its symbols, because of how its quantities are defined or
because a conservation law requires it. It is checked by asking whether every term is counted
across the same boundary and over the same interval. It names no cause and gives no lever.

A definition brings in a new quantity as a combination of others. It cannot be false. It can
only be read in a sense its author did not mean, and it is checked by reading the author's
where-clause.

A model assumption is a claim, adopted by the author, about how a body or a population
behaves. It could be false. It is checked against measurements, and it holds only as far as
they support it.

A fitted equation has a form chosen by its author and constants estimated from one set of
measurements. It is checked by asking whom it was fitted on, and over what range. It holds for
people like those, over that range.

One printed equation can mix kinds: a model assumption with a fitted constant, or a definition
rearranged and then used to estimate a quantity from inputs that are themselves fitted or
adopted. Each part is then checked by its own kind.

A notebook entry records one equation so that it can be used and checked later. It holds six
things.

1. The equation as printed.
2. Each symbol in words, with its unit.
3. The whole equation said as one sentence.
4. Its kind.
5. What it assumes, or whom it was fitted on.
6. The paper, with the equation's number or page.

**In plain terms.** Equations in papers look alike: letters, an equals sign, more letters. They are not alike. Some
are true whatever happens. Some are true because someone decided what a word means. Some are
guesses about how bodies behave. Some are lines drawn through somebody else's measurements.

Which kind you are looking at decides what you check. For the first, check that both sides are
counted the same way. For the second, check you mean what the author meant. For the third, ask
for the evidence. For the fourth, ask whose measurements, and whether your patient is like them.

So keep a notebook. For each equation you meet, write down six things.

The equation. What each letter means, with its unit. The equation said as a sentence. Its kind.
What it assumes, or whose data it came from. And where you found it.

**Illustration.** Start with an equation that went wrong for Indian adults, and find out why by sorting it.

Three United Nations bodies wrote a report together in 2004: the Food and Agriculture
Organization (FAO), the World Health Organization and the United Nations University (UNU). The
report, FAO/WHO/UNU 2004, prints equations for basal metabolic rate (BMR), the energy a body
spends at complete rest. They come from Schofield,
and the consultation "decided to retain" them. For men aged 18 to 30, the equation in kcal a
day says: BMR is 15.057 times body weight in kg, plus 692.2.

```working
BMR = 15.057 × weight + 692.2
```

Try it on a made-up man of 60 kg.

```working
15.057 times 60 plus 692.2 = 1595.62
```

About 1,596 kcal a day.

Now sort it. It is not an identity: nothing forces a body's BMR to be this number. It is not
a definition: BMR is measured, lying down after 10 to 12 hours without food, and this
equation stands in for the measurement. It is a fitted equation. Its form, a straight line in weight, was chosen.
Its two numbers were estimated from measured men, 2,879 of them in this age band, the table
says.

So ask the fitted equation's question: whom was it fitted on? ICMR-NIN, the Indian Council of
Medical Research's National Institute of Nutrition (NIN), answers it for you. The FAO/WHO/UNU
equations "can overestimate the BMR by 10 -12%, because the FAO/WHO/UNU data set included
young and muscular subjects." For Indian adults, ICMR-NIN lowered the BMR these equations give,
by 5% in its earlier report and by another 5% in 2020.

Nothing was wrong with the line on its own data. It was carried onto people unlike the ones it
was drawn through. Sorting the equation is what told you which question to ask.

Now write the entry. Six parts.

- The equation as printed: BMR in kcal a day = 15.057kg + 692.2, men aged 18 to 30, where the
  table's "kg" stands for body weight in kg.
- Each symbol with its unit: BMR, basal metabolic rate, in kcal a day. Weight in kg. 15.057,
  in kcal a day for each kg. 692.2, in kcal a day. Check the units: kcal a day per kg times kg
  is kcal a day, the same as the 692.2 it is added to.
- In words: for men aged 18 to 30, BMR is about 15 kcal a day for each kilogram, plus about
  692 kcal a day.
- Kind: fitted.
- Assumes, or fitted on: Schofield's measured men, 2,879 in this band. ICMR-NIN finds these
  equations can run 10 to 12% high for Indians.
- Source: FAO/WHO/UNU 2004, chapter 5, Table 5.2.

A second entry shows an equation of two kinds at once. Polidori and colleagues write their
Equation 4 for how intake answers weight loss (Polidori 2016). In words: the change in energy
intake at time t is the change in body weight at time t, times kP, with the sign turned round.

```working
ΔEI(t) = −kP × ΔBW(t)
```

- Symbols: the change in intake from the start, ΔEI(t), is in kcal a day. The change in body
  weight (BW) from the start, ΔBW(t), is in kg. The constant kP is "the feedback strength". It
  is greater than zero, in kcal a day per kg. The minus sign makes intake rise when weight falls.
- In words: for every kilogram lost, intake rises by kP kcal a day.
- Kind: a model assumption with one fitted constant. The straight-line form is the assumption.
  The authors write that they "do not yet know whether the simple proportional controller
  represented by Equation 4 is valid for a range of weight losses." The constant kP was fitted
  to the trial's group means, and came out at about 100 kcal a day per kg.
- Assumes: intake answers weight in proportion. Fitted on group means, not on any one person.
- Source: Polidori and colleagues 2016, Methods, Equation 4.

**Where this picture breaks.** The 60 kg man is made up. The Schofield line gives a group's expected BMR, not any one man's.
ICMR-NIN's finding is about groups of Indian adults. It is not a correction to apply to a
single patient's measured BMR.

Sorting is not always this clean. Take the Atwater factors of `S02-R1-C10`: 4, 9 and 4 kcal a
gram. They are averages of measurements, rounded, and then adopted by agreement. So they are
fitted and then fixed by a body. Record both kinds when an equation has both.

**Must know points for you.**

- Say an equation's kind before you use it, because the check differs. For an identity, check that both sides are counted across the same boundary and interval. For a definition, read the where-clause. For a model assumption, ask for the evidence. For a fitted equation, ask whom it was fitted on.
- An identity cannot tell you what to change. Energy intake minus expenditure equals the change in stores whatever caused either one. When someone offers the identity as a reason for an instruction, ask which model assumption they have added to it.
- ICMR-NIN finds that the FAO/WHO/UNU equations for BMR can run 10 to 12% high for Indians. The data behind them came from young, muscular people. Before you estimate an Indian patient's needs from those equations, use ICMR-NIN's figures for Indian adults, which build in a reduction.
- An energy requirement is BMR times the physical activity level (PAL). That is a definition used to make an estimate, and the estimate moves when its inputs move. ICMR-NIN's 2020 note cut the sedentary figure from 1.53 to 1.40. At the same BMR, that alone lowers the estimate by about 8.5%. Quote such a table with the year of its inputs.
- A fitted equation holds for people like those it was fitted on, over the range it was fitted. Outside that, find an equation fitted on people like yours, or measure. If you can do neither, say that you used the equation on people unlike those it was fitted on.
- A constant fitted to a group's means is not any one person's. Polidori's about 100 kcal a day per kg was fitted to group means. Do not tell a patient their appetite will rise by exactly that much.
- A notebook entry without its kind and its assumptions is not finished. When you copy an equation from a typeset image, have a second reader check it symbol by symbol. No search can find a symbol you copied wrongly.
- Teach a trainee that a definition cannot be confirmed by data. A study that "confirms" that PAL equals total energy expenditure (TEE) divided by BMR has confirmed only its own arithmetic.

**Exercise 1** (build). Start the notebook this book has been building towards: ten equations from papers you have
read, each with a full six-part entry.

Here are ten candidates from papers this book has quoted. Choose any ten, from here or from
your own reading. For each, write the six parts.

1. The energy balance equation, ES = EI − EO (Hall and colleagues 2012, Question 1).
2. PAL = TEE / BMR (FAO/WHO/UNU 2004, glossary and chapter 5).
3. TEE = BMR × PAL (FAO/WHO/UNU 2004, chapter 5; ICMR-NIN 2020).
4. One row of Table 5.2, such as BMR = 14.818 × weight + 486.6 for women aged 18 to 30 (FAO/WHO/UNU 2004).
5. Energy in kcal = 4 × protein + 9 × fat + 4 × carbohydrate, each in grams (FAO Food and Nutrition Paper 77, §3.5.1).
6. W(t) = W0 − ΔEB × t / 3500 (Thomas and colleagues 2013, Methods).
7. Equation 1 of Polidori and colleagues 2016, the change in intake from weights.
8. Equation 4 of Polidori and colleagues 2016, proportional control.
9. Equation 5 of Polidori and colleagues 2016, which adds an integral term.
10. The rule of thumb (Hall and colleagues 2012, Question 3). Eventual weight change in pounds = the permanent change in intake in kcal a day, divided by 10.

Two more are worth adding if you can get them. One is Equations 1 and 2 of Chow and Hall 2008.
The other is Hall's 2008 equation for the energy density of weight loss. Both are printed as
images. Copy them symbol by symbol and have someone check your copy.

**Exercise 2** (teaching). A state health secretary asks why the national energy requirement for sedentary adults fell
in 2020, when nobody's body changed. One page, answer first, no methods section.

