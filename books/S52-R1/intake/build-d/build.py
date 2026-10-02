# S52-R1 intake group d: builds four source files from material Harsh supplied on 2026-10-02:
#   herndon_2014_cje, bruford_2020_hgnc, nmc_pg_md_community_medicine, nchs_nhanes_2021_2023_bmx_demo.
# Raw texts (books/S52-R1/intake/raw/, never edited):
#   herndon_2014_cje-pdftotext-layout.txt        pdftotext -layout herndon_2014_cje.pdf
#   bruford_2020_hgnc-pdftotext.txt               pdftotext bruford_2020_nat_genet.pdf (default mode)
#   bruford_2020_hgnc-pdfinfo-meta.txt            pdfinfo -meta bruford_2020_nat_genet.pdf (XMP metadata)
#   nmc_pg_md_community_medicine-pdftotext.txt    pdftotext nmc_md_community_medicine.pdf (default mode)
#   nchs_nhanes_2021_2023_bmx_demo-BMX_L-codebook.txt, -DEMO_L-codebook-part{1,2,3}.txt
#                                                 pdftotext -layout -x 0 -y 0 -W 480 -H 842 <pdf>
#   nchs_nhanes_2021_2023_bmx_demo-facts.txt      output of build-d/nhanes.R
#   nchs_nhanes_2021_2023_bmx_demo-printed-vs-computed.txt   output of build-d/compare.R
#   nhanes_s52r1-nchs-dua.txt, nhanes_s52r1-examination-2021-2023.txt, nhanes_s52r1-demographics-2021-2023.txt
#                                                 TinyFish fetches saved by group c (2026-10-02)
# Every passage is raw[i:j] between literal anchors (end inclusive unless end_excl). Nothing in a passage is
# typed by hand. Gaps between consecutive blocks of one raw file are printed so each omission can be
# described. Writes manifest-d.json (raw name, offsets, text) for verify.py. Run from the repository root.
import json, re

RAW = "books/S52-R1/intake/raw/"
SRC = "sources/"
BAR = "=" * 79
MANIFEST = []
OMIT = "\n\n[...]\n"


def rawtext(name):
    return open(RAW + name, encoding="utf-8").read()


def cut(rawname, start, end, frm=0, end_excl=False):
    raw = rawtext(rawname)
    i = raw.find(start, frm)
    assert i != -1, (rawname, start[:60])
    j = raw.find(end, i + (1 if end_excl else len(start)))
    assert j != -1, (rawname, end[:60])
    if not end_excl:
        j += len(end)
    p = raw[i:j].rstrip()
    return i, i + len(p), p


def blocks(key, rawname, where, specs, first=1):
    out, spans, pos = [], [], 0
    for k, (heading, start, end, excl, note) in enumerate(specs):
        n = first + k
        i, j, p = cut(rawname, start, end, pos, excl)
        spans.append((heading, i, j))
        pos = j
        MANIFEST.append({"key": key, "raw": rawname, "block": n, "heading": heading, "i": i, "j": j, "text": p})
        s = "\n\n" + BAR + "\n" + f"{n}. {heading}\nRAW: {rawname} ({where})\n" + BAR + "\n\n"
        if note:
            s += "[NOTE] " + note + "\n\n"
        s += '"' + p + '"\n'
        out.append(s)
    raw = rawtext(rawname)
    for (h1, _, j1), (h2, i2, _) in zip(spans, spans[1:]):
        gap = raw[j1:i2]
        print(f"--- gap {rawname}: after [{h1[:40]}] before [{h2[:40]}]: {len(gap)} chars:",
              repr(" ".join(gap.split())[:140]))
    return out


TRANSCRIPTION = """Transcription rule for this file: every line beneath a block heading that is not
prefixed with [NOTE] is an exact, unaltered slice of the raw text named in that heading
(RAW: books/S52-R1/intake/raw/<name>), cut programmatically (raw[i:j], one contiguous slice per
block) by books/S52-R1/intake/build-d/build.py and re-checked by build-d/verify.py as a
whitespace-normalised substring of that raw text; nothing has been paraphrased, smoothed or
merged. Each block's passage is set in double quotation marks (the marks are this file's).
Material left out is marked [...] with a [NOTE]. Lines beginning [NOTE] are this file's own
annotation and are NOT source text."""

# ================================================================================ Herndon 2014
HR = "herndon_2014_cje-pdftotext-layout.txt"
HW = "pdftotext -layout"
LAY = ("The layout raw keeps each printed line as a line: words hyphenated at a line end stay split "
       "('exclu-' / 'sion'), the publisher's vertical margin line 'Downloaded from http://cje.oxfordjournals.org/ "
       "by guest on September 9, 2016' sits inside the passage on its own line, and running heads, page numbers "
       "and footnotes fall where they stand on each page.")
