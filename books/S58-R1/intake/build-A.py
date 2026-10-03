# Builds the group-A source files for S58-R1 (scientific writing) from the saved raw fetches.
# Every passage is raw[i:j], located by unique start/end anchors or by line numbers of the raw file.
# Nothing in a passage is typed by hand. Run from the repository root: python books/S58-R1/intake/build-A.py
import json

RAW = "books/S58-R1/intake/raw/"
MANIFEST = []
SEP = "=" * 100


def load(rawname):
    return open(RAW + rawname, encoding="utf-8").read()


def cut(rawname, start, end, end_inclusive=True):
    raw = load(rawname)
    i = raw.find(start)
    assert i != -1, (rawname, start[:60])
    assert raw.find(start, i + 1) == -1, ("start anchor not unique", rawname, start[:60])
    j = raw.find(end, i + len(start) if end_inclusive else i)
    assert j != -1, (rawname, end[:60])
    if end_inclusive:
        j += len(end)
    return raw[i:j].rstrip()


def cutlines(rawname, a, b):
    """Lines a..b inclusive (1-based) of the raw file, as one contiguous slice raw[i:j]."""
    raw = load(rawname)
    starts = [0]
    for k, ch in enumerate(raw):
        if ch == "\n":
            starts.append(k + 1)
    i = starts[a - 1]
    j = starts[b] - 1 if b < len(starts) else len(raw)
    return raw[i:j].rstrip()


def block(rawname, url, heading, text, note=None):
    MANIFEST.append({"raw": rawname, "url": url, "heading": heading, "text": text})
    out = "\n" + SEP + "\n" + heading + "\nFETCHED: " + url + "\n" + SEP + "\n\n"
    if note:
        out += "[NOTE] " + note + "\n\n"
    return out + "[TEXT]\n" + text + "\n[END TEXT]\n"


def omit(note):
    return "\n[...]\n[NOTE] " + note + "\n"


RULE = ("Transcription rule for this file: every line between a [TEXT] line and its [END TEXT] line is an\n"
        "exact, unaltered slice of the text returned by the TinyFish fetch_content tool for the URL in that\n"
        "block's FETCHED line, cut by script (raw[i:j]) from the saved fetch; nothing has been paraphrased,\n"
        "re-wrapped or merged. [...] marks an omission; lines beginning [NOTE], and everything outside\n"
        "[TEXT] ... [END TEXT], are this file's own annotation and are NOT source text. Fetched 2026-10-02\n"
        "(the sandbox clock read 2026-10-01 UTC).\n")

FILES = {}

