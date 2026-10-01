# Builds the group-a source files for S52-R1 (textbooks, manuals, guides) from the saved raw fetches.
# Every passage is raw[i:j]: i = first occurrence of a literal start anchor, j = first occurrence of a
# literal end anchor after i (exclusive), or end of text. Nothing in a passage is typed by hand.
# Run: python3 build_a.py  (absolute paths; writes sources/<key>.txt and build-a/manifest-a.json)
import json, re, os

ROOT = "/home/claude/work/obesity-course/"
RAW = ROOT + "books/S52-R1/intake/raw/"
OUT = ROOT + "sources/"
MANIFEST = []
BEGIN, END = "--- passage begins ---", "--- passage ends ---"


def cut(rawname, start, end):
    raw = open(RAW + rawname + ".txt").read()
    i = raw.find(start)
    assert i != -1, ("start not found", rawname, start[:70])
    assert raw.count(start) == 1 or start.startswith("#"), ("start not unique", rawname, start[:70], raw.count(start))
    if end is None:
        j = len(raw)
    else:
        j = raw.find(end, i + len(start))
        assert j != -1, ("end not found", rawname, end[:70])
    return raw[i:j].rstrip()


def url_of(rawname):
    return json.load(open(RAW + rawname + ".meta.json"))["url"]


def build(key, title, header, blocks):
    """blocks: list of (rawname, heading, start, end, omitted_before_note or None)"""
    s = title + "\n" + "=" * 100 + "\n\n" + RULE + "\n" + header.strip() + "\n\nBLOCKS HELD:\n"
    for n, b in enumerate(blocks, 1):
        s += "  %d. %s (%s)\n" % (n, b[1], url_of(b[0]))
    for n, (rawname, heading, start, end, omit) in enumerate(blocks, 1):
        if omit:
            s += "\n[...]\n[NOTE] " + omit + "\n"
        p = cut(rawname, start, end)
        u = url_of(rawname)
        MANIFEST.append({"key": key, "block": n, "raw": rawname + ".txt", "url": u, "text": p})
        s += "\n" + "=" * 100 + "\nBLOCK %d - %s\nFETCHED: %s\n" % (n, heading, u) + "=" * 100 + "\n"
        s += BEGIN + "\n" + p + "\n" + END + "\n"
    s += "\n[...]\n[NOTE] End of the held excerpts. Everything not listed above is NOT held; absence of a passage from this file is not absence from the work.\n"
    open(OUT + key + ".txt", "w").write(s)
    print(key, len(blocks), "blocks", len(s), "chars")


RULE = ("Transcription rule for this file: every line between '" + BEGIN + "' and '" + END + "' is an exact,\n"
        "unaltered slice of the text returned by the TinyFish fetch_content tool (markdown output) for the URL\n"
        "named in that block's heading, cut by script (raw[i:j]) from the saved fetch; nothing has been\n"
        "paraphrased, re-wrapped or merged. The extraction's own artefacts are kept as returned (code fences\n"
        "split around inline code, '> >' prompts, escaped '\\*', figures dropped). [...] marks an omission;\n"
        "lines beginning [NOTE] and everything outside the passage markers are this file's own annotation and\n"
        "are NOT source text. Reference lists are never held. Fetched 2026-10-02.\n")

