# Source intake log · S52-R1 · group b (papers and statements)

One pass, 2026-10-02. Every stored passage was cut by script (`books/S52-R1/intake/build-b.py`) as `raw[i:j]`
between literal anchors from a saved `mcp__TinyFish__fetch_content` result. Each result was saved by the
harness to a file, decoded from JSON unchanged, and its `text` field written to `books/S52-R1/intake/raw/`
(with a `.meta.json` beside it recording the URL fetched). The written source files were then re-parsed by
`books/S52-R1/intake/verify-b.py`, which tests each passage as a whitespace-normalised substring of the raw
file named in its block heading and checks that the heading's URL is that raw file's URL. No WebFetch output
is stored; nothing was fetched with curl, wget or a Python HTTP client. Identifiers and bibliographic details
were confirmed with the PubMed tools (`convert_article_ids`, `get_article_metadata`) and, for the three
non-PubMed works, from their Crossref records (fetched with TinyFish; raw saved as `*-crossref*.txt`).
Passage list with character counts: `books/S52-R1/intake/manifest-b.json`.

**Verbatim check: 26 of 26.**

| Source | URL fetched (stored passages) | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Ziemann, Eren & El-Osta 2016 *Genome Biol* 17:177 (PMID 27552985, PMC4994289) | https://pmc-oa-opendata.s3.amazonaws.com/PMC4994289.1/PMC4994289.1.xml | 2 | 2/2 | "distributed under the terms of the Creative Commons Attribution 4.0 International License" | `ziemann_2016` |
| Herndon, Ash & Pollin, PERI Working Paper 322 (April 2013, revised) | https://peri.umass.edu/images/WP322.pdf (PDF text layer; served from PERI's server at 64.225.7.238); https://peri.umass.edu/publication/does-high-public-debt-consistently-stifle-economic-growth-a-critique-of-reinhart-and-rogoff/ | 5 | 5/5 | none stated for the paper; PERI page: "Code and data are open-source under the BSD 2-clause license" (code/data package only) | `herndon_2013_wp322` (**not** `herndon_2014`) |
| Public Health England, statement on delayed reporting of COVID-19 cases, GOV.UK, 4 Oct 2020 (updated 5 Oct) | https://www.gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases (default extraction for the page; body-scoped extraction for the footer) | 2 | 2/2 | "All content is available under the Open Government Licence v3.0, except where otherwise stated" / "© Crown copyright" (page footer) | `phe_2020_delayed` |
| Trisovic, Lau, Pasquier & Crosas 2022 *Sci Data* 9:60 (PMID 35190569, PMC8861064) | https://pmc-oa-opendata.s3.amazonaws.com/PMC8861064.1/PMC8861064.1.xml | 2 | 2/2 | "licensed under a Creative Commons Attribution 4.0 International License" | `trisovic_2022` |
| Peng 2011 *Science* 334(6060):1226-1227 (PMID 22144613, PMC3383002, NIH author manuscript) | https://pmc-oa-opendata.s3.amazonaws.com/PMC3383002.1/PMC3383002.1.xml | 3 | 3/3 | "This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law." No open licence | `peng_2011` |
| Sandve, Nekrutenko, Taylor & Hovig 2013 *PLoS Comput Biol* 9(10):e1003285 (PMID 24204232, PMC3812051) | https://pmc-oa-opendata.s3.amazonaws.com/PMC3812051.1/PMC3812051.1.xml | 2 | 2/2 | "© 2013 Sandve et al ... distributed under the terms of the Creative Commons Attribution License" (XML licence link CC BY 4.0) | `sandve_2013` |
| Wilson, Bryan, Cranston, Kitzes, Nederbragt & Teal 2017 *PLoS Comput Biol* 13(6):e1005510 (PMID 28640806, PMC5480810) | https://pmc-oa-opendata.s3.amazonaws.com/PMC5480810.1/PMC5480810.1.xml | 4 | 4/4 | "© 2017 Wilson et al ... distributed under the terms of the Creative Commons Attribution License" (XML licence link CC BY 4.0) | `wilson_2017` |
| Wickham 2014 *J Stat Softw* 59(10):1-23 | https://www.jstatsoft.org/index.php/jss/article/view/v059i10/772 (PDF text layer); https://www.jstatsoft.org/article/view/v059i10 (body-scoped, licence box) | 3 | 3/3 | "Article: Creative Commons Attribution License (CC-BY)"; page links CC BY 3.0; metadata dc.rights "Copyright (c) 2013 Hadley Wickham" | `wickham_2014_tidy` |
| Broman & Woo, "Data organization in spreadsheets" (Am Stat 2018;72(1):2-10; PeerJ Preprints 6:e3183v2) | https://kbroman.org/Paper_DataOrg/manuscript.html (authors' manuscript); https://peerj.com/preprints/3183v2.html; https://github.com/kbroman/Paper_DataOrg/blob/master/LICENSE.md | 3 | 3/3 | preprint: "open access article distributed under the terms of the Creative Commons Attribution License" (Crossref: CC BY 4.0); repository: 'The manuscript "Data organization in spreadsheets" is licensed under CC BY' | `broman_woo_2018` |

