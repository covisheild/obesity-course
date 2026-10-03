#!/usr/bin/env python3
"""S58-R1 intake, group C1: build sources/<citekey>.txt from the saved raw TinyFish fetches.

Every passage is one contiguous slice raw[i:j] of a raw file in intake/raw/, located by
start and end anchors (or the start/end of the raw text). Nothing is typed by hand into a
passage. Run verify-C1.py afterwards. Writes only files named in OUT; touches nothing else.
"""
import json, os

ROOT = '/home/claude/obesity-course'
RAW = ROOT + '/books/S58-R1/intake/raw/'
SRC = ROOT + '/sources/'
DATE = '2026-10-02'
RULE = '=' * 79

TRANSCRIPTION_RULE = """Transcription rule for this file: every line beneath a block heading that is not
prefixed with [NOTE] is an exact, unaltered slice of the text returned by the TinyFish
fetch_content tool for the URL in that heading, cut programmatically from the saved fetch
(raw[i:j], one contiguous slice per block); nothing has been paraphrased, smoothed or merged.
Each block's passage is set in double quotation marks (the marks are this file's, not the
source's). Markdown marks (#, *, |) are the extraction's. Tables keep the line breaks and pipes
the extraction produced. Material left out is marked [...] with a [NOTE]. Lines beginning
[NOTE] are this file's own annotation and are NOT source text. Reference lists are never held."""


def raw(name):
    return open(RAW + name, encoding='utf-8').read()


def cut(name, start=None, end=None, end_inclusive=None):
    """Return raw[i:j]. start: anchor string (slice begins at it) or None for 0.
    end: anchor string (slice ends just before it) or None for len(raw).
    end_inclusive: anchor string (slice ends just after it)."""
    t = raw(name)
    i = 0 if start is None else t.index(start)
    if end_inclusive is not None:
        j = t.index(end_inclusive, i) + len(end_inclusive)
    elif end is not None:
        j = t.index(end, i)
    else:
        j = len(t)
    s = t[i:j].strip()
    assert s and s in t
    return s


def block(n, label, url, rawname, passage, how='TinyFish fetch_content, markdown'):
    return (f"{RULE}\n{n}. {label}\n{url}\n({how}; raw file {rawname}, fetched {DATE})\n{RULE}\n\n"
            f"\"{passage}\"\n")


MANIFEST = []  # (source file, block no, url, raw file, passage) for the verifier


def write(fname, header, blocks):
    parts = [header.rstrip() + '\n\n']
    for b in blocks:
        if isinstance(b, str):            # an omission note between blocks
            parts.append('\n' + b.rstrip() + '\n\n')
            continue
        n, label, url, rawname, passage, how = b
        parts.append('\n' + block(n, label, url, rawname, passage, how) + '\n')
        MANIFEST.append({'file': fname, 'block': n, 'url': url, 'raw': rawname, 'chars': len(passage)})
    open(SRC + fname, 'w', encoding='utf-8').write(''.join(parts))
    print('wrote', fname, sum(1 for b in blocks if not isinstance(b, str)), 'blocks')


# ---------------------------------------------------------------- Rougier 2014
ROUG_URL = 'https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833'
ROUG_XML = 'https://pmc-oa-opendata.s3.amazonaws.com/PMC4161295.1/PMC4161295.1.xml'
R1 = 'C1-rougier_2014_ten_rules_figures-plos.txt'
R2 = 'C1-rougier_2014_ten_rules_figures-pmcxml.txt'