# ============================================================================== R4DS 2e
R4 = "r4ds_2e-"
r4ds_header = """
WORK: Wickham H, Cetinkaya-Rundel M, Grolemund G. R for Data Science: Import, Tidy, Transform,
Visualize, and Model Data. 2nd edition. O'Reilly Media; 2023. Online edition: https://r4ds.hadley.nz/
AUTHORS AS STATED: the site's own author metadata reads "Hadley Wickham, Mine Çetinkaya-Rundel, and
Garrett Grolemund" (home page, fetched 2026-10-02); the Acknowledgments say "the product of Hadley, Mine,
and Garrett". The page title is "R for Data Science (2e)". Publisher and year (O'Reilly, 2023) are NOT
stated in any fetched page and come from READY.md; the Colophon (block 2) says the online version "will
continue to evolve in between reprints of the physical book", so the online text may differ from print.
LICENCE AS STATED (home page, fetched 2026-10-02): "This website is and will always be free, licensed
under the CC BY-NC-ND 3.0 License." READY.md records the link target as
https://creativecommons.org/licenses/by-nc-nd/3.0/us/.
*** NO DERIVATIVES. These passages are held ONLY so that short quotations in the course can be checked
*** against the original. Do NOT adapt, paraphrase closely, translate or rework this text, its code or
*** its figures into the course. Quote briefly with attribution, or write in your own words from
*** understanding and cite.
VERSIONS: the online book's printed outputs are regenerated on each site build. The page's own
startup message (held in block 1, "The tidyverse") reads "tidyverse 2.0.0" with "dplyr 1.2.1", "readr 2.2.0", "ggplot2
4.0.3", "tidyr 1.3.2", "forcats 1.0.1", "lubridate 1.9.5", "stringr 1.6.0", "tibble 3.3.1", "purrr 1.2.2".
These are NEWER than the versions installed for S52-R1 (dplyr 1.1.4, readr 2.1.5, ggplot2 3.4.4, tidyr
1.3.1, forcats 1.0.0, lubridate 1.9.3, stringr 1.5.1, tibble 3.2.1). Any output printed below (lines
beginning "#>") is from those newer versions and must not be presented as what the course's own code
prints; rerun the code here. Example: ch. 16 and ch. 17 print the warning "The `file` argument of
`read_csv()` should use `I()` for literal data as of readr 2.2.0", which readr 2.1.5 does not give.
The book itself recommends "R 4.2.0 or later" and "at least RStudio 2022.02.0" (block 1).
WHAT IS HELD: per chapter, the sections that state a rule, definition or procedure the S52-R1 inventory
uses, each as one contiguous slice from its section heading to the next heading named in the [NOTE]s.
Chapter exercises, the Google Sheets half of ch. 20, and every section not listed under BLOCKS HELD are
NOT held. Figures are images and were dropped by the extraction (captions survive where the extractor
kept them). In-text cross-references ("Section 3.3.1") and footnote markers (a bare digit after a word,
e.g. "use_blank_slate()\\n\\n2") are as returned.
DROPPED CODE: the extractor drops some code blocks. Known case: 17.2.2's examples (the ymd(), mdy(),
dmy() calls and their output) are missing; only the rule in words survives ("identify the order in
which year, month, and day appear in your dates, then arrange "y", "m", and "d" in the same order").
For what mdy() and dmy() do, cite the lubridate help pages (S52-R1 group c). Absence of code here is not
absence from the book.
"""
r4ds_blocks = [
    (R4 + "ch01i-intro", "Introduction: Prerequisites (R, RStudio, the tidyverse, other packages) and Running R code",
     "## Prerequisites", "## Acknowledgments", None),
    (R4 + "ch01i-intro", "Introduction: Colophon", "## Colophon", "* If you’d like a comprehensive overview",
     "Introduction: Acknowledgments omitted; the Colophon's footnote omitted after the block."),
    (R4 + "ch01-data-visualize", "Ch. 1 Data visualization: 1.1 Introduction and 1.1.1 Prerequisites",
     "# 1 Data visualization", "## 1.2 First steps",
     "Ch. 1 begins (the page opens with a library(tidyverse) startup message, lines before the chapter heading, omitted)."),
    (R4 + "ch01-data-visualize", "Ch. 1: 1.2 First steps, 1.2.1 The penguins data frame (variable, value, observation, tabular data), 1.2.2 Ultimate goal, 1.2.3 Creating a ggplot, 1.2.4 Adding aesthetics and layers",
     "## 1.2 First steps", "### 1.2.5 Exercises", None),
    (R4 + "ch01-data-visualize", "Ch. 1: 1.3 ggplot2 calls; 1.4 Visualizing distributions (1.4.1 categorical, 1.4.2 numerical)",
     "## 1.3 ggplot2 calls", "### 1.4.3 Exercises", "1.2.5 Exercises omitted."),
    (R4 + "ch01-data-visualize", "Ch. 1: 1.5 Visualizing relationships, 1.5.1 to 1.5.4 (including facets)",
     "## 1.5 Visualizing relationships", "### 1.5.5 Exercises", "1.4.3 Exercises omitted."),
    (R4 + "ch01-data-visualize", "Ch. 1: 1.6 Saving your plots (ggsave)", "## 1.6 Saving your plots",
     "### 1.6.1 Exercises", "1.5.5 Exercises omitted."),
    (R4 + "ch01-data-visualize", "Ch. 1: 1.7 Common problems", "## 1.7 Common problems", "## 1.8 Summary",
     "1.6.1 Exercises omitted."),
    (R4 + "ch02-workflow-basics", "Ch. 2 Workflow: basics, 2.1 Coding basics (assignment), 2.2 Comments, 2.3 What's in a name?, 2.4 Calling functions",
     "## 2.1 Coding basics", "## 2.5 Exercises", "Ch. 1 summary and the chapter's opening paragraph of ch. 2 omitted."),
    (R4 + "ch02-workflow-basics", "Ch. 2: 2.6 Summary", "## 2.6 Summary", None, "2.5 Exercises omitted."),
    (R4 + "ch03-data-transform", "Ch. 3 Data transformation: 3.1.3 dplyr basics; 3.2 Rows (filter, common mistakes, arrange, distinct)",
     "### 3.1.3 dplyr basics", "### 3.2.5 Exercises", "Ch. 3 introduction, 3.1.1 prerequisites and 3.1.2 nycflights13 omitted."),
    (R4 + "ch03-data-transform", "Ch. 3: 3.3 Columns (mutate, select, rename, relocate)", "## 3.3 Columns",
     "### 3.3.5 Exercises", "3.2.5 Exercises omitted."),
    (R4 + "ch03-data-transform", "Ch. 3: 3.4 The pipe; 3.5 Groups (group_by, summarize, slice_, multiple variables, ungrouping, .by)",
     "## 3.4 The pipe", "### 3.5.7 Exercises", "3.3.5 Exercises omitted."),
    (R4 + "ch03-data-transform", "Ch. 3: 3.6 Case study: aggregates and sample size",
     "## 3.6 Case study: aggregates and sample size", "## 3.7 Summary", "3.5.7 Exercises omitted."),
    (R4 + "ch04-workflow-style", "Ch. 4 Workflow: code style, 4.1 Names to 4.5 Sectioning comments",
     "## 4.1 Names", "## 4.6 Exercises", "Ch. 4 opening paragraphs (styler, command palette) omitted."),
    (R4 + "ch05-data-tidy", "Ch. 5 Data tidying: 5.1 Introduction", "# 5 Data tidying", "### 5.1.1 Prerequisites", None),
    (R4 + "ch05-data-tidy", "Ch. 5: 5.2 Tidy data (the three rules)", "## 5.2 Tidy data", "### 5.2.1 Exercises",
     "5.1.1 Prerequisites omitted."),
    (R4 + "ch05-data-tidy", "Ch. 5: 5.3 Lengthening data, 5.3.1 Data in column names", "## 5.3 Lengthening data",
     "### 5.3.2 How does pivoting work?", "5.2.1 Exercises omitted."),
    (R4 + "ch05-data-tidy", "Ch. 5: 5.4 Widening data (opening)", "## 5.4 Widening data", "### 5.4.1 How does",
     "5.3.2 to 5.3.4 omitted."),
    (R4 + "ch05-data-tidy", "Ch. 5: 5.5 Summary", "## 5.5 Summary", None, "5.4.1 omitted."),
    (R4 + "ch06-workflow-scripts", "Ch. 6 Workflow: scripts and projects, 6.1 Scripts (6.1.1 Running code, 6.1.2, 6.1.3 Saving and naming), 6.2 Projects (6.2.1 What is the source of truth?, 6.2.2 Where does your analysis live?, 6.2.3 RStudio projects, 6.2.4 Relative and absolute paths)",
     "# 6 Workflow: scripts and projects", "## 6.3 Exercises", None),
    (R4 + "ch06-workflow-scripts", "Ch. 6: 6.4 Summary", "## 6.4 Summary", "* Not to mention",
     "6.3 Exercises omitted; the chapter's two footnotes omitted after the block."),
    (R4 + "ch07-data-import", "Ch. 7 Data import: 7.1 Introduction, 7.2 Reading data from a file (7.2.1 Practical advice, 7.2.2 Other arguments, 7.2.3 Other file types)",
     "# 7 Data import", "### 7.2.4 Exercises", None),
    (R4 + "ch07-data-import", "Ch. 7: 7.3 Controlling column types (7.3.1 Guessing types, 7.3.2 Missing values, column types, and problems, 7.3.3 Column types)",
     "## 7.3 Controlling column types", "## 7.4 Reading data from multiple files", "7.2.4 Exercises omitted."),
    (R4 + "ch07-data-import", "Ch. 7: 7.5 Writing to a file", "## 7.5 Writing to a file", "## 7.6 Data entry",
     "7.4 Reading data from multiple files omitted."),
    (R4 + "ch07-data-import", "Ch. 7: 7.7 Summary", "## 7.7 Summary", None, "7.6 Data entry omitted."),
    (R4 + "ch08-workflow-help", "Ch. 8 Workflow: getting help, opening, 8.1 Google is your friend, 8.2 Making a reprex",
     "This book is not an island", "## 8.3 Investing in yourself", None),
    (R4 + "ch12-logicals", "Ch. 12 Logical vectors: 12.2.2 Missing values, 12.2.3 is.na()", "### 12.2.2 Missing values",
     "### 12.2.4 Exercises", "Ch. 8 sections 8.3 and 8.4, and ch. 12 sections 12.1 to 12.2.1, omitted."),
    (R4 + "ch12-logicals", "Ch. 12: 12.3.1 Missing values (in Boolean algebra)", "### 12.3.1 Missing values",
     "### 12.3.2 Order of operations", "12.2.4 Exercises and 12.3 Boolean algebra opening omitted."),
    (R4 + "ch12-logicals", "Ch. 12: 12.3.3 %in%", "### 12.3.3 ``` %in% ```", "### 12.3.4 Exercises",
     "12.3.2 Order of operations omitted."),
    (R4 + "ch12-logicals", "Ch. 12: 12.5 Conditional transformations (12.5.1 if_else(), 12.5.2 case_when(), 12.5.3 Compatible types)",
     "## 12.5 Conditional transformations", "### 12.5.4 Exercises", "12.3.4 Exercises and 12.4 Summaries omitted."),
    (R4 + "ch16-factors", "Ch. 16 Factors: 16.1 Introduction, 16.2 Factor basics", "## 16.1 Introduction",
     "## 16.3 General Social Survey", "Ch. 12 remainder omitted. (The ch. 16 page as extracted begins at 16.1; its chapter title line was not returned.)"),
    (R4 + "ch16-factors", "Ch. 16: 16.4 Modifying factor order (fct_reorder, fct_relevel, fct_infreq)",
     "## 16.4 Modifying factor order", "### 16.4.1 Exercises", "16.3 General Social Survey and exercises omitted."),
    (R4 + "ch16-factors", "Ch. 16: 16.5 Modifying factor levels (fct_recode, fct_collapse, fct_lump)",
     "## 16.5 Modifying factor levels", "### 16.5.1 Exercises", "16.4.1 Exercises omitted."),
    (R4 + "ch17-datetimes", "Ch. 17 Dates and times: 17.1 Introduction, 17.2 Creating date/times, 17.2.1 During import (ISO8601), 17.2.2 From strings (the y/m/d naming rule; the example calls were dropped by the extractor)",
     "# 17 Dates and times", "### 17.2.3 From individual components", "Ch. 16 remainder omitted."),
    (R4 + "ch17-datetimes", "Ch. 17: 17.2.4 From other types", "### 17.2.4 From other types", "### 17.2.5 Exercises",
     "17.2.3 From individual components omitted."),
    (R4 + "ch17-datetimes", "Ch. 17: 17.4 Time spans (durations, periods, intervals)", "## 17.4 Time spans",
     "### 17.4.4 Exercises", "17.2.5 Exercises and 17.3 Date-time components omitted."),
    (R4 + "ch18-missing-values", "Ch. 18 Missing values: 18.1 Introduction, 18.2 Explicit missing values (18.2.1 LOCF, 18.2.2 Fixed values, 18.2.3 NaN)",
     "# 18 Missing values", "## 18.3 Implicit missing values", "Ch. 17 remainder omitted."),
    (R4 + "ch18-missing-values", "Ch. 18: 18.3 Implicit missing values (opening)", "## 18.3 Implicit missing values",
     "### 18.3.1 Pivoting", None),
    (R4 + "ch18-missing-values", "Ch. 18: 18.5 Summary", "## 18.5 Summary", None, "18.3.1 to 18.4 omitted."),
    (R4 + "ch19-joins", "Ch. 19 Joins: 19.1 Introduction, 19.2 Keys (19.2.1 Primary and foreign keys, 19.2.2 Checking primary keys, 19.2.3 Surrogate keys)",
     "# 19 Joins", "### 19.2.4 Exercises", None),
    (R4 + "ch19-joins", "Ch. 19: 19.3 Basic joins, 19.3.1 Mutating joins", "## 19.3 Basic joins",
     "### 19.3.2 Specifying join keys", "19.2.4 Exercises omitted."),
    (R4 + "ch19-joins", "Ch. 19: 19.3.3 Filtering joins (semi_join, anti_join)", "### 19.3.3 Filtering joins",
     "### 19.3.4 Exercises", "19.3.2 Specifying join keys omitted."),
    (R4 + "ch19-joins", "Ch. 19: 19.4.1 Row matching (duplicate keys and many-to-many)", "### 19.4.1 Row matching",
     "### 19.4.2 Filtering joins", "19.3.4 Exercises and 19.4 opening omitted."),
    (R4 + "ch20-spreadsheets", "Ch. 20 Spreadsheets: 20.1 Introduction, 20.2 Excel (20.2.1 to 20.2.8: getting started, reading spreadsheets, worksheets, part of a sheet, 20.2.6 Data types, writing, formatted output)",
     "# 20 Spreadsheets", "### 20.2.9 Exercises", "Ch. 19 remainder omitted."),
    (R4 + "ch20-spreadsheets", "Ch. 20: 20.4 Summary", "## 20.4 Summary", None,
     "20.2.9 Exercises and 20.3 Google Sheets omitted."),
]
build("r4ds_2e", "R FOR DATA SCIENCE, 2ND EDITION (WICKHAM, CETINKAYA-RUNDEL, GROLEMUND) - VERBATIM EXCERPTS FOR QUOTE-CHECKING ONLY (CC BY-NC-ND 3.0)",
      r4ds_header, [(r, h, s, e, o) for (r, h, s, e, o) in r4ds_blocks])

