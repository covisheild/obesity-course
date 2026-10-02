#!/usr/bin/env python3
"""Re-parse each group F source file from disk and test every [TEXT] passage as a whitespace-normalised
substring of the raw fetch saved for the URL on its block's URL line. Also checks the key coefficient
strings are present in the held text."""
import re
REPO = '/home/claude/obesity-course'
RAW = REPO + '/books/S58-R1/intake/raw/'
URLRAW = {
    'https://eric.ed.gov/?id=ED506404': 'F-flesch_1948-eric-ED506404-record.txt',
    'https://eric.ed.gov/?copyright': 'F-eric-copyright.txt',
    'https://files.eric.ed.gov/fulltext/ED506404.pdf': 'F-flesch_1948-eric-ED506404-pdf.txt',
    'https://pages.stern.nyu.edu/~wstarbuc/Writing/': 'F-nyustern-writing-index.txt',
    'https://pages.stern.nyu.edu/~wstarbuc/Writing/Flesch.htm': 'F-flesch_1979-nyustern.txt',
    'https://web.archive.org/web/2016/http://www.mang.canterbury.ac.nz/writing_guide/writing/flesch.shtml':
        'F-flesch_1979-canterbury-wayback.txt',
}
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
BAR = '=' * 99
total = ok = 0
for key, must in [('flesch_1948_readability_yardstick', ['RE = 206.835 - .846 wl', 'C75 = .0846', '– .846 wl – 1.015 sl']),
                  ('flesch_1979_plain_english', ['Multiply the average word length by 84.6'])]:
    txt = open(f'{REPO}/sources/{key}.txt', encoding='utf-8').read()
    blocks = re.split(r'\n' + BAR + r'\n(\d+\. [^\n]*)\n([^\n]*)\n' + BAR + r'\n', txt)
    n = k = 0
    held = ''
    for b in range(1, len(blocks) - 1, 3):
        head, url, body = blocks[b], blocks[b + 1], blocks[b + 2]
        raw = norm(open(RAW + URLRAW[url], encoding='utf-8').read())
        pas = re.findall(r'^\[TEXT\]\n(.*?)\n\[END TEXT\]$', body, re.S | re.M)
        rest = re.sub(r'^\[TEXT\]\n.*?\n\[END TEXT\]$', '', body, flags=re.S | re.M)
        stray = [l for l in rest.split('\n') if l.strip() and l.strip() != '[...]' and not l.startswith('[NOTE] ')]
        if stray:
            print('  UNPARSED', key, head, stray[:2])
        for p in pas:
            n += 1
            hit = norm(p) in raw
            k += hit
            held += p + '\n'
            if not hit:
                print('  FAIL', key, head, p[:80])
    for m in must:
        print(f'  {key}: contains {m!r}:', m in held)
    print(f'{key}: {k}/{n}')
    total += n
    ok += k
print(f'TOTAL {ok}/{total}')
