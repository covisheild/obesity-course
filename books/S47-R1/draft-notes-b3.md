# Draft notes · batch b3 (S47-R1-C07, C08, C09)

## Records written

- `check/records/S47/S47-R1-C07.yml` · How a rule or regulation is made, and where the public gets in
- `check/records/S47/S47-R1-C08.yml` · Schemes and budgets: policy without a statute
- `check/records/S47/S47-R1-C09.yml` · When no single body decides

All three are institutional, `quantitative: false` (no drill set; the inventory marks none of them
quantitative). Each has a retrieval exercise, `retrieval_items`, a figure, `review.as_of`
2026-10-02, and status `drafted`. `python check/build.py --check`: blocking 0. Two warnings remain
on my records, both on prompts that quote an instrument verbatim (C07 exercise 2, FSS Act s.94(1);
C08 exercise 2, the NMEO-Oilseeds release); I left the source's words as they stand.

Every quote was confirmed by script against the file in `sources/` (whitespace and case
normalised, as the build does), and every number entry passes the build's "quote states the
number" test. All arithmetic was recomputed in Python (dates: 19 Mar to 2 Apr 2018 = 14 days, 19
Mar to 24 Dec 2018 = 280 days; 10,103 / 7 = 1,443.29; 3/4 = 0.75, 100/3 = 33.3, 200/3 = 66.7,
75 - 33.3 = 41.7).

## Things the auditor should look at

1. **C07, General Clauses Act s.23 and regulations.** Section 23 is written for "rules or
   bye-laws". The Act's definition of "rule" (s.3), which would say whether s.23 reaches an FSSAI
   regulation, is not held. The record says s.23 applies to rules, says plainly that the
   definition is not held, and uses the 2018 Packaging Regulations to show FSSAI followed the same
   steps under FSS Act s.92(1). It never states that s.23 governs FSSAI regulations. If the
   conductor wants that stated, `general_clauses_act_1897` needs s.3(51) added.
2. **C07, laying.** Written as the text has it: laid "as soon as may be after it is made"; the Houses
   may modify or annul; things done stay valid. No claim that laying is a condition of validity.
3. **C07, e-Gazette.** The e-Gazette site's search was never opened (terms unreadable at intake), so
   the record teaches finding the deadline inside a notification, not searching the site. It names
   the Gazette Part only for the two notices held (Part III s.4 for the FSSAI regulation).
4. **C07, two "section 23"s.** The packaging regulation's enacting words cite FSS Act s.23
   (packaging and labelling), which the record flags as different from General Clauses Act s.23.
5. **C08, Poshan 2.0 approver.** The guidelines say the scheme "has been approved" for the 15th
   Finance Commission period and do not name the approving body; the record says so. No held text
   says whether it continued after March 2026.
6. **C08, NHP 2017.** Cabinet approval rests on `pib_1513000`, not on the policy text. The held copy
   is an excerpt (ss.1-3.2 and 26-28); the record says ss.3.3-25 were not read.
7. **C09, the States' side of GST.** Nothing is said about the SGST notifications beyond Art. 279A
   (recommendations go "to the Union and the States") and the release's 40% as the GST rate. The
   record never says the Union levies 40%, and never says how the 40% splits.
8. **C09, weighted voting.** The record does not work out how many States a decision needs:
   Art. 279A(9) does not say how the States' two-thirds is divided, and the Council's procedure
   (cl. 8) is not held.
9. **C09, the canteen.** Left as "not yet traced: it touches food and it touches schools", per the
   brief. No body is named.

Nothing is unsourced. No reference is `opened: false`.

## Reference kinds

All references are `instrument` (Acts, the Constitution, Gazette notifications, PIB releases, the
2022 Poshan 2.0 guidelines, the NHP 2017 text, the Allocation of Business Rules, the 2014
consultation policy), matching how the exemplars cite PIB releases. Copyright-restricted
`goi_aob_rules_1961` is quoted for two short item names only (C09).

## Practice-set size

None: C07-C09 are not quantitative in the inventory, so no `practice[]`.

## Figures (all drawn with `python check/figures/draw.py --book S47-R1`; looked at as PNGs)

- `s47-r1-c07-packaging-path.png`: bar chart, days in the 2018 Packaging Regulations' path (14,
  30, 280). The diagram I would have preferred, a flow from draft to notice date to objections to
  approval to final notification to laying, is not something the tool draws.
- `s47-r1-c08-poshan-shares.png`: grouped bars from the record's own table, the Centre's share by
  component and category (60/25/50, 90/90/90, 100/100/100). y-axis runs to 150 so the legend
  clears the bars.
- `s47-r1-c09-gst-votes.png`: two bars (33.3, 66.7) under a reference line at 75 (Art. 279A(9)).
  Wanted but not drawable: a diagram of the order of acts (Council recommends, then the
  Central Government notifies, then the notification is amended).

## Numbers keys

Used: `{{n:plcp_comment_days}}` (C07), `{{n:gst_demerit_rate_pct}}` and
`{{n:cgst_sugary_drinks_rate_pct}}` (C09). No new keys proposed. The 30 days for objections in the
2018 packaging draft and the 30 days of laying under FSS Act s.93 are written as literals on
purpose: they are not the consultation policy's thirty and must not share its key.

## Glossary rows (proposed; same columns as `prose/GLOSSARY.md`)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| centrally sponsored scheme | a scheme the States carry out with money from both the Union and the State, shared by a stated ratio | `S47-R1-C08` |
| previous publication | a draft must be published first, with a date, before the final rule or regulation is made | `S47-R1-C07` |
| scheme | a programme the executive runs, with a name, a period, an amount of money and guidelines saying how it works; many rest on no Act of their own | `S47-R1-C08` |
| subordinate legislation | rules and regulations together: instruments made under an Act by a body the Act names | `S47-R1-C07` |
| weighted votes (GST Council) | votes counted by weight, not by head: the Centre's weighs one-third of the votes cast and all the States' together two-thirds; a decision needs three-fourths | `S47-R1-C09` |

If C01 already teaches "scheme" (it teaches "programme"), keep C01's row and drop mine.
