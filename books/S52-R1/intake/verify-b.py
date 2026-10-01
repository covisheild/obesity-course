# Re-parses the group-b source files written by build-b.py and tests every passage as a
# whitespace-normalised substring of the saved raw fetch named in its block heading (RAW:), and
# checks that the block's FETCHED: URL is the URL recorded for that raw file. Run from the repo root:
#   python3 books/S52-R1/intake/verify-b.py
import json, re

RAW = "books/S52-R1/intake/raw/"
SEP = "=" * 100
norm = lambda t: re.sub(r"\s+", " ", t).strip()
files = ["ziemann_2016", "herndon_2013_wp322", "phe_2020_delayed", "trisovic_2022", "peng_2011",
         "sandve_2013", "wilson_2017", "wickham_2014_tidy", "broman_woo_2018"]
total = ok = 0
for f in files:
    s = open(f"sources/{f}.txt").read()
    parts = s.split("\n" + SEP + "\nBLOCK ")[1:]
    n = good = 0
    for part in parts:
        head, body = part.split("\n" + SEP + "\n", 1)
        url = head.split("\nFETCHED: ")[1].split("\n")[0].strip()
        rawname = head.split("\nRAW: ")[1].split("\n")[0].strip()
        meta = json.load(open(RAW + rawname[:-4] + ".meta.json"))
        assert meta["url"] == url, (f, rawname, meta["url"], url)
        out = []
        for ln in body.split("\n"):
            if ln.startswith("[...]"):
                break
            if ln.startswith("[NOTE]"):
                continue
            out.append(ln)
        passage = "\n".join(out)
        raw = open(RAW + rawname).read()
        n += 1
        if norm(passage) and norm(passage) in norm(raw):
            good += 1
        else:
            print("FAIL", f, head.split("\n")[0])
    print(f"{f}: {good}/{n}")
    total += n
    ok += good
print(f"TOTAL {ok}/{total}")
