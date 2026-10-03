# Intake fragment, group d (material Harsh supplied, 2 Oct 2026) · S52-R1

For the main thread to merge into `sources/INDEX.yml`, `check/references/library.bib` and `sources/SOURCES.md`.
Four new citekeys: `herndon_2014_cje`, `bruford_2020_hgnc`, `nmc_pg_md_community_medicine`,
`nchs_nhanes_2021_2023_bmx_demo`; plus two data files, `sources/data/BMX_L.xpt` and `sources/data/DEMO_L.xpt`
(byte for byte, MD5 checked after copying). None of the four keys occurs in `sources/INDEX.yml` or
`check/references/library.bib` on this branch or on `origin/main` (951b18a, grepped after `git fetch origin`,
2026-10-02), nor in the other group fragments. The four `sources/*.txt` files are written by
`books/S52-R1/intake/build-d/build.py` and rechecked by `build-d/verify.py` (31/31 passages, 52/52 header
quotes, 31/31 manifest offsets). The working paper stays filed as `herndon_2013_wp322`.

**One edit to an existing entry is suggested, not made:** the `herndon_2013_wp322` .bib note ends "...
doi:10.1093/cje/bet075, which was not consulted"; the journal article is now held as `herndon_2014_cje`, so the
note could end "..., filed as herndon_2014_cje". The working paper remains the source for its footnote 9
("the advantages of reproducible code relative to working spreadsheets"), which the journal article does not
contain.

## 1. `sources/INDEX.yml`

Four new entries under `files:`.

```yaml
  herndon_2014_cje:
    file: herndon_2014_cje.txt
    what: >-
      Herndon, Ash & Pollin, Camb J Econ 2014;38(2):257-279 (doi:10.1093/cje/bet075), the published article,
      from the PDF Harsh supplied (text layer, pdftotext -layout): title page with abstract and copyright line,
      sections 1-3.7 without a break (selective exclusion of Australia, Canada and New Zealand years; the
      spreadsheet coding error excluding Australia, Austria, Belgium, Canada and Denmark, footnote 9 "lines
      30–44 instead of lines 30–49"; weighting by country means; Tables 1-7: corrected >90% mean +2.2% vs RR
      −0.1%, medians 1.6 / 2.3 / 2.5) and section 4 Conclusion whole. Section 3.8, Figures 2-5, Table 8,
      bibliography and Table A1 omitted. Publisher copyright, all rights reserved
  bruford_2020_hgnc:
    file: bruford_2020_hgnc.txt
    what: >-
      Bruford et al., Guidelines for human gene nomenclature, Nat Genet 2020;52:754-758
      (doi:10.1038/s41588-020-0669-3), from the PDF Harsh supplied: p. 754 whole (introduction, Box 1, gene
      definition), Box 3 whole ("all symbols that autoconverted to dates in Microsoft Excel have been changed
      (for example, SEPT1 is now SEPTIN1; MARCH1 is now MARCHF1)"), "Nomenclature updates" with gene-symbol
      usage and HGNC ID, affiliations and DOI, and the metadata copyright line (© 2020 Springer Nature America)
  nmc_pg_md_community_medicine:
    file: nmc_pg_md_community_medicine.txt
    what: >-
      Guidelines for competency based postgraduate training programme for MD in Community Medicine (PDF on
      nmc.org.in; pages watermarked Medical Council of India; undated, no version; PDF made 2 May 2019), from the
      PDF Harsh supplied: title, preamble, subject-specific objectives 1-3 (3: "conduct data collection and
      management, data analysis and report"), psychomotor domain whole and miscellaneous skills 1-8, course
      contents item 3 with objectives i-vi (vi: SPSS, Epi-info, MS office), opening of the summative assessment
  nchs_nhanes_2021_2023_bmx_demo:
    file: nchs_nhanes_2021_2023_bmx_demo.txt
    what: >-
      NHANES August 2021-August 2023, BMX_L (Body Measures) and DEMO_L (Demographics and Sample Weights): the
      script-recorded facts of the two data files held at data/BMX_L.xpt and data/DEMO_L.xpt (haven 2.5.4:
      8860 x 22 and 11933 x 27; MD5; labels; NA counts; join on SEQN, 6064 BMX rows aged 20+), the comparison
      of all 155 printed codebook rows with the data (all agree), both codebooks whole from Harsh's printouts
      of the CDC pages (documentation, analytic notes, every variable's code table), the data-page rows listing
      the files, and the NCHS Data User Agreement (17 Sep 2024)
```

## 2. `check/references/library.bib`

