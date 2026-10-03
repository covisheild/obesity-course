"""Write books/S52-R1/intake/fragment-c.md (INDEX.yml, library.bib and SOURCES.md entries for group c)."""
import json, os, re

ROOT = '/home/claude/work/obesity-course'
HERE = os.path.dirname(os.path.abspath(__file__))
meta = json.load(open(os.path.join(HERE, 'pkgmeta.json'), encoding='utf-8'))
TEX = {'ç': r'{\c{c}}', 'ü': r'{\"u}', 'é': r"{\'e}"}
tex = lambda s: ''.join(TEX.get(c, c) for c in s)
words = lambda k: f"{len(open(os.path.join(ROOT, 'sources', k + '.txt'), encoding='utf-8').read().split()):,}"

topics = {
    'base': ('mean; NA and is.na; c; stopifnot; source; set.seed (Rd "Random"); extras round, library',
             '`mean()` and `na.rm`; `NA` "a logical constant of length 1 which contains a missing value indicator" and `is.na()`; `c()` and the hierarchy NULL < raw < logical < integer < ...; `stopifnot()` stops when an expression is not all TRUE; `source()` reads, parses and evaluates the expressions of a file in turn; `set.seed()` and the random number generator; `round()`; `library()`'),
    'utils': ('sessionInfo; Rscript; extras packageVersion (Rd "packageDescription"), install.packages',
              '`sessionInfo()` as the record of R version, platform and attached packages; `Rscript` the scripting front-end, "Options --no-echo --no-restore are always supplied"; `packageVersion()`; `install.packages()` from repositories'),
    'stats': ('extras median, sd, quantile (nine types; default 7), IQR',
              '`median()`, `sd()` ("uses denominator n - 1"), `quantile()` with its nine types (default 7), `IQR()`'),
    'dplyr': ('filter, select, mutate, summarise, group_by, arrange, count, if_else, case_when, left_join (Rd "mutate-joins"), anti_join (Rd "filter-joins"); extras across, n_distinct, rename, desc, n (Rd "context"); vignettes "dplyr" (to before "Patterns of operations") and "two-table" (to before "Set operations")',
              '`filter()` drops rows whose condition is NA; `select()`, `mutate()` (`.keep`, `.before`), `summarise()` and `.groups`, `group_by()`/`ungroup()`, `.by`, `arrange()` puts NA last, `count()`, `if_else()` with `missing`, `case_when()` and `.default`, joins and `relationship`, `anti_join()`; vignette: verbs, the pipe, joins and duplicate keys'),
    'tidyr': ('pivot_longer, pivot_wider, drop_na; vignettes "tidy-data" (definitions and the first two messy cases) and "pivot" (introduction, longer, first case; wider, first case)',
              '`pivot_longer()`/`pivot_wider()` arguments; `drop_na()`; "Tidy data" vignette: the three rules ("Each variable is a column; each column is a variable" etc.), values in column names, multiple variables in one column; "Pivoting" vignette examples with printed output'),
    'readr': ('read_csv (Rd "read_delim"), problems; vignette "readr" whole',
              '`read_csv()` arguments incl. `na = c("", "NA")`, `col_types`, `show_col_types`; `problems()`; vignette: parsers, column specification and guessing, overriding defaults, available col_* specifications'),
    'readxl': ('read_excel', '`read_excel()` with `sheet`, `range`, `na`, `col_types`, `skip`'),
    'haven': ('read_sav (Rd "read_spss"), read_xpt', '`read_sav()`/`read_spss()` and `user_na`; `read_xpt()` for SAS transport files'),
    'ggplot2': ('ggplot, aes, geom_histogram (Rd "geom_histogram"), geom_boxplot, ggsave, facet_wrap',
                '`ggplot()`, `aes()` mappings, `geom_histogram()` (stat_bin "uses 30 bins; this is not a good default"), `geom_boxplot()` (hinges, whiskers 1.5 x IQR), `ggsave()` (defaults to the last plot, size and units), `facet_wrap()`'),
    'forcats': ('fct_recode, fct_relevel, fct_infreq (Rd "fct_inorder"); vignette "forcats" whole',
                '`fct_recode()` "the name gives the new level, and the value gives the old level"; `fct_relevel()`; `fct_infreq()` order by frequency; vignette with printed output'),
    'lubridate': ('ymd, dmy, mdy (one Rd, "ymd")', '`ymd()`, `dmy()`, `mdy()`; Value: Date when tz is NULL (the default); heterogeneous formats guessed from a subset, "All formats failed to parse" error; `truncated`'),
    'stringr': ('str_trim, str_to_lower (Rd "case")', '`str_trim()` removes whitespace from start and end; `str_to_lower()`'),
    'here': ('here', '`here()` builds paths from the project root'),
}
PK = list(topics)

