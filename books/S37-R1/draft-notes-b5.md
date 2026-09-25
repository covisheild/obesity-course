# Draft notes · S37-R1 · batch b5 (C13, C14, C15)

Drafted 2026-09-24 (stopped during self-check), finished 2026-09-25 under `FINISH-BRIEF.md`.
Not committed.

## Records written

- `check/records/S37/S37-R1-C13.yml`: What a ration, a meal or a take-home ration provides
  (derivable, quantitative). NFSA 2013 s. 3(1), s. 2(5), Schedule II; PIB 1812421 (PM POSHAN norms
  table); IFCT 2017 (rows A015, A014, A020, B021, A003; 3.6; Table 4); ICMR-NIN 2020 brief Table 1b;
  DFPD Annual Report 2025-26 para 4.1; Poshan 2.0 guidelines 2022 (3.2.1, 3.3, 3.6, 3.7); PIB
  2251769; OpenStax Chemistry 2e §5.3 as the textbook anchor for chained unit conversion.
- `check/records/S37/S37-R1-C14.yml`: The state as a food provider (empirical). DFPD Annual Report
  2025-26 (2.6, 2.8, 3.35 table, 3.39); PIB 1980689, 1812421, 2082323, 2251769; Poshan 2.0
  guidelines 2022.
- `check/records/S37/S37-R1-C15.yml`: The double burden, and double-duty action (empirical).
  NFHS-5 India fact sheet (indicators 81-89, 92, 93, 95, 97); WHO double-duty brief 2017; Swinburn
  2019; Poshan 2.0 guidelines 2022; PIB 2251769.

`python check/build.py --check`: blocking 0, no warnings for these three. `draw.py --book S37-R1`
draws all three figures; each PNG looked at and its values recomputed.

## What finishing changed

- **C15, Hawkes et al. 2020 removed.** The `hawkes_2020_double_duty` reference (opened: false)
  blocked an empirical record. It is gone, along with its mention in the review trigger and in an
  `analogy_breaks_when` ("the published source most likely to define them was not opened"), now
  "the WHO brief does not use them, and no other source quoted here does". C15 rests on WHO 2017,
  Swinburn 2019 and NFHS-5. "Single-duty" and "working against the other burden" stay defined as
  this book's own reading words. If Harsh later obtains Hawkes 2020, it can be added and the two
  terms checked against its wording.
- **C15, 4a:** the national 24.0 per cent (women overweight or obese) was applied to the women in
  a hypothetical State's anganwadi households; the sentence now says it is a national figure, gives
  the rural 19.7, and treats it as a warning, not a measurement. Same in exercise (a).
- **C15:** "a third of children stunted" (35.5) is now "more than a third" where stated as a
  fact; anaemia in women now separates all women (57.0) from non-pregnant (57.2), matching the
  cut-off given; the white-sugar rule used in exercise (a) now has its own reference.
- **C13:** practice problem 6 answer said the wheat meal falls "about 52 kcal short"; it is
  700 minus 649.1 = 50.9, now "about 51". Added an IFCT 3.6 quote for "worked out by the Atwater
  system", which had none.
- **C14:** international equivalents added at first use (crore, lakh, lakh tonnes); one 37-word
  sentence split.
- Withdrawn sources: none of the three records cites `eca_1955` or `food_corporations_act_1964`.

## Unsourced or caveated

- **C13, the 2023 PM POSHAN guidelines** are not held; PIB 1812421's norms table stands in.
  Cost sharing is not stated.
- **C13, THR norms** are NFSA Schedule II's (pre-January 2023); every THR sum says so. Revised
  figures are not held.
- **C13, vegetables** are left out of the school meal sum (no IFCT vegetable row used); the text
  says the total is short by that amount. Oil counted as pure fat, an upper bound, said.
