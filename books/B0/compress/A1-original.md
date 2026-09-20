### A1 · Counting, place value, and what a calculator is actually doing

*B0-R0-C01 · derivable*

**Definition.** A number written in digits carries two things at once: which digits were used, and the place
each one occupies. The place fixes what the digit is worth. In 4,505 the two fives stand for
five hundred and for five.

Each place is worth ten times the place immediately to its right. That is the whole of what a
written number means, and it is why the system is called base ten.

Grouping the digits with commas is a separate matter, and it is not done the same way
everywhere. The Indian system groups the last three digits together and every pair above that,
naming them thousand, lakh and crore. The international system groups in threes throughout,
naming them thousand, million and billion. One number, two groupings: 10,00,000 and 1,000,000.

A calculator applies base ten faster than a person can. It does not check what was typed into
it, and it holds no view on whether the answer it returns is possible.

**In plain terms.** Write a number down and two things decide what it means. Which digits you used, and where you put
them.

Take 4,505. There are two fives in it, and one of them is worth five hundred while the other is
worth five. Nothing about the digit 5 tells you that. Its place does. Move one step to the left
and a digit is worth ten times as much. That is the whole rule.

Now the part that catches people in India. Where you put the commas is a different question from
what the digits are worth. And India does not do it the way most places do. Here the last three
digits go together and everything above that is grouped in pairs: 10,00,000. In most other places
they run in threes all the way along: 1,000,000. Same number, same value, different commas.

The names follow the commas. India counts thousand, lakh, crore. Most other places count
thousand, million, billion. One lakh is a hundred thousand and one crore is ten million, so the
two ladders never line up. That is where the mistakes come from.

A calculator does base ten for you, fast and without complaint, but it cannot read your mind.
Type one zero too many and it will work the sum out correctly and hand you an answer ten times
too big.

**Illustration.** Open `sources/fss_act_2006.txt`, which is the Food Safety and Standards Act, 2006. Search inside
it for "misleading advertisement".

The first hit is not what you want, and it is worth knowing why. Every Indian Act opens with a
list of its section names, so your first hit is the line `53. Penalty for misleading
advertisement` in that list. It names the section and carries no figure. Search again and take
the second hit, which is section 53 itself.

Now read what it says the penalty may extend to. It says ten lakh rupees. Write that in digits, the Indian way, and then the international way.

```
    10,00,000      1,000,000
```

Count the zeros in each. Five, and five. The number has not changed. Only the commas moved.

Now watch the mistake happen, because it is worth seeing once. Somebody reading the Act writes a
note in English for a reader abroad. Ten lakh, they think, and lakh sounds like million. So ten
lakh becomes ten million, and they type this.

```
    1,00,00,000
```

Look at what they have done. Ten million is one crore. They have multiplied the penalty by ten,
in a note that other people will quote back at them.

The slow way stops it. Say the number out loud in the naming system you are writing in. Ten lakh
is one million. One crore is ten million. A lakh is a hundred thousand, and a crore is a hundred
lakh, so the two ladders step at different places.

Now a clean case, so you can feel the difference. Search the same file for "Penalty for
sub-standard food". The contents list comes up first again, and the section itself is the second
hit. That is the pattern in every Act, so expect it from now on.

Section 51 caps that penalty at five lakh rupees. Five lakh is five hundred thousand. Write it
both ways.

```
    5,00,000      500,000
```

Six digits each time. They agree, so no place has slipped.

Last, the calculator. Section 53's ceiling is ten lakh and section 51's is five lakh. Type one
million, then divide by five hundred thousand, and it returns 2. That is right: the first
ceiling is twice the second. Now type it again and leave one zero off the second number. It
returns 20.

The calculator did not object either time, and it never will. Checking the question is your job.
Counting the digits before you press equals is how you do it.

**Where this picture breaks.** Place value is a rule about writing numbers down. It tells you what 10,00,000 means. It tells you
nothing about whether ten lakh rupees is a large penalty or a small one. It tells you nothing
about whether anybody has ever been made to pay it.

The commas break in a second way, and quietly. A spreadsheet or a website prints the grouping it
was built for, and does not say which one that is. So count the digits, not the commas. Where the
two disagree, the digits are right.

