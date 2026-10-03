# D5 · Average and spread, and why the average is not the person

**Definition.** This section turns a distribution into two single numbers: a typical value, and how spread out
the rest are around it.

The mean of a set of values is their sum divided by how many there are. The median is the
middle value of the same set once it is ordered from smallest to largest; where the count is
even, it is the mean of the two middle values.

The first quartile is the median of the lower half of the ordered values, and the third
quartile is the median of the upper half. The second quartile is the median of the whole set.
When the count itself is odd, leave the middle value out of both halves before taking their
medians. The interquartile range is the third quartile minus the first, and it describes the
spread of the middle half of the values, ignoring anything beyond it.

The population is the whole group a question is about. The sample is the part of that group
that was actually measured.

The deviation of a value from the mean is that value minus the mean. The variance is worked out
from the squared deviations: add them, then divide by the count for a whole population, or by
one less than the count for a sample. The standard deviation is the square root of the
variance, expressed in the same unit as the original values, because taking a square root
undoes the squaring. To say how far one value sits from the mean in standard deviations, divide
its deviation by the standard deviation.

The mean of a set of values says nothing on its own about where any one member of the set
actually sits.

**In plain terms.** Take six numbers: 5, 8, 12, 15, 20, 40. Add them and divide by how many there are. That is the
mean, which everyday speech calls the average.

```working
    5 plus 8 plus 12 plus 15 plus 20 plus 40 = 100
    100 divided by 6 = 16.6666666667...
```

The mean is about 16.7.

For the median, put the same six numbers in order, which they already are, and find the middle.
With six values there is no single middle one, so take the two in the middle and average them.

```working
    12 plus 15 = 27
    27 divided by 2 = 13.5
```

The median is 13.5, noticeably below the mean of 16.7. One number in this set, the 40, sits a
long way above the rest. It drags the mean up with it and leaves the median almost where it would
have been without it.

Take eight ordered numbers: 2, 4, 4, 6, 8, 8, 10, 12. The middle value, the second quartile, is
the average of the two central values.

```working
    6 plus 8 = 14
    14 divided by 2 = 7
```

Now split the set into its lower half and its upper half, four numbers each, and find the middle
of each half the same way. The lower half is 2, 4, 4, 6.

```working
    4 plus 4 = 8
    8 divided by 2 = 4
```

That gives the first quartile, 4. Now the upper half, 8, 8, 10, 12.

```working
    8 plus 10 = 18
    18 divided by 2 = 9
```

That gives the third quartile, 9. The interquartile range is the third quartile minus the first.

```working
    9 minus 4 = 5
```

It says the middle half of these eight values is spread across five units.

Now the standard deviation, step by step, on six more bare numbers: 5, 7, 3, 7, 10, 4.

First, the mean.

```working
    5 plus 7 plus 3 plus 7 plus 10 plus 4 = 36
    36 divided by 6 = 6
```

The mean is 6. Now the deviation of every value: how far it sits from that mean, kept with its
sign.

```working
    5 minus 6 = -1
    7 minus 6 = 1
    3 minus 6 = -3
    7 minus 6 = 1
    10 minus 6 = 4
    4 minus 6 = -2
```

Square every deviation next, which means multiplying each one by itself. A negative number times
a negative number gives a positive number.

```working
    -1 times -1 = 1
    1 times 1 = 1
    -3 times -3 = 9
    1 times 1 = 1
    4 times 4 = 16
    -2 times -2 = 4
```

Add the squares.

```working
    1 plus 1 = 2
    2 plus 9 = 11
    11 plus 1 = 12
    12 plus 16 = 28
    28 plus 4 = 32
```

Divide that by one less than the count of values, which is five here, not six. That division is
the variance.

```working
    32 divided by 5 = 6.4
```

The variance is 6.4, and it is in the wrong unit. Squaring every deviation squared the unit too,
so a variance worked out from kilograms is really in kilograms squared, which nobody can picture.
Take the square root and the unit comes back to the one you started in. That last step is the
standard deviation.

```working
    square root of 6.4 = 2.529822128
```

The standard deviation of these six numbers is about 2.53.

Go back to the division by five rather than six. Most papers do the same thing: a sample's
variance is divided by one less than the count. Distances from the sample's own mean come out a
little small on average, because that mean sits in the middle of these particular numbers.
Dividing by one less than the count makes the variance come out right on average. The textbook
this book follows puts it briefly: dividing by one less 'gives a better estimate of the
population variance'.

