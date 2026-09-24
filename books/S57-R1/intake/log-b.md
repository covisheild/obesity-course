# Source intake log · S57-R1 · group b (statistics, teaching guides, assessment, leadership)

One pass, 2026-09-24/25. Every stored passage was cut by script (`books/S57-R1/intake/build-b.py`) as `raw[i:j]`
from a saved `mcp__TinyFish__fetch_content` result in `books/S57-R1/intake/raw/` (the JSON the harness saved,
decoded unchanged; the `text` field written out). The written files were then re-parsed by
`books/S57-R1/intake/verify-b.py` and each passage tested as a whitespace-normalised substring of the raw fetch
for the URL in its block heading. No WebFetch output is stored; nothing was fetched with curl, wget or Python
HTTP. Identifiers were confirmed with the PubMed tool (`lookup_article_by_citation`, `get_article_metadata`,
`convert_article_ids`) and, for Hake and Biggs, from their Crossref records.

**Verbatim check: 19 of 19.**

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| OpenStax *Introductory Statistics 2e* §1.4 Experimental Design and Ethics (appended to the held file) | https://openstax.org/books/introductory-statistics-2e/pages/1-4-experimental-design-and-ethics; details page re-read | 1 (whole page) | 1/1 | "by OpenStax is licensed under Creative Commons Attribution-NonCommercial-ShareAlike License v4.0" (details page, 2026-09-24; web version still "Jul 07, 2026") | `openstax_intro_stats_2e` (INDEX `what:` update, not a new entry) |
| Cochrane Handbook v6.5, ch. 6, Key Points and §6.5.1-6.5.1.2 | https://training.cochrane.org/handbook/current/chapter-06 (redirects to cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-06) | 2 | 2/2 | none in the extracted text; site footer "Copyright © 2026 The Cochrane Collaboration" (search snippet only) | `cochrane_handbook_ch06_v6_5` |
| Chatterjee & Corral 2017 *J Educ Perioper Med* 19(4):E610 | https://www.seahq.org/assets/docs/xix_4_chatterjee.pdf (publisher PDF text layer); PMC front matter via https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=5944406 | 3 | 3/3 | "© 2017 Society for Education in Anesthesia" (PMC front matter) | `chatterjee_corral_2017_objectives` |
| Adams 2015 *J Med Libr Assoc* 103(3):152-153 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4511057/ | 1 (whole article) | 1/1 | "Copyright: © 2015, Authors." (PMC page) | `adams_2015_bloom` |
| Hake 1998 *Am J Phys* 66(1):64-74, **abstract only** | https://api.crossref.org/works/10.1119/1.18809 (abstract string JSON-decoded) | 1 | 1/1 | publisher copyright (AAPT); none stated in the record | `hake_1998_normalized_gain` |
| Biggs 1996 *High Educ* 32(3):347-364, **abstract only** | https://link.springer.com/article/10.1007/BF00138871 | 1 | 1/1 | publisher copyright; page says "This is a preview of subscription content" | `biggs_1996_constructive_alignment` |
| Frich et al. 2015 *J Gen Intern Med* 30(5):656-674 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4395611.1/PMC4395611.1.xml | 6 | 6/6 | "© The Author(s) 2014 https://creativecommons.org/licenses/by/4.0/ Open Access This article is distributed under the terms of the Creative Commons Attribution License ..." | `frich_2015_physician_leadership` |
| Stoller 2020 *Chest* 159(3):1147-1154 (substitute for Kotter 1990) | https://pmc-oa-opendata.s3.amazonaws.com/PMC7501065.1/PMC7501065.1.xml | 4 | 4/4 | "© 2020 American College of Chest Physicians. Published by Elsevier Inc. All rights reserved." plus Elsevier's COVID-19 resource-centre permission (quoted in file) | `stoller_2020_leadership` |

Obtained: 6 of 8 assigned works in usable form (OpenStax §1.4, Cochrane, Chatterjee, Adams, Frich; Hake as its
abstract, which carries the whole C12 need). Biggs and Kotter: see below. Kirkpatrick's four levels are carried by
Frich 2015 (Methods, Data Analysis and Table 1), so no separate source was filed for C13.

