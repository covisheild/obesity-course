# Draft notes · S37-R1 · batch b3 (C07, C08, C09)

Drafted 2026-09-24 by an earlier b3 drafter (stopped during self-check). Finished 2026-09-25 under
`FINISH-BRIEF.md`. Not committed.

## Records written

- `check/records/S37/S37-R1-C07.yml`: What Indians eat and spend on food, measured (empirical,
  quantitative, 12 practice problems). HCES 2022-23 factsheet, PIB 2097601 (HCES 2023-24), NSS
  Report 594, Popkin 2012 (forward pointer only).
- `check/records/S37/S37-R1-C08.yml`: Built against hunger (empirical). DFPD Annual Report
  2025-26, Economic Survey 2025-26 Table 1.19, NFSA Schedule II.
- `check/records/S37/S37-R1-C09.yml`: Minimum support price and procurement (institutional).
  NFSA s.2(2), s.2(10); PIB 2260617 (kharif MSP 2026-27), PIB 2173567 (rabi MSP 2026-27), PIB
  2258113 (sugarcane FRP 2026-27), PIB MSP backgrounder (10 Oct 2025), DFPD Year End Review 2025.

`python check/build.py --check`: blocking 0 overall and for these three; no warnings on them.
Every quote re-found in its file; every `numbers` quote states its value (build gate plus
`/home/claude/scratch-b3/quotes.py`). Every working line and practice answer recomputed in
`/home/claude/scratch-b3/recompute.py`.

## What finishing changed

- **C08, withdrawn source.** `food_corporations_act_1964` removed (two references, one must-know
  ref, the illustration's first step, the retrieval exercise and one retrieval item). FCI's job is
  now sourced from DFPD Annual Report 2025-26 para 3.64 ("the main instrument ... for procurement
  and distribution of wheat, rice and coarse-grains ... maintaining the buffer stock"). The Act is
  named only as "an Act of 1964", from DFPD's history sentence; its s.13 and its Act number are
  no longer stated. The unused NFSA long-title reference was dropped. No `eca_1955` use in any of
  the three.
- **C07.** Two references added so every must-know claim has a quote: the MRP/MMRP note (reference
  periods before 2009-10 differ) and 2.9.6.0's last sentence (intake depends on cooking); the
  2.9.6.0 quote extended to carry "committee ... in 2025". One critique prompt split; one level-10
  sentence softened.
- **C09.** Kharif and rabi were used undefined; a gloss added (see below).

## Unsourced or caveated

- **C08 scope gaps (inventory row):** the Green Revolution, 1960s import dependence and CACP's
  founding (1965, "Agricultural Prices Commission") are not covered: no held source (CACP "About
  us" 403; the Acts withdrawn). The section rests on DFPD's own history and the Economic Survey.
- **C08 "coarse grains, the cereals other than those two"** (simplified explanation): my gloss;
  no held file defines coarse grains. Confirm or cut at audit.
- **C09 "kharif / rabi ... India's two main crop seasons"**: gloss not stated in any held file (the
  releases use the words without defining them). The "marketing season, the months when the crop
  is sold" gloss is likewise mine.
- **C09 "procurement concentrated in a few states"** (inventory row): no held release gives
  state-wise procurement; the record says so in its boundary point and `analogy_breaks_when`.
- **C07:** NSS 594 revised its conversion table in 2025; the report does not say in the held text
  whether its 2011-12 column was recomputed with the new table. The record compares within Table
  3.14 only, as the report itself does, and a trap point tells the reader to ask.
- **C07:** 2023-24 food-group shares are held only as headline percentages (PIB) and chart labels;
  the record says eight groups against fifteen.
- **C09 as-of:** rabi MSP is RMS 2026-27 (1 Oct 2025); the RMS 2027-28 decision is due about
  October 2026 and is the review trigger. PM-AASHA continuation held only "up to 2025-26".

## Practice set

- **C07: 12 problems** (levels 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10). The technique has several
  moves that compose: part ÷ whole, share back to amount, points against per cent, which base a
  share is of, the ratio of two shares, and rounding from printed rupees. Each gets at least one
  problem, reversed at least once; twelve reaches both ends without repeating a move.
- C08, C09: not quantitative in the inventory.

## Figures

All drawn by `python check/figures/draw.py --book S37-R1`, looked at, values recomputed.

- C07 `s37-r1-c07-rural-shares.png`: grouped bars, cereals against beverages/processed food share
  of rural MPCE, 2011-12, 2022-23, 2023-24 (from the illustration's table).
- C08 `s37-r1-c08-net-imports.png`: net imports 2022-23, rice, wheat, other cereals (negative) and
  pulses; check that the three cereals sum to -30352.
- C09 `s37-r1-c09-kharif-procurement.png`: paddy 8418 against the other 13 kharif crops 328 lakh
  tonnes, 2014-15 to 2025-26; `s37-r1-c09-msp-floor.png`: 1.5 times cost against MSP for paddy
  (kharif 2026-27) and wheat (rabi 2026-27).
- Wanted, not drawable: none.

## Glossary rows

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| buffer stock | grain the state holds in reserve | `S37-R1-C08` |
| central pool | the Government's own stock of grain, bought at MSP and held for the ration system and other schemes (NFSA s.2(2)) | `S37-R1-C09` |
| coarse grains | the cereals other than wheat and rice (unsourced gloss; see notes) | `S37-R1-C08` |
| Commission for Agricultural Costs and Prices (CACP) | the body of experts that recommends MSPs and the sugarcane FRP | `S37-R1-C09` |
| fair and remunerative price (FRP) | the price the Union Government fixes for sugarcane, which sugar mills must pay | `S37-R1-C09` |
| Household Consumption Expenditure Survey (HCES) | MoSPI's survey of what a sample of households spent on goods and services | `S37-R1-C07` |
| kharif, rabi | the names the MSP releases use for India's two main crop seasons | `S37-R1-C09` |
| marketing season | the months when a season's crop is sold | `S37-R1-C09` |
| minimum support price (MSP) | the price at which government agencies stand ready to buy a crop, announced before the season | `S37-R1-C09` |
| monthly per capita consumption expenditure (MPCE) | a household's spending in a month divided by the number of people in it | `S37-R1-C07` |
| net imports | imports minus exports; a minus sign means more went out than came in | `S37-R1-C08` |
| procurement | the state buying grain from farmers | `S37-R1-C08` |
| quintal | 100 kilograms | `S37-R1-C09` |
| share of MPCE | a group's spending divided by all spending, times 100 | `S37-R1-C07` |
