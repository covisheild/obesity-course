# Builds the group-b source files for S52-R1 from the saved raw fetches in books/S52-R1/intake/raw/.
# Every passage is raw[i:j], located by a literal start marker and a literal end marker (end inclusive).
# Nothing in a passage is typed by hand. Run from the repository root:
#   python3 books/S52-R1/intake/build-b.py
import json

RAW = "books/S52-R1/intake/raw/"
MANIFEST = []
SEP = "=" * 100


def cut(rawname, start, end):
    raw = open(RAW + rawname).read()
    i = raw.find(start)
    assert i != -1, (rawname, "start", start[:60])
    j = raw.find(end, i)
    assert j != -1, (rawname, "end", end[:60])
    return raw[i:j + len(end)]


def block(n, label, rawname, url, start, end, note=None):
    p = cut(rawname, start, end)
    MANIFEST.append({"block": n, "raw": rawname, "url": url, "chars": len(p), "text": p})
    out = "\n" + SEP + "\nBLOCK " + str(n) + " - " + label + "\nFETCHED: " + url + "\nRAW: " + rawname + "\n" + SEP + "\n\n"
    if note:
        out += "[NOTE] " + note + "\n\n"
    return out + p + "\n"


def omit(note):
    return "\n[...]\n[NOTE] " + note + "\n"


RULE = ("Transcription rule for this file: every line beneath a block heading that does not begin with\n"
        "[NOTE] or [...] is an exact, unaltered slice of the text returned by the TinyFish fetch_content tool\n"
        "for the URL in that heading, cut by script (raw[i:j]) from the saved fetch; nothing has been\n"
        "paraphrased, re-wrapped or merged. [...] marks an omission; lines beginning [NOTE] are this file's\n"
        "own annotation and are NOT source text. Fetched 2026-10-02 (S52-R1 intake, group b).\n")


def title(t):
    return t + "\n" + SEP + "\n\n" + RULE + "\n"


def write(key, text):
    open("sources/" + key + ".txt", "w").write(text)


# ---------------------------------------------------------------- Ziemann 2016
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC4994289.1/PMC4994289.1.xml"
R = "ziemann_2016-pmcxml.txt"
s = title("ZIEMANN, EREN & EL-OSTA 2016, GENOME BIOLOGY - GENE NAME ERRORS ARE WIDESPREAD IN THE SCIENTIFIC\nLITERATURE (WHOLE ARTICLE TEXT, REFERENCES OMITTED)") + """CITATION: Ziemann M, Eren Y, El-Osta A. Gene name errors are widespread in the scientific
literature. Genome Biol 2016;17:177. doi:10.1186/s13059-016-1044-7. PMID 27552985, PMCID PMC4994289
(confirmed with the PubMed tool, 2026-10-02; article type "Comment"; published 23 August 2016).
TEXT FETCHED FROM: the PMC open-access JATS XML (markdown rendering), URL below, 2026-10-02. The
extraction runs front-matter fields together at the start of block 1.
LICENCE (block 1): "This article is distributed under the terms of the Creative Commons Attribution
4.0 International License (http://creativecommons.org/licenses/by/4.0/)". The XML licence field
reads "CC BY".
WHAT THIS FILE HOLDS: licence and abstract (block 1); the whole article body - background with the
SEPT2/MARCH1 examples, methods (18 journals 2005-2015, the screen), results with the counts (35,175
files screened, 987 files and 704 articles affected, 19.6%, GEO 228 of 574 = 39.7%), Table 1 (flattened
to text), the Fig. 1 caption, and the discussion including Google Sheets and the 166 files (block 2).
OMITTED: the electronic-supplementary-material line, keywords and funder metadata, abbreviations,
acknowledgements, funding, availability, contributions, competing interests, ethics, references.
NOTE ON SCOPE: the article attributes the conversions to "Microsoft Excel, when used with default
settings" and says LibreOffice Calc and Apache OpenOffice Calc also cannot permanently deactivate
date conversion. It does not say how the error arose in any particular paper.
"""
s += block(1, "licence and abstract", R, U,
           "© The Author(s). 2016https://",
           "contain erroneous gene name conversions.")