**Illustration.** Open Table 1 of the paper used in the section on variation: Kiran, Harshitha and Bhargava, 282
medical students in Mangaluru. It gives weight, height, body-mass index and more, each as a
mean with its standard deviation beside a median with its first and third quartiles. Papers
write the standard deviation (SD) by its two initials. Read the first two rows for the 131 men.

```table
indicator     mean (SD)      median (first and third quartiles)
weight (kg)   72.0 (13.1)    70.9 (167.7, 177.8)
height (cm)   172.2 (6.8)    173 (62.6, 80.9)
```

Stop on the weight row's two quartiles, and check them yourself. The median has to sit between
the two quartiles printed beside it: the first quartile below it, the third above it. Here the
median is 70.9, and the two numbers printed beside it are 167.7 and 177.8. 70.9 sits below both
of them, not between them.

Try the same check on the height row underneath it. The median there is 173, and the two
numbers printed beside it are 62.6 and 80.9. It sits above both of them, not between them
either.

Both rows fail, in opposite directions. Each passes against the other row's numbers: 70.9
sits between 62.6 and 80.9, and 173 between 167.7 and 177.8. The numbers fit if the two rows' quartiles were printed in each other's places.

Men's mean body-mass index is 24.2 kilograms per square metre, with a standard deviation of
3.9.

Forty-two of the men are in the band from 25 to 29.9. Ten more are at 30 or more.

```working
    42 plus 10 = 52
```

Fifty-two of the 131 men have a body-mass index of 25 or more.

```working
    52 divided by 131 = 0.396946565...
    0.396946565 times 100 = 39.6946565
```

That rounds to about 39.7 per cent, close to two in every five. The mean of the group, 24.2,
sits under the line at 25. Close to two in five of the individual men in that same group sit at
it or above it. The mean describes the group. It was never a description of any one of the 131
men. Deciding whether one particular man is above or below 25 needs his own reading, not the
group's average.

Men's mean body fat is 22.1 per cent and their median is 20.3 per cent. The mean sits above the
median.

```working
    22.1 minus 20.3 = 1.8
```

By the median's own definition, at least half of the 131 men have a body fat percentage at or
below 20.3. That is also below the mean of 22.1. The men above the median must reach far
enough up to pull the mean past it. The quartiles printed beside the median show it: 16.7 and
28.8.

```working
    20.3 minus 16.7 = 3.6
    28.8 minus 20.3 = 8.5
```

The first quartile sits 3.6 below the median, and the third sits 8.5 above it. The quarter of
men just above the median stretches more than twice as far as the quarter just below it. That
is a longer stretch running upward than downward. It is exactly the shape the section on
variation described in words.

**Where this picture breaks.** Checking a median against its own two quartiles catches a pair of quartiles that sits nowhere
near the median.

The mean sitting below 25 while many men sit above it is a fact about this one group. It is 131
men, measured this way, in this college, in 2019. It says nothing about any other group. It
says nothing about any one of these men beyond what his own reading gives you.

The standard deviation and the interquartile range answer different questions about the same
spread. Neither can be worked out from the other.

**Figure.** The six numbers from this section on one line. The median, 13.5, sits in the middle of the crowd. The mean, 16.7, has been pulled towards the single value of 40. Without it, both would be 12.

*What the figure shows:* Six dots on a number line at 5, 8, 12, 15, 20 and 40. A solid line marks the median at 13.5, between 12 and 15. A dashed line marks the mean at 16.7, to the right of 15, pulled towards the lone dot at 40.

**Must know points for you.**

- A long tail on one side of a distribution pulls the mean toward it. Reading this backwards, "the mean is higher, so most values are higher", is an error.
- Compute the median alongside the mean whenever a handful of extreme values might be present. Compare the two before you quote either one on its own. A gap between them is itself a finding, not a rounding difference to ignore.
- A mean, on its own, says nothing about any one person in the group it was computed from.
- Divide by one less than the count whenever you compute a standard deviation from a sample.
- A mean sitting below a cut-off does not mean most of a group is below it.
- Check a printed median against the two quartiles printed beside it before you trust any of the three.
- In a lopsided distribution, the standard deviation hides that the two sides spread out differently. Where the mean and median disagree by much, look at the quartiles instead of trusting a single standard deviation to describe both sides.