rougier_header = f"""ROUGIER, DROETTBOOM AND BOURNE 2014, PLOS COMPUTATIONAL BIOLOGY — VERBATIM SOURCE PACK (WHOLE TEXT, NO REFERENCES)
{'=' * 60}

{TRANSCRIPTION_RULE}

CITATION: Rougier NP, Droettboom M, Bourne PE. Ten simple rules for better figures. PLoS Comput
Biol 2014;10(9):e1003833. Published 11 September 2014.
PMID: 25210732   PMCID: PMC4161295   DOI: 10.1371/journal.pcbi.1003833   (confirmed with the PubMed
ID converter, {DATE})
TEXT FETCHED FROM: {ROUG_URL} (the publisher's article page; TinyFish fetch_content, markdown),
{DATE}. Figure titles from the PMC open-access JATS XML, {ROUG_XML}.
LICENCE AS STATED ON THE ARTICLE PAGE (block 1): "This is an open-access article, free of all
copyright, and may be freely reproduced, distributed, transmitted, modified, built upon, or
otherwise used by anyone for any lawful purpose. The work is made available under the Creative
Commons CC0 public domain dedication." The PMC XML links https://creativecommons.org/publicdomain/zero/1.0/
(CC0), not CC BY 4.0 as READY.md guessed.

WHAT THIS FILE HOLDS: block 1 is the whole article page text from the citation line to the end of
the Notes: citation, date, licence, funding, the introduction, Rules 1-10 in full, the Figure 1-8
captions (each caption paragraph sits under its rule, as the page gives it), the Rule 10 tool
list, and the Notes. Block 2 holds the eight figure titles from the PMC XML. Omitted: the
reference list (refs 1-10), and the figures themselves (images, NOT held).
[NOTE] The article page drops the figure number and title in front of each caption paragraph.
In block 1 the caption paragraphs are, in order, those of Figures 1, 2, 3 (under Rules 1, 2, 3),
4, 5, 6, 7, 8 (under Rules 5, 6, 7, 8, 9); Rules 4 and 10 have no figure. Block 2 gives the
numbers and titles from the XML. Captions should be cited by figure number from block 2.
[NOTE] Defect of the extraction: in the Figure 3 caption, the inline mathematics after "a
dual-particle system" is lost and reads "(, , , )". Nothing in that parenthesis is held.
"""

rougier_blocks = [
    (1, 'Whole article text: citation, licence, introduction, Rules 1-10 with Figure 1-8 captions, Notes',
     ROUG_URL, R1, cut(R1, 'Citation: Rougier NP', '## References'), 'TinyFish fetch_content, markdown'),
    '[...]\n[NOTE] Omitted after block 1: the reference list (references 1-10).',
]
# one block per figure title line, each a contiguous slice of the XML text
fig_blocks = []
for k, ttl in enumerate(['Know your audience.', 'Identify your message.',
                         'Adapt the figure to the support medium.', 'Do not trust the defaults.',
                         'Use color effectively.', 'Do not mislead the reader.', 'Avoid chartjunk.',
                         'Message trumps beauty.'], start=1):
    anchor = f'10.1371/journal.pcbi.1003833.g00{k}Figure {k}{ttl}'
    fig_blocks.append(cut(R2, anchor, end_inclusive=anchor))
# block 2 holds eight one-line slices, 2a-2h, so each is its own checked passage
for k, s in enumerate(fig_blocks):
    rougier_blocks.append((f'2{"abcdefgh"[k]}', f'Figure {k+1} title (PMC JATS XML; the DOI, figure label and title run together as the extraction gives them)',
                           ROUG_XML, R2, s, 'TinyFish fetch_content, markdown'))
    if k < 7:
        rougier_blocks.append(f'[...]\n[NOTE] Omitted between 2{"abcdefgh"[k]} and 2{"abcdefgh"[k+1]}: the caption and the article text that follow this title in the XML (the captions are held in block 1).')
write('rougier_2014_ten_rules_figures.txt', rougier_header, rougier_blocks)

