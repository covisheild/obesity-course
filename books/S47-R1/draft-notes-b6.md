# Draft notes · S47-R1 batch b6 (C15, C16)

## Records written
- `check/records/S47/S47-R1-C15.yml`: Reading the frame in a public argument (derivable, quantitative, 10 practice problems).
- `check/records/S47/S47-R1-C16.yml`: What evidence can settle in a policy choice, and what it cannot (derivable, not quantitative).

Build: my only blocks are `concept_deps` on records other batches have not yet written (C15 needs C13, C14; C16 needs C09). Every definition quote was checked by script against the `[TEXT]` blocks of its source (41/41), and so were the quotes used in the illustrations and practice prompts (21/21). Remaining warnings are reading-grade warnings on three prompts made up mostly of quoted source text (C15 exercise 1, practice 4, practice 6). The sources' wording cannot be changed.

## Sourcing decisions
- **Textbook anchors.** Both concepts use `openstax_amgov_4e` (kind `textbook`). For C15: §8.4 framing, word choice and priming, and §16.4 "frame the issue". For C16: the §16.4 analyst and normative sentences, and the ch. 16 key term "regressive tax". The Gilson Reader was not used.
- **Indian public texts read in C15** are `pib_2163555`, `mohfw_2017_nhp`, `pib_2105618` and `fssai_eat_right_india`, all with kind `primary`. They are the texts being read, not instruments with force. The release says the notifications alone have the force of law.
- **Entman** is cited only "as reported by Koon et al.". **Fogarty & Chapman** (Australia, alcohol, newspapers) comes from Koon's Appendix row and is used as a real frame/counter-frame pair. It is bounded in `analogy_breaks_when`.
- **Summan 2026** carries three claims, each stated as Summan's report: the modelling figures (Varghese et al. 2024, *not held, not opened*; the quoted sentence names no country or base rate, and the record says so); the earmarking statement ("India does not allow for the earmarking of tax revenues", *the law behind it is not traced*); and the KII-04 quotation (one interviewee).
- **40%** is always written as the combined rate the Council recommended, via `{{n:gst_demerit_rate_pct}}`. Nothing says the Union levies it.
- **Unsourced, flagged:** in C15 practice 7, the gloss of the tagline "Sahi Bhojan. Behtar Jeevan" as "roughly, right food, better life" is my translation. No held source gives it.

## Practice-set size (C15)
Ten. The technique has five moves (four slots plus what is left out), plus the counter-frame and the reader's own frame, and ten problems meet each move at least twice. The set runs: levels 1–3 on made-up sentences (empty slots, cue words); 4–6 on real texts (NHP 2017, Mann Ki Baat, then a counter-frame built from Eat Right India, which reverses the direction); 7–8 on a mislabelled Eat Right India reading and a "neutral" note that campaigns; 9–10 on the Summan official's quote and a made-up "war on sugar" headline. The same reasoning is in `practice_note`.

## Figures
Neither section has a figure. Both have a `figure_note`. Diagrams wanted (draw.py does not draw them):
- C15: a frame and its counter-frame as two columns of five slots, with the slot where they differ most marked (e.g. Mann Ki Baat against Eat Right India: the remedy).
- C16: one argument drawn as a chain, where an evidence premise and a value premise join into a conclusion, with the value premise marked as the link evidence cannot supply.

## Glossary rows (proposed; not added)
| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| counter-frame | the problem, cause, judgement and remedy an opponent would give the same facts | `S47-R1-C15` |
| cue word | a word or short phrase that carries a frame in a few letters; a metaphor is one kind | `S47-R1-C15` |
| evidence-informed policymaking | finding and judging the evidence systematically and openly, while the decision still weighs values and other factors | `S47-R1-C16` |
| feasibility (of a policy option) | whether it can be carried out with the bodies, laws and money available | `S47-R1-C16` |
| regressive tax | a tax applied at a lower overall rate as income rises, so it takes a bigger share of a poorer household's income | `S47-R1-C16` |
| value premise | a premise that says what matters, or what ought to be done | `S47-R1-C16` |

## Numbers keys
No new key is proposed. `gst_demerit_rate_pct` is used in both records. Summan's 10%–30% and 7%–30% appear only in C16 (twice in its own text). If another section uses them, propose `summan_model_tax_range` = "10%–30%" and `summan_model_ssb_demand_fall` = "7%–30%", source `summan_2026_foodtax`.

## For other batches (to check, not edits)
- C12/C13/C14: C15 uses the slot names **problem, cause, judgement, remedy** and the frame labels "personal choice", "food environment" / "food system", "financing" and "revenue". If C12–C14 name these differently, C15 should follow them.
- C14 reads the Mann Ki Baat call as a personal-choice frame. C15 practice 5 asks the reader to fill all five lines on the same passage, and practice 6 builds its counter-frame. That is deliberate reuse, but C14 should not print a full five-line grid of the passage, or practice 5 is answered in advance.
- C17: C16's last illustration ends on "the researcher's job ... is to lay out both options". It does not teach analyst against advocate, so it should not collide with C17.
