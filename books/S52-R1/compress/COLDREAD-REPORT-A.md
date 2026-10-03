# Cold read (5b), reader A: S52-R1-C01 to C11 — gap report

Cold reader v2 (fresh subagent, 3 Oct 2026), reading /tmp/coldread2/a/: the cut sections (`-pass1.md`) with the
records' illustrations inserted and `{{n:}}` values filled (prepare.py's assemble omits `illustrations[]`; the
first cold read, v1, ran without them and its reports are void for code teaching). The reader could not write
the file; the conductor saved its returned text (gap part, verbatim in substance).

Totals: 126 gaps. C01 8, C02 12, C03 6, C04 15, C05 10, C06 11, C07 11, C08 13, C09 19, C10 11, C11 10.

Three worst: (1) C04's practice set relies on things never taught (P11 NA inside `[ ]`; P7/P9 text ordering
and text-vs-number comparison; P2 TRUE as 1; P5 several positions in `[ ]`), so an honest prediction is wrong.
(2) Problems that cannot be started: C07 P10 (deleting, filtering, writing, comparing files), C09 P10 (copying a
file and editing one character), C04 Ex1 (changing one element in code). (3) Sentences pointing at nothing,
apparently where text was cut: "Read it word by word" (C02), "That list is not your script" (C03), "Read that
report every time" (C09), "The help page says…" (C08); C08's definition promises three rules and gives two.

## C01 (8)
1. "704 ÷ 3597" and "× 100": symbols never introduced; Book 0 used words.
2. "a line of code", "reproducible code", "comment": used before C02 defines them.
3. "so did the weighting alone": weighting never explained.
4. "Of the 987 files with errors": switch from papers to files unexplained.
5. "Excel's behaviour in 2016": the paper's year never given.
6. "90% of its GDP, the highest category": GDP and the categories undefined.
7. "Book 0's section on percentages": the earlier book is never called Book 0.
8. "default settings" and spreadsheet "formula" assumed.

## C02 (12)
1. "from their own websites": no URLs or steps; cannot install.
2. "pane", "prompt": where the console is on screen never said.
3. "Read it word by word." "It" points at nothing.
4. "Book 0 taught you the sign ÷": false for the earlier book as given.
5. "<text>:1:4:" unexplained.
6. "unexpected symbol" in P8 unexplained until C03.
7. The `+` prompt asserted, never shown, yet Ex1 tests it.
8. "typing the letter x as times does too": never demonstrated.
9. "An adult's BMI is a number in the tens": B6 refused to give typical values.
10. Whether spaces matter in code never said.
11. How to select all lines, and Mac keys, not covered.
12. The echo of code lines when running a script not shown.

## C03 (6)
1. "That list is not your script. It holds every line you ran today": "that list" dangling; also does not match what `ls()` prints (objects, not lines).
2. Empty brackets in `ls()` unexplained until C05.
3. "snake case", "style guide", "tidyverse": undefined.
4. The Environment pane never located.
5. Book 0 never wrote `BMI = w / h^2`; whether `=` can assign never answered.
6. Quotation marks in `ls()` output unexplained.

## C04 (15)
1. "numeric" in the text versus `"double"` from `typeof()`: never tied together.
2. "argument", "binary operator": undefined.
3. Warning versus error: shown, never defined; `mean.default` unexplained.
4. `>` never named; `>=` never introduced.
5. P2: TRUE as a number untaught.
6. P5: several positions inside `[ ]` untaught.
7. P7: `max()` and text ordering untaught.
8. P9: comparing text with a number untaught.
9. P11: NA inside a logical index untaught; the likely prediction is wrong.
10. Ex1: assigning to one element untaught.
11. "approximation in binary": binary undefined.
12. "You build one", "The three you need": antecedents only in the Definition.
13. `.csv` undefined until C09.
14. Display of 152.0 and the leading space before `[1]` unexplained.
15. Possible return values of `typeof()` never listed.

## C05 (10)
1. `median()` and `sd()` not introduced as R functions (nothing links sd() to D5 or says n or n − 1).
2. "trim became 0.5": trim unexplained; explanation circular; read three times.
3. The help page is never shown, but Ex1 and P5 need it.
4. Typing `|>`, line continuation after it, and indentation not covered.
5. `mean()` errors on its own but works in a pipe (unexplained).
6. "a later rung": rung undefined.
7. The "n = 9" notation undefined.
8. P4: R printing 19 rather than 19.0 untaught.
9. P6: whether `sum()` takes `na.rm` not stated.
10. "you need a function of your own": the reader cannot write one (pointer only).

