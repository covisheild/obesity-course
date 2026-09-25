# S55-R1 glossary merge report

CONDUCTOR step 8. Checked against the final text as built by `python3 check/build.py --subject S55-R1`
(`check/_build/S55-R1.md`, 25 September 2026), not against the draft notes. Section n is record
`S55-R1-C0n`. No record was edited. No existing row of `prose/GLOSSARY.md` was changed; new rows
were inserted in their alphabetical places, as the file's header asks. The five batches' proposals
were merged into one definition per term, in the final text's words.

## 1. Rows added to `prose/GLOSSARY.md` (39)

answerable (research question) (C04); case report (C06); case-control study (C03); cause question
(C03); citation (C06); citation database (C06); citation window (C06); cohort study (C03); comparison
(in a research question) (C02); comparison group (C03); conflict of interest (C07); context placement
(C05); cross-sectional study (C03); describe question (C03); empirical question (C04); exposure (C02);
feasible (question) (C04); FINER (C04); how-common question (C02); implementation money (C07);
information gain (C05); intervention (C02); meta-analysis (C06); open window (of a citation count)
(C06); PECO (C02); peer-reviewed (paper) (C06); PICO (C02); relate question (C03); research money
(C07); research question (C01); research topic (C01); scoring sheet (five-item sheet) (C08);
self-citation (C06); systematic review (C03); uncited (C06); uncitedness ratio (C06); value question
(C04); who-is-waiting test (C07); worth answering (C05).

Three of these were in no batch's proposals but are taught in a Definition of the final text:
answerable (C04), peer-reviewed (C06, "one checked by other researchers before the journal accepts
it") and self-citation (C06).

## 2. Draft-note proposals not added, or changed

- **problem base** (b3) and **CSR (corporate social responsibility) funds** (b4): not in the final
  text. No row.
- **associated** (b2): the final text never glosses the word on its own; it is carried by the relate
  question row ("associated with an outcome: whether the two go together"). No row.
- **Renamed to the final text's terms**: b2's "causal question (cause question)", "descriptive
  question (describe question)" and "relational question (relate question)" became cause question,
  describe question and relate question: the final text never says causal, descriptive question or
  relational. b5's "open citation window" became **open window (of a citation count)**: C06 says
  "an open window" only. b4's "scoring sheet" keeps the name, with C08's "five-item sheet" as alias.
- **how-common question and describe question**: two rows, not one. C02 teaches "how-common
  question"; C03's Definition says a describe question "is what the last section called a how-common
  question". The describe question row points back to C02.
- **Definitions corrected to the final text**: comparison (b1's "some sources call it the control or
  the comparator" is gone); feasible (C04's list); FINER ("a published guide, not a rule", C04
  Must-know); cohort and case-control study (C03's "starts from the exposure / the outcome");
  cross-sectional study (C03 Definition plus "one visit, one count"); context placement and
  information gain (C05 now names them "second" and "third" features and asks "is the study large
  enough to inform?"); uncitedness ratio (b3 credited the term to Golosovsky and Larivière; C06 gives
  it as Nicolaisen and Frandsen's measure, "a share written as a fraction of 1"); uncited (C06
  Definition plus the Must-know reading "no citation found in this database by this date");
  conflict of interest (C07 Must-know: "a party who gains from one answer"); who-is-waiting test
  and worth answering (C07 and C05 Definitions).
- **Inline glosses not added (conductor to decide)**: protocol ("the written plan of a study drawn
  up before it starts", C02 Illustration 1); pilot ("a small try-out of the hardest line before the
  main study", C04); guideline group ("the panel that writes the advice clinicians follow", C07);
  cases and controls (folded into the case-control study row). None is in a Definition or "In plain
  terms", and no batch proposed them. `pilot interview` (`S36-R1-C14`) is a different, interview-only
  term; a general "pilot" row would not clash with it.

## 3. Existing rows used in the same sense (not re-added), and wording checks

| Term (row) | This book's first use | Wording |
| --- | --- | --- |
| population (`B0-R0-C28`) | C02: "the group the answer is about", bounded by place, person and time | differs: row says "the whole group a question is about"; C02 adds the fence. Same sense |
| prevalence (`B0-R0-C26`) | C03: "of the people in the group, how many have the condition at that time" | close; C03 adds "at that time" and omits P(condition present) |
| randomised controlled trial (`S36-R1-C01`) | C03 In plain terms | matches the row word for word |
| ethics committee (EC) (`S36-R1-C07`) | C04 In plain terms | matches the row's first clause; C04 never expands or uses "EC" |
| median (`B0-R0-C28`) | C06: "the middle value once the counts are put in order" | matches |
| body mass index (`B0-R0-C14`) | C05 Exercise 1: weight in kilograms divided by the square of height in metres | matches |
| sample, sampling variation (`B0-R0-C28`, `-C29`) | C03, C04 | same sense |
| argument, premise, conclusion, inference (`B0-R0-C42`) | C01, C05, C06, C07 exercises and C07 In plain terms | same sense |
| percentage, percentage change (`B0-R0-C04`) | C08 | same sense |

## 4. Sense clash (existing row unchanged)

1. **outcome.** Row (`B0-R0-C24`): "one member of the sample space". C02's Definition: "the outcome
   is what is measured to answer the question". Different sense. The file's header forbids changing
   a row mid-book ("a between-rounds job"), so no sense (2) was added. Between rounds the row should
   become "(1) one member of the sample space (`B0-R0-C24`); (2) in a research question, what is
   measured to answer it (`S55-R1-C02`)". Until then this book's sense has no glossary record.

## 5. Drift inside S55-R1, and terms used before they are defined

- **how-common question** is first named in C02 Illustration 1 ("That is a how-common question");
  C02's In plain terms says only "It asks how common something is". The figure caption before
  Illustration 1 also says "how-common question".
- **comparison / comparison group**: C02 teaches "comparison" as a part of the question (group or
  level of exposure); C03 teaches "comparison group" as people without the exposure *or without the
  outcome* (the controls). Consistent, but two rows.
- **randomised trial**: C06 shortens "randomised controlled trial" to "randomised trial" and says so.
- **systematic review**: C05 speaks of "reviews that have gathered earlier studies" (Must-know),
  consistent with C03.
- **ethics committee**: used as "ethics approval" in C08 item 2; consistent.
- Build note: `build.py --subject` reports PICO, PECO, FINER, PMID, BY, PMC, XML, HHS "used before
  anything expands them". PICO appears in the C02 Must-know (Morgan) after its In plain terms; the
  expansion "PICO is population, intervention, ..." is not in the "(ABBR)" form the check
  recognises. Not a glossary matter.

## 6. Collision check with GitHub main

`prose/GLOSSARY.md` on main (sha f7f2e68) differs from this branch only by three `S36-R1-C07` rows
(Data Fiduciary, Data Principal, personal data). None of the 39 terms added here is on main. No
collision. The branch will need those three rows when it is merged or rebased; this merge did not
add them.

## 7. Build

`python3 check/parallel.py registries`: 0 problems.
`python3 check/build.py --check`: 0 blocking, 169 warnings, the same count as the `--subject` build
before the merge.
- Conductor added: protocol (C02, "the written plan of a study"). Pilot and guideline group not added: not defined in the final text.
