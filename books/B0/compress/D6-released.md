# D6 · Sampling: how a part can tell you about a whole

**Definition.** A parameter is a number that describes the population, if every member of it could be measured.
A statistic is the same kind of number, computed instead from a sample.

A random sample is picked at random: every member of the population has exactly the same chance
of being the one picked, and an actual chance process decides it, not the person picking. A
convenience sample is built the other way, out of whoever happens to be available, and the
chance that any one member of the population ends up in it is neither equal nor known.

Draw a second random sample of the same size from the same population and its statistic will
not match the first sample's exactly. This is sampling variation.

Take the average of a random sample. Over many samples of the same size, that average has its
own spread, meaning its standard deviation as the section on average and spread taught it. The
square-root law states that this spread equals the spread of the individual values in the
population, divided by the square root of the sample size. Multiplying the sample size by four
divides that spread by two. This spread does not depend on how big the population is, only on
how big the sample is. Papers name this spread the standard error of the mean.

The square-root law describes how far a random sample's average is likely to sit from the
average of the population it was actually drawn from. It says nothing about whether that
population is the one the sample was meant to stand for. Enlarging the sample does not close
that gap.

**In plain terms.** Call the whole group a question is about the population. Call the part of that group that was actually measured the sample.

A number that describes the whole population exactly is called a parameter. You could only get it by measuring everyone,
which is usually too slow, too costly or simply impossible. A number worked out the same way from your sample is called a
statistic. Since a sample is not the whole population, a statistic is not the parameter. It is an estimate of it, a number
made from part of the group and used to stand in for the whole.

A random sample is picked at random: every member of the population has exactly the same chance of being the one picked. A
convenience sample is whoever happens to be available: volunteers, people who answered an advertisement, the first hundred
people through a door. Nothing forces a convenience sample to look like the population it gets used to describe.

Draw one random sample of a hundred people and work out its average. Draw a second random sample of a hundred different
people, from the same population, the same way, and work out its average too. The two averages will not be the same number.
This bouncing around from sample to sample is called sampling variation, and every sample has it.

Take a sample four times the size, and the bounce in its average shrinks to half of what it was. This is the square-root law.
A paper that reports this spread usually calls it the standard error of the mean.

Suppose a convenience sample of volunteers is not representative of the group it is meant to describe. No amount of enlarging
it brings it any closer.

Sample size protects you against sampling variation. It buys you nothing against a sample that was never random to begin
with.

**Illustration.** Kiran and colleagues did the study you have already met three times.

Before recruiting anyone, they set their target using a figure from the National Family Health Survey, NFHS-4, run in 2015-16. The study itself ran in July to
September 2019. The paper gives the prevalence of overweight as 19 per cent in men and 21 per cent in women. It reports these as NFHS-4's figures for India, without
saying which ages or which people they cover. The authors rounded them to a planning figure of 20 per cent to size their study. NFHS-4's figures are themselves a
survey result that reaches this book second-hand, through the paper, not a fixed truth.

They measured a sample: 282 medical students at one college in Mangaluru who came forward after the study was announced on campus. Nobody drew these 282 by chance.

They chose to come forward, from the one college that was convenient to the researchers.

Table 2 puts 83 of the 282 students at a body-mass index of 25 to 29.9, and another 15 at 30 or more. Add the two bands together.

```working
    83 plus 15 = 98
    98 divided by 282 = 0.3475177305
```

Ninety-eight of the 282 students, about 34.8 per cent, had a body-mass index of 25 or more. The gap between that and the 20 per cent planning figure is about 14.8
percentage points.

Take the population made of these eight numbers: 2, 4, 4, 4, 5, 5, 7, 9. Work out its mean the way the section on average and spread taught.

```working
    2 plus 4 plus 4 plus 4 plus 5 plus 5 plus 7 plus 9 = 40
    40 divided by 8 = 5
```

Now its spread, the same way: each value's distance from 5, squared, then averaged, then square-rooted.

```table
value   distance from 5   squared
2       -3                9
4       -1                1
4       -1                1
4       -1                1
5       0                 0
5       0                 0
7       2                 4
9       4                 16
```

```working
    9 plus 1 plus 1 plus 1 plus 0 plus 0 plus 4 plus 16 = 32
    32 divided by 8 = 4
    square root of 4 = 2
```

This is the whole population, not a sample from it, so the division is by 8, the full count, not by 7. This population's spread is 2.

Draw a sample of four numbers from it, one at a time, putting each one back before the next draw. Here are three such samples.

```table
sample                  numbers        sum   mean
first sample of four    5, 4, 7, 2     18    4.5
second sample of four   4, 4, 5, 2     15    3.75
third sample of four    4, 2, 4, 7     17    4.25
```

That bouncing around is sampling variation. The square-root law says how big it typically is: divide the population's spread, 2, by the square root of the sample size,
which is 2.

```working
    2 divided by 2 = 1
```

For samples of four, the law predicts a spread of 1 around the true mean of 5.