```bibtex
@article{herndon_2014_cje,
  title        = {Does High Public Debt Consistently Stifle Economic Growth? {A} Critique of
                  {Reinhart} and {Rogoff}},
  author       = {Herndon, Thomas and Ash, Michael and Pollin, Robert},
  journal      = {Cambridge Journal of Economics},
  year         = {2014},
  volume       = {38},
  number       = {2},
  pages        = {257--279},
  doi          = {10.1093/cje/bet075},
  note         = {Advance Access publication 24 December 2013. Copyright as printed: The Author
                  2013, published by Oxford University Press on behalf of the Cambridge Political
                  Economy Society, all rights reserved; no licence to reuse. Revised version of PERI
                  Working Paper 322 (herndon_2013_wp322); wording and some numbers differ. Issue
                  number from Crossref (not printed on the PDF). Text from a PDF supplied by the
                  author of this course, 2 October 2026},
  url          = {https://doi.org/10.1093/cje/bet075}
}

@article{bruford_2020_hgnc,
  title        = {Guidelines for Human Gene Nomenclature},
  author       = {Bruford, Elspeth A. and Braschi, Bryony and Denny, Paul and Jones, Tamsin E. M.
                  and Seal, Ruth L. and Tweedie, Susan},
  journal      = {Nature Genetics},
  year         = {2020},
  volume       = {52},
  pages        = {754--758},
  doi          = {10.1038/s41588-020-0669-3},
  note         = {Comment, published online 3 August 2020 (August 2020 issue; issue number not
                  printed). No copyright or licence line on the pages; the PDF's metadata reads
                  2020 Springer Nature America, Inc. Not open access. Box 3 gives the renaming of
                  symbols that autoconverted to dates in Microsoft Excel (SEPT1 to SEPTIN1, MARCH1
                  to MARCHF1). Text from a PDF supplied by the author of this course, 2 October 2026},
  url          = {https://doi.org/10.1038/s41588-020-0669-3}
}

@misc{nmc_pg_md_community_medicine,
  title        = {Guidelines for Competency Based Postgraduate Training Programme for {MD} in
                  Community Medicine},
  author       = {{National Medical Commission}},
  year         = {n.d.},
  note         = {Undated; no version or issuing body named in the text. The pages carry a Medical
                  Council of India watermark and seal; the PDF file was made on 2 May 2019. Hosted
                  on the National Medical Commission website. No licence stated},
  howpublished = {National Medical Commission},
  url          = {https://nmc.org.in/storage/new/MD-Community-Medicine.pdf},
  urldate      = {2026-10-02}
}

@misc{nchs_nhanes_2021_2023_bmx_demo,
  title        = {National Health and Nutrition Examination Survey, August 2021--August 2023: Body
                  Measures ({BMX_L}) and Demographic Variables and Sample Weights ({DEMO_L}), Data
                  Files and Documentation},
  author       = {{National Center for Health Statistics}},
  year         = {2024},
  note         = {Centers for Disease Control and Prevention. Data files BMX_L.xpt and DEMO_L.xpt
                  (SAS transport) and their codebooks, first published September 2024, last revised
                  NA. Use governed by the NCHS Data User Agreement (17 September 2024): statistical
                  reporting and analysis only, no attempt to identify any person, no linkage with
                  identifiable data; no copyright or licence stated. Files downloaded and codebook
                  pages printed by the author of this course, 2 October 2026},
  howpublished = {NCHS},
  url          = {https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Examination&Cycle=2021-2023},
  urldate      = {2026-10-02}
}
```

## 3. `sources/SOURCES.md`

Rows for the table (after the group b-c rows):

