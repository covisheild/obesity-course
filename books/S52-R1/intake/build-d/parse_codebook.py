# S52-R1 intake group d: parses the printed code tables of the NHANES BMX_L and DEMO_L codebooks
# (raw text: pdftotext -layout of Harsh's printed PDFs, cropped to the main column) into
# books/S52-R1/intake/build-d/codebook-printed.tsv, one row per printed table row:
# dataset, variable, target, code_or_value, description, count, cumulative, skip_to.
# compare.R then counts the same rows in the .xpt files. Run from the repository root.
import re

RAW = "books/S52-R1/intake/raw/nchs_nhanes_2021_2023_bmx_demo-"
SRC = {"BMX_L": ["BMX_L-codebook.txt"],
       "DEMO_L": ["DEMO_L-codebook-part1.txt", "DEMO_L-codebook-part2.txt", "DEMO_L-codebook-part3.txt"]}
ROW = re.compile(r"^ {6,}(\S+(?: to \S+)?) {2,}(.+?) {2,}(\d+) +(\d+)(?: {2,}(\S+))?\s*$")

out = ["dataset\tvariable\ttarget\tcode_or_value\tdescription\tcount\tcumulative\tskip_to"]
nvars = {}
for ds, parts in SRC.items():
    text = "".join(open(RAW + p, encoding="utf-8").read() for p in parts)
    blocks = re.split(r"\n\s+Variable Name:\s+", text)[1:]
    nvars[ds] = len(blocks)
    for b in blocks:
        var = b.split()[0]
        tgt = re.search(r"Target:\s+(.+)", b).group(1).strip()
        rows = 0
        for line in b.splitlines():
            if line.startswith("http"):
                break
            m = ROW.match(line)
            if m:
                code, desc, cnt, cum, skip = m.groups()
                out.append("\t".join([ds, var, tgt, code, desc.strip(), cnt, cum, skip or ""]))
                rows += 1
        if rows == 0:
            out.append("\t".join([ds, var, tgt, "", "(no code table printed)", "", "", ""]))
open("books/S52-R1/intake/build-d/codebook-printed.tsv", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("variables parsed:", nvars, "table rows:", len(out) - 1)