s += omit("Supplementary-material line, keywords, funder identifiers and PMC status fields omitted.")
s += block(2, "article body, Table 1, Fig. 1 caption, discussion", R, U,
           "The problem of Excel software",
           "database curators remain vigilant.")
s += omit("Additional file, abbreviations, acknowledgements, funding, availability, contributions, "
          "competing interests, ethics and references omitted.")
write("ziemann_2016", s)

# ---------------------------------------------------------------- Herndon, Ash & Pollin 2013 (PERI WP 322)
U = "https://peri.umass.edu/images/WP322.pdf"
R = "herndon_2013_wp322-pdf.txt"
UP = "https://peri.umass.edu/publication/does-high-public-debt-consistently-stifle-economic-growth-a-critique-of-reinhart-and-rogoff/"
RP = "herndon_2013_wp322-peripage.txt"
s = title("HERNDON, ASH & POLLIN 2013, PERI WORKING PAPER 322 - DOES HIGH PUBLIC DEBT CONSISTENTLY STIFLE\nECONOMIC GROWTH? A CRITIQUE OF REINHART AND ROGOFF (EXCERPTS)") + """CITATION (what is held): Herndon T, Ash M, Pollin R. Does high public debt consistently stifle
economic growth? A critique of Reinhart and Rogoff. Working Paper 322, Political Economy Research
Institute (PERI), University of Massachusetts Amherst, April 2013. The PDF's own title page reads
"Thomas Herndon Michael Ash Robert Pollin / April 15, 2013 / JEL codes: E60, E62, E65".
PUBLISHED VERSION (NOT HELD): Herndon T, Ash M, Pollin R. Cambridge Journal of Economics
2014;38(2):257-279, doi:10.1093/cje/bet075 (volume, issue, pages and author initials confirmed from
the Crossref record https://api.crossref.org/works/10.1093/cje/bet075, 2026-10-02; published online
24 December 2013). The journal text could not be opened (academic.oup.com: bot_blocked; its PDF:
target_unreachable). Wording, tables and numbers in the journal version may differ from the
working paper; cite this file as the working paper.
TEXT FETCHED FROM: the PDF text layer via TinyFish, URL below (the request was served from
https://64.225.7.238/wp-content/uploads/joomla/images/WP322.pdf, PERI's server), 2026-10-02; and
PERI's publication page for the paper (block 1). In the PDF text layer, ligatures appear as single
characters ("ﬁ", "ﬀ"), decimals in tables are split ("4 .1"), and minus signs are "−".
WHICH REVISION: the PDF's date line still says April 15, 2013, but its text contains both corrections
PERI lists for 17 April (Belgium in the spreadsheet-error list; "in the lowest, 0–30-percent" on
p. 13) and both changes listed for 22 April (expanded Table 3; "Nine countries are available from
1946"), so the file fetched is the revised paper.
LICENCE: none stated on the PDF or on PERI's page for the paper text. PERI's page says the authors'
"Code and data are open-source under the BSD 2-clause license" - that is the code and data package,
not the paper. Treat the paper as all rights reserved: quote briefly for audit and cite.
WHAT THIS FILE HOLDS: PERI's page for the paper, whole (summary, list of linked files, the two
correction notes) (block 1); the paper from its title page and abstract through the end of section 2
"Replication" - selective exclusion of data, the "Spreadsheet coding error" paragraph with footnote 5
("RR averaged cells in lines 30 to 44 instead of lines 30 to 49."), unconventional weighting,
footnote 6 on the transcription error, and the summary (block 2); section 4 "Conclusion" with
footnote 9 ("the advantages of reproducible code relative to working spreadsheets") (block 3);
Table 2 (block 4) and Table 3 (block 5) as flattened text.
OMITTED: section 3 "Non-linearity at the 'historical boundary'?" (pp. 11-14), the references, Figures
1-4 (their text layer is plot residue), Tables 1 (it is inside block 2), 4, 5 and A-1.
"""
s += block(1, "PERI publication page for WP 322 (whole page)", RP, UP,
           "# Does High Public Debt Consistently Stifle Economic Growth?",
           "has been added.")
