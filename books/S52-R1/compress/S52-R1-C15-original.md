# S52-R1-C15 · Dates

**Definition.** In R, a date is an object of class `Date`. It is stored as a number of days since 1 January
1970 and printed in the ISO 8601 form, year-month-day, such as 2021-04-03.

Text becomes a date by parsing: reading it according to the order of its parts. The lubridate
functions are named for that order. `ymd()` reads year, month, day; `dmy()` reads day, month,
year; `mdy()` reads month, day, year. Each accepts any separator. Text that does not fit the
order becomes `NA`, with a warning that says how many values failed to parse. `read_csv()`
recognises dates already written as year-month-day and leaves other forms as text.

Subtracting one date from another gives a time difference in days. Adding a number to a date
gives the date that many days later.

A spreadsheet such as Excel also stores a date as a number of days, counted from a starting
date of its own, and may export that number in place of the date.

**In plain terms.** The last few sections cleaned numbers, missing values and categories. Dates need cleaning too,
and they fail in quieter ways.

To R, a date is a number of days, counted from 1 January 1970, that prints as year-month-day.
Because it is a number underneath, you can subtract one date from another and get days. That is
how you work out a child's age at a camp, or the gap between screening and a clinic visit.

A date usually arrives as text, such as "03/04/2021". Text has to be read into a date, and to
read it R needs the order of the parts. Is that 3 April or 4 March? The text cannot tell you.
You tell R, by choosing the function whose name spells the order: **dmy()** for day first,
**mdy()** for month first, **ymd()** for year first.

Here is the trap. If you pick the wrong order, some dates come out wrong and still look like
dates. Others fail and become `NA`. A warning tells you how many failed. Read it, and look for
a date whose day is above 12, which settles the order for the whole column.

The cure for all of this is in how dates are written down. Broman and Woo recommend the ISO 8601
form, year-month-day: 2021-04-03. It sorts correctly, it cannot be read two ways, and
`read_csv()` reads it as a date by itself. Data Carpentry's lesson gives other options, such as
year, month and day in separate columns. Pick one, and write it in the data dictionary.

Spreadsheets add one more trap. They store a date as a count of days from their own starting
date, and sometimes that count is what reaches you. Convert it in code, and check one date you
already know.

**Must know points for you.**

- The error is to think a wrongly parsed date will show up as an error. Read day-first text with `mdy()`, and every date whose day is 12 or less comes out as a real, wrong date. Only the others fail.
- Before parsing a date column, find out the order of its parts from the data dictionary or the form. Then look for a value with a day above 12; it confirms the order.
- Read every "failed to parse" warning. The number in it is the count of dates you have turned into `NA`. They will drop out of every later count without another word.
- When you design a form or a register, write dates as year-month-day, ISO 8601, as Broman and Woo recommend. Such a date cannot be read two ways, sorts correctly as text, and is read as a date by `read_csv()` with no extra step.
- A spreadsheet date may reach you as a day count such as 41822. Convert it in code, and check the result against one date you know. The starting date differs between systems, and a one-day or four-year slip looks like a real date.
- Compute age from the date of birth and the visit date, never by subtracting years. Subtracting years makes anyone whose birthday has not yet come a year too old.
- Parsing can only read what was written. If a spreadsheet already turned a gene name or a date into something else, no function in R can tell you what was there before.

**Exercise 1** (calculation). In your penguin script, give the date of the first and the last nest observed in the file, and
the number of days between them.

**Exercise 2** (retrieval). Without looking back, say which lubridate function reads "28/02/2021", and what `mdy()` would
give for "03/04/2021".

**Exercise 3** (design). You are designing the data-entry sheet for a made-up school survey that records each child's
date of birth and the date they were measured. Write the two lines of the data dictionary for
these columns, and say what the analysis script will do with them.

**1.** Turn the text "2023-11-14" into a date. Say what class the result has.

**2.** Before you run them, say what each line gives.

```r norun
library(lubridate)

dmy("05/06/2022")
mdy("05/06/2022")
```

**3.** Before you run it, say how many days this gives, and why.

```r norun
library(lubridate)

ymd("2024-03-01") - ymd("2024-02-01")
```

**4.** Read the penguin file.

```r
library(readr)

penguins_raw <- read_csv(
  here::here("data-raw", "penguins_raw.csv"),
  show_col_types = FALSE
)
```

How many days separate the first nest observed in the file and the first nest of the
second season, which starts on 2008-11-02?

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

How many nests were observed in November 2008?

**6.** A made-up register records two children measured at a school camp. Work out each child's age at
measurement in completed years.

```r
library(dplyr)
library(lubridate)

children <- tibble(
  id = c("C1", "C2"),
  dob = dmy(c("21/06/2014", "05/12/2013")),
  measured = dmy(c("20/06/2024", "20/06/2024"))
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union


Attaching package: ‘lubridate’

The following objects are masked from ‘package:base’:

    date, intersect, setdiff, union
```

**7.** A colleague reads a made-up register whose dates were typed day first, and reports: "Visit dates
were missing for all three patients."

```r
library(lubridate)

visits <- c("12/01/2022", "19/01/2022", "26/01/2022")
ymd(visits)
```

```output

Attaching package: ‘lubridate’

The following objects are masked from ‘package:base’:

    date, intersect, setdiff, union

[1] NA NA NA
Warning message:
All formats failed to parse. No formats found.
```

Find what broke.

**8.** A colleague reads a made-up register whose dates were typed day first. They report: "1 of the 3
screening dates was missing; the first patient was screened on 2 March 2023."

```r
library(lubridate)

screened <- c("02/03/2023", "11/03/2023", "17/03/2023")
mdy(screened)
```

```output

Attaching package: ‘lubridate’

The following objects are masked from ‘package:base’:

    date, intersect, setdiff, union

[1] "2023-02-03" "2023-11-03" NA
Warning message:
 1 failed to parse.
```

Find what broke.

**9.** A made-up spreadsheet export gives two visit dates as day counts, 45292 and 45306. The colleague
who exported it remembers that the first visit was on 1 January 2024. A resident converts them:

```r
library(lubridate)

ymd("1899-12-31") + c(45292, 45306)
```

```output

Attaching package: ‘lubridate’

The following objects are masked from ‘package:base’:

    date, intersect, setdiff, union

[1] "2024-01-02" "2024-01-16"
```

They report: "The first visit was on 2 January 2024." Find what broke.

**10.** A made-up clinic note says: "The median time from screening to the first clinic visit was 14
days." Here are the dates for the five patients it describes, typed day first.

```r
library(dplyr)
library(lubridate)

clinic <- tibble(
  id = c(1, 2, 3, 4, 5),
  screened = dmy(c("02/05/2024", "02/05/2024", "09/05/2024", "09/05/2024", "16/05/2024")),
  visited = dmy(c("13/05/2024", "20/05/2024", "23/05/2024", "06/06/2024", "30/05/2024"))
)
```

```output

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union


Attaching package: ‘lubridate’

The following objects are masked from ‘package:base’:

    date, intersect, setdiff, union
```

Check the claim, and say what your answer does not establish.

**11.** A made-up draft report on the penguin file says: "All penguins in the 2008–09 season laid their
first egg in November 2008." The `studyName` column names the season; PAL0809 is 2008–09. Check
the claim in code, and say what the file can and cannot support.

