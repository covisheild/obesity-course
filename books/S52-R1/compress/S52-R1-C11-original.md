# S52-R1-C11 · Choosing rows and columns

**Definition.** Four functions of the dplyr package choose parts of a data frame. Each takes a data frame as its
first argument and returns a new data frame. None of them changes the data frame it was given.
To keep a result, assign it to a name.

`select()` keeps the columns you name, in the order you name them, and drops the rest. Every row
is kept. A column can be renamed inside it with `new_name = old_name`. Selection helpers pick
columns by their names: `starts_with("Culmen")` picks every column whose name starts with
"Culmen".

`rename()` changes the names of columns you name, with `new_name = old_name`, and keeps every
column, in its place.

`filter()` keeps the rows for which a condition is `TRUE`. A condition is built from
comparisons (`==` equal to, `!=` not equal to, `<`, `>`, `<=`, `>=`) joined by `&` (and), `|`
(or) and `!` (not). `x %in% c(a, b)` is `TRUE` where `x` equals one of the values listed.
Several conditions separated by commas must all be `TRUE`. A row whose condition is `NA` is
dropped. So a test for a missing value is written `is.na(x)`, never `x == NA`.

`arrange()` sorts the rows by the values of the columns named, smallest first. `desc()` sorts
largest first. Missing values go to the end either way.

The pipe passes the data frame on its left to the function on its right, as that function's
first argument: `x |> f(y)` is `f(x, y)`.

**In plain terms.** The section on reading a raw file left you with the whole penguin file in R as one data frame:
{{n:penguins_rows}} rows and {{n:penguins_cols}} columns. Most questions need a few of those columns and some of the rows. Four functions do the
choosing.

**select()** keeps columns. You name the ones you want and the rest are dropped. Every row stays.

**rename()** gives columns new names and keeps all of them.

**filter()** keeps rows. You write a test, and a row stays only if the test says `TRUE` for it.
"Island is Dream" is a test. So is "body mass is more than 4,000 g".

**arrange()** puts the rows in order: smallest first, or largest first with `desc()`.

Here is the trap that catches everyone once. A test on a missing value gives neither `TRUE` nor
`FALSE`. It gives `NA`, "don't know". `filter()` drops every row where the test says "don't know".
So a test written as "body mass equals missing" says "don't know" on every row, and you get no
rows at all. To find the missing ones, ask `is.na()`, which answers `TRUE` or `FALSE`.

One more thing holds for all four. None of them touches the data frame you gave it. Each hands
back a new one, prints it, and forgets it, unless you give the result a name with `<-`. Your raw
data stays exactly as it was read.

The pipe, `|>`, lets you write the steps one under another. Read each `|>` as "then": take the
penguins, then keep these rows, then keep these columns, then sort.

**Figure.** Rows left after each step of the second example's pipe: 344 rows in the file, 176 on Dream or Torgersen, and 85 of those recorded as FEMALE.

*What the figure shows:* A bar chart with three bars: all penguins 344, island is Dream or Torgersen 176, and sex is FEMALE 85.

**Must know points for you.**

- The error is to write `filter(x == NA)` to find missing values. It returns no rows, without a warning, and reads like "none are missing". Write `filter(is.na(x))`.
- An empty result is a claim about your test before it is a claim about your data. When `filter()` returns no rows, or far fewer than you expected, print the column you tested and look at its values. "Adelie penguin" with a small p matches nothing in this file.
- `filter()` drops a row whose test is `NA`. So "body mass more than 4000 g" also drops the two penguins with no body mass. Whenever you report a count after a filter, say whether missing values were dropped by it.
- Never type a filter into the raw file by deleting rows. Write the `filter()` line in the script. It is visible, it can be undone by deleting one line, and the raw file stays whole for the next question.
- A verb that is not assigned changes nothing. If a result vanishes on the next line, look for the missing `<-`.
- Rename awkward column names once, near the top of the script, into snake case (lowercase words joined by `_`). Every later line is shorter, and nobody has to type backticks again.
- `filter()` keeps the rows that pass the test you wrote. It cannot tell you whether that test matches your question. "Female" in a sex column may be coded "F", "FEMALE", 2 or "female"; read the data dictionary before you write the test.

**Exercise 1** (teaching). A first-year resident has ten minutes and a whiteboard. Their code `filter(hb == NA)` on an
anaemia survey file returned no rows, and they have written "no missing haemoglobin values" in
their results. Explain what happened and how to check.

**Exercise 2** (retrieval). Without looking back, take each of `select()`, `rename()`, `filter()` and `arrange()` in turn.
Say what it does to the rows and to the columns. Then say what it does to the data frame you
gave it.

**Exercise 3** (design). Write the first block of your analysis script after the line that reads the penguin file. It
should keep the species, island, sex, flipper length and body mass columns, and give each a
snake-case name that carries its unit. Show that the result has {{n:penguins_rows}} rows and 5 columns.

**1.** A made-up clinic register has three rows.

