# Draft notes · S58-R1 · batch b4 (C09, C10)

Drafter: Opus 5.5, Task 2, 2 Oct 2026. Brief: `books/S58-R1/DRAFT-BRIEF.md`.

## Records written

- `check/records/S58/S58-R1-C09.yml`: Numbers in a sentence: the unit, the count behind the
  percentage, and no more digits than the data hold. Derivable, quantitative, 13 practice problems,
  3 exercises (retrieval, critique with `skill_ref: S58-R1-K01`, teaching to a journalist), 8
  must-know points, `common_misreading` and `reporting_sentence`, one figure.
- `check/records/S58/S58-R1-C10.yml`: One idea per paragraph: the topic sentence, its support,
  and the reverse outline. Derivable, not quantitative, 4 exercises (retrieval, two critiques with
  `skill_ref: S58-R1-K01`, teaching to a first-year resident), 7 must-know points,
  `common_misreading`, one figure.

## Sources used (all held, all quotes checked as whitespace-normalised substrings of the files)

- C09: `cole_2015_too_many_digits` (textbook: Table 1 rows Mean, Percentage, p value; body text on
  significant digits, rule of four, intermediate precision, "recommendations not requirements", the
  OR 22.68 and HR 0.03 examples, the birth-weight example, the range rule for percentages);
  `lang_altman_2013_sampl` (guideline, off-type, held and quoted: numerators and denominators,
  mean (SD), P values to one or two decimal places, P <0.001 smallest; the 2013 EQUATOR PDF, not
  the 2015 journal version); `icmje_2026_manuscript_preparation` (guideline, off-type: IV.A.3.e,
  one sentence only, per ICMJE's request); `nfhs5_india_factsheet` (indicators 88-89 and the
  introduction's 724,115 women; footnote 21).
- C10: `openstax_writing_guide_handbook` (H2 Effective Paragraphs); `mensh_kording_2017_structuring_papers`
  (Rule 3 C-C-C at paragraph scale, Rule 4 zig-zag and parallelism, Rule 7 results paragraphs,
  Rule 9 outline).

## Anything unsourced, or the book's own

- **Reverse outline** is this book's name and procedure (C10 definition says "In this book"). No held
  source names it; it is Mensh and Kording's Rule 9 outline (one sentence per paragraph) made after
  the draft, and C04's "outline" (one sentence per planned paragraph) run backwards.
- **"Zig-zag" definition** is the book's reading of Mensh and Kording's Rule 4 paragraph; the paper
  uses the word only in the rule's heading (noted in the reference's `verified.note`).
- **The 100 ÷ n step** (C09) is derived arithmetic, not a source's rule. The record says it is the
  smallest move the count allows and not the uncertainty of the percentage.
- **Cole's "round up" for P values**: the record's examples all use values where rounding up and
  rounding to the nearest agree (0.38, 0.047, 0.0026, 0.67, 0.0086, 0.096); the illustration's
  `analogy_breaks_when` names the case where they part (0.032) and tells the reader to say which
  they did. Cole does not say which he means beyond the word "up".
- **SAMPL and 0.0026**: SAMPL's "one or two decimal places" cannot write 0.0026 as an equality;
  the record says so and does not invent what SAMPL would want there.
- **The SD rule vs the SE rule for a mean** giving different digits at large or small n is derived
  from Cole's Table 1 row ("either ... or"), shown with made-up output.

## Why 13 practice problems (C09)

Six moves compose in one reported number (significant figures, a percentage with its count, points
against per cent, the mean rule, the rule of four, the two P-value rules); each gets a mechanical or
applied pass, then two diagnostic and two transfer problems. Levels: 1, 2, 2, 3, 3, 4, 5, 6, 6, 7,
8, 9, 10. Real figures carry `refs` (NFHS-5, Cole, SAMPL); everything else is labelled made up.

## Figures

- `s58-r1-c09-one-person-step.png` (scatter + curve y = 100/x, ref line at 1 point): how far one
  person moves a percentage as n grows. Drawn, 0 problems; looked at.
- `s58-r1-c10-topic-changes.png` (step): the topic of each of 7 sentences before (6 changes) and
  after (2 changes) the rewrite, from the illustration's first table. Drawn, 0 problems; looked at.
  The y axis ticks at 0.5 steps; topics are whole numbers.
- **Wanted, not drawable with the tool:** for C10, a diagram of a page with a margin column (each
  paragraph boxed, its one-sentence note beside it), before and after; for C09, a paired bar of the
  NFHS women and men rows (NFHS-4, NFHS-5) with the change labelled in points and per cent. The
  second is drawable, but `draw.py` does not substitute `{{n:key}}`, so a figure whose numbers are
  only in `{{n:}}` form fails `draw.py`'s number check (the build substitutes first, `draw.py`
  does not). **Tooling note for the conductor:** any S58 figure plotting NFHS values needs either
  `draw.py` to call `reader_checks.apply_numbers`, or the numbers written literally somewhere in the
  record's reader text, which the brief forbids.

## numbers.yml keys added

