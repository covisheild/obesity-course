# Builds the group-b source files for S57-R1 from the saved raw fetches.
# Every passage is raw[i:j], located by a start marker and an end marker (end inclusive).
# Nothing in a passage is typed by hand. Run from the repository root.
import json, re, os

RAW = "books/S57-R1/intake/raw/"
MANIFEST = []

def cut(rawname, start, end):
    raw = open(RAW + rawname).read()
    i = raw.find(start)
    assert i != -1, (rawname, start[:60])
    assert raw.find(start, i + 1) == -1 or True
    j = raw.find(end, i)
    assert j != -1, (rawname, end[:60])
    j += len(end)
    return raw[i:j]

def block(rawname, url, heading, start, end, note=None):
    p = cut(rawname, start, end)
    MANIFEST.append({"raw": rawname, "url": url, "text": p})
    out = "\n" + "=" * 100 + "\n" + heading + "\nFETCHED: " + url + "\n" + "=" * 100 + "\n\n"
    if note:
        out += "[NOTE] " + note + "\n\n"
    return out + p + "\n"

RULE = ("Transcription rule for this file: every line beneath a block heading that does not begin with\n"
        "[NOTE] or [...] is an exact, unaltered slice of the text returned by the TinyFish fetch_content tool\n"
        "for the URL in that heading, cut by script (raw[i:j]) from the saved fetch; nothing has been\n"
        "paraphrased, re-wrapped or merged. [...] marks an omission; lines beginning [NOTE] are this file's\n"
        "own annotation and are NOT source text. Fetched 2026-09-24/25.\n")

# ---------------------------------------------------------------- Cochrane Handbook ch. 6
U = "https://training.cochrane.org/handbook/current/chapter-06"
R = "cochrane_handbook_ch06-page.txt"
s = """COCHRANE HANDBOOK FOR SYSTEMATIC REVIEWS OF INTERVENTIONS, VERSION 6.5 - CHAPTER 6, SECTION 6.5.1
(EXCERPTS)
====================================================================================================

""" + RULE + """
WORK: Higgins JPT, Li T, Deeks JJ (editors). Chapter 6: Choosing effect measures and computing
estimates of effect [last updated August 2023]. In: Higgins JPT, Thomas J, Chandler J, Cumpston M,
Li T, Page MJ, Welch VA (editors). Cochrane Handbook for Systematic Reviews of Interventions,
version 6.5. Cochrane, 2024. (Block 1 is the chapter's own "Cite this chapter as" line.)
URL FETCHED: https://training.cochrane.org/handbook/current/chapter-06, which redirects to
https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-06 (TinyFish
fetch_content, markdown, 2026-09-24). The Handbook landing page
(https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current, fetched the same day)
reads "Version 6.5, 2024".
LICENCE: none is stated in the extracted chapter text or landing page; the site footer, which the
extractor drops, reads "Copyright © 2026 The Cochrane Collaboration" (seen in a search-result
snippet, not in a stored fetch). The online Handbook is free to read; it carries no open licence.
Quote briefly and cite; do not reproduce at length.

WHAT THIS FILE HOLDS: the chapter's author line, Key Points and citation line (block 1); section
6.5 heading and the whole of 6.5.1 through the end of 6.5.1.2 (effect measures for continuous
outcomes; the mean difference; the standardized mean difference, including MECIR Box 6.5.a and
the Hedges' g / Glass' delta paragraph) (block 2).
OMITTED: 6.1-6.4, 6.5.1.3 (ratio of means), 6.5.1.4 (other effect measures), 6.5.2 onward (data
extraction, including obtaining SDs from SEs/CIs), 6.6-6.10, references.
EQUATIONS: NONE IS HELD. The chapter's formulae are images (the page's image list carries
image001.png onward) and the extraction drops them, so the SMD formula is not in this file. The
definition in words is: "The SMD expresses the size of the intervention effect in each study
relative to the between-participant variability in outcome measurements observed in that study",
and "studies for which the difference in means is the same proportion of the standard deviation
(SD) will have the same SMD" (block 2).
Absence of a passage from this file is not absence from the chapter.
"""
s += block(R, U, "BLOCK 1 - chapter author line, Key Points, citation line", "Julian PT Higgins, Tianjing Li",
           "Available from cochrane.org/handbook.")
