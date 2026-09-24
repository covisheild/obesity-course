# S02-R1-C11 · A matrix, and what multiplying by one does

**Definition.** A matrix is a rectangular table of numbers, named by a capital letter. Its size is written
rows by columns. A matrix with 3 rows and 2 columns is a 3 × 2 matrix, said "3 by 2". An entry
is found by its row first and its column second. In a data matrix each row is one case, such
as a person or an equation, and each column is one variable, in a fixed order.

A matrix A times a vector x, written Ax, is defined when A has as many columns as x has
entries. The result is a vector with one entry for each row of A. Its entry for a given row is
that row of A dotted with x. The same result is a weighted sum of the columns of A, with the
entries of x as the weights.

A matrix A times a matrix B, written AB, is defined when A has as many columns as B has rows.
If A is m × r and B is r × n, then AB is m × n. The entry of AB in row i and column j is row i
of A dotted with column j of B. Column j of AB is A times column j of B. AB and BA are
usually different, and one of them may not be defined at all.

A matrix times a scalar c, written cA, has every entry multiplied by c.

The fixed numbers that a formula multiplies by are its coefficients. In the words of
`S02-R1-C10`, they are the weights of a weighted sum. A model written y = Xb says: each case's
predicted value, an entry of y, is that case's row of the data matrix X dotted with one shared
vector of coefficients b.

**In plain terms.** A matrix is a table of numbers with the labels taken off. Each row is one case. Each column is
one kind of measurement, always in the same place.

Multiplying a matrix by a vector does one dot product for each row. Take a table with one row
for each of two equations. Each row holds the equation's slope and its intercept, the height of
its line at zero (`B0-R0-C19`).

```table
equation  slope  intercept
first     3      10
second    2      15
```

Put a person's value in a vector as (value, 1). The 1 is there so the intercept is added once.
Try the value 5.

```working
3 times 5 plus 10 times 1 = 25
2 times 5 plus 15 times 1 = 25
```

One multiplication runs both equations for this person and gives the vector (25, 25).

Multiplying a matrix by a matrix does the same thing for several vectors at once. Put one
person in each column of the second matrix, and each column of the answer is one person's
results.

The sizes have to fit. Each row of the first matrix is dotted with each column of the second.
So a row and a column need the same number of entries. If they do not match, the product does
not exist.

**Illustration.** Book 1 met the basal metabolic rate (BMR): the energy spent lying at rest after a fast. Three
United Nations bodies wrote a joint report on it in 2004. They are the Food and Agriculture
Organization, the World Health Organization and the United Nations University, and the report
goes by their initials, FAO/WHO/UNU. It predicts
BMR from body weight with one straight line for each sex and age band. Its Table 5.2 keeps the
equations Schofield proposed in 1985. The report is *Human energy requirements*, and chapter 5
is at https://www.fao.org/4/y5686e/y5686e07.htm. Here are the two rows for adult men, in kcal/day, as
the report prints them.

```table
men, age (years)  slope (kcal/day per kg)  intercept (kcal/day)
18-30             15.057                   692.2
30-60             11.472                   873.1
```

Each row says the same thing with its own numbers: BMR is the slope times body weight, plus
the intercept. Take the labels off and keep the four numbers. That is a 2 × 2 matrix. Call it
B. Its rows are the two equations, and its columns are the slope and the intercept.

Now you can run both equations on a man of 65 kg. That is the reference man of the Indian Council of
Medical Research and National Institute of Nutrition (ICMR-NIN), in its 2020 requirements.
Write his vector as w = (65, 1). The 1 lines up with the intercept column, so the intercept is
added once.

Row by row, each row of B dotted with w:

```working
15.057 times 65 plus 692.2 times 1 = 1670.905
11.472 times 65 plus 873.1 times 1 = 1618.78
```

So Bw = (1670.905, 1618.78). That is about 1,671 kcal/day by the equation for ages 18 to 30,
and about 1,619 by the equation for ages 30 to 60.

Column by column, 65 lots of the slope column plus 1 lot of the intercept column:

```working
65 times 15.057 = 978.705
65 times 11.472 = 745.68
978.705 plus 692.2 = 1670.905
745.68 plus 873.1 = 1618.78
```

The same vector comes out. The two readings of a matrix times a vector always agree. Use
whichever is easier to check.

Now three men, of 52, 65 and 80 kg. The 52 and 80 are made up. Put each man in a row, with his
body weight and a 1: (52, 1), (65, 1) and (80, 1). That is a 3 × 2 data matrix. Call it X. Its
rows are people. Its columns are body weight and the constant 1.

To run both equations on all three men at once, put each equation in a column instead. This
is the same four numbers as B, with its rows turned into columns. Call it C.