- **C14, 595.05 vs 607.40:** the report's text and table disagree; the record quotes the table and
  says so. "Hostels, public hospitals and government canteens are the same lever" is a framing
  sentence routed to rung 2; only the hostel allocation (5.83) is sourced.
- **C14, 11.80 crore children** is a 2022 figure; no newer PM POSHAN count held.
- **C15, household- or individual-level double burden** is not shown by any held source; the
  record says a fact sheet cannot show it.
- **C15, Poshan Maah "retrofit"** reading is the book's; PIB reports intention, no effect.
- **C15, exercise proposals** are marked made up.
- `nfsa_2013` resolves to India Code (held from earlier books, not withdrawn); flag only if the
  India Code withdrawal is meant to cover it too.

## Practice-set sizes

- **C13: twelve.** The technique has six moves that compose (scale a per-100 g value, month to day,
  household to person, add a meal's parts, kJ to kcal with a stated factor, divide by a norm); each
  gets a problem, the direction reverses twice (norm to packet), and the set reaches levels 1 to 10
  (three mechanical, five applied, two diagnostic, two transfer).
- C14 and C15 are not quantitative (inventory: no).

## Figures

All three drawn by `draw.py` from specs, none wanted beyond them:

- `s37-r1-c13-school-meal-energy.png`: bars of the primary meal's kJ by food and total, reference
  line at the 1,881 kJ norm; `check` that the parts sum to the total.
- `s37-r1-c14-grain-allocation.png`: 2025-26 allocation by scheme, lakh tonnes.
- `s37-r1-c15-double-burden-bars.png`: six NFHS measures, NFHS-4 beside NFHS-5.

## Glossary rows

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| allocation (of foodgrains) | grain the Union sets aside for a scheme for a year; not grain lifted, and not grain eaten | `S37-R1-C14` |
| anaemia (NFHS cut-off) | haemoglobin below a set level: 11.0 g/dl in a child of 6 to 59 months, 12.0 in a non-pregnant woman, 13.0 in a man | `S37-R1-C15` |
| de novo (double-duty) | the WHO's third level: a new action designed for both burdens from the start | `S37-R1-C15` |
| do no harm (double-duty) | the WHO's first level: check that an existing action does not raise the risk of the other forms of malnutrition | `S37-R1-C15` |
| double burden of malnutrition | undernutrition together with overweight, obesity or diet-related noncommunicable disease, in one person, household or population (WHO) | `S37-R1-C15` |
| double-duty action | an intervention, programme or policy that can reduce both undernutrition and overweight or diet-related disease at once (WHO) | `S37-R1-C15` |
| entitlement (food) | a mass of food a person or household is owed, over a period, under a law or scheme | `S37-R1-C13` |
| fair price shop | the ration shop through which PDS grain is handed out | `S37-R1-C14` |
| food composition table | a table of what 100 g of each food holds; India's is the Indian Food Composition Tables 2017 | `S37-R1-C13` |
| Global Syndemic | the Lancet Commission's (2019) name for obesity, undernutrition and climate change as epidemics that occur together, interact and share drivers | `S37-R1-C15` |
| offtake (lifted) | grain actually taken from the central pool for a scheme, as against grain allocated | `S37-R1-C14` |
| retrofit (double-duty) | the WHO's second level: change an existing action so it also acts on the other burden | `S37-R1-C15` |
| single-duty change | this book's word: a change that acts on one burden and neither aims at nor checks the other | `S37-R1-C15` |
| stunted | height-for-age more than two standard deviations below the WHO growth standard | `S37-R1-C15` |
| take-home ration (THR) | packaged food given at an anganwadi to take home, not raw grain | `S37-R1-C13` |
| underweight (child) | weight-for-age more than two standard deviations below the WHO standard | `S37-R1-C15` |
| wasted | weight-for-height more than two standard deviations below the WHO standard | `S37-R1-C15` |
| working against the other burden | this book's word: a change that acts on one burden and raises the risk of the other | `S37-R1-C15` |
