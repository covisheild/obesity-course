# Notes for other batches and the conductor, from b1 (C01-C03)

- **All batches / conductor (code gate).** The gate prints a parse error (a line R cannot read) as
  `Error: <text>:1:4: unexpected input` followed by the line and a caret, while the interactive
  console prints `Error: unexpected input in "72 ÷"` (checked with `R --vanilla -q`, R 4.3.3). Also,
  in a block with a parse error on line 3, the gate runs nothing (lines 1-2 print nothing), while
  RStudio sending the lines would print line 2's result first. TOOLING-CODE-GATE.md's list of
  differences from a console does not mention this. Prose describing a parse error should not claim
  the console layout matches the printed output. C02 and C03 say "in the RStudio console the same
  message reads ...".
- **Terms introduced in C01-C03 for later sections to reuse, same words:** "console", "script",
  "comment", "error message", "object", "name", "assignment" (read `<-` as "gets"), "workspace"
  (RStudio's Environment pane, listed by `ls()`), "snake case". C03 says "variable" has three
  meanings (Book 0 letter, R object name, and later a column of a data frame); C08 should name the
  third meaning when it arrives.
- **C02 script name.** C02's first script is `bmi_arithmetic.R` (typed numbers, no data). C07 and
  C21 introduce `code/analysis.R`; C02 says "later sections add a folder, data files and a whole
  analysis".
- **C15 (b5).** C01 cites Ziemann for SEPT2 -> "2-Sep" and MARCH1 -> "1-Mar" (19.6%, 704 of 3597
  papers, 18 journals, 2005-2015) and Bruford for the renaming SEPT1 -> SEPTIN1, MARCH1 -> MARCHF1.
  C15's "gene-name case of C01 seen again" can point back to C01 with those facts.
- **C19 (b7).** C01's PHE illustration ends on "compare one count with another" and the rule
  "count your rows before and after each step"; C19 discharges it.
- **Conductor.** C01's name differs from the inventory (see draft-notes-b1.md, item 1).
