# B5 · Concentration units: mg/dL, mmol/L, and converting between them

**Definition.** A concentration is an amount of something held in a volume of something else. Two kinds of
amount are in use in laboratory work, and they are different kinds of quantity.

A mass concentration is a mass in a volume. Milligrams per decilitre, written mg/dL, is a
mass concentration. The prefix milli means one thousandth and the prefix deci means one
tenth, so a decilitre is a tenth of a litre and one litre holds ten decilitres.

An amount-of-substance concentration is an amount of substance in a volume. Millimoles per
litre, written mmol/L, is an amount-of-substance concentration. The mole is the SI base
unit of amount of substance, and it counts elementary entities rather than weighing them. A
millimole is one thousandth of a mole.

The molar mass of a substance is the mass of one mole of it. The capital letter M stands
for the molar mass, and it is measured in grams per mole, written g/mol. Molar mass is a
property of the substance and differs from one substance to another.

Converting a mass concentration into an amount-of-substance concentration therefore
requires the identity of the substance. The small letter c stands for a value in mg/dL, and
the same quantity in mmol/L is c times 10, divided by M. The factor of 10 carries decilitres
to litres and the division by M carries milligrams to millimoles.

A molar mass is measured and computed, not decided, so it can be revised. The molecular
weight used here for D-glucose is the value computed for PubChem release 2025.09.15. A
revision of the standard atomic weights, or a correction to that record, would change it,
and such a change would fall in the last digits rather than the first.


**In plain terms.** A laboratory number has two parts, like every other measurement: a number and a unit. Here
the unit is the part that does the work.

Milligrams per decilitre, written mg/dL, is a weight of something in a volume of blood. Milli
means a thousandth and deci means a tenth, so a decilitre is a tenth of a litre. A litre
holds ten decilitres. What mg/dL counts is weight.

Millimoles per litre, written mmol/L, counts something else. A mole is a fixed count of
things, molecules here. It is one of the seven SI base units you met a few sections back. A
millimole is a thousandth of a mole. What mmol/L counts is how many of those things there are.

Those are two different kinds of quantity. One says how heavy. The other says how many.

Now the bridge, and this is the whole section. To get from how heavy to how many, you have to
know how heavy one mole is. That weight is called the molar mass, and it is written in grams
per mole, g/mol.

Here is the trap. The molar mass belongs to the substance. Glucose has one. Cholesterol has a
different one. So there is no single conversion factor between mg/dL and mmol/L, and there
never can be. A factor that is right for glucose is wrong for cholesterol, and the wrong
answer looks exactly like a right one.

So the job has four steps.

1. Find out what the substance is. Read the row label, not the number.
2. Get its molar mass in grams per mole. Look it up. Do not guess it.
3. Multiply the mg/dL figure by ten, because a litre holds ten decilitres. That gives
   milligrams per litre.
4. Divide by the molar mass. That gives millimoles per litre.

To go the other way, run the same steps backwards. Multiply by the molar mass, then divide by
ten.

Step 2 is where the work is, and it is the step people skip.

One last thing, and it comes from the section on significant figures. A conversion renames an
amount. It does not make the amount better known. A laboratory value of 100 does not turn
into 5.550621670 because a calculator says so.


**Illustration.** Start with the sum you cannot do, because that is the one this section is really about.

A report in front of you gives two numbers, both in mg/dL. One is glucose. One is total
cholesterol. A paper you want to read alongside it gives both in mmol/L. So you have two
conversions to do, and they look like the same job done twice.

Do the glucose one first.

Open PubChem, the free compound database run by the United States National Library of
Medicine, and search for D-glucose. The record is compound 5793. The page gives the
molecular formula as C6H12O6 and the molecular weight as 180.16 g/mol. The second figure is
what you came for. One mole of glucose weighs 180.16 grams.

Take a glucose value of 100 mg/dL and work it a line at a time.

```working
    100 mg in every decilitre
    a litre holds ten decilitres
    100 times 10 = 1,000
    so 1,000 mg in every litre
    one mole weighs 180.16 grams, so one millimole weighs 180.16 milligrams
    1,000 divided by 180.16 = 5.5506
    so 5.5506 mmol in every litre
```

Now cut the digits, the way the section on significant figures asks. The laboratory gave you
100, to the nearest whole milligram. That is three digits you can stand behind. Write 5.55
mmol/L. The calculator's 5.550621670 is a claim about the laboratory's work, not about
yours.

Now the cholesterol, and watch it stop.

Go back to PubChem and search for cholesterol. The record is compound 5997. The page gives
the molecular formula as C27H46O. You now know the substance exactly, atom by atom.

And you still cannot do the sum.

The molecular weight was not captured when that page was read for this course. It sat below
the fold on the screen, and this book writes down only what somebody actually saw. So the
course can hand you glucose's molar mass and cannot hand you cholesterol's.

Look at what you are holding. You know the method. You know the substance. You know its
formula. None of that is enough. The one number the method needs is a measured property of
cholesterol, and nothing you know produces it.

Here is what you must not do. Do not add up the atomic weights of 27 carbons, 46 hydrogens
and one oxygen out of your head. Do not reuse glucose's divisor because both numbers came
off the same report. Both moves hand you a number, and a number is exactly what nobody
checking you will question.

Here is what you do instead. Write down that the conversion is pending. Name what you need,
which is cholesterol's molar mass in grams per mole. Go and read it off PubChem compound
5997. Then come back and run the same four steps you ran for glucose.

That is a five-minute job in a browser. Writing down a number you did not look up is a job
that never ends, because you can never take it back.