Obtained: **9 of 9** works in usable form. Two with qualifications: Herndon et al. is the **working paper**, not
the journal article; Broman & Woo is the **authors' manuscript**, not the typeset journal article.

## Bibliographic details confirmed (READY.md wrote six from memory)

| Work | READY.md said | Confirmed from | Result |
| --- | --- | --- | --- |
| Wickham 2014 | *J Stat Softw* 2014;59(10):1-23 | PDF header ("August 2014, Volume 59, Issue 10"), article-page metadata (pages "1 - 23"), Crossref | correct |
| Broman & Woo 2018 | *Am Stat* 2018;72(1):2-10; PeerJ 6:e3183v2 | Crossref for both DOIs; manuscript title block (Karl W. Broman, Kara H. Woo) | correct. Note: kbroman.org/dataorg says "The American Statistician 78:2–10", a typo on that page; Crossref and the repository README give 72 |
| Herndon, Ash & Pollin 2014 | *Camb J Econ* 2014;38(2):257-279 | Crossref (authors T. Herndon, M. Ash, R. Pollin; issue 2; pages 257-279; online 24 Dec 2013) | correct; but that article is not held (see below) |
| Peng 2011 | *Science* 2011, volume and pages to confirm | PubMed: 334(6060):1226-7, 2 Dec 2011 | 334(6060):1226-1227 |
| Sandve et al. 2013 | *PLoS Comput Biol* 9(10):e1003285, four authors | PubMed and XML header | correct |
| Wilson et al. 2017 | *PLoS Comput Biol* 13(6):e1005510, six authors | PubMed and XML header | correct (Greg Wilson, Jennifer Bryan, Karen Cranston, Justin Kitzes, Lex Nederbragt, Tracy K. Teal) |
| Ziemann et al. 2016 | *Genome Biol* 17:177 | PubMed | correct (article type Comment) |
| Trisovic et al. 2022 | *Sci Data* 9:60, author list to confirm | PubMed and XML header | correct (Ana Trisovic, Matthew K. Lau, Thomas Pasquier, Mercè Crosas) |

## What was not obtained, and what Harsh would download

Nothing blocks the gate for group b: every concept's claim has an opened source. Two published versions were
not reached, and C01/C08/C09/C10/C15 must cite the versions that are held.

| Not obtained | Tried (2026-10-02) | Why | If Harsh wants it |
| --- | --- | --- | --- |
| Herndon, Ash & Pollin, *Cambridge Journal of Economics* 38(2):257-279 (2014), the published article | https://academic.oup.com/cje/article/38/2/257/1714018 (bot_blocked); http://academic.oup.com/cje/article-pdf/38/2/257/4790811/bet075.pdf (target_unreachable) | publisher blocks automated access; subscription article | download the PDF in a browser from https://doi.org/10.1093/cje/bet075 (needs institutional access) and put it in `sources/`. **Not needed for C01**: the working paper carries the spreadsheet error, the exclusions, the weighting and the corrected 2.2 vs −0.1 percent |
| Broman & Woo, *The American Statistician* 72(1):2-10 (2018), typeset article | https://www.tandfonline.com/doi/full/10.1080/00031305.2017.1375989 (bot_blocked); preprint PDF https://peerj.com/preprints/3183v2.pdf (target_unreachable) | publisher blocks automated access; PeerJ PDF unreachable | only if exact journal wording is wanted: https://www.tandfonline.com/doi/pdf/10.1080/00031305.2017.1375989, or the PeerJ preprint PDF https://peerj.com/preprints/3183v2.pdf. The authors' manuscript held here has every principle and section |

## Findings the conductor and writers should know

