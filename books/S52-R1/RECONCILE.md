# Task 2b reconcile · S52-R1 · 3 Oct 2026

Backup of the 22 records before any edit: `/tmp/claude-0/reconcile-backup/S52/`.
After the edits: `code_gate.py --write` on C06–C09, then `--check --subject S52-R1` gave 0 failures
(230 sessions), and `build.py --check` gave blocking 0.

## Notes from the batches: what happened to each

Key: **applied** = edited here; **already handled** = the records already did it; **rejected** =
not done, reason given; **conductor** = outside the records, left for the conductor.

### b1 (C01–C03)

| Note | Disposition |
| --- | --- |
| The gate's parse-error layout differs from the console's, and the gate runs nothing from a block it cannot parse | **Applied**, in part. Checked with `R --vanilla -q` in a UTF-8 locale. C02 and C03 already give the console's wording as a second form; they do not claim the layout matches. C02 practice 8 had a script whose line 2 prints `[1] 1.65` in a console before the error. Its answer now says so, and says the book's output shows the error alone. Listing this difference in TOOLING-CODE-GATE.md is **conductor**. |
| Terms from C01–C03 to reuse | **Applied** where they had drifted. C06 now calls `.GlobalEnv` "the workspace", as C03 and C21 do. C03 now glosses "session" at first use; C21's "fresh session" builds on it. |
| C08 should name the third meaning of "variable" | **Already handled** (C08 simplified explanation and retrieval). |
| C02's script `bmi_arithmetic.R`; `code/analysis.R` comes in C07/C21 | **Already handled**. 29 uses of `Rscript code/analysis.R`. The other script names are examples (C07's `count_rows.R`, `clean.R`). |
| C15 can point back to C01's gene-name facts | **Already handled**. C15 says "as the first section of this book showed" and uses `{{n:ziemann_affected_pct}}`. |
| C19 discharges C01's "compare one count with another" | **Applied**. C19's simplified "Row count" bullet now points back to the PHE case in the first section. |
| C01 renamed | **Applied** (accepted). The record already had the title "When data change silently: three documented failures". INVENTORY.md row C01 now has the same title, and "what the four share — a step done by hand" now reads "what the three share — the change was silent", with the reason. The other pointers to C01 (C15, C19, C20) describe it as "the first section"; all three agree with the new title. No pointer anywhere says "four" or "by hand" about C01. |

### b2 (C04–C06)

| Note | Disposition |
| --- | --- |
| Terms; "workspace" versus `.GlobalEnv` | **Applied** (C06: "`.GlobalEnv` is the workspace, where …"). |
| C07 can say `here()` was met in C06 | **Already handled**. C06 glosses it and points forward. A recall in C07 is optional; nothing added. |
| C04's "the same ten numbers" promise; C09 keeps readr's default `na` | **Already handled**. C09 reads with the default. Its `na = "-99"` example is the trap it teaches. |
| C11 can point back to C04's `== NA` | **Already handled**. C11 teaches only `filter()` dropping NA. |
| C12 reuses `round()` | **Already handled**. |
| C13 can point back to C05's `na.rm` count | **Already handled**. Nothing contradicts it. |
| C21 versions: add keys if repeated | **Already handled** (b8: C21 does not repeat R 4.6.1 or dplyr 1.2.0). |

### b3 (C07–C09)

| Note | Disposition |
| --- | --- |
| The gate dropped line breaks in cli messages | **Already handled**. The gate is fixed. C09's column report prints on separate lines. |
| `penguins_rows`, `penguins_cols`, `bmx_rows`, `bmx_cols` keys | **Applied** in every prose field (see the numbers section). |
| Do not write "344 penguins" | **Applied** where the book's own voice said it: C02 practice 4 prompt and practice 10 answer; C04 illustration 2; C06 illustration 1 and practice 4; C11 figure caption; C16 practice 8. Quoted claims that are wrong on purpose (C08 practice 9, C13 practice 9, C18 practice 9) were kept. The C11 bar label "all penguins" sits in the table the figure is drawn from. It was left alone because changing it means a redraw. **Audit**. |
| C10 README lists the checksum, pointing back to C09 | **Applied**. C10's README now has an "MD5 checksum on arrival" line (the value is C09's gate output, `049da101…`) and a sentence pointing to the section on reading a raw file. The list of six README parts and the retrieval answer now include the checksum. |
| C13 can reuse C09's `na` and BMX_L missing counts | **Already handled**. C13 does not reprint 106/361/389/670, so no key is needed. |
| C07's terminal paragraph versus C21 | **Applied**. C07 keeps the paragraph and adds one sentence pointing forward to C21. |
| `$`, backticks and `I()` taught once | **Applied**. Before C08, `$` and backticks appear only in C07 practice 10's answer, which now has a one-line gloss and a forward pointer. C11's sentence that taught backticks again now recalls C08. |
| C06 uses `glimpse()` from tibble; C11 uses `|`; the terms list | **Already handled** (for information only). |