# ------------------------------------------------------------------ 1. ICMJE, IV.A Preparing a Manuscript
U = "https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html"
R = "A-icmje-preparing.txt"
UH = "https://www.icmje.org/recommendations/"
RH = "A-icmje-recommendations-home.txt"
UIV = "https://www.icmje.org/recommendations/browse/manuscript-preparation/"
RIV = "A-icmje-section-iv.txt"
UF = "https://www.icmje.org/about-icmje/faqs/icmje-recommendations/"
RF = "A-icmje-faq.txt"
s = """ICMJE RECOMMENDATIONS (UPDATED JANUARY 2026) - SECTION IV.A, PREPARING A MANUSCRIPT FOR SUBMISSION
TO A MEDICAL JOURNAL: IV.A.1 GENERAL PRINCIPLES AND IV.A.3.a-k MANUSCRIPT SECTIONS (EXCERPTS)
====================================================================================================

""" + RULE + """
WORK: International Committee of Medical Journal Editors. Recommendations for the Conduct, Reporting,
Editing, and Publication of Scholarly Work in Medical Journals. Updated January 2026 (block 1, the
Recommendations home page). Section IV (block 2, "IV. Manuscript Preparation and Submission"), part A,
"Preparing a Manuscript for Submission to a Medical Journal".
[NOTE] SECTION NUMBER: READY.md and the intake prompt call this "II.A". The ICMJE site numbers it
IV.A: the parent page is headed "IV. Manuscript Preparation and Submission" (block 2), and the page
itself cross-refers to "section II.E" (protection of participants) and "Section III.D.3", which are
other parts. Cite it as IV.A.1 and IV.A.3.a-k.
URL FETCHED: the web version of IV.A (block 3), its parent page, the Recommendations home page and the
ICMJE FAQ on the Recommendations (TinyFish fetch_content, markdown). The downloadable PDF
(https://www.icmje.org/icmje-recommendations.pdf) was NOT fetched; the web pages are the official
version per the FAQ ("The official and most current document is freely available to the public at on
the ICMJE web site").
LICENCE / REUSE AS STATED (block 5, the ICMJE FAQ): "Other organizations should not reprint in their
own publications or post the ICMJE recommendations on their own websites, but are welcome to post a
link to the freely available, periodically updated official version on www.ICMJE.org." No open
licence; no copyright line appears in the extracted page text. READY.md's "free to reproduce for
non-commercial education (to confirm)" is NOT confirmed: the FAQ asks others not to reprint or
post. This file is held for private study so that quotations can be checked; quote briefly in the
book and link to icmje.org; do not reproduce sections.
HOW TO CITE (block 6, the FAQ's own form): "International Committee of Medical Journal Editors
[homepage on the Internet]. Recommendations for the Conduct, Reporting, Editing and Publication of
Scholarly Work in Medical Journals [insert month/day/year you accessed site] Available from:
http://www.ICMJE.org."

WHAT THIS FILE HOLDS: the version line (block 1); the Section IV heading (block 2); IV.A heading and
IV.A.1 General Principles, whole (block 3); IV.A.3 Manuscript Sections from its heading through
3.a Title Page, 3.b Abstract, 3.c Introduction, 3.d Methods (with i-iii), 3.e Results, 3.f Discussion,
3.g References, 3.h Tables, 3.i Illustrations (Figures), 3.j Units of Measurement and 3.k Abbreviations
and Symbols, whole, to the end of the page (block 4); the FAQ paragraphs on reprinting and translating (block 5) and on how
to cite (block 6).
OMITTED: IV.A.2 Reporting Guidelines (routed to S56 by the inventory) and the page's "Page Contents"
line is inside block 3 as extracted; IV.A.4 onward and IV.B (Sending the Submission) are on other
pages and were not fetched; Sections I-III and V are not held. In 3.a the extraction runs the
run-in heads (Article title, Author information, Disclaimers ...) into one paragraph, as held.
Absence of a passage from this file is not absence from the Recommendations.
"""
s += block(RH, UH, "BLOCK 1 - Recommendations home page: version line",
           cut(RH, "# Recommendations", "Updated January 2026"))
s += block(RIV, UIV, "BLOCK 2 - Section IV heading (parent page)",
           cut(RIV, "# IV. Manuscript", "Preparation and Submission"))
s += block(R, U, "BLOCK 3 - IV.A heading; IV.A.1 General Principles",
           cut(R, "# A. Preparing a Manuscript for Submission to a Medical Journal",
               "simultaneously with the primary manuscript."))
s += omit("IV.A.2 Reporting Guidelines omitted (one paragraph; CONSORT, STROBE, PRISMA, STARD, SAGER, EQUATOR).")
s += block(R, U, "BLOCK 4 - IV.A.3 Manuscript Sections, a (Title Page) to k (Abbreviations and Symbols), to end of page",
           cut(R, "## 3. Manuscript Sections", "unless the abbreviation is a standard unit of measurement."))
s += omit("Rest of the FAQ page (where to find the URMs, print copies, member journals) omitted except the passages below.")
s += block(RF, UF, "BLOCK 5 - ICMJE FAQ: reprinting and translating the Recommendations",
           cut(RF, "## Can I translate/reprint the Recommendations",
               "Users should cite this official version when citing the document.”"))
s += omit("FAQ paragraphs on notifying ICMJE of translations and on republication of editorials omitted.")
s += block(RF, UF, "BLOCK 6 - ICMJE FAQ: how to cite",
           cut(RF, "## How do I cite the Recommendations", "Available from: http://www.ICMJE.org."))
FILES["icmje_2026_manuscript_preparation.txt"] = s