# ============================================================================== An Introduction to R
RI = "r_intro_manual-page"
rintro_header = """
WORK: Venables WN, Smith DM, and the R Core Team. An Introduction to R. Notes on R: A Programming
Environment for Data Analysis and Graphics. Manual for R version 4.6.1 (2026-06-24).
https://cran.r-project.org/doc/manuals/r-release/R-intro.html (the "r-release" URL always serves the
current release's manual).
VERSION AS STATED (block 1): "This manual is for R, version 4.6.1 (2026-06-24)." The S52-R1 book's code
runs on R 4.3.3; nothing in the held passages is known to differ between 4.3.3 and 4.6.1, but the
passages describe 4.6.1 and were not compared with the 4.3.3 manual.
COPYRIGHT AND PERMISSION AS STATED (block 1, quoted in full there): Copyright 1990 W. N. Venables;
1992 Venables & D. M. Smith; 1997 R. Gentleman & R. Ihaka; 1997, 1998 M. Maechler; 1999-2026 R Core
Team. "Permission is granted to make and distribute verbatim copies of this manual provided the
copyright notice and this permission notice are preserved on all copies", with modified versions
allowed "under the conditions for verbatim copying, provided that the entire resulting derived work is
distributed under the terms of a permission notice identical to this one." Not a Creative Commons
licence. Block 1 preserves the notice as the permission requires.
EXTRACTION: the HTML manual's chapter and section headings (e.g. "2.1 Vectors and assignment") were
NOT returned by the extractor, so blocks are named here by their content and the manual's section
names are given from the manual's structure only as orientation in brackets. Inline code is split onto
separate fenced lines and example commands carry a doubled "> >" prompt; both are extraction artefacts.
THE PIPE: the manual contains no "|>" and does not describe the native pipe (searched 2026-10-02); cite
R4DS 2e ch. 3.4 or the base R help page for the pipe instead.
WHAT IS HELD: the version and permission notice; getting help; names, commands and comments; source(),
objects and the workspace; vectors and assignment through simple arithmetic and summary functions;
logical vectors and missing values (NA, is.na, NaN); index vectors (opening and the replacement
example); objects, modes and coercion; packages and namespaces; the Rscript front-end. Everything
else (arrays, lists, data frames, reading data, distributions, statistical models, graphics, the
sample session, appendices other than the Rscript passage) is NOT held.
"""
rintro_blocks = [
    (RI, "Version line, copyright and permission notice", "This manual is for R, version 4.6.1",
     "approved by the R Core Team.\n", None),
    (RI, "[1.7 Getting help with functions and features] help(), ?, help.start(), help.search, example()",
     "R has an inbuilt help facility", "Technically R is an expression language", "Preface and sections 1.1 to 1.6 omitted."),
    (RI, "[1.8 R commands, case sensitivity, etc.] names, expressions and assignments, commands, comments",
     "Technically R is an expression language", "If a command is not complete at the end of a line", None),
    (RI, "[1.10 Executing commands from a file; 1.11 Data permanency and removing objects] source(), objects(), the workspace, .RData",
     "If commands5 are stored in an external file", "R operates on named data structures.",
     "1.9 Recall and correction of previous commands omitted."),
    (RI, "[2.1 Vectors and assignment; 2.2 Vector arithmetic] c(), <-, element-by-element arithmetic, recycling, max/min/length/sum/mean/var/sort",
     "R operates on named data structures.", "R has a number of facilities for generating commonly used sequences", None),
    (RI, "[2.4 Logical vectors; 2.5 Missing values; opening of 2.6 Character vectors]",
     "As well as numerical vectors, R allows manipulation of logical", "Character quantities and character vectors are used frequently",
     "2.3 Generating regular sequences omitted."),
    (RI, "[2.7 Index vectors] opening paragraph and the logical index vector (x[!is.na(x)])",
     "Subsets of the elements of a vector may be selected", "```\nlength(x)\n```\n\n}. The corresponding elements",
     "2.6 Character vectors (body) omitted."),
    (RI, "[end of 2.7] replacement with an index vector, x[is.na(x)] <- 0; [3.1 Intrinsic attributes: mode and length] atomic structures, modes, coercion with as.character()/as.integer()",
     "An indexed expression can also appear on the receiving end of an", "An “empty” object may still have a mode.",
     "The rest of 2.7 (positive, negative and character index vectors) omitted."),
    (RI, "[13 Packages; 13.1 Standard packages; 13.2 Contributed packages and CRAN; 13.3 Namespaces] library(), install.packages(), search(), ::",
     "All R functions and datasets are stored in packages.", "R has quite extensive facilities to access the OS",
     "Sections 3.1 (rest) to 12 omitted."),
    (RI, "[Appendix B, Scripting with R] Rscript", "This is made simpler by the alternative front-end",
     "One thing to consider is what", "Chapter 14 and the rest of Appendix B before the Rscript passage omitted."),
]
build("r_intro_manual", "AN INTRODUCTION TO R (R CORE TEAM; MANUAL FOR R 4.6.1) - VERBATIM EXCERPTS",
      rintro_header, rintro_blocks)