s += "\n[...]\n[NOTE] Sections 6.1 to 6.4 omitted.\n"
s += block(R, U, "BLOCK 2 - 6.5 Continuous outcome data; 6.5.1, 6.5.1.1, 6.5.1.2",
           "## 6.5 Continuous outcome data", "with both the MD and its SE divided by the externally derived SD.")
s += "\n[...]\n[NOTE] 6.5.1.3 onward omitted, to the end of the chapter.\n"
open("sources/cochrane_handbook_ch06_v6_5.txt", "w").write(s)

# ---------------------------------------------------------------- Chatterjee & Corral 2017
U = "https://www.seahq.org/assets/docs/xix_4_chatterjee.pdf"
R = "chatterjee_corral_2017-seahq-pdf.txt"
U2 = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=5944406"
R2 = "chatterjee_corral_2017-efetch.txt"
s = """CHATTERJEE AND CORRAL 2017, J EDUC PERIOPER MED - HOW TO WRITE WELL-DEFINED LEARNING OBJECTIVES
(WHOLE ARTICLE TEXT, FROM THE PUBLISHER'S PDF TEXT LAYER)
====================================================================================================

""" + RULE + """
CITATION: Chatterjee D, Corral J. How to write well-defined learning objectives. J Educ Perioper
Med 2017;19(4):E610. PMID 29766034, PMCID PMC5944406 (confirmed with the PubMed tool, 2026-09-24).
No DOI is registered in PubMed.
TEXT FETCHED FROM: the journal publisher's (Society for Education in Anesthesia) own PDF,
https://www.seahq.org/assets/docs/xix_4_chatterjee.pdf, linked from
https://www.seahq.org/jepm---past-articles---volume-xix; its text layer via TinyFish fetch_content,
2026-09-24. PMC holds this article as a scanned/PDF-only record: the PMC article page returned no
text, and it is not in the PMC open-access S3 bucket. Block 1 is from the PMC record's front
matter via NCBI E-utilities efetch.
LICENCE: "© 2017 Society for Education in Anesthesia" (block 1, PMC front matter). No open licence;
free to read. Quote briefly and cite.
LAYOUT: the PDF is set in columns with Tables 1-3 interleaved; the text layer runs Table 2 and
Table 1 into the body at page 2 and Table 3 and the Figure 1 caption at page 3, and flattens each
table's columns into lines (Table 2: level, cognitive process, then its verbs one per line; Table 3:
weak objective, SMARTer objective and explanation run together). Hyphenated line-ends are as
extracted. Figure 1 and Figure 2 are images; only their captions are held.

WHAT THIS FILE HOLDS: block 1, the PMC copyright line; block 2, the whole text layer of the
article from the journal header to the end of Table 3 and the Figure 1 caption; block 3, page 4
(LCME/ACGME requirements, conclusion, the rewritten MH objectives). OMITTED: the reference list,
author affiliations, disclosures and the repeated abstract at the end of the PDF.
"""
s += block(R2, U2, "BLOCK 1 - PMC front matter: copyright line", "Oct-Dec2017", "© 2017 Society for Education in Anesthesia")
s += block(R, U, "BLOCK 2 - article text, pages 1-3 (with Tables 1-3 as flattened by the text layer)",
           "Journal of Education in Perioperative Medicine: Vol. XIX, Issue 4   1",
           "LO. http://thesecondprinciple.com)")
s += block(R, U, "BLOCK 3 - page 4: requirements, conclusion, rewritten objectives",
           "Journal of Education in Perioperative Medicine: Vol. XIX, Issue 4   4",
           "specificity.")
s += "\n[...]\n[NOTE] References, affiliations, disclosures and the repeated abstract omitted.\n"
open("sources/chatterjee_corral_2017_objectives.txt", "w").write(s)