**Exercise 1** (critique). A report states this. "Average daily step count in our clinic's patients is 6,200, comfortably
above the report's own target of 5,000 steps. So inactivity is not a major concern here." (The
figures are made up for this exercise.)

The same report's raw data shows a median of 4,100 steps. Say what the gap between the two
numbers tells you. Say what you would ask for before agreeing with the conclusion.

**Exercise 2** (teaching). A first-year resident reads a paper's abstract, sees a mean below a clinical cut-off, and
concludes "so this group is fine". You have ten minutes and a whiteboard.

Teach them why a mean sitting below a cut-off does not mean the group is.

**1.** Find the mean and the median of these seven numbers.

```working
    4   9   2   15   7   9   3
```

**2.** Find the mean and the median of these six numbers.

```working
    6   9   11   14   18   50
```

**3.** These eight numbers are already ordered.

```working
    3   5   5   9   11   11   15   19
```

Find the first quartile, the second quartile, the third quartile, and the interquartile range.

**4.** These seven numbers are already ordered.

```working
    2   5   7   9   12   15   20
```

Find the first quartile, the second quartile, the third quartile, and the interquartile range.

**5.** Work out the sample standard deviation of these six numbers, step by step.

```working
    8   6   10   4   12   8
```

**6.** Give the sample variance and the sample standard deviation of a sample whose deviations from its
own mean are the five values below.

```working
    -2   4   -1   3   -4
```

**7.** Table 1 of Kiran et al. (2022) gives men's mean body-mass index as 24.2 kg/m^2 and their median
as 23.8 kg/m^2.

Work out the gap between the two, and say which side of the distribution its tail is likely on.

**8.** Men's body-mass index in the same table has a median of 23.8 kg/m^2, with the two quartiles
printed beside it as 21.2 and 26.8.

Work out the interquartile range as a single number, and check whether the median sits between
the two quartiles it is printed beside.

**9.** The same table prints men's body-mass index as a median of 23.8 kg/m^2, with a first quartile
of 21.2 and a third quartile of 26.8.

Work out how far each quartile sits from the median. Say what the two distances suggest about
which side of the distribution has the longer tail.

**10.** Suppose a man in this group had a body-mass index of 30 kg/m^2. The men's mean is 24.2 with a
standard deviation of 3.9.

Work out how many standard deviations above the mean his reading would sit.

**11.** Table 1 of Kiran et al. (2022) gives the 151 women's body fat as a mean of 33.8 per cent. The
median is 34.0 per cent, with the two quartiles printed beside it as 28.1 and 39.2.

Work out the interquartile range as a single number. Check whether the median sits between the
two quartiles. Then say which way the mean sitting below the median points.

**12.** Five patients were picked from a clinic's much larger patient list. Here is someone's worked
sample standard deviation of their ages, in years. Find the step that broke.

```working
    the numbers are 12, 15, 9, 21, 18
    mean = (12 plus 15 plus 9 plus 21 plus 18) divided by 5 = 15
    deviations: -3, 0, -6, 6, 3
    squares: 9, 0, 36, 36, 9
    sum of squares = 90
    variance = 90 divided by 5 = 18
    standard deviation = square root of 18 = 4.242640687
```

**13.** A teammate is about to quote this line from Table 1 of Kiran et al. (2022) in a talk.

"Median weight among the women was 57.4 kilograms, with quartiles of 155.0 and 163.0."

Find what is wrong with the line. Say what you would check before quoting any pair of
quartiles taken from a table you have not read closely.

**14.** Somebody makes this claim from the body fat figures in Table 1 of Kiran et al. (2022).

"The mean body fat among the men is 22.1 per cent and the median is 20.3 per cent. Since the
mean is higher, most men must have a body fat percentage above 22.1."

Find the error in the reasoning.

**15.** A note about the study says this. "Women's average body-mass index was 23.0, under the cut-off
of 25, so weight was not a concern in this group of students."

Decide what to compute, compute it, and say what your answer does not establish.

**16.** A colleague says this about the same study. "Body fat in this group of men averages 22 per
cent, so most men have a body fat percentage somewhere between 20 and 24."

Decide what to compute, compute it, and say what your answer does not establish.

