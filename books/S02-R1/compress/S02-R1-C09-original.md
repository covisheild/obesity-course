# S02-R1-C09 · Highest and lowest points: slope zero and curvature

**Definition.** A function f has a local maximum at an input c when f(c) is at least as large as f(x) for
every x in some stretch of inputs on both sides of c. It has a local minimum at c when f(c) is
no larger than every such f(x). Over a stated range of inputs, the overall maximum is the
largest value f takes anywhere in the range, and the overall minimum is the smallest.
Textbooks call these the absolute maximum and the absolute minimum. "Absolute" there has
nothing to do with absolute value.

A critical point of f is an input c, inside the range, at which the derivative f′(c) is zero
or does not exist. If f has a local maximum or minimum at c, and has a derivative there, then
f′(c) = 0. The reverse does not hold. A critical point is a candidate, not a guarantee:
f(x) = x³ has a critical point at x = 0 and neither a maximum nor a minimum there.

The first derivative test sorts a critical point c by the sign of f′ on either side. If f′
changes from positive to negative as x rises through c, f has a local maximum at c. If it
changes from negative to positive, f has a local minimum. If it keeps the same sign, neither.

The second derivative test does the same job with one number. Suppose f′(c) = 0. If the
second derivative f″(c) is greater than zero, f has a local minimum at c. If f″(c) is less
than zero, f has a local maximum. If f″(c) = 0, this test decides nothing, and the first
derivative test has to be used instead.

Take a closed range of inputs from a to b, and a function with no breaks in it. Its overall
maximum and its overall minimum each sit either at an end of the range or at a critical point
inside it. To find them, work out f at both ends and at every critical point, and compare.

A quadratic is a function of the form f(x) = px² + qx + r, for fixed numbers p, q and r.
Where f is a quadratic and f′(c) = 0, a step of any size h away from c changes f by exactly
half of f″(c) times h². So the size of f″(c) measures how fast f climbs away from its lowest
point, or falls away from its highest.

For a set of n data values x and a candidate centre m, the sum of squared deviations from m is
S(m) = Σ (x − m)². It has one critical point, at m equal to the mean of the values, and there
its second derivative is 2n, which is positive. So the mean is the one value of m that makes
S smallest. The smallest value of S is the sum of squared deviations from the mean.

An equilibrium, in the sense of `S02-R1-C08`, is a state at which a rate of change over time
is zero and stays zero. A maximum or a minimum is an input at which the slope of a function,
taken with respect to that input, is zero. Both are found by setting a derivative to zero.
They answer different questions.

**In plain terms.** Picture a smooth hill. At the very top, the ground is level for an instant. A marble set down
exactly there does not roll either way. The same is true at the bottom of a smooth valley.

So to find a top or a bottom, look for where the slope is zero. In the words of `S02-R1-C02`,
look for where the derivative is zero.

Level ground does not tell you which of the two you are standing on. Walk across a hilltop and
the slope goes from uphill to downhill, so the slope is falling. Walk across a valley floor and
the slope goes from downhill to uphill, so the slope is rising. The second derivative from
`S02-R1-C03` is the rate at which the slope changes. Positive means a valley floor. Negative
means a hilltop.

Try it on f(x) = x² − 4x + 7. The rules of `S02-R1-C03` give both derivatives.

```working
f′(x) = 2x − 4
f″(x) = 2
```

The first is zero when 2x = 4, that is at x = 2. The second derivative is 2, which is positive,
so x = 2 is a valley floor. Put x = 2 into f for the lowest value.

```working
2 times 2 minus 4 times 2 plus 7 = 3
```

The lowest value of f is 3, at x = 2.

Two warnings go with this. Ground can be level without being a top or a bottom. A flat landing
on a staircase is level, and the stairs keep climbing after it. And suppose you may walk only
part of the hill. Then the highest place you can reach may be the edge of that part, where the
ground is still sloping upward.

The same idea settles a question from Book 0. You have several readings of one thing and want a
single number to stand for them. Choose the number that makes the misses, each squared and then
added up, as small as they can be. That number turns out to be the mean.

**Illustration.** Start with the way this goes wrong. Take f(x) = x³ − 3x, and suppose you want its highest
and lowest values for x anywhere from −2 to 3. Differentiate with the power, constant-multiple
and sum rules of `S02-R1-C03`.

```working
f′(x) = 3x² − 3
```

Set the derivative to zero and solve.

```working
3x² − 3 = 0
3x² = 3
x² = 1
x = 1 or x = −1
```

There are two critical points. The second derivative sorts them.

```working
f″(x) = 6x
f″(−1) = −6, less than zero, so a local maximum
f″(1) = 6, greater than zero, so a local minimum
```