# ============================================================================== R Language Definition
RL = "r_lang_def-page"
rlang_header = """
WORK: R Core Team. R Language Definition. Manual for R version 4.6.0 (2026-04-24).
https://cran.r-project.org/doc/manuals/r-release/R-lang.html
VERSION AS STATED (block 1): "This manual is for R, version 4.6.0 (2026-04-24)." (Note: the R-intro
manual served at the same time is for 4.6.1; the book's code runs on R 4.3.3.)
COPYRIGHT AND PERMISSION AS STATED (block 1): "Copyright © 2000–2026 R Core Team", with the same
verbatim-copy permission notice as An Introduction to R. Not a Creative Commons licence.
EXTRACTION: section headings were not returned by the extractor; blocks are named by content, with the
manual's section names in brackets as orientation only. The type table after block 3 was mangled by
the extractor into pipe fragments and is NOT held.
OPTIONAL SOURCE (READY.md): held only for exact statements about objects, types and NA.
WHAT IS HELD: the version and permission notice; [2 Objects] opening; [2.1.1 Vectors] the six atomic
types; [3.3.4 NA handling] how NA behaves; [10.4.2 Infix and prefix operators] the operator precedence
list, which places |> . Everything else is NOT held.
"""
rlang_blocks = [
    (RL, "Version line, copyright and permission notice", "This manual is for R, version 4.6.0",
     "approved by the R Core Team.\n", None),
    (RL, "[2 Objects] opening paragraph", "In every computer language variables provide a means",
     "In this chapter we provide preliminary descriptions", "Chapter 1 Introduction omitted."),
    (RL, "[2.1 Basic types] coercion; [2.1.1 Vectors] the six atomic vector types", "R objects are often coerced to different types",
     "The modes and storage modes for the different vector types", "The rest of chapter 2.1 before the coercion paragraph omitted."),
    (RL, "[3.3.4 NA handling]", "Missing values in the statistical sense", "However, an",
     "The type table and everything from 2.1.2 to 3.3.3 omitted."),
    (RL, "[10.4.2 Infix and prefix operators] precedence list", "The order of precedence (highest first) of the operators is",
     "Note that", "The rest of 3.3.4 and chapters 3.4 to 10.4.1 omitted."),
]
build("r_lang_def", "R LANGUAGE DEFINITION (R CORE TEAM; MANUAL FOR R 4.6.0) - VERBATIM EXCERPTS",
      rlang_header, rlang_blocks)

