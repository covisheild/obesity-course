#!/usr/bin/env python3
"""Cuts the Tufte passages from the pdftotext -layout extraction of the four PDFs Harsh supplied
(2 Oct 2026) and writes sources/tufte_1983_visual_display.txt. Every passage is raw[i:j] of one saved
raw text (whitespace-flexible anchors, as build-K.py). After writing, the file is re-read from disk and
every [TEXT] passage is re-checked as a whitespace-normalised substring of the raw it names."""
import re
R = '/home/claude/obesity-course/'
RAWDIR = R + 'books/S58-R1/intake/raw/'
RAWS = {p: f'T-tufte_2001-part{p}-pdftotext.txt' for p in (1, 2, 3, 4)}
raw = {p: open(RAWDIR + f, encoding='utf-8').read() for p, f in RAWS.items()}
PDFFILE = {1: '664e5786-1_SplittRare_... (PDF pages 1-50)', 2: 'abae68c0-51_SplittRare_... (PDF pages 51-100)',
           3: '4701cb92-101_SplittRare_... (PDF pages 101-150)', 4: '5949e965-151_SplittRare_... (PDF pages 151-208)'}

def rx(t):
    return r'\s+'.join(re.escape(w) for w in t.split())

def cut(part, start, end):
    s = raw[part]
    ms = list(re.finditer(rx(start), s)); assert len(ms) == 1, (start, len(ms))
    i = ms[0].start()
    me = re.search(rx(end), s[i:]); assert me, (end,)
    j = i + me.end()
    assert s[i:j].count('\f') == 0, ('passage crosses a page break', start)
    return s[i:j]

