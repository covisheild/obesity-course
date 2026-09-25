# Source intake log · S37-R1 · group B (the state as provider)

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