herndon = [
    ("Title page (p. 257): journal line, title, authors, abstract, key words, start of 1. Introduction, "
     "first-page notes and copyright line",
     "Cambridge Journal of Economics 2014, 38, 257–279", "All rights reserved.", False, LAY),
    ("1. Introduction, continued (pp. 258-260), with Table 1 (RR's published means) and footnotes 1-2",
     "258\u2003\u2003 T. Herndon, M. Ash and R. Pollin", "2. Public impact and policy relevance", True,
     "Contiguous with blocks 1 and 3. " + LAY),
    ("2. Public impact and policy relevance (pp. 260-261), with footnotes 3-7",
     "2. Public impact and policy relevance", "3. Replication", True, "Contiguous with blocks 2 and 4."),
    ("3. Replication, opening (p. 261): RR's three datasets and the working spreadsheet",
     "3. Replication", "3.1 Data gaps and selective exclusion of available data", True,
     "Contiguous with blocks 3 and 5. The page's footnotes 6 and 7 come at the end of this block."),
    ("3.1 Data gaps and selective exclusion of available data (pp. 262-263), with footnote 8",
     "3.1 Data gaps and selective exclusion of available data", "3.2 Spreadsheet coding error", True,
     "Contiguous with blocks 4 and 6. Footnote 8 (the US 1946-49 growth figures) is printed at the foot of "
     "p. 263 and appears in block 7, after the opening lines of 3.3, where the layout raw puts it."),
    ("3.2 Spreadsheet coding error (p. 263), with footnote 9 (the rows the formula averaged)",
     "3.2 Spreadsheet coding error", "3.3 Summarising all RR data exclusions", True,
     "Contiguous with blocks 5 and 7. Footnote 9 is printed at the foot of p. 263; the raw puts it after the "
     "opening lines of 3.3, so it is in block 7, not here."),
    ("3.3 Summarising all RR data exclusions for highest public debt/GDP category (pp. 263-265), with "
     "footnotes 8-10 and Table 2",
     "3.3 Summarising all RR data exclusions", "3.4 Inappropriate weighting in calculating summary statistics",
     True, "Contiguous with blocks 6 and 8. Contains footnotes 8 and 9 (foot of p. 263), Table 2 (p. 264) "
     "and footnote 10 (foot of p. 264)."),
    ("3.4 Inappropriate weighting in calculating summary statistics (pp. 265-266)",
     "3.4 Inappropriate weighting in calculating summary statistics", "3.5 Impact of RR exclusions, errors", True,
     "Contiguous with blocks 7 and 9."),
    ("3.5 Impact of RR exclusions, errors and methodology (pp. 266-269), with footnote 11 and Tables 3, 4 "
     "and 5",
     "3.5 Impact of RR exclusions, errors", "3.6 Reassessing RR’s mean GDP calculations", True,
     "Contiguous with blocks 8 and 10. Table 4's last row ('Average GDP growth for all countries in >90% "
     "public debt/GDP category', -0.1% RR estimate, +2.2% with full data and country-year weighting) and "
     "Table 5's first row ('All data with country-year weighting', 4.2 / 3.1 / 3.2 / 2.2) were checked "
     "against the page images of pp. 268-269."),
    ("3.6 Reassessing RR's mean GDP calculations for 1790-2009 and 3.7 Reassessing RR median GDP growth "
     "calculations for 1946-2009 (pp. 269-272), with the caption of Figure 1, Tables 6 and 7 and footnote 12",
     "3.6 Reassessing RR’s mean GDP calculations", "3.8 Non-linearity at historical boundary?", True,
     "Contiguous with block 9. The plotted points of Figure 1 are a drawing; only its caption, note and source "
     "line are text (inside this block)."),
    ("4. Conclusion (pp. 277-278), whole",
     "4. Conclusion", "will consistently produce sharp declines in economic growth.", False,
     "Omitted before this block: 3.8 'Non-linearity at historical boundary?' (3.8.1 adding a category, "
     "3.8.2 scatter plots with regression line, footnote 13 on the mgcv package in R, 3.8.3 subperiods with "
     "Table 8 and footnote 14) and Figures 2-5 (pp. 272-277)."),
]
hb = blocks("herndon_2014_cje", HR, HW, herndon)

