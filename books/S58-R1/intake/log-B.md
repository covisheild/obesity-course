# Source intake log · S58-R1 · group B (numbers and readability)

One pass, 2026-10-02, against the four group-B lines of `READY.md` ("To obtain"): Cole 2015, Lang & Altman
SAMPL, Kincaid et al. 1975, Plavén-Sigray et al. 2017; plus the fallback the brief allowed for the Flesch
formulas. Every fetch was `mcp__TinyFish__fetch_content`. Results too large for the reply were saved by the
harness and decoded from JSON unchanged into `books/S58-R1/intake/raw/B-*.txt`; small replies were re-fetched
in a batch large enough to be saved the same way, so no stored text was retyped. Every passage was cut by
script (`intake/build-B.py`, `raw[i:j]` between anchor strings; cut offsets in `raw/B-cutlog.json`), and the
written source files were then re-parsed from disk by `intake/verify-B.py`, each passage tested as a
whitespace-normalised substring of the raw fetch for the URL in its block heading. No WebFetch output is
stored; nothing was fetched with curl, wget or a Python HTTP client. Identifiers were confirmed with the PubMed
tools (`get_article_metadata`, `convert_article_ids`).

**Verbatim check: 35 of 35** (Cole 5, Plavén-Sigray 20, SAMPL 5, Edwards fallback 5).

**Obtained 3 of 4, plus 1 fallback.** Kincaid 1975 was not obtained.

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Cole TJ, Too many digits, *Arch Dis Child* 2015;100:608-9 (PMID 25877157, PMC4483789). Whole body, Table 1 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4483789.1/PMC4483789.1.xml (markdown; html of the same URL read only for two markup notes on Table 1) | 5 | 5/5 | "This is an Open Access article distributed in accordance with the terms of the Creative Commons Attribution (CC BY 4.0) license ..." (in the XML) | `cole_2015_too_many_digits` (new) |
| Lang & Altman, SAMPL Guidelines: the PDF the EQUATOR page links (2013, Science Editors' Handbook version). Guiding principles; reporting numbers and descriptive statistics; risk, rates and ratios; hypothesis tests | https://www.equator-network.org/wp-content/uploads/2013/07/SAMPL-Guidelines-6-27-13.pdf (text layer, markdown). Library page read for the link: https://www.equator-network.org/reporting-guidelines/sampl/ | 5 | 5/5 | PDF: "This document may be reprinted without charge but must include the original citation." EQUATOR terms of use: materials "may be downloaded or copied provided that ALL copies retain the copyright and any other proprietary notices" | `lang_altman_2013_sampl` (new) |
| Plavén-Sigray P et al., *eLife* 2017;6:e27725 (PMID 28873054, PMC5584989). Excerpts incl. whole Discussion, Tables 1-2, FRE formula (MathML) | https://pmc-oa-opendata.s3.amazonaws.com/PMC5584989.1/PMC5584989.1.xml (markdown for prose and tables; html for the MathML) | 20 (1 MathML) | 20/20 | "This article is distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use and redistribution provided that the original author and source are credited." (XML links CC BY 4.0) | `plavensigray_2017_readability` (new) |
| Kincaid JP, Fishburne RP, Rogers RL, Chissom BS, *Derivation of New Readability Formulas ...*, Research Branch Report 8-75, 1975 | tried: https://apps.dtic.mil/sti/citations/ADA006655 and https://apps.dtic.mil/sti/pdfs/ADA006655.pdf and https://apps.dtic.mil/dtic/tr/fulltext/u2/a006655.pdf; https://eric.ed.gov/?id=ED108134 and https://files.eric.ed.gov/fulltext/ED108134.pdf; https://stars.library.ucf.edu/istlibrary/56/ and its PDF https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=1055&context=istlibrary | 0 | — | not obtained (STARS record: "Not to be used for commercial purposes except by permission.") | none filed |
| **Fallback** for Kincaid: Edwards CS et al., *Surg Neurol Int* 2022;13:401 (PMID 36128118, PMC9479524). FRE bands; FKGL and FRE formulas in words; refs 10, 15 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9479524.1/PMC9479524.1.xml (markdown) | 5 | 5/5 | "Creative Commons Attribution-Non Commercial-Share Alike 4.0 License" (CC BY-NC-SA 4.0, in the XML) | `edwards_2022_readability_formulas` (new) |

## Not obtained: Kincaid et al. 1975

- **DTIC** (ADA006655): the citation page redirected to DTIC's "Under Maintenance" page on 2026-10-02 (two
  tries); both PDF URLs returned `target_unreachable`.
