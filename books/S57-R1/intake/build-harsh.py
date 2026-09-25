# Builds / extends three S57-R1 source files from the PDFs Harsh supplied on 2026-09-25:
#   pashler_2008_learning_styles (extended), rozenblit_keil_2002_ioed (extended),
#   kotter_1990_what_leaders_do (new).
# Raw text = `pdftotext <pdf> <txt>` (poppler, default reading-order mode, no -layout), saved in
# intake/raw/ and never edited. Every passage is raw[i:j] between literal anchors (end inclusive,
# unless end_excl). Nothing in a passage is typed by hand. Run from the repository root.
# The gaps between consecutive blocks of one raw file are printed so that every omission can be
# described in a [NOTE].
import json, os, sys

RAW = "books/S57-R1/intake/raw/"
SRC = "sources/"
MANIFEST = []
BAR = "=" * 79


def cut(rawname, start, end, frm=0, end_excl=False):
    raw = open(RAW + rawname, encoding="utf-8").read()
    i = raw.find(start, frm)
    assert i != -1, (rawname, start[:60])
    j = raw.find(end, i + len(start) if not end_excl else i + 1)
    assert j != -1, (rawname, end[:60])
    if not end_excl:
        j += len(end)
    p = raw[i:j].rstrip()
    return i, i + len(p), p


def blocks(rawname, where, specs):
    """specs: list of (heading, start, end, end_excl, note_before). Returns text and spans."""
    out, spans, pos = [], [], 0
    for (n, heading, start, end, excl, note) in specs:
        i, j, p = cut(rawname, start, end, pos, excl)
        spans.append((heading, i, j))
        pos = j
        MANIFEST.append({"raw": rawname, "block": n, "heading": heading, "text": p})
        s = "\n\n" + BAR + "\n" + f"{n}. {heading}\n{where}\n" + BAR + "\n\n"
        if note:
            s += "[NOTE] " + note + "\n\n"
        s += '"' + p + '"\n'
        out.append(s)
    raw = open(RAW + rawname, encoding="utf-8").read()
    for (h1, _, j1), (h2, i2, _) in zip(spans, spans[1:]):
        gap = raw[j1:i2]
        print(f"--- gap {rawname}: after [{h1[:40]}] before [{h2[:40]}]: {len(gap)} chars:",
              repr(" ".join(gap.split())[:160]))
    return out


def old_blocks(path):
    t = open(path, encoding="utf-8").read()
    k = t.find("\n" + BAR + "\n1. ")
    assert k != -1
    e = t.find("\n[...]\n[NOTE] Blocks 4-", k)
    if e == -1:
        e = t.find("\n[NOTE] Blocks 4-", k)
    return (t[k:e] if e != -1 else t[k:]).rstrip() + "\n"


OMIT = "\n\n[...]\n"

# ------------------------------------------------------------------------------ Pashler
PR = "pashler_2008_learning_styles-harsh.txt"
PW = ("PDF supplied by Harsh, text layer by pdftotext (raw: books/S57-R1/intake/raw/" + PR + ")")
pashler = [
    (4, ("Whole article from the title through footnote 1 (Summary, Introduction, overview of doctrines "
         "and industry, why the approach spread, what evidence is necessary: the crossover-interaction "
         "criterion)"),
     "Learning Styles\nConcepts and Evidence", "1H and 1I in the learning-styles literature.", False,
     "Contiguous with blocks 5-8 except where marked [...]. The raw text keeps the PDF's running heads, "
     "page numbers and 'Volume 9—Number 3' footers inside the passage. At the foot of the Introduction's "
     "first page the extraction placed the continuation line 'would provide sufficient evidence ... this "
     "minimal criterion.' before the heading INTRODUCTION; it belongs after '... what kinds of findings' "
     "(end of the Introduction). Left as extracted."),
    (5, "Figure 1, panel heading 'Acceptable Evidence' (text printed inside the figure)",
     "Acceptable Evidence\nIn examples A, B, and C", "the mean test score of the other kind of learner.", False,
     "Omitted before this block: the page number and running head. The nine plotted panels (A-I) of "
     "Figure 1 are drawings; their axis labels ('Test Score', 'Method 1', 'Method 2', 'A Style Learners', "
     "'B Style Learners') come out of the text layer as scattered one-word lines and are omitted between "
     "blocks 5, 6 and 7. Block 7 is the caption, which states the patterns in words."),
    (6, "Figure 1, panel heading 'Unacceptable Evidence' (text printed inside the figure)",
     "Unacceptable Evidence\nIn examples D through I", "thereby precluding the need to customize instruction.", False,
     "Omitted before this block: axis labels of panels A-C."),
    (7, "Figure 1 caption, and the text that follows it to the page break",
     "Fig. 1. Acceptable and unacceptable evidence", "number facility, spatial visualization, associative memory,",
     False, "Omitted before this block: axis labels of panels D-I."),
    (8, ("Figure 2 caption, then the rest of the article body through the Summary (Primary Mental Abilities "
         "continued; Evaluation of learning-styles literature: Sternberg et al. 1999, Massa & Mayer 2006, "
         "Cook et al. 2009, Constantinidou & Baker 2002; related literatures (aptitude-by-treatment "
         "interactions); other approaches; conclusions and recommendations; Summary)"),
     "Fig. 2. Examples of crossover interactions",
     "If classification of students’ learning styles has\npractical utility, it remains to be demonstrated.", False,
     "Omitted before this block: the running head and the axis labels and tick values of Figure 2's two "
     "plotted panels (A: learning style on the x-axis; B: learning method on the x-axis), which the text "
     "layer scatters; the caption states what they show. The body text resumes after the caption with "
     "'perceptual speed, and reasoning.' (the sentence begun at the end of block 7). Footnote 2 sits "
     "inside the passage where the extraction placed it."),
]
pb = blocks(PR, PW, pashler)

