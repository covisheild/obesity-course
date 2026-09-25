# Source intake log · S57-R1 · group a (learning-science papers)

One pass, 2026-09-24 to 2026-09-25, against sources 1-11 of the group-a brief (READY.md lines for
Freeman, Deslauriers, Agarwal, Weinstein, Dunlosky, Pashler, Newton and Miah, Rozenblit and Keil,
Sweller, Roediger and Karpicke, Cepeda). Tool for every stored passage: `mcp__TinyFish__fetch_content`.
Its result was saved by the harness to a tool-result file; `saveraw.py` (scratchpad) decoded that
JSON and wrote each URL's `text` unchanged to `raw/<citekey>-<route>.txt`, with the rest of the
result (url, final_url, title, the tool-result file path) in a `.meta.json` beside it. Every passage
was cut by script from that text as one contiguous `raw[i:j]` located by start and end anchors
(`build_a.py`), and every written file was then re-parsed and each passage tested as a
whitespace-normalised substring of the raw fetch for the URL in its block heading (`verify_a.py`).
No WebFetch output is stored anywhere; nothing was fetched with curl, wget or a Python HTTP client.
Identifiers were confirmed with the PubMed tools (`lookup_article_by_citation`,
`convert_article_ids`) and, for Rozenblit and Keil, the Europe PMC REST record. Nothing was committed.

**Verbatim check: 36 of 36.** A passage is one block; most are whole sections, several thousand
words long.

**Obtained: 9 of 11 in full or substantial text, 2 of 11 abstract only**, plus one substitute
filed for the missing body of Rozenblit and Keil. Both "PDF or paywalled, which only Harsh can
get" items in this group (Roediger and Karpicke 2006, Cepeda 2008) were obtained, from copies not
served by the publisher; the headers say which.

| Source | URL fetched (stored passages) | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Freeman et al. 2014 *PNAS* 111:8410 (PMID 24821756, PMC4060654) | https://www.pnas.org/doi/10.1073/pnas.1319030111 | 4 | 4/4 | "Freely available online through the PNAS open access option." (article page; no CC licence) | `freeman_2014_active_learning` |
| Deslauriers et al. 2019 *PNAS* 116:19251 (PMID 31484770, PMC6765278) | https://pmc-oa-opendata.s3.amazonaws.com/PMC6765278.1/PMC6765278.1.xml | 3 | 3/3 | "This open access article is distributed under Creative Commons Attribution-NonCommercial-NoDerivatives License 4.0 (CC BY-NC-ND)." | `deslauriers_2019_feeling_of_learning` |
| Agarwal, Nunes, Blunt 2021 *Educ Psychol Rev* 33:1409 (DOI 10.1007/s10648-021-09595-9) | https://pdf.poojaagarwal.com/Agarwal_etal_2021_EDPR.pdf (published PDF, first author's site) | 1 | 1/1 | "The Author(s), under exclusive licence to Springer Science+Business Media, LLC part of Springer Nature 2021" (PDF). **Not open access**: Springer page is a subscription preview | `agarwal_2021_retrieval_practice` |
| Weinstein, Madan, Sumeracki 2018 *Cogn Res* 3:2 (PMID 29399621, **PMC5780548**) | https://pmc-oa-opendata.s3.amazonaws.com/PMC5780548.1/PMC5780548.1.xml | 3 | 3/3 | "distributed under the terms of the Creative Commons Attribution 4.0 International License" | `weinstein_2018_science_of_learning` |
| Dunlosky et al. 2013 *PSPI* 14:4 (PMID 26173288) | https://www.whz.de/fileadmin/lehre/hochschuldidaktik/docs/dunloskiimprovingstudentlearning.pdf (published PDF, third-party host) | 5 | 5/5 | "© The Author(s) 2013 / Reprints and permission: sagepub.com/journalsPermissions.nav" (PDF); APS page offers it free to read | `dunlosky_2013_learning_techniques` |
| Pashler et al. 2008 *PSPI* 9:105 (PMID 26162104) | https://digitalcommons.usf.edu/psy_facpub/1765/ | 2 | 2/2 | none stated (repository record); publisher copyright | `pashler_2008_learning_styles` (**abstract only**) |
| Newton & Miah 2017 *Front Psychol* 8:444 (PMID 28396647, PMC5366351) | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00444/full | 2 | 2/2 | "distributed under the terms of the Creative Commons Attribution License (CC BY)" | `newton_miah_2017_learning_styles` |
| Rozenblit & Keil 2002 *Cogn Sci* 26:521 (PMID 21442007, PMC3062901, NIHMS268518) | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=3062901 | 3 | 3/3 | "© 2002 Published by Cognitive Science Society, Inc."; PMC flags "open-access no", "manuscript yes" | `rozenblit_keil_2002_ioed` (**abstract only**) |
| (substitute) Fisher & Keil, *Cognitive Science* online first 2015, doi 10.1111/cogs.12280 | https://cogdevlab.yale.edu/sites/default/files/files/Fisher2015.pdf (Keil lab copy) | 3 | 3/3 | "Copyright © 2015 Cognitive Science Society, Inc. All rights reserved." | `fisher_keil_2015_ioed` |
| Sweller, van Merriënboer, Paas 2019 *Educ Psychol Rev* 31:261 (DOI 10.1007/s10648-019-09465-5) | https://link.springer.com/article/10.1007/s10648-019-09465-5 | 6 | 6/6 | "Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License" | `sweller_2019_cognitive_load` |
| Roediger & Karpicke 2006 *Psychol Sci* 17:249 (PMID 16507066) | https://gwern.net/doc/psychology/spaced-repetition/2006-roediger.pdf (published PDF, third-party host) | 2 | 2/2 | "Copyright r 2006 Association for Psychological Science" (PDF footer; "r" is the © sign) | `roediger_karpicke_2006_testing_effect` |
| Cepeda et al. 2008 *Psychol Sci* 19:1095 (PMID 19076480, ERIC ED505660) | https://files.eric.ed.gov/fulltext/ED505660.pdf (authors' **in-press manuscript**) | 2 | 2/2 | none stated; ERIC record: "Its contents may differ from the final published version." | `cepeda_2008_spacing_ridgeline` |