# ------------------------------------------------------------------ 2. Sollaci & Pereira 2004
U = "https://pmc.ncbi.nlm.nih.gov/articles/PMC442179/"
R = "A-sollaci_pereira-pmcpage.txt"
s = """SOLLACI AND PEREIRA 2004, J MED LIBR ASSOC - THE IMRAD STRUCTURE: A FIFTY-YEAR SURVEY
(WHOLE ARTICLE TEXT EXCEPT REFERENCES; FIGURES ARE IMAGES)
====================================================================================================

""" + RULE + """
CITATION: Sollaci LB, Pereira MG. The introduction, methods, results, and discussion (IMRAD)
structure: a fifty-year survey. J Med Libr Assoc 2004;92(3):364-367. PMID 15243643, PMCID PMC442179
(confirmed with the PubMed tools, 2026-10-02). No DOI is registered in PubMed.
[NOTE] PAGES: PubMed gives "364-7"; the PMC page header (block 1) reads "364–371". The citation above
follows PubMed and READY.md; the difference is noted, not resolved.
TEXT FETCHED FROM: the PMC article page (TinyFish fetch_content, markdown), 2026-10-02. The article is
not in the PMC open-access S3 bucket (https://pmc-oa-opendata.s3.amazonaws.com/PMC442179.1/PMC442179.1.xml
returned 404), so it is not in the open-access subset.
LICENCE AS STATED (block 1): "Copyright © 2004, Medical Library Association" with a link "PMC
Copyright notice". No open licence. Free to read in PMC. Quote briefly and cite.

WHAT THIS FILE HOLDS: block 1, the PMC front matter (issue line, title, authors, affiliations,
received/accepted dates, copyright line, PMCID/PMID); block 2, the whole article from the structured
abstract through Methods, Results (with the captions of Figures 1 and 2) and Discussion.
OMITTED: contributor e-mail lines and the reference list. Figures 1 and 2 are images: only their
captions are held, so the year-by-year percentages plotted in them are NOT held; the numbers held are
those stated in the text (none in 1935; over 10% in all journals by 1950; over 80% in the 1970s;
from none to 20% 1935-1955; more than quadrupled 1955-1975; n = 1,297; kappa 0.95).
"""
s += block(R, U, "BLOCK 1 - PMC front matter",
           cut(R, ". 2004 Jul;92(3):364–371.", "PMID: 15243643"))
s += block(R, U, "BLOCK 2 - Abstract, introduction, Methods, Results, Discussion",
           cut(R, "## Abstract", "caution should be taken in extrapolating these findings to other journals."))
s += omit("Contributor information and the 15 references omitted.")
FILES["sollaci_pereira_2004_imrad.txt"] = s

# ------------------------------------------------------------------ 3. Mensh & Kording 2017
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC5619685.1/PMC5619685.1.xml"
R = "A-mensh_kording-pmcxml.txt"
UC = "https://pmc-oa-opendata.s3.amazonaws.com/PMC5679512.1/PMC5679512.1.xml"
RC = "A-mensh_kording-correction-pmcxml.txt"
s = """MENSH AND KORDING 2017, PLOS COMPUTATIONAL BIOLOGY - TEN SIMPLE RULES FOR STRUCTURING PAPERS
(WHOLE TEXT EXCEPT ACKNOWLEDGEMENT NAMES AND REFERENCES)
====================================================================================================

""" + RULE + """
CITATION: Mensh B, Kording K. Ten simple rules for structuring papers. PLoS Comput Biol
2017;13(9):e1005619. PMID 28957311, PMCID PMC5619685, DOI 10.1371/journal.pcbi.1005619 (confirmed with
the PubMed ID converter, 2026-10-02). Editorial ("Ten simple rules" series).
CORRECTION: PLOS Computational Biology Staff. Correction: Ten simple rules for structuring papers.
PLoS Comput Biol 2017;13(11):e1005830, PMC5679512 (block 3): Fig 1's key was missing; the
corrected figure is an image and is not held. The correction changes nothing in the text.
TEXT FETCHED FROM: the PMC open-access JATS XML (TinyFish fetch_content, markdown). The extraction
strips the XML tags, so the front matter runs together (block 1) and section and rule headings are
run onto the text in places (e.g. "parallelismAvoiding zig-zag"); text is otherwise as published.
LICENCE AS STATED (block 1): "© 2017 Mensh, Kording" ... "This is an open access article distributed
under the terms of the Creative Commons Attribution License, which permits unrestricted use,
distribution, and reproduction in any medium, provided the original author and source are credited."
(link https://creativecommons.org/licenses/by/4.0/; CC BY 4.0).

WHAT THIS FILE HOLDS: block 1, the copyright and licence statement (with the run-together XML front
matter around it cut away); block 2, the whole article text from the Overview through the
Introduction, Principles (Rules 1-4), The components of a paper (Rules 5-8, with the Fig 1 caption),
Process (Rules 9-10, with Table 1 in full: the ten rules and the sign each is violated) and the
Discussion to "...more effectively enable integrative science."; block 3, the correction notice.
OMITTED: the names in the acknowledgement paragraph and the 18 references. Fig 1 (an image) is not
held, only its caption.
"""
s += block(R, U, "BLOCK 1 - Copyright and licence statement (XML front matter)",
           cut(R, "© 2017 Mensh, Kording", "provided the original author and source are credited."))