P_HEAD = """PASHLER, McDANIEL, ROHRER AND BJORK, LEARNING STYLES: CONCEPTS AND EVIDENCE,
PSYCHOLOGICAL SCIENCE IN THE PUBLIC INTEREST - WHOLE ARTICLE BODY (REFERENCES NOT HELD)
============================================================

Transcription rule for this file: every line beneath a block heading that is not
prefixed with [NOTE] is an exact, unaltered slice of the raw text named in that heading,
cut programmatically (raw[i:j], one contiguous slice per block); nothing has been
paraphrased, smoothed or merged. Blocks 1-2 come from the TinyFish fetch_content result for
the USF record (2026-09-24). Blocks 4-8 come from the text layer of the article PDF,
extracted with pdftotext (poppler, default mode, no -layout; the -layout mode set the two
columns side by side on each line and was not used), 2026-09-25. That raw text is NOT
corrected: ligatures stay as extracted (ﬁ, ﬂ: search for "speciﬁc", not "specific", where
they occur), words hyphenated at a line end are joined without the hyphen as pdftotext
joined them (e.g. "learningstyles", "aptitudeby-treatment"), the PDF's "©" comes out as
"r" ("Copyright r 2009"), "=" can come out as "5" ("N 5 180"), and running heads, page
numbers and footers sit inside passages. Each block's passage is set in double quotation
marks (the marks are this file's). Material left out is marked [...] with a [NOTE]. Lines
beginning [NOTE] are this file's own annotation and are NOT source text. The reference list
is not held.

CITATION: Pashler H, McDaniel M, Rohrer D, Bjork R. Learning styles: concepts and evidence.
Psychol Sci Public Interest 2008;9(3):105-119.
PMID: 26162104   DOI: 10.1111/j.1539-6053.2009.01038.x   (PMID confirmed via PubMed citation
lookup, 2026-09-24; no PMCID)
PRINTED ON THE PDF ITSELF: "Volume 9—Number 3" (every page footer), page numbers 105-119, and
"Copyright r 2009 Association for Psychological Science" (first page; "r" is the © sign). The
PDF prints no issue date; its own copyright year is 2009, and the DOI stem is 2009. The issue is
catalogued (PubMed, the USF record in block 2) as 2008, vol 9 issue 3; the citation above keeps
2008 as the issue year. [NOTE] If a reader sees "Pashler et al. 2009" elsewhere, it is the same
article.
SOURCE: PDF supplied by Harsh, 2026-09-25 (downloaded by him from the publisher; the file name,
"pashler-et-al-2009-learning-styles.pdf", is SAGE Journals' download pattern; PDF title "Learning
Styles", 15 pages). Copied unchanged to books/S57-R1/intake/raw/pashler_2008_learning_styles-
harsh.pdf; its text is raw/""" + PR + """.
Earlier, the abstract (blocks 1-2) was fetched from https://digitalcommons.usf.edu/psy_facpub/1765/
(University of South Florida Digital Commons record; TinyFish fetch_content, markdown), 2026-09-24.
LICENCE: publisher copyright (Association for Psychological Science; the PDF states "Copyright r
2009 Association for Psychological Science" and no licence to reuse). Held for private study and
checking quotations; quote briefly, cite.

WHAT THIS FILE HOLDS: the abstract from the USF record (blocks 1-2, kept from the first intake),
and the WHOLE ARTICLE from the PDF (blocks 4-8): title, authors, Summary, Introduction, the
overview of learning-styles doctrines and industry, why the approach spread, "What evidence is
necessary to validate interventions based on learning styles?" (the style-by-method crossover
interaction as the criterion, with Figure 1's caption and in-figure headings for acceptable
patterns A-C and unacceptable patterns D-I, and Figure 2's caption on crossovers that do not
validate the hypothesis when method is on the horizontal axis), primary mental abilities, the
evaluation of the learning-styles literature (the one arguable study, Sternberg et al. 1999; the
studies with appropriate methods and negative results: Massa & Mayer 2006, Cook et al. 2009,
Constantinidou & Baker 2002), related literatures with appropriate methodologies
(aptitude-by-treatment interactions), conclusions and recommendations, and the Summary.
NOT HELD: the plotted panels of Figures 1 and 2 (drawings; only scattered axis labels are in the
text layer, omitted and marked [...]); the Acknowledgments; the reference list.
"""

