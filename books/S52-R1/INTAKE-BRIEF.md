# Source intake brief · S52-R1 (for intake subagents)

You file sources for S52-R1 to the intake checklist in `PIPELINE.md` ("Before anything: the source gate",
"The intake checklist") and `claude.md` §7b and §8 (read those three sections only). Model the method on
`books/S57-R1/INTAKE.md` (read its first 25 lines) and `books/S57-R1/INTAKE-BRIEF.md`. Repo root:
`/home/claude/work/obesity-course`, branch `book/S52-R1`. Use ABSOLUTE paths. No `rm` in the repo from
scratch scripts. Never push. Do not commit (the conductor commits).

Fetch with `mcp__TinyFish__fetch_content` (load it with ToolSearch "select:mcp__TinyFish__fetch_content"); PubMed
tools (`mcp__PubMed__*`) may confirm identifiers and give PMC full text. TinyFish can return a PDF's text layer —
try it before declaring a PDF unobtainable. PMC open-access XML is also at
`https://pmc-oa-opendata.s3.amazonaws.com/PMC<id>.1/PMC<id>.1.xml`. Never use curl/wget/Python HTTP to fetch
anything the tools refuse (the proxy blocks several hosts on purpose; if a host is refused, record "not
obtained" and why; do not look for a way round). Never store WebFetch output. Never paraphrase into a source
file: every stored passage is cut by script from the saved raw fetch text (`raw[i:j]`) and re-checked as a
whitespace-normalised substring of it. Wikipedia and its kind are leads, never sources. Do not use India Code or
sansad.in (not needed here). Read a site's terms before fetching if in doubt.

Read `books/S52-R1/READY.md` (the "To obtain" table has the proposed citekey, URL, licence lead and the concepts
each source serves) and `books/S52-R1/INVENTORY.md` (what each concept must cover) for YOUR group's sources only.

For each source in your group:
1. Fetch; save the raw result under `books/S52-R1/intake/raw/<citekey>-*.txt` (your own file names only).
2. Write `sources/<citekey>.txt`: an honest header (what it is, URL fetched, date 2026-10-02 or later, licence
   quoted from the work's own page or the article's own header, exactly which parts are held, every omission
   marked `[...]` with a `[NOTE]`), then the passages. Keep the passages the inventory's concepts need: results
   with their numbers, definitions, rules, key code and its stated output. Whole relevant sections are better than
   fragments; skip reference lists. Confirm author lists, volume and page ranges from the work's own header and put
   them in the log (READY.md's bibliographic details for some works were written from memory and must be
   confirmed).
3. Citekey: new and unique, as proposed in READY.md. `grep` it in `sources/INDEX.yml` and
   `check/references/library.bib` first (GitHub's main may have moved: also run
   `git -C /home/claude/work/obesity-course fetch origin` and grep `origin/main:` copies of those two files).
   Another book chat (S47-R1, policy craft) is adding sources on an unpublished branch: prefer specific keys.
4. Do NOT edit `sources/INDEX.yml`, `check/references/library.bib` or `sources/SOURCES.md` (three intake agents run
   at once). Write your entries into your own fragment file
   `books/S52-R1/intake/fragment-<group>.md` with three fenced blocks: the INDEX.yml `files:` entries (same shape as
   existing ones, `what:` naming exactly what is held), the `.bib` entries (same shape as existing; `note` gives
   licence and identifiers; NO repository path anywhere in the entry; make sure every entry's braces balance), and
   the SOURCES.md lines (same format as the existing table).
5. Verbatim check by script for every passage; record passages and pass counts.
6. Write `books/S52-R1/intake/log-<group>.md`: one table row per source (source, URL, passages, check n/n, licence
   as stated, citekey) and, for anything NOT obtained, why and the exact file/URL Harsh would download from a
   browser. If a source is unobtainable but an open substitute carries the same claim, you may file the substitute
   and say so.

Reply at most 150 words: obtained n/m, citekeys, what needs Harsh, your log path.

## Groups

**Group a: textbooks, manuals, guides** (citekeys `r4ds_2e`, `r_intro_manual`, `r_lang_def` optional, `swc_r_gapminder`,
`dc_spreadsheets` optional, `tidyverse_style`). R4DS 2e is CC BY-NC-ND 3.0 US (no derivatives): hold passages for
quote-checking only, never adapt; say so in the header. Hold, per chapter, the passages that state a rule,
definition or procedure the inventory uses (e.g. ch. 5 the three tidy rules; ch. 6 scripts, projects, "source of
truth", relative and absolute paths; ch. 7 import; ch. 18 missing values; ch. 20 spreadsheets/data types), plus
code with its printed output only if the page prints it. For the R manuals take: assignment, vectors and
types, missing values (NA), getting help, packages, and the pipe if present; note the manual's header version
(R 4.6.1) differs from the book's 4.3.3.

**Group b: papers and statements** (citekeys `wickham_2014_tidy`, `broman_woo_2018`, `ziemann_2016`, `herndon_2014`,
`phe_2020_delayed`, `trisovic_2022`, `peng_2011`, `sandve_2013`, `wilson_2017`). Held for C01, C08, C09, C10, C15,
C19, C20, C21, C22. Broman & Woo and Herndon et al. could not be opened at Task 1 (bot_blocked / unreachable):
try the other routes (PeerJ preprint PDF text layer via TinyFish, Europe PMC, the authors' own pages such as
kbroman.org, PERI page and the paper's Cambridge Journal of Economics PDF as hosted on an author or institutional
page). If neither works, mark "not obtained", say which file Harsh must download, and file only what you could
open (the abstract), labelled as abstract only. For the PHE statement hold the whole page; it does not name Excel
and no file may say it does.

**Group c: local documentation, changelogs, dataset** (no web fetch for the first two items). (i) Version-matched
help pages from the installed packages in this sandbox (R 4.3.3; dplyr 1.1.4, tidyr 1.3.1, readr 2.1.5, readxl
1.4.3, haven 2.5.4, ggplot2 3.4.4, forcats 1.0.0, lubridate 1.9.3, stringr 1.5.1, here 1.0.1, base R): render each
needed Rd help page to text with `tools::Rd2txt()` (and key vignettes' text) via `Rscript`, saving the raw render
under `intake/raw/`; the stored passages are cut from it. Needed functions: base `mean`, `NA`, `c`, `is.na`,
`stopifnot`, `sessionInfo`, `source`, `Rscript`'s documentation (`?Rscript`), `set.seed`; dplyr `filter`, `select`,
`mutate`, `summarise`, `group_by`, `arrange`, `count`, `if_else`, `case_when`, `left_join`, `anti_join`; tidyr
`pivot_longer`, `pivot_wider`, `drop_na`; readr `read_csv`, `problems`; readxl `read_excel`; haven `read_sav`,
`read_xpt`; ggplot2 `ggplot`, `aes`, `geom_histogram`, `geom_boxplot`, `ggsave`, `facet_wrap`; forcats `fct_recode`,
`fct_relevel`, `fct_infreq`; lubridate `ymd`, `dmy`, `mdy`; stringr `str_trim`, `str_to_lower`; here `here`. Header
gives each package's licence from its DESCRIPTION file and the version read with `packageVersion()`. Citekey
`rdocs_s52r1_<package>` (one file per package, or one file `rdocs_s52r1` with one block per function: your choice,
stated in the log). (ii) Changelogs for versions AFTER the installed ones, from the NEWS pages named in READY.md
"Optional" (ggplot2 4.0.x, dplyr 1.2.x, readr 2.2.0, tidyr 1.3.2): fetch with TinyFish and hold only the entries
about behaviour a beginner's code in this book could meet (default changes, deprecations of functions in the
needed-functions list above); citekey `tidyverse_news_s52r1`. (iii) The dataset: the palmerpenguins `penguins_raw.csv`
shipped in the installed package (file `system.file("extdata","penguins_raw.csv",package="palmerpenguins")`): copy it
byte-for-byte to `sources/data/penguins_raw.csv` (create the folder; check whether `sources/` already has a data
convention with `ls /home/claude/work/obesity-course/sources`), record its MD5, row and column counts and every
missing-value count by script (not by memory), the package's DESCRIPTION licence line and its CRAN page via
TinyFish (licence CC0; check). Citekey `horst_2020_palmerpenguins`. Then try, once, reading the NHANES data page
and the NCHS Data User Agreement via TinyFish and record the file names and sizes the page lists
(`BMX_L.xpt`, `DEMO_L.xpt`); you cannot download the files (host blocked): list exactly what Harsh would download.