```markdown
| `herndon_2014_cje.txt` | Herndon, Ash & Pollin, *Camb J Econ* 2014;38(2):257-279, the published article, text layer of the PDF Harsh supplied (pdftotext -layout). Publisher copyright, all rights reserved. **Excerpts: sections 1-3.7 and 4; section 3.8, bibliography and appendix omitted** | 9,924 | "(i) selective exclusion of available data, (ii) coding errors and (iii) inappropriate methods for the weighting of summary statistics"; "above 90% averaged 2.2% real annual GDP growth, not −0.1% as published"; spreadsheet coding error "unintentionally excludes five countries entirely (Australia, Austria, Belgium, Canada and Denmark)"; footnote 9 means and medians of "lines 30–44 instead of lines 30–49" (1946-2009) and "lines 5–19 instead of lines 5–24" (1790-2009); Table 2 country-years 110 / 96 / 71; New Zealand 1951 −7.6%, transcribed −7.9%; Table 4 RR −0.1% vs +2.2%; Table 5 every combination of the errors; Table 7 medians 1.6 (RR) / 2.3 (HAP) / 2.5 (RR Errata); conclusion: RR acknowledged the spreadsheet errors. **Has no counterpart to the working paper's footnote 9 on reproducible code** |
| `bruford_2020_hgnc.txt` | Bruford et al., Guidelines for human gene nomenclature, *Nat Genet* 2020;52:754-758, text layer of the PDF Harsh supplied. No licence; metadata © 2020 Springer Nature America. **Excerpts: p. 754, Box 3, Nomenclature updates** | 2,499 | Box 3 "Symbols that affect data handling and retrieval. For example, all symbols that autoconverted to dates in Microsoft Excel have been changed (for example, SEPT1 is now SEPTIN1; MARCH1 is now MARCHF1)"; stability of symbols "a key priority"; quote the HGNC ID. **Does not name SEPT2, give a date or count, or use the word "spreadsheet"** |
| `nmc_pg_md_community_medicine.txt` | Guidelines for competency based postgraduate training programme for MD in Community Medicine, PDF on nmc.org.in (MCI watermark), text layer of the copy Harsh supplied. Undated; no licence. **Excerpts** | 1,896 | objective 3 "conduct data collection and management, data analysis and report"; psychomotor "Do data collection, compilation, tabular and graphical presentation, analysis and interpretation, applying appropriate statistical tests, using computer-based software application for validation of findings"; course contents 3(v) data, information & intelligence, types of data; 3(vi) "SPSS, Epi-info, MS office and other advanced versions"; COVERAGE.md lines 15-18 quotes all found |
| `nchs_nhanes_2021_2023_bmx_demo.txt` | NHANES August 2021-August 2023, BMX_L and DEMO_L: script-recorded facts of the two data files, both codebooks whole (from Harsh's printouts of the CDC pages), the data-page rows and the NCHS Data User Agreement. No copyright or licence stated; DUA terms. **Codebooks whole** | 11,227 | BMX_L 8860 rows x 22 columns, DEMO_L 11933 x 27 (haven 2.5.4); NA: BMXWT 106, BMXHT 361, BMXBMI 389, BMXWAIST 670; all 8860 BMX SEQNs in DEMO_L; 6064 BMX rows with RIDAGEYR >= 20; RIDSTATR 3073 interviewed only / 8860 examined; RIAGENDR 5575 / 6358; RIDAGEYR 0-80, 80 = "80 years of age and over" (525); BMI "weight in kilograms divided by height in meters squared, and then rounded to one decimal place"; all 155 printed code-table rows agree with the data; sample weights "should be used"; DUA "statistical reporting and analysis only" |
| `data/BMX_L.xpt` | The NHANES 2021-2023 Body Measures data file itself (SAS transport), downloaded by Harsh from https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.xpt on 2 Oct 2026 and copied byte for byte. NCHS Data User Agreement. Described in `nchs_nhanes_2021_2023_bmx_demo.txt`; cite that key | 1,563,200 bytes | MD5 ab25a36296e5b61881d42fef61c06b84; 8860 rows, 22 columns (read_xpt, haven 2.5.4) |
| `data/DEMO_L.xpt` | The NHANES 2021-2023 Demographic Variables and Sample Weights data file itself (SAS transport), downloaded by Harsh from https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt on 2 Oct 2026 and copied byte for byte. NCHS Data User Agreement. Described in `nchs_nhanes_2021_2023_bmx_demo.txt`; cite that key | 2,582,160 bytes | MD5 14555b1f4e3c909172e900f63a2ecd03; 11933 rows, 27 columns (read_xpt, haven 2.5.4) |
```

Paragraph for SOURCES.md, below the table:

```markdown
**S52-R1 intake, group d (material Harsh supplied), 2026-10-02.** Harsh supplied three PDFs the sandbox could
not fetch (the *Cambridge Journal of Economics* article by Herndon, Ash & Pollin; Bruford et al. 2020; the NMC
MD Community Medicine guidelines), the NHANES 2021-2023 BMX_L and DEMO_L codebook pages printed to PDF, and
the two `.xpt` data files. Only text extracts of the PDFs are in the repository (`books/S52-R1/intake/raw/`);
the PDFs are not. Numbers the book may cite were checked against the page images as well as the text layer.
Every printed count in the two codebooks was compared with the data by script and all agree. Verbatim check
31 of 31 passages and 52 of 52 header quotations. Log: `books/S52-R1/intake/log-d.md`.
```
