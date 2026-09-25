# Draft notes · S37-R1 · batch b1 (C01, C02, C03)

Drafted 2026-09-25 under `DRAFT-BRIEF.md`. Not committed.

## Records written

- `check/records/S37/S37-R1-C01.yml`: What a food system is (institutional). HLPE 2017 only.
- `check/records/S37/S37-R1-C02.yml`: One fresh food from field to plate in India (empirical).
  RBI WP 08/2024 (onion and potato chains), e-NAM FAQ, PIB 2151371 (NABCONS), UNEP FWI 2024.
- `check/records/S37/S37-R1-C03.yml`: A packaged food is many chains meeting (institutional).
  FSS (Labelling and Display) Regulations 2020, compendium Version-VIII.

`python check/build.py --check`: blocking 0 for these three. One warning left, C01's definition
sentence of 39 words, which is HLPE's definition quoted whole (the definition field may be exact).

## Unsourced or caveated

- **Retail formats** (kirana, cart, modern trade, quick commerce), asked for in the inventory's C02
  row: no held source describes them. C02 names only what RBI WP 08/2024 says: retailers in
  "neighbourhood markets in urban areas", organised retailers (HOPCOMS, SAFAL, Namdhari Fresh) for
  tomato, and contract sales to processors for potato. Kirana and quick commerce are not mentioned.
- **HLPE Figure 1 actor-to-step pairing** (C01): only the text layer is held. The record pairs each
  actor list with the step name before it in the extraction order, and says so in `verified.note`.
  Confirm against the printed figure at audit.
- **The eight stages** (C01) are this book's reading of two HLPE sentences, and the record says so.
  HLPE prints no eight-stage list.
- **C01 roti table and C03 chain table** are sketches. Both say so in the text, and C03's
  ingredient list is marked made up. "Farm, trader, flour mill" and so on are generic and
  unsourced on purpose; they are framed as questions to check.
- **NABCONS figures** come from the ministry's release, not the study. The release does not say
  per cent of what, and gives no per-crop total. The record never adds the two columns.
- **Table-1 eggs row** (7363.00 under "Million MT") is used as the failure case in C02, compared
  with Annexure-I's 337033 thousand tonnes for 2022-23 from the same release. Its unit is not
  guessed.
- **NABCONS** is not expanded. The release gives only "NABARD Consultancy Services Pvt. Ltd.", and
  NABARD's own expansion is not in any held file. The prose says "the consultancy NABCONS".
- **Kharif and rabi** are left out of the prose. The onion weight loss is given as "around 10 or 5
  per cent depending on the season the onion was grown in"; the words are in the numbers' quotes.
- **C03, origin of ingredients:** I searched the whole held labelling file for "origin". Only
  imported foods need a country of origin; the other hits are veg/non-veg marks and the
  misleading-claims clause. Noted in `verified.note`.

## Practice sets

None. C01 to C03 are not quantitative in the inventory (`quantitative: false` set explicitly).

## Figures

- **C02**: `s37-r1-c02-post-harvest-loss.png`, grouped bars, farm-operations against
  market-level per cent loss for paddy, wheat, tomato, onion and potato (NABCONS, 2020-22).
  `from_table` block 1. Drawn, looked at; the values match the table.
- **C01, wanted, not drawable** (figure_note): a flow of eight stage boxes (production, storage,
  processing, distribution, retail, preparation, consumption, waste), each with its actor (farmer;
  farmer, trader or warehouse; flour mill; distributor or transporter; shopkeeper; whoever cooks;
  the household; the household) and arrows between. Two boundaries drawn round it: a small one round
  preparation, consumption and waste, labelled "your kitchen", with atta and fuel crossing in and
  scraps crossing out; a large one round all eight, labelled "India", with "food bought from other
  countries" crossing in and "food sold to other countries" crossing out. No numbers.
- **C03, wanted, not drawable** (figure_note): several chains converging on one factory. From left:
  wheat (farm, trader, flour mill), sugar crop (farm, sugar mill), oil palm (plantation, oil mill,
  refinery; "which country?"), milk (dairy farm, dairy plant), salt, and a greyed "Choco chips
  (under 5 per cent: own chains not declared)". All feed one box, "factory: processing, packaging,
  brand", then one chain out (distribution, retail, household). A dashed line at the factory door
  labelled "what the label can see". No numbers.

## Glossary rows

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| actor (in a food system) | anyone whose decision moves the food on: a farmer, a trader, a mill, a shopkeeper, the person who cooks | `S37-R1-C01` |
| APMC (Agricultural Produce Marketing Committee) | the body, set up under state law, that runs a regulated mandi and fixes its fees | `S37-R1-C02` |
| brand owner | the company whose name and address the label must carry, which may be the maker or only the marketer | `S37-R1-C03` |
| class title | one name the labelling regulation allows for a whole group of ingredients, such as "Sugar" for sucrose | `S37-R1-C03` |
| commission agent | a middleman paid a percentage for arranging a sale in a mandi | `S37-R1-C02` |
| compound ingredient | an ingredient that is itself made of two or more ingredients | `S37-R1-C03` |
| food loss | food that leaves the supply chain before the shop: in the field, in sorting, in storage, in transport (UNEP: up to, and excluding, retail) | `S37-R1-C02` |
| food supply chain | HLPE's name for the activities and actors that take food from production to consumption and to the disposal of its waste; its steps stop at retail and markets | `S37-R1-C01` |
| food system | everything that happens to food, and everyone who does it, from the field to the bin (HLPE's 2014 definition) | `S37-R1-C01` |
| food waste | food, with its inedible parts such as peels and bones, thrown away at the shop, in food service or at home | `S37-R1-C02` |
| mandi | a regulated wholesale market for farm produce, run under state law | `S37-R1-C02` |
| quintal | 100 kg | `S37-R1-C02` |
| stage (of a food system) | one of this book's eight kinds of activity: production, storage, processing, distribution, retail, preparation, consumption, waste | `S37-R1-C01` |

`boundary`, `stock` and `flow` are used in Book 0's senses (`B0-R0-C33`, `B0-R0-C23`).
