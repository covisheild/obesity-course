#!/usr/bin/env python3
"""Group R2 intake builder for S58-R1 (referencing: NLM Citing Medicine, 2nd ed., chapters 4, 22 and 25: reports, Internet books/reports, web sites).
Every passage is cut from a saved raw fetch by raw[i:j] between anchor strings; nothing is typed by hand.
Writes sources/nlm_citing_medicine_2007_reports_web.txt and intake/raw/R2-cutlog.json, then re-reads the written file and
checks every [TEXT] passage as a whitespace-normalised substring of the raw named in its block."""
import json
import re

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

    def block(self, heading, url, rawfile):
        self.n += 1
        self.raw = rawfile
        self.parts += ['', BAR, f'{self.n}. {heading}', url, f'(raw: books/S58-R1/intake/raw/{rawfile})', BAR, '']

    def note(self, *lines):
        self.parts += ['[NOTE] ' + ln for ln in lines] + ['']

    def text(self, start, end, after=None):
        s, i, j = cut(self.raw, start, end, after)
        self.parts += ['[TEXT]', s, '[END TEXT]', '']
        CUTLOG.append({'citekey': self.key, 'block': self.n, 'raw': self.raw, 'i': i, 'j': j, 'chars': j - i})

    def omit(self):
        self.parts += ['[...]', '']

    def write(self):
        open(SRC + self.key + '.txt', 'w', encoding='utf-8').write('\n'.join(self.parts).rstrip() + '\n')


HOME, HOME_URL = 'R-nlm_citing_medicine-NBK7256-home.txt', 'https://www.ncbi.nlm.nih.gov/books/NBK7256/ (raw saved by group R, same day)'
TOC, TOC_URL = 'R2-nlm_citing_medicine-NBK7256-contents.txt', 'https://www.ncbi.nlm.nih.gov/books/NBK7256/ (contents list, fetched again by group R2 with links to find the chapter IDs)'
CPY, CPY_URL = 'R-ncbi-bookshelf-copyright.txt', 'https://www.ncbi.nlm.nih.gov/books/about/copyright/ (raw saved by group R, same day)'
CH4, CH4_URL = 'R2-nlm_citing_medicine-NBK7280-ch4-reports.txt', 'https://www.ncbi.nlm.nih.gov/books/NBK7280/'
CH22, CH22_URL = 'R2-nlm_citing_medicine-NBK7269-ch22-internet-books.txt', 'https://www.ncbi.nlm.nih.gov/books/NBK7269/'
CH25, CH25_URL = 'R2-nlm_citing_medicine-NBK7274-ch25-websites.txt', 'https://www.ncbi.nlm.nih.gov/books/NBK7274/'

