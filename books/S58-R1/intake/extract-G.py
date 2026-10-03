#!/usr/bin/env python3
"""Group G (Cleveland & McGill 1984): makes the two raw text files from the PDF Harsh supplied (2 Oct 2026).
1. raw/G-cleveland_mcgill_1984-pdftotext.txt: `pdftotext -layout` of the whole PDF, unaltered.
2. raw/G-cleveland_mcgill_1984-pdftotext-columns.txt: the same tool and mode (`pdftotext -layout -r 72`), run on
   each page's left and right column separately (-x/-y/-W/-H crop at the page's gutter, found as the x in 300-360
   pt with the fewest word boxes from `pdftotext -bbox`). Needed because -layout prints the journal's two
   columns side by side, so a sentence in one column is interleaved with the other column's lines.
   Each crop's output is preceded by one marker line '##### PDF page N, left|right column (x a-b pt) #####'
   (written by this script, not source text; passages never include it). PDF page N = journal page N + 529."""
import re,subprocess,glob
R='/home/claude/obesity-course/books/S58-R1/intake/raw/'
PDF=glob.glob('/root/.claude/uploads/f2099557-ac04-5a0f-a543-1cd2874da8af/4663e75d-*.pdf')[0]
subprocess.run(['pdftotext','-layout',PDF,R+'G-cleveland_mcgill_1984-pdftotext.txt'],check=True)
bbox=subprocess.run(['pdftotext','-bbox',PDF,'-'],capture_output=True,text=True,check=True).stdout
pages=bbox.split('<page')[1:]
out=[]
for n,p in enumerate(pages,1):
    W,H=[float(v) for v in re.search(r'width="([\d.]+)" height="([\d.]+)"',p).groups()]
    if n==1:
        crops=[('whole page',0,W)]
    else:
        cov=[0]*2000
        for a,b in re.findall(r'xMin="([\d.]+)" yMin="[\d.]+" xMax="([\d.]+)"',p):
            a,b=float(a),float(b)
            if a<25: continue
            for x in range(int(a),int(b)+1): cov[x]+=1
        g=min(range(300,360),key=lambda x:(cov[x],abs(x-326)))
        crops=[('left column',0,g),('right column',g,W)]
    for name,x0,x1 in crops:
        t=subprocess.run(['pdftotext','-layout','-r','72','-f',str(n),'-l',str(n),'-x',str(int(x0)),'-y','0',
                          '-W',str(int(x1-x0)),'-H',str(int(H)+1),PDF,'-'],capture_output=True,text=True,check=True).stdout
        out.append(f'##### PDF page {n}, {name} (x {int(x0)}-{int(x1)} pt) #####\n'+t)
open(R+'G-cleveland_mcgill_1984-pdftotext-columns.txt','w',encoding='utf-8').write('\n'.join(out))
print('pages',len(pages))
