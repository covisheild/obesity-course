# Builds the group-C2 source files for S58-R1 from the saved raw fetches in books/S58-R1/intake/raw/.
# Every passage is raw[i:j]: either a run of whole lines (L) or a span from a start marker to an end marker
# inclusive (M). Nothing in a passage is typed by hand. Run from the repository root.
# Raw files are the `text` field of mcp__TinyFish__fetch_content results, JSON-decoded unchanged and written out
# by script from the session's saved tool results (see each .meta.json beside the raw file).
import json

RAW = "books/S58-R1/intake/raw/"
SEP = "=" * 100
MANIFEST = []


def L(rawname, a, b):
    """Lines a..b (1-indexed, inclusive) of the raw file, as the exact slice raw[i:j]."""
    raw = open(RAW + rawname).read()
    starts = [0]
    for k, ch in enumerate(raw):
        if ch == "\n":
            starts.append(k + 1)
    i = starts[a - 1]
    j = (starts[b] - 1) if b < len(starts) else len(raw)
    return raw[i:j]


def M(rawname, start, end):
    raw = open(RAW + rawname).read()
    i = raw.find(start)
    assert i != -1, (rawname, start[:60])
    j = raw.find(end, i)
    assert j != -1, (rawname, end[:60])
    return raw[i:j + len(end)]


def block(n, rawname, url, heading, text, note=None):
    MANIFEST.append({"raw": rawname, "url": url, "chars": len(text)})
    out = "\n" + SEP + "\nBLOCK " + str(n) + " - " + heading + "\nFETCHED: " + url + "\n" + SEP + "\n\n"
    if note:
        out += "[NOTE] " + note + "\n\n"
    return out + text + "\n"


def omit(note):
    return "\n[...]\n[NOTE] " + note + "\n"


RULE = ("Transcription rule for this file: every line beneath a block heading that does not begin with\n"
        "[NOTE] and comes before the next [...] is an exact, unaltered slice of the text returned by the TinyFish\n"
        "fetch_content tool for the URL in that heading, cut by script (raw[i:j]) from the saved fetch\n"
        "(books/S58-R1/intake/build-C2.py); nothing has been paraphrased, re-wrapped or merged. [...] marks an\n"
        "omission; lines beginning [NOTE] are this file's own annotation and are NOT source text.\n"
        "Fetched 2026-10-02 (session clock; the fetch records carry 2026-10-01 UTC).\n")