## What the concepts get, and the gaps that matter

- **C01, C03, C11 (Roediger and Karpicke).** Held whole: Exp. 1 restudy 81% vs test 75% at 5 min,
  test 68% vs 54% at 2 days, 56% vs 42% at 1 week; Exp. 2 SSSS 83%, SSST 78%, STTT 71% at 5 min and
  40%, 56%, 61% at 1 week; SSSS most confident. The PDF text layer writes "=" as "5" ("t(39) 5 3.22").
  Agarwal 2021 restates the 5-minute vs one-week reversal in words (no numbers) as a second anchor.
- **C04 (Cepeda).** Held whole, but it is the in-press manuscript. Optimal tested gaps 1, 11, 21, 21
  days for RIs 7, 35, 70, 350 days (recall); fitted optimum 23 days for RI 350 ("just 7% of the RI");
  abstract "about 20% of the test delay for delays of a few weeks, falling to about 5% when delay was
  one year". Figure 3's per-condition proportions are an image and are not held, so the drill set
  can use only the gaps, RIs and ratios the text states. Weinstein 2018 restates that "the optimal gap
  between study sessions was contingent on the retention interval" (no numbers). Dunlosky 2013 does
  not cite Cepeda 2008.
- **C01, C05, C13 (Deslauriers).** Whole body. Its test of learning was taken at the end of each class
  period, not days later; the header says so. Use it for "feeling of learning and measured learning
  diverge", not for "learning tested days later".
- **C06 (Pashler).** Abstract only. It defines the meshing hypothesis and states the criterion in
  words (style groups, random assignment to methods, same test, the method best for one style is not
  best for the other) and "virtually no evidence". The 2 x 2 crossover figures and the named studies
  are **not** held. Newton and Miah is whole.
- **C07 (Rozenblit and Keil).** Abstract only. The "ratings fall after explaining" claim rests on the
  Fisher and Keil 2015 substitute, which states the paradigm and "a consistent drop from Time 1 to
  Time 2" citing Rozenblit and Keil. The course should attribute that sentence to Fisher and Keil, or
  wait for the original.
- **C08 (Sweller).** Excerpts; no numeric working-memory capacity is stated in the paper's held text,
  and its Table 1 did not come through the extraction.
- **C02 (Freeman).** SMD 0.47 (Hedges' g), odds ratio 1.95, failure 21.8% vs 33.8%, Table 1 by
  design quality; the SI tables are not held.

## Not obtained, and what Harsh would need

| Item | Why not | What to download |
| --- | --- | --- |
| Pashler et al. 2008, body | SAGE bot-blocked; APS PDF links unreachable; an appstate.edu copy returned no text; academia.edu is behind sign-up | Open https://doi.org/10.1111/j.1539-6053.2009.01038.x in a browser, download the PDF (free via APS), and put it in `sources/` for transcription |
| Rozenblit & Keil 2002, body | Author manuscript not in the PMC OA subset; PMC page empty to the fetcher; Europe PMC REST 500 three times; Wiley bot-blocked | Open https://pmc.ncbi.nlm.nih.gov/articles/PMC3062901/ and save the page or its PDF |
| Cepeda et al. 2008, published version (optional) | Held text is the ERIC in-press manuscript; SAGE and lab PDFs unreachable | Only if the published figures must be checked: the PDF from https://doi.org/10.1111/j.1467-9280.2008.02209.x |
| Dunlosky 2013 and Roediger & Karpicke 2006 from the publisher (optional) | Held text is the published PDF, but from third-party hosts (whz.de, gwern.net) | Only if a publisher-served copy is required: the PDFs from their DOIs |

## Corrections to READY.md found at intake

- Weinstein et al. 2018 is **PMC5780548**, not PMC5780106.
- Agarwal et al. 2021 is **not** Springer open access and not CC BY: the article page is a
  subscription preview and the PDF says "under exclusive licence to Springer". It was obtained from
  the first author's own site.
- Deslauriers et al. 2019's licence is CC BY-NC-ND 4.0.
- Roediger and Karpicke 2006 and Cepeda et al. 2008 were obtainable from a session, so they need not
  wait for Harsh (see the caveats above about which copy).

## Raw files (this group only)

`raw/freeman_2014_active_learning-pnas.txt`, `raw/deslauriers_2019_feeling_of_learning-pmcxml.txt`,
`raw/agarwal_2021_retrieval_practice-authorpdf.txt`, `raw/agarwal_2021_retrieval_practice-springer.txt`
(paywall preview, kept as the evidence for the licence finding), `raw/weinstein_2018_science_of_learning-pmcxml.txt`,
`raw/dunlosky_2013_learning_techniques-whzpdf.txt`, `raw/pashler_2008_learning_styles-usf.txt`,
`raw/newton_miah_2017_learning_styles-frontiers.txt`, `raw/rozenblit_keil_2002_ioed-efetch.txt`,
`raw/fisher_keil_2015_ioed-yalepdf.txt`, `raw/sweller_2019_cognitive_load-springer.txt`,
`raw/roediger_karpicke_2006_testing_effect-gwernpdf.txt`, `raw/cepeda_2008_spacing_ridgeline-ericpdf.txt`,
each with a `.meta.json`.