s += block(2, "title page, abstract, sections 1 and 2 (to the end of 'Summary: years, spreadsheet, weighting, and transcription')", R, U,
           "Does High Public Debt Consistently Stiﬂe Economic",
           "which alone accounts for one-seventh of RR’s result for the highest public debt/GDP\ncategory.")
s += omit("Section 3 'Non-linearity at the \"historical boundary\"?' and its subsection 'Different results by "
          "period' (pp. 11-14) omitted.")
s += block(3, "section 4 Conclusion, with footnote 9", R, U,
           "4 Conclusion\nThe inﬂuence",
           "austerity agenda itself in both Europe and the United States.")
s += omit("References and Figures 1-4 omitted.")
s += block(4, "Table 2 (years and growth above 90 percent, by country)", R, U,
           "Table 2: Years and real GDP growth with public debt/GDP above 90 percent, by country",
           "error of −7.6 to −7.9.")
s += block(5, "Table 3 (published and replicated average growth, by category and error)", R, U,
           "Table 3: Published and replicated average real GDP growth, by public debt/GDP category",
           "Values from bar chart in RR 2010a Figure 2 are approximate.")
s += omit("Tables 4, 5 and A-1 omitted.")
write("herndon_2013_wp322", s)

# ---------------------------------------------------------------- PHE 2020
U = "https://www.gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases"
R = "phe_2020_delayed-govuk.txt"
RB = "phe_2020_delayed-govuk-body.txt"
s = title("PUBLIC HEALTH ENGLAND, 4 OCTOBER 2020 (UPDATED 5 OCTOBER 2020) - PHE STATEMENT ON DELAYED REPORTING\nOF COVID-19 CASES (WHOLE PAGE)") + """WORK: Public Health England. PHE statement on delayed reporting of COVID-19 cases. News story,
GOV.UK. Published 4 October 2020; last updated 5 October 2020 ("Added background information").
TEXT FETCHED FROM: the GOV.UK page, URL below, 2026-10-02: once with the default extraction (block 1)
and once scoped to the page body to capture the site footer, which the default extraction drops
(block 2).
LICENCE (block 2, the page's own footer): "All content is available under the Open Government
Licence v3.0, except where otherwise stated" and "© Crown copyright".
WHAT THIS FILE HOLDS: the whole statement as rendered - title, summary, publication details, both
quoted statements (Michael Brodie; Susan Hopkins), the "Background information" section with the
cause sentence, and the table of cases by date (block 1); the footer licence line (block 2).
OMITTED: GOV.UK navigation and share links only.
WHAT THIS PAGE DOES NOT SAY: it does not name Excel, any spreadsheet program, the .xls format or a
row limit. The cause it gives is that "some files containing positive test results exceeded the
maximum file size that takes these data files and loads then into central systems" (sic). No file
may attribute the failure to Excel on the strength of this source.
NOTE ON THE NUMBERS: the statement gives 15,841 cases "between 25 September and 2 October" and
11,968 ("over 75%") in the most recent days; its table lists the cases by recorded date 24/09/2020 to
01/10/2020 (expected reporting dates 25/09/2020 to 02/10/2020), and says the delayed cases were all
Pillar 2 positives "between 24 September and 1 October".
"""
s += block(1, "the statement, whole", R, U, "News story", "| 01/10/2020 | 02/10/2020 | 4786 |")
s += omit("Share links and GOV.UK navigation omitted.")
s += block(2, "site footer licence line (body-scoped fetch of the same URL)", RB, U,
           "All content is available under the Open Government Licence v3.0",
           "© Crown copyright")
write("phe_2020_delayed", s)

