# S52-R1 step 5c, batch r1 (C01 to C11): restore decisions

Restorer: not the cutter and not the cold reader. Inputs: `COLDREAD-REPORT-A.md` (126 gaps), the
cold reader's own texts in `/tmp/coldread2/a/` (to see each gap in place), and `<S>-original.md`,
`<S>-prose.yml` and `<S>-pass1-prose.yml` for each section. The restore lists are in
`restore-lists/S52-R1-Cnn.txt`, and each restored line is commented with the gap it closes. The
outputs are `S52-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and checked by
`check/compress/validate.py`. The tools were not changed. No record was edited and nothing was
committed. A partial r1 from an interrupted attempt (lists and finals for C01 to C03) was ignored
and overwritten.

Key: **restored** means original sentences were put back because they let the reader do the thing.
**hole** means it was not closable here and is written up in `HOLES-r1.md` (H number given).
**not a defect** means nothing to do. "Restored, residual" means the restored sentences close what
the reader could not do, and a remaining part goes to `HOLES-r1.md`.

The cut touched only prose fields. Gaps that sit in an illustration, a practice problem or an
exercise could be closed only if a cut prose sentence answered them; otherwise they are holes.

## Word counts (reader-facing prose, as `validate.py` measures it)

Measured under the conductor's code-span-aware splitter (3 Oct 2026, third revision). Under it the
originals' means changed for C03, C05, C06, C09 and C11.

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → cut → final | Validate |
|---|---|---|---|---|---|---|
| C01 | 983 | 538 | 560 | +22 | 14.00 → 13.72 → 13.93 | OK |
| C02 | 815 | 445 | 485 | +40 | 12.12 → 11.68 → 12.10 | **FAIL** (tool conflict, below) |
| C03 | 746 | 378 | 409 | +31 | 12.15 → 12.10 → 11.94 | OK |
| C04 | 932 | 474 | 529 | +55 | 13.17 → 12.50 → 12.59 | OK |
| C05 | 844 | 444 (adjusted) | 485 | +41 | 13.67 → 13.43 → 13.45 | OK |
| C06 | 775 | 321 | 380 | +59 | 12.53 → 11.46 → 11.90 | OK |
| C07 | 830 | 382 | 411 | +29 | 14.30 → 14.09 → 14.12 | OK |
| C08 | 833 | 339 | 384 | +45 | 12.58 → 10.18 → 10.89 | OK |
| C09 | 842 | 482 (adjusted) | 493 | +11 | 14.48 → 14.12 → 13.64 | OK |
| C10 | 816 | 405 | 405 | 0 | 12.64 → 12.06 → 12.06 | OK |
| C11 | 753 | 391 | 391 | 0 | 12.15 → 11.50 → 11.50 | OK |
| **Total** | 9069 | 4599 | 4932 | +333 | | 10 OK, 1 FAIL |

Counts: **21 restored, 78 holes, 27 not a defect** (126). 6 of the restored carry a residual hole.

`python check/build.py --check` / `--subject S52-R1` was not run: it needs the final text written
back into the records, which is outside this step's brief.

## Pass-1 cuts adjusted (C05, C09), on the conductor's instruction

Under the code-span-aware splitter both pass-1 cuts failed the mean check on their own: C05 13.67 →
14.36 and C09 14.48 → 14.80. I adjusted them by deletion only, counted against the original. Each
added sentence is the original's own, put back in its place by `restore.py` from a list. The
result replaced `-pass1-prose.yml`. Both validate, and both were re-assembled with
`prepare.py assemble`. The old pass-1 files are kept in `/tmp/claude-0/scratch-restore-r1/pass1-backup/`.
The cold read was made on the old cuts. The restore lists were then rebuilt against the adjusted
cuts.

- **C05** (+5 sentences; words 400 → 444; mean 14.36 → 13.43):
  - "Whatever goes inside the brackets is an argument." and "Many functions take more than one." lead into the kept "`round()` takes ...".
  - "Leave out an argument altogether and R uses its default." is the antecedent of the kept "The default for `digits` is 0".
  - "`round(x, digits = 1)` says what the 1 is." completes the kept "Name every argument after the first."
  - "Fix that argument and nothing else, then run the line again."
- **C09** (words 446 → 482; mean 14.80 → 14.12):
  - "Other formats need other functions.", "The commonest raw file is a CSV." and "The first line holds the column names." are short original sentences that bring the mean down.
  - "Never open the raw file and retype the cell."
  - The whole unit "The error is to think that a file which reads without an error has been read correctly. -99 read as a height raises no warning." The cut had kept only its first sentence. The splitter still reads the two as one unit, because "-99" is plain text, not a code span, so no restore list could pass while the cut held half of it. It now sits in pass 1 whole.

## Tool conflict (C02): needs the conductor's decision

Under the third splitter the earlier conflicts in C03, C05 and C11 are gone, and C09's was settled
in the cut (above). One new conflict appeared, in C02, with an unchanged list:

- **C02 `simplified_explanation`.** The paragraph lost sentences, so `restore.py` re-wraps it (`_wrap`, line breaks only), and the wrap falls inside a code span. Pass 1 has "R prints `[1] 5`." on one line; the final has "R prints `[1]` + newline + `5`." The code-span-aware splitter then does not end the sentence after it. It returns "R prints [1] 5. The [1] only marks the first value on the line; ignore it for now." as one sentence, so `validate.py` reports both of the cut's sentences ("R prints [1] 5." and "The [1] only marks ...") as "kept by the cut, missing after restore". Any rebuild re-wraps this paragraph, an empty list included, so no list can pass. The fix belongs to `_wrap` (never break inside backticks) or to the splitter (a newline inside a code span counts as a space). The tools were not touched.

## Validation notes (lists, not tools)

- C01: "They confirmed gene name errors in 987 files from 704 articles, ..." (A-C01-4, 28 words) raised the mean to 14.17 (original 14.00). Withdrawn; H4.
- C03: "The tidyverse style guide asks for names in lower case, ..." (A-C03-3, 25 words) raised the mean to 12.29 (original 12.15 under the third splitter). Withdrawn; H15. A-C11-10 goes with it.
- C07: "A relative path starts from the working directory, the folder R treats as its current home ..." (A-C07-2, 28 words) raised the mean to 14.56 (original 14.30). Withdrawn; H37.
- C06-2 (session): C03's original definition of a session ("... in the current session (R from the moment it starts until it is closed or restarted) ...", 30 words) would close it, but it took C03's gap-only mean to 12.97 against the original's 12.57 under the first splitter. Not restored; H31.

## Gap by gap

### C01
- **A-C01-1** hole (H1): ÷ and × appear only in Illustration 1's working block; no prose in the original introduces them, and Book 0's records contain no ÷ at all.
- **A-C01-2** hole (H2): the original also uses "line of code" and "comment" before C02 defines them.
- **A-C01-3** hole (H3): the original names "inappropriate weighting of summary statistics" but never explains weighting; naming it would not let the reader follow "so did the weighting alone".
- **A-C01-4** hole (H4): the original sentence that ties 987 files to 704 articles failed validation (above).
- **A-C01-5** not a defect: the illustration sentence states the year itself ("Excel's behaviour in 2016, as the authors report it"); nothing depends on the paper's date.
- **A-C01-6** restored: "The papers' highest category was public debt above 90% of gross domestic product (GDP), a measure of the size of an economy." It defines GDP and "the highest category", which Illustration 2's table relies on.
- **A-C01-7** not a defect: "Book 0" is the series convention (brief).
- **A-C01-8** not a defect: "default settings" and "formula" are everyday spreadsheet words for this reader; no exercise turns on them.

### C02
- **A-C02-1** hole (H5): the original names no website or install steps either.
- **A-C02-2** restored, residual (H6): "Open RStudio and you see several panes." This gives "pane" its meaning. Where the console sits on screen is not said in the original.
- **A-C02-3** restored: "When R cannot do what you asked, it prints an error message." It is the antecedent of "Read it word by word."
- **A-C02-4** hole (H7): the illustration's "Book 0 taught you the sign ÷" is not supported by Book 0's records (no ÷ anywhere). An error, not missing text.
- **A-C02-5** restored, residual (H8): "It says what it could not do and, for a line it could not read, where on the line it stopped." The reader now knows the numbers mark a place. That `1:4` means line 1, character 4 is in neither version.
- **A-C02-6** not a defect: P8 asks for the cause, which the caret and the kept comment rule ("Everything after a `#` on a line is a comment") give; the wording "unexpected symbol" is not needed.
- **A-C02-7** not a defect: Ex 1 is retrieval, and the kept definition says "If the instruction is incomplete, R shows `+` instead of `>`".
- **A-C02-8** hole (H9): the claim about the letter x is asserted, not demonstrated, in the original too; demonstrating it needs a code block.
- **A-C02-9** hole (H10): cross-book contradiction with B6; needs a decision.
- **A-C02-10** hole (H11): the original never says whether spaces matter.
- **A-C02-11** hole (H12): select-all and Mac keys are not in the original.
- **A-C02-12** hole (H13): the output block omits the echoed lines; changing it is a code-gate change.

