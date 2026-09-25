# Re-parses the group-b source files and tests every passage as a whitespace-normalised
# substring of the saved raw fetch for the URL in its block heading. Run from the repo root.
import re
RAW = "books/S57-R1/intake/raw/"
URL2RAW = {
    "https://training.cochrane.org/handbook/current/chapter-06": "cochrane_handbook_ch06-page.txt",
    "https://www.seahq.org/assets/docs/xix_4_chatterjee.pdf": "chatterjee_corral_2017-seahq-pdf.txt",
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=5944406": "chatterjee_corral_2017-efetch.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC4511057/": "adams_2015_bloom-pmcpage.txt",
    "https://api.crossref.org/works/10.1119/1.18809": "hake_1998-crossref-abstract-decoded.txt",
    "https://link.springer.com/article/10.1007/BF00138871": "biggs_1996-springer.txt",
    "https://pmc-oa-opendata.s3.amazonaws.com/PMC4395611.1/PMC4395611.1.xml": "frich_2015-pmcxml.txt",
    "https://pmc-oa-opendata.s3.amazonaws.com/PMC7501065.1/PMC7501065.1.xml": "stoller_2020-pmcxml.txt",
}
norm = lambda t: re.sub(r"\s+", " ", t).strip()
SEP = "=" * 100
files = ["cochrane_handbook_ch06_v6_5", "chatterjee_corral_2017_objectives", "adams_2015_bloom",
         "hake_1998_normalized_gain", "biggs_1996_constructive_alignment",
         "frich_2015_physician_leadership", "stoller_2020_leadership"]
total = ok = 0
for f in files:
    s = open(f"sources/{f}.txt").read()
    parts = s.split("\n" + SEP + "\nBLOCK ")[1:]
    n = good = 0
    for part in parts:
        head, body = part.split("\n" + SEP + "\n", 1)
        url = head.split("\nFETCHED: ")[1].strip()
        lines = body.split("\n")
        out = []
        for ln in lines:
            if ln.startswith("[...]"):
                break
            if ln.startswith("[NOTE]"):
                continue
            out.append(ln)
        passage = "\n".join(out)
        raw = open(RAW + URL2RAW[url]).read()
        n += 1
        if norm(passage) and norm(passage) in norm(raw):
            good += 1
        else:
            print("FAIL", f, head.split("\n")[0])
    print(f"{f}: {good}/{n}")
    total += n; ok += good
# OpenStax 1.4 append
s = open("sources/openstax_intro_stats_2e.txt").read()
k = s.index("SECTION: 1.4 Experimental Design and Ethics")
body = s[k:].split(SEP + "\n", 1)[1]
body = "\n".join(l for l in body.split("\n") if not l.startswith("[NOTE]"))
raw = open(RAW + "openstax_intro_stats_2e-1-4.txt").read()
r = norm(body) in norm(raw) and len(norm(body)) >= len(norm(raw)) - 5
print("openstax_intro_stats_2e (1.4 append):", "1/1" if r else "0/1")
total += 1; ok += int(r)
print(f"TOTAL {ok}/{total}")
