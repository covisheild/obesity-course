# S52-R1-C16 · Summaries by group

**Definition.** `summarise()`, from the dplyr package, makes a new data frame. It has one row for each
group, or a single row for the whole data frame when there are no groups. It has one column
for each grouping variable and one for each summary you name.

A summary is a function that turns a column into one value. The function `n()` gives the
number of rows in the group, whatever they hold. The functions `mean()` and `median()` give
the mean and the median. The function `sd()` gives the standard deviation, dividing by one
less than the count. The function `quantile()` gives quartiles and other quantiles, and
`IQR()` gives the interquartile range. Both use the seventh of nine rules for placing a
quantile between two values, unless told otherwise.

When the column holds a missing value, `mean()`, `median()` and `sd()` give `NA`, and
`quantile()` and `IQR()` stop with an error, unless `na.rm = TRUE` is given.

`group_by()` marks a data frame as grouped by one or more columns, so that the next verbs
work group by group. `ungroup()` removes the marking. A `summarise()` on data grouped by
several columns removes only the last of them, so its result is still grouped. The `.by`
argument of `summarise()` groups for that one step only, and leaves the result ungrouped.

`count(a)` gives the number of rows for each value of `a`. It is roughly
`group_by(a) |> summarise(n = n())`.

**In plain terms.** Earlier sections chose the rows of a data frame and changed its columns, one row still standing
for one observation. This one shrinks it. A summary turns many rows into one number: how many there are, their mean, their
median, their spread. Book 0 taught each of these by hand. Here R does the arithmetic, and your
job moves to choosing the summary and reading it.

**summarise()**, met once in the section on missing values, gives one row. Ask it for the mean body mass of every penguin in the file and
you get one row with one number.

**group_by()** before it, or **.by** inside it, gives one row per group: one row per species,
one row per district, one row per clinic. The shape of the answer tells you what you asked for.
Three species give three rows. If you expected three rows and got eight, you grouped by
something else as well.

Put the count beside every summary. A mean of 3700 g from 151 penguins and a mean of 3700 g
from 3 penguins are not the same evidence. The reader of your table cannot tell them apart
unless you print the count. Be careful which count. `n()` counts rows. If some rows have no
value, the mean used fewer than `n()` of them. Count the values the mean actually used with
`sum(!is.na(x))`.

Quartiles have more than one recipe. Book 0's recipe, R's default and the one SPSS uses can give
three different answers on the same small set of numbers. None is wrong. Say which you used.

When the table is done, write it to a file in `output/` with code. Never copy a number off the
screen into a report. If the data change, rerun the script and the file changes with them.

A summary describes the rows in your file. It is not, by itself, a figure for anyone outside it.

**Figure.** Mean body mass of the penguins in the file, by species, from the first illustration's table: Adelie 3701 g from 151 body masses, Gentoo 5076 g from 123, Chinstrap 3733 g from 68. The bars start at zero, so their lengths compare the means. The means describe the rows of this file.

*What the figure shows:* A bar chart of three species. Adelie 3701 grams, Gentoo 5076 grams, Chinstrap 3733 grams, on an axis that starts at zero.

**Must know points for you.**

- Print the count beside every summary, and print the right count. `n()` counts rows. With `na.rm = TRUE`, a mean uses only the rows that have a value, so count those with `sum(!is.na(x))`. A table that prints {{n:penguins_adelie}} beside a mean of 151 values is wrong by one, and the reader cannot see it.
- The error is to think `na.rm = TRUE` fixes missing values. It only leaves them out, without a word. Report how many were left out, in every table.
- Check the shape of the result before reading a number. One row per group is what you asked for. If there are more rows than groups you expected, an extra grouping column, or an `NA` group, is in there.
- After `group_by()` on two columns, `summarise()` leaves the result grouped by the first. A percentage worked out next is a percentage within each group, not of the total. Use `.by`, or end with `ungroup()`.
- Quartiles from R, SPSS and Book 0's hand method can differ on the same small set of numbers. When two tables disagree on a quartile, ask which rule each used before you suspect the data. Name your software and rule in your methods.
- Write every summary table to `output/` with code. A number copied off the screen into a thesis cannot be traced back. It also stays wrong when the data are corrected.
- When a trainee shows you a table of means, ask first for the count in each row and for how many values were missing. Then ask for the median beside the mean, as Book 0 taught.
- A summary describes the rows in your file. It is not an estimate for any population unless the rows were chosen to stand for one. For a survey, it also needs the survey's sample weights, which a later book teaches. No line of `summarise()` can supply either.

**Exercise 1** (calculation). Add to your penguin script a summary of flipper length by island. Give, for each island, the
number of rows, the number of flipper lengths used, the mean and the median in millimetres.
Write the table to `output/flipper_by_island.csv`, and say which island's mean rests on the
fewest measurements.

