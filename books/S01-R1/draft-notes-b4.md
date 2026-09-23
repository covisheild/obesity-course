# Draft notes — batch b4

## Records written

- `check/records/S01/S01-R1-C09.yml` — Intake and expenditure are outputs of a regulated system
  (empirical, no practice/drill set — not quantitative per inventory). Sources: Rosenbaum & Leibel
  2010 (adaptive fall in expenditure, 20-25% after 10%+ loss, 10-15 points beyond body-composition
  prediction, ~300-400 kcal/day), Polidori 2016 (~100 kcal/day per kg lost, >3-fold the expenditure
  adaptation), Hall & Guo 2017 (intake/expenditure as interdependent variables; individual
  variation in the response). `concept_deps: [S01-R1-C04]` — C04 was not yet in `check/records/S01/`
  when I wrote this; if still missing at merge, the build will flag the forward dependency.
- `check/records/S01/S01-R1-C10.yml` — Arithmetically true, practically insufficient (derivable;
  the rung's build target and gate). Built as an argument (premise/inference/conclusion, per
  `B0-R0-C42`): the identity is true, the instruction smuggles in an unstated premise that
  expenditure and appetite hold still, C09 shows that premise false. Textbook anchor added
  (OpenStax Chemistry 2e §5.1, conservation of energy) because a derivable concept needs a
  `textbook` reference; Hall & Guo 2017 carries the "naive bookkeeping" / willpower claim and the
  correction. Carries the rung's `build` exercise (one-page write-up) and a `teaching` exercise for
  the health-secretary audience, matching the gate ("three minutes, no mechanism, no moral claim").

Both pass `python check/build.py --check` with zero blocking on these two files. Per Hall et al.
2012 not being held, I did not use it anywhere; Hall 2011 Lancet was read but did not carry a claim
these two concepts needed, so it is not cited here.

## Unsourced / cut

- The inventory's "add exercise and intake partly rises" clause for C09: no held source states
  that adding exercise specifically raises intake (Hall & Guo's physical-activity paragraph only
  says PA expenditure falls with weight loss unless compensated). I did not write this claim.
  Flagging for the audit/next pass in case a held source elsewhere covers it.

## Practice-set sizing

Neither concept is quantitative (inventory marks both "no"), matching both exemplars
(`B0-R0-C38`, `B0-R0-C42`), so no `practice[]` block on either.

## Figures wanted

None beyond the `illustration.numbers` already in C09 (expenditure and appetite effect sizes).

## Glossary rows (proposed; not already in `prose/GLOSSARY.md`)

| Term | Plain words | First taught in |
| --- | --- | --- |
| adaptive thermogenesis | the extra fall in expenditure after weight loss, beyond what the smaller body alone explains | `S01-R1-C09` |
| settling point | the body-weight model where expenditure, not intake, does the pushing back | `S01-R1-C09` |
| set point | the body-weight model where both intake and expenditure push back, intake harder | `S01-R1-C09` |
