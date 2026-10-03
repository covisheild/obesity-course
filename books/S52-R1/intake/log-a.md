# S52-R1 intake log, group a (textbooks, manuals, guides)

Intake agent for group a, 2026-10-02. Every page was fetched with `mcp__TinyFish__fetch_content`
(markdown). Results too large to show inline were saved by the harness as JSON and split, text unchanged,
into `books/S52-R1/intake/raw/<citekey>-*.txt` (with a `.meta.json` per URL) by `intake/build-a/split.py`.
Every stored passage was cut by `intake/build-a/build_a.py` as `raw[i:j]` between literal anchors (start
inclusive, end exclusive; anchors and the omitted ranges are in the script), and `intake/build-a/verify_a.py`
re-parsed the written source files and tested each passage (the text between `--- passage begins ---` and
`--- passage ends ---`) as a whitespace-normalised substring of the raw fetch for the URL in its block
heading. `intake/build-a/manifest-a.json` lists each passage with its raw file and URL. Nothing was fetched
with curl, wget or a Python HTTP client; no WebFetch output is stored. Registry entries are in
`intake/fragment-a.md` (not merged: the conductor merges). Citekeys checked in `sources/INDEX.yml` and
`check/references/library.bib` on this branch and on `origin/main` after `git fetch origin`: all six new.

**Verbatim check: 96 of 96 passages** (r4ds_2e 46, r_intro_manual 10, r_lang_def 5, swc_r_gapminder 22,
dc_spreadsheets 7, tidyverse_style 6). **Obtained 6 of 6** (including both optional works).

| Source | URL(s) fetched (stored passages) | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Wickham, Çetinkaya-Rundel, Grolemund, *R for Data Science* 2e, online edition | https://r4ds.hadley.nz/ (home) and chapter pages intro.html, data-visualize.html, workflow-basics.html, data-transform.html, workflow-style.html, data-tidy.html, workflow-scripts.html, data-import.html, workflow-help.html, logicals.html, factors.html, datetimes.html, missing-values.html, joins.html, spreadsheets.html | 46 | 46/46 | "This website is and will always be free, licensed under the CC BY-NC-ND 3.0 License." (home page). **No derivatives**: held for quote-checking only; the file header says so | `r4ds_2e` |
| R Core Team, *An Introduction to R* | https://cran.r-project.org/doc/manuals/r-release/R-intro.html | 10 | 10/10 | "Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies." (plus modified-version and translation clauses; held in full in block 1). Copyright 1990 Venables; 1992 Venables & Smith; 1997 Gentleman & Ihaka; 1997-98 Maechler; 1999-2026 R Core Team | `r_intro_manual` |
| R Core Team, *R Language Definition* (optional) | https://cran.r-project.org/doc/manuals/r-release/R-lang.html | 5 | 5/5 | Same verbatim-copy permission notice; "Copyright © 2000–2026 R Core Team" | `r_lang_def` |
| The Carpentries, *R for Reproducible Scientific Analysis* (Software Carpentry) | https://swcarpentry.github.io/r-novice-gapminder/ , LICENSE.html, 01-rstudio-intro, 02-project-intro, 03-seeking-help, 04-data-structures-part1, 08-plot-ggplot2, 11-writing-data, 12-dplyr, 13-tidyr (.html) | 22 | 22/22 | "All Carpentries ... instructional material is made available under the Creative Commons Attribution license" ... "CC BY 4.0" (LICENSE page, last updated 2026-09-01); software MIT | `swc_r_gapminder` |
| The Carpentries, *Data Organization in Spreadsheets for Ecologists* (Data Carpentry; optional) | https://datacarpentry.github.io/spreadsheet-ecology-lesson/ , LICENSE.html, 01-format-data, 02-common-mistakes, 03-dates-as-data, 04-quality-control, 05-exporting-data (.html) | 7 | 7/7 | Same CC BY 4.0 statement on this lesson's own LICENSE page (last updated 2025-02-03) | `dc_spreadsheets` |
| The tidyverse team, *The tidyverse style guide* | https://style.tidyverse.org/ , files.html, syntax.html, pipes.html; licence from https://github.com/tidyverse/style/blob/main/LICENSE.md | 6 | 6/6 | Site pages state none; the repository's LICENSE.md is "Creative Commons Legal Code / Attribution-ShareAlike 3.0 Unported" (CC BY-SA 3.0) | `tidyverse_style` |

## Bibliographic details confirmed (and not)