H_HEAD = """HERNDON, ASH & POLLIN 2014, CAMBRIDGE JOURNAL OF ECONOMICS 38:257-279 - DOES HIGH PUBLIC DEBT
CONSISTENTLY STIFLE ECONOMIC GROWTH? A CRITIQUE OF REINHART AND ROGOFF (PUBLISHED ARTICLE)
============================================================

""" + TRANSCRIPTION + """
The raw text is the text layer of the article PDF, extracted with pdftotext -layout (poppler),
2026-10-02. The default (reading-order) mode was tried and not used: on these single-column pages it
moved the abstract, footnotes and the margin line out of page order, so that sentences were split
by other material (e.g. p. 262's last sentence 'In' resumed only after section 3.2 and two
footnotes); the -layout mode keeps every page's lines in order and keeps table rows aligned. In
the raw, words hyphenated at a line end stay hyphenated and split across lines (search for
"exclu-", not "exclusion", where it occurs), and the margin line "Downloaded from
http://cje.oxfordjournals.org/ by guest on September 9, 2016" (printed vertically on every page)
sits on its own line inside passages.

CITATION: Herndon T, Ash M, Pollin R. Does high public debt consistently stifle economic growth? A
critique of Reinhart and Rogoff. Camb J Econ 2014;38(2):257-279. doi:10.1093/cje/bet075.
PRINTED ON THE PDF ITSELF (block 1): "Cambridge Journal of Economics 2014, 38, 257–279 /
doi:10.1093/cje/bet075 / Advance Access publication 24 December 2013"; authors "Thomas Herndon,
Michael Ash and Robert Pollin"; "Manuscript received 9 October 2013; final version received 12
November 2013." The issue number (2) is not printed on the PDF; it is from the Crossref record
quoted in sources/herndon_2013_wp322.txt (volume, pages and authors there agree with this PDF).
SOURCE: PDF supplied by Harsh, 2026-10-02 (file herndon_2014_cje.pdf, 23 pages, 951,156 bytes, MD5
05779c6386c1e6f95b2483feaaf17dc5; PDF creator "Adobe InDesign CS5.5 (7.5)", created 28 Feb 2014).
Its margin line shows that this copy was downloaded from the journal's site
(cje.oxfordjournals.org) "by guest on September 9, 2016". The PDF is not held in the repository;
only its text layer is (books/S52-R1/intake/raw/""" + HR + """).
COPYRIGHT AS PRINTED (p. 257, inside block 1): "© The Author 2013. Published by Oxford University
Press on behalf of the Cambridge Political Economy Society. All rights reserved."
[NOTE] No licence to reuse is stated. Held for private study and for checking quotations only; it
must not be republished or distributed. Reader-facing text should paraphrase, quote briefly and
cite.

WHAT THIS FILE HOLDS: the article from the title page through section 3.7 without a break (blocks
1-10: abstract; introduction with Table 1, RR's published means 4.1% / 2.8% / 2.8% / -0.1%; public
impact; replication: data gaps and the selective exclusion of Australia 1946-50, New Zealand 1946-49
and Canada 1946-50; the spreadsheet coding error that "unintentionally excludes five countries
entirely (Australia, Austria, Belgium, Canada and Denmark)", with footnote 9, "RR calculated both
means and medians of cells in lines 30–44 instead of lines 30–49" (1946-2009) and "lines 5–19
instead of lines 5–24" (1790-2009); Table 2, 110 / 96 / 71 country-years above 90%; the weighting
of country means ("means of country means"); Tables 3-5, the corrected mean for the >90% category
"+2.2%" against RR's "−0.1%"; the 1790-2009 means, Table 6, 1.7 -> 2.1; the medians, Table 7,
1.6 (RR 2010) -> 2.3 (HAP) and 2.5 (RR's own Errata recalculation)), and section 4 Conclusion whole
(block 11).
NOT HELD: section 3.8 'Non-linearity at historical boundary?' with Figures 2-5 and Table 8
(pp. 272-277); the bibliography; the Appendix, Table A1 (pp. 278-279). The plotted points of
Figure 1 (a drawing).
[NOTE] The working paper that preceded this article is filed separately as herndon_2013_wp322
(PERI WP 322, April 2013, revised). The two differ in wording and in some numbers: see
books/S52-R1/intake/log-d.md. In particular, the working paper's footnote 9 on "the advantages of
reproducible code relative to working spreadsheets" has no counterpart in this article; cite the
working paper for that sentence.
"""
open(SRC + "herndon_2014_cje.txt", "w", encoding="utf-8").write(
    H_HEAD + "".join(hb[:10]) + OMIT + "[NOTE] Section 3.8 (pp. 272-277) omitted; see the note to block 11.\n"
    + hb[10] + OMIT + "[NOTE] Omitted after block 11: Bibliography and Appendix (Table A1).\n")

# ================================================================================ Bruford 2020
BR = "bruford_2020_hgnc-pdftotext.txt"
BW = "pdftotext, default reading-order mode"
BM = "bruford_2020_hgnc-pdfinfo-meta.txt"
bruford = [
    ("Title, standfirst, authors, introduction, Box 1 'Summary of the guidelines' and 'Gene naming' (p. 754), "
     "to the page footer",
     "Guidelines for human gene nomenclature\nStandardized", "754–758 | www.nature.com/naturegenetics", False,
     "The large initial 'T' of the first word comes out on its own line ('T' / 'he first guidelines'). The "
     "page number '754' and the page footer, which prints the journal, volume, month, year and pages, are "
     "inside the passage."),
    ("Box 3 'Scenarios that may merit a symbol change' (p. 757), first column of the box",
     "Box 3 | Scenarios that may merit a symbol change", "I subunit F).", False,
     "Omitted before this block: pp. 755-757 to this point (Box 2; Table 1 'Key factors in assigning gene "
     "nomenclature'; Gene naming by biotype: protein-coding genes, Fig. 1 on naming lncRNA genes, pseudogenes, "
     "non-coding RNA genes, readthrough transcripts, in part). The four bullet marks of the box come out as "
     "a run of '•' lines before the first entry."),
    ("Box 3, second column of the box (p. 757): pejorative symbols; misleading nomenclature; 'Symbols that "
     "affect data handling and retrieval'",
     "Pejorative symbols.", "CARS1).", False,
     "Omitted before this block: the end of 'Readthrough transcripts', 'Gene segments', 'Genomic regions', the "
     "start of 'Genes found within subsets of the population' and the page footer, which the reading-order "
     "mode sets between the box's two columns. The two passages of blocks 2 and 3 together are the whole of "
     "Box 3. Page images checked: Box 3 on p. 757 prints exactly these words, the gene symbols in italics."),
    ("'Nomenclature updates' (pp. 757-758): placeholders, replacing underused and problematic nomenclature, "
     "gene-symbol usage and the HGNC ID",
     "Nomenclature updates\n\nAlthough", "nomenclature changes.", False,
     "Omitted before this block: the rest of p. 757 (status; naming across vertebrates; the VGNC; species "
     "designation, in part). The page number '758' is inside the passage."),
    ("Author names and affiliations, publication date and DOI (p. 758)",
     "Elspeth A. Bruford", "https://doi.org/10.1038/s41588-020-0669-3", False,
     "Omitted before this block: the end-of-article mark ('\u2750') only."),
]
bb = blocks("bruford_2020_hgnc", BR, BW, bruford)
bm = blocks("bruford_2020_hgnc", BM, "pdfinfo -meta: the PDF's embedded XMP metadata", [
    ("Copyright statement in the PDF's embedded metadata (not printed on the pages)",
     "<prism:copyright>", "</prism:copyright>", False,
     "The five printed pages carry no copyright or licence line (checked on the page images of pp. 754 and "
     "758 and in the text layer). This element of the file's XMP metadata is the only statement found."),
], first=6)

