# Source intake log · S52-R1 · group d (material Harsh supplied)

One pass, 2026-10-02, against `INTAKE-BRIEF.md` (general rules) and the conductor's brief for group d. Harsh
supplied, outside the repository in `/home/claude/work/harsh-supplied-S52/`: three PDFs the sandbox could not
fetch, the NHANES 2021-2023 BMX_L and DEMO_L codebook pages printed to PDF, and the two NHANES `.xpt` data
files. Nothing was fetched from the web in this pass; the NCHS Data User Agreement and the two NHANES data-page
rows are cut from group c's saved fetches.

**Method.** Text layers by `pdftotext` (poppler); both the default reading-order mode and `-layout` were tried
for every PDF and the one that keeps sentences whole was saved under `intake/raw/` (choice per source below).
PDF metadata by `pdfinfo` (saved), MD5 of every supplied PDF in `raw/group-d-harsh-pdf-md5.txt`. The PDFs
themselves are **not** in the repository. Every passage is cut by `build-d/build.py` as `raw[i:j]` between
literal anchors (offsets in `build-d/manifest-d.json`) and rechecked by `build-d/verify.py` as a
whitespace-normalised substring of its raw file; header quotations are checked the same way (two exceptions,
both declared in the script: one watermark seen only on the page images, one word the header says is absent
and which the script confirms is absent). Output of the check: `build-d/verify-output.txt`. The NHANES facts
come from `build-d/nhanes.R` (R 4.3.3, haven 2.5.4); the printed codebook rows were parsed by
`build-d/parse_codebook.py` into `build-d/codebook-printed.tsv` and counted in the data by `build-d/compare.R`.
`build-d/check_coverage.py` checks COVERAGE.md lines 15-18. No commit.

**Verbatim check: 31 of 31 passages; 52 of 52 header quotations; 31 of 31 manifest offsets (raw[i:j] = text).**

| Source | File | Raw extract (mode) | Passages | Check | Page images checked (printed page numbers) | Licence / copyright as stated | Citekey |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Herndon, Ash & Pollin, *Camb J Econ* 2014;38:257-279, published article (PDF from Harsh, 23 pp.) | `sources/herndon_2014_cje.txt` | `herndon_2014_cje-pdftotext-layout.txt` (`-layout`; default mode moved the abstract, footnotes and margin line out of page order and split sentences) | 11 (title page to 3.7 without a break; 4 Conclusion) | 11/11 + 16/16 header | 257 (abstract 2.2% / −0.1%; copyright line), 263 (3.2 and footnote 9), 264 (Table 2: 110 / 96 / 71), 267 (Table 3 weights), 268 (Table 4: −0.1% vs +2.2%), 269 (Table 5), 270 (Table 6), 271 (Table 7 medians), 277-278 (Conclusion). All agree with the text layer | "© The Author 2013. Published by Oxford University Press on behalf of the Cambridge Political Economy Society. All rights reserved." No licence | `herndon_2014_cje` |
| Bruford et al., Guidelines for human gene nomenclature, *Nat Genet* 2020;52:754-758 (PDF from Harsh, 5 pp.) | `sources/bruford_2020_hgnc.txt` | `bruford_2020_hgnc-pdftotext.txt` (default; `-layout` interleaves the three columns) and `bruford_2020_hgnc-pdfinfo-meta.txt` | 6 (p. 754; Box 3 in two column-halves; Nomenclature updates; affiliations/DOI; metadata copyright) | 6/6 + 15/15 header | 754 (title, authors, footer "Nature Genetics | VOL 52 | August 2020 | 754–758"), 757 (Box 3 wording, exact), 758 (online date, DOI; no copyright line) | None printed on the pages. PDF metadata: "© 2020, Springer Nature America, Inc" | `bruford_2020_hgnc` |
| NMC, Guidelines for competency based postgraduate training programme for MD in Community Medicine (PDF from Harsh, 16 pp.) | `sources/nmc_pg_md_community_medicine.txt` | `nmc_pg_md_community_medicine-pdftotext.txt` (default; `-layout` only adds justification spaces) | 4 (title, preamble, objectives; psychomotor and miscellaneous skills; course contents 3; summative assessment opening) | 4/4 + 9/9 header (1 image-only) | 1 (title; watermark), 2 (objective 3), 3 (psychomotor heading as printed), 4 (data-handling bullet), 6 (course contents 3 v-vi) | None stated in text or metadata | `nmc_pg_md_community_medicine` |
| NCHS, NHANES Aug 2021-Aug 2023, BMX_L and DEMO_L: data files, codebooks (Harsh's printouts), data-page rows, NCHS Data User Agreement | `sources/nchs_nhanes_2021_2023_bmx_demo.txt`; data `sources/data/BMX_L.xpt`, `sources/data/DEMO_L.xpt` | codebooks: `pdftotext -layout -x 0 -y 0 -W 480 -H 842` (cropped to the main column; uncropped `-layout` and default both mix the browser's navigation sidebar into the text); uncropped `-layout` copies kept for the footers' page counters; facts and comparison: script output | 10 (facts; printed-vs-computed; BMX documentation; BMX codebook; DEMO parts 1-3; two data-page rows; DUA) | 10/10 + 12/12 header | BMX_L 1, 4 (BMDSTATS), 5 (BMXWT), 6 (BMIWT), 11 (BMXHT), 12 (BMIHT), 13 (BMXBMI), 21 (BMXWAIST); DEMO_L 2 (RIDAGEYR top code, 85 years), 4 (MVUs, weights), 7 (RIDSTATR), 8 (RIAGENDR), 9 (RIDAGEYR), 20 (RIDEXPRG), 28 (WTMEC2YR), 29 (SDMVSTRA), 30 (SDMVPSU). All agree with the text layer | No copyright or licence stated in the codebooks or the DUA. Terms: NCHS Data User Agreement dated "September 17, 2024" (statistical reporting and analysis only; no attempt to identify; no linkage with identifiable data; no assessment of disclosure methods) | `nchs_nhanes_2021_2023_bmx_demo` |

