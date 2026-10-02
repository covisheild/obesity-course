# S58-R1 · Task 2b reconcile

Reconciler, 2 Oct 2026 (PIPELINE.md "Task 2b — reconcile the batches"). Read `DRAFT-BRIEF.md`
(its rules bind these edits) and `draft-notes-b1.md` … `b9.md`; checked every note for others
against the 23 records in `check/records/S58/`; then checked the records against each other.
Nothing committed. Originals of every record and of `numbers.yml` are in
`/home/claude/scratch-s58-reconcile/` (outside the repository).

**Result:** `python check/build.py --check` blocking 0 (see the end); `python check/figures/draw.py
--book S58-R1` 21 figures, 0 problems.

## What changed, in one list

| Record or file | Change | Why |
| --- | --- | --- |
| `numbers.yml` | 20 keys added (below) | drafters' proposed shared numbers that really are shared |
| C02–C05, C09, C10, C14, C15, C17, C18, C23 | "who were overweight or obese" → "with overweight or obesity" (and "had", "have" forms) in the book's own prose, model sentences, captions and answers | one wording for the book's running term, people-first (claude.md §9); b3, b8, b9 notes |
| C04, C07–C10, C20, C21, C23 | literal 25.0 (BMI cut-off) → `{{n:nfhs5_ow_ob_bmi_cutoff}}` | shared number |
| C09, C20, C21, C23 | 724,115 and 101,839 → keys | shared numbers |
| C09, C10, C17, C21, C22, C23 | other shared numbers → keys (gap, range, ratio, relative rises, Lie Factors, Tufte's 1.05, FRE/FKGL constants, Kanchipuram n, 8 to 13 cm) | shared numbers |
| C23 | reference illustration rewritten: entry 1 formatted on Citing Medicine ch. 22 example 7 (new source `nlm_citing_medicine_2007_reports_web`); 4 new quoted references; boundary must-know, retrieval item and simplified explanation updated; the old "Suggested citation" reference removed | specific item 1 |
| C23 | figure `s58-r1-c23-rise-from-zero.png` removed (it repeated C17's `s58-r1-c17-bars-from-zero.png`); the text now says it is C17's figure and prints its caption as text; PNG and spec moved to `books/S58-R1/superseded-figures/` (moved, not deleted) | specific item 2 |
| C23 | NFHS literals in `working` blocks → keys (allowed once the duplicate figure went: the remaining figure plots only the three FRE scores and 60) | shared numbers |
| C04 | second expansion of ICMJE dropped | b2 note (C01 expands it first) |
| C14 | "a legend in the corner" → "a key in the corner saying which colour is which" | C14 uses "legend" for the journals' caption; one term, one meaning |
| C15 | "baseline" (3×) → "shared start" | GLOSSARY's "baseline" is S02's start of a weight series; C17 avoided it too |
| C17 | one sentence repaired after the wording change (urban and rural women, log-axis paragraph) | |
| C21 | new boundary must-know: Wilke's same-decimals rule against Cole's warning about fixed decimals; two Cole quotes added to its references | b4 note |
| `GLOSSARY-PROPOSED.md` | new: every batch's glossary rows, conflicts resolved | specific item 3 |
| `check/notation.yml` | not changed | no batch needs a row (below) |

## Specific items

1. **C05 and C23, report and web citation.** C23 said the NLM format for a report was not held and
   left entry 1 unformatted. Revised: C23 now cites Citing Medicine ch. 22 for a fact sheet read
   online (quote: "may also be smaller works such as a brochure, single-page fact sheet, or brief
   treatise"), quotes example 7 (the Kaiser Commission line) whole, says the chapter's general
   format is a picture this book does not hold, and builds entry 1 "modelled on example 7":
   `International Institute for Population Sciences. National Family Health Survey - 5, 2019-21:
   India fact sheet [Internet]. *place*: Ministry of Health and Family Welfare; *year* [cited 2026
   Sep 24]. Available from: https://dhsprogram.com/pubs/pdf/OF43/India_National_Fact_Sheet.pdf`.
   Place and year are not on the cover, so they stay as marked gaps (the bib's "Mumbai" and "2021"
   come from the file header and the bib note, not a passage, so the record does not print them).
   Author = the body that prepared it, publisher = the body issuing it (ch. 22: "A publisher is
   defined as the individual or organization issuing the book"); title capitalised by ch. 4's rule.
   The `analogy_breaks_when` names what is not held (the "(US)"-style country rule; how an entry
   shortens when one body both prepares and issues). **C05 not changed**: it says a report "follows
   other chapters of Citing Medicine, which this section does not teach", which is still true; it
   never says no format is held. **For the auditor:** whether the Ministry or IIPS is the publisher
   is the reconciler's reading of the cover (the drafter's "issued by / prepared by" table), not a
   statement in the fact sheet.
2. **C23's figure duplicated C17's.** The journey's own decision is that the paper keeps the table
   and the figure goes to the talk, so the book need not draw it twice. The duplicate is removed;
   C23's figure step now points to C17's bars-from-zero figure and prints the caption as text. C23
   keeps its other figure, the three drafts' FRE scores, which does work no other section's figure
   does.
3. **Glossary.** `GLOSSARY-PROPOSED.md`: 96 rows, alphabetical, plus a table of the conflicts and
   how each was settled ("subject" two senses replacing the existing row; "legend" two senses;
   "gap" merged; "confidence interval" merged across C09/C20; "hypothesis" kept at C04; "baseline",
   "precision", "vector" avoided). `prose/GLOSSARY.md` not edited.
4. **Figure planner.** Below, unresolved.

## Notes for others: dispositions

Legend: **applied** (edit made), **handled** (the records already do it; no edit), **rejected**
(with the reason).

### b1 (C01–C03)

| Note | Disposition |
| --- | --- |
| ICMJE cited as IV.A, quoted briefly; C01 expands ICMJE and IMRAD, later sections may use them bare | handled; C04's second expansion **applied** (dropped), see b2 |
| C04 builds on C01's section jobs; C02 claim-first vs Mensh & Kording Rule 7 | handled: C04 teaches Rule 7 at paragraph level, C10 illustration 2 names both shapes as sound; no record calls either wrong |
| C05 owns numbering and NLM style | handled |
| C09 should say what a writer does when the source gives no numerator | handled: C09 illustration 1 and must-know 7 (say there is no count; never multiply the interviewed total) |
| C10: keep C02's C/E/S letters or say they are dropped | rejected: C10 labels sentences by topic and never uses letters; C02's letters are its own exercise device, so there is nothing for a reader to reconcile |
| C14 and R2: one message for paper, talk and poster | handled: C14 remakes the slide figure, not the message |
| C23 reuses C02/C03 (message, titles, limits) | handled: C23 reuses C03's message verbatim (the wording change was made identically in both) and states the limits |
| C03: the fact sheet prints NFHS-4 beside NFHS-5 but not the change | handled: nothing contradicts it |
| Numbers: 40, 36, 1,297 | not registered: each is used in one section only |

### b2 (C04, C05)

| Note | Disposition |
| --- | --- |
| C01: Sollaci & Pereira pages 364–371 (PMC) vs 364-7 (PubMed) | handled at intake: `library.bib` prints 364-367 with a note; no record prints the pages. Left for the audit if the rendered reference list should follow the article itself |
| C04 re-expands ICMJE; keep the first expansion | **applied** in C04. C08 (a retrieval prompt) and C09 also spell out the name; left, as harmless for a reader who starts at that section |
| C10 should point back to C04 for Rule 7 | handled (C10 illustration 2) |
| C21 must not contradict table-only reference numbering | handled: C21 says nothing on it |
| C23: NLM report/web format not held | **applied** with the new source (item 1) |
| C09/C23: differences in points, not stated in C04/C05 | handled |
| Predatory journals routed to R2 | handled |
| Glossary: drop C04's gloss of "hypothesis" if C01 glosses it | C01 uses it without a gloss, so C04's gloss stays; logged in `GLOSSARY-PROPOSED.md` for the audit |
| Numbers: 25.0 | **applied** (`nfhs5_ow_ob_bmi_cutoff`); Rougier's date, C05 only, not registered |

### b3 (C06–C08)

| Note | Disposition |
| --- | --- |
| C09 must not report a P value without its test | handled: C09 exercise 1's answer sends the girls-boys comparison "with its test" |
| C10: "topic sentence", never "topic position"; C10 carries K01 | handled (C10 never says "topic position"; its exercises carry `S58-R1-K01`) |
| C11 may quote Gopen & Swan's "29" | rejected: optional; C11 already makes the trip-wire point with Plavén-Sigray and the formulas' fitting samples; adding a quote is drafting |
| C12's "compressing" in C07's sense | handled (both: fusing ideas into fewer, longer units) |
| C21, C23: one term "overweight or obesity", person-first | **applied book-wide**; see "One wording" below |
| All sections: no more than three abbreviations | rejected as a book rule: it is C08's advice for a paper; the book expands each abbreviation at first use and the build's acronym check covers it |
| "UA" left unexpanded on purpose (C08) | handled; the audit should expect the render's acronym list to print it |
| Numbers: 25.0; 18.5; survey years; Barnett & Doubleday's rates | 25.0 **applied**; 18.5 and the acronym rates are C08's alone (C09's 0.4 and 4.1 are other quantities); survey years rejected: "2015-16" and "2019-21" are the rounds' labels, part of the survey's name like "NFHS-5", not quantities |

### b4 (C09, C10)

| Note | Disposition |
| --- | --- |
| C20 keeps C09's CI gloss | handled: C09 leaves the working-out aside, C20 gives the 95% meaning; merged into one glossary row |
| C21's "same decimals" vs Cole's warning | **applied**: C21 must-know 9 and two Cole references |
| C23 reuses C09's reporting sentence, one decimal, no count from 724,115 | handled |
| C02/C04/C10 paragraph shapes | handled |
| C04's "outline" wording stable | handled (C10 defines the reverse outline as C04's outline made after the draft) |
| C12 may use C10's empty closing sentence | rejected: optional, not needed |
| Wording on weight ("never obese women") | handled, and superseded by the book-wide wording below |
| "per cent" in prose, "%" in tables | handled; no change |
| "margin note" shared with C12 | handled |
| Later sections printing a P value follow one rule | handled: C20 and C21 print none (C21 leaves the P-value column out) |
| Tool note: draw.py does not substitute `{{n:}}` | to the figure planner and conductor (below) |
| Notation: a row for "<" | rejected: `check/notation.py` skips ASCII, so the row would never print; the build reports no unknown S58 symbol |
| Numbers: 724,115; 13.5; 0.165 and 0.212; 5.1 | **applied**: `nfhs5_women_interviewed`, `nfhs5_women_ow_ob_urban_rural_gap_pp`, `nfhs_women_ow_ob_rel_rise_pct` (17) and `nfhs_men_ow_ob_rel_rise_pct` (21) for the rounded per cents in prose, `nfhs_ow_ob_totals_range_pp`. The unrounded 0.165 and 0.212 stay in `working` lines, where the arithmetic gate recomputes them |

### b5 (C11–C13)

| Note | Disposition |
| --- | --- |
| C13's four parts of a message vs C03 | handled: C03 names no parts, so nothing to align |
| C07 teaches splitting and the active voice | handled (C07 must-know and definition item 5) |
| C10 defines the reverse outline in margin terms | handled |
| C09 must not imply a score is neutral to figures | handled |
| C23: FRE weight 84.6 from Flesch, counting rule stated, bands from Flesch 1979; one `build` exercise (C13) | handled; C23's FRE/FKGL constants now come from the registry |
| Flesch 1979's publisher from general knowledge | nothing in the records; a `library.bib` matter |
| No "now"/"currently" of NFHS-5 | handled |
| Numbers: FRE/FKGL constants; 60; Plavén-Sigray; Kincaid sample; 2021 | constants **applied** (6 keys, used in C23's working; C11 keeps literals because its figures plot them). 60 not registered: both records that print it (C11, C23) plot it in a figure and must keep it literal, so a key would only warn as unused. Plavén-Sigray and Kincaid figures are C11's alone. 2021 rejected: a date, quoted where it matters ("30 April 2021") |

### b6 (C14–C16)

| Note | Disposition |
| --- | --- |
| C14 calls a figure's statement its "claim" | handled |
| C17 builds on C15 (axis above zero for points; log axis: amounts as dots) | handled: C17 says the same and adds ratios as bars from 1; no contradiction |
| C18 need not repeat the pie conclusion | handled |
| C20 owns the rest of the caption | handled |
| C21 uses the same sentence/table/figure rule | handled |
| C22: a slide figure is made again | handled (and C23 says so) |
| C23: urban-rural trend not checkable | handled |
| Terms: strip chart, box plot, bar chart | handled; and C15's "baseline" **applied** → "shared start" (GLOSSARY clash) |
| Orphan PNGs | handled before reconcile (in `superseded-figures/`) |
| Tool: categorical x / `x_ticks` | to the figure planner |
| `kind: dataset` rejected by the build | to the conductor (all records use `instrument`) |
| Numbers | none shared beyond one section |

### b7 (C17, C18)

| Note | Disposition |
| --- | --- |
| C19, C20 point back to C18's direct labels | handled |
| C22 takes its axis and decoration steps from C17, C18 | handled (C22 works the Lie Factor and asks of each default what it tells the reader) |
| C23 uses "Lie Factor (LF)", "axis start", a ÷ (a − s) | handled |
| Tufte is 1983 | handled (no "2001" outside quotes) |
| Correll's 4.6 for C09 | rejected: optional; C17 practice 9 already uses it |
| Bateman: no "recall" | handled (only in quotes and locators) |
| C17 does not contradict Book 0 F2 | handled |
| 1.685 reported as 1.69 in C09 and C17 | **applied**: `nfhs5_women_urban_rural_ratio` |
| Numbers: 1.05; 34.3 | `tufte_lf_threshold` **applied** (used in C23; C17 keeps the literal, which its figure's reference line plots). 34.3 is C17's alone (C09's 34.3 is a made-up mean age) |
| Truncated bar figure wanted | to the figure planner |

### b8 (C19–C21)

| Note | Disposition |
| --- | --- |
| `kind: dataset`; arithmetic gate | informational |
| 25.0 | **applied** |
| C18 must define direct label and legend | handled; and C14's one key-sense "legend" **applied** → "key" |
| C14 vs C20 wording | **applied** book-wide |
| C16 must not call an SE bar spread | handled |
| SD and SE expanded again in C20 | no change |
| 724,115 and 101,839 are not the BMI rows' n | handled (C17 and C22 never use them); keys **applied** |
| C22 keeps "in grey", "simulator", 8 to 13 cm | handled; 8 and 13 **applied** as keys (C20, C22) |
| C23 reuses C21's table, table or figure not both | handled |
| Krishnamurthy is one district | handled |
| Reproductions | nothing to do |
| Numbers: Kanchipuram rows, 8 per cent | `cvd_kanchipuram_boys_n` **applied** in C21's prompt; C19 keeps the literal (its figure's table states it). Cases, per cents and rows are not registered: C21 has them only in its reprint of Krishnamurthy's Table 1, which is treated as a quotation. 8 per cent is C19's alone |

### b9 (C22, C23)

| Note | Disposition |
| --- | --- |
| C14/C21 table-or-figure consistency | handled |
| Wording (person-first) | **applied** book-wide |
| C23's new "does not mean" line | nothing to do |
| C21 must not say Cole requires one decimal | handled; C21's new point agrees with C23 |
| C22 routes code to S52 unnamed | handled |
| C22 relies on C19/C20 wording | handled |
| C23 figure overlaps C17 | **applied** (item 2) |
| NLM entry unformatted | **applied** (item 1) |
| Palette nearly merges in grey | to the figure planner, unresolved |
| Numbers: 25.0; 5.1; 14.3; 7.92/21; 0.165; 724,115; anaemia rows | 25.0, 5.1, 724,115 **applied**; 7.9 and 21 registered (`nfhs_women_lf_axis18`, `nfhs_men_lf_axis18`; C17 keeps 7.92 and 21 where its figure plots them); 14.3 is C23's alone; 0.165 see b4; anaemia values in C21 and C22 that look alike are different rows |

## Cross-checks across the 23 records

**One wording for the running term.** C08 says "This book writes 'women with overweight or
obesity', putting the person first", and claude.md §9 asks for people-first construction; about 60
places wrote "were overweight or obese". Changed in the book's own voice: narration, model and
reporting sentences, the one message (C03 and its copy in C23, identically), captions, tables of
model claims, answers. **Not changed, on purpose:** quotations of the fact sheet's row label;
C14's "Search for overweight or obese" (the words to search the PDF for); figure axis titles
(`y_label` "overweight or obese (%)", the indicator's label, and C23's sentence naming that
title); `numbers[].unit` fields; `working` labels; invented drafts written to be criticised (C01's
draft introduction, C02's diary, C23's diary); and drafts whose words and syllables are counted
(C11, C12, C23's claim draft and cut paragraph), where a change would break the counts. C23's
reader test now says "The draft's 'overweight or obese'…", since the draft she read keeps the
adjective. **For Harsh:** if he reads §9 as allowing the predicate "were overweight or obese",
the change is easy to undo from the originals in the scratch folder.

**One term, one meaning.** "legend" (C14 key use changed; C20 already explains the two senses);
"baseline" (C15 changed); "gap" (C01/C04, one sense); "outline"/"reverse outline" (C04/C10, one
sense); "compressing" (C07/C12, one sense); "claim"/"one message" (C02/C03/C14, one sense);
"caption" (C14 onward). No other clash found.

**One symbol, one meaning.** a, b and s (smaller bar, larger bar, axis start) mean the same in
C17, C22 and C23; n is a count of independent people or units throughout; LF, ASL, ASW, FRE, FKGL
are expanded in the sections that introduce them. `check/notation.yml`: no row added. Every batch
reported none needed, and the build reports no S58 symbol without a row (the only candidate, "<",
is ASCII and is skipped by `notation.py`).

**Pointers.** Every "the last section", "the next section", "the last two sections" was checked
against the sequence: C06→C07 (twice), C09→C07–C08, C15→C16, C15→C14 (twice), C16→C14–C15,
C19→C18, C23→C22. All right. No pointer names a section number.

**Numbers.** Policy used: a number printed in two or more sections comes from `numbers.yml`, in
prose, tables and `working` lines alike, except (a) inside quotes and in tables that reprint a
source's own table, (b) in a record whose own figure plots or prints that value (draw.py reads the
raw record, so the literal must stay there; the figure check confirmed 0 problems), and (c)
unrounded intermediate results in `working` lines, which the arithmetic gate recomputes. Keys
added:

| Key | Value | Used in |
| --- | --- | --- |
| `nfhs5_ow_ob_bmi_cutoff` | 25.0 | C04, C07, C08, C09, C10, C20, C21, C23 (C14 keeps the literal: its caption states it) |
| `nfhs5_women_interviewed`, `nfhs5_men_interviewed` | 724,115; 101,839 | C09, C20, C21, C23 |
| `nfhs5_women_ow_ob_urban_rural_gap_pp` | 13.5 | C09, C10 |
| `nfhs5_women_ow_ob_urban_rural_ratio` | 1.69 | C09, C17 |
| `nfhs_ow_ob_totals_range_pp` | 5.1 | C09, C17, C23 |
| `nfhs_women_ow_ob_rel_rise_pct`, `nfhs_men_ow_ob_rel_rise_pct` | 17; 21 | C09, C23; C09 (C17 keeps "21" literal, which its figure states) |
| `nfhs_women_lf_axis18`, `nfhs_men_lf_axis18` | 7.9; 21 | C17, C23; C23 |
| `tufte_lf_threshold` | 1.05 | C23 (C17 literal, plotted) |
| `fre_constant`, `fre_asl_weight`, `fre_asw_weight`, `fkgl_asl_weight`, `fkgl_asw_weight`, `fkgl_constant` | 206.835, 1.015, 84.6, 0.39, 11.8, 15.59 | C23 (C11 literal, plotted) |
| `cvd_kanchipuram_boys_n` | 74,986 | C21 (C19 literal, plotted from its table) |
| `figure_check_width_low_cm`, `figure_check_width_high_cm` | 8; 13 | C20, C22 |

The ten keys from Task 1 were already used through `{{n:}}`; their literal copies remain only in
quotes, in C08/C14/C23 blockquotes of the fact-sheet rows, and in C14 and C17, whose figures plot
them.

## For the figure planner (unresolved)

Figures the drafters wanted and the tool cannot draw, as they described them:

- **C04 (b2):** the paper's argument as a funnel and its mirror: Introduction narrowing from field
  to gap to question; Methods and Results as a column of claim boxes, each arrowing into the next;
  Discussion widening from the answer to explanations, limits, meaning. Labels from C04's outline
  table; no numbers. Model: Mensh & Kording Fig 1 (CC BY 4.0; image not held, caption only).
- **C05 (b2):** one reference annotated: "Rougier NP, Droettboom M, Bourne PE. Ten simple rules for
  better figures. PLoS Comput Biol. 2014 Sep 11;10(9):e1003833." with a bracket and label under
  each element and each punctuation mark called out.
- **C06 (b3):** a marked-up sentence: subject, verb, object and doer labelled under "Written informed
  consent was obtained ... by the investigator", and its active twin.
- **C10 (b4):** a page with a margin column, each paragraph boxed with its one-sentence note beside
  it, before and after.
- **C09 (b4):** a paired bar chart of the NFHS women and men rows (NFHS-4, NFHS-5) with the change
  labelled in points and per cent. Drawable, but every value is `{{n:}}` in C09's text and
  draw.py does not substitute, so the figure check fails unless the numbers are typed literally.
- **C15 (b6):** a line over the two NFHS rounds; numeric x of 4 and 5 printed meaningless ticks.
  Needs categorical x (or an `x_ticks` option) for line and scatter.
- **C16 (b6):** a true strip chart, one column of jittered dots per ward (same need: categorical x).
  The drafter drew each ward's dots in order instead.
- **C17 (b7):** the brief's same data with a zero and a truncated baseline: NFHS women 20.6% and
  24.0% as bars on an axis from 20 (drawn heights 0.6 and 4.0, second bar 6.67 times the first,
  LF 34.3) beside the same bars from zero. `figspec.verify` blocks any bar chart not starting at
  zero, by design; it would need a deliberate "wrong on purpose" bar kind with a mandatory label.
- **C20 (b8):** the three error bars (SD 12.0, SE 6.93, approximate 95% CI 27.7) drawn around the
  mean of 40.0; no error-bar kind, so the arm lengths are drawn as bars.
- **C01 (b1, cosmetic):** the 1935 point sits on the x axis and the 1985 point on the top edge
  (y range 0-100); 105 would have to be stated in the text.
- **C23:** its duplicate bars-from-zero figure was moved to `superseded-figures/`; if the planner
  wants the journey to show its talk slide, that is a new figure.

**The palette nearly merges in grey (b9).** The S58-R1 palette's `primary` #b6206b and `secondary`
#138613 have relative luminance about 0.12 and 0.17 (contrast about 1.3:1), so the two series of a
two-series figure nearly merge in greyscale: the test C19 teaches ("make the two colours differ in
lightness, not only in hue") and C22 tells readers to run. b9 names C14, C17, C22 and C23 (C23's
two-series figure is now superseded). The reconciler's reading of the specs, not a drafter's: every
figure with two or more series uses the same pair, so C07, C08, C11 (counting rule), C15, C16
(every value, three series) and C18 are in the same position. A fix in `style_for` means redrawing
every S58 figure; C22's text was written not to claim its colours differ in lightness.

**Axis titles and the wording change.** Figure axis titles still read "overweight or obese (%)"
(C14, C17, the indicator's label). If the people-first wording should reach the figures too, they
need relabelling and redrawing.

**Tooling (b4, b6, b7, b8):** `draw.py --book` does not run `reader_checks.apply_numbers`, so a
figure whose numbers are only in `{{n:}}` form fails; drafters kept such numbers literal in the
records that plot them, and this reconcile kept that rule. The build also rejects `kind: dataset`
although the schema lists it.

## Build

`python check/build.py --check` after the last edit: see the line below, appended when the run
finished. S58 warnings are the drafters' deliberate long sentences (unchanged), C05's "paradigm"
(a title), and none new from these edits (two new 26-plus-word sentences were split).

Run 2 Oct 2026 after the last edit: `records 149 | clusters 9 | blocking 0 | warnings 217` (the
same 217 as before the reconcile), exit 0. `draw.py --book S58-R1`: 21 figures, 0 problems.