## Findings the conductor should know

- **Cochrane SMD formula is not held.** The chapter's equations are images; the text defines MD and SMD in words
  only. C02's drill set (SMD = difference in means ÷ SD) can quote "studies for which the difference in means is
  the same proportion of the standard deviation (SD) will have the same SMD"; the pooled-SD formula itself has no
  quotable source here.
- **Kirkpatrick's labels in Frich differ from the usual ones:** "reaction (Level 1), knowledge (Level 2), behavioral
  change (Level 3), and system results (Level 4)", and Frich says the typology is "modified after Collins & Holton
  and Kirkpatrick". If C13 wants the words "learning" and "results", it needs another source (Kirkpatrick's
  own book is not open).
- **Frich does not carry Kotter's lists.** Its introduction has one leadership/management sentence citing Yukl
  (ref 16) and cites Kotter (ref 17) only for "separate systems of action". Stoller 2020 Table 1 carries Kotter's
  six functions, labelled "After Kotter", so it is Stoller's adaptation, not Kotter's words.
- **Frich's comparison-group count is inconsistent in the paper:** the abstract and Table 2 say four (9 %), the
  Results text says "Only five studies ... used a comparison group". Quote whichever is used with its own words.
- **Chatterjee is PDF-only in PMC** (the PMC page returns no text; not in the OA bucket). The file is the publisher's
  own PDF from seahq.org; its tables are flattened by the text layer.

## Not obtained, and what Harsh would need

| Work | Why not | What to download |
| --- | --- | --- |
| Kotter JP. What leaders really do. *Harv Bus Rev* 1990;68(3):103-111 (republished Dec 2001) | hbr.org returned only the metered teaser (standfirst and first paragraph); body behind HBR paywall | https://hbr.org/2001/12/what-leaders-really-do, saved as PDF or print-to-PDF from a logged-in/subscriber session (HBR reprint R0111F). Until then `stoller_2020_leadership` stands in (Table 1, "After Kotter"). An alternative open restatement exists in Amelung et al. (eds), *Handbook Integrated Care* (Springer open access, 2021), a box sourced "Kotter (2001)"; not filed |
| Biggs J. Enhancing teaching through constructive alignment. *High Educ* 1996;32:347-364, full text | Springer subscription content | https://link.springer.com/content/pdf/10.1007/BF00138871.pdf from an institutional login. A copy is posted at https://teaching.helsinki.fi/system/files/inline-files/Biggs1996_Article_EnhancingTeachingThroughConstr.pdf (University of Helsinki); not used, redistribution licence unstated. For C10 the abstract (held) plus Chatterjee's "constructive alignment" paragraph may suffice |
| Hake RR 1998, full text | pubs.aip.org returned bot_blocked; Hake's own copy at http://www.physics.indiana.edu/~sdi/ajpv3i.pdf unreachable (host down, Wayback unreachable from the session) | Only needed if the course quotes beyond the abstract: https://doi.org/10.1119/1.18809 (AIP PDF) from an institutional login, or Hake's copy if that host returns. Third-party uploads (stemteachersnyc.org, jgravesedu.com) were not used |

## Files

- New: `sources/cochrane_handbook_ch06_v6_5.txt`, `sources/chatterjee_corral_2017_objectives.txt`,
  `sources/adams_2015_bloom.txt`, `sources/hake_1998_normalized_gain.txt`,
  `sources/biggs_1996_constructive_alignment.txt`, `sources/frich_2015_physician_leadership.txt`,
  `sources/stoller_2020_leadership.txt`.
- Extended: `sources/openstax_intro_stats_2e.txt` (header updated; §1.4 appended after §4.2).
- Index/bib/SOURCES entries: `books/S57-R1/intake/fragment-b.md`. Raw fetches: `books/S57-R1/intake/raw/`
  (group-b names: `openstax_intro_stats_2e-*`, `cochrane_handbook*`, `chatterjee_corral_2017-*`, `adams_2015_bloom-*`,
  `hake_1998-*`, `biggs_1996-*`, `frich_2015-*`, `stoller_2020-*`, `kotter-hbr.txt`).