Now return to the medical students. Suppose the 282 had instead been drawn at random from young adults, the group the paper set out to study. The square-root law would
then say something concrete.

They were not drawn at random. They were students at one college who chose to come forward.

Nothing in this arithmetic can say which of several things produced the 14.8-point gap. It could be that these are medical students at one college. It could be the
years between when NFHS-4 was measured and when the study ran. It could simply be who chose to volunteer. Size cannot settle that question.

**Where this picture breaks.** A real population's spread is usually not known in advance. Papers estimate it from the same
sample they are using. That estimate adds its own extra uncertainty, which this demonstration
does not show.

Real surveys never ask the same person twice, so they sample without replacement. That matters
only when the sample is a large share of a small population, such as one village. There the
scatter is a little less than the law predicts.

**Figure.** Each bar counts how many of 5,000 sample means landed there. Top: samples of 10. Bottom: samples of 40, four times bigger. Both crowd around the population mean of 5, and the bottom crowd is half as wide, 0.317 against 0.633, which is the square-root law happening rather than being stated. The draw was made by computer from the eight numbers 2, 4, 4, 4, 5, 5, 7 and 9, each put back after it was drawn.

*What the figure shows:* Two histograms on the same horizontal scale, one above the other. The top one, for samples of 10, runs from 3 to about 7.6. The bottom one, for samples of 40, is taller and about half as wide, from 4 to about 6.2. Both are centred on a vertical line at 5.

**Must know points for you.**

- A bigger sample is not a repair for a biased one. Enlarging a convenience sample tightens its estimate of whatever population it actually came from.
- Before trusting a report's sample size, ask how the people in it were found. A small random sample can outperform a huge convenience sample.
- Kiran and colleagues' 282 medical students gave 34.8 per cent with a body-mass index of 25 or more, worked out from Table 2. The planning figure the authors rounded from NFHS-4 was 20 per cent. Size alone cannot tell you what made the two figures differ.
- The square-root law describes only how a random sample's answer scatters around the population it was actually drawn from. Quoting it does not rescue a sample that was never random.
- Halving the scatter of a sample's average costs four times as many people, every time.
- Teach a trainee to name the intended population before looking at a study's sample size. If they cannot say who a convenience sample leaves out, they have not learned the part of this that matters.

**Exercise 1** (critique). A hospital's social media post reads: "We surveyed 4,000 followers and found 60 per cent
support a new clinic timing. With a sample this large, the result is extremely reliable."

Say what the sample size claim gets right and what it leaves out.

**Exercise 2** (teaching). A first-year resident says a colleague's finding "must be right because they had a huge sample
size." You have ten minutes and a whiteboard.

Teach them the difference between a sample being big and a sample being random.

**1.** A population has a spread (standard deviation) of 10. Work out the spread of the average of a
sample of size 4 from it.

**2.** A population has a spread of 8. Work out the spread of the average of a sample of size 16.
Then work out the spread of the average of a sample of size 64, and say what happened to it.

**3.** A population has a spread of 15. What sample size gives a sample average with a spread of 3?

**4.** Kiran and colleagues report a standard deviation of 3.9 kg/m² for body-mass index among the 131
men in their sample (Table 1). Suppose a fresh sample of 25 men is drawn from a population with
that same spread. Work out the spread of that sample's average body-mass index.

**5.** Kiran and colleagues report a body-mass index spread of 3.9 kg/m² for the men in their own
sample. Suppose a random sample of 131 men is drawn from a population with that same spread.
Work out the spread of the sample average. Then say what the spread would be for a fresh sample
of 524 men from the same population.

**6.** Suppose a population's spread for body-mass index is 3.9 kg/m². What sample size would bring
the spread of the sample average down to 0.1 kg/m²?

**7.** A colleague writes in a report: "Kiran and colleagues' men have a mean body-mass index of 24.2
kg/m². The standard deviation is 3.9. So the true mean for the population lies between 20.3
and 28.1."

Find the step that broke.

**8.** Here is a worked answer. Find the step that broke.

```working
    a population has a spread of 50
    a sample of 100 has a spread of 50 divided by square root of 100, which is 5
    doubling the sample to 200 should halve the spread
    so the new spread is 5 divided by 2, which is 2.5
```

**9.** Here is a note passed round a department.

```working
    Kiran and colleagues found 98 of 282 medical students, 34.8%, at a body-mass index of 25 or more
    NFHS-4 gives 20% for young adults nationally
    a sample four times the size, 1,128, would have half the sampling spread by the square-root law
    so a bigger sample would bring the 34.8% much closer to the true national 20%
```

Find the step that broke.

**10.** A colleague sends you this line for a newsletter.

> Kiran and colleagues found that medical students are far more overweight than India's young
> adults generally.

Decide what to compute, compute it, and say what your answer does not establish.

**11.** A colleague says: "A random sample of 2,000 people can't possibly tell us anything reliable
about a whole country. You would need several million to get a trustworthy number."

Decide what to compute, compute it, and say what your answer does not establish.

