### A8 · Orders of magnitude and the back-of-envelope sanity check

*B0-R0-C08 · derivable*

**Definition.** The order of magnitude of a quantity is the power of ten nearest to it. Two quantities are of
the same order of magnitude when their ratio is smaller than about ten.

An order-of-magnitude estimate rounds every input to one significant figure, carries out the
arithmetic on the powers of ten, and claims the answer only to the nearest power of ten. Its
output is a range rather than a value.

Its purpose is to test a figure, not to produce one. An estimate of this kind detects an error
of a factor of ten or more and cannot detect an error of a factor of two.

Every input that was assumed rather than obtained is recorded as an assumption, because the
result is a claim about the arithmetic and about those assumptions jointly, and about nothing
else.

**In plain terms.** Somebody reads you a number over the phone and asks what you think. You have no data and thirty
seconds. There is still something you can do.

Round every number in sight to one digit and a power of ten. Do the arithmetic on the powers of
ten, which is adding and subtracting small numbers. Then compare the answer against something
whose size you already know.

What you get back is not an answer. It is a verdict on somebody else's answer. It comes in one of
three forms: that figure is about right, that figure is impossible, or I cannot tell.

Being about right here is a loose thing. This method catches a number that is out by a factor of
ten or a hundred. It will never catch one that is out by a factor of two, and pretending
otherwise is the way it gets misused.

The discipline that makes it honest is one line long. Every number you supplied yourself gets
written down and labelled a guess. Not kept in your head — written down, in the working, where
anybody can see it and argue with it. An estimate is a claim about the arithmetic and about your
guesses together. Hide the guesses and you have turned an argument into a fact.

**Illustration.** Somebody asks you, in a meeting, roughly how much food energy a district's school meal
programme puts out in a year. You do not have the figures. Do it anyway, on paper, in front of
them.

Start with what you can stand behind. The second schedule of the National Food Security Act,
2013 sets a lower primary hot cooked meal at 450 calories. Round it to one digit.

```
    450 calories, to one digit: 5 times 10^2
```

Now the two numbers you do not have. Write each one down and mark it.

```
    children in the district      1,00,000  =  10^5      <- a guess
    school days in a year         200       =  2 times 10^2   <- a guess
```

Multiply, working on the powers of ten.

```
    5 times 10^2, times 10^5, times 2 times 10^2
    = (5 times 2) times 10^(2 plus 5 plus 2)
    = 10 times 10^9
    = 10^10 calories in a year
```

Ten thousand million calories, which is a thousand crore. That number means nothing on its own,
and that is the point people miss. An estimate is only worth anything once you compare it against something.

So compare. About how much does one person eat in a year? Take two thousand calories a day and
mark it a guess as well.

```
    2,000 a day  =  2 times 10^3      <- a guess
    365 days     =  4 times 10^2      (rounded to one digit)
    2 times 10^3, times 4 times 10^2 = 8 times 10^5, call it 10^6 calories a year
```

Now divide the programme by the person.

```
    10^10 divided by 10^6 = 10^(10 minus 6) = 10^4
```

The programme delivers about as much food energy in a year as ten thousand people eat in a
year. Does that sound right for a lakh of children getting one meal on some of the days?

Check it roughly. One meal of 450 against a day of 2,000 is about a fifth. Two hundred school
days out of 365 is about half. A fifth of a half is a tenth, and a tenth of a lakh of children
is ten thousand. It agrees, so nothing has fallen over.

Now the failure, which is why anyone bothers with the second half. Suppose that while typing you
had put the district's children at ten lakh instead of one lakh.

```
    10^6 children instead of 10^5
    answer becomes 10^11 calories
    10^11 divided by 10^6 = 10^5
```

A hundred thousand people's worth of annual eating, from school meals, in one district. Hold
that against a district population of a few lakh and it cannot be right. The school meals would
be feeding a large part of everybody, all year, on one meal a day for part of the week.

Notice what caught it. Not the arithmetic, which was faultless both times. The comparison
against something whose size you already knew. That is the whole method, and the first half of
it is useless without the second.

Last, what you say out loud when you have done this. Not "it is ten to the ten". Say something
like this.

> On a rough calculation this comes out around the amount ten thousand people eat in a year. I
> assumed a lakh of children and two hundred school days. If it is wrong by a factor of ten,
> one of those assumptions is wrong and I want the real figures.

**Where this picture breaks.** This method is built to catch a factor of ten and it is blind to a factor of two. So it can
never settle an argument about whether an effect is large enough to matter, and reaching for it
in that argument is misuse. It answers one question: is this number possible.

The comparison is where it can go quietly wrong. The method only works if the thing you compare
against is one you actually know. Compare against another estimate and you have two guesses
agreeing with each other, which feels like confirmation and is not.

