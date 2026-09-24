# Source intake log · S37-R1

One pass, 2026-09-24, by four intake subagents (A-D) under `books/S37-R1/INTAKE-BRIEF.md`, TinyFish fetch_content only. Raw fetches saved unchanged; the conductor re-ran the verbatim check from them independently: **314 of 314** passages (chunks of 15+ characters between omission and table marks) are whitespace-normalised substrings of their raw fetch. Citekey `rbi_wp_2024_06_tops` renamed `rbi_wp_2024_08_tops` by the conductor (the paper is WP 08/2024).

---

## Group: Source intake log · S37-R1 · group A (frameworks and international)

One pass, 2026-09-24, against group A of `INTAKE-BRIEF.md`. Tool for every stored passage:
`mcp__TinyFish__fetch_content` (markdown). Each fetch result was taken from the session's own record
of the tool call by script, decoded from JSON to its `text` field unchanged, and saved to
`/home/claude/intake-raw/A/<citekey>__<n>.txt`. Every passage was cut from that text by script
(`raw[i:j]`, start and end marker strings), and each file was then re-parsed and every passage tested
as a whitespace-normalised substring of the raw fetch for the URL in its block heading. WebSearch was
used only to find URLs; nothing from WebFetch, curl, wget or a Python HTTP client is stored. The PubMed
tool was used only to confirm bibliographic details (authors, volume, pages, PMCID); none of its text
is stored.

**Verbatim check: 74 of 74.** A passage is one run of source text between two `[NOTE]`, `[...]` or
table marks (or two adjacent quoted blocks).

**Obtained 8 of 9.** NOT OBTAINED: Hawkes et al. 2020.

| Source | URL fetched | Passages | Check | Licence as stated | Citekey | What the file holds |
| --- | --- | --- | --- | --- | --- | --- |
| HLPE Report 12, *Nutrition and food systems* (Sep 2017) | https://www.fao.org/fileadmin/user_upload/hlpe/hlpe_documents/HLPE_Reports/HLPE-Report-12_EN.pdf (PDF text layer) | 12 | 12/12 | "This report is made publicly available and its reproduction and dissemination is encouraged. Non-commercial uses will be authorized free of charge, upon request." | `hlpe_2017` | Excerpts: reproduction statement; Summary paras 1-6, 22-28; s.1.1; openings of 1.2 and 1.2.1; Figure 1 labels; s.1.2.2 food environments with Definition 1 and the opening of each of its four elements |
| WCRF NOURISHING framework | https://www.wcrf.org/research-policy/policy/nutrition-policy/nourishing-framework/ ; https://policydatabase.wcrf.org/level_one?page=nourishing-level-one | 4 | 4/4 | no licence statement found on either page | `wcrf_nourishing` | Framework page less a testimonial and link list; database page whole (ten policy areas in three domains) |
| FAO *Food Balance Sheets: a handbook* (2001) | https://www.fao.org/4/x9892e/ x9892e00.htm, X9892e.htm, X9892e01.htm, X9892e02.htm, X9892e04.htm (X9892e05.htm, annexes, also fetched, not used) | 17 | 17/17 | no licence or copyright statement found on the HTML pages | `fao_fbs_handbook_2001` | Excerpts: ch.I nature of FBS; ch.II items 1-4 (supply identity, concept (c)), 9, 11, 12; ch.IV IDR and SSR definitions |
| UNEP *Food Waste Index Report 2024* | https://wedocs.unep.org/bitstreams/5c6e505d-e1d3-4731-b5b8-4ecb9693a056/download (English PDF from record https://wedocs.unep.org/handle/20.500.11822/45230, also fetched) | 17 | 17/17 | "This publication may be reproduced in whole or in part and in any form for educational or non-profit services without special permission from the copyright holder, provided acknowledgement of the source is made." | `unep_fwi_2024` | Excerpts: definitions page; confidence ratings; Table 3; Table 23; India rows of Tables 13 and 16; Annex 3 Southern Asia rows |
| WHO *Double-duty actions for nutrition: policy brief* (2017) | https://iris.who.int/server/api/core/bitstreams/e286dbe4-6d69-49ba-a7d9-b48a4aeea3bb/content (PDF linked from https://www.who.int/publications/i/item/WHO-NMH-NHD-17.2, also fetched) | 9 | 9/9 | "© World Health Organization 2017. Some rights reserved. This work is available under the CC BY-NC-SA 3.0 IGO licence." | `who_double_duty_2017` | Prose nearly whole; figures and references left out |
| Swinburn et al. *Lancet* 2019;393:791 (verify_at_intake `S37-R2-A01`) | https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(18)32822-8/fulltext | 5 | 5/5 | "Copyright: © 2019 Elsevier Ltd. All rights reserved." | `swinburn_2019_syndemic` | Excerpts: article info; executive summary opening and three subsections; Introduction paragraphs incl. the syndemic definition |
| Popkin, Adair, Ng *Nutr Rev* 2012;70:3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3257829.1/PMC3257829.1.xml (the PMC page returned empty content) | 4 | 4/4 | "This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law." | `popkin_2012_transition` | Excerpts from the NIH author manuscript: title, statement, abstract, Introduction |
| NFHS-5 (2019-21) India fact sheet | https://dhsprogram.com/pubs/pdf/OF43/India_National_Fact_Sheet.pdf (IIPS copy at rchiips.org unreachable) | 6 | 6/6 | no licence or copyright statement found in the fact sheet | `nfhs5_india_factsheet` | Excerpts: cover; fieldwork and sample; indicators 81-98 with footnotes 18-22; funding line |

