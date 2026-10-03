# S52-R1-C17 · Reshaping and joining

**Definition.** `pivot_longer()`, from the tidyr package, makes a data frame longer: it turns a set of
columns into two, one holding the old column names and one holding their values, and
repeats the other columns. It increases the rows and decreases the columns. `pivot_wider()`
does the reverse.

A key is a column, or set of columns, whose values pick out the row they belong to. A join
combines two data frames, `x` and `y`, by matching rows whose keys are equal.
`left_join(x, y)`, from the dplyr package, keeps every row of `x` and adds the columns of
`y`. A row of `x` with no match in `y` gets `NA` in the new columns. A row of `x` that
matches several rows of `y` appears once for each match. `anti_join(x, y)` returns the rows
of `x` that have no match in `y`.

`by` names the key. Left out, the join uses every column whose name the two data frames
share. The `relationship` argument states how many matches each row is expected to have, and
the join stops with an error if the data break it.

**In plain terms.** The last section summarised one data frame. Real data often arrive in two shapes that summaries
cannot use directly. This section fixes both.

**The wide table.** A clinic writes a patient's weight at three visits in three columns: visit 1,
visit 2, visit 3. It reads well on paper. But "visit" is a variable, and here its values sit in
the column names. There, `summarise(.by = visit)` cannot reach them.

**pivot_longer()** turns the three columns into two: one saying which visit, one saying the
weight. Three patients with three visits become nine rows, one per patient per visit.
**pivot_wider()** turns it back, for the table you print.

**The two files.** A survey sends the demographics in one file and the measurements in another,
with a participant number in both. That number is the key. **left_join()** matches the rows of
the two files on the key and puts the columns side by side. It keeps every row of the first file.
A row with no partner in the second file gets `NA`.

Here is the trap with joins. Suppose a key appears twice in the second file, by a slip in data
entry. Then the matching row of the first file appears twice in the result. No error, no warning.
The row count goes up by one, and every summary afterwards counts that person twice.

So count the rows before and after every join. Find keys that appear more than once. Find rows that did not match
with **anti_join()**. And tell the join what you expect with `relationship`, so it stops when
the data break the rule.

A join is one of the oldest operations in computing. Databases do it in a language called SQL,
and the next level of this subject teaches it there.

**Figure.** Rows in the two NHANES 2021–2023 files and in their join on SEQN. The body measures file has 8860 rows and the demographics file 11933. The left join of body measures to demographics keeps 8860, and the 3073 demographic rows with no body measures are participants who were interviewed but not examined. These are counts of rows, not survey estimates.

*What the figure shows:* A bar chart of four counts: body measures file 8860, demographics file 11933, joined file 8860, demographic rows with no match 3073.

**Must know points for you.**

- Count the rows before and after every join. A `left_join()` that returns more rows than went in has found a key that appears more than once in the second table. It says nothing about it.
- The error is to think a join only adds columns. It also adds rows when a key repeats, and every count and mean after it counts those rows again. Say what you expect with `relationship`, so the join stops when the data break it.
- Before a join, check the key in each table: count each value with `count()` and keep those with `n > 1`. After it, find the rows that did not match with `anti_join()`, and find out why.
- Always write `by`. Left out, the join matches on every column the two tables share by name. A column called `year` or `date` that means different things in each will then quietly match nothing.
- A wide table with one column per visit, district or year has values of a variable in its column names. Turn it long with `pivot_longer()` before summarising, and wide again only for the table you print.
- A mean at each visit compares visits only if the same people are in every visit. Print the count at each visit. A mean that moves when someone misses a visit is a change in who was measured, not in weight.
- When a trainee's merged thesis file "has a few more rows than it should", do not let them delete rows by hand. Ask for the key counts before and after the join, and fix the duplicate in code.
- The join checks can tell you that keys match and how often. They cannot tell you that two rows with the same key are really the same person. An ID reused for two people, or typed wrongly, joins two people's data without a trace.

**Exercise 1** (calculation). Add to a script the join of the NHANES body measures file to the demographics file on `SEQN`.
Print five counts: the rows of each file, the rows of the result, the body-measures rows with no
demographics, and the joined rows with an age of 20 or over. State what each count tells you.

**Exercise 2** (critique). A colleague merged her thesis questionnaire file with the laboratory results in a spreadsheet.
She sorted both by participant ID, pasted the laboratory columns beside the questionnaire
columns, and saved the result as a new file. Say what can go wrong, and how to do it in code.

**Exercise 3** (retrieval). Without looking back, say what each of these returns: `pivot_longer()`, `pivot_wider()`,
`left_join(x, y)` and `anti_join(x, y)`.