s += block(R, U, "BLOCK 2 - Overview, Introduction, Rules 1-10 with Table 1, Discussion",
           cut(R, "Overview\n\nGood scientific writing is essential",
               "more effectively enable integrative science."))
s += omit("Acknowledgement paragraph and list of names, and the references, omitted.")
s += block(RC, UC, "BLOCK 3 - Correction notice (e1005830)",
           cut(RC, "Fig 1 is incorrect–the key is absent.", "The authors have provided a corrected version here."))
FILES["mensh_kording_2017_structuring_papers.txt"] = s

# ------------------------------------------------------------------ 4. OpenStax Writing Guide with Handbook
UD = "https://openstax.org/details/books/writing-guide"
RD = "A-openstax_writing-details.txt"
UHB = "https://openstax.org/books/writing-guide/pages/handbook"
RHB = "A-openstax_writing-handbook.txt"
U66 = "https://openstax.org/books/writing-guide/pages/6-6-editing-focus-subject-verb-agreement"
R66 = "A-openstax_writing-6-6.txt"
U36 = "https://openstax.org/books/writing-guide/pages/3-6-editing-focus-sentence-structure"
R36 = "A-openstax_writing-3-6.txt"
s = """OPENSTAX, WRITING GUIDE WITH HANDBOOK (2021) - HANDBOOK H2 (EFFECTIVE PARAGRAPHS), H3 (CLEAR AND
EFFECTIVE SENTENCES), H7 (VERB DEFINITION); SECTIONS 6.6 (SUBJECT AND PREDICATE) AND 3.6 (DOERS AND
ACTIONS; WORDINESS) (EXCERPTS)
====================================================================================================

""" + RULE + """
WORK: Robinson MB, Jerskey M, featuring Fulwiler T (senior contributing authors). Writing Guide with
Handbook. Houston, Texas: OpenStax, Rice University; 2021. Publish date Dec 21, 2021; web version
last updated Apr 23, 2026; digital PDF ISBN 978-1-951693-47-3 (block 1, the book's details page).
LICENCE AS STATED (block 1, details page): "by OpenStax is licensed under Creative Commons
Attribution-NonCommercial-ShareAlike License v4.0" (CC BY-NC-SA 4.0).
SECTIONS IDENTIFIED AT INTAKE (READY.md left them to be identified): the Handbook is one web page
(https://openstax.org/books/writing-guide/pages/handbook) with parts H1-H13. Paragraph structure
(topic sentence, development) is H2 "Paragraphs and Transitions" > "Effective Paragraphs" >
"Developing a Main Point" and "Supporting Evidence and Analysis". Sentence structure is H3 "Clear and
Effective Sentences": Emphasis, Concrete Nouns, Active Voice, Conciseness, Parallelism, Variety (whose
Simple/Compound/Complex/Compound-Complex Sentences subsections define main and subordinate clauses).
The Handbook has no definition of "subject" by itself; H7 opens with the definition of a verb, and the
chapter section it points to, 6.6 "Editing Focus: Subject-Verb Agreement", defines subject and
predicate (block 5). Section 3.6 "Editing Focus: Sentence Structure", which H3 cross-refers to, gives
the "doer" and "action" pattern and the wordiness example (block 6).
FORMATTING IN THE EXTRACTION: the web page marks examples with underlining, which the extraction
renders as literal words: "underline...end underline" (single underline: in H2 the topic sentence;
in H3 subjects or the changed words; in 6.6 subjects) and "double underline...end double underline"
(in H3 and 6.6 the verb or main clause). These words are the extraction's, not the book's text.

WHAT THIS FILE HOLDS: block 1, details page (dates, ISBNs, licence); block 2, H2 introduction and
"Effective Paragraphs" through "Supporting Evidence and Analysis" with its example paragraph; block 3,
H3 whole (Emphasis to Compound-Complex Sentences); block 4, H7's opening definition of a verb; block 5,
6.6's opening paragraphs (subject, predicate, agreement); block 6, 3.6 "Revising Common Sentence
Patterns for More Effective Communication", whole.
OMITTED: H1, H2 Opening/Closing Paragraphs and Transitions, H4-H6, the rest of H7, H8-H13; the rest of
6.6 (agreement cases and practice set) and of 3.6 (learning outcomes, sentence combining, the editing
exercise). Absence of a passage from this file is not absence from the book.
"""
s += block(RD, UD, "BLOCK 1 - Book details page: dates, ISBNs, licence",
           cut(RD, "#### Publish Date:", "Attribution-NonCommercial-ShareAlike License v4.0"))