```table
| | 18-30 equation | 30-60 equation |
| multiplies body weight | 15.057 | 11.472 |
| multiplies the constant 1 | 692.2 | 873.1 |
```

X is 3 × 2 and C is 2 × 2. X has 2 columns and C has 2 rows, so the product XC is defined,
and it is 3 × 2. Each entry is one man's row dotted with one equation's column.

```working
15.057 times 52 plus 692.2 times 1 = 1475.164
11.472 times 52 plus 873.1 times 1 = 1469.644
15.057 times 65 plus 692.2 times 1 = 1670.905
11.472 times 65 plus 873.1 times 1 = 1618.78
15.057 times 80 plus 692.2 times 1 = 1896.76
11.472 times 80 plus 873.1 times 1 = 1790.86
```

Rounded to one decimal place, XC is this table.

```table
body weight (kg)  18-30 equation (kcal/day)  30-60 equation (kcal/day)
52                1475.2                     1469.6
65                1670.9                     1618.8
80                1896.8                     1790.9
```

Its rows are people and its columns are equations. Each column on its own is y = Xb: the
data matrix X times one equation's coefficient vector b. For the younger band,
b = (15.057, 692.2), and y is the three men's predicted BMRs.

Now try the product the other way round, CX. C is 2 × 2 and X is 3 × 2. C has 2 columns but X
has 3 rows, so CX does not exist. The order of a matrix product is part of its meaning.

Last, a scalar multiple. ICMR-NIN's 2020 brief note says the FAO/WHO/UNU equations run high for
Indian adults. The note is *A Brief Note on Nutrient Requirements for Indians*, at
https://www.nin.res.in/rdabook/brief_note.pdf. Its earlier committee had cut the BMR from those equations by 5%. The 2020
committee "further reduced the BMR by another 5 %". A cut of a fixed percentage multiplies
every predicted BMR by one number. So it multiplies the whole matrix XC by one scalar.

Which scalar, though? The note does not say whether the second 5% comes off the original
figure or off the figure already cut. The two readings give two scalars.

```working
1 minus 0.05 minus 0.05 = 0.9
0.95 times 0.95 = 0.9025
```

On the 65 kg man's figure from the younger band:

```working
0.9 times 1670.905 = 1503.8145
0.9025 times 1670.905 = 1507.9918
```

The two readings differ by about 4 kcal/day. That is small next to the cut itself, about 167
kcal/day. But a paper that applies "the ICMR-NIN reduction" should say which scalar it used.

**Where this picture breaks.** The matrix product is exact arithmetic on the numbers it is given. It does not make the
equations right for any one person. They were fitted to a large international set of
measurements, and ICMR-NIN's note says that for Indians they can overestimate BMR by 10 to 12%.

Running both men's equations on the same three men is for showing the arithmetic. For a real
man, only the column for his own age band applies.

The weights 52 and 80 kg are made up. The 65 kg is ICMR-NIN's reference man, not a measured
person.

The columns of B and C carry different units: kcal/day per kg for the slope, and kcal/day for
the intercept. The 1 in each man's row is a pure number. Every product comes out in kcal/day
only because each slope meets a body weight in kg and each intercept meets the 1.

**Figure.** The product XC drawn. Each column of XC is one FAO/WHO/UNU equation for men, run on the three men of 52, 65 and 80 kg. The side axis does not start at zero, so the gap between the lines looks larger than it is.

*What the figure shows:* Two rising straight lines of three points each. The 18-30 equation runs from 1475.2 kcal/day at 52 kg to 1896.8 at 80 kg. The 30-60 equation runs from 1469.6 to 1790.9, and is flatter.

**Must know points for you.**

- Check the sizes before you multiply. The first matrix needs as many columns as the second has rows, and the answer has the first one's rows and the second one's columns. Then read the answer's size back as meaning: three rows of people means three people's results.
- Order matters. AB and BA are usually different, and one may not exist. A data matrix times a vector of coefficients gives one prediction per person. Written the other way round, the same symbols describe nothing.
- The column of 1s is what carries the intercept. Leave it out of a data matrix, and every prediction silently loses the intercept. For the Schofield equation for men aged 18 to 30, that is 692.2 kcal/day off every man's BMR.
- ICMR-NIN's 2020 note cuts the BMR from the FAO/WHO/UNU equations for Indian adults by 5% on top of an earlier 5%. Applied to a table of predictions, that is one scalar multiple of the whole table. The note does not say whether the scalar is 0.90 or 0.9025. When you apply the cut, say which, and when you read a paper that applies it, look for which.
- Exact arithmetic is not an exact prediction. A matrix product gives the equations' output to every decimal place, but the equations were fitted to other people. ICMR-NIN says they can run 10 to 12% high for Indians. Quote a computed BMR as an estimate for a group, not as a patient's measured rate.
- Read y = Xb in a methods section as "each person's prediction is their row dotted with one set of coefficients". How the coefficients b were chosen from data is a separate question, which the statistics books take up. The multiplication tells you nothing about whether they were chosen well.

