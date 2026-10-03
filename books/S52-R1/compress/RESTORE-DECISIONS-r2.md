# S52-R1 step 5c: restore decisions, batch r2 (C12 to C22)

Restorer: not the cutter and not the cold reader. Inputs: `COLDREAD-REPORT-B.md` (69 gaps), and
`<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml` for C12 to C22, with the cold reader's
copy in `/tmp/coldread2/b/` to see the illustrations as read. Restore lists are in
`restore-lists/S52-R1-Cnn.txt`, each line commented with the gap it closes. Outputs are
`S52-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and checked by
`check/compress/validate.py`. The tools were not changed. An earlier interrupted r2 attempt left
files in `restore-lists/` (`c13a.txt`, `diff.py`, `empty-S52-R1-C*.txt`); they were ignored, not
deleted (no `rm` in the repo), and every `S52-R1-C12.txt` to `C22.txt` and every final file here
was rewritten in this run.

Key: **restored** means the original's own sentences were put back because they let the reader do
the thing. **hole** means it could not be closed here: it is listed in `HOLES-r2.md` for the fixer.
**not a defect** means nothing to do.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → final | Validate |
|---|---|---|---|---|---|---|
| C12 | 819 | 401 | 459 | +58 | 14.37 → 13.50 | **FAIL** (tool conflict) |
| C13 | 693 | 353 | 359 | +6 | 13.86 → 13.81 | **FAIL** (tool conflict) |
| C14 | 684 | 318 | 356 | +38 | 13.41 → 13.19 | **FAIL** (tool conflict) |
| C15 | 709 | 357 | 375 | +18 | 14.47 → 13.89 | OK |
| C16 | 863 | 398 | 430 | +32 | 13.28 → 12.65 | OK |
| C17 | 785 | 496 | 496 | 0 | 14.02 → 13.78 | OK |
| C18 | 789 | 544 | 544 | 0 | 13.37 → 13.27 | OK |
| C19 | 906 | 606 | 606 | 0 | 13.28 → 13.11 | OK |
| C20 | 932 | 527 | 538 | +11 | 14.56 → 14.16 | OK |
| C21 | 886 | 498 | 498 | 0 | 14.21 → 13.78 | OK |
| C22 | 673 | 360 | 360 | 0 | 12.31 → 11.00 | OK |
| **Total** | 8739 | 4858 | 5021 | +163 | | 8 OK, 3 FAIL |

Decisions: 8 restored, 56 holes, 5 not a defect (69). One extra hole (C12 "Also", `tibble()`)
is recorded but not counted among the 69.

`python check/build.py --check` / `--subject S52-R1` was not run: it needs the final text written
back into the records, which is outside this step's brief.

## Tool conflict (C12, C13, C14): needs the conductor's decision

The same conflict as S01-R1 C02/C07. In five places pass 1 kept only part of what
`build._sentences` counts as one sentence. The splitter does not split before a word that starts
in lower case once markup is stripped, so `` `rename_with()` ``, `` **str_trim()** ``,
`` `mutate()` ``, `` `sum(...)` `` and `` `levels(f)` `` after a full stop do not start a new
unit:

- C12 `definition.text`: "Both come from the stringr package. `rename_with()` renames columns ..." (cut kept the first half).
- C12 `simplified_explanation`: "Text columns get cleaned the same way. **str_trim()** takes spaces off the ends. **str_to_lower()** ..." (cut kept the second and third parts).
- C12 `must_know[7].point`: "A new column is only as right as the rule you wrote. `mutate()` will compute any rule ..." (cut kept the first half).
- C13 `simplified_explanation`: "The second job is to count. `sum(is.na(x))` counts the missing values in one column." (cut kept the second half).
- C14 `definition.text`: "With no levels given, they are taken from the data in alphabetical order. `levels(f)` lists them." (cut kept the first half).

`restore.py` keeps an original unit only if the whole unit was kept or is named, so an empty list
drops the kept fragment (C12 `must_know[7].point` then comes out empty). Naming the unit brings back
all of it, and `validate.py` then reports the fragment as "kept by the cut, missing after restore",
though its text is present (checked by substring for all five). No list can pass. Each final file
carries the whole unit, which adds words no gap asked for: about 9 (C12 definition, the
`rename_with()` sentence, which happens to bear on gap C12-7), 6 (C12 "Text columns get cleaned the
same way."), 9 (C12 `mutate()` will compute ...) and 6 (C13 "The second job is to count."). In C14 the
added half, "`levels(f)` lists them.", is what gap C14-3 asked for. The fix belongs to the cut or to
the tools: re-cut on the splitter's boundaries, or make `restore.py` and `validate.py` agree on the
boundary. Tools were not touched.

## Restores tried and withdrawn because the mean sentence length rose

The original filled these gaps, but restoring them raised the mean sentence length above the
original's, which `validate.py` fails and `claude.md` §12 calls a failure whatever the word count.
They go to the fixer as holes, with the original's sentences named in `HOLES-r2.md`.

- C13-1: "A missing value reaches R in one of two ways." with "Either it is already NA, ..." → 13.86 → 13.89.
- C17-3: "The relationship argument states how many matches ..." → 14.02 → 14.08.
- C18-1: "It cannot guarantee that the data are right, ..." → 13.37 → 13.40.
- C20-1: "Peng (2011) calls replication ..." with "Between no replication and full replication he describes a spectrum ..." → 14.56 → 14.74. The second sentence alone passes (14.55), but its "he" would point at nothing, so it was not restored alone.

## Gap by gap

### C12
- **1** restored: "Where the condition is `NA`, the result is `NA`, unless a value is given for `missing`." P2 asks what the NA row gets from `if_else()`, and the cut left no rule for it. That `if_else()` is never shown in code is not separately a defect: its full call form is in the definition.
- **2** not a defect: `str_trim()` is defined, and the kept "Together they turn "Male ", "male" and "MALE" into "male"" shows its effect. P6 can be done from that.
- **3** restored: "A 5 at the cut is rounded to the even digit, so `round(2.5)` is 2." P3 is answerable only with it.
- **4** hole: the original never says that `digits` in `print()` counts significant digits.
- **5** hole: the cut "Rounding acts on the number as the computer stores it ..." does not explain why rounding cures the comparison either. Nothing in the original does.
- **6** hole: the original never shows `.default =` written out before P9.
- **7** hole: passing a function by name, without brackets, is never explained in the original. The tool-conflict restore puts back "`rename_with()` renames columns by applying a function to their names", which says what it does but not the bracket rule.
- **Also** (`tibble()` after only `library(dplyr)`) hole, not counted.

### C13
- **1** hole: the original's two sentences close it but raise the mean (see above).
- **2** hole (contradiction, illustration 2): `"999"` against C09's -99.
- **3** hole (error, illustration 1): "describes 34 nests".
- **4** hole (practice problem 7): 64.5 cannot come from the code shown.
- **5** not a defect: `max()` (C04) and `min()` (C09) are taught, so the reader can look at each column's largest and smallest values.

### C14
- **1** not a defect: the sentence states the fact the reader needs (text is read as text); no history is assumed.
- **2** hole: the original never says how `fct_recode()` gives text levels.
- **3** restored: "With no levels given, they are taken from the data in alphabetical order. `levels(f)` lists them." (one splitter unit; see tool conflict).
- **4** hole: `fct_relevel()` is described, never written in code. The original is the same.
- **5** hole: a printed factor is never shown.
- **6** not a defect: C05 teaches how to open a help page, and P4 needs nothing more.
- **7** restored: "A clean count shows how many rows hold each category." This gives the referent of "It cannot show ...".
- **8** restored: "`count()`, from dplyr, gives the number of rows for each value of one column, or for each combination of values of two or more columns." This states that it is one count over a combination. The wording "Two counts at once" stays as the original has it.

### C15
- **1** hole: "class" is never defined in the original.
- **2** hole (illustration 1): the `I()` sentence is garbled.
- **3** hole (illustration 1): `camp$visit_date <-` is never taught.
- **4** restored: "To R, a date is a number of days, counted from 1 January 1970, that prints as year-month-day." This gives the referent of "Because it is a number underneath".
- **5** hole (practice problem 5): date comparison is never shown.
- **6** hole: what `Date Egg` records drifts between illustration and problems.
- **7** hole (practice problem 8): the framing does not match the code output.

### C16
- **1** hole: "quantile", and the 0% and 100% columns, are never explained in the original.
- **2** hole: type 7 is named and never shown.
- **3** hole: `readLines()` is never explained in the original.
- **4** hole (error, illustration): "where" should be "whereas".
- **5** restored: "When a trainee shows you a table of means, ask first for the count in each row and for how many values were missing." (must_know[6]) and "A summary describes the rows in your file." (must_know[7]). Both are the antecedents the kept bullets point at.
- **6** hole: `write_csv()` is never defined in the original prose. "When the table is done, write it to a file in output/ with code." does not name it.

### C17
- **1** hole: `pivot_wider()`'s arguments are never explained in the original.
- **2** hole (wording): the original reads the same.
- **3** hole: the original sentence would close it but raises the mean (see above).
- **4** hole (practice problem 5).
- **5** hole (practice problem 6).

### C18
- **1** hole (contradiction). Pass 1 kept "The grammar guarantees that the figure draws your data faithfully" and cut the limit after it. The original's following sentence would restore the contrast but raises the mean. Even with it, "guarantees ... faithfully" contradicts the section's bins, removed rows and colour trap.
- **2** hole (wording): two senses of "left". The definition and illustration agree once they are worked out.
- **3** hole: the original never says where the 1.5 × IQR is measured from.
- **4** hole (illustration code): `count(name = expression)`.
- **5** hole (illustration code): `quantile()` with its probability passed by position.
- **6** hole: the ggplot2 version is not stated.
- **7** hole (illustration): the 6300 g maximum is never shown.

### C19
- **1** hole: `all()` is never explained in the original.
- **2** hole: the error output for an unnamed check is never shown. The definition says the expression is named, not the wording.
- **3** hole (practice problem 7): `abs()` first appears in C22.
- **4** hole (illustration): "barely move it" against 26.2 → 23.7.

### C20
- **1** hole: the original's two Peng sentences close it but raise the mean (see above).
- **2** hole (illustration): how the "best of both" row is built is never explained.
- **3** restored: "Journals with the strictest data-sharing policies had the highest re-execution rates." This is the body finding that must_know[6] summarises.
- **4** hole (illustration): "The parts of the paper this book holds" is repository-speak.
- **5** not a defect: "correlation coefficients" names an output in a story about a script that failed to save a plot. No task asks the reader to compute or read one, and must_know[6] uses "correlation" in its plain sense.

### C21
- **1** hole: "attached" and "loaded" are used loosely in the original too.
- **2** hole (practice problem 2): `exists()`.
- **3** hole: "rung" is undefined in the original too ("It comes two rungs up").
- **4** hole (illustration): `ls` and `cat` in the shell are never explained.

### C22
- **1** to **6** hole (illustration code): `factor(labels =)`, `abs()`, `"\n"`, `NULL`, `ggsave()` units and `dpi`, and the shell commands. These need glosses or code changes.
- **7** hole (wording, illustration 2).
- **8** hole (error, illustration 2): the 41 came from `count()`, not the codebook.
- **9** hole (contradiction): "as Book 0 taught them" against C16.
- **10** hole: `|>` into `ggplot()` then `+`, against C18 P9.
- **11** hole: "gate" and "rung" are undefined in the original too.