# ---------------------------------------------------------------- Trisovic 2022
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC8861064.1/PMC8861064.1.xml"
R = "trisovic_2022-pmcxml.txt"
s = title("TRISOVIC, LAU, PASQUIER & CROSAS 2022, SCIENTIFIC DATA - A LARGE-SCALE STUDY ON RESEARCH CODE QUALITY\nAND EXECUTION (EXCERPTS)") + """CITATION: Trisovic A, Lau MK, Pasquier T, Crosas M. A large-scale study on research code quality and
execution. Sci Data 2022;9:60. doi:10.1038/s41597-022-01143-6. PMID 35190569, PMCID PMC8861064
(confirmed with the PubMed tool, 2026-10-02; published 21 February 2022; article type "Analysis").
Author list read from the XML header: Ana Trisovic, Matthew K. Lau, Thomas Pasquier, Mercè Crosas.
TEXT FETCHED FROM: the PMC open-access JATS XML (markdown rendering), URL below, 2026-10-02. Figures
are images and appear only as captions; Table 1 and the RQ 4 results table are flattened to text.
LICENCE (block 1): "This article is licensed under a Creative Commons Attribution 4.0 International
License".
WHAT THIS FILE HOLDS: licence and abstract (block 1); everything from the Introduction through the
end of "Best Practices and Recommendations": background, implementation and methods (2109
replication packages, 9078 R files, three R versions in a clean Docker environment, the code
cleaning step), RQ 1-RQ 10 with all their numbers, the re-execution table, Limitations of the
Study, and the recommendations for researchers, repositories and journals (block 2).
OMITTED: subject terms and funder metadata, "Related Work", the appendices, data and code
availability, acknowledgements, references.
CAUTION FOR WRITERS - THE ABSTRACT AND THE RESULTS TABLE USE DIFFERENT BASES: the abstract says "74% of
R files failed to complete without error in the initial execution, while 56% failed when code
cleaning was applied". The RQ 4 table (block 2) gives success rates of 25% without code cleaning,
40% with code cleaning and 56% for "Best of both", with time-limit-exceeded (TLE) files counted
separately; RQ 5 says the comparison that excludes TLE files shows "a total increase of about 10%".
The 56% in the abstract (failed) and the 56% in the table (success, best of both) are not the same
quantity. Quote the abstract sentence as the authors' summary, or quote the table with its row and
column labels; do not mix them. This file does not reconcile the two.
"""
s += block(1, "licence and abstract", R, U,
           "© The Author(s) 2022https://",
           "aimed at researchers, journals, and repositories.")
s += omit("Subject terms, funder identifiers and PMC status fields omitted.")
s += block(2, "Introduction through Best Practices and Recommendations", R, U,
           "Introduction\n\nResearchers increasingly",
           "We explore some aspects of this use in follow-up works46.")
s += omit("'Related Work', appendices, data and code availability, acknowledgements and references omitted.")
write("trisovic_2022", s)

# ---------------------------------------------------------------- Peng 2011
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC3383002.1/PMC3383002.1.xml"
R = "peng_2011-pmcxml.txt"
s = title("PENG 2011, SCIENCE - REPRODUCIBLE RESEARCH IN COMPUTATIONAL SCIENCE (NIH AUTHOR MANUSCRIPT, WHOLE TEXT,\nREFERENCES OMITTED)") + """CITATION: Peng RD. Reproducible research in computational science. Science 2011;334(6060):1226-1227.
doi:10.1126/science.1213847. PMID 22144613, PMCID PMC3383002, NIHMS382015 (volume, issue and pages
confirmed with the PubMed tool, 2026-10-02; published 2 December 2011).
TEXT FETCHED FROM: the PMC JATS XML of the NIH author manuscript (markdown rendering), URL below,
2026-10-02. This is the author's accepted manuscript ("NIHPA Author Manuscripts"), not the
typeset Science article; wording may differ slightly from the published version. Fig. 1 is an image;
only its caption is held.
LICENCE / TERMS (block 1, the manuscript's own statement): "This file is available for text mining. It
may also be used consistent with the principles of fair use under the copyright law." No open
licence; publisher copyright (AAAS). Quote briefly for audit and cite.
WHAT THIS FILE HOLDS: the terms statement and abstract (block 1); the whole body - replication as
the ultimate standard, reproducibility as "an attainable minimum standard", the spectrum between
full replication and no replication, the Biostatistics reproducibility policy (21 of 125 articles
with a kite-mark, five with "R"), "reproducible does not guarantee ... correctness", and the
proposed steps (block 2); the Fig. 1 caption (block 3).
OMITTED: grant line, PMC status fields, references.
"""
s += block(1, "terms statement and abstract", R, U,
           "This file is available for text mining.",
           "full independent replication of a study is not possible.")