idx, bib, rows = [], [], []
for p in PK:
    k = f'rdocs_s52r1_{p}'
    if p in meta:
        m = meta[p]; v = m['version']
        aut = m['aut'] if isinstance(m['aut'], list) else [m['aut']]
        lic = m['license']
        author = ' and '.join(tex(a) for a in aut)
        title = f"{p}: {m['title']}, version {v}: help pages"
        year = m['date'][:4]
        url = f'https://CRAN.R-project.org/package={p}'
        lic_note = f'Licence as stated in the package DESCRIPTION: {lic}'
        hp = 'R package, CRAN'
    else:
        v = '4.3.3'; author = '{R Core Team}'
        title = f"R {v}, package {p}: help pages"
        year = '2024'; url = 'https://www.R-project.org/'
        lic_note = 'DESCRIPTION: Part of R 4.3.3; R is distributed under the GNU General Public License versions 2 or 3'
        hp = 'R Foundation for Statistical Computing'
    what = f'{p} {v} help pages as installed in the book\'s R 4.3.3 sandbox, rendered by tools::Rd2txt, each whole: {topics[p][0]}; DESCRIPTION whole. Version-matched to the book\'s outputs, not to the current release'
    idx.append(f'  {k}:\n    file: {k}.txt\n    what: >-\n      ' + '\n      '.join(x.rstrip() for x in re.findall(r'.{1,104}(?:\s|$)', what)).rstrip())
    bib.append(f"""@misc{{{k},
  title        = {{{tex(title)}}},
  author       = {{{author}}},
  year         = {{{year}}},
  note         = {{Documentation of the version used for every output in this book ({p} {v}, R 4.3.3),
                  read with help() in the installed package on 2026-10-02; newer versions exist and their
                  help pages may differ. {lic_note}}},
  howpublished = {{{hp}}},
  url          = {{{url}}},
  urldate      = {{2026-10-02}}
}}""")
    rows.append(f'| `{k}.txt` | {p} {v} help pages, version-matched, rendered from the installed package in the R 4.3.3 sandbox (tools::Rd2txt). Licence per DESCRIPTION: {"Part of R 4.3.3 (GPL-2 | GPL-3)".replace("|", "or") if p not in meta else meta[p]["license"]}. **Excerpts: listed pages whole** | {words(k)} | {topics[p][1]} |')

# changelogs
idx.append("""  tidyverse_news_s52r1:
    file: tidyverse_news_s52r1.txt
    what: >-
      Changelog pages of ggplot2, dplyr, readr and tidyr (tidyverse.org/news), fetched 2026-10-02. Only entries
      for versions after the book's installed ones that a beginner's code could meet: ggplot2 4.0.3 whole, the
      4.0.1 stat_bin(boundary) fix, 4.0.0 breaking and lifecycle changes plus the label-attribute bullet, 3.5.0
      summary and breaking changes plus boxplot outliers, facet axes and ggsave create.dir; dplyr 1.2.0
      filter_out, case_when family and .unmatched, lifecycle changes, summarise multi-row defunct, .groups
      message, base pipe, R >= 4.1.0; readr 2.2.0 and 2.1.6 whole; tidyr 1.3.2 whole""")
