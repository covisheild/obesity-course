# S02-R1-C10 · Vectors as data rows, and the weighted sum

**Definition.** A vector is an ordered list of numbers, called its entries. Its length is the number of
entries it has. In this book a vector is named by a lowercase letter and written in round
brackets, so x = (2, 5, 1) is a vector of length three. The order is part of the vector:
(2, 5, 1) and (5, 2, 1) are different vectors.

One row of a data table is a vector, with one entry for each column, in the order of the
columns. Textbooks often write a vector as a column instead of a row. It is the same list.

Two vectors of the same length are added entry by entry. A vector is multiplied by a single
number by multiplying every entry by that number. A single number used this way is called a
scalar. Vectors of different lengths cannot be added.

A weighted sum of vectors v and w, with numbers c and d, is the vector cv + dw. The numbers c
and d are its weights. Textbooks also call it a linear combination.

The dot product of two vectors of the same length, written a · b and said "a dot b", is a
single number. Multiply the entries in matching positions, then add the products. For two
vectors of length three, (p, q, r) · (s, t, u) = ps + qt + ru. The dot product is a weighted
sum of the entries of one vector, with the entries of the other as the weights.

Suppose a total T is found as a · x, for a fixed vector of weights a. Raise one entry of x by
one unit and hold every other entry fixed. Then T changes by the matching entry of a. Rung 2
of this subject calls that number a partial derivative.

**In plain terms.** Write down a food's grams of protein, fat and carbohydrate, always in that order. That list is a
vector. The list (10, 30, 50) means 10 g of protein, 30 g of fat and 50 g of carbohydrate.

Book 0 gave the energy each gram supplies (`B0-R0-C32`). A gram of protein gives about 4 kcal.
A gram of fat gives about 9, and a gram of carbohydrate about 4. So multiply each count of grams by its
factor, and add.

```working
4 times 10 plus 9 times 30 plus 4 times 50 = 510
```

That multiply-and-add is called the dot product of the factor list (4, 9, 4) with the gram list
(10, 30, 50). The answer is 510 kcal.

Each factor is a weight. It says how much one more gram of that nutrient adds to the total,
with the other two left alone. "Weight" here means a multiplier, not body weight. The clash is
in the textbooks. This book writes "body weight" whenever it means the person.

**Illustration.** Start with a row that does not behave like numbers you can add up. A clinic records four
things about each patient, always in the same order. They are age in years, body weight in kg,
height in cm and waist in cm. One patient's row, made up for this example, is a vector.

```working
x = (40, 68, 162, 88)
```

Swap two entries and you have a different patient, not the same patient written another way.
The order is part of the meaning.

Now try the two operations on it. Add a second patient's row to this one, and you get a list
of four numbers that describes nobody. Multiply this row by 2 and you get a person of 80 years
and 136 kg, which is not a doubled version of anyone. The arithmetic runs, and the answer means
nothing.

One operation on these rows does mean something. Take the same patient a year later, with the
new row y = (41, 65, 162, 84), also made up. Subtract entry by entry.

```working
41 minus 40 = 1
65 minus 68 = -3
162 minus 162 = 0
84 minus 88 = -4
```

The change vector y − x is (1, −3, 0, −4). It says one year older, 3 kg lighter, no change in
height and 4 cm less at the waist. Subtraction works because the two rows describe one person,
in the same order and the same units.

Food rows are different. Adding and scaling them is the whole point. A packaged snack's label
gives its grams per 100 g. Take one made up for this example.

```working
g = (10, 30, 50)
```

The entries are grams of protein, fat and carbohydrate in 100 g of the snack. A serving is
30 g, which is 0.3 of 100 g. Scale the vector by 0.3.

```working
0.3 times 10 = 3
0.3 times 30 = 9
0.3 times 50 = 15
```

A serving holds (3, 9, 15): 3 g of protein, 9 g of fat and 15 g of carbohydrate. That is 27 g
of the three together. The other 3 g of the serving are whatever else the snack contains,
such as water or minerals.

