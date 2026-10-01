# Fragment b · S52-R1 intake (papers and statements)

For the conductor to merge into `sources/INDEX.yml`, `check/references/library.bib` and `sources/SOURCES.md`
in one commit. Nine new files, no updates to existing entries. Log: `books/S52-R1/intake/log-b.md`.

**Citekey change from READY.md:** the Herndon, Ash & Pollin file is filed as `herndon_2013_wp322`, not the
proposed `herndon_2014`, because what is held is PERI Working Paper 322 (April 2013, revised), not the 2014
*Cambridge Journal of Economics* article, which could not be opened. The other eight keys are as proposed.
All nine were grepped on 2026-10-02 in `sources/INDEX.yml` and `check/references/library.bib` on this branch
and on `origin/main` (after `git fetch origin`): no match.

## 1. `sources/INDEX.yml`

Nine new entries under `files:`.

```yaml
  ziemann_2016:
    file: ziemann_2016.txt
    what: >-
      Ziemann, Eren & El-Osta, Genome Biol 2016;17:177 (PMC4994289, CC BY 4.0), whole article text from the PMC
      open-access XML except back matter and references: licence, abstract, SEPT2/MARCH1 examples, methods,
      results (35,175 files; 987 files and 704 articles affected; 19.6%; GEO 228 of 574, 39.7%), Table 1 as text,
      Fig. 1 caption, discussion
  herndon_2013_wp322:
    file: herndon_2013_wp322.txt
    what: >-
      Herndon, Ash & Pollin, PERI Working Paper 322 (April 2013, revised after the 17 and 22 April corrections),
      excerpts from the PDF text layer: title page, abstract, sections 1-2 (selective exclusion, the spreadsheet
      coding error with footnote 5 "lines 30 to 44 instead of lines 30 to 49", weighting, transcription error),
      section 4 Conclusion with footnote 9, Tables 2 and 3; plus PERI's page for the paper (summary, linked
      files, correction notes). Section 3, figures and Tables 1 (in block 2), 4, 5, A-1 partly or wholly omitted.
      NOT the Camb J Econ 2014 article, which was not obtained
  phe_2020_delayed:
    file: phe_2020_delayed.txt
    what: >-
      Public Health England, "PHE statement on delayed reporting of COVID-19 cases", GOV.UK news story, 4 Oct
      2020, updated 5 Oct 2020 (OGL v3.0), whole page: both quoted statements, background information with the
      cause ("files ... exceeded the maximum file size"), table of 15,841 cases by date, footer licence line.
      Does not name Excel, a spreadsheet, the .xls format or a row limit
  trisovic_2022:
    file: trisovic_2022.txt
    what: >-
      Trisovic, Lau, Pasquier & Crosas, Sci Data 2022;9:60 (PMC8861064, CC BY 4.0), excerpts from the PMC
      open-access XML: licence, abstract, and Introduction through Best Practices and Recommendations (methods,
      RQ 1-10 with the re-execution table, limitations, recommendations). Related Work, appendices and
      references omitted. Header warns that the abstract's 74%/56% "failed" and the table's 25%/40%/56%
      success rates are on different bases
  peng_2011:
    file: peng_2011.txt
    what: >-
      Peng, Science 2011;334(6060):1226-1227 (PMC3383002), NIH author manuscript, whole text except references:
      fair-use terms statement, abstract, body (replication vs reproducibility, the spectrum, Biostatistics
      kite-marks 21 of 125, proposed steps), Fig. 1 caption. Not open access; quote briefly
  sandve_2013:
    file: sandve_2013.txt
    what: >-
      Sandve, Nekrutenko, Taylor & Hovig, PLoS Comput Biol 2013;9(10):e1003285 (PMC3812051, CC BY), whole text
      except references: licence, introduction, Rules 1-10 each with its "as a minimum" sentence
  wilson_2017:
    file: wilson_2017.txt
    what: >-
      Wilson, Bryan, Cranston, Kitzes, Nederbragt & Teal, PLoS Comput Biol 2017;13(6):e1005510 (PMC5480810,
      CC BY), excerpts: licence, author summary, Overview, Introduction, Box 1, the whole of Data management,
      Software, Collaboration and Project organization (Box 2 "runall" script, Box 3 project layout), the
      opening of Keeping track of changes, Conclusion. Manuscripts and What we left out omitted
  wickham_2014_tidy:
    file: wickham_2014_tidy.txt
    what: >-
      Wickham, J Stat Softw 2014;59(10):1-23 (CC BY per the article page), excerpts from the PDF text layer:
      header, abstract, sections 1-3 (Defining tidy data with the variable/observation definitions and the
      three rules; Tidying messy datasets, the five common problems, 3.1-3.5 with tables as flattened text),
      affiliation and submission dates; plus the article page's licence box. Sections 4-6 omitted
  broman_woo_2018:
    file: broman_woo_2018.txt
    what: >-
      Broman & Woo, "Data organization in spreadsheets": the authors' own manuscript (kbroman.org, from the
      GitHub repository, CC BY), whole text except acknowledgements and references, plus the PeerJ Preprints
      6:e3183v2 page (CC BY; abstract with the twelve principles) and the repository licence line. The
      typeset Am Stat 2018;72(1):2-10 article was NOT obtained; quoted wording is the authors' manuscript
```