s += omit("Handbook H1 Introduction omitted.")
s += block(RHB, UHB, "BLOCK 2 - Handbook H2 Paragraphs and Transitions: introduction; Effective Paragraphs; Developing a Main Point; Supporting Evidence and Analysis",
           cut(RHB, "## H 2 . Paragraphs and Transitions", "#### Opening Paragraphs", end_inclusive=False))
s += omit("H2 Opening Paragraphs, Closing Paragraphs and Transitions omitted.")
s += block(RHB, UHB, "BLOCK 3 - Handbook H3 Clear and Effective Sentences, whole",
           cut(RHB, "## H 3 . Clear and Effective Sentences", "## H 4 . Sentence Errors", end_inclusive=False))
s += omit("H4 Sentence Errors, H5 Words and Language, H6 Point of View omitted.")
s += block(RHB, UHB, "BLOCK 4 - Handbook H7 Verbs: opening definition",
           cut(RHB, "## H 7 . Verbs", "### Subject-Verb Agreement", end_inclusive=False))
s += omit("Rest of H7 and H8-H13 omitted.")
s += block(R66, U66, "BLOCK 5 - Section 6.6 Editing Focus: Subject-Verb Agreement, opening (subject and predicate defined)",
           cut(R66, "## 6.6 Editing Focus: Subject-Verb Agreement", "Subject-verb agreement gets tricky in several", end_inclusive=False))
s += omit("Rest of 6.6 (the agreement questions and the practice set) omitted.")
s += block(R36, U36, "BLOCK 6 - Section 3.6 Editing Focus: Sentence Structure, Revising Common Sentence Patterns for More Effective Communication",
           cut(R36, "### Revising Common Sentence Patterns for More Effective Communication",
               "### Editing for More Effective Sentences", end_inclusive=False))
s += omit("3.6's learning outcomes, Sentence Combining and the Editing for More Effective Sentences exercise omitted.")
FILES["openstax_writing_guide_handbook.txt"] = s

