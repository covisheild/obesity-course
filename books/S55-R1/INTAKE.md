# Source intake log · S55-R1

One pass on 2026-09-25, before drafting, against the eleven "To obtain at intake" lines and the two
optional lines not marked **Harsh only** in `READY.md`. Every stored passage was fetched with
`mcp__TinyFish__fetch_content`. Each result was taken from the tool's own result record, either the
session transcript or the harness's saved result file for large results. It was decoded from JSON
unchanged and saved to the scratch folder `/home/claude/intake-S55/raw/<citekey>[__part].txt`. Every
passage was cut from that text by script as a contiguous slice (`raw[i:j]`; `build_sources.py` in the
same folder). The written files were then re-parsed, and each `[TEXT]` run was tested as a
whitespace-normalised substring of the raw fetch. The check is `python3 /home/claude/intake-S55/verify.py`,
which the conductor can re-run. No omission falls inside a run. What lies between runs is listed in each
file's header. No WebFetch output is stored anywhere, and nothing was fetched with curl, wget or a Python
HTTP client. The PMIDs, PMCIDs and DOIs of the nine journal articles in PubMed were confirmed with the
PubMed tool (`convert_article_ids`, `get_article_metadata`; Van Noorden by `lookup_article_by_citation`).
Golosovsky & Larivière is not in PubMed. Its DOI is as printed on the PDF.

**Verbatim check: 31 of 31.** That is 25 runs in the twelve new files and 6 in the Blackstone chapter 4
blocks. The twelve runs S36 filed in `blackstone_2012.txt` were not re-checked, because their raw
fetches are S36's. Most runs are whole articles or whole chapters.

