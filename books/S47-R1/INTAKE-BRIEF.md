# Intake brief · S47-R1 (four parallel intake subagents, groups A–D)

You take in the sources of your group (listed in your prompt) for Book 5 = S47-R1, to the intake
checklist. Repository: `/home/claude/obesity-course`, branch `book/S47-R1`. Do not commit, push or
switch branches. **No `rm` anywhere in the repository.** Absolute paths only.

## Read first (and nothing else from the repo)
- `/home/claude/obesity-course/PIPELINE.md` lines 103–160 (the source gate and the intake checklist).
- `/home/claude/obesity-course/books/S55-R1/INTAKE.md` (the method a previous book used; copy it).
- `/home/claude/obesity-course/sources/aslam_emmanuel_2010.txt` first 60 lines (the file format:
  header with CITATION, IDs, ARTICLE PAGE, TEXT FETCHED FROM, LICENCE AS STATED, READ BEFORE QUOTING,
  WHAT THIS FILE HOLDS; then numbered blocks, each `[TEXT] ... [END TEXT]`).
- `/home/claude/obesity-course/books/S47-R1/READY.md` rows for your sources, and
  `/home/claude/obesity-course/books/S47-R1/INVENTORY.md` rows of the concepts they serve (so you take
  the passages those concepts need, whole sections preferred over snippets).

## Method (non-negotiable)
1. Fetch with `mcp__TinyFish__fetch_content` (load it with ToolSearch). WebFetch output is a model
   summary and must **never** be stored as source text; you may use WebFetch/WebSearch only to find
   URLs. Never curl/wget/Python HTTP. For PMC articles, the OA XML at
   `https://pmc-oa-opendata.s3.amazonaws.com/PMC<id>.1/PMC<id>.1.xml` works when the article page
   returns empty; Europe PMC `https://europepmc.org/api/getPdf?pmcid=PMC<id>` gives a PDF text layer.
2. Save each raw fetch unchanged to your own scratch folder `/home/claude/intake-S47/<group>/raw/`.
   Cut every stored passage by script as a contiguous slice (`raw[i:j]`) into
   `/home/claude/obesity-course/sources/<citekey>.txt`. Write `/home/claude/intake-S47/<group>/verify.py`
   that re-parses each file you wrote and checks every `[TEXT]` run is a whitespace-normalised
   substring of its raw fetch; run it; it must pass. Use file names unique to your group (other groups
   run at the same time).
3. **Licence** read from the work's own page / details page / copyright line, quoted exactly in the
   header. Never assume. **The header says exactly what the file holds**; an excerpt is never called
   complete; omissions listed.
4. **Citekey is new**: check `grep` of `/home/claude/obesity-course/sources/INDEX.yml` and
   `/home/claude/obesity-course/check/references/library.bib`. Style: `author_year_word`, lower case.
5. Confirm journal IDs (PMID/PMCID/DOI) with the PubMed tools (`mcp__PubMed__convert_article_ids`,
   `get_article_metadata`) where the article is in PubMed.
6. **Forbidden portals**: India Code (indiacode.nic.in, indiacode.gov.in, and its API) forbids
   automated access — never fetch from it. Before fetching from any government portal, open its
   terms/copyright/policy page and record what it says; if it forbids automated access, stop and mark
   the source "not obtained: site terms". Wikipedia and similar are leads only, never sources.
7. PDFs: if a PDF yields a usable text layer through TinyFish, it may be stored (say so in the header
   and note any spacing defects). If it yields nothing usable, record "not obtained: PDF without a
   text layer" with the URL.

## Do NOT edit the shared registries
Do not touch `sources/INDEX.yml`, `check/references/library.bib`, `sources/SOURCES.md`, or
`books/S47-R1/READY.md`. Instead write `/home/claude/intake-S47/<group>/REGISTRY.md` containing, per
source obtained: the INDEX.yml entry (YAML, same shape as existing entries), the `.bib` entry (no
repository path in any field; `url` to the work's public page), a one-paragraph SOURCES.md line, and a
row for the intake log (Source | URL fetched | Passages | Check n/n | Licence as stated | Citekey).
Then a **Not obtained** table: source | concepts | URL(s) tried | why (CAPTCHA, login, robot block,
PDF without text layer, paywall, not found, site terms) | where Harsh can get it.

## Reply
At most 150 words: obtained (citekeys), not obtained (with reason), verify.py result n/n, anything
the conductor must decide (e.g. a citation in READY.md that proved wrong).
