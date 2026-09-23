# D1 · What a probability is

**Definition.** A probability is a number from 0 to 1 that states how often an outcome would turn up if the
same chance process were repeated a great many times. It is the long-run relative frequency:
the fraction of all the tries in which it happened, as the tries go on and on. The complete list of everything
that could happen is the sample space. One member of that list is an outcome, and any collection
of outcomes from it is an event.

When every outcome in the sample space is equally likely, the probability of an event is the
count of outcomes in the event, divided by the count of outcomes in the whole sample space.

The complement of an event is every outcome in the sample space that is not in it. An event's
probability and its complement's probability always add to 1.

Call the probability of an event p, the letter p standing for probability. The odds of that
event are a different number, built from the same p. The odds are how many times more likely
the event is than its opposite: p divided by (1 minus p).
Probability and odds carry the same fact about the event and are not the same number.

**In plain terms.** A probability is a proportion. It is a part out of the whole it came from, never more than
one. Work it out before the draw, not after it.

A probability is a number that says how often something would happen if you could run the same
situation over and over. It always sits between 0, which means never, and 1, which means every
time.

Everything that could possibly happen is the sample space — the complete list of outcomes an
event could draw from. One thing that could happen is an outcome. A group of outcomes you care
about, such as "the number is even", is an event.

When every outcome is exactly as likely as every other, working out a probability is counting.
Count the outcomes that make your event true. Count every outcome there is. Divide the first by
the second.

The complement of an event is everything that is not it. Roll a die and call a six the event.
Everything else — one, two, three, four, five — is the complement. An event and its complement
cover the sample space between them, so their probabilities always add to 1.

Now the part that catches people, because you will meet it in many of the studies you read.
Alongside probability there is a second number for the same fact, called odds. Odds are how many
times more likely the event is than its opposite, not how likely it is. To get them, divide the
probability by 1 minus the probability — that is, by the complement.

A probability of 0.5 gives odds of 1, usually said as "evens" or "one to one". A probability of
0.75 gives odds of 3, said "three to one". Odds and probability agree on which way a chance
leans. They do not agree by how much, and the gap grows as the probability climbs toward 1.
Confusing the two is a common mistake in reading a medical paper. Many papers you will read
later report odds rather than probabilities. Learn to move between the two now.

**Illustration.** Go back to section 3(1) of the National Food Security Act, 2013. It set five kilograms of
foodgrains per person per month for a priority household. Read on to section 3(2), which sets
a ceiling on how many people that entitlement can reach. It shall extend up to seventy-five per
cent. of the rural population, and up to fifty per cent. of the urban population.

Pick one rural person, anywhere the Act covers, entirely at random. At random means every rural
person has exactly the same chance of being the one you pick. So the whole rural population is
your sample space, and the person you land on is your outcome.

Let A be the event that the person you pick is covered by the entitlement. Ask for P(A), said
"P of A", meaning the probability of A. P(A) is the p of the definition, for this particular
event.

You are not told how many people are actually covered, only the largest share the Act allows.
So work with 0.75 as a ceiling on P(A), not a measured figure, and carry that qualification
into every answer below.

```working
    P(A) is at most 0.75
```

Now the complement. Not being covered is everything else in the sample space.

```working
    1 minus 0.75 = 0.25
```

At least one rural person in four, on this reading of the Act, is not covered.

Now the trap. Turn 0.75 into odds: the probability divided by its complement.

```working
    0.75 divided by 0.25 = 3
```

The odds a random rural person is covered are, at most, three to one. Here that happens to
read the same as "three in four". That is exactly what makes the trap dangerous. It works once
and then stops working.

Watch it stop. The urban ceiling is fifty per cent. Turn that into odds the same way.

```working
    0.5 divided by 0.5 = 1
```

Odds of one to one, usually said "evens". A reader who hears "odds of one" as "always" has
read the odds as a probability. Odds of one mean half the time. Fifty per cent probability is
odds of one, not odds of fifty. And one hundred per cent probability is odds you cannot even
write down, because dividing by 1 minus 1 divides by zero.

Now go back the other way, because you will meet odds in print far more often than you will be
handed a probability. Suppose you read that the odds are two to one against — two to one that
the event does not happen. Odds "against" are the odds of the complement, so first flip them
round: odds of two to one against is odds of one-half in favour.