# ============================================================================== Software Carpentry
SW = "swc_r_gapminder-"
swc_header = """
WORK: The Carpentries. R for Reproducible Scientific Analysis (Software Carpentry lesson,
"r-novice-gapminder"). https://swcarpentry.github.io/r-novice-gapminder/ . Each episode page reads "Last
updated on 2026-09-01" (held at the top of each block's source page; the dates were read from the
fetches). Authorship: the lesson credits The Carpentries community; individual maintainers are not
named on the fetched pages, so cite the organisation as author.
LICENCE AS STATED (the lesson's own LICENSE page, block 1, "Last updated on 2026-09-01"): "All
Carpentries (Software Carpentry, Data Carpentry, and Library Carpentry) instructional material is made
available under the Creative Commons Attribution license", "the CC BY 4.0 license"; attribution must
mention "that your work is derived from work that is Copyright (c) The Carpentries". Example programs
and other software are under the MIT licence (same page). CC BY 4.0 permits adaptation with credit.
[NOTE] The site footer, which the extractor drops, links to creativecommons.org/licenses/by-sa/4.0/
(seen in the outbound-link list of a first, unstored fetch of the index and LICENSE pages on 2026-10-02;
that footer link most likely refers to the lesson template); the LICENSE page's own text says CC BY 4.0
and links to creativecommons.org/licenses/by/4.0/, and that page text is the licence relied on here.
EPISODES HELD: index (summary and prerequisites); 01 Introduction to R and RStudio; 02 Project
Management With RStudio; 03 Seeking Help; 04 Data Structures (the opening through vectors and type
coercion only); 08 ggplot2; 11 Writing Data; 12 dplyr; 13 tidyr. Episodes 05-07, 09, 10, 14, 15 were NOT
fetched. Factors: episode 04 as held only tells learners to check for and avoid automatic factors (the
"Check your data for factors" box); the lesson's own treatment of factors (episode 05 or later) is NOT
held. Challenges, solutions and most code-output blocks inside omitted ranges are NOT held; within a held
range, "### R" and "### OUTPUT" lines are the lesson's code/output labels as extracted, and the outputs are
the lesson's own printed outputs (R and package versions not stated on the pages).
"""
swc_blocks = [
    (SW + "license", "LICENSE page: Instructional Material", "Last updated on 2026-09-01", "## Software", None),
    (SW + "index", "Lesson index: summary and prerequisites", "# Summary and Setup", None, None),
    (SW + "ep01", "Ep. 01 Introduction to R and RStudio: R scripts", "### R scripts", "## Workflow within RStudio",
     "Ep. 01 overview, objectives, 'Before Starting', 'Why use R' and the RStudio overview omitted."),
    (SW + "ep01", "Ep. 01: Workflow within RStudio; Introduction to R; Using R as a calculator; Mathematical functions; Comparing things; Variables and assignment; Vectorization; Managing your environment; R Packages",
     "## Workflow within RStudio", "### Challenge 2", None),
    (SW + "ep02", "Ep. 02 Project Management With RStudio: Introduction; A possible solution", "## Introduction",
     "### Challenge 1: Creating a self-contained project", "Ep. 01 challenges omitted."),
    (SW + "ep02", "Ep. 02: Best practices for project organization (Treat data as read only; Data Cleaning; Treat generated output as disposable; Good Enough Practices tip; Separate function definition and application; Save the data in the data directory)",
     "## Best practices for project organization", "### Challenge 3", "Ep. 02 Challenges 1 and 2 omitted."),
    (SW + "ep02", "Ep. 02: Working directory", "### Working directory", "### Challenge 5", "Ep. 02 Challenges 3 and 4 omitted."),
    (SW + "ep02", "Ep. 02: File does not exist errors; Version Control", "### Tip: File does not exist errors", None,
     "Ep. 02 Challenge 5 omitted."),
    (SW + "ep03", "Ep. 03 Seeking Help: Reading Help Files; Special Operators; Getting Help with Packages; When You Remember Part of the Function Name",
     "## Reading Help Files", "## When You Have No Idea Where to Begin", "Ep. 03 overview omitted."),
    (SW + "ep04", "Ep. 04 Data Structures: opening (feline-data.csv), Check your data for factors, Data Types, Vectors and Type Coercion, the type hierarchy",
     "One of R’s most powerful features is its ability to deal with tabular", "### Challenge 1",
     "Ep. 03 remainder omitted."),
    (SW + "ep08", "Ep. 08 Creating Publication-Quality Graphics with ggplot2: grammar of graphics, first plot",
     "Plotting our data is one of the best ways", "### Challenge 1", "Ep. 04 remainder (Challenge 1 onward: basic vector functions, lists, names, data frames, matrices) omitted."),
    (SW + "ep08", "Ep. 08: Layers (including the tip on setting an aesthetic to a value instead of a mapping)", "## Layers",
     "### Challenge 3", "Ep. 08 Challenges 1 and 2 omitted."),
    (SW + "ep08", "Ep. 08: Multi-panel figures", "## Multi-panel figures", "## Modifying text",
     "Ep. 08 Transformations and statistics omitted."),
    (SW + "ep08", "Ep. 08: Exporting the plot (ggsave)", "## Exporting the plot", "### Challenge 5", "Ep. 08 Modifying text omitted."),
    (SW + "ep11", "Ep. 11 Writing Data: Saving plots", "## Saving plots", "### Challenge 1", None),
    (SW + "ep11", "Ep. 11: Writing data", "## Writing data", "### Challenge 2", "Ep. 11 Challenge 1 omitted."),
    (SW + "ep12", "Ep. 12 Data Frame Manipulation with dplyr: the dplyr package; Using select(); Using filter()",
     "## The ``` dplyr ``` package", "### Challenge 1", "Ep. 12 opening (base R repetition example) omitted."),
    (SW + "ep12", "Ep. 12: Using group_by(); Using summarize()", "## Using group\\_by()", "### Challenge 2",
     "Ep. 12 Challenge 1 omitted."),
    (SW + "ep12", "Ep. 12: count() and n(); Using mutate(); Connect mutate with logical filtering: ifelse",
     "## count() and n()", "## Combining ``` dplyr ``` and ``` ggplot2 ```", "Ep. 12 Challenge 2 and its solutions omitted."),
    (SW + "ep13", "Ep. 13 Data Frame Manipulation with tidyr: opening (long and wide formats)",
     "Researchers often want to reshape their data frames", "## Getting started", "Ep. 12 remainder omitted."),
    (SW + "ep13", "Ep. 13: From wide to long format with pivot_longer()", "## From wide to long format with pivot\\_longer()",
     "### Challenge 2", "Ep. 13 Getting started and Challenge 1 omitted."),
    (SW + "ep13", "Ep. 13: From long to intermediate format with pivot_wider() (opening)",
     "## From long to intermediate format with pivot\\_wider()", "### R", "Ep. 13 Challenge 2 omitted."),
]
build("swc_r_gapminder", "SOFTWARE CARPENTRY, R FOR REPRODUCIBLE SCIENTIFIC ANALYSIS (THE CARPENTRIES, CC BY 4.0) - VERBATIM EXCERPTS",
      swc_header, swc_blocks)