bib.append("""@misc{tidyverse_news_s52r1,
  title        = {Changelogs of ggplot2, dplyr, readr and tidyr: entries after ggplot2 3.4.4, dplyr 1.1.4,
                  readr 2.1.5 and tidyr 1.3.1},
  author       = {{Tidyverse team}},
  year         = {2026},
  note         = {Package NEWS pages, newest entries on 2026-10-02: ggplot2 4.0.3 (2026-04-22), dplyr 1.2.0
                  (2026-02-03), readr 2.2.0, tidyr 1.3.2 (2025-12-19). Pages also at
                  https://dplyr.tidyverse.org/news/, https://readr.tidyverse.org/news/ and
                  https://tidyr.tidyverse.org/news/. No licence stated on the pages; the packages are MIT
                  licensed per their DESCRIPTION files},
  howpublished = {tidyverse.org},
  url          = {https://ggplot2.tidyverse.org/news/},
  urldate      = {2026-10-02}
}""")
rows.append(f'| `tidyverse_news_s52r1.txt` | Changelog (NEWS) pages of ggplot2, dplyr, readr, tidyr, TinyFish markdown, 2026-10-02. No licence on the pages (packages MIT per DESCRIPTION). **Excerpts: entries after the installed versions only** | {words("tidyverse_news_s52r1")} | ggplot2 4.0.0 "In binning stats, the default boundary is now chosen to better adhere to the nbin argument. This may affect plots that use default binning"; S7 replaces S3; pre-3.0.0 deprecations now error; geom_boxplot fatten deprecated, quantile.type (4.0.3, default 7); facet_wrap dir/as.table; label attribute as default label; 3.5.0 legend key look changes with theme_gray, coord_flip superseded, trans renamed transform, boxplot outliers argument, ggsave create.dir; dplyr 1.2.0 filter_out(), case_when family and .unmatched, .by stable, case_match soft-deprecated, if_else size deprecated, summarise more or less than 1 row per group defunct (use reframe), R >= 4.1.0; readr 2.2.0 literal data must be wrapped in I() (deprecation warning), quoted_na errors; tidyr 1.3.2 R >= 4.1.0, pivot_wider internal error fixed |')

# dataset
idx.append("""  horst_2020_palmerpenguins:
    file: horst_2020_palmerpenguins.txt
    what: >-
      palmerpenguins 0.1.1 (CC0): penguins_raw help page, DESCRIPTION, citation(), CRAN page (2026-10-02),
      the first three lines of the CSV, and in the header the script-recorded facts of the book's dataset
      sources/data/penguins_raw.csv (53,098 bytes, MD5 049da101568e078f9845c8b366481810, 344 rows, 17
      columns, missing-value count per column). The CSV itself is held byte for byte at data/penguins_raw.csv""")
