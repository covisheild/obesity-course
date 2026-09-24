# S02-R1-C01 · Reading the symbols in a methods section

**Definition.** A symbol in an equation stands for a quantity, and the paper fixes which quantity in words:
in a clause beginning "where" after the equation, or in the sentences around it. Until that
clause is found, the symbol has no meaning that can be relied on.

A subscript is a small letter or number set low after a symbol, and it is part of the
symbol's name. It labels which of several related quantities is meant: E with I for intake,
O for output, S for storage. Or it counts through a list: body weight (BW) with i is the
weight in interval i, and BW with 0 is the baseline value. A subscript never multiplies.

A Greek letter is a symbol like any other and is read by its name: ρ (rho), Δ (capital
delta), δ (small delta), ε (epsilon), Σ (capital sigma). A capital Δ written before a symbol
means "the change in" that quantity and is not a quantity of its own.

Capital sigma, Σ, with a counter and its first and last values attached, means: put each
value of the counter in turn into the expression after it, and add the results. The counter
only keeps track of the terms; any letter may be used for it.

Every term added to or subtracted from another, and each side of an equals sign, carries the
same unit. So the unit of a symbol the paper does not state can be worked out from the terms
beside it. A term whose unit differs from its neighbours signals a misread symbol, or a
conversion the equation does not show.

**In plain terms.** An equation in a paper is a sentence written in symbols. Each symbol stands for a quantity, and
the paper says which one, in words, somewhere near the equation. Often that sentence starts
with the word "where". Find it before you read the equation. Until you have found it, you are
guessing.

Book 0 gave you most of the tools. A letter stands for a number (`B0-R0-C15`). Two symbols
side by side are multiplied. f(x) is the output of a rule called f, not f times x
(`B0-R0-C18`). The triangle Δ, delta, means "the change in" (`B0-R0-C34`).

And dy/dx, "dee y by dee x", is the rate at an instant (`B0-R0-C21`). Methods sections add
four more things.

**Subscripts.** A subscript is a small letter or number set low after a symbol. It is part of
the symbol's name, and it does one of two jobs.

It can label. Hall and colleagues write E for energy and set a small I, O or S after it. E with
I is energy intake (EI). E with O is energy output (EO). E with S is energy stored (ES). The
small letter says which energy.

This book writes these on the line, as EI and ES. For output it writes energy expenditure
(EE), the name Book 1 used. EE and Hall's EO are the same quantity.

Or it can count. BW with a small i after it is the body weight in interval number i. BW with a
small 0 is the weight at the start, the baseline. When a subscript counts, this book writes it
after an underscore, BW_i, so you can see where the name stops.

Here is the one exception to Book 0's rule. Side by side means multiply, except for a
subscript. BW_0 is the starting weight. It is not BW times zero.

**Greek letters.** They are letters like x and y, with names. Say the name out loud as you
read. These are the ones the papers in this book use.

```table
| letter | its name | say it | what one paper in this book uses it for |
| ρ | rho | "roe" | an energy density, energy per kilogram |
| Δ | capital delta | "delta" | the change in whatever follows it |
| δ | small delta | "delta" | a physical activity quantity (Polidori) |
| ε | epsilon | "ep-sih-lon" | how expenditure depends on weight (Polidori) |
| Σ | capital sigma | "sigma" | add up |
```

The last column is not fixed. Each paper decides what its letters mean, in its own "where"
clause.

**Sigma.** Σ means "add up". It comes with a counter, usually i, and the counter's first and
last values. On the page the first value sits under the Σ and the last sits over it. On one
line this book writes them in square brackets after it. Say the sum in words, then write
it out.

```working
    Σ[i = 1 to 4] 2i
    = the sum, for i from 1 to 4, of 2 times i
    = 2 times 1 plus 2 times 2 plus 2 times 3 plus 2 times 4
    = 2 plus 4 plus 6 plus 8
    = 20
```

The counter only keeps track of which term you are on. It does not appear in the answer.

**Units.** Every term that is added or subtracted must carry the same unit, and so must the
two sides of an equals sign (`B0-R0-C11`). Use that to find the unit of a symbol the paper
never states. If a line adds kilocalories a day to kilograms, you have misread a symbol, or a
conversion is hidden somewhere.

