# Source intake log · S52-R1 · group c (local documentation, changelogs, dataset)

One pass, 2026-10-02, against `INTAKE-BRIEF.md` group c and the last "To obtain" line of `READY.md`
(installed package documentation), its "Optional" changelog line and the dataset table (candidates A and B).

**Method.** (i) Help pages and vignettes were **not fetched from the web**: they were rendered from the packages
installed in this sandbox by `build-c/render.R` (R 4.3.3, UTF-8 locale, `options(useFancyQuotes = FALSE)`,
`tools::Rd2txt(..., underline_titles = FALSE, width = 80)`; vignettes from the installed HTML by xml2, block by
block). The renders, each package's DESCRIPTION (copied byte for byte), a topic-to-Rd map and the
`packageVersion()` record are in `intake/raw/rdocs_s52r1_*`. (ii) The four changelog pages and the CRAN, NHANES
and NCHS pages were read with `mcp__TinyFish__fetch_content` (markdown, ttl 0); the harness saved the JSON,
which was decoded unchanged into `intake/raw/` (one `.txt` per URL plus `.meta.json`). (iii) The dataset was
copied and described by `build-c/penguins.R`. Every passage was then cut by `build-c/build.py` (`raw[i:j]`
between literal anchors, offsets in `build-c/manifest.json`) and re-checked by `build-c/verify.py` as a
whitespace-normalised substring of its raw file; header quotes are cut and checked the same way. No WebFetch,
curl, wget or Python HTTP. `build-c/fragment.py` writes `fragment-c.md`.

**Choice stated (brief item i):** one file per package, citekeys `rdocs_s52r1_<package>` (13 files: base, utils,
stats, dplyr, tidyr, readr, readxl, haven, ggplot2, forcats, lubridate, stringr, here), so each file carries its
own package's licence line. `sessionInfo` and `Rscript` are in utils, so utils has its own file; stats was added
for four [extra] pages.

**Verbatim check: 98 of 98 passages; 51 of 51 header quotes.** CSV MD5 rechecked against the installed file.