bib.append("""@misc{horst_2020_palmerpenguins,
  title        = {palmerpenguins: Palmer Archipelago (Antarctica) Penguin Data},
  author       = {Horst, Allison Marie and Hill, Alison Presmanes and Gorman, Kristen B},
  year         = {2020},
  note         = {R package version 0.1.1 (CRAN, published 2022-08-15); file penguins_raw.csv in the
                  package's extdata folder. doi:10.5281/zenodo.3960218. License: CC0 (DESCRIPTION and CRAN
                  page). Data from Palmer Station Antarctica LTER and K. Gorman; first published in Gorman,
                  Williams and Fraser, PLoS ONE 2014;9(3):e90081},
  howpublished = {CRAN},
  url          = {https://allisonhorst.github.io/palmerpenguins/},
  urldate      = {2026-10-02}
}""")
rows.append(f'| `horst_2020_palmerpenguins.txt` | palmerpenguins 0.1.1 (Horst, Hill and Gorman), documentation of `penguins_raw`, the book\'s dataset; DESCRIPTION, citation(), CRAN page via TinyFish. CC0. **Whole as listed** | {words("horst_2020_palmerpenguins")} | 344 rows, 17 columns (read_csv, readr 2.1.5); missing: Culmen Length, Culmen Depth, Flipper Length, Body Mass 2 each, Sex 11, Delta 15 N 14, Delta 13 C 13, Comments 290; 34 complete rows; Date Egg read as Date, 2007-11-09 to 2009-12-01; species counts 152/68/124; help page: 17 variables with units, sources (EDI 2020 data packages; Gorman et al. 2014 PLoS ONE); License: CC0 |')
rows.append('| `data/penguins_raw.csv` | The raw data file itself, copied byte for byte from the installed palmerpenguins 0.1.1 (`system.file("extdata", "penguins_raw.csv", package = "palmerpenguins")`), 2026-10-02. CC0. Described in `horst_2020_palmerpenguins.txt`; cite that key | 53,098 bytes | MD5 049da101568e078f9845c8b366481810; 345 lines (header + 344 rows) |')

bibtext = '\n\n'.join(bib)
assert bibtext.count('{') == bibtext.count('}'), 'unbalanced braces'
for e in bib:
    assert e.count('{') == e.count('}'), e[:40]
    assert 'sources/' not in e and 'books/' not in e and 'intake' not in e, e[:40]

out = f"""# Intake fragment, group c (local documentation, changelogs, dataset) · S52-R1

For the main thread to merge into `sources/INDEX.yml`, `check/references/library.bib` and `sources/SOURCES.md`
in one commit. Fifteen new citekeys (13 `rdocs_s52r1_<package>`, one file per package; `tidyverse_news_s52r1`;
`horst_2020_palmerpenguins`), plus the data file `sources/data/penguins_raw.csv` (new folder; `sources/` had
no data convention before). None collides with INDEX.yml or library.bib, locally or on `origin/main`
(grepped 2026-10-02 after `git fetch origin`). The 15 `sources/*.txt` files are written;
`books/S52-R1/intake/build-c/render.R` and `penguins.R` (R) make the raw renders, `build.py` regenerates the
source files and `verify.py` rechecks them (98/98 passages, 51/51 header quotes). This file was generated by
`build-c/fragment.py`; every `.bib` entry's braces were checked by script.

## INDEX.yml (`files:` entries)

```yaml
{chr(10).join(idx)}
```

## library.bib entries

```bibtex
{bibtext}
```

## SOURCES.md rows

```markdown
{chr(10).join(rows)}
```

Paragraph for SOURCES.md, below the table:

```markdown
**S52-R1 intake, group c (local documentation, changelogs, dataset), 2026-10-02.** Thirteen `rdocs_s52r1_*`
files hold the help pages of the exact package versions the book's outputs are made with (R 4.3.3, dplyr
1.1.4, tidyr 1.3.1, readr 2.1.5, readxl 1.4.3, haven 2.5.4, ggplot2 3.4.4, forcats 1.0.0, lubridate 1.9.3,
stringr 1.5.1, here 1.0.1), rendered by `tools::Rd2txt()` from the installed packages, not fetched from the
web; block headings carry `rhelp://` and `rvignette://` locators instead of URLs. `tidyverse_news_s52r1`
holds the changelog entries for later versions a beginner could meet. `data/penguins_raw.csv` is the book's
dataset (CC0), described in `horst_2020_palmerpenguins.txt`. Verbatim check 98 of 98. Log:
`books/S52-R1/intake/log-c.md`.
```
"""
open(os.path.join(ROOT, 'books/S52-R1/intake/fragment-c.md'), 'w', encoding='utf-8').write(out)
print('ok', len(idx), len(bib), len(rows))