p_old = old_blocks(SRC + "pashler_2008_learning_styles.txt")
open(SRC + "pashler_2008_learning_styles.txt", "w", encoding="utf-8").write(
    P_HEAD + "\n" + p_old
    + "\n[...]\n[NOTE] Blocks 4-8 below are from the article PDF. The abstract in block 1 is printed in\n"
      "the PDF as the 'SUMMARY' at the start of block 4.\n"
    + pb[0] + OMIT + pb[1] + OMIT + pb[2] + OMIT + pb[3] + OMIT + pb[4]
    + "\n[...]\n[NOTE] Omitted after block 8: Acknowledgments and the reference list.\n")

# ------------------------------------------------------------------------------ Rozenblit & Keil
RR = "rozenblit_keil_2002_ioed-harsh-nihms268518.txt"
RW = ("PDF supplied by Harsh (PMC author manuscript NIHMS268518), text layer by pdftotext (raw: "
      "books/S57-R1/intake/raw/" + RR + ")")
HDRNOTE = ("The manuscript PDF prints 'NIH-PA Author Manuscript' in its margins, and a footer 'Cogn Sci. "
           "Author manuscript; available in PMC 2011 March 23.' and header 'Rozenblit and Keil / Page n' on "
           "every page; the text layer puts these inside the passage. They are not the article's words.")
roz = [
    (4, "Title, abstract, keywords and 1. Introduction",
     "The misunderstood limits of folk science: an illusion of\nexplanatory depth",
     "2. An illusion of explanatory depth with devices", True,
     HDRNOTE + " The first page's footnotes (copyright line, corresponding author, 'Uncited references') "
     "fall inside this block where the extraction placed them."),
    (5, ("2. An illusion of explanatory depth with devices: Studies 1-6 (methods, results with the "
         "ANOVA statistics, discussions) and the general discussion of Studies 1-6"),
     "2. An illusion of explanatory depth with devices", "3. Calibration of comprehension across knowledge domains",
     True, "Contiguous with blocks 4 and 6. The mean ratings at T1-T5 are plotted in Figures 3-6 (captions in "
     "block 9), not printed as numbers in the text; the text gives the tests of the drop (e.g. Study 1, "
     "F(4, 56) = 16.195, p < .001; Study 2, F(4, 124) = 38.9, p < .001)."),
    (6, "3. Calibration of comprehension across knowledge domains: Studies 7-10 (facts, procedures, "
        "narratives, natural phenomena)",
     "3. Calibration of comprehension across knowledge domains", "4. Exploring the causes behind the illusion",
     True, None),
    (7, "4. Exploring the causes behind the illusion: Studies 11 and 12",
     "4. Exploring the causes behind the illusion", "5. General discussion", True, None),
    (8, "5. General discussion (whole)",
     "5. General discussion", "once some skeletal level of causal comprehension is reached.", False, None),
    (9, "Figure captions, Figs. 1-6",
     "Fig. 1.\n\nThree illustrations", "because Study 4 did not\ninclude T4.)", False,
     "Omitted before this block: 'Supplementary Material' (a pointer to PMC), Acknowledgments, Appendix A "
     "(devices stimuli and instructions), Appendix B (procedures stimuli and instructions) and the "
     "reference list. The figures themselves are images; only their captions are text."),
    (10, "Table 8, Summary of experimental methods and results",
     "Table 8\n\nSummary of experimental methods and results", "Visibility of internal parts predicts\noverconfidence.",
     False,
     "Omitted before this block: Tables 1-7. Their cells come out of the text layer column by column "
     "and out of order (numbers separated from their row and column labels), so they cannot be read "
     "reliably as text; see the PDF. Table 8 also comes out cell by cell, one cell per line, in the "
     "order Study, Participants, Stimuli/procedures, Results for each row, which can be read."),
]
rb = blocks(RR, RW, roz)