HEADER = [
    'Transcription rule for this file: every line between [TEXT] and [END TEXT] is an exact, unaltered',
    'slice of the text returned by the TinyFish fetch_content tool (markdown format) for the URL under its',
    'block heading, cut programmatically from the saved fetch (raw[i:j]; script',
    'books/S58-R1/intake/build-R2.py; offsets in books/S58-R1/intake/raw/R2-cutlog.json). Nothing has been',
    'paraphrased, corrected or merged. [...] marks an omission. Lines beginning [NOTE] are this file\'s own',
    'annotation and are NOT source text.',
    '',
    'WORK: Patrias K; Wendling D, technical editor. Citing Medicine: The NLM Style Guide for Authors,',
    'Editors, and Publishers [Internet]. 2nd ed. Bethesda (MD): National Library of Medicine (US); 2007-.',
    'NCBI Bookshelf ID NBK7256. The SAME WORK as citekey nlm_citing_medicine_2007 (chapter 1, journals);',
    'this file holds other chapters under its own key so that file stays unchanged. Chapter 4, Scientific',
    'and Technical Reports (NBK7280); chapter 22, Books and Other Individual Titles on the Internet',
    '(NBK7269); chapter 25, Web Sites (NBK7274); each "Created: October 10, 2007; Last Update: August 11,',
    '2015" (contents list, block 1).',
    'FETCHED: 2 Oct 2026, TinyFish fetch_content (markdown). The /books/n/citmed/ch4/, /ch25/ and',
    '/n/citmed/A38179/, /A59231/ addresses each returned a reCAPTCHA page ("Checking your browser") twice',
    'and once; the NBK addresses (found by a web search restricted to ncbi.nlm.nih.gov) returned the',
    'chapters on the first read.',
    'LICENCE AS STATED: Citing Medicine home page (block 1): "This publication is in the public domain. For',
    'more information, see the Bookshelf Copyright Notice." Bookshelf Copyright Notice (block 1): for U.S.',
    'government content "No permission is needed to reproduce or distribute this type of content, but the',
    'authoring institute or agency must be given appropriate attribution."',
    'TERMS ON AUTOMATED ACCESS: the Copyright Notice says "Crawlers and other automated processes may NOT be',
    'used to systematically retrieve content from the Bookshelf web site." Group R2 made single, targeted',
    'reads of three chapters plus one contents-list read (and six captcha-blocked attempts listed above);',
    'see log-R2.md.',
    '',
    'WHAT IS HELD: public-domain line, suggested citation and the Copyright Notice paragraphs (block 1);',
    'chapter dates (block 1). Chapter 4 part A (entire reports): introduction (sponsoring vs performing',
    'organisation; report numbers; "See also Chapter 18 and Chapter 22" for reports on the Internet), the',
    'element order, GENERAL rules for author, title, place, publisher, date and report number, examples 1-3,',
    '11-14 and 23 (block 2). Chapter 22 part A (entire books and other individual titles on the Internet,',
    'which the chapter says include "technical reports" and "single-page fact sheet[s]"): introduction,',
    'element order, GENERAL rules for type of medium, place, publisher, dates (publication, update, citation),',
    'extent and availability, examples 1, 7-9, 27-28 and 49 (technical report on the Internet) (block 3).',
    'Chapter 25 part A (homepages): introduction (incl. when a component is cited as a book under ch. 22),',
    'element order, GENERAL rules for author, title, type of medium, place, publisher, dates and',
    'availability, examples 1, 5, 21-22; part B (parts of web sites): introduction and example 1 (block 4).',
    'NOT HELD: every "Specific Rules" box (the fetch returned their headings only), all other examples, part',
    'B of chapter 4, parts B-C of chapter 22, the part B rules of chapter 25, every other chapter.',
    'EXTRACTION ARTEFACTS: each chapter\'s "general format ... including punctuation" is an IMAGE on the page',
    'and is NOT in the text: chapter 4 shows three empty bullet captions (sponsoring / performing',
    'organisation scenarios) and chapters 22 and 25 show nothing after the colon. The examples carry the',
    'format instead. Links are reduced to anchor text; underscores in URLs appear escaped (\\_) as fetched.',
    '',
    'POINTS FOR THE INVENTORY (where the passages are): a government report read online, such as a PDF',
    'fact sheet, is cited under chapter 22 (an Internet "book" includes technical reports and fact sheets;',
    'chapter 4 points there for reports on the Internet; chapter 25 says a book on a Web site is cited under',
    'chapter 22): Author (organisation). Title [Internet]. Place: Publisher; date [cited date]. extent.',
    'Report No. Available from: URL - shown by ch. 22 examples 7 and 49 (block 3). Print report pattern:',
    'ch. 4 examples 1-3, 11-12 (block 2). Homepage pattern: Title [Internet]. Place: Publisher; date',
    '[updated date; cited date]. Available from: URL - ch. 25 example 21 (block 4).',
]

d = Doc('nlm_citing_medicine_2007_reports_web',
        'NLM, CITING MEDICINE, 2ND ED. (PATRIAS, ED., 2007-; NCBI BOOKSHELF NBK7256): CHAPTER 4 SCIENTIFIC AND '
        'TECHNICAL REPORTS, CHAPTER 22 BOOKS AND OTHER INDIVIDUAL TITLES ON THE INTERNET, CHAPTER 25 WEB SITES '
        '- VERBATIM SOURCE PACK', HEADER)

