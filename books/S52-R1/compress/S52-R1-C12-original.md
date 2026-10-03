# S52-R1-C12 · Making new columns

**Definition.** `mutate()`, from the dplyr package, adds columns to a data frame. Each new column is computed
from columns already there, one row at a time, and the result has the same number of rows as
the input. A new column goes on the right. If its name is the name of an existing column, it
replaces that column. Within one `mutate()`, a column made first can be used by the next.

`if_else(condition, true, false)` gives one value where the condition is `TRUE` and another
where it is `FALSE`. Where the condition is `NA`, the result is `NA`, unless a value is given
for `missing`.

`case_when()` takes a list of cases, each written `condition ~ value`. It checks them in order,
and each row gets the value of the first case whose condition is `TRUE`. A row that matches no
case gets `.default` if one is given, and `NA` otherwise. A row whose conditions are all `NA`
counts as matching no case.

`round(x, digits)` rounds to that many decimal places. A 5 at the cut is rounded to the even
digit, so `round(2.5)` is 2. Rounding acts on the number as the computer stores it, which may
differ from the number as printed.

`str_trim()` removes spaces from the start and end of a piece of text. `str_to_lower()` turns
text into lower case. Both come from the stringr package. `rename_with()` renames columns by
applying a function to their names.

**In plain terms.** The last section chose rows and columns that were already in the file. This one makes columns
that were not there. A body mass index comes from weight and height. A body mass in kilograms
comes from one in grams. A group label comes from a cut-point.

**mutate()** adds a column. You give the new column a name and a rule, and R applies the rule to
every row. The number of rows does not change. Book 0's rule for BMI, weight in kilograms divided
by height in metres squared, becomes one line of code.

Give the new column a new name. If you reuse an old name, the old column is replaced, and its
values are gone from your data frame. The raw file still has them, but your script no longer
shows where the new numbers came from.

**if_else()** sorts rows into two groups by one test. **case_when()** sorts them into several
groups. Its tests are checked in order, and each row takes the label of the first test it passes.
So the order of
the tests is part of the rule, and so is which side of each cut-point the boundary value falls on.
A row with a missing value passes no test and gets `NA`, which is what you want. Be careful with
`.default`, the label for "everything else": a missing value lands there too.

**round()** is for showing a number, not for storing it. Keep full precision in the column you
compute with, and round only what you print.

Text columns get cleaned the same way. **str_trim()** takes spaces off the ends.
**str_to_lower()** turns capitals into small letters. Together they turn "Male ", "male" and
"MALE" into "male".

All of it happens in the script. The raw file is never edited: not to convert a unit, not to fix
a spelling, not to add a column.

**Figure.** The four made-up patients with a BMI, at one decimal place, against the two NFHS-5 cut-points: 18.5 and 25.0 kg/m^2. Patient 102 sits exactly on 25.0, which the survey's rule puts in the upper group. Patient 104 has no weight, so no BMI.

*What the figure shows:* A bar chart of four patients: 101 at 17.7, 102 at 25.0, 103 at 27.4 and 105 at 21.3, with dashed lines across at 18.5 and 25.

**Must know points for you.**

- Convert units in code, in a new column, before using them. Never type converted values into the raw file: the conversion is then invisible, and a second conversion by someone else doubles the error.
- A BMI computed from height in centimetres is 10,000 times too small. Before trusting any new column, look at a few of its values and ask whether they are the right size.
- The error is to think a value that prints as 25 is 25. A stored number can sit a hair below or above what is printed. At a cut-point, decide a rounding rule, write it in a comment, and group on the rounded column.
- The order of the cases in `case_when()` is part of the rule. With `bmi >= 18.5` first and `bmi >= 25` second, nobody is ever put in "25 or more", and no error says so.
- Leave `.default` out unless you mean it. With `.default` set, a missing value is given that label as if it had been measured. Without it, a missing value stays `NA`.
- Give a new column a new name. Reusing the name of a column from the raw file replaces it, and the script no longer shows where the new values came from.
- Round for the table you print, not for the column you compute with. Rounding first and computing after carries the rounding error into every later number.
- A new column is only as right as the rule you wrote. `mutate()` will compute any rule on every row without complaint. It cannot tell you that a cut-point is the wrong one for the people in your data.

**Exercise 1** (critique). A colleague's thesis dataset has a weight column in kilograms. They opened the spreadsheet,
typed a formula into a new column to compute BMI, filled it down, and saved the file. Then they
read it into R. Say what is wrong with this, and what they should do instead.

**Exercise 2** (retrieval). Without looking back, name four ways a new column made with `mutate()` and `case_when()` can be
wrong without any error message.

**Exercise 3** (calculation). Add to your penguin script a column of flipper length in centimetres. Add another that labels
each penguin's body mass as "4.5 kg or more" or "under 4.5 kg". The cut-point is chosen for
practice; it is not a biological threshold. Count how many penguins get each label, including
any missing.