R_HEAD = """ROZENBLIT AND KEIL 2002, COGNITIVE SCIENCE - STUDIES 1-12 AND GENERAL DISCUSSION
(NIH AUTHOR MANUSCRIPT; APPENDICES, TABLES 1-7 AND REFERENCES NOT HELD)
============================================================

Transcription rule for this file: every line beneath a block heading that is not
prefixed with [NOTE] is an exact, unaltered slice of the raw text named in that heading,
cut programmatically (raw[i:j], one contiguous slice per block); nothing has been
paraphrased, smoothed or merged. Blocks 1-3 come from the TinyFish fetch_content result for the
NCBI efetch record (2026-09-25, first intake). Blocks 4-10 come from the text layer of the NIH
author-manuscript PDF, extracted with pdftotext (poppler, default mode, no -layout), 2026-09-25.
That raw text is NOT corrected: ligatures and characters stay as extracted, words hyphenated at
a line end are joined without the hyphen as pdftotext joined them (e.g. "selfrated",
"initialratings"), and the manuscript's margin marks, running heads and footers sit inside
passages. Each block's passage is set in double quotation marks (the marks are this file's).
Material left out is marked [...] with a [NOTE]. Lines beginning [NOTE] are this file's own
annotation and are NOT source text. The reference list is not held.

CITATION: Rozenblit L, Keil F. The misunderstood limits of folk science: an illusion of
explanatory depth. Cogn Sci 2002;26(5):521-562.
PMID: 21442007   PMCID: PMC3062901 (NIH author manuscript NIHMS268518)   DOI:
10.1207/s15516709cog2605_1   (confirmed via PubMed ID converter and Europe PMC, 2026-09-24/25;
the PDF prints "Cogn Sci. 2002 September 1; 26(5): 521–562. doi:10.1207/s15516709cog2605_1.")
SOURCE: PDF supplied by Harsh, 2026-09-25 (downloaded by him from PMC; file nihms268518.pdf, the
PMC author-manuscript PDF of PMC3062901, 47 pages). Copied unchanged to books/S57-R1/intake/raw/
rozenblit_keil_2002_ioed-harsh-nihms268518.pdf; its text is raw/""" + RR + """.
Earlier, blocks 1-3 were fetched from
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=3062901 (TinyFish
fetch_content, markdown), 2026-09-25.
LICENCE AS STATED (block 1, and on the PDF's first page): "© 2002 Published by Cognitive Science
Society, Inc." The PMC record flags the item as an author manuscript that is not open access
(blocks 2-3). This is the accepted manuscript ("Published in final edited form as: Cogn Sci ..."),
not the publisher's typeset version; page numbers in it are the manuscript's, not 521-562. Held
for private study and checking quotations; quote briefly, cite.

WHAT THIS FILE HOLDS: the abstract and status flags from the efetch record (blocks 1-3, kept from
the first intake), and from the PDF (blocks 4-10) the whole text from the title through the
General discussion: Introduction; Studies 1-6 on devices (the 7-point scale, the ratings T1
initial, T2 after writing a step-by-step causal explanation, T3 after a diagnostic question, T4
re-rating after an expert explanation, T5 current knowledge; results with their ANOVA statistics;
Study 5's independent ratings; Study 6's explicit warning); Studies 7-10 across domains (facts,
procedures, narratives, natural phenomena); Studies 11-12 (desirability; correlates of confidence
and overconfidence); the General discussion; the captions of Figures 1-6 (Fig. 3: "Self-ratings
of knowledge in both Studies decrease as the result of efforts to explain"); and Table 8, the
summary of all twelve studies.
NOT HELD: the figures (images: the mean self-ratings at each time are plotted, not printed, so
the file holds the tests of the drop, not the plotted means); Tables 1-7 (cells scrambled by the
extraction); Supplementary Material pointer; Acknowledgments; Appendices A and B (stimulus lists
and instructions); the reference list.
[NOTE] fisher_keil_2015_ioed was filed at the first intake as a substitute for the rating drop;
with this file extended it is no longer needed for that claim, and it stays filed.
"""

