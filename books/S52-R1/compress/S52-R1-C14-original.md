# S52-R1-C14 · Categories as factors

**Definition.** A categorical variable takes one of a fixed, known set of values, such as sex or island. In R
it can be stored as text (a character vector) or as a factor. A factor stores each value
together with its levels: the list of allowed categories, in a set order. The order of the
levels decides the order of the rows in a count and of the categories in a table or plot.

`factor(x, levels = ...)` makes a factor with the levels given. A value of `x` that is not
among the levels becomes `NA`, without an error. With no levels given, they are taken from
the data in alphabetical order. `levels(f)` lists them.

Three functions come from the forcats package. The first, `fct_recode()`, renames levels,
written `new = "old"`, and leaves the others as they are. The second, `fct_relevel()`, moves
the named levels to the front. The third, `fct_infreq()`, orders the levels by how many rows have each one, largest first.

`count()`, from dplyr, gives the number of rows for each value of one column, or for each
combination of values of two or more columns. For a factor, `.drop = FALSE` also lists the
combinations that never occur, with a count of 0.

**In plain terms.** The last section counted what was missing. This one counts what is there, when what is there is
a category: female or male, Biscoe or Dream, a thali or a sandwich.

A category column has a short list of allowed values. Typed by hand, it rarely keeps to the
list. "Male", "male " with a space at the end, and "M" are three different values to R. Each one
becomes its own group in a count, and nobody meant three groups.

**count()** shows you every value a column actually holds, and how many rows hold it. Run it on
every category column before you do anything else with it. A misspelling shows up as an extra
row.

A **factor** is a category column that knows its list. You give the list, called the levels, and
their order. The order then decides how a count or a table is laid out.

Here is the trap. When you make a factor and a value is not on your list, R turns it into `NA`
and says nothing. A misspelt "Female" quietly becomes missing. So clean the text first, with the
tools from the section on making new columns, and count again after making the factor.

Codes need the same care. A file may store sex as 1 and 2. The data dictionary says which is
which, and **fct_recode()** writes that into the script: `female = "1"`. Never guess the codes
from the data.

Two counts at once, `count(species, island)`, is Book 0's two-way table, written as one row
per pair.

**Figure.** Rows of the penguin file on each island, in the order fct_infreq() gives: Biscoe 168, Dream 124, Torgersen 52. The order follows the counts; a fixed order from fct_relevel() would not.

*What the figure shows:* A bar chart with three bars in falling order: Biscoe 168, Dream 124, Torgersen 52.

**Must know points for you.**

- Run `count()` on every category column before you use it. Each misspelling, stray space or capital letter shows up as an extra row, and that is the only place it shows up.
- The error is to think `factor()` warns about a value that is not one of its levels. It does not. The value becomes `NA`, silently. Count the factor after making it, and treat any new `NA` as a spelling you missed.
- Turn numeric codes into labelled categories with the labels from the data dictionary, written once in the script with `fct_recode()`. Refuse a summary that averages a code.
- If you misspell an old level in `fct_recode()`, R warns "Unknown levels" and leaves that level unchanged. Read the warning; it means a category you meant to rename is still there.
- Set the order of the levels on purpose, with the levels you list or with `fct_relevel()`. The order decides how every later count, table and plot is laid out.
- Use `.drop = FALSE` when you need the categories with no rows. A table that leaves out its zeros hides that a combination never occurred.
- A clean count shows how many rows hold each category. It cannot show that the category was recorded correctly in the first place. A patient entered as male when female stays male in every count.

**Exercise 1** (calculation). In your penguin script, make `sex` a factor with the levels "female" and "male", in that order,
from the file's `Sex` column. Count it, and say how many penguins have no recorded sex.

**Exercise 2** (retrieval). Without looking back, say what `factor()` does with a value that is not among the levels you
gave it. Then name the line you run to catch that.

**Exercise 3** (teaching). A first-year resident has ten minutes and a whiteboard. Their thesis data has a column
`tobacco` coded 0, 1 and 2, and they have reported "mean tobacco use 0.8". Explain what is
wrong, and show them how to fix it.

**1.** Before you run it, say what this prints, and in what order the levels come.

```r norun
factor(c("Dream", "Biscoe", "Dream", "Torgersen"))
```

**2.** Before you run it, say what the levels of the result are, in order.

```r norun
library(forcats)

fct_infreq(c("rice", "roti", "rice", "millet", "rice", "roti"))
```

**3.** A made-up column codes the meal eaten as 1 (breakfast), 2 (lunch) or 3 (dinner). Turn it into
a factor with those labels.

```r
meal_code <- c(2, 3, 3, 1, 2)
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

Count the rows for each value of `Clutch Completion`. What does a "No" mean, according to the
data's help page?

**5.** Read the penguin file.

```r
library(readr)
library(dplyr)
library(forcats)

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

Make a factor of island in which Torgersen comes first and the other islands keep their
alphabetical order. Count it.

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

Count the penguins of each species by sex, in one count. Which species has the most rows with
no recorded sex?

**7.** A colleague makes a factor from a made-up register and reports: "2 of the 6 patients were
female."

```r
library(dplyr)

register <- tibble(sex = c("female", "Female", "male", "female", "Female ", "male"))

register |>
  mutate(sex = factor(sex, levels = c("female", "male"))) |>
  count(sex)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

# A tibble: 3 × 2
  sex        n
  <fct>  <int>
1 female     2
2 male       2
3 <NA>       2
```

Find what broke, and why the report looks reasonable.

**8.** A colleague shortens the species names in the penguin file:

```r
library(readr)
library(dplyr)
library(forcats)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)

penguins_raw |>
  mutate(
    species = fct_recode(
      Species,
      Adelie = "Adelie Penguin (Pygoscelis adeliae)",
      Chinstrap = "Chinstrap Penguin (Pygoscelis antarctica)",
      Gentoo = "Gentoo penguin (Pygoscelis papua)"
    )
  ) |>
  count(species)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

# A tibble: 3 × 2
  species                                       n
  <fct>                                     <int>
1 Adelie                                      152
2 Chinstrap penguin (Pygoscelis antarctica)    68
3 Gentoo                                      124
Warning message:
There was 1 warning in `mutate()`.
ℹ In argument: `species = fct_recode(...)`.
Caused by warning:
! Unknown levels in `f`: Chinstrap Penguin (Pygoscelis antarctica)
```

Their table has three rows, labelled "Adelie", "Chinstrap penguin (Pygoscelis antarctica)" and
"Gentoo". They decide the file's Chinstrap name is "too long to fix" and leave it. Find what
broke.

**9.** A made-up study's data dictionary says sex is coded 1 = male, 2 = female. A resident writes:

```r
library(dplyr)
library(forcats)

study <- tibble(sex_code = c(2, 2, 1, 2, 1, 2, 2))

study |>
  mutate(sex = fct_recode(as.character(sex_code), female = "1", male = "2")) |>
  count(sex)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union

# A tibble: 2 × 2
  sex        n
  <fct>  <int>
1 female     2
2 male       5
```

Their results say "5 of the 7 participants were male". Find what broke.

**10.** A made-up draft report says: "Of the 333 penguins with sex recorded, {{n:penguins_male}} were male." Check the
sentence against the penguin file and say what it does not establish.

**11.** In a made-up meeting, someone says: "The penguin data show that Gentoo penguins live only on
Biscoe." Turn the claim into a count, run it, and say what the result does and does not
establish.

