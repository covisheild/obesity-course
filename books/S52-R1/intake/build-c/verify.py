"""Re-parse the written sources/*.txt files of group c and check every [TEXT] block, and every header
quote in manifest.json, as a whitespace-normalised substring of its raw file. Also re-check the CSV MD5.
Run: python3 /home/claude/work/obesity-course/books/S52-R1/intake/build-c/verify.py
"""
import hashlib, json, os, re

ROOT = '/home/claude/work/obesity-course'
RAW = os.path.join(ROOT, 'books/S52-R1/intake/raw')
HERE = os.path.dirname(os.path.abspath(__file__))
norm = lambda s: ' '.join(s.split())
man = json.load(open(os.path.join(HERE, 'manifest.json')))


def rawtext(name):
    return open(os.path.normpath(os.path.join(RAW, name)), encoding='utf-8').read()


blocks = [m for m in man if m[0] == 'BLOCK']
heads = [m for m in man if m[0] == 'HEADER']
keys = sorted({m[1] for m in blocks})
tot = ok = 0
for k in keys:
    s = open(os.path.join(ROOT, 'sources', k + '.txt'), encoding='utf-8').read()
    found = re.findall(r'={79}\n(\d+)\. [^\n]*\n(\S+)\n={79}\n\n\[TEXT\]\n(.*?)\n\[END TEXT\]', s, re.S)
    mine = [m for m in blocks if m[1] == k]
    assert len(found) == len(mine), (k, len(found), len(mine))
    n = 0
    for (no, loc, text), m in zip(found, mine):
        tot += 1
        r = rawtext(m[2])
        good = norm(text) in norm(r) and norm(text) == norm(r[m[4]:m[5]])
        loc_ok = (loc == m[3]) or (loc == 'file://' + m[3])
        if good and loc_ok:
            ok += 1; n += 1
        else:
            print('FAIL', k, no, loc)
    print(f'{k}: {n}/{len(found)} blocks pass, {len(s.split())} words')
hok = sum(1 for _, k, name, _, i, j in heads if norm(rawtext(name)[i:j]) in norm(rawtext(name)))
print(f'passages {ok}/{tot}; header quotes {hok}/{len(heads)}')
a = hashlib.md5(open(os.path.join(ROOT, 'sources/data/penguins_raw.csv'), 'rb').read()).hexdigest()
b = hashlib.md5(open('/usr/lib/R/site-library/palmerpenguins/extdata/penguins_raw.csv', 'rb').read()).hexdigest()
print('penguins_raw.csv md5', a, 'matches installed' if a == b else 'MISMATCH')
