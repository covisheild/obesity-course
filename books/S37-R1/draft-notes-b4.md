# Draft notes · S37-R1 · batch b4 (C10, C11, C12)

Drafted 2026-09-24 by the first b4 drafter, which was stopped during its self-check before it wrote
these notes. Finished 2026-09-25 under `FINISH-BRIEF.md`. Not committed.

## Records written

- `check/records/S37/S37-R1-C10.yml`: How the state moves a price: support price, subsidy, import
  duty (derivable, quantitative). PIB 2260617 (kharif MSP 2026-27), PIB rabi MSP 2026-27, DFPD
  Foodgrains Bulletin December 2025 and Year End Review 2025 (`s37_economic_cost_grain`), PIB
  2314297 edible-oil duty cut of 24 Sep 2026 (`s37_edible_oil_duty`), PIB 2200287, PIB 1980689,
  NFSA 2013. Textbook anchor OpenStax *Prealgebra 2e* ch. 6, `opened: false`.
- `check/records/S37/S37-R1-C11.yml`: The National Food Security Act and the public distribution
  system (institutional). NFSA 2013; PIB 1980689; DFPD Year End Review 2025; DFPD Annual Report
  2025-26 (`dfpd_pds`).
- `check/records/S37/S37-R1-C12.yml`: School meals and anganwadi food (institutional). NFSA 2013
  ss. 2(1), 4-7, Schedule II; PIB 1812421 (PM POSHAN norms); Saksham Anganwadi and Poshan 2.0
  guidelines 2022; PIB 2251769.

`python check/build.py --check` (on a copy of the repository with other batches' unfinished S37
records set aside): blocking 0 for these three. One warning is left: C10's OpenStax anchor is not
opened. This drafter was barred from the web, and C10 is derivable, so it warns and does not block.

## What the finishing pass changed

- **Withdrawn sources.** None of the three cited `eca_1955` or `food_corporations_act_1964`. C11's
  definition names the Essential Commodities Act, 1955 only in NFSA s. 2(4)'s own words, which are
  quoted from `nfsa_2013`.
- **C10.** The 300 quote for the 2022-23 issue price was cut so that the build's number reader
  does not merge "300 200" into one number. The line saying the section would switch to ÷ and ×
  was removed, because the section never switches. The edible-oil `analogy_breaks_when` had
  paired the backgrounder's 16.5 per cent "effective customs duty" with the June 2025 basic duty of
  10 per cent. The source does not make that pairing, so the text now says only what the
  backgrounder says. A level 9 answer said C09 showed procurement is "in a few States". C09 says
  the opposite: its figures cannot show which States. The answer now uses C09's point that a farmer
  may sell to the agency or in the open market. A forward pointer to C13 was cut. `nfsa_2013` was
  added to the refs of the 5 kg wheat problem.
- **C11.** The free-grain quote was extended to include "under the Pradhan Mantri Garib Kalyan Anna
  Yojana (PMGKAY)", so that it carries the scheme name the definition gives.
- **C12.** Ten references were added so that every sentence taken from the 2022 guidelines or the
  2026 backgrounder has its quote. These cover the approval period, the "under revision" note, the
  funding pattern, the 300 days, "bridge the gap", "driven by calorie intake", jaggery, the food
  items being State-specific, raw ration and THR in lieu, and "revised in January 2023". The 450 and
  700 number quotes were split so that each states its number. The "gap between need and intake"
  sentence now uses the guidelines' own words. The THR must-know now says "severely malnourished",
  as the guidelines do, and its kind is changed from `number` (it carried none) to `move`.

## Unsourced or caveated

- **Anganwadi norms (C12).** The 500 kcal and 12-15 g figures are the Schedule II and 2022 table
  values. The 2022 table is marked "under revision". PIB 2251769 says the norms were revised in
  January 2023 but gives no figures. The revised norms are not held. The record says this every
  time it quotes 500.
- **PM POSHAN (C12).** The Ministry of Education's 2023 guidelines are not held. The norms come from
  PIB 1812421, a 2022 Lok Sabha reply by the Minister of Women and Child Development. No held
  document gives PM POSHAN's Centre-State cost sharing, and the record states none. The
  anganwadi cost sharing (50:50, 90:10, 100:0) is from the 2022 guidelines' table.
- **Scheme approvals (C12).** Both schemes were approved for 2021-22 to 2025-26. Nothing held says
  whether either runs beyond that or on what terms. The must-know says to find the current approval.