Citekeys grepped on 2026-10-02 in `sources/INDEX.yml` and `check/references/library.bib` on this branch and on
`origin/main` (951b18a, after `git fetch origin`) and in the group a-c fragments: no match for any of the four.

## 1. Herndon, Ash & Pollin 2014 (`herndon_2014_cje`)

**Bibliographic details confirmed from the PDF:** "Cambridge Journal of Economics 2014, 38, 257–279",
"doi:10.1093/cje/bet075", "Advance Access publication 24 December 2013", authors "Thomas Herndon, Michael Ash and
Robert Pollin", received 9 Oct 2013, final version 12 Nov 2013. The issue number (2) is not printed on the PDF
(taken from the Crossref record already quoted in `herndon_2013_wp322.txt`). READY.md's line (38(2):257–279)
agrees. The PDF's margin line says this copy was downloaded from cje.oxfordjournals.org "by guest on September 9,
2016"; PDF made 28 Feb 2014 (InDesign).

**What the article says, for C01** (all in the file): the three problems, "(i) selective exclusion of available
data, (ii) coding errors and (iii) inappropriate methods for the weighting of summary statistics"; 3.1 the
exclusion of Australia (1946–50), New Zealand (1946–49) and Canada (1946–50), "At no point do RR either explicitly
explain they why they chose to make these data exclusions or even indicate that they had done so"; 3.2 "a coding
error in the RR working spreadsheet also unintentionally excludes five countries entirely (Australia, Austria,
Belgium, Canada and Denmark) from all parts of the analysis", "The omitted countries are selected alphabetically",
"RR have since acknowledged this to be the case", footnote 9: "In their analysis with the 1946–2009 dataset, RR
calculated both means and medians of cells in lines 30–44 instead of lines 30–49. In their analysis with the
1790–2009 dataset, RR calculated both means and medians for cells in lines 5–19 instead of lines 5–24"; footnote 10:
Austria and Denmark had no years above 90%, so their exclusion did not affect the >90% estimate; Table 2: 110
country-years correct, 96 after RR's chosen exclusions, 71 after exclusions plus spreadsheet errors (10 / 8 / 7
countries); 3.4 "RR compute overall averages as means of country means" (New Zealand's one year, 1951, −7.6%,
weighted equally with the UK's 19 years); transcription error −7.6% → −7.9%, worth 0.1 point; **corrected result**:
Table 4, average growth for the >90% category "−0.1%" (RR estimate) against "+2.2%" (full data, country-year
weighting); Table 5 all combinations (spreadsheet error only 1.9; all three errors 0.0; plus transcription −0.1);
Table 6 (1790-2009 means) >90%: 1.7 → 2.1; Table 7 medians >90%: RR 2010 1.6, HAP 2.3, RR's own Errata
recalculation 2.5; Conclusion: "RR did acknowledge their spreadsheet errors", and four unaddressed problems.

**Differences from the working paper (`herndon_2013_wp322`), compared against `sources/herndon_2013_wp322.txt`:**

1. Abstract and naming of the problems. WP: "coding errors, selective exclusion of available data, and
   **unconventional** weighting of summary statistics lead to serious errors". Article: "selective exclusion of
   available data, coding errors and **inappropriate** weighting of summary statistics lead to serious
   miscalculations" (in the layout raw the article's words "exclusion" and "statistics" are split across lines
   as "exclu- sion" and "sta- tistics"; checked on the page image of p. 257). The WP's section is "Unconventional weighting of summary statistics" ("a non-standard
   weighting methodology"); the article's is "3.4 Inappropriate weighting in calculating summary statistics".
   **For C01:** INVENTORY.md and PERI's page say "unconventional weighting"; that is the WP's word. If C01 cites
   the 2014 article, the word is "inappropriate".