B_HEAD = """BRUFORD ET AL. 2020, GUIDELINES FOR HUMAN GENE NOMENCLATURE, NATURE GENETICS 52:754-758
(HGNC GUIDELINES; EXCERPTS)
============================================================

""" + TRANSCRIPTION + """
The raw text is the text layer of the article PDF, extracted with pdftotext (poppler, default
reading-order mode), 2026-10-02. The -layout mode was tried and not used: it sets the three columns
side by side on each line. The reading-order mode keeps each column's sentences in order and
dehyphenates line-end breaks; boxes and footers come out where the column flow puts them (see the
block notes). Block 6 comes from the PDF's embedded metadata, read with pdfinfo -meta.

CITATION: Bruford EA, Braschi B, Denny P, Jones TEM, Seal RL, Tweedie S. Guidelines for human gene
nomenclature. Nat Genet 2020;52:754-758. doi:10.1038/s41588-020-0669-3.
PRINTED ON THE PDF ITSELF: the article type "comment" (every page head); authors "Elspeth A.
Bruford, Bryony Braschi, Paul Denny, Tamsin E. M. Jones, Ruth L. Seal and Susan Tweedie"; the page
footer "Nature Genetics | VOL 52 | August 2020 | 754–758 | www.nature.com/naturegenetics" (block 1);
"Published online: 3 August 2020 / https://doi.org/10.1038/s41588-020-0669-3" (block 5). No issue
number is printed.
SOURCE: PDF supplied by Harsh, 2026-10-02 (file bruford_2020_nat_genet.pdf, 5 pages, 917,678 bytes,
MD5 14d07b96d7ee80e611323e4e8e7e1765; PDF title "Guidelines for human gene nomenclature", creator
"Springer"). The PDF is not held in the repository; its text layer and metadata are
(books/S52-R1/intake/raw/""" + BR + """ and """ + BM + """).
COPYRIGHT AS STATED: none on the printed pages. The PDF's embedded metadata (block 6) reads
"© 2020, Springer Nature America, Inc".
[NOTE] No licence to reuse is stated. Held for private study and for checking quotations only; it
must not be republished or distributed. Quote briefly and cite.

WHAT THIS FILE HOLDS: p. 754 whole (the introduction: stability of gene symbols "is now a key
priority for the HGNC"; Box 1, the five summary guidelines; the definition of a gene) (block 1);
Box 3 "Scenarios that may merit a symbol change", whole, including "Symbols that affect data
handling and retrieval. For example, all symbols that autoconverted to dates in Microsoft Excel
have been changed (for example, SEPT1 is now SEPTIN1; MARCH1 is now MARCHF1)" (blocks 2-3); the
section "Nomenclature updates" with "Gene-symbol usage" and the advice to quote the HGNC ID (block
4); authors' affiliations, online publication date and DOI (block 5); the metadata copyright line
(block 6).
NOT HELD: pp. 755-757 apart from Box 3 and the start of "Nomenclature updates" (Box 2, Table 1,
Fig. 1, gene naming by biotype, genes in population subsets, status, naming across vertebrates);
references, acknowledgements, author contributions, competing interests.
[NOTE] What the article does and does not say about spreadsheets: Box 3 names Microsoft Excel,
autoconversion to dates and two examples, SEPT1 -> SEPTIN1 and MARCH1 -> MARCHF1. It does not
name SEPT2, does not say "families", gives no date for the renaming, gives no count of symbols
changed, and does not cite Ziemann et al. 2016 or any study of gene lists in papers. The word
"spreadsheet" does not occur in the article.
"""
open(SRC + "bruford_2020_hgnc.txt", "w", encoding="utf-8").write(
    B_HEAD + bb[0] + OMIT + bb[1] + OMIT + bb[2] + OMIT + bb[3] + OMIT + bb[4]
    + OMIT + "[NOTE] Omitted after block 5: references, acknowledgements, author contributions, competing\n"
      "interests, additional information and the last page footer.\n" + bm[0])