**PMC pages were again unreliable for the tool.** Ratan 2019 and Ioannidis 2016 loaded as article
pages, but those pages carry no licence line, so their licences were read in the PMC OA XML. Aslam
2010 and Ioannidis 2014 returned `empty_content` and were taken from the PMC OA XML. Morgan 2018 has no
OA XML (404 for `.1` and `.2`). Europe PMC's REST full text returned HTTP 500, and its article page
redirected to the home page. Europe PMC's `api/getPdf` route gave the author manuscript's text layer.

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Blackstone 2012, **chapter 4** "Beginning a Research Project": introduction and 4.1–4.5, each to its Key Takeaways, exercises omitted; Tables 4.1–4.2 | https://saylordotorg.github.io/text_principles-of-sociological-inquiry-qualitative-and-quantitative-methods/s07-beginning-a-research-project.html (one page holds the whole chapter; markdown, body scope) | 6 | 6/6 | CC BY-NC-SA 3.0 (the book's licence page, already held as block 1) | `blackstone_2012` (extended; append-only, blocks 13–18) |
| Jhangiani et al. 2019, *Research Methods in Psychology* 4e, chapter "Generating Good Research Questions", whole, and the licence block | https://kpu.pressbooks.pub/psychmethods4e/chapter/generating-good-research-questions/ (body scope) | 2 | 2/2 | "Research Methods in Psychology Copyright © 2019 by Rajiv S. Jhangiani, I-Chant A. Chiang, Carrie Cuttler, & Dana C. Leighton is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License, except where otherwise noted." (page) | `jhangiani_2019_methods` (new) |
| CDC, *Principles of Epidemiology in Public Health Practice* 3e (SS1978), Lesson 1 §6 and §7 to the start of their exercises, with each section's references; CDC's reuse page; the course home page's dates | https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson1/section6.html, `.../section7.html`, `.../ss1978/index.html` (body scope); https://www.cdc.gov/other/agencymaterials.html | 6 | 6/6 | **None on the lesson pages.** CDC's own statement: "Most of the information on the CDC and ATSDR websites is not subject to copyright, is in the public domain, and may be freely used or reproduced without obtaining copyright permission." It lists exceptions and four conditions (the "Use of Agency Materials" page, last reviewed 1 May 2023) | `cdc_ss1978_lesson1` (new) |
| Aslam & Emmanuel 2010 *Indian J Sex Transm Dis AIDS* 31:47: licence; abstract, whole body with Table 1 (PICO and FINER), end matter | https://pmc-oa-opendata.s3.amazonaws.com/PMC3140151.1/PMC3140151.1.xml (the PMC page returned no content) | 2 | 2/2 | "© Indian Journal of Sexually Transmitted Diseases and AIDS2010https://creativecommons.org/licenses/by/2.0/This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited." (PMC XML; CC BY 2.0) | `aslam_emmanuel_2010` (new) |
| Morgan et al. 2018 *Environ Int* 121:1027, EPA author manuscript, whole with Table 1 | https://europepmc.org/api/getPdf?pmcid=PMC6908441 (PDF text layer) | 1 | 1/1 | **None stated** in the manuscript: "EPA Public Access / Author manuscript" | `morgan_peco_2018` (new) |
| Ratan, Anand & Ratan 2019 *J Indian Assoc Pediatr Surg* 24:15: licence; whole article without references | https://pmc-oa-opendata.s3.amazonaws.com/PMC6322175.1/PMC6322175.1.xml (licence); https://pmc.ncbi.nlm.nih.gov/articles/PMC6322175/ (text) | 2 | 2/2 | "Copyright: © 2018 Journal of Indian Association of Pediatric Surgeons … distributed under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 License …" (PMC XML) | `ratan_2019` (new) |
| Ioannidis 2016 *PLoS Med* 13:e1002049: licence; whole essay with Tables 1–3, references omitted | https://pmc-oa-opendata.s3.amazonaws.com/PMC4915619.1/PMC4915619.1.xml (licence); https://pmc.ncbi.nlm.nih.gov/articles/PMC4915619/ (text) | 2 | 2/2 | "© 2016 John P. A. Ioannidis … This is an open-access article distributed under the terms of the Creative Commons Attribution License …" (PMC XML; CC BY 4.0) | `ioannidis_2016_useful` (new) |
| Ioannidis et al. 2014 *Lancet* 383:166, HHS author manuscript: rights line; whole body without references | https://pmc-oa-opendata.s3.amazonaws.com/PMC4697939.1/PMC4697939.1.xml (the PMC page returned no content) | 2 | 2/2 | "This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law." (PMC XML). Not an open licence | `ioannidis_2014_waste` (new) |
| Van Noorden 2017 *Nature* 552:162, news feature, whole text layer with its correction | https://media.nature.com/original/magazine-assets/d41586-017-08404-0/d41586-017-08404-0.pdf | 1 | 1/1 | "© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved." (PDF). **All rights reserved** | `van_noorden_2017` (new) |
| Golosovsky & Larivière 2021 *Quant Sci Stud* 2:899, whole article to the data statement | https://umontreal.scholaris.ca/server/api/core/bitstreams/3812c254-b9af-4e69-9656-e6a10b5e031c/content (the published PDF) | 1 | 1/1 | "Copyright: © 2021 Michael Golosovsky and Vincent Larivière. Published under a Creative Commons Attribution 4.0 International (CC BY 4.0) license." (PDF) | `golosovsky_lariviere_2021` (new) |
| Companies Act 2013 s.135 with its amendment footnotes; Schedule VII whole; India Code's terms of use | https://indiacode.gov.in/server/api/core/items/844b5729-0925-4d9c-a9ea-8ba9e43b83b7 (s.135 record); `.../core/bitstreams/ab921e98-1910-4c2c-8cea-05f96e4f5c26/content` (Schedule VII extracted text; the PDF bitstream was also fetched and agrees); https://indiacode.gov.in/info/term-of-use | 4 | 4/4 | India Code Term of Use: "All content … is the property of the Legislative Department … and is protected by Indian and international copyright laws"; "You may access, download, and print materials from this Portal for personal, non-commercial use only" | `companies_act_2013_s135` (new) |
| *Optional.* Farrugia et al. 2010 *Can J Surg* 53:278, whole text layer with Boxes 1–3 | https://europepmc.org/api/getPdf?pmcid=PMC2912019 | 1 | 1/1 | none; the page head reads "© 2010 Association médicale canadienne" | `farrugia_2010` (new) |
| *Optional.* Nowroozzadeh & Salehi-Marzijarani 2019 *J Gen Intern Med* 34:2695, whole letter | https://europepmc.org/api/getPdf?pmcid=PMC6854350 | 1 | 1/1 | none; "© Society of General Internal Medicine 2019" | `nowroozzadeh_2019` (new) |

