# S52-R1-C09 · Reading a raw file without changing it

**Definition.** A CSV file, short for comma-separated values, is plain text. Each line is one row; within a
line, values are separated by commas; the first line, the header row, gives the column names.
Nothing in the file says what type each column is.

Reading a file copies its contents into R as a data frame. The file on disk is not changed by
being read, and an analysis that never writes to it can always be rerun from it.

`read_csv()`, from the readr package, reads a CSV file. It guesses each column's type from a
sample of its values and prints the guess, the column specification. Values listed in its `na`
argument become `NA`, R's code for a missing value; by default the list is the empty string and
the text `NA`. The `col_types` argument states the types you expect instead of letting readr
guess. A value that does not fit its stated type becomes `NA`, readr warns, and `problems()`
lists each such value with its row and column.

Other formats need other functions. `read_excel()`, from readxl, reads Excel `.xls` and `.xlsx`
files, one sheet at a time, optionally from a stated cell range. From haven, `read_sav()` reads
SPSS `.sav` files and `read_xpt()` reads SAS transport `.xpt` files; both keep each column's
label, the description stored with it in the file, as a label attribute of that column.

**In plain terms.** A raw file is the data as it first reached you. It may be the export from a survey tablet, the
file a laboratory machine wrote, or the spreadsheet a camp team typed. Tools for collecting data in the
field, such as KoboToolbox, ODK and REDCap, write such files, and the next level of this subject
teaches them. Here the file has already arrived.

The commonest raw file is a CSV. Open one in a plain text editor, such as Notepad, and you see
lines of text with commas between the values. The first line holds the column names. That is
all there is: no colours, no formulas, and nothing saying which column is a number.

So `read_csv()` has to guess. It looks at the values in each column and decides: numbers, text,
dates or TRUE and FALSE. Then it prints what it decided. Read that report every time. A column
you expected to be numbers that comes out as text means some cell in it is not a number.

Two habits keep the guess honest:

- **Name the missing-value codes.** If the file uses -99, or "NR", for "not recorded", say so
  in `na = c("", "NA", "-99", "NR")`. Otherwise -99 is read as a real number.
- **Say what you expect.** `col_types` tells `read_csv()` which type each column should have.
  A value that does not fit is reported, instead of quietly turning the whole column into text.

Reading never changes the file. `read_csv()` makes a copy inside R and leaves the file alone.
The file is changed only if something writes to it: you, in a spreadsheet, or a line of code
that saves over it. In this book nothing does.

Data in a department may come as an Excel or SPSS file, and some surveys publish files in other
formats. `read_excel()` reads Excel files. The haven package reads SPSS files with `read_sav()`
and the SAS transport files of American surveys with `read_xpt()`.

**Figure.** Missing values in four body-measure columns of the NHANES 2021–2023 body measures file, as read_xpt() reads it: weight 106, height 361, BMI 389, waist 670 rows. BMI is missing in exactly the 389 rows that lack a weight or a height. These are counts of rows in the file, not survey estimates.

*What the figure shows:* A bar chart with four bars. BMXWT 106, BMXHT 361, BMXBMI 389, BMXWAIST 670 missing values.

**Must know points for you.**

- The error is to think that a file which reads without an error has been read correctly. -99 read as a height raises no warning. Read the column report, and declare every missing-value code from the file's documentation in `na` before you compute anything.
- Giving `na` replaces the default list. Write `na = c("", "NA", "-99")`, not `na = "-99"`; the second form stops reading empty cells and the text "NA" as missing.
- A number column that the report calls `chr` holds at least one value that is not a number. Find it with `col_types` and `problems()`, then deal with it in code. Never open the raw file and retype the cell.
- Record the MD5 checksum of every raw file in the README on the day it arrives. When someone says "it's the same file", you can check in one line instead of arguing.
- Open an Excel file you were sent only as a copy. Browsing the original invites typing into it or saving over it by accident. Read the original into R with `read_excel()`, giving the sheet and range.
- When a department hands over an SPSS file, read it with `read_sav()` rather than asking for an Excel export. The SPSS file carries its labels and its missing-value codes; an export may drop both.
- Any average you compute from an NHANES file without its sample weights describes the people in the file only. Say "unweighted" next to it, and never present it as the figure for the United States, still less for India.
- Reading carefully catches codes and types. It cannot catch a wrong value that is a valid number: a height of 182 cm typed for 128 cm reads perfectly. That needs a check on the values themselves.