# =============================================================================== Correll 2020
R, RA, RL = "C2-correll_2020-arxiv-pdf.txt", "C2-correll_2020-arxiv-abs.txt", "C2-correll_2020-arxiv-licence.txt"
U = "https://arxiv.org/pdf/1907.02035v2"
UA = "https://arxiv.org/abs/1907.02035"
UL = "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"
s = """CORRELL, BERTINI AND FRANCONERI 2020, TRUNCATING THE Y-AXIS: THREAT OR MENACE? - VERBATIM EXCERPTS
""" + SEP + "\n\n" + RULE + """
WORK: Correll M, Bertini E, Franconeri S. Truncating the Y-Axis: Threat or Menace? In: Proceedings of the 2020
CHI Conference on Human Factors in Computing Systems (CHI '20). ACM, 2020: 1-12.
doi:10.1145/3313831.3376222 (pages 1-12 confirmed from the Crossref record,
https://api.crossref.org/works/10.1145/3313831.3376222, fetched 2026-10-02 and saved as raw C2-correll_2020-crossref.txt).
TEXT FETCHED FROM: the authors' arXiv version, arXiv:1907.02035v2 (8 Jan 2020), PDF text layer:
https://arxiv.org/pdf/1907.02035v2 (TinyFish fetch_content, markdown). The arXiv abstract page
https://arxiv.org/abs/1907.02035 was fetched the same day (block 1). The ACM Digital Library was NOT used.
VERSION: this is the arXiv preprint (v2, revised 8 Jan 2020), not the ACM typeset version. Its text matches the
CHI paper's title and authors; page numbers of the CHI version are not visible in it, so locate passages by
section heading (EXPERIMENT, Experiment One, Results, DISCUSSION, Conclusion).
LICENCE AS STATED: the arXiv abstract page links "view license" to http://arxiv.org/licenses/nonexclusive-distrib/1.0/
(the link is in the page's outbound links, recorded in C2-correll_2020-arxiv-abs-licencelink.meta.json). That
page (block 2) reads: "I grant arXiv.org a perpetual, non-exclusive license to distribute this article." This
is arXiv's minimal distribution licence, not an open reuse licence: the authors (and ACM, for the CHI version;
Crossref lists https://www.acm.org/publications/policies/copyright_policy) keep their rights. Quote briefly
and cite; do not reproduce at length.

WHAT THIS FILE HOLDS: the arXiv abstract-page record (block 1); the arXiv licence page (block 2); from the
PDF text layer, the whole running text of the paper from the title to the end of the Conclusion, in eleven
runs, with every figure caption (Figs 1-4, 6-9) kept in place (blocks 3-13).
OMITTED: the arXiv side-stamp line; the chart text that the PDF text layer extracts from inside Figures 1-9
(axis tick labels, panel letters, plotted labels: these are not prose and are not readable as text); the
Figure 5 caption with its stimuli; Acknowledgments; References. Every omission is marked [...] in place.
TEXT-LAYER ARTEFACTS kept as they stand: ligatures (the "fi" ligature appears as a single character),
line-end hyphenation ("harm-\\nful"), symbols flattened ("Mage = 27.7" is M subscript age; "F(2,76) = 89"),
Eslope and Emagnitude formulas with flattened subscripts ("Q f irst" is Q subscript first). A fraction in the
coders' discussion appears as "( 5\\n97 of codes)" (5/97).
KEY NUMBERS HELD (for C16): Experiment One, 40 participants, "increased y-axis truncation results in increased
perceived severity (F(2,76) = 89, p < 0.0001)"; no effect of chart type "(F(1,38) = 0.5, p = 0.50)"; framing
effect 0.07 against "an increase of 0.36 for starting the y-axis at 25% rather than 0%"; Experiment Two, 32
participants, broken-axis and gradient designs did not differ "(F(2,60) = 3.1, p = 0.05)"; Experiment Three, 25
participants, truncation still raised severity "(F(1,20) = 11,p = 0.003)" while trend-estimation error did not
differ "(F(1,20) = 0.002, p = 0.96)"; the Fig 1 caption's Fox News example, "the second bar is 6 times taller
than the first bar, even though there is only a 4.6% increase in tax rate (ratio of 1.13 to 1)".
Absence of a passage from this file is not absence from the paper.
"""
s += block(1, RA, UA, "arXiv abstract page: submission dates, title, authors, abstract, identifiers", L(RA, 3, 21))
s += block(2, RL, UL, "arXiv licence page linked from the abstract page as 'view license'", L(RL, 1, 18),
           note="The fetch followed a redirect to https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html.")
s += block(3, R, U, "Title, authors, ABSTRACT, INTRODUCTION, EXISTING GUIDELINES (Huff; Brinton, opening)", L(R, 1, 103))
s += omit("The arXiv side-stamp line ('arXiv:1907.02035v2 [cs.HC] 8 Jan 2020') and the chart text extracted from "
          "inside Figure 1 (axis tick values, panel labels) omitted. The Figure 1 caption follows.")
s += block(4, R, U, "Figure 1 caption", L(R, 176, 179))
s += omit("Chart text extracted from inside Figure 2 (axis labels 'Billion Dollars', tick values, month letters) omitted. "
          "The Figure 2 caption follows, then the running text resumes with Brinton's quoted rule.")
s += block(5, R, U, "Figure 2 caption; EXISTING GUIDELINES continued (Brinton, Cairo, Bergstrom & West)", L(R, 214, 259))
s += block(6, R, U, "EXISTING GUIDELINES continued (Tufte, Skelton, Jones; competing considerations)", L(R, 261, 315))
s += omit("Chart text extracted from inside Figure 3 (axis tick values and labels of four example charts; the panel "
          "sub-captions (a)-(d) sit among the tick values) omitted. The Figure 3 caption follows, then the running text.")
s += block(7, R, U, "Figure 3 caption; prior empirical results (Pandey et al., Witt)", L(R, 386, 396))
s += omit("Panel labels and tick values extracted from inside Figure 4 omitted. The Figure 4 caption follows.")
s += block(8, R, U, "Figure 4 caption; prior results continued; Research Questions; EXPERIMENT (general method)", L(R, 422, 547))
s += omit("Figure 5 stimuli labels and caption ('The two visualization designs in Experiment One') omitted.")
s += block(9, R, U, "Experiment One: Framing Interventions (methods, hypotheses, results); Experiment Two (opening, methods)",
           L(R, 552, 708))