### C03
- **A-C03-1** restored, residual (H14): "The objects you have made so far sit in a list called the workspace." and "RStudio shows it in the Environment pane, and `ls()` prints it." They are the antecedent of "That list is not your script." The next kept sentence ("It holds every line you ran today ...") still says lines where `ls()` shows objects; that is in the original too.
- **A-C03-2** not a defect: the reader can type `ls()` as shown; what the brackets mean is C05's subject.
- **A-C03-3** hole (H15): the original's style-guide sentence (defining snake case and the style guide) failed validation (above).
- **A-C03-4** hole (H16): the original never locates the Environment pane.
- **A-C03-5** restored, residual (H17): "R accepts `=` in most places." The reader knows `=` can assign. Why the book uses `<-` went with the withdrawn style-guide sentence (H15). Whether Book 0 ever wrote `BMI = w / h^2` (illustration) could not be confirmed in Book 0's records.
- **A-C03-6** not a defect: the reader needs only the names `ls()` prints; text in quotation marks is taught in C04.

### C04
- **A-C04-1** restored: "Numeric values are numbers (R keeps two kinds, integer and double, and treats both as numbers)." It ties the text's "numeric" to `typeof()`'s `"double"`.
- **A-C04-2** not a defect: the illustration glosses the message ("one of the things being multiplied is not a number").
- **A-C04-3** hole (H18): warning versus error, and `mean.default`, are not explained in the original prose.
- **A-C04-4** hole (H19): the original never names `>` or introduces `>=` (P9).
- **A-C04-5** hole (H20): P2, TRUE as 1, untaught in the original.
- **A-C04-6** hole (H21): P5, several positions in `[ ]`, untaught.
- **A-C04-7** hole (H22): P7, `max()` and text ordering, untaught.
- **A-C04-8** hole (H23): P9, text compared with a number, untaught.
- **A-C04-9** hole (H24): P11, `NA` in a logical index, untaught; the honest prediction is wrong.
- **A-C04-10** hole (H25): assigning to one element is never taught; Ex 1 needs it.
- **A-C04-11** not a defect: the usable rule ("Never test two decimals with `==`") does not need binary explained; the original also leaves it undefined.
- **A-C04-12** restored: "In R, a set of values in a row, kept in order under one name, is a vector." and "A vector holds one type of value." They are the antecedents of "You build one" and "The three you need now".
- **A-C04-13** not a defect: the reader needs only the file's name here; the text says reading it comes later.
- **A-C04-14** hole (H26): padding to 152.0 and the leading space before `[1]` are not explained in the original.
- **A-C04-15** restored with A-C04-1: the same sentence names integer and double. With the kept "character" and "logical", the reader can map every `typeof()` answer the section uses.