**Exercise 1** (retrieval). Without looking back, write the argument that makes `read_csv()` treat -99 as missing without
losing its default missing values. Then name the function that lists the values that did not
fit the types given in `col_types`.

**Exercise 2** (design). A district team sends you `screening_2026.csv`, exported from their form. Its documentation
says four things:

- height and weight are in cm and kg;
- 999 means "not measured";
- "NR" means "not recorded";
- `village_code` is a code with leading zeros, such as 0042.

Write the reading line, with every
argument you need, and say what each argument protects you from.

**Exercise 3** (interpretation). You read a made-up clinic file and `read_csv()` prints this report:

`Rows: 1250 Columns: 6`, then `chr (3): patient_id, sex, weight_kg` and `dbl (3): age_years,
height_cm, visit_no`.

What does the report tell you, what does it not tell you, and what do you do next?

**1.** Read this made-up CSV text with `read_csv()` and print the result. Wrap the text in `I()`.

```r norun
"district,children,with_obesity
Raipur,410,23
Durg,385,19"
```

**2.** In this made-up text, -1 means "not recorded". Read it so that -1 becomes `NA`, keeping the
default missing values too, and print it.

```r norun
"child_id,age_years
A1,7
A2,-1
A3,9"
```

**3.** Read this made-up text with `col_types` given as a short string, one letter per column: `c`
for text and `d` for numbers. Print the result.

```r norun
"ward,beds,occupied
A,30,27
B,24,24"
```

**4.** Read the Excel example workbook that comes with readxl, `readxl_example("deaths.xlsx")`, taking
only the cells `A5:C8` of the sheet called `arts`. How many rows and columns do you get?

**5.** Read the penguin file with its column report showing. How many columns were read as text, as
numbers and as dates? Which numeric columns would you expect, from their names?

**6.** Read the NHANES demographics file, `DEMO_L.xpt`, from the project's `data-raw` folder. Give its
number of rows and columns, and the label of the column `RIDAGEYR`.

**7.** A resident wants all the measurements read as numbers. She writes this, gets a warning, and
notes "child IDs missing in the file". Run it. Find what broke and why her note looks
reasonable. The data are made up.

```r
library(readr)
camp <- read_csv(I("child_id,height_cm,weight_kg
S01,128,26.0
S02,133,24.5
S03,131,27.5"), col_types = cols(.default = col_double()))
camp
```

```output
Warning message:
One or more parsing issues, call `problems()` on your data frame for
details, e.g.:
  dat <- vroom(...)
  problems(dat)
# A tibble: 3 × 3
  child_id height_cm weight_kg
     <dbl>     <dbl>     <dbl>
1       NA       128      26
2       NA       133      24.5
3       NA       131      27.5
```

**8.** The penguin file has no -99 codes, but a resident adds `na = "-99"` to be safe. Then she counts
the penguins of unknown sex and finds none. Run her code. Find what broke, and why the answer
looked believable.

```r
library(readr)
library(here)
penguins_raw <- read_csv(here("data-raw", "penguins_raw.csv"), na = "-99")
sum(is.na(penguins_raw$Sex))
```

```output
here() starts at ~/project
Rows: 344 Columns: 17
── Column specification ────────────────────────────────────────────────
Delimiter: ","
chr  (15): studyName, Species, Region, Island, Stage, Individual ID,...
dbl   (1): Sample Number
date  (1): Date Egg

ℹ Use `spec()` to retrieve the full column specification for this data.
ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
[1] 0
```

**9.** A slide at a journal club says: "NHANES 2021–2023 measured {{n:bmx_rows}} people; their mean weight was
70.5 kg." Check the two numbers against the body measures file, and say what the slide's
sentence does not establish.

**10.** A colleague says: "I only opened the CSV in Excel to look at it and saved it. Nothing changed;
it is still the original." The project's README recorded the file's MD5 checksum on the day it
arrived: `049da101568e078f9845c8b366481810`. Decide what to compute, and compute it for the
project's copy. Then show what a single hand edit does to the checksum, using a copy in
`output/`. Say what the check does not establish.

