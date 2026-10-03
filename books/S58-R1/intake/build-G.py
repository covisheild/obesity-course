#!/usr/bin/env python3
"""Cuts the Cleveland & McGill 1984 passages from the column-by-column `pdftotext -layout` extraction of the PDF
Harsh supplied (2 Oct 2026) and writes sources/cleveland_mcgill_1984_graphical_perception.txt.
Every passage is raw[i:j] of raw/G-cleveland_mcgill_1984-pdftotext-columns.txt (made by extract-G.py).
Start and end phrases are matched whitespace-flexibly; a hyphen at a line break is written 'neces- sary.'
After writing, the script re-reads the source file and checks every passage (1) as a whitespace-normalised
substring of the columns raw and (2) line by line against the whole-page `pdftotext -layout` raw."""
import re,json
R='/home/claude/obesity-course/'
RAWP='books/S58-R1/intake/raw/G-cleveland_mcgill_1984-pdftotext-columns.txt'
WHOLEP='books/S58-R1/intake/raw/G-cleveland_mcgill_1984-pdftotext.txt'
OUTP='sources/cleveland_mcgill_1984_graphical_perception.txt'
raw=open(R+RAWP,encoding='utf-8').read()
whole=open(R+WHOLEP,encoding='utf-8').read()
MARK=[(m.start(),int(m.group(1))) for m in re.finditer(r'##### PDF page (\d+),',raw)]
def page_of(i):
    return [p for s,p in MARK if s<=i][-1]
def rx(t):
    return r'\s+'.join(re.escape(w) for w in t.split())
def cut(start,end):
    ms=list(re.finditer(rx(start),raw)); assert len(ms)==1,(start,len(ms))
    i=ms[0].start()
    me=re.search(rx(end),raw[i:]); assert me,(end,)
    s=raw[i:i+me.end()]
    assert '#####' not in s,(start,'crosses a page/column marker')
    return s,page_of(i)
