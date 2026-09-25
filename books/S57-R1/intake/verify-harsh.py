# Re-parses the three files written by build-harsh.py and checks every quoted block passage as a
# whitespace-normalised substring of the raw text named for that block. Run from the repo root.
import re, sys
RAW = "books/S57-R1/intake/raw/"
FILES = {
    "sources/pashler_2008_learning_styles.txt": {"usf": "pashler_2008_learning_styles-usf.txt",
                                                 "pdf": "pashler_2008_learning_styles-harsh.txt"},
    "sources/rozenblit_keil_2002_ioed.txt": {"usf": "rozenblit_keil_2002_ioed-efetch.txt",
                                             "pdf": "rozenblit_keil_2002_ioed-harsh-nihms268518.txt"},
    "sources/kotter_1990_what_leaders_do.txt": {"pdf": "kotter_1990_what_leaders_do-harsh.txt"},
}
norm = lambda s: " ".join(s.split())
bar = "=" * 79
total = ok = 0
for f, raws in FILES.items():
    t = open(f, encoding="utf-8").read()
    parts = re.split(r"\n" + bar + r"\n(\d+)\. (.*?)\n(.*?)\n" + bar + r"\n", t)
    for k in range(1, len(parts), 4):
        n, head, where, body = parts[k], parts[k + 1], parts[k + 2], parts[k + 3]
        body0 = body.strip()
        if body0.startswith("[NOTE]"):
            body0 = body0.split("\n\n", 1)[1]
        body0 = re.split(r'"\n+(?:\[\.\.\.\]|\[NOTE\])', body0 + "\n[NOTE]", 1)[0] + '"'
        assert body0.startswith('"') and body0.endswith('"'), (f, n, body0[:80], body0[-80:])
        passage = body0[1:-1]
        rawname = raws["pdf"] if "pdftotext" in where else raws["usf"]
        raw = open(RAW + rawname, encoding="utf-8").read()
        good = norm(passage) in norm(raw)
        total += 1; ok += good
        print(("PASS" if good else "FAIL"), f.split("/")[-1], n, len(norm(passage).split()), "words", rawname)
print(f"verbatim check: {ok}/{total}")
sys.exit(0 if ok == total else 1)