**1.** A made-up table:

```r
library(tidyr)
library(dplyr)

screen <- tibble(child = "A", height_2024 = 121, height_2025 = 127)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Make it long, with a column `year` and a column `height_cm`. How many rows will it have?

**2.** A made-up long table:

```r
library(tidyr)
library(dplyr)

long <- tibble(
  district = c("Durg", "Durg", "Korba", "Korba"),
  round = c("r1", "r2", "r1", "r2"),
  screened = c(410, 455, 380, 362)
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Make it wide, with one row per district and one column per round.

**3.** Two made-up tables:

```r
library(dplyr)

x <- tibble(id = c(1, 2, 3), weight_kg = c(60, 72, 55))
y <- tibble(id = c(2, 3, 3, 4), ward = c("A", "B", "C", "D"))
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Before you run `left_join(x, y, by = "id")`, say how many rows the result will have and which
`ward` each row gets. Then run it.

**4.** Read the two NHANES files.

```r
library(dplyr)

bmx <- haven::read_xpt(here::here("data-raw", "BMX_L.xpt"))
demo <- haven::read_xpt(here::here("data-raw", "DEMO_L.xpt"))
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Check that `SEQN` identifies one row in each file: count how many values of `SEQN` appear more
than once in each.

**5.** Read the penguin file.

```r
library(readr)
library(dplyr)
library(tidyr)

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

Make a table with one row per species and one column per island, holding the number of rows of
each species on each island. Put 0 where a species was not found on an island, and say why
that is the right value here.

**6.** Read the two NHANES files.

```r
library(dplyr)

bmx <- haven::read_xpt(here::here("data-raw", "BMX_L.xpt"))
demo <- haven::read_xpt(here::here("data-raw", "DEMO_L.xpt"))
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union
```

Join the age column `RIDAGEYR` to the body measures file. Then count how many examined
participants are children under 2, and how many of those have a standing height (`BMXHT`).
Say why the second count is what it is.

**7.** A colleague wants one tidy column of penguin measurements. He writes this, and reports
"the mean measurement of Gentoo penguins is 1780".

```r
library(readr)
library(dplyr)
library(tidyr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)

penguins_raw |>
  pivot_longer(
    cols = c(`Culmen Length (mm)`, `Flipper Length (mm)`, `Body Mass (g)`),
    names_to = "measure",
    values_to = "value"
  ) |>
  summarise(mean_value = mean(value, na.rm = TRUE), .by = Species)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

# A tibble: 3 × 2
  Species                                   mean_value
  <chr>                                          <dbl>
1 Adelie Penguin (Pygoscelis adeliae)            1310.
2 Gentoo penguin (Pygoscelis papua)              1780.
3 Chinstrap penguin (Pygoscelis antarctica)      1326.
```

Find what broke.

**8.** A made-up clinic keeps two tables. In `visits`, `year` is the year of the visit. In `register`,
`year` is the year of birth. A colleague joins them and reports "no patient's sex is recorded".

```r
library(dplyr)

visits <- tibble(id = c(1, 2, 3), year = c(2025, 2025, 2026), bmi = c(26.2, 31.0, 23.4))
register <- tibble(id = c(1, 2, 3), year = c(1980, 1972, 1991), sex = c("F", "M", "F"))

visits |>
  left_join(register)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

Joining with `by = join_by(id, year)`
# A tibble: 3 × 4
     id  year   bmi sex
  <dbl> <dbl> <dbl> <chr>
1     1  2025  26.2 <NA>
2     2  2025  31   <NA>
3     3  2026  23.4 <NA>
```

Find what broke.

**9.** A colleague joins a made-up laboratory table to a register. The laboratory file was read with
every column as text.

```r
library(dplyr)

register <- tibble(id = c(101, 102, 103), sex = c("F", "M", "F"))
lab <- tibble(id = c("101", "102", "103"), hb = c("12.1", "14.3", "11.8"))
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
  left_join(lab, by = "id")
```

```output
Error in `left_join()`:
! Can't join `x$id` with `y$id` due to incompatible types.
ℹ `x$id` is a <double>.
ℹ `y$id` is a <character>.
```

Read the error. Say what broke and fix it.

**10.** A made-up methods section says: "We merged the NHANES 2021–2023 body measures and demographic
files on the sequence number; 11,933 participants had body measures." Check the claim, and say
what the merge does not establish.

**11.** In a made-up journal club, someone says: "In NHANES, women have a higher BMI than men." Turn the
sentence into code on the joined files, for adults aged 20 or over, run it, and say what the
result does not establish.

