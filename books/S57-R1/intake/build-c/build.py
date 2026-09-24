"""Build the group-c source files for S57-R1 from the saved raw TinyFish fetches.

Every passage and every quoted evidence line is cut from the raw text by script (raw[i:j]);
nothing between [TEXT] and [END TEXT] is typed by hand. Run verify.py afterwards.
"""
import os, json, sys
sys.path.insert(0, os.path.dirname(__file__))
from cut import cut, block, raw

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
SRC = os.path.join(ROOT, 'sources')
FETCHED = '2026-09-24'
MANIFEST = []   # (citekey, block no, raw file, url, i, j)

U = {
 'vol1': 'https://nmc.org.in/storage/new/UG-Curriculum-Vol-I.pdf',
 'fc': 'https://nmc.org.in/storage/new/FOUNDATION-COURSE-MBBS-17.07.2019.pdf',
 'ugpage': 'https://nmc.org.in/page/information-desk-for-colleges-ug-curriculum',
 'rules': 'https://nmc.org.in/page/rules-regulations-rules-regulations-nmc',
 'gmer23': 'https://nmc.org.in/storage/cms/rules-regulation-nmc/G83KmfBTvRKFfp99s6Vvjuuw3gJ7WM2ZP28Z3Zhk.pdf',
 'gmer23c': 'https://nmc.org.in/storage/cms/rules-regulation-nmc/QwhpGdAJfo2yFLcbox9qHeAAJ4ZVhjAxq2CU2YlG.pdf',
 'cbme24': 'https://nmc.org.in/storage/cms/rules-regulation-nmc/YTW423v3EsCFdtPv3I5qZkaNNhuXfub42UZITDRM.pdf',
 'cbme24c': 'https://nmc.org.in/storage/cms/rules-regulation-nmc/fzR5SHdI5dNhLCPbGWQNS6WhYGVohp8FRY7AWh7t.pdf',
 'gmer19': 'https://nmc.org.in/19GraduateMedicalEducationRegulations1997Amendment04112019-2.pdf',
 'miqf': 'https://nmc.org.in/storage/cms/rules-regulation-nmc/QZSDeGu7WXS9MMI0dL5ZR1EbS48kLaFbvMTpww2B.pdf',
 'miqffaq': 'https://nmc.org.in/storage/cms/rules-regulation-nmc/iFB9GIjrd5y98IADDnFGyTzqgguiEYO5HI37Jh6L.pdf',
 'teq': 'https://nmc.org.in/storage/cms/rules-regulation-nmc/YTXtXo4jg8rF1oti1OoeyStBhePAQ5NoS3qVE16H.pdf',
 'mahajan': 'https://pmc-oa-opendata.s3.amazonaws.com/PMC11189270.1/PMC11189270.1.xml',
 'disc': 'https://nmc.org.in/page/disclaimer',
 'hindu': 'https://www.thehindu.com/news/national/nmc-withdraws-graduate-medical-education-regulations-2023/article67011152.ece',
}
RF = {
 'vol1': 'mci_cbme_ug_curriculum_vol1_2018.txt', 'fc': 'mci_foundation_course_2019.txt',
 'ugpage': 'nmc_ug_curriculum_page-20260924.txt', 'rules': 'nmc_rules_regs_page-20260924.txt',
 'gmer23': 'nmc_gmer_2023-gazette-20230602.txt', 'gmer23c': 'nmc_gmer_2023-corrigendum-20230616.txt',
 'cbme24': 'nmc_cbme_2024-20240912.txt', 'cbme24c': 'nmc_cbme_2024-clarification-20241010.txt',
 'gmer19': 'mci_gmer_1997_amend_2019-20191104.txt', 'miqf': 'nmc_miqf_2025-20250630.txt',
 'miqffaq': 'nmc_miqf_2025-faq-20251028.txt', 'teq': 'nmc_teq_2022-20220214.txt',
 'mahajan': 'mahajan_gupta_2024_gmer-PMC11189270.txt', 'disc': 'nmc_site_disclaimer-20260925.txt',
 'hindu': 'thehindu_20230626_gmer_withdrawal.txt',
}

def q(src, start, end, after=0, nth=1):
    """A verbatim evidence quote for a header, cut from raw; recorded for the check."""
    s, i, j = cut(RF[src], start, end, after, nth)
    MANIFEST.append(('HEADER', 0, RF[src], U[src], i, j))
    return s

class F:
    def __init__(self, key):
        self.key, self.parts, self.n = key, [], 0
    def b(self, title, src, start, end, after=0, nth=1, note=None, kind='TEXT'):
        s, i, j = cut(RF[src], start, end, after, nth)
        self.n += 1
        MANIFEST.append((self.key, self.n, RF[src], U[src], i, j))
        if note:
            self.parts.append('\n' + '\n'.join('[NOTE] ' + x for x in note) + '\n')
        self.parts.append(block(self.n, title, U[src], s, kind))
    def gap(self, *lines):
        self.parts.append('\n[...]\n' + '\n'.join('[NOTE] ' + x for x in lines) + '\n')
    def write(self, header):
        with open(os.path.join(SRC, self.key + '.txt'), 'w', encoding='utf-8') as fh:
            fh.write(header.rstrip() + '\n' + ''.join(self.parts))