# (heading, part, book pages, PDF pages, [(start, end)], [notes])
P = [
 ('Scan provenance leaf and copyright page (edition and printing)', 1, 'front matter, unnumbered', '5, 8',
  [('Digitized by the Internet Archive', 'https://archive.org/details/owb_T2-EQU-551'),
   ('Copyright © 1983 by Edward R. Tufte', 'Tenth printing, March 1990')],
  ['[NOTE] OCR error: the page image (PDF p. 5) reads "https://archive.org/details/bwb_T2-EQU-551" (bwb, not owb).',
   '[NOTE] The page image (PDF p. 8) confirms: Copyright (c) 1983 by Edward R. Tufte; Graphics Press, Box 430, Cheshire,',
   '[NOTE] Connecticut 06410; ALL RIGHTS RESERVED; Tenth printing, March 1990. This is the FIRST edition, not the',
   '[NOTE] second edition of 2001.']),
 ('Ch. 2 Graphical Integrity: the first two principles (book p. 56)', 2, '56', '60',
  [('At any rate, given the perceptual difficulties, the best we can', 'Label important events in the data.')],
  []),
 ('Ch. 2: the Lie Factor, its definition, the acceptable range, and the fuel-economy example (book pp. 57-58)', 2, '57, 58', '61, 62',
  [('Violations of the first principle constitute one form of graphic', 'These standards and the dates for their attainment were shown:'),
   ('This line, representing 18 miles per', 'gallon in 1978, is 0.6 inches long.'),
   ('This line, representing 27.5 miles per', 'gallon in 1985, is 5.3 inches long.'),
   ('The magnitude of the change from 1978 to 1985 is shown in the', 'which is too big.')],
  ['[NOTE] The Lie Factor formula is set as a display fraction and the text layer garbles it ("TSE CC Oe ee oe").',
   '[NOTE] Read from the page image (book p. 57, PDF p. 61):',
   '[NOTE]     Lie Factor = (size of effect shown in graphic) / (size of effect in data)',
   '[NOTE] OCR errors, true readings from the page images: p. 57 "1007 = 53%" is "x 100 = 53%", i.e.',
   '[NOTE]     (27.5 - 18.0) / 18.0 x 100 = 53%;',
   '[NOTE] p. 58 "X< 100:= 783%" is "x 100 = 783%", i.e. (5.3 - 0.6) / 0.6 x 100 = 783%;',
   '[NOTE] p. 58 "Lie Factor = 7 = 14.8 / 59" is "Lie Factor = 783 / 53 = 14.8" (read from the page image).',
   '[NOTE] In "27.5 — 18.0" and "5.3 — 0.6" the page prints a minus sign, not a dash; "———" on p. 58 is a fraction bar.',
   '[NOTE] The two "This line, representing ..." passages are labels printed beside the figure on p. 57; the figure',
   '[NOTE] itself (New York Times, August 9, 1978, p. D-2) and the redrawn version on p. 58 are not held.']),
 ('Ch. 2: design variation (book pp. 60-61)', 2, '60, 61', '64, 65',
  [('Design and Data Variation', 'take the four years’ worth of data up to a comparable decade),'),
   ('the U.S. curve turned sharply upward in the post-1970 interval.', 'the U.S. curve turned sharply upward in the post-1970 interval.'),
   ('A correction, with the actual data for 1971-80, is at the right:', 'is at the right:'),
   ('The confounding of design variation with data variation over the', 'Show data variation, not design variation.'),
   ('Five different vertical scales show the price:', 'That is design variation.')],
  ['[NOTE] p. 60: the [...] breaks fall where the side-note citation (National Science Foundation, Science Indicators,',
   '[NOTE] 1974) runs into the text layer; no words of the running text are omitted. The Nobel Prize and OPEC figures',
   '[NOTE] are not held. On p. 61 the page image prints "design variation" and "data variation" in italics, and the',
   '[NOTE] scale table uses en dashes ("January–March 1979"); the text layer has em dashes. Numbers checked: $8.00,',
   '[NOTE] $4.73, $4.37, $4.16, $3.92; 3.8 and 0.57 years; 0.31 and 4.69 square inches; 4.69/0.31 = 15.1.']),
 ('Ch. 2: areas and dimensions, the shrinking dollar and the barrels (book pp. 70-71)', 2, '70, 71', '74, 75',
  [('Many published efforts using areas to show magnitudes make', 'such charts:'),
   ('If the area of the dollar is accurately to reflect its purchasing power', 'then the 1978 dollar should be about twice as big as that shown.'),
   ('By surface area, the Lie Factor for this graphic is 9.4.', 'which is a record.'),
   ('Conclusion: The use of two (or three) varying dimensions to', 'number of dimensions in the data.')],
  ['[NOTE] p. 70: the ">" after "purchasing power" is a text-layer artefact; the page image has no such mark.',
   '[NOTE] p. 71: the paragraph before "By surface area" ("There are considerable ambiguities ...") is not held because',
   '[NOTE] the figure\'s text is interleaved with it in the text layer. The figures are not held. Numbers checked on the',
   '[NOTE] page image: 9.4; 27,000 percent; 454 percent; 59.4; "volume" is italic on the page.']),
 ('Ch. 2: the six principles of graphical integrity (book p. 77)', 2, '77', '81',
  [('Graphical integrity is more likely to result if these six principles', 'Graphics must not quote data out of context.')],
  []),
 ('Ch. 4 Data-Ink and Graphical Redesign: data-ink and the data-ink ratio (book pp. 93-94)', 2, '93, 94', '97, 98',
  [('A large share of ink on a graphic should present data-information,', 'without loss of data-information.'),
   ('Most of the ink in this graphic is data-ink (the dots and labels', '(the grid ticks and the frame):')],
  ['[NOTE] The data-ink ratio is a display fraction; the text layer prints the fraction bar as "————__________".',
   '[NOTE] Read from the page image (book p. 93, PDF p. 97):',
   '[NOTE]     Data-ink ratio = data-ink / total ink used to print the graphic',
   '[NOTE]                    = proportion of a graphic\'s ink devoted to the non-redundant display of data-information',
   '[NOTE]                    = 1.0 - proportion of a graphic that can be erased without loss of data-information.',
   '[NOTE] "Data-ink" is italic in its defining sentence on the page. The p. 94 sentence introduces a scatterplot (Bonner',
   '[NOTE] 1965, not held).']),
 ('Ch. 4: maximize the data-ink ratio; the two erasing principles (book p. 96)', 2, '96', '100',
  [('Maximizing the Share of Data-Ink', 'The labeled, shaded bar of the bar chart, for example,'),
   ('unambiguously locates the altitude in six separate ways (any five', 'the nuinber itself. That is')],
  ['[NOTE] OCR errors, true readings from the page image (book p. 96): "sometiines" is "sometimes"; "nuinber" is',
   '[NOTE] "number". The bar between the two passages is labelled "35.9" on the page (the text layer reads "659").',
   '[NOTE] "Redundant data-ink" is italic on the page. The sentence continues on p. 97 (next block).']),
 ('Ch. 4: redundant data-ink, continued (book pp. 97 and 100)', 3, '97, 100', '101, 104',
  [('more ways than are needed. Gratuitous decoration and reinforce-', 'ment of the data measures generate much redundant data-ink:'),
   ('Most data representations, however, are of a single, uncomplicated', 'Erase redundant data-ink, within reason.')],
  ['[NOTE] pp. 97-99 (bilateral symmetry, uses of redundancy, Marey\'s train schedule) are not held.']),
 ('Ch. 4: the five principles of the theory of data graphics (book p. 105)', 3, '105', '109',
  [('Five principles in the theory of data graphics produce substantial', 'Revise and edit.')],
  []),
 ('Ch. 5 Chartjunk: Vibrations, Grids, and Ducks: opening (book p. 107)', 3, '107', '111',
  [('The interior decoration of graphics generates a lot of ink that does', 'sional scientific production of data graphics.')],
  ['[NOTE] The text layer prints the chapter number as "§"; the page image reads "5 Chartjunk: Vibrations, Grids, and',
   '[NOTE] Ducks". The book gives no one-sentence definition of chartjunk; this paragraph is where the term is introduced.']),
 ('Ch. 5: the grid (book pp. 112-113, 116)', 3, '112, 113, 116', '116, 117, 120',
  [('One of the more sedate graphical elements, the grid should usually', 'initial plotting of data at home or office rather than for putting'),
   ('into print. Dark grid lines are chartjunk. They carry no informa-', 'to data information.'),
   ('When a graphic serves as a look-up table, then a grid may help', 'than a dark grid.')],
  ['[NOTE] The first two passages are one sentence broken by the page turn (p. 112 to p. 113). "gray grid" is italic on',
   '[NOTE] p. 116.']),
 ('Ch. 5: the duck (book p. 116)', 3, '116', '120',
  [('Self-Promoting Graphics: The Duck', 'itself decoration, just as in the duck data graphic.')],
  ['[NOTE] "duck" is italic on the page.']),
 ('Ch. 5: conclusion (book p. 121)', 3, '121', '125',
  [('Chartjunk does not achieve the goals of its propagators.', 'the grid, and the duck.')],
  ['[NOTE] "intriguing and curiosity-provoking" is italic on the page.']),
]