# ---------------------------------------------------------------- Bergstrom & West
BW_URL = 'https://callingbullshit.org/tools/tools_proportional_ink.html'
BW = 'C1-bergstrom_west_2016_proportional_ink-body.txt'
bw_header = f"""BERGSTROM AND WEST, "THE PRINCIPLE OF PROPORTIONAL INK" (CALLING BULLSHIT, TOOLS) — VERBATIM SOURCE PACK (WHOLE TEXT)
{'=' * 60}

{TRANSCRIPTION_RULE}

CITATION: Bergstrom CT, West JD. The principle of proportional ink. Calling Bullshit (course
website), Tools section. {BW_URL}
DATE AND AUTHORS: the page carries no byline and no date. The authors are named in the site
footer (block 2: "Calling Bullshit has been developed by Carl Bergstrom and Jevin West"); the year
2016 is the one Wilke gives when citing this page ("Bergstrom, C. T., and J. West. 2016. 'The
Principle of Proportional Ink.'", Fundamentals of Data Visualization ch. 17 reference list, held in
the raw fetch of that chapter, not in a source file). The page itself does not state 2016.
TEXT FETCHED FROM: the URL above, TinyFish fetch_content, markdown, with include_selectors ["body"]
so that headings and the footer are kept, {DATE}. (A first default-markdown fetch dropped the
headings and footer; its text matches block 1's paragraphs and is kept only as raw.)
LICENCE AS STATED: no licence is stated on the page. The only rights line is the footer:
"Copyright © Calling Bullshit 2017-2019" (block 2). No open licence: all rights reserved by
default; quotation for teaching only. The site has no robots.txt (404 on {DATE}) and no terms
page forbidding automated access was found; the footer disclaimer says the site "is intended for
personal educational use".

WHAT THIS FILE HOLDS: block 1, the whole article from its title to the end of its Conclusion
(sections Bar charts, Line graphs, Bubble charts, Donut bar charts, A changing denominator, Three
dimensions, Perspective, Pie charts, Conclusion); block 2, the site footer (authors, disclaimer,
copyright line). Omitted: the site navigation menu above the article. The example charts are
images and NONE is held; the text describes them. Not held: the companion pages the article
links to (the article on misleading axes; the separate page on logarithmic scales).
"""
bw_blocks = [
    '[...]\n[NOTE] Omitted before block 1: the site navigation menu ("Toggle navigation ... Contact") and the section label "Visualization".',
    (1, 'The article, whole: title to the end of the Conclusion', BW_URL, BW,
     cut(BW, '# The Principle of Proportional Ink', end_inclusive='Design carefully to avoid violating this principle yourself.'),
     'TinyFish fetch_content, markdown, include_selectors ["body"]'),
    (2, 'Site footer: authors, disclaimer, copyright line', BW_URL, BW,
     cut(BW, 'Calling Bullshit has been developed by', end_inclusive='Copyright © Calling Bullshit 2017-2019'),
     'TinyFish fetch_content, markdown, include_selectors ["body"]'),
]
write('bergstrom_west_2016_proportional_ink.txt', bw_header, bw_blocks)

# ---------------------------------------------------------------- Wilke chapters
WELCOME_URL = 'https://clauswilke.com/dataviz/'
WEL = 'C1-wilke_2019_dataviz-welcome.txt'
CHAPTERS = [
    # num, slug, title as the chapter heading gives it, concepts
    ('03', 'coordinate-systems-axes', 'Coordinate systems and axes', 'C16'),
    ('04', 'color-basics', 'Color scales', 'C18'),
    ('05', 'directory-of-visualizations', 'Directory of visualizations', 'C14'),
    ('07', 'histograms-density-plots', 'Visualizing distributions: Histograms and density plots', 'C15'),
    ('09', 'boxplots-violins', 'Visualizing many distributions at once', 'C15'),
    ('17', 'proportional-ink', 'The principle of proportional ink', 'C14, C16'),
    ('19', 'color-pitfalls', 'Common pitfalls of color use', 'C18'),
    ('20', 'redundant-coding', 'Redundant coding', 'C17, C19'),
    ('22', 'figure-titles-captions', 'Titles, captions, and tables', 'C19 (and the table gap in COVERAGE.md)'),
    ('23', 'balance-data-context', 'Balance the data and the context', 'C17'),
    ('24', 'small-axis-labels', 'Use larger axis labels', 'C19'),
    ('26', 'no-3d', 'Don’t go 3D', 'C17'),
    ('27', 'image-file-formats', 'Understanding the most commonly used image file formats', 'C20'),
    ('28', 'choosing-visualization-software', 'Choosing the right visualization software', 'C20'),
    ('29', 'telling-a-story', 'Telling a story and making a point', 'C13'),
]

