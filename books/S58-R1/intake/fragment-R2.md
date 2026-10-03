# S58-R1 intake, group R2 (referencing: NLM Citing Medicine, reports and web pages): entries to merge

Three blocks for the conductor to paste into `sources/INDEX.yml` (under `files:`),
`check/references/library.bib` (append) and `sources/SOURCES.md` (add a row to the group R section, or a
new section). One file. House practice is one citekey per file (`file:` is singular in INDEX.yml), so the
new chapters go under their own key rather than a second file under `nlm_citing_medicine_2007`. The
citekey was grepped in `sources/INDEX.yml`, `check/references/library.bib`, `sources/SOURCES.md`, every
`books/*/intake/fragment-*.md` and `git log --all -S` on 2026-10-02: none exists. Grep again at merge.
Log: `books/S58-R1/intake/log-R2.md`.

## 1. `sources/INDEX.yml`, under `files:`

```yaml
  nlm_citing_medicine_2007_reports_web:
    file: nlm_citing_medicine_2007_reports_web.txt
    what: >-
      NLM, Citing Medicine, 2nd ed. (Patrias K; Wendling D, tech. ed.; 2007-; NCBI Bookshelf NBK7256; public
      domain as stated); same work as nlm_citing_medicine_2007, other chapters. Chapter 4 Scientific and
      Technical Reports, part A (NBK7280): introduction (sponsoring vs performing organisation), element
      order, GENERAL rules for author, title, place, publisher, date, report number; examples 1-3, 11-14, 23.
      Chapter 22 Books and Other Individual Titles on the Internet, part A (NBK7269; covers technical reports
      and fact sheets online): introduction, element order, GENERAL rules for type of medium, place,
      publisher, dates incl. [cited], extent, availability; examples 1, 7-9, 27-28, 49 (technical report on
      the Internet). Chapter 25 Web Sites (NBK7274): part A homepages introduction, element order, GENERAL
      rules, examples 1, 5, 21-22; part B introduction and example 1. Specific-rules boxes and the format
      diagrams (images) NOT held
```

## 2. `check/references/library.bib`, append

```bibtex
@book{nlm_citing_medicine_2007_reports_web,
  title        = {Citing Medicine: The {NLM} Style Guide for Authors, Editors, and Publishers},
  author       = {Patrias, Karen},
  editor       = {Wendling, Dan},
  edition      = {2},
  year         = {2007},
  publisher    = {National Library of Medicine (US)},
  address      = {Bethesda, MD},
  note         = {[Internet]; NCBI Bookshelf ID NBK7256; Dan Wendling, technical editor. Chapter 4,
                  Scientific and Technical Reports (NBK7280); chapter 22, Books and Other Individual
                  Titles on the Internet (NBK7269); chapter 25, Web Sites (NBK7274); each last updated
                  2015 Aug 11. ``This publication is in the public domain.'' Same work as
                  nlm_citing_medicine_2007 (chapter 1)},
  url          = {https://www.ncbi.nlm.nih.gov/books/NBK7256/},
  urldate      = {2026-10-02}
}
```

## 3. `sources/SOURCES.md`, row (same columns as the main table)

```markdown
| `nlm_citing_medicine_2007_reports_web.txt` | NLM, *Citing Medicine*, 2nd ed. (Patrias, 2007-; NBK7256; public domain as stated): chapter 4 (technical reports) part A introduction, element order, general rules, examples 1-3, 11-14, 23; chapter 22 (books and other titles on the Internet) part A introduction, element order, general rules, examples 1, 7-9, 27-28, 49; chapter 25 (web sites) part A introduction, element order, general rules, examples 1, 5, 21-22, part B introduction and example 1 | 7,986 | Online technical reports and fact sheets are cited as Internet books (ch. 22: "Online books are often electronic versions of large printed texts, such as textbooks, manuals, or technical reports, but may also be smaller works such as a brochure, single-page fact sheet"; ch. 4 "See also Chapter 18 and Chapter 22"); ch. 22 ex. 7 "Kaiser Commission on Medicaid and the Uninsured. The uninsured and their access to health care [Internet]. Washington: Henry J. Kaiser Family Foundation; 2006 Oct [cited 2006 Nov 3]. 2 p. Available from: ..."; report: identify sponsoring and performing organisation, "Report No.: "; homepage ex. 21 "MedlinePlus [Internet]. Bethesda (MD): U.S. National Library of Medicine; [1998 Oct] - [updated 2015 May 6; cited 2015 May 6]. Available from: ..."; "Simply adding a Uniform Resource Locator (URL) ... is not sufficient" |
```
