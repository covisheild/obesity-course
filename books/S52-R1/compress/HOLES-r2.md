# S52-R1 step 5c: holes for the fixer, batch r2 (C12 to C22)

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