# ================================================================================ NMC
NR = "nmc_pg_md_community_medicine-pdftotext.txt"
NW = "pdftotext, default reading-order mode"
nmc = [
    ("Title, Preamble and 'SUBJECT SPECIFIC OBJECTIVES' 1-3 (pp. 1-2)",
     "GUIDELINES FOR COMPETENCY BASED POSTGRADUATE", "data analysis\nand report.", False,
     "The page number '1' is inside the passage. Objective 3 ('Research: ...') begins on p. 2; checked on the "
     "page image."),
    ("'A. C. Psychomotor domain' (pp. 3-4) whole, and 'Miscellaneous skills' 1-8 (pp. 4-5)",
     "A. C. Psychomotor domain", "8. Use modern IT applications especially internet & internet-based applications.",
     False,
     "Omitted before this block: 'SUBJECT SPECIFIC COMPETENCIES', A. Cognitive domain items 1-34 and B. "
     "Affective domain 1-3 (pp. 2-3). The heading prints as 'A. C. Psychomotor domain: ((The student should be "
     "able to:)' on the page image of p. 3, as in the raw. Each bullet mark of the list comes out as the "
     "private-use character U+F0B7 on a line of its own (a blank or a box in most fonts). The fourth bullet, 'Do data collection, compilation, "
     "tabular and graphical presentation, ... for validation of findings', was checked on the page image of "
     "p. 4. The page number '4' is inside the passage."),
    ("Syllabus, course contents item 3 'Applied Epidemiology, Health research, Bio-statistics' with its "
     "learning objectives i-vi (pp. 5-6)",
     "3.\n\nApplied Epidemiology, Health research, Bio-statistics", "MS office and other advanced versions.", False,
     "Omitted before this block: 'Syllabus', course contents items 1 and 2 (p. 5). Objectives v and vi "
     "were checked on the page image of p. 6."),
    ("Summative assessment, opening (p. 13): the regulations it refers to",
     "SUMMATIVE ASSESSMENT, ie., at the end of training", "MEDICAL EDUCATION REGULATIONS, 2000.", False,
     "Omitted before this block: course contents items 4-onward, teaching programme, formative assessment "
     "(pp. 6-13). This block is held only because it is the document's one reference to a dated instrument."),
]
nb = blocks("nmc_pg_md_community_medicine", NR, NW, nmc)

N_HEAD = """NMC (WATERMARK: MEDICAL COUNCIL OF INDIA), GUIDELINES FOR COMPETENCY BASED POSTGRADUATE TRAINING
PROGRAMME FOR MD IN COMMUNITY MEDICINE (EXCERPTS)
============================================================

""" + TRANSCRIPTION + """
The raw text is the text layer of the PDF, extracted with pdftotext (poppler, default
reading-order mode), 2026-10-02. The -layout mode was tried; on these single-column pages it adds
only justification spaces, and the default mode was kept because COVERAGE.md's quotations are
whitespace-normalised substrings of it.

TITLE AS PRINTED (p. 1): "GUIDELINES FOR COMPETENCY BASED POSTGRADUATE / TRAINING PROGRAMME FOR MD IN
COMMUNITY MEDICINE".
ISSUER, DATE, VERSION: the text names no issuing body, carries no date and no version or edition
number. The only dated item in the text is the reference to "POSTGRADUATE MEDICAL EDUCATION
REGULATIONS, 2000" (block 4); the annexure refers to postings "as per MCI norm". Every page image
carries a large diagonal watermark "Medical Council of India" with the Council's seal (seen on the
page images of pp. 1-4 and 6; the watermark is not in the text layer). The PDF's own metadata:
producer "doPDF Ver 9.3 Build 239", created and modified 2 May 2019 (raw/""" + "nmc_pg_md_community_medicine-pdfinfo.txt" + """);
that is the date the PDF file was made, not a date of issue. Cite as undated (n.d.), from the
National Medical Commission's website, with the URL below.
URL: https://nmc.org.in/storage/new/MD-Community-Medicine.pdf (Harsh downloaded it from this
address; Task 1 opened the same URL through TinyFish for COVERAGE.md and found no date).
SOURCE: PDF supplied by Harsh, 2026-10-02 (file nmc_md_community_medicine.pdf, 16 pages of 612 x
1008 pts, 161,949 bytes, MD5 2a5dc4005ad04c3cfe1d7b1eb64f7911). The PDF is not held in the
repository; its text layer is (books/S52-R1/intake/raw/""" + NR + """).
LICENCE: none stated in the document or its metadata.
[NOTE] Held for checking the quotations in books/S52-R1/COVERAGE.md and for any sentence of the book
that cites the curriculum. Quote briefly and cite.

WHAT THIS FILE HOLDS: the title, the Preamble and the three subject-specific objectives, of which
objective 3 is "Research: To formulate research questions, do literature search, conduct study
with an appropriate study design and study tool; conduct data collection and management, data
analysis and report." (block 1); the psychomotor domain whole, with "Do data collection,
compilation, tabular and graphical presentation, analysis and interpretation, applying appropriate
statistical tests, using computer-based software application for validation of findings", and the
miscellaneous skills including "8. Use modern IT applications especially internet &
internet-based applications." (block 2); course contents item 3 with objectives v ("Understand
difference between data, information & intelligence, types of data, ...") and vi ("Apply computer
based software application for data designing, data management & collation analysis e.g. SPSS,
Epi-info, MS office and other advanced versions.") (block 3); the opening of the summative
assessment (block 4).
NOT HELD: the cognitive (1-34) and affective (1-3) competencies; course contents items 1, 2 and
4-onward; teaching programme; formative assessment; theory papers; practical examination; the
appraisal form (Annexure I); pp. 7-16 apart from block 4.
"""
open(SRC + "nmc_pg_md_community_medicine.txt", "w", encoding="utf-8").write(
    N_HEAD + nb[0] + OMIT + nb[1] + OMIT + nb[2] + OMIT + nb[3]
    + OMIT + "[NOTE] Omitted after block 4: the rest of the assessment section and the annexures.\n")

