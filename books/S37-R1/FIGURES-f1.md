# Figure plan · S37-R1 · planner f1 (C01 to C09)

Done 2026-09-25 under `FIGURE-BRIEF.md`. Not committed. Only `figures:`, `figure_note` and spec
`derived` entries were edited; no prose touched. `python check/figures/draw.py --book S37-R1`: 0
problems. `python check/build.py --check`: blocking 0. Every PNG below opened and looked at.

## C01 · What a food system is: figure_note (kept)

No numbers to chart; the note names the wanted diagram. **Wanted (later contract-change chat):**
eight stage boxes in a row (production, storage, processing, distribution, retail, preparation,
consumption, waste), each with its actor (farmer; farmer, trader or warehouse; flour mill;
distributor or transporter; shopkeeper; whoever cooks; the household; the household), arrows
between. A small boundary round the last three, "your kitchen", with atta and fuel crossing in and
scraps crossing out; a large boundary round all eight, "India", with "food bought from other
countries" in and "food sold to other countries" out. No numbers.

## C02 · One fresh food from field to plate

- `s37-r1-c02-post-harvest-loss.png` (drafter's, kept): grouped bars, farm operations against
  market level, per cent lost, five crops, `from_table` block 1. Farm bar above market bar in every
  row, as the text says; no total drawn (the release gives none).
- `s37-r1-c02-household-waste-range.png` (new): three bars, lowest of the 7 city studies 20, UNEP's
  India estimate 55, highest 88 kg per person a year. Shows the national figure is scaled from a
  wide spread of city studies. All three numbers stated in the illustration. No relation drawn.

## C03 · A packaged food is many chains meeting: figure_note (kept)

Only number is the 5 per cent threshold. **Wanted:** several chains converging on one factory. From
the left: wheat (farm, trader, flour mill), sugar crop (farm, sugar mill), oil palm (plantation, oil
mill, refinery; "which country?"), milk (dairy farm, dairy plant), salt, and a greyed "Choco chips
(under 5 per cent: own chains not declared)". All feed one box, "factory: processing, packaging,
brand", then one chain out (distribution, retail, household). A dashed line at the factory door
labelled "what the label can see".

## C04 · Where the consumer's rupee goes (quantitative)

- `s37-r1-c04-gram-tur-rupee.png` (kept): Rs per kg added per stage; checks `sum(y1) = 71`,
  `sum(y2) = 111`.
- `s37-r1-c04-farmer-share.png` (kept): nine farmer's shares, 30.8 to 75.2 per cent.
- `s37-r1-c04-markup-base.png` (new, the worked relationship): for tur at Rs 111, a mark-up of x
  rupees as per cent of the shop price, `y = 100*x/111`, and on the buying price,
  `y = 100*x/(111 - x)`, over x from 1 to 39; points at x = 16 of 14.4 and 16.8. Each curve is tied
  to its series, so the checker confirms it passes through the plotted point (1600/111 = 14.41,
  1600/95 = 16.84). Reference line at Rs 16.

## C05 · Who decides: figure_note replaced by a figure

- `s37-r1-c05-onion-rupee.png` (new): bars of the RBI paper's Delhi onion rupee split, farmers 36.2,
  traders 17.6, wholesalers 15.0, retailer 31.3 (all stated in the illustration). Check
  `sum(y) = 100.1`, with 100.1 under `derived` (36.2 + 17.6 + 15.0 + 31.3); the caption says the four
  add to 100.1 as printed.
- The `figure_note` was removed because the section now has a figure. **Diagram still wanted:** the
  chain stages (farmer, contracting processor or pre-harvest contractor, trader, mandi with APMC fee
  and commission, wholesaler, processor with brand, retailer) with arrows into one "food
  environment" box of four cells (what is there and how near; what it costs; how it is promoted;
  what quality), each cell with arrows from the actors that set it; a person outside the box and a
  leaflet arrow reaching only the person.

## C06 · Where a country's food comes from (quantitative)

- `s37-r1-c06-pulses-identity.png` (kept): 22801 + 1733 - 615 = 23919; check holds.
- `s37-r1-c06-self-sufficiency.png` (kept, checks added): cereals 111.1 and edible oil 43.75 against
  a reference line at 100. New checks recompute each bar from its formula:
  `y[0] = round(100*303628/(303628 - 30352), 1)` and `y[1] = round(100*12.18/(12.18 + 15.66), 2)`.
- `s37-r1-c06-rice-row-gap.png` (new): rice 2022-23 availability by the identity 110553 against the
  printed 115120. Checks `y[0] = 125438 - 22347 + 7462` and `y[1] - y[0] = 4567`.

## C07 · What Indians eat and spend on food (quantitative)

- `s37-r1-c07-rural-shares.png` (kept): cereals against beverages and processed food shares, three
  surveys.
- `s37-r1-c07-cereal-rupees.png` (new): rural cereal spending Rs 153.7 (2011-12) against Rs 185
  (2022-23). Checks `y[0] = round(1430*10.75/100, 1)` and `y[1] - y[0] = 31.3`. The caption says the
  figures are nominal rupees, not grain.
- `s37-r1-c07-rural-energy.png` (new): rural energy intake 2,233 (2011-12) against 2,212 (2023-24)
  kcal, bars from zero, so the reader sees that intake hardly moved. No relation drawn.

## C08 · Built against hunger

- `s37-r1-c08-net-imports.png` (kept): negative bars for rice, wheat and other cereals, and pulses
  positive; check that the three cereals sum to -30352.

## C09 · MSP and procurement

- `s37-r1-c09-kharif-procurement.png` (kept): paddy 8418 against the other 13 crops 328; check sums
  to 8746.
- `s37-r1-c09-msp-floor.png` (kept, checks added): `y1[0] = 1.5*1627`, `y1[1] = 1.5*1239`, beside
  the existing `y2[1] - y1[1] = 726.5`.
- `s37-r1-c09-msp-cost-line.png` (new, the rule as a line): scatter of MSP against cost for paddy
  (1627, 2441), wheat (1239, 2585), gram (3699, 5875) and safflower (4360, 6540), with the curve
  `y = 1.5*x` from 1239 to 4360. Checks recompute the rabi table's margins 109, 59 and 50 from
  MSP and cost. Paddy and safflower sit on the line, gram above it, wheat far above. Gram and
  safflower come from the interpretation exercise's table, which is reader-facing text. Paddy
  is kharif and the other three are rabi; the caption says so.

## Caveats

- C04 markup-base: the curves run to x = 39. That is the chain's whole post-farm addition, used
  only as an axis end, and no label on the figure uses it.
- C09 msp-cost-line: the margin checks are written against constants, not tied to the plotted `y`,
  because the source rounds each margin to a whole per cent. The points themselves are the stated
  MSP and cost figures.
- No figure in the range could not be made correct.