RULE_TXT = """Transcription rule for this file: every line between a [TEXT] and an [END TEXT] line is an exact,
unaltered slice of the text returned by the TinyFish fetch_content tool for the URL in that block's
heading, cut programmatically from the saved fetch (raw[i:j]); nothing has been paraphrased, smoothed or
merged. The text is a PDF's text layer as TinyFish extracted it, so it keeps that layer's line breaks,
split words ("Graduat e") and stray spacing, and page furniture (running heads, page numbers) where it
falls inside a passage. Quoted evidence in this header is cut the same way and passes the same check.
Where material is left out, the omission is marked [...] in place. Lines beginning [NOTE] are this
file's own annotation and are NOT source text."""

NMC_SITE = q('disc', 'National Medical Commission (“NMC”) authorizes you to copy any documents', 'is expressly prohibited.')

# ---------------------------------------------------------------- 1. CBME curriculum Vol I, 2018
f = F('mci_cbme_ug_curriculum_2018_vol1')
lic = q('vol1', 'The co ntents, embodied in this', 'competent authorities of the Medical Council of India.')
f.b('Title page', 'vol1', 'COMPETENCY BASED UNDERGRADUATE CURRICULUM \nFOR THE  \nINDIAN MEDICAL GRADUATE', 'New Delhi 110 077')
f.gap('Omitted: the Board of Governors foreword (pp. 3-4) and the list of contributors (pp. 5-6).')
f.b('Copyright grant and how to cite (p. 7)', 'vol1', 'Grant of Copyright to the Competency based Undergraduate Curriculum', '(give page nos.)')
f.b('Contents, Vol. I (p. 8)', 'vol1', 'Contents \nVol. I', 'List of contribut ing subject experts   252')
f.gap('Omitted: contents pages for Vols II and III (pp. 9-10).')
f.b('Preamble; How to use the Manual (Section 1, IMG goals and roles; Section 2, domains and levels; Section 3, '
    'integration; worked examples deriving objectives, learning methods and assessment from a competency); '
    'Definitions used in the Manual, domains of learning and levels of competency (pp. 11-39)',
    'vol1', 'COMPETENCY BASED UNDERGRADUATE CURRICULUM \nFOR  \nTHE INDIAN MEDICAL GRADUATE \n \nPreamble',
    'or the phase in which the competency has been identified.')
f.b('Head of the first subject table, Human Anatomy (p. 40 onward): the column headings every subject table uses',
    'vol1', 'HUMAN ANATOMY (CODE: AN)', 'Assessment \nMethods')
f.gap('Omitted: all subject competency tables (Anatomy AN p. 41 to Forensic Medicine FM p. 251) and the list of '
      'contributing subject experts. Absence of a passage from this file is not absence from the document.')
f.write(f"""MCI, COMPETENCY BASED UNDERGRADUATE CURRICULUM FOR THE INDIAN MEDICAL GRADUATE, VOL. 1 (2018)
— VERBATIM SOURCE PACK (EXCERPTS)
============================================================

{RULE_TXT}

CITATION: Medical Council of India. Competency based Undergraduate Curriculum for the Indian Medical
Graduate, 2018. Vol. 1. New Delhi: MCI; 2018 (issued by the Board of Governors in supersession of MCI;
implemented from the MBBS batch admitted August 2019).
URL FETCHED: {U['vol1']} (linked as "UG-Curriculum-Vol-I" from the NMC UG Curriculum page,
{U['ugpage']}). TinyFish fetch_content, markdown, {FETCHED}; the PDF's text layer came back whole
(536,399 characters).

LICENCE / COPYRIGHT AS STATED IN THE DOCUMENT (p. 7): "{lic}"
The NMC website's disclaimer ({U['disc']}, fetched 2026-09-25) adds: "{NMC_SITE}"
[NOTE] So this is NOT an open licence. The passages below are held for internal quote-checking only; the
reader-facing text should cite and paraphrase, quoting only briefly. Harsh to decide whether that is enough.

CURRENCY: SUPERSEDED as the curriculum in force. NMC's Rules & Regulations page (fetched {FETCHED}) lists
"Competency Based Medical Education (CBME) Guideline dated 01.08.2023" and "Competency Based Medical
Education (CBME) Curriculum 2024 dated 12.09.2024" under the UGMEB; the 2024 document is held as
`nmc_cbme_2024`. The 2018 Vol. 1 is the original CBME curriculum (in force for batches from 2019) and
the historical source for the five IMG roles and the K/KH/SH/P coding. What changed in 2024: two roles
added (Critical Thinker, Researcher) and "S - Shows" dropped from the levels list (see `nmc_cbme_2024`).

WHAT THIS FILE HOLDS: title page; the copyright grant and citation line (p. 7); the Vol. I contents; the
whole run from the Preamble (p. 11) to the end of "Levels of competency" (p. 39), which carries the
extract from the GMER on IMG goals and the five roles (2.3.1-2.3.5) and their competencies (3.1-3.5), the
subject-outcome counts, how domains (K/S/A/C), levels (K, KH, S, SH, P) and core (Y/N) are coded,
the worked examples deriving objectives, teaching methods and assessment methods from a competency
(PA42.3, MI2.4), the integration statement (alignment, sharing, nesting; "not to exceed 20%";
"Assessment will continue to be subject based"), definitions, action verbs and the levels table; and
the column headings of the first subject table. Omitted: foreword, contributors, all subject tables.
""")