**Illustration.** Start with a sentence that trips a careful reader. Hall and colleagues (2012) wrote a
consensus statement on energy balance — a text a panel of experts agreed on together. In it
they write the energy balance equation like this.

```working
    ES = EI minus EO
```

Here is a first reading. ES is the energy stored in the body. The same paper puts the energy
held in a lean adult's fat cells at about 130,000 kcal. So ES is about 130,000 kcal, and the
equation says intake minus output is about 130,000 kcal.

Run the unit check before you believe that. The paragraph says what the terms are measured
in: "All of these terms are expressed as energy per unit of time." So EI and EO are in
kilocalories a day. Subtract one from the other and you get kilocalories a day.

The left side has to match. So ES here cannot be the 130,000 kcal, which has no time in its
unit. It must be kilocalories a day as well.

Now read the next sentences. The paper says it in words: "ES is the rate of change in the
body's macronutrient stores." Two sentences earlier, the same two letters named the stores
themselves. The unit check caught the switch before the words did.

This book keeps the two apart. ES is the store, in kilocalories. Its rate of change is
dES/dt, said "dee ES by dee t". That is the rate of change of ES with respect to t, with t
in days.
In this book's letters Hall's equation says this. The rate of change of stored energy equals
energy intake minus energy expenditure.

```working
    dES/dt = EI minus EE
```

EO has become EE. Hall calls expenditure "output". Book 1 called it expenditure. Two papers,
two letters, one quantity, and the "where" clause is what tells you so.

Now a full equation from a methods section. Polidori and colleagues (2016) worked out how
much people's eating changed during a trial of a drug. The drug raises urinary glucose
excretion (UGE): the body loses glucose in the urine. Here is their Equation 1. Subscripts are printed after an underscore. Symbols
side by side multiply, except for subscripts.

```working
    ΔEI_i = ρ (dBW_i/dt) + ε(BW_i − BW_0) + (Δδ/(1 − β)) BW_0 + UGE
```

Do not read it left to right. Make a table with one row for each symbol. Fill the "words"
column from the paper's own sentences. Leave a cell empty rather than guess.

The words are in the Methods. "We calculated the changes in energy intake, ΔEI, for each
subject". One input was "the change of body weight versus baseline over each interval,
(BWi − BW0)". The other was "the rate of change of body weight over each interval, dBWi/dt".

Then "The model parameter ρ was the effective energy density associated with the body weight
change". A parameter is a number the model holds fixed while it runs. Then "ε defined how energy expenditure depends on body weight". And "Δδ represents
changes in physical activity".

UGE is not spelled out beside the equation. That is common. When a short form is not spelled
out, search the paper for words that fit its letters. Here the abstract has them: a drug
"that increases urinary glucose excretion".

β is harder. Search the Methods for the sentence that says what β is. If you cannot find
one, write "not found" in its row.

Now the units. Start with the ones you know. The results give changes in intake in
kilocalories a day, so ΔEI_i is in kcal a day. Body weight is in kilograms. Time between
weighings was counted in days, so dBW_i/dt is in kilograms a day.

Every term on the right must also be in kcal a day. Work out each unknown unit from that.

```working
    ρ times (kg a day) = kcal a day, so ρ is in kcal per kg
    ε times (kg) = kcal a day, so ε is in kcal a day per kg
    1 minus β: a bare 1 can only lose a bare number, so β has no unit
    Δδ times (kg) = kcal a day, so Δδ is in kcal a day per kg
```

The first row agrees with the words. An energy density is energy per kilogram, and the unit
check gave kcal per kg.

```table
| symbol | say it | the paper's words | unit |
| ΔEI_i | delta E I sub i | change in energy intake, interval i | kcal a day |
| BW_i | B W sub i | body weight, interval i | kg |
| BW_0 | B W sub zero | body weight at baseline | kg |
| dBW_i/dt | dee B W sub i by dee t | rate of change of body weight, interval i | kg a day |
| ρ | rho | effective energy density of the weight change | kcal per kg (worked out) |
| ε | epsilon | how expenditure depends on weight | kcal a day per kg (worked out) |
| Δδ | delta delta | change in physical activity | kcal a day per kg (worked out) |
| β | beta | not found | none (worked out) |
| UGE | U G E | urinary glucose excretion | must be kcal a day |
```

