#!/usr/bin/env python3
"""Cuts the Kincaid 1975 passages from the pdftotext -layout extraction of the PDF Harsh supplied
(2 Oct 2026) and writes sources/kincaid_1975_readability.txt. Every passage is raw[i:j]."""
import re
R='/home/claude/obesity-course/'
raw=open(R+'books/S58-R1/intake/raw/K-kincaid_1975-ucf-pdf-pdftotext.txt',encoding='utf-8').read()
def rx(t):
    return r'\s+'.join(re.escape(w) for w in t.split())
def cut(start,end):
    ms=list(re.finditer(rx(start),raw)); assert len(ms)==1,(start,len(ms))
    i=ms[0].start()
    me=re.search(rx(end),raw[i:]); assert me,(end,)
    return raw[i:i+me.end()]
P=[
 ('Title page of the report and the repository statement',
  [('NAVAL TECHNICAL TRAINING COMMAND','DISTRIBUTION UNLIMITED'),
   ('This Research Report is brought to you for free and open access','lee.dotson@ucf.edu.')]),
 ('Summary (derivation sample, what was recalculated, the simplified formulas)',
  [('Three readability formulas were recalculated to be more suitable for Navy use.','simplified formulas and this is trivial.'),
   ('A number of recent studies have suggested that readability formulas','(average sentence length).')]),
 ('Introduction: the Flesch Reading Ease formula before this study',
  [('Most readability formulas have been derived and validated on the general population.','Navy enlistees reading and comprehending Navy training material.')]),
 ('Results: the regression, the new formulas, the correlations',
  [('A multiple regression statistical procedure was applied','measure.'),
   ('The recalculated Flesch and ARI formulas derived','larger subtracted constant.'),
   ('Table 2 also shows the grade levels of each passage','Tables 1 and 2.'),
   ('Table 4 contains the intercorrelations','inversely proportional to grade level.')]),
 ('Table 3: existing and recalculated formulas',
  [('EXISTING AND RECALCULATED READABILITY FORMULAS FOR THE','grade level is determined from a conversion table.')]),
 ('Appendix B: Instructions for Recalculated Flesch Formula (report pp. 38-39)',
  [('Instructions for Recalculated Flesch Formula','(Syllables/Word) – 16')]),
]
# 'The recalculated' is not unique: use the full phrase
HDR='''KINCAID, FISHBURNE, ROGERS AND CHISSOM 1975, DERIVATION OF NEW READABILITY FORMULAS - VERBATIM EXCERPTS
====================================================================================================

Transcription rule for this file: every line beneath a block heading that does not begin with [NOTE] and comes
before the next [...] is an exact, unaltered slice of the text layer of the PDF named below, cut by script
(raw[i:j], books/S58-R1/intake/build-K.py) from the text extracted by pdftotext -layout and saved as raw
K-kincaid_1975-ucf-pdf-pdftotext.txt. Nothing has been paraphrased or merged. [...] marks an omission; lines
beginning [NOTE] are this file's own annotation and are NOT source text.
Taken in 2 Oct 2026. This source was NOT fetched by a tool: Harsh downloaded the PDF by hand (the earlier fetch
attempts at DTIC, ERIC and UCF STARS failed) and supplied it in the chat.

WORK: Kincaid JP, Fishburne RP Jr, Rogers RL, Chissom BS. Derivation of New Readability Formulas (Automated
Readability Index, Fog Count and Flesch Reading Ease Formula) for Navy Enlisted Personnel. Research Branch
Report 8-75, Naval Technical Training Command, Millington, Tennessee, February 1975. Repository copy: University of
Central Florida STARS, Institute for Simulation and Training, item 56, https://stars.library.ucf.edu/istlibrary/56
(the PDF's own cover page; metadata: creation date 4 June 2019). Also DTIC ADA006655, ERIC ED108134.
FILE: "Derivation Of New Readability Formulas Automated Readability Ind.pdf", 49 pages (cover page, then the
report). The report's own page numbers appear in the text layer (e.g. "14" under Table 3).
LICENCE AS STATED: cover page, "APPROVED FOR PUBLIC RELEASE / DISTRIBUTION UNLIMITED" (block 1); UCF STARS
page, "This Research Report is brought to you for free and open access by the Digital Collections at STARS"
(block 1). A work of the U.S. Navy.
TEXT LAYER: the PDF has a text layer (it is not an image-only scan), but its ocr quality varies: the typed
body text and Table 3 extract cleanly; some pages of the acknowledgements and tables extract with errors
("'l'll'rae readability fot"1llul") and are NOT used here. The numbers in Table 3 were checked against the page
image (report p. 14, PDF page 24) by the conductor on 2 Oct 2026: every coefficient in the text layer
matches the image. The two Appendix B formulas (report p. 39, PDF page 49) were also checked against the page image and match; the rest of Appendix B was read from the text layer only.
NAMING: the report never uses the name "Flesch-Kincaid". It calls the new Flesch formula "New: GL = .39 ..."
(a grade level) and the old one "Old: RE = 206.835 ..." (a Reading Ease score). Later writers call the new GL
formula the Flesch-Kincaid grade level; a book must not attribute that name to this report's wording.
KEY NUMBERS HELD (for C10): old Flesch Reading Ease, RE = 206.835 - 1.015 (words/sentence) - .836
(syllables/100 words), "grade level is determined from a conversion table"; new, GL = .39 (words/sentence) +
11.8 (syllables/word) - 15.59; simplified GL = .4 (words/sentence) + 12 (syllables/word) - 16; 531 Navy enlisted
personnel; 18 test passages; counting rules for words, sentences and syllables (Appendix B).
DISCREPANCY (found 2 Oct 2026 at intake, settled the same day): this report's Table 3 prints the old formula's
syllable term as .836 (syllables/100 words); the page image shows .836. Flesch's own article gives .846
(flesch_1948_readability_yardstick, a public-domain reprint: "RE = 206.835 - .846 wl - 1.015 sl", consistent with
his worked tables), as do Plaven-Sigray 2017 and Edwards 2022 (84.6 per syllable-per-word). The .836 here is a
misprint in this report: quote Table 3 only for the new GL formula, and take the Reading Ease formula from Flesch.
WHAT IS HELD: blocks 1-6 below. NOT HELD: the acknowledgements, tables 1, 2 and 5, the ARI and Fog Count
instructions, the method and reading-test details, Appendices A and the other appendices.
Absence of a passage from this file is not absence from the report.
'''
BAR='='*100
out=[HDR]
n=0
for bi,(head,pas) in enumerate(P,1):
    out.append('\n'+BAR+f'\nBLOCK {bi} - {head}\nFETCHED: PDF text layer, books/S58-R1/intake/raw/K-kincaid_1975-ucf-pdf-pdftotext.txt\n'+BAR+'\n')
    out.append('[TEXT]')
    for k,(s,e) in enumerate(pas):
        if k: out.append('[...]')
        out.append(cut(s,e)); n+=1
    out.append('[END TEXT]')
open(R+'sources/kincaid_1975_readability.txt','w',encoding='utf-8').write('\n'.join(out)+'\n')
print('passages',n)