2. The spreadsheet rows. WP footnote 5: "RR averaged cells in lines 30 to 44 instead of lines 30 to 49." Article
   footnote 9 adds that both **means and medians** were affected and that the same error occurs in the 1790–2009
   sheet ("lines 5–19 instead of lines 5–24").
3. Country-years after the spreadsheet error. WP text: "RR in fact estimated GDP growth in the highest public debt/GDP
   category with only 71" [footnote 4 intervenes in the raw] "country-years of data", but WP Table 2 prints **75** in
   the spreadsheet column ("Country-Years 110 96 75"); the WP is internally inconsistent. The article's Table 2
   prints **71** (checked on the page image of p. 264), consistent with its text.
4. RR's Figure 2 as approximated, ≤30% category: WP Table 3 "4 .1"; article Table 5 "3.8" (page image p. 269).
   The other values of that row (2.9, 3.4, −0.1) agree.
5. The size of the overstatement. WP: "RR overstates the gap by 2 .3 percentage points or a factor of nearly two
   and a half". Article: "by a factor of nearly two-and-a-half" (no 2.3).
6. Unchanged between the two: the corrected mean +2.2% against −0.1%; 110 and 96 country-years; the five
   countries; New Zealand −7.6% / −7.9%; the 14.3% weights; Table 5 = WP Table 3 except item 4.
