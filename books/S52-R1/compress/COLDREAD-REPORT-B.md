# Cold read (5b), reader B: S52-R1-C12 to C22 — gap report

Cold reader v2 (fresh subagent, 3 Oct 2026), reading /tmp/coldread2/b/ (cut sections with illustrations inserted
and `{{n:}}` filled; C01–C11 as background). Saved by the conductor from the reader's returned text.

Totals: 69 gaps. C12 7, C13 5, C14 8, C15 7, C16 6, C17 5, C18 7, C19 4, C20 5, C21 4, C22 11.

Three worst: (1) C18 must-know: "The grammar guarantees that the figure draws your data faithfully" says the
opposite of the section (chosen bins, silently removed rows, the colour trap); it probably lost "does not".
(2) C12 rounding: P3 `round(c(0.5, 1.5, 2.5))` tests a half-rounding rule never taught (Book 0's rule gives 1 2 3);
`digits` means decimal places in `round()` but significant digits in `print()`, unexplained; why rounding cures
the binary-storage problem asserted, not explained. (3) C16/C22 quartiles: R's type-7 rule never given, so R's
quartiles cannot be checked by hand; C22 then calls them "as Book 0 taught them", contradicting C16.

## C12 (7)
1. `if_else` defined but never shown before Ex3/P2 need it.
2. `str_trim` defined but never shown in code.
3. P3: R's rule for rounding halves never taught; Book 0 says "five or more, push it up".
4. `print(..., digits = 17)`: here digits means significant digits, but the definition says round's digits are decimal places.
5. "many decimals… have no exact binary form" with "rounding applies to the number as stored", yet round is the fix; why rounding makes the comparison safe never explained. Read twice.
6. The `.default =` syntax first appears in P9.
7. `rename_with(str_to_lower)` passes a function without brackets, a new idea.
Also: `tibble()` used after only `library(dplyr)`, while C08 said it comes from the tibble package.

## C13 (5)
1. "Or it arrives disguised…" starts with "Or" with no first alternative; "it" refers to nothing.
2. "declared codes with na = c("", "NA", "999")": C09 used -99.
3. "describes 34 nests": a row is one adult's observation, two per nest.
4. P7: the reported 64.5 is the correct mean and cannot come from the code shown.
5. "look at the largest and smallest values of each column": no code given.

## C14 (8)
1. "R has read text as text since version 4.0.0" assumes history never given.
2. `fct_recode` "renames levels" but is applied to text; how text has levels not explained.
3. `levels()` used without introduction.
4. `fct_relevel` never shown, but P5 needs it.
5. What a factor looks like when printed never shown (P1).
6. P4 needs the dataset's help page; how to open one never taught.
7. "It cannot show that the category was recorded correctly": "it" refers to nothing.
8. "Two counts at once": it is one count over two columns.

## C15 (7)
1. "object of class Date": "class" never defined (type was taught); `class()` never shown.
2. "held in R as I() marks it…" garbled.
3. `camp$visit_date <-` adds a column in an untaught way (always mutate before).
4. "Because it is a number underneath": "it" has no referent.
5. P5 needs date comparison, never shown.
6. Date Egg drifts between "nest recorded", "nests observed" and "laid their first egg"; the column never defined.
7. P8: the report's "2 March" is the true date, which does not match the code output (framing).

## C16 (6)
1. "quantile" undefined; the 0% and 100% columns unexplained.
2. "the seventh of nine rules" never shown, so R's quartiles cannot be checked or predicted in P3.
3. `readLines()` unexplained.
4. "…first appears in the file, where group_by() sorted them": "where" must mean "whereas". Read twice.
5. Must-know bullets "Then ask for the median…" and "It is not an estimate…" point at nothing.
6. `write_csv()` never defined, though C21 later refers back to it as explained.

## C17 (5)
1. `pivot_wider`'s arguments, and how it picks the identifying columns, not explained.
2. "There, summarise(.by = visit) cannot reach them": "There" unclear.
3. `relationship = "one-to-one"` never defined; "so no SEQN appears twice" asserted.
4. P5 asks to fill 0, which no taught tool does.
5. P6 "Say why the second count is what it is" needs knowledge about infants the text does not give.

## C18 (7)
1. "The grammar guarantees that the figure draws your data faithfully" reverses the section's message.
2. "the bin to its left" vs `closed = "left"`: the edge value goes to the right-hand bin. Read three times.
3. "within 1.5 times the IQR of the box": measured from where?
4. `count(bin_start_g = floor(...)*500)`: counting a computed expression not taught.
5. `quantile(x, 0.25, …)` passes an argument by position, against C05's rule.
6. The ggplot2 version behind the outputs not stated, though P8 compares versions.
7. "Body masses run from 2700 g to 6300 g": the 6300 maximum never shown.

## C19 (4)
1. `all()` never explained; looks redundant given "not TRUE in every element"; P1 drops it.
2. Error wording for an unnamed check never shown (P1, P4).
3. P7 needs `abs()`, which first appears in C22.
4. "barely move it", then "moved from 26.2 to 23.7". Read twice.

## C20 (5)
1. "Peng's spectrum": Peng never introduced.
2. The "best of both" row (5790 timeouts, 8609 files) exceeds either single run; how built not explained.
3. The must-know about journals with the strictest data-sharing policies does not appear in the body.
4. "The parts of the paper this book holds" unclear (and repository-speak).
5. "correlation coefficients" never taught.

## C21 (4)
1. "attached" and "loaded" used as synonyms, but sessionInfo distinguishes them.
2. `exists()` untaught (P2).
3. "two rungs up": "rung" never defined.
4. Shell commands `ls` and `cat` unexplained.

## C22 (11)
1. `factor(..., labels = )` never taught.
2. `abs()` unexplained.
3. `"\n"` in `cat()` unexplained.
4. `labs(x = NULL)`: NULL unexplained.
5. `ggsave(width = 5, height = 4, dpi = 150)` has no units, against C18's rule; `dpi` unexplained.
6. `cp`, `rm -r`, `> /dev/null 2>&1`, `cmp`, `&&`, `echo` unexplained.
7. "The first step that went wrong… goes first", but the join comes first.
8. "the codebook gave the number of pregnant participants", but the 41 came from `count()` in the script.
9. "as Book 0 taught them" refers to R's type-7 quartiles, which C16 showed differ from Book 0's.
10. `|> ggplot() + geom_` mixes the pipe and `+` right after C18 P9 called that an error; no explanation.
11. "gate" and "rung" undefined.

## Symbols / two meanings (summary)
Before explanation: if_else, str_trim, `.default =`, function passed without (), print(digits=); levels(),
fct_relevel; class, `$<-`, date comparisons; quantile, readLines, write_csv; pivot_wider arguments, one-to-one;
count(name = expr); all(); abs(); exists(); labels =, NULL, "\n", dpi, shell commands; `<int>`, `<lgl>`, `<fct>`,
`<date>`, `<dttm>`; `<NA>` vs NA; `#` in tibble headers; character(0); leading dot in .default/.by/.drop/.groups.
Two meanings: `~` (case_when vs facet_wrap); digits (round vs print); "left" (default edge rule vs closed = "left");
type (data type vs quantile type); class vs type; range; n (column, n(), "n ="); nest/row/penguin;
season/expedition; sex/gender; loaded/attached; the survey-weights pointer under three names; NHANES code 1 in
three columns; `$` picks and creates.
