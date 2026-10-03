# Notes for other batches, from b2 (C04-C06), 2 Oct 2026

Nothing in another batch's record was edited. These say what C04-C06 already teach or assume,
so later sections can point back and not re-teach, and earlier ones can match terms.

| Section | What | Why |
| --- | --- | --- |
| C02, C03 (b1) | C04-C06 assume these terms from C02/C03: "console", "script", "session" and "fresh session", "object", "run", the assignment `<-`, and the arithmetic operators already introduced in words. C04 opens "The last section gave a name to one value at a time". C06 says ".GlobalEnv is where the objects you make are kept" and avoids "workspace"; if C03 names that list "the environment", say so and I will match it. | One term for one thing (SELFCHECK 7); C04's first sentence stands on C03. |
| C07 (b3) | C06 uses `here::here("data-raw", "penguins_raw.csv")` once, glossed as "builds the path to the file from the top of your project" and pointed to the project-folders section. | C07 can say it was met in C06 and now explained. |
| C08, C09 (b3) | C06 uses `readr::read_csv(..., show_col_types = FALSE) \|> nrow()` (gives 344), glossed and pointed forward. C04 types the first ten `Body Mass (g)` values into `c()` and promises that reading the file "gives the same ten numbers" (true with readr's default `na`). | C09 should keep that true, and can point back to C04's NA example. |
| C11 (b4) | C04 already teaches `x == NA` returning NA for every element, `is.na()`, `!` and `&` (in a practice answer), and that a logical NA inside `[ ]` gives an NA element. | C11's "why filter(x == NA) returns nothing" can point back to C04 and only add filter()'s dropping of NA rows. |
| C12 (b4) | C04 gives BMI in words and code once (`70.1 / 1.68^2`, made-up adult, prints 24.83702) and C05 teaches `round()`, `digits`, and "round once, at the end". | C12 can reuse without re-teaching `round()`. |
| C13 (b5) | C05 already teaches that `na.rm = TRUE` changes the count behind a mean (3769.444 g from 9, against 3392.5 g with the missing value typed as 0), counting present values with `sum(!is.na(x))`, and reporting "(n = 9)". C04's boundary point names -99/999 codes and points to declaring them when reading. | C13 can point back and spend its space on counting per column, `drop_na()` and missing codes. |
| C21 (b8) | C06 teaches `packageVersion()`, `R.version.string`, install once / load every session, and defers `sessionInfo()` and renv to "a later section on running a script from top to bottom" (renv "two rungs above"). C06 states once that R 4.6.1 (June 2026) and dplyr 1.2.0 (February 2026) existed when the book was written. | If C21 repeats those two versions, add `numbers.yml` keys and I will switch C06 to them. |