7. Added in the article: section 2 on public impact; the 1790-2009 means (Table 6); the medians (Table 7, after
   RR's Errata of 5 May 2013); the conclusion's list of what RR acknowledged and did not.
8. **Not in the article:** the WP's footnote 9, "For econometricians a lesson from the problems in RR is the
   advantages of reproducible code relative to working spreadsheets." The article mentions R only in footnote
   13 (the mgcv smoother, section 3.8, not held). Any sentence in the book about reproducible code must cite the
   working paper, not the article.
9. Conclusions differ: WP ends that RR's findings being wrong "should therefore lead us to reassess the austerity
   agenda itself"; the article ends that "policy makers cannot defend austerity measures on the grounds that
   public debt levels greater than 90% of GDP will consistently produce sharp declines in economic growth".

## 2. Bruford et al. 2020 (`bruford_2020_hgnc`)

**Bibliographic details confirmed from the PDF:** authors "Elspeth A. Bruford, Bryony Braschi, Paul Denny,
Tamsin E. M. Jones, Ruth L. Seal and Susan Tweedie"; footer "Nature Genetics | VOL 52 | August 2020 | 754–758";
"Published online: 3 August 2020"; DOI 10.1038/s41588-020-0669-3; article type "comment". No issue number
printed. READY.md's line agrees.

**The passage C01 and C15 need, exactly as printed (Box 3, p. 757; page image checked):** "Symbols that affect
data handling and retrieval. For example, all symbols that autoconverted to dates in Microsoft Excel have been
changed (for example, SEPT1 is now SEPTIN1; MARCH1 is now MARCHF1); tRNA synthetase symbols that were also common
words have been changed (for example, WARS is now WARS1; CARS is now CARS1)." Box 3 is headed "Scenarios that
may merit a symbol change".

**What the PDF does not say (nothing below may be asserted from it):** it does not name SEPT2 (INVENTORY C01's
example, which is Ziemann's); it does not speak of gene families or of all SEPT genes; it gives no date for the renaming
and no count of symbols changed; it does not cite Ziemann et al. or any study of spreadsheet errors in papers;
the word "spreadsheet" does not occur (checked by script). It names Microsoft Excel and autoconversion to dates
only. It also states that stability of gene symbols "is now a key priority for the HGNC" and advises quoting the
HGNC ID "to avoid ambiguity" (held, block 1 and block 4). So C01 can say: HGNC's 2020 guidelines report that
all symbols that Excel autoconverted to dates have been changed, for example SEPT1 to SEPTIN1 and MARCH1 to
MARCHF1.

## 3. NMC MD Community Medicine guidelines (`nmc_pg_md_community_medicine`)

**Date and version:** none. The text carries no date, no version and names no issuing body. The only dated item
is a reference to "POSTGRADUATE MEDICAL EDUCATION REGULATIONS, 2000" (held, block 4). Every page image carries a
large "Medical Council of India" watermark with the Council's seal (not in the text layer). The PDF metadata says
it was made with doPDF on **2 May 2019** (creation and modification), which dates the file, not the guideline.
Cited as n.d., hosted on nmc.org.in.

**COVERAGE.md lines 15-18, each quotation checked by `build-d/check_coverage.py` (all four found verbatim):**

| COVERAGE.md line | Quotation | Found | What the printed sentence continues with | Mismatch? |
| --- | --- | --- | --- | --- |
| 15 | "conduct data collection and management, data analysis and report" | yes (objective 3, p. 2) | ends with "." | none |
| 16 | "Apply computer based software application for data designing, data management & collation analysis e.g. SPSS, Epi-info, MS office" | yes (course contents 3(vi), p. 6) | "... MS office **and other advanced versions.**" | words exact; COVERAGE stops mid-sentence without an ellipsis. Suggest adding "…" or the last four words |
| 17 | "data collection, compilation, tabular and graphical presentation, analysis and interpretation, applying appropriate statistical tests, using computer-based software application" | yes (psychomotor domain, p. 4) | printed "**Do** data collection, ... software application **for validation of findings**" | words exact; leading "Do" and closing "for validation of findings" not shown, no ellipsis. Suggest "…" at the end |
| 18 | "difference between data, information & intelligence, types of data" | yes (course contents 3(v), p. 6) | "**Understand** difference ... types of data, survey methods, formulating questionnaires, ..." | words exact; truncated at both ends, no ellipsis |

COVERAGE.md also calls them "Objective 3", "Course content 3(vi)", "Course content 3(v)" and "Psychomotor": these
match the document's numbering (course contents item "3. Applied Epidemiology, Health research, Bio-statistics",
learning objectives v and vi; "SUBJECT SPECIFIC OBJECTIVES" 3, "Research:"; "A. C. Psychomotor domain").

## 4. NHANES 2021-2023 BMX_L and DEMO_L (`nchs_nhanes_2021_2023_bmx_demo`)

**Data files:** copied byte for byte (`cp -p`, then `chmod 644`) to `sources/data/BMX_L.xpt` (1,563,200 bytes,
MD5 ab25a36296e5b61881d42fef61c06b84) and `sources/data/DEMO_L.xpt` (2,582,160 bytes, MD5
14555b1f4e3c909172e900f63a2ecd03); MD5 re-checked after copying, both match the brief. `sources/data/` is not
git-ignored.

**Recorded by `nhanes.R` (raw `nchs_nhanes_2021_2023_bmx_demo-facts.txt`, held as block 1):** BMX_L 8860 rows x 22
columns; DEMO_L 11933 x 27; all variables numeric; labels as read listed in block 1 (five DEMO_L labels contain
byte 0x92 for the apostrophe, printed by R as `<92>`). BMX_L missing: BMXWT 106, BMXHT 361, BMXBMI 389, BMXWAIST
670. DEMO_L: RIDSTATR 1 = 3073, 2 = 8860, NA 0; RIAGENDR 1 = 5575, 2 = 6358, NA 0; RIDAGEYR range 0 to 80, NA 0,
525 at the top code 80. SEQN unique in both files; all 8860 BMX_L SEQNs are in DEMO_L; the join keeps 8860 rows,
all with RIDSTATR = 2; **BMX rows with RIDAGEYR >= 20: 6064**; of these, missing BMXWT 81, BMXHT 67, BMXBMI 94,
BMXWAIST 302, and RIDEXPRG = 1 (pregnant at exam) 41.

**Printed codebook counts against the data:** every printed code-table row of both codebooks was parsed (22 + 27
variables; SEQN has no table in either) and counted in the `.xpt` files: **155 of 155 rows agree**, count and
cumulative, including every range's endpoints (printed ranges equal the data's min and max, e.g. BMXWT 2.7 to
248.2, WTMEC2YR 4581.595095 to 227108.296958 plus 3073 zeros "Not MEC Examined"). The 15 variables the brief
names (SEQN, BMDSTATS, BMXWT, BMIWT, BMXHT, BMIHT, BMXBMI, BMXWAIST, RIAGENDR, RIDAGEYR, RIDSTATR, RIDEXPRG,
WTMEC2YR, SDMVPSU, SDMVSTRA) are all among them; their pages were also checked on the page images (table above).
Full table: block 2 of the source file and `raw/nchs_nhanes_2021_2023_bmx_demo-printed-vs-computed.txt`.