# ------------------------------------------------------------------ 5. Gopen & Swan 1990
U = "https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf"
R = "A-gopen_swan-usenixpdf.txt"
s = """GOPEN AND SWAN 1990, AMERICAN SCIENTIST - THE SCIENCE OF SCIENTIFIC WRITING
(WHOLE ARTICLE TEXT, FROM A REPRINT'S PDF TEXT LAYER; BIBLIOGRAPHY OMITTED)
====================================================================================================

""" + RULE + """
CITATION: Gopen GD, Swan JA. The science of scientific writing. American Scientist 1990;78(6):550-558.
(Volume, issue and pages as in READY.md and as cited by Mensh and Kording 2017, ref. 17; the reprint
held here carries no volume or page numbers.)
TEXT FETCHED FROM: https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf
(a third-party host), its text layer via TinyFish fetch_content; the fetch reported a final URL on a
Cloudflare IP for usenix.org and the PDF title "Microsoft Word - Science of Writing.rtf". The JSTOR
copy was NOT fetched (JSTOR's terms forbid automated download).
WHAT THE REPRINT SAYS OF ITSELF (block 1): "This article, downloaded from
https://www.e-education.psu.edu/styleforstudents/c10_p1.html (Style for Students Online), originally
appeared in American Scientist, journal of Sigma Xi, copyright © 1990 by Sigma Xi, The Scientific
Research Society. Reprinted with the permission of American Scientist." So this is a retyped reprint
(via Penn State's Style for Students Online), not the typeset article: the typeset article's
example boxes, figures and layout are not reproduced, and page numbers are absent.
LICENCE: copyright 1990 Sigma Xi; no open licence. Held for private study so that quotations can be
checked; quote briefly and cite the American Scientist article.
LAYOUT: the text layer keeps the PDF's line breaks (lines end with a space and newline) and some
words are hyphenated across lines. The example passages are set as plain paragraphs.

WHAT THIS FILE HOLDS: block 1, the whole article from the title line through the last paragraph of
"Writing and the Scientific Process" ("...Improving either one will improve the other."): the
sections Reader Expectations for the Structure of Prose, Subject-Verb Separation, The Stress Position,
The Topic Position, Perceiving Logical Gaps, Locating the Action, Writing and the Scientific Process.
OMITTED: the Bibliography (four items) only.
"""
s += block(R, U, "BLOCK 1 - Whole article text (title line to end of Writing and the Scientific Process)",
           cut(R, "The Science of Scientific Writing \nby George D. Gopen and Judith A. Swan",
               "Improving either one will improve the other."))
s += omit("Bibliography omitted.")
FILES["gopen_swan_1990_scientific_writing.txt"] = s