A calculator is only as good as what you typed. It does not know what the number is about. It
will divide a sum of money by a count of children and hand you an answer. That answer is
arithmetic rather than sense.

One thing about the figures themselves. They are what this copy of the Act says, and the copy in
`sources/` names no change to it after 2008. A later section of this book teaches you how to
check whether a copy of a law is up to date. Until then, treat these as the numbers in this
file rather than as the penalties in force today.

**Must know points for you.**

- A lakh is not a million. One lakh is a hundred thousand. One crore is ten million. A note that slides from one ladder to the other is wrong by a factor of ten. That is the size of error nobody spots in a table, because every digit in it still looks reasonable.

- Before you press equals, count the digits in each number you typed. Then say the number out loud, in the naming system you are writing in. Two habits, a few seconds, and between them they catch the whole class of error above.

- Indian statutes, budgets and ministry papers state money in lakh and crore. Journals and international agencies state it in million and billion. Every time a figure crosses between the two, write it in digits first and count them. That is the only step where the mistake is visible.

- Asked on the spot how big a crore is, do not answer "a lot". Say ten million, say a hundred lakh, and say how many digits that is. A number you can place immediately is the difference between being quoted and being talked over.

- A trainee who cannot move between the two groupings will hand you a broken table. It will be right in one column and ten times wrong in the next. When a table looks odd, check the conversion before you check the arithmetic. The arithmetic is usually fine.

- This gets you to what a written number means and no further. It does not tell you whether the number is right, how it was counted, or whether the thing it counts is worth caring about.


**Exercise B0-R0-C01-E1** (calculation). Section 50 of the Food Safety and Standards Act, 2006 sets a ceiling of five lakh rupees. A
proviso lowers it to twenty-five thousand rupees for small food businesses — petty retailers,
hawkers, temporary stalls and the like. Write both figures in digits, in both groupings. Then
say how many times larger the ceiling is than the proviso figure.

*Record your confidence as a percentage before turning to the answer.*

**Exercise B0-R0-C01-E2** (critique). Here is a sentence from a report.

> The maximum penalty for a misleading food advertisement in India is one million rupees. That
> is about ten crore.

Find the mistake, and say which step it happened at.

**Practice.** Ten problems on this technique, easiest first. Work them on paper. The answers are in the appendix at the back, under these numbers.

**B0-R0-C01-P01.** In the number 90,807, say what each digit is worth. Then say how many digits the number has.

**B0-R0-C01-P02.** Write each of these in digits, twice: once in the Indian grouping and once in the
international one. Two lakh. Twelve lakh. Three crore.

**B0-R0-C01-P03.** Which is larger, 90,90,000 or 9,900,000? Say how you decided, in one line.

**B0-R0-C01-P04.** Section 21(2) of the Consumer Protection Act, 2019 caps a penalty for a false or misleading
advertisement at ten lakh rupees. A proviso raises it to fifty lakh for a repeat. Write both
figures in both groupings, then say how many times larger the second is.

**B0-R0-C01-P05.** Section 34(1) of the Consumer Protection Act, 2019 gives the District Commission complaints
worth up to one crore rupees. Section 47 gives the State Commission up to ten crore. Write both
in both groupings and count the digits in each.

**B0-R0-C01-P06.** A district serves 1,00,000 lower primary meals. The second schedule of the National Food
Security Act, 2013 sets that meal at 450 calories. Work out the total calories. Write the
answer in digits in both groupings, and name it in both naming systems.

**B0-R0-C01-P07.** Here is a line from a note. Find the step that broke.

> The repeat ceiling is fifty lakh rupees, which is 5,000,000, or five crore.

**B0-R0-C01-P08.** A colleague adds three penalty ceilings — ten lakh, three lakh and five lakh — and reports the
total as "18,00,000, or about 1.8 crore". Find the step that broke and say what the total
should be called.

**B0-R0-C01-P09.** Here is a press line.

> India's food regulator can fine a company up to ten million rupees for a misleading food
> advertisement.

You have the Food Safety and Standards Act, 2006 open. Decide what to check, check it, then say
what your answer does not establish.

**B0-R0-C01-P10.** In a meeting somebody says this.

> The scheme costs 400 crore, which is about 4 billion rupees. That is roughly 4,000 rupees for
> each of the ten lakh people it reaches.

Decide what to compute, compute it, and say what your answer does not establish.
