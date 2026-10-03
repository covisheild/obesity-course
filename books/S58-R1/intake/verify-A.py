# Re-parses the group-A source files and tests every [TEXT] passage as a whitespace-normalised
# substring of the raw fetch for the URL on its block's FETCHED line. Run from the repository root.
import json, re, glob

RAW = "books/S58-R1/intake/raw/"
FILES = ["icmje_2026_manuscript_preparation", "sollaci_pereira_2004_imrad",
         "mensh_kording_2017_structuring_papers", "openstax_writing_guide_handbook",
         "gopen_swan_1990_scientific_writing", "plain_language_2011_guidelines",
         "barnett_doubleday_2020_acronyms"]

url2raw = {}
for m in glob.glob(RAW + "A-*.meta.json"):
    meta = json.load(open(m, encoding="utf-8"))
    url2raw[meta["url"]] = m[:-len(".meta.json")] + ".txt"

norm = lambda t: re.sub(r"\s+", " ", t).strip()
total = ok = 0
for f in FILES:
    text = open("sources/%s.txt" % f, encoding="utf-8").read()
    blocks = re.findall(r"FETCHED: (\S+)\n=+\n\n(?:\[NOTE\][^\n]*\n\n)?\[TEXT\]\n(.*?)\n\[END TEXT\]", text, re.S)
    n_text = text.count("[TEXT]\n")
    assert len(blocks) == n_text, (f, len(blocks), n_text)
    good = 0
    for url, passage in blocks:
        raw = norm(open(url2raw[url], encoding="utf-8").read())
        if norm(passage) in raw:
            good += 1
        else:
            print("FAIL", f, url, passage[:80])
    total += len(blocks); ok += good
    print("%-40s %d/%d" % (f, good, len(blocks)))
print("TOTAL %d/%d" % (ok, total))
