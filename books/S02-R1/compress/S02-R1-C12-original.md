# S02-R1-C12 · A column that is a weighted sum of other columns

**Definition.** Take a table whose rows are cases and whose columns are variables, as `S02-R1-C11` sets one
up. Read each column as a vector, with one entry for each row.

A column y is a weighted sum of the columns a1, a2, ..., ak when there are fixed numbers
w1, w2, ..., wk, called the weights, that make the following true on every row. The entry of
y equals w1 times the entry of a1, plus w2 times the entry of a2, and so on up to wk times
the entry of ak. The same weights must hold on every row. In the
notation of `S02-R1-C11`, this is y = Xb: X is the matrix whose columns are a1 to ak, and b is
the vector of weights (w1, w2, ..., wk). Textbooks call y a linear combination of the columns
of X.

A column of 1s counts as a column. So a column y that equals 2 times a, plus 5, on every row
is a weighted sum of a and the column of 1s, with weights 2 and 5.

Such a column is redundant: once the other columns are known, it says nothing about any row
that they did not already say.

The test for it treats the weights as unknowns. Each row gives one equation in them. Find the
weights from as many rows as there are weights. With two weights, that is two equations in
two unknowns, solved as in `B0-R0-C17`. With more, look for rows in which every column but
one is zero, because each such row gives one weight on its own.

Then put the weights into every other row. If every row holds, y is a weighted sum of those
columns. If the equations have no solution, or a single leftover row fails, it is not. If the
rows you picked repeat each other, so that their equations have infinitely many solutions,
pick another row.

When a table holds a column beside the columns it is a weighted sum of, the table no longer
fixes the weights on a weighted sum of all of them together. Weight can be moved from that
column onto its parts, in proportion, in infinitely many ways, and every row's total stays the
same. This is the case in `B0-R0-C17` of two equations that repeat each other and so have
infinitely many solutions.

A food table whose energy was worked out from the grams with the Atwater general factors of
`B0-R0-C32` has such a column. Its energy, in kilocalories, is the weighted sum of protein,
fat and carbohydrate, in grams, with weights 4, 9 and 4.

The test finds weighted sums and nothing else. A column made from others by multiplying them
together is fixed by them and still fails it.

How many of a table's columns are not redundant is its rank. A column that is nearly, but not
exactly, a weighted sum of others is the problem called collinearity. Both belong to the next
rung of this subject, and this section computes neither.

**In plain terms.** Picture an order sheet at a tiffin stall. Each row is one order. One column counts the idlis,
one counts the dosas, and the last column is the amount paid.

Suppose an idli costs 20 rupees and a dosa costs 50. Then on every row the amount paid is 20
times the idlis plus 50 times the dosas. The prices are the weights. The amount column adds
nothing: cover it with your hand and you can still write it back in.

To find out whether a column is like that, treat the prices as unknowns. Two orders give you
two equations, and you solve them as in Book 0. Then check the prices on every other order. If
one order does not fit, perhaps because of a discount, the column is not a fixed weighted sum.

Now try asking, "Among orders with the same idlis and dosas, which paid more?" There is no such
pair of orders to compare. The question looks sensible and asks for something the sheet cannot
hold.

**Illustration.** Here is a question that sounds reasonable and has no answer. "Among foods with the same
protein, fat and carbohydrate, what goes with an extra 100 kilocalories?" Try to answer it
from this table.

The table is made up, with round numbers chosen so the arithmetic shows. Each row is an item,
and each column is grams in 100 grams of it, except energy, which is kilocalories (kcal) in
100 grams.

```table
item  protein (g)  fat (g)  carbohydrate (g)  energy (kcal)
1     0            100      0                 900
2     0            0        100               400
3     10           20       60                460
4     25           5        50                345
```

Look for two items that match in protein, fat and carbohydrate and differ in energy. There
are none. Add a thousand more rows made the same way and there will still be none. The test
shows why.