## NOT OBTAINED

- **Hawkes C, Ruel MT, Salm L, Sinclair B, Branca F. Double-duty actions: seizing programme and
  policy opportunities to address malnutrition in all its forms. *Lancet* 2020;395:142-155**
  (`hawkes_2020_double_duty`). The Lancet full-text, abstract and PDF URLs and the ScienceDirect page
  all returned `bot_blocked` to TinyFish; PubMed's page returned a cookie wall; the PubMed ID
  converter shows no PMC copy; the CGIAR repository record (https://cgspace.cgiar.org/items/03f249c7-9292-42d2-872a-fa00a6eccb4c,
  raw saved as `hawkes_2020_double_duty__0.txt`) is "Limited Access", "Copyrighted; all rights
  reserved", with no file. A ResearchGate copy exists but is a mirror and was not used. **What a person
  would need to do:** Harsh to open https://doi.org/10.1016/S0140-6736(19)32506-1 in a browser and save the page or PDF text; the passages C15 needs are the definitions of double-duty
  actions and the ten actions, and any wording on programmes that worked against the other burden.
  The bib entry is supplied (details confirmed via PubMed) with a note that the text is not held.

## What a drafter must know

- **"Single-duty" and "working against" are not in the WHO brief.** INVENTORY C15 asks for
  double-duty, single-duty and "working against the other burden" defined. The WHO brief has the
  double-duty definition and three levels (do no harm, retrofit, de-novo). The other two terms would
  come from Hawkes 2020, which is not held. C15 can define double-duty and "do no harm" from the WHO
  brief; nothing else can be quoted.
- **Global Syndemic (`S37-R2-A01`, verify_at_intake): verified.** The Lancet full text opened. The
  executive summary defines The Global Syndemic as three pandemics, obesity, undernutrition and climate
  change, forming "a syndemic, or synergy of epidemics, because they co-occur in time and place,
  interact with each other to produce complex sequelae, and share common underlying societal
  drivers". The Introduction gives the original three-part definition of a syndemic.
- **UNEP India figure:** household food waste **55 kg per capita per year** (78 192 338 tonnes a
  year), **Medium confidence**, 2022 population basis. It is built from seven city-level datapoints
  (20-88 kg), not a national survey. UNEP gives no Indian food-service or retail datapoint. The
  global household average is 79 kg.
- **Food loss against food waste (UNEP):** food loss runs "up to, and excluding, the retail level";
  the Food Waste Index covers retail, food service and household. The FAO handbook's "waste" element
  (storage and transport losses) is a different thing and **excludes** household waste.
- **FAO identity:** the handbook states it as concept (c), "Production + imports - exports + changes in
  stocks (decrease or increase) = supply for domestic utilization", with a stock increase entered with
  a minus sign. It also defines IDR as imports / (production + imports - exports) x 100 (a fraction
  drawn with underscores in the HTML), not imports / consumption as INVENTORY C06 words it.