**Where this picture breaks.** The 180.16 g/mol belongs to D-glucose and to nothing else. Every line of the glucose working
above rests on it. The working carries over to another substance only once that substance's
own molar mass is in your hand.

The method itself holds for one pure substance dissolved in a volume. A figure that lumps
several substances into a single total has no single molar mass, so there is nothing for the
method to divide by.

And the conversion renames an amount. It cannot improve it. Every error in the value the
laboratory handed you is still there afterwards, carried across untouched. The extra digits
a calculator produces are evidence of nothing.


**Must know points for you.**

- There is no single number that turns mg/dL into mmol/L. The factor belongs to the substance, not to the pair of units. Dividing by 18 is a glucose move and it is wrong on everything else. The answer it gives looks exactly as reasonable as a right one.
- One mole of D-glucose weighs 180.16 grams, as PubChem's record for compound 5793 gives it. That one figure moves a glucose value between mg/dL and mmol/L in either direction. Quote it by name when somebody asks where your conversion came from.
- Convert in four steps and say them out loud. Name the substance. Get its molar mass in grams per mole. Multiply the mg/dL figure by ten, because a litre holds ten decilitres. Divide by the molar mass, and the answer is in mmol/L.
- Two laboratory numbers in the same unit are not two numbers about the same thing. Nothing in mg/dL or mmol/L names a substance. Read the row label before you convert, and carry the substance with every converted value you hand on.
- This conversion needs one substance with one molar mass. A figure that is a mixture reported as a single total has no molar mass, so it cannot be put into mmol/L at all. Meeting such a conversion in a paper means somebody chose a molar mass for a mixture. Ask which one, and ask why.
- A conversion never adds a digit. A value the laboratory gave you as 100 mg/dL comes out as 5.55 mmol/L, not as 5.550621670 mmol/L. Writing the long form claims a laboratory did work it never did.
- When you do not hold the molar mass, say so and stop. Saying you need to look up the molar mass for that substance costs you one sentence in a committee. Quoting a converted value you cannot source costs you everything you say after it.

**Exercise 1** (critique). Here is a line from a draft laboratory protocol.

> To convert any laboratory value from mg/dL to mmol/L, divide by 18.

Say what is wrong with it, and write the sentence you would put in its place.


**Exercise 2** (teaching). A journalist has three minutes. They have two papers open. One reports a blood sugar figure
as 92 and the other reports it as 5.1, and they want to know which paper is right.

Explain it without jargon. Give one quotable sentence, and say how confident you are.


**1.** A litre holds ten decilitres. Rewrite each of these.

```working
    5 per decilitre, as a figure per litre
    0.7 per decilitre, as a figure per litre
    120 per litre, as a figure per decilitre
    96 per litre, as a figure per decilitre
```


**2.** Work each of these out and write the answer to four digits.

```working
    1,000 divided by 180.16
    920 divided by 180.16
    2,500 divided by 180.16
```


**3.** Take each number below, multiply it by ten, then divide the result by 180.16. Write each
answer to four digits.

```working
    72      110      45
```


**4.** Now reverse the order. Take each number below, multiply it by 180.16, then divide the result
by ten.

```working
    4      6.5      9
```


**5.** A laboratory reports a glucose value of 92 mg/dL. PubChem gives the molecular weight of
D-glucose as 180.16 g/mol.

Give that value in mmol/L, keep the unit on the answer, and say how many digits you would
write down.


**6.** A paper gives a glucose value as 7.2 mmol/L and your form needs it in mg/dL. PubChem gives
the molecular weight of D-glucose as 180.16 g/mol.

Convert it, keep the unit on the answer, and say how many digits you would write down.


**7.** People often say that a glucose value in mg/dL becomes mmol/L if you divide it by 18.
PubChem gives the molecular weight of D-glucose as 180.16 g/mol.

Work out the exact divisor. Then convert a glucose value of 180 mg/dL twice, once with the
exact divisor and once with 18. Say how far apart the two answers are, as a share of the
answer.


**8.** A report gives a glucose value of 110 mg/dL and a total cholesterol value of 200 mg/dL.
Somebody asks you for both in mmol/L. PubChem gives the molecular weight of D-glucose as
180.16 g/mol, and its record for cholesterol gives the molecular formula as C27H46O.

Do what can be done. Then say plainly what cannot be done, and what you would do about it.


**9.** Here is a worked answer. Find the step that broke.

```working
    total cholesterol is 200 mg/dL
    to turn a mg/dL figure into mmol/L you divide by 18
    200 divided by 18 = 11.1
    so the cholesterol is 11.1 mmol/L
```


**10.** Here is a worked answer. Find the step that broke.

```working
    a glucose value is 90 mg/dL
    the molecular weight of D-glucose is 180.16 g/mol
    90 divided by 180.16 = 0.4996
    so the glucose is 0.4996 mmol/L
```


**11.** Here is a worked answer. Every line of arithmetic in it is correct. Find the step that broke
anyway.

```working
    a glucose value is 100 mg/dL
    the molecular weight of D-glucose is 180.16 g/mol
    100 times 10 = 1,000
    1,000 divided by 180.16 = 5.550621670
    so the glucose is 5.550621670 mmol/L
```


**12.** A colleague sends you this line about a planned pooled analysis.

> Their glucose figures are all in mmol/L and ours are all in mg/dL. The two sets cannot be
> pooled, so we would have to sample our participants again.

Decide what to compute, compute it, and say what your answer does not establish.


**13.** In a meeting somebody says this.

> The trial reports mean total cholesterol as 4.5 mmol/L. Our audit reports it as 210 mg/dL.
> Those are the same figure, near enough, so the two groups are comparable on this.

Decide what to compute, compute it, and say what your answer does not establish.

