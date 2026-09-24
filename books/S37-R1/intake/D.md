# Source intake log · S37-R1 · group D (chains, availability, spending)

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