**Exercise 1** (interpretation). A methods section says: "Predicted BMR was computed as y = Xb. Here X is an n × 2 matrix whose
rows are (body weight in kg, 1), and b = (15.057, 692.2)."

Say what each symbol stands for, with its unit and size. Then say in one sentence what the
equation claims.

**1.** A is the matrix below.

```table
| | column 1 | column 2 | column 3 |
| row 1 | 2 | 0 | 1 |
| row 2 | 3 | 4 | -1 |
```

What is the size of A? What is the entry in row 2, column 3? What is the entry in row 1,
column 2?

**2.** With A as in the last problem, work out Ax for x = (1, 2, 3), row by row.

**3.** Work out the same Ax again, this time as a weighted sum of the columns of A.

**4.** Work out 3A, with A as in the first problem.

**5.** P has rows (1, 2) and (3, 4). Q has rows (0, 1) and (1, 0). Work out PQ and QP.

**6.** For each pair of sizes, say whether the product exists, and if it does, give its size.

1. a 3 × 2 matrix times a 2 × 4 matrix
2. a 2 × 4 matrix times a 3 × 2 matrix
3. a 2 × 2 matrix times a 2 × 1 matrix
4. a 1 × 3 matrix times a 3 × 1 matrix

**7.** FAO/WHO/UNU Table 5.2 gives these BMR equations for women, in kcal/day. For ages 18 to 30, the
slope is 14.818 and the intercept 486.6. For ages 30 to 60, the slope is 8.126 and the
intercept 845.6. ICMR-NIN's
reference woman weighs 55.0 kg.

Write the equations as a 2 × 2 matrix, one equation in each row, and multiply it by the vector
for the reference woman. Say what each entry of the answer is.

**8.** Three women weigh 45, 55 and 70 kg; the 45 and 70 are made up. Write their data matrix X with
rows (body weight, 1). Use the FAO/WHO/UNU equation for women aged 18 to 30, b = (14.818, 486.6)
(Table 5.2), to work out y = Xb.

**9.** FAO/WHO/UNU say that multiplying a group's physical activity level (PAL) by its BMR gives its
energy requirement. They treat a PAL of 1.75 or more as desirable. Take the vector of the two
men's-equation BMRs for a 65 kg man from this section, (1670.905, 1618.78) kcal/day. Multiply
it by the scalar 1.75.

**10.** Put the two FAO/WHO/UNU women's equations in the columns of a matrix D. The first column is
(14.818, 486.6), for ages 18 to 30. The second is (8.126, 845.6), for ages 30 to 60. With X as in
the problem before last, rows (45, 1), (55, 1) and (70, 1), work out XD. At which of the three
body weights does the equation for ages 30 to 60 predict the higher BMR?

**11.** Here is a worked answer for a 65 kg man's BMR. It uses the FAO/WHO/UNU equation for men aged
18 to 30, with b = (15.057, 692.2). Find the step that broke.

```working
his vector: (1, 65)
BMR = 15.057 times 1 plus 692.2 times 65
BMR = 45,008 kcal/day
```

**12.** Here is a worked answer for PQ, with P rows (1, 2) and (3, 4), and Q rows (5, 6) and (7, 8).
Find the step that broke.

```working
PQ is 2 × 2
multiply matching entries: 1 times 5, 2 times 6, 3 times 7, 4 times 8
PQ has rows (5, 12) and (21, 32)
```

**13.** Someone wants to apply a 10% cut to the FAO/WHO/UNU BMR equation for men aged 18 to 30. Here
is their worked answer for a 65 kg man. Find the step that broke.

```working
cut the equation by 10%: 0.9 times 15.057 = 13.5513
new equation: 13.5513 times body weight plus 692.2
BMR = 13.5513 times 65 plus 692.2 = 1573.0345 kcal/day
```

**14.** A colleague says: "ICMR-NIN says the FAO/WHO/UNU equations overestimate BMR in Indians by 10
to 12%. So multiply them by 0.88 to 0.90 to get the true figure."

Decide what to compute, compute it, and say what your answer does not establish.

**15.** A clinic manager says: "Our spreadsheet computes every patient's BMR with a single matrix
multiplication, so the figures are exact."

Decide what to compute, compute it, and say what your answer does not establish.