d.block('Citing Medicine: public-domain line; chapter 4, 22 and 25 dates; suggested citation; Bookshelf Copyright Notice', HOME_URL, HOME)
d.text('# Citing Medicine, 2nd edition', 'see the Bookshelf Copyright Notice.')
d.omit()
d.text('#### Suggested citation:', 'Available from: http://www.nlm.nih.gov/citingmedicine')
d.omit()
d.note('The next three passages are from the contents list fetched by group R2 (raw: books/S58-R1/intake/raw/' + TOC + ').')
d.raw = TOC
d.text('  + Chapter 4. Scientific and Technical Reports [PDF Version]', 'Last Update: August 11, 2015.')
d.omit()
d.text('  + Chapter 22. Books and Other Individual Titles on the Internet [PDF Version]', 'Last Update: August 11, 2015.')
d.omit()
d.text('  + Chapter 25. Web Sites [PDF Version]', 'Last Update: August 11, 2015.')
d.omit()
d.note('The next two passages are from the Bookshelf Copyright Notice (raw: books/S58-R1/intake/raw/' + CPY + ').')
d.raw = CPY
d.text('## Publications in the Public Domain', 'before it can be reproduced or distributed.')
d.omit()
d.text('## Restrictions on Systematic Downloading of Books or Chapters', 'automated downloading of content in Bookshelf.')

d.block('Chapter 4 Scientific and Technical Reports, part A: Entire Reports (introduction, element order, general rules, examples)', CH4_URL, CH4)
d.text('## A. Sample Citation and Introduction to Citing Entire Reports', 'Continue to Examples of Citations to Entire Reports.')
d.note('The three general formats (one per publication scenario) are images on the page; only their captions',
       'were returned, each followed by nothing. Examples 1-3 below show the three scenarios in order.')
d.text('## Citation Rules with Examples for Entire Reports', 'Notes (O)')
d.text('### Author/Editor for Reports (required)', '* End author/editor information with a period')
d.omit()
d.note('Author affiliation (optional) omitted.')
d.text('### Title for Reports (required)', 'or a Type of Medium follows it')
d.omit()
d.note('Type of medium, edition and secondary authors omitted.')
d.text('### Place of Publication for Reports (required)', '* End date information with a period')
d.omit()
d.note('Pagination, physical description, series omitted.')
d.text('### Report Number for Reports (required)', '* End the number with a period')
d.omit()
d.note('Contract/grant number, language and notes omitted.')
d.text('## Examples of Citations to Entire Reports', 'Supported by the Robert Wood Johnson Foundation.')
d.omit()
d.note('Examples 4-10 omitted.')
d.text('### 11. Report with an organization as the author or editor', 'Geneva: World Health Organization; 2003. 193 p.')
d.omit()
d.note('Examples 15-22 omitted.')
d.text('### 23. Report with governmental or national agency as publisher', 'Report No.: 431501009.')
d.omit()
d.note('Examples 24-35 and part B (parts of reports) omitted.')

d.block('Chapter 22 Books and Other Individual Titles on the Internet, part A: Entire Books (introduction, element order, general rules, examples incl. technical report on the Internet)', CH22_URL, CH22)
d.text('## A. Sample Citation and Introduction to Citing Entire Books and Other Individual Titles on the Internet',
       'Refer also to Chapter 2 Books for more examples of book citations.')
d.note('The general format "including punctuation" is an image on the page and is not in the text.')
d.text('## Citation Rules with Examples for Entire Books and Other Individual Titles on the Internet', 'Notes (O)')
d.omit()
d.note('Author, affiliation, title, content type rules omitted (as for print books; see block 2 for the report forms).')
d.text('### Type of Medium for Entire Books on the Internet (required)', '* See Chapter 18 for books on CD-ROM, DVD, or disk')
d.omit()
d.note('Edition and secondary authors omitted.')
d.text('### Place of Publication for Entire Books on the Internet (required)',
       'as [about 10 p.]\n* End extent information with a period')
d.omit()
d.note('Series omitted.')
d.text('### Availability for Entire Books on the Internet (required)',
       '* End with a period only if the URL ends with a slash, otherwise end with no punctuation')
d.omit()
d.text('### 1. Standard citation to a book on the Internet', 'http://www.nlm.nih.gov/pubs/factsheets/aidsinfs.html')
d.omit()
d.note('Optional content-type forms of example 1 and examples 2-6 omitted.')
d.text('### 7. Book on the Internet with an organization(s) as author',
       'c1997 [cited 2006 Nov 1]. 4 p. Available from: http://www.painmed.org/productpub/statements/pdfs/opioids.pdf')
