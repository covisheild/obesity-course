# S52-R1 glossary merge report

CONDUCTOR step 8. Checked against the final text as built by `python check/build.py --subject S52-R1`
(`check/_build/S52-R1.md`, 3 October 2026), not against the draft notes. Section n is record
`S52-R1-C0n` or `S52-R1-Cn`. No record was edited. Plain words are the final record's own, shortened.
No draft note (b1 to b8) or `RECONCILE.md` proposed glossary rows as such, so every row comes from the
final text's Definition and In plain terms. New rows were inserted in their alphabetical places. Four
existing rows gained a second (or third) sense (§3); no existing sense was changed. R function names
(`filter()`, `mutate()` and so on) were not given rows: they are code, not terms of art.

## 1. Rows added to `prose/GLOSSARY.md` (72)

absolute path (C07); aesthetic mapping (C18); assignment (C03); base R (C06); check (in code) (C19);
checksum (MD5 checksum) (C07 first use, C09 defined); class (of an R object) (C15); coercion (C04);
column specification (C09); comment (in code) (C02); complete-case analysis (C13); condition (in code)
(C11); console (C02); CRAN (C02, C06); CSV file (C09); data dictionary (C10); data frame (C08); date (in
R) (C15); default (of an argument) (C05); end-to-end analysis (C22); error message (C02); factor (C14);
fresh session (C06 first use, C21 defined); function call (C05); geom (C18); help page (C05); hidden
state (C21); install (a package) (C06); ISO 8601 (C15); join (C17); key (C17, C19); key check (C19);
label (of a column) (C09); layer (of a plot) (C18); level (of a factor) (C14); load (a package) (C06);
mapped, set (of a visual property) (C18); missing-value code (C09, C13); NA (C04); object (in R) (C03);
observation (in tidy data) (C08); package (C06); parsing (a date) (C15); path (C07); pipe (C05);
project folder (C07); project root (C07); quantile (C16); R (C02); range check (C19); raw file (raw
data) (C01 first use, C09 defined); README (C07 first use, C10 defined); relative path (C07);
replicated (result) (C20); replication package (C20); reproducible (result) (C20); row-count check
(C19); RStudio (C02); script (C02); seed (random-number seed) (C21); session (R session) (C06); sheet
(of a workbook) (C09); silent change (C01); snake case (C03); terminal (C07); tibble (C08); tidy data
(C08); tidyverse (C03 first use, C06 defined); type (of a value in R) (C04); verb (dplyr) (C11); working
directory (C07); workspace (C03).

From the brief's list, not added: **code gate** (not a reader term, as the brief says); **replicable**
(the text says "replicated" only, so the row is "replicated (result)").

## 2. Terms used but not given a row (no record edited)

- **element (of a vector).** C04's Definition says "Every element of a vector has the same type" and
  uses "element by element", with no gloss. S02-R1-C10 calls the same thing an **entry** (existing row
  "entry (of a vector or matrix)"). Conductor: either C04 glosses "element" (and says S02 calls it an
  entry), or a row is added at a between-rounds pass.
- **observational unit.** C08 quotes Wickham's third rule ("Each type of observational unit forms a
  table") without defining the phrase; its plain terms say "one table, one kind of unit". The existing
  row **unit of observation** (`B0-R0-C39`, "what one row of a table stands for") is a near-identical
  phrase with a different job (one row versus one table). The book uses Book 0's phrase "what one row
  stands for" consistently, so it agrees with that row; the risk is only the look-alike names.
- **session** in C03. `RECONCILE.md` says C03 glosses "session" at first use; the final C03 does not use
  the word. The first gloss is C06, which the row cites.
- **parsing** has a broader use in C09 (readr's printed "parsing issues", for any value that does not fit
  its type) before C15 defines parsing for dates. The row is qualified "(a date)".
- **LICENSE, CITATION** (C10): named in one sentence each, not taught as terms.

## 3. Rows given a further sense (existing sense kept word for word)

