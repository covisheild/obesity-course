# S55-R1 Task 2 · drafter notes, batch b2 (C03, C04)

## Records written

- `check/records/S55/S55-R1-C03.yml` — Three kinds of question, and the study each needs (derivable).
- `check/records/S55/S55-R1-C04.yml` — A question you can answer (derivable).

`python check/build.py --check`: zero blocking for both (the only block, missing `S55-R1-C02`, cleared
once C02 landed). Every quote checked verbatim (whitespace-normalised) against its `sources/` file by a
script in `/home/claude/scratch-b2/quotes.py`: 35 of 35 found. The only numbers quoted (2003; 94%, 39%,
133 items, C03 illustration 2) each sit in a quote that states them.

Remaining warnings (five, sentence length and one reading grade 9.1): all fall on research questions
written as one sentence, in exercise prompts and answers. The course asks for a question in one
sentence, so these were left long on purpose; the conductor may shorten them.

## Sources and support

- Textbook anchors: C03 `cdc_ss1978_lesson1` (§7) and `blackstone_2012` (5.2, causality criteria); C04
  `blackstone_2012` (4.2, 4.5, 3.1, 3.2) and `jhangiani_2019_methods`. `ratan_2019` and
  `aslam_emmanuel_2010` as `primary`. No kind relabelled.
- **Nothing unsourced as fact.** Claims derived rather than quoted, and flagged in `verified.note`:
  that chance assignment stops a third thing deciding who is exposed (C03); "or less often" in
  "associated" (C03).
- Ratan pairs "incidence" with a survey; C03 follows CDC (a one-time survey measures prevalence) and
  says so in the note.
- Ratan lists eight question types; C03 folds them into three (describe, relate, cause). That folding is
  the course's, noted in the record.
- FINER is credited to Hulley and colleagues only "as Aslam and Emmanuel report it" (Hulley not held).
  Farrugia not used.
- The minors-need-guardian-consent line in C04 is attributed to Blackstone's American textbook and is not
  stated as an Indian rule. No NMC, ICMR or thesis rule is stated anywhere.
- C03 illustration 2 is real (CDC's hepatitis A case-control study, 94% against 39% ate salsa). Every other
  question, survey, school and result is made up and says so.

## Terms chosen, for the other drafters

- C03: describe, relate, cause (as the three kinds); cross-sectional study, cohort study, case-control
  study (cases, controls), comparison group, associated, randomised controlled trial (S36's existing
  gloss, "a way to test a treatment in which chance decides who gets it, and then the groups are
  compared"), systematic review, prevalence (glossary sense).
- C04: **value question** is the course term for Blackstone's "ethical question", so that FINER's "ethical"
  (a study a committee would approve) is not confused with it. Ethics committee uses the existing S36 gloss
  (shortened). C08's sheet can cite C04's two tests as "empirical" and "feasible".

## Practice sets

Neither concept is quantitative (inventory), so neither carries `practice[]`.

## Figures

Both carry a `figure_note`; `draw.py --book S55-R1` ran with 0 problems (it drew C02's and C08's).
- C03 wanted figure: a timeline, one row per design (cross-sectional, cohort, case-control, randomised
  trial), time running left to right, marking when the exposure is recorded and when the outcome is
  measured: cross-sectional both at time 0; cohort exposure at 0, outcome at the end (e.g. 1 year);
  case-control outcome now, exposure looked for in the past; trial exposure assigned by chance at 0,
  outcome at the end. No numbers needed beyond a notional time axis. The tool draws only charts of data,
  so no spec was declared.
- C04: none wanted; any chart would need invented numbers.

## Glossary rows (proposed; not added to prose/GLOSSARY.md)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| associated (exposure with outcome) | people with the exposure have the outcome more often, or less often, than people without it | `S55-R1-C03` |
| case-control study | a study that enrols people who have the outcome (cases) and people who do not (controls), and compares their past exposures | `S55-R1-C03` |
| causal question (cause question) | a question that asks whether changing the exposure would change the outcome | `S55-R1-C03` |
| cohort study | a study that records who is exposed and who is not, follows them over time, and compares how often the outcome appears in each group | `S55-R1-C03` |
| comparison group | the people without the exposure, or without the outcome, whom the others are set against | `S55-R1-C03` |
| cross-sectional study | a study that takes a sample and measures exposure and outcome at the same time, on one visit | `S55-R1-C03` |
| descriptive question (describe question) | a question that asks how common an outcome is, or how much of it there is, and in whom; it names no exposure | `S55-R1-C03` |
| relational question (relate question) | a question that asks whether an exposure is associated with an outcome | `S55-R1-C03` |
| systematic review | a study of studies: it collects and combines the results of the studies already done on one question | `S55-R1-C03` |
| empirical question | a question that observing the world can answer | `S55-R1-C04` |
| feasible (question) | you, with what you have, can actually get the answer: people you can reach, a way to measure, time, money, equipment and skill, and ethics committee approval | `S55-R1-C04` |
| FINER | a published checklist for a research question: feasible, interesting, novel, ethical, relevant; a guide, not a rule | `S55-R1-C04` |
| value question | a question about what ought to be done, which people answer from their values; no observation settles it (Blackstone calls it an ethical question) | `S55-R1-C04` |

Check at merge: C02 may propose "comparison" and a second sense of "outcome"; C03 uses both in C02's sense.

## For the conductor

- `concept_deps`: C03 → C02; C04 → C02, C03.
- C04 exercise 2 carries `skill_ref: S55-R1-K01` (one-sentence question).
- C03 bridges S55-R2-P02 (the designs named; costs and returns routed to R2 in one line).