# ============================================================================== Data Carpentry spreadsheets
DC = "dc_spreadsheets-"
dc_header = """
WORK: The Carpentries. Data Organization in Spreadsheets for Ecologists (Data Carpentry lesson,
"spreadsheet-ecology-lesson"). https://datacarpentry.github.io/spreadsheet-ecology-lesson/ . Episode
pages state "Last updated on" 2024-03-08 (ep. 01), 2025-07-23 (ep. 02 and 04), 2026-08-04 (ep. 03),
2024-03-09 (ep. 05). Cite the organisation as author; individual maintainers are not named on the
fetched pages.
LICENCE AS STATED (this lesson's own LICENSE page, block 1, "Last updated on 2025-02-03"): "All
Carpentries ... instructional material is made available under the Creative Commons Attribution
license", "the CC BY 4.0 license". [NOTE] As with the Software Carpentry lesson, the site footer (seen in the
outbound-link list of an unstored first fetch) links to the BY-SA 4.0 deed; the LICENSE page's own text
(CC BY 4.0) is relied on.
OPTIONAL SOURCE (READY.md).
WHAT IS HELD: LICENSE (instructional material); index summary; ep. 01 'Keeping track of your analyses',
'Structuring data in spreadsheets' and 'Columns for variables and rows for observations'; ep. 02 the
whole list of common spreadsheet errors and each error's section (multiple tables and tabs, zeros,
problematic null values and its table, formatting, comments or units in cells, more than one piece of
information in a cell, field names, special characters, metadata); ep. 03 the whole episode text from
its opening to the end (including its exercises as extracted); ep. 04 Quality Assurance; ep. 05 the whole
episode text. Figures (including ep. 02's null-value table if it is an image) were dropped by the
extractor wherever they were images.
[NOTE] For dates, this lesson recommends storing YEAR, MONTH, DAY in separate columns (or YEAR and
DAY-OF-YEAR), block on ep. 03 'Preferred date format'; Broman & Woo 2018 recommend a single ISO 8601
YYYY-MM-DD form. The two sources disagree; the course must not merge them into one rule.
"""
dc_blocks = [
    (DC + "license", "LICENSE page: Instructional Material", "Last updated on 2025-02-03", "## Software", None),
    (DC + "index", "Lesson index: summary", "# Summary and Setup", "### Getting Started", None),
    (DC + "ep01", "Ep. 01 Formatting data tables in Spreadsheets: Keeping track of your analyses; Structuring data in spreadsheets; Columns for variables and rows for observations",
     "### Keeping track of your analyses", "### Discussion", "Index setup instructions and ep. 01 overview omitted."),
    (DC + "ep02", "Ep. 02 Formatting problems: Common Spreadsheet Errors and every error section", "## Common Spreadsheet Errors",
     None, "Ep. 01 Discussion and Exercise omitted; ep. 02 overview omitted."),
    (DC + "ep03", "Ep. 03 Dates as data: whole episode text after the objectives", "Dates in spreadsheets can be a problem.",
     None, "Ep. 03 overview omitted."),
    (DC + "ep04", "Ep. 04 Quality control: Quality Assurance", "## Quality Assurance", "## Quality Control",
     "Ep. 04 overview omitted."),
    (DC + "ep05", "Ep. 05 Exporting data: whole episode text after the objectives", "Storing the data you’re going to work with",
     None, "Ep. 04 Quality Control (sorting, conditional formatting) omitted; ep. 05 overview omitted."),
]
build("dc_spreadsheets", "DATA CARPENTRY, DATA ORGANIZATION IN SPREADSHEETS FOR ECOLOGISTS (THE CARPENTRIES, CC BY 4.0) - VERBATIM EXCERPTS",
      dc_header, dc_blocks)