And rounding to one digit cuts both ways. Round three numbers down and your answer is low by a
factor of two or three before you start. That is inside the tolerance of the method, which is
why the answer is stated as "around" and never with a second digit. The moment somebody writes
your estimate down as a figure with two digits after the point, it has stopped being an
estimate. Nobody will have noticed.

**Must know points for you.**

- An order-of-magnitude estimate is not a rough version of the right answer. It is a different tool with a different job: deciding whether a number somebody else has given you is possible. Using it to produce a figure for a document is the misuse to watch for in yourself.

- Round every input to one digit and a power of ten. Do the arithmetic on the exponents. Then compare the answer against a quantity whose size you already know. The comparison is not the last step. It is the step that does the work.

- Write down every number you supplied yourself and label it a guess, in the working, where somebody can argue with it. An estimate is a claim about the arithmetic and about your assumptions jointly, and an unlabelled assumption turns it into a claim about the world.

- This catches an error of a factor of ten and never one of a factor of two. So it cannot be used to argue that an effect is big enough to matter. Anyone who uses it that way, including you, should be stopped.

- When a journalist reads you a figure on the phone, you can usually say within thirty seconds whether it is possible. Say exactly that and no more: whether it is possible, and what you assumed. It is far more useful to them than a refusal and far safer than agreement.

- Indian figures cross between lakh, crore and million inside one discussion, and this is where a power of ten goes missing. Doing the estimate in powers of ten rather than in names is what stops it, because 10^5 and 10^7 cannot be confused by ear.

- In a committee, an estimate offered with its assumptions written on the page is very hard to dismiss and very easy to improve. Someone will correct one of your guesses, which is the point. An estimate offered without them is a number that can only be believed or disbelieved.

- Asked to check a calculation under time pressure, do not redo it. Estimate it independently and see whether the two land on the same power of ten. Redoing somebody's arithmetic repeats their assumptions; estimating it does not.


**Exercise B0-R0-C08-E1** (calculation). A note claims that a state's school meal programme served 2 crore meals last year. Take the 450
calorie lower primary standard from the second schedule of the National Food Security Act, 2013.
Estimate the total food energy. Then estimate how many people's annual eating that represents.
Write down every assumption you make and mark it. Then say whether the claim of 2 crore meals is
possible for a state, and what you assumed to decide that.

*Record your confidence as a percentage before turning to the answer.*

**Exercise B0-R0-C08-E2** (critique). A press note says a proposed scheme will "reach 12 crore children at a cost of 40 crore rupees a
year". Do an order-of-magnitude check on the cost per child and say what you conclude. Then say
what your check can and cannot establish.

**Practice.** Ten problems on this technique, easiest first. Work them on paper. The answers are in the appendix at the back, under these numbers.

**B0-R0-C08-P01.** Round each of these to one digit and a power of ten.

```
    4,820      61       938,000      0.0037
```

**B0-R0-C08-P02.** Estimate each of these by rounding both numbers to one digit first. Then say, for the first
one, whether your estimate is above or below the true answer.

```
    412 times 7,900        61,000 divided by 290
```

**B0-R0-C08-P03.** Two quantities are 4 times 10^6 and 9 times 10^7. Are they of the same order of magnitude? Show
the working that decides it.

**B0-R0-C08-P04.** The second schedule of the National Food Security Act, 2013 sets an upper primary meal at 700
calories. Estimate the calories a school of 600 children receives across 200 school days. Mark
every input you were not given.

**B0-R0-C08-P05.** Estimate the number of school meals served in one Indian district in a school year. Mark every
input you supply yourself, and give your answer to the nearest power of ten.

**B0-R0-C08-P06.** Section 3(1) of the National Food Security Act, 2013 gives 5 kilograms per person per month.
Estimate the tonnes a district needs in a year. Mark every input you supply, and say which one
your answer depends on most.

**B0-R0-C08-P07.** Here is a worked estimate. Find the step that broke.

```
    3 times 10^4 households
    each getting 20 kilograms a month
    3 times 20 = 60
    so 60 times 10^4 = 6 times 10^4 kilograms a month
```

**B0-R0-C08-P08.** Here is a worked estimate. Find what is wrong with it, and it is not the arithmetic.

```
    a district has about 10 lakh people          <- a guess
    about 2 per cent need the service            <- a guess
    each needs about 3 visits a year             <- a guess
    10^6 times 0.02 times 3 = 6 times 10^4 visits a year
```

**B0-R0-C08-P09.** Here is a claim from a press note.

> The programme will provide 50 lakh children with a daily glass of milk for 200 days at a cost
> of 100 crore rupees.

Decide what to compute, compute it, and say what your answer does not establish.

**B0-R0-C08-P10.** A journalist reads you a figure over the phone and wants a comment in the next ten minutes.

> A new tax on sugary drinks will raise 40,000 crore rupees a year.

Decide what to compute, compute it, say what you would tell the journalist, and say what your
answer does not establish.