d.omit()
d.note('Examples 10-26 omitted.')
d.text('### 27. Book on the Internet with government agency or other national body as publisher',
       'Jointly published by the American Pain Society.')
d.omit()
d.note('Examples 29-48 omitted.')
d.text('### 49. Technical report on the Internet', 'http://purl.access.gpo.gov/GPO/LPS9308')
d.omit()
d.note('Examples 50-51 and parts B (parts of Internet books) and C (contributions) omitted.')

d.block('Chapter 25 Web Sites: part A Homepages (introduction, element order, general rules, examples); part B Parts of Web Sites (introduction, example 1)', CH25_URL, CH25)
d.text('## A. Sample Citation and Introduction to Citing Homepages',
       'If in doubt about the status of a component, cite it separately using the instructions in the appropriate chapter.')
d.note('The general format "including punctuation" is an image on the page and is not in the text.')
d.omit()
d.text('## Citation Rules with Examples for Homepages', 'Notes (O)')
d.text('### Author for Homepages (required)', '* See Editor and other Secondary Authors below if there are no authors but editors are named')
d.omit()
d.note('Author affiliation omitted.')
d.text('### Title for Homepages (required)', '* End a title with a space')
d.omit()
d.note('Content type omitted.')
d.text('### Type of Medium for Homepages (required)', '* Add location information (URL, etc) according to the instructions under Availability below')
d.omit()
d.note('Edition and secondary authors omitted.')
d.text('### Place of Publication for Homepages (required)',
       '* End with a period only if the URL ends with a slash, otherwise end with no punctuation')
d.omit()
d.note('Language and notes omitted.')
d.text('## Examples of Citations to Homepages',
       'AMA: helping doctors help patients [homepage on the Internet]. Chicago: American Medical Association; c1995-2007 [cited 2007 Feb 22]. Available from: http://www.ama-assn.org/.')
d.omit()
d.note('Examples 2-4 omitted.')
d.text('### 5. Homepage with an organization(s) as author', 'and other types of experts.')
d.omit()
d.note('Examples 6-20 omitted.')
d.text('### 21. Homepage with government agency or other national body as publisher', 'http://www.cancerbackup.org.uk/.')
d.omit()
d.note('Examples 23-36 omitted.')
d.text('## B. Sample Citation and Introduction to Citing Parts of Web Sites', 'Continue to Examples of Citations to Parts of Web Sites.')
d.note('The general format for a part of a Web site is an image on the page and is not in the text.')
d.omit()
d.note('Part B citation rules omitted.')
d.text('### 1. Standard part of a Web site', 'ucm101557.htm')
d.omit()
d.note('Part B examples 2-17 omitted.')
d.write()

json.dump(CUTLOG, open(RAW + 'R2-cutlog.json', 'w'), indent=1)

# ---- verbatim check: re-read the written file from disk. Each [TEXT] passage is checked against the raw
# named in its block, or in the nearest preceding [NOTE] that names a raw (block 1 mixes three raws).
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
out = open(SRC + 'nlm_citing_medicine_2007_reports_web.txt', encoding='utf-8').read()
blocks = re.split(r'\n' + BAR + r'\n(?=\d+\. )', out)
ok = total = 0
for b in blocks[1:]:
    rawname = re.search(r'\(raw: books/S58-R1/intake/raw/(\S+)\)', b).group(1)
    for m in re.finditer(r'\(raw: books/S58-R1/intake/raw/(\S+?)\)\.?|\[TEXT\]\n(.*?)\n\[END TEXT\]', b, re.S):
        if m.group(1):
            rawname = m.group(1)
            continue
        total += 1
        good = norm(m.group(2)) in norm(open(RAW + rawname, encoding='utf-8').read())
        ok += good
        if not good:
            print('FAIL', rawname, m.group(2)[:60])
print(f'verbatim check: {ok}/{total}; passages cut: {len(CUTLOG)}; words in passages:',
      sum(len(re.findall(r"\S+", p)) for p in re.findall(r'\[TEXT\]\n(.*?)\n\[END TEXT\]', out, re.S)))
