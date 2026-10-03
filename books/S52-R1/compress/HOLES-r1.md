# S52-R1 step 5c, batch r1 (C01 to C11): holes for the fixer

These gaps could not be closed by restoring the original's own sentences. For each, the original
has the same gap, or the gap is an error or contradiction, or it sits in an illustration, practice
problem or exercise (which the cut did not touch), or restoring broke validation. Gap ids refer to
`COLDREAD-REPORT-A.md`. "As it stands" quotes the final text (`<S>-final-prose.yml`) or, for
illustrations, problems and exercises, the record. Nothing here has been fixed. Any fix that adds or
changes a code block or its output goes through the code gate. "Residual" marks the part left
after a restore.

Field names: `illustrations[n]` is Illustration n+1 as printed; Pn is practice problem n; Ex n is
exercise n.

## C01

**H1 · A-C01-1 · illustrations[0] (working block)**
As it stands: "704 ÷ 3597 = 0.1957 / 0.1957 × 100 = 19.57"
Wrong: ÷ and × are never introduced, and Book 0's records contain no ÷ at all (checked: no hit in `check/records/B0`). C02 then teaches `/` and `*` as replacements for signs the reader may never have seen.
To close: write the working as Book 0 writes it (in words, or with `/`), or add a one-line gloss at first use.

**H2 · A-C01-2 · simplified_explanation, must_know[2]**
As it stands: "Every change you make to the data is a line of code, kept in a file, that anyone can read and run again." / "Write it as a line of code with a comment saying why."
Missing: "line of code", "comment" (and "reproducible code" in illustrations[1]) are used before C02 defines them. Minor; no exercise blocked.
To close: a one-line pointer ("C02 shows what a line of code and a comment look like").

**H3 · A-C01-3 · illustrations[1]**
As it stands: "So did the exclusions alone, and so did the weighting alone."
Missing: weighting is never explained (the original prose only names "inappropriate weighting of summary statistics"). The reader cannot follow why weighting mattered. Also worth checking against Herndon, Ash and Pollin's Table 3 that each problem alone gives 1.9%.
To close: one or two sentences saying that each country's average counted equally whatever its number of years (from the source), and confirm the "alone" figures.

**H4 · A-C01-4 · definition.text / illustrations[0]**
As it stands (illustration): "Of the 987 files with errors, 166 held nothing else ..."
Missing: the switch from 704 papers to 987 files. The original's "They confirmed gene name errors in 987 files from 704 articles, which is ... of the 3597 articles whose Excel files held gene lists." (28 words) would close it, but raised C01's mean sentence length from 14.00 to 14.17 (fail).
To close: in the illustration, one short sentence: "Those 704 papers held 987 files with errors."

## C02