| Source | URL fetched / how obtained | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| base 4.3.3 help: mean, NA (+ is.na), c, stopifnot, source, Random (set.seed); [extra] Round, library; DESCRIPTION | local render, `rhelp://base@4.3.3/...` | 9 | 9/9 | DESCRIPTION "License: Part of R 4.3.3"; `R --version`: "GNU General Public License versions 2 or 3" | `rdocs_s52r1_base` |
| utils 4.3.3 help: sessionInfo, Rscript; [extra] packageDescription (packageVersion), install.packages; DESCRIPTION | local render | 5 | 5/5 | "License: Part of R 4.3.3" | `rdocs_s52r1_utils` |
| stats 4.3.3 help, all [extra]: median, sd, quantile, IQR; DESCRIPTION | local render | 5 | 5/5 | "License: Part of R 4.3.3" | `rdocs_s52r1_stats` |
| dplyr 1.1.4 help: filter, select, mutate, summarise, group_by, arrange, count, if_else, case_when, mutate-joins, filter-joins; [extra] across, n_distinct, rename, desc, context (n); vignettes "dplyr" (to before "Patterns of operations"), "two-table" (to before "Set operations"); DESCRIPTION | local render | 19 | 19/19 | "License: MIT + file LICENSE" | `rdocs_s52r1_dplyr` |
| tidyr 1.3.1 help: pivot_longer, pivot_wider, drop_na; vignette "tidy-data" (2 blocks), "pivot" (2 blocks); DESCRIPTION | local render | 8 | 8/8 | "License: MIT + file LICENSE" | `rdocs_s52r1_tidyr` |
| readr 2.1.5 help: read_delim (read_csv), problems; vignette "readr" whole; DESCRIPTION | local render | 4 | 4/4 | "License: MIT + file LICENSE" | `rdocs_s52r1_readr` |
| readxl 1.4.3 help: read_excel; DESCRIPTION | local render | 2 | 2/2 | "License: MIT + file LICENSE" | `rdocs_s52r1_readxl` |
| haven 2.5.4 help: read_spss (read_sav), read_xpt; DESCRIPTION | local render | 3 | 3/3 | "License: MIT + file LICENSE" | `rdocs_s52r1_haven` |
| ggplot2 3.4.4 help: ggplot, aes, geom_histogram, geom_boxplot, ggsave, facet_wrap; DESCRIPTION | local render | 7 | 7/7 | "License: MIT + file LICENSE" | `rdocs_s52r1_ggplot2` |
| forcats 1.0.0 help: fct_recode, fct_relevel, fct_inorder (fct_infreq); vignette "forcats" whole; DESCRIPTION | local render | 5 | 5/5 | "License: MIT + file LICENSE" | `rdocs_s52r1_forcats` |
| lubridate 1.9.3 help: ymd (ymd, dmy, mdy); DESCRIPTION | local render | 2 | 2/2 | "License: GPL (>= 2)" | `rdocs_s52r1_lubridate` |
| stringr 1.5.1 help: str_trim, case (str_to_lower); DESCRIPTION | local render | 3 | 3/3 | "License: MIT + file LICENSE" | `rdocs_s52r1_stringr` |
| here 1.0.1 help: here; DESCRIPTION | local render | 2 | 2/2 | "License: MIT + file LICENSE" | `rdocs_s52r1_here` |
| Changelogs after the installed versions: ggplot2 4.0.3 whole, 4.0.1 (1 bullet), 4.0.0 (breaking + lifecycle, 1 bullet), 3.5.0 (summary + breaking, 3 bullets); dplyr 1.2.0 (8 cuts); readr 2.2.0 and 2.1.6 whole; tidyr 1.3.2 whole | https://ggplot2.tidyverse.org/news/, https://dplyr.tidyverse.org/news/, https://readr.tidyverse.org/news/, https://tidyr.tidyverse.org/news/ | 19 | 19/19 | none on the pages; packages MIT per DESCRIPTION; pages record the MIT relicensing (quoted in header) | `tidyverse_news_s52r1` |
| palmerpenguins 0.1.1: penguins_raw help page, DESCRIPTION, citation(), CRAN page, first 3 lines of the CSV; header holds the script-recorded facts | local render + https://cran.r-project.org/package=palmerpenguins (→ /web/packages/palmerpenguins/index.html) | 5 | 5/5 | DESCRIPTION "License: CC0"; CRAN page "License: CC0" | `horst_2020_palmerpenguins` |

Total: 15 source files, 98 passages, 65,000 words (the help pages are held whole, examples included).

## The dataset (iii)