# ------------------------------------------------------------------ 6. Federal Plain Language Guidelines 2011
U = "https://wid.org/wp-content/uploads/2022/03/FederalPLGuidelines.pdf"
R = "A-plain_language_2011-widpdf.txt"
UG = "https://www.plainlanguage.gov/guidelines/"
RG = "A-plain_language-digitalgov.txt"
s = """FEDERAL PLAIN LANGUAGE GUIDELINES, MARCH 2011, REVISION 1, MAY 2011 (PLAIN) - SECTIONS ON ACTIVE
VOICE, HIDDEN VERBS, NOUNS FROM VERBS, ABBREVIATIONS, SHORT SIMPLE WORDS, OMITTING UNNECESSARY WORDS,
CONSISTENT TERMS, SHORT SENTENCES, SUBJECT-VERB-OBJECT, TOPIC SENTENCES, ONE TOPIC PER PARAGRAPH
(EXCERPTS)
====================================================================================================

""" + RULE + """
WORK: Plain Language Action and Information Network (PLAIN). Federal Plain Language Guidelines. March
2011, Revision 1, May 2011 (block 1, the title page and introduction). Page numbers below are the
document's own, from its running footer.
TEXT FETCHED FROM: a copy of the 2011 PDF hosted by the World Institute on Disability,
https://wid.org/wp-content/uploads/2022/03/FederalPLGuidelines.pdf (its text layer via TinyFish
fetch_content). The government's own copy is gone: https://www.plainlanguage.gov/media/FederalPLGuidelines.pdf
was unreachable, a GitHub raw path for it was unreachable, and https://www.plainlanguage.gov/guidelines/
now redirects to https://digital.gov/guides/plain-language, which says the PlainLanguage.gov content is
archived in the GSA GitHub repository (block 11). The WID copy's title page, revision line and
"Revision 1 Changes" page match the 2011 Rev. 1 document cited elsewhere; it is a third-party copy.
LICENCE: the PDF carries no copyright or licence statement. PLAIN describes itself as "a community of
federal employees" (block 1); a work of U.S. federal employees in their official duties is not
subject to U.S. copyright (17 U.S.C. 105) - that conclusion is this file's, not a statement in the
document.
LAYOUT: the text layer keeps line breaks; the two-column "Don't say / Say" and "Passive / Active"
tables are flattened, so the two columns' cells run one after another, line by line; bullets are
shown as a private-use glyph. Each block runs from a section heading to the end of that section's
"Sources" list, and keeps the running footer ("Federal Plain Language Guidelines, March 2011, Rev. 1,
May 2011  <page>") wherever a section crosses a page.

WHAT THIS FILE HOLDS: block 1, title page, introduction and "Revision 1 Changes"; blocks 2-10, these sections whole, each
with its Sources list: III.a.1.i Use active voice (pp. 20-21); III.a.1.iii Avoid hidden verbs
(pp. 23-24); III.a.2.i Don't turn verbs into nouns (p. 29); III.a.2.iii Minimize abbreviations
(pp. 33-34); III.a.3.i Use short, simple words and III.a.3.ii Omit unnecessary words (pp. 36-40);
III.a.3.iv Use the same term consistently for a specific thought or object (p. 45); III.b.1 Write
short sentences and III.b.2 Keep subject, verb, and object close together (pp. 50-53); III.c.1 Have
a topic sentence (p. 63); III.c.4 Cover only one topic in each paragraph (p. 68); block 11, the
digital.gov page the old URL now redirects to.
OMITTED: the table of contents, sections I-II, all other parts of III, and IV-V. The prompt's four
sections (active voice, short words, omit unnecessary words, short sentences) are blocks 2, 6 and 8;
the others are held because inventory concepts C06, C07, C09 and C11 name them (hidden verbs and nouns
from verbs; subject close to verb; abbreviations; one term for one thing; topic sentence; one topic).
"""
s += block(R, U, "BLOCK 1 - Title page, Introduction and Revision 1 Changes (pp. cover, i, ii)", cutlines(R, 1, 41))
s += omit("Table of contents, sections I, II and III.a introduction omitted.")
s += block(R, U, "BLOCK 2 - III.a.1.i Use active voice (pp. 20-21)", cutlines(R, 625, 693))
s += omit("III.a.1.ii Use the simplest form of a verb omitted.")
s += block(R, U, "BLOCK 3 - III.a.1.iii Avoid hidden verbs (pp. 23-24)", cutlines(R, 735, 789))
s += omit("III.a.1.iv-v and III.a.2 introduction omitted.")
s += block(R, U, "BLOCK 4 - III.a.2.i Don't turn verbs into nouns (p. 29)", cutlines(R, 912, 948))
s += omit("III.a.2.ii Use pronouns to speak directly to readers omitted.")
s += block(R, U, "BLOCK 5 - III.a.2.iii Minimize abbreviations (pp. 33-34)", cutlines(R, 1045, 1097))
s += omit("III.a.3 introduction omitted.")
s += block(R, U, "BLOCK 6 - III.a.3.i Use short, simple words; III.a.3.ii Omit unnecessary words (pp. 36-40)", cutlines(R, 1110, 1258))
s += omit("III.a.3.iii Dealing with definitions omitted.")
s += block(R, U, "BLOCK 7 - III.a.3.iv Use the same term consistently for a specific thought or object (p. 45)", cutlines(R, 1380, 1392))
s += omit("III.a.3.v-vi and III.b introduction omitted.")
s += block(R, U, "BLOCK 8 - III.b.1 Write short sentences; III.b.2 Keep subject, verb, and object close together (pp. 50-53)", cutlines(R, 1499, 1623))
s += omit("III.b.3-5 and III.c introduction omitted.")
s += block(R, U, "BLOCK 9 - III.c.1 Have a topic sentence (p. 63)", cutlines(R, 1924, 1945))
s += omit("III.c.2-3 omitted.")
s += block(R, U, "BLOCK 10 - III.c.4 Cover only one topic in each paragraph (p. 68)", cutlines(R, 2115, 2148))
s += omit("III.d onward, IV and V omitted.")
s += block(RG, UG, "BLOCK 11 - The page the old plainlanguage.gov/guidelines URL now redirects to (digital.gov, 2025)",
           cut(RG, "This content is adapted from PlainLanguage.gov", "Guidelines section of the repository."),
           note="Held to document where the original site went; not a source for any claim.")
