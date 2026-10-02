# S47-R1 step 5c, batch r2: restore decisions (C07 to C12)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` sections 1, 2 and 4
(gaps C07-* to C12-*), and `<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml` for each
section. Restore lists: `restore-lists/S47-R1-Cnn.txt`, each line commented with the gap it closes.
Outputs: `S47-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and checked by
`check/compress/validate.py`. Tools not changed. Holes are written up for the fixer in `HOLES-r2.md`.

Key: **restored** = original sentences put back because they let the reader do the thing.
**hole** = not closable here (the original does not fill it, or it is an error or contradiction).
**not a defect** = nothing to do, with the reason.

Section 1 and section 2 items in this range cite the same gap ids as section 4 (C07-5, C07-6,
C08-1, C08-7, C09-1, C09-2, C09-3, C09-6, C09-8, C11-8, C11-10 to C11-13), so they are decided once,
below. The section 1 point "counting convention" for C11 P6 is C07-3.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → final | Validate |
|---|---|---|---|---|---|---|
| C07 | 882 | 467 | 516 | +49 | 14.70 → 13.95 | OK |
| C08 | 773 | 450 | 510 | +60 | 13.56 → 13.42 | OK |
| C09 | 733 | 398 | 522 | +124 | 13.83 → 13.38 | OK |
| C10 | 1120 | 516 | 600 | +84 | 13.33 → 11.54 | OK |
| C11 | 1130 | 618 | 713 | +95 | 13.22 → 12.40 | OK |
| C12 | 760 | 345 | 477 | +132 | 11.81 → 11.00 | OK |
| **Total** | 5398 | 2794 | 3338 | +544 | | 6 OK |

Two first lists failed validation on mean sentence length and were cut back (first versions kept in
`/home/claude/scratch-restore-r2/`): C07 lost the two section 93 sentences (C07-4, now not a defect),
and C08 lost the National Mission on Edible Oils sentence (C08-5, now a hole).

`python check/build.py --check` was not run: the final text is not yet written back into the
records, which is outside this step.

## Gap by gap

### C07
- **C07-1** restored: "Section 23 of the General Clauses Act, 1897 applies where a Central Act gives a
  power to make "rules or bye-laws" subject to previous publication." Names the source the
  Definition's next sentences paraphrase. What the General Clauses Act is stays unexplained in the
  original too (minor; not carried as a hole).
- **C07-2** hole (H-r2-1) for "days of sitting", unexplained in the original. The placeholders are not
  a defect: `packaging_draft_objection_days` = thirty, `laying_days` = thirty.
- **C07-3** hole (H-r2-2): the original does not teach how to count the period either.
- **C07-4** not a defect: the period is in must_know[3] (thirty days of sitting) and the effect in
  must_know[0] (modify or annul, things done stay valid). The original's two section 93 sentences
  were tried and dropped: they raised the mean sentence length past the original's.
- **C07-5** restored: "It, and any authority whose sanction, approval or concurrence is needed, must
  consider any objection ..." The approving body considers the objections, so approval follows
  publication. The original never states the order outright; residual noted in H-r2-3.
- **C07-6** hole (H-r2-4), possibly an error: the original says "Every rule and regulation made under
  that Act is laid before each House of Parliament"; State rules under section 94 are not covered.
- **C07-7** hole (H-r2-5): how a Committee of Secretaries decision "binds officials" is not explained
  in the original either.

### C08
- **C08-1** restored: "Under Article 112(1) the President lays before both Houses of Parliament ..."
  Ex1 was blocked without it, and "Two articles" now has both.
- **C08-2** hole (H-r2-6): "Anganwadi" is undefined in the original; the NFSA sections are cited
  there, not quoted.
- **C08-3** not a defect: the reader inferred "Act and scheme" correctly; with C08-4's restore the
  policy is named, and the original words it identically.
- **C08-4** restored: "The National Health Policy 2017 was approved by the Union Cabinet on 15 March
  2017." (definition, closing the dangling "It was not passed") and "The Union Cabinet approved the
  National Health Policy 2017; Parliament did not pass it." (must_know[0], the referent of "It says").
- **C08-5** hole (H-r2-7): the original's introducing sentence ("The National Mission on Edible Oils
  – Oilseeds was approved ...") was tried and dropped, because it failed the mean-sentence gate.
- **C08-6** hole (H-r2-8): the figure's components (general, salary, supplementary nutrition) are not
  explained in the original; its 60:40 sentence names "general components" without saying what
  they are.
- **C08-7** hole (H-r2-9): "crore" is undefined in the original.
- **C08-8** hole (H-r2-10): the original names no instrument or numbered provision for a scheme
  (shared with C11-7).

### C09
- **C09-1** not a defect (placeholders): `cgst_sugary_drinks_rate_pct` = 20, `gst_demerit_rate_pct` =
  40, `gst_council_majority` = three-fourths, `gst_union_vote_weight` = one-third,
  `gst_states_vote_weight` = two-thirds, `gst_council_majority_pct` = 75. What the 40 is relative to
  the 20 is C09-3.
- **C09-2** hole (H-r2-11): "heading" and the tariff numbering are undefined in the original.
- **C09-3** hole (H-r2-12): the State half of GST; no held SGST source, and the original has no
  sentence stating what PIB 2163555 says about it.
- **C09-4** restored: "A food advertisement that misleads falls under section 24 ..." and "It also
  falls under section 21 of the Consumer Protection Act, 2019 ..." An example for the third shape.
  The first shape is left as is: C04 gives the Concurrent List.
- **C09-5** hole (H-r2-13): contradiction across C02, C09 and C18; the original has the same rule.
- **C09-6** restored: "The Central Government notifies the rate of central goods and services tax
  (CGST), under section 9(1) ..." and "It does so "on the recommendations of the Council", at a rate
  not exceeding ... per cent." Shows the link between Article 279A(4) and section 9(1), so Ex3's
  "whenever it chooses" can be refuted. Also closes the dangling "A recommendation is not a tax."
- **C09-7** restored by the same two sentences: section 9(1) is now quoted, not asserted.
- **C09-8** restored: "It sits in Schedule III of Notification 9/2025-Central Tax (Rate), in force 22
  September 2025, as amended by 01/2026 from 1 May 2026." Names the instrument amended and the
  amending notification. What 01/2026 changed is not in the original; residual in H-r2-14.
- **C09-9** restored: "Each decision needs not less than ... of the weighted votes of the members
  present and voting." How the States' votes divide is not a defect: must_know[6] says the map does
  not tell you.
- **C09-10** not a defect: Ex2 asks for things the table does not tell; Schedule I is one of them,
  and exercises are not this step's to change.

### C10
- **C10-1** restored: "Summan and colleagues held {{n:summan_kii_n}} interviews in 2024 and reviewed
  documents." Antecedent of "They".
- **C10-2** restored: "When a trainee hands you a stakeholder table, point at each row and ask two
  questions aloud: does this actor decide, or push?" Subject of the orphan question.
- **C10-3** restored: "The next level of this subject gives all this a formal shape, the policy
  triangle of Walt and Gilson." and "It looks at four things together ..." What "This section gives
  you the actors" was contrasting with.
- **C10-4** hole (H-r2-15): "process theories" is undefined in the original, and the next level is
  outside this book.
- **C10-5** hole (H-r2-16): the original's Definition also defines lobbying as an organisation's case
  while plain terms count researchers as actors who lobby. Outside lobbying is in plain terms, so the
  reader was not blocked by its absence from the Definition.
- **C10-6** restored: "A campaign, a press storm or a powerful company can move a decision." Antecedent
  of "None of them" and "it".

### C11
- **C11-1** restored: "When a trainee's proposal says "the government should", hand it back with three
  blanks: X, Y and Z." Antecedent of "them" and "each".
- **C11-2** restored: "Write both candidate deciders, the step where the trace stopped, and the
  document that would settle it." What to write when a trace forks.
- **C11-3** restored: "The GST Council's own release says its decisions take effect through
  notifications ..." (introduces the release) and "The central GST rate on sugar-added drinks is ...
  per cent, in Schedule III ..." (the Union's share). Placeholder: `gst_demerit_rate_pct` = 40. The
  Union/State split itself is C09-3.
- **C11-4** hole (H-r2-17): conflict with C01's definition of a proposal; same in the original.
- **C11-5** restored: "India is a Party to the WHO Framework Convention on Tobacco Control, and the
  Convention itself leaves action to "national law"." Why a treaty comes up.
- **C11-6** hole (H-r2-18): order of commencement, notification and laying not given in the original.
- **C11-7** hole (H-r2-10, with C08-8).
- **C11-8** hole (H-r2-19): practice-set wording (P3 "which step", singular).
- **C11-9** hole (H-r2-20): P2(a) entry 52 not tied to C04 in the original.
- **C11-10** hole (H-r2-21): COTPA never expanded; P5 notification and bodies unexplained.
- **C11-11** hole (H-r2-22): section 92(2), "read with", and the two "section 23"s.
- **C11-12** hole (H-r2-23): no agriculture entry, no NMEO ministry, scheme-and-List question unsettled.
- **C11-13** not a defect (placeholder): `gst_demerit_rate_pct` = 40. Whether P10's request is moot
  is the problem's point (the Ministry of Health does not impose GST), not a missing sentence.
- **C11-14** hole (H-r2-24): "wholesome" undefined in the original.

### C12
- **C12-1** restored: "In the form most used in health policy research, the choice serves four
  functions." and "The account defines a problem, diagnoses its cause, passes a moral judgement and
  suggests a remedy." The four are named before "all four".
- **C12-2** restored: "Not every account carries all four." The clause "But" contrasts with.
- **C12-3** restored: "Agenda setting is the choice of which issues get attention at all, the part of
  the policy process that comes first." Ties the term to C01's first stage. The original's "Two
  neighbouring ideas ..." was not restored, because its priming half was not needed.
- **C12-4** restored: "Before you agree or disagree with a paragraph, write its four labels: problem,
  cause, judgement, remedy." What "Then" follows.
- **C12-5** restored: "Keep the three ideas apart in a meeting." and its three sentences "Agenda
  setting decides ...", "Framing decides ...", "Priming is what ..." Names the three.
- **C12-6** restored: "These four are Entman's (1993), as reported by Koon, Hawkins and Mayhew in a
  2016 review of framing research on health policy." Authors and year to find the review.

## Counts

| Section | Restored | Hole | Not a defect |
|---|---|---|---|
| C07 | 2 | 4 | 1 |
| C08 | 2 | 5 | 1 |
| C09 | 5 | 3 | 2 |
| C10 | 4 | 2 | 0 |
| C11 | 4 | 9 | 1 |
| C12 | 6 | 0 | 0 |
| **Total (51)** | **23** | **23** | **5** |
