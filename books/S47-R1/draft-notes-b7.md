# Draft notes · S47-R1 batch b7 (C17, C18)

## Records written
- `check/records/S47/S47-R1-C17.yml`: Informing policy and campaigning for it (derivable, quantitative, 10 practice problems, 2 illustrations, 1 figure).
- `check/records/S47/S47-R1-C18.yml`: A one-page note on one Indian proposal (derivable, `journey: true`, not quantitative, 2 illustrations, 5 exercises including the rung's `build`, 1 figure).

Build (filtered check, last run 2 Oct 2026): blocking 0 for both records; whole-tree blocking 0 at that moment. The warnings left are sentence-length and reading-grade warnings on C17 practice 4 and 5 prompts. Those prompts are mostly quoted source text (PIB 2163555, Summan 2026), and the sources' wording cannot be changed. Every definition quote and illustration-number quote was checked by script against its source file (C17 22/22, C18 40/40). Each number quote states its value (build's `_numbers_stated`). The real sentences quoted in prompts and prose (PIB 2163555 ×4, PIB 2105618 ×3, Summan ×4) were checked the same way. Arithmetic lines (C17: 1 plus 4 = 5, 6 plus 0 = 6; C18: 40 minus 28 = 12, 28 plus 12 = 40, 3 divided by 4 = 0.75, 75 minus 33.3 = 41.7) were recomputed.

## Sourcing decisions
- **Textbook anchor** for both: `openstax_amgov_4e` §16.4 (analysts, advocates; Key Terms). It is a US text, used for the distinction only. Journal papers (Oxman 2009, Oliver & Cairney 2019, Cairney & Oliver 2017, Summan 2026) are `primary`. The Constitution, CGST Act s.9, Notifications 9/2025 and 01/2026, and PIB releases are `instrument` (as in C11). They are off-type on a derivable concept, and each carries its quote. The Gilson Reader was not used.
- **Pielke not held.** C17 names only "honest broker" against "issue advocate", as Oliver & Cairney 2019 state it. It notes that Cairney & Oliver 2017 use "honest broker" in a second sense (one who works with stakeholders to define problems). The four roles are not taught. The INVENTORY row asks for them; the brief overrides it.
- **C17's four marks** are each sourced to Oxman 2009: selective use and spurious uncertainty; advocating without the limits of the evidence; evidence is not a conclusion; conflicts of interest. OpenStax adds "understate costs and overstate benefits" and "known bias". The grouping into four marks is this book's own, and the record does not attribute the list to any source.
- **40% / 20%.** The 40% is always "the combined rate the release gives" (`{{n:gst_demerit_rate_pct}}`). The central tax is 20 per cent (`{{n:cgst_sugary_drinks_rate_pct}}`), under s.9(1) and Schedule III of 9/2025. C18 does not say the Union levies 40%.
- **Dating.** The rate is dated "as amended by 01/2026-CT(Rate), in force 1 May 2026". 01/2026 re-states Schedule III S. Nos. 2–3 and does not touch S. No. 1. **19/2025 (31 Dec 2025) is not held.** So whether it touched S. No. 1 is unchecked, and C18's note says so in its own text.
- **State share.** The SGST Acts and Chhattisgarh's notification are not held. C18 says only that each State notifies its own tax under its own GST Act (on Art. 246A(1) and Art. 279A(4)), and names the State notification as unchecked.
- **28% + 12% cess.** The claim that the 2025 change did not raise the combined rate on sugar-sweetened drinks rests on Summan 2026, which says the reform "consolidated the earlier 28% rate and 12% compensation cess into a single rate" (citing Ministry of Finance 2026, not held). The claim is kept to those drinks only. The record says the cess on "other non-alcoholic beverages" (18%→40%) is unknown.
- **Weighted votes (C18 line 6).** The arithmetic is aligned with C09's (percentages, 75 − 33.3 = 41.7). Like C09, C18 does not work out how many States a change needs.
- **Summan's modelled figure** (10–30% extra tax → 7–30% fall in demand) is from Varghese et al. 2024. That paper is **not held or opened**. Both records say it is a model reported by the review, not a change measured in India.
- **Kerala 2016** is not mentioned (not held).
- **Unsourced, flagged:** none as fact. Everything made up is said to be made up: the department's draft paragraph, the head of department's newspaper statement and the three experts in C17; the first-draft note in C18; the made-up letters, memos and report lines in the exercises.

