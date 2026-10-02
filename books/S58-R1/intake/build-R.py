#!/usr/bin/env python3
"""Group R intake builder for S58-R1 (referencing: NLM Citing Medicine, 2nd ed., the journal-article chapter).
Every passage is cut from a saved raw fetch by raw[i:j] between anchor strings; nothing is typed by hand.
Writes sources/nlm_citing_medicine_2007.txt and intake/raw/R-cutlog.json, then re-reads the written file and
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


HOME, HOME_URL = 'R-nlm_citing_medicine-NBK7256-home.txt', 'https://www.ncbi.nlm.nih.gov/books/NBK7256/'
CPY, CPY_URL = 'R-ncbi-bookshelf-copyright.txt', 'https://www.ncbi.nlm.nih.gov/books/about/copyright/'
CH1, CH1_URL = 'R-nlm_citing_medicine-NBK7282-ch1-journals.txt', 'https://www.ncbi.nlm.nih.gov/books/NBK7282/'
APB, APB_URL = 'R-nlm_citing_medicine-NBK7253-appB.txt', 'https://www.ncbi.nlm.nih.gov/books/n/citmed/appb/ (resolved to https://www.ncbi.nlm.nih.gov/books/NBK7253/)'
SMP, SMP_URL = 'R-nlm_sample_references.txt', 'https://www.nlm.nih.gov/bsd/uniform_requirements.html'

HEADER = [
    'Transcription rule for this file: every line between [TEXT] and [END TEXT] is an exact, unaltered',
    'slice of the text returned by the TinyFish fetch_content tool (markdown format) for the URL under its',
    'block heading, cut programmatically from the saved fetch (raw[i:j]; script',
    'books/S58-R1/intake/build-R.py; offsets in books/S58-R1/intake/raw/R-cutlog.json). Nothing has been',
    'paraphrased, corrected or merged. [...] marks an omission. Lines beginning [NOTE] are this file\'s own',
    'annotation and are NOT source text.',
    '',
    'WORK: Patrias K; Wendling D, technical editor. Citing Medicine: The NLM Style Guide for Authors,',
    'Editors, and Publishers [Internet]. 2nd ed. Bethesda (MD): National Library of Medicine (US); 2007-.',
    'NCBI Bookshelf ID NBK7256. Chapter 1, Journals (NBK7282): "Created: October 10, 2007; Last Update:',
    'May 18, 2018" (contents page, block 1). Appendix B (NBK7253): "Last Update: October 2, 2015".',
    'Block 5 is a SEPARATE NLM page, "Samples of Formatted References for Authors of Journal Articles"',
    '(the ICMJE-linked sample references; "Last Reviewed: June 2, 2026"), held for its short format examples',
    'and its preprint examples; cite it as its own web page if quoted, not as Citing Medicine.',
    'FETCHED: 2 Oct 2026, TinyFish fetch_content (markdown). The first fetch of NBK7282 returned a reCAPTCHA',
    'interstitial ("Checking your browser"); a second single fetch returned the chapter. The PDF version',
    '(Bookshelf_NBK7282.pdf) was unreachable.',
    'LICENCE AS STATED: Citing Medicine home page (block 1): "This publication is in the public domain. For',
    'more information, see the Bookshelf Copyright Notice." Bookshelf Copyright Notice (block 2): for U.S.',
    'government content "No permission is needed to reproduce or distribute this type of content, but the',
    'authoring institute or agency must be given appropriate attribution." The Sample References page (block 5)',
    'states no licence on the fetched text; it is an NLM (U.S. government) web page.',
    'TERMS ON AUTOMATED ACCESS: the same Copyright Notice says "Crawlers and other automated processes may',
    'NOT be used to systematically retrieve content from the Bookshelf web site." This intake made single,',
    'targeted page reads (the book\'s contents page, chapter 1, appendix B, the notice itself), not systematic',
    'retrieval, and fetched nothing else from Bookshelf. ncbi.nlm.nih.gov/robots.txt (User-agent: *) does not',
    'disallow /books/NBK pages (only /books/?term=). Recorded for Harsh in log-R.md.',
    '',
    'WHAT IS HELD: the book\'s title, authorship, public-domain line and suggested citation (block 1); the',
    'Bookshelf notice paragraphs on public-domain content and on systematic downloading (block 2); from',
    'chapter 1, part A (journal articles): the introduction and its "important points", the ordered list of',
    'citation elements, the GENERAL rules for author, article title, journal title, date, volume, issue and',
    'pagination, and examples 1-4 and 69-71 (standard article; many authors; optional limit to 3 or 6 authors',
    'with "et al."; organisation as author; epub ahead of print; PMID; DOI) (block 3); appendix B\'s opening',
    'paragraphs (ISO 4; the NLM Catalog as the first place to find an abbreviation) (block 4); the Sample',
    'References introduction, item 1 and item 34 (forthcoming and preprints) (block 5).',
    'NOT HELD: the chapter\'s collapsed "Specific Rules" boxes (the fetch returned their headings only), the',
    'rules for the optional and rarely needed elements, examples 5-68 and 72-75, parts B and C of chapter 1,',
    'every other chapter and appendix.',
    'EXTRACTION ARTEFACTS: the "general format for a reference to a journal article, including punctuation"',
    'that chapter 1 introduces is an image on the page and is NOT in the text (block 3 shows the sentence',
    'followed by nothing); the standard examples carry the format instead. Links are reduced to their',
    'anchor text. "Use arabic numbers onlyconvert LX" (volume rules) is the page\'s own run-together text.',
    '',
    'POINTS FOR THE INVENTORY (where the passages are): the Vancouver journal-article pattern, Author AA,',
    'Author BB. Title of article. Abbreviated Journal Title. Year Mon Day;Volume(Issue):pages., is shown by',
    'example 1 in block 3 and item 1 in block 5; authors surname first with at most two initials, all',
    'authors given (Citing Medicine) or optionally the first 3 or 6 then "et al." (example 3; the Sample',
    'References page: "List the first six authors, followed by et al."); only the first word and proper',
    'nouns of an article title capitalised; journal titles abbreviated (ISO 4; look the title up in the NLM',
    'Catalog first, block 4; ICMJE section IV.A.3.g in icmje_2026_manuscript_preparation says the same:',
    'MEDLINE style, www.ncbi.nlm.nih.gov/nlmcatalog/journals); page ranges shortened (123-125 becomes',
    '123-5); a preprint marked "[Preprint]" (block 5, item 34); "Cite the version you saw" (block 3).',
]

d = Doc('nlm_citing_medicine_2007',
        'NLM, CITING MEDICINE, 2ND ED. (PATRIAS, ED., 2007-; NCBI BOOKSHELF NBK7256): CHAPTER 1 JOURNALS, PART A '
        '(JOURNAL ARTICLES), WITH APPENDIX B AND THE NLM SAMPLE REFERENCES - VERBATIM SOURCE PACK', HEADER)

d.block('Citing Medicine, 2nd edition: title page, public-domain line, chapter 1 dates, suggested citation', HOME_URL, HOME)
d.text('# Citing Medicine, 2nd edition', 'see the Bookshelf Copyright Notice.')
d.omit()
d.text('Chapter 1. Journals [PDF Version]', 'Last Update: May 18, 2018.')
d.omit()
d.text('#### Suggested citation:', 'Available from: http://www.nlm.nih.gov/citingmedicine')

d.block('NCBI Bookshelf Copyright Notice: public-domain content; systematic downloading', CPY_URL, CPY)
d.text('## Publications in the Public Domain', 'before it can be reproduced or distributed.')
d.omit()
d.text('## Restrictions on Systematic Downloading of Books or Chapters', 'automated downloading of content in Bookshelf.')

d.block('Chapter 1 Journals, part A: Journal Articles (introduction, element order, general rules, examples)', CH1_URL, CH1)
d.text('Journals are a particular type of periodical.', 'Continue to Examples of Citations to Journal Articles.')
d.note('The page shows the general format with its punctuation as an image after "including punctuation:";',
       'it is not in the fetched text. Example 1 below carries the same pattern.')
d.text('## Citation Rules with Examples for Journal Articles', 'Language (R) | Notes (O)')
d.text('### Author for Journal Articles (required)', 'See exceptions for Author in Appendix F: Notes for Citing MEDLINE® /PubMed®.')
d.omit()
d.note('Author affiliation (optional) omitted.')
d.text('### Article Title for Journal Articles (required)', 'See exceptions for Article Title in Appendix F: Notes for Citing MEDLINE® /PubMed®')
d.omit()
d.note('Article type (optional) omitted.')
d.text('### Journal Title for Journal Articles (required)', 'See exceptions for Journal Title (Journal Title Abbreviation) in Appendix F: Notes for Citing MEDLINE® /PubMed®')
d.omit()
d.note('Edition and type of medium omitted (they apply to the rare journal with editions, and to non-print media).')
d.text('### Date of Publication for Journal Articles (required)', 'then end with a colon')
d.omit()
d.note('Supplements, parts and special numbers to a date or volume omitted.')
d.text('### Volume Number for Journal Articles (required)', 'then follow with a colon')
d.omit()
d.text('### Issue Number for Journal Articles (required)', '(see Further subdivisions to supplements, parts, etc., to an issue below)')
d.omit()
d.text('### Location (Pagination) for Journal Articles (required)', 'End pagination information with a period')
d.omit()
d.note('Physical description, language and notes omitted (language: give it if other than English).')
d.text('## Examples of Citations to Journal Articles', 'Arch Neurol. 2005 Feb;62(2):241-8.')
d.omit()
d.note('Examples 5-68 omitted.')
d.text('### 69. Journal article with indication article published electronically before print', 'doi:10.1542/peds.2004-1441.')
d.omit()
d.note('Examples 72-75 and parts B (parts of articles) and C (entire journal titles) omitted.')

d.block('Appendix B, Additional Sources for Journal Title Abbreviations: opening paragraphs', APB_URL, APB)
d.text('# Appendix BAdditional Sources for Journal Title Abbreviations', 'when rules for specific words change.')
d.omit()
d.note('The Source List of non-NLM abbreviation lists omitted. "Appendix BAdditional" is the page\'s run-together heading.')

d.block('NLM, Samples of Formatted References for Authors of Journal Articles: introduction, item 1, item 34 (A SEPARATE NLM PAGE)', SMP_URL, SMP)
d.text('# Samples of Formatted References for Authors of Journal Articles', 'Brain Res. 2002;935(1-2):40-6.')
d.omit()
d.note('The optional forms of item 1 (continuous pagination, PMID, trial registration) and items 2-33 omitted.')
d.text('34. Forthcoming and Preprints', 'doi: https://doi.org/10.1101/088278')
d.omit()
d.note('The fourth preprint example and items 35-44 omitted. The page ends "Last Reviewed: June 2, 2026".')
d.write()

json.dump(CUTLOG, open(RAW + 'R-cutlog.json', 'w'), indent=1)

# ---- verbatim check: re-read the written file from disk
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
out = open(SRC + 'nlm_citing_medicine_2007.txt', encoding='utf-8').read()
blocks = re.split(r'\n' + BAR + r'\n(?=\d+\. )', out)
ok = total = 0
for b in blocks[1:]:
    m = re.search(r'\(raw: books/S58-R1/intake/raw/(\S+)\)', b)
    raw = norm(open(RAW + m.group(1), encoding='utf-8').read())
    for p in re.findall(r'\[TEXT\]\n(.*?)\n\[END TEXT\]', b, re.S):
        total += 1
        ok += norm(p) in raw
print(f'verbatim check: {ok}/{total}; passages cut: {len(CUTLOG)}; words in passages:',
      sum(len(re.findall(r"\S+", p)) for p in re.findall(r'\[TEXT\]\n(.*?)\n\[END TEXT\]', out, re.S)))