# ---------------------------------------------------------------- 2. CBME Guidelines / Curriculum 2024
f = F('nmc_cbme_2024')
gm23 = q('cbme24', 'Following the Regulations on Gra duate Medical Education (GMER) 1997', 'was placed last year.')
f.b('NMC covering letter, 12-09-2024', 'cbme24', 'No. D-11011/500/2024-AcademicCell', 'Encl.: As above')
f.b('Guidelines part: 1 Preamble; 2 Objectives of the Indian Graduate Medical Training Programme; 3 National '
    'Goals; 4 Institutional Goals; 5 Goals for the Learner (the seven Roles); 6 Competency Based Training '
    'Programme of the IMG (competencies under each role, a-g) (pp. 1-9)',
    'cbme24', 'COMPETENCY BASED MEDICAL EDUCATION (CBME) CURRICULUM 2024', 'Demonstrate basic principles and ethical implications of research governance.')
f.gap('Omitted: "A. CURRICULUM" subject goals, Anatomy to Radiodiagnosis (pp. 9-26), and the language-of-'
      'instruction paragraph that ends p. 26.')
f.b('Foundation Course and training period; phases; teaching hours; new teaching/learning elements (Foundation '
    'Course, Early Clinical Exposure, Electives, AETCOM, Alignment and integration, Learner-doctor method); '
    'Assessment (attendance, internal assessment, certifiable competencies, remedial measures, university '
    'examinations, passing criteria, appointment of examiners) (pp. 27-45)',
    'cbme24', 'In order to ensure that training is in alignment with the goals  and',
    '(10) There shall be NO grace marks to be considered for passing in an examination.')
f.gap('Omitted: Annexures 1-3 (AETCOM governance, academic calendar, phase-wise subjects).')
f.b('Annexure 4: Foundation Course hours (2 weeks)', 'cbme24', 'Annexure 4 \nFoundation Course- 2 weeks', 'Total 80')
f.gap('Omitted: Annexures 5-13, the disability guidelines, and the curriculum volumes\' forewords and contents.')
f.b('Curriculum volume, "How to use the Manual": Section 1 (IMG roles extracted from the CBME Guidelines 2024) '
    'through "Definitions used in the Manual", domains of learning and "Levels of competency" (Vol. I pp. 8-31)',
    'cbme24', 'How to use the Manual \n \nThis Manual is intended for curriculum planners',
    'necessarily in the subject or the phase in which the competency has been identified', after=100000)
f.b('Head of the first subject table, Anatomy (Vol. I p. 34): column headings and the first two competencies',
    'cbme24', 'Number COMPETENCY \nThe student should be able to \nPredominant', 'K K H Y LGT Written/ viva  ', after=100000)
f.gap('Omitted: every subject competency table in Vols I-III, and the lists of contributors.')
f.b('NMC letter of 10-10-2024 and the UGMEB clarification with its Corrigendum/Addendum to the CBME Guideline 2024',
    'cbme24c', 'Subject: UGMEB reference: Additional clari', 'does not\nfall under the purview of MBBS curriculum.')
