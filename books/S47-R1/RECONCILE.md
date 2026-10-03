# RECONCILE · S47-R1 (Book 5) · Task 2b

Reconciler, 2 October 2026. Read: `notes-for-others-b4.md` to `-b7.md`, and the notes, "for
other batches" and "for the conductor" parts of `draft-notes-b1.md` to `-b7.md`. Each note was
checked against the records in `check/records/S47/` as they stood. Every edit is the smallest one
that settles the note. `python3 check/build.py --check`: **blocking 0** before and after; warnings
231 before, 230 after (no new warning on any S47 record).

## 1. Notes for other batches

| # | From | Section | Note | Disposition | Reason / edit |
| --- | --- | --- | --- | --- | --- |
| 1 | b4 | C02 | Expand "FSS Act" once as "(FSS)" | **applied** | C02 definition: "the Food Safety and Standards (FSS) Act, 2006". The render-time acronym scan no longer lists FSS. |
| 2 | b4 | C08 | Expand NMEO as "(NMEO)" or drop it | **applied** | C08 illustration: "the National Mission on Edible Oils (NMEO) – Oilseeds". The scan no longer lists NMEO. |
| 3 | b4 | C08 | Build blocks on "10,103 divided by 7 = 1,443.3" and a stale figure | **already done** | The line now reads "is about 1,443.3"; no block on C08. |
| 4 | b5 | C15 | Use C12's slot words (problem, cause, judgement, remedy); cite Entman "as reported by Koon et al." | **already done** | C15 uses the same four words throughout and attributes Entman the same way. No "diagnosis" or "prescription" labels. |
| 5 | b5 | C15 | Recall the Shetty / PM / Eat Right India / PIB 2163555 passages instead of introducing them fresh | **rejected (no change)** | C15 does not use Shetty. It uses the PM and Eat Right India passages as practice texts on purpose (b6). Recalling them in a practice prompt would give away the answer. Left to the compression pass. |
| 6 | b5 | C11, C15, C18, all | "Instrument" must keep Book 0's legal sense; use "measure" for a policy tool | **applied** | C11 definition step 1: a scheme is no longer listed as an instrument ("Or say none is needed: an executive decision, such as a scheme, can act without a new law"). C11 illustration 2 and practice 10: "a rate notification", not "a tax rate". C18 exercise 3: "no instrument or scheme is named". C18 exercise 4 (two places) and C17 practice 7: "measure". C01 definition: "one place in which a policy can be recorded", not "one kind of instrument" beside a policy statement. C15's "no instrument named" is already the legal sense. |
| 7 | b5 | numbers | Keys for the 10% oil call, Barry's N, Barry's 77.5, Summan's 18 | **applied in part** | Added `edible_oil_cut_pct`, `barry_n` and `summan_kii_n` (each used in two or more sections). `barry_toxic_env_important_pct` **rejected**: 77.5 appears only in C13. |
| 8 | b6 | C14 | Do not print a full five-line grid of the Mann Ki Baat passage | **already done** | C14 names the frame and its menu only. C15 practice 5 is not answered in advance. |
| 9 | b6 | C12–C14 | Tell C15 the slot and frame labels | **already done / no change** | Slots match (row 4). Frame labels: "personal choice", "revenue" and "health" are used alike. "Food-environment frame" (C13–C15, Barry) and "food-system frame" (C14, C15, Eat Right India) are not two names for one thing. Each uses its existing S37-R1 glossary sense (food environment is part of the food system). |
| 10 | b7 | C11 / C18 | Keep C11's one-sentence trace and its as-of wording consistent with C18 | **applied** | Trace sentences agree. C11's "as amended up to Notification No. 01/2026" changed to "as amended by", the wording C09 and C18 use. "Up to" implied that the unheld 19/2025 had been read. |
| 11 | b7 | C09 / C18 | Keep the vote-share working (75; 33.3; 66.7; 41.7) identical; keys for three-fourths, one-third and two-thirds | **applied** | The working was identical. Added `gst_council_majority`, `gst_union_vote_weight` and `gst_states_vote_weight` (Article 279A(9)). Also added `gst_council_majority_pct`, `gst_union_vote_pct`, `gst_states_vote_pct` and `gst_states_needed_pct` (arithmetic), because those numbers recur in both sections. Text inside quotation marks (the Article's own words) and the C09 figure spec stay literal, because `draw.py` reads raw YAML. |
| 12 | b7 | C13, C14, C15, C18 | KII-04 revenue quote appears in four sections; cut one | **deferred to the compression pass** | No contradiction: each section does a different job with the quote (name the frame, C13; the decider's frame, C14; read the slots, C15; a counter-frame in the note, C18). Cutting one is a Task 5 decision. |
| 13 | b7 | C15 / C17 | Practice 8 in both is a "neutral paragraph that campaigns" | **deferred to the compression pass** | The two test different skills (frame slots against informing vs campaigning). Vary one in Task 5 if they read alike. |
| 14 | b7 | C16 / C17 | Summan's earmarking sentence is used in both | **no change (intentional)** | Both quote the same words for different purposes, as b7 says. |
| 15 | b7 | C16 / C17 | Keep "value premise" and its gloss identical | **already done** | C16 and C17 both say "a premise that says what matters, or what ought to be done". |
| 16 | b7 | C02 / C17 | If C02 glosses "policy advocate", C17 follows it | **already done / no change** | C02 has the OpenStax sentence only as a quote and glosses nothing. The C17 row stands (see `GLOSSARY-PROPOSED.md`). |
| 17 | b7 | C14, C15 | The release's "(28% to 40%)" must not read as a 12-point rise | **applied** | C09 illustration 1 said the drinks "move from 28% to 40%" with no caveat. It now says they "go to {{n:gst_demerit_rate_pct}}%"; C09's point is recommend against impose, and it needs no 28. C15 prints "(28% to 40%)" only as a quoted list heading and draws nothing from it: no change. C14 does not print 28. C18 carries the cess explanation. |

## 2. Draft-notes parts addressed to others or to the conductor

| # | From | Note | Disposition | Reason |
| --- | --- | --- | --- | --- |
| 18 | b1 | Gilson 2012 Reader entered as `textbook` in C01 | **left as drafted (conductor ruling 2)** | C01 also cites `openstax_amgov_4e` and `openstax_intro_polisci_1_2` as `textbook`, so the derivable concept's textbook requirement does not rest on the Reader's label. Not relabelled. |
| 19 | b1 | Key `dpdp_commencement_date` if another section reuses the DPDP dates | **rejected** | The DPDP dates appear only in C03. |
| 20 | b2 | `plcp_2014` and `rajyasabha_2005_legislative` entered as `guideline` | **accepted (conductor ruling 3)** | No change. |
| 21 | b2 | "15th Lok Sabha" equated with PRS's "current term of Parliament" (C06) | **left for the auditor (Task 3)** | A claim-support question, not a cross-batch one. |
| 22 | b3 | If C01 teaches "scheme", drop b3's row | **rejected** | C01 teaches "programme", C08 "scheme". Both rows are kept and the glosses agree. |
| 23 | b3 | Auditor items 1–9 (GCA s.23 reach, laying, e-Gazette, Poshan 2.0 approver, NHP excerpt, SGST, weighted voting, canteen) | **left for the auditor** | Checked for consistency only: the canteen, SGST and weighted-voting statements match C04, C09, C11 and C18. |
| 24 | b4 | C11 has no textbook that carries the tracing method | **for the conductor** | Not relabelled (brief: "never relabel"). Logged here. |
| 25 | b4 | Key `laying_days` (C07, C11) | **applied** | Added `laying_days` = "thirty" (FSS Act s.93; COTPA s.31(3)). Also added `packaging_draft_objection_days` = "thirty" (2018 Packaging Regulations; C07 and C11), so the book's "two different thirties" (C07 must-know) are two keys, apart from `plcp_comment_days`. C07's must-know was reworded so that neither thirty opens a sentence. |
| 26 | b5 | Koon 2016 as `primary`; Barry figures within short quotation | **for the conductor** | No change. |
| 27 | b6 | C15 practice 7: the English gloss "roughly, right food, better life" of "Sahi Bhojan. Behtar Jeevan" is unsourced | **applied (conductor ruling 1)** | The translation was removed. The Hindi tagline stays: `fssai_eat_right_india` carries it ("The tagline 'Sahi Bhojan. Behtar Jeevan'"). The answer now says only that the tagline "is written to the person who eats". |
| 28 | b6 | C16's last illustration ("lay out both options") should not collide with C17 | **no change** | It does not teach analyst against advocate. It agrees with C17's informing role. |
| 29 | b6, b7 | Keys `summan_model_tax_range`, `summan_model_ssb_demand_fall` | **applied** | Used in C16, C17 and C18. Keys `summan_model_tax_range` = "10% to 30%" and `summan_model_demand_fall` = "7% to 30%". The review writes "10%–30%" and "7%–30%", and the quotes keep that form. C17's made-up "cuts demand by 30%" stays literal. |
| 30 | b7 | Keys `gst_drinks_prior_rate_pct` (28) and `ssb_compensation_cess_pct` (12) | **rejected** | After row 17, 28 is written only in C18 (C15's is inside a quoted heading), and the 12% cess appears only in C18. |
| 31 | b7 | C18 figure table keeps literal 28/40 | **no change** | `draw.py` reads raw YAML. Figure specs stay literal throughout. |

## 3. Cross-section checks

**Numbers.** Fifteen keys added to `numbers.yml` (rows 7, 11, 25, 29). Literal reused numbers
outside quotation marks were converted to keys:

- `gst_demerit_rate_pct` and `cgst_sugary_drinks_rate_pct`: C09's exercises and retrieval answer,
  and C18's line-4 working.
- `plcp_comment_days`: C06's definition, exercises and retrieval answer.

The rule followed: words inside quotation marks, `quote` fields, illustration `numbers[].value` and
`unit` fields, and figure specs stay literal. C14's "a special de-merit rate of
{{n:gst_demerit_rate_pct}}%" sits inside a quotation and was left as drafted; it renders
identically. One YAML fault was introduced and fixed: an answer beginning with `{{` parses as a
mapping, so C09's retrieval answer now opens "The rate is …".

**GST case.** All sections say:

- the Council recommends; the 40% is the combined rate the release gives;
- the Central Government notifies central tax at 20% under s.9(1), Schedule III of 9/2025, as
  amended by 01/2026, in force 1 May 2026;
- 19/2025 is not held;
- the States' share is unread.

C09 and C18 also refute "the Union levies 40%". Two wordings were aligned:

- C10's Summan finding was written as "the Ministry of Finance and the GST Council set tax design
  and rates". It now quotes Summan's "determine tax design and rates" and adds the book's
  recommend/notify terms.
- C17's spoken answer: "what the GST Council decided" became "recommended".

**School canteen.** No section names a deciding body or asserts whose subject it is:

- C04 lists the entries;
- C09 says "not yet traced";
- C11 stops at the fork;
- C18 says "has not been traced".

C05's "much of a canteen rule could be the State's" is hedged.

**PLCP.** C06 and C07 agree: thirty days minimum; a Committee of Secretaries decision; a policy,
not a law; departments may skip it and record why; no compliance record kept (2022).

**Who decides.** The wordings match across sections:

- Food regulations: the Food Authority under s.92(1), with the Central Government's previous
  approval and after previous publication (C02, C07, C11).
- Food safety in a State: the State's Commissioner and the district Designated Officer (C02).

**Terms.** Agenda setting had two senses: a policy-cycle stage in C01 and a media sense in C12.
C12's definition now ties it to C01's stage. C10's CSO gloss was aligned to the existing glossary
row. The glossary list is in `GLOSSARY-PROPOSED.md`.

**Symbols.** A bare "N =" sat unexplained in C13's retrieval answer. It now reads "{{n:barry_n}}
surveyed". R-squared is glossed where C14 uses it.

## 4. Left for others

- **Render-time acronym scan.** The scan (`build.py` at render, not `--check`) still lists
  FSSAI, PIB, PRS, PLCP, KII, FCTC, PM, CBIC, DFPD and others. Most sit in quoted text or
  reference lists, or are expanded only after first use: for example, C02 exercise 3 uses "FSSAI"
  one sentence before its expansion. This is for the fixer (Task 4); no note asked for it.
- **Existing sentence-length and reading-grade warnings** on prompts that quote instruments
  (C02, C03, C07, C08, C11, C15, C17). Not touched.