s += omit("Grant line and PMC status fields omitted.")
s += block(2, "body", R, U,
           "The rise of computational science",
           "sustained effort from the scientific community.")
s += omit("References omitted.")
s += block(3, "Fig. 1 caption", R, U, "Fig. 1The spectrum", "The spectrum of reproducibility.")
write("peng_2011", s)

# ---------------------------------------------------------------- Sandve 2013
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC3812051.1/PMC3812051.1.xml"
R = "sandve_2013-pmcxml.txt"
s = title("SANDVE, NEKRUTENKO, TAYLOR & HOVIG 2013, PLOS COMPUTATIONAL BIOLOGY - TEN SIMPLE RULES FOR\nREPRODUCIBLE COMPUTATIONAL RESEARCH (WHOLE TEXT, REFERENCES OMITTED)") + """CITATION: Sandve GK, Nekrutenko A, Taylor J, Hovig E. Ten simple rules for reproducible computational
research. PLoS Comput Biol 2013;9(10):e1003285. doi:10.1371/journal.pcbi.1003285. PMID 24204232,
PMCID PMC3812051 (confirmed with the PubMed tool, 2026-10-02; published 24 October 2013; an
Editorial, edited by Philip E. Bourne).
TEXT FETCHED FROM: the PMC open-access JATS XML (markdown rendering), URL below, 2026-10-02.
LICENCE (block 1): "© 2013 Sandve et al ... This is an open-access article distributed under the terms
of the Creative Commons Attribution License, which permits unrestricted use, distribution, and
reproduction in any medium, provided the original author and source are properly credited." The
XML licence link is https://creativecommons.org/licenses/by/4.0/ and its licence field reads "CC BY".
WHAT THIS FILE HOLDS: the copyright and licence statement (block 1); the whole text - introduction
and Rules 1 to 10, each with its "As a minimum" sentence (block 2).
OMITTED: author affiliations, funding statement, PMC status fields, references.
"""
s += block(1, "copyright and licence", R, U,
           "© 2013 Sandve et al2013",
           "provided the original author and source are properly credited.")
s += omit("Funding statement and PMC status fields omitted.")
s += block(2, "introduction and Rules 1-10", R, U,
           "Replication is the cornerstone",
           "cited by other researchers after publication [25].")
s += omit("References omitted.")
write("sandve_2013", s)

# ---------------------------------------------------------------- Wilson 2017
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC5480810.1/PMC5480810.1.xml"
R = "wilson_2017-pmcxml.txt"
s = title("WILSON, BRYAN, CRANSTON, KITZES, NEDERBRAGT & TEAL 2017, PLOS COMPUTATIONAL BIOLOGY - GOOD ENOUGH\nPRACTICES IN SCIENTIFIC COMPUTING (EXCERPTS)") + """CITATION: Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, Teal TK. Good enough practices in
scientific computing. PLoS Comput Biol 2017;13(6):e1005510. doi:10.1371/journal.pcbi.1005510.
PMID 28640806, PMCID PMC5480810 (confirmed with the PubMed tool, 2026-10-02; published 22 June 2017;
a Perspective). Author list read from the XML header: Greg Wilson, Jennifer Bryan, Karen Cranston,
Justin Kitzes, Lex Nederbragt, Tracy K. Teal.
TEXT FETCHED FROM: the PMC open-access JATS XML (markdown rendering), URL below, 2026-10-02. Box
layouts are flattened (one line per item); Fig 1 is an image, caption only.
LICENCE (block 1): "© 2017 Wilson et al ... This is an open access article distributed under the terms
of the Creative Commons Attribution License, which permits unrestricted use, distribution, and
reproduction in any medium, provided the original author and source are credited." The XML licence
link is https://creativecommons.org/licenses/by/4.0/.
WHAT THIS FILE HOLDS: the licence and author summary (block 1); Overview, Introduction, Box 1 (summary
of practices), the whole of "Data management" (1a save the raw data, 1c replace "-99" with NA,
1d tidy data, 1e record all steps, 1f unique identifiers), "Software" (2a-2j, including 2g make
dependencies explicit), "Collaboration" (3a README, 3d LICENSE, 3e CITATION) and "Project
organization" (4a-4f, Box 2 "runall" script, Box 3 project layout) (block 2); the opening of "Keeping
track of changes" (block 3); the Conclusion (block 4).
OMITTED: the rest of "Keeping track of changes" (manual versioning and version control detail),
"Manuscripts", "What we left out", acknowledgements, references.
"""
s += block(1, "licence and author summary", R, U,
           "© 2017 Wilson et al2017",
           "workshops to over 11,000 people since 2010.")