f.write(f"""NMC, COMPETENCY BASED MEDICAL EDUCATION (CBME) CURRICULUM / GUIDELINES 2024 (12 SEPTEMBER 2024)
— VERBATIM SOURCE PACK (EXCERPTS)
============================================================

{RULE_TXT}

CITATION: National Medical Commission, Undergraduate Medical Education Board. Guidelines for Competency
Based Medical Education (CBME) Curriculum 2024. Letter No. D-11011/500/2024-AcademicCell (e-8284443),
12 September 2024, with the Competency Based Undergraduate Curriculum for the Indian Medical Graduate
2024 (Vols I-III) enclosed; and the UGMEB's "Additional clarification on CBME Guideline, 2024",
letter of 10 October 2024 with Corrigendum/Addendum.
URLS FETCHED: {U['cbme24']} (805,200 characters of text layer) and {U['cbme24c']}; both linked from
{U['rules']} as items 2.3 and 2.3.a under "Under-Graduate Medical Education Board (UGMEB)". TinyFish
fetch_content, markdown, {FETCHED}.

LICENCE / COPYRIGHT: none is stated in the document (no copyright or reproduction line in the text
layer). The NMC website disclaimer ({U['disc']}) applies to documents on the site: "{NMC_SITE}"

CURRENCY: This is the latest undergraduate curriculum instrument listed on NMC's Rules & Regulations
page on {FETCHED}; it replaces the CBME Guideline of 01.08.2023 (not held: its PDF, {U['rules']} item
2.2, returned no text layer). Its own preamble places it under GMER 2023: "{gm23}"
It is a guideline issued by letter, not a Gazette regulation. Event trigger for review: any later NMC
CBME curriculum/guideline or a GMER amendment.

WHAT THIS FILE HOLDS: the covering letter; the guideline sections 1-6 whole (preamble, national and
institutional goals, the seven IMG roles a-g and the competencies under each); pp. 27-45 whole
(Foundation Course requirement, training period, phases, hours, the new teaching-learning elements
with the Foundation Course goal and objectives, AETCOM, alignment and integration, learner-doctor
method, and the whole Assessment section); Annexure 4 (Foundation Course hours); the curriculum
volume's "How to use the Manual" through "Levels of competency" (roles and competencies, domains
K/S/A/C, levels K/KH/SH/P); the head of the Anatomy table; and the 10 October 2024 clarification
with its corrigendum. Omitted: subject goals, most annexures, the disability guidelines, all subject
competency tables. Absence of a passage from this file is not absence from the document.
[NOTE] In the 2024 levels table "S - Shows" no longer appears (2018 had K, KH, S, SH, P), and the Anatomy
table heads its domain column "Predominant Domain".
""")

# ---------------------------------------------------------------- 3. GMER 2023
f = F('nmc_gmer_2023')
ev_rules = q('rules', 'Under-Graduate Medical Education Board (UGMEB)', '2.3.a. Additional clarification on CBME Guideline, 2024 published on 12.09.2024 dated 10.10.2024')
ev_mah1 = q('mahajan', 'We have deliberately omitted mention', 'which are the CBME Guidelines 2023 (News ID 523).')
ev_mah2 = q('mahajan', 'These regulations, gazette notified and never withdrawn, remain in force.', 'All these documents are currently in force.')
ev_hindu = q('hindu', '“It is informed that the Circular of even number dated 12.06.2023', 'Undergraduate Medical Education Board (UGMEB).”')
f.b('GMER 2023, English version, whole (Gazette of India, Extraordinary, Part III Sec. 4, No. 367, 2 June 2023, '
    'pp. 6-9): preamble goals 1-11, Chapters I-VII, signature and language note',
    'gmer23', 'NATIONAL MEDICAL COMMISSION \n(Under Graduate Medical Education Board, 2023)',
    'doubt about the interpretation of these Regulations.',
    note=['The Hindi version (pp. 1-5) is omitted. The English note at the end says the English version prevails.',
          'The regulation numbering runs 1, 2, 3, 4, 6 in Chapter II (no 5) as printed.'])
f.b('Corrigendum of 16 June 2023 (Gazette No. 421, 19 June 2023), English version, whole', 'gmer23c',
    'NATIONAL MEDICAL COMMISSION \n(Under Gradaute Medical Education Board)', '[ADVT.-III/4/Exty./202/2023-24]')
f.b('Front-matter of the Gazette issue (for the notification number and date)', 'gmer23',
    'सं.   367] नई कदल्ली', 'CG-DL-E-02062023-246254')