# ================================================================================ NHANES
K = "nchs_nhanes_2021_2023_bmx_demo"
FR = K + "-facts.txt"
CR = K + "-printed-vs-computed.txt"
XR = K + "-BMX_L-codebook.txt"
D1, D2, D3 = (K + f"-DEMO_L-codebook-part{p}.txt" for p in (1, 2, 3))
CW = "pdftotext -layout cropped to the main column: -x 0 -y 0 -W 480 -H 842"
CROP = ("The crop leaves out the page's right-hand navigation sidebar (the browser's 'TABLE' of contents, "
        "printed beside every page) and with it the page counter at the right end of each footer; each "
        "page keeps its print-time header ('10/2/26, ...') and its footer URL inside the passage.")

_raw = rawtext(FR)
_i = _raw.index("R version:")
_j = _raw.index("\n== FREQUENCIES")
_t = _raw[_i:_j].rstrip()
MANIFEST.append({"key": K, "raw": FR, "block": 1, "heading": "facts", "i": _i, "j": _i + len(_t), "text": _t})
fblock = ("\n\n" + BAR + "\n1. Facts recorded by script from the two .xpt files held in sources/data/ (whole output "
          "up to the frequency listing)\nRAW: " + FR + " (output of build-d/nhanes.R, R 4.3.3, haven 2.5.4)\n" + BAR
          + "\n\n[NOTE] This block is output of this repository's script, not text of NCHS. The labels of five "
            "DEMO_L variables contain the byte 0x92 (a Windows-1252 apostrophe) where the codebook prints "
            "'person\u2019s'; R prints that byte as <92>.\n\n\"" + _t + "\"\n")

comp = blocks(K, CR, "output of build-d/compare.R, haven 2.5.4", [
    ("Every printed code-table row of both codebooks compared with the count in the .xpt files",
     "haven 2.5.4", "variables with no printed code table: BMX_L SEQN DEMO_L SEQN", False,
     "Output of this repository's scripts, not text of NCHS: parse_codebook.py read the rows from the raw "
     "codebook texts (blocks 5-9); compare.R counted each row in the data (a code counts equal values; a "
     "range counts non-missing values between its ends that have no code row of their own; '.' counts NA) "
     "and recomputed the cumulative column."),
], first=2)

bmx = blocks(K, XR, CW, [
    ("BMX_L documentation: title block, component description, eligible sample, protocol and procedure, "
     "quality assurance, data processing and editing, analytic notes (printed pp. 1-3)",
     "10/2/26, 11:31 AM", "Codebook and Frequencies", True, CROP),
    ("BMX_L codebook and frequencies: all 22 variables (printed pp. 3-24)",
     "Codebook and Frequencies", "BMX_L.htm", True,
     "Contiguous with block 3, to the last footer URL (exclusive of the final 'BMX_L.htm', which is the end "
     "of that URL). Variables in order: SEQN, BMDSTATS, BMXWT, BMIWT, BMXRECUM, BMIRECUM, BMXHEAD, BMIHEAD, "
     "BMXHT, BMIHT, BMXBMI, BMDBMIC, BMXLEG, BMILEG, BMXARML, BMIARML, BMXARMC, BMIARMC, BMXWAIST, BMIWAIST, "
     "BMXHIP, BMIHIP. The heading line 'BMXRECUM - Recumbent Length (cm)' at the top of printed p. 7 does not "
     "come out in the cropped text layer; its table does."),
], first=3)
# block 4 must run to the LAST footer of the BMX raw, not the first: rebuild it explicitly
_raw = rawtext(XR)
i4 = MANIFEST[-1]["i"]
j4 = _raw.rfind("https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.htm") + len(
    "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.htm")
MANIFEST[-1]["j"] = j4
MANIFEST[-1]["text"] = _raw[i4:j4]
bmx[1] = ("\n\n" + BAR + "\n4. BMX_L codebook and frequencies: all 22 variables (printed pp. 3-24)\nRAW: " + XR
          + " (" + CW + ")\n" + BAR + "\n\n[NOTE] Contiguous with block 3, to the last page's footer URL. Variables "
          "in order: SEQN, BMDSTATS, BMXWT, BMIWT, BMXRECUM, BMIRECUM, BMXHEAD, BMIHEAD, BMXHT, BMIHT, BMXBMI, "
          "BMDBMIC, BMXLEG, BMILEG, BMXARML, BMIARML, BMXARMC, BMIARMC, BMXWAIST, BMIWAIST, BMXHIP, BMIHIP. The "
          "heading line 'BMXRECUM - Recumbent Length (cm)' does not come out in the cropped text layer; its "
          "variable block and table do. Page images checked: printed pp. 4 (BMDSTATS), 5 (BMXWT), 6 (BMIWT), "
          "11 (BMXHT), 12 (BMIHT), 13 (BMXBMI), 21 (BMXWAIST).\n\n\"" + MANIFEST[-1]["text"] + "\"\n")