s += omit("Plotted values and axis labels extracted from inside Figure 6 omitted. The Figure 6 caption follows.")
s += block(10, R, U, "Figure 6 caption", L(R, 739, 742))
s += omit("Panel labels of Figure 7 omitted. The Figure 7 caption follows.")
s += block(11, R, U, "Figure 7 caption; Experiment Two continued (designs, hypotheses, results); Experiment Three (methods, hypotheses, results opening)",
           L(R, 747, 894))
s += omit("Plotted points and axis labels extracted from inside Figure 8 omitted. The Figure 8 caption follows.")
s += block(12, R, U, "Figure 8 caption", L(R, 936, 941))
s += omit("Plotted points and axis labels extracted from inside Figure 9 omitted. The Figure 9 caption follows, "
          "then the running text to the end of the Conclusion.")
s += block(13, R, U, "Figure 9 caption; Experiment Three results; DISCUSSION; Limitations & Future Work; Conclusion",
           L(R, 975, 1099))
s += omit("ACKNOWLEDGMENTS and REFERENCES omitted.")
open("sources/correll_2020_truncating_yaxis.txt", "w").write(s)

# =============================================================================== Heer & Bostock 2010
R, RP = "C2-heer_bostock_2010-authorpdf.txt", "C2-heer_bostock_2010-labpage.txt"
U = "http://vis.stanford.edu/files/2010-MTurk-CHI.pdf"
UP = "http://vis.stanford.edu/papers/crowdsourcing-graphical-perception"
s = """HEER AND BOSTOCK 2010, CROWDSOURCING GRAPHICAL PERCEPTION - VERBATIM EXCERPTS
""" + SEP + "\n\n" + RULE + """
WORK: Heer J, Bostock M. Crowdsourcing graphical perception: using Mechanical Turk to assess visualization
design. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '10). ACM, 2010:
203-212. doi:10.1145/1753326.1753357 (pages confirmed from the Crossref record,
https://api.crossref.org/works/10.1145/1753326.1753357, saved as raw C2-heer_bostock_2010-crossref.txt, and
from the lab's paper page, block 1).
TEXT FETCHED FROM: the authors' own copy on their lab site (Stanford Visualization Group),
http://vis.stanford.edu/files/2010-MTurk-CHI.pdf (PDF text layer; TinyFish fetch_content, markdown). The fetch
was served from the lab server's address (final URL http://171.67.77.70/files/2010-MTurk-CHI.pdf). The lab's
paper page http://vis.stanford.edu/papers/crowdsourcing-graphical-perception (block 1) gives the abstract and
the citation "ACM Human Factors in Computing Systems (CHI), 203-212, 2010". The ACM Digital Library was NOT used.
LICENCE AS STATED (block 4, the paper's own notice): "Permission to make digital or hard copies of all or part
of this work for personal or classroom use is granted without fee provided that copies are not made or
distributed for profit or commercial advantage and that copies bear this notice and the full citation on the
first page." and "Copyright 2010 ACM". Publisher copyright; author-posted copy. Quote briefly and cite.

WHAT THIS FILE HOLDS: the lab paper page (block 1); title, abstract and keywords (block 2); the opening of the
Introduction (block 3); the ACM notice (block 4); the rest of the Introduction and the whole GRAPHICAL
PERCEPTION section (block 5); RESEARCH GOALS and EXPERIMENT 1A (proportional judgment; the Cleveland & McGill
replication) with the Figure 3 and 4 captions (blocks 6-9); EXPERIMENT 1B (rectangular area judgments) with
the Figure 5 caption (blocks 8, 10); FINDINGS AND FUTURE WORK (block 11).
OMITTED: WEB-BASED EXPERIMENTS AND MECHANICAL TURK; Experiment 2 (gridline alpha contrast); Experiment 3 (chart
size and gridline spacing; its result is restated in block 10); MECHANICAL TURK: PERFORMANCE AND COST;
References; the chart text extracted from inside Figures 1-5; the Figure 1 and 2 stimulus captions.
TEXT-LAYER ARTEFACTS kept as they stand: ligatures, line-end hyphenation, and the log-error formula flattened
across two lines ("log 2(|judged percent - true percent| + 1\\n8)" is log2(|judged - true| + 1/8)); the
footnote's "1\\n8 term" is the 1/8 term.
KEY CONTENT (for C14): seven judgment types (position on a common scale T1-T3, length T4-T5, angle T6, circular
area T7) plus rectangular area (T8, T9); "The ranking of types by accuracy is consistent between the two
experiments (Figure 4)"; "position encoding still significantly outperformed length encoding"; "psychophysical
theory [7, 34] predicts area to perform worse than angle, and both to be significantly worse than position";
"only 14 out of 3,481 were incorrect (0.4%)"; N=50 subjects per chart.
Absence of a passage from this file is not absence from the paper.
"""
s += block(1, RP, UP, "The lab's paper page: title, abstract, citation (whole page as extracted)", L(RP, 1, 999))
s += block(2, R, U, "Title, authors, ABSTRACT, classification, keywords", L(R, 1, 27))
s += block(3, R, U, "INTRODUCTION, opening paragraphs", L(R, 28, 43))
s += block(4, R, U, "The ACM permission and copyright notice (first-page footer)", L(R, 44, 51))
s += block(5, R, U, "INTRODUCTION continued; GRAPHICAL PERCEPTION", L(R, 52, 144))
s += omit("WEB-BASED EXPERIMENTS AND MECHANICAL TURK omitted (how MTurk works; prior MTurk studies).")
s += block(6, R, U, "RESEARCH GOALS; EXPERIMENT 1A: PROPORTIONAL JUDGMENT, Method", L(R, 206, 267))
s += omit("Chart text extracted from inside Figures 1 and 2 (stimuli: bar charts, a pie, a bubble chart, a treemap) "
          "and their captions omitted.")