Citekeys were checked against the local `sources/INDEX.yml` and `check/references/library.bib`, and
against both files on GitHub `main`, fetched on 2026-09-25. None was in use.

## The Companies Act: how it was reached

`www.indiacode.nic.in` (the handle page and the section page) and the MCA PDFs
(`www.mca.gov.in/Ministry/pdf/...`) were unreachable from the tool. MCA's acts page is script-rendered
and names no file. `indiacode.gov.in`, which serves the Constitution and the other Acts already
held, answered, but only through its DSpace REST API. `discover/search/objects` found the section 135
item, handle 123456789/515134, in the SECTION collection. Its text is a metadata field
(`dc.identifier.section_page_note`) and its amendment footnotes another (`section_footnote`). The
Schedule VII item, handle 123456789/511211, holds a PDF and DSpace's own extracted text of it; the
extracted text is filed, because the PDF layer splits words. Last modified on India Code: section 135 on
2026-07-10; Schedule VII's text extracted 2026-07-15. Its footnotes run to Act 29 of 2020 (in force
22-1-2021) and G.S.R. 525(E) of 24 August 2020.

**The Companies (CSR Policy) Rules 2014 were not taken.** `READY.md` asks for them only "if C07 says
anything about what CSR money may fund". Schedule VII is the list of permitted activities. The Rules
add definitions, exclusions and reporting. If C07 goes beyond "Schedule VII lists activities including
health care and research", the Rules must be obtained first. The RULE collection on the same API is the
likely route.

## Findings for the gate

