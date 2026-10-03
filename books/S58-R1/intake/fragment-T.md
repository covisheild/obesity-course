# S58-R1 intake, group T (Tufte: Lie Factor, graphical integrity, data-ink, chartjunk): entries to merge

Three blocks for the conductor to paste into `sources/INDEX.yml` (under `files:`),
`check/references/library.bib` (append) and `sources/SOURCES.md` (a new section). One file:
`sources/tufte_1983_visual_display.txt`. Log: `books/S58-R1/intake/log-T.md`.

**Citekey changed from the task's `tufte_2001_visual_display` to `tufte_1983_visual_display`:** the copy
Harsh supplied is the FIRST edition (copyright page: "Copyright © 1983 by Edward R. Tufte", "Tenth printing,
March 1990", checked on the page image), not the 2001 second edition. A 2001 key would misdate what is held.
If the course must cite the 2001 edition, the page numbers need checking in a 2001 copy first. Citekeys grepped
(`tufte_` in INDEX.yml, library.bib, SOURCES.md, every `books/*/intake/fragment-*.md`, and `git log --all -S`)
on 2026-10-02 at start and end: none exists. Grep again at merge (S47-R1 and S52-R1 add keys on other branches).

## 1. `sources/INDEX.yml`, under `files:`

```yaml
  tufte_1983_visual_display:
    file: tufte_1983_visual_display.txt
    what: >-
      Tufte, The Visual Display of Quantitative Information, Graphics Press 1983 (FIRST edition, tenth printing
      March 1990; not the 2001 2nd ed.). Scan supplied by Harsh 2 Oct 2026 from Anna's Archive (a shadow
      library; Internet Archive digitisation bwb_T2-EQU-551), OCR text layer; in copyright, short excerpts held
      privately for study and quotation. 30 passages, every page checked against its image: ch. 2 pp. 56-58
      (first two principles; Lie Factor = size of effect shown in graphic / size of effect in data, formula read
      from the page image; "greater than 1.05 or less than .95 indicate substantial distortion"; fuel-economy
      example 53% vs 783%, Lie Factor 14.8), pp. 60-61 (design variation, OPEC 15.1x), pp. 70-71 (dimensions;
      barrels 9.4 and 59.4), p. 77 (the six principles); ch. 4 pp. 93-94 (data-ink, data-ink ratio), pp. 96-97,
      100 (maximize the ratio; erase non-data-ink; erase redundant data-ink), p. 105 (the five principles);
      ch. 5 pp. 107, 112-113, 116, 121 (chartjunk introduced, the grid, the duck, conclusion). No figures
```

## 2. `check/references/library.bib`, append

```bibtex
@book{tufte_1983_visual_display,
  title        = {The Visual Display of Quantitative Information},
  author       = {Tufte, Edward R.},
  year         = {1983},
  publisher    = {Graphics Press},
  address      = {Cheshire, Connecticut},
  note         = {First edition (``Copyright 1983 by Edward R. Tufte ... All rights reserved''), quoted
                  from the tenth printing, March 1990. Short excerpts held privately for study and quotation
                  from a scan supplied by the author of this course (Internet Archive digitisation, obtained
                  through a shadow library), checked against the page images. A second edition was published
                  by Graphics Press in 2001; these page numbers were not checked against it}
}
```

## 3. `sources/SOURCES.md`, new section (same columns as the main table)

```markdown
## S58-R1 intake, group T: Tufte on graphical integrity and data-ink (2 Oct 2026)

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `tufte_1983_visual_display.txt` | Tufte, *The Visual Display of Quantitative Information*, Graphics Press, **first edition 1983** (tenth printing, March 1990), not the 2001 2nd ed.; scan supplied by Harsh from Anna's Archive (a shadow library), OCR text layer. In copyright, all rights reserved: **short excerpts only**, held privately for study and quotation; OCR errors left in place, true readings in [NOTE]s from the page images | 2,225 | Lie Factor = size of effect shown in graphic ÷ size of effect in data (p. 57, read from the page image); "Lie Factors greater than 1.05 or less than .95 indicate substantial distortion" (p. 57); fuel economy 18 to 27.5 mpg, (27.5 − 18.0)/18.0 = 53%, lines 0.6 and 5.3 in., 783%, Lie Factor 783/53 = 14.8 (pp. 57-58); OPEC design variation 4.69/0.31 = 15.1 (p. 61); barrels 9.4 by area, 59.4 by volume (p. 71); six principles of graphical integrity, first "directly proportional to the numerical quantities represented" (p. 77); data-ink ratio = data-ink ÷ total ink = 1.0 − erasable proportion (p. 93, read from the page image); maximize the data-ink ratio, erase non-data-ink, erase redundant data-ink, each "within reason" (pp. 96, 100); five principles (p. 105); chartjunk introduced (p. 107), "Dark grid lines are chartjunk" (p. 113), the duck (p. 116), "Forgo chartjunk" (p. 121) |
```
