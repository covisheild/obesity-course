# S52-R1 change record, version 1.0

For Harsh only. The build renders this file to check/_build/S52-R1-change-record.docx. Nothing here is printed in
the book (Harsh, 28 Sep 2026).

## What this version is
Built from scratch, 2–3 October 2026: 22 sections teaching R as a language, the tidyverse verbs and data frames,
and the rule that raw data is never edited, ending with one NHANES dataset analysed end to end in a script that
reruns with one command. It is the first book in the series with R code; every output printed in it was produced
by running the code (R 4.3.3) and is rechecked by the build's new code gate.

## Changes, by section
| Section | Change | Why (defect, reader note, new source) |
| --- | --- | --- |
| All | New book | Rung S52-R1 of the curriculum |
| C01 | Three documented failures, not four; PHE described as an automated transfer that never names Excel; Herndon's journal numbers | Only three cases have held sources; audit |
| C10–C22 | `library(dplyr, warn.conflicts = FALSE)` in every session | Removes a 9-line message repeated across the book |
| C10, C22 | Data dictionaries split or narrowed | Rendered tables broke words mid-word |
| C17 | Visit chart ticks at 1, 2, 3 | Figure showed 1.25, 1.5 … on a visit axis |
| C18 | Histogram practice recomputed with a sixth value | ggplot2 3.4.4 keeps the last bin's right edge (checked by running) |
| Map | Amendment S52-R2-A01: iteration added to S52-R2 | Coverage gap you accepted at the source gate |

## Open decisions for Harsh
- Length: 322 pages against the 240-page budget. The answers appendix is about 90 pages, because each practice
  answer prints its code and output. A v1.1 could print answers' code without outputs, or move half the drill sets
  to an online appendix; neither is done without your word.
- R versions: the outputs are from R 4.3.3 and ggplot2 3.4.4; a reader on ggplot2 4.x may see different default
  plots. Rebuild on a newer R when the sandbox offers one.

## Not taught, and why
- How to open a terminal on your computer (no held source).
- Survey weights (S54), missing-data mechanisms (S15-R2), functions, Git, Quarto, DuckDB and form tools (S52-R2),
  renv and targets (S52-R3).
- Regular expressions: refused as a map amendment.