HDR = '''TUFTE 1983, THE VISUAL DISPLAY OF QUANTITATIVE INFORMATION (FIRST EDITION) - VERBATIM EXCERPTS
====================================================================================================

Transcription rule for this file: every line between [TEXT] and [END TEXT] that is not [...] is an exact,
unaltered slice of the text layer of the PDF named in its block, cut by script (raw[i:j],
books/S58-R1/intake/build-T.py) from the text extracted by pdftotext -layout and saved as raw
T-tufte_2001-part<N>-pdftotext.txt. OCR errors are NOT corrected inside a passage. [...] marks an omission.
Lines beginning [NOTE] are this file's own annotation, are NOT source text, and give the true reading where the
OCR is wrong, read from the page image.
Taken 2 Oct 2026. NOT fetched by a tool: Harsh supplied the book by hand, as four PDFs split from one scan.

PROVENANCE (stated plainly): the PDFs come from Anna's Archive, a shadow library (file names end
"--_Anna_s_Archive.pdf"; md5 ff300c8fa949fefdc4b55643eca4b995 in the file names). The scan itself is an
Internet Archive digitisation ("Digitized by the Internet Archive in 2023 with funding from Kahle/Austin
Foundation", item bwb_T2-EQU-551, block 1). The book is in copyright; this file keeps only short excerpts, held
privately for study and for quotation with attribution. It is not a licensed copy and must not be redistributed.

WORK: Tufte ER. The Visual Display of Quantitative Information. Cheshire, Connecticut: Graphics Press; 1983.
EDITION HELD: the FIRST edition, "Copyright (c) 1983 by Edward R. Tufte", "Tenth printing, March 1990" (copyright
page, block 1, checked against the page image). It is NOT the second edition (Graphics Press, 2001) named in the
intake task. Page numbers below are the 1983 printing's own (running heads, checked on the page images); the
second edition is said to keep the first edition's text and pagination for these chapters, but that was NOT
checked: before a book cites the 2001 edition with these page numbers, check them in a 2001 copy.
LICENCE AS STATED: "Copyright (c) 1983 by Edward R. Tufte / Published by Graphics Press ... ALL RIGHTS RESERVED".
FILES: four PDFs, PDF pages 1-50, 51-100, 101-150, 151-208 of one 208-page scan (PDFsam split); OCR text layer.
Book page = PDF page - 4 throughout the pages held.
TEXT LAYER: OCR, good for running prose, poor for display formulas, figure labels and side notes, which are
interleaved with the text. Every page from which a passage is held was rendered (pdftoppm -r 80) and read
against its passage on 2 Oct 2026: PDF pp. 5, 8, 60, 61, 62, 64, 65, 74, 75, 81, 97, 98, 100, 101, 104, 109,
111, 116, 117, 120, 125 (book pp. 56, 57, 58, 60, 61, 70, 71, 77, 93, 94, 96, 97, 100, 105, 107, 112, 113,
116, 121). OCR errors found in held passages are listed in each block's [NOTE]s.
KEY CONTENT HELD (for S58-R1 C16 and C17):
- Lie Factor = size of effect shown in graphic / size of effect in data (p. 57; formula read from the page
  image). "Lie Factors greater than 1.05 or less than .95 indicate substantial distortion" (p. 57). Fuel-economy
  example: data change (27.5 - 18.0)/18.0 = 53%; lines 0.6 in. and 5.3 in., change 783%; Lie Factor 783/53 = 14.8
  (pp. 57-58). Barrels: 9.4 by area, 59.4 by volume, "a record" (p. 71).
- The six principles of graphical integrity (p. 77), with the first two introduced on p. 56, design variation
  (pp. 60-61; OPEC example 15.1 times), and dimensions (pp. 70-71).
- Data-ink, defined; data-ink ratio = data-ink / total ink used to print the graphic = 1.0 - proportion that can
  be erased without loss of data-information (p. 93; formula read from the page image). "Maximize the data-ink
  ratio, within reason", "Erase non-data-ink, within reason" (p. 96), "Erase redundant data-ink, within reason"
  (p. 100); the five principles: Above all else show the data; Maximize the data-ink ratio; Erase non-data-ink;
  Erase redundant data-ink; Revise and edit (p. 105).
- Chartjunk: introduced p. 107 (decoration that "does not tell the viewer anything new", "all non-data-ink or
  redundant data-ink, and it is often chartjunk"); dark grid lines are chartjunk (p. 113); the duck (p. 116);
  "Forgo chartjunk, including moire vibration, the grid, and the duck" (p. 121).
NOT HELD: everything else, including all figures, chapters 1, 3, 6-9 and the epilogue, ch. 2 pp. 53-55, 59, 62-69,
72-76, ch. 4 pp. 91-92, 95, 98-99, 101-104, ch. 5 pp. 108-111, 114-115, 117-120, notes and index.
Absence of a passage from this file is not absence from the book.
'''
BAR = '=' * 100
out = [HDR]
n = 0
cuts = []
for bi, (head, part, bpp, pdfp, pas, notes) in enumerate(P, 1):
    out.append('\n' + BAR + f'\nBLOCK {bi} - {head}\nBOOK PAGES: {bpp} | PDF PAGES: {pdfp} | PDF FILE: {PDFFILE[part]}\n'
               f'TEXT LAYER: books/S58-R1/intake/raw/{RAWS[part]} | PAGE IMAGES CHECKED: PDF {pdfp}\n' + BAR + '\n')
    out.append('[TEXT]')
    for k, (s, e) in enumerate(pas):
        if k: out.append('[...]')
        c = cut(part, s, e); out.append(c); n += 1; cuts.append((bi, part, c))
    out.append('[END TEXT]')
    out.extend(notes)
dst = R + 'sources/tufte_1983_visual_display.txt'
open(dst, 'w', encoding='utf-8').write('\n'.join(out) + '\n')

# re-check from disk
norm = lambda x: re.sub(r'\s+', ' ', x).strip()
txt = open(dst, encoding='utf-8').read()
blocks = re.split(r'\n' + BAR + r'\nBLOCK (\d+) - [^\n]*\n[^\n]*\nTEXT LAYER: books/S58-R1/intake/raw/(\S+) [^\n]*\n' + BAR + r'\n', txt)
ok = tot = 0
for b in range(1, len(blocks) - 1, 3):
    rawn = norm(open(RAWDIR + blocks[b + 1], encoding='utf-8').read())
    body = re.search(r'^\[TEXT\]\n(.*?)\n\[END TEXT\]$', blocks[b + 2], re.S | re.M).group(1)
    for p in body.split('\n[...]\n'):
        tot += 1; ok += norm(p) in rawn
        if norm(p) not in rawn: print('FAIL block', blocks[b], p[:60])
print('passages written', n, '| verbatim re-check', f'{ok}/{tot}', '| words held', len(' '.join(c for _, _, c in cuts).split()))