f.write(f"""NMC, GRADUATE MEDICAL EDUCATION REGULATIONS, 2023 ("GMER-23") — VERBATIM SOURCE PACK
============================================================

{RULE_TXT}

CITATION: National Medical Commission (Under Graduate Medical Education Board). Graduate Medical
Education Regulations, 2023. Notification No. U-14021-8-2023-UGMEB, New Delhi, 2 June 2023. Gazette
of India, Extraordinary, Part III, Section 4, No. 367 (CG-DL-E-02062023-246254). Corrigendum F. No.
U.14021-8-2023-UGMEB, 16 June 2023 (Gazette No. 421, CG-DL-E-19062023-246659), substituting clause
11(a) (NEET-UG age: 31 December).
URLS FETCHED: {U['gmer23']} and {U['gmer23c']}, linked from {U['rules']} as UGMEB items 2 and 2.a.
TinyFish fetch_content, markdown, {FETCHED}. (The PDF host redirected to a bare IP address,
https://3.111.69.97/..., which served the file.)

LICENCE / COPYRIGHT: none is stated in the Gazette text. NMC website disclaimer ({U['disc']}):
"{NMC_SITE}"

WHICH GRADUATE MEDICAL EDUCATION REGULATIONS ARE IN FORCE (checked {FETCHED}):
GMER 2023 was notified in the Gazette and, on the evidence found, has not been withdrawn or held in
abeyance. What was withdrawn in June 2023 was a separate circular of 12 June 2023 issuing "Guidelines
under Graduate Medical Education Regulations 2023". The detailed curriculum, Foundation Course and
assessment rules now sit in NMC's CBME Guidelines 2024 (held as `nmc_cbme_2024`), which were issued
under GMER 2023; GMER 2023 itself is short and names none of the IMG roles, the Foundation Course or
the K/KH/SH/P levels. The older Regulations on Graduate Medical Education, 1997, Part II (added by the
2019 amendment, held as `mci_gmer_2019_amendment`) are still listed on NMC's site among the erstwhile
MCI regulations; the GMER 2023 text held here contains no repeal or supersession clause.
Evidence:
(1) NMC Rules & Regulations page, UGMEB section, as fetched ({U['rules']}) — it lists GMER 2023 and its
corrigendum with no abeyance or withdrawal entry (contrast the EMRB section of the same page, which lists
an "Amendment Notification Keeping Regulation Dated 02.08.2023 in Abeyance" for a different regulation):
"{ev_rules}"
(2) Mahajan R, Gupta K, Int J Appl Basic Med Res 2024;14(2):71-77 (held as `mahajan_gupta_2024_gmer_cbme`):
"{ev_mah1}" and, on GMER 2023's Chapter V clause 21: "{ev_mah2}"
(3) The Hindu, 26 June 2023 (news report, not filed as a source; raw fetch kept at
books/S57-R1/intake/raw/{RF['hindu']}), quoting the NMC circular: "{ev_hindu}"
[NOTE] The withdrawal circular itself (NMC circular of about 23 June 2023) was not fetched from nmc.org.in;
the two reports above quote or describe it. If a reader-facing claim rests on the withdrawal wording,
Harsh should locate that circular on nmc.org.in (Circulars/Public Notices, June 2023).
(4) NMC's CBME Guidelines 2024, preamble (held in `nmc_cbme_2024`): "{gm23}"

WHAT THIS FILE HOLDS: the whole English text of GMER 2023 and of its 16 June 2023 corrigendum, and the
Gazette front-matter line giving the issue number and date. Omitted: the Hindi versions.
""")

# ---------------------------------------------------------------- 4. GMER 1997 Part II (2019 amendment)
f = F('mci_gmer_2019_amendment')
f.b('Amendment notification (4 November 2019), arrangement of clauses of Part II, and Chapter I whole: '
    '1 Introduction; 2 IMG training programme, national and institutional goals; 2.3 Goals and Roles for the '
    'Learner; 3 competencies under each role; 4 broad outline on training format; 4.2 faculty development',
    'gmer19', 'BOARD OF GOVERNORS IN SUPER-SESSION  \nOF MEDICAL COUNCIL OF INDIA \nAMENDMENT NOTIFICATION',
    'their teaching skills to curricular objectives.')
f.b('Chapter IV, opening paragraph (the curriculum for batches from 2019-20)', 'gmer19',
    'CHAPTER IV \nPHASE WISE TRAINING AND TIME DISTRIBUTION FOR PROFE SSIONAL DEVELOPMENT',
    'remain as contained in the Part I of these Regulations.')
f.gap('Omitted: clauses 7-8 (training period, phases, examination timing) and Tables 1-2.')
f.b('Table 3: Foundation Course (one month), hours and notes', 'gmer19', 'Table 3: Foundation Course (one month)',
    'Teaching of Foundation Course will be organized by pre-clinical departments.')
f.gap('Omitted: Tables 4-8 (teaching hours and postings) and clause 8.6 onward to 9.')
f.b('Clause 9 / 9.1 Foundation Course, whole', 'gmer19', '9.  New teaching / learning elements',
    '9.1.11  Every college must arrange for a meeting with parents and their wards.', after=907000)
f.gap('Omitted: 9.2-9.5 (early clinical exposure, electives, AETCOM, clinical clerkship) and Chapter V '
      '(subject competencies).')
f.b('Chapter VI Assessment, clause 11.1 Eligibility to appear for Professional examinations (attendance, '
    'internal assessment)', 'gmer19', 'CHAPTER VI \nASSESSMENT  \n11.', 'for appearing at the final university examination of that subject.')
f.gap('Omitted: 11.2 University Examinations onward, Chapter VII Internship, and the Hindi version (which '
      'fills the first 873,000 characters of the text layer).')
