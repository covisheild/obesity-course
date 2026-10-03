#!/usr/bin/env python3
"""Group F intake builder for S58-R1 (the Flesch Reading Ease coefficient and bands).
Every passage is cut from a saved raw fetch by raw[i:j] between anchor strings; nothing is typed by
hand. Writes sources/flesch_1948_readability_yardstick.txt and sources/flesch_1979_plain_english.txt,
and intake/raw/F-cutlog.json. Then run verify-F.py."""
import json

REPO = '/home/claude/obesity-course'
RAW = REPO + '/books/S58-R1/intake/raw/'
SRC = REPO + '/sources/'
BAR = '=' * 99
CUTLOG = []


def cut(rawfile, start, end, after=None):
    t = open(RAW + rawfile, encoding='utf-8').read()
    pos = t.index(after) if after else 0
    i = t.index(start, pos)
    assert t.count(start) == 1 or after, f'start anchor not unique in {rawfile}: {start[:40]!r}'
    j = t.index(end, i) + len(end)
    return t[i:j], i, j


class Doc:
    def __init__(self, key, title, header):
        self.key = key
        self.parts = [title, '=' * 99, ''] + header + ['']
        self.n = 0

    def block(self, heading, url):
        self.n += 1
        self.parts += ['', BAR, f'{self.n}. {heading}', url, BAR, '']

    def note(self, *lines):
        self.parts += ['[NOTE] ' + ln for ln in lines] + ['']

    def text(self, rawfile, start, end, after=None):
        s, i, j = cut(rawfile, start, end, after)
        self.parts += ['[TEXT]', s, '[END TEXT]', '']
        CUTLOG.append({'citekey': self.key, 'block': self.n, 'raw': rawfile, 'i': i, 'j': j, 'chars': j - i})

    def omit(self):
        self.parts += ['[...]', '']

    def write(self):
        open(SRC + self.key + '.txt', 'w', encoding='utf-8').write('\n'.join(self.parts).rstrip() + '\n')


RULE = [
    'Transcription rule for this file: every line between [TEXT] and [END TEXT] is an exact, unaltered',
    'slice of the text returned by the TinyFish fetch_content tool (markdown format) for the URL on the',
    'line under its block heading, cut programmatically from the saved fetch (raw[i:j]; script',
    'books/S58-R1/intake/build-F.py; offsets in books/S58-R1/intake/raw/F-cutlog.json). Nothing has been',
    'paraphrased, corrected or merged; misprints in the source are kept as they stand. [...] marks an',
    'omission. Lines beginning [NOTE] are this file\'s own annotation and are NOT source text.',
]

# ------------------------------------------------------------------------------------- Flesch 1948
F48 = 'F-flesch_1948-eric-ED506404-pdf.txt'
F48_URL = 'https://files.eric.ed.gov/fulltext/ED506404.pdf'
REC = 'F-flesch_1948-eric-ED506404-record.txt'
REC_URL = 'https://eric.ed.gov/?id=ED506404'
COPY = 'F-eric-copyright.txt'
COPY_URL = 'https://eric.ed.gov/?copyright'

# Arithmetic check on Flesch's own worked examples (Tables 4 and 7 of the article as reprinted):
# inputs (syllables per 100 words, words per sentence, printed score), both candidate coefficients.
EX = [('Table 4, New Yorker', 148, 20, 61), ('Table 4, Reader\'s Digest', 145, 16, 68),
      ('Table 7, Life', 165, 22, 46), ('Table 7, New Yorker', 145, 18, 66)]
calc = []
for lab, wl, sl, printed in EX:
    a = 206.835 - 0.846 * wl - 1.015 * sl
    b = 206.835 - 0.836 * wl - 1.015 * sl
    calc.append(f'  {lab}: wl {wl}, sl {sl}, printed {printed}; with .846 -> {a:.1f}; with .836 -> {b:.1f}')
