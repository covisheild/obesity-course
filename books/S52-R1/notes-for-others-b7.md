# Notes for other batches and the conductor, from b7 (C19, C20)

| Section | What | Why |
| --- | --- | --- |
| C13 (b5) | C19 says missing values "are counted and reported, as the section on missing values taught", and shows 67 adults with no height and 81 with no weight in NHANES (aged 20 or over). | Check the pointer matches C13; if C13 prints these counts, register keys. |
| C17 (b6) | C19 joins `BMX_L` to `DEMO_L` with `left_join(demo, by = "SEQN")`, checks SEQN unique in both with `n_distinct()`, stores `n_before` and checks the row count after (8860). Practice level 8 shows a repeated ID in the right-hand table adding a row with no warning, citing the `relationship` argument of the dplyr 1.1.4 help page. C19 says "as the section on reshaping and joining used them". | If C17 teaches `relationship = "many-to-one"` or the row-count check itself, the reconcile step can shorten C19's or point back. |
| C21, C22 (b8) | `numbers.yml` has `nhanes_adults_rows` (6064). C19 also prints 5970 adults with both height and weight. C20 uses `trisovic_fail_initial_pct` and `trisovic_fail_cleaned_pct`. | Use the keys; register 5970 if reused. |
| C21 (b8) | C20 ends on "test your code in a clean environment before sharing" (Trisovic's recommendation) and Peng's spectrum; it names setwd(), missing packages and versions, paths and missing objects as the study's error kinds. It does not teach `sessionInfo()` or renv. | C21 can discharge the lesson without repeating the study's figures. |
| C22 (b8) | C19's checks: named `stopifnot()` tests; range limits 50 to 250 cm and 20 to 300 kg for adults, stated as a decision; key check; row counts after each step. | So the journey's script uses the same checks and limits. |
| terms | b7 uses: check, range check, key, key check, row-count check, limits (a decision or a source), "corrected in code, raw file not edited"; reproduce, replicate, re-execution, replication package. | One term for one thing. |