**H5 · A-C02-1 · simplified_explanation**
As it stands: "Install R first, then RStudio, from their own websites."
Missing: where the websites are, and the steps. The reader cannot install.
To close: name the two sites (CRAN and Posit's RStudio download page) and the one-line choice the reader makes (installer for their system).

**H6 · A-C02-2 (residual) · simplified_explanation**
As it stands: "Open RStudio and you see several panes. ... **The console** is where R waits for you."
Missing: where the console sits in the window (by default the lower left; the script editor above it).
To close: one sentence locating the console and the script editor.

**H7 · A-C02-4 · illustrations[0]**
As it stands: "One more slip. Book 0 taught you the sign ÷."
Wrong: Book 0's records do not use ÷ (see H1). Error, not missing text. The kept "Times is `*`, not ×. Divided by is `/`, not ÷." carries the same assumption.
To close: "You may have learnt the sign ÷ at school." or drop the attribution to Book 0.

**H8 · A-C02-5 (residual) · illustrations[0] output**
As it stands: "Error: <text>:1:4: unexpected input" with the restored "It says what it could not do and, for a line it could not read, where on the line it stopped."
Missing: that `1:4` is line 1, character 4.
To close: one clause in the illustration's reading of the message.

**H9 · A-C02-8 · must_know[1]**
As it stands: "Typing × or ÷ stops R with an error, and typing the letter x as times does too."
Missing: the letter x case is never shown (and its error differs: "unexpected symbol").
To close: a code line in illustrations[0] (code gate), or cut the clause.

**H10 · A-C02-9 · illustrations[0]**
As it stands: "An adult's BMI is a number in the tens."
Wrong: cross-book contradiction; the reader reports B6 declined to give typical values. Needs Harsh's decision on whether this book may state a plausible range.
To close: align with B6, or say what "in the tens" is based on.

**H11 · A-C02-10 · definition.text / simplified_explanation**
Missing: whether spaces inside a line matter (`72/1.6` versus `72 / 1.6`). The original is silent.
To close: one sentence ("Spaces around signs do not matter to R; this book puts them in so the line reads easily").

**H12 · A-C02-11 · simplified_explanation**
As it stands: "Select every line and press Ctrl and Enter, and the whole file runs from the top."
Missing: how to select all (Ctrl and A), and Mac keys (Cmd).
To close: a parenthesis with both.

**H13 · A-C02-12 · illustrations[1] output**
Missing: when a script runs, RStudio echoes each code line into the console before its answer; the output block shows only the answers.
To close: show the echo or say it is left out (code gate if the output block changes).

## C03

**H14 · A-C03-1 (residual) · simplified_explanation, must_know[1]**
As it stands: "That list is not your script. It holds every line you ran today, in whatever order you ran it, including lines you typed only in the console."
Wrong: the workspace (and `ls()`) holds objects, not lines. The original says the same.
To close: "It holds every object made by whatever you ran today ..." (and the same in must_know[1]).

**H15 · A-C03-3, A-C11-10 · definition.text (C03)**
As it stands: "Write names in small letters, with `_` between words, and put the unit in the name" (simplified_explanation). The illustration speaks of "The style guide's snake case ... the tidyverse made".
Missing: "snake case", "style guide" and "tidyverse" are undefined at first use; snake case is defined only in C11, tidyverse in C06. The original's "The tidyverse style guide asks for names in lower case, with words joined by `_` (snake case), and for `<-` rather than `=` for assignment." (25 words) would close the first two, but raised C03's mean from 11.94 to 12.29 (original 12.15) under the third splitter.
To close: the same content in two short sentences, with a pointer to C06 for the tidyverse.

**H16 · A-C03-4 · definition.text, simplified_explanation**
As it stands: "RStudio shows it in the Environment pane, and `ls()` prints it."
Missing: where the Environment pane is (by default upper right).
To close: one clause.

**H17 · A-C03-5 (residual) · illustrations[0]**
As it stands: "Book 0's algebra letter is the wrong picture here. In `BMI = w / h^2`, w stands for whatever ..."
Unverified: the reader says Book 0 never wrote `BMI = w / h^2`; no such formula was found in Book 0's records. Needs a check against Book 0.
To close: quote Book 0's own form, or drop "Book 0's".

## C04

**H18 · A-C04-3 · illustrations[0]**
As it stands: "You get `NA` and a warning, not a number." / "That one stops with an error."
Missing: the difference between a warning (R carries on) and an error (R stops); and `mean.default` (explained only in C05).
To close: one sentence after the first warning; move or copy C05's gloss of `mean.default`.

**H19 · A-C04-4 · simplified_explanation; P9**
As it stands: "height_cm > 155" (code) and P9's `bmi >= 25`.
Missing: `>` is never named "greater than", and `>=` never appears before P9 (C11's definition lists the signs without meanings, H70).
To close: one line naming `>`, `<`, `>=`, `<=`, `==`, `!=` at first use.

**H20 · A-C04-5 · P2**
As it stands: "c(0, TRUE, FALSE)"
Missing: that TRUE becomes 1 and FALSE 0 when mixed with numbers. Taught only in C05's illustration.
To close: one line in the coercion paragraph, or move P2's second line to C05.

**H21 · A-C04-6 · P5**
As it stands: "Then print the body masses of the first three penguins in grams."
Missing: several positions inside `[ ]` (`x[1:3]` or `x[c(1, 2, 3)]`) are never taught.
To close: one code line in the simplified explanation's bracket example (code gate), or change P5.

**H22 · A-C04-7 · P7**
As it stands: "height_cm <- c("98", "102", "110") / max(height_cm) / [1] "98""
Missing: `max()` and the rule that text sorts character by character. The reader cannot explain the output.
To close: a gloss of `max()` and one sentence on text ordering, or move P7 later.

**H23 · A-C04-8 · P9**
As it stands: "bmi <- c(22.1, 27.4, "NA", 30.2, 25.8) / bmi >= 25"
Missing: what happens when text is compared with a number (the number is turned into text, then compared as text).
To close: one sentence, or change P9.

**H24 · A-C04-9 · P11**
As it stands: "Of the first ten penguins in the file, two weighed more than 4000 g." Check with code.
Wrong-prediction trap: `body_mass_g[body_mass_g > 4000]` returns 4675, 4250 and an `NA`, which is never taught. An honest prediction is wrong.
To close: one sentence that an `NA` in a logical index gives an `NA` element (and point to `!is.na()` or `which()`), or add the case to Illustration 2 (code gate).

**H25 · A-C04-10 · Ex 1**
As it stands: "Say ... how the analysis should go on without editing anything by hand."
Missing: replacing one element in code (`hb_g_dl[3] <- "9.8"` or rebuilding) is never taught.
To close: a code line in Illustration 1 (code gate), or reword Ex 1 to ask only what should happen.

**H26 · A-C04-14 · simplified_explanation output**
As it stands: "[1] 152.0 160.5 171.0"
Missing: why 152 prints as 152.0 (a vector prints with one shared number of decimals) and why long outputs start with a space before `[1]`.
To close: one sentence each, or accept as minor.

## C05

**H27 · A-C05-1 · definition.text**
As it stands: "For `mean()`, `median()` and `sd()`, the argument `na.rm` says whether missing values (`NA`) are removed before the computation."
Missing: that `sd()` is Book 0's sample standard deviation, dividing by n − 1. P5 needs it.
To close: one gloss at first use.

**H28 · A-C05-2 · illustrations[1]**
As it stands: "So `trim` became 0.5, and the "mean" of the single value 3750 is 3750."
Missing: what `trim` does (drops a fraction of values from each end before averaging). The explanation reads as circular.
To close: one sentence from the help page's own words.

**H29 · A-C05-4 · simplified_explanation**
As it stands: "The pipe, written `|>`, puts the steps in the order they happen."
Missing: how to type `|>`, that a line ending in `|>` continues on the next (C02's `+` prompt), and that the indent is for reading only.
To close: one or two sentences.

**H30 · A-C05-6 · illustrations[0], must_know[6]**
As it stands: "Which values go missing, and why, is a question for a later rung." / "Writing one is taught at the next rung of this subject."
Missing: "rung" is course vocabulary, undefined for this reader (S01 recorded the same as GL-2).
To close: "a later book in this course", or define rung once at the book's front.

## C06

**H31 · A-C06-2 · simplified_explanation, illustrations[0]**
As it stands: "**Load it, in every session.**" / "Start a fresh R session ..."
Missing: what a session is, and how to start a fresh one (close and reopen R, or Session, Restart R in RStudio). C03's original definition ("... the current session (R from the moment it starts until it is closed or restarted) ...", 30 words) would close it but raises C03's mean from 12.32 to 12.97 (original 12.57; measured under the old splitter).
To close: a short gloss in C06 at first use.

**H32 · A-C06-3 · definition.text; P6**
Missing: why `install.packages("dplyr")` takes quotes and `library(dplyr)` does not. P6 turns on this.
To close: one sentence ("install.packages() needs the name as text, in quotes; library() accepts the bare name").

**H33 · A-C06-7 · P4**
As it stands: "Without loading any package, count the rows of `penguins_raw.csv` in your project's `data-raw` folder ..."
Missing: the project and the file do not exist until C07, and here/path/project are forward references.
To close: move P4 after C07, or tell the reader where to get the file and set it up first.

**H34 · A-C06-8 · illustrations[0]**
As it stands: "The file has 344 rows, one for each nesting observation of a penguin."
Missing: "nesting observation" undefined (C08 discusses what a row is, also without defining it).
To close: a gloss from the palmerpenguins documentation.

**H35 · A-C06-10 · illustrations[1]**
As it stands: "packageVersion("dplyr") >= "1.1.0""
Missing: why a version can be compared with text (`packageVersion()` returns a version object that compares numerically).
To close: one clause.

## C07

**H36 · A-C07-1 · illustrations[0], [1] output**
As it stands: "[1] "~/project""
Missing: `~` is shorthand for the user's home folder.
To close: one clause at first appearance.

**H37 · A-C07-2 · definition.text**
As it stands: "A path is the address of a file. An absolute path starts from the top of one computer's disk ..."
Missing: "relative path" and "working directory" are never defined. The original's definition ("A relative path starts from the working directory, the folder R treats as its current home when it looks for a file or saves one, such as `data-raw/heights.csv`.", 28 words) raises C07's mean from 14.12 to 14.56 (original 14.30).
To close: the same content in two shorter sentences.

**H38 · A-C07-3 · illustrations[1]**
As it stands: "In this book's project the marker is an empty file called `.here`. An RStudio project file works the same way."
Missing: how to create either (`here::set_here()` or `file.create(".here")`; File, New Project in RStudio). The reader cannot set up a project.
To close: one code line (code gate) or the RStudio menu steps.

**H39 · A-C07-4, A-C10-7 · illustrations[1]; C10 illustrations[1]**
As it stands: "These are commands for the computer's terminal ..." / "open a terminal in this folder and type `Rscript code/analysis.R`."
Missing: how to open a terminal (RStudio's Terminal tab; Windows and Mac equivalents) and how to make it start in the project folder.
To close: one or two sentences.

**H40 · A-C07-5 (residual) · simplified_explanation**
Missing: CSV is defined only in Ex 2 ("one CSV file, a plain-text table") and in C09. Illustration 1 uses `read_csv()` first.
To close: a gloss at Illustration 1's first CSV.

**H41 · A-C07-7 · P8**
As it stands: "penguins_test <- head(penguins_raw, 300) / write_csv(penguins_test, here("data-raw", "penguins_raw.csv"))"
Missing: `head()` and `write_csv()` are never introduced before this problem.
To close: a one-line gloss in P8.

**H42 · A-C07-8 · P10**
As it stands: "Show that the cleaned file is disposable: delete it, remake it from code, and check that the remade file is identical to the first."
Missing: deleting a file (`file.remove()`), filtering rows (C11), writing (`write_csv()`), comparing files (`tools::md5sum()`, C09). The reader cannot start.
To close: move P10 after C11, or give the functions.

## C08

**H43 · A-C08-3 (residual) · illustrations[0] output**
Missing: what `<chr>`, `<dbl>`, `<date>` (and later `<int>`, `<lgl>`, `<dttm>`) stand for. The restored sentence says only that the printout shows each column's type.
To close: one line mapping chr to character, dbl to double (numeric), date, and so on.

**H44 · A-C08-4 · illustrations[0] output**
As it stands: "! Tibble columns must have compatible sizes. • Size 3 ... ℹ Only values of size one are recycled."
Missing: "recycled" (C04's repeating rule) and what the `!`, `•`, `ℹ` marks mean (error, detail, hint).
To close: one sentence after the output.

**H45 · A-C08-5 · illustrations[1]; Ex 2**
As it stands: "The units sit in the column names, `(mm)` and `(g)`, as Broman and Woo suggest ..." / Ex 2: "Find every place where the sheet breaks the tidy rules or Broman and Woo's advice ..."
Missing: Broman and Woo's advice is never listed. Ex 2 cannot be done against it.
To close: a short list of their rules used in Ex 2 (units out of cells, no colour as data, one rectangle, no merged cells, ...), with the citation.

**H46 · A-C08-6, A-C10-10 · illustrations[1]; C10 illustrations[0]**
As it stands: "The help page says the file holds nesting observations of adult penguins ..."
Missing: which help page (palmerpenguins' `?penguins_raw`) and how to open it (install palmerpenguins, then `?palmerpenguins::penguins_raw`).
To close: name it and give the line.

**H47 · A-C08-7 · illustrations[1]; P5**
As it stands: "length(unique(penguins_raw$`Individual ID`))"
Missing: `unique()` is never glossed.
To close: one clause ("unique() keeps one copy of each value").

**H48 · A-C08-8 · illustrations[1]**
Missing: `glimpse()` comes from dplyr or tibble (the code loads tibble), and "…" means the line was cut short to fit.
To close: one sentence.

**H49 · A-C08-11 · P10**
As it stands: "The penguin file has data on 344 penguins." Decide what to compute ...
Missing: the tool for counting combinations of columns (`n_distinct()` on two columns) appears only in C10.
To close: move P10 to C10, or accept the IDs-only answer.

**H50 · A-C08-12 · illustrations output**
As it stands: "# A tibble: 3 × 4"
Wrong signal: C02 says "Everything after a `#` on a line is a comment"; here `#` begins a line of output.
To close: one line ("In printed output, R starts the tibble's summary lines with #; they are not code").

## C09

**H51 · A-C09-2 · definition.text**
As it stands: "by default the list is the empty string and the text `NA`."
Missing: that `""` is the empty string, an empty cell.
To close: a parenthesis.

**H52 · A-C09-3 · definition.text, illustrations[2]**
As it stands: "From haven, `read_sav()` reads SPSS `.sav` files and `read_xpt()` reads SAS transport `.xpt` files; both keep each column's label ... as a label attribute of that column."
Missing: SPSS and SAS (statistics programs), sheet and cell range (Excel), attribute (extra information stored with an R object).
To close: short glosses at first use.

**H53 · A-C09-4 to -9, A-C09-11 · illustrations[0], [1], [2]**
Missing, each used without a gloss: `writeLines()` and text across several lines (C09-4); `vroom(...)` in the warning (C09-5); `[c("row", ...)]` column selection and `<int>` (C09-6); `unname()` and "byte" (C09-7); `readxl_example()` and `system.file()` (C09-8); `...2` names, date serial numbers, `<lgl>`, `<dttm>`, finding sheet names (`excel_sheets()`) (C09-9); `attr()`, `sapply()`, `colSums()`, `bmx[c(...)]` (C09-11).
To close: a one-clause gloss beside each, or cut the less needed outputs (code gate for any output change).

**H54 · A-C09-10 · illustrations[2]; P6, P9**
As it stands: "This book's project holds the body measures file of the 2021–2023 cycle."
Missing: where the reader gets `BMX_L.xpt` and `DEMO_L.xpt` (the CDC NHANES download pages) and that they go in `data-raw/`.
To close: one sentence with the source.

**H55 · A-C09-12 · must_know[6], illustrations[2]**
As it stands: "Any average you compute from an NHANES file without its sample weights describes the people in the file only."
Missing: "sample weights" undefined, and it sits beside body weight.
To close: one sentence (each person counts for a number of people in the population; not body weight).

**H56 · A-C09-13 · illustrations[2]**
As it stands: "The four counts also match the code tables printed in the survey's own codebook. ... They are not survey estimates"
Missing: codebook, code tables, survey estimates.
To close: short glosses.

**H57 · A-C09-14 · Ex 2**
As it stands: "`village_code` is a code with leading zeros, such as 0042."
Missing: that reading it as a number drops the zeros (0042 becomes 42). The reader cannot say what the argument protects against.
To close: one sentence in the col_types paragraph.

**H58 · A-C09-17 · P10**
As it stands: "Then show what a single hand edit does to the checksum, using a copy in `output/`."
Missing: copying a file (`file.copy()`) and changing one character in code are never taught.
To close: give the two functions, or reword.

**H59 · A-C09-19 · P7**
As it stands: "col_types = cols(.default = col_double())"
Missing: `.default` sets the type of every column not named. P7 turns on it.
To close: one clause in Illustration 1 or in P7.

## C10

**H60 · A-C10-1, A-C11-5 · illustrations[0]; C11 throughout**
As it stands: "penguins_raw |> count(Sex)"
Missing: why dplyr functions take bare column names without `$` (they look the name up inside the data frame).
To close: one sentence at first use (C10), repeated briefly in C11's definition.

**H61 · A-C10-2 · illustrations[0]**
As it stands: "head -n 5 data-raw/penguins_raw.csv"
Missing: a terminal command that prints the first 5 lines of a file; not glossed.
To close: one clause.

**H62 · A-C10-3 · illustrations[0] output**
As it stands: ""Adult, 1 Egg Stage""
Missing: that quotes in a CSV keep a comma inside one value.
To close: one sentence.

**H63 · A-C10-4 · illustrations[0] output**
As it stands: "`Date Egg` = col_date(format = "")"
Missing: `format = ""` means the default year-month-day format.
To close: one clause.

**H64 · A-C10-5 · illustrations[1]**
As it stands: "collected by Palmer Station Antarctica LTER and K. Gorman, and first published by Gorman, Williams and Fraser in PLoS ONE in 2014." / "Wilson and colleagues describe it as the "No Rights Reserved" licence"
Missing: LTER expanded, and Wilson and colleagues not cited in the text.
To close: expand LTER; add the citation.

**H65 · A-C10-6 · illustrations[1] against C07**
As it stands: "Type it into a plain-text file called `README.txt`" (C07: "a short plain-text file called README").
Wrong: two names for the same file.
To close: pick one name across C07 and C10.

**H66 · A-C10-8 · must_know[4] against illustrations[0]**
As it stands: "Leave it blank and say why, until a source or a protocol gives the range." against "Leave it saying what you know, until a source or a decision fills it."
Wrong: contradiction (blank cell, or a cell saying "expected range not stated" as in the table).
To close: one rule in both places; the table's practice is the second.

**H67 · A-C10-9 · illustrations[0] against C07**
As it stands: "Save it as a CSV file, `penguins_raw_dictionary.csv`, beside the raw file in `data-raw/`. ... No code ever writes to that folder."
Wrong: C07 says data-raw holds the raw data as it arrived; the dictionary is added later, by hand.
To close: state that hand-written documentation of the raw data belongs in data-raw, or put the dictionary elsewhere.

**H68 · A-C10-11 · illustrations[0] output**
As it stands: "<int>" in the `count()` output.
Missing: `<int>` (integer) unexplained. Same fix as H43.

## C11

**H69 · A-C11-1 · P1 to P3**
As it stands: "library(dplyr) / clinic <- tibble( ..."
Wrong: C08 teaches `tibble()` as "from the tibble package"; these problems load only dplyr. It runs (dplyr re-exports `tibble()`) but the reader following C08 predicts an error.
To close: add `library(tibble)` (code gate), or say dplyr also provides `tibble()`.

**H70 · A-C11-2 · definition.text**
As it stands: "A condition is built from comparisons (`==` equal to, `!=` not equal to, `<`, `>`, `<=`, `>=`) joined by ..."
Missing: meanings of `<`, `>`, `<=`, `>=`.
To close: add "less than", "greater than", "at most", "at least".

**H71 · A-C11-3 · must_know[4]**
As it stands: "A verb that is not assigned changes nothing."
Missing: "verb" (the dplyr name for these functions) undefined.
To close: one clause in the definition.

**H72 · A-C11-4 · illustrations[1]**
As it stands: "print(n = 5)"
Missing: `print()` with `n` (show only the first n rows) unglossed.
To close: one clause.

**H73 · A-C11-6 · P9**
Missing: operator precedence among `&`, `|` and comparisons, and "complex types", are never taught. The reader cannot do P9 honestly.
To close: one sentence and an example, or change P9.

**H74 · A-C11-9 · illustrations output**
As it stands: "3 <NA>      11" (C10) and `<NA>` in C11 printouts, against `NA` elsewhere.
Missing: a tibble prints a missing text value as `<NA>`; it is the same `NA`.
To close: one clause.

## Not holes: tool and cut items for the conductor

These are not reader gaps. They are recorded here so the fixer does not try to close them in text.
The details are in RESTORE-DECISIONS-r1.md.

- **T1 · C02 simplified_explanation.** `restore.py`'s re-wrap breaks the code span `` `[1] 5` `` across a line, and the code-span-aware splitter then merges "R prints [1] 5." with the next sentence. Validation fails on survival, and no list can pass.
- **T2 · C05, C09 pass 1.** Adjusted by deletion only (sentences put back) so that each cut passes the mean check under the third splitter. The cold read was made on the earlier cuts.