# ============================================================================== tidyverse style guide
TS = "tidyverse_style-"
ts_header = """
WORK: Wickham H (the tidyverse team). The tidyverse style guide. https://style.tidyverse.org/ . Author
as stated in the site's own metadata: "The tidyverse team" (home page). Undated online book; no edition
or date is given on the fetched pages. Source repository: github.com/tidyverse/style.
LICENCE AS STATED: the site's pages, as extracted, state no licence. The repository's LICENSE.md
(https://github.com/tidyverse/style/blob/main/LICENSE.md, fetched 2026-10-02, block 1) is the text of
"Creative Commons Legal Code" / "Attribution-ShareAlike 3.0 Unported" (CC BY-SA 3.0). Adaptation is
permitted with attribution and share-alike; quoting with attribution is the course's practice.
WHAT IS HELD: the repository licence heading; the home page (purpose, derivation from Google's R style
guide, styler and lintr); chapter 1 Files, 1.1 Names (whole page as extracted); chapter 2 Syntax: 2.1
Object names to 2.4 Function calls (including 2.4.2 Assignment) and 2.7 Semicolons to 2.10 Comments;
chapter 4 Pipes (whole page). Chapter 2.5-2.6 (braces, control flow) and chapters 3, 5 onward are NOT held.
"""
ts_blocks = [
    (TS + "license-github", "Repository LICENSE.md: licence name", "# Creative Commons Legal Code",
     "CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM", None),
    (TS + "index", "Home page: Welcome", "# Welcome", None, "The rest of the licence text omitted."),
    (TS + "files", "1 Files: 1.1 Names (and the rest of the page as extracted)", "## 1.1 Names", None, None),
    (TS + "syntax", "2 Syntax: 2.1 Object names, 2.2 Spacing, 2.3 Vertical space, 2.4 Function calls (2.4.1 Named arguments, 2.4.2 Assignment, 2.4.3 Long function calls)",
     "## 2.1 Object names", "## 2.5 Braced expressions", None),
    (TS + "syntax", "2 Syntax: 2.7 Semicolons, 2.8 Assignment, 2.9 Data, 2.10 Comments", "## 2.7 Semicolons", None,
     "2.5 Braced expressions and 2.6 Control flow omitted."),
    (TS + "pipes", "4 Pipes: 4.1 Introduction to 4.6 magrittr (whole page as extracted)", "## 4.1 Introduction", None, None),
]
build("tidyverse_style", "THE TIDYVERSE STYLE GUIDE (THE TIDYVERSE TEAM; CC BY-SA 3.0 PER REPOSITORY LICENSE) - VERBATIM EXCERPTS",
      ts_header, ts_blocks)

json.dump(MANIFEST, open(ROOT + "books/S52-R1/intake/build-a/manifest-a.json", "w"), indent=1, ensure_ascii=False)
print("passages:", len(MANIFEST))