## C06 (11)
1. CRAN and repository undefined; internet access not mentioned.
2. Session, and how to start a fresh one, not explained.
3. The quotes rule for `install.packages("x")` versus `library(x)` never stated, yet P6 depends on it.
4. The base package never introduced.
5. What dplyr and readr do not said; reader never told to install dplyr.
6. Curly quotes in ‘1.1.4’ unexplained.
7. here, path and project are forward references, yet P4 needs them.
8. "nesting observation" undefined.
9. `code/analysis.R` notation before C07.
10. `>= "1.1.0"` comparing a version with text unexplained.
11. "Each has a version number" ambiguous.

## C07 (11)
1. `~` never explained.
2. "relative path" never defined; working directory undefined.
3. How to create `.here` or an RStudio project never shown; reader cannot set one up.
4. How to open a terminal not covered.
5. CSV defined only in an exercise; README contents not given.
6. P4: column count unknown at this point (dim() appears in C09).
7. P8: `head()` and `write_csv()` unintroduced.
8. P10: cannot start.
9. Why the backslash is special not said.
10. P6: no existence check taught.
11. "no capital letters used to tell two files apart" ambiguous.

## C08 (13)
1. "three rules hold" followed by only two.
2. tidyverse still undefined.
3. `<chr>`, `<dbl>`, `<date>` unexplained.
4. "recycled", and the `!` / `•` / `ℹ` bullets unexplained.
5. Broman and Woo appear with no summary, yet Ex2 depends on their advice.
6. "The help page says": which help page never said.
7. `unique()` used without introduction.
8. Where `glimpse()` comes from and the "…" truncation not explained.
9. P4–P6 unpredictable; `table()` output never shown.
10. P8: no splitting tool taught.
11. P10: the tool for combining columns comes only in C10.
12. "# A tibble" contradicts "# is a comment".
13. "(Wickham 2014)": name and year only.

## C09 (19)
1. "Read that report every time.": dangling.
2. "the empty string" and `""` never explained.
3. SPSS, SAS, sheet, cell range, attribute undefined.
4. `writeLines()` and multi-line text unexplained.
5. `vroom(...)` in the warning never mentioned.
6. `[c("row", ...)]` column selection untaught; `<int>` new.
7. `unname()` and "byte" unexplained.
8. `readxl_example()` and `system.file()` unexplained.
9. In the Excel output, `...2`, serial numbers in date columns, `<lgl>`, `<dttm>`, how to find sheet names, all unexplained.
10. NHANES `.xpt` files appear with no instruction on obtaining them.
11. `attr()`, `sapply()`, `colSums()`, `bmx[c(...)]` get almost no explanation.
12. "sample weights" undefined, right beside body weight.
13. codebook, code tables, survey estimates undefined.
14. Ex2: losing leading zeros never taught.
15. P3: the short `col_types` string format never shown.
16. P6 and P9 unpredictable.
17. P10: cannot start.
18. "kg/m**2": `**` as power unexplained.
19. `.default` unexplained.

## C10 (11)
1. `count(Sex)`: bare column names without `$` never explained.
2. `head -n 5` unexplained.
3. Quoted field "Adult, 1 Egg Stage" containing a comma unexplained.
4. `col_date(format = "")` unexplained.
5. LTER, PLoS ONE and "Wilson and colleagues" uncited in the text.
6. README versus README.txt.
7. "open a terminal in this folder" not taught.
8. "Leave it blank and say why" versus "leave it saying what you know".
9. C07 says data-raw is written to once, on arrival, but the dictionary is added later.
10. How to open the palmerpenguins help page not said.
11. `<int>` unexplained.

## C11 (10)
1. P1–P3 call `tibble()` with only dplyr loaded, against C08's rule.
2. `<`, `>`, `<=`, `>=` given no meanings.
3. "verb" undefined.
4. `print(n = 5)` new.
5. Bare column names still unexplained.
6. P9: operator precedence and "complex types" untaught.
7. Forward reference to "the section on missing values".
8. P4–P6, P12, P13 unpredictable (values need running).
9. `<NA>` versus `NA` in printouts unexplained.
10. snake case defined only here, though C03 used it.

## Symbols before explanation; signs with two meanings (summary)
÷ and × (C01); `<text>:1:4:`; the `+` prompt; `()` in `ls()`; `>`/`>=`/`<`/`<=`; dbl/chr/lgl/int/date/dttm; `[4]`
position markers; `|>`, `...`, `::`; `~`, `\`, `.here`, `cd`, `Rscript`, `head -n`; `#` in tibble output; `!`, `•`, `ℹ`;
`I()`, `""`; `**`; `...2`; `<NA>`. Two meanings: variable; weight (body / weighting / sample weights); range;
`=`; `#`; `$`; `^`; `*`; `/`; `+`; `>`; `-`; `!`; `|`; `:`; `.`; `...`; `[ ]`; `( )`; x; n; NA; numeric/double/dbl;
head; README/README.txt; "the help page" (function vs dataset); observation (row vs "nesting observation").