FILES["plain_language_2011_guidelines.txt"] = s

# ------------------------------------------------------------------ 7. Barnett & Doubleday 2020
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC7556863.1/PMC7556863.1.xml"
R = "A-barnett_doubleday-pmcxml.txt"
s = """BARNETT AND DOUBLEDAY 2020, ELIFE - THE GROWTH OF ACRONYMS IN THE SCIENTIFIC LITERATURE
(WHOLE TEXT EXCEPT FUNDING, ACKNOWLEDGEMENTS, REFERENCES AND APPENDIX 1)
====================================================================================================

""" + RULE + """
CITATION: Barnett A, Doubleday Z. The growth of acronyms in the scientific literature. eLife
2020;9:e60080. PMID 32701448, PMCID PMC7556863, DOI 10.7554/eLife.60080 (confirmed with the PubMed ID
converter, 2026-10-02). Feature Article, Meta-Research.
TEXT FETCHED FROM: the PMC open-access JATS XML (TinyFish fetch_content, markdown). The extraction
strips XML tags, so front matter runs together (block 1), and figure and table captions run onto
their labels ("Figure 1.Mean proportions ...").
LICENCE AS STATED (block 1): "© 2020, Barnett and Doubleday" ... "This article is distributed under
the terms of the Creative Commons Attribution License, which permits unrestricted use and
redistribution provided that the original author and source are credited." (link
https://creativecommons.org/licenses/by/4.0/; CC BY 4.0).

WHAT THIS FILE HOLDS: block 1, copyright and licence; block 2, the abstract; block 3, the author
impact statement; block 4, the whole body: Introduction with Box 1, Results (24,873,372 titles and
18,249,091 abstracts; 1,112,345 unique acronyms; acronyms per 100 words in titles 0.7 in 1950 to 2.4
in 2019 and in abstracts 0.4 in 1956 to 4.1 in 2019; at least one acronym in 19% of titles and 73% of
abstracts; 30% used once, 49% two to ten times, 0.2% over 10,000 times; 11% re-used within a year;
title length 9.0 to 14.6 words, abstract length 128 to 220 words), Table 1 (top 20 acronyms with
counts), figure captions, Discussion, Materials and methods with Tables 2 and 3, Statistical analysis,
Data and code availability, and Limitations.
OMITTED: keywords and funding metadata, the funding, acknowledgement, author and competing-interest
notes, the data-availability repeat, the references and Appendix 1 (text-processing algorithm).
Figures 1-3 and the videos are not held; only their captions.
"""
s += block(R, U, "BLOCK 1 - Copyright and licence statement (XML front matter)",
           cut(R, "© 2020, Barnett and Doubleday", "provided that the original author and source are credited."))
s += block(R, U, "BLOCK 2 - Abstract",
           cut(R, "Some acronyms are useful and are widely understood",
               "potentially increase the value of science."))
s += omit("Keywords and funding metadata omitted.")
s += block(R, U, "BLOCK 3 - Author impact statement",
           cut(R, "A study of 24 million articles has revealed", "most of which have been used fewer than 10 times."))
s += block(R, U, "BLOCK 4 - Introduction, Results, Table 1, Discussion, Materials and methods (with Tables 2 and 3), Limitations",
           cut(R, "As the number of scientific papers published every year continues to grow",
               "hence other trends and patterns could be examined."))
s += omit("Funding, acknowledgements, author notes, references and Appendix 1 omitted.")
FILES["barnett_doubleday_2020_acronyms.txt"] = s

# ------------------------------------------------------------------ write
for name, text in FILES.items():
    open("sources/" + name, "w", encoding="utf-8").write(text)
json.dump(MANIFEST, open("books/S58-R1/intake/manifest-A.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for name, text in FILES.items():
    print(name, len(text.split()), "words")
print(len(MANIFEST), "passages")