r_old = old_blocks(SRC + "rozenblit_keil_2002_ioed.txt")
open(SRC + "rozenblit_keil_2002_ioed.txt", "w", encoding="utf-8").write(
    R_HEAD + "\n" + r_old
    + "\n[NOTE] Blocks 4-10 below are from the author-manuscript PDF.\n"
    + rb[0] + rb[1] + rb[2] + rb[3] + rb[4] + OMIT + rb[5] + OMIT + rb[6]
    + "\n[...]\n[NOTE] Omitted between blocks 9 and 10: Tables 1-7 (see block 10's note).\n")

# ------------------------------------------------------------------------------ Kotter
KR = "kotter_1990_what_leaders_do-harsh.txt"
KW = ("PDF supplied by Harsh (HBR reprint R0111F), text layer by pdftotext (raw: books/S57-R1/intake/raw/"
      + KR + ")")
RUN = ("The passage keeps the running footers and heads ('harvard business review • december 2001', "
       "'page n', 'What Leaders Really Do •• •B EST OF HBR') where the extraction put them.")
kot = [
    (1, "Standfirst, title, copyright line, editor's introduction, and the article to '... some of the best'",
     "They don’t make plans", "brilliantly innovative; in fact, some of the best", False,
     RUN + " The author's biographical note ('Now retired, John P. Kotter ...') is a margin box that the "
     "extraction set after the heading 'The Difference Between Management and Leadership'. The sentence "
     "that ends this block continues at the start of block 3; the extraction put the Eastman Kodak box "
     "(block 2) between them."),
    (2, "Box: 'Aligning People: Chuck Trowbridge and Bob Crandall at Eastman Kodak'",
     "Aligning People: Chuck Trowbridge", "more than doubled between 1985 and 1988.", False, RUN),
    (3, "Article continued ('are not. Effective business visions ...' to '... suddenly starts talking about')",
     "are not. Effective business visions", "in an industry suddenly starts talking about", False,
     "Omitted before this block: running footer and head only. The sentence that ends this block "
     "continues in block 6 ('becoming number one, that is a pipe dream, not a vision.')."),
    (4, "Box: 'Setting a Direction: Lou Gerstner at American Express'",
     "Setting a Direction: Lou Gerstner", "also outperformed most low-growth but highproﬁt businesses.", False, RUN),
    (5, "Pull quote (repeats words of the article)",
     "The idea of getting people\nmoving in the same", "not organize people but\nalign them.", False,
     "Omitted before this block: running footer and head only."),
    (6, "Article continued ('becoming number one ...' through 'Aligning People Versus Organizing and Staffing' "
        "to '... the communicator’s repu-')",
     "becoming number one, that is a pipe dream", "the communicator’s repu-", False,
     RUN + " The word 'repu-' continues as 'tation' at the start of block 8."),
    (7, "Pull quote (repeats words of the article)",
     "Management is about\ncoping with complexity.", "is about coping with\nchange.", False,
     "Omitted before this block: running footer and head only."),
    (8, "Article continued ('tation for integrity ...' through 'Motivating People Versus Controlling and "
        "Problem Solving' to '... traditional management roles.')",
     "tation for integrity and trustworthiness", "differ from those coordinating traditional\nmanagement roles.",
     False, RUN),
    (9, "Box: 'Motivating People: Richard Nicolosi at Procter and Gamble'",
     "Motivating People: Richard Nicolosi", "the fact that the competition continued to get tougher.", False,
     "Omitted before this block: running footer and head only. " + RUN),
    (10, "Article continued ('Strong networks of informal relationships ...' through 'Creating a Culture of "
         "Leadership' to '... requires more')",
     "Strong networks of informal relationships—", "But developing people for important leadership positions requires more",
     False, "Omitted before this block: running footer and head only. " + RUN),
    (11, "Pull quote (repeats words of the article)",
     "Well-led businesses tend\nto recognize", "develop leaders.", False,
     "Omitted before this block: running footer and head only."),
    (12, "Article concluded ('work on the part of senior executives ...' to the end, with the reprint number)",
     "work on the part of senior executives", "Reprint R0111F", False, RUN),
]
kb = blocks(KR, KW, kot)

