# Draft notes · Book 0 Part D, D1–D3 (concepts C24–C26)

Written by the Sonnet chat that drafted `B0-R0-C24.yml`, `B0-R0-C25.yml` and `B0-R0-C26.yml`
against `books/B0/INVENTORY-part-D.md` and `books/B0/READY-part-D.md`. D4–D7 are being drafted in
parallel by another chat; this note only speaks to D1–D3. Build run against all records currently
present: 0 blocking lines name C24, C25 or C26 (two blocking lines belong to C29/C30, the parallel
batch's files, and are untouched here).

## Drill-set counts, and why

| Concept | Count | Inventory's expectation | Why this count |
| --- | --- | --- | --- |
| C24 (D1) | 9 | 8–10 | One counting-and-complement move, plus the odds conversion drilled in both directions. The counting move needs little repetition; the odds trap needed two mechanical, two applied (rural, then urban for contrast), two diagnostic (one per direction of the conversion) and one transfer. Landed at 9 rather than 10 because a tenth mechanical or applied problem would have repeated a move already covered without adding a new failure mode. |
| C25 (D2) | 13 | 12–14 | Three moves that compose: list-and-count (powers of two), multiply-for-independent, add-for-mutually-exclusive, plus the complement shortcut for "at least one". Five mechanical problems were needed to give each move its own bare-number drill; three applied (different households, same household, "at least one of three") carry the real NFSA case; three diagnostic because two *distinct* wrong moves needed separate problems (adding instead of multiplying; multiplying non-independent draws), plus a third showing an impossible-probability giveaway; two transfer. |
| C26 (D3) | 15 | 14–16 | The flagship section: build the table, condition, reverse, name four ratios, move the prevalence. Four mechanical problems on an invented table cover build/condition/reverse/naming before any real data appears. Five applied problems carry the real Kiran rebuild, its two predictive values, and the rounding-recovery check. Three diagnostic problems use the paper's own three real internal inconsistencies (see below) — each is a different *kind* of resolution (recomputation settles it; recomputation can't; the paper's own printed check settles it), so none could be dropped without losing a distinct lesson. Three transfer problems carry the prevalence move twice (real 20%, then a hypothetical 10% to show the trend continuing) plus a closing words-claim critique. |

All three reach every band (mechanical, applied, diagnostic, transfer) per `check/_build/check_report.md`'s practice-sets table.

## New glossary terms introduced

Per `claude.md` §7 note 7: `prose/GLOSSARY.md` was not written to. These go to the main thread for
reconciliation against `prose/glossary-inbox-D.md` and the parallel D4–D7 batch.

| Term | Plain words at first use | Concept |
| --- | --- | --- |
| sample space | "the complete list of everything that could happen" | B0-R0-C24 |
| outcome | "one member of that list" | B0-R0-C24 |
| event | "any collection of outcomes" | B0-R0-C24 |
| complement | "every outcome in the sample space that is not in it" | B0-R0-C24 |
| odds | "how many times more likely an event is than its opposite, not how likely it is" | B0-R0-C24 |
| independent (events) | "knowing that one has happened tells you nothing about the chance of the other" | B0-R0-C25 |
| mutually exclusive | "the two events... cannot both happen" | B0-R0-C25 |
| two-way table | "sorts one group of people by two categories at once, one down the rows and one across the columns" | B0-R0-C26 |
| cell | "the count where a row meets a column" | B0-R0-C26 |
| row total / column total / grand total | "found by adding the counts inside them" | B0-R0-C26 |
| conditional probability | "restricts which total a count is divided by" | B0-R0-C26 |
| sensitivity | "the share of the truly-affected the test catches" | B0-R0-C26 |
| specificity | "the share of the truly-unaffected the test correctly clears" | B0-R0-C26 |
| positive predictive value | "the share of positive results that are right" | B0-R0-C26 |
| prevalence | "how many people in a group have it" — reused unchanged from `check/prose/hardwords.yml`'s `teach_once` entry | B0-R0-C26 |
| Youden's index | "sensitivity plus specificity, minus one... also useful as a check" | B0-R0-C26 |

`prevalence` is not new to the corpus — it already sat in `check/prose/hardwords.yml`'s
`teach_once` list with this exact gloss, unused until now. I used the recorded words unchanged.

**Flag for the main thread:** `Youden's index` is not in the inventory's list of screening
vocabulary (sensitivity, specificity, PPV, prevalence). I introduced it because it is the only way
to resolve one of the three real diagnostic problems the course owner asked for (the neck-
circumference specificity conflict, 82% in running text against 71% in Table 3) using only what the
paper itself prints — no external formula, no invented check. If the main thread judges this out of
scope for D3, the fix is to drop that one diagnostic problem (practice level 8) and replace it with
a plain "you cannot resolve this without the raw counts" problem, which is a smaller lesson but
keeps the vocabulary list exactly as scoped.

## Figure proposals

None added to any of the three records. Per the inventory, D3 explicitly needs no figure ("the
table *is* the picture"), and D1/D2 are not on its figure candidate list.

One candidate the main thread may want to consider for **D1**: a curve of probability against odds
(p from 0 to 1 on one axis, p/(1-p) on the other) would show the divergence near p=1 that the
prose currently states in words (0.5→1, 0.75→3, 0.9→9, 0.99→99, 0.999→999 — all computable from
the record as written). I did not add it because the prose illustration's own worked comparison
(rural 0.75 vs urban 0.5, giving odds of 3 vs 1) seems to carry the point without a picture, and a
curve here would mostly repeat what four lines of arithmetic already show. Numbers, if wanted:
p = 0.5, 0.6, 0.75, 0.9, 0.99, 0.999 against odds = 1, 1.5, 3, 9, 99, 999.

## Places I was unsure

1. **The MUAC rebuild's rounding choice.** 0.86 × 52 = 44.72 rounds to 45; 0.74 × 79 = 58.46 rounds
   to 58. I used ordinary nearest-integer rounding both times and cross-checked the pair against the
   paper's own printed Youden's index for that row (0.60 = 0.86 + 0.74 − 1, which matches). That
   cross-check confirms 86/74 are mutually consistent; it does not independently confirm 45/58 are
   the *unique* nearest-integer counts consistent with them — the record itself says so
   (`analogy_breaks_when`). Worth the audit step redoing this arithmetic independently, since the
   whole of D3's applied and diagnostic bands sit on this one rebuilt table.
2. **Whether reusing D1's NFSA ceiling (0.75) as an exact figure for D2's compounding is
   sound.** The Act's own word is "up to", so every probability computed from it is a bound. C04 and
   C05 both already compute with the ceiling as though it were exact while narrating the "at most"
   qualifier in every sentence; I followed that established convention rather than inventing a new
   one, but flag it because D2 compounds the ceiling three ways (×3 in the "at least one" problem),
   and a bound compounded three times is a much looser bound than the original, a point the record
   tries to make explicit in `analogy_breaks_when` but which is easy to read past.
3. **D2's real material spans two subsections of the Act.** The inventory attributes D2's real
   material to "NFSA s.3(1): coverage is decided per household." I used s.3(1)'s "every person
   belonging to priority households" clause for the household-unit argument, and reused s.3(2)'s
   75%/50% ceilings (D1's own citation) for the actual numbers to compound. I believe this is the
   intended reading — s.3(1) alone gives no probability to compute with — but flag the cross-
   reference for the audit to confirm rather than treat as a citation error.
4. **The invented "wrong formula" diagnostic in D1** (practice level 8: odds computed as
   p/(1+p) instead of p/(1-p)) is a constructed error, not a documented real one, in the same way
   the diagnostic-band problems in C04/C05/C18/C21 are constructed. I want to flag this explicitly
   given how much of D3's diagnostic band uses *real* documented errors instead — the contrast in
   kind between D1/D2's constructed diagnostics and D3's real ones is intentional (D1/D2 have no
   real published error to draw on; D3's source does), but worth the audit noting so it isn't read
   as an inconsistency.
5. **D3 level-9's second prevalence (10%) is explicitly invented**, reusing only the study's real
   sensitivity and specificity. The record says so in the prompt and again in the answer. I believe
   this satisfies "real figures or none" (the *test performance* is real; the *scenario prevalence*
   is a labelled hypothetical extending a pattern already shown once for real, mirroring how C05's
   level 10 and C21's level 9 both label invented scenario numbers as invented). Flag for audit
   confirmation since this is the least standard move in the three records.
6. **D2's level-10 problem is the most conceptually demanding item across all three sets** — it
   requires recognising that "at least one of four household members not covered" collapses to a
   single household-level event rather than four independent draws, which is the whole point of the
   section but is easy to get subtly wrong even while writing it. I checked it twice; a third check
   by the audit step would be worth the time given how load-bearing that reasoning is for the
   section's central lesson.

## Things I think the inventory should double-check, or got right

- The inventory's own rebuilt table (arm 31.3 cm or more: 45/21/66; under: 7/58/65; totals
  52/79/131) was independently re-derived here from Table 2 and Table 3 and matches exactly. No
  correction needed — flagging only as a positive confirmation, since this is the number the whole
  section stands on.
- The inventory's PPV figures (68% at the study's own prevalence, 45% at 20%) were also
  independently recomputed and match (45/66 = 0.6818, 172/380 = 0.4526).
- One place the inventory is silent and I made a choice: it does not say whether D1 should use the
  urban 50% ceiling as well as the rural 75% one. I used both, because the odds-diverge-near-the-
  ends teaching point needs a second data point for contrast, and the Act gives one for free. This
  is a genuine addition beyond the inventory's stated minimum for D1, not a correction of an error
  in it.
- Nothing else in the inventory's D1–D3 sections struck me as wrong. The bridge-ref table, the
  sequence trap note (D3 must not lean on F1), and the "never say what arm circumference is good
  for" instruction were all followed as written and checked against the build (no forward
  references, no claims about what the measurement screens for well).

## Build status

`python3 check/build.py --check` at the time of writing: 0 blocking lines name C24, C25 or C26.
Two blocking lines exist for C29 and C30 (a `must_know` kind of `teaching`, which is not in the
schema's enum) — these belong to the parallel D4–D7 batch and were left untouched per instruction.
Reading-grade and long-sentence warnings on C24–C26 were reduced from an initial worst case of 15.3
down to a worst case of 11.8, in line with the rest of the corpus; remaining warnings are the kind
the style sheet treats as a ceiling rather than a target, and none flagged a hard-word replacement.