**1.** A made-up table of three heights:

```r
library(dplyr)

heights <- tibble(height_cm = c(150, 162.5, 178))
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Add a column `height_m` with the heights in metres.

**2.** A made-up table of three weights:

```r
library(dplyr)

weights <- tibble(weight_kg = c(72, 55, NA))
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Add a column that says "60 or more" or "under 60". Before you run it, say what the third row
will get.

**3.** Before you run it, say what this prints.

```r norun
round(c(0.5, 1.5, 2.5))
```

**4.** Read the penguin file.

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

Add a column of flipper length in centimetres. What is the first penguin's flipper length in
centimetres?

**5.** Read the penguin file.

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

Work out body mass in kilograms. Then put each penguin in one of three groups. The groups are
"under 3.5 kg", "3.5 to under 4.5 kg" and "4.5 kg or more", cut-points chosen for practice.
Count the penguins in each group.

**6.** A made-up register typed sex by hand:

```r
library(dplyr)
library(stringr)

register <- tibble(sex = c("Male", " female", "MALE ", "Female", "male"))
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

How many different spellings are there now? Clean the column into a new one, and count the
values of the new one.

**7.** A colleague computes BMI on a made-up register:

```r
library(dplyr)

register <- tibble(
  height_cm = c(158, 172, 149),
  weight_kg = c(62, 85, 47)
)

register |>
  mutate(bmi = weight_kg / height_cm^2) |>
  mutate(below_18_5 = bmi < 18.5)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

# A tibble: 3 × 4
  height_cm weight_kg     bmi below_18_5
      <dbl>     <dbl>   <dbl> <lgl>
1       158        62 0.00248 TRUE
2       172        85 0.00287 TRUE
3       149        47 0.00212 TRUE
```

They report "all three patients have a BMI below 18.5 kg/m^2". Find what broke.

**8.** A colleague groups BMI on a made-up register:

```r
library(dplyr)

register <- tibble(bmi = c(17.2, 23.9, 26.4, 31.0))

register |>
  mutate(
    bmi_group = case_when(
      bmi < 18.5 ~ "below 18.5",
      bmi >= 18.5 ~ "18.5 to below 25",
      bmi >= 25 ~ "25 or more"
    )
  )
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

# A tibble: 4 × 2
    bmi bmi_group
  <dbl> <chr>
1  17.2 below 18.5
2  23.9 18.5 to below 25
3  26.4 18.5 to below 25
4  31   18.5 to below 25
```

They report "nobody in the register has a BMI of 25 or more". Find what broke.

**9.** A colleague groups BMI on a made-up register, and wants every row to have a group:

```r
library(dplyr)

register <- tibble(bmi = c(17.2, 23.9, NA, 26.4))

register |>
  mutate(
    bmi_group = case_when(
      bmi < 18.5 ~ "below 18.5",
      bmi < 25 ~ "18.5 to below 25",
      .default = "25 or more"
    )
  ) |>
  count(bmi_group)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

# A tibble: 3 × 2
  bmi_group            n
  <chr>            <int>
1 18.5 to below 25     1
2 25 or more           2
3 below 18.5           1
```

They report "2 of the 4 patients have a BMI of 25 or more". Find what broke.

**10.** A colleague converts body mass to kilograms and reports the mean:

```r
library(readr)
library(dplyr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)

penguins <- penguins_raw |>
  mutate(`Body Mass (g)` = `Body Mass (g)` / 1000)

mean(penguins$`Body Mass (g)`, na.rm = TRUE)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

[1] 4.201754
```

Their table says "mean body mass 4.2 g". Find what broke.

**11.** A colleague writes:

```r
library(dplyr)

register <- tibble(
  height_cm = c(158, 172, 149),
  weight_kg = c(62, 85, 47)
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

```r error
register |>
  mutate(bmi = weight_kg / height_m^2) |>
  mutate(height_m = height_cm / 100)
```

```output
Error in `mutate()`:
ℹ In argument: `bmi = weight_kg/height_m^2`.
Caused by error:
! object 'height_m' not found
```

Read the error. Say what broke and fix it.

**12.** A made-up clinic audit says: "2 of our 5 patients had a BMI of 25.0 kg/m^2 or more." Here is the
register.

```r
library(dplyr)

audit <- tibble(
  id = c(1, 2, 3, 4, 5),
  height_cm = c(160, 155, 170, 165, 150),
  weight_kg = c(64, 52, 75, 62, 54)
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Check the claim, and say what your answer does not establish.

**13.** A made-up draft thesis says: "Mean body mass of the Gentoo penguins was 5.08 kg." The penguin
file records body mass in grams. Turn the sentence into code, run it, and say what the result
does not establish.

