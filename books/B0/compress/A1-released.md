# A1 · Counting, place value, and what a calculator is actually doing

**Definition.** A number written in digits carries two things at once: which digits were used, and the place
each one occupies. The place fixes what the digit is worth.

Each place is worth ten times the place immediately to its right. That is the whole of what a
written number means, and it is why the system is called base ten.

A negative number is a number less than zero. On the number line it lies as far below zero as
the matching positive number lies above it, and it is written with a minus sign in front.

The operations in a written calculation are carried out in a fixed, agreed order: anything in
brackets first, then powers, then multiplication and division, then addition and subtraction.
Within multiplication and division, and within addition and subtraction, the work runs from
left to right.

**In plain terms.** Take 4,505. There are two fives in it, and one of them is worth five hundred while the other is
worth five. Move one step to the left and a digit is worth ten times as much.

Now the part that catches people in India. Where you put the commas is a different question from
what the digits are worth. And India does not do it the way most places do. Here the last three
digits go together and everything above that is grouped in pairs: 10,00,000. In most other
places they run in threes all the way along: 1,000,000. Same number, same value, different
commas.

The names follow the commas. India counts thousand, lakh, crore. Most other places count
thousand, million, billion. One lakh is a hundred thousand and one crore is ten million, so the
two ladders never line up.

A calculator does base ten for you, fast and without complaint, but it cannot read your mind.
Type one zero too many and it will work the sum out correctly and hand you an answer ten times
too big.

Numbers do not stop at zero. Take 240 away from 52 and the 52 runs out after 52 steps. The
other 188 steps carry on below zero, and you land on minus 188. It is written -188, with the
sign in front of the number.

So the minus sign has two jobs. Between two numbers it means take away, as in 52 minus 240. In
front of one number it says the number is below zero, as in -188. People say "minus 3" out loud
for both, so ask which job the sign is doing.

A negative answer makes sense only if the thing you are measuring can go below zero. A
temperature can fall below zero. A bank balance can be a debt. A room cannot hold minus two
people. When a thing like that comes out negative, something went wrong before the answer. Either
a mistake happened earlier, or a rule was run past the point where it holds.

A written line of sums is also worked in a fixed order. You multiply and divide before you add and
take away. So 3 plus 2 times 4 is 11, not 20. Nobody discovered that order. Everybody agreed to
it, so that one line of sums has one answer. Anything in brackets comes first, so (3 plus 2) times
4 is 20.

A calculator that shows the whole line as you type it, as most phone and scientific ones do,
follows this order. A basic desk calculator does not. It works each step out as you press the
next key. Test yours with 3 plus 2 times 4. If it shows 11, it follows the order.

The catch is the equals key. Press it part way through a line, and you have chosen the order
yourself.

**Illustration.** Open the Food Safety and Standards Act, 2006, which you can open at
<https://indiacode.gov.in/handle/123456789/586348>. Search inside it for "misleading
advertisement".

Every Indian Act opens with a list of its section names, so your first hit is the line 53.
Penalty for misleading advertisement in that list. Search again and take the second hit, which
is section 53 itself.

It says ten lakh rupees. Write that in digits, the Indian way, and then the international way.

```working
    10,00,000      1,000,000
```

Count the zeros in each. Five, and five. The number has not changed. Only the commas moved.

Somebody reading the Act writes a note in English for a reader abroad. Ten lakh, they think, and
lakh sounds like million. So ten lakh becomes ten million, and they type this.

```working
    1,00,00,000
```

Ten million is one crore. They have multiplied the penalty by ten, in a note that other people
will quote back at them.

Ten lakh is one million. One crore is ten million.

Section 53's ceiling is ten lakh and section 51's is five lakh. Type one million, then divide by
five hundred thousand, and it returns 2. That is right: the first ceiling is twice the second.
Now type it again and leave one zero off the second number. It returns 20.

The calculator did not object either time, and it never will. Checking the question is your job.
Counting the digits before you press equals is how you do it.

Two more things the calculator does without telling you. It handles numbers below zero, and it
follows an order.

Start with a number line. Draw a line, mark 0 in the middle, and mark 1, 2, 3 going right. Now
keep marking to the left of 0, at the same spacing: -1, -2, -3. Every number left of zero is
negative. The further left, the smaller it is, so -200 is smaller than -3.

Work out 52 minus 240 on it. Start at 52 and step left 240 times. After 52 steps you are at
zero, and 188 steps are still to go. They carry on past zero.

```working
    240 minus 52 = 188        (steps still to go at zero)
    52 minus 240 = -188
```

Take away another 48 and you go further left, not back up.

```working
    -188 minus 48 = -236
```

Now look at your calculator. The key that takes one number from another is the minus key. Many
calculators have a second key for the sign of one number. A key marked (-) types a minus in
front of the next number. A key marked +/- flips the sign of the number already showing.

Type 52, the minus key, 240, and equals. The display shows -188. The minus key did the taking away. The
dash on the display is the other job: the sign of one number.

Three rules cover everything this book does with negatives. Here is each one once.