Look at the last row. Elsewhere the paper says urinary glucose excretion "was assumed to be
~90 g/day". That is grams a day. Grams a day cannot be added to kcal a day. So somewhere the
authors turned grams of glucose into energy, and the equation does not show it. Before you
put 90 into this equation, find that conversion.

Look at Δδ too. The capital delta and the small delta are two different symbols. Read it as
"the change in δ", where δ is the physical activity quantity.

Last, sigma on a real stretch of days. Book 1 (`S01-R1-C05`) worked through a made-up week of
intake and expenditure. Here are that week's seven daily changes, intake minus expenditure,
in megajoules.

```table
day i  EI_i minus EE_i (MJ)
1      0.5
2      -0.3
3      1.1
4      -1.0
5      0.9
6      0
7      1.6
```

Book 1 added them in a line. A paper would write the same sum with sigma. Say it first: the
sum, for i from 1 to 7, of EI_i minus EE_i.

```working
    Σ[i = 1 to 7] (EI_i − EE_i)
    = (EI_1 − EE_1) + (EI_2 − EE_2) + ... + (EI_7 − EE_7)
    0.5 plus -0.3 plus 1.1 plus -1.0 plus 0.9 plus 0 plus 1.6 = 2.8
```

Stores rose by 2.8 megajoules over the week, as Book 1 found.

Book 1 then checked it the other way. It added the seven intakes, added the seven
expenditures, and subtracted once. In sigma that check reads as follows.

```working
    Σ[i = 1 to 7] (EI_i − EE_i) = Σ[i = 1 to 7] EI_i − Σ[i = 1 to 7] EE_i
```

The two ways agree for any list of numbers. Adding is done in any order. So all the intakes
can be added first, and then all the expenditures taken away.

Now go the other way, from a written-out sum back to sigma. Take 3 plus 6 plus 9 plus 12.
Each term is 3 times its place in the list, so it is Σ[i = 1 to 4] 3i. Check it by writing it
out again.

```working
    3 times 1 plus 3 times 2 plus 3 times 3 plus 3 times 4 = 30
    3 plus 6 plus 9 plus 12 = 30
```

**Where this picture breaks.** The unit check shows that ES must be a rate in Hall's equation. It cannot show that the
equation is right, because a wrong number in front of a term changes no unit (`B0-R0-C11`).

Other papers use ES for the store itself. The unit settles it only inside one paper, and only
once you have found what the other terms are measured in.

The table tells you what each symbol denotes and what unit it must carry. It does not tell you
that the model is a good description of anyone. Polidori's own Methods call Equation 1 "a
linearization" of a larger model. That is a straight-line stand-in for it, close only for
small changes in weight. The authors also ran it on the group mean only.

A unit worked out from the terms beside it is only as sure as the units you started from. If
you misread ΔEI's unit, every unit worked out from it is wrong in the same way.

The week's numbers are made up, in Book 1, to show the arithmetic. A sum over days is exact
only for quantities counted day by day.

Sigma adds a list of separate terms. A quantity that changes smoothly inside each day is added
up another way, with the integral sign that Book 0 named in `B0-R0-C22`.

**Figure.** Σ[i = 1 to 7] (EI_i − EE_i) drawn as its seven terms, one point a day, in megajoules. The points below zero, days 2 and 4, count as minus when you add, and day 6 adds nothing. The seven terms add to 2.8 megajoules, the change in stores over the week.

*What the figure shows:* Seven labelled points for days 1 to 7 at 0.5, -0.3, 1.1, -1.0, 0.9, 0 and 1.6 megajoules: two below zero on days 2 and 4, one at zero on day 6, and the highest, 1.6, on day 7.

**Must know points for you.**

- Find the "where" clause before you read an equation. Then write a table: each symbol, its words from the paper, and its unit. Leave a row empty rather than guess, and mark it "not found".
- One paper can use the same letters for two things. Hall's ES names the stores in one sentence and their rate of change in the next. When the words are unclear, let the unit decide.
- A subscript is part of a name and never multiplies. BW_0 is the starting weight, not BW times zero. Read it as "B W sub zero", out loud, until the habit holds.
- Work out a unit the paper does not print from the terms beside it. Whatever is subtracted from a bare 1 has no unit. Whatever multiplies kilograms to give kilocalories a day is in kilocalories a day per kilogram.
- A figure quoted in the text in one unit may enter the equation in another. Polidori's glucose loss is quoted in grams a day and sits in an equation of kilocalories a day. Find the conversion before you put a number in.
- Matching units show that an equation is not malformed. They never show it is right, and they cannot tell apart two quantities with the same unit. Hall's ρF and Polidori's ρ are both energy per kilogram, and they are different quantities from different models.
- Teach a trainee to read Σ aloud as "the sum, for i from 1 to n, of". Then have them write out the first two terms and the last. A sum they have written out is a sum they can check.