None (the brief forbids editing). Keys used: `nfhs5_women_ow_ob_pct`, `nfhs4_women_ow_ob_pct`,
`nfhs5_men_ow_ob_pct`, `nfhs4_men_ow_ob_pct`, `nfhs5_women_ow_ob_urban_pct`,
`nfhs5_women_ow_ob_rural_pct`, `nfhs5_women_ow_ob_change_pp`, `nfhs5_men_ow_ob_change_pp`.

Numbers written literally that the reconciler may want in the registry:

| value | meaning | how obtained |
| --- | --- | --- |
| 724,115 | women NFHS-5 gathered information from (not the denominator of indicator 88) | `nfhs5_india_factsheet`, introduction: "gathered information from 636,699 households, 724,115 women, and 101,839 men" |
| 13.5 | urban minus rural women overweight or obese, NFHS-5, percentage points | 33.2 minus 19.7 (C09 practice L4, C10 illustration 2) |
| 0.165 (about 17%) | relative rise in women overweight or obese, NFHS-4 to NFHS-5 | 3.4 divided by 20.6 |
| 0.212 (about 21%) | relative rise for men | 4.0 divided by 18.9 |
| 5.1 | range of the four NFHS women/men, NFHS-4/5 figures (Cole's range rule) | 24.0 minus 18.9 |

## Notation rows needed

None new: the records use ÷, ±, ×-free prose, `^` exponents (kg/m^2) and ASCII `<`, all of which
are either in `check/notation.yml` or ignored by `check/notation.py`. If the PDF's symbol page should
list "<" (less than, as in P < 0.001), a row is wanted: `"<": {kind: sign, read: "less than",
meaning: "The left side is smaller than the right: P < 0.001"}`; the checker currently skips ASCII.

## Glossary rows

Checked `prose/GLOSSARY.md`: percentage point (`B0-R0-C04`), rounding and significant figures
(`B0-R0-C03`), numerator, denominator, odds, prevalence (`B0-R0-C26`) and argument are already there;
the records use those senses. The glossary's "precision" (`B0-R0-C30`: how closely repeated readings
agree) is a different sense from Cole's, so C09 avoids the bare word and uses "significant figures"
and "false precision" (Book 0 C03's phrase). New rows proposed:

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| false precision | a number carrying more digits than the data can support | `S58-R1-C09` |
| rule of four | round a risk ratio or odds ratio to two significant figures if its first non-zero digit is 4 or more, otherwise three | `S58-R1-C09` |
| confidence interval (CI) | a range, worked out from the data, that shows how precisely an estimate is known; how it is worked out is beyond this book | `S58-R1-C09` |
| P value | the number a statistical test prints beside a comparison; its meaning is beyond this book | `S58-R1-C09` |
| topic sentence | the sentence that states a paragraph's one point | `S58-R1-C10` |
| zig-zag (of a paragraph or draft) | leaving a topic and coming back to it later | `S58-R1-C10` |
| reverse outline | one sentence per paragraph, stating its one point, written from the finished draft and read alone | `S58-R1-C10` |

## Notes for others

- **C20 (words on a figure, error bars)** must use C09's gloss of confidence interval (CI) and not
  contradict it; C09 leaves the meaning of a CI and of a P value "beyond this book".
- **C21 (tables)**: C09 teaches Cole's digits rules (mean by SD or SE; percentages whole or one
  decimal under 10%; the range rule for comparing groups; rule of four). C21's "same decimal digits
  throughout" should say that Cole warns against fixed-decimal columns ("tables ought not to be
  restricted to columns of numbers with fixed decimal places") and recommends aligning on the
  decimal point; reconcile with ICMJE/Wilke there.
- **C23 (journey)** may reuse C09's `reporting_sentence` for the NFHS women row, and should keep
  one decimal place for the NFHS comparison (Cole's range rule, range 5.1) while not computing a
  count from 724,115.
- **C02 vs C04 vs C10, paragraph shape**: C02 says put the claim first; C04 says open a results
  paragraph with its question and end with the answer. C10 reconciles them: both are one-point
  shapes; pick one per section (Mensh and Kording's parallel form); for a hurried reader, point first.
  C02 and C04 should not call either shape wrong.
- **C04 defines "outline"**; C10's reverse outline is defined as C04's outline made after the draft.
  Keep C04's wording of "outline" stable.
- **C12 (cutting)** comes after C10: C10 cuts one empty closing sentence ("This shows that action is
  needed") without naming C12. C12 may use it as a case.
- **Wording on weight**: both records write "women ... overweight or obese" or "with a BMI of 25.0
  kg/m^2 or more", never "obese women", per §9. The NFHS indicator name is quoted only in quotes.
- **Per cent and %**: both records write "per cent" in prose and in model sentences (blockquotes,
  `reporting_sentence`), and "%" only in tables, working blocks and quotations. C09 says once that
  journals print the sign and the reader should follow the journal. If the reconciler prefers "%"
  inside model paper sentences, change C09 and C10 together.
- **"Margin note"**: C10 calls the one-sentence summary beside each paragraph a "margin note" and the
  list of them the reverse outline; C12 already uses "margin note" in the same sense. Keep it.
- **P values**: C09 says Cole and SAMPL differ and that the journal's instructions decide; any later
  section that prints a P value should follow one of the two and say so.