- **ERIC** (ED108134): the record page opened (abstract only; it gives the availability line "National
  Technical Information Service ... (AD-A006 655/5GA ...)" and no full-text link); `files.eric.ed.gov/fulltext/ED108134.pdf`
  returned `target_unreachable` three times, so ERIC probably holds no full text for this record.
- **UCF STARS** (Institute for Simulation and Training, istlibrary/56; the report's own repository record,
  48 pages, table of contents incl. "Appendix B (Instructions for Recalculated Formulas)"): terms read first
  (STARS FAQ: "Materials may be downloaded for education and research purposes provided due recognition is
  given to the author"; robots.txt does not exclude `/cgi/viewcontent.cgi`; the Elsevier/Digital Commons terms
  bar continuous automated scraping, not a single fetch). The PDF returned `empty_content` twice (markdown and
  html): almost certainly a scan with no text layer. Nothing from it is stored.
- **What Harsh would need:** download the PDF from https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=1055&context=istlibrary
  (or from DTIC, https://apps.dtic.mil/sti/citations/ADA006655, once maintenance ends) and put it in `sources/`.
  It is a scan, so the formulas (the recalculated Flesch Reading Ease and the grade-level formula, Appendix B
  and the Results) must be copied by a person from the page images and checked by a second reader; no OCR text
  should be trusted unchecked. Suggested key when it arrives: `kincaid_1975_readability` (not yet in INDEX or .bib).
- **Until then:** C10's formulas stand on the fallback (Edwards 2022, both formulas and the seven bands, a
  secondary restatement) and on Plavén-Sigray 2017 (FRE formula as MathML, and "A FRE score of 100 ... 10- to
  11-year old. A score between 0 and 30 ... college graduates", citing Flesch 1948 and Kincaid 1975). Neither is
  the original. Why Edwards: of ten open PMC readability papers fetched and searched, it was the one with both
  formulas in prose, the constant 15.59 (PMC5690750 prints 15.39; PMC10761760 prints 1015 for 1.015), and the
  full seven-band scale. Its FKGL callout "[10,13]" points to an unrelated ref. 13, so it is not cited for who
  derived FKGL.

## Things a drafter or Harsh should know

1. **SAMPL is held from the 2013 EQUATOR PDF, not the 2015 journal article** (Int J Nurs Stud 52:5-9, Elsevier,
   not opened). The key is `lang_altman_2013_sampl`; READY.md lists the 2015 citation. If the book must cite the
   journal version, someone has to open it and compare wording. Licence is not CC: reprint "without charge" with
   the citation.
2. **Cole and SAMPL disagree on p values.** SAMPL: P values "to one or two decimal places", smallest "P <0.001".
   Cole: "Round up to one significant digit", "The lower limit may be smaller than 0.001, but never 0.000", and
   he names decimal-places rules for p values as the kind that fails. C08 should present the difference, not
   blend the two.
3. **Cole's Table 1** is laid out in the XML with each statistic's further examples as one-cell rows; a [NOTE]
   in the file says how to read it. Two superscripts are lost ("χs=4.1" is χ<sup>s</sup> in the XML, likely a typo
   for χ²; "6.10−9" is 6.10<sup>−9</sup>). Reference callouts run into Cole's prose as bare digits.
4. **Plavén-Sigray exponents are flattened**: "p <10-15" is p < 10^−15.
5. Raw files of the Kincaid attempt keep the names `B-kincaid_1975_readability-*` (terms pages only; no report
   text). The first html fetch of the SAMPL PDF is kept as `raw/B-lang_altman_2013_sampl-pdf-html.txt` but not
   quoted: it encodes "<" and the apostrophe as HTML entities.

Files: `sources/cole_2015_too_many_digits.txt`, `sources/lang_altman_2013_sampl.txt`,
`sources/plavensigray_2017_readability.txt`, `sources/edwards_2022_readability_formulas.txt`; entries to
merge in `books/S58-R1/intake/fragment-B.md`. Nothing committed; INDEX.yml, library.bib and SOURCES.md not
edited.