```working
    odds in favour = 1 divided by 2 = 0.5
```

Turn odds back into a probability by counting parts. Odds of 0.5 mean 0.5 parts for the event
to 1 part against it. Add those parts and there is one and a half parts in all. The
probability is the "for" part out of that total.

```working
    0.5 divided by 1.5 = 0.3333...
```

About a third. That is the rule in words: the probability is the "for" side of the odds,
divided by the "for" plus the "against". The event happens roughly one time in three, on this
figure, and nothing in the words "two to one against" told you that directly.

**Where this picture breaks.** Every probability above is a ceiling, not a measurement. The Act bounds how far the
entitlement can extend; it does not say how many people are actually receiving it in any one
district. Treat 0.75 as the largest the chance of being covered could be, and 0.25 as the
smallest the chance of not being covered could be. Say so whenever you quote a figure built
from them.

Odds and probability are almost the same number near 0: 0.01 gives odds of 0.0101. Near 1 they pull apart:
0.99 gives 99, and 0.999 gives 999.

**Must know points for you.**

- Odds of a figure are not the same as a probability of that figure. Reading "odds of 0.25" as a one-in-four chance is a common slip. Odds of 0.25 convert to a probability of 0.25 divided by 1.25, which is 0.2 — a one-in-five chance. Convert before you speak.
- Near 0, odds and probability are almost the same number. Above one half they pull apart, and near 1 they pull apart fast: 0.99 to 0.999 multiplies the odds by ten. Ask which end of the scale you are near before you trust a guess about the size of a change.
- A probability describes a group, or a process repeated many times. It does not describe the one person in front of you. Knowing that 0.75 of a population is covered by an entitlement tells you nothing about whether this particular person is one of them. Use the figure to plan for a group. Then go and check the individual case on its own.
- A statute's own words often give you a ceiling, marked "up to", rather than a measured figure. Every probability, complement and odds you compute from a ceiling is itself a ceiling. Say so in the same sentence you quote the number, or the reader will treat it as a count.
- When a journalist reads you an odds figure over the phone, do not repeat it as a percentage without converting it first. "Odds of three to one" means three chances in four. Say "three in four" and the journalist hears it right.

**Exercise 1** (teaching). A journalist calls about the National Food Security Act's rural ceiling. She says, "so the odds
of being covered are seventy-five per cent." You have three minutes and no jargon.

Correct the sentence, explain the difference between the two figures, and give the journalist
one sentence they can print.

**Exercise 2** (critique). A briefing paper contains this line: "The odds of coverage in this block are 60%."

Say what is wrong with the sentence, and rewrite it so the figure means something.

**1.** A bag holds 5 red balls and 3 blue balls, and nothing else. One ball is drawn at random.

Work out the probability of drawing red, and the probability of drawing blue. Check that they
add to 1.

**2.** An event has a probability of 0.2. Work out its odds.

Separately, an event has odds of three to two — that is, 1.5. Work out its probability.

**3.** An event has a probability of 0.4. Work out its complement, and then work out the odds.

**4.** Section 3(2) of the National Food Security Act, 2013 sets the entitlement's reach at up to 75
per cent of the rural population. Pick one rural person at random.

Work out the largest that the probability they are covered can be, and the smallest that the
probability they are not covered can be.

**5.** Use the rural ceiling of 0.75 from section 3(2) of the National Food Security Act, 2013. Work
out the odds, at most, that a randomly picked rural person is covered.

**6.** Section 3(2) of the National Food Security Act, 2013 sets the urban ceiling at up to 50 per
cent. Work out the odds, at most, of coverage in the urban population, and compare them with
the rural odds of three to one. Say what the comparison shows about how odds behave.

**7.** Here is a worked answer. Find the step that broke.

```working
    a report gives the odds of household coverage as 0.25
    odds of 0.25 mean a probability of 0.25
    so a quarter of households are covered
```

**8.** Here is a worked answer. Find the step that broke.

```working
    a probability of coverage is 0.6
    odds equal probability divided by 1 plus probability
    0.6 divided by 1.6 = 0.375
    so the odds of coverage are 0.375
```

**9.** A briefing note says: "Under the food security law, three in four rural people here are
covered."

Decide what to compute, compute it, and say what your answer does not establish.