s += omit("Funding line and PMC status fields omitted.")
s += block(2, "Overview through Project organization (Boxes 1-3)", R, U,
           "Overview\n\nWe present",
           "describing the project findings.")
s += block(3, "opening of Keeping track of changes", R, U,
           "Keeping track of changes\n\nKeeping track",
           "manage changes to the same set of files.")
s += omit("Rest of 'Keeping track of changes', 'Manuscripts' and 'What we left out' omitted.")
s += block(4, "Conclusion", R, U,
           "Conclusion\n\nWe have outlined",
           "looks like and how to achieve it.")
s += omit("Acknowledgements and references omitted.")
write("wilson_2017", s)

# ---------------------------------------------------------------- Wickham 2014
U = "https://www.jstatsoft.org/index.php/jss/article/view/v059i10/772"
R = "wickham_2014_tidy-jsspdf.txt"
UP = "https://www.jstatsoft.org/article/view/v059i10"
RP = "wickham_2014_tidy-jsspage-body.txt"
s = title("WICKHAM 2014, JOURNAL OF STATISTICAL SOFTWARE - TIDY DATA (EXCERPTS: SECTIONS 1-3)") + """CITATION: Wickham H. Tidy data. J Stat Softw 2014;59(10):1-23. doi:10.18637/jss.v059.i10. The PDF's
own header reads "August 2014, Volume 59, Issue 10"; its back matter "Submitted: 2013-02-20 /
Accepted: 2014-05-09" (block 3). Pages 1-23 from the article page metadata
("dc.identifier.pagenumber": "1 - 23") and the last page number of the PDF; single author confirmed
from the PDF title page and the Crossref record (https://api.crossref.org/works/10.18637/jss.v059.i10).
TEXT FETCHED FROM: the article PDF's text layer via TinyFish (URL below; served from
https://www.jstatsoft.org/article/download/v059i10/772), 2026-10-02; and the article page, scoped to
the page body so that the licence box is kept (block 1). In the PDF text layer ligatures appear as
single characters ("ﬁ", "ﬀ") and tables are flattened to space-separated text.
LICENCE (block 1, the article page): "Article: Creative Commons Attribution License (CC-BY)" and
"Software: GPL General Public License version 2 or version 3 or a GPL-compatible license." The page
links the licence to http://creativecommons.org/licenses/by/3.0/; its metadata field dc.rights reads
"Copyright (c) 2013 Hadley Wickham". The PDF itself states no licence.
WHAT THIS FILE HOLDS: the licence box (block 1); the PDF from its header and abstract through the end
of section 3 - section 1 Introduction, section 2 "Defining tidy data" (2.1 data structure, 2.2 data
semantics with the variable and observation definitions, 2.3 the three rules), and section 3
"Tidying messy datasets" with the five common problems and 3.1-3.5 including Tables 1-12 as flattened
text (block 2); the affiliation and submission dates (block 3).
OMITTED: section 4 "Tidy tools", section 5 "Case study", section 6 "Discussion", acknowledgements,
references.
"""
s += block(1, "article page licence box (body-scoped fetch)", RP, UP,
           "## License Information",
           "GPL-compatible license.")
s += block(2, "header, abstract, sections 1-3", R, U,
           "JSS\n Journal of Statistical Software",
           "making tidying this dataset a\nconsiderable challenge.")
