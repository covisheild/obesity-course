# Group c intake: cut passages from saved raw TinyFish fetch text by script (raw[i:j]).
import os, re, json
RAW = os.path.join(os.path.dirname(__file__), '..', 'raw')
def raw(name): return open(os.path.join(RAW, name), encoding='utf-8').read()
def cut(name, start, end, after=0, nth=1):
    t = raw(name)
    i = after - 1
    for _ in range(nth):
        i = t.find(start, i + 1)
        if i < 0: raise SystemExit(f'start not found in {name}: {start!r}')
    j = t.find(end, i)
    if j < 0: raise SystemExit(f'end not found in {name}: {end!r}')
    return t[i:j + len(end)], i, j + len(end)
def norm(s): return re.sub(r'\s+', ' ', s).strip()
RULE = '=' * 79
def block(n, title, url, text, kind='TEXT'):
    return f"\n{RULE}\n{n}. {title}\n{url}\n{RULE}\n\n[{kind}]\n{text}\n[END {kind}]\n"