- **PHE does not name Excel.** The statement's cause is "some files containing positive test results exceeded
  the maximum file size that takes these data files and loads then into central systems" (sic, "then"). No
  passage in any group-b file supports "Excel", ".xls", "65,536 rows" or "row limit" for the PHE failure.
  The header says so. The table's daily counts sum to 15,841 and its last three rows to 11,968 (checked by
  arithmetic on the held figures). The page gives two date ranges: "between 25 September and 2 October" in
  the statements and "between 24 September and 1 October" for the Pillar 2 positives (table by recorded date
  24/09 to 01/10, reported dates 25/09 to 02/10); C01 should use the statement's wording and say which range.
- **Trisovic 2022: the abstract and the results table are on different bases.** Abstract: "74% of R files
  failed to complete without error in the initial execution, while 56% failed when code cleaning was
  applied". RQ 4 table: success rate 25% without cleaning, 40% with cleaning, 56% "best of both", with
  time-limit-exceeded files counted separately (TLE: 3829, 3719, 5790 files). The 56% in the abstract
  ("failed") and the 56% in the table (success, best of both) are not the same quantity, and 1 − 40% is 60%,
  not 56%. The inventory's C20 wording ("74% failed ... and 56% after automatic code cleaning") matches the
  abstract; C20 should quote the abstract sentence as the authors' summary and, if it uses the table, quote
  its labelled cells. This file does not reconcile them; it is a question for the C20 writer and auditor.
- **Herndon: the spreadsheet error is specific and quotable.** "A coding error in the RR working spreadsheet
  entirely excludes five countries, Australia, Austria, Belgium, Canada, and Denmark" with footnote 5 "RR
  averaged cells in lines 30 to 44 instead of lines 30 to 49." The paper attributes most of the gap to the
  exclusions and weighting, not the spreadsheet error: "The exclusion of years coupled with the country—as
  opposed to country-year—weighting alone accounts for almost −2 percentage points ... The spreadsheet and
  transcription errors account for an additional −0.4 percentage point." C01 should not imply the spreadsheet
  slip alone overturned the result. The PDF's date line reads 15 April 2013 but the text includes the 17 and
  22 April revisions.
- **Ziemann's scope.** The paper says Excel "when used with default settings" converts symbols, and that
  LibreOffice Calc and OpenOffice Calc also cannot permanently disable date conversion. "About one-fifth" is
  the abstract's phrase; the result is "19.6 %" of papers with Excel gene lists in the 18 journals screened.
- **Broman & Woo carry Ziemann as "~20% of gene lists"**, which differs from Ziemann's own unit (papers with
  supplementary Excel gene lists). Cite Ziemann directly for the figure.
- **Peng's terms are restrictive** (fair use; publisher copyright). Quote briefly. The "spectrum" figure is an
  image; only the caption and the body's description are held.
- **Herndon key.** Filed as `herndon_2013_wp322` so that the key names the document held; the conductor
  should update READY.md and the C01 inventory row (which name "Herndon, Ash & Pollin 2014 *Camb J Econ*
  38:257, or PERI WP 322 (2013)") to cite the working paper.
- **Raw files for this group** (all under `books/S52-R1/intake/raw/`): `ziemann_2016-pmcxml`, `herndon_2013_wp322-pdf`,
  `herndon_2013_wp322-peripage`, `herndon_2013_wp322-crossref-cje`, `phe_2020_delayed-govuk`,
  `phe_2020_delayed-govuk-body`, `trisovic_2022-pmcxml`, `peng_2011-pmcxml`, `sandve_2013-pmcxml`,
  `wilson_2017-pmcxml`, `wickham_2014_tidy-jsspdf`, `wickham_2014_tidy-jsspage`, `wickham_2014_tidy-jsspage-body`,
  `wickham_2014_tidy-crossref`, `broman_woo_2018-manuscripthtml`, `broman_woo_2018-manuscripthtml-body`,
  `broman_woo_2018-peerjv2html`, `broman_woo_2018-peerjpage`, `broman_woo_2018-peerjpage-body`,
  `broman_woo_2018-githublicense`, `broman_woo_2018-githubrepo`, `broman_woo_2018-tutorialhome`,
  `broman_woo_2018-crossref`, `broman_woo_2018-crossref-preprint` (each `.txt`, most with `.meta.json`). Only those
  named in block headings back stored passages; the rest record licence and identifier checks.