s += block(7, R, U, "EXPERIMENT 1A continued (task format); Results, with footnote 1 (midmean; log scale)", L(R, 285, 319))
s += omit("Plotted values and axis labels extracted from inside Figure 3 omitted. The Figure 3 caption follows.")
s += block(8, R, U, "Figure 3 caption; Experiment 1A results continued (angle, area); EXPERIMENT 1B, opening and Method",
           L(R, 338, 375))
s += omit("Axis labels extracted from inside Figures 4 and 5 omitted; the Figure 4 caption follows, then the "
          "Figure 5 caption and the running text.")
s += block(9, R, U, "Figure 4 caption", L(R, 396, 398))
s += omit("Axis values and aspect-ratio labels of Figure 5 omitted.")
s += block(10, R, U, "Figure 5 caption; EXPERIMENT 1B Method continued; Results", L(R, 408, 463))
s += omit("EXPERIMENT 2 (gridline alpha contrast), EXPERIMENT 3 (chart size and gridline spacing) and MECHANICAL TURK: "
          "PERFORMANCE AND COST omitted.")
s += block(11, R, U, "FINDINGS AND FUTURE WORK (whole section)", L(R, 924, 1014))
s += omit("REFERENCES omitted.")
open("sources/heer_bostock_2010_crowdsourcing_perception.txt", "w").write(s)

# =============================================================================== Weissgerber 2015
R = "C2-weissgerber_2015-pmcxml.txt"
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC4406565.1/PMC4406565.1.xml"
s = """WEISSGERBER, MILIC, WINHAM AND GAROVIC 2015, BEYOND BAR AND LINE GRAPHS - VERBATIM SOURCE PACK
""" + SEP + "\n\n" + RULE + """
WORK: Weissgerber TL, Milic NM, Winham SJ, Garovic VD. Beyond bar and line graphs: time for a new data
presentation paradigm. PLoS Biol 2015;13(4):e1002128.
PMID 25901488; PMCID PMC4406565; DOI 10.1371/journal.pbio.1002128 (confirmed with the PubMed tools,
convert_article_ids and get_article_metadata, 2026-10-02).
TEXT FETCHED FROM: the PMC open-access JATS XML, https://pmc-oa-opendata.s3.amazonaws.com/PMC4406565.1/PMC4406565.1.xml
(TinyFish fetch_content, markdown, which strips the XML tags and runs front-matter fields together).
LICENCE AS STATED (block 2): "© 2015 Weissgerber et al" with https://creativecommons.org/licenses/by/4.0/ and
"This is an open-access article distributed under the terms of the Creative Commons Attribution License, which
permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source
are properly credited." CC BY 4.0.

WHAT THIS FILE HOLDS: the title, authors and affiliations (block 1, front matter as the extraction runs it
together); the licence (block 2); the abstract and the one-line summary (block 3); the WHOLE article body
from the first paragraph to the end of Conclusions, including Figure 1-3 captions, Box 1 and the three
recommendations (block 4); the S2 Fig legend (block 5).
OMITTED: funding statement; Supporting Information file descriptions other than S2 Fig (S1 Text, S2-S6 Text,
S1 Fig); abbreviations; references. The figures themselves are images and are not held.
NOTE ON EXTRACTION: citation numbers run into words ("Medical Journal [1]" keeps its brackets, but some
reference cues are flattened); front-matter fields are concatenated without spaces (block 1).
KEY NUMBERS HELD (for C15): systematic review of "research articles published in top physiology journals
(n = 703)"; "85.6% of papers included at least one bar graph"; sample-size and analysis figures in the body
("78.1% of studies performed only parametric analyses"); "Many different datasets can lead to the same bar graph"
(Fig 1 title).
Absence of a passage from this file is not absence from the article.
"""
s += block(1, R, U, "Front matter: article type, title, authors, affiliations, competing interests",
           M(R, "PerspectiveBeyond Bar and Line Graphs", "The authors have declared that no competing interests exist."),
           note="Cut from the article-type word 'Perspective' onward; the journal and identifier codes before it on the "
                "same line are omitted.")
