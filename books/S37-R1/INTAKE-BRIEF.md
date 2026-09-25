# Source intake brief · S37-R1 (one brief, four intake subagents A–D)

You are an intake subagent for book S37-R1. Repo: `/home/claude/obesity-course`, branch `book/S37-R1`
(already checked out). **Do not commit, do not switch branch, do not push.** The conductor merges and
commits. Your group letter and source list are in your prompt.

## Read first (only these)
- `sources/SOURCES.md` (whole) — the transcription rule and why it exists.
- The header of `sources/chow_hall_2008.txt` (first ~60 lines) and of `sources/nss_594_nutritional_intake.txt`
  (first ~40 lines) — the file format to copy.
- `books/S37-R1/READY.md` — your sources' rows (URLs are search leads, not confirmed).
- `books/S37-R1/INVENTORY.md` — only the rows of the concepts your sources serve, so you know which
  passages the drafters will need.
- `books/S02-R1/INTAKE.md` (first 40 lines) — what the intake log looks like.

## The rule (non-negotiable)
1. **Transcribe only with `mcp__TinyFish__fetch_content`** (load it with ToolSearch
   `select:mcp__TinyFish__fetch_content`). Never store WebFetch output; never use curl/wget/Python HTTP.
   WebSearch / WebFetch may be used only to *find* the right URL. If TinyFish is not available to you,
   stop and say so.
2. Save every raw fetch result **unchanged** to `/home/claude/intake-raw/<GROUP>/<citekey>__<n>.txt`
   (decode the JSON to its text; do not edit). The conductor re-verifies from these files.
3. Every stored passage is a **contiguous slice** of the raw text, cut by script (`raw[i:j]`), not
   retyped. Omissions marked `[...]` in place with a `[NOTE]` saying what was left out. Tables between
   `[TABLE]` and `[END TABLE]`. Your own words only on lines starting `[NOTE]`.