- **C02 (PICO, PECO).** Aslam 2010 carries PICO and FINER together in Table 1, with a worked
  foreground question ("In children with acute otitis media (P), is cefuroxime (I) effective in reducing
  the duration of symptoms (O) as compared to amoxicillin (C)?"). Morgan 2018 has PECO, with five
  scenarios and P/E/C/O examples. Farrugia 2010's Box 2 adds T (time), which gives PICOT. Ratan 2019
  does not use PICO, as `READY.md` said.
- **C03 (question and study design).** CDC §7 names exposure and health outcome, and cohort,
  case-control and cross-sectional studies. It says the cross-sectional study "usually cannot
  disentangle risk factors for occurrence of disease (incidence) from risk factors for survival with the
  disease". Ratan 2019's "Research question and study design" gives an example for each: incidence leads
  to a survey, risk factors to a case-control or cohort study.
- **C04 (feasibility).** Jhangiani lists "time, money, equipment and materials, technical knowledge
  and skill, and access to research participants". Blackstone 4.5 covers identity, access, time and
  money. FINERMAPS (Ratan) and FINER (Aslam, Farrugia) both begin with Feasible.
- **C01 (a good question).** Blackstone 4.4's Key Takeaways gives five features: "written in the form
  of a question, clearly focused, beyond yes/no, more than one plausible answer, and consider
  relationships among concepts". Table 4.2 shows sample questions with their strengths, weaknesses and
  alternatives. The table's multi-line cells are split across rows in the extraction.
- **C06 (uncitedness) must carry its qualifiers.** Van Noorden reports the 1990 *Science* claim ("55%
  of articles published between 1981 and 1985 hadn't been cited in the 5 years after their
  publication"). For biomedical papers the feature's figure is "Of all biomedical-sciences papers
  published in 2006, just 4% are uncited today", on Web of Science. "Today" means the feature's date,
  December 2017. The feature adds that these proportions rise when self-citations are removed. It also
  reports, as "independent calculations from Waltman and Larivière", that papers "with only one or two
  citations outnumber those that have zero". The figures come from a news feature. Their chart data were
  later withdrawn from public view: the PDF prints a correction saying "the data are not available to
  make public". Golosovsky & Larivière give "12% for Medical Sciences to 70% for Arts & Humanities",
  attributed to Sugimoto & Larivière 2018 (not held). Nowroozzadeh 2019 (optional) adds a medical-journal
  figure from Web of Science: mean five-year uncitedness in five top general medical journals fell from
  8.3 (1990 cohort) to 0.7 (2010 cohort).
- **C05 and C07 (usefulness, waste).** Ioannidis 2016's Table 1 and its eight features are held whole.
  Its "85%" figure, if the drafter wants it, is a repetition of another source; `READY.md` already says
  it must come from Chalmers & Glasziou 2009, which is **Harsh only**. Ioannidis 2014 holds "Problem 2:
  poor utility of information" and "Problem 4: insufficient consideration of other evidence" whole.
- **C07 (CSR).** Section 135(5) is held: the two per cent spending rule and its local-area proviso.
  So are the thresholds in 135(1). Schedule VII item (i) includes "promoting health care including
  preventive health". Item (ix) is on research contributions (ICMR is named). The Schedule's own
  misprints are kept.

## Not obtained

| Source | Why | Where Harsh can get it |
| --- | --- | --- |
| Companies (CSR Policy) Rules 2014 | Not needed unless C07 says what CSR money may fund beyond Schedule VII; not attempted | India Code RULE collection, or MCA |
| Morgan 2018 Figure 1; Ratan 2019 Tables 1–2; Golosovsky figures; Van Noorden and Nowroozzadeh charts | Images | The article pages |
| The **Harsh only** optional lines (Patsopoulos 2005, Chalmers & Glasziou 2009, Chalmers et al. 2014, Nicolaisen & Frandsen 2019) | Paywalled; not attempted, as `READY.md` provides | As in `READY.md` |

## Caveats found during intake

- **India Code forbids automated access.** Its Term of Use, updated 22 June 2026 and held in the file,
  asks users to "Not use any automated means to access the Portal for any purpose without our express
  written permission", and permits "personal, non-commercial use only". This intake reached it with an
  automated fetch tool, as earlier intakes did for the Acts already held. The statutory text itself is
  reproducible under s.52(1)(q) of the Copyright Act 1957. That is general knowledge and was not fetched.
  **Conductor, 2026-09-25: withdrawn.** `companies_act_2013_s135` removed from `sources/`, `INDEX.yml`,
  the `.bib` and `SOURCES.md` before commit; the terms are respected, not argued around. C07 names CSR
  as a word only. Acts already held from earlier intakes are raised with Harsh in the handover.
- **Farrugia 2010's running text will fail the quote check** when it is quoted correctly, because spaces
  fall inside words. Boxes 1–3 are clean. Quote the boxes, or copy the file's spacing and have a person
  check it against the PDF.
- **Van Noorden 2017 is all rights reserved.** It is held for audit only: short quotations, no charts.
  Ioannidis 2014 (fair use), Morgan 2018, Farrugia 2010 and Nowroozzadeh 2019 carry no open licence.
- **Aslam 2010's licence is CC BY 2.0**, not the "cc by" of unstated version that `READY.md` recorded.
- **Jhangiani's chapter is numbered 9**, not 2.3, in the Pressbooks edition. Cite it by title.
- **CDC dates.** The lesson pages were last reviewed 18 May 2012. The course home page gives "Book
  originally published: October 2006 / Book updated: November 2011". Several §6 figures are credited to
  outside sources and are images. None is held.
- **The Schedule VII text keeps India Code's misprints** ("slum are development", "including windows",
  "Swatch Bharat Kosh", "(CAPE)"). A quotation must reproduce them or stop short of them.
- **Raw fetches** are in `/home/claude/intake-S55/raw/`, outside the repository, with `build_sources.py`,
  `verify.py` and `manifest.json`.
