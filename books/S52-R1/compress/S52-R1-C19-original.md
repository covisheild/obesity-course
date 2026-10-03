# S52-R1-C19 · Checking the data in code

**Definition.** A check, in this book, is a line of code that states something you believe about the data and
stops the script with an error when it is false.

`stopifnot()`, from base R, takes one or more expressions. If any of them is not `TRUE` in every
element, it stops with an error naming the first expression that failed, and the expressions
after it are not evaluated. A missing value counts as not `TRUE`, so an expression that gives
`NA` fails. When an expression is given a name, the name is printed in place of the expression.
When every expression is `TRUE`, `stopifnot()` prints nothing.

Three checks recur. A range check tests that every recorded value of a column lies between a
lower and an upper limit written in the code. The limits come from a source or a stated
decision, never from the smallest and largest values in the same data. A key is the column, or
set of columns, meant to pick out one row each. A key check tests that the key has as many
different values as the data have rows. `n_distinct()`, from dplyr, counts the different values
or combinations. A
row-count check stores the number of rows before a step that could change it, such as a join,
and compares it with the number after.

A value a check finds wrong is corrected by a line of code, never in the raw file. The line
picks out the row by its key, writes the corrected value into a new column, and carries a
comment giving the date, what was changed, and where the correct value came from.

**In plain terms.** Every analysis rests on beliefs about the data that nobody wrote down. Every height is in
centimetres. Each child appears once. The join did not add rows. A check writes one such belief as
a line of code, and the script stops the moment the belief is false.

**stopifnot()** is the tool. Give it a test that should be `TRUE`. If it is, nothing happens and
the script carries on. If it is not, the script stops with an error. Give each test a name that
says the belief in words, and the error prints that name.

Three checks cover most of what goes wrong.

- **Range.** Every height lies between two limits you wrote down. This is Book 0's
  order-of-magnitude check, done by the computer on every row, every time the script runs.
- **Key.** Every row has its own ID. Count the different IDs with `n_distinct()` and compare with
  the number of rows.
- **Row count.** Count the rows before a join or a filter and again after. Then compare. The
  cases left out of the daily figures in the first section of this book grew unseen until
  someone compared one count with another.

A check that fails is a question, not a verdict. Look at the rows it found. Go back to the paper
register, the form or the person who measured. Then write the fix as a line of code, with the date
and the reason in a comment. Never fix it in the raw file. The raw file stays as it came, and the
script shows every change made to it.

**Figure.** Rows after each step of the NHANES 2021–2023 example: 8860 in the body measures file as read, 8860 after joining the demographics file on SEQN, 6064 aged 20 or over, and 5970 with both height and weight recorded. The 94 adults missing a height, a weight or both are the difference between the last two bars. These are counts of rows in the files, unweighted, and estimate nothing about the United States.

*What the figure shows:* A bar chart of four steps. BMX_L as read: 8860 rows. After the join to DEMO_L on SEQN: 8860. Aged 20 or over: 6064. Both height and weight recorded: 5970.

**Must know points for you.**

- The error is to think that a script which runs without an error has checked the data. It has checked nothing you did not write as a check. A BMI computed from a height in metres runs as smoothly as a right one.
- Write each belief about the data as a `stopifnot()` line with a name that says the belief in words. When it fails, the error message tells the next reader exactly what was assumed.
- A missing value fails `stopifnot()`. Do not delete the check to make the script run. Count the missing values and report them, then check the recorded values with `na.rm = TRUE` inside `all()`.
- Never set a range check's limits from the smallest and largest values in the same data. Limits taken from the data always pass on that data. Take them from a source or a stated decision, and write which in a comment.
- Count the rows before and after every join and every filter, and compare the two in code. An ID repeated in the table you join to adds rows with no warning. Every mean after it counts someone twice. dplyr warns only when IDs repeat in both tables.
- Fix a wrong value with a line of code. Pick the row by its ID and write the right value into a new column. Say in a comment the date and where the right value came from. If no record gives the right value, set it to `NA` and report it. Never guess it.
- Never fix a row by its position, as in "row 3". Sorting or filtering earlier in the script moves the rows, and the fix lands on someone else without any error.
- A check that fails is a question, not a verdict. A weight of 180 kg outside your limits may be a real person, and a repeated ID may be a second visit. Look at the rows and the paper before you change anything.
- A range check catches a value outside its limits and never a wrong value inside them. A height of 126 cm typed for 162 cm passes. So a script whose checks all pass has data that are possible, not data that are right.

**Exercise 1** (critique). A colleague found a weight of 620 kg in their thesis spreadsheet. They looked up the paper form,
which said 62, typed 62 into the cell, saved the file and reran their analysis. Say what is wrong
with this, and what they should have done.

**Exercise 2** (design). Your thesis dataset, made up for this exercise, is a CSV file of school children aged 6 to 14 from
one district. It has one row per child. Its columns are `child_id`, `school_code`, `age_years`,
`sex` (written `F` or `M`), `height_cm` and `weight_kg`. Write the checks you would put at the top
of your script, straight after reading the file. For each limit, say where it comes from.