**Exercise 2** (critique). A colleague's thesis table gives "Mean haemoglobin 11.2 g/dL (n = 312)" for the women in her
study. She ran `mean(hb, na.rm = TRUE)` in the console and read the answer off the screen. She
typed it into the Word table, with `nrow()` of her data frame as the n. Say what can be wrong
with that number and its n, and how her script should produce them instead.

**Exercise 3** (teaching). A first-year resident has ten minutes and a whiteboard. She has just made a table of mean BMI
by district from a screening register. She does not see why you want a count in every row.
Teach her.

**Exercise 4** (retrieval). Without looking back, name three ways a table of summaries by group can be wrong, or
misleading, without any error message.

**1.** A made-up table:

```r
library(dplyr)

scores <- tibble(score = c(4, 9, 5))
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Write one line that gives the number of rows and the mean score, in one row.

**2.** A made-up table of two groups:

```r
library(dplyr)

visits <- tibble(
  clinic = c("A", "B", "A", "B", "A"),
  patients = c(12, 7, 9, 11, 6)
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Give the total number of patients for each clinic. Before you run it, say how many rows the
answer will have.

**3.** Use Book 0's method, the median of each half, on the four numbers 2, 4, 6 and 8. Work out the
first quartile, the third quartile and the interquartile range. Then run `quantile()` and `IQR()` on the same four
numbers in R. Say why the answers differ.

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

For each island, give the number of rows and the number of different species found there.
(`n_distinct(x)` counts the different values in `x`.)

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

Give the median body mass in grams for each value of `Sex`, with the number of rows and the
number of body masses used. Say what the third row is, and why it is there.

**6.** Read the penguin file.

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

Make a table of culmen length by species: the number of values used, the mean and the
standard deviation. The culmen is the ridge of the bill, measured in millimetres. Write it to
`output/culmen_by_species.csv`. Then show that the file exists and how many lines it has.

**7.** A colleague runs this and writes in her notes: "Adelie and Gentoo body masses were not
recorded; only Chinstrap has data."

```r
library(readr)
library(dplyr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)

penguins_raw |>
  summarise(mean_g = mean(`Body Mass (g)`), .by = Species)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

# A tibble: 3 × 2
  Species                                   mean_g
  <chr>                                      <dbl>
1 Adelie Penguin (Pygoscelis adeliae)          NA
2 Gentoo penguin (Pygoscelis papua)            NA
3 Chinstrap penguin (Pygoscelis antarctica)  3733.
```

Find what broke.

**8.** A colleague's table of Gentoo body mass reads "n = {{n:penguins_gentoo}}, mean 5076 g". Here is his code.

```r
library(readr)
library(dplyr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)

penguins_raw |>
  filter(Species == "Gentoo penguin (Pygoscelis papua)") |>
  summarise(
    n = n(),
    mean_g = mean(`Body Mass (g)`, na.rm = TRUE)
  )
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

# A tibble: 1 × 2
      n mean_g
  <int>  <dbl>
1   124  5076.
```

The mean is right. Find what is wrong with the table.

**9.** A colleague wants each species-and-sex group's share of all the penguins, and reports
"Gentoo males are 49.2% of the penguins in the file."

```r
library(readr)
library(dplyr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)

penguins_raw |>
  group_by(Species, Sex) |>
  summarise(n = n()) |>
  mutate(pct = 100 * n / sum(n)) |>
  filter(Sex == "MALE")
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

`summarise()` has grouped output by 'Species'. You can override using
the `.groups` argument.
# A tibble: 3 × 4
# Groups:   Species [3]
  Species                                   Sex       n   pct
  <chr>                                     <chr> <int> <dbl>
1 Adelie Penguin (Pygoscelis adeliae)       MALE     73  48.0
2 Chinstrap penguin (Pygoscelis antarctica) MALE     34  50
3 Gentoo penguin (Pygoscelis papua)         MALE     61  49.2
```

Find what broke.

**10.** A colleague runs this to get mean body mass by short species name:

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

```r error
penguins_raw |>
  summarise(
    mean_g = mean(`Body Mass (g)`, na.rm = TRUE),
    .by = species
  ) |>
  mutate(
    species = case_when(
      species == "Adelie Penguin (Pygoscelis adeliae)" ~ "Adelie",
      species == "Chinstrap penguin (Pygoscelis antarctica)" ~ "Chinstrap",
      species == "Gentoo penguin (Pygoscelis papua)" ~ "Gentoo"
    )
  )
```

```output
Error in `summarise()`:
! Can't subset columns that don't exist.
✖ Column `species` doesn't exist.
```

Read the error. Say what broke and fix it.

**11.** A made-up draft thesis says: "Gentoo penguins (n = {{n:penguins_gentoo}}) were heavier than Adelie penguins
(n = {{n:penguins_adelie}}), with mean body masses of 5076 g and 3701 g." Check every number in the sentence
against the penguin file. Then say what the result does not establish.

**12.** In a made-up lab meeting, someone says: "Male penguins in this dataset average about 4.5 kg."
Turn the sentence into code, run it, and say what the result does not establish.