**Codebook provenance as the PDFs show it:** each page header prints the print time ("10/2/26, 11:31 AM" BMX_L;
"10/2/26, 11:32 AM" DEMO_L) and the title; each footer prints
"https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.htm" (or DEMO_L.htm) and a page counter, "1/24"
to "24/24" and "1/31" to "31/31"; DEMO_L's 31 pages are split across part1 (pp. 1-11), part2 (12-21), part3
(22-31), consecutive and complete. Both: "First Published: September 2024", "Last Revised: NA". PDF creator for
BMX_L is Chrome 154 (Skia/PDF); the DEMO_L parts were split with PDFsam Basic.

**Inconsistencies printed in the codebooks themselves (not errors of this intake; the book should use the
variable names in the code tables and the data):** (a) BMX_L data-processing note says "Component status code
(BMXSTATS)", but the variable is BMDSTATS; (b) BMX_L protocol note says "age in months at exam (RIDEXAGEM)", but
the DEMO_L variable is RIDEXAGM; (c) DEMO_L note says RIDAGEYR is age "for survey participants between the ages of
1 and 79 years", but the code table prints "0 to 79" and the data contain 0; (d) in the DEMO_L code table for
DMDBORN4 the description of code 1 is cut at "Washington," in the cropped text layer (the cell wraps outside the
crop; the page prints more). None affects the counts.

**Terms:** the NCHS Data User Agreement is held whole (block 10), cut from group c's raw
`nhanes_s52r1-nchs-dua.txt` (https://www.cdc.gov/nchs/policy/data-user-agreement.html, fetched 2026-10-02), dated
"September 17, 2024". Neither it nor the codebooks state a copyright or licence. The header of the source file
records that any summary in the book is unweighted and estimates nothing about the US population.

## Files written

- `sources/herndon_2014_cje.txt`, `sources/bruford_2020_hgnc.txt`, `sources/nmc_pg_md_community_medicine.txt`,
  `sources/nchs_nhanes_2021_2023_bmx_demo.txt`
- `sources/data/BMX_L.xpt`, `sources/data/DEMO_L.xpt`
- `books/S52-R1/intake/raw/`: `herndon_2014_cje-pdftotext-layout.txt`, `herndon_2014_cje-pdfinfo.txt`,
  `bruford_2020_hgnc-pdftotext.txt`, `bruford_2020_hgnc-pdfinfo-meta.txt`,
  `nmc_pg_md_community_medicine-pdftotext.txt`, `nmc_pg_md_community_medicine-pdfinfo.txt`,
  `nchs_nhanes_2021_2023_bmx_demo-*` (cropped codebook texts, uncropped layout copies, pdfinfo, facts,
  printed-vs-computed), `group-d-harsh-pdf-md5.txt`
- `books/S52-R1/intake/build-d/`: `build.py`, `verify.py`, `verify-output.txt`, `nhanes.R`,
  `parse_codebook.py`, `codebook-printed.tsv`, `compare.R`, `check_coverage.py`, `manifest-d.json`
- `books/S52-R1/intake/fragment-d.md`, this log

## For the conductor or Harsh

- Suggested (not made): update the `herndon_2013_wp322` .bib note, which says the journal article "was not
  consulted", to point to `herndon_2014_cje`.
- C01 wording: "inappropriate weighting" if citing the 2014 article; "unconventional" only with the working paper.
- C01 / C15 gene names: Bruford supports SEPT1 → SEPTIN1 and MARCH1 → MARCHF1 only; SEPT2 is Ziemann's example.
- COVERAGE.md lines 16-18: add ellipses where the quotations stop mid-sentence (words are exact).
- NMC guideline: undated; cite as n.d. (PDF file made 2 May 2019; MCI watermark).