### b4 (C10–C12)

| Note | Disposition |
| --- | --- |
| 1. One object name for the read file | **Applied**. C06–C09 named it `penguins` and C10–C21 named it `penguins_raw`. Every code use in C06–C09 is now `penguins_raw` (59 changed lines, two of them inline code in prose). The book's convention is now the same throughout: `penguins_raw` is the file as read, and `penguins` is a cleaned copy made with `mutate()` (C11, C12, C14, C16, C18). Outputs were refilled by the gate. The only output change was C08 practice 7's parse-error column (1:20 → 1:24), and the prose does not cite that column. The sentence the note suggests, saying that newer base R ships `datasets::penguins_raw`, is **rejected for now**. Intake log-a finding 2 says the R version is not established and must be checked before the book says anything. **Conductor**: source it, then add one sentence in C09. |
| 2. C09 column report | **Already handled** (the gate is fixed). |
| 3. Backticks and `show_col_types` taught twice | **Applied** for backticks (C11 now recalls C08). The `show_col_types` gloss in C11 stays: C09 shows the message but does not gloss the argument. |
| 4. The `data-raw/` rule versus a dictionary typed by hand | **Applied**. C07 said "Nothing ever writes into `data-raw/`" and its table said "nobody, ever". That contradicted C10, where the dictionary is typed into `data-raw/`, and C07's own rename-on-arrival point. C07 now says "No code ever writes into `data-raw/`, and no one edits a raw file there", the table says "you, once, when it arrives; never the code", and the retrieval answer says "no code writes to it". |
| 5. C11 and C12 point to the section on missing values | **Already handled** (C13 declares codes and reports missing values). |
| 6. C19 range checks agree with C10 | **Already handled**. C19 has the trap of taking limits from min/max. |
| 7. C22 README names the dictionary and the outputs | **Already handled** (`data-raw/nhanes_dictionary.csv`, both outputs). |
| 8. `count()` and `n_distinct()` used early with a gloss | **Applied** where a gloss was missing. C12's first `count()` now has a gloss and a pointer to the section on categories. C10 and C11 already had both. `n_distinct()` is in fact introduced in C06. |

### b5 (C13–C15)

| Note | Disposition |
| --- | --- |
| C16: `summarise()` was met in C13 | **Applied**. C16's simplified explanation now says "met once in the section on missing values". Its first sentence said the earlier sections "kept every row", which is false for `filter()` and `drop_na()`, so it was reworded. |
| C16: `count()` was taught in C14 | **Already handled** (C16 says "met in the section on categories"). |
| C18: factor order | **Already handled** (for information only). |
| C19 row counts point back to C13 | **Already handled**. |
| RIAGENDR coding is the reverse of C14's made-up codes | **Already handled**. C17 and C22 cite the codebook (1 Male, 2 Female). C14 says its codes are made up and come from a dictionary. No edit. |
| forcats and lubridate in the front-matter package list | **Conductor**. |
| Terms | **Already handled**. |

### b6 (C16–C18)

| Note | Disposition |
| --- | --- |
| C09 11933 → `{{n:demo_rows}}` | **Applied** (C09 practice answer). |
| C13 already teaches `n()` versus values used | **Rejected** as an edit here. Shortening C16's illustration is compression-pass work (Task 5). The two do not contradict each other. |
| C14 introduces `count()`; the title to use | **Already handled** ("section on categories" fits "Categories as factors"). |
| C19 discharges the dedup promise; `relationship` | **Already handled** (C19 practice 8 and the dated-comment fix). **Applied** a recall too: C19's NHANES join now says C17 wrote the same promise into the join with `relationship = "one-to-one"`, and that the row-count check works after any step. |
| C19 and C22 reuse the join and the numbers | **Already handled** for the join (C22 matches C17; C19 joins without `relationship` on purpose, to show the hand checks). **Applied** for the numbers: 2680, 3290, 29.3 and 28.1 are now keys. |
| C21 and C22 output idiom (`dir.create`) | **Already handled** (the same idiom in C07, C09, C16, C18, C21, C22). |
| C21: histogram bins change on ggplot2 4.x | **Rejected**. Optional, and C21 makes its version point without it. |
| The gate cannot see plots | **Conductor** / audit. |

### b7 (C19, C20)

| Note | Disposition |
| --- | --- |
| C13: check the pointer; register 67/81 if reused | **Already handled**. The pointer is correct, and 67/81 appear only in C19. |
| C17: `relationship` and the row count; shorten or point back | **Applied** (C19 recall, as above). |
| C21 and C22 keys; 5970 | **Already handled**. 5970 appears only in C19, and C22 uses 5929 and 6023 (other quantities). |
| C21 discharges C20 | **Already handled**. |
| C22 uses C19's checks and limits | **Already handled** (50–250 cm and 20–300 kg in both). |
| Terms | **Already handled**. |

