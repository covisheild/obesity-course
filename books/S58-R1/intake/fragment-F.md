# S58-R1 intake, group F (Flesch Reading Ease: the original coefficient and bands): entries to merge

Three blocks for the conductor to paste into `sources/INDEX.yml` (under `files:`),
`check/references/library.bib` (append) and `sources/SOURCES.md` (a new section). Two files. Citekeys
were grepped in `sources/INDEX.yml`, `check/references/library.bib`, `sources/SOURCES.md`, every
`books/*/intake/fragment-*.md` and `git log --all -S` on 2026-10-02, at the start and at the end of intake:
none exists. Grep again at merge (S47-R1 and S52-R1 are adding keys on other branches). Log:
`books/S58-R1/intake/log-F.md`.

**Merge consequence:** the `kincaid_1975_readability` INDEX entry ends "... print 84.6 per
syllable-per-word: not settled" and its source-file header says Flesch 1948 is "not held". Both can now
point to `flesch_1948_readability_yardstick`: Flesch published .846 per 100 words (84.6 per word); the
Kincaid .836 is best treated as a misprint in the report. That edit is the conductor's to make (this
agent did not touch the Kincaid file or INDEX).

## 1. `sources/INDEX.yml`, under `files:`

```yaml
  flesch_1948_readability_yardstick:
    file: flesch_1948_readability_yardstick.txt
    what: >-
      Flesch, A new readability yardstick, J Appl Psychol 1948;32(3):221-233 (PMID 18867058), NOT the APA
      original: the retyped reprint in DuBay (ed.), The Classic Readability Studies, 2007, ERIC ED506404 (PDF
      text layer; ERIC abstract: reprinted articles "all in the public domain"). Whole article less references:
      Formula A RE = 206.835 - .846 wl - 1.015 sl (wl = syllables per 100 words), untransformed C75 = .0846 wl
      + .1015 sl - 5.6835, Formula B human interest, Tables 1-7 incl. Table 5 Reading Ease bands (reprint prints
      "0 to 20" for Very Difficult), The Formulas Restated steps 1-8. Plus DuBay's introduction (his words: 84.6 x
      ASW restatement, two tables from Flesch 1949). Settles the coefficient: .846/84.6, not Kincaid's .836
  flesch_1979_plain_english:
    file: flesch_1979_plain_english.txt
    what: >-
      Flesch, How to Write Plain English (1979), chapter 2 "Let's Start With the Formula", whole, as reproduced
      on W. H. Starbuck's NYU Stern page, with the formula and grade table also from the Univ. of Canterbury copy
      (Wayback 2017). No licence stated; in-copyright book. Flesch's own words: counting rules for words,
      syllables, sentences; "Multiply the average word length by 84.6"; score to school-grade bands (0-30
      college graduate ... 90-100 5th grade); Plain English minimum 60; scores of 19 publications. Nomogram NOT held
```

## 2. `check/references/library.bib`, append

```bibtex
@article{flesch_1948_readability_yardstick,
  title        = {A New Readability Yardstick},
  author       = {Flesch, Rudolf},
  journal      = {Journal of Applied Psychology},
  year         = {1948},
  month        = jun,
  volume       = {32},
  number       = {3},
  pages        = {221--233},
  doi          = {10.1037/h0057532},
  note         = {PMID 18867058. Quoted from the retyped reprint in W. H. DuBay (ed.), The Classic
                  Readability Studies (Costa Mesa, CA: Impact Information, 2007), pp. 99--111, ERIC
                  ED506404; the ERIC record states the reprinted articles are ``all in the public
                  domain''. The original's page numbers are not shown in the reprint}
}

@book{flesch_1979_plain_english,
  title        = {How to Write Plain English: A Book for Lawyers and Consumers},
  author       = {Flesch, Rudolf},
  year         = {1979},
  publisher    = {Harper \& Row},
  address      = {New York},
  note         = {Chapter 2, ``Let's Start With the Formula'', quoted from web reproductions of the
                  chapter (W. H. Starbuck, NYU Stern; University of Canterbury Department of Management,
                  via the Internet Archive), which give no page numbers and no licence. Publisher and
                  place not stated on those pages: confirm before printing},
  url          = {https://pages.stern.nyu.edu/~wstarbuc/Writing/Flesch.htm},
  urldate      = {2026-10-02}
}
```

## 3. `sources/SOURCES.md`, new section (same columns as the main table)

```markdown
## S58-R1 intake, group F: the Flesch Reading Ease original (2 Oct 2026)

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `flesch_1948_readability_yardstick.txt` | Flesch, *J Appl Psychol* 1948;32:221-233, **retyped reprint** in DuBay (ed.), *The Classic Readability Studies*, 2007, ERIC ED506404 (ERIC: reprints "all in the public domain"). Whole article less references, plus DuBay's introduction (his words) | 8,360 | Formula A "RE = 206.835 - .846 wl - 1.015 sl", wl = syllables per 100 words (Findings, and Step 7 of The Formulas Restated); untransformed "C75 = .0846 wl + .1015 sl - 5.6835", R = .7047; score 100 = fourth grade completed, "barely functionally literate"; 363 McCall-Crabbs passages; Table 5 bands (reprint: "0 to 20" Very Difficult, 30-50 Difficult, 50-60 Fairly difficult, 60-70 Standard, 70-80 Fairly easy, 80-90 Easy, 90-100 Very easy); Tables 4 and 7 worked scores, which reproduce with .846 and not .836; counting rules (contractions and hyphenated words one word; syllables as read aloud) |
| `flesch_1979_plain_english.txt` | Flesch, *How to Write Plain English* (1979), ch. 2, as reproduced on an NYU Stern faculty page (and the Canterbury copy via Wayback). No licence stated. Whole chapter | 2,659 | "Multiply the average sentence length by 1.015. Multiply the average word length by 84.6. Add the two numbers. Subtract this sum from 206.835."; counting rules (Steps 1-6); 0 "practically unreadable", 100 "extremely easy"; Plain English minimum 60; grade bands 90-100 5th grade to 0-30 college graduate; "John loves Mary" 92; 19 publication scores, Internal Revenue Code minus 6 |
```