It is tempting to stop here and write "the maximum is at x = −1". Do not. Work out f at both
critical points and at both ends of the range. Add x = 0 and x = 2 so you can see the shape.

```working
-2 times -2 times -2 minus 3 times -2 = -2
-1 times -1 times -1 minus 3 times -1 = 2
0 times 0 times 0 minus 3 times 0 = 0
1 times 1 times 1 minus 3 times 1 = -2
2 times 2 times 2 minus 3 times 2 = 2
3 times 3 times 3 minus 3 times 3 = 18
```

```table
x   f(x)
-2  -2
-1  2
0   0
1   -2
2   2
3   18
```

The overall maximum over this range is 18, at x = 3. That is an end of the range, and the
slope there is nowhere near zero.

```working
3 times 3 times 3 minus 3 = 24
```

That line is f′(3), which is 24. The local maximum at x = −1 is only a peak among its
neighbours, with a value of 2. The overall minimum is −2, and f reaches it twice: at the
critical point x = 1, and at the end x = −2.

One more trap sits at x = 0 for the plain cube, g(x) = x³. There g′(x) = 3x² is zero, and
g″(x) = 6x is zero too, so the second derivative test decides nothing. Go back to the sign of
g′ on each side. 3x² is positive for every x except 0. So g rises before 0 and rises after it.
The point is a level landing on a rising staircase, not a top and not a bottom.

Now the case that earns this section its place in a book about reading papers. A person is
weighed on five mornings of one week, on the same scale. The readings are made up for this
example: 70.4, 70.6, 70.2, 70.8 and 71.0 kg. Which single number should stand for them?

One answer: choose the number m that makes the misses, squared and added up, as small as they
can be. Call that total S(m), said "S of m".

```working
S(m) = Σ (x − m)²
```

The capital sigma, Σ, from `S02-R1-C01`, says: add this up over every reading x. Try the
candidate m = 70.4. Find each miss first.

```working
70.4 minus 70.4 = 0
70.6 minus 70.4 = 0.2
70.2 minus 70.4 = -0.2
70.8 minus 70.4 = 0.4
71.0 minus 70.4 = 0.6
```

Square each miss and add.

```working
0 times 0 plus 0.2 times 0.2 plus -0.2 times -0.2 plus 0.4 times 0.4 plus 0.6 times 0.6 = 0.60
```

S(70.4) is 0.60 square kilograms, written kg². The unit is squared because each miss, in
kilograms, was multiplied by itself. Do the same for the candidate m = 70.6.

```working
-0.2 times -0.2 plus 0 times 0 plus -0.4 times -0.4 plus 0.2 times 0.2 plus 0.4 times 0.4 = 0.40
```

The same work for three more candidates gives this table.

```table
m (kg)  S(m) (kg²)
70.2    1.20
70.4    0.60
70.6    0.40
70.8    0.60
71.0    1.20
```

The smallest S in the table is at 70.6. A table only tests the candidates in it. The
derivative shows that no m anywhere does better, for any set of n readings. Follow it one move
at a time.

Open the square first. `B0-R0-C15` multiplies every term inside one bracket by every term
inside the other.

```working
(x − m)² = (x − m) times (x − m)
(x − m)² = x times x − x times m − m times x + m times m
(x − m)² = x² − 2mx + m²
```

Now add that up over all n readings. The candidate m is the same number in every term, so it
comes outside the sum. And m² is added once for each reading, n times in all.

```working
S(m) = Σ x² − 2m Σ x + n m²
```

Differentiate with respect to m, using the rules of `S02-R1-C03`. The first term, Σ x², has no
m in it, so its derivative is zero. The second is the fixed number −2 Σ x times m, so its
derivative is −2 Σ x. The third is n times m², so its derivative is 2n times m.

```working
S′(m) = −2 Σ x + 2nm
```

Set it to zero and solve for m.

```working
2nm = 2 Σ x
m = Σ x divided by n
```

Σ x divided by n is the sum of the readings divided by how many there are. That is the mean of
`B0-R0-C28`. Differentiate once more to see which kind of critical point it is.

```working
S″(m) = 2n
```

2n is positive for any count of readings, so the mean is a minimum. It is the only critical
point, so it is the overall minimum as well. Check it on the five weighings.

```working
70.4 plus 70.6 plus 70.2 plus 70.8 plus 71.0 = 353
353 divided by 5 = 70.6
```

The mean is 70.6 kg, where the table put the lowest S. Choosing a number by making squared
misses as small as possible is called least squares. The mean is the least-squares answer when
the thing you choose is a single number.

Next, the size of the second derivative. Take any quadratic, f(x) = px² + qx + r, with its
level point at c. Step a distance h away from c and expand.

