# C3 · Two equations at once

**Definition.** Everything below concerns equations in which each unknown appears on its own, multiplied by a
number and added — the only kind this book uses.

An equation may hold two unknowns. On its own such an equation does not fix either of them.

A system of two equations in two unknowns is a pair of equations required to hold at the same
time. A solution of the system is a pair of values that satisfies both equations, not one.

Two methods solve such a system. Substitution rearranges one equation to give one unknown in
terms of the other, and puts that expression into the second equation, which then holds one
unknown. Elimination adds a multiple of one equation to the other, choosing the multiple so
that one unknown cancels.

A system of two such equations has exactly one solution, or none, or infinitely many. It has
none when the two equations make statements that cannot both be true. It has infinitely many
when one equation is a multiple of the other, and so states nothing the first did not.

**In plain terms.** The section before this one solved equations with one letter in them. This one starts where a
line has two.

Here is such a line.

```working
    x + y = 10
```

Ask what x is. There is no single answer. Try some pairs and see.

```table
    x   y
    1   9
    4   6
    7   3
```

One equation with two unknowns does not pin either of them down. It ties them together. Fix one
and the other follows; fix neither and you have nothing.

Now add a second statement that has to be true at the same time.

```working
    x + y = 10
    x minus y = 4
```

Now there is one pair that works, and only one. Two statements, two unknowns.

There are two ways to find it, and they are the same idea approached from different sides.

The first is substitution. You have substituted a number for a letter before now. This is the
same move with an expression in place of the number, and what it leaves behind is algebra rather
than arithmetic.

Rearrange one equation so that one letter stands alone, then put that into the other equation.

Rearrange the first line to give x on its own.

```working
    x = 10 minus y
```

Now put that in place of x in the second line.

```working
    10 minus y minus y = 4
    10 minus 2y = 4
    2y = 6
    y = 3
```

Then go back and get x.

```working
    x = 10 minus 3
    x = 7
```

The second way is elimination. Add the two equations together, left to left and right to right.
The y and the minus y cancel.

```working
    2x = 10 plus 4
    10 plus 4 = 14
    14 divided by 2 = 7
```

So x is 7. Elimination has found one unknown, and it is not finished. Put the 7 back into either
line to get the other. The first line is the simpler one.

```working
    7 + y = 10
    10 minus 7 = 3
```

So y is 3, the same as substitution gave. Now check. Put both numbers into both statements, not
into one of them.

```working
    7 plus 3 = 10
    7 minus 3 = 4
```

Both hold, so the pair is the solution.

Adding worked because one line had plus y and the other had minus y. When the same letter
carries the same number and the same sign in both lines, subtract instead. Take one line from
the other, left from left and right from right.

```working
    x + y = 10
    x + 3y = 16
```

Take the first line from the second. The x terms cancel, and 3y take away y leaves 2y.

```working
    16 minus 10 = 6
    2y = 6
    6 divided by 2 = 3
```

So y is 3. Put it back into the first line to get x.

```working
    10 minus 3 = 7
```

So x is 7. Check the pair in both lines.

```working
    7 plus 3 = 10
    3 times 3 = 9
    7 plus 9 = 16
```

And sometimes no letter carries matching numbers at all. Then make a match. Multiply every term
of one line, on both sides, by the same number. That is the rule from the section before this:
whatever you do to one side, do to the other.

```working
    x + y = 10
    3x + 2y = 27
```

The second line has 2y and the first has only y. So multiply the whole of the first line by 2.

```working
    2 times 10 = 20
    2x + 2y = 20
```

Now the y terms match. Take this new line from the second line. The 2y terms cancel, and 3x take
away 2x leaves x.

```working
    27 minus 20 = 7
```

So x is 7. Put it back into the first line to get y.

```working
    10 minus 7 = 3
```

So y is 3. Check the pair in both lines.

```working
    7 plus 3 = 10
    3 times 7 = 21
    2 times 3 = 6
    21 plus 6 = 27
```

The same pair sits behind all three examples, so you can watch each method land on it. Every
elimination has the same four steps. Make one letter match, if it does not already. Add or
subtract the lines so that it cancels. Solve for the letter that is left. Then put that value
back into either line to get the other.

