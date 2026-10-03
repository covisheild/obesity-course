# Draft notes · S47-R1 · batch b4 (C10, C11)

## Records written

- `check/records/S47/S47-R1-C10.yml` — The people around a decision (derivable, not quantitative).
- `check/records/S47/S47-R1-C11.yml` — Finding who decides: the tracing method (derivable, quantitative, 10 practice problems).

Both validate against the schema. Every definition quote (C10: 29, C11: 60) and every illustration
number quote was confirmed by script to be inside a `[TEXT]` run of its source file, and each number's
quote states its number (`build._states_value`). `build.py --check`: no block on either record (the
only earlier block, C11's dependency on C05, cleared once C05 was written). Remaining warnings are
long sentences inside quoted instrument text (FSS Act s.92(1), the 2018 Packaging Regulations'
preamble, COTPA s.6) and "Framework" in the treaty's own name.

## Sources: what was used, and what was not

- **Conflict of interest.** The ICMR 2017 excerpt held has only the contents line "2.8 Conflict of
  interest" and a checklist line; it carries no definition, so it is **not cited**. The concept rests on
  Ioannidis et al. 2014 (held for another book; quotes: conflicts "can also affect the design,
  analysis, and interpretation of results"; "declared or undeclared financial or other conflicts of
  interest"), written about medical research and said so in the record. The term is used in the
  glossary's existing sense (`S55-R1-C07`: what a party has when it gains from one answer).
- **Gilson 2012 Reader: not used.** Its "Policy actors" passage is interleaved column text; Walt 2008
  carries what C10 needs. So the textbook-or-primary question for the Reader does not arise.
- **Gilson & Walt 2023: not used** (it does not list the triangle's four elements). The triangle is
  named from Walt 2008 as the next level's formal version.
- **Summan et al. 2026** (CC BY) supplies C10's Indian actors (Table 1 groups, Table 3 rows, the
  "largely advisory role" finding). It is attributed throughout as one study's interviews (18, Feb–Sep
  2024, informants mostly in Delhi) and review; Table 3 is called "examples" by its authors. The media
  are left out of the actors table because the paper reports claims about coverage, not media
  organisations' own interests.
- **WHO/UNICEF industry-interference guidance**: named as the next level's, not cited (not held).
  FCTC Art. 5.3 is quoted as the one held clause on guarding policy from an industry's interests.
- **GCA s.23** is cited only for rules. For FSSAI drafts (regulations) C10 cites the 2018 Packaging
  Regulations' own preamble, to avoid asserting that s.23 governs regulations (GCA s.3 not held).

## For the conductor to decide

1. **C11 has no textbook that carries the method.** Its `textbook` references (OpenStax 16.4,
   enacted-then-implemented; 16.1, Congress leaving the detail to the EPA) carry pieces only, and the
   notes say so. The six steps are assembled from B0 `C43` and the Indian instruments. Nothing was
   relabelled.
2. **School-canteen trace (C11, illustration 1) deliberately stops at step 3** with two candidate
   deciders (Food Authority under FSS Act s.92(1); the State under Art. 162 for its own schools). No
   held source says whether an FSSAI regulation or a Chhattisgarh order on canteens exists, or how far
   "safe and wholesome food" (s.16(1)) reaches. Matching FSS Act s.2 and COTPA s.2 to Union List entry
   52 is presented as the reader's inference (the Acts do not name the entry).
3. **Tax trace** is dated "as amended up to 01/2026-CT(Rate), in force 1 May 2026"; 19/2025 is named
   as unread. The record never says the Union levies 40% (it says that claim would be wrong).
4. **COTPA** is read as enacted (2007 Amendment Act not held); the 2008 Rules from the Indian Kanoon
   print. Practice 5 (tobacco sale within 100 yards of schools) says s.6 may have been amended.
   COTPA's first preamble recital year is OCR-garbled ("19S6") and is not used; only the 1990
   resolution is cited.

## Practice set (C11): why ten

The method has six steps and three kinds of input: a bare provision, a real proposal traced forward
(or into a rule that already exists), and a finished instrument traced backward. Levels 1–3 drill the
mechanical moves (read a power-giving provision; read list entries under Art. 246; assemble the
sentence and spot the missing step). Levels 4–6: the label proposal forward (FSS Act), tobacco near
schools (finds the decision already taken, so the ask becomes enforcement), the 2018 Packaging
Regulations backward (the notification hides the Central Government's approval and the laying).
Levels 7–8: the minister named instead of the regulator; a Cabinet scheme mistaken for an Act
(NMEO-Oilseeds). Levels 9–10: a press line on the 10% oil call (no instrument at all); a report line
asking the Health Ministry for a 40% tax (wrong body, and the rate already stands).

## Figures wanted (neither section has one; `figure_note` on both)

- **C10:** an actor map round the sugary-drink tax decision: the two tax-setting bodies at the
  centre, the Health Ministry as adviser, pushers (industry associations, sugar mills and farmers,
  CSOs, researchers) and the affected (buyers and families) around them, with arrows marked inside or
  outside lobbying.
- **C11:** a chain-of-authority flow for each worked trace: Constitution → Act → rule, regulation or
  notification → enforcing officers, with the canteen trace drawn as a fork at step 3 and the treaty
  drawn beside the COTPA chain, not above it.

`check/figures/draw.py` was not run: neither record declares a figure spec, and running it would
redraw other batches' figures.

## Numbers keys

Used: `{{n:cgst_sugary_drinks_rate_pct}}`, `{{n:gst_demerit_rate_pct}}` (C11). Proposed:

- `laying_days`: value "thirty"; meaning: total days a rule or regulation is laid before each House
  of Parliament; source: `fss_act_2006` s.93 and `cotpa_2003` s.31(3); sections C07, C11. C11 uses the
  literal "thirty days" meanwhile.

## Glossary rows (proposed; same columns as `prose/GLOSSARY.md`)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| actor (around a policy decision) | a person or organisation that tries to shape a decision, or is affected by it, without holding the power to take it; a second sense beside "actor (in a food system)", `S37-R1-C01` | `S47-R1-C10` |
| civil society organisation (CSO) | a group of citizens outside government and outside business | `S47-R1-C10` |
| disclosure (of an interest) | stating an interest so that others can weigh the advice; it does not remove the interest | `S47-R1-C10` |
| inside lobbying | taking an organisation's case straight to lawmakers and officials | `S47-R1-C10` |
| interest (of an actor) | what an actor stands to gain or lose from a decision | `S47-R1-C10` |
| interest group | a formal association of people or organisations that tries to influence government decisions or public policy | `S47-R1-C10` |
| lobbying | representing an organisation's case before government to influence policy | `S47-R1-C10` |
| outside lobbying | taking the case to the public, through the media and campaigns, so that the public presses the lawmakers | `S47-R1-C10` |
| preamble | an Act's opening statement of why it was made | `S47-R1-C11` |
| public interest group | an interest group that seeks a good reaching everyone; it still has an interest | `S47-R1-C10` |
| ratify (a treaty) | the step by which a country becomes a Party, bound by the treaty | `S47-R1-C11` |
| trace (who decides) | six steps from a proposal to the body that can make it policy, the provision it would use, the process, and who else must agree | `S47-R1-C11` |
| trade association | a group of companies in one trade that act together | `S47-R1-C10` |

`conflict of interest` is already glossed (`S55-R1-C07`) and is used in that sense.

## Self-check notes

- 4a: no rate or fitted equation; the one "model" (list-entry matching) is flagged as inference.
- 4b: each headline figure says what it does not mean (Summan's finding is one study's judgement; the
  20% is the central share, not the 40% GST rate).
- Pointers: "the last section" in C10 is C09 (GST Council recommends, Central Government notifies,
  as C09 states); in C11 it is C10 (the Health Ministry's "advises" row). All named sections are in
  `concept_deps`.
- §9: no weight language beyond "obesity"; the Prime Minister's quoted lines are about oil only.
