# S52-R1-C13 · Missing values: counting them and saying how many

**Definition.** In R, a missing value is the constant `NA`, "not available". Any arithmetic on `NA` gives
`NA`. A raw file may instead mark a missing value with a code: an empty cell, a number such
as -99 or 999, or text such as "not recorded". R turns a code into `NA` only when it is told
to, at reading or in a later line of code. A code it was not told about is kept as an
ordinary value.

`is.na(x)` returns `TRUE` for each element of `x` that is `NA`. In arithmetic, `TRUE` counts
as 1 and `FALSE` as 0, so `sum(is.na(x))` is the number of missing values in `x`. Applied to
a data frame, `is.na()` returns a grid of `TRUE` and `FALSE` the shape of the data frame, and
`colSums()` adds it up column by column.

`mean(x, na.rm = TRUE)` and similar summaries leave out the missing values. The number of
values behind the result is then `sum(!is.na(x))`, not `length(x)`.

`drop_na()`, from the tidyr package, keeps only the rows with no missing value in the columns
it is given, or in every column when it is given none. Analysing only such rows is called
complete-case analysis.

**In plain terms.** The last section made new columns. Some of the values it worked on were missing, and every
calculation that touched one gave `NA`. This section counts those gaps, and makes you say how
many there were.

A missing value reaches R in one of two ways. Either it is already `NA`, because the cell was
empty or the reading step was told which codes mean missing. Or it arrives disguised as a
real value: a weight of 999, a height of -99, the words "not recorded". R cannot tell a
disguised code from a measurement. A weight of 999 kg goes into the mean like any other
weight.

So the first job is to find the codes. Read the data dictionary, then look at the largest and
smallest values of each column. Turn every code into `NA` in your script, never in the file.

The second job is to count. `sum(is.na(x))` counts the missing values in one column.
`colSums(is.na(data))` counts them in every column at once.

The third job is to say how many values stand behind each number you report. Book 0 taught that
a mean is a sum divided by how many values there are. With `na.rm = TRUE` that "how many" is
smaller than the number of rows. Write it beside the mean.

Dropping every row with a gap, with `drop_na()`, is a choice, not a clean-up. It changes which
rows your answer is about. Name the columns you drop on, and report how many rows were left.

**Figure.** Rows of the penguin file kept by four choices: all 344 rows; 342 with a body mass; 333 with a body mass and a recorded sex; 34 with no gap in any column. The last drop is driven by the Comments column, which is empty in 290 rows.

*What the figure shows:* A bar chart with four bars: all rows 344, body mass present 342, body mass and sex present 333, every column present 34.

**Must know points for you.**

- The error is to think a missing value always shows as `NA`. A code such as 999 or -99 is an ordinary number to R until you say otherwise. Before any summary, look at each column's smallest and largest values, and check the data dictionary for its missing codes.
- Count missing values with `sum(is.na(x))`, or `colSums(is.na(data))` for every column. Do it once at the top of the script, and keep the printed counts with your outputs.
- Beside every mean, median or percentage, write the n it was computed from. With `na.rm = TRUE` that n is `sum(!is.na(x))`, not the number of rows. Refuse a table whose n is the row count of the file.
- `drop_na()` with no columns named drops a row for a gap in any column, including a free-text note. On the penguin file it keeps 34 of {{n:penguins_rows}} rows. Always name the columns, and print `nrow()` before and after.
- Turn codes into `NA` in a new column made by code, never by editing the raw file. Then anyone can see which values were changed and why.
- Complete-case analysis is a choice with consequences: it changes which people your answer is about. Say in the methods which columns you required, and how many rows that left.
- Counting missing values tells you how many are gone, never why. A count cannot show whether the people with gaps differ from the rest. So it cannot tell you whether leaving them out has biased the answer.

**Exercise 1** (calculation). In your penguin script, count the missing values in every column. Then give the mean flipper
length in millimetres, with the number of penguins it was computed from, written the way a
table would show it.

**Exercise 2** (critique). A made-up thesis methods section says: "Participants with missing data were excluded. Mean
BMI was 26.1 kg/m^2." The dataset had 412 participants and 28 columns. Say what is missing from
these two sentences, and rewrite them.

**Exercise 3** (retrieval). Without looking back, write the line that counts the missing values in one column `x`. Then
write the line that counts them in every column of a data frame `d`. Last, say what
`drop_na()` does when no column is named.

**1.** How many missing values does this made-up vector hold? Write the line that counts them, and
say what it prints before you run it.

```r norun
x <- c(3, NA, 7, NA, NA, 2)
```

**2.** Before you run them, say what each line prints, and how many values the second mean is
computed from.

```r norun
weights <- c(54, 61, NA, 70)
mean(weights)
mean(weights, na.rm = TRUE)
```

**3.** A made-up three-row table:

```r
library(tidyr)

d <- tibble::tibble(
  height_cm = c(150, NA, 162),
  weight_kg = c(48, 55, NA)
)
```

How many rows does `drop_na(d)` keep? How many does `drop_na(d, height_cm)` keep? Say both
before you run them.

**4.** Read the penguin file.

```r
library(readr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)
```

How many penguins have no recorded sex? What percentage of the rows is that, to one decimal
place?

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

In one `summarise()`, give the number of rows, the number of missing values of `Delta 15 N
(o/oo)`, and the mean of the values present. Write the result as a table would show it. The
data's help page describes Delta 15 N as a measure of the ratio of two forms of nitrogen,
taken from a blood sample.

**6.** Read the penguin file.

```r
library(readr)
library(tidyr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)
```

A question needs culmen length, culmen depth and both blood measurements, `Delta 15 N (o/oo)`
and `Delta 13 C (o/oo)`. How many rows have all four? How many does that leave out?

**7.** A colleague's made-up register used 999 for "not weighed". They report: "Mean weight was 64.5
kg, after removing missing values."

```r
weights <- c(58, 999, 66, 71, 999, 63)
mean(weights[!is.na(weights)])
```

```output
[1] 376
```

Run it. Find what broke, and why the report looks reasonable.

**8.** A made-up camp file has a height column where the field worker wrote "not recorded" for one
child. A resident reads it and asks for the mean height:

```r
library(readr)

camp <- read_csv(I("id,height_cm
1,131
2,not recorded
3,128"), show_col_types = FALSE)

mean(camp$height_cm)
```

```output
[1] NA
Warning message:
In mean.default(camp$height_cm) :
  argument is not numeric or logical: returning NA
```

They report: "height could not be summarised; the data are missing". Find what broke.

**9.** A colleague wants the mean body mass of the penguins whose sex is known. They write:

```r
library(readr)
library(tidyr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)

known <- drop_na(penguins_raw)

nrow(known)
mean(known$`Body Mass (g)`)
```

```output
[1] 34
[1] 3877.206
```

Their table says "mean body mass of penguins of known sex, 3877.206 g". Find what broke.

**10.** A made-up draft report says: "Mean body mass was {{n:penguins_mass_mean_g}} g in the {{n:penguins_rows}} penguins studied." Check
the sentence against the penguin file, rewrite it, and say what your rewritten sentence does
not establish.

**11.** In a made-up department meeting, a resident presenting the penguin analysis says: "We did a
complete-case analysis, so missing data were not a problem." The analysis needs body mass,
flipper length and sex. Find out what the complete-case analysis did, and say what the
resident's sentence claims that the data cannot show.