## Practice-set size (C17)
Ten. The technique has four moves: sort a sentence, name the mark, rewrite into informing, and decide a whole document's job. Each move gets a mechanical problem (levels 1–3). Real Indian texts get three applied problems (4: PIB 2163555; 5: Summan 2026; 6: Mann Ki Baat). Level 6 adds the move "open campaigning is not a fault". There are two diagnostics (7: a number-and-method sentence that concludes a value; 8: a "neutral" paragraph that campaigns without "should") and two transfers (9: the PM's "one in eight" line as a figure for an informing note; 10: a report line to classify, rewrite and bound). The INVENTORY suggested 5–6. Ten reach both ends of the ladder and meet each move at least twice. No `practice_note` is included, since the count is inside 3–18.

## Figures
- C17: `s47-r1-c17-draft-and-rewrite.png`, a bar chart of sentence counts by job in the made-up draft against the rewrite (1/4 against 6/0). Checks: totals 5 and 6.
- C18: `s47-r1-c18-drink-rates.png`, the six heading-2202 rows of PIB 2163555 Annexure-I, before and after (28→40, 18→40, 28→40, 12→5, 12→5, 18→5). The caption says the before rates exclude the cess. Labels are short forms, explained in the prose. Values were checked against the PIB rows. I looked at both PNGs.
- `draw.py --book S47-R1` redraws every S47 figure, so other batches' PNGs were rewritten too (their specs, unchanged).
- Diagram wanted (draw.py cannot draw it): for C18, the path from Council recommendation (3 Sep 2025) to central notification 9/2025 (17 Sep, in force 22 Sep 2025) to amendment 01/2026 (1 May 2026), with a parallel, unread State branch.

## Glossary rows (proposed; not added)
| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| campaigning (for policy), advocacy | starting from what ought to be done and arguing for one option | `S47-R1-C17` |
| honest broker | (1) in Oliver and Cairney 2019, a researcher who passes on evidence honestly, clearly and in time, and stays neutral; (2) in Cairney and Oliver 2017, one who works with stakeholders to define policy problems | `S47-R1-C17` |
| informing (policy) | setting out the options, what the evidence says about each and how sure it is, without choosing | `S47-R1-C17` |
| issue advocate | a researcher who recommends specific policy options from their research | `S47-R1-C17` |
| policy advocate | someone who works to propose or keep a policy, starting from what ought to be done | `S47-R1-C17` (C02 uses the textbook's definition first; if C02 glosses it, C02 owns the row) |
| policy analyst | someone who sets out all the choices open to a decider and judges the effect of each | `S47-R1-C17` |
| cess | an extra tax charged alongside the main one | `S47-R1-C18` |

## Numbers keys proposed (literal values used meanwhile)
- `summan_model_tax_range` = "10%–30%" and `summan_model_ssb_demand_fall` = "7%–30%", source `summan_2026_foodtax` (Varghese 2024 via Summan). Used in C16, C17 and C18 (b6 proposed the same keys).
- `gst_drinks_prior_rate_pct` = "28" and `ssb_compensation_cess_pct` = "12", source `pib_2163555` (28) and `summan_2026_foodtax` (28, 12). Used in C18 and, judging by their quotes, C14/C15 (the "(28% to 40%)" list).
- `gst_council_majority` = "three-fourths", `gst_union_vote_weight` = "one-third", `gst_states_vote_weight` = "two-thirds", source `constitution` Art. 279A(9). Used in C09 and C18.
- Note: the C18 figure table keeps literal 28/40 values, because `draw.py` reads the raw YAML, where `{{n:}}` is not substituted.

## Self-check notes
- 4a/4b: every headline number says what it does not mean. 40% is not the Union's rate. "28% to 40%" is not a rise. 7–30% is a model, of demand and not weight. 0.2 servings a week is reported intake for adults in 2018, and says nothing about children or the district. The 18 interviews show the arguments exist, not how widely they are held.
- No "recall". Pointers: C17's "the section before this one" is C16. C18 names sections by title, and all are in `concept_deps` (C01–C17).
- §9 language checked: "people with obesity" form throughout. A PIB quote line that uses "obese" (pib_2105618, a guest's words) was deliberately not used.
