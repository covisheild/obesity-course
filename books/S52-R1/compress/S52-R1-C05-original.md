# S52-R1-C05 · Functions and arguments

**Definition.** A function call is a function's name followed by round brackets. The values written inside
the brackets are its arguments, and the call returns one result, which R prints or which you
assign to a name.

Each argument has a name. An argument may be given by name, as `digits = 1`, or by position,
in the order the function lists its arguments. Arguments given by name are matched first, and
the rest are matched by position.

Most arguments have a default value, which is used when the call does not give one. The
defaults are shown in the Usage section of the function's help page, as in
`mean(x, trim = 0, na.rm = FALSE, ...)`. For `mean()`, `median()` and `sd()`, the argument
`na.rm` says whether missing values (`NA`) are removed before the computation. Its default,
`FALSE`, makes the result `NA` whenever a value is missing. Setting it to `TRUE` computes the
result from the values that are present, so the count behind the result is smaller.

Calls can be nested, as in `round(mean(x), 1)`, and R works from the inside out. The pipe,
`|>`, part of R since version 4.1.0, writes the same thing in reading order: `x |> f(y)` is
the call `f(x, y)`. The thing on the left becomes the first argument of the call on the right.

A help page, opened with `?name` or `help(name)`, describes one function in fixed sections:
Description, Usage, Arguments, Value (what it returns) and Examples. An error message names the
call that failed and says what was wrong with its arguments.

**In plain terms.** The last section ended with a sum that came back `NA`. Getting past that needs functions.

You met functions in Book 0 as input, rule and output, written f(x). R writes them the same
way: a name, then brackets, then the input inside. The rule is the function's job. The output
is the value it gives back:

```r
heights_cm <- c(152, 160.5, 171)
mean(heights_cm)
```

```output
[1] 161.1667
```

Whatever goes inside the brackets is an argument. Many functions take more than one. Each
argument has a name. `round()` takes the number to round, called `x`, and how many decimal places to
keep, called `digits`:

```r
round(161.1667, digits = 1)
```

```output
[1] 161.2
```

You can leave the names out, and R then matches the values by their order. You can also give
every name and put them in any order. These three lines do the same thing:

```r
round(161.1667, 1)
round(x = 161.1667, digits = 1)
round(digits = 1, x = 161.1667)
```

```output
[1] 161.2
[1] 161.2
[1] 161.2
```

Leave out an argument altogether and R uses its default. The default for `digits` is 0, so
`round(161.1667)` gives a whole number.

One call can sit inside another, and R works from the inside out:

```r
round(mean(heights_cm), 1)
```

```output
[1] 161.2
```

That line is short, but long nests are hard to read, because the first step is buried in the
middle. The pipe, written `|>`, puts the steps in the order they happen. Read it as "then":

```r
heights_cm |>
  mean() |>
  round(1)
```

```output
[1] 161.2
```

Take the heights, then take their mean, then round it to one decimal place. The pipe hands
the thing on its left to the call on its right, as the first argument. So `round(1)` here means
`round(the mean, 1)`.

To find out what a function's arguments are called and what they do, open its help page. Type
a question mark and the name: `?round`.

**Figure.** The same ten body masses, with penguin 4 missing, summarised three ways. Typing the missing weight as 0 gives a mean of 3392.5 g. Leaving it out with na.rm = TRUE gives a mean of 3769.444 g and a median of 3650 g, both from 9 values.

*What the figure shows:* A bar chart with three bars: missing weight typed as 0, mean, 3392.5 g; na.rm = TRUE, mean, 3769.444 g; na.rm = TRUE, median, 3650 g.

**Must know points for you.**

- The error is to read `mean(x, na.rm = TRUE)` as the mean of all your values. It is the mean of the values present. Report the count with it, "3.77 kg (n = 9)", every time.
- A missing value typed as 0 gives no `NA` and no warning, and pulls the mean down. In the penguin example it moved the mean from 3769.444 g to 3392.5 g. When a mean looks low, look for zeros that mean "not measured".
- Name every argument after the first. `round(x, digits = 1)` says what the 1 is. `mean(3750, 3800, 3250)` runs, gives 3750 and is wrong, because unnamed values were matched by position to arguments you did not intend.
- Before you use a function for the first time, open its help page and read Usage and Arguments. The defaults decide what happens when you say nothing, and `na.rm = FALSE` is a default that changes answers.
- Read an error message as a sentence about one call: which function, which argument, what was wrong. Fix that argument and nothing else, then run the line again.
- No argument can tell you why a value is missing. `na.rm = TRUE` gives the right mean of the values present. Whether that mean stands for the whole group depends on which values went missing, and no function call can check that.
- If you find yourself copying the same block of calls three times with one thing changed, you need a function of your own. Writing one is taught at the next rung of this subject.

**Exercise 1** (teaching). A first-year resident has ten minutes and R open. They have never read a help page. Teach
them to find out, from `?round` alone, what `round(3.14159)` will give and why.

**Exercise 2** (retrieval). Without looking back, say what `na.rm = TRUE` does in `mean(x, na.rm = TRUE)` and what its
default is. Then say what you must report beside a mean computed this way.

**1.** A made-up adult's BMI is 24.83702 kg/m^2. Write one call that rounds it to one decimal
place and one that rounds it to a whole number.

**2.** Find the mean of the four numbers 4, 8, a missing value and 6, with the default behaviour.
Then find it using only the values that are present.

**3.** Rewrite this nested call with the pipe, one step per line, and check that it gives the same
answer.

```r norun
round(mean(c(61.2, 58.4, 70.9)), 1)
```

**4.** The first ten flipper lengths in `penguins_raw.csv` are 181, 186, 195, a missing value, 193,
190, 181, 195, 193 and 190 mm. Give their mean and their median in centimetres, each to one
decimal place, and say how many penguins each is based on.

**5.** Using only the help page of `sd()`, find how to make it leave out missing values. The first
ten body masses in `penguins_raw.csv` are 3750, 3800, 3250, a missing value, 3450, 3650,
3625, 4675, 3475 and 4250 g. Give their standard deviation, rounded to the nearest gram.

**6.** Without using `mean()`, write code that gives the same number as
`mean(body_mass_g, na.rm = TRUE)` for the ten body masses in problem 5. Then show that the
two agree.

**7.** A colleague wants the mean of three body masses. Their code and output are below, and they
report "the mean body mass was 3750 g". Find what broke, and say why the answer looks
reasonable.

```r
mean(3750, 3800, 3250)
```

```output
[1] 3750
```

**8.** A colleague's script stops at this line. The error is below. Find what broke.

```r error
body_mass_g <- c(3750, 3800, 3250, NA, 3450)
mean(body_mass_g, na.rm = true)
```

```output
Error: object 'true' not found
```

**9.** A colleague reports the mean of the first ten body masses (problem 5) in kilograms, to two
decimal places, as 3.78 kg. Their code and output are below. Find what broke, and say why the
answer looks reasonable.

```r
body_mass_g <- c(3750, 3800, 3250, NA, 3450, 3650, 3625, 4675, 3475, 4250)
round(body_mass_g / 1000) |>
  mean(na.rm = TRUE) |>
  round(2)
```

```output
[1] 3.78
```

**10.** A made-up draft report says: "The average body mass of the first ten penguins was 3392.5 g."
The first ten body masses are as in problem 5. Work out with code how that number could have
been produced. Say what the sentence gets wrong, and what a corrected sentence still does not
establish.

**11.** A made-up thesis table reports "median body mass 3650 g (n = 10)" for the first ten penguins
in the practice file. The values are as in problem 5. Check both numbers with code, and say
what the checked result does not establish.