Write the energy column as unknown weights times the other three. Call the weight on protein
p, on fat f and on carbohydrate c. On every row, energy must equal p times protein, plus f
times fat, plus c times carbohydrate. The same p, f and c must serve every row.

Row 1 has no protein and no carbohydrate, so it holds f alone: 100 times f is 900.

```working
900 divided by 100 = 9
```

So f is 9. Row 2 holds c alone: 100 times c is 400.

```working
400 divided by 100 = 4
```

So c is 4. Row 3 now has one unknown left, p. Put in the two weights you have.

```working
20 times 9 plus 60 times 4 = 420
460 minus 420 = 40
40 divided by 10 = 4
```

So p is 4. Three rows went into finding three weights. Row 4 is the check.

```working
4 times 25 plus 9 times 5 plus 4 times 50 = 345
```

The table says 345. The weights (4, 9, 4) hold on every row, so the energy column is a
weighted sum of the other three. They are the Atwater general factors of `B0-R0-C32`: 4
kilocalories for each gram of protein and of carbohydrate, and 9 for each gram of fat. The
column was made from the other three by that arithmetic, which is how a label's energy is
made.

Now go back to the question. Energy is 4 times protein plus 9 times fat plus 4 times
carbohydrate. For it to rise while the grams stay fixed, one of those three parts would have
to move. None can. The question asks about a row this table cannot contain.

Here is what that does to any sum built from all four columns. Take a made-up score for each
item that equals its energy: 1 times energy, and no weight on the grams. Row 3 gives this.

```working
1 times 460 = 460
```

Now put all the weight on the grams instead, and none on energy.

```working
4 times 10 plus 9 times 20 plus 4 times 60 = 460
```

Now split it half and half: 2, 4.5 and 2 on the grams, and 0.5 on energy.

```working
2 times 10 plus 4.5 times 20 plus 2 times 60 plus 0.5 times 460 = 460
```

All three give 460 on row 3, and they agree on every other row too. So do infinitely many
splits in between. Handed only the table and the scores, nobody can say whether the score
"comes from" energy or from the grams. This is Book 0's pair of equations that repeat each
other, now sitting inside a table.

Now the other way round: a column that is fixed by two others and still fails the test.

Three United Nations bodies wrote the report *Human energy requirements* together in 2004.
They are the Food and Agriculture Organization (FAO), the World Health Organization (WHO) and
the United Nations University (UNU). The report defines the physical activity level, PAL, as a person's total energy expenditure for
the day, TEE, divided by their basal metabolic rate, BMR. BMR is the energy spent lying at
rest after a fast. So, in the report's words, "BMR times PAL is equal to TEE". BMR and TEE are in
megajoules a day (MJ/day); PAL has no unit.

Take three made-up adults.

```table
adult  BMR (MJ/day)  PAL  TEE (MJ/day)
1      6.0           1.5  9.0
2      6.0           2.0  12.0
3      8.0           1.5  12.0
```

Test whether TEE is a weighted sum of BMR and PAL. Call the weights u and v. Rows 1 and 2
give two equations.

```working
row 1: 6.0 times u plus 1.5 times v = 9.0
row 2: 6.0 times u plus 2.0 times v = 12.0
```

Subtract row 1 from row 2, the elimination move of `B0-R0-C17`. The u terms cancel.

```working
2.0 minus 1.5 = 0.5
12.0 minus 9.0 = 3.0
3.0 divided by 0.5 = 6
```

So 0.5 times v is 3.0, and v is 6. Put v back into row 1.

```working
1.5 times 6 = 9
9.0 minus 9 = 0
```

So 6.0 times u is 0, and u is 0. Now check row 3, the row you did not use.

```working
0 times 8.0 plus 6 times 1.5 = 9
```

The table says 12.0, not 9. Row 3 fails, so TEE is not a weighted sum of BMR and PAL.

Yet every TEE in the table is fixed by the other two columns.

```working
6.0 times 1.5 = 9
6.0 times 2.0 = 12
8.0 times 1.5 = 12
```