f.write(f"""MCI (BOARD OF GOVERNORS), REGULATIONS ON GRADUATE MEDICAL EDUCATION (AMENDMENT), 2019 — PART II OF
THE REGULATIONS ON GRADUATE MEDICAL EDUCATION, 1997 ("GMER 2019") — VERBATIM SOURCE PACK (EXCERPTS)
============================================================

{RULE_TXT}

CITATION: Board of Governors in super-session of Medical Council of India. Regulations on Graduate
Medical Education (Amendment), 2019. Notification No. MCI-34(41)/2019-Med./161726, New Delhi,
4 November 2019. Gazette of India, Extraordinary, Part III, Section 4, No. 390, 6 November 2019. Adds
Part II to the Regulations on Graduate Medical Education, 1997, governing MBBS batches from 2019-20.
URL FETCHED: {U['gmer19']} (linked from {U['rules']} as "Graduate Medical Education Regulations 1997
(Amendment Dated 04.11.2019 (UGMEB)"). TinyFish fetch_content, markdown, {FETCHED}.

LICENCE / COPYRIGHT: none is stated in the Gazette text. NMC website disclaimer ({U['disc']}):
"{NMC_SITE}"

CURRENCY: historical for the curriculum. The CBME curriculum and its regulations have since been
restated in NMC's CBME Guidelines 2023 and CBME Curriculum 2024 (held: `nmc_cbme_2024`) under the
Graduate Medical Education Regulations, 2023 (held: `nmc_gmer_2023`, whose header records what was
found on which is in force). This is the first regulation to define the "Indian Medical Graduate" and
the five roles; cite it for that history, not for current rules.

WHAT THIS FILE HOLDS: the notification; the arrangement of clauses; Chapter I whole (IMG definition,
goals, the five roles 2.3.1-2.3.5, the competencies 3.1-3.5, the training-format outline including
4.1.8 formative and summative assessment and 4.2 faculty development programmes); Chapter IV's opening
paragraph; Table 3 (Foundation Course hours); clause 9.1 whole (Foundation Course); clause 11.1
(eligibility: attendance, internal assessment). Omitted as marked.
""")

# ---------------------------------------------------------------- 5. Foundation Course module 2019
f = F('mci_foundation_course_2019')
lic = q('fc', 'All rights reserved.', 'permitted by copyright law 2019.')
f.b('Title page', 'fc', 'Foundation Course for the Undergraduate \nMedical Education Program', 'New Delhi 110 077')
f.b('Rights statement and how to cite', 'fc', 'All rights reserved.', 'pp 1-46.')
f.gap('Omitted: the list of authors and expert group.')
f.b('Sections 1-9 whole: objective of the document, glossary, introduction, purpose, the GMER 9.1 context, '
    'major components, programme structure (Table 1), module list, learning outcomes FC 1.1-5.5 with domain '
    'and level, formative and internal assessment, capacity building for faculty, curricular governance',
    'fc', 'FOUNDATION COURSE \nObjective of the document', 'within four weeks of completion of Foundation Course.')
f.gap('Omitted: the sample weekly schedule and the lesson plans for modules 1-3, 4A-4C.')
f.b('Lesson plan 4D: Working in a health care team', 'fc', '4D Professionalism and Ethics Module: Working in a health care team',
    'Assessment : Formative assessment during group discussions / presentations')
f.gap('Omitted: lesson plans 4E-4I.')
f.b('Lesson plan 4J: Learning', 'fc', '4J  Professionalism and Ethics: Learning', 'Assessment: Nil',
    note=['Objective 2 of 4J reads "To identify and maximize one\'s learning style" and its method includes a',
          '"learning style evaluation"; relevant to the book\'s learning-styles concept (S57-R1-C06).'])
f.gap('Omitted: lesson plans 5A-6 and the further-reading links.')
f.write(f"""MCI, FOUNDATION COURSE FOR THE UNDERGRADUATE MEDICAL EDUCATION PROGRAM (2019), CURRICULUM
IMPLEMENTATION SUPPORT PROGRAM MODULE 1 — VERBATIM SOURCE PACK (EXCERPTS)
============================================================

{RULE_TXT}

CITATION: Medical Council of India (Board of Governors in supersession). Foundation Course for the
Undergraduate Medical Education Program, 2019. Curriculum Implementation Support Program, Module 1.
New Delhi: MCI; 2019: pp 1-46 (file dated 17.07.2019).
URL FETCHED: {U['fc']} (linked as "Foundation Course For Undergraduate Medical Education" from
{U['ugpage']}). TinyFish fetch_content, markdown, {FETCHED}; text layer whole (64,479 characters).

LICENCE / COPYRIGHT AS STATED IN THE DOCUMENT: "{lic}"
[NOTE] Not an open licence: brief quotation in critical review is what it allows. Held for internal
quote-checking; the reader-facing text should paraphrase and cite. Harsh to decide.

CURRENCY: the module describes a one-month Foundation Course under GMER 2019. The CBME Guidelines 2024
(held: `nmc_cbme_2024`, p. 29 and Annexure 4) now set the Foundation Course at two weeks (80 teaching
hours) with revised objectives. Cite this module for the course's design and history; cite
`nmc_cbme_2024` for the current duration and objectives.

WHAT THIS FILE HOLDS: title page; the rights statement; sections 1-9 whole (including the learning
outcomes table FC 1.1-5.5, each with domain and K/KH/SH level, and section 7 on formative and internal
assessment); the lesson plans for 4D (working in a health care team) and 4J (learning). Omitted: the
author list, sample schedule and the other lesson plans.
""")

