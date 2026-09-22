# A1 · Counting, place value, and what a calculator is actually doing

**Definition.** A number written in digits carries two things at once: which digits were used, and the place
each one occupies. The place fixes what the digit is worth.

Each place is worth ten times the place immediately to its right. That is the whole of what a
written number means, and it is why the system is called base ten.

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

**Where this picture breaks.** Place value is a rule about writing numbers down. It tells you nothing about whether ten lakh
rupees is a large penalty or a small one.

The commas break in a second way, and quietly. A spreadsheet or a website prints the grouping it
was built for, and does not say which one that is. So count the digits, not the commas. Where
the two disagree, the digits are right.

A calculator is only as good as what you typed. It will divide a sum of money by a count of
children and hand you an answer. That answer is arithmetic rather than sense.

**Must know points for you.**

- A lakh is not a million. One lakh is a hundred thousand. One crore is ten million.
- Before you press equals, count the digits in each number you typed. Then say the number out loud, in the naming system you are writing in.
- Indian statutes, budgets and ministry papers state money in lakh and crore. Journals and international agencies state it in million and billion. Every time a figure crosses between the two, write it in digits first and count them.
- Asked on the spot how big a crore is, do not answer "a lot". Say ten million, say a hundred lakh, and say how many digits that is.
- A trainee who cannot move between the two groupings will hand you a broken table. When a table looks odd, check the conversion before you check the arithmetic.

**Exercise 1** (calculation). Section 50 of the Food Safety and Standards Act, 2006 sets a ceiling of five lakh rupees. A
proviso lowers it to twenty-five thousand rupees for small food businesses — petty retailers,
hawkers, temporary stalls and the like. Write both figures in digits, in both groupings. Then
say how many times larger the ceiling is than the proviso figure.

**Exercise 2** (critique). Here is a sentence from a report.

> The maximum penalty for a misleading food advertisement in India is one million rupees. That
> is about ten crore.

Find the mistake, and say which step it happened at.

**1.** In the number 90,807, say what each digit is worth. Then say how many digits the number has.

**2.** Write each of these in digits, twice: once in the Indian grouping and once in the
international one. Two lakh. Twelve lakh. Three crore.

**3.** Which is larger, 90,90,000 or 9,900,000? Say how you decided, in one line.

**4.** Section 34(1) of the Consumer Protection Act, 2019 gives the District Commission complaints
worth up to one crore rupees. Section 47 gives the State Commission up to ten crore. Write both
in both groupings and count the digits in each.

**5.** A district serves 1,00,000 lower primary meals. The second schedule of the National Food
Security Act, 2013 sets that meal at 450 calories. Work out the total calories. Write the
answer in digits in both groupings, and name it in both naming systems.

**6.** A colleague is checking two ceilings in the Food Safety and Standards Act, 2006. Section 53
sets ten lakh rupees for a misleading advertisement. Section 51 sets five lakh rupees for
sub-standard food. They want to know how many times larger the first one is. Here is what they
typed, and what came back.

```working
    10000000 divided by 500000 = 20
```

> The advertising ceiling is twenty times the sub-standard food ceiling.

Find the step that broke, and say why the answer looks reasonable.

**7.** A colleague adds three penalty ceilings — ten lakh, three lakh and five lakh — and reports the
total as "18,00,000, or about 1.8 crore". Find the step that broke and say what the total
should be called.

**8.** Here is a press line.

> India's food regulator can fine a company up to ten million rupees for a misleading food
> advertisement.

You have the Food Safety and Standards Act, 2006 open. Decide what to check, check it, then say
what your answer does not establish.

**9.** In a meeting somebody says this.

> The scheme costs 400 crore, which is about 4 billion rupees. That is roughly 4,000 rupees for
> each of the ten lakh people it reaches.

Decide what to compute, compute it, and say what your answer does not establish.

