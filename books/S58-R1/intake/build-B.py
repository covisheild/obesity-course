#!/usr/bin/env python3
"""Group B intake builder for S58-R1. Every passage is cut from a saved raw fetch by raw[i:j];
nothing is typed by hand. Run, then run check_B.py."""
import re, json, sys

REPO = '/home/claude/obesity-course'
RAW = REPO + '/books/S58-R1/intake/raw/'
SRC = REPO + '/sources/'
BAR = '=' * 79
LOG = []  # (citekey, block, kind, rawfile, i, j)


def cut(rawfile, start, end, occ=1, after=None):
    t = open(RAW + rawfile, encoding='utf-8').read()
    pos = 0
    if after:
        pos = t.index(after)
    i = pos - 1
    for _ in range(occ):
        i = t.index(start, i + 1)
    j = t.index(end, i) + len(end)
    s = t[i:j]
    return s, i, j


def wrap(lines, width=99):
    out = []
    for ln in lines:
        out.append(ln)
    return out


class Doc:
    def __init__(self, key, title, header):
        self.key, self.parts, self.n = key, [title, '=' * 60, ''] + header + [''], 0
        self.passages = []

    def block(self, heading, url):
        self.n += 1
        self.parts += ['', BAR, f'{self.n}. {heading}', url, BAR, '']

    def note(self, *lines):
        for ln in lines:
            self.parts.append('[NOTE] ' + ln)
        self.parts.append('')

    def omit(self):
        self.parts += ['[...]', '']

    def prose(self, rawfile, start, end, **kw):
        s, i, j = cut(rawfile, start, end, **kw)
        assert '"' not in s[-1:], 'ends with quote'
        if '<p>' in s or '</p>' in s or 'Statistical Analyses and Methods in the Published Literature: the SAMPL' in s:
            raise SystemExit(f'page tag inside passage {self.key}: {start[:40]}')
        self.parts += ['"' + s + '"', '']
        self.passages.append(('prose', rawfile, s))
        LOG.append((self.key, self.n, 'prose', rawfile, i, j))

    def table(self, rawfile, start, end, **kw):
        s, i, j = cut(rawfile, start, end, **kw)
        self.parts += ['[TABLE]', s, '[END TABLE]', '']
        self.passages.append(('table', rawfile, s))
        LOG.append((self.key, self.n, 'table', rawfile, i, j))

    def mathml(self, rawfile, start, end, **kw):
        s, i, j = cut(rawfile, start, end, **kw)
        self.parts += ['[MATHML]', s, '[END MATHML]', '']
        self.passages.append(('mathml', rawfile, s))
        LOG.append((self.key, self.n, 'mathml', rawfile, i, j))

    def raw_lines(self, *lines):
        self.parts += list(lines) + ['']

    def write(self):
        txt = '\n'.join(self.parts).rstrip() + '\n'
        open(SRC + self.key + '.txt', 'w', encoding='utf-8').write(txt)
        json.dump([(k, r, s) for k, r, s in self.passages],
                  open(RAW + 'B-' + self.key + '-passages.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        return txt


RULE = [
    'Transcription rule for this file: every line beneath a block heading that is not prefixed',
    'with [NOTE] and is not inside a NOT OBTAINED record is an exact, unaltered slice of the text',
    'returned by the TinyFish fetch_content tool for the URL in that heading, cut programmatically',
    'from the saved fetch (raw[i:j]); nothing has been paraphrased, smoothed or merged. Prose',
    'passages are set in double quotation marks (the marks are this file\'s, not the source\'s).',
    'Tables are set between [TABLE] and [END TABLE] and keep the line breaks the extraction',
    'produced; MathML is set between [MATHML] and [END MATHML]. Where text is left out, the',
    'omission is marked [...] in place. Lines beginning [NOTE] are this file\'s own annotation',
    'and are NOT source text.',
    '',
]

# ---------------------------------------------------------------- Cole 2015
COLE_MD = 'B-cole_2015_too_many_digits-pmcxml.txt'
COLE_HT = 'B-cole_2015_too_many_digits-pmcxml-html.txt'
COLE_URL = 'https://pmc-oa-opendata.s3.amazonaws.com/PMC4483789.1/PMC4483789.1.xml'
d = Doc('cole_2015_too_many_digits', 'COLE 2015, ARCHIVES OF DISEASE IN CHILDHOOD, "TOO MANY DIGITS" — VERBATIM SOURCE PACK', RULE + [
    'CITATION: Cole TJ. Too many digits: the presentation of numerical data. Arch Dis Child',
    '2015;100(7):608-609.',
    'PMID: 25877157   PMCID: PMC4483789   DOI: 10.1136/archdischild-2014-307149   (confirmed via',
    'PubMed, 2026-10-02)',
    'TEXT FETCHED FROM: ' + COLE_URL,
    '(PMC open-access JATS XML; TinyFish fetch_content, markdown format for the text, and a second',
    'fetch of the same URL in html format, used only for the [NOTE]s on Table 1\'s markup), 2026-10-02.',
    'This is the publisher\'s article as deposited in PMC (pmc-prop-manuscript: no).',
    'LICENCE AS STATED IN THE ARTICLE (block 1): "This is an Open Access article distributed in',
    'accordance with the terms of the Creative Commons Attribution (CC BY 4.0) license ..." (CC BY 4.0).',
    '',
    'WHAT THIS FILE HOLDS: the licence and copyright lines; the WHOLE body text of the article (one',
    'continuous passage, from the opening Amadeus quotation to the paragraph introducing Table 1);',
    'Table 1 "Rounding rules for summary statistics" in full as the extraction gives it; and the',
    'closing sentence. Omitted: the reference list, the competing-interests and provenance lines.',
    'The article has no abstract.',
    'EXTRACTION ARTEFACTS (read before quoting): reference callouts are superscripts in the',
    'article and run into the text here as bare digits ("presentation of numerical data.1",',
    '"(Goldilocks rounding).2", "2–3 effective digits”.3", "change of medication.4", the "3\\n12"',
    'after "measures of variability."). Never quote such a digit as part of a number.',
])
d.block('Licence and copyright lines (PMC XML front matter)', COLE_URL)
d.prose(COLE_MD, 'Published by the BMJ Publishing Group Limited.', 'rights-licensing/permissions')
d.prose(COLE_MD, 'This is an Open Access article distributed', 'See: http://creativecommons.org/licenses/by/4.0/')
d.block('Whole body text (opening quotation to the paragraph introducing Table 1)', COLE_URL)
d.note('One continuous slice. Superscript reference numbers appear as bare digits (see header).',
       'Key passages inside it: the definitions of decimal places and significant digits; the EASE',
       'rule "2–3 effective digits"; the OR 22.68 (7.51 to 73.67) worked example; birth weight in g',
       'vs kg; the rule of four; the percentage rule ("if the range is 10% or more use whole',
       'numbers ..."); "intermediate calculations are carried out to full precision"; and the general',
       'principle "two or three significant digits for effect sizes, and one or two significant',
       'digits for measures of variability".')
d.prose(COLE_MD, 'Emperor Joseph II: My dear young man', 'the pervasive problem of reporting too many digits.')
d.block('Table 1. Rounding rules for summary statistics', COLE_URL)
d.note('How to read this table: in the PMC XML each statistic\'s FIRST example sits in its own row;',
       'its further examples follow as one-cell rows (e.g. after "Mean ... | 3320 g |" comes "| 3.32 kg |",',
       'which is the second example for Mean, not a new statistic). The markdown keeps that structure.',
       'Two markup losses, checked against the html fetch of the same XML: the third test-statistic',
       'example is "χ<sup>s</sup>=4.1" in the XML (so "χs=4.1" here; the row label is "χ<sup>2</sup>");',
       'the last p value example is "6.10<sup>−9</sup>" (so "6.10−9" here: 6 x 10 to the power -9).')
d.table(COLE_MD, 'Table\xa01Rounding rules for summary statistics', '| 6.10−9 |')
d.block('Closing sentence', COLE_URL)
d.prose(COLE_MD, 'Fortunately for us, Emperor Joseph', 'which digits they can ditch.')
d.raw_lines(BAR, 'OMITTED: reference list (13 entries), competing interests, provenance. Not needed by the', 'inventory; reference 2 is Lang and Altman\'s SAMPL guidelines, filed separately.', BAR)
COLE = d.write()

# ---------------------------------------------------------------- Plaven-Sigray 2017
PS_MD = 'B-plavensigray_2017_readability-pmcxml.txt'
PS_HT = 'B-plavensigray_2017_readability-pmcxml-html.txt'
PS_URL = 'https://pmc-oa-opendata.s3.amazonaws.com/PMC5584989.1/PMC5584989.1.xml'
d = Doc('plavensigray_2017_readability', 'PLAVÉN-SIGRAY ET AL. 2017, eLIFE, READABILITY OF SCIENTIFIC TEXTS — VERBATIM SOURCE PACK (EXCERPTS)', RULE + [
    'CITATION: Plavén-Sigray P, Matheson GJ, Schiffler BC, Thompson WH. The readability of',
    'scientific texts is decreasing over time. eLife 2017;6:e27725.',
    'PMID: 28873054   PMCID: PMC5584989   DOI: 10.7554/eLife.27725   (confirmed via PubMed, 2026-10-02)',
    'TEXT FETCHED FROM: ' + PS_URL,
    '(PMC open-access JATS XML; TinyFish fetch_content, markdown for the prose and tables; html',
    'format of the same URL for the MathML of the FRE formula), 2026-10-02.',
    'LICENCE AS STATED IN THE ARTICLE (block 1): "This article is distributed under the terms of the',
    'Creative Commons Attribution License, which permits unrestricted use and redistribution',
    'provided that the original author and source are credited." The XML links',
    'https://creativecommons.org/licenses/by/4.0/ (CC BY 4.0).',
    '',
    'WHAT THIS FILE HOLDS: EXCERPTS, not the whole article. Licence; abstract; author impact',
    'statement; the first two paragraphs of the Introduction; from Results, the yearly-trend',
    'paragraph, the mixed-model paragraph with Table 1, the abstract/full-text paragraph, and the',
    'two hypothesis tests with Table 2; the WHOLE Discussion; from Materials and methods, the',
    'Language preprocessing paragraph and the FRE part of "Language and readability metrics" (with',
    'the FRE formula as MathML). Omitted: figure and table-supplement captions, journal selection,',
    'the New Dale-Chall formula and the word-list construction, statistical methods, references.',
    'Absence of a passage from this file is not absence from the article.',
    'EXTRACTION ARTEFACTS: exponents are flattened. "p <10-15" is p < 10 to the power -15. In the',
    'markdown the FRE formula reads "FRE=206.835−1.015(wordssentences)−84.6(syllableswords)" because',
    'the fractions are flattened; block 9 holds the MathML, which shows words/sentences and',
    'syllables/words as fractions.',
])
d.block('Licence statement (PMC XML front matter)', PS_URL)
d.prose(PS_MD, '© 2017, Plavén-Sigray et al', '© 2017, Plavén-Sigray et al')
d.prose(PS_MD, 'This article is distributed under the terms', 'original author and source are credited.')
d.block('Abstract and author impact statement', PS_URL)
d.prose(PS_MD, 'Clarity and accuracy of reporting are fundamental', 'accessibility of research findings.')
d.prose(PS_MD, 'Scientific abstracts have become less readable', 'than older texts.')
d.block('Introduction, paragraphs 1-2', PS_URL)
d.prose(PS_MD, 'Reporting science clearly and accurately', 'or a high NDC score (Figure 1A).')
d.block('Results: yearly trend in FRE and NDC and their components', PS_URL)
d.prose(PS_MD, 'The primary research question was', 'p <10-15) (Figure 2E).')
d.block('Results: mixed-effects model, Table 1', PS_URL)
d.prose(PS_MD, 'The readability of individual abstracts was formally', '(Figure 3—figure supplement 1).')
d.note('Figure 3 caption and its source-data and supplement lines omitted.')
d.omit()
d.table(PS_MD, '10.7554/eLife.27725.007Table', '| M2 | 0 | 0 | 0.016 | [0.015, 0.018] | 20.5 | 117 | p <10-15 |')
d.note('Rows under "FRE" and "NDC" continue that metric: the second and third rows of each group',
       'are M1 and M2 for the metric named in the row above them.')
d.block('Results: abstracts against full texts', PS_URL)
d.prose(PS_MD, 'To verify that the readability of abstracts', 'generalizes to the full texts.')
d.block('Results: the two hypotheses (number of authors; general scientific jargon), Table 2', PS_URL)
d.prose(PS_MD, 'There could be a number of explanations', "(i.e. a 'science-ese').")
d.note('Figure 5 caption and supplement omitted.')
d.omit()
d.prose(PS_MD, 'To test the first hypothesis, we divided', 'does decrease with more authors.')
d.table(PS_MD, '10.7554/eLife.27725.018Table', '| Authors | 0.008 | [0.007, 0.008] | 40.3 | 701014 | p <10-15 |')
d.prose(PS_MD, 'To test the second hypothesis, we constructed', 'accounts for the decreasing readability.')
d.block('Discussion (whole)', PS_URL)
d.note('Holds: "A FRE score of 100 is designed to reflect the reading level of a 10- to 11-year old.',
       'A score between 0 and 30 is considered understandable by college graduates"; 14% (1960) and 22%',
       '(2015) of abstracts with FRE below 0; the limits of readability formulas ("Changing a text',
       'solely to improve readability scores does not automatically make a text more understandable").')
d.prose(PS_MD, 'From analyzing over 700,000 abstracts', 'emphasize clarity in their writing.')
d.block('Materials and methods: Language preprocessing; Language and readability metrics (FRE part)', PS_URL + '  (MathML: same URL, html format)')
d.note('Journal selection section omitted.')
d.omit()
d.prose(PS_MD, 'Abstracts downloaded from PubMed were preprocessed', 'Sentences containing only one word were ignored.')
d.note('Heuristic-rules paragraph omitted.')
d.omit()
d.prose(PS_MD, 'Two well-established readability measures were used', 'compares well with more recent methods for analyzing readability (Benjamin, 2012).')
d.prose(PS_MD, 'Counting the syllables of a word', 'counting the number of periods in the preprocessed abstracts.')
d.note('Paragraph on the NDC difficult-word list omitted.')
d.omit()
d.prose(PS_MD, 'FRE uses both the average number of syllables', 'to estimate the reading level.')
d.mathml(PS_HT, '<disp-formula><mml:math><mml:mstyle><mml:mrow><mml:mstyle><mml:mi>F</mml:mi>', '</disp-formula>')
d.note('Plain-text rendering of the MathML above (this file\'s notation, made by reading mn/mo/mtext',
       'in order and writing mfrac as (numerator/denominator)): FRE = 206.835 − 1.015 (words/sentences)',
       '− 84.6 (syllables/words)')
d.prose(PS_MD, "where 'words', 'sentences' and 'syllables' entail", 'the number of each in the text, respectively.')
d.note('NDC paragraph and formula, and the rest of Materials and methods, omitted.')
PS = d.write()

# ---------------------------------------------------------------- Lang & Altman SAMPL (EQUATOR PDF)
SA = 'B-lang_altman_2013_sampl-pdf.txt'
SA_URL = 'https://www.equator-network.org/wp-content/uploads/2013/07/SAMPL-Guidelines-6-27-13.pdf'
d = Doc('lang_altman_2013_sampl', 'LANG AND ALTMAN, THE SAMPL GUIDELINES (EQUATOR NETWORK PDF, 2013) — VERBATIM SOURCE PACK (EXCERPTS)', RULE + [
    'WHAT THE DOCUMENT IS: Lang T, Altman D. "Basic Statistical Reporting for Articles Published in',
    'Biomedical Journals: The "Statistical Analyses and Methods in the Published Literature" or The',
    'SAMPL Guidelines", the 9-page PDF the EQUATOR Network links as "Download the SAMPL Guidelines',
    '(PDF)". Its page-1 footnote cites it as published in Smart P, Maisonneuve H, Polderman A (eds).',
    'Science Editors\' Handbook, European Association of Science Editors, 2013.',
    'JOURNAL VERSION, NOT HELD: Lang TA, Altman DG. Int J Nurs Stud 2015;52(1):5-9, PMID 25441757,',
    'DOI 10.1016/j.ijnurstu.2014.09.006 (confirmed via PubMed, 2026-10-02). That version was not',
    'opened; this file does not show that its wording matches the PDF below.',
    'EQUATOR LIBRARY PAGE (read for the link, 2026-10-02): https://www.equator-network.org/reporting-guidelines/sampl/',
    'TEXT FETCHED FROM: ' + SA_URL,
    '(the PDF\'s text layer, via TinyFish fetch_content, markdown format), 2026-10-02. No passage',
    'below crosses a PDF page (each page begins with the running header "Lang T, Altman D.',
    'Statistical Analyses and Methods in the Published Literature: the SAMPL Guidelines." and its',
    'page number; none is inside a passage).',
    'LICENCE / TERMS AS STATED: the PDF (block 1): "This document may be reprinted without charge',
    'but must include the original citation." EQUATOR\'s terms of use (www.equator-network.org/',
    'terms-of-use/, read 2026-10-02): "The materials contained in the site may be downloaded or',
    'copied provided that ALL copies retain the copyright and any other proprietary notices',
    'contained on the materials." No CC licence is stated.',
    '',
    'WHAT THIS FILE HOLDS: EXCERPTS. The title and authors; the reprint statement; the two guiding',
    'principles; "General Principles for Reporting Statistical Results": the whole of "Reporting',
    'numbers and descriptive statistics" and "Reporting risk, rates, and ratios"; and the whole of',
    '"Reporting hypothesis tests" (P values to one or two decimal places; P <0.001 as the smallest).',
    'Omitted: the introduction, the methods principles, the sections on association, correlation,',
    'regression, ANOVA, survival and Bayesian analyses, the references.',
    'EXTRACTION ARTEFACTS: the PDF is two-column; line breaks are the PDF\'s, each followed by a space.',
    'Bullets are "•". Reference callouts are in square brackets as printed. A first fetch of the',
    'same PDF in html format (raw kept) encoded "<" and the apostrophe as entities, so the markdown',
    'fetch is the one quoted.',
])
d.block('Title, authors and reprint statement (PDF page 1)', SA_URL)
d.prose(SA, 'Basic Statistical Reporting for  \nArticles Published', 'b Director, Centre for Statistics in Medicine, Oxford University')
d.note('"Langa" and "Altmanb": the affiliation marks a and b are superscripts in the PDF.',
       'The Esquirol epigraph and the opening of the Introduction are omitted here; the reprint',
       'statement below is the page-1 footnote, which the text layer places mid-column.')
d.omit()
d.prose(SA, 'Lang T, Altman D. Basic statistical reporting for \narticles', 'include the original citation.')
d.block('Guiding principles (PDF page 3)', SA_URL)
d.prose(SA, 'Guiding Principles for Reporting Statistical Methods and Results', 'usually a 95% confidence interval.')
d.note('"General Principles for Reporting Statistical Methods" (preliminary, primary and supplementary',
       'analyses) omitted.')
d.omit()
d.block('General Principles for Reporting Statistical Results: numbers and descriptive statistics; risk, rates and ratios (PDF page 4)', SA_URL)
d.prose(SA, 'General Principles for Reporting Statistical Results \nReporting numbers', 'ratios.')
d.block('Reporting hypothesis tests (PDF page 5)', SA_URL)
d.prose(SA, 'Reporting hypothesis tests \n', 'Name the statistical software package used in the \nanalysis.')
d.note('Sections on association, correlation, regression, ANOVA/ANCOVA, survival and Bayesian',
       'analyses, and the references, omitted.')
SAMPL = d.write()

# ---------------------------------------------------------------- Edwards 2022 (fallback for the FRE scale and FKGL formula)
ED = 'B-edwards_2022_readability_formulas-pmcxml.txt'
ED_URL = 'https://pmc-oa-opendata.s3.amazonaws.com/PMC9479524.1/PMC9479524.1.xml'
d = Doc('edwards_2022_readability_formulas', 'EDWARDS ET AL. 2022, SURGICAL NEUROLOGY INTERNATIONAL — FALLBACK FOR THE FLESCH FORMULAS AND THE READING-EASE SCALE — VERBATIM SOURCE PACK (EXCERPTS)', RULE + [
    'WHY THIS FILE EXISTS: FALLBACK ONLY. Kincaid et al. 1975 (the Navy report that states the',
    'Flesch Reading Ease and Flesch-Kincaid grade formulas) could not be opened from the session (see',
    'books/S58-R1/intake/log-B.md), and Flesch 1948 is Harsh-only. This open article restates both',
    'formulas and the Reading Ease interpretation bands, citing Flesch 1948 (its ref. 10) and Kincaid',
    'et al. 1975 (its ref. 15). It is a SECONDARY restatement: the bands and coefficients below have',
    'not been checked against Flesch 1948 or Kincaid 1975. Cite it as what this paper states, or',
    'replace it when Harsh supplies Kincaid 1975.',
    'CITATION: Edwards CS, Ammanuel SG, Silva ONN, Greeneway GP, Bunch KM, Meisner LW, Page PS,',
    'Ahmed AS. Academics versus the Internet: Evaluating the readability of patient education',
    'materials for cerebrovascular conditions from major academic centers. Surg Neurol Int',
    '2022;13:401.',
    'PMID: 36128118   PMCID: PMC9479524   DOI: 10.25259/SNI_502_2022   (confirmed via PubMed, 2026-10-02)',
    'TEXT FETCHED FROM: ' + ED_URL + ' (PMC OA JATS XML; TinyFish fetch_content, markdown), 2026-10-02.',
    'LICENCE AS STATED IN THE ARTICLE (block 1): Creative Commons Attribution-Non Commercial-Share',
    'Alike 4.0 (CC BY-NC-SA 4.0).',
    '',
    'WHAT THIS FILE HOLDS: EXCERPTS. Licence; the Introduction paragraph with the Reading Ease scale;',
    'the Methods paragraph giving both formulas in words; reference entries 10 and 15 as the',
    'extraction gives them (run together). Everything else omitted, including all results.',
    'CAUTION: the article cites FKGL to "[10,13]"; its ref. 13 is Karliner et al. on language',
    'barriers, so that callout looks mistaken. Do not cite this paper for who derived FKGL.',
    'Why this paper and not another: of ten open PMC readability papers opened, it is the one that',
    'gives both formulas in prose with 15.59 (one other gives 15.39, another 1015 for 1.015) AND the',
    'full seven-band scale.',
])
d.block('Licence statement (PMC XML front matter)', ED_URL)
d.prose(ED, 'This is an open-access article distributed under the terms', 'licensed under the identical terms.')
d.block('Introduction, paragraph 3: the grade-level recommendation, FKGL and FRE, the FRE bands', ED_URL)
d.prose(ED, 'The National Institute of Health (NIH) recommends', '30–0 “very difficult.”[10]')
d.block('Materials and methods: the two formulas', ED_URL)
d.prose(ED, 'All documents were assessed using plain text', '− 84.6 × (syllables/words).')
d.note('Rest of the paragraph (reliability of the two examiners) and the rest of the article omitted.')
d.block('Reference entries 10 and 15 (run together by the extraction)', ED_URL)
d.prose(ED, '10FleschRA new readability yardstick', '10.1037/h0057532')
d.prose(ED, '15KincaidJPFishburneRPJr', 'Research Branch Report197587516')
d.note('As extracted, the fields run together with no separators. Ref. 10 reads as Flesch R, "A new',
       'readability yardstick", J Appl Psychol, then the digits 1948 32 221 33 18867058 (year, volume,',
       'pages, PMID) and the DOI. Ref. 15 reads as Kincaid JP, Fishburne RP Jr, Rogers RL, Chissom BS, a',
       'title with words missing, "Research Branch Report", then "197587516": plausibly 1975, 8-75, and',
       '16 (the number of the next entry). Whether the missing words are the article\'s or the',
       'extraction\'s is not known. This reading is the file\'s, not the source\'s.')
ED_T = d.write()

json.dump(LOG, open(RAW + 'B-cutlog.json', 'w'), indent=0)
print('written; passages:', len(LOG))
for k in ['cole_2015_too_many_digits', 'plavensigray_2017_readability', 'lang_altman_2013_sampl', 'edwards_2022_readability_formulas']:
    print(k, sum(1 for x in LOG if x[0] == k))
