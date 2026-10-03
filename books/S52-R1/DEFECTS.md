# S52-R1 defects

## Found by the compression pass (Task 5, 3 Oct 2026)

Holes the cold read found that the full-length original did not fill either, or errors and contradictions it exposed. Collected from the two restorers' files; each goes through the audit and fix loop. The first cold read (v1) ran without the records' illustrations (prepare.py's assemble omits `illustrations[]`) and was discarded; v2 had them.

### C01-C11 (restorer r1)


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

### C12-C22 (restorer r2)


These are gaps from `COLDREAD-REPORT-B.md` that restoring cannot close. Some the original never
filled. Some are errors or contradictions. Some sit in code, illustrations or problems, which the
cut did not touch. Four (C13-1, C17-3, C18-1, C20-1) the original fills, but restoring them raised
the mean sentence length. Gap ids follow the report (`B-Cnn-k`). "Field" is the record field.
"Illus. n" is illustration n's body. "Pn" is practice problem n. Every fix that adds or changes a
code block goes through the code gate.

## C12 (making new columns)

- **B-C12-4** · Illus. 2 · "Ask R whether that BMI equals 25, and then print it with more digits." over `print(clinic$bmi[2], digits = 17)` · Here `digits` counts significant digits, while the definition says `round()`'s `digits` counts decimal places, and nothing tells the two apart. · Close with a one-line gloss after the output: in `print()`, `digits` is the number of significant digits shown, not decimal places.
- **B-C12-5** · Illus. 2 · "The help page for `round()` warns of this: rounding applies to the number as stored, not as printed." followed by "round the BMI to one decimal in a separate column" · It never says why rounding makes the comparison safe. The reader read it twice. · Close with a gloss: `round(x, 1)` returns the stored number nearest to a one-decimal value, so 24.999999999999996 becomes the same stored 25 that `25` is, and `bmi_1dp < 25` is then `FALSE`.
- **B-C12-6** · `definition.text` · "A row that matches no case gets `.default` if one is given, and `NA` otherwise." · How `.default` is written first appears in P9. · Close with a one-line gloss or an illustration line: `.default = "label"` goes as the last argument of `case_when()`, after the cases.
- **B-C12-7** · Illus. 3 · "`rename_with()` applies a function to every name. Give it `str_to_lower`:" · Passing a function by name without `()` is a new idea and is not explained. · Close with a gloss: written without brackets, a function is handed over to be used, not called.
- **B-C12-also** (not counted) · Illus. 1 and P1, P2, P6, P7 · `tibble(...)` after only `library(dplyr)` · C08 said `tibble()` comes from the tibble package. · Close with a one-line gloss: dplyr makes `tibble()` available too.

## C13 (missing values)

- **B-C13-1** · `simplified_explanation` · "Or it arrives disguised as a real value: a weight of 999, a height of -99, the words "not recorded"." · It starts with "Or" with no first alternative, and "it" has no referent. · The original closes it with "A missing value reaches R in one of two ways." and "Either it is already NA, because the cell was empty or the reading step was told which codes mean missing.", but restoring them raises the mean sentence length 13.86 → 13.89. The fixer may shorten them, or shorten another sentence, so that the pair fits.
- **B-C13-2** · Illus. 2 · "An earlier section declared codes with `na = c("", "NA", "999")` in `read_csv()`." · C09 declared -99, not 999. This is a contradiction. · Close by matching C09's actual `na =` vector, or by saying "with `na =` in `read_csv()`" without quoting the vector.
- **B-C13-3** · Illus. 1 · "Any summary of `complete` describes 34 nests" · A row is one adult's observation, two per nest. This is an error. · Close with "describes 34 rows" (or "34 birds").
- **B-C13-4** · P7 · "They report: "Mean weight was 64.5 kg, after removing missing values."" · 64.5 is the correct mean and cannot come from the code shown, so there is nothing to find. · Change the reported number to what the code gives, or change the code so it produces a wrong figure.

## C14 (categories)

- **B-C14-2** · `definition.text` / Illus. 2 · "The first, `fct_recode()`, renames levels" applied to `sex_clean`, a text column · It is not explained how text has levels. · Close with a gloss: the forcats functions turn a text column into a factor first, with its levels in alphabetical order.
- **B-C14-4** · `definition.text` · "The second, `fct_relevel()`, moves the named levels to the front." · It is never written in code, and P5 needs it. · Close with an illustration line such as `fct_relevel(island, "Torgersen")` with its output (code gate), or change P5.
- **B-C14-5** · Illus. / P1 · "Before you run it, say what this prints, and in what order the levels come." · How a factor prints (the values, then a `Levels:` line) is never shown. · Close with one printed factor in an illustration (code gate), or change P1 to ask only for the order of the levels.

## C15 (dates)

- **B-C15-1** · `definition.text` · "In R, a date is an object of class `Date`." · "Class" is never defined. The book taught "type". P1 asks for the class. · Close with a one-line gloss: the class says what kind of object it is and how R prints it, and `class(x)` shows it.
- **B-C15-2** · Illus. 1 · "Here is its text, held in R as `I()` marks it, the way an earlier section read a small file." · The sentence is garbled. · Rewrite it, for example: "Here is its text, read with `I()` to mark it as text rather than a file name, as an earlier section did."
- **B-C15-3** · Illus. 1 · `camp$visit_date <- dmy(camp$visit)` · Adding a column with `$<-` is never taught. Every earlier section used `mutate()`. · Close with a one-line gloss on `$<-`, or change the code to `mutate()` (code gate).
- **B-C15-5** · P5 · (date comparison needed) · Comparing dates (`<`, `>=` against `ymd("...")`) is never shown. · Close with an illustration line, a one-line gloss, or a changed problem.
- **B-C15-6** · Illus. 3 and P8-P10 · "The first nest was recorded on 9 November 2007" / "nests observed" / "laid their first egg" · What `Date Egg` records drifts, and the column is never defined. · Define it once, from the dataset's documentation, and use one wording.
- **B-C15-7** · P8 · "the first patient was screened on 2 March 2023." · The report's date is the true date and does not match what the code outputs, so the framing contradicts the code. · Make the report state what the colleague's code printed.

## C16 (summaries)

- **B-C16-1** · `definition.text` / Illus. · "The function `quantile()` gives quartiles and other quantiles"; output headed `0% 25% 50% 75% 100%` · "Quantile" is undefined, and the 0% and 100% columns (minimum and maximum) are unexplained. · Close with a gloss: a quantile is the value below which a given share of the data lies, and 0% and 100% are the smallest and largest values.
- **B-C16-2** · `definition.text` · "Both use the seventh of nine rules for placing a quantile between two values, unless told otherwise." · Type 7 is never shown, so P3 cannot be checked by hand. · Close with type 7's rule and one worked case, or change P3 so it does not need a hand prediction.
- **B-C16-3** · Illus. · `readLines(here::here("output", "mass_by_species.csv"))` · `readLines()` is unexplained. · Close with a gloss: it prints a text file's lines as they are, to show what was written.
- **B-C16-4** · Illus. · "... first appears in the file, where `group_by()` sorted them" · This is an error: "where" should be "whereas". The reader read it twice. · Close with "whereas".
- **B-C16-6** · `simplified_explanation` / Illus. · "When the table is done, write it to a file in output/ with code." (cut) and the illustration's `write_csv(` · `write_csv()` is never defined, though C21 refers back to it as explained. · Close with a definition line: `write_csv(data, path)`, from readr, writes a data frame to a CSV file.

## C17 (reshaping and joining)

- **B-C17-1** · Illus. · `pivot_wider(names_from = visit, ...)` · The arguments, and how it picks the identifying columns, are not explained. · Close with a gloss on `names_from` and `values_from`: the other columns identify the rows.
- **B-C17-2** · `simplified_explanation` · "There, summarise(.by = visit) cannot reach them." · "There" is unclear. The original reads the same. · Close with "In the column names, `summarise(.by = visit)` cannot reach them."
- **B-C17-3** · Illus. · `relationship = "one-to-one"` ... "so no `SEQN` appears twice in either file." · `relationship` and its values are never defined. · The original's definition sentence, "The `relationship` argument states how many matches each row is expected to have, and the join stops with an error if the data break it.", closes it, but restoring it raises the mean 14.02 → 14.08. The fixer may shorten it, or shorten another sentence. "one-to-one" also needs a gloss: each key appears at most once on each side.
- **B-C17-4** · P5 · (fill with 0) · No tool taught here fills with 0. · Close with a gloss on `values_fill = 0`, or change the problem.
- **B-C17-5** · P6 · "Say why the second count is what it is." · The answer needs knowledge about infants that the text does not give. · Close by adding the needed fact to the problem, or change it.

## C18 (plotting)

- **B-C18-1** · `must_know[7].point` · "The grammar guarantees that the figure draws your data faithfully." · This contradicts the section's chosen bins, silently removed rows and colour trap. The cut also removed the original's following limit, "It cannot guarantee that the data are right, ...", and restoring that raised the mean 13.37 → 13.40. · Rewrite the point so it states the limit, for example "The grammar draws exactly what the code says; it cannot guarantee that the data are right ..."
- **B-C18-2** · `definition.text` and Illus. · "A value on the edge between two bins is then counted in the bin to its left." / "`closed = "left"` makes each bin run from its left edge ..." · "Left" has two senses (the bin on the left, against the bin's left edge), and the edge value goes to the right-hand bin under `closed = "left"`. The reader read it three times. · Close with a gloss naming both cases with 3000 g: by default it is in "2500 to 3000", and with `closed = "left"` it is in "3000 to under 3500".
- **B-C18-3** · `definition.text` · "Its whiskers reach the furthest values within 1.5 times the interquartile range of the box." · It never says where this is measured from. · Close with "... within 1.5 times the IQR beyond each end of the box (below Q1, above Q3)".
- **B-C18-4** · Illus. · `count(bin_start_g = floor(body_mass_g / 500) * 500)` · Counting a named, computed expression is never taught. · Close with a gloss: `count()` can make the column it counts, named on the left.
- **B-C18-5** · Illus. · `quantile(body_mass_g, 0.25, na.rm = TRUE)` · The probability is passed by position, against C05's rule. · Write `probs = 0.25` (code gate), or gloss the exception.
- **B-C18-6** · Illus. / P8 · (outputs, P8 compares versions) · The ggplot2 version behind the outputs is not stated. · State the version the outputs were made with.
- **B-C18-7** · Illus. · "Body masses run from 2700 g to 6300 g" · The 6300 g maximum is never shown. · Show `range()` or `min()`/`max()` output (code gate), or point to where it was shown.

## C19 (checks)

- **B-C19-1** · Illus. and `definition.text` · `all(clinic$height_cm >= 50 & ...)` against "If any of them is not TRUE in every element ..." · `all()` is never explained and looks redundant. P1 drops it. · Close with a gloss: `all()` turns many TRUE/FALSE values into one, and it is needed for `na.rm = TRUE`.
- **B-C19-2** · `definition.text` / P1, P4 · "it stops with an error naming the first expression that failed" · The error wording for an unnamed check is never shown. · Show one unnamed failure's output (code gate).
- **B-C19-3** · P7 · (needs `abs()`) · `abs()` first appears in C22. · Close with a one-line gloss in P7, or change the problem.
- **B-C19-4** · Illus. · "two absurd values at the top barely move it" ... "The median moved from 26.2 to 23.7 kg/m^2." · These contradict each other. The reader read it twice. · Reword one of them: the median moved 2.5 units, not "barely".

## C20 (reproducibility)

- **B-C20-1** · Illus. · "Now place your own thesis on Peng's spectrum." · Peng and the spectrum are never introduced. · The original's two definition sentences ("Peng (2011) calls replication the ultimate standard ..." and "Between no replication and full replication he describes a spectrum ...") close it, but together they raise the mean 14.56 → 14.74. The fixer may shorten them to fit.
- **B-C20-2** · Illus. · "| best of both | 1581 | 1238 | 5790 |" and "1581 + 1238 + 5790 = 8609" · The total is larger than either single run's, and how the row was built is not explained. · Close with a gloss from the paper on how "best of both" combines the two runs, and why the base is larger.
- **B-C20-4** · Illus. · "The parts of the paper this book holds do not show how the abstract's figures were worked" · The sentence is unclear and uses repository-speak. · Close with "The parts of the paper read for this section ...", or name the parts.

## C21 (fresh session)

- **B-C21-1** · `definition.text` / `simplified_explanation` · "It has attached no package ..." / "Every package you loaded stays loaded." · "Attached" and "loaded" are used as synonyms, while the `sessionInfo()` output distinguishes them. · Close with a one-line gloss on the difference, or use one word in the prose and gloss the output's headings.
- **B-C21-2** · P2 · `exists("height_cm")` · `exists()` is never taught. · Close with a one-line gloss in P2.
- **B-C21-3** · Illus. · "Pinning versions ... is what renv does, two rungs up" · "Rung" is never defined (series vocabulary). · Close with a one-line gloss at first use (one level of this subject's sequence of books), or with a pointer.
- **B-C21-4** · Illus. · `ls output` / `cat output/rows_to_check.csv` · The shell commands are unexplained. · Close with a gloss: `ls` lists a folder and `cat` prints a file.

## C22 (end-to-end)

- **B-C22-1** · Illus. · `factor(..., labels = ...)` · `labels =` is never taught (C14 taught `levels =` and `fct_recode()`). · Close with a one-line gloss.
- **B-C22-2** · Illus. · `abs(...)` · It is unexplained. · Close with a gloss: absolute value.
- **B-C22-3** · Illus. · `cat(..., "\n")` · `"\n"` is unexplained. · Close with a gloss: a new line.
- **B-C22-4** · Illus. · `labs(x = NULL)` · `NULL` is unexplained. · Close with a gloss: no title on that axis.
- **B-C22-5** · Illus. · `ggsave(..., width = 5, height = 4, dpi = 150)` · No `units`, against C18's rule, and `dpi` is unexplained. · Add `units = "in"` (code gate), and gloss `dpi`.
- **B-C22-6** · Illus. · `cp`, `rm -r`, `> /dev/null 2>&1`, `cmp`, `&&`, `echo` · The shell commands are unexplained. · Close with a one-line gloss per command, or a short glossary line.
- **B-C22-7** · Illus. 2 · "The first step that went wrong while this section was being written goes first." · The join comes first, not the step that went wrong (the pregnancy filter). · Reword or drop the sentence.
- **B-C22-8** · Illus. 2 · "The expected count caught the pregnancy filter because the codebook gave the number of pregnant participants" · This is an error: the 41 came from `count()` in the script. · Correct it to name the `count()`.
- **B-C22-9** · Illus. · "The three quartiles answer the question, as Book 0 taught them" · These are R's type-7 quartiles, which C16 showed can differ from Book 0's. This is a contradiction. · Close with "as R's default (type 7) gives them", or drop "as Book 0 taught them".
- **B-C22-10** · Illus. · `... |> ggplot() + geom_...` · It mixes `|>` and `+` right after C18 P9 called that an error. · Close with a gloss: the pipe hands the data to `ggplot()`, and the layers after it still join with `+`.
- **B-C22-11** · `must_know[5].point` / Illus. · "The gate is one command from raw data to the same outputs." / "the gate to the next rung" · "Gate" and "rung" are undefined (series vocabulary). · Close with a one-line gloss at first use in the book, or with a pointer.
