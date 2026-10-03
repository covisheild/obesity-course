# Re-parses each written source file, takes every passage between the markers, and tests it as a
# whitespace-normalised substring of the saved raw fetch for the URL in its block heading.
import json, re, glob
ROOT = "/home/claude/work/obesity-course/"
RAW = ROOT + "books/S52-R1/intake/raw/"
norm = lambda t: re.sub(r"\s+", " ", t).strip()
url2raw = {}
for m in glob.glob(RAW + "*.meta.json"):
    u = json.load(open(m))["url"]
    url2raw.setdefault(u, m[:-len(".meta.json")] + ".txt")
keys = ["r4ds_2e", "r_intro_manual", "r_lang_def", "swc_r_gapminder", "dc_spreadsheets", "tidyverse_style"]
tot = ok = 0
for k in keys:
    s = open(ROOT + "sources/" + k + ".txt").read()
    blocks = re.findall(r"\nBLOCK (\d+) - [^\n]*\nFETCHED: (\S+)\n=+\n--- passage begins ---\n(.*?)\n--- passage ends ---\n", s, re.S)
    n = sum(1 for b in blocks if norm(b[2]) in norm(open(url2raw[b[1]]).read()))
    nwords = sum(len(b[2].split()) for b in blocks)
    print(f"{k}: {n}/{len(blocks)} passages verbatim; {nwords} words held; file words {len(s.split())}")
    tot += len(blocks); ok += n
print(f"TOTAL {ok}/{tot}")
