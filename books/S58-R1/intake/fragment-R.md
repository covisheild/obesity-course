# S58-R1 intake, group R (referencing: NLM Citing Medicine, journal articles): entries to merge

Three blocks for the conductor to paste into `sources/INDEX.yml` (under `files:`),
`check/references/library.bib` (append) and `sources/SOURCES.md` (a new section). One file. The citekey
was grepped in `sources/INDEX.yml`, `check/references/library.bib`, `sources/SOURCES.md`, every
`books/*/intake/fragment-*.md` and `git log --all -S` on 2026-10-02, at the start and at the end of intake:
none exists. Grep again at merge (S47-R1 and S52-R1 are adding keys on other branches). Log:
`books/S58-R1/intake/log-R.md`.

## 1. `sources/INDEX.yml`, under `files:`

```yaml
  nlm_citing_medicine_2007:
    file: nlm_citing_medicine_2007.txt
    what: >-
      NLM, Citing Medicine, 2nd ed. (Patrias K; Wendling D, tech. ed.; 2007-; NCBI Bookshelf NBK7256; public
      domain as stated). Chapter 1 Journals, part A (journal articles; last update 18 May 2018): introduction
      ("Cite the version you saw"), ordered list of required and optional elements, GENERAL rules for author,
      article title, journal title, date, volume, issue, pagination; examples 1-4 (standard article, many
      authors, limit to 3 or 6 then et al., organisation as author) and 69-71 (epub ahead of print, PMID, DOI).
      Appendix B opening (ISO 4; NLM Catalog first for abbreviations). Plus a separate NLM page, Samples of
      Formatted References (intro, item 1, item 34 forthcoming and preprints). Specific-rules boxes, the
      format diagram (an image) and other chapters NOT held
```

## 2. `check/references/library.bib`, append

```bibtex
@book{nlm_citing_medicine_2007,
  title        = {Citing Medicine: The {NLM} Style Guide for Authors, Editors, and Publishers},
  author       = {Patrias, Karen},
  editor       = {Wendling, Dan},
  edition      = {2},
  year         = {2007},
  publisher    = {National Library of Medicine (US)},
  address      = {Bethesda, MD},
  note         = {[Internet]; NCBI Bookshelf ID NBK7256; Dan Wendling, technical editor. Chapter 1,
                  Journals (NBK7282), last updated 2018 May 18. ``This publication is in the public
                  domain.'' Also quoted: NLM, Samples of Formatted References for Authors of Journal
                  Articles (web page, last reviewed 2026 Jun 2)},
  url          = {https://www.ncbi.nlm.nih.gov/books/NBK7256/},
  urldate      = {2026-10-02}
}
```

## 3. `sources/SOURCES.md`, new section (same columns as the main table)

```markdown
## S58-R1 intake, group R: citing and referencing (2 Oct 2026)

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `nlm_citing_medicine_2007.txt` | NLM, *Citing Medicine*, 2nd ed. (Patrias, 2007-; NBK7256; public domain as stated): chapter 1 part A (journal articles) introduction, element order, general rules, examples 1-4 and 69-71; appendix B opening; plus NLM's Samples of Formatted References (intro, items 1 and 34) | 2,609 | Example "Petitti DB, Crooks VC, Buckwalter JG, Chiu V. Blood pressure levels before dementia. Arch Neurol. 2005 Jan;62(1):112-6."; surname first, "a maximum of two initials", "Give all authors, regardless of the number"; optional limit to 3 or 6 then "et al."; capitalise only the first word and proper nouns of an article title; abbreviate journal titles (ISO 4; NLM Catalog first); "123-125 becomes 123-5"; "Cite the version you saw"; BMJ cited as Br Med J before 1988; preprints marked "[Preprint]"; Sample References: "List the first six authors, followed by et al." |
```