The test finds weighted sums and only weighted sums. A column made by multiplying two others
passes straight through it, and "not a weighted sum" must never be read as "carries
something new".

**Where this picture breaks.** The weights come out exactly (4, 9, 4) only because this table's energy was worked out from
these exact grams. A real label also rounds its figures. The check then holds only to within
the rounding. A row that misses by a fraction of a kilocalorie is not a sign of a separate
column.

Energy measured by burning the food in a bomb calorimeter is not made by the Atwater
arithmetic. A table of measured energy is close to a weighted sum of the grams, not exactly
one. How close is too close is a question for the next rung.

The three adults are made up, and the relation holds exactly only because the report defines
PAL as TEE divided by BMR. In a table where TEE was measured and PAL was estimated some other
way, the three would not tie together exactly.

Add a column of 1s and there are three weights for three rows. The weights would then fit
all three rows and leave nothing to check. The practice problems return to this.

**Figure.** The four made-up items' energy against 4 times protein plus 9 times fat plus 4 times carbohydrate, both in kilocalories. Every point sits on the line where the two are equal, so the energy column says nothing the three gram columns do not.

*What the figure shows:* Four points at 345, 400, 460 and 900 kilocalories, each on the dashed line where the energy column equals the weighted sum of the grams.

**Figure.** The three made-up adults' TEE against the weights found from adults 1 and 2, 0 times BMR plus 6 times PAL, in megajoules a day. The weights fit the two adults they were found from and miss adult 3, whose TEE is 12.0, by 3.

*What the figure shows:* Paired bars for adults 1, 2 and 3: TEE 9.0, 12.0 and 12.0 against the weighted sum 9, 12 and 9. Only adult 3's pair differs.

**Must know points for you.**

- Before you read meaning into the weight on any column of a table, test whether that column is a weighted sum of the others. Find the weights from some rows, then check every other row. One row that fails settles it: the column is not a weighted sum.
- A table that carries energy beside protein, fat and carbohydrate, with energy worked out from the Atwater factors, carries one column too many. "Energy, with the three held fixed" and "fat, with energy and the other two held fixed" both ask about rows that cannot exist. Refuse the question, or drop one column and say which one you dropped.
- A column that looks like no other column can still be redundant. Energy matches none of protein, fat or carbohydrate on its own; it is fixed by the three together. Comparing columns two at a time will never find it.
- The check needs rows to spare. With as many rows as weights, almost any column fits exactly. Count the rows you used to find the weights, and believe the result only once rows beyond them hold too.
- The test finds weighted sums and nothing else. A column made by multiplying others, like TEE as BMR times PAL in the FAO/WHO/UNU report, fails it and is still fixed by them. A column worked out and then rounded, like a label's energy, passes only to within the rounding. When a column is nearly but not exactly a weighted sum, this test cannot say whether that matters. Say so, and leave it to the next rung's collinearity.
- When you hear that a model "found no effect of fat once calories were accounted for", ask how the calories were worked out. If they came from the grams, the model had no way to find an effect of fat. The claim is about the table, not about fat.

**Exercise 1** (critique). A methods section says this.

> Energy intake (kcal/day) was calculated from protein (P), fat (F) and carbohydrate (C)
> intakes as E = 4P + 9F + 4C. All four were entered together as predictors of weight change.

Say what each symbol denotes, with its unit. Then say what the second sentence cannot deliver,
and what the authors could have done instead.

**1.** Take the columns a = (1, 2, 3) and b = (4, 0, 1).

Work out the column 3a + 2b, that is, 3 times a plus 2 times b, row by row.

**2.** Take a = (1, 2, 3), b = (1, 0, 2) and y = (5, 6, 13).

Find weights u and v with y equal to u times a plus v times b on every row, or show that
there are none.

**3.** Take a = (2, 1, 4) and b = (1, 3, 0), and y = (7, 8, 8).

Is y equal to 2 times a plus 3 times b?

**4.** Take a = (2, 3, 1, 4), b = (1, 2, 5, 3) and y = (4, 7, 11, 9).