Sometimes no whole-number multiple of one line matches the other. Then multiply both lines, each
by its own number.

```working
    2x + 3y = 12
    3x + 2y = 13
```

Multiply the whole of the first line by 3 and the whole of the second by 2. Both x terms become
6x.

```working
    6x + 9y = 36
    6x + 4y = 26
```

Take the second new line from the first. The 6x terms cancel, and 9y take away 4y leaves 5y.

```working
    36 minus 26 = 10
    5y = 10
    10 divided by 5 = 2
```

So y is 2. Put it back into the first line to get x.

```working
    3 times 2 = 6
    12 minus 6 = 6
    6 divided by 2 = 3
```

So x is 3. Check the pair in both lines.

```working
    2 times 3 = 6
    3 times 2 = 6
    6 plus 6 = 12
    3 times 3 = 9
    2 times 2 = 4
    9 plus 4 = 13
```

Two more shapes to recognise, because they arrive without warning.

Sometimes the second statement repeats the first.

```working
    x + y = 10
    2x + 2y = 20
```

The second line is the first line doubled. It is true whenever the first is true, so it adds
nothing, and you are back to as many answers as you like.

And sometimes the two statements cannot both hold.

```working
    x + y = 10
    x + y = 12
```

Two numbers cannot add to 10 and to 12. There is no pair at all, and the useful thing to say is
not the answer but that one of the two statements is wrong.

**Illustration.** A packet reaches you with two lines of its panel gone. The energy is still there, 468
kilocalories in every 100 grams, and so is the protein, 12 grams. The carbohydrate line and
the fat line have torn away. Those figures are made up for this problem. The label rule is
the real one you have used in the two sections before this.

```working
    E = 4c + 4p + 9f
```

Put in what the panel still gives you.

```working
    4 times 12 = 48
```

Take that 48 off both sides.

```working
    468 minus 48 = 420
```

So what you know is this.

```working
    4c + 9f = 420
```

One line, two unknowns.

Look at three pairs that all satisfy that line.

```table
    carbohydrate grams   fat grams   from carbohydrate   from fat   total
    60   20   240   180   420
    105   0   420   0   420
    15   40   60   360   420
```

Every row is a genuine answer to the arithmetic. Not every row is a possible packet. The
second row puts 105 grams of carbohydrate and 12 grams of protein into 100 grams of food. The
section before this taught you to throw out a negative mass, and this row fails the same kind
of test. Run that second check on any answer, because the arithmetic never runs it for you.

So what would fix them? A second statement that has to be true at the same time.

Suppose the maker tells you the carbohydrate is three times the fat. Write it beside the
first.

```working
    4c + 9f = 420
    c = 3f
```

Now substitute. Put 3f in place of c in the first line, so 4c becomes 4 times 3f.

```working
    4 times 3f, plus 9f = 420
    12f + 9f = 420
    21f = 420
```

What went in for c here was a single term, 3f. Often it is a difference instead, such as 75
minus f. Then it goes in inside brackets, and you expand them as the section on variables
showed. Every term inside is multiplied by the 4.

```working
    4(75 minus f) = 300 minus 4f
```

Back to the packet. Divide both sides by 21.

```working
    420 divided by 21 = 20
```

Twenty grams of fat. Now go back for the carbohydrate.

```working
    3 times 20 = 60
```

Sixty grams of carbohydrate.

Check both numbers in both statements. Checking one is not checking the pair.

```working
    4 times 60 = 240
    9 times 20 = 180
    240 plus 180 = 420
```

The first statement holds. And 60 is three times 20, so the second holds as well.

**Where this picture breaks.** The second statement was handed to you here. In real work it has to come from somewhere, and
where it came from is the part that decides whether your answer means anything.

**Must know points for you.**

- One equation with two unknowns has many answers, not one. Anyone who reads a single relationship as fixing a single quantity is reading something that is not there.
- Count the unknowns and count the equations before you start.
- Check a solved pair in both equations.
- When somebody draws a conclusion about one quantity from a single relationship, ask what the second statement is and where it came from.
- Two statements pin two unknowns down only when they say different things. Two that repeat each other leave you with as many answers as before. Two that contradict each other leave you with none, which is itself worth reporting.
- Use substitution when one equation already has a letter standing nearly alone. Use elimination when the same letter carries matching numbers in both lines. Use it too when you can make them match by multiplying one whole line by a number.
- Solving a pair tells you what follows from the two statements, and nothing about whether either is true.