# (block heading, [(start,end),...], [NOTE lines])
P=[
 ('Cover page of the Taylor & Francis download (citation, DOI, terms of use) and the article\'s copyright line',
  [('This article was downloaded by: [Michigan State University]','http://dx.doi.org/10.1080/01621459.1984.10478080'),
   ('This article may be used for research, teaching, and private study purposes.','and-conditions'),
   ('0 Journal of the American Statistical Association','Applications Section')],
  ['The cover page (PDF p. 1) is the publisher\'s, added at download; it is not part of the 1984 article.',
   'OCR: "0 Journal of the American Statistical Association" is, on the page image (p. 531), "(c) Journal of the American',
   'Statistical Association" (the copyright sign).']),
 ('Abstract',
  [('The subject of graphical methods for data analysis and','framed-rectangle charts.')],
  ['The line "Downloaded by [Michigan State University] at 01:41 28 February 2015" inside this block (and twice in',
   'block 5) is the download stamp printed in the page margin, not article text.',
   'OCR: "divided barcharts" is "divided bar charts" on the page image (p. 531). Throughout this file the text layer',
   'prints a hyphen where the page has an em dash (e.g. "perception-the visual decoding", "ranks-3, 5 , and 6-have").']),
 ('Section 2: the ten elementary perceptual tasks (Figure 1)',
  [('Figure 1 illustrates 10 elementary perceptual tasks that','people use to extract quantitative information from'),
   ('graphs. (Color saturation is not illustrated, to avoid the','color reproduction.)'),
   ('We do not pretend that our list is exhaustive; for example, color hue','rather than real variables.')],
  ['Figure 1 (p. 532, image checked) shows ten labelled panels: position common scale, position non-aligned scales,',
   'length, direction, angle, area, volume, curvature, shading, color saturation. The figure itself is not held.']),
 ('Section 3: ordering the elementary perceptual tasks by the accuracy of extraction (the ranking)',
  [('3. THEORY: ORDERING THE ELEMENTARY','quan- tities.'),
   ('Our premise, however, is this:','other graphical f o r m (with the same quantitative in-'),
   ('formation) will result in better organization and in-','accuracy of judgments.'),
   ('The following are the 10 elementary tasks in Figure 1,','6. Shading, color saturation'),
   ('Three of the ranks-3, 5 , and 6-have more than one','separate the ties.'),
   ('In the ordering of perceptual tasks, length judgments','experimental results.')],
  ['OCR: "an ordering of the I0" is "an ordering of the 10" on the page image (p. 535).',
   'OCR: "graphical f o r m" is "graphical form" (italic) on the page image (p. 535); the premise is set in italics.',
   'The six-rank list was checked against the page image (p. 536): it reads exactly 1. Position along a common scale;',
   '2. Positions along nonaligned scales; 3. Length, direction, angle; 4. Area; 5. Volume, curvature; 6. Shading,',
   'color saturation ("5 ." in the text layer is "5." on the page). The ordering is the authors\' HYPOTHESIS; the',
   'paper\'s two experiments test only position against length and position against angle (blocks 5-7).']),
 ('Section 4.1-4.3: the two experiments, their subjects and the accuracy measure',
  [('We began checking the hypothesized ordering by run-','correctly predicted the outcome.'),
   ('In one experiment 55 subjects were shown the five','Hence we call this the po- sition-length experiment.'),
   ('In this position-length experiment, the values involved','five judgment types.'),
   ('In the second experiment 54 subjects judged the two','we call this the position- angle experiment.'),
   ('For the values that actually arose in the constrained random se-','ratios ranged from 10.0 to 99.7%.'),
   ('In the position-length experiment, the judgments of','51 subjects remained for analysis.'),
   ('We did not detect any differences in the accuracies of','the judgments of the nontechnical and technical groups.'),
   ('To measure accuracy we used','tended to change by factors less than 10.'),
   ('Principally because of the outliers, we estimated the lo-','(Mosteller and Tukey 1977).'),
   ('subjects were judging. The striking pattern is that the log','pie chart more accurate on average than the bar chart.')],
  ['OCR, checked against the page image (p. 539): "8 t x 11 page" is "8 1/2 x 11 page"; "s i = 10 x 10(i-l)\'lz" is',
   's_i = 10 x 10^((i-1)/12) (i = 1, ..., 10; 10 x 10^(9/12) = 56.2 agrees); ".18to .83" is ".18 to .83";',
   '"56.2.Subjects" is "56.2. Subjects". The numbers 55, 54, 20 graphs, 10.0 to 99.7%, four and three deleted, 51 match.',
   'OCR, checked against the page image (p. 540): the accuracy measure "logz( I judged percent - true percent I + I/@."',
   'is log2(|judged percent - true percent| + 1/8); "least accurate (3.)" is "least accurate (5).)"; 51, 3 of the 40',
   'match.']),
 ('Section 4.3 results: position against length, position against angle, and large errors',
  [('The top panel of Figure 16 shows that average errors','is statistically sig- nificant.'),
   ('The top panel of Figure 17 shows a summary of the','large errors that occurred for each of the'),
   ('judgment types. Seventy-eight percent of the large errors','is 7.3 times that for the position judgments.')],
  ['OCR, checked against the page image (p. 541, also at 200 dpi): "a factor of 2\'.32 = 2.5" is 2^1.32 = 2.5;',
   '"a factor of 2.97 = 1.96" is 2^.97 = 1.96; "greater than 4-" is "greater than 4."; "Figure l7" is "Figure 17".',
   'The numbers .05, 1.32, .51, 1.4, 40%-250%, .97, 2,550, 136 match the image. Page 542 (image checked): 5.3, 219,',
   '4,080, 7.3 and the words "Seventy-eight" and "Eighty-eight" match.']),
 ('Section 4.5: Summary of the Experiments',
  [('4.5 Summary of the Experiments','the theory seems appropriate.')],
  ['Checked against the page image (p. 544): 51, 1/8, 1.4 to 2.5, 1.96, 95%, 25-50 match. The lone ";" line inside',
   'the passage is a text-layer artifact; the page has no such mark.']),
 ('Section 5 and 5.1: designing graphs from the ordering; pie charts and divided bar charts replaced by dot charts',
  [('The mode of graph design that we advocate is the con-','detect patterns and organize the quantitative information.'),
   ('For certain types of data structures, one cannot always','25 or 50% are also reasonable simple choices.'),
   ('Actually we prefer dot charts, which are introduced','reader to Cleveland 1983.)'),
   ('Figure 22 is a pie chart. What is the ordering of the','based on angle judgments.'),
   ('A divided bar chart can always be replaced by a','to a grouped bar chart. To'),
   ('illustrate the replacement of divided bar charts, consider','increased accuracy of percep- tions.'),
   ('Our analysis has provided, in a sense, a resolution of','demonstrably better.')],
  ['Checked against the page images (pp. 544-545): 0 to 100%, 0 to 25 or 50%, Figures 16, 17, 20, 22-25 match.',
   'OCR: "For\\each" is "For each" (a speck on the page). Figures 22-25 (pie chart, dot chart, divided bar chart,',
   'grouped dot chart) are not held.']),
 ('Section 5.3: shading at the bottom of the hierarchy',
  [('To judge the values of a real variable encoded on a','bottom of our perceptual hierarchy.')],
  []),
 ('Section 6: Perspectives, realism, and criticism (the paper\'s conclusions)',
  [('is accumulated. The outcomes of the two experiments','appears nec- essary.'),
   ('The ordering of the perceptual tasks does not provide','judgment in designing a graph.'),
   ('We cannot realistically claim to','much overlap.'),
   ('Whatever the limitations of the current theory, it ap-','other areas of science.')],
  ['Checked against the page images (pp. 552-553): 0 cm, 2.8 cm, 5.6 cm, Types 1-3, "10 basic" match. The first',
   'passage begins mid-sentence: the sentence starts at the foot of the left column of p. 552, which is not held.']),
]
HDR='''CLEVELAND AND McGILL 1984, GRAPHICAL PERCEPTION - VERBATIM EXCERPTS
====================================================================================================

Transcription rule for this file: every line beneath a block heading that does not begin with [NOTE] and comes
before the next [...] or [END TEXT] is an exact, unaltered slice of the text layer of the PDF named below, cut by
script (raw[i:j], books/S58-R1/intake/build-G.py) from the text extracted by pdftotext -layout. Nothing has been
paraphrased, merged or corrected: OCR errors are left in the passages and the correct reading is given in a
[NOTE]. [...] marks an omission; lines beginning [NOTE] are this file's own annotation and are NOT source text.
Taken 2 Oct 2026. This source was NOT fetched by a tool: Harsh downloaded the PDF by hand and supplied it in the
chat (JSTOR and the publisher's site may not be fetched automatically for this course).

WORK: Cleveland WS, McGill R. Graphical perception: theory, experimentation, and application to the development of
graphical methods. Journal of the American Statistical Association 1984 Sep;79(387):531-554 (Applications Section).
doi:10.1080/01621459.1984.10478080. Authors at AT&T Bell Laboratories, Murray Hill, NJ.
FILE: a Taylor & Francis download, 25 PDF pages: a publisher cover page ("This article was downloaded by: [Michigan
State University] On: 28 February 2015", block 1), then the article, journal pp. 531-554 = PDF pp. 2-25
(PDF page = journal page - 529). Scanned pages with an OCR text layer ("Acrobat 5.0 Paper Capture"); each article
page carries a margin stamp "Downloaded by [Michigan State University] at 01:41 28 February 2015".
SHA-256 of the PDF: 804f08bebc1929d7eeabce9d55b9796d9a3b67d7b429b1f9956e8e91eab5def3.
COPYRIGHT AND TERMS AS STATED: the article's first page, "(c) Journal of the American Statistical Association"
(block 1); the publisher's cover page, "This article may be used for research, teaching, and private study
purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic
supply, or distribution in any form to anyone is expressly forbidden" (block 1). Publisher copyright (American
Statistical Association; published by Taylor & Francis). NOT open access. Held here as short verbatim excerpts,
privately, for study and for quotation with citation in the course; never to be redistributed as a whole.
EXTRACTION: `pdftotext -layout` prints the journal's two columns side by side, so the whole-page extraction
(books/S58-R1/intake/raw/G-cleveland_mcgill_1984-pdftotext.txt) interleaves the columns. The passages are therefore
cut from books/S58-R1/intake/raw/G-cleveland_mcgill_1984-pdftotext-columns.txt: the same tool and mode run on each
page's left and right column separately (crop at the gutter; books/S58-R1/intake/extract-G.py). Each passage was
also checked line by line against the whole-page extraction (every line found there).
OCR CHECK: every block that carries a number or the ranking was checked against the page image (pdftoppm -r 80;
the exponents on p. 541 and two lines on pp. 539-540 also at 200 dpi): pages 531 (abstract and copyright line),
532 (Figure 1 and the ten tasks), 535-537 (the ranking), 539-542 (design, subjects, accuracy measure, results),
544-545 (summary, dot charts), 547 (shading), 552-553 (conclusions), and the cover page. OCR errors found in the
held passages: "I0" for 10 (p. 535); "8 t x 11" for 8 1/2 x 11, the formula s_i, ".18to", "56.2.Subjects"
(p. 539); the accuracy measure "logz( I ... I + I/@." for log2(|judged percent - true percent| + 1/8) and "(3.)"
for "(5).)" (p. 540); "2'.32" for 2^1.32, "2.97" for 2^.97, "4-" for "4.", "l7" for 17 (p. 541); "barcharts",
"0 Journal" for (c) Journal (p. 531); "For\\each" (p. 545); a stray ";" (p. 544); em dashes as hyphens throughout.
Every other number in the held passages matched the image. Each error is noted under its block.
KEY CONTENT HELD (for S58-R1 C14): the abstract; the ten elementary perceptual tasks and the hypothesised order,
most to least accurate: 1 position along a common scale; 2 positions along nonaligned scales; 3 length, direction,
angle; 4 area; 5 volume, curvature; 6 shading, color saturation (ranks 3, 5 and 6 are ties); position-length
experiment (55 subjects, 51 analysed; 5 judgment types on bar charts, types 1-3 position, 4-5 length) and
position-angle experiment (54 subjects, 51 analysed; pie chart vs bar chart); accuracy = midmean of
log2(|judged - true| + 1/8); length errors 40%-250% larger than position (factors 1.4 to 2.5); angle errors a
factor of 1.96 larger than position; the pie chart more accurate than the bar chart in only 3 of 40 cases; large
errors 5.3 (length) and 7.3 (angle) times as frequent as for position; the recommendations: replace pie charts and
divided bar charts by (grouped) dot charts or bar charts, "neither graphical form should be used"; the stated
limits of the theory.
WHAT IS NOT HELD: the introduction after the abstract, the descriptions of graph forms in section 2, the
psychophysics (Stevens's power law, Baird, Weber's law) and the framed rectangle in section 3, the bias analysis,
the bootstrap (section 4.4), sections 5.2-5.4 except one sentence of 5.3, most of section 6, all figures, the
references. Absence of a passage from this file is not absence from the paper.
'''
BAR='='*100
def norm(t): return ' '.join(t.split())
out=[HDR]; n=0; log=[]
for bi,(head,pas,notes) in enumerate(P,1):
    cuts=[cut(s,e) for s,e in pas]
    pg=sorted({p for _,p in cuts})
    where=', '.join(('cover page (PDF p. 1)' if p==1 else f'journal p. {p+529} (PDF p. {p})') for p in pg)
    out.append('\n'+BAR+f'\nBLOCK {bi} - {head}\nWHERE: {where}\nFROM: PDF text layer, {RAWP}\n'+BAR+'\n')
    out.append('[TEXT]')
    for k,((s,e),(t,p)) in enumerate(zip(pas,cuts)):
        if k: out.append('[...]')
        out.append(t); n+=1
        log.append({'block':bi,'pdf_page':p,'journal_page':(p+529 if p>1 else None),'start':s,'end':e,
                    'chars':len(t),'words':len(t.split())})
    out.append('[END TEXT]')
    for note in notes: out.append('[NOTE] '+note)
open(R+OUTP,'w',encoding='utf-8').write('\n'.join(out)+'\n')
# ---- verbatim re-check, from the written file ----
txt=open(R+OUTP,encoding='utf-8').read()
body=txt[len(HDR):]
blocks=re.findall(r'\[TEXT\]\n(.*?)\n\[END TEXT\]',body,flags=re.S)
passages=[p for b in blocks for p in b.split('\n[...]\n')]
nraw=norm(raw); wl=[norm(l) for l in whole.splitlines()]
ok1=sum(norm(p) in nraw for p in passages)
ok2=0
for p in passages:
    lines=[norm(l) for l in p.splitlines() if l.strip()]
    if all(any(l in w for w in wl) for l in lines): ok2+=1
    else: print('whole-layout miss in passage starting',p[:60].strip())
for x,p in zip(log,passages): x['verbatim_columns_raw']=norm(p) in nraw
json.dump(log,open(R+'books/S58-R1/intake/raw/G-cutlog.json','w'),indent=1)
print('passages',n,'blocks',len(blocks),'words',sum(x['words'] for x in log))
print(f'verbatim vs columns raw {ok1}/{len(passages)}; every line found in whole-page -layout raw {ok2}/{len(passages)}')