s += block(2, R, U, "Corresponding e-mail, dates and licence (front matter)",
           M(R, "\\* E-mail: weissgerber.tracey@mayo.edu", "provided the original author and source are properly credited."),
           note="The digits run together after the e-mail address are the PMC publication-date and volume fields, not prose.")
s += block(3, R, U, "Abstract; one-line summary", L(R, 21, 23))
s += omit("Funding statement omitted.")
s += block(4, R, U, "Whole article body: introduction, Figs 1-3 captions, systematic review, Box 1, recommendations, Conclusions",
           L(R, 27, 95))
s += omit("Supporting Information descriptions S1 Text to S1 Fig omitted.")
s += block(5, R, U, "S2 Fig legend: figure types, sample sizes, and statistical analysis", L(R, 151, 153))
s += omit("Remaining supporting-information lines, abbreviations and references omitted.")
open("sources/weissgerber_2015_beyond_bar_graphs.txt", "w").write(s)

# =============================================================================== Bateman 2010
R, RP = "C2-bateman_2010-columbia-pdf.txt", "C2-bateman_2010-authorpage.txt"
U = "https://sites.stat.columbia.edu/gelman/communication/Bateman2010.pdf"
UP = ("https://scottbateman.github.io/publication/2010-01-01-Useful-junk-The-effects-of-visual-embellishment-on-"
      "comprehension-and-memorability-of-charts")