4. **Header says exactly what the file holds** (which sections/tables; "EXCERPTS" if not whole). Never
   call an excerpt complete. Include CITATION, URL fetched, date fetched (2026-09-24), the tool, and the
   **licence / terms as stated by the source itself** (quote it; if the page states none, say "no
   licence statement found on <page>"; never assume).
5. Take generous passages: every sentence, table row and figure the concept rows need, **with the
   numbers and their as-of dates/units**, plus enough context to show what the number is (the table
   title, column headers, footnotes). For PDFs: TinyFish returns the text layer; if it returns no text
   or garbage (scanned image), record the source as NOT OBTAINED with the reason.
6. Official Indian figures: take the newest official release. For MSP / FRP / duty / economic cost,
   record the season or date of the figure.
7. After writing each file, run a check: re-parse your file, and for every non-`[NOTE]` passage line
   block confirm it is a whitespace-normalised substring of the raw fetch it came from. Report the
   count (e.g. 14/14).
8. No secondary summaries (news, PRS, coaching sites, mirrors) are stored. If the only reachable copy
   of an official document is a mirror, record NOT OBTAINED and name the mirror in a [NOTE] in your log.

## What you write
- `sources/<citekey>.txt` for each source obtained (file name = citekey unless told otherwise).
- `books/S37-R1/intake/<GROUP>.md` — your log: a table (source, URL fetched, passages, verbatim check
  n/n, licence as stated, citekey, what the file holds) and a list of NOT OBTAINED with the reason and
  what a person would need to do (e.g. "PDF is a scanned image; Harsh to download X from Y").
- `books/S37-R1/intake/<GROUP>.index.yml` — the `sources/INDEX.yml` entries (same shape as existing
  ones: `citekey: {file:, what:}`), `what` stating exactly what the file holds.
- `books/S37-R1/intake/<GROUP>.bib` — BibTeX entries for `check/references/library.bib`, same style as
  existing ones (`@misc` for instruments and web pages, `@techreport` for reports, `@article` for
  papers; `url`, `urldate = {2026-09-24}`). **No repository path in any field.**
- `books/S37-R1/intake/<GROUP>.sources.md` — rows for the table in `sources/SOURCES.md`
  (| file | what it is | words | verified in it |), the "verified in it" column listing only what you
  found in the file.

**Citekeys are pre-assigned below.** Use exactly these; if you need an extra one, prefix it with
`s37_` and say so. Do not edit `sources/INDEX.yml`, `library.bib` or `sources/SOURCES.md` yourself.

Reply in at most 150 words: obtained n of m, verbatim check totals, NOT OBTAINED list with reasons,
anything a drafter must know (e.g. a figure that differs from what READY.md expected).

## Groups and citekeys

**A — frameworks and international**
- `hlpe_2017` HLPE Report 12 *Nutrition and food systems* (2017): food-system definition, the
  conceptual framework (Figure 1 and its text), food environments, drivers.
- `wcrf_nourishing` WCRF NOURISHING framework page(s).
- `fao_fbs_handbook_2001` FAO *Food Balance Sheets: a handbook* (2001): the supply/utilisation identity.
- `unep_fwi_2024` UNEP *Food Waste Index Report 2024*: definitions of food loss vs food waste; India's
  household food waste estimate (kg/capita/year) and its confidence level.
- `who_double_duty_2017` WHO *Double-duty actions for nutrition: policy brief* (2017).
- `hawkes_2020_double_duty` Hawkes et al. *Lancet* 2020;395:142 (use a PMC/open copy if one exists).
- `swinburn_2019_syndemic` Swinburn et al. *Lancet* 2019;393:791 (verify_at_intake: summary + the
  definition of the Global Syndemic; if blocked, NOT OBTAINED).
- `popkin_2012_transition` Popkin, Adair, Ng *Nutr Rev* 2012;70:3 (PMC3257829): abstract and the
  stages passage only.
- `nfhs5_india_factsheet` NFHS-5 (2019-21) India fact sheet: stunting, wasting, underweight, anaemia,
  overweight/obesity rows (children, women, men).

**B — the state as provider**
- `pib_2082323`, `pib_2251769` the two PIB releases named by amendment S37-R1-A01 (whole text).
- `pib_1980689` PMGKAY free foodgrains, 81.35 crore beneficiaries (whole text).
- `pib_1847548` Saksham Anganwadi and Poshan 2.0 PIB summary (whole text).
- `pm_poshan_guidelines_2023` PM POSHAN guidelines: coverage, the food norms table (g per child per
  day), calorie and protein norms, cost sharing; plus the "About us" page if the PDF fails.
- `poshan2_guidelines_2022` Mission Saksham Anganwadi and Poshan 2.0 guidelines: supplementary
  nutrition norms (energy, protein per beneficiary category), THR vs HCM, beneficiaries.
- `ifct_2017` ICMR-NIN *Indian Food Composition Tables 2017*: energy and protein per 100 g for rice
  (raw, milled), wheat flour (atta) and whole wheat, the main pulses (e.g. red gram/arhar dal, bengal
  gram), and the main millets (jowar, bajra, ragi). Record the table numbers and units (kJ and/or kcal).
- `dfpd_pds` DFPD pages describing the PDS/TPDS and its history.

**C — prices, procurement, trade, missions**
- `pib_2260617` Kharif MSP 2026-27 (whole text incl. the cost and margin table).
- `pib_rabi_msp` the newest rabi MSP release (wheat) — find the PRID; name the file `pib_rabi_msp.txt`
  and put the PRID in the header.
- `pib_sugarcane_frp` the newest sugarcane FRP release.
- `cacp_about` CACP "About us"/mandate page (establishment 1965, mandated crops).
- `fci_about` FCI "About us"; `food_corporations_act_1964` the Act from India Code (s.13 functions at least).
- `s37_economic_cost_grain` an official statement of the economic cost of rice and wheat per quintal
  for the newest year (FCI/DFPD page, or a PIB reply in Parliament) and the central issue price.
- `s37_edible_oil_duty` the newest official statement of the basic customs duty on crude edible oils
  (PIB release preferred; CBIC notification otherwise).
- `pib_2061646` NMEO-Oilseeds; `pib_2200287` NMEO-Oil Palm (whole text; import dependence figures).
- `pib_millets` the newest PIB release on the millet mission / Shree Anna (name file `pib_millets.txt`).
- `eca_1955` Essential Commodities Act 1955 (India Code): s.3 (power to control production, supply,
  distribution, incl. stock limits) at least.

**D — chains, availability, spending**
- `rbi_wp_2024_08_tops` RBI DEPR Working Paper 06/2024 (tomato, onion, potato): abstract, the
  farmers'-share table/numbers; `rbi_wp_2024_07_pulses` WP 07/2024 (pulses); and the companion
  fruits and poultry/eggs papers if reachable (`rbi_wp_2024_fruits`, `rbi_wp_2024_poultry`).
- `pib_2151371` NABCONS post-harvest loss study as reported (whole text, the loss table).
- `enam_about` e-NAM "About" page (APMC mandi, commission agents).
- `des_agstat_10_1` DES Table 10.1 per capita net availability of foodgrains per day (with years);
  `econ_survey_tab_1_19` the Economic Survey Statistical Appendix Table 1.19 if DES fails.
- `pib_2097601` HCES 2023-24 PIB release; `hces_2023_24_press_note` MoSPI press note (the food-group
  share table, rural and urban); `hces_2022_23_factsheet` the 2022-23 factsheet (food-group shares).