## 2. `check/references/library.bib`

Nine new entries.

```bibtex
@article{ziemann_2016,
  title        = {Gene name errors are widespread in the scientific literature},
  author       = {Ziemann, Mark and Eren, Yotam and El-Osta, Assam},
  journal      = {Genome Biology},
  year         = {2016},
  volume       = {17},
  pages        = {177},
  doi          = {10.1186/s13059-016-1044-7},
  note         = {PMID 27552985, PMC4994289. Open access under CC BY 4.0. Quoted from the PMC
                  open-access text},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC4994289/},
  urldate      = {2026-10-02}
}

@techreport{herndon_2013_wp322,
  title        = {Does High Public Debt Consistently Stifle Economic Growth? {A} Critique of
                  {Reinhart} and {Rogoff}},
  author       = {Herndon, Thomas and Ash, Michael and Pollin, Robert},
  institution  = {Political Economy Research Institute, University of Massachusetts Amherst},
  type         = {PERI Working Paper},
  number       = {322},
  year         = {2013},
  month        = apr,
  note         = {Dated 15 April 2013 on its title page; the version quoted includes PERI's
                  corrections of 17 and 22 April 2013. No licence stated for the paper (the
                  authors' code and data are BSD 2-clause). Published in revised form as Cambridge
                  Journal of Economics 38(2):257--279 (2014), doi:10.1093/cje/bet075, which was
                  not consulted},
  url          = {https://peri.umass.edu/publication/does-high-public-debt-consistently-stifle-economic-growth-a-critique-of-reinhart-and-rogoff/},
  urldate      = {2026-10-02}
}

@misc{phe_2020_delayed,
  title        = {{PHE} statement on delayed reporting of {COVID-19} cases},
  author       = {{Public Health England}},
  year         = {2020},
  howpublished = {GOV.UK news story},
  note         = {Published 4 October 2020; last updated 5 October 2020 (background information
                  added). Open Government Licence v3.0. The statement gives the cause as files that
                  exceeded a maximum file size; it does not name the software involved},
  url          = {https://www.gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases},
  urldate      = {2026-10-02}
}

@article{trisovic_2022,
  title        = {A large-scale study on research code quality and execution},
  author       = {Trisovic, Ana and Lau, Matthew K and Pasquier, Thomas and Crosas, Merc{\`e}},
  journal      = {Scientific Data},
  year         = {2022},
  volume       = {9},
  pages        = {60},
  doi          = {10.1038/s41597-022-01143-6},
  note         = {PMID 35190569, PMC8861064. Open access under CC BY 4.0. Quoted from the PMC
                  open-access text},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC8861064/},
  urldate      = {2026-10-02}
}

@article{peng_2011,
  title        = {Reproducible research in computational science},
  author       = {Peng, Roger D},
  journal      = {Science},
  year         = {2011},
  volume       = {334},
  number       = {6060},
  pages        = {1226--1227},
  doi          = {10.1126/science.1213847},
  note         = {PMID 22144613, PMC3383002 (NIH author manuscript, NIHMS382015). Not open
                  access: publisher copyright; the manuscript is free to read and is quoted under
                  fair use},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC3383002/},
  urldate      = {2026-10-02}
}

@article{sandve_2013,
  title        = {Ten simple rules for reproducible computational research},
  author       = {Sandve, Geir Kjetil and Nekrutenko, Anton and Taylor, James and Hovig, Eivind},
  journal      = {PLoS Computational Biology},
  year         = {2013},
  volume       = {9},
  number       = {10},
  pages        = {e1003285},
  doi          = {10.1371/journal.pcbi.1003285},
  note         = {PMID 24204232, PMC3812051. Open access under the Creative Commons Attribution
                  License. Quoted from the PMC open-access text},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC3812051/},
  urldate      = {2026-10-02}
}

@article{wilson_2017,
  title        = {Good enough practices in scientific computing},
  author       = {Wilson, Greg and Bryan, Jennifer and Cranston, Karen and Kitzes, Justin and
                  Nederbragt, Lex and Teal, Tracy K},
  journal      = {PLoS Computational Biology},
  year         = {2017},
  volume       = {13},
  number       = {6},
  pages        = {e1005510},
  doi          = {10.1371/journal.pcbi.1005510},
  note         = {PMID 28640806, PMC5480810. Open access under the Creative Commons Attribution
                  License. Quoted from the PMC open-access text},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC5480810/},
  urldate      = {2026-10-02}
}

@article{wickham_2014_tidy,
  title        = {Tidy data},
  author       = {Wickham, Hadley},
  journal      = {Journal of Statistical Software},
  year         = {2014},
  volume       = {59},
  number       = {10},
  pages        = {1--23},
  doi          = {10.18637/jss.v059.i10},
  note         = {Article licensed CC BY (Creative Commons Attribution, per the journal's article
                  page). Quoted from the article PDF},
  url          = {https://www.jstatsoft.org/article/view/v059i10},
  urldate      = {2026-10-02}
}

@article{broman_woo_2018,
  title        = {Data organization in spreadsheets},
  author       = {Broman, Karl W and Woo, Kara H},
  journal      = {The American Statistician},
  year         = {2018},
  volume       = {72},
  number       = {1},
  pages        = {2--10},
  doi          = {10.1080/00031305.2017.1375989},
  note         = {Quoted from the authors' manuscript (CC BY), published by the first author;
                  the typeset journal article was not consulted and its wording may differ.
                  Preprint: PeerJ Preprints 6:e3183v2, doi:10.7287/peerj.preprints.3183v2 (CC BY 4.0)},
  url          = {https://kbroman.org/Paper_DataOrg/manuscript.html},
  urldate      = {2026-10-02}
}
```

