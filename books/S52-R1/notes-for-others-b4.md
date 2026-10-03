# Notes for other batches, from b4 (C10-C12)

1. **Object name for the read file (all batches, C06/C09 especially).** C10-C12 read the file as
   `penguins_raw <- read_csv(here::here("data-raw", "penguins_raw.csv"), show_col_types = FALSE)`.
   Newer base R (per R4DS ch. 1's masking message, intake log-a finding 2) ships its own
   `datasets::penguins_raw`, so a reader on a current R who skips the read line silently gets base R's
   copy. If C09 picks another name, reconcile C10-C12 to it; if it keeps `penguins_raw`, C06 or C09 may
   want one sentence on this.
2. **C09 (b3): `read_csv()`'s column report.** In a draft of C10 the gate printed
   `Rows: 344 Columns: 17── Column specification ──…` with the newline missing before the rule. C10 now
   uses `spec()` instead, but C09 prints that report: check the gate output there, and tell the conductor
   if it is a gate formatting bug. The report also truncates long name lists (`Flip...`); `spec()` gives
   them whole (readr vignette, held).
3. **C09 (b3): backticks.** C11 teaches backticks for non-syntactic names in one sentence (cited to R4DS
   7.2) and turns off the column report with `show_col_types = FALSE`, glossed. If C09 already teaches
   both, the C11 sentences can be cut at reconcile.
4. **C07 (b3): data-raw rule.** C10 saves the hand-typed data dictionary as
   `data-raw/penguins_raw_dictionary.csv` (Wilson 4c: raw data and metadata together) and says "no code
   ever writes to that folder". Make sure C07's rule is worded so this does not contradict it.
5. **C13 (b5).** C11's first illustration points ahead: a missing value written as -99 or "not recorded"
   is not `NA` unless declared at read time, "and the section on missing values deals with it". C12's
   level 10 answer says the missing Gentoo body mass should be reported, pointing to the same section.
6. **C19 (b7).** C10 and C12 point ahead to "checking a range in code, so the script stops", and C10 says
   an expected range must not be filled from the file's own min and max. C19 should agree.
7. **C22 (b8).** C10's README names the dictionary file above, the command `Rscript code/analysis.R`, and
   says outputs go to `output/`, without naming the output files. The README in C22 should use the same
   dictionary file name and name its outputs.
8. **C14/C16 (b5, b6).** `count()` is used in C10 and C11 answers with a one-line gloss; `n_distinct()` in
   C10 (C19's territory). Neither re-teaches them.