**Exercise 1** (interpretation). A district officer shows you one line from a planning note.

> Every meal served costs us the grain plus the cooking fuel, and the two together come to 18
> rupees a meal.

They then ask you how much the grain alone costs.

Say what you can and cannot answer from that line. Then say exactly what one further piece of
information would let you answer it, and give two different forms that piece could take.

**Exercise 2** (teaching). A journalist has three minutes and no appetite for algebra. They have been told two things
about a scheme. Its total spend went up, and its total number of meals went up. They want
to write that the cost of each meal went up.

Explain why that does not follow, in words they can use, with one sentence they could quote.

**1.** Two statements have to hold at the same time.

```working
    x + y = 7
    x minus y = 1
```

Say for each of these pairs whether it is a solution.

```table
    x   y
    4   3
    5   2
    6   1
```

**2.** Write down four different pairs of numbers that make this statement true.

```working
    x + y = 12
```

Then say how many such pairs there are, and what that means about what this one line can tell
you.

**3.** Solve this pair by substitution.

```working
    y = 2x
    x + y = 18
```

**4.** Solve this pair by elimination.

```working
    x + y = 15
    x minus y = 3
```

**5.** A panel gives the energy as 440 kilocalories in every 100 grams and the protein as 10 grams.
The carbohydrate line and the fat line are missing. A note attached to the packet says the
carbohydrate and the fat together weigh 75 grams. All four figures are made up for this
problem.

Using the factors the Food Safety and Standards (Labelling and Display) Regulations, 2020 set
for calculating declared energy, work out the carbohydrate and the fat. Show every line and
check the pair in both statements.

**6.** Schedule II of the National Food Security Act, 2013 sets two figures you need here. The hot
cooked meal for lower primary classes is 450 kilocalories. The one for upper primary classes
is 700 kilocalories.

A kitchen serves 50 meals in a day, some lower primary and some upper primary, and its plan
totals 27,500 kilocalories for the day. The 50 and the 27,500 are made up for this problem.

Work out how many meals of each kind the plan is for. Show every line, and check the pair in
both statements.

**7.** Schedule II of the National Food Security Act, 2013 sets four figures you need here. The hot
cooked meal for lower primary classes is 450 kilocalories and 12 grams of protein. The one
for upper primary classes is 700 kilocalories and 20 grams of protein.

A kitchen's day sheet gives only two totals: 27,500 kilocalories and 760 grams of protein.
The meal count has not been written down. Both totals are made up for this problem.

Work out how many meals of each kind the sheet describes. Use elimination rather than
substitution. Show every line, and check the pair in both statements.

**8.** Here is a worked answer. Find the step that broke.

```working
    two statements have to hold at the same time
    x + y = 20
    x minus y = 6
    rearrange the first statement
    x = 20 minus y
    put that into the first statement
    20 minus y + y = 20
    20 = 20
    so both statements hold whatever y is
    and any pair adding to 20 will do
```

**9.** Here is a worked answer. Find the step that broke.

```working
    a note carries two statements about a kitchen's day
    the lower primary and upper primary meals together number 50
    L + U = 50
    twice the lower primary meals and twice the upper primary meals together number 100
    2L + 2U = 100
    that is two statements and two unknowns, so the pair can be solved
    from the first, L = 50 minus U
    put it into the second
    2 times the whole of 50 minus U, plus 2U = 100
    100 minus 2U + 2U = 100
    100 = 100
    so L is 25 and U is 25
```

**10.** A programme note says this about a school kitchen.

> Between last year and this year the kitchen's total number of meals went up, and its total
> kilocalories went up. So it served more lower primary meals and more upper primary meals
> than it did last year.

Schedule II of the National Food Security Act, 2013 sets the lower primary hot cooked meal at
450 kilocalories. It sets the upper primary hot cooked meal at 700 kilocalories. Take last year as
30 lower primary meals and 20 upper primary meals a day. Those two counts are made up for
this problem.

Decide what to compute, compute it, and say what your answer does not establish.