```working
f(c + h) = p(c + h)² + q(c + h) + r
f(c + h) = pc² + 2pch + ph² + qc + qh + r
f(c + h) = f(c) + (2pc + q)h + ph²
```

The bracket 2pc + q is f′(c), which is zero at a level point, so the middle term drops out.
And f″ is 2p, so p is half of f″.

```working
f(c + h) = f(c) + half of f″(c) times h²
```

For the weighings, S″ is 2n, which is 10, so half of it is 5. S rises from its lowest value of
0.40 by 5 times the square of the step. Check it on the table's last row, a step of 0.4 kg.

```working
0.40 plus 5 times 0.4 times 0.4 = 1.20
```

With 20 readings instead of 5, S″ would be 40. The same step of 0.4 kg would then raise S by 20
times 0.16, not 5 times 0.16.

```working
5 times 0.4 times 0.4 = 0.8
20 times 0.4 times 0.4 = 3.2
```

The more readings, the sharper the valley. A sharp valley pins the best value down: a small step
off it costs a lot. Rung 2 of this subject uses the same curvature on a different measure of
fit, called a likelihood. There it says how precisely a quantity has been estimated.

Last, the lowest value of S itself, 0.40 kg². That is the sum of squared deviations from the
mean. `B0-R0-C28` divided it by one less than the count to get the sample variance.

```working
0.40 divided by 4 = 0.1
```

The sample variance of the five weighings is 0.1 kg², and their standard deviation is its
square root, about 0.32 kg.

Keep all this apart from the equilibrium of `S02-R1-C08`. Suppose a person's body weight rose
for some weeks after a change in their life, then turned and fell. At the top of that curve,
the rate of change of body weight with respect to time was zero for an instant. The weight did
not stay there. An equilibrium is a weight at which the rule that gives the rate from the
weight gives zero, so the weight stays. A zero slope for an instant marks a turning point. A
rate held at zero marks a settling point.

**Where this picture breaks.** The hill picture needs a smooth curve. At a sharp corner, a top can have no slope at all. That
is the other kind of critical point, where the derivative does not exist, and setting a
derivative to zero will never find it.

The rule that a step h raises f by half of f″(c) times h² is exact only for a quadratic. For
other curves it is close for small steps and drifts for larger ones. For f(x) = x³ − 3x at its
local minimum x = 1, half of f″(1) is 3. The rule predicts f(2) as −2 plus 3, which is 1. The
table says f(2) is 2.

The mean wins only because the misses were squared before they were added. Squaring makes one
big miss count for a great deal. Add up the sizes of the misses without squaring them, and a
different centre can come out best.

The five weighings are made up, and they are all the arithmetic here describes. They say
nothing about any real person's week.

**Figure.** f(x) = x³ − 3x for x from −2 to 3. The slope is zero at x = −1 and at x = 1, but the highest value over the range, 18, is at the end x = 3.

*What the figure shows:* A smooth curve through six points: (−2, −2), (−1, 2), (0, 0), (1, −2), (2, 2) and (3, 18). It has a small peak at x = −1, a dip at x = 1, then climbs steeply to 18 at x = 3.

**Figure.** The five made-up weighings. For each candidate centre m, S(m) is the sum of squared misses. It is lowest, 0.40 square kilograms, at the mean of 70.6 kg, and rises by 5 times the square of the step on either side.

*What the figure shows:* Five points on a U-shaped curve: 1.20 at 70.2 kg, 0.60 at 70.4, 0.40 at 70.6, 0.60 at 70.8 and 1.20 at 71.0.

**Must know points for you.**

- A derivative of zero marks a candidate, not an answer. The misconception is that f′ = 0 means a maximum. It can be a minimum, or a level step with neither. Check the second derivative, or the sign of f′ on each side, before you name what you found.
- Over a range of inputs, work out the value at both ends as well as at every critical point. The highest value can sit at an end, where the slope is not zero at all. When a study reports that the best dose was the highest dose it tested, that is an end of the range. It is not a peak, and doses beyond the range remain untested.
- The derivative test finds local answers: a point lower than its near neighbours. It does not say the point is the lowest anywhere. Compare every candidate before you call one the overall minimum. If the second derivative is zero there, the test has said nothing, and you must look at the sign of the slope on each side.
- When a paper says "least squares", read it as this section's move: write the total of the squared misses, set its derivative to zero, solve. For one number, the answer is the mean. Because the misses are squared, one far-off reading pulls the answer toward itself. Look at the readings before you accept a least-squares figure.
- The size of the second derivative at a minimum says how sharply the best value is pinned down. For the sum of squared deviations it is twice the count of readings. So more readings give a sharper valley, and a value off the mean costs more.
- A slope of zero on a weight curve is not a settling point. If a patient's weight peaked and turned, its rate of change with respect to time was zero for an instant only. Call a weight an equilibrium only when the rule that gives the rate stays at zero there.