### b8 (C21, C22)

| Note | Disposition |
| --- | --- |
| C07 terminal paragraph and C21 | **Applied** (forward pointer in C07). |
| C17 points forward to C22 on pregnancy | **Applied** ("…before summarising, as the last section of this book does"). |
| C19 limits in step with C22 | **Already handled**. |
| C06 versions | **Already handled**. |
| The build does not quote-check numbers under `illustrations[]` | **Conductor** / audit. |
| `sessionInfo()` lines are specific to this machine | **Conductor** (for information only). |

### Points from the draft-notes files that bear on consistency

- b2: C06's early use of `here::here()`, `show_col_types` and `nrow()` is glossed and points forward. Kept.
- b4 4: `r norun` for code whose output the reader predicts. C04–C06 use it the same way. Kept.
- b4 5: the dplyr masking message repeats in practice prompts. **Conductor** (decide on `library(dplyr, warn.conflicts = FALSE)` or leave as is).

## Fixes made across batches

1. **Object name.** `penguins` → `penguins_raw` in the code of C06–C09 (see b4 1).
2. **Numbers: existing keys now used in prose.** About 70 literals in prose were replaced, in C01, C02, C04, C06–C14, C16–C19, C21 and C22: 344 → `{{n:penguins_rows}}`, 17 columns → `{{n:penguins_cols}}`, 8860 → `{{n:bmx_rows}}`, 6064 → `{{n:nhanes_adults_rows}}`, 11933 → `{{n:demo_rows}}`, 19.6% → `{{n:ziemann_affected_pct}}`, and C18's ggplot2 3.4.4 → `{{n:ggplot2_version}}`. Left as typed, on purpose: code and output blocks; ```table and ```working blocks; figure captions, alt text, `numbers[].value` and spec checks; quote fields; C10's quotation of the help page ("a tibble with 344 rows and 17 variables"); "344 combinations" in C10 (another quantity); and C20's "56%" (Trisovic's success rate, not the key's failure rate).
3. **Numbers: 18 new keys** in `numbers.yml`, each with its meaning and the record and chunk that prints it, and each now used in prose: `penguins_ids` 190, `penguins_mass_n` 342, `penguins_mass_mean` 4201.754, `penguins_mass_mean_g` 4202, `penguins_adelie` 152, `penguins_chinstrap` 68, `penguins_gentoo` 124, `penguins_gentoo_mass_n` 123, `penguins_female` 165, `penguins_male` 168, `penguins_sex_missing` 11, `penguins_torgersen` 52, `penguins_biscoe` 168, `penguins_dream` 124, `nhanes_men_bmi_n` 2680, `nhanes_women_bmi_n` 3290, `nhanes_men_bmi_mean` 29.3, `nhanes_men_bmi_median` 28.1. Each value was checked against a gate-filled output. Left as typed: C22's women's figures (3249, 30.3, 28.7). They come after the pregnancy exclusion, so they are other quantities from C17's even where the printed value is the same. 333 is also left: in C13 it counts rows complete on mass, flipper and sex, and in C14 rows with sex recorded, a different meaning.
4. **Backward pointers checked** (all 60 "section on…/last section" phrases). Fixed: C11 said "the last section left you with the whole penguin file" (the last section is C10), now "the section on reading a raw file"; C14 said "the last section but one", now "the section on making new columns". The rest name the right section.
5. **Forward uses without a gloss**, now glossed with a pointer: `read_csv()` at its first use in C07; `$`, backticks and `write_csv()` in C07 practice 10; `count()` in C12.
6. **One term, one meaning.** Workspace (C06); session glossed (C03); "raw-data folder" → `data-raw/` (C07); the `data-raw/` rule (C07 versus C10). Checked and consistent: `|>` throughout, taught in C05; `<-`; snake_case; no `library(tidyverse)`; no `=` assignment; the same `dir.create(here("output"), showWarnings = FALSE)`; "tibble" is "the tidyverse's kind of data frame" (C08) and is used only for printed tables; "variable" has three meanings (C03, C08); NHANES range limits.

## Open, for the conductor or the audit

- The base R `datasets::penguins_raw` sentence: find a source for the R version first (log-a finding 2).
- C11 figure: the bar label "all penguins" in table block 0. Changing it needs a redraw.
- TOOLING-CODE-GATE.md "Remaining differences": add that a block with a parse error prints nothing from its earlier lines.
- Front-matter package list (forcats, lubridate); dplyr masking message noise; numbers under `illustrations[]` not quote-checked; `sessionInfo()` lines specific to this machine.
- Seven version keys in `numbers.yml` are still unused (tidyverse, tidyr, readxl, haven, lubridate, forcats, renv). They are for the front matter.
- Process slip: while drafting this I ran `rm` once, on an empty scratch file I had created by mistake (`books/S52-R1/numbers.yml.new`), seconds after creating it. Nothing else was deleted.
