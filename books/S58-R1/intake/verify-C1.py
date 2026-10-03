#!/usr/bin/env python3
"""S58-R1 intake, group C1: re-parse each written source file and test every passage as a
whitespace-normalised substring of the raw fetch named in its block heading."""
import re, sys, glob

ROOT = '/home/claude/obesity-course'
RAW = ROOT + '/books/S58-R1/intake/raw/'
FILES = ['rougier_2014_ten_rules_figures.txt', 'bergstrom_west_2016_proportional_ink.txt',
         'wilke_2019_dataviz_preface.txt'] + sorted(
         p.split('/')[-1] for p in glob.glob(ROOT + '/sources/wilke_2019_dataviz_ch*.txt'))
RULE = '=' * 79
norm = lambda s: re.sub(r'\s+', ' ', s).strip()

total = ok = 0
for f in FILES:
    text = open(ROOT + '/sources/' + f, encoding='utf-8').read()
    # block heading = RULE / label / url / (... raw file NAME, fetched DATE) / RULE; the passage is
    # everything after it up to the next omission mark "[...]", the next heading, or end of file.
    hp = re.compile(re.escape(RULE) + r'\n(.+?)\n(\S+)\n\(.*?raw file (\S+), fetched [0-9-]+\)\n' + re.escape(RULE) + r'\n')
    hs = list(hp.finditer(text))
    n = good = 0
    for k, m in enumerate(hs):
        label, url, rawname = m.groups()
        stop = hs[k + 1].start() if k + 1 < len(hs) else len(text)
        body = text[m.end():stop]
        cut = body.find('\n[...]\n')
        if cut != -1:
            body = body[:cut]
        body = body.strip()
        assert body.startswith('"') and body.endswith('"'), (f, label)
        passage = body[1:-1]
        n += 1
        rawt = open(RAW + rawname, encoding='utf-8').read()
        if norm(passage) in norm(rawt) and len(passage) > 20:
            good += 1
        else:
            print('FAIL', f, label[:60])
    heads = text.count(RULE) // 2
    if heads != n:
        print('PARSE MISMATCH', f, heads, 'headings,', n, 'parsed')
    print(f'{f}: {good}/{n}')
    total += n; ok += good
print(f'TOTAL {ok}/{total}')
sys.exit(0 if ok == total else 1)
