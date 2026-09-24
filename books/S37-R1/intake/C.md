# Source intake log · S37-R1 · group C (prices, procurement, trade, missions)

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