- **HLPE Figure 1** is a diagram: only its labels are held, not its arrows or layout. The definition
  of a food system is quoted in the report from HLPE 2014a (the report on food losses and waste).
- **Popkin 2012** held from the NIH author manuscript, whose title and abstract wording differ from
  the published version. It does **not** set out numbered stages or patterns of the nutrition
  transition. Fine for a forward pointer; not a source for "Popkin's stages".
- **NFHS-5:** adult rows cover ages 15-49 only, and the fact sheet has only "overweight or obese" (BMI
  25 or more), with no separate obesity row. Children: stunted 35.5%, wasted 19.3%, underweight 32.1%,
  overweight 3.4%; women overweight or obese 24.0%, men 22.9%; anaemia in children 6-59 months 67.1%,
  women 57.0%, men 25.0% (NFHS-4 totals alongside in the file).
- **WCRF:** the pages carry no licence line and no last-updated date; "developed in 2013" is the only
  date.

---

## Group: Source intake log · S37-R1 · group B (the state as provider)

One pass, 2026-09-24. Tool for every stored passage: `mcp__TinyFish__fetch_content`. Each result was taken
from the session transcript (or the harness's saved tool-result file for the large PDFs), decoded from JSON and
written unchanged to `/home/claude/intake-raw/B/<citekey>__<n>.txt` (URL for each in `_manifest.json` there).
Every passage was cut by script (`raw[i:j]` between a start and an end string), then each written file was
re-parsed and every passage tested as a whitespace-normalised substring of its raw fetch. Search tools
(TinyFish search) were used only to find URLs. No WebFetch output, curl, wget or Python HTTP.

**Verbatim check: 35 of 35.** Obtained 7 of the 8 assigned citekeys, plus one extra (`s37_pib_1812421`).

| Source | URL fetched | Passages | Check | Licence as stated | Citekey | What the file holds |
| --- | --- | --- | --- | --- | --- | --- |
| PIB 2082323, 6 Dec 2024, PM POSHAN (LS reply) | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2082323&reg=48&lang=2 | 1 | 1/1 | no licence statement found on the release page | `pib_2082323` | whole text |
| PIB 2251769, 14 Apr 2026, Mission Poshan 2.0 backgrounder | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2251769&reg=3&lang=1 | 1 | 1/1 | no licence statement found on the release page | `pib_2251769` | whole text (linked PDF not fetched) |
| PIB 1980689, 29 Nov 2023, PMGKAY | https://www.pib.gov.in/PressReleasePage.aspx?PRID=1980689 | 1 | 1/1 | no licence statement found on the release page | `pib_1980689` | whole text |
| PIB 1847548, 2 Aug 2022, Poshan 2.0 guidelines issued | https://www.pib.gov.in/PressReleasePage.aspx?PRID=1847548 | 1 | 1/1 | no licence statement found on the release page | `pib_1847548` | whole text |
| PIB 1812421, 1 Apr 2022, PM POSHAN norms (LS reply) | https://www.pib.gov.in/PressReleasePage.aspx?PRID=1812421 | 5 | 5/5 | no licence statement found on the release page | `s37_pib_1812421` (**extra**) | whole text, two tables |
| MoWCD Poshan 2.0 Scheme Guidelines (2022), PDF text layer | https://wcd.gov.in/documents/uploaded/Mission%20Saksham%20Anganwadi%20and%20Poshan%202.0%20scheme%20guidelines.pdf | 9 | 9/9 | no licence statement found in the PDF's text layer | `poshan2_guidelines_2022` | excerpts: 1.1-1.3, 2.7-2.8, 3.1, 3.3, 3.2.1-3.2.2 norms, 3.4-3.7 |
| ICMR-NIN IFCT 2017, PDF text layer | https://www.nin.res.in/ebooks/IFCT2017.pdf | 4 | 4/4 | "The use and dissemination of the data in this book is encouraged. This publication can be reproduced for personal use with full acknowledgment of the source. However, no part of this publication can be stored or reproduced in any electronic format for creating a product without the prior written permission of the National Institute of Nutrition, Hyderabad." | `ifct_2017` | excerpts: title verso, 3.6, Table 4, Table 1 A001-A024 and B001-B022 |
| DFPD Annual Report 2025-26, PDF text layer | https://dfpd.gov.in/WriteReadData/AnnualRecordUploadDocuments/43bf089b-73cc-4329-aeb6-c883d2f2ea55_Food%20AR%202025-26%20English.pdf | 13 (5 blocks) | 13/13 | no licence statement found in the PDF's text layer | `dfpd_pds` | excerpts: history to 1965, 2.6-2.8, 3.35-3.41, 3.64-3.66, 4.1-4.8 |

(Passage counts: the check counts each quoted run or table; `dfpd_pds` has 13 such runs across 5 blocks,
`poshan2_guidelines_2022` 9 — total 1+1+1+1+5+9+4+13 = 35.)

## NOT OBTAINED

- **`pm_poshan_guidelines_2023`** — Ministry of Education, *Guidelines on PM POSHAN Scheme* (2023). The PDF
  (https://pmposhan.education.gov.in/Files/Guidelines/2023/Guidelines%20on%20PM%20POSHAN%20SCHEME.pdf) returned
  null text on four attempts (markdown and html, http and https, cached and live); the "About us" page and the site
  home page returned `proxy_error`; another PDF on the same host (material cost revision, May 2025) also returned
  null. The whole host is unreachable from the session. **Harsh to download the guidelines PDF in a browser**
  (and check it has a text layer) for coverage, cost sharing and the food-norms table in the guidelines' own words.
  Stand-in held: `s37_pib_1812421` (official PIB release carrying the same nutrition and food norms table) and the
  PM POSHAN foodgrain tonnage in `dfpd_pds`. Cost sharing for PM POSHAN is **not** held anywhere.
- **DFPD web pages** ("History of Public Distribution", FAQs, home) — script-rendered; TinyFish returned only
  page chrome (raws saved as `dfpd_pds__1`, `__3`, `__4`). Covered instead from DFPD's own Annual Report 2025-26
  under the same citekey `dfpd_pds`. Nothing further needed unless the web page's wording is specifically wanted.

## For drafters

- **The two A01 sources do not give PDS scale.** `pib_2082323` has no numbers at all; `pib_2251769` gives
  anganwadi scale only (14,03,170 AWCs, 8,95,29,425 beneficiaries, March 2026). PDS and PM POSHAN scale in tonnes
  comes from `dfpd_pds` (allocation 2025-26; offtake to Dec 2025) and in persons from `pib_1980689` (81.35 crore).
- `dfpd_pds` 3.35 says "595.05 lakh Mt" allocated in 2025-26, but the table under it totals 607.40 (554.11 TPDS +
  51.77 OWS + 1.52 additional). Quote the table, or say which figure.
- Anganwadi norms: `poshan2_guidelines_2022`'s table (500 kcal / 12-15 g for children, etc.) is marked "under
  revision"; `pib_2251769` says they were revised in January 2023. The revised numbers are not held.
- IFCT 2017 prints energy in **kJ only**, and converts with **1 kcal = 4.18 kJ** (not 4.184). Rice raw milled
  1491 kJ, 7.94 g protein per 100 g.
- The DFPD report's text layer drops capital T ("the", "tPDS", "Uts"); passages are stored as extracted.
- `pib_1980689` gives economic cost for 35 kg rice (Rs 1371) and wheat (Rs 946), as of Nov 2023 — relevant to
  group C's `s37_economic_cost_grain`.

---

## Group: Source intake log · S37-R1 · group C (prices, procurement, trade, missions)

One pass, 2026-09-24. Tool for every stored passage: `mcp__TinyFish__fetch_content`. Each fetch result was saved
unchanged (decoded from JSON) to `/home/claude/intake-raw/C/<citekey>__<n>.txt`: small results were taken from the
session transcript's copy of the tool result, large ones from the file the harness wrote; in both cases the stored
text is the tool's `text` field as returned. Every passage was cut from that text by script (`raw[i:j]` between a
start and an end marker). The written files were then re-parsed and each passage tested as a whitespace-normalised
substring of the raw fetch named in its block. WebSearch and TinyFish search were used only to find URLs. No WebFetch
output is stored; nothing was fetched with curl, wget or a Python HTTP client.

**Verbatim check: 30 of 30** across 12 files.

| Source | URL fetched | Passages | Check | Licence as stated | Citekey | What the file holds |
| --- | --- | --- | --- | --- | --- | --- |
| PIB, Kharif MSP for KMS 2026-27 (13 May 2026) | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2260617 | 3 (1 table) | 3/3 | no licence statement found on the release page | `pib_2260617` | Whole release incl. the MSP / cost / margin table |
| PIB, Rabi MSP for RMS 2026-27 (1 Oct 2025), **PRID 2173567** | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2173567 | 3 (1 table) | 3/3 | none found on the release page | `pib_rabi_msp` (file `pib_rabi_msp.txt`) | Whole release incl. table; wheat MSP 2585, cost 1239, margin 109% |
| PIB, Sugarcane FRP for sugar season 2026-27 (5 May 2026), PRID 2258113 | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2258113 | 1 | 1/1 | none found on the release page | `pib_sugarcane_frp` | Whole release; FRP Rs 365/qtl at 10.25% recovery; cost A2+FL Rs 182 |
| PIB backgrounder, "Minimum Support Prices: From Safety Net to Self-Sufficiency" (10 Oct 2025) | https://www.pib.gov.in/PressNoteDetails.aspx?ModuleId=3&NoteId=155448&reg=48&lang=2 | 3 (1 table) | 3/3 | none found on the page | `s37_pib_msp_backgrounder` (**new, extra**) | Nearly whole text: 22 mandated crops, factors CACP considers, cost concept, 1.5x rule, who procures what, procurement figures |
| FCI "About us" | https://fci.gov.in/about-us | 1 | 1/1 | none found on the page | `fci_about` | The About-us paragraph, **Hindi only** (English not served); a labelled non-quotable gloss in a [NOTE] |
| Food Corporations Act 1964, India Code | https://indiacode.gov.in/server/api/discover/search/objects?query=… (two queries, see file) | 2 | 2/2 | none found in the records; India Code copyright-policy page returned no content | `food_corporations_act_1964` | s.3 (establishment) and s.13 (functions) |
| Essential Commodities Act 1955, India Code | https://indiacode.gov.in/server/api/discover/search/objects?query=… (see file) | 2 | 2/2 | as above | `eca_1955` | s.2A and s.3 in full as recorded (incl. UP state amendments) |
| PIB, edible oil BCD cut (24 Sep 2026, PRID 2314297) and BCD 20%→10% (11 Jun 2025, PRID 2135774) | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2314297 ; …PRID=2135774 | 2 | 2/2 | none found on the release pages | `s37_edible_oil_duty` | Both releases whole |
| DFPD Foodgrains Bulletin, December 2025 (PDF text layer) + DFPD Year End Review 2025 (PIB PRID 2210211) | https://dfpd.gov.in/WriteReadData/FoodBulletinUploadDocuments/8cc19261-0d0a-4ca7-b589-ab8708fb1b4d_Foodgrains%20Bulletin%20for%20December,%202025.pdf ; https://www.pib.gov.in/PressReleasePage.aspx?PRID=2210211 | 8 (4 tables) | 8/8 | none found in the PDF text or the release | `s37_economic_cost_grain` | Definitions (economic cost, CIP, etc.); economic cost tables 2019-20 to 2025-26 (BE); CIP footnote; economic cost / CIP / subsidy statement; free-grain, procurement and wheat stock-limit paragraphs |
| PIB, Cabinet approves NMEO-Oilseeds (3 Oct 2024) | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2061646 | 1 | 1/1 | none found on the release page | `pib_2061646` | Whole release |
| PIB backgrounder, National Mission on Edible Oils (8 Dec 2025) | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2200287 | 1 | 1/1 | none found on the page | `pib_2200287` | Whole text incl. references |
| PIB, "Shree Anna for Shreshta Bharat" backgrounder (8 Aug 2025, PDF) + Lok Sabha reply PRID 2290630 (28 Jul 2026) | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/aug/doc202588602801.pdf ; https://www.pib.gov.in/PressReleasePage.aspx?PRID=2290630 | 3 | 3/3 | none found in either text | `pib_millets` (file `pib_millets.txt`) | Backgrounder from Key Takeaways through Union support, production and exports; two millet bullets of the reply |

Extra citekey: **`s37_pib_msp_backgrounder`** (prefixed as the brief requires), added because the CACP site could not be
fetched; it is an official PIB text that covers most of what C09 needs from CACP, but not the 1965 date.

## NOT OBTAINED

- **`cacp_about`** (CACP "About us": established 1965, mandate, mandated crops). cacp.da.gov.in refused every fetch with
  HTTP 403 (`/`, `/content.aspx?pid=32`, `/Home/AboutUs`) and its report PDFs came back `target_unreachable`. A search
  snippet shows the About-us page says the mandate is to recommend MSP for 22 commodities and the FRP of sugarcane,
  and CACP report snippets say "since its inception in 1965"; neither is stored (snippets are not transcriptions).
  **Harsh to open https://cacp.da.gov.in/Home/AboutUs in a browser and save the page (or its text).** Until then the
  1965 date and the name "Agricultural Prices Commission" rest on no held source. (The only held text naming the
  "Agricultural Prices Commission" is ECA s.3(3B)(d) in `eca_1955`, which does not date it.)
- **FCI "About us" in English.** Every URL variant tried served the body in Hindi (held). Harsh to save the English
  page from a browser if an English quotation is wanted; otherwise cite the Act (s.3, s.13).
- **Economic cost for 2026-27 (BE).** The newest figure obtained is 2025-26 (BE) from the December 2025 bulletin.
  dfpd.gov.in's listing pages (reports, bulletin archive) return no content to the fetch tool, so later bulletins
  could not be located. Harsh to download the newest Foodgrains Bulletin from dfpd.gov.in › Reports if the 2026-27
  figure is wanted. PRS's analysis carries such figures but is secondary and was not used.
- **CBIC customs notification for the 24 Sep 2026 edible oil duty change** (reported as No. 31/2026-Customs, 23 Sep
  2026). Not fetched; the PIB release is held. The notification would give the refined-oil rates and effective date.
- **India Code HTML pages and PDFs for both Acts.** indiacode.nic.in and the PDF bitstreams were unreachable; the
  section records were fetched from India Code's own search API instead (the record field holding the section text).
  This is India Code itself, not a mirror. Mirrors seen in search (advocatekhoj, latestlaws, state civil-supplies
  sites, a Gujarat-uploaded copy on India Code) were not used.

## What a drafter must know

- **Edible oil duty changed on the day of intake.** From the PIB release of 24 Sep 2026: BCD on crude sunflower oil
  Nil, on crude soybean and crude palm oil 5% (both from 10%); 19.25% crude-refined differential kept. READY.md and
  the NMEO releases carry older figures (20% in Oct 2024; "5.5% to 16.5%" effective duty in Dec 2025). The release
  does not give the effective duty including cesses; use BCD in the landed-price arithmetic and say so, or wait for
  the notification.
- **Rabi MSP.** Newest is RMS 2026-27 (PRID 2173567, 1 Oct 2025). The RMS 2027-28 decision is due around October
  2026; C09/C10's event trigger will fire soon after this intake.
- **Economic cost vs CIP.** 2025-26 (BE): rice Rs 4173.34, wheat Rs 2980.06 per quintal. CIP for NFSA beneficiaries
  is zero since 1 Jan 2023, so subsidy = economic cost (100%); before that NFSA CIP was Rs 300/200 per quintal (rice/
  wheat), i.e. Rs 3/2 per kg. The bulletin's page-41 table decomposes economic cost into pool cost (weighted MSP) +
  procurement incidental + distribution cost; the column order is settled by arithmetic in the file's [NOTE].
- **ECA s.3 as held has no sub-section (1A).** "Stock limits" is not a phrase in s.3; the stock clauses are
  s.3(2)(d) and (f). A 2025 wheat stock-limit order is described in `s37_economic_cost_grain` block 6. (My
  understanding, not verified from a held source: the 2020 amendment that inserted s.3(1A) was repealed in 2021.)
- **No Union "millet mission" as such** in the PIB texts: millets run through the Nutri-Cereals sub-mission of
  NFSM/NFSNM, PM-RKVY and PLISMBP. The 28 Jul 2026 reply is the newest PIB mention and says only one sentence.
- **FCI "About us" is Hindi only**; quote the Act for FCI's functions.
- **Import dependence** (pib_2200287): 56.25% in 2023-24 (63.2% in 2015-16); imports 15.66 Mt, production 12.18 Mt
  (2023-24). pib_2061646 (Oct 2024) says 57%. Use the dated figure the concept needs.

---

## Group: Source intake log · S37-R1 · group D (chains, availability, spending)

One pass, 2026-09-24. Tool for every stored passage: `mcp__TinyFish__fetch_content`. Each fetch result
was taken unchanged (decoded from JSON) from the harness's record of the tool result and saved to
`/home/claude/intake-raw/D/<citekey>__<n>.txt`; every passage was cut from that text by script
(`raw[i:j]`, trimmed of surrounding whitespace only). Each written file was then re-parsed and every
quoted passage and every `[TABLE]` block tested as a whitespace-normalised substring of the raw fetch
named for its block. The checker was shown to fail on a deliberately altered copy (two digits
changed, 3/5) before the final run. WebSearch was used only to find URLs; nothing from WebFetch,
curl, wget or a Python HTTP client is stored.

**Verbatim check: 74 of 74.**

| Source | URL fetched | Passages | Check | Licence as stated | Citekey | What the file holds |
| --- | --- | --- | --- | --- | --- | --- |
| RBI WP **08**/2024, tomato-onion-potato | https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=22723 (RBI's HTML text of the paper) | 9 (1 table) | 9/9 | no licence statement found on the page | `rbi_wp_2024_08_tops` | Excerpts: abstract, Introduction (CPI weight; value-chain summary), Section IV tomato, onion, potato value chains with the farmers' shares, tomato Table 1 |
| RBI WP 07/2024, pulses | https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=22722 | 5 (1 table) | 5/5 | no licence statement found on the page | `rbi_wp_2024_07_pulses` | Excerpts: abstract, shares paragraph, value-chain passage, Table 2 (price build-up, Rs/kg and %) whole |
| RBI WP 06/2024, fruits | https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=22721 | 8 (2 tables) | 8/8 | no licence statement found on the page | `rbi_wp_2024_fruits` | Excerpts: abstract, grapes and banana shares, mango Tables 7 and 8 |
| RBI WP 05/2024, milk, poultry meat, eggs | https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=22720 | 8 (2 tables) | 8/8 | no licence statement found on the page (authors' disclaimer footnote held) | `rbi_wp_2024_poultry` | Excerpts: abstract, shares summary, V.3 with Tables 2 and 3 and the broiler/egg notes |
| PIB 2151371 (1 Aug 2025), NABCONS post-harvest losses | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2151371&reg=3&lang=2 | 4 (3 tables) | 4/4 | no licence statement found on the release page | `pib_2151371` | Whole release bar the visitor counter |
| PIB 2097601 (30 Jan 2025), HCES 2023-24 | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2097601&reg=3&lang=2 | 15 (7 tables) | 15/15 | no licence statement found on the release page | `pib_2097601` | Whole release |
| MoSPI HCES 2023-24 press note, 27 Dec 2024 | https://www.mospi.gov.in/sites/default/files/press_release/HCES_Press_Note_2023-24_27122024_rev.pdf (PDF text layer) | 8 (2 tables) | 8/8 | the extracted text carries no licence or copyright statement | `hces_2023_24_press_note` | Excerpts: findings, Table 1, Figures 4-5 data labels (food-group shares), imputation footnote |
| MoSPI HCES 2022-23 fact sheet | https://www.mospi.gov.in/sites/default/files/publication_reports/Factsheet_HCES_2022-23.pdf (PDF text layer) | 11 (6 tables) | 11/11 | the extracted text carries no licence or copyright statement | `hces_2022_23_factsheet` | Excerpts: coverage, Statements 1, 2, 3, 5, 6, 7 |
| Economic Survey 2025-26, Stat. App. Table 1.19 | https://www.indiabudget.gov.in/economicsurvey/doc/stat/tab1.19.pdf (PDF text layer) | 1 (table) | 1/1 | the extracted text carries no licence or copyright statement | `econ_survey_tab_1_19` | Whole table with notes, 2020-21 to 2022-23 |
| e-NAM portal: FAQs, APMCs, Farmers, Traders, Mandi Board | https://enam.gov.in/resources/FAQs-of-eNam ; …/stakeholders-Involved/Apmcs ; …/farmers ; …/traders ; …/mandi-board | 5 | 5/5 | no licence statement found on these pages | `enam_about` | Excerpts (see NOT OBTAINED for the About page) |

Raw files: `rbi_wp_2024_08_tops__1`, `rbi_wp_2024_07_pulses__1`, `rbi_wp_2024_fruits__1`,
`rbi_wp_2024_poultry__1`, `pib_2151371__1`, `pib_2097601__1`, `hces_2023_24_press_note__1`,
`hces_2022_23_factsheet__1`, `econ_survey_tab_1_19__1`, `enam_about__1` to `__5`, and
`des_agstat_10_1__1` (the DES landing page, kept as evidence of the failure below).

## NOT OBTAINED

- **`des_agstat_10_1`, DES Table 10.1.** The landing page
  (https://desagri.gov.in/document-report/10-1-per-capita-net-availability-of-food-grains-per-day-in-india/,
  "Last updated : 25-08-2026") holds only a link to an Excel file,
  https://desagri.gov.in/wp-content/uploads/2021/04/10.1.xls (29 KB), which TinyFish returned as
  `target_unreachable`. No file written. The brief's fallback, Economic Survey Table 1.19, was obtained
  and carries the same series (its source line is the DA&FW Economics, Statistics & Evaluation
  Division). To get the DES table itself: Harsh to download the .xls from that page in a browser; note
  the upload path says 2021, so it may be older than the Economic Survey table.
- **e-NAM "About" page.** https://www.enam.gov.in/NAMV2/home/about_nam.html now lands on the home
  page, and the home page returns only its menu; the Operational Guidelines PDFs
  (…/Revised-Operational-Guidelines-of-e-NAM.pdf and …/web/docs/namguidelines.pdf) were unreachable.
  `enam_about` is built from the FAQ and stakeholder pages instead. **Commission agents are not
  described on any e-NAM page fetched**; the RBI papers carry them (TOP: mandi fee 1 per cent and
  commission 4 per cent for onion; pulses Table 2: "Arthia commission (2 per cent)").
- **HCES 2023-24 detailed report** (full item-group table for 2023-24) was not sought beyond the
  press note and PIB release; 2023-24 food-group shares are held only as eight chart categories.

## What a drafter must know

1. **RBI paper numbers.** Tomato-onion-potato is WP **08**/2024, not 06; 06/2024 is the fruits paper;
   poultry is 05/2024. The pre-assigned citekey `rbi_wp_2024_08_tops` was kept as instructed; its
   header and bib entry say 08. The conductor may wish to rename it.
2. **Farmers' shares, as the papers state them:** tomato 33.5, onion 36.2, potato 36.7 (abstract
   rounds to 33/36/37); gram ~75, moong ~70, tur ~65; banana 30.8 (abstract 31), grapes ~35 domestic
   (21 export), mango 42-43 (abstract 43); milk ~70, eggs 75 (75.2 three-year average), poultry meat
   56 to farmers and integrators together (farmers under contract only 5-6). The only full price-spread
   tables with rupee values are pulses Table 2, mango Table 7, milk Table 2 and poultry/egg Table 3;
   the vegetable splits are in images (Charts 18-20) and only the prose figures are held.
3. **NABCONS figures are per cent of production lost, split into farm operations and market level**;
   the release gives no single total per crop. Table-1's eggs row (7363.00 under "Million MT") has no
   stated unit and must not be used as tonnes.
4. **Per capita availability: newest official year is 2022-23** (Economic Survey 2025-26), foodgrains
   568.8 g/day; financial-year basis, not comparable with the older calendar-year series.
5. **HCES shares:** 2022-23 has a full 15-group table (Statement 5) and trends back to 1999-00
   (Statements 3, 6, 7). 2023-24 is available only as the PIB/press-note headline shares and chart
   labels. Rural cereals share: 10.75 (2011-12) → 4.91 (2022-23) → 4.99 (2023-24, "cereals and cereal
   substitutes"); the 2023-24 figure is a slight rise, not a continued fall. Beverages, refreshments
   and processed food: rural 7.90 (2011-12) → 9.62 → 9.84; urban 8.98 → 10.64 → 11.09. The 2022-23 and
   2011-12 splits of "cereal" vs "cereals & cereal substitutes" differ in the second decimal; say which.
6. The Economic Survey bib year (2026) is inferred from the 2025-26 edition, not stated in the file.