K_HEAD = """KOTTER, WHAT LEADERS REALLY DO, HARVARD BUSINESS REVIEW (1990; BEST OF HBR REPRINT,
DECEMBER 2001) - WHOLE ARTICLE
============================================================

Transcription rule for this file: every line beneath a block heading that is not
prefixed with [NOTE] is an exact, unaltered slice of the raw text named in that heading,
cut programmatically (raw[i:j], one contiguous slice per block); nothing has been
paraphrased, smoothed or merged. The raw text is the text layer of the PDF, extracted with
pdftotext (poppler, default mode, no -layout), 2026-09-25. The -layout mode set the two columns
side by side on each line and was not used; the default mode keeps each column's sentences in
order and puts the boxes (case studies), pull quotes and the author note as separate runs where
they fall on the page. That raw text is NOT corrected: ligatures stay as extracted ("ﬁ", "ﬂ":
search for "signiﬁcant", "ﬁrst", "conﬂict" in this file, not "significant"), words hyphenated
at a line end are joined without the hyphen as pdftotext joined them (e.g. "overcapacity in
capitalintensive", "highproﬁt", "longterm"), and running heads and footers sit inside passages.
Each block's passage is set in double quotation marks (the marks are this file's). Blocks are in
the order the extraction gives them; where a box or pull quote interrupts the article's own
text, the [NOTE] says where the sentence resumes. Lines beginning [NOTE] are this file's own
annotation and are NOT source text.

CITATION: Kotter JP. What leaders really do. Harv Bus Rev 1990;68(3):103-111. Republished as a
"Best of HBR" article, Harv Bus Rev December 2001 (reprint R0111F). The text held is the
2001 reprint, which adds an unsigned editor's introduction (block 1, "The article reprinted here
stands on its own ... ") and the author note "Now retired, John P. Kotter ..."; the PDF itself
states "“What Leaders Really Do,” ﬁrst published in 1990" and prints "harvard business review •
december 2001" and "Reprint R0111F". The 1990 volume, issue and pages are not printed on this PDF
(taken from the S57-R1 READY.md line and not re-verified here); nor are the 2001 reprint's
volume, issue or journal pages. Printed page numbers run 3-11 (PDF pages 1-9).
SOURCE: PDF supplied by Harsh, 2026-09-25 (downloaded by him from the publisher, Harvard Business
Publishing; PDF title "R0111F_pdf.fm", 9 pages). Copied unchanged to books/S57-R1/intake/raw/
kotter_1990_what_leaders_do-harsh.pdf; its text is raw/""" + KR + """.
COPYRIGHT AS PRINTED (PDF p. 1, and inside block 1):
"COPYRIGHT © 2001 HARVARD BUSINESS SCHOOL PUBLISHING CORPORATION. ALL RIGHTS RESERVED."
[NOTE] No licence to reuse is stated. This file is held for private study and for checking
quotations only; it must not be republished or distributed. Reader-facing text should
paraphrase and quote briefly, with citation.

WHAT THIS FILE HOLDS: the whole article as printed in the reprint: standfirst, title, copyright
line, editor's introduction, author note; the article's sections "The Difference Between
Management and Leadership" (management copes with complexity: planning and budgeting, organizing
and staffing, controlling and problem solving; leadership copes with change: setting a direction,
aligning people, motivating and inspiring), "Setting a Direction Versus Planning and Budgeting",
"Aligning People Versus Organizing and Staffing", "Motivating People Versus Controlling and
Problem Solving", "Creating a Culture of Leadership"; the three case boxes (Eastman Kodak,
American Express, Procter & Gamble); the three pull quotes; the reprint number.
NOT HELD: the HBR ordering/reprint page that the last page points to ("To order, see the next
page ..."), which is not in the PDF; the ordering lines after "Reprint R0111F" are omitted.
The article has no reference list.
"""

open(SRC + "kotter_1990_what_leaders_do.txt", "w", encoding="utf-8").write(
    K_HEAD + "".join(kb)
    + "\n[...]\n[NOTE] Omitted after block 12: the ordering lines ('To order, see the next page / or call "
      "... / or go to www.hbr.org') and the page number.\n")

json.dump(MANIFEST, open("books/S57-R1/intake/manifest-harsh.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("blocks cut:", len(MANIFEST))