Now the energy. The Food and Agriculture Organization (FAO) of the United Nations gives the
Atwater general factors. They are 4.0 kcal/g for protein, 9.0 for fat and 4.0 for
carbohydrate. You can find them in FAO Food and Nutrition Paper 77, 2003, §3.5.1
(https://www.fao.org/4/y5022e/y5022e04.htm).
Write them as a vector in the same order as the grams.

```working
a = (4, 9, 4)
```

The energy in a serving is a · (3, 9, 15). Multiply matching entries and add.

```working
4 times 3 = 12
9 times 9 = 81
4 times 15 = 60
12 plus 81 plus 60 = 153
```

A serving gives 153 kcal. The energy in the whole 100 g is a · g.

```working
4 times 10 plus 9 times 30 plus 4 times 50 = 510
0.3 times 510 = 153
```

Scaling the grams by 0.3 scaled the energy by 0.3. That is no accident. Every product in the
dot product was scaled by 0.3, so their sum was too.

Adding works the same way. A second item eaten with the snack, a biscuit, gives (2, 5, 20) per
serving, also made up. The meal is the sum of the two vectors.

```working
3 plus 2 = 5
9 plus 5 = 14
15 plus 20 = 35
```

The meal holds (5, 14, 35). Its energy can be found two ways, and they must agree.

```working
4 times 5 plus 9 times 14 plus 4 times 35 = 286
4 times 2 plus 9 times 5 plus 4 times 20 = 133
153 plus 133 = 286
```

Dot the meal's vector once, or dot each item and add the energies. Both give 286 kcal. Use
that as a check on any diet app that shows a meal's total.

Now read the weights. Add 1 g of fat to the serving and hold the other two entries fixed.

```working
4 times 3 plus 9 times 10 plus 4 times 15 = 162
162 minus 153 = 9
```

The total rose by 9 kcal, the weight on fat. Each weight in a is the change in the total for one
more unit of its own entry, with the others held fixed.

The same grams dotted with a different vector of weights give a total in a different unit. FAO
gives the factors in kilojoules as 17, 37 and 17 kJ/g.

```working
17 times 10 plus 37 times 30 plus 17 times 50 = 2130
```

The 100 g of snack gives 2,130 kJ. The grams did not change. Only the weights did.

In India this is not only a textbook exercise. Look at the Food Safety and Standards (Labelling
and Display) Regulations, 2020, regulation 5(3)(e)(i). It says a packaged food's label energy
is to be calculated with fixed conversion factors. Among them are 4 kcal/g for carbohydrates
and protein, and 9 kcal/g for fat. So the energy printed on a packet is a dot product
of its declared grams with those factors.

**Where this picture breaks.** The factors are general factors: one value for each nutrient, whatever the food. So a · g gives
the energy a label would declare. It is not the energy a particular person absorbs from that
food (`B0-R0-C32`).

Adding and scaling rows is meaningful only when the entries match in order and in unit. Food
grams add. Patients' rows do not.

"One more gram of fat, with the others held fixed" describes the formula. A real food rarely
lets you change one nutrient alone, so a real swap changes several entries at once.

The snack, the biscuit and the patient are made up. Only the factors 4, 9 and 4 kcal/g, and 17,
37 and 17 kJ/g, come from the sources.

**Figure.** Where the 153 kcal in a 30 g serving of the made-up snack come from. Each bar is one term of the dot product (4, 9, 4) · (3, 9, 15): 12 kcal from protein, 81 from fat and 60 from carbohydrate.

*What the figure shows:* Three bars starting at zero: protein 12 kcal, fat 81 kcal, carbohydrate 60 kcal. The fat bar is the tallest.

**Must know points for you.**

- Before you take a dot product, line up the two vectors' orders. If a label lists fat, then protein, then carbohydrate, and your factors run protein, fat, carbohydrate, the arithmetic still gives a number. It is the wrong number, and nothing on the page will warn you.
- The misconception is that a weight tells you what happens when you change one thing in a real food. It tells you the change with every other entry held fixed. Swapping fat for sugar changes two entries at once. Write the whole change vector and dot that.
- A weighted sum throws information away. Many different gram vectors give the same total energy. So two foods with the same kilocalories per 100 g can differ in every nutrient. Never infer a food's make-up from its energy figure.
- Add or scale rows only when every entry means the same thing, in the same unit, in the same place. Food grams add. Two patients' rows do not. The difference between one patient's rows at two visits does mean something: it is the change in each measurement.
- Check a meal's energy in an app or a diet chart two ways. Add the foods' gram vectors and dot the total once. Then dot each food and add the energies. The two answers must agree. If they do not, one of the rows or one of the factors is wrong.
- When you teach this, say "weights" for the multipliers and "body weight" for the person, every time. A trainee who hears "the weight on fat is 9" beside a patient's weight of 68 kg will otherwise hear one word doing two jobs.

**Exercise 1** (interpretation). The FAO report gives the Atwater general factors in kilojoules as 17 kJ/g for protein, 37 kJ/g
for fat and 17 kJ/g for carbohydrate. Write the energy E of a food, in kJ, as an equation in
its grams of protein p, fat f and carbohydrate c. Say what each symbol stands for, with its
unit. Then write the same equation as a dot product of two named vectors, and say which vector
holds the weights.

**1.** u = (2, 5, 1) and v = (3, −1, 4). Work out u + v and 3u.

**2.** With the same u = (2, 5, 1) and v = (3, −1, 4), work out the weighted sum 2u − 3v.

**3.** Work out u · v for u = (2, 5, 1) and v = (3, −1, 4). Then work out (4, 9, 4) · (0, 1, 0) and
(4, 9, 4) · (1, 1, 1).

**4.** For each, say whether it can be worked out. Where it can, work it out.

1. (1, 2, 3) · (4, 5)
2. (1, 2) + (3, 4, 5)
3. 2.5 times (4, 0, −2)
4. (1, 2, 3) · (4, 5, 6)

**5.** A packaged food's label, made up for this problem, gives per 100 g: protein 7 g, fat 18 g,
carbohydrate 66 g. Use the Atwater general factors of 4.0, 9.0 and 4.0 kcal/g (FAO 2003) to
work out the energy in 100 g, in kcal.

**6.** Take the same food, (7, 18, 66) grams per 100 g. Work out its energy in kJ with the FAO factors
of 17, 37 and 17 kJ/g. Then divide the kJ figure by the kcal figure from the last problem.

**7.** The food in the last two problems, (7, 18, 66) grams per 100 g, is eaten in a 25 g serving.
Work out the grams in the serving, then the energy in the serving in kcal. Check the answer
against the 454 kcal per 100 g.

**8.** FAO's Atwater system also gives alcohol a rounded factor of 7.0 kcal/g. A drink, made up for
this problem, holds no protein, no fat, 10 g of carbohydrate and 14 g of alcohol. Write the
grams and the factors as two vectors of length four, and work out the drink's energy in kcal.

**9.** A label, made up for this problem, gives 480 kcal per 100 g, 8 g of protein and 24 g of fat.
The carbohydrate figure is smudged. Taking the energy as the dot product with (4, 9, 4), find
the grams of carbohydrate.

**10.** A meal is one serving of each of three made-up foods. In grams of protein, fat and
carbohydrate they are (4, 2, 30), (9, 6, 12) and (1, 8, 22). Work out the meal's energy in kcal in two
ways, with the factors (4, 9, 4), and show that they agree.

**11.** Here is a worked answer. Find the step that broke.

```working
a made-up label lists, per 100 g: fat 30 g, protein 10 g, carbohydrate 50 g
grams, as read off the label: (30, 10, 50)
factors for protein, fat, carbohydrate: (4, 9, 4)
energy = 4 times 30 plus 9 times 10 plus 4 times 50 = 410 kcal
```

**12.** Here is a worked answer for the energy in a 30 g serving of this section's made-up snack. Its
grams per 100 g are (10, 30, 50). Find the step that broke.

```working
the serving is 0.3 of 100 g
grams in the serving: 0.3 times (10, 30, 50) = (3, 9, 15)
factors for a serving: 0.3 times (4, 9, 4) = (1.2, 2.7, 1.2)
energy = 1.2 times 3 plus 2.7 times 9 plus 1.2 times 15 = 45.9 kcal
```

**13.** A food blog says: "Replace 10 g of fat in your recipe with 10 g of sugar. You cut 90 kcal,
because fat carries 9 kcal a gram."

Decide what to compute, compute it, and say what your answer does not establish.

**14.** A colleague says: "These two snacks both give 510 kcal per 100 g, so nutritionally they are
the same food."

Decide what to compute, compute it, and say what your answer does not establish.

