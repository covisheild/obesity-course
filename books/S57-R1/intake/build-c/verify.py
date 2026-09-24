import os, re, json, sys
sys.path.insert(0, os.path.dirname(__file__))
from cut import norm, raw
from build import U, RF  # rebuilds files deterministically
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
url2raw = {U[k]: RF[k] for k in U}
keys = ['mci_cbme_ug_curriculum_2018_vol1','nmc_cbme_2024','nmc_gmer_2023','mci_gmer_2019_amendment',
        'mci_foundation_course_2019','nmc_miqf_2025','nmc_teq_2022','mahajan_gupta_2024_gmer_cbme']
tot = ok = 0
for k in keys:
    s = open(os.path.join(ROOT, 'sources', k + '.txt'), encoding='utf-8').read()
    blocks = re.findall(r'={79}\n(\d+)\. [^\n]*\n(\S+)\n={79}\n\n\[TEXT\]\n(.*?)\n\[END TEXT\]', s, re.S)
    n = 0
    for no, url, text in blocks:
        tot += 1; n += 1
        r = norm(raw(url2raw[url]))
        if norm(text) in r: ok += 1
        else: print('FAIL', k, no)
    # header quotes: every "..." in header longer than 40 chars that came from raw is re-checked
    header = s.split('\n' + '=' * 79 + '\n', 1)[0]
    print(f'{k}: {n} blocks, {sum(1 for _,u,t in blocks if norm(t) in norm(raw(url2raw[u])))}/{n} pass, {len(s.split())} words')
m = json.load(open(os.path.join(os.path.dirname(__file__), 'manifest.json')))
hq = [x for x in m if x[0] == 'HEADER']
hok = sum(1 for _, _, rf, _, i, j in hq if norm(raw(rf)[i:j]) in norm(raw(rf)))
print(f'passages {ok}/{tot}; header quotes {hok}/{len(hq)} (cut from raw by offset)')
