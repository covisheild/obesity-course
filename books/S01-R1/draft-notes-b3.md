# Draft notes · batch b3 (S01-R1-C07, S01-R1-C08)

## Records written

- `check/records/S01/S01-R1-C07.yml` — Sizing an imbalance, and the static rule. `python
  check/build.py --check` gives zero blocking and zero warnings for this record.
- `check/records/S01/S01-R1-C08.yml` — Spotting a claim that breaks conservation. Same, zero
  blocking and zero warnings.

## Sourcing decisions

- **C02's adipose-tissue figure is not used anywhere.** Per the brief, the 7,716 kcal/kg
  figure in both records is arithmetic on the static rule's own 3,500 kcal/lb (Thomas 2013),
  converted with NIST's exact pound factor — not a claim about what adipose tissue holds.
  Both records say so explicitly and point the reader to C02 for that separate question.
- **Hall 2008 is not cited.** C07 uses Hall 2011's own line on the rule's origin
  ("derived by estimation of the energy content of weight lost") instead of Hall 2008
  directly. C08's glycogen-and-water point uses Hall 2011's Panel paragraph, per the brief.
- **C08's specimen is the FTC Gut Check page**, Claim 1's own wording ("Lose up to 2 pounds a
  day without diet or exercise"). Both the definition note and the illustration state
  plainly that this is the regulator's own illustrative example, never a real advertisement.
- OpenStax A&P §24.7 is cited in C07 only to show the rule is commonly taught in that form
  (matching Thomas 2013's own observation), and only in that role — the do-not-cite mark on
  its figure is respected; it is never the source for a number treated as true, and it is
  used as the deliberately-wrong specimen in one diagnostic practice problem.
- Every citekey used (`thomas_2013_3500kcal`, `hall_2011_lancet`, `nist_sp811_pound`,
  `nist_sp811`, `openstax_anatphys_2e`, `ftc_gut_check_2014`, `openstax_college_physics_2e`)
  is already `opened: true` in `sources/INDEX.yml`; nothing here is `opened: false`.

## Practice set sizes

- **C07: eight problems** (levels 1, 2, 4, 5, 7, 8, 9, 10). The technique has one core move —
  multiply or divide by the rule's own rate — so it reaches all four bands without padding:
  two mechanical, two applied against real published scenarios (Thomas 2013's cohort, Hall
  2011's 100 kg man), two diagnostics (a linear-forever extrapolation off the OpenStax
  specimen, and a kg/lb unit swap), two transfers.
- **C08: eight problems** (levels 1, 2, 4, 5, 7, 8, 9, 10). The technique has two moves —
  convert a claimed change to kcal, then bound it against a real deficit or flag the
  glycogen-water exception — so eight problems cover both moves at every band, including one
  diagnostic each for the "conservation therefore true" fallacy and for running the fat rate
  on an early-loss, glycogen-heavy figure.

## Figures wanted, not drawn

- A plotted comparison of the static rule's straight line against Hall 2011's dynamic-model
  curve for the 100 kg man over 10 years (their Figure 2A) would strengthen C07's "trap"
  point beyond the one-year table given here.
- A simple boundary diagram (person, arrows in and out, one arrow crossed out for the FTC
  claim) would help C08's illustration; described in words only, per the brief.

## Glossary rows

None proposed. Both records reuse terms already established in Book 0 (`boundary`,
`crossing`, `deficit`, `conservation`) via `ground_floor_deps`, and coin nothing new.

## Unsourced / left open

Nothing in either record rests on an unopened source. The only content deliberately left
out, per the brief, is any adipose-tissue-specific energy figure (C02's job) and any claim
citing Hall 2008 or Hall 2012 directly.
