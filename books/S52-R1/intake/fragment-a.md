# S52-R1 intake, group a (textbooks, manuals, guides): entries to merge

Three blocks for the conductor to paste into `sources/INDEX.yml` (under `files:`),
`check/references/library.bib` (append) and `sources/SOURCES.md` (a new section). Six files for the six
assigned works (two of them optional: `r_lang_def`, `dc_spreadsheets`). Citekeys grepped on 2026-10-02 in
`sources/INDEX.yml` and `check/references/library.bib` on `book/S52-R1` and in `origin/main:` copies of
both files (after `git fetch origin`): none exists. Brace balance of the `.bib` block checked by script.

## 1. `sources/INDEX.yml`, under `files:`

```yaml
  r4ds_2e:
    file: r4ds_2e.txt
    what: >-
      Wickham, Cetinkaya-Rundel and Grolemund, R for Data Science 2e, online edition r4ds.hadley.nz
      (CC BY-NC-ND 3.0: NO DERIVATIVES, held for quote-checking only). Excerpts, whole sections: Introduction
      prerequisites and colophon; ch. 1 (1.1-1.4.2, 1.5, 1.6 ggsave, 1.7); ch. 2 (2.1-2.4, 2.6); ch. 3 (3.1.3,
      3.2.1-3.2.4, 3.3.1-3.3.4, 3.4 pipe, 3.5.1-3.5.6, 3.6); ch. 4 (4.1-4.5); ch. 5 (5.1, 5.2 three rules,
      5.3-5.3.1, 5.4 opening, 5.5); ch. 6 whole except exercises; ch. 7 (7.1-7.2.3, 7.3, 7.5, 7.7); ch. 8 (8.1-8.2);
      ch. 12 (12.2.2-12.2.3, 12.3.1, 12.3.3, 12.5.1-12.5.3); ch. 16 (16.1-16.2, 16.4, 16.5); ch. 17 (17.1-17.2.2,
      17.2.4, 17.4.1-17.4.3); ch. 18 (18.1-18.2.3, 18.3 opening, 18.5); ch. 19 (19.1-19.2.3, 19.3-19.3.1, 19.3.3,
      19.4.1); ch. 20 (20.1-20.2.8, 20.4). Exercises, Google Sheets and all other sections NOT held. Printed
      outputs are from dplyr 1.2.1, ggplot2 4.0.3, readr 2.2.0 etc., not the book's versions
  r_intro_manual:
    file: r_intro_manual.txt
    what: >-
      R Core Team (Venables, Smith et al.), An Introduction to R, manual for R 4.6.1 (2026-06-24), CRAN HTML
      (verbatim-copy permission notice, held in full). Excerpts: getting help; names, commands, comments;
      source() and the workspace; vectors and assignment, vector arithmetic; logical vectors and missing
      values (NA, is.na, NaN); index vectors (logical, replacement); modes and coercion; packages, CRAN and
      namespaces (::); Rscript. No pipe in the manual. Section headings were not extracted
  r_lang_def:
    file: r_lang_def.txt
    what: >-
      R Core Team, R Language Definition, manual for R 4.6.0 (2026-04-24), CRAN HTML (verbatim-copy
      permission notice). Excerpts: objects opening; the six atomic vector types; NA handling; operator
      precedence list (places |>). Type table NOT held (mangled by extraction)
  swc_r_gapminder:
    file: swc_r_gapminder.txt
    what: >-
      The Carpentries, Software Carpentry lesson R for Reproducible Scientific Analysis (r-novice-gapminder),
      pages last updated 2026-09-01 (CC BY 4.0 per its LICENSE page). Excerpts: LICENSE; index; ep. 01 scripts,
      calculator, comparison, assignment, vectorization, environment, packages; ep. 02 project organisation
      (data read-only, output disposable), working directory; ep. 03 help files; ep. 04 opening to type
      coercion; ep. 08 ggplot2 grammar, layers, facets, ggsave; ep. 11 writing data; ep. 12 dplyr select,
      filter, group_by, summarize, count, mutate; ep. 13 long/wide, pivot_longer, pivot_wider opening.
      Episodes 05-07, 09, 10, 14, 15 and all challenges NOT held
  dc_spreadsheets:
    file: dc_spreadsheets.txt
    what: >-
      The Carpentries, Data Carpentry lesson Data Organization in Spreadsheets for Ecologists (CC BY 4.0 per
      its LICENSE page; episodes last updated 2024-03-08 to 2026-08-04). Excerpts: LICENSE; index summary;
      ep. 01 structuring data, columns = variables, rows = observations; ep. 02 all common spreadsheet errors;
      ep. 03 dates as data (whole); ep. 04 quality assurance; ep. 05 exporting data (whole). Ep. 01 exercise
      and ep. 04 quality control NOT held. Its date advice (separate year/month/day columns) differs from
      Broman and Woo's ISO 8601
  tidyverse_style:
    file: tidyverse_style.txt
    what: >-
      The tidyverse team, The tidyverse style guide, style.tidyverse.org (undated; CC BY-SA 3.0 per the
      github.com/tidyverse/style LICENSE.md, held). Excerpts: home page; 1.1 file names; 2.1-2.4 object names,
      spacing, function calls and assignment; 2.7-2.10; chapter 4 Pipes (whole). 2.5-2.6 and other chapters
      NOT held
```