# The untransformed formula as printed: C75 = .0846 wl + .1015 sl - 5.6835; 150 - 10*C75 gives:
assert abs((150 + 10 * 5.6835) - 206.835) < 1e-9

d = Doc('flesch_1948_readability_yardstick',
        'FLESCH 1948, "A NEW READABILITY YARDSTICK" (J APPL PSYCHOL 32:221-233), AS REPRINTED IN DUBAY (ED.), '
        'THE CLASSIC READABILITY STUDIES, ERIC ED506404 - VERBATIM SOURCE PACK', RULE + [
    '',
    'WORK: Flesch R. A new readability yardstick. J Appl Psychol 1948 Jun;32(3):221-233.',
    'PMID 18867058; DOI 10.1037/h0057532 (both confirmed with the PubMed tool, get_article_metadata, 2 Oct 2026).',
    'COPY HELD: NOT the APA original (paywalled; not fetched). The article as REPRINTED (retyped, not a',
    'facsimile) in: DuBay WH, editor. The Classic Readability Studies. Costa Mesa (CA): Impact Information;',
    '2007 (ERIC record date 2007-Mar-10; the PDF\'s copyright page says "Introductions (c) 2006"). ERIC',
    'ED506404, 118 pages. The article occupies the reprint\'s pp. 99-111 (the reprint\'s own page numbers,',
    'which appear in the text stream), under its own heading "Journal of Applied Psychology / Vol. 32, No.',
    '3 ... June, 1948 / A New Readability Yardstick* / Rudolf Flesch". The 1948 page numbers 221-233 are',
    'NOT shown in the reprint, so a page pin-cite to the original cannot be made from this copy.',
    'TEXT FETCHED FROM: ' + F48_URL + ' (PDF text layer, via TinyFish fetch_content, markdown),',
    'and the ERIC record page ' + REC_URL + ' and ERIC\'s copyright page ' + COPY_URL + ', all 2 Oct 2026.',
    'eric.ed.gov/robots.txt: "User-agent: * / Disallow:" (nothing excluded); files.eric.ed.gov has no',
    'robots.txt (404).',
    'LICENCE / COPYRIGHT AS STATED: ERIC record abstract (block 1): "The articles reprinted here (all in',
    'the public domain) are the following: ... \'A New Readability Yardstick\' by Rudolf Flesh [sic],',
    'published June, 1948, in Journal of Applied Psychology ...". PDF copyright page (block 3) lists the',
    'reprinted articles and says "Introductions (c) 2006 William H. DuBay. All Rights Reserved." ERIC\'s',
    'copyright page (block 2): authors or publishers retain copyright to works in ERIC, "used by ERIC',
    'with permission". The public-domain status of the 1948 article is DuBay\'s statement as recorded by',
    'ERIC; this file has not verified it. DuBay\'s introduction (block 4) is his own copyright work: brief',
    'quotation only.',
    '',
    'WHO IS SPEAKING: block 5 is FLESCH\'S OWN WORDS (the 1948 article, as retyped by DuBay). Block 4 is',
    'DUBAY\'S introduction (a RESTATEMENT, with his own updated formula and two tables he attributes to',
    'Flesch\'s 1949 books). Do not attribute block 4 wording to Flesch.',
    '',
    'COEFFICIENT (the reason this file was filed). Flesch 1948 gives the syllable coefficient as .846 per',
    'syllable-per-100-words, i.e. 84.6 per syllable-per-word, NOT .836 / 83.6:',
    '  - Formula A in Findings: "RE = 206.835 - .846 wl - 1.015 sl", with wl defined as "word length',
    '    (syllables per 100 words)" and sl as "sentence length in words";',
    '  - restated in "The Formulas Restated", Step 7: "R.E. ("reading ease") - 206.835 - .846 wl - 1.015',
    '    sl" (the reprint has "-" where "=" is meant: a retyping slip);',
    '  - the untransformed regression as printed: "C75 = .0846 wl + .1015 sl - 5.6835". Multiplying by -10',
    '    and adding 150 (so that predicted grade 5, i.e. fourth grade completed, scores 100, as the article',
    '    explains) gives 206.835 - .846 wl - 1.015 sl exactly. The .0846, the .846 and the 206.835 are',
    '    therefore mutually consistent, which makes a retyping error in .846 very unlikely.',
    '  - Flesch\'s own worked scores (Tables 4 and 7) recomputed by build-F.py from the printed inputs:',
] + calc + [
    '    Three of four reproduce the printed score with .846 and none with .836; Life (inputs rounded in',
    '    the table) falls between. (This file\'s arithmetic, not the source\'s.)',
    'DuBay\'s own introduction (block 4) restates the "updated" formula as 84.6 x ASW (syllables per word).',
    'CONSEQUENCE FOR C10: the ".836 (syllables/100 words)" in Kincaid et al. 1975 Table 3 (held,',
    'kincaid_1975_readability; the page image shows .836) does not match the coefficient Flesch published.',
    'It is best treated as a misprint in the Kincaid report. Residual caveat: this is a retyped reprint, not',
    'the APA page image; the arithmetic above is what closes the question, not the reprint alone.',
    '',
    'BANDS. Flesch 1948 Table 5 "Pattern of "Reading Ease" Scores" (score, description of style, typical',
    'magazine, syllables per 100 words, average sentence length) is in block 5. As reprinted its first row',
    'reads "0 to 20 Very Difficult", leaving 20-30 unassigned; the next row starts at 30. DuBay\'s',
    'introduction (block 4) gives "0 to 30" for Very Difficult in both tables he takes from Flesch 1949, and',
    'Flesch 1979 (flesch_1979_plain_english) gives "0 to 30" for "college graduate". "0 to 20" is probably',
    'a retyping slip, but this copy cannot prove it: a book should either cite the band as 0-30 from',
    'Flesch 1979 / DuBay, or say the reprint prints 0-20. DuBay\'s 1949 "Art of Readable Writing" table',
    'in block 4 also has a misprinted row ("30 to 40" for Difficult; his Table 1 below it has "30 to 50").',
    '',
    'EXTRACTION ARTEFACTS: the reprint\'s page numbers (96-111) and running heads ("The Classic',
    'Readability Studies  1948-The Flesch Formulas") run into the text; drop caps are lost ("N 1943" for',
    '"In 1943"; a stray "I" or "T"); words are hyphenated at line ends ("syl-" / "lables"). Tables are',
    'flattened: Tables 1-2 and 4-7 keep their rows, DuBay\'s 1949 table in block 4 is split into columns.',
    'Some retyping slips are visible ("35.58.22" in Table 2; "H.L" for H.I.; "314 ps" where Formula B',
    'earlier reads ".314 ps"; "Table 6 / Pattern of "Reading Ease" Scores" over the human-interest table;',
    '"cm" for C50). Quote with care and never silently correct.',
    '',
    'WHAT IS HELD: block 1 ERIC record (abstract); block 2 ERIC copyright statement; block 3 the reprint\'s',
    'copyright page; block 4 DuBay\'s introduction to the Flesch article (pp. 96-98) whole; block 5 the',
    'Flesch 1948 article whole, from its heading to "Received November 3, 1947." NOT HELD: the article\'s',
    'reference list (20 items) and every other part of the 118-page book.',
])