s = """BATEMAN, MANDRYK, GUTWIN, GENEST, McDINE AND BROOKS 2010, USEFUL JUNK? - VERBATIM EXCERPTS
""" + SEP + "\n\n" + RULE + """
WORK: Bateman S, Mandryk RL, Gutwin C, Genest A, McDine D, Brooks C. Useful junk? The effects of visual
embellishment on comprehension and memorability of charts. In: Proceedings of the SIGCHI Conference on Human
Factors in Computing Systems (CHI '10). ACM, 2010: 2573-2582. doi:10.1145/1753326.1753716 (pages confirmed from
the Crossref record, https://api.crossref.org/works/10.1145/1753326.1753716, saved as raw
C2-bateman_2010-crossref.txt, and from the page footers in the PDF: first page 2573, last page 2582).
TEXT FETCHED FROM: a public copy of the camera-ready PDF on a THIRD-PARTY academic host, NOT an author's site:
https://sites.stat.columbia.edu/gelman/communication/Bateman2010.pdf (Andrew Gelman's "communication" reading
folder, Columbia University Department of Statistics; served from 128.59.30.7). PDF text layer, TinyFish
fetch_content, markdown. The PDF's own metadata title is "Microsoft Word - pap0297-bateman3.doc" and every
page carries the CHI 2010 running footer, so it is the authors' camera-ready file as printed in the
proceedings. The ACM Digital Library was NOT used.
WHY NOT AN AUTHOR COPY: the first author's publication page (block 1) gives the citation only, with no PDF;
the lab pages (hci.usask.ca member pages for Mandryk and Gutwin) load their publication lists by script and
show no file; the lab's former upload URL (hci.usask.ca/uploads/173-pap0161-bateman.pdf) and its Wayback copy
returned "target_unreachable". See log-C2.md. Harsh may prefer to replace this with his own ACM DL download.
LICENCE AS STATED (block 4, the paper's own notice): "Permission to make digital or hard copies of all or part
of this work for personal or classroom use is granted without fee provided that copies are not made or
distributed for profit or commercial advantage and that copies bear this notice and the full citation on the
first page." and "Copyright 2010 ACM". Publisher copyright. Quote briefly and cite.

WHAT THIS FILE HOLDS: the first author's page for the paper (block 1); title, authors, abstract, keywords
(block 2); the Introduction (blocks 3, 5) and the ACM notice (block 4); COMPARISON OF PLAIN AND EMBELLISHED
CHARTS: design, participants, apparatus, procedure, measures (blocks 6-7); RESULTS: description, recall, user
preferences, gaze detection (blocks 8-11); the whole DISCUSSION including design implications and "The wider
problem of bias in charts" (block 12); CONCLUSION (block 13).
OMITTED: PREVIOUS WORK (the chartjunk debate, interpretation time and errors, aesthetics, memorability);
figure contents and the labels the text layer extracts from inside Figures 3-9; Acknowledgements; References.
TEXT-LAYER ARTEFACTS kept as they stand: stray spaces inside words ("fo r", "s ubject", "pr eferred"), page
running footers ("CHI 2010: Graphs / April 10-15, 2010, Atlanta, GA, USA / <page>") where they fall inside a
run, and subscripts flattened ("t 19=0.84" is t with 19 df).
KEY NUMBERS HELD (for C17): 20 participants, 14 Holmes charts and plain versions; description accuracy no
different (subject t19=0.84, p=.412; categories t19=1.38, p=.185; trend t19=0.23, p=.818); value message better
for Holmes charts (t19=3.37, p=.003); long-term recall (2-3 weeks) better for Holmes charts (subject t9=2.56,
p=.015; categories t9=5.03; trend t9=1.95, p=.042; value message t9=2.41, p=.020); no difference after a
five-minute gap except the value message.
Absence of a passage from this file is not absence from the paper.
"""
s += block(1, RP, UP, "First author's own publication page for the paper (citation only; no PDF offered)", L(RP, 1, 999))
s += block(2, R, U, "Title, authors, ABSTRACT, keywords, classification, general terms", L(R, 1, 33))
s += block(3, R, U, "INTRODUCTION (first column)", L(R, 34, 63))
s += block(4, R, U, "The ACM permission and copyright notice (first-page footer) and page footer", L(R, 65, 76))
s += block(5, R, U, "INTRODUCTION continued", L(R, 78, 124))
s += omit("PREVIOUS WORK omitted (The Debate over Visual Embellishment; Interpretation Time and Errors; Aesthetics and "
          "Preferences; Chart Memorability).")
s += block(6, R, U, "COMPARISON OF PLAIN AND EMBELLISHED CHARTS: design; Participants and Apparatus; Procedure; Measures (to Gaze Data)",
           L(R, 273, 506))
s += omit("Region labels extracted from inside Figure 3 ('data', 'embellishment', 'dual coded') omitted.")
s += block(7, R, U, "Gaze Data, continued", L(R, 513, 515))
s += block(8, R, U, "RESULTS: opening; Description; Recall (immediate group)", L(R, 516, 566))
s += omit("Axis values and labels extracted from inside Figures 4 and 5 omitted; the Figure 6 caption follows.")
s += block(9, R, U, "Figure 6 caption; Recall (long-term group) and prompting", L(R, 606, 627))
s += omit("Axis values and labels extracted from inside Figure 7 omitted.")
s += block(10, R, U, "User Preferences", L(R, 646, 659))
s += omit("Axis values and labels extracted from inside Figure 8 omitted.")
s += block(11, R, U, "Gaze Detection", L(R, 671, 693))
s += omit("Values and labels extracted from inside Figure 9 omitted.")
s += block(12, R, U, "DISCUSSION (whole): five findings; explanations; Design Questions and Implications; The wider problem of bias in charts",
           L(R, 714, 943))
s += block(13, R, U, "CONCLUSION", L(R, 944, 963))
s += omit("ACKNOWLEDGEMENTS and REFERENCES omitted.")
open("sources/bateman_2010_useful_junk.txt", "w").write(s)

