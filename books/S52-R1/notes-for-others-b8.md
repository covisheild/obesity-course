# Notes for other batches and the conductor, from b8 (C21-C22), 2 Oct 2026

Nothing in another batch's record was edited.

| Section | What | Why |
| --- | --- | --- |
| C07 (b3) | C21 teaches `Rscript` fully (fresh process, no restored workspace, stops at first error; cited to the utils Rscript help page). | C07's terminal paragraph can stay as the first meeting; the reconcile step may point forward in one clause or shorten it. |
| C17 (b6) | C17's analogy_breaks_when says a real analysis would decide about women pregnant at the exam "in code, before summarising". C22 does exactly that (RIDEXPRG; 41 excluded; 6023 adults; 5929 with BMI). | C17 could point forward to the end-to-end section if the reconcile wants the link. |
| C19 (b7) | C22 uses C19's limits (height 50-250 cm, weight 20-300 kg) and named `stopifnot()` conditions, and says so. C22's figure is now the BMI quartiles by gender, not a row-count chart, so it does not duplicate C19's `s52-r1-c19-nhanes-row-counts.png`. | Keep the limits in step if C19 changes them. |
| C06 (b2) | C21 does not restate R 4.6.1 or dplyr 1.2.0 (it says "a newer dplyr"), so no numbers key is needed for them. | b2's note asked. |
| conductor | The build checks `quote` for numbers under `illustration` (singular) only; numbers under `illustrations[]` are not quote-checked (`check_quotes` in check/build.py). Several S52 records use `illustrations`. | A quote gap the audit should cover by hand, or the build could be extended. |
| conductor | `sessionInfo()` output in C21/C22 contains the sandbox's platform, BLAS paths, locale and time zone. It is gate-filled and stable here; a gate run on another machine would differ in those lines. | Worth knowing before a rerun elsewhere. |