Adding a negative number is the same as taking away the positive one. Taking away a negative
number is the same as adding the positive one.

```working
    10 plus -4 = 6
    10 minus -4 = 14
```

Multiplying and dividing share one rule. If the two numbers have the same sign, the answer is
positive. If the signs differ, the answer is negative.

```working
    3 times -4 = -12
    -3 times -4 = 12
    -12 divided by 4 = -3
    -12 divided by -4 = 3
```

So a negative divided by a positive is negative. And two negatives multiplied give a positive.

Now the check that matters most. A negative number means something only if the quantity can go
below zero. Some quantities have a direction built in. A temperature can fall below zero. A
budget can run a deficit, which is spending more than there was. A bank balance can be a debt.
For these, the minus sign says which way, and it is a real answer.

Other quantities are amounts of something: the mass of a thing, a count of people, a volume of
water. None of these can be less than nothing.

So when one of them comes out negative, stop. Do not report it as the amount, and do not round it
to zero. Report that the figures do not add up. Something went wrong before the answer. A figure
was copied wrongly, a step was done in the wrong order, or a sign was dropped. Or a rule was run
past the point where it holds, like a stock worked forward past the day it runs out. Go back and
find which.

The last thing a calculator does is follow an order. Type 3 plus 2 times 4. Should it add first,
or multiply first? The two choices give different answers.

```working
    adding first
    3 plus 2 = 5
    5 times 4 = 20

    multiplying first
    2 times 4 = 8
    3 plus 8 = 11
```

Both lines of working are correct arithmetic, so the arithmetic cannot settle it. People settled
it by agreement. The order of operations is a rule that was chosen, not a fact that was found. It
exists so that one written line has one answer, and here that answer is 11.

The order runs like this.

1. Anything inside brackets.
2. Powers, meaning a number multiplied by itself a set number of times. A later section
   teaches them.
3. Multiplying and dividing.
4. Adding and taking away.

Within one level, work from left to right. So 12 divided by 2 times 3 is 18, not 2. And 10 minus
4 plus 3 is 9, not 3.

```working
    3 plus 2 times 4 = 11
    (3 plus 2) times 4 = 20
    12 divided by 2 times 3 = 18
    10 minus 4 plus 3 = 9
```

Brackets are how you get the other answer when you want it. Put them round the part that has to
happen first.

Here is where a calculator catches people. A calculator that shows the whole line as you type it
follows this order. Press equals part way through, and you have chosen the order yourself.

Go back to the two ceilings in the Act. Say a note needs the section 53 ceiling plus twice the
section 51 ceiling. As one line, that is ten lakh plus 2 times five lakh. Type it whole and press
equals once.

```working
    10,00,000 plus 2 times 5,00,000 = 20,00,000
```

Now press the same keys in a different rhythm. Press equals straight after the 2, then carry on.

```working
    10,00,000 plus 2 = 10,00,002
    10,00,002 times 5,00,000 = 5,00,00,10,00,000
```

Same keys, different answer. The right one has seven digits and the wrong one has twelve.
Counting the digits catches it here, as it caught the extra zero.

Some small desk calculators work out each step as soon as you press the next key. That is the
same as pressing equals every time. Test yours. Type 3 plus 2 times 4 and press equals once. If
it shows 11, it follows the order. If it shows 20, it does not, and you must press the keys in
the order you want the work done.

**Where this picture breaks.** Place value is a rule about writing numbers down. It tells you nothing about whether ten lakh
rupees is a large penalty or a small one.

The commas break in a second way, and quietly. A spreadsheet or a website prints the grouping it
was built for, and does not say which one that is. So count the digits, not the commas. Where
the two disagree, the digits are right.

A calculator is only as good as what you typed. It will divide a sum of money by a count of
children and hand you an answer. That answer is arithmetic rather than sense.

The below-zero check works on amounts, not on changes. A mass cannot be negative, but a change in
mass can. A count of people cannot, but the change in that count from one year to the next can.
So before you run the check, say whether the number is an amount or a change.

The order of operations is an agreement about how to read a written line. It says nothing about
which order the sum needed. A line typed without the brackets it needed is read by the agreed
order, and gives the wrong answer without complaint.

**Must know points for you.**

- A lakh is not a million. One lakh is a hundred thousand. One crore is ten million.
- Before you press equals, count the digits in each number you typed. Then say the number out loud, in the naming system you are writing in.
- Indian statutes, budgets and ministry papers state money in lakh and crore. Journals and international agencies state it in million and billion. Every time a figure crosses between the two, write it in digits first and count them.
- Asked on the spot how big a crore is, do not answer "a lot". Say ten million, say a hundred lakh, and say how many digits that is.
- A trainee who cannot move between the two groupings will hand you a broken table. When a table looks odd, check the conversion before you check the arithmetic.
- When a quantity that cannot go below zero comes out negative, do not report it as the amount and do not round it to zero. Report that the figures do not add up. A mass, a count of people or a volume below zero means a figure, a step or a sign went wrong earlier. Or a rule was run past where it holds. Go back and find which.
- A calculator that shows the whole line follows the agreed order, and only on a line you type whole. A basic desk calculator does not follow it at all, so test yours with 3 plus 2 times 4. Press equals part way and you have chosen the order yourself. Type mixed sums as one line, with brackets round whatever must happen first.