## 3. `sources/SOURCES.md`

Nine new rows for the main table (word counts are of the whole file, `wc -w`, 2026-10-02).

```markdown
| `ziemann_2016.txt` | Ziemann, Eren & El-Osta, *Genome Biol* 2016;17:177 (PMC4994289), CC BY 4.0. **Whole article; back matter and references omitted** | 2,029 | SEPT2 to "2-Sep" and MARCH1 to "1-Mar" "by default"; 18 journals 2005-2015; 35,175 Excel files screened, 7467 gene lists, 3597 papers; errors confirmed in 987 files from 704 articles; "19.6 %" of papers with Excel gene lists; GEO 228 of 574 (39.7 %); 15 % annual increase; Google Sheets did not convert; 166 files with no other identifiers |
| `herndon_2013_wp322.txt` | Herndon, Ash & Pollin, PERI Working Paper 322 (April 2013, revised), PDF text layer, plus PERI's page. No licence for the paper. **Excerpts; the Camb J Econ 2014 article is not held** | 5,710 | "coding errors, selective exclusion of available data, and unconventional weighting of summary statistics"; corrected mean growth above 90% debt/GDP 2.2 percent, not −0.1; spreadsheet error excluded Australia, Austria, Belgium, Canada and Denmark; footnote 5 "RR averaged cells in lines 30 to 44 instead of lines 30 to 49"; New Zealand transcription −7.6 to −7.9; Table 3 effect of each error; footnote 9 "advantages of reproducible code relative to working spreadsheets" |
| `phe_2020_delayed.txt` | Public Health England statement on delayed reporting of COVID-19 cases, GOV.UK, 4 Oct 2020 (updated 5 Oct), OGL v3.0. **Whole page** | 1,330 | 15,841 cases between 25 September and 2 October not included in reported daily cases; 11,968 (over 75%) in the most recent days; cause: "some files containing positive test results exceeded the maximum file size"; mitigation splits large files; table by date sums to 15,841. **Does not name Excel or a row limit** |
| `trisovic_2022.txt` | Trisovic, Lau, Pasquier & Crosas, *Sci Data* 2022;9:60 (PMC8861064), CC BY 4.0. **Excerpts; Related Work, appendices, references omitted** | 8,361 | 2109 replication packages, 9078 R files, Harvard Dataverse 2010-2020; abstract "74% of R files failed ... initial execution, while 56% failed when code cleaning was applied"; RQ 4 table success 25% / 40% / 56% (best of both) with TLE counted apart; code cleaning fixed all setwd errors; library and path errors; renv in 2 packages; recommendations: capture versions (renv or sessionInfo()), relative paths, test in a clean environment |
| `peng_2011.txt` | Peng, *Science* 2011;334:1226-1227 (PMC3383002), NIH author manuscript, fair-use terms. **Whole text; references omitted** | 1,959 | reproducibility "as an attainable minimum standard" when replication is not feasible; same data and code vs independently collected data; spectrum between full replication and no replication (Fig. 1); Biostatistics kite-marks, 21 of 125 articles, five with "R"; reproducible does not guarantee correctness |
| `sandve_2013.txt` | Sandve, Nekrutenko, Taylor & Hovig, *PLoS Comput Biol* 2013;9:e1003285 (PMC3812051), CC BY. **Whole text; references omitted** | 3,273 | Rule 1 keep track of how every result was produced; Rule 2 avoid manual data manipulation; Rule 3 archive exact program versions; Rule 4 version control; Rule 5 record intermediate results; Rule 6 note random seeds; Rule 7 store raw data behind plots; Rule 8 hierarchical output; Rule 9 connect statements to results; Rule 10 public access |
| `wilson_2017.txt` | Wilson et al., *PLoS Comput Biol* 2017;13:e1005510 (PMC5480810), CC BY. **Excerpts; Manuscripts and What we left out omitted** | 6,098 | Box 1 practices; 1a save the raw data, read-only; 1c replace "-99" with NA; 1d tidy data; 1e "write scripts for every stage of data processing"; 1f unique identifiers across tables; 3a README; 3d LICENSE; 3e CITATION; 4a-4f project directories data, results, src, doc; Box 2 "runall" script; Box 3 project layout |
| `wickham_2014_tidy.txt` | Wickham, *J Stat Softw* 2014;59(10):1-23, CC BY (article page). **Excerpts: sections 1-3** | 5,579 | variable and observation defined; "1. Each variable forms a column. 2. Each observation forms a row. 3. Each type of observational unit forms a table."; Codd's 3rd normal form; five common problems (column headers are values; multiple variables in one column; variables in rows and columns; multiple types in one table; one type in multiple tables); melting |
| `broman_woo_2018.txt` | Broman & Woo, "Data organization in spreadsheets": authors' manuscript (CC BY) and PeerJ Preprints 6:e3183v2 page (CC BY 4.0). **Whole manuscript; the typeset Am Stat 2018;72:2-10 text is not held** | 5,553 | the twelve principles (be consistent, YYYY-MM-DD, no empty cells, one thing per cell, a single rectangle with one header row, data dictionary, no calculations in raw files, no colour as data, good names, backups, data validation, plain text); no -999 for missing; Excel dates as day counts from 1900-01-01 or 1904-01-01; Panko 88% of 13 audits; rearrangement "best accomplished via code" |
```