# ---------------------------------------------------------------- 6. MIQF 2025
f = F('nmc_miqf_2025')
f.b('Notification (30 June 2025), preamble with the supersession of TEQ 2022, regulation 1 (short title and '
    'commencement) and regulation 2 (definitions)', 'miqf', 'NATIONAL MEDICAL COMMISSION\n  \nNOTIFICATION \nNew Delhi, the 30th June 2025.',
    'specified by the Commission from time to time; \n(k) "Schedule" means the Schedule annexed to these regulations;')
f.gap('Omitted: regulation 2(1)(l)-(2) and regulations 3-12.')
f.b('Regulations 13-14 (counting of teaching experience; exemption from the Basic Course in Medical Education)',
    'miqf', '13. Counting of teaching experience in certain postings.', 'two years of appointment in a recognised medical institution.')
f.gap('Omitted: regulations 15 onward and Schedule Tables A-D (qualifications by specialty).')
f.b('Schedule, Table E: experience, research and other requirements for faculty in broad specialties (MD/MS), '
    'whole; Table F: the same for super specialties (DM/MCh), whole; signature and language note',
    'miqf', '(e) Table E \nExperience, research and other requirements', 'of any doubt about the interpretation of these Regulations.')
f.b('Dentistry faculty (regulation 20 table): Professor, Associate and Assistant Professor rows as far as the '
    'Senior Resident row', 'miqf', '(b) (i) have published at least two research publications \nafter appointment as Associate Professor',
    'Lecturer in the concerned subject in a recognised medical \nor dental college after acquiring MDS degree.',
    note=['This block begins mid-row (Professor, M.D.S., part (b)); the row\'s part (a) is on the previous page and is omitted.'])
f.b('PGMEB public notice on the FAQs (gives the Gazette date 30.06.2025)', 'miqffaq', 'PUBLIC NOTICE', 'Frequently Asked Questions (FAQs).', after=1000)
f.b('FAQ Q5 (Note 2 of Table E: BCME and BCBR within two years)', 'miqffaq', 'Q5.', 'research within two years of the appointment.', after=5000)
f.write(f"""NMC, MEDICAL INSTITUTIONS (QUALIFICATIONS OF FACULTY) REGULATIONS, 2025 — VERBATIM SOURCE PACK (EXCERPTS)
============================================================

{RULE_TXT}

CITATION: National Medical Commission. Medical Institutions (Qualifications of Faculty) Regulations,
2025. Notification F. No. N-P051(12)/18/2024-PGMEB-NMC, New Delhi, 30 June 2025. Gazette of India,
Extraordinary, Part III, Section 4 (issue number not in the text layer; "4268 GI/2025" printer's
line). Made in supersession of the Teachers Eligibility Qualifications in Medical Institutions
Regulations, 2022. FAQs: PGMEB letter No. N-P016(11)/2/2025-PGMEB-NMC, 28 October 2025.
URLS FETCHED: {U['miqf']} and {U['miqffaq']}, linked from {U['rules']} as PGMEB items 1 and 1.1.
TinyFish fetch_content, markdown, {FETCHED}.

LICENCE / COPYRIGHT: none is stated in the Gazette text. NMC website disclaimer ({U['disc']}):
"{NMC_SITE}"

WHICH INSTRUMENT REQUIRES THE COURSE (answer to READY.md's "to identify"): this one, now. The Teachers
Eligibility Qualifications in Medical Institutions Regulations, 2022 (TEQ 2022; held as `nmc_teq_2022`)
required "the basic course in Medical Education Technology" and "the Basic course in Biomedical
Research" for Associate Professor and Professor; these 2025 regulations supersede TEQ 2022 (block 1).
Under Table E (block 3) an Associate Professor or Professor in a broad specialty "shall be required to
undergo Basic Course in Medical Education provided their broad specialty subject is covered under
undergraduate training", and must have completed the Basic Course in Biomedical Research; regulation 14
(block 2) exempts super-specialty faculty, faculty in broad specialties outside the undergraduate
curriculum, and (with a two-year catch-up) faculty in institutes of national importance. The Assistant
Professor row of Table E does not list the Basic Course in Medical Education (block 3). Table F (super
specialties) lists only the Basic Course in Biomedical Research. Event trigger: any amendment of these
regulations.

WHAT THIS FILE HOLDS: the English notification and regulations 1-2(1)(k); regulations 13-14; Tables E
and F whole with the signature; part of the dentistry faculty table; the FAQ public notice and FAQ Q5.
Omitted: the Hindi version, regulations 3-12 and 15 onward, Tables A-D, the other FAQs.
""")

# ---------------------------------------------------------------- 7. TEQ 2022 (superseded)
f = F('nmc_teq_2022')
f.b('Title, notification (14 February 2022), regulations 1-2', 'teq', 'TEACHERS ELIGIBILITY QUALIFICATIONS IN MEDICAL INSTITUTIONS  \nREGULATIONS, 2022',
    'so as to maintain a standard of teaching in medical institutions.')
f.gap('Omitted: regulations 3-10 (general norms) up to Table 1A.')
f.b('Table 1A: norms for faculty appointment and promotion in broad specialties (Professor, Associate '
    'Professor, Assistant Professor, Senior Resident/Tutor)', 'teq', 'Table 1A.  Norms for Faculty Appointment and Promotion in Broad Specialties',
    'The posts of Senior Resident and Tutor are tenure positions not exceeding 3 \nyears.')
