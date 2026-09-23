# Draft notes · batch opus-c07 · S01-R1

Drafter: Opus, blind side of the drafter comparison. No other draft of C07 and no other
`draft-notes-*` file was read.

## Records written

- `check/records/S01/S01-R1-C07.yml` — Sizing an imbalance, and the static rule. Derivable,
  quantitative, 12 practice problems, one illustration, 8 must-know points, 3 exercises
  (retrieval, critique, teaching to a first-year resident), 4 retrieval items.

## Build state

`python check/build.py --check`: C07 has four blocking lines, all "concept_deps references missing
record" for S01-R1-C02, C03, C04 and C05. Those records are being drafted elsewhere and are not in
this worktree; the lines clear on merge. Nothing else blocks. Remaining C07 warnings: three long
sentences that are verbatim quotations (Hall 2011 twice, the 30 kJ sentence), practice 4 prompt at
reading grade 9.1 (three proper names), and the NIST pound factor flagged as `derived` (the footnote
prints 4.535 923 7 E-01, which the number reader cannot parse as 0.45359237).

Every working line in the record, diagnostic prompts included, was recomputed in Python; all hold.
Every blockquote in the illustration and practice answers was found verbatim in its source file,
except the two claims the prompts say are made up (practice 9, practice 10).

## Unsourced, or deliberately not asserted

- **The energy in a kilogram of adipose tissue, or of lost weight, is not stated.** That is C02's
  figure and rests on Hall 2008 (not held). The record uses only the rule's own figure (3,500 kcal a
  pound, which is 7,716.18 kcal/kg, 32.28 MJ/kg) and FAO's Atwater 9.0 kcal/g for fat in food as a
  comparison (9,000 kcal/kg). It says the rule's kilogram is about 86 per cent of the latter and
  sends "why" to C02. Hall 2011's 39.5 MJ per kg of body fat is held but was left to C02.
- **The OpenStax A&P 2e §24.7 paragraph** is quoted in the illustration as the specimen whose
  straight line fails. It is not in the references and no figure is taken from it; the 200 kcal is
  called the book's own example. The reader is given the page URL to open.
- **The ICMR-NIN 2020 requirements** (2,110 and 1,660 kcal/d, sedentary, from the Brief Note Table
  1b; 2,710 and 3,470 in practice 5) are called adopted requirements, not measured expenditure,
  every time. They are institutional; the record's review clock stays `long` because the concept
  is derivable, but those figures will move at the next ICMR-NIN revision.
- **Hall 2011's 100 kg man, 75 kg plateau and rule-of-thumb** are model output and are called that.
  The rule of thumb (100 kJ/d per kg, 10 kcal/d per lb) is used once, in practice 9, as the contrast
  to the static rule, not taught; computing the curve is left to rung 2.
- **Thomas 2013:** the 7.4 lb shortfall is a mean of individual differences, not 27.6 minus 20.1;
  practice 6 also explains why 1,439 × 64.8 / 3,500 gives 26.6, not the paper's 27.6.
- **Hall 2012** (not held) is not cited; Hall and Guo 2017 carries "expenditure considered
  constant" for the static model.

## Why twelve practice problems

The technique has four moves (summing a daily flow; converting the rule's per-pound figure;
dividing energy by energy-per-mass, in both directions; putting a kilogram against days of
requirement), and the diagnostic band needs both kinds of break this concept produces (a unit slip,
twice: pound-for-kilogram and kJ-for-kcal; and a premise slip: the straight line), so twelve.

## Figures wanted

1. Weight against time, 0–10 years, for Hall 2011's 100 kg man, 480 kcal/d cut: the static rule's
   straight line (22.7 kg/yr, reaching 0 kg before year 5 and 227 kg lost at year 10, drawn through
   a shaded "no body" region below 0) against a curve falling to about 75 kg, half the loss in about
   one year, 95 per cent in about three. Label the curve "model with expenditure falling" and cite
   Hall 2011 for the 75 kg, 1 yr and 3 yr points only; do not draw a curve shape the paper does not
   give beyond those.
2. A bar pair: Thomas 2013, 27.6 lb predicted against 20.1 lb lost (mean, n = 103, 31–93 days),
   with the ±11.3 lb spread on the observed bar.

## Glossary rows

Checked against `prose/GLOSSARY.md`: none of these is glossed there. If C05 or C02 glosses
"energy imbalance" or "megajoule" first, their wording wins and C07 follows it.

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| 3,500 kcal per pound rule | the rule that every pound of weight change is 3,500 kilocalories, which is about 7,700 kilocalories a kilogram | `S01-R1-C07` |
| energy imbalance | energy intake minus energy expenditure, per day: the daily gap between what comes in and what goes out | `S01-R1-C07` (defer to `S01-R1-C05` if it glosses it) |
| pound | an older unit of mass, exactly 0.45359237 of a kilogram | `S01-R1-C07` |
| static rule | the 3,500 kcal per pound rule used to draw a straight line into the future, holding everything still except the one number changed | `S01-R1-C07` |