def whole(rawname, n, heading, note):
    raw = rawtext(rawname)
    s = raw.find("10/2/26, 11:32 AM")
    e = raw.rfind("DEMO_L.htm") + len("DEMO_L.htm")
    t = raw[s:e]
    MANIFEST.append({"key": K, "raw": rawname, "block": n, "heading": heading, "i": s, "j": e, "text": t})
    return ("\n\n" + BAR + f"\n{n}. {heading}\nRAW: {rawname} ({CW})\n" + BAR + "\n\n[NOTE] " + note
            + "\n\n\"" + t + "\"\n")


demo = [
    whole(D1, 5, "DEMO_L documentation and codebook, part 1 of Harsh's print (printed pp. 1-11): title block, "
          "component description, eligible sample, interview setting, quality assurance, data processing and "
          "editing, analytic notes, references; variables SEQN, SDDSRVYR, RIDSTATR, RIAGENDR, RIDAGEYR, "
          "RIDAGEMN, RIDRETH1",
          "The whole of this part's text, from the first page's print-time header to the last page's footer URL. "
          + CROP + " Page images checked: printed pp. 2 and 4 (RIDAGEYR top-code note; MVUs; sample weights), "
          "7 (RIDSTATR), 8 (RIAGENDR), 9 (RIDAGEYR)."),
    whole(D2, 6, "DEMO_L codebook, part 2 (printed pp. 12-21): RIDRETH3, RIDEXMON, RIDEXAGM, DMQMILIZ, DMDBORN4, "
          "DMDYRUSR, DMDEDUC2, DMDMARTZ, RIDEXPRG, DMDHHSIZ",
          "Whole part. Contiguous in print with block 5 (Harsh saved the 31 printed pages as three consecutive "
          "PDFs). In DMDBORN4 the description of code 1 is cut at 'Washington,' in the text layer: the cell "
          "wraps and its second line falls outside the crop. Page image checked: printed p. 20 (RIDEXPRG)."),
    whole(D3, 7, "DEMO_L codebook, part 3 (printed pp. 22-31): DMDHRGND, DMDHRAGZ, DMDHREDZ, DMDHRMAZ, DMDHSEDZ, "
          "WTINT2YR, WTMEC2YR, SDMVSTRA, SDMVPSU, INDFMPIR",
          "Whole part. Contiguous in print with block 6. Page images checked: printed pp. 28 (WTMEC2YR), "
          "29 (SDMVSTRA), 30 (SDMVPSU)."),
]
pages = blocks(K, "nhanes_s52r1-examination-2021-2023.txt", "TinyFish fetch_content, markdown, 2026-10-02, "
               "saved by group c; URL https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Examination&Cycle=2021-2023",
               [("NHANES data page, Examination 2021-2023: the Body Measures row", "Body Measures\nBMX\\_L Doc",
                 "September 2024", False, "Backslashes before underscores are the fetch tool's markdown escapes.")],
               first=8)
pages += blocks(K, "nhanes_s52r1-demographics-2021-2023.txt", "TinyFish fetch_content, markdown, 2026-10-02, "
                "saved by group c; URL https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Demographics&Cycle=2021-2023",
                [("NHANES data page, Demographics 2021-2023: the table header and the DEMO_L row",
                  "Data File Name\nDoc File", "September 2024", False,
                  "Backslashes before underscores are the fetch tool's markdown escapes.")], first=9)
dua = blocks(K, "nhanes_s52r1-nchs-dua.txt", "TinyFish fetch_content, markdown, 2026-10-02, saved by group c; "
             "URL https://www.cdc.gov/nchs/policy/data-user-agreement.html", [
                 ("NCHS Data User Agreement (the terms of use for the two data files), whole text of the page",
                  "September 17, 2024\n\n# Data User Agreement", "or fined not more than $250,000, or both.", False,
                  "The page's closing date line, 'Sources / Print / Share' and the empty 'Content Source:' are "
                  "omitted after the passage.")], first=10)

