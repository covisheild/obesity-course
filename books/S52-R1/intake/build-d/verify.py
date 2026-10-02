# S52-R1 intake group d: re-checks the four source files written by build.py. Run from the repo root.
# 1. Every block passage (between the block's opening and closing double quotation marks) must be a
#    whitespace-normalised substring of the raw text named on its RAW: line, and must equal raw[i:j]
#    at the offsets recorded in manifest-d.json.
# 2. Every double-quoted string in each file's header (before the first block) must be a
#    whitespace-normalised substring of one of that file's raw texts, with " / " read as a line break
#    and "..." read as an omission; the few exceptions are listed below with the reason (page image
#    only, or a word the header says is ABSENT, which is then checked to be absent).
import json, re, sys

RAW = "books/S52-R1/intake/raw/"
BAR = "=" * 79
norm = lambda s: " ".join(s.split())
FILES = {
    "sources/herndon_2014_cje.txt": ["herndon_2014_cje-pdftotext-layout.txt", "herndon_2014_cje-pdfinfo.txt",
                                     "herndon_2013_wp322-pdf.txt"],
    "sources/bruford_2020_hgnc.txt": ["bruford_2020_hgnc-pdftotext.txt", "bruford_2020_hgnc-pdfinfo-meta.txt"],
    "sources/nmc_pg_md_community_medicine.txt": ["nmc_pg_md_community_medicine-pdftotext.txt",
                                                 "nmc_pg_md_community_medicine-pdfinfo.txt"],
    "sources/nchs_nhanes_2021_2023_bmx_demo.txt": [
        "nchs_nhanes_2021_2023_bmx_demo-facts.txt", "nchs_nhanes_2021_2023_bmx_demo-printed-vs-computed.txt",
        "nchs_nhanes_2021_2023_bmx_demo-BMX_L-codebook.txt", "nchs_nhanes_2021_2023_bmx_demo-DEMO_L-codebook-part1.txt",
        "nchs_nhanes_2021_2023_bmx_demo-DEMO_L-codebook-part2.txt", "nchs_nhanes_2021_2023_bmx_demo-DEMO_L-codebook-part3.txt",
        "nchs_nhanes_2021_2023_bmx_demo-BMX_L_codebook-uncropped-layout.txt",
        "nchs_nhanes_2021_2023_bmx_demo-DEMO_L_codebook_part1-uncropped-layout.txt",
        "nchs_nhanes_2021_2023_bmx_demo-DEMO_L_codebook_part3-uncropped-layout.txt",
        "nchs_nhanes_2021_2023_bmx_demo-BMX_L_codebook-pdfinfo.txt", "nhanes_s52r1-nchs-dua.txt"],
}
IMAGE_ONLY = {"Medical Council of India": "watermark on the page images; not in the text layer"}
ABSENT = {"sources/bruford_2020_hgnc.txt": {"spreadsheet": ["bruford_2020_hgnc-pdftotext.txt"]}}

total = ok = 0
for f, raws in FILES.items():
    t = open(f, encoding="utf-8").read()
    head = t[:t.find("\n" + BAR + "\n1. ")]
    parts = re.split(r"\n" + BAR + r"\n(\d+)\. (.*?)\nRAW: (\S+) .*?\n" + BAR + r"\n", t)
    for k in range(1, len(parts), 4):
        n, heading, rawname, body = parts[k], parts[k + 1], parts[k + 2], parts[k + 3]
        b = body.strip()
        if b.startswith("[NOTE]"):
            b = b.split("\n\n", 1)[1]
        b = re.split(r'"\n+(?:\[\.\.\.\]|\[NOTE\])', b + "\n[NOTE]", maxsplit=1)[0] + '"'
        assert b.startswith('"') and b.endswith('"'), (f, n, b[:60], b[-60:])
        passage = b[1:-1]
        raw = open(RAW + rawname, encoding="utf-8").read()
        good = norm(passage) in norm(raw)
        total += 1; ok += good
        print(("PASS" if good else "FAIL"), f.split("/")[-1], n, len(passage.split()), "words", rawname)
    # header quotes
    rawall = norm(" ".join(open(RAW + r, encoding="utf-8").read() for r in raws))
    hq = hok = 0
    for q in re.findall(r'"([^"\n]{2,}(?:\n[^"\n]+)*)"', head):
        if q in IMAGE_ONLY:
            print("  header quote (image only):", q, "-", IMAGE_ONLY[q]); continue
        if q in ABSENT.get(f, {}):
            r = " ".join(open(RAW + x, encoding="utf-8").read() for x in ABSENT[f][q]).lower()
            print("  header word asserted absent:", q, "->", "absent" if q not in r else "PRESENT (FAIL)")
            hq += 1; hok += q not in r; continue
        pieces = [p for p in re.split(r"\s*\.\.\.\s*", re.sub(r"\s+/\s+", " ", q)) if p.strip()]
        good = all(norm(p) in rawall for p in pieces)
        hq += 1; hok += good
        if not good:
            print("  header quote NOT FOUND:", q)
    print(f"  header quotes {f.split('/')[-1]}: {hok}/{hq}")
    total += hq; ok += hok

man = json.load(open("books/S52-R1/intake/build-d/manifest-d.json", encoding="utf-8"))
mok = sum(open(RAW + m["raw"], encoding="utf-8").read()[m["i"]:m["j"]] == m["text"] for m in man)
print(f"manifest raw[i:j] == text: {mok}/{len(man)}")
print(f"verbatim check (passages + header quotes): {ok}/{total}")
sys.exit(0 if ok == total and mok == len(man) else 1)