# =============================================================================== Crameri 2020
R = "C2-crameri_2020-pmcxml.txt"
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC7595127.1/PMC7595127.1.xml"
s = """CRAMERI, SHEPHARD AND HERON 2020, THE MISUSE OF COLOUR IN SCIENCE COMMUNICATION - VERBATIM SOURCE PACK
""" + SEP + "\n\n" + RULE + """
WORK: Crameri F, Shephard GE, Heron PJ. The misuse of colour in science communication. Nat Commun
2020;11(1):5444. PMID 33116149; PMCID PMC7595127; DOI 10.1038/s41467-020-19160-7 (confirmed with the PubMed
tools, 2026-10-02). Article type: Perspective.
TEXT FETCHED FROM: the PMC open-access JATS XML, https://pmc-oa-opendata.s3.amazonaws.com/PMC7595127.1/PMC7595127.1.xml
(TinyFish fetch_content, markdown, which strips the XML tags).
LICENCE AS STATED (block 1): "© The Author(s) 2020" with https://creativecommons.org/licenses/by/4.0/ and "Open
Access This article is licensed under a Creative Commons Attribution 4.0 International License ..." CC BY 4.0
(third-party material excepted, as the statement says).

WHAT THIS FILE HOLDS: the licence statement (block 1); the abstract (block 2); the WHOLE article body from
the Introduction to the end of "A proactive step forward for the science community", including Boxes 1 and 2,
the "How to recognise an unscientific colour map" checks, and the figure captions (block 3).
OMITTED: the editor's summary, subject terms and funding codes; Methods (colour spaces; the CIEDE2000 formula);
supplementary-file list; acknowledgements, author contributions, data availability, competing interests;
references. Figures are images and are not held; their captions are.
NOTE ON EXTRACTION: reference numbers run into the text as superscripts flattened to digits ("en masse8" is
"en masse" with reference 8).
KEY CONTENT (for C18): "The general estimate is that worldwide 0.5% of women and 8% of men are subject to a
colour-vision deficiency (CVD; e.g., refs. 24,25, and references therein)"; rainbow and red-green colour maps;
perceptual uniformity; greyscale readability; the four checks for an unscientific colour map.
Absence of a passage from this file is not absence from the article.
"""
s += block(1, R, U, "Copyright and licence statement (front matter)",
           M(R, "© The Author(s) 2020https://creativecommons.org/licenses/by/4.0/Open Access",
             "To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/."))
s += block(2, R, U, "Abstract", L(R, 3, 3))
s += omit("Editor's summary, subject terms and funding codes omitted.")
s += block(3, R, U, "Whole article body: Introduction; Boxes 1-2; colour and data distortion; design of colour maps; how to recognise an unscientific colour map; a proactive step forward",
           L(R, 9, 111))
s += omit("Methods (defining colour spaces; the CIEDE2000 colour-difference formula), supplementary information, "
          "acknowledgements, author contributions, data availability, competing interests and references omitted.")
open("sources/crameri_2020_misuse_colour.txt", "w").write(s)

# =============================================================================== Cumming 2007
R = "C2-cumming_2007-pmcxml.txt"
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC2064100.1/PMC2064100.1.xml"
s = """CUMMING, FIDLER AND VAUX 2007, ERROR BARS IN EXPERIMENTAL BIOLOGY - VERBATIM SOURCE PACK
""" + SEP + "\n\n" + RULE + """
WORK: Cumming G, Fidler F, Vaux DL. Error bars in experimental biology. J Cell Biol 2007;177(1):7-11.
PMID 17420288; PMCID PMC2064100; DOI 10.1083/jcb.200611141 (confirmed with the PubMed tools, 2026-10-02).
TEXT FETCHED FROM: the PMC open-access JATS XML, https://pmc-oa-opendata.s3.amazonaws.com/PMC2064100.1/PMC2064100.1.xml
(TinyFish fetch_content, markdown).
LICENCE AS STATED (block 1): "Copyright © 2007, The Rockefeller University Press" and "This article is
distributed under the terms of an Attribution-Noncommercial-Share Alike-No Mirror Sites license for the first
six months after the publication date (see http://www.rupress.org/terms). After six months it is available
under a Creative Commons License (Attribution-Noncommercial-Share Alike 4.0 Unported license, as described at
http://creativecommons.org/licenses/by-nc-sa/4.0/)." So CC BY-NC-SA 4.0 now. (Dashes in this header are
typed as hyphens; the source has en dashes, as in block 1.)

WHAT THIS FILE HOLDS: the licence (block 1); the abstract (block 2); the WHOLE article body, from "What are
error bars for?" to the end of the Conclusion, with Table I (common error bars) as a text table, all eight
Rules, and the Figure 1-7 captions (block 3).
OMITTED: the funding line and references. Figures are images and are not held; their captions are.
EQUATIONS: the SD formula and the SD row of Table I are held as the LaTeX source that the PMC XML carries
(a \\documentclass ... \\begin{document} preamble followed by the formula); this is the XML's own encoding,
transcribed by the extractor, not retyped. SE = SD/√n and the CI formula are in plain text in Table I.
KEY CONTENT (for C19): Rule 1 "when showing error bars, always describe in the figure legends what they are";
Rule 2, n stated in the legend; descriptive (range, SD) against inferential (SE, CI) bars; SE bars doubled
give an approximate 95% CI when n is 10 or more, multiplied by 4 when n = 3.
Absence of a passage from this file is not absence from the article.
"""
s += block(1, R, U, "Copyright and licence statement (front matter)",
           M(R, "Copyright © 2007, The Rockefeller University Press",
             "as described at http://creativecommons.org/licenses/by-nc-sa/4.0/)."))
