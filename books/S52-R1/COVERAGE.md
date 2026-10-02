# S52-R1 coverage against outside standards

Written at Task 1 (PIPELINE.md) on 2026-10-02, after the inventory. The map was audited once as a whole; this
checks the rung at its own level against three standards opened now, so the inventory is not judged only
by the map it was built from. The three: the NMC's competency guidelines for MD Community Medicine (what
the reader's own training asks of data handling), the table of contents of *R for Data Science* 2e (the
standard first R text, and the one the tidyverse's own "Learn" page names as the place to start), and the
Carpentries' lessons for people who have never programmed (Software Carpentry's *R for Reproducible
Scientific Analysis* and Data Carpentry's *Data Organization in Spreadsheets*). Items a first-rung book
should hold are listed (Carpentries episodes by the names their pages use in the lesson's episode list); items clearly beyond it are listed only where a later rung or another subject
holds them, so that nothing is lost silently.

| Standard (URL opened) | Item | Here | Where |
| --- | --- | --- | --- |
| NMC, MD Community Medicine guidelines (https://nmc.org.in/storage/new/MD-Community-Medicine.pdf) | Objective 3: "conduct data collection and management, data analysis and report" | covered | C07, C09, C10, C19, C21, C22 |
| NMC, MD Community Medicine | Course content 3(vi): "Apply computer based software application for data designing, data management & collation analysis e.g. SPSS, Epi-info, MS office" | covered (management and analysis, in R); data-entry design deferred | C09 reads SPSS (.sav) and Excel files; designing a data-capture form deferred to S52-R2 (P5) |
| NMC, MD Community Medicine | Psychomotor: "data collection, compilation, tabular and graphical presentation, analysis and interpretation, applying appropriate statistical tests, using computer-based software application" | covered (compilation, tables, graphs); tests deferred | C16, C18; statistical tests to S03 and S04 |
| NMC, MD Community Medicine | Course content 3(v): "difference between data, information & intelligence, types of data" | covered (types of data as stored: numeric, text, logical, categorical, date); data/information/intelligence not taught | C04, C14, C15 |
| R4DS 2e contents (https://r4ds.hadley.nz/) | Whole game: data visualisation (ch. 1) | covered | C18 |
| R4DS 2e | Workflow: basics (ch. 2) | covered | C02, C03, C05 |
| R4DS 2e | Data transformation (ch. 3) | covered | C11, C12, C16 |
| R4DS 2e | Workflow: code style (ch. 4) | covered | C03 |
| R4DS 2e | Data tidying (ch. 5) | covered | C08, C17 |
| R4DS 2e | Workflow: scripts and projects (ch. 6) | covered | C02, C07, C21 |
| R4DS 2e | Data import (ch. 7) | covered | C09 |
| R4DS 2e | Workflow: getting help (ch. 8) | covered | C05 |
| R4DS 2e | Layers (ch. 9) | covered | C18 |
| R4DS 2e | Exploratory data analysis (ch. 10) | covered in part (summaries and plots); EDA as a method deferred | C16, C18; S58-R2 (visualisation) |
| R4DS 2e | Communication: labels, scales, themes (ch. 11) | covered in part (labels with units, honest axes) | C18; S58 |
| R4DS 2e | Logical vectors; numbers (ch. 12–13) | covered | C04, C11 |
| R4DS 2e | Strings (ch. 14) | covered in part (trimming, case) | C12, C14 |
| R4DS 2e | Regular expressions (ch. 15) | **gap** | no S52 rung names it; proposed amendment 2 |
| R4DS 2e | Factors (ch. 16) | covered | C14 |
| R4DS 2e | Dates and times (ch. 17) | covered (dates; times of day not taught) | C15 |
| R4DS 2e | Missing values (ch. 18) | covered | C13 |
| R4DS 2e | Joins (ch. 19) | covered (doorstep: `left_join`, `anti_join`) | C17 |
| R4DS 2e | Spreadsheets (ch. 20) | covered (reading Excel); Google Sheets not taught | C09, C15 |
| R4DS 2e | Databases; Arrow (ch. 21–22) | deferred | S52-R2 (P4, R3) |
| R4DS 2e | Hierarchical data; web scraping (ch. 23–24) | deferred | web scraping to S53-R2; hierarchical (JSON) data not on the S52 ladder and not needed by any build target seen |
| R4DS 2e | Functions (ch. 25) | deferred | S52-R2 (P1); C05 teaches calling |
| R4DS 2e | Iteration (ch. 26) | **gap** | S52-R2 P1 names functions, not iteration; proposed amendment 1 |
| R4DS 2e | A field guide to base R (ch. 27) | covered in part (`[ ]`, `$`) | C04, C08 |
| R4DS 2e | Quarto; Quarto formats (ch. 28–29) | deferred | S52-R2 (P3, R1) |
| Software Carpentry, *R for Reproducible Scientific Analysis* (https://swcarpentry.github.io/r-novice-gapminder/) | Prerequisite: files, folders, paths | covered (the lesson assumes it; this book teaches it, since Book 0 does not) | C07 |
| Software Carpentry | 01 R and RStudio introduction | covered | C02, C03 |
| Software Carpentry | 02 Project introduction | covered | C07 |
| Software Carpentry | 03 Seeking help | covered | C05 |
| Software Carpentry | 04–05 Data structures | covered | C04, C08, C14 |
| Software Carpentry | 06 Data subsetting | covered | C04, C11 |
| Software Carpentry | 07 Control flow | **gap** (as amendment 1) | `if_else()`/`case_when()` in C12 cover the vectorised case; loops are on no rung |
| Software Carpentry | 08 Plotting with ggplot2 | covered | C18 |
| Software Carpentry | 09 Vectorisation | covered | C04 |
| Software Carpentry | 10 Functions | deferred | S52-R2 (P1) |
| Software Carpentry | 11 Writing data | covered | C16, C21 |
| Software Carpentry | 12 dplyr | covered | C11, C12, C16 |
| Software Carpentry | 13 tidyr | covered | C17 |
| Software Carpentry | 14 knitr and markdown | deferred | S52-R2 (P3) |
| Data Carpentry, *Data Organization in Spreadsheets* (https://datacarpentry.github.io/spreadsheet-ecology-lesson/) | Formatting data tables in spreadsheets; common mistakes | covered | C08, C10 |
| Data Carpentry, spreadsheets | Dates as data | covered | C15 |
| Data Carpentry, spreadsheets | Quality control (including data validation at entry) | covered for checks in code; validation at entry deferred | C19; S52-R2 (P5) |
| Data Carpentry, spreadsheets | Exporting data to plain text (CSV) | covered | C09 |

**Gaps proposed to Harsh** (in the source-gate message; never added without his word; `map/AMENDMENTS-v3.1.yml` not edited):

1. **Iteration and control flow** (R4DS ch. 26; Software Carpentry episode 07). Repeating one operation over many columns or files (`across()`, `purrr::map()`, a `for` loop) is in every first R course opened and on no S52 rung. Proposed: revise S52-R2 P1 to "Writing functions and iterating with them rather than repeating blocks; data.table idioms for larger data". Rung 1 keeps `across()` inside `summarise()` (C13) and vectorised `if_else()`/`case_when()` (C12) only.
2. **Regular expressions** (R4DS ch. 15). Pattern matching in text — cleaning free-text survey answers, extracting codes from IDs — is in R4DS and on no S52 rung. Proposed: add to S52-R2 as a concept ("Text cleaning with regular expressions, for free-text and coded fields"). Rung 1 teaches only trimming and case (C12, C14).
3. Not proposed, recorded for completeness: the NMC guideline names SPSS, Epi-info and MS Office as the software; the course teaches R. C09 reads SPSS and Excel files so the reader can move a department's existing files into R. Whether C09 or C22 should cite the NMC line (it would need filing at intake, with its date established) is Harsh's call; it is listed as optional in READY.md.

**Harsh's decision, 2 Oct 2026:** gap 1 (iteration) accepted, added as `S52-R2-A01` (revises S52-R2 P1); gap 2 (regular expressions) refused, not added.