- **R4DS 2e**: authors confirmed from the site's own author metadata, "Hadley Wickham, Mine Çetinkaya-Rundel, and
  Garrett Grolemund" (in `raw/r4ds_2e-home.meta.json`; also "the product of Hadley, Mine, and Garrett" in the
  Acknowledgments). Title on the site: "R for Data Science (2e)". **Publisher (O'Reilly) and year (2023) are not
  stated on any page fetched**; they come from READY.md and are unconfirmed. No ISBN seen. The Colophon says the
  online version "will continue to evolve in between reprints of the physical book".
- **R-intro**: "This manual is for R, version 4.6.1 (2026-06-24)." Authors as the copyright lines give them
  (Venables, Smith, Gentleman, Ihaka, Maechler, R Core Team); the bib entry names Venables, Smith and R Core Team,
  the conventional form.
- **R-lang**: "This manual is for R, version 4.6.0 (2026-04-24)" (not 4.6.1, unlike R-intro served the same day).
- **Carpentries lessons**: no individual authors or maintainers are named on the fetched pages; author is the
  organisation. Dates are each episode's "Last updated on" line.
- **Style guide**: author metadata "The tidyverse team"; READY.md's "Wickham H, and contributors" is not on the
  page. Undated.

## Findings the conductor and drafters need

1. **Version gap in R4DS outputs.** The online book's own startup output (held, intro block 1) lists tidyverse
   2.0.0 with dplyr 1.2.1, readr 2.2.0, ggplot2 4.0.3, tidyr 1.3.2, forcats 1.0.1, lubridate 1.9.5, stringr
   1.6.0, tibble 3.3.1, purrr 1.2.2: newer than the sandbox (dplyr 1.1.4, readr 2.1.5, ggplot2 3.4.4, ...).
   Every `#>` output in `r4ds_2e.txt` is from the newer versions. Chapters 16 and 17 print a warning new in
   readr 2.2.0 ("The `file` argument of `read_csv()` should use `I()` for literal data as of readr 2.2.0").
   Never paste R4DS output as the book's own; rerun here.
2. **palmerpenguins and base R.** R4DS ch. 1 prints, on `library(palmerpenguins)`, "The following objects are
   masked from 'package:datasets': penguins, penguins_raw" (held, ch. 1 block). So newer R ships its own
   `penguins` and `penguins_raw` in `datasets`; a reader on a current R may get base R's copy when the package is
   not loaded. Relevant to dataset option B and to C06 (masking). Which R version added them is not stated on
   the page; group c / the conductor should check before the book says anything about it.
3. **Two versions of the third tidy rule.** R4DS 2e 5.2: "Each value is a cell; each cell is a single value."
   Wickham 2014 (group b): "each type of observational unit is a table". C08 quotes the 2014 form; it must be
   cited to Wickham 2014, not to R4DS. Data Carpentry adds "cells = data (values)".
4. **Dates: the sources disagree.** Data Carpentry ep. 03 recommends storing "YEAR, MONTH, DAY in separate
   columns or as YEAR and DAY-OF-YEAR in separate columns"; C15 plans ISO 8601 YYYY-MM-DD from Broman & Woo
   (group b). Do not present either as the single rule. DC ep. 03 also states Excel counts days from 31 Dec 1899
   (2 Jul 2014 = 41822) and has a 1904 system, and that Excel turns "MAR1, DEC1, OCT4" into dates (a lesson's
   statement, not a study; C01's gene-name claim still rests on Ziemann 2016).
5. **R4DS ch. 8 "getting help" is Google, Stack Overflow and reprex, not `?`.** For `?mean` and reading a help
   page (C05) cite R-intro (help(), ?, help.start(), example()) or SWC ep. 03 "Reading Help Files".
6. **R4DS does not use `here::here()`** (searched all fetched chapters); C07's `here()` needs the here help page
   (group c). R4DS 6.2.2 recommends RStudio projects and says of `setwd()` "we do not recommend it".
7. **The pipe.** R-intro contains no `|>`; R4DS 3.4 states the base pipe arrived "in R 4.1.0 in 2021"; R-lang
   has only its place in the precedence list; the style guide's Pipes chapter has the layout rules.
8. **Extraction losses.** Some code blocks were dropped by the extractor (known: R4DS 17.2.2's `ymd()/mdy()/dmy()`
   examples; only the rule in words survives). R-intro and R-lang lost their section headings, so blocks are
   named by content. The R-lang type table came out mangled and is not held. Figures are not held anywhere.
9. **Carpentries footer link.** The site footer of both lessons links to the CC BY-SA 4.0 deed (seen in the
   outbound-link list of a first fetch whose result was shown inline and not stored), while each lesson's
   LICENSE page text says CC BY 4.0. The LICENSE page text is relied on and quoted in each file.
10. **Not held, by choice of scope**: SWC episodes 05-07, 09, 10, 14, 15 (so SWC's own factors material is
    not held; C14's "Carpentries ep. 4 factors" has only ep. 04's "Check your data for factors" box, which
    says R 4.0.0 and later no longer converts text to factors); R4DS chapters 9 (Layers), 13 (Numbers) and
    14 (Strings) were not fetched; R4DS exercises everywhere. Fetch them if a drafter needs them.

## Not obtained

Nothing in group a. No host refused; no PDF was needed.

## What needs Harsh

Nothing blocking. Optional: confirm R4DS 2e publisher/year from the print book or the O'Reilly page if the
reference list must state them (the online edition does not).