Test whether y is a weighted sum of a and b.

**5.** Take a = (1, 2, 4) and y = (8, 11, 17).

Test whether y is a weighted sum of a and the column of 1s.

**6.** A made-up packet label gives these figures for each 100 grams: protein 8 g, fat 12 g,
carbohydrate 60 g, and energy 380 kcal.

Check whether the energy is the weighted sum of the grams with the Atwater general factors as
weights.

**7.** A made-up table lists three items. None has any protein. For each 100 grams it gives the fat
and the carbohydrate in grams. It gives the energy in kcal.

```table
item  fat (g)  carbohydrate (g)  energy (kcal)
A     10       50                290
B     20       30                300
C     5        70                325
```

Find the weights that make energy a weighted sum of fat and carbohydrate. Check them. Give
their unit. Then compare them with the Atwater factors.

**8.** Hall and colleagues (2012) write the energy balance equation as ES = EI − EO. Each term is an
amount of energy per unit of time. ES is how fast the body's energy stores change. EI is the
energy taken in. EO is the energy spent, which this book writes EE.

Here are three made-up days, in kcal a day.

```table
day  EI (kcal/day)  EO (kcal/day)  ES (kcal/day)
1    2500           2400           100
2    2000           2200           -200
3    2300           2300           0
```

Without using the equation, find weights that make the ES column a weighted sum of the EI
and EO columns, and check them.

**9.** A table lists foods. It gives protein, fat and carbohydrate in grams, and energy in
kilocalories. The energy was worked out with the Atwater general factors. An analyst finds
that a score equals 0.01 times energy on every row.

Give two other sets of weights on the four columns (protein, fat, carbohydrate, energy) that
give the same score on every row. Check both on the row with protein 10 g, fat 20 g,
carbohydrate 60 g and energy 460 kcal.

**10.** Here is a worked answer. Find the step that broke.

```working
a = (1, 2, 3, 5), b = (2, 1, 1, 1), y = (5, 4, 5, 9)
row 1: 1 times u plus 2 times v = 5
row 2: 2 times u plus 1 times v = 4
from row 2, v = 4 minus 2 times u; into row 1: u plus 8 minus 4 times u = 5, so u = 1
then v = 4 minus 2 = 2
the weights 1 and 2 fit, so y is a weighted sum of a and b, y = a + 2b
```

**11.** Here is a worked answer. Find the step that broke.

```working
three made-up adults: (BMR 6.0, PAL 1.5, TEE 9.0), (6.0, 2.0, 12.0), (8.0, 1.5, 12.0), in MJ/day except PAL
test TEE as u times BMR plus v times PAL plus w times the column of 1s
solving the three rows gives u = 1.5, v = 6, w = -9
check: 1.5 times 6.0 plus 6 times 1.5 minus 9 = 9.0, and the other two rows also hold
so TEE is a weighted sum of BMR, PAL and the column of 1s
```

**12.** Here is a worked answer. Find the step that broke.

```working
a made-up label, per 100 g, printing energy as a whole number: protein 7.3 g, fat 11.6 g, carbohydrate 58.4 g, energy 367 kcal
Atwater weighted sum: 4 times 7.3 plus 9 times 11.6 plus 4 times 58.4 = 367.2
367.2 is not 367
so energy is not a weighted sum of the grams, and it carries information of its own
keep all four columns as separate predictors
```

**13.** A study reports this, and says its energy intake was worked out from the grams with the
Atwater factors.

> With energy intake, protein and carbohydrate in the model, fat intake had no effect on
> weight gain.

Decide what to compute, compute it, and say what your answer does not establish.

**14.** A food composition table lists what is in each 100 grams of a food. Its notes say its
carbohydrate is found "by difference". That is 100 minus water, protein, fat and ash, all in
grams. A colleague says:

> Then the carbohydrate column is redundant. Drop it; we lose nothing.

Decide what to compute, compute it, and say what your answer does not establish.

