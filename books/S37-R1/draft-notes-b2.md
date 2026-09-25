# Draft notes · S37-R1 · batch b2 (C04, C05, C06)

Drafted 2026-09-24/25 under `DRAFT-BRIEF.md`; finished 2026-09-25 under `FINISH-BRIEF.md` (the first
drafter stopped during self-check). Not committed.

## Records written

- `check/records/S37/S37-R1-C04.yml`: Where the consumer's rupee goes: the price build-up
  (derivable, quantitative). RBI WP 07/2024 (pulses), 08/2024 (tomato-onion-potato), fruits,
  milk/poultry/eggs.
- `check/records/S37/S37-R1-C05.yml`: Who decides what is available, at what price, in what place
  (empirical). HLPE 2017 ch. 1 and Summary; the four RBI papers; WCRF NOURISHING (one must-know).
- `check/records/S37/S37-R1-C06.yml`: Where a country's food comes from (derivable, quantitative).
  FAO FBS handbook 2001 ch. II and IV; Economic Survey 2025-26 Table 1.19; PIB 2200287;
  `s37_edible_oil_duty` (24 Sep 2026).

`python check/build.py --check`: blocking 0 (whole corpus at time of finishing). Warnings on these
three: only `openstax_prealgebra_2e` unopened on C04 and C06 (derivable anchor; not fetched, no held
file; content is Book 0 A4/A5/C9 arithmetic).

Withdrawn sources: none of the three cites `eca_1955` or `food_corporations_act_1964` (checked).

## Self-check done at finish

- Every quote searched in its source file (build plus `scratch-b2/verify.py`, `q2.py`); every
  number's quote states the number. Quoted phrases in prose (e.g. "bears the maximum risk of
  perishability and wastage", "declares daily region-specific farm gate prices for eggs", "meeting
  around 72% of our projected domestic requirement") found verbatim. The milk-cooperative table
  in C04 practice (35, 3, 2, 1, 2, 1, 1.5, 3.5; 49) checked against RBI poultry paper Table 2.
- Every `working` line and every practice answer recomputed in Python; all hold at the precision
  shown. The only unparsed line is the deliberately wrong level-8 prompt in C04.
- Table 1.19 identity recomputed on all 18 rows. **Fixed:** C06's `verified.note` said sixteen rows
  close; it is thirteen. Five miss: rice, cereals, foodgrains 2022-23 (4,567 / 4,572 / 4,572) and
  pulses, foodgrains 2021-22 (-102 / -101). The illustration's claims (rice 2022-23 the only large
  single-food gap; pulses 2021-22 the other) were right. **Added** to C06 level 10 that the 2021-22
  foodgrain row misses by 101 (about 0.2 g a day).
- Small fixes: "a SSR" to "an SSR"; C04's mandi gloss aligned with C02's glossary sense
  ("regulated wholesale market"); one over-long definition line rewrapped.
- SELFCHECK 4a: every share, ratio and per-capita figure is stated with its route, year or scope;
  C06 says national availability is not a state's or a household's intake.
- Figures: `draw.py --book S37-R1` passes; the four PNGs looked at, values match the text.

## Anything unsourced or caveated

- `openstax_prealgebra_2e` (C04, C06) is `opened: false`: the instrument needed is OpenStax
  *Prealgebra 2e* ch. 6, Percents (mark-up; percentage of a stated base). Derivable, so it warns.
- RBI TOP paper's 5.3 per cent trader margin has no stated base; C04 says so and never subtracts it.
- FAO IDR formula is laid out as a fraction drawn with underscores in the HTML; read as numerator
  over denominator (noted in `verified.note`). IDR uses FAO's definition, not imports ÷ consumption.
- PIB 2200287 prints self-sufficiency 43.74 against 43.75 from its own two figures; C06 says which.
- PIB 2200287's per capita edible oil consumption (C06 level 6): the release does not name the survey.
- Table 1.19's 2022-23 rice row gap is shown, not explained; C06 tells the reader not to guess.
- C05's element-to-actor table is drawn only from the chains the RBI papers traced (named places).

## Practice-set sizes

- **C04, 13** (levels 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10): three moves (build-up by addition,
  share of a base, reversing the base) plus the processed-food unit trap; each gets a mechanical
  and an applied problem, and the base trap gets its own diagnostic.
- **C06, 14** (levels 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10): four moves that compose (the
  identity with its stock sign, per capita per day with unit changes, IDR and SSR, working back);
  two diagnostics because the sign and the net-imports error are different mistakes.
- C05 is not quantitative.

## Figures

- C04: `s37-r1-c04-gram-tur-rupee.png` (grouped bars, rupees added per stage, gram and tur, checks
  sum 71 and 111); `s37-r1-c04-farmer-share.png` (nine farmer's shares, 30.8 to 75.2 per cent).
- C06: `s37-r1-c06-pulses-identity.png` (22801, 1733, -615, 23919; check holds);
  `s37-r1-c06-self-sufficiency.png` (cereals 111.1, edible oil 43.75, reference line at 100).
- **C05, wanted, not drawable** (`figure_note`): a flow picture. Left to right, the chain stages
  (farmer, contracting processor or pre-harvest contractor, trader, mandi with APMC fee and
  commission, wholesaler, processor with brand, retailer) with arrows into one box on the right, "food
  environment", split into four cells (what is there and how near; what it costs; how it is
  promoted; what quality), each cell with arrows from the actors that set it (as C05's table). A
  person stands outside the box; a leaflet arrow reaches only the person, not the box. No numbers.

## Glossary rows

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| farm-gate price | the price the farmer received at the first sale | `S37-R1-C04` |
| farmer's share of the consumer rupee | the farm-gate price divided by the retail price, times 100: the part of each Rs 100 paid at the shop that reaches the farmer, before the farmer's own costs | `S37-R1-C04` |
| margin | what is left of a mark-up after the actor's own costs of handling the unit | `S37-R1-C04` |
| mark-up | an actor's selling price minus its buying price; it holds that actor's costs and its margin | `S37-R1-C04` |
| retail price | the price paid for a unit of food at the shop | `S37-R1-C04` |
| food environment | the place where a person meets the food system: what is there and how near, what it costs, how it is promoted, what quality it is (HLPE 2017) | `S37-R1-C05` |
| integrator model | broiler farming in which a company markets the farmer's birds | `S37-R1-C05` |
| pre-harvest contractor | a buyer who contracts with a farmer before harvest to fix the price and quantity | `S37-R1-C05` |
| import dependency ratio (IDR) | imports divided by production plus imports minus exports, times 100 (FAO) | `S37-R1-C06` |
| net availability (of foodgrains) | production less seed, feed and wastage, less exports, plus imports, less the rise in stocks: what was there to be eaten, not what was eaten | `S37-R1-C06` |
| self-sufficiency ratio (SSR) | production divided by production plus imports minus exports, times 100 (FAO) | `S37-R1-C06` |
| supply for domestic utilization | production plus imports minus exports, minus the rise in stocks (or plus the fall), over a stated period (FAO) | `S37-R1-C06` |

`stock`, `flow` and `identity` are used in Book 0's senses (`B0-R0-C23`; `S02-R1-C17` for identity).
`mandi` and `APMC` are used in C02's senses.
