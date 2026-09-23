# Draft notes · Book 0 Part D, D6–D7 (concepts C29–C30)

Written by the chat that drafted `B0-R0-C29.yml` (D6, *Sampling: how a part can tell you about a
whole*) and `B0-R0-C30.yml` (D7, *Random error and systematic error as different things*) against
`books/B0/INVENTORY-part-D.md` and `books/B0/READY-part-D.md`. D1–D5 were drafted in parallel by
other chats and had already landed in `check/records/B0/` by the time this batch ran its checks.

Build run against all 34 records currently present: `python3 check/build.py --check` reports
**0 blocking** and **0 warnings** naming C29 or C30 (34 records, 9 clusters, 156 warnings total
across the whole corpus before this pass, 110 after — all of the reduction is from these two
files; every remaining warning line names a different concept from a different batch).

## Drill-set counts, and why

| Concept | Count | Inventory's expectation | Why this count |
| --- | --- | --- | --- |
| C29 (D6) | 10 | 10–12 | One formula (spread of sample average = population spread ÷ √n) taught forward and backward, applied once to a bare population and once to Kiran's real body-mass-index spread, at both 1× and 4× sample size. That is a narrow technique, so mechanical and applied close in six problems (three mechanical passes on the formula in both directions, three applied passes anchored to real numbers). The weight of the section is in two distinct diagnostic failures — mistaking "double the sample" for "double the sample halves the spread" (a pure arithmetic slip), and correctly applying the law to a gap it was never built to close (a scope slip, not an arithmetic one) — and two transfer problems that force the reader to tell a real sampling-variation gap from a real bias gap using the study's own 34.8%-vs-20% figures and a generic "2,000 people can't tell us anything" claim. Ten problems land both failure modes without repeating a move. |
| C30 (D7) | 10 | 10–12 | The technique composes more moves than D6: compute a single error, average several errors to read off bias, take their range to read off scatter, then keep resolution, precision and accuracy conceptually apart. That composition earns a slightly richer mechanical/applied band (six problems: bare-number error, a same-sign-vs-crossing-zero comparison that previews systematic-vs-random by eye, then three applied problems on stated or real instruments). It only needs two diagnostic problems (averaging does not fix a zero error; a stated "accuracy" figure is really a resolution figure, using Kiran's own sentence) and two transfer problems (an extra decimal place is not evidence of accuracy; a single observer removes between-observer variation but not that observer's own habit, again using Kiran's own strength claim) to land its two failure modes. |

Both reach every band (mechanical, applied, diagnostic, transfer) per
`check/_build/check_report.md`'s practice-sets table. Ten sits at the bottom of the inventory's
stated 10–12 "expectation to test, not a target" for both; I did not find a third failure mode in
either section that would have justified an eleventh or twelfth problem without repeating a move
already drilled.

## How the VIM (jcgm_vim3) citation was handled

D7's core vocabulary — error, systematic error, measurement bias, random error, accuracy,
trueness, precision, resolution, zero error — comes from the International Vocabulary of
Metrology (VIM3), not from the OpenStax anchor. The build requires a `derivable` concept's
`definition.references[].kind` to be `textbook` only, and VIM's own `library.bib` entry is kind
`instrument`, so VIM cannot appear in `B0-R0-C30.yml`'s `definition.references` at all.

Handled as follows, matching the batch instruction:

- Every VIM definition actually taught to the reader is quoted **inline in prose** — in
  `definition.text`, `simplified_explanation` and `illustration.body` — naming "the VIM" and its
  entry number directly beside the quoted words (for example: `measurement bias (VIM 2.18)`).
- `definition.references` carries only the two OpenStax quotes that ground this as a
  `derivable` concept (the sampling-error / nonsampling-error distinction), with a `verified.note`
  on the first entry spelling out why VIM sits outside this list and where it is cited instead.
- The `jcgm_vim3` citekey is attached to `must_know[].refs` on four of the seven points and to
  `practice[].refs` on practice level 8 (the resolution-vs-accuracy diagnostic problem), which the
  build validates only against `library.bib` (citekey exists) and does not quote-check — exactly
  the mechanism the instruction pointed at.
- No VIM number appears in `illustration.numbers` because none of the VIM quotations used here are
  themselves numeric values; the one entry in `illustration.numbers` (100 g, the stated
  "accuracy"/actual resolution figure) is cited to `kiran_2022_muac_nc`, not VIM.

## New glossary terms introduced

Per the batch instruction, `prose/GLOSSARY.md` was read but not written to. These go to the main
thread for reconciliation.

| Term | Plain words at first use | Concept |
| --- | --- | --- |
| population | "the entire group a question is about" | B0-R0-C29 |
| sample | "the part of that group whose members are actually measured" | B0-R0-C29 |
| parameter | "a number that describes the population, if every member of it could be measured" | B0-R0-C29 |
| statistic | "the same kind of number, computed instead from a sample" | B0-R0-C29 |
| estimate | "your best guess at it... built from evidence rather than pulled from nowhere" | B0-R0-C29 |
| random sample | "every member of the population has an equal chance of being chosen... decided by an actual chance process" | B0-R0-C29 |
| convenience sample | "built... out of whoever happens to be available" | B0-R0-C29 |
| sampling variation | "draw a second random sample of the same size... its statistic will not match the first sample's exactly... a property of sampling itself" | B0-R0-C29 |
| square-root law | "the spread of the sample average... equals the spread of the individual values in the population divided by the square root of the sample size" (named as a rule, not derived) | B0-R0-C29 |
| standard error of the mean | "papers name this spread" — used exactly once, built on nowhere else, per the course owner's instruction | B0-R0-C29 |
| error (measurement) | "the value it returns minus the value that is actually true" | B0-R0-C30 |
| systematic error | "the part of the error that... remains constant or varies in a predictable manner" | B0-R0-C30 |
| measurement bias | "an estimate of a systematic error" — flagged explicitly as the same shape of problem as sampling bias | B0-R0-C30 |
| random error | "the part that... varies in an unpredictable manner from one reading to the next" | B0-R0-C30 |
| measurement accuracy | "closeness of agreement between a measured quantity value and a true quantity value" | B0-R0-C30 |
| measurement trueness | "closeness of agreement between the average of an infinite number of replicate measured quantity values and a reference quantity value" | B0-R0-C30 |
| resolution | "the smallest step an instrument's display can move by" | B0-R0-C30 |
| zero error | "an instrument reading something other than zero when it should read zero" | B0-R0-C30 |

**Precision is not a new row.** `prose/GLOSSARY.md` already records `precision` at effective
first use `B0-R0-C03` ("how tightly a measurement pins the number down"). D7 reuses that exact
recorded wording, then sharpens it to the VIM sense (VIM 2.15, closeness of repeated readings to
each other, not to the truth). This is a resharpening, not a new introduction, and I have not
added or changed the glossary row.

## Figure proposals

Neither figure is added to either record's YAML; both records' prose already carries every number
a figure would need, so the numbers below are read out of the records, not invented for this note.

**D6 — sample averages from many samples of 10 vs many samples of 40, from one stated
population.** Population used throughout the record: `2, 4, 4, 4, 5, 5, 7, 9` (mean 5, population
spread 2, both computed by hand in the record's own working blocks). Three hand-drawn samples of 4
are shown individually in the record (`5,4,7,2` → 4.5; `4,4,5,2` → 3.75; `4,2,4,7` → 4.25). The
proposed figure is the record's own next step: draw 5,000 samples of size 10 and, separately, 5,000
samples of size 40, with replacement, from this same eight-number population (seed `110` for the
draw that produced the record's stated figures). The empirical spread of the 5,000 sample-of-10
means comes out at 0.633; the empirical spread of the 5,000 sample-of-40 means comes out at 0.317 —
both numbers already appear in `illustration.body`'s prose and its `0.633 divided by 2 = 0.3165`
working block. A histogram of the two sets of 5,000 means, drawn to the same horizontal scale, with
the n=10 histogram visibly wider than the n=40 histogram, would make the square-root law's
"halving" visible rather than only asserted. I did not draw this — no plotting tool was available —
but the exact seed, population and rep count are given here so the figure can be regenerated
deterministically.

**D7 — two stated scales, twenty readings each, against one true weight.** True weight: 60.0 kg.
Both full reading lists are already given verbatim in `illustration.body`'s two `table` fences and
are reused unchanged here:

```
Scale A (tight and shifted), seed 42:
60.5 60.5 60.5 60.5 60.5 60.4 60.5 60.5 60.5 60.5
60.5 60.6 60.5 60.5 60.5 60.4 60.5 60.6 60.5 60.5
mean 60.5, error +0.5 kg (systematic — a zero error)

Scale B (centred and wide), seed 99:
59.7 60.2 60.2 60.4 60.0 59.6 59.4 60.6 58.7 59.7
59.4 60.0 59.7 59.7 60.4 59.7 59.4 60.5 60.5 60.7
mean 59.925, error -0.075 kg (random — much smaller on average despite wider scatter)
```

The proposed figure is a single dot plot with both sets of twenty readings on the same horizontal
axis, a vertical line at the true 60.0 kg, and the two scales' means marked. Scale A's dots should
visibly cluster tightly but off the true-weight line; Scale B's dots should visibly scatter widely
but straddle it. This is the exact contrast the record's prose argues in words ("Scale A looks
better reading by reading... and it sits further from the truth on average than scale B ever
does"). I did not draw this for the same reason as above; the numbers are exact and reproducible
from the stated seeds.

## Places I was unsure

1. **Whether ten practice problems is enough, against the inventory's 10–12 "expectation to test,
   not a target."** Both records land at the floor of that range. I could not find a third
   diagnostic or transfer failure mode in either section that would not have repeated a move
   already drilled (see the drill-set table above for the reasoning I used to stop at ten). I would
   like the audit to check whether it agrees a third failure mode exists that I missed, particularly
   for D7, which has more component moves than D6.

2. **Whether the DEXA/BIA passage in D7's illustration stays clear of being read as evidence.**
   The record names DEXA as the paper's own stated gold standard and states plainly that
   bioimpedance was used instead, "without claiming any specific bias magnitude" since none is
   stated in the paper. I worded this as "nothing in the paper states how big any gap between the
   two methods actually is, so none is claimed here." I want the audit to confirm this reads as
   using the paper to teach the concept of an unstated method gap, not as a claim about bioimpedance
   itself, since that line is the closest either record comes to sounding like it is evaluating an
   instrument rather than illustrating a word.

3. **`provenance.bridge_ref: []` on both records, against the inventory's own bridge table.** The
   batch instruction was explicit and I followed it literally: both records carry an empty
   `bridge_ref` list, overriding what I read in the inventory's bridge-sufficiency table (which
   names S03 rung 1's confidence-interval material as resting on D6, and S08 rung 2's classical/
   Berkson error material as resting on D7). I do not know whether this is a deliberate decision to
   defer bridge-linking to a later pass, or an instruction that did not anticipate the inventory
   naming specific downstream dependents. I did not add either bridge reference, per the explicit
   instruction, but flag it here in case the empty list needs to be revisited once S03/S08 exist.

## Nothing in the inventory looks wrong to me

I did not find a place where the inventory's brief for D6 or D7 was mistaken. The one place I made
a judgement call beyond the letter of the brief is the exact split of Kiran's overweight/obese
figures used for D6's lead illustration (83 overweight + 15 obese = 98/282, 34.8%) — the inventory
names this comparison in general terms without specifying which of the paper's printed figures to
combine, and 83+15 is the only combination that reproduces a body-mass-index-≥25 count consistent
with the paper's own Table 2 bands, so I used it without alternative candidates to weigh.