### C05
- **A-C05-1** hole (H27): the original names `median()` and `sd()` but never ties `sd()` to Book 0's standard deviation or says it divides by n − 1.
- **A-C05-2** hole (H28): `trim` is never explained in the original prose.
- **A-C05-3** restored: "A help page, opened with `?name` or `help(name)`, describes one function in fixed sections: Description, Usage, Arguments, Value (what it returns) and Examples." With R open, the reader can now find and read the page Ex 1 and P5 need.
- **A-C05-4** hole (H29): continuing a line after `|>` and indenting it are not covered.
- **A-C05-5** restored: "So `round(1)` here means `round(the mean, 1)`." It shows that the piped value fills the first argument, which is why `mean()` with no `x` works in a pipe.
- **A-C05-6** hole (H30): "rung" is course vocabulary, never defined for this reader.
- **A-C05-7** not a defect: the kept must-know says "Report the count with it, "3.77 kg (n = 9)""; n is the count.
- **A-C05-8** not a defect: P4 asks the reader to run the code.
- **A-C05-9** not a defect: P6 can be done with `sum(known_g) / length(known_g)`, shown in Illustration 1.
- **A-C05-10** restored: "Writing one is taught at the next rung of this subject." The reader is told not to attempt it here. ("Rung" stays a hole, H30.)