**Exercise 3** (retrieval). Without looking back, write the three kinds of check this section uses, one line of code for each.
Then say what `stopifnot()` does with a missing value.

**Exercise 4** (teaching). A first-year resident has ten minutes and a whiteboard. They say: "I always look at my data before
I analyse it, so I don't need checks in code." Teach them what a check in code does that looking
does not.

**1.** Before you run them, say what each line prints.

```r norun
stopifnot(2 + 2 == 4)
stopifnot(c(5, 12, 7) > 0)
stopifnot(c(5, -12, 7) > 0)
```

**2.** Five made-up heights, in centimetres:

```r
heights <- c(152, 1.6, 171, 158, 16.5)
```

Write one line that counts how many lie outside 50 to 250 cm.

**3.** Five made-up patient IDs:

```r
library(dplyr)

ids <- c(101, 102, 103, 103, 104)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Write a check that stops if any ID appears twice. Say what it prints.

**4.** Three made-up weights, in kilograms, one missing:

```r
weights <- c(58, NA, 72)
```

Say what `stopifnot(all(weights > 20))` prints. Then write a version that checks only the
recorded weights, and a line that counts the missing ones.

**5.** Read the penguin file:

```r
library(readr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)
```

Write a check that stops the script if any recorded body mass, in grams, lies outside 1000 to
10,000 g. Those limits are a decision made for practice, not a fact about penguins. Then count the
rows with no body mass.

**6.** Read the penguin file:

```r
library(readr)
library(dplyr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

The section on the data dictionary found that species together with sample number picks out one
row each. Write two checks: that the file has the {{n:penguins_rows}} rows its help page states, and that species
with sample number is a key. Then try the same key check on `Individual ID` alone, and say what
happens.

**7.** Read the NHANES body measures file:

```r
library(haven)

bmx <- read_xpt(here::here("data-raw", "BMX_L.xpt"))
```

The file has a BMI column, `BMXBMI`, in kg/m^2, beside weight `BMXWT` in kilograms and height
`BMXHT` in centimetres. Check in code that the BMI column agrees with weight divided by height in
metres squared, on every row where all three are recorded. The file prints BMI to one decimal
place, so allow a difference of up to 0.05.

**8.** A colleague checks the heights in a made-up register:

```r
library(dplyr)

register <- tibble(
  id = c(1, 2, 3),
  height_cm = c(158, 1.62, 171)
)

stopifnot(
  "heights are between 50 and 250 cm" =
    all(register$height_cm >= 50 | register$height_cm <= 250)
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Nothing printed, and they write in their notes: "heights checked, all within range." Find what
broke.

**9.** A colleague corrects a height in a made-up register. The paper register gives 160 cm for patient
103.

```r
library(dplyr)

clinic <- tibble(
  id = c(101, 102, 103),
  height_cm = c(171, 160, 1.6)
)

clinic_sorted <- clinic |>
  arrange(height_cm)

# register page for id 103 reads 160 cm
clinic_sorted$height_cm[3] <- 160

clinic_sorted
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

# A tibble: 3 × 2
     id height_cm
  <dbl>     <dbl>
1   103       1.6
2   102     160
3   101     160
```

All three heights now look sensible. Find what broke.

**10.** A colleague writes a range check on made-up weights:

```r
weights <- c(58, 64, 620, 71, 49)

lower <- min(weights, na.rm = TRUE)
upper <- max(weights, na.rm = TRUE)

stopifnot(
  "weights are within range" =
    all(weights >= lower & weights <= upper, na.rm = TRUE)
)
```

The check passes, and they report "all weights within range". Find what broke.

**11.** A colleague joins made-up visit records to a made-up table of people:

```r
library(dplyr)

visits <- tibble(id = c(1, 2, 3), weight_kg = c(61, 74, 55))
people <- tibble(
  id = c(1, 2, 2, 3),
  sex = c("female", "male", "male", "female")
)

n_before <- nrow(visits)

joined <- visits |>
  left_join(people, by = "id")
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

```r error
stopifnot("the join kept every row" = nrow(joined) == n_before)
```

```output
Error: the join kept every row
```

They say: "The check is too strict. I deleted it, the script runs, and the mean weight is 66 kg."
Find what broke.

**12.** A draft thesis on the NHANES 2021–2023 files says: "Height and weight were checked for all {{n:nhanes_adults_rows}}
adults, and every value was plausible." The adults are those aged 20 or over. Turn the sentence into
code, with limits of 50 to 250 cm and 20 to 300 kg. Run it, and say what the result does not
establish.

**13.** A colleague's script reads the penguin file and computes the mean body mass of each species. In a
made-up meeting they say: "The data are clean. The script ran without a single error." Decide what
you would have to compute before you could call the penguin file clean. Write it, run it, and say
what it still does not establish.