- **Economic cost (C10).** The 2025-26 budget estimate is the newest figure held. The 2026-27 figure
  would need a newer Foodgrains Bulletin.
- **Edible-oil duty (C10).** Basic customs duty only. The release gives no effective duty, no
  refined-oil rates and no notification number. Every world price is labelled made up.
- **C10 exercise 1.** "When the issue price was Rs 300 a quintal it was fixed, so it did not follow
  the MSP" is read from the bulletin rows (300 in both 2021-22 and 2022-23) and from Schedule I's
  "fixed by the Central Government". No held text states it in those words.
- **Kharif and rabi (C10)** are glossed in plain words ("sown with the monsoon", "sown after the
  monsoon, in winter") without a source. C09 may carry a sourced gloss that the compression pass
  could point to instead.

## Practice-set size

- **C10: 14.** The section teaches three moves: a margin over a base, a subsidy as a gap, and a
  price times one plus a rate. Each move gets its own mechanical and applied problems. Two of the
  moves have a named trap (the base of the margin, and "halved duty, halved price"), and each trap
  gets a diagnostic and a transfer problem. Levels 1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9, 10. Every
  answer and every `working` line in all three records was recomputed in Python.
- C11 and C12 are not quantitative. C13 carries the arithmetic on rations and meals.

## Figures

- **C10:** `s37-r1-c10-duty-landed-price.png`, the landed price against the duty for a made-up Rs
  100 before duty (a fit, y = 100 + x). Also `s37-r1-c10-rice-subsidy-share.png`, bars of the rice
  subsidy as a percentage of economic cost, 2021-22 to 2025-26 (91.6, 91.9, 100.0, 100.0, 100.0).
- **C11:** `s37-r1-c11-household-entitlement.png`, kg a month against household size, priority
  (5 kg a person) against Antyodaya (35 kg flat), crossing at 7.
- All three were drawn by `draw.py --book S37-R1` with no problems. I looked at each one: the
  numbers match the text, the bars start at zero, and no label sits over the data.
- **C12: figure_note.** Book 0 F2 already draws Schedule II's energy column, and C13 draws school-meal
  energy. **Wanted, not drawable (a flow diagram):** four boxes top to bottom, from the C12 teaching
  answer. (1) Parliament: NFSA 2013 s. 5(1)(a) and Schedule II, "500 kcal, 12-15 g protein, old
  norm, revised January 2023, new figures not held". (2) Union ministry (Women and Child
  Development): Poshan 2.0 guidelines 2022, who gets THR and who gets HCM, at least 300 days. (3)
  State: runs the scheme, pays its share of supplementary nutrition (half where the State has a
  legislature, outside the north-eastern and Himalayan States), sets the food items. (4) Anganwadi
  centre: cooks and serves. Draw a side arrow from box 3 labelled "to change the plate, go here".

## Glossary rows

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| anganwadi | a government child care and development centre, set up under the Integrated Child Development Services Scheme | `S37-R1-C12` |
| Antyodaya household | one of the poorest households under the National Food Security Act, entitled to 35 kg of grain a month for the whole household | `S37-R1-C11` |
| basic customs duty | the duty charged at the border on an import, as a percentage of its value before duty; not the same as the "effective" duty some releases quote | `S37-R1-C10` |
| central issue price | the price at which the Union government issues grain to the States for the public distribution system; zero for NFSA households since 1 January 2023 | `S37-R1-C10` |
| economic cost (of grain) | what grain costs the government to buy, store and move: acquisition cost plus distribution cost | `S37-R1-C10` |
| fair price shop | a ration shop, licensed to hand out grain to ration-card holders | `S37-R1-C11` |
| hot cooked meal (HCM) | a meal cooked on the day and eaten at the anganwadi or school | `S37-R1-C12` |
| landed price | the price of an import at the port after duty: the price before duty times one plus the duty rate | `S37-R1-C10` |
| margin over cost | the gap between a price and a cost, as a percentage of the cost, not of the price | `S37-R1-C10` |
| price wedge | a gap that a public decision opens between two prices of the same food | `S37-R1-C10` |
| priority household | a household under the National Food Security Act entitled to 5 kg of grain a month for each person in it | `S37-R1-C11` |
| ration card | the document a State issues that lets a household buy or collect grain at a fair price shop | `S37-R1-C11` |
| subsidy (on ration grain) | the economic cost minus the issue price: what the government pays that the household does not | `S37-R1-C10` |
| take-home ration (THR) | a prepared food, not raw grain, handed out at the anganwadi to be eaten at home | `S37-R1-C12` |