## 2. `check/references/library.bib`, append

```bibtex
@book{r4ds_2e,
  title        = {R for Data Science: Import, Tidy, Transform, Visualize, and Model Data},
  edition      = {2},
  author       = {Wickham, Hadley and {\c{C}}etinkaya-Rundel, Mine and Grolemund, Garrett},
  publisher    = {O'Reilly Media},
  year         = {2023},
  note         = {Online edition, which the authors say continues to evolve between reprints.
                  Licensed CC BY-NC-ND 3.0 (no derivatives): quoted briefly for checking, never
                  adapted. Publisher and year not stated on the pages read; author line from the
                  site's own metadata. Outputs on the site are printed with newer package versions
                  (dplyr 1.2.1, ggplot2 4.0.3, readr 2.2.0) than this book uses},
  url          = {https://r4ds.hadley.nz/},
  urldate      = {2026-10-02}
}

@manual{r_intro_manual,
  title        = {An Introduction to R: Notes on R, a Programming Environment for Data Analysis
                  and Graphics},
  author       = {Venables, W. N. and Smith, D. M. and {R Core Team}},
  organization = {R Core Team},
  year         = {2026},
  note         = {Manual for R version 4.6.1 (2026-06-24); this book's code runs on R 4.3.3.
                  Verbatim copies permitted with the copyright and permission notice preserved
                  (not a Creative Commons licence)},
  url          = {https://cran.r-project.org/doc/manuals/r-release/R-intro.html},
  urldate      = {2026-10-02}
}

@manual{r_lang_def,
  title        = {R Language Definition},
  author       = {{R Core Team}},
  organization = {R Core Team},
  year         = {2026},
  note         = {Manual for R version 4.6.0 (2026-04-24); this book's code runs on R 4.3.3.
                  Verbatim copies permitted with the copyright and permission notice preserved},
  url          = {https://cran.r-project.org/doc/manuals/r-release/R-lang.html},
  urldate      = {2026-10-02}
}

@misc{swc_r_gapminder,
  title        = {R for Reproducible Scientific Analysis},
  author       = {{The Carpentries}},
  howpublished = {Software Carpentry lesson (r-novice-gapminder)},
  year         = {2026},
  note         = {Episode pages last updated 1 September 2026. Instructional material licensed
                  CC BY 4.0 (the lesson's LICENSE page); example code MIT. Episodes 01-04, 08,
                  11-13 quoted},
  url          = {https://swcarpentry.github.io/r-novice-gapminder/},
  urldate      = {2026-10-02}
}

@misc{dc_spreadsheets,
  title        = {Data Organization in Spreadsheets for Ecologists},
  author       = {{The Carpentries}},
  howpublished = {Data Carpentry lesson (spreadsheet-ecology-lesson)},
  year         = {2026},
  note         = {Episode pages last updated between 8 March 2024 and 4 August 2026.
                  Instructional material licensed CC BY 4.0 (the lesson's LICENSE page).
                  Episodes 01-05 quoted},
  url          = {https://datacarpentry.github.io/spreadsheet-ecology-lesson/},
  urldate      = {2026-10-02}
}

@misc{tidyverse_style,
  title        = {The tidyverse style guide},
  author       = {{The tidyverse team}},
  howpublished = {Online book},
  note         = {Undated. Licensed CC BY-SA 3.0 Unported per the LICENSE file of its source
                  repository, github.com/tidyverse/style. Chapters Files, Syntax and Pipes quoted},
  url          = {https://style.tidyverse.org/},
  urldate      = {2026-10-02}
}
```

## 3. `sources/SOURCES.md`, new section

