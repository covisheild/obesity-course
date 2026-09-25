# Draft notes · S37-R1 · batch b6 (C16, C17, C18)

Drafted 2026-09-24 by an earlier b6 drafter (stopped during its self-check). Finished 2026-09-25
under `FINISH-BRIEF.md`. Not committed.

## Records written

- `check/records/S37/S37-R1-C16.yml`: The main Indian food policy tools, on one map (institutional).
  PIB MSP backgrounder, PIB 2260617, 2061646, 2200287, 2082323, 1847548, 2251769, 1812421, the
  millets backgrounder, the edible oil duty releases, DFPD Annual Report 2025-26, the DFPD year-end
  review, FSS Act 2006, NFSA 2013, the labelling regulations, the Constitution (Art. 279A).
- `check/records/S37/S37-R1-C17.yml`: Locating an intervention in the food system (derivable).
  OpenStax anchor; HLPE 2017, WCRF NOURISHING, Poshan 2.0 guidelines 2022, PIB releases.
- `check/records/S37/S37-R1-C18.yml`: Sketching the supply chain of a packaged product (derivable;
  the rung's build). Labelling regulations 2020, MSP backgrounder, sugarcane FRP, duty release,
  PIB 2200287.

`python check/build.py --check`: blocking 0 (whole corpus, 88 records). One warning of mine: C18's
365 is `derived` because the build's number reader does not split "Rs.365".

## What finishing changed

- **Withdrawn sources removed.** `food_corporations_act_1964` (C16) and `eca_1955` (C16 twice,
  C16 must-know, C18) are gone.
  - C16 storage row now rests on DFPD Annual Report 2025-26 (FCI set up 1965 "under the Food
    Corporation Act, 1964"; para 3.64 "main instrument ... buffer stock"; para 4.3). The Act is named
    only as "an Act of 1964"; no section is stated.
  - C16's Essential Commodities Act row is replaced by the 2025 wheat stock limits (DFPD year-end
    review, which names no Act). The Act now appears only through NFSA s.2(4) and s.29(1) (the PDS
    (Control) Order 2001), with a sentence saying its own text is not held. The must-know trap was
    rewritten: do not name the Act behind a stock limit from memory. The purpose-sort row for the
    Act became "Procurement and the buffer stock" (DFPD's objectives of food management).
  - C18's sugar row lost "Essential Commodities Act powers over sugar"; it now names the CCEA's
    FRP approval (`pib_sugarcane_frp`).
- C17: the NOURISHING area for front-of-pack warnings now names which of the two N areas; the
  school-nutrition-gardens claim now has a quote (PIB 2082323); PM POSHAN expanded at first use.
- C18: wheat row states "rabi marketing season 2026-27".

## Unsourced or caveated

- **Essential Commodities Act and stock limits** (inventory's C16 row asks for "storage and stock
  limits (Essential Commodities Act)"): no held text links the two. The record says so. If Harsh
  downloads the Act by hand, the ECA row and C18's sugar powers can come back.
- **Food Corporations Act title**: DFPD writes "Food Corporation Act"; the record avoids the title.
- **C16 figure, 2024 bar**: the 3 Oct 2024 release says "20% import duty on edible oils", not
  "basic customs duty"; the June 2025 release confirms BCD was 20% before its cut. The figure's axis
  says basic customs duty. Auditor to judge; the table header says "as stated".
- **Continuation of PM POSHAN and Poshan 2.0 after March 2026**: not held; C16 says so.
- **C18 biscuit ingredient list** is made up and says so.

## Practice sets

None. C16 to C18 are not quantitative in the inventory (`quantitative: false`).

## Figures

- **C16**: `s37-r1-c16-oil-duty-bars.png`, grouped bars from the illustration's duty table
  (block 0). Redrawn with `draw.py --book S37-R1` into scratch; spec passes, PNG looked at, values
  match the table (20/20, 10/10, 5/0).
- **C17, wanted, not drawable** (figure_note): a chain of stage boxes (production, storage,
  processing, distribution, retail, preparation, consumption) with each proposal from the two
  tables pinned to its stage, coloured upstream vs on the person: duty cut (trade and distribution,
  two pins), PM POSHAN local procurement (purchase for meals), millet incentive (processing),
  jaggery rule (preparation), Poshan Maah theme, oilseeds IEC campaign, counselling (consumption,
  on the person). No numbers.
- **C18, wanted, not drawable** (figure_note): the biscuit sketch as a flow, wheat, sugarcane,
  oil palm, milk, salt into "factory (brand owner seen; maker unknown)", then distributor
  (unknown), kirana (seen). Each link carries its mark (checked / seen / unknown); policy tools
  hang off each crop (wheat MSP Rs 2,585/qtl RMS 2026-27; FRP Rs 365/qtl SS 2026-27; crude palm
  oil BCD 5% from 24 Sep 2026).

## Glossary rows

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| effective customs duty | what a text calls the whole duty on an import, as against the basic customs duty alone | `S37-R1-C16` |
| food policy tool | any means by which a government changes what is grown, stored, traded, processed, sold, served or eaten; *instrument* is kept for the legal text a tool stands on | `S37-R1-C16` |
| locate (an intervention) | name its stage, whose decision it changes, and what it moves in the food environment | `S37-R1-C17` |
| on the person (acting) | changing only the eater's own decision, with the food on offer left as it was | `S37-R1-C17` |
| stock limit | a cap on how much of a food a trader, retailer or processor may hold | `S37-R1-C16` |
| supply-chain sketch | a written map of one packaged product, from crops to shop, each link marked checked, seen or unknown | `S37-R1-C18` |
| upstream (acting) | changing a decision taken before the person chooses: a crop, a recipe, a price, a shelf, a ration | `S37-R1-C17` |

`brand owner` and `class title` are C03's rows (draft-notes-b1), and `buffer stock` is taught in C08; used in those senses.