`sources/data/penguins_raw.csv` created (new folder: `sources/` had no data folder or data convention; the
brief's path was used). Copied byte for byte from
`system.file("extdata", "penguins_raw.csv", package = "palmerpenguins")`. By script (`penguins.R`, output in
`raw/horst_2020_palmerpenguins-facts.txt`): **53,098 bytes; MD5 049da101568e078f9845c8b366481810** (copy =
installed; Task 1 found the same MD5 on GitHub); 345 text lines; **344 rows, 17 columns** (`read_csv`, readr
2.1.5, default `na = c("", "NA")`); missing per column: Culmen Length (mm) 2, Culmen Depth (mm) 2, Flipper
Length (mm) 2, Body Mass (g) 2, Sex 11, Delta 15 N (o/oo) 14, Delta 13 C (o/oo) 13, Comments 290, all others 0;
336 missing cells; 34 complete rows; `Date Egg` guessed as Date, 2007-11-09 to 2009-12-01; species 152 / 68 /
124; Sex FEMALE 165, MALE 168. These agree with READY.md's Task 1 figures. Licence CC0 on both the DESCRIPTION
and the CRAN page (version 0.1.1, published 2022-08-15). Discrepancy recorded in the header: the package's own
`citation()` says "R package version 0.1.0" and year 2020; the bib entry uses 2020 (the citation's year) and
version 0.1.1 (installed).

## NHANES (tried once, as the brief says): not obtained

Read via TinyFish, 2026-10-02, saved as `raw/nhanes_s52r1-*`; **not filed as a source** (the brief asks only
for a record, and the data files themselves cannot be reached: the proxy refuses wwwn.cdc.gov to curl, per
READY.md).

| Page | What it lists (as extracted) |
| --- | --- |
| https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Examination&Cycle=2021-2023 | "Body Measures" · "BMX\_L Doc" · "BMX\_L Data [XPT - 1.5 MB]" · "September 2024" |
| https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Demographics&Cycle=2021-2023 | "Demographic Variables and Sample Weights" · "DEMO\_L Doc" · "DEMO\_L Data [XPT - 2.5 MB]" · "September 2024" |
| https://www.cdc.gov/nchs/policy/data-user-agreement.html | dated "September 17, 2024"; users will "1. Use the data in this dataset for statistical reporting and analysis only. 2. Make no attempt to learn the identity of any person or establishment included in these data. 3. Not link this dataset with individually identifiable data from other NCHS or non-NCHS datasets. 4. Not engage in any efforts to assess disclosure methodologies ..."; no copyright or licence statement on the page |

**What Harsh would download from a browser, if he chooses dataset A** (four files, from the page links):
- https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.xpt (listed 1.5 MB)
- https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.htm (its documentation / codebook)
- https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt (listed 2.5 MB)
- https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.htm

then put them in `sources/data/` and say so; the intake would then record MD5s, counts and the two codebooks.

## Findings the conductor should carry

1. **dplyr's newest version is 1.2.0 on the page fetched today, not 1.2.1** as READY.md and INVENTORY.md
   say. Change those lines (or re-check) before C06/C21 print "dplyr 1.2.1".
2. **The tidyr page has no "tidyr 1.3.1" heading** (it goes 1.3.2, then 1.3.0) although 1.3.1 is installed.
   readr 2.2.0 has no CRAN release date on the page.
3. Changes a reader on current versions may meet (each held verbatim in `tidyverse_news_s52r1`): ggplot2 4.0.0
   changed the default histogram bin `boundary` ("This may affect plots that use default binning"), replaced S3
   with S7, turned pre-3.0.0 deprecations into errors, deprecated `fatten` in `geom_boxplot()`, and tries a
   variable's label attribute as the default axis label (relevant to haven-read files); 3.5.0 changed the
   legend key look under the default theme, superseded `coord_flip()`, renamed `trans` to `transform`, and
   `ggsave()` no longer creates directories unless `create.dir` is set; 4.0.3 added `quantile.type`
   (default 7) to `geom_boxplot()`. dplyr 1.2.0 adds `filter_out()` and the `case_when()` family with
   `.unmatched`, makes `.by` stable, makes multi-row `summarise()` defunct (use `reframe()`), soft-deprecates
   `case_match()`, deprecates `if_else(size =)`, requires R >= 4.1.0. readr 2.2.0 warns when literal data is
   passed to `read_csv()` without `I()`. tidyr 1.3.2 requires R >= 4.1.0. None was tested: the sandbox cannot
   install the new versions.
4. "MIT + file LICENSE": the LICENSE files are **not present in the installed packages**, so the copyright
   year and holder lines were not read; the headers say so.
5. Help pages are rendered with straight quotes (`options(useFancyQuotes = FALSE)`); a drafter quoting them
   should copy from the source file, not from an RStudio help pane, which shows curly quotes.
6. Render must run in a UTF-8 locale (the sandbox default is POSIX, which escaped characters as `<U+2019>`);
   `render.R` says so. lubridate's installed vignette has no HTML, so none is held.
7. Extras beyond the brief's list, marked [extra] in the files: base round, library; utils packageVersion,
   install.packages; stats median, sd, quantile, IQR; dplyr across, n_distinct, rename, desc, n. Not held:
   tidyselect helpers (`starts_with()`), `glimpse()`, `rename_with()`, `read_dta()`.

Nothing in `sources/INDEX.yml`, `check/references/library.bib` or `sources/SOURCES.md` was edited. Nothing was
committed.
