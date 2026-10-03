# S52-R1-C08 · Tidy data and the data frame

**Definition.** A data frame is R's table. It is a set of named columns placed side by side, where each column
is a vector and every column has the same number of elements, so the columns line up into rows.
Different columns may hold different types, but all the values within one column share one
type.

A tibble is the form of data frame the tidyverse uses. It prints its number of rows and
columns and the type of each column.

A variable, in the sense used here, is everything that measures one attribute, such as height,
across all the units measured. An observation is everything measured on one unit, such as one
child at one visit, across all the attributes.

Data are tidy (Wickham 2014) when three rules hold. Each variable forms a column. Each
observation forms a row. Each type of observational unit forms a table: facts about a child
that do not change between visits go in one table, and measurements made at each visit go in
another. Any other arrangement is untidy.

Three untidy shapes are common. Values are used as
column names, as when weight at visits 1, 2 and 3 sits in three columns. Two variables are
stored in one column, as in a blood pressure written "104/66". Two kinds of unit are stored in
one table.

**In plain terms.** Book 0 asked four questions of every table, and the first was: what does one row stand for?
Tidy data turns that question into rules for how a table is built.

In R a table is a data frame. Picture it as columns standing side by side. Each column is a
vector, a set of values of one type: all numbers, or all text. Every column has the same
length. So the first value of every column belongs to the first row, the second to the second
row, and so on. A tibble is the tidyverse's kind of data frame. It tells you its size and the
type of each column when it prints.

A table is tidy when three things are true:

- **One column, one variable.** Height in one column, weight in another, and nothing else in
  either.
- **One row, one observation.** One child at one visit is one row. A second visit is a second
  row, not a second column.
- **One table, one kind of unit.** A child's sex and date of birth do not change between visits,
  so they go in a table with one row per child. Weight at each visit goes in a table with one
  row per visit.

The word "variable" now has three meanings in this book, and they must be kept apart. In Book 0
it was a letter standing for a number. In R it is the name of an object you made. In a data
frame it is a column: everything measured about one attribute.

Data typed into a spreadsheet often break the rules. Weights at three visits sit in three
columns. Blood pressure is typed as "104/66" in one cell. Girls are marked by colouring their
rows pink. Each of these looks fine to the eye. Each stops the computer from using the data.

**Must know points for you.**

- The error is to read the number of rows as the number of people, or birds, or children. Ask first what one row stands for. Count the IDs, and check that an ID always points to the same person, before you write "n = " in a report.
- When a register has one column per visit, the visit is hiding in the column names. Store it as a column called `visit` with one row per visit. A fourth visit then adds rows, and no code changes.
- One cell, one value. "104/66", "45 kg", "2.3 or 2.4" and "0 (below detection)" each stop a column from being numbers. Split the two numbers into two columns, move the unit into the column name or the data dictionary, and put notes in a notes column.
- Colour and highlighting are not data. A row painted yellow to mean "recheck" is lost the moment the file is saved as CSV. Add a column, such as `recheck` with TRUE or FALSE, instead.
- Facts that do not change between visits, such as sex and date of birth, go in a table with one row per person. Repeating them on every visit row invites the day when the copies disagree.
- Before a data-entry team fills its first form, look at the sheet they designed. Ask for one header row, one rectangle, one value per cell and no merged cells. Fixing the layout later costs far more than agreeing it first.
- The word "variable" has three meanings: Book 0's letter, R's named object, and a data frame's column. When a trainee is confused, ask which one they mean before you answer.
- Tidy data makes the next step easy. It does not make the values right. A tidy table can hold a weight of 700 kg as neatly as one of 70 kg.

**Exercise 1** (retrieval). Without looking back, say what a data frame is made of, and what one row of the penguin file
stands for.

**Exercise 2** (critique). Here is a made-up data-entry sheet from a school health camp. It has one header row, with these
column headings: `Name`, `Class/Section`, `Ht 1 (cm)`, `Ht 2 (cm)`, `Wt (kg)`, `BMI`, `Remarks`. Rows for
children referred to the clinic are highlighted red. Find every place where the sheet breaks
the tidy rules or Broman and Woo's advice, and give the tidy layout.

**1.** How many rows and columns does this made-up tibble have? Check with `nrow()` and `ncol()`.

```r norun
tibble::tibble(x = c(1, 2, 3), y = c("a", "b", "c"))
```

**2.** Make a tibble of three made-up children with columns `child_id`, `height_cm` and `weight_kg`.
Print it.

**3.** Using the tibble from the previous problem, or the one below, pick out the weight column with
`$` and find its mean.

```r norun
children <- tibble::tibble(
  child_id = c("A01", "A02", "A03"),
  height_cm = c(121, 127, 118),
  weight_kg = c(22.5, 25.1, 20.9)
)
```

**4.** Read `penguins_raw.csv` from the project. Give its number of rows and columns, and the mean
flipper length of the penguins with one recorded, with its unit.

**5.** Which islands does the penguin file cover? Use `unique()` on the right column.

**6.** In the penguin file, how many rows come from each of the three expeditions named in the
column `studyName`? Use `table()`, which counts how often each value occurs. Then say what one
row of the file stands for, and why it is not "one penguin".

**7.** A resident tries to find the average body mass. Run her code. Find what broke and say why the
code looked right to her.

```r
library(readr)
library(here)
penguins_raw <- read_csv(here("data-raw", "penguins_raw.csv"), show_col_types = FALSE)
```

```output
here() starts at ~/project
```

```r error
mean(penguins_raw$Body Mass (g), na.rm = TRUE)
```

```output
Error: <text>:1:24: unexpected symbol
1: mean(penguins_raw$Body Mass
                           ^
```

**8.** A camp register is entered with blood pressure as text. The data are made up. A resident runs
this code to find the average blood pressure and writes "BP data not available" in her report.
Run it. Find what broke, and say why her conclusion looks reasonable.

```r
camp <- tibble::tibble(
  child_id = c("K1", "K2", "K3", "K4"),
  bp = c("102/64", "108/70", "96/60", "110/72")
)
mean(camp$bp)
```

```output
[1] NA
Warning message:
In mean.default(camp$bp) : argument is not numeric or logical: returning NA
```

**9.** A made-up thesis draft says: "Weight was recorded at three visits for each of the three
children (Table 2)." Table 2 has columns `child`, `visit_1`, `visit_2` and `visit_3`. The
weights are, in kilograms: child P1 18.2, 18.6, 19.1; P2 20.4, 20.9, 21.0; P3 17.5, 17.8, 18.4.
Build the tidy table, check its number of rows against the sentence, and find the mean weight.
Then say what your table does not establish.

**10.** In a meeting someone says: "The penguin file has data on {{n:penguins_rows}} penguins." Decide what to compute
to test the claim, compute it, and say what your answer does not establish.

