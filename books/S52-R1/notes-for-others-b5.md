# Notes for other batches and the conductor, from b5 (C13-C15)

Nothing in another batch's record was edited.

| Section | What | Why |
| --- | --- | --- |
| C16 (b6) | C13 uses `summarise()` once with `n()`, `sum(is.na(x))` and `mean(..., na.rm = TRUE)`, glossed as "collapses a data frame into one row of summaries; a later section uses it for groups", with no `group_by()`. C13 also teaches writing the n beside every summary as `sum(!is.na(x))`, e.g. "4202 g (n = 342)". | C16 can say summarise() was met in C13 and add groups; keep the "(n = ...)" form. |
| C16 (b6) | C14 teaches `count()` on one and two columns, `.drop = FALSE` for empty factor combinations, and lays `count(species, island)` out as Book 0's two-way table (Adelie 44/56/52, Chinstrap 0/68/0, Gentoo 124/0/0). | C16's `count()` need not re-teach; can point back. |
| C18 (b7?) | C14 sets factor level order (`fct_infreq()`, `fct_relevel()`, `factor(levels =)`) and says the order decides how later counts, tables and plots are laid out. | C18 can use these to order bars without re-teaching. |
| C19 (b7) | C13 counts missing values with `colSums(is.na(penguins_raw))` and `drop_na()` on named columns, with `nrow()` before and after (344 -> 342 -> 333; 34 if no column named). | C19's row counts after each step can point back. |
| C17, C19, C22 (NHANES) | C14 uses made-up numeric codes (1 = female, 2 = male) and stresses labels come from the data dictionary. NHANES DEMO_L codes RIAGENDR the other way round (1 = Male, 2 = Female, codebook). | Whoever labels RIAGENDR should cite the codebook line; C14 never mentions NHANES. |
| conductor | `forcats` and `lubridate` added to the packages the book loads. lubridate prints its own masking message on `library(lubridate)` (date, intersect, setdiff, union), as dplyr does; C15 mentions it once. | Front-matter package list (numbers.yml already has both versions). |
| terms | b5 uses: missing value / missing-value code, complete-case analysis, level(s), factor, parse ("read text into a date"), time difference, ISO 8601, day count (for spreadsheet serial numbers). | One term per thing (SELFCHECK 7). |