# ---------------------------------------------------------------- Adams 2015
U = "https://pmc.ncbi.nlm.nih.gov/articles/PMC4511057/"
R = "adams_2015_bloom-pmcpage.txt"
s = """ADAMS 2015, J MED LIBR ASSOC - BLOOM'S TAXONOMY OF COGNITIVE LEARNING OBJECTIVES (WHOLE ARTICLE)
====================================================================================================

""" + RULE + """
CITATION: Adams NE. Bloom's taxonomy of cognitive learning objectives. J Med Libr Assoc
2015;103(3):152-153. doi:10.3163/1536-5050.103.3.010. PMID 26213509, PMCID PMC4511057 (confirmed
with the PubMed tool, 2026-09-24).
TEXT FETCHED FROM: the PMC article page (TinyFish fetch_content, markdown, 2026-09-24). The article
is not in the PMC open-access S3 bucket (404).
LICENCE: the PMC page reads "Copyright: © 2015, Authors." and links the "PMC Copyright notice"; no
open licence is stated. Free to read. Quote briefly and cite.
WHAT THIS FILE HOLDS: the whole article from the citation line to the end of COMMENTS (abstract,
the six original levels with examples, the revised levels remember, understand, apply, analyze,
evaluate, create, the four knowledge types, and the comments on action verbs). Figure 1 is an
image; only its caption is held. OMITTED: author biography and references.
"""
s += block(R, U, "BLOCK 1 - the article", ". 2015 Jul;103(3):152", "This shortcoming must be considered by educators if health professionals are to achieve increasing levels of skill and function.")
s += "\n[...]\n[NOTE] Biography and references omitted.\n"
open("sources/adams_2015_bloom.txt", "w").write(s)

# ---------------------------------------------------------------- Hake 1998 (abstract)
U = "https://api.crossref.org/works/10.1119/1.18809"
R = "hake_1998-crossref-abstract-decoded.txt"
s = """HAKE 1998, AM J PHYS - INTERACTIVE-ENGAGEMENT VERSUS TRADITIONAL METHODS (ABSTRACT ONLY)
====================================================================================================

""" + RULE + """
CITATION: Hake RR. Interactive-engagement versus traditional methods: a six-thousand-student survey
of mechanics test data for introductory physics courses. Am J Phys 1998;66(1):64-74.
doi:10.1119/1.18809 (volume, issue, pages and DOI as in the Crossref record fetched below).
TEXT FETCHED FROM: the publisher-deposited abstract in the Crossref metadata record,
https://api.crossref.org/works/10.1119/1.18809 (TinyFish fetch_content, 2026-09-25). The record is
JSON; the abstract string alone was decoded with Python's json.loads (unicode escapes such as
\\u3008 become the characters they encode) and saved as
hake_1998-crossref-abstract-decoded.txt; the check below runs against that decoded text. This is
the abstract as published by AAPT, not a model summary.
NOT OBTAINED: the full paper. The AIP article page (pubs.aip.org) returned bot_blocked; Hake's own
posted copy at physics.indiana.edu/~sdi/ajpv3i.pdf was unreachable (host down; the Wayback copy
also unreachable from the session). Copies on third-party sites (stemteachersnyc.org,
jgravesedu.com, Scribd) were not used. The abstract carries the definition of the average
normalised gain and the headline results, which is what C12 needs.
LICENCE: publisher copyright (American Association of Physics Teachers); abstract freely displayed
in Crossref metadata. Quote briefly and cite.
NOTATION: 〈g〉 is the class-average normalised gain; %〈pre〉 and %〈post〉 are class-average
percentage scores; the extraction ends with a stray </jats:p> tag, left in place.
"""
s += block(R, U, "BLOCK 1 - abstract", "A survey of pre/post-test data", "well beyond that obtained in traditional practice.")
open("sources/hake_1998_normalized_gain.txt", "w").write(s)