ft = rawtext(FR)
g = lambda pat: re.search(pat, ft).group(1)
X_HEAD = """NHANES AUGUST 2021-AUGUST 2023: BODY MEASURES (BMX_L) AND DEMOGRAPHIC VARIABLES AND SAMPLE WEIGHTS
(DEMO_L) - THE TWO DATA FILES, THEIR CODEBOOKS AND THE NCHS DATA USER AGREEMENT
============================================================

""" + TRANSCRIPTION + """
Blocks 1-2 are output of this repository's scripts (R 4.3.3, haven 2.5.4) run on the data files;
blocks 3-7 are the text layer of the codebook PDFs Harsh printed; blocks 8-10 are pages fetched by
the S52-R1 group c intake (TinyFish, 2026-10-02).

WHAT IT IS: the National Center for Health Statistics (NCHS, Centers for Disease Control and
Prevention), National Health and Nutrition Examination Survey (NHANES), August 2021-August 2023
cycle: the public data files BMX_L.xpt (Body Measures, Mobile Examination Center) and DEMO_L.xpt
(Demographic Variables and Sample Weights), SAS transport format, each "First Published: September
2024", "Last Revised: NA" (blocks 3 and 5).
CITATION: National Center for Health Statistics. National Health and Nutrition Examination Survey,
August 2021-August 2023: Body Measures (BMX_L) and Demographic Variables and Sample Weights (DEMO_L)
data files and documentation. NCHS, Centers for Disease Control and Prevention; first published
September 2024. https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/ (accessed 2 October 2026).

THE DATA FILES HELD (byte for byte, not text): sources/data/BMX_L.xpt and sources/data/DEMO_L.xpt.
Harsh downloaded them in a browser on 2 Oct 2026 from the .xpt links of the same folder as the
codebooks, https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/ (BMX_L.xpt, DEMO_L.xpt),
and supplied them to this intake; they were copied unchanged into sources/data/ and their MD5
re-checked after copying. Recorded by script (block 1):
  BMX_L.xpt: """ + g(r"== BMX_L\nfile: \S+ \nbytes: (\d+)") + """ bytes, MD5 """ + g(r"== BMX_L\n.*\n.*\nmd5: (\w+)") + """, """ + g(r"== BMX_L\n(?:.*\n){3}rows: (\d+)") + """ rows x """ + g(r"== BMX_L\n(?:.*\n){4}columns: (\d+)") + """ columns
  DEMO_L.xpt: """ + g(r"== DEMO_L\nfile: \S+ \nbytes: (\d+)") + """ bytes, MD5 """ + g(r"== DEMO_L\n.*\n.*\nmd5: (\w+)") + """, """ + g(r"== DEMO_L\n(?:.*\n){3}rows: (\d+)") + """ rows x """ + g(r"== DEMO_L\n(?:.*\n){4}columns: (\d+)") + """ columns
  missing (NA) in BMX_L: BMXWT """ + g(r"BMXWT: (\d+)\n") + """, BMXHT """ + g(r"BMXHT: (\d+)\n") + """, BMXBMI """ + g(r"BMXBMI: (\d+)\n") + """, BMXWAIST """ + g(r"BMXWAIST: (\d+)\n") + """
  every BMX_L SEQN is in DEMO_L; after the join on SEQN, BMX rows with RIDAGEYR >= 20: """ + g(r"RIDAGEYR >= 20: (\d+)") + """
THE CODEBOOKS: printed by Harsh to PDF from the CDC pages
https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.htm and .../DEMO_L.htm on 2 Oct 2026.
The PDFs confirm it: every page's header prints the print time ("10/2/26, 11:31 AM" on BMX_L,
"10/2/26, 11:32 AM" on DEMO_L) and the page title, and every footer prints the page's URL and a
page counter ("1/24" ... "24/24" for BMX_L; "1/31" ... "31/31" for DEMO_L, the 31 pages split by Harsh
into three consecutive PDFs of 11, 10 and 10 pages). BMX_L_codebook.pdf: 24 pages, 4,783,331
bytes, MD5 a79aea0f5af6fb33900adc1de12abaa7, creator Chrome 154 (Skia/PDF). DEMO_L_codebook_part1/2/3.pdf:
319,478 / 262,890 / 250,196 bytes, MD5 92b19db5aa76e918fa4912fcd6eea083 / fd825c0fb9eab2e687c72642bd1a75c6 /
5287d4d238f8a588b7e7bd9bad2b7128 (split with PDFsam Basic). The PDFs are not held in the repository.
PRINTED COUNTS AGAINST THE DATA: every printed code-table row of both codebooks (155 rows, 47
variables with tables) agrees with the count computed from the .xpt files, cumulative column
included (block 2). SEQN has no table in either codebook.
TERMS (block 10): the NCHS Data User Agreement, dated "September 17, 2024": users will "1. Use the
data in this dataset for statistical reporting and analysis only. 2. Make no attempt to learn the
identity of any person or establishment included in these data. 3. Not link this dataset with
individually identifiable data from other NCHS or non-NCHS datasets. ..." Neither the agreement
nor the codebooks state a copyright or a licence.
[NOTE] Any summary of these files in the book is unweighted: the codebooks say the examination
sample weights "should be used to analyze the body measures data" (block 3) and the 2-year weights
"should be used for all NHANES August 2021-August 2023 analyses" (block 5). An unweighted mean
describes these participants and estimates nothing about the US population (survey weights are
S54's subject).

WHAT THIS FILE HOLDS: script-recorded facts of the two data files (block 1); the printed-vs-computed
comparison (block 2); the BMX_L documentation and codebook whole (blocks 3-4); the DEMO_L
documentation and codebook whole (blocks 5-7); the two rows of the NHANES data pages that list the
files (blocks 8-9); the NCHS Data User Agreement (block 10).
NOT HELD: the frequency listing at the end of the nhanes.R output (it is in the raw file and is
superseded by block 2); the browser's navigation sidebar on each codebook page; the NHANES
Anthropometry Procedures Manual, Plan and Operations report and Analytic Guidelines that the
codebooks name (not opened).
"""
open(SRC + K + ".txt", "w", encoding="utf-8").write(
    X_HEAD + fblock + comp[0] + bmx[0] + bmx[1] + demo[0] + demo[1] + demo[2] + pages[0] + pages[1] + dua[0]
    + OMIT + "[NOTE] Omitted after block 10: the page's repeated date line and its 'Sources / Print / Share'\n"
      "links.\n")

json.dump(MANIFEST, open("books/S52-R1/intake/build-d/manifest-d.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("blocks cut:", len(MANIFEST))
