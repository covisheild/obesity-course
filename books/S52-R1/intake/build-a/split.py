# Splits a saved TinyFish fetch_content result (JSON) into one raw text file per URL, text unchanged.
# usage: python split.py <saved.json> <name-for-url1> <name-for-url2> ...
import json, sys
RAW = "/home/claude/work/obesity-course/books/S52-R1/intake/raw/"
d = json.load(open(sys.argv[1]))
names = sys.argv[2:]
for r, n in zip(d["results"], names):
    open(RAW + n + ".txt", "w").write(r["text"])
    meta = {k: v for k, v in r.items() if k != "text"}
    json.dump(meta, open(RAW + n + ".meta.json", "w"), indent=1)
    print(n, r["url"], len(r["text"]))
print("errors:", d.get("errors"))
