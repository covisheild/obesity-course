# Draft notes · S47-R1 batch b1 (C01–C03)

Drafted 2026-10-02 by the b1 drafter. Records written:

- `check/records/S47/S47-R1-C01.yml` — A proposal is not a policy (derivable)
- `check/records/S47/S47-R1-C02.yml` — Four jobs around a decision (institutional)
- `check/records/S47/S47-R1-C03.yml` — Where a body's power comes from (institutional)

`python check/build.py --check`: no blocking item for C01–C03. Remaining warnings on these records
are long sentences inside quoted statute text (C02 exercise 2 prompt, C03 exercise 2 prompt), left
because they are the instruments' own words.

## Sources and support

- Every quote checked by script (`/home/claude/scratch-S47-b1/checkquotes.py`, `checktext.py`):
  all present in the held file (whitespace and case normalised), all inside `[TEXT]` runs where the
  file has them, and every illustration number's quote states its value (build's `_states_value`).
- No claim rests on an unheld source; every reference is `opened: true`.
- **Gilson 2012 Reader kind: `textbook`.** Reason: Part 1 is the editor's teaching introduction to
  the field in a WHO methods reader, closer to "canonical text for the subject" than to primary
  research. Only three short one-line clean runs are quoted. C01 also has two OpenStax textbooks,
  so the concept's textbook requirement does not depend on this label; the conductor may relabel it
  `primary` with no effect on the build.
- Off-type references: C01 cites `mohfw_2017_nhp` and `pib_1513000` (instrument) for the worked
  example only; C02 cites `openstax_amgov_4e` (textbook, US) only for "proposing is a job others do".
- C03 cites `pib_2260617` for an **absence**: the release, held whole, contains no whole-word
  "Act", "section", "statute" or "article" (checked by grep on the whole file). The record says this
  tells the reader to look at executive power and does not prove no statute applies.
- C03's DPDP stage dates (13 Nov 2026, 13 May 2027) are the reader's arithmetic from the printed
  date; the record states the 13/14 November ambiguity and that no later notification was checked.
  "As of 2 October 2026, stages (b) and (c) not in force" rests on G.S.R. 843(E) alone.
- C03's reading of arts 73/162 ("has power to make laws", not "has made laws") is presented as a
  reading of the words, plus F5's own must-know that a programme without a statute rests on an
  executive decision. No case law is held; nothing is claimed beyond the text.
- C02's court line says only what arts 32(2) and 226(1) say (directions, orders or writs) and that
  s.92 gives regulation-making to the Food Authority; how far courts go is routed to S48-R1.
- Running proposal (2), the canteen rule: no record asserts whose subject it is. C02's critique
  answer says whether canteens fall within the FSS Act is a separate question.

## Practice sets

None: C01–C03 are not quantitative (inventory). Each has a `retrieval` exercise (confidence_first)
plus three or four others; skill_ref S47-R1-K01 on the exercises that identify who would act.

## Figures

No figure is drawable honestly (no measured numbers); each record has a `figure_note`. Diagrams
wanted, for a later tool or by hand outside the build:

- C01: the four-stage cycle (agenda setting with its two parts, enactment, implementation,
  evaluation) with a feedback arrow from evaluation, and "your proposal" marked at agenda setting.
- C02: four boxes in a row (propose, advise, decide, carry out), the food-regulation bodies under
  each (anyone; Central Advisory Committee s.12(2); Food Authority + Central Government s.92(1);
  State Commissioner s.30(1) + district Designated Officer s.36(2)), with a vertical line where the
  Union ends and the State begins.
- C03: a ladder from the Constitution (art 245) to the DPDP Act s.40(1) to the DPDP Rules G.S.R.
  846(E), with a side branch "executive power, arts 73 and 162" ending at "a Cabinet decision".

## Numbers

No registry key used or proposed: none of C01–C03's numbers (dates of assent and notification,
"one year", "eighteen months") is reused by another section as far as the inventory shows. If a
later batch (C07 on rule-making, C11 tracing) reuses the DPDP dates, propose
`dpdp_commencement_date` = "13 November 2025" (dpdp_commencement_2025).

## Glossary rows (proposed; not added to prose/GLOSSARY.md)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| proposal | what someone wants a public body to do; it stays a proposal until a body with the power to decide has decided it | `S47-R1-C01` |
| public policy | what a government has decided and does about a matter of concern to some part of society, including its outcomes and a choice not to act | `S47-R1-C01` |
| programme | the work an office does to carry a policy out: staff, money, forms, visits | `S47-R1-C01` |
| four jobs (around a decision) | propose, advise, decide, carry out; often held by different bodies | `S47-R1-C02` |
| chain of authority | the ladder from the Constitution to an Act to a rule or regulation to a notification or order, each resting on the one above | `S47-R1-C03` |
| executive power | the power of a government to act by its own decision, reaching as far as the matters its legislature may make laws on (arts 73, 162) | `S47-R1-C03` |
| commencement | the date a provision of an Act comes into force, often set later by notification | `S47-R1-C03` |

`minimum support price` is used in its existing S37-R1-C09 sense; C02 glosses it in those words.

## For the conductor

- C02 points to "Book 4 on the food system" for MSP and to "a later book" for courts and labelling
  (S48-R1), without ids.
- C03 uses the DPDP Act only because it is the held, clean commencement example; it makes no
  obesity claim about it.
