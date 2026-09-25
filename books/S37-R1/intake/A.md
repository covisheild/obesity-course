# Source intake log · S37-R1 · group A (frameworks and international)

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