s += omit("Sections 4 'Tidy tools', 5 'Case study' and 6 'Discussion', acknowledgements and references omitted.")
s += block(3, "affiliation and submission dates", R, U,
           "Aﬃliation:\nHadley Wickham",
           "Accepted: 2014-05-09")
write("wickham_2014_tidy", s)

# ---------------------------------------------------------------- Broman & Woo 2018
UM = "https://kbroman.org/Paper_DataOrg/manuscript.html"
RM = "broman_woo_2018-manuscripthtml.txt"
UV = "https://peerj.com/preprints/3183v2.html"
RV = "broman_woo_2018-peerjv2html.txt"
UL = "https://github.com/kbroman/Paper_DataOrg/blob/master/LICENSE.md"
RL = "broman_woo_2018-githublicense.txt"
s = title("BROMAN & WOO 2018 - DATA ORGANIZATION IN SPREADSHEETS (AUTHORS' MANUSCRIPT, WHOLE TEXT, REFERENCES\nOMITTED; PREPRINT ABSTRACT AND LICENCE)") + """CITATION (journal version, NOT HELD): Broman KW, Woo KH. Data organization in spreadsheets. Am Stat
2018;72(1):2-10. doi:10.1080/00031305.2017.1375989. Volume, issue, pages and authors confirmed from
the Crossref record (https://api.crossref.org/works/10.1080/00031305.2017.1375989, 2026-10-02;
published online 24 April 2018, issue dated 2 January 2018). The journal page (tandfonline.com)
answered "bot_blocked" on 2026-10-02 and was not read.
PREPRINT: Broman KW, Woo KH. Data organization in spreadsheets. PeerJ Preprints 6:e3183v2 (2018),
doi:10.7287/peerj.preprints.3183v2 (block 1). The preprint PDF (peerj.com/preprints/3183v2.pdf) was
"target_unreachable"; its HTML page gives the abstract and licence only.
WHAT IS QUOTED HERE: the authors' own manuscript as published by the first author at
kbroman.org/Paper_DataOrg/manuscript.html, compiled from manuscript.Rmd in the repository
github.com/kbroman/Paper_DataOrg, whose README names the American Statistician article (block 3). It
is the authors' version, not the typeset journal article, and which revision it matches (PeerJ v1,
v2 or the accepted journal text) is not stated on the page; wording may differ from the journal
version. Figures are images; only their captions are held.
LICENCE: PeerJ preprint v2 page (block 1): "This is an open access article distributed under the
terms of the Creative Commons Attribution License"; its Crossref record lists
http://creativecommons.org/licenses/by/4.0/. Repository LICENSE.md (block 2): 'The manuscript "Data
organization in spreadsheets" is licensed under CC BY' (the repository README links CC BY 3.0). The
journal version's licence was not seen.
WHAT THIS FILE HOLDS: the PeerJ preprint v2 page - licence and abstract listing the twelve principles
(block 1); the repository licence statement (block 2); the whole manuscript - introduction (Panko's
88% of 13 audited spreadsheets; Excel converting gene names to dates) and every section: be
consistent (missing-value codes, no -999), choose good names, write dates as YYYY-MM-DD (Excel's
1900/1904 day counts; Ziemann et al. "~20%"), no empty cells, one thing in a cell, make it a
rectangle, create a data dictionary, no calculations in raw data files, no colour as data, make
backups, data validation, save as plain text, and the summary (block 3).
OMITTED: GitHub page navigation (block 2), the manuscript's acknowledgements and references.
"""
s += block(1, "PeerJ Preprints v2 page: licence and abstract", RV, UV,
           "# Data organization in spreadsheets",
           "simplified one bit of text.")
s += block(2, "repository LICENSE.md statement", RL, UL,
           "The manuscript \"",
           "is licensed under\nCC BY")
s += block(3, "authors' manuscript, whole text", RM, UM,
           "# Data organization in spreadsheets\n\n#### *Karl W. Broman*",
           "so you never lose the record of what you did to the data.")
s += omit("Acknowledgments and References omitted.")
write("broman_woo_2018", s)

json.dump(MANIFEST, open("books/S52-R1/intake/manifest-b.json", "w"), ensure_ascii=False, indent=1)
print(len(MANIFEST), "passages written")
