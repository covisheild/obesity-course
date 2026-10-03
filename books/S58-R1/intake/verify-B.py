#!/usr/bin/env python3
"""Re-parse each Group B source file from disk and test every passage as a whitespace-normalised
substring of the raw fetch saved for the URL in its block heading."""
import re
REPO = '/home/claude/obesity-course'
RAW = REPO + '/books/S58-R1/intake/raw/'
URLRAW = {
    'https://pmc-oa-opendata.s3.amazonaws.com/PMC4483789.1/PMC4483789.1.xml': ['B-cole_2015_too_many_digits-pmcxml.txt'],
    'https://pmc-oa-opendata.s3.amazonaws.com/PMC5584989.1/PMC5584989.1.xml': ['B-plavensigray_2017_readability-pmcxml.txt'],
    'https://pmc-oa-opendata.s3.amazonaws.com/PMC5584989.1/PMC5584989.1.xml  (MathML: same URL, html format)':
        ['B-plavensigray_2017_readability-pmcxml.txt', 'B-plavensigray_2017_readability-pmcxml-html.txt'],
    'https://www.equator-network.org/wp-content/uploads/2013/07/SAMPL-Guidelines-6-27-13.pdf': ['B-lang_altman_2013_sampl-pdf.txt'],
    'https://pmc-oa-opendata.s3.amazonaws.com/PMC9479524.1/PMC9479524.1.xml': ['B-edwards_2022_readability_formulas-pmcxml.txt'],
}
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
BAR = '=' * 79
total = ok = 0
for key in ['cole_2015_too_many_digits', 'plavensigray_2017_readability', 'lang_altman_2013_sampl',
            'edwards_2022_readability_formulas']:
    txt = open(f'{REPO}/sources/{key}.txt', encoding='utf-8').read()
    # split into blocks: BAR \n heading \n url \n BAR
    blocks = re.split(r'\n' + BAR + r'\n(\d+\. [^\n]*)\n([^\n]*)\n' + BAR + r'\n', txt)
    n = k_ok = 0
    for b in range(1, len(blocks) - 1, 3):
        head, url, body = blocks[b], blocks[b + 1], blocks[b + 2]
        body = body.split('\n' + BAR + '\nOMITTED')[0]
        raws = [norm(open(RAW + f, encoding='utf-8').read()) for f in URLRAW[url]]
        body = '\n'.join(l for l in body.split('\n') if not l.startswith('[NOTE]'))
        pas = []
        pas += re.findall(r'^\[TABLE\]\n(.*?)\n\[END TABLE\]$', body, re.S | re.M)
        pas += re.findall(r'^\[MATHML\]\n(.*?)\n\[END MATHML\]$', body, re.S | re.M)
        rest = re.sub(r'^\[(TABLE|MATHML)\]\n.*?\n\[END (TABLE|MATHML)\]$', '', body, flags=re.S | re.M)
        pas += re.findall(r'^"(.*?)"$\n(?=\n|\Z)', rest + '\n', re.S | re.M)
        leftover = re.sub(r'^".*?"$\n(?=\n|\Z)', '', rest + '\n', flags=re.S | re.M)
        leftover = [l for l in leftover.split('\n') if l.strip() and l.strip() != '[...]']
        if leftover:
            print('  UNPARSED in', key, head, leftover[:3])
        for p in pas:
            n += 1
            hit = any(norm(p) in r for r in raws)
            k_ok += hit
            if not hit:
                print('  FAIL', key, head, p[:80])
    print(f'{key}: {k_ok}/{n}')
    total += n; ok += k_ok
print(f'TOTAL {ok}/{total}')