### C06
- **A-C06-1** restored: "Most are kept on CRAN, the Comprehensive R Archive Network, a set of websites from which R downloads them." It defines CRAN and says installing downloads from websites.
- **A-C06-2** hole (H31): session and starting a fresh one are not explained in C06's original; C03's definition would close it but fails validation (above).
- **A-C06-3** hole (H32): the quotes rule (`install.packages("x")` versus `library(x)`) is never stated; P6 depends on it.
- **A-C06-4** restored: "A package is a collection of R functions, data and documentation that extends what base R, the set of standard packages installed with R itself, can do." It introduces base R, and gives the definition back its defining sentence.
- **A-C06-5** not a defect: the kept install line installs dplyr, and Ex 1 says readr reads the file and dplyr reshapes it.
- **A-C06-6** not a defect: R's print format; only the number matters.
- **A-C06-7** hole (H33): P4 needs the project and the file in `data-raw/`, which C07 sets up.
- **A-C06-8** hole (H34): "nesting observation" is undefined in the original too.
- **A-C06-9** not a defect: the folder in the file name does not stop the reader writing the script.
- **A-C06-10** hole (H35): comparing a version with text is unexplained in the original.
- **A-C06-11** restored: "Packages change." It is the antecedent of "Each has a version number".

### C07
- **A-C07-1** hole (H36): `~` is never explained.
- **A-C07-2** hole (H37): the original's definition failed validation (above).
- **A-C07-3** hole (H38): the original names the marker but never shows how to create `.here` or an RStudio project.
- **A-C07-4** hole (H39): opening a terminal is not covered (also A-C10-7).
- **A-C07-5** restored, residual (H40): "It says what the project is, where the data came from, and how to run it again." This gives the README's contents. CSV is still defined only in Ex 2.
- **A-C07-6** not a defect: P4 names `dim()` and says what it gives; the reader runs it.
- **A-C07-7** hole (H41): `head()` and `write_csv()` in P8 are not introduced anywhere in the original prose.
- **A-C07-8** hole (H42): P10 needs deleting, writing and comparing files, never taught.
- **A-C07-9** not a defect: the instruction (type forward slashes) is usable without knowing why.
- **A-C07-10** not a defect: `list.files(here())`, shown in Illustration 2, shows whether the folder exists.
- **A-C07-11** restored: "`Final data (2).xlsx` and `final data.xlsx` are a quarrel waiting to happen." The example shows what "capital letters used to tell two files apart" means.