**Exercise 1** (interpretation). Polidori and colleagues (2016) model the change in eating after weight loss with this
equation, their Equation 4.

```working
    ΔEI(t) = − k_P × ΔBW(t)
```

The sentence after it reads: "where the parameter kP>0 quantifies the feedback strength".
Their abstract reports eating "above baseline by ~100 kcal/day per kg of lost weight".

Write the symbol table for Equation 4: each symbol, how you say it, what it denotes, and its
unit. Then say in one sentence what the minus sign does, and what number k_P took.

**1.** Write this sum out term by term, then work it out.

```working
    Σ[i = 1 to 4] 3i
```

**2.** Write this sum in sigma notation.

```working
    2 plus 4 plus 6 plus 8 plus 10
```

**3.** Four values are x_1 = 4, x_2 = 7, x_3 = 1 and x_4 = 8.

Work out Σ[i = 1 to 4] x_i, then Σ[i = 2 to 3] x_i, then Σ[i = 1 to 4] 5x_i.

**4.** An equation reads A = B + C × D. B is in kilocalories a day. D is in kilograms.

Work out the unit of A and the unit of C.

**5.** Three United Nations bodies wrote a report on human energy requirements (2004). They are the
Food and Agriculture Organization (FAO), the World Health Organization (WHO) and the United
Nations University (UNU). The report divides total energy expenditure (TEE) by basal
metabolic rate (BMR), both in megajoules a day. The result is the physical activity level
(PAL).

```working
    PAL = TEE/BMR
```

The same passage gives a man with a PAL of 1.75 and a mean BMR of 7.10 MJ/day.

Work out his TEE. Then give the unit of PAL, and say why it has that unit.

**6.** Hall (2008) writes: "The energy density of the body fat mass change, ρF = 39.5 MJ/kg". He
uses ΔF for the change in body fat.

Say both symbols in words. Then take ΔF = -3 kg, a made-up figure. Work out ρF times ΔF, with
its unit, and say what the sign means.

**7.** Polidori and colleagues (2016) define the length of each interval. They write "The interval
length was t = (N−1)*T". Then they say what the letters are. "N = 2 was the number of body
weight measurements per interval". And "T = 52 was the number of days between
measurements".

Say what t, N and T each stand for, with their units. Work out t. Then work out what t would
be with three measurements per interval, the same distance apart.

**8.** Here is a worked answer. Find the step that broke.

```working
    Equation 1 of Polidori and colleagues ends in "+ UGE"
    UGE was assumed to be about 90 g/day
    so the last term adds 90 to the change in energy intake
    the other terms come to 250 kcal a day for this interval
    250 plus 90 = 340, so ΔEI is 340 kcal a day
```

The 250 is made up for this problem.

**9.** Here is a worked answer. Find the step that broke.

```working
    one term of an equation is ε(BW_i − BW_0)
    two symbols side by side are multiplied
    so BW_0 is BW times 0, which is 0
    so the term is ε times BW_i
    with ε = 20 and BW_i = 80, the term is 1600
```

Both numbers are made up for this problem.

**10.** A colleague reads Hall and colleagues' (2012) equation and says this.

> ES = EI − EO. The paper also says a lean adult's fat cells hold about 130,000 kcal. So a
> lean adult has eaten 130,000 kcal more than they have spent.

Decide what to check, check it, and say what your answer does not establish.

**11.** A trainee's notes on two papers say this.

> Hall (2008) gives ρ = 39.5 MJ/kg. Polidori and colleagues (2016) have a ρ in Equation 1.
> So in their model each kilogram of weight change carries 39.5 MJ. That is about 9,441
> kcal.

Decide what to check, check it, and say what your answer does not establish.

