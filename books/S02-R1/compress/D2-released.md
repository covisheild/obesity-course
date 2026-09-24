# D2 · Counting outcomes; independence

**Definition.** Tossing a coin n times has 2 to the power n outcomes, one factor of 2 for every toss.

Independence is checked, not assumed: A and B are independent exactly when P(A and B) — the
probability that A and B both happen — equals P(A) times P(B), and dependent otherwise. Where
no joint figure exists, the check is an argument that knowing one tells you nothing about the
other. If you can make neither, treat them as dependent. When they are independent, multiply
to get P(A and B).

When A and B cannot both happen — they are mutually exclusive — P(A or B), the probability
that at least one of A or B happens, equals P(A) plus P(B): add.

**In plain terms.** Toss a coin twice and write out every pair: heads-heads, heads-tails, tails-heads, tails-tails.
Four outcomes, because each toss has two and there are two tosses. Every extra toss doubles the
list. Two tosses give 2 squared outcomes. Three tosses give 2 cubed, which is 2 to the power 3,
and n tosses give 2 to the power n.

The word "and" points at multiplying, but only on one condition. The two events have to be
independent — meaning that finding out one of them happened tells you nothing new about the
other. Multiply their probabilities to get the probability of both.

The word "or" points at adding, and it too has a condition: the two events have to be mutually
exclusive, meaning they cannot both happen. If they can both happen, plain adding counts the
overlap twice, and the fix is to take the overlap back out once.

Never multiply two probabilities together just because a sentence has the word "and" in it. Check
first: does knowing one change the chance of the other?

**Illustration.** Section 3(1) of the National Food Security Act, 2013 entitles every person belonging to a
priority household to five kilograms of foodgrains a month. Section 3(2) caps how far that
entitlement reaches: up to 75 per cent of the rural population. Treat 0.75 as the probability,
at most, that a rural person picked at random is covered — the figure from the section before
this one.

Pick two rural people entirely at random, from two different, unrelated households. Knowing
whether the first is covered tells you nothing about the second, so treat the two as
independent. Multiply.

```working
    0.75 times 0.75 = 0.5625
```

At most 0.5625, so a little over half, that both are covered.

Now pick two people from the same household instead. If the household is covered, every person
belonging to it is covered along with it. The Act gives the entitlement to "every person
belonging to priority households". It is households that the State Government
identifies. The two outcomes are not independent, and
multiplying is the wrong move.

```working
    P(both covered, same household) is at most 0.75
```

Not 0.5625.

Pick three rural people, each from a different household, and ask for the probability that at
least one of them is covered. Go by the complement instead: work out the probability that none
of the three is covered, and subtract that from 1. If the three "covered" events are
independent, the three "not covered" events are too. So multiply the three "not covered"
chances. Each "1 minus" step turns a ceiling into a floor, or a floor into a ceiling.

```working
    1 minus 0.75 = 0.25
```

P(not covered) is at least 0.25.

```working
    0.25 times 0.25 = 0.0625
```

```working
    0.0625 times 0.25 = 0.015625
```

P(none covered) is at least 0.015625.

```working
    1 minus 0.015625 = 0.984375
```

P(at least one covered) is at most 0.984375. At most, about 98.4 per cent that at least one of the three is covered.

**Where this picture breaks.** Two people can look like two separate draws and actually be one draw, counted twice. Before
multiplying, name what would have to be true for the two events to be independent. Then check
whether it is.

"At most 0.5625" and "at most 98.4 per cent" are bounds built from a bound, not measured
figures. Every extra multiplication carries that same qualification forward. It does not
sharpen it.

**Must know points for you.**

- Independence is a checkable claim, not a default. Test it by asking whether P(A and B) equals P(A) times P(B).
- Two people drawn from the same unit that a decision is made about are almost never independent. Think of the same household, the same clinic, the same litter. This holds even when the underlying probability looks identical to two people drawn from different units. Ask what the decision was actually made about, before you multiply.
- The word "and" in a sentence is not permission to multiply, and the word "or" is not permission to add.
- "At least one of several things happens" is answered fastest through the complement. Work out the probability that none of them happen, and subtract from 1.
- Multiplying ceilings gives a ceiling, and multiplying floors gives a floor. Every "1 minus" step turns one into the other. Label each line "at most" or "at least" as you go.
- When you teach this to a trainee, put the independence check before the arithmetic every time, even in a case where it is obviously true.

**Exercise 1** (critique). A colleague claims that the chance two randomly chosen rural residents are both covered is
0.75 times 0.75, which is 0.5625. No further detail about the two residents is given.

Say what is missing from the claim before it can be checked. Then say what changes if it turns
out the two residents live in the same household.

**Exercise 2** (teaching). A first-year resident keeps multiplying probabilities together whenever a question uses the
word "and". You have ten minutes and a whiteboard.

Teach them the actual test for independence, so they leave able to catch themselves the next
time they reach for multiplication.

**1.** A coin is tossed 3 times. List every outcome, and say how many there are.

**2.** Event A has a probability of 0.6 and event B has a probability of 0.5, and A and B are
independent. Work out P(A and B).

Separately, event C has a probability of 0.3 and event D has a probability of 0.4, and C and D
are mutually exclusive. Work out P(C or D).

**3.** Two independent events each have a probability of 0.2. Work out the probability that at least
one of them happens.

**4.** You are told P(A) = 0.5, P(B) = 0.4 and P(A and B) = 0.2. Check whether A and B are
independent.

**5.** Two fair coins, each equally likely to land heads or tails, are tossed. Let A be the event that the first toss is heads, and B be the event
that the second toss is heads. List the sample space, then check whether A and B are
independent by counting outcomes.

**6.** Under section 3(2) of the National Food Security Act, 2013, the rural coverage ceiling is 0.75.
Pick two rural people at random from two different, unrelated households.

Work out the probability, at most, that both are covered.

**7.** Now pick two rural people from the same household. Using the same 0.75 ceiling, work out the
probability, at most, that both are covered. Then compare your answer with the previous
problem's.

**8.** Pick three rural people at random, each from a different household. Use the 0.75 coverage
ceiling from section 3(2) of the National Food Security Act, 2013.

Work out the probability, at most, that at least one of the three is covered.

**9.** Here is a worked answer. Find the step that broke.

```working
    event A has a probability of 0.7, event B has a probability of 0.6, and they are independent
    the probability of A or B happening is P(A) plus P(B)
    0.7 plus 0.6 = 1.3
    so P(A or B) is 1.3
```

**10.** Here is a worked answer. Find the step that broke.

```working
    two rural people are picked from the same household
    the coverage ceiling is 0.75 for each person
    P(both covered) = 0.75 times 0.75
    0.75 times 0.75 = 0.5625
    so at most 0.5625 of same-household pairs have both people covered
```

**11.** Here is a worked answer. Find the step that broke.

```working
    three rural people are picked, each from a different household, coverage ceiling 0.75 each
    the probability that at least one is covered is found by adding the three probabilities
    0.75 plus 0.75 plus 0.75 = 2.25
    so at most 2.25 of the three are covered, meaning it is virtually certain at least one is
```

**12.** A note says: "Two rural residents are picked at random; the chance both are covered is
0.5625."

Decide what has to be true for that figure to be correct, and say what your answer does not
establish.

**13.** A district report says coverage is up to 75 per cent of the rural population. Pick one rural
person at random. They live in a household of four. The report concludes that the chance at
least one member of that household is not covered is high.

Decide what to compute, compute it, and say what your answer does not establish.