f.gap('Omitted: the rest of the regulations to clause 15.')
f.b('Clause 16, Repeal; signature', 'teq', '16.  Repeal:', '[ADVT.-III/4/Exty./657/2021-22]')
f.write(f"""NMC, TEACHERS ELIGIBILITY QUALIFICATIONS IN MEDICAL INSTITUTIONS REGULATIONS, 2022 — SUPERSEDED —
VERBATIM SOURCE PACK (EXCERPTS)
============================================================

{RULE_TXT}

CITATION: National Medical Commission (Postgraduate Medical Education Board). Teachers Eligibility
Qualifications in Medical Institutions Regulations, 2022. Notification F. No. NMC/MCI-23(I)/2021-MED.,
New Delhi, 14 February 2022; published in the Gazette of India, Part III Section 4, 22 February 2022
(per the 31 March 2023 amendment notification's note). Amended 31 March 2023 (clause 12.3, foreign PG
qualifications; not relevant here).
URL FETCHED: {U['teq']}, linked from {U['rules']} as PGMEB item 5. TinyFish fetch_content, markdown,
{FETCHED}.

LICENCE / COPYRIGHT: none is stated in the Gazette text. NMC website disclaimer ({U['disc']}):
"{NMC_SITE}"

CURRENCY: SUPERSEDED on 30 June 2025 by the Medical Institutions (Qualifications of Faculty)
Regulations, 2025 (held: `nmc_miqf_2025`, block 1). Held only for the history of the requirement
("basic course in Medical Education Technology"). Do not cite for the current rule.

WHAT THIS FILE HOLDS: the title and regulations 1-2; Table 1A whole; the repeal clause. Omitted as marked.
""")

# ---------------------------------------------------------------- 8. Mahajan & Gupta 2024
f = F('mahajan_gupta_2024_gmer_cbme')
lic = q('mahajan', 'This is an open access journal, and articles are distributed', 'licensed under the identical terms.')
f.b('Licence statement (JATS XML)', 'mahajan', 'Copyright: © 2024 International Journal of Applied and Basic Medical Research', 'licensed under the identical terms.')
f.b('Introduction, Table 1, "Curriculum Regulatory Reforms" and "Roles of Indian Medical Graduate", whole',
    'mahajan', 'The National Medical Commission (NMC), established by an act of parliament',
    'hopefully, they will be notified soon.')
f.gap('Omitted: "Curriculum, Time Period, and Time Distribution" with Table 2, "Clinical Rotation" with Table 3.')
f.b('"Supplementary Examinations and Course Duration" (GMER 2019, CBME Guidelines 2023, FAQs, GMER 2023 in force)',
    'mahajan', 'Regarding Supplementary Examinations and Course Duration', 'give these clauses legal sanctity.')
f.gap('Omitted: passing criteria, examiners, conclusion, references.')
f.write(f"""MAHAJAN AND GUPTA 2024, INT J APPL BASIC MED RES — VERBATIM SOURCE PACK (EXCERPTS)
============================================================

{RULE_TXT}
[NOTE] This file's text is from JATS XML rendered to markdown by TinyFish, not a PDF text layer.

CITATION: Mahajan R, Gupta K. Periodically modified regulatory reforms for implementation of
competency-driven undergraduate medical curriculum in India: a comparative analysis. Int J Appl Basic
Med Res 2024;14(2):71-77. Editorial.
PMID: 38912356   PMCID: PMC11189270   DOI: 10.4103/ijabmr.ijabmr_205_24   (confirmed via PubMed, {FETCHED})
URL FETCHED: {U['mahajan']} (PMC open-access XML; the PMC article page returned empty content).
TinyFish fetch_content, markdown, {FETCHED}.

LICENCE AS STATED IN THE ARTICLE: "{lic}" (CC BY-NC-SA 4.0).

WHY HELD: secondary, but the one open, dated analysis found that sets GMER 1997, GMER 2019, the CBME
Guidelines 2023 and GMER 2023 side by side, compares the IMG roles (five in 2019, seven in 2023), and
states that GMER 2023 was never withdrawn. It is evidence for the currency finding in `nmc_gmer_2023`,
not a substitute for the instruments. Written April 2024, before the CBME Curriculum 2024.

WHAT THIS FILE HOLDS: the licence; the Introduction with Table 1, "Curriculum Regulatory Reforms",
"Roles of Indian Medical Graduate"; "Supplementary Examinations and Course Duration". Omitted as marked.
""")

json.dump(MANIFEST, open(os.path.join(os.path.dirname(__file__), 'manifest.json'), 'w'), indent=0)
print('built', len([m for m in MANIFEST if m[0] != 'HEADER']), 'blocks,', len([m for m in MANIFEST if m[0] == 'HEADER']), 'header quotes')