```r
library(dplyr)

clinic <- tibble(
  id = c(101, 102, 103),
  sex = c("F", "M", "F"),
  weight_kg = c(61.2, 78.5, NA)
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Write one line that keeps the rows for women.

**2.** The same made-up register:

```r
library(dplyr)

clinic <- tibble(
  id = c(101, 102, 103),
  sex = c("F", "M", "F"),
  weight_kg = c(61.2, 78.5, NA)
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Write one line that keeps only the `id` and `weight_kg` columns, in that order.

**3.** The same made-up register:

```r
library(dplyr)

clinic <- tibble(
  id = c(101, 102, 103),
  sex = c("F", "M", "F"),
  weight_kg = c(61.2, 78.5, NA)
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Sort it heaviest first. Before you run it, say where the row with no weight will go.

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

How many rows are Chinstrap penguins? The species is written in the file exactly as
"Chinstrap penguin (Pygoscelis antarctica)".

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

How many penguins on Biscoe island have a flipper length of 210 mm or more? Give the number
with its unit of count and its condition.

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

The two isotope columns are `Delta 15 N (o/oo)` and `Delta 13 C (o/oo)`. How many penguins
are missing both? How many are missing at least one?

**7.** A colleague wants the number of Adelie penguins and writes:

```r
library(readr)
library(dplyr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)

penguins_raw |>
  filter(Species == "Adelie penguin (Pygoscelis adeliae)") |>
  nrow()
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

[1] 0
```

They report "there are no Adelie penguins in the file". Find what broke.

**8.** A colleague wants the penguins with no sex recorded and writes:

```r
library(readr)
library(dplyr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)

penguins_raw |>
  filter(Sex == NA) |>
  nrow()
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

[1] 0
```

They write in their notes: "sex was recorded for every penguin". Find what broke, and give the
right count.

**9.** A colleague wants the male and female penguins on Dream island and writes:

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
  filter(Island == "Dream", Sex == "MALE" | "FEMALE")
```

```output
Error in `filter()`:
ℹ In argument: `Sex == "MALE" | "FEMALE"`.
Caused by error in `Sex == "MALE" | "FEMALE"`:
! operations are possible only for numeric, logical or complex types
```

Read the error. Say what broke and fix it.

**10.** A colleague wants the mean body mass without the two missing values and writes:

```r
library(readr)
library(dplyr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)

penguins_raw |>
  filter(!is.na(`Body Mass (g)`))

mean(penguins_raw$`Body Mass (g)`)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

# A tibble: 342 × 17
   studyName `Sample Number` Species Region Island Stage `Individual ID`
   <chr>               <dbl> <chr>   <chr>  <chr>  <chr> <chr>
 1 PAL0708                 1 Adelie… Anvers Torge… Adul… N1A1
 2 PAL0708                 2 Adelie… Anvers Torge… Adul… N1A2
 3 PAL0708                 3 Adelie… Anvers Torge… Adul… N2A1
 4 PAL0708                 5 Adelie… Anvers Torge… Adul… N3A1
 5 PAL0708                 6 Adelie… Anvers Torge… Adul… N3A2
 6 PAL0708                 7 Adelie… Anvers Torge… Adul… N4A1
 7 PAL0708                 8 Adelie… Anvers Torge… Adul… N4A2
 8 PAL0708                 9 Adelie… Anvers Torge… Adul… N5A1
 9 PAL0708                10 Adelie… Anvers Torge… Adul… N5A2
10 PAL0708                11 Adelie… Anvers Torge… Adul… N6A1
# ℹ 332 more rows
# ℹ 10 more variables: `Clutch Completion` <chr>, `Date Egg` <date>,
#   `Culmen Length (mm)` <dbl>, `Culmen Depth (mm)` <dbl>,
#   `Flipper Length (mm)` <dbl>, `Body Mass (g)` <dbl>, Sex <chr>,
#   `Delta 15 N (o/oo)` <dbl>, `Delta 13 C (o/oo)` <dbl>,
#   Comments <chr>
[1] NA
```

The `filter()` printed {{n:penguins_mass_n}} rows, so they expected a number. They got `NA`. Find what broke.

**11.** A colleague wants the heaviest penguin in the file and writes:

```r
library(readr)
library(dplyr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)

penguins_raw |>
  arrange(`Body Mass (g)`) |>
  select(Species, `Body Mass (g)`) |>
  print(n = 1)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

# A tibble: 344 × 2
  Species                                   `Body Mass (g)`
  <chr>                                               <dbl>
1 Chinstrap penguin (Pygoscelis antarctica)            2700
# ℹ 343 more rows
```

They report "the heaviest penguin was a Chinstrap at 2700 g". Find what broke.

**12.** A line in a made-up field report says: "More than half of the Adelie penguins on Torgersen were
female." Check it against the file, and say what your answer does not establish.

**13.** In a made-up lab meeting, someone says: "The Gentoo penguins over 6 kg were all males." Turn
this into code, run it, and say what the result does not establish.