s += block(2, R, U, "Abstract", L(R, 8, 8))
s += block(3, R, U, "Whole article body: What are error bars for?; Table I; descriptive and inferential bars; Rules 1-8; Conclusion",
           L(R, 14, 144))
s += omit("Funding line and references omitted.")
open("sources/cumming_2007_error_bars.txt", "w").write(s)

# =============================================================================== Bonus: Krishnamurthy 2021 (CVD prevalence, India)
R = "C2-cvd_kanchipuram-pmcxml.txt"
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC8482944.1/PMC8482944.1.xml"
s = """KRISHNAMURTHY, RANGAVITTAL, CHANDRASEKAR AND NARAYANAN 2021, COLOUR VISION DEFICIENCY IN SCHOOL BOYS, SOUTH INDIA
- VERBATIM SOURCE PACK
""" + SEP + "\n\n" + RULE + """
WORK: Krishnamurthy SS, Rangavittal S, Chandrasekar A, Narayanan A. Prevalence of color vision deficiency among
school-going boys in South India. Indian J Ophthalmol 2021;69(8):2021-2025. PMID 34304169; PMCID PMC8482944;
DOI 10.4103/ijo.IJO_3208_20 (confirmed with the PubMed tools, 2026-10-02).
TEXT FETCHED FROM: the PMC open-access JATS XML, https://pmc-oa-opendata.s3.amazonaws.com/PMC8482944.1/PMC8482944.1.xml
(TinyFish fetch_content, markdown).
LICENCE AS STATED (block 1): "Copyright: © 2021 Indian Journal of Ophthalmology" with
https://creativecommons.org/licenses/by-nc-sa/4.0/ and "This is an open access journal, and articles are
distributed under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 License ...".

WHAT THIS FILE HOLDS: the licence (block 1); the structured abstract (block 2); the whole Introduction
(block 3); the whole Methods, including the screening protocol and the definition of a confirmed case
(block 4); the whole Results with Tables 1 and 2 as text tables, the Discussion and the Conclusion (block 5).
OMITTED: keywords and PMC status codes; the funding and conflicts lines; references. Figure 1 (a map) is an
image and is not held; its caption is.
SCOPE OF THE CLAIM: boys only (class grades 6-12, age 11-17), one district (Kanchipuram, Tamil Nadu), screened
with Dalton's plates and confirmed with Ishihara's plates; girls were not tested. It is an Indian prevalence for
boys, not for the whole population.
KEY NUMBERS (for C18): "The overall prevalence of CVD was found to be 2.76% (n = 2073; 95% confidence interval
[CI]: 2.65–2.88)" among 74986 boys screened; the introduction's "The worldwide prevalence of congenital color
vision deficiency (CVD) is reported to be around 8% in men and 0.5% in women."
Absence of a passage from this file is not absence from the article.
"""
s += block(1, R, U, "Copyright and licence statement (front matter)",
           M(R, "Copyright: © 2021 Indian Journal of Ophthalmology", "licensed under the identical terms."))
s += block(2, R, U, "Structured abstract: Purpose (unlabelled in the extraction), Methods, Results, Conclusion", L(R, 3, 15))
s += omit("Keywords and PMC status codes omitted.")
s += block(3, R, U, "Introduction (whole)", L(R, 19, 23))
s += block(4, R, U, "Methods (whole): setting, study procedures, eye examination, CVD screening, definitions, data analysis",
           L(R, 25, 51))
s += block(5, R, U, "Results (whole) with Figure 1 caption and Tables 1-2; Discussion; Conclusion", L(R, 53, 120))
s += omit("Financial support, conflicts of interest and references omitted.")
open("sources/krishnamurthy_2021_cvd_india.txt", "w").write(s)

json.dump(MANIFEST, open("books/S58-R1/intake/manifest-C2.json", "w"), indent=1)
print(len(MANIFEST), "blocks")