**Exercise 1** (interpretation). Below is the derivation from this section that the mean makes the sum of squared deviations
smallest. The move taken at each line has been left out, and one line has been removed.

```working
S(m) = Σ (x − m)²
S(m) = Σ x² − 2m Σ x + n m²
S′(m) = −2 Σ x + 2nm
m = Σ x divided by n
S″(m) = 2n
```

Write beside each line the one move that produced it from the line before. Then write the
missing line in its place, with its move.

**1.** f(x) = x² − 6x + 11. Find the input at which f′(x) is zero. Say whether f has a local maximum
or a local minimum there, and give the value of f at that point.

**2.** g(x) = −2x² + 8x + 1. Find the critical point, say which kind it is, and give its value.

**3.** h(x) = x³ − 12x. Find both critical points, sort each with the second derivative, and give
the value of h at each.

**4.** f(x) = x⁴. Show that x = 0 is a critical point and that the second derivative test decides
nothing there. Then decide what kind of point it is.

**5.** f(x) = x² − 4x + 5, for x from 0 to 5. Find the overall maximum and the overall minimum over
that range, and where each occurs.

**6.** The five values are 3, 7, 8, 12 and 5. Find the number m that makes Σ (x − m)² smallest.
Give the smallest value of that sum, and the second derivative of the sum with respect to m.

**7.** A nurse measures one patient's waist three times in a row. The readings are made up for this
problem: 88.4, 89.0 and 88.7 cm.

Find the single value that makes the sum of squared misses smallest, and that smallest sum,
with its unit. Then find the sum of squared misses if 89.0 cm were reported instead.

**8.** A municipality has 400 metres of fencing for a rectangular walking ground in a park. One long
side runs along an existing wall and needs no fence. The figures are made up for this problem.

Which side lengths give the largest area, and what is that area?

**9.** Two people are weighed repeatedly on the same scale. Person A is weighed 4 times and person B
16 times. Each set of readings has a mean of 70.0 kg. The figures are made up for this problem.

Someone reports 70.5 kg for each person instead of the mean. By how much does each person's sum
of squared misses rise? Say what the difference between the two answers shows.

**10.** A paper's supplement gives, for one person's repeated body weights in kg, the sum of squared
misses as a function of a candidate centre m. The formula is made up for this problem.

```working
S(m) = 4m² − 560m + 19,601
```

How many readings were there? What was their mean? What is S at the mean, and what is the
sample variance?

**11.** Here is a worked answer. Find the step that broke.

```working
f(x) = −x² + 6x
f′(x) = −2x + 6, which is zero at x = 3
f(3) = −9 + 18 = 9
so the smallest value f ever takes is 9
```

**12.** Here is a worked answer for f(x) = 2x³ − 3x² on the range from −1 to 2. Find the step that
broke.

```working
f′(x) = 6x² − 6x = 6x(x − 1), zero at x = 0 and x = 1
f″(x) = 12x − 6
f″(0) = −6, so a local maximum, f(0) = 0
f″(1) = 6, so a local minimum, f(1) = −1
so over the range, the largest value is 0 and the smallest is −1
```

**13.** Here is a worked derivation of the value of m that makes Σ (x − m)² smallest. Find the step
that broke.

```working
(x − m)² = x² − 2mx + m²
S(m) = Σ x² − 2m Σ x + m²
S′(m) = −2 Σ x + 2m
setting S′(m) = 0 gives m = Σ x
```

**14.** Here is a worked argument about a patient. The figures are made up. Find the step that broke.

```working
her body weight rose for six weeks after she changed jobs, then fell
at week 6 her body weight was 82 kg, and its rate of change was zero
a rate of change of zero means an equilibrium
so 82 kg is her settling point
```

**15.** A press release says: "Weight loss rose with every dose we tested, so our top dose, 30 units,
is the optimal dose." The trial's table, made up for this problem, gives the average weight
loss at each dose.

```table
dose (units)  weight loss (kg)
10            2.0
20            3.5
30            4.5
```

Decide what to compute, compute it, and say what your answer does not establish.

**16.** A colleague says: "The mean is the best single number to report for a patient's repeated
weighings. That is a mathematical fact."

Here are five weighings of one person, made up for this problem. The last was taken in outdoor
clothes: 70.2, 70.4, 70.3, 70.5 and 72.6 kg.

Decide what to compute, compute it, and say what your answer does not establish.