### C08
- **A-C08-1** restored: "Each type of observational unit forms a table: facts about a child that do not change between visits go in one table, and measurements made at each visit go in another." It is the third of the "three rules".
- **A-C08-2** restored in C06: "The tidyverse is a family of packages built to work together." (C06 `simplified_explanation`, 11 words). C06 is where the reader meets the tidyverse before C08.
- **A-C08-3** restored, residual (H43): "It tells you its size and the type of each column when it prints." The reader now knows `<chr>`, `<dbl>` and `<date>` are types. What each abbreviation stands for is in neither version.
- **A-C08-4** hole (H44): "recycled" and the `!`/`•`/`ℹ` bullets are unexplained in the original.
- **A-C08-5** hole (H45): Broman and Woo's advice is never summarised; Ex 2 depends on it.
- **A-C08-6** hole (H46): "the help page" (palmerpenguins) is never named or shown how to open (also A-C10-10).
- **A-C08-7** hole (H47): `unique()` is used without a gloss.
- **A-C08-8** hole (H48): `glimpse()`'s package and the "…" truncation are unexplained.
- **A-C08-9** not a defect: P4 to P6 ask the reader to run code, and P6 explains `table()`.
- **A-C08-10** not a defect: P8 asks what broke and why the conclusion looks reasonable; no splitting is needed.
- **A-C08-11** hole (H49): P10 needs combining columns (C10's `n_distinct()` on two columns).
- **A-C08-12** hole (H50): `# A tibble` in output against "`#` starts a comment".
- **A-C08-13** not a defect: author-year citation is the book's convention.

### C09
- **A-C09-1** restored: "So `read_csv()` has to guess." and "Then it prints what it decided." They are the antecedent of "Read that report every time."
- **A-C09-2** hole (H51): `""` as the empty string is never glossed.
- **A-C09-3** hole (H52): SPSS, SAS, sheet, cell range and attribute are used undefined in the original too.
- **A-C09-4 to A-C09-9, A-C09-11** hole (H53): code in the illustrations used without a gloss in either version.
- **A-C09-10** hole (H54): the NHANES `.xpt` files are never said to be obtained; P6 and P9 need them.
- **A-C09-12** hole (H55): "sample weights" undefined, beside body weight.
- **A-C09-13** hole (H56): codebook, code tables, survey estimates undefined.
- **A-C09-14** hole (H57): Ex 2's leading zeros are never taught.
- **A-C09-15** not a defect: P3 gives the letters (`c`, `d`); the reader with R can try them as the `col_types` string.
- **A-C09-16** not a defect: P6 and P9 ask the reader to run code.
- **A-C09-17** hole (H58): P10 needs copying a file and editing one character, never taught.
- **A-C09-18** not a defect: the table directly below translates `kg/m**2` as kg/m^2.
- **A-C09-19** hole (H59): `.default` in P7 is unexplained; the problem turns on it.

### C10
All eleven are holes; the original prose fills none of them.
- **A-C10-1** H60; **A-C10-2** H61; **A-C10-3** H62; **A-C10-4** H63; **A-C10-5** H64; **A-C10-6** H65; **A-C10-7** H39; **A-C10-8** H66 (contradiction); **A-C10-9** H67 (contradiction); **A-C10-10** H46; **A-C10-11** H68.

### C11
- **A-C11-1** hole (H69): P1 to P3 call `tibble()` with only dplyr loaded, against C08's "from the tibble package"; a code change.
- **A-C11-2** hole (H70): the definition lists `<`, `>`, `<=`, `>=` without meanings (original too).
- **A-C11-3** hole (H71): "verb" undefined.
- **A-C11-4** hole (H72): `print(n = 5)` new, unglossed.
- **A-C11-5** hole (H60): bare column names.
- **A-C11-6** hole (H73): P9 needs operator precedence and "complex types", never taught.
- **A-C11-7** not a defect: a forward pointer to a later section; nothing here needs it.
- **A-C11-8** not a defect: P4 to P6, P12 and P13 ask the reader to run code.
- **A-C11-9** hole (H74): `<NA>` against `NA` in printouts.
- **A-C11-10** hole (H15): it would have been closed by C03's style-guide sentence, which was withdrawn.