d.block('ERIC record for ED506404: bibliographic fields and abstract (the public-domain statement)', REC_URL)
d.text(REC, 'ERIC Number: ED506404', 'pp. 221-233.')
d.note('The record continues with descriptors and ERIC metadata, not held.')

d.block('ERIC Content Disclaimers: copyright paragraph', COPY_URL)
d.text(COPY, 'The ERIC website contains full-text resources',
       'cannot grant permission to use indexed works under copyright protection.')

d.block('The Classic Readability Studies, copyright page (PDF p. ii)', F48_URL)
d.text(F48, 'Copyright', 'All Rights Reserved.')
d.note('The list on this page omits the Thorndike, Ojemann and Dale-Tyler reprints that the ERIC abstract',
       'names; it is reproduced as it stands.')

d.block('DuBay\'s introduction, "1948 - The Flesch Formulas" (reprint pp. 96-98). DUBAY\'S WORDS, NOT FLESCH\'S', F48_URL)
d.text(F48, '1948— The Flesch Formulas', '—WHD')
d.note('84.6 x ASW here is DuBay\'s restatement of "the updated Flesch Reading Ease score" (per syllable per',
       'word). The two tables are DuBay\'s renderings of tables he attributes to Flesch\'s 1949 books; the first',
       'is extracted column by column (scores, then descriptions, then grades, then percentages). Its row',
       '"30 to 40" is a misprint for 30 to 50 (the second table has "30 to 50"). The "1976" Navy study is',
       'Kincaid et al., dated February 1975 on its own title page.')

