# Source intake log · S58-R1 · group C1 (figure design: Rougier 2014, Wilke 2019, Bergstrom and West)

One pass, 2026-10-02, against the three C1 lines of `READY.md` "To obtain" (Rougier, Droettboom and
Bourne 2014; Wilke, *Fundamentals of Data Visualization*, ch. 3, 4, 5, 7, 9, 17, 19, 20, 22, 23, 24, 26,
27, 28, 29; Bergstrom and West, principle of proportional ink). Tool for every stored passage:
`mcp__TinyFish__fetch_content` (markdown). Each URL's `text` was taken unchanged from the tool's own
result (the harness's tool-result file, or the result as recorded in this agent's transcript) by
`intake/extract-C1.py` and written to `raw/C1-<citekey>-<route>.txt`, with a `.meta.json` beside it
(url, format, selectors, date). Every passage was cut by script as one contiguous `raw[i:j]`, located
by start and end anchors (`intake/build-C1.py`), and every written file was then re-parsed and each
passage tested as a whitespace-normalised substring of the raw file named in its block heading
(`intake/verify-C1.py`); a second check confirmed each parsed passage has exactly the length that
was cut. No WebFetch output is stored anywhere; nothing was fetched with curl, wget or a Python HTTP
client. Rougier's identifiers were confirmed with the PubMed ID converter. Nothing was committed;
`sources/INDEX.yml`, `library.bib` and `SOURCES.md` were not touched (entries in `fragment-C1.md`).

**Verbatim check: 57 of 57.** **Obtained: 3 of 3**, in whole text (reference lists and images
excepted). Eighteen source files: one per Wilke chapter (fifteen), plus Wilke's Preface (not
asked for; added for C20, see below), Rougier, and Bergstrom and West.

**Site terms.** clauswilke.com and callingbullshit.org both return 404 for robots.txt; neither
site has a terms page forbidding automated access (callingbullshit.org's footer disclaimer says it
"is intended for personal educational use"). journals.plos.org and the PMC open-data bucket are
the hosts previous intakes used. No JSTOR, ACM or India Code fetch was made.

| Source | URL fetched (stored passages) | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Rougier, Droettboom, Bourne 2014 *PLoS Comput Biol* 10(9):e1003833 (PMID 25210732, PMC4161295) | https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833 (whole text); https://pmc-oa-opendata.s3.amazonaws.com/PMC4161295.1/PMC4161295.1.xml (figure titles) | 9 | 9/9 | "This is an open-access article, free of all copyright, and may be freely reproduced, distributed, transmitted, modified, built upon, or otherwise used by anyone for any lawful purpose. The work is made available under the Creative Commons CC0 public domain dedication." (article page) | `rougier_2014_ten_rules_figures` |
| Wilke, *Fundamentals of Data Visualization*, ch. 3, 4, 5, 7, 9, 17, 19, 20, 22, 23, 24, 26, 27, 28, 29 (author's manuscript online) | https://clauswilke.com/dataviz/<chapter>.html, fifteen pages, each fetched twice (whole page; then scoped to `p.caption` for the captions); welcome page https://clauswilke.com/dataviz/ for the licence | 44 (15 welcome-licence, 15 chapter bodies, 14 caption sets; ch. 5 has no captions) | 44/44 | "This work is licensed under the Attribution-NonCommercial-NoDerivatives 4.0 International License." (welcome page) | `wilke_2019_dataviz_ch03`, `_ch04`, `_ch05`, `_ch07`, `_ch09`, `_ch17`, `_ch19`, `_ch20`, `_ch22`, `_ch23`, `_ch24`, `_ch26`, `_ch27`, `_ch28`, `_ch29` |
| Wilke, Preface (extra) | https://clauswilke.com/dataviz/preface.html | 2 | 2/2 | as above | `wilke_2019_dataviz_preface` |
| Bergstrom and West, "The principle of proportional ink" (Calling Bullshit, Tools) | https://callingbullshit.org/tools/tools_proportional_ink.html (scoped to `body`, to keep headings and footer) | 2 | 2/2 | No licence stated. Footer: "Copyright © Calling Bullshit 2017-2019" | `bergstrom_west_2016_proportional_ink` |

## What the files say about themselves (headers carry the detail)

- **Rougier: licence is CC0, not CC BY 4.0** as READY.md guessed. The article page drops each figure's
  number and title, so the Figure 1-8 titles are held separately from the PMC XML (blocks 2a-2h); the
  caption paragraphs sit under their rules in block 1. The Figure 3 caption's inline maths is lost
  ("(, , , )") and is not held.
- **Wilke: CC BY-NC-ND 4.0.** Every header says the file is a verbatim excerpt held privately for
  study and attributed quotation, never edited or adapted. The website is "the complete author
  manuscript before final copy-editing"; the headers say to cite the website version. The website
  gives **no year**: 2019 is READY.md's print-edition year and is marked as such; no subtitle, place
  or ISBN was entered (none was checked).
- Wilke ch. 22: the body extraction lacks the chapter heading and its sections are unnumbered; the
  captions fetch (scoped to `h1` too) confirms "# 22 Titles, captions, and tables". COVERAGE.md's
  "§22.3 Tables" is the third section, "Tables" (the six table-layout rules are held).
- Wilke ch. 4: a stray R build message on the website ("## Warning: package 'sf' was built under R
  version 3.5.2") is omitted, marked. Ch. 19's Table 19.1 (Okabe-Ito palette) and ch. 27's Table 27.1
  (file formats) are held as extracted (one cell per line); headers say so.
- Bergstrom and West: the page has **no byline and no date**. Authors are from the site footer;
  **the year 2016 comes only from Wilke's ch. 17 reference list**, and the header and .bib note say so.
  The example charts are images and are not held; the companion pages (misleading axes, log scales)
  were not fetched.

## For the conductor and Harsh

1. **Nothing in C1 needs Harsh to download anything.** All three sources are held in whole text.
2. **Decision for Harsh (C20):** INVENTORY C20 says "any tool (a spreadsheet will do)". Wilke's
   Preface says "Excel is an interactive plot program as well and is not recommended for figure
   preparation (or data analysis)", and ch. 28 argues for reproducible, scripted figures. The
   drafter will need to either drop "a spreadsheet will do" or present it as a deliberate departure
   from the cited source. The Preface is filed (`wilke_2019_dataviz_preface`) so either choice can be
   cited.
3. **Licence constraint for drafters:** Wilke is NoDerivatives. Course text may quote short
   attributed passages and cite; it may not adapt his figures or rework his prose. Bergstrom and West
   state no licence (all rights reserved): quote briefly, with attribution.
4. READY.md's Wilke line can record "CC BY-NC-ND 4.0 (confirmed on the welcome page 2026-10-02)";
   Rougier's line should change "CC BY 4.0 (to confirm)" to "CC0 (confirmed)"; Bergstrom and West's
   "to confirm" becomes "no licence stated; © Calling Bullshit 2017-2019".