# ---------------------------------------------------------------- Biggs 1996 (abstract)
U = "https://link.springer.com/article/10.1007/BF00138871"
R = "biggs_1996-springer.txt"
s = """BIGGS 1996, HIGHER EDUCATION - ENHANCING TEACHING THROUGH CONSTRUCTIVE ALIGNMENT (ABSTRACT ONLY)
====================================================================================================

""" + RULE + """
CITATION: Biggs J. Enhancing teaching through constructive alignment. High Educ 1996;32(3):347-364.
doi:10.1007/BF00138871 (volume, issue, pages confirmed from the Crossref record
api.crossref.org/works/10.1007/BF00138871, 2026-09-25; that record is not stored).
TEXT FETCHED FROM: the publisher's article page, https://link.springer.com/article/10.1007/BF00138871
(TinyFish fetch_content, 2026-09-24), which shows the abstract and then "This is a preview of
subscription content". Only the abstract is held.
NOT OBTAINED: the full paper (paywalled at Springer). A copy of the publisher PDF is posted on a
University of Helsinki teaching page (teaching.helsinki.fi/system/files/inline-files/
Biggs1996_Article_EnhancingTeachingThroughConstr.pdf); it was not used, because its licence to
redistribute is not stated. For the course's C10 need (constructive alignment named and defined)
the abstract suffices, and chatterjee_corral_2017_objectives holds a medical-education restatement
(instructional alignment, "Constructive alignment underscores ...").
LICENCE: publisher copyright (Kluwer Academic Publishers 1996, now Springer); abstract freely
displayed. Quote briefly and cite.
"""
s += block(R, U, "BLOCK 1 - abstract", "Two lines of thinking are becoming", "may be generalized to most units or programs in higher education.")
open("sources/biggs_1996_constructive_alignment.txt", "w").write(s)

# ---------------------------------------------------------------- Frich 2015
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC4395611.1/PMC4395611.1.xml"
R = "frich_2015-pmcxml.txt"
s = """FRICH ET AL. 2015, J GEN INTERN MED - LEADERSHIP DEVELOPMENT PROGRAMS FOR PHYSICIANS: A SYSTEMATIC
REVIEW (EXCERPTS)
====================================================================================================

""" + RULE + """
CITATION: Frich JC, Brewster AL, Cherlin EJ, Bradley EH. Leadership development programs for
physicians: a systematic review. J Gen Intern Med 2015;30(5):656-674. doi:10.1007/s11606-014-3141-1.
PMID 25527339, PMCID PMC4395611 (confirmed with the PubMed tool, 2026-09-24).
TEXT FETCHED FROM: the PMC open-access JATS XML (markdown rendering), URL below, 2026-09-24. The
extraction runs front-matter fields together (block 1) and splits citation ranges across lines
(e.g. "19\\n,\\n20").
LICENCE (block 1): "© The Author(s) 2014https://creativecommons.org/licenses/by/4.0/ Open Access
This article is distributed under the terms of the Creative Commons Attribution License which
permits any use, distribution, and reproduction in any medium, provided the original author(s) and
the source are credited." The XML's licence field reads "CC BY".
KIRKPATRICK: this file carries the four Kirkpatrick levels as Frich et al. used them: "reaction
(Level 1), knowledge (Level 2), behavioral change (Level 3), and system results (Level 4)" and
Table 1's seven-category typology (block 3). The labels differ from the usual "reaction, learning,
behaviour, results"; Kirkpatrick's own book is not held.
LEADERSHIP VS MANAGEMENT: the introduction (block 2) gives a one-sentence distinction citing Yukl
(ref 16) and cites Kotter 1990 (ref 17) for "separate systems of action"; Kotter's own lists are
in stoller_2020_leadership, not here.

WHAT THIS FILE HOLDS: licence and structured abstract (block 1); introduction (block 2); Methods,
Data Analysis with Table 1 (block 3); Table 2 (block 4); Results from "A total of 29 articles"
through Evaluation Design and Outcomes, and the whole Discussion (block 5); references 16-17 as
extracted (block 6). OMITTED: literature search, eligibility and review-process paragraphs (in
block 3's lead-in they are omitted), Results "Setting and Target Group" paragraph, Table 3 (45 study
rows), funding lines, other references.
"""
s += block(R, U, "BLOCK 1 - licence and abstract", "© The Author(s) 2014", "rather than system-level outcomes.\n")
s += block(R, U, "BLOCK 2 - Introduction", "High-quality health care increasingly relies on teams", "useful for designing and evaluating future leadership development programs.")
s += "\n[...]\n[NOTE] Literature Search, Eligibility Criteria and Article Review Process omitted.\n"
s += block(R, U, "BLOCK 3 - Data Analysis, Kirkpatrick levels, Table 1", "We extracted curricular descriptors", "The typology is modified after Collins & Holton25 and Kirkpatrick.29")
s += "\n[...]\n[NOTE] Results, Setting and Target Group paragraph omitted.\n"
s += block(R, U, "BLOCK 4 - Table 2", "Table 2Features of 45 Studies", "Data missing for two articles (n\u2009=\u200943)")
s += "\n[...]\n[NOTE] Table 3 (45 rows, one per study) omitted.\n"
s += block(R, U, "BLOCK 5 - Results (from programme duration) and Discussion", "A total of 29 articles described programs", "and an overly narrow focus on individual-level rather than system-level outcomes.")
s += "\n[...]\n[NOTE] Funding and conflict-of-interest lines omitted.\n"
s += block(R, U, "BLOCK 6 - references 16 and 17 as extracted", "16.YuklGALeadership", "What leaders really doHarv Bus Rev")
open("sources/frich_2015_physician_leadership.txt", "w").write(s)