d.block('Flesch R, "A New Readability Yardstick", J Appl Psychol 1948;32(3):221-233, as reprinted (pp. 99-111). FLESCH\'S OWN WORDS', F48_URL)
d.text(F48, 'Journal of Applied Psychology \nVol. 32', 'Received November 3, 1947.')
d.omit()
d.note('Omitted: the article\'s reference list (items 1-20), which follows "Received November 3, 1947."')
d.note('Where the coefficient is: "Formula A (for predicting "reading ease"): RE = 206.835 - .846 wl -',
       '1.015 sl." (Findings, reprint p. 103); "C75 = .0846 wl + .1015 sl - 5.6835" (same paragraph); Step 7',
       'of "The Formulas Restated" (p. 107). wl = syllables per 100 words. Bands: Table 5 (p. 108).',
       '(Typographic minus signs rendered here as hyphens in this NOTE only; the [TEXT] keeps the source\'s.)')
d.write()

# ------------------------------------------------------------------------------------- Flesch 1979
NYU = 'F-flesch_1979-nyustern.txt'
NYU_URL = 'https://pages.stern.nyu.edu/~wstarbuc/Writing/Flesch.htm'
IDX = 'F-nyustern-writing-index.txt'
IDX_URL = 'https://pages.stern.nyu.edu/~wstarbuc/Writing/'
CAN = 'F-flesch_1979-canterbury-wayback.txt'
CAN_URL = 'https://web.archive.org/web/2016/http://www.mang.canterbury.ac.nz/writing_guide/writing/flesch.shtml'

