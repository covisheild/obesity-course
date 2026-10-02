# S47-R1 step 5c: restore decisions, batch r3 (C13 to C18)

Restorer: not the cutter and not the cold reader. Inputs: `COLD-READ-GAPS.md` (sections 1, 2 and 4,
gaps C13-* to C18-*), and `<S>-original.md`, `<S>-prose.yml` and `<S>-pass1-prose.yml` for C13 to
C18. Restore lists are in `restore-lists/S47-R1-Cnn.txt`, each line commented with the gap it
closes. Outputs are `S47-R1-Cnn-final-prose.yml`, built by `check/compress/restore.py` and checked by
`check/compress/validate.py`. The tools were not changed.

Key: **restored** means original sentences were put back because they let the reader do the thing.
**hole** means it was not closable here; it is written up for the fixer in `HOLES-r3.md`. **not a
defect** means nothing to do. Placeholder-only gaps are not a defect (conductor's S47 note); the
key's value from `books/S47-R1/numbers.yml` is given.

## Word counts (reader-facing prose, as `validate.py` measures it)

| Section | Original | Cut (pass 1) | Final | Restored | Mean sentence orig → cut → final | Validate |
|---|---|---|---|---|---|---|
| C13 | 1056 | 474 | 645 | +171 | 13.30 → 10.66 → 12.08 | OK |
| C14 | 876 | 487 | 561 | +74 | 14.80 → 14.67 → 14.68 | OK |
| C15 | 769 | 463 | 505 | +42 | 12.73 → 11.17 → 11.63 | OK |
| C16 | 810 | 429 | 469 | +40 | 11.00 → 10.05 → 10.50 | OK |
| C17 | 1197 | 608 | 635 | +27 | 12.49 → 12.44 → 12.49 | OK (equal, at the limit) |
| C18 | 995 | 545 | 554 | +9 | 12.79 → 12.59 → 12.47 | OK |
| **Total** | 5703 | 3006 | 3369 | +363 | | 6 OK |

Two restorations were tried and dropped because they raised the mean sentence length above the
original's (C14 and C17 first lists failed validation at 15.0 and 12.78): the Koon quotation in C14
(C14-7) and the four-marks limit in C17 (C17-3). The list was changed, not the tool.

`python check/build.py --check` was not run: the final text is not yet written back into the records,
which is outside this step's brief.

## Gap by gap

Counts: restored 16, hole 17, not a defect 11 (44 gaps).

### C13
- **C13-1** restored: "The held studies name these among others." Gives the lead-in, so the five
  sentences read as frames the studies name, not as the book's assertions.
- **C13-2** hole (H1): "held" is undefined in the original too.
- **C13-3** restored: "Respondents were shown seven short accounts of why Americans had become
  heavier ..." Gives the antecedent of "The seven were". How the seven accounts map onto the five
  frames is not stated in the original either (residue in H2).
- **C13-4** hole (H3): "social justice against market justice" undefined in the original.
- **C13-5** hole (H4): weighting unexplained in the original.
- **C13-6** restored: "It was fielded from late 2006 to early 2007 to {{n:barry_n}} adults ..." Gives
  sample size (barry_n = 1,009) and fielding years, which reconciles 2006-07 with "(2009)". Ex1 can
  now be completed.
- **C13-7** restored: "In Summan and colleagues' interviews, a health finance official is reported
  saying ..." and "Summan and colleagues report that taxes on junk foods are perceived as falling
  hardest on poorer buyers." These source and illustrate the revenue and fairness frames. Neither
  version says whether "revenue" is a sixth frame or "fairness" is the Justice frame (residue in H5).
- **C13-8** hole (H6): the body-diversity frame is unsourced in the original too.
- **C13-9** restored: "One is an Indian survey that put the same accounts ..." and "Another is a
  review that found many obesity framing studies from India."
- **C13-10** hole (H7): the five frames carry no named source in the original (only "The held studies
  name these among others", restored under C13-1).
- **C13-11** restored: "The held Indian evidence is one study of taxes and subsidies on food (Summan
  and colleagues, 2026)." and "It rests on {{n:summan_kii_n}} interviews, held between February and
  September 2024 ..." Introduces Summan in the text and separates the 2026 publication from the 2024
  interviews (also closes C15-8). The Koon figure is already drawn on in must-know 6.

### C14
- **C14-1** not a defect: placeholder; barry_n = 1,009.
- **C14-2** restored: "It asked about sixteen measures against obesity, besides the seven accounts of
  cause." "Them" now has its antecedent.
- **C14-3** restored: "Which accounts a respondent endorsed predicted which measures they supported,
  beyond what their background, health and politics predicted." Says what the model relates. What R²
  is, and what "measures aimed at helping or protecting people" covers, are not in the original
  (it calls the model "beyond this book"): residue in H8.
- **C14-4** hole (H9): "special de-merit rate" is quoted nowhere in any original section; "the GST
  release" is never introduced by that name.
- **C14-5** not a defect: placeholder; edible_oil_cut_pct = 10.
- **C14-6** restored: "In the survey the disability account went with support for protection from
  discrimination and for treatment, and with less support for most other measures."
- **C14-7** restored: "Framing research states this as a premise." and "One survey in the United
  States found exactly this kind of link." These mark the menu bullets as premise and the survey as
  finding. The Koon/Schattschneider quotation was tried and dropped (mean length), so the premise's
  source stays unnamed in the text (residue in H10).

### C15
- **C15-1** restored: "Watch for cue words — a word or short phrase that carries a frame in a few
  letters." and "A metaphor is one kind: a "sea" of cheap food ..." Needed for P3 and P7.
- **C15-2** not a defect: the Definition glosses value words by what they say ("how bad the problem
  is, whose duty it is, what is fair"), and the reader inferred them correctly.
- **C15-3** hole (H11): "social determinants of health" sits in a quoted exercise passage and is not
  explained in the original.
- **C15-4** hole (H12): "citizens at large" is in no given passage, and the tagline is untranslated,
  in the original too; exercise text is not the pass's to change.
- **C15-5** hole (H13): "slab" undefined; "highest" not checkable from any section.
- **C15-6** hole (H14): "Centre" is never equated with Union / Central Government in any original.
- **C15-7** not a defect: "Then do two more things" names the two steps Ex3 asks for.
- **C15-8** restored in C13 (C13-11): the 2026 study and 2024 interviews are now stated together.

### C16
- **C16-1** not a defect: placeholders; summan_model_tax_range = 10% to 30%,
  summan_model_demand_fall = 7% to 30%. The sentences carrying them were kept by the cut.
- **C16-2** hole (H15): the original gives no scale or wording for degrees of certainty.
- **C16-3** restored: "The researcher's part in it is to set out the options with the evidence for
  each, its uncertainty, and the judgements the choice still needs." Gives the term a use. No source
  for the definition in the original either (residue in H16).
- **C16-4** restored: "That depends on which body holds the power, what the law allows, and the
  money." Says what feasibility turns on. Why that is not partly evidential is not argued in the
  original (residue in H17).

### C17
- **C17-1** hole (H18): the paragraph and rewrite the Figure counts are absent from the original too.
- **C17-2** restored: "Some of the advice Oliver and Cairney reviewed says researchers who want
  influence must engage so far that it blurs." and "This book's rule does not deny that."
- **C17-3** not a defect: the reader was not blocked (reported minor). The original's limit sentence
  ("They do not tell you whether its evidence is good ...") was tried and dropped: it raised the mean
  above 12.49.
- **C17-4** not a defect: context in an exercise passage, not needed for the task.
- **C17-5** not a defect here: the source is shown correctly in C17; the gap is C10's (C10-1, another
  batch).

### C18
- **C18-1** hole (H19): Ex4's "finished note above" exists in no version. The original even promises
  "The worked case below runs the whole note on the first running proposal" and supplies none.
- **C18-2** hole (H20): "cess" undefined, "a 2026 review" unnamed, in the original too.
- **C18-3** restored, with the placeholders not a defect (gst_demerit_rate_pct = 40,
  cgst_sugary_drinks_rate_pct = 20): "The {{n:gst_demerit_rate_pct}}% is the combined rate the
  release gives." This cut sentence is what tells the reader that 40 is the combined rate and 20 the
  central share.
- **C18-4** hole (H21): three addressee rules (C02, C09, C18) unreconciled in the originals; which
  minister Chhattisgarh names is not given.
- **C18-5** not a defect: Ex2 names all three running proposals (tax, canteen rule, warning label) and
  Ex3 fixes the canteen rule as "second". The original's "worked case below" sentence was not restored,
  since it points at absent material (H19).
- **C18-6** hole (H22): education / schools appear in no Seventh Schedule entry or business-rules item
  in any original.
- **C18-7** not a defect.
- **C18-8** hole (H23): the State half of GST (no held SGST source; PIB 2163555 not stated in any
  original), the cess, and what raising the section 9(1) cap would take.
- **C18-9** not a defect: the table cites section topics in descriptive form; the reader could map them.