WILKE_LICENCE = f"""LICENCE AS STATED ON THE BOOK'S WELCOME PAGE ({WELCOME_URL}, block 1): "This work is licensed
under the Attribution-NonCommercial-NoDerivatives 4.0 International License." (CC BY-NC-ND 4.0.)
[NOTE] Because the licence forbids derivatives, this file is a verbatim excerpt held privately
for study and for quotation with attribution. It has not been edited or adapted, and nothing in
it may be reworked into course text except as short attributed quotation.
STATUS OF THE TEXT: the welcome page says the website "contains the complete author manuscript
before final copy-editing and other quality control" of the O'Reilly book. Wording may differ
from the printed edition; cite the website version. The year 2019 is the print edition's
(READY.md); the website does not state a year."""


def wilke_header(num, slug, title, concepts, has_caps, extra_notes):
    url = f'https://clauswilke.com/dataviz/{slug}.html'
    n = int(num)
    caps = ("block 3 holds every figure caption of the chapter (\"Figure %d.1: ...\" onward), from a "
            "second fetch scoped to p.caption" % n) if has_caps else (
            "the chapter's figures have no captions (a fetch scoped to p.caption matched nothing)")
    return f"""WILKE, FUNDAMENTALS OF DATA VISUALIZATION, CHAPTER {n} "{title.upper()}" — VERBATIM SOURCE PACK (WHOLE CHAPTER TEXT, NO REFERENCES)
{'=' * 60}

{TRANSCRIPTION_RULE}

CITATION: Wilke CO. Fundamentals of Data Visualization. O'Reilly Media; 2019. Chapter {n},
{title}. Author's manuscript online at {url}
[NOTE] The website names the publisher ("published by O’Reilly Media, Inc.", block 1) but gives
no year, subtitle or ISBN; none of those was checked at intake.
TEXT FETCHED FROM: {url} (TinyFish fetch_content, markdown), {DATE}.
{WILKE_LICENCE}

WHAT THIS FILE HOLDS: block 1, the welcome page (what the website is, and the licence); block 2,
the whole text of chapter {n} as the extraction gives it, from the start of the chapter to the end
of the last section; {caps}. Omitted: the chapter's reference list. The figures are images and NONE
is held. Concepts served (INVENTORY.md): {concepts}.
{extra_notes}"""


EXTRA = {
    '04': """[NOTE] Omitted inside block 2's chapter: nothing. Omitted after block 2: a stray R build message
that the website prints at the end of section 4.3 ("## Warning: package 'sf' was built under R
version 3.5.2", inside empty code fences) and the reference list.""",
    '19': """[NOTE] Table 19.1 (the Okabe-Ito colour-blind-safe palette: name, hex code, hue, CMYK, RGB)
is held inside block 2 as the extraction gives it: a pipe-table header row, then one cell per
line.""",
    '22': """[NOTE] The chapter-body extraction (block 2) begins at the chapter's first paragraph; it does
not carry the chapter heading, and its three section headings appear unnumbered ("Figure titles and
captions", "Axis and legend titles", "Tables"). The chapter number and title are confirmed by the
heading in block 3 ("# 22 Titles, captions, and tables"), from the second fetch, which was scoped
to h1 and p.caption. COVERAGE.md's "Wilke §22.3 Tables" is the third of these sections.""",
    '23': """[NOTE] Block 3's fetch was scoped to h1 and p.caption, so it opens with the site title and the
chapter heading before the captions.""",
}
for c in ('24', '26', '27', '28', '29'):
    EXTRA[c] = EXTRA['23']
EXTRA['27'] = EXTRA['23'] + """
[NOTE] Table 27.1 (graphics formats: acronym, name, type, application) is held inside block 2 as
the extraction gives it: one cell per line, no pipes or rules; read it in groups of four lines."""
EXTRA['28'] += """
[NOTE] For C20 ("a spreadsheet will do"): this chapter and the book's Preface argue against
interactive, hand-edited figure making; the Preface says "Excel is an interactive plot program as
well and is not recommended for figure preparation (or data analysis)". The Preface is held in
wilke_2019_dataviz_preface.txt."""