e = Doc('flesch_1979_plain_english',
        'FLESCH 1979, HOW TO WRITE PLAIN ENGLISH, CHAPTER 2 "LET\'S START WITH THE FORMULA" - VERBATIM SOURCE PACK',
        RULE + [
    '',
    'WORK: Flesch R. How to Write Plain English: A Book for Lawyers and Consumers. 1979. Chapter 2, "Let\'s',
    'Start With the Formula". (Subtitle and year as DuBay gives them in flesch_1948_readability_yardstick',
    'block 4, "How to Write in Plain English: A Book for Lawyers and Consumers (1979)"; the publisher,',
    'Harper & Row, New York, is NOT stated on either fetched page and is given from general knowledge: confirm',
    'before citing.) The fetched pages give no page numbers.',
    'COPIES HELD: (a) the chapter as reproduced on William H. Starbuck\'s NYU Stern faculty pages, listed',
    'there as ""How To Write Plain English" by Rudolf Flesch" among readings on writing (blocks 1-2);',
    '(b) the University of Canterbury (NZ) Department of Management "Guide to Academic Writing" copy of the',
    'same chapter, the one most papers cite (mang.canterbury.ac.nz/writing_guide/writing/flesch.shtml), now',
    'offline; fetched as the Internet Archive snapshot of 12 Jan 2017',
    '(https://web.archive.org/web/20170112043649/http://www.mang.canterbury.ac.nz/writing_guide/writing/flesch.shtml)',
    '(block 3, the formula and grade table only, to corroborate (a)). The two copies match word for word',
    'apart from two trivial differences (a space after "mis-"; list markers in the example sentence).',
    'Both are retyped web transcriptions, not page images (e.g. "simpie. short", "11/2" for 1 1/2).',
    'The chart (nomogram) the chapter refers to is not on either page.',
    'FETCHED 2 Oct 2026, TinyFish fetch_content (markdown). pages.stern.nyu.edu/robots.txt disallows only',
    '/~tang/aboutus/recruiters/; the Wayback page was a single fetch.',
    'LICENCE AS STATED: none. Neither page carries a licence or copyright line. The book is a commercially',
    'published work, presumably still in copyright; these pages are third-party educational reproductions',
    'whose permission status is not stated. Hold for private study; quote briefly, with attribution to the',
    'book, never to the web page as author.',
    '',
    'WHO IS SPEAKING: FLESCH\'S OWN WORDS (first person: "I developed the formula in the early 1940s").',
    '',
    'COEFFICIENT: 84.6, per syllable per word: "Multiply the average sentence length by 1.015. Multiply the',
    'average word length by 84.6. Add the two numbers. Subtract this sum from 206.835. The balance is your',
    'readability score." (Average word length = syllables divided by words, Step 4.) This is the same',
    'formula as Flesch 1948\'s ".846 wl" with wl in syllables per 100 words. It does NOT support Kincaid',
    '1975\'s .836.',
    'BANDS (Flesch\'s own, 1979 form): scores to school level: 90-100 5th grade; 80-90 6th; 70-80 7th; 60-70',
    '8th and 9th; 50-60 10th to 12th (high school); 30-50 college; 0-30 college graduate. Also: "Zero means',
    'practically unreadable and 100 means extremely easy"; "The minimum score for Plain English is 60";',
    'worked sentences scoring 92 ("very easy"), 67 ("Plain English") and 32 ("difficult"); scores for 19',
    'publications, from comics (92) to the Internal Revenue Code (minus 6). The 1979 chapter does NOT give',
    'the "very easy ... very difficult" description column as a table; that is Flesch 1948 Table 5.',
    'EXTRACTION ARTEFACTS: the two tables are flattened to one cell per line with blank lines between.',
    '',
    'WHAT IS HELD: the whole chapter as the NYU page gives it (block 2); the NYU listing line (block 1); the',
    'Canterbury snapshot\'s title lines and its formula-to-grade-table run (block 3). Nothing else of the',
    'book.',
])

e.block('NYU Stern, W. H. Starbuck\'s writing readings: the listing line', IDX_URL)
e.text(IDX, '"How To Write Plain English" by Rudolf Flesch', '"How To Write Plain English" by Rudolf Flesch')

e.block('Flesch 1979, How to Write Plain English, Chapter 2, whole, as reproduced on the NYU Stern page', NYU_URL)
e.text(NYU, 'HOW TO WRITE PLAIN ENGLISH', "can't be translated into Plain English.")

e.block('The same chapter, University of Canterbury copy (Wayback snapshot 2017-01-12): title lines', CAN_URL)
e.text(CAN, '# How to Write Plain English', "## Chapter 2: Let's Start With the Formula")
e.omit()
e.note('Omitted: the chapter text from its first paragraph to Step 6, identical to block 2 but for the two',
       'trivial differences named in the header.')
e.text(CAN, 'You can also use this formula', 'college graduate')
e.omit()
e.note('Omitted: the two closing tips, identical to block 2.')
e.write()

json.dump(CUTLOG, open(RAW + 'F-cutlog.json', 'w'), indent=1)
for c in CUTLOG:
    print(c)
