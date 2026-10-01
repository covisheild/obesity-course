# Re-parses the group-C2 source files and tests every passage as a whitespace-normalised substring of the
# saved raw fetch for the URL in its block heading. Also checks that each key number quoted in a header is
# present in the file's passages. Run from the repository root.
import re, json, glob

RAW = "books/S58-R1/intake/raw/"
# URL -> raw file, built from the .meta.json written when each raw file was saved
URL2RAW = {}
for m in glob.glob(RAW + "C2-*.meta.json"):
    d = json.load(open(m))
    rawname = m[len(RAW):-len(".meta.json")] + ".txt"
    URL2RAW.setdefault(d["url"], []).append(rawname)

norm = lambda t: re.sub(r"\s+", " ", t).strip()
SEP = "=" * 100
files = ["correll_2020_truncating_yaxis", "heer_bostock_2010_crowdsourcing_perception",
         "weissgerber_2015_beyond_bar_graphs", "bateman_2010_useful_junk", "crameri_2020_misuse_colour",
         "cumming_2007_error_bars", "krishnamurthy_2021_cvd_india"]
# Spot quotes the header promises; each must be inside a passage (not just the header).
KEYS = {
    "correll_2020_truncating_yaxis": ["(F(2,76) = 89, p < 0.0001)", "(F(1,38) = 0.5, p = 0.50)",
        "an increase of 0.36 for", "(F(2,60) = 3.1, p = 0.05)", "(F(1,20) = 11,p = 0.003)",
        "0.002, p = 0.96)", "the second bar is 6 times taller than the ﬁrst bar",
        "I grant arXiv.org a perpetual, non-exclusive license to distribute this article."],
    "heer_bostock_2010_crowdsourcing_perception": ["only 14 out of 3,481 were incorrect (0.4%)",
        "The ranking of types by accuracy is consistent", "position encoding still signiﬁcantly outperformed length encoding",
        "predicts area to perform worse than angle", "Copyright 2010 ACM", "203–212"],
    "weissgerber_2015_beyond_bar_graphs": ["(n = 703)", "85.6% of papers included at least one bar graph",
        "78.1% of studies performed only parametric analyses", "Many different datasets can lead to the same bar graph"],
    "bateman_2010_useful_junk": ["(t 19=0.84, p=.412)", "(t 19=3.37, p=.003)", "(t9=2.56, p=.015)", "(t9=2.41, p=.020)",
        "Twenty participants", "Copyright 2010 ACM"],
    "crameri_2020_misuse_colour": ["worldwide 0.5% of women and 8% of men are subject to a colour-vision deficiency",
        "Creative Commons Attribution 4.0 International License"],
    "cumming_2007_error_bars": ["Rule 1", "Rule 2: the value of n", "SE = SD/√n", "Rule 8",
        "Attribution–Noncommercial–Share Alike 4.0"],
    "krishnamurthy_2021_cvd_india": ["2.76% (n = 2073; 95% confidence interval [CI]: 2.65–2.88)",
        "around 8% in men and 0.5% in women", "| Total | 74986 | 2073 | 2.76 |  |"],
}
total = ok = 0
rows = []
for f in files:
    s = open(f"sources/{f}.txt").read()
    parts = s.split("\n" + SEP + "\nBLOCK ")[1:]
    n = good = 0
    passages = []
    for part in parts:
        head, body = part.split("\n" + SEP + "\n", 1)
        url = head.split("\nFETCHED: ")[1].strip()
        out = []
        for ln in body.split("\n"):
            if ln.startswith("[...]"):
                break
            if ln.startswith("[NOTE]"):
                continue
            out.append(ln)
        passage = "\n".join(out)
        passages.append(passage)
        n += 1
        hit = any(norm(passage) and norm(passage) in norm(open(RAW + r).read()) for r in URL2RAW[url])
        good += hit
        if not hit:
            print("FAIL", f, head.split("\n")[0][:80])
    joined = norm("\n".join(passages))
    kmiss = [k for k in KEYS[f] if norm(k) not in joined]
    rows.append((f, good, n, len(KEYS[f]) - len(kmiss), len(KEYS[f])))
    if kmiss:
        print("KEY MISSING", f, kmiss)
    total += n
    ok += good
for r in rows:
    print("%-45s passages %d/%d   key quotes %d/%d" % r)
print("TOTAL passages %d/%d" % (ok, total))