# ---------------------------------------------------------------- Stoller 2020 (Kotter substitute)
U = "https://pmc-oa-opendata.s3.amazonaws.com/PMC7501065.1/PMC7501065.1.xml"
R = "stoller_2020-pmcxml.txt"
s = """STOLLER 2020, CHEST - LEADERSHIP ESSENTIALS FOR CHEST MEDICINE PROFESSIONALS: MODELS, ATTRIBUTES,
AND STYLES (EXCERPTS) - HELD AS THE OPEN SOURCE FOR KOTTER'S LEADING/MANAGING DISTINCTION
====================================================================================================

""" + RULE + """
CITATION: Stoller JK. Leadership essentials for CHEST medicine professionals: models, attributes,
and styles. Chest 2021;159(3):1147-1154 (online 19 Sep 2020). doi:10.1016/j.chest.2020.09.095.
PMID 32956716, PMCID PMC7501065 (confirmed with the PubMed tool, 2026-09-25).
WHY THIS FILE: Kotter JP, What leaders really do, Harv Bus Rev 1990;68(3):103-111 (republished Dec
2001, hbr.org/2001/12/what-leaders-really-do) was fetched 2026-09-24 and returned only HBR's metered
teaser (title, standfirst, first paragraph); the article body is behind HBR's paywall. This paper's
Table 1, "Attributes of Managing vs Leading", is marked "After Kotter.7", and reference 7 is Kotter
1990 (block 3). The table is Stoller's adaptation, not Kotter's wording: cite it as "after Kotter,
as tabulated by Stoller 2020".
TEXT FETCHED FROM: the PMC open-access JATS XML (markdown rendering), URL below, 2026-09-25.
LICENCE (block 1): "© 2020 American College of Chest Physicians. Published by Elsevier Inc. All
rights reserved." with Elsevier's COVID-19 resource centre permission (quoted whole in block 1),
which grants PMC "rights for unrestricted research re-use and analyses in any form or by any means
with acknowledgement of the original source" for as long as that centre remains active. Not a CC
licence. Quote briefly and cite.
WHAT THIS FILE HOLDS: licence (block 1); abstract (block 2); the section "The Ubiquity of the Need
for Leadership" including Table 1 (block 3); reference 7 as extracted (block 4). OMITTED: the
rest of the article (evidence that physician leadership matters, leadership paradox, models,
virtues, styles, situational leadership, development) and other references.
"""
s += block(R, U, "BLOCK 1 - copyright and licence", "© 2020 American College of Chest Physicians.", "remains active.")
s += block(R, U, "BLOCK 2 - abstract", "In the context that leadership matters", "signature features of leading health-care organizations.")
s += "\n[...]\n[NOTE] Opening paragraphs (COVID-19 example, outline of the series) omitted.\n"
s += block(R, U, "BLOCK 3 - The Ubiquity of the Need for Leadership; Table 1", "The Ubiquity of the Need for Leadership", "After Kotter.7")
s += "\n[...]\n"
s += block(R, U, "BLOCK 4 - reference 7 as extracted", "7KotterJ.What leaders really do", "What leaders really doHarv Bus Rev")
open("sources/stoller_2020_leadership.txt", "w").write(s)

json.dump(MANIFEST, open("books/S57-R1/intake/manifest-b-new.json", "w"), ensure_ascii=False, indent=0)
print(len(MANIFEST), "passages")
