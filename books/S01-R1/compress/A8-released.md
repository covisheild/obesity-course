# A8 · Orders of magnitude and the back-of-envelope sanity check

**Definition.** The order of magnitude of a quantity is the power of ten nearest to it. Two quantities are of
the same order of magnitude when their ratio is smaller than about ten.

An order-of-magnitude estimate rounds every input to one significant figure, carries out the
arithmetic on the powers of ten, and claims the answer only to the nearest power of ten.

Its purpose is to test a figure, not to produce one.

**In plain terms.** Round every number in sight to one digit and a power of ten. Do the arithmetic on the powers of
ten, which is adding and subtracting small numbers. Then compare the answer against something
whose size you already know.

What you get back is not an answer. It is a verdict on somebody else's answer.

**Illustration.** Somebody asks you, in a meeting, roughly how much food energy a district's school meal programme
puts out in a year. You do not have the figures. Do it anyway, on paper, in front of them.

The second schedule of the National Food Security Act, 2013 sets a lower primary hot cooked meal
at 450 calories. Round it to one digit.

```working
    450 calories, to one digit: 5 times 10^2
```

Now the two numbers you do not have. Write each one down and mark it.

```working
    children in the district      1,00,000  =  10^5      <- a guess
    school days in a year         200       =  2 times 10^2   <- a guess
```

Multiply, working on the powers of ten.

```working
    5 times 10^2, times 10^5, times 2 times 10^2
    = (5 times 2) times 10^(2 plus 5 plus 2)
    = 10 times 10^9
    = 10^10 calories in a year
```

An estimate is only worth anything once you compare it against something.

So compare. About how much does one person eat in a year? Take two thousand calories a day and
mark it a guess as well.

```working
    2,000 a day  =  2 times 10^3      <- a guess
    365 days     =  4 times 10^2      (rounded to one digit)
    2 times 10^3, times 4 times 10^2 = 8 times 10^5, call it 10^6 calories a year
```

Now divide the programme by the person.

```working
    10^10 divided by 10^6 = 10^(10 minus 6) = 10^4
```

The programme delivers about as much food energy in a year as ten thousand people eat in a year.
Does that sound right for a lakh of children getting one meal on some of the days?

Check it roughly. One meal of 450 against a day of 2,000 is about a fifth. Two hundred school
days out of 365 is about half. A fifth of a half is a tenth, and a tenth of a lakh of children
is ten thousand. It agrees, so nothing has fallen over.

Now the failure, which is why anyone bothers with the second half. Suppose that while typing you
had put the district's children at ten lakh instead of one lakh.

```working
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

**Where this picture breaks.** This method is built to catch a factor of ten and it is blind to a factor of two. It answers one
question: is this number possible.

The method only works if the thing you compare against is one you actually know. Compare against
another estimate and you have two guesses agreeing with each other, which feels like
confirmation and is not.

And rounding to one digit cuts both ways. Round three numbers down and your answer is low by a
factor of two or three before you start.

**Must know points for you.**

- An order-of-magnitude estimate is not a rough version of the right answer. It is a different tool with a different job: deciding whether a number somebody else has given you is possible.
- Then compare the answer against a quantity whose size you already know. The comparison is not the last step. It is the step that does the work.
- Write down every number you supplied yourself and label it a guess, in the working, where somebody can argue with it.
- This catches an error of a factor of ten and never one of a factor of two. So it cannot be used to argue that an effect is big enough to matter.
- When a journalist reads you a figure on the phone, you can usually say within thirty seconds whether it is possible. Say exactly that and no more: whether it is possible, and what you assumed.
- Indian figures cross between lakh, crore and million inside one discussion, and this is where a power of ten goes missing.
- In a committee, an estimate offered with its assumptions written on the page is very hard to dismiss and very easy to improve. Someone will correct one of your guesses, which is the point.
- Asked to check a calculation under time pressure, do not redo it. Estimate it independently and see whether the two land on the same power of ten.

**Exercise 1** (calculation). A note claims that a state's school meal programme served 2 crore meals last year. Take the 450
calorie lower primary standard from the second schedule of the National Food Security Act, 2013.
Estimate the total food energy. Then estimate how many people's annual eating that represents.
Write down every assumption you make and mark it. Then say whether the claim of 2 crore meals is
possible for a state, and what you assumed to decide that.

**Exercise 2** (critique). A press note says a proposed scheme will "reach 12 crore children at a cost of 40 crore rupees a
year". Do an order-of-magnitude check on the cost per child and say what you conclude. Then say
what your check can and cannot establish.

**1.** Round each of these to one digit and a power of ten.

```working
    4,820      61       938,000      0.0037
```

**2.** Estimate each of these by rounding both numbers to one digit first. Then say, for the first
one, whether your estimate is above or below the true answer.

```working
    412 times 7,900        61,000 divided by 290
```

**3.** Two quantities are 4 times 10^6 and 9 times 10^7. Are they of the same order of magnitude? Show
the working that decides it.

**4.** Estimate the number of school meals served in one Indian district in a school year. Mark every
input you supply yourself, and give your answer to the nearest power of ten.

**5.** Section 3(1) of the National Food Security Act, 2013 gives 5 kilograms per person per month.
Estimate the tonnes a district needs in a year. Mark every input you supply, and say which one
your answer depends on most.

**6.** Here is a worked estimate. Find the step that broke.

```working
    3 times 10^4 households
    each getting 20 kilograms a month
    3 times 20 = 60
    so 60 times 10^4 = 6 times 10^4 kilograms a month
```

**7.** Here is a worked estimate. Find the step that broke.

```working
    a scheme covers 30 lakh people
    each is to get 2 kilograms of grain a month
    30 lakh = 3 million = 3 times 10^5
    3 times 10^5, times 2 = 6 times 10^5 kilograms a month
    = 600 tonnes a month
```

**8.** Here is a worked estimate. Find what is wrong with it, and it is not the arithmetic.

```working
    a district has about 10 lakh people          <- a guess
    about 2 per cent need the service            <- a guess
    each needs about 3 visits a year             <- a guess
    10^6 times 0.02 times 3 = 6 times 10^4 visits a year
```

**9.** Here is a worked estimate and the conclusion drawn from it. The arithmetic is right. Say what
is wrong with the conclusion.

```working
    district A   4 lakh households      <- a guess
                 3 visits each a year   <- a guess
                 4 times 10^5, times 3 = 1.2 times 10^6 visits
    district B   6 lakh households      <- a guess
                 3 visits each a year   <- a guess
                 6 times 10^5, times 3 = 1.8 times 10^6 visits
    so district B needs half as many staff again as district A
```

**10.** Here is a claim from a press note.

> The programme will provide 50 lakh children with a daily glass of milk for 200 days at a cost
> of 100 crore rupees.

Decide what to compute, compute it, and say what your answer does not establish.

**11.** A journalist reads you a figure over the phone and wants a comment in the next ten minutes.

> A new tax on sugary drinks will raise 40,000 crore rupees a year.

Decide what to compute, compute it, say what you would tell the journalist, and say what your
answer does not establish.