for num, slug, title, concepts in CHAPTERS:
    url = f'https://clauswilke.com/dataviz/{slug}.html'
    body = f'C1-wilke_2019_dataviz-ch{num}-{slug}.txt'
    capf = f'C1-wilke_2019_dataviz-ch{num}-captions.txt'
    has_caps = os.path.exists(RAW + capf)
    t = raw(body)
    if num == '04':
        end = '```\n```\n## Warning'
    elif '### References' in t:
        end = '### References'
    else:
        end = None
    blocks = [
        (1, 'Welcome page: what the website is; the licence', WELCOME_URL, WEL,
         cut(WEL, 'This is the website for the book', end_inclusive='4.0 International License.'),
         'TinyFish fetch_content, markdown'),
        '[...]\n[NOTE] Omitted between blocks 1 and 2: the book\'s front matter and every chapter not named in this file.',
        (2, f'Chapter {int(num)}, whole text' + (' (to the end of the last section)' if end else ''),
         url, body, cut(body, None, end), 'TinyFish fetch_content, markdown'),
    ]
    if end:
        blocks.append('[...]\n[NOTE] Omitted after block 2: ' + (
            "the R build message and the reference list (see header)." if num == '04' else 'the chapter\'s reference list.'))
    if has_caps:
        how = 'TinyFish fetch_content, markdown, include_selectors ["p.caption"]' if int(num) < 22 else \
              'TinyFish fetch_content, markdown, include_selectors ["p.caption", "h1"]'
        blocks.append((3, f'Chapter {int(num)}, all figure captions', url, capf, cut(capf), how))
    write(f'wilke_2019_dataviz_ch{num}.txt',
          wilke_header(num, slug, title, concepts, has_caps, EXTRA.get(num, '')), blocks)

# Preface (short; held for C20's tool question)
PRE = 'C1-wilke_2019_dataviz-preface.txt'
PRE_URL = 'https://clauswilke.com/dataviz/preface.html'
pre_header = f"""WILKE, FUNDAMENTALS OF DATA VISUALIZATION, PREFACE — VERBATIM SOURCE PACK (WHOLE PREFACE)
{'=' * 60}

{TRANSCRIPTION_RULE}

CITATION: Wilke CO. Fundamentals of Data Visualization. O'Reilly Media; 2019. Preface. Author's
manuscript online at {PRE_URL}
TEXT FETCHED FROM: {PRE_URL} (TinyFish fetch_content, markdown, include_selectors ["h1", "p"]),
{DATE}.
{WILKE_LICENCE}

WHAT THIS FILE HOLDS: block 1, the welcome page (licence); block 2, the whole Preface: why figures
matter, "eye", reading piecemeal, software-agnostic principles, automation and reproducibility
("the moment you manually edit a figure, your final figure becomes irreproducible"), interactive
plot programs and Excel "not recommended for figure preparation", acknowledgements. Not in
READY.md's chapter list: added because it bears on C20's "a spreadsheet will do", which it
contradicts. The extraction opens with the site title and the "# Preface" heading.
"""
pre_blocks = [
    (1, 'Welcome page: what the website is; the licence', WELCOME_URL, WEL,
     cut(WEL, 'This is the website for the book', end_inclusive='4.0 International License.'),
     'TinyFish fetch_content, markdown'),
    '[...]\n[NOTE] Omitted between blocks 1 and 2: nothing of the Preface; the rest of the book is not in this file.',
    (2, 'Preface, whole', PRE_URL, PRE, cut(PRE, '# Preface'),
     'TinyFish fetch_content, markdown, include_selectors ["h1", "p"]'),
]
write('wilke_2019_dataviz_preface.txt', pre_header, pre_blocks)

json.dump(MANIFEST, open(ROOT + '/books/S58-R1/intake/manifest-C1.json', 'w'), indent=1)
print(len(MANIFEST), 'passages')