**Exercise 1** (calculation). Section 50 of the Food Safety and Standards Act, 2006 sets a ceiling of five lakh rupees. A
proviso lowers it to twenty-five thousand rupees for small food businesses — petty retailers,
hawkers, temporary stalls and the like. Write both figures in digits, in both groupings. Then
say how many times larger the ceiling is than the proviso figure.

**Exercise 2** (critique). Here is a sentence from a report.

> The maximum penalty for a misleading food advertisement in India is one million rupees. That
> is about ten crore.

Find the mistake, and say which step it happened at.

**1.** In the number 90,807, say what each digit is worth. Then say how many digits the number has.

**2.** Work these out. 15 minus 40. 8 minus -5. -6 plus -9. -6 times -7. -36 divided by 4.

**3.** Write each of these in digits, twice: once in the Indian grouping and once in the
international one. Two lakh. Twelve lakh. Three crore.

**4.** Work these out in the agreed order. 5 plus 3 times 6. (5 plus 3) times 6. 20 divided by 4 times
5. 18 minus 6 divided by 3. Then say which of the four would give a different answer if you
worked strictly from left to right.

**5.** Which is larger, 90,90,000 or 9,900,000? Say how you decided, in one line.

**6.** A school kitchen has a budget of 3,50,000 rupees for a month and spends 4,20,000 rupees. Its
store starts the month with 40 sacks of rice, receives 25 sacks, and records 70 sacks issued.
All of these figures are made up for this problem. Work out the money left and the sacks left.
For each answer, say whether its sign makes sense.

**7.** Section 34(1) of the Consumer Protection Act, 2019 gives the District Commission complaints
worth up to one crore rupees. Section 47 gives the State Commission up to ten crore. Write both
in both groupings and count the digits in each.

**8.** The second schedule of the National Food Security Act, 2013 sets a lower primary meal at 450
calories. A school serves 1,200 of those meals in a week, and adds 50,000 calories of fruit.
The 1,200 meals and the 50,000 calories of fruit are made up for this problem. Write the total
as one line and work it out. Then say what a calculator shows if you press equals straight
after the first addition.

**9.** A district serves 1,00,000 lower primary meals. The second schedule of the National Food
Security Act, 2013 sets that meal at 450 calories. Work out the total calories. Write the
answer in digits in both groupings, and name it in both naming systems.

**10.** A colleague is checking two ceilings in the Food Safety and Standards Act, 2006. Section 53
sets ten lakh rupees for a misleading advertisement. Section 51 sets five lakh rupees for
sub-standard food. They want to know how many times larger the first one is. Here is what they
typed, and what came back.

```working
    10000000 divided by 500000 = 20
```

> The advertising ceiling is twenty times the sub-standard food ceiling.

Find the step that broke, and say why the answer looks reasonable.

**11.** A colleague wants the average number of meals served over two days: the two days added
together, then divided by 2. Monday had 1,150 meals and Tuesday 1,250. These figures are made
up for this problem. They type one line into a phone calculator, and here is what came back.

```working
    1150 plus 1250 divided by 2 = 1775
```

> The average is 1,775 meals a day.

Find the step that broke, and say why the answer looks reasonable.

**12.** A colleague adds three penalty ceilings — ten lakh, three lakh and five lakh — and reports the
total as "18,00,000, or about 1.8 crore". Find the step that broke and say what the total
should be called.

**13.** A ration shop's register shows 120 sacks of wheat at the start of the month, 30 sacks received
and 165 sacks issued. These figures are made up for this problem. A clerk works out the stock
at the end of the month.

```working
    120 plus 30 = 150
    150 minus 165 = 15
```

> Stock at the end of the month: 15 sacks.

Find the step that broke, and say why the wrong answer looks reasonable.

**14.** Here is a press line.

> India's food regulator can fine a company up to ten million rupees for a misleading food
> advertisement.

You have the Food Safety and Standards Act, 2006 open. Decide what to check, check it, then say
what your answer does not establish.

**15.** In a meeting somebody says this.

> Enrolment at the school changed by plus 300 last year and by minus 400 this year. So
> enrolment is now minus 100.

The figures are made up for this problem. Decide what to compute, compute it, and say what your
answer does not establish.

**16.** In a meeting somebody says this.

> The scheme costs 400 crore, which is about 4 billion rupees. That is roughly 4,000 rupees for
> each of the ten lakh people it reaches.

Decide what to compute, compute it, and say what your answer does not establish.

**17.** A note to a district office says this.

> Cost per child: 4,00,000 plus 2,00,000 divided by 400 children, which comes to 1,500 rupees a
> child.

The figures are made up for this problem. Decide what to compute, compute it, and say what your
answer does not establish.

