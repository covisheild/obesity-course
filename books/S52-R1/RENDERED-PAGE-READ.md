# Rendered-page cold read (Step 5b, second pass) · S52-R1 · 3 Oct 2026

A fresh subagent read 112 of the 321 pages of `check/_build/S52-R1.pdf` (all front matter, the first pages of all
22 sections, code, figures and practice in every section, the appendix, glossary and back matter) and searched the
extracted text. Its list, with the conductor's disposition of what is a renderer matter.

## Fixed by the conductor in the renderer or shared files (not record defects)
- Inline code drew ligatures (`<-` as ←, `==` as ═, `>=` ⩾, `<=` ⩽, `!=` ≠, `|>` ▷, `::` spaced, `...` as an
  ellipsis): `check/pdf/style.css` now switches ligatures off for all `code`, not only code blocks.
- Bibliography: "Crosas, Merc`e" and "-Rundel" (Çetinkaya dropped): this book's `.bib` entries now carry the
  accented names in UTF-8 (trisovic_2022, r4ds_2e, rdocs_s52r1_dplyr). The renderer's mishandling of LaTeX accents
  (`{\c{C}}`, ``{\`e}``) also affects an earlier book's entry (openintro_stats_4e): handover note.
- Glossary "vector" row printed a record id inside its meaning: the ids now sit only in the section column.
- Series-wide, not this book's: the Symbols page prints "10 ³" (superscript minus missing in the table face);
  every Definition box carries the record's whole citation run (series convention); half-empty section openings
  when two figures move to the next page (layout engine). Handover notes.

## Record-level faults (to the fixer; page numbers refer to the 3 Oct render)
1. Code and output lines running past the margin or wrapping badly: p50 `('~/` / `project/code')`; p76 the
   `head -n 5` output breaking mid-field ("Date" / "Egg"); p156 `caption = "...as read from` / `data-raw/"`.
   Shorten the code line (split arguments over lines); for an output that wraps, show fewer columns.
2. Lists: p43 the second step is numbered "1." again ("1. Install it… 1. Load it"); p311 Exercise 2 item 10
   ("printouts are compared…") renders as a code block (indentation); p311 Exercise 3 and p258 "- The README
   gives…" print as literal hyphens inside one paragraph (needs a blank line before the list).
3. Function names set in bold body font instead of code: p80 **filter()**, p89 **mutate()** / **if_else()** /
   **case_when()** / **round()** / **str_trim()**, p140 **pivot_longer()** / **anti_join()**, p161
   **stopifnot()**: write them in backticks.
4. Sentences starting with lowercase "section N" (p11, p46, p78, p103): reword so a sentence never opens with a
   record id that renders lowercase.
5. Repetition: p172 then p174 give the Trisovic study details twice; p175 prints "Figures quoted… [353]" twice;
   p177/178 print the same script block twice; tables that repeat an output already shown (p31 nine masses, p69
   repeats the output and the p63 figure, p103, p131, p154–155, p190, p193): cut the repeat.
6. Tables too narrow, breaking words mid-word: p76–77 data dictionary ("Typ e", "num ber"; continues onto p77
   without its header); p187–188 NHANES dictionary ("Varia ble", "RIAG ENDR", "DEM O_L", "kg/ m2", "BMX _L"):
   fewer columns, shorter headers, or split into two tables.
7. p155–157: the text says "Look at the plot…" but no plot is printed (the book draws figures only through the
   figure system): say what the reader will see when they run it, or point to the section's figure.
8. Appendix heading "22 · One dataset, end to end" vs section title "Worked journey: One dataset, end to end":
   check whether the record or the renderer adds the prefix; report, do not change the renderer.
9. Length (judgement, not a fault): answers appendix 90 pages with full code and output repeated for every
   practice item; "library(readr)" 87 times and "show_col_types = FALSE" 111 times; long tibble printouts;
   the full sessionInfo (kept by decision). Where a practice answer repeats setup code its prompt already shows,
   the answer may show only the new lines (the gate runs prompt then answer in one session).