1. **argument.** (1) `B0-R0-C42`, premises and a statement they establish, unchanged. (2) added: of a
   function call, a value written inside its brackets, given by name or by position (`S52-R1-C05`).
2. **error.** (1) `B0-R0-C30`, measured value minus reference value, unchanged. (2) added: in R, R
   stopping because it could not carry out an instruction, reported in an error message (`S52-R1-C02`).
   The book says "stops with an error" throughout (C02 onwards, C19's check).
3. **variable.** (1) `B0-R0-C15`, a letter in place of a number, unchanged. (2) added: in R, another name
   for a named object (`S52-R1-C03`). (3) added: in a table of data, what one column holds
   (`S52-R1-C08`). C03 names all three meanings and C08's must-know asks the reader to tell them apart.
4. **vector.** (1) `S02-R1-C10`, unchanged. (2) added: in R, an ordered set of values of one type held as
   one object under one name; each column of a data frame is one (`S52-R1-C04`; the column point is C08's).

## 4. For the conductor: same term, wording at odds (neither row nor record changed)

1. **vector: row versus column.** S02's row says "one row of a data table is a vector"; S52 C08 says
   "Each column is a vector". Different senses (mathematical list of numbers versus R object of one
   type), now numbered apart, but a reader of both books meets opposite pictures. A one-line note in
   either book would settle it.
2. **quartile.** The row (`B0-R0-C28`) defines the quartiles by one recipe, the median of each half. C16
   says "Quartiles have more than one recipe. None is wrong", and shows R's default (type 7) giving 127
   and 134 against Book 0's 126 and 136 on nine heights. Same sense, so no second sense was added; the
   row reads as the definition where C16 treats it as one rule of several. Possible between-rounds
   widening: "by Book 0's rule, the first quartile is ...".
3. **cell.** The row's sense (1) (`B0-R0-C26`) says a cell holds "the count of people who are both". S52
   uses spreadsheet cells holding any value (C08 "one cell, one value", "104/66" in one cell; C09 "an
   empty cell"). Same mismatch S57's report §5 noted for group means; the row may want widening to "the
   value where a row meets a column".
4. **range.** Both senses of the row are single numbers or sets (outputs of a rule; largest minus
   smallest). C10 ("the range you expect") and C19's range check use range for an interval between two
   limits. Not taught bare, so only "range check" was added.
5. **function.** The row (`B0-R0-C18`): every input gives exactly one output. C21's `sample(344, 5)`
   gives different picks on each run unless the seed is set, so an R function is not always a function
   in the row's sense. The book never claims it is (C05 defines only the function call), so nothing to
   fix unless a reader asks.

## 5. Drift inside S52-R1 (no record edited)

1. **key.** C17: "whose values pick out the row they belong to". C19: "meant to pick out one row each".
   Compatible (C19 adds that it is meant to be unique, which its key check tests); one row cites both.
2. **reproducible.** C20 defines it (same data, same code, same result). C22 narrows it to "this book's
   sense": the outputs come back the same from the raw files with one command. Compatible; the row uses
   C20's words.
3. **README.** C07 says it holds what the project is, where the data came from and how to run it again;
   C10's Definition gives only the one command and the folder. C10's illustration and C22 carry all
   three, so the row gives the union.
4. **CRAN** is glossed in C02 and again in C06; same words in substance.

## 6. Existing rows used by S52-R1 in the same sense

**unit of observation** ("what one row stands for", C08, C10, C19); **two-way table** (C14: `count(species,
island)` "is Book 0's two-way table"); **interquartile range** and **standard deviation** (C16, divides
by one less than the count, as Book 0 does for a sample); **bin** (C18); **mean**, **median**,
**percentage** (C13, C16); **table**; **scale** (C18, axis scale); **data matrix** (S02: one row a case,
one column a measurement, consistent with tidy data).

## 7. Build

`python check/parallel.py registries`: 0 problems.
`python check/build.py --check`: records 166, blocking 0, warnings 278, the same as before the merge.