```markdown
## S52-R1 (R, reproducibility, data management): group a, textbooks, manuals, guides (intake 2 Oct 2026)

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `r4ds_2e.txt` | Wickham, Çetinkaya-Rundel and Grolemund, *R for Data Science* 2e, online edition (r4ds.hadley.nz). CC BY-NC-ND 3.0: **no derivatives, held for quote-checking only**. **Excerpts** (46 whole sections) | 40,938 | 5.2 three tidy rules ("Each variable is a column; each column is a variable", observation/row, "Each value is a cell; each cell is a single value"); 6.1 scripts and file-naming principles; 6.2.1 "your source of truth should be the R scripts", restart and re-run; 6.2.2 working directory, setwd() not recommended; 6.2.4 "you should only ever use relative paths not absolute paths"; 7.2-7.3 read_csv, na =, col_types, problems(); 18.2 explicit missing values and fixed-value codes; 20.2 read_excel, sheets, ranges, 20.2.6 data types; 3.2-3.6 filter/arrange/mutate/select/rename, the pipe (R 4.1.0), group_by, summarize, .by, n() and sample size; 12.2.2 NA comparisons, 12.5 if_else/case_when; 16 factors; 17.2.2 the y/m/d naming rule for lubridate parsers (its example calls were dropped by the extractor), 17.4 durations; 19.2 keys, 19.3 left_join, anti_join, 19.4.1 duplicate keys; 1.2-1.7 ggplot, aes, histogram, boxplot, facets, ggsave. Printed outputs come from newer package versions than this book's |
| `r_intro_manual.txt` | R Core Team, *An Introduction to R*, manual for R 4.6.1 (2026-06-24). Verbatim-copy permission. **Excerpts** | 5,144 | help(solve), ?solve, help.start(), ??; case sensitivity, allowed names, comments with #; source(); objects(), the workspace and .RData; x <- c(10.4, 5.6, 3.1, 6.4, 21.7), element-by-element arithmetic and recycling; mean(x) as sum(x)/length(x); logical vectors; NA "not available", "any operation on an NA becomes an NA", is.na(), x == NA undecidable, NaN; x[!is.na(x)]; x[is.na(x)] <- 0; atomic modes and coercion with as.character()/as.integer(); "All R functions and datasets are stored in packages", library(), install.packages(), CRAN, ::; Rscript foo.R. Contains no pipe |
| `r_lang_def.txt` | R Core Team, *R Language Definition*, manual for R 4.6.0 (2026-04-24). Verbatim-copy permission. **Excerpts** | 1,057 | Objects referred to through symbols; "R has six basic ('atomic') vector types: logical, integer, real, complex, character ... and raw"; NA "Missing values in the statistical sense", default NA type is logical, NA calculations generally return NA, 'FALSE & NA' is FALSE, testing with is.na; operator precedence list including \|> |
| `swc_r_gapminder.txt` | The Carpentries, Software Carpentry *R for Reproducible Scientific Analysis*, pages last updated 1 Sep 2026. CC BY 4.0. **Excerpts** (episodes 01-04, 08, 11-13) | 14,001 | Ep. 01 scripts vs console, R as a calculator and order of operations, comparisons, assignment with <-, vectorization, ls()/rm(), install.packages() and library(); ep. 02 "treat your data as 'read-only'", generated output "disposable", Good Enough Practices layout, working directory; ep. 03 ?function, help files, vignettes; ep. 04 data types, typeof(), type coercion and the type hierarchy, R 4.0.0 no longer makes factors from text; ep. 08 grammar of graphics (data, mapping aesthetics, layers), aesthetic value vs mapping, facets, ggsave; ep. 11 write.csv; ep. 12 select, filter, group_by, summarize, count, n(), mutate; ep. 13 long vs wide, pivot_longer |
| `dc_spreadsheets.txt` | The Carpentries, Data Carpentry *Data Organization in Spreadsheets for Ecologists*, episodes updated 2024-2026. CC BY 4.0. **Excerpts** (episodes 01-05) | 7,521 | "columns = variables, rows = observations, cells = data (values)"; the list of common spreadsheet errors (multiple tables and tabs, zeros, problematic null values, formatting as information, units in cells, more than one piece of information in a cell, field names, special characters, metadata); Excel turns gene names such as MAR1, DEC1, OCT4 into dates; dates stored as day counts from 31 Dec 1899 (2 Jul 2014 = 41822), the 1904 system; recommends separate YEAR, MONTH, DAY columns; data validation; export to CSV |
| `tidyverse_style.txt` | The tidyverse team, *The tidyverse style guide* (undated). CC BY-SA 3.0 per the repository LICENSE. **Excerpts** | 3,127 | Derived from Google's R style guide, styler and lintr; file names machine and human readable; object names lowercase with underscores (snake_case); spacing after commas and around infix operators; "Use <-, not =, for assignment"; pipes: space before \|>, one step per line |
```
