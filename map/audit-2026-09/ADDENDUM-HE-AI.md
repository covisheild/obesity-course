# Addendum, 30 Sep 2026: health economics and AI/ML

Harsh asked whether the curriculum held enough health economics and machine learning / AI, and then
asked for what was missing to be added. This file records the gap check, the plan, and the 20 entries
appended to `map/AMENDMENTS-v3.1.yml` (ids below). Sources opened for them are in
`map/audit-2026-09/SOURCES-HE-AI.md`. The map stays frozen. No book id, position or count changes.

## 1. What the map already had

**Health economics** is strong. Part 12 has S40 (demand, elasticity, externality; Advanced),
S41 (fiscal instruments; Advanced), S42 (burden of disease, economic evaluation, Markov and
microsimulation, extended cost-effectiveness, value of information; Advanced) and S43 (financing, HTA,
PM-JAY, NLEM; Intermediate). S51 (health-system financing) and S14 (policy evaluation) add to it. The
September audit marked NMC's "principles of Health Economics" and ASPHER's "health economic evaluation"
as covered.

**ML/AI** is capped on purpose. S07 (prediction modelling and ML) stops at Intermediate. The front
matter names machine learning as a place where "going deeper is … interesting and wrong". ML also
appears in S12-R3 (double machine learning), S09/S31 (wearables), S38 (scraping), S34-R3 (apps),
S52-R3 (AI tools: "check everything") and S61 (deep learning is routed).

## 2. Gaps found (map text search, then read in context)

| Gap | What was missing | Evidence it matters |
|---|---|---|
| HE1 | Budget impact analysis: 0 hits. The audit's own standard 11.3 lists it. | India has national BIA guidelines (Prinja 2021). US analyses find anti-obesity drugs judged cost-effective can still cost more at uptake than payers can fund (Pearson 2025). S43-R2 asks how generic semaglutide reaches scale. |
| HE2 | Cost-benefit analysis and willingness to pay: 0 hits. The Indian threshold is not named. | The Indian reference case says no formally recognised threshold exists (Sharma 2023). Chugh 2026 (e-pub 2025) proposes one. |
| HE3 | Stated preference / discrete choice experiments: 0 hits. | Uptake is a main uncertainty in budget impact and in microsimulation. Indian NCD DCEs exist (Leslie 2023). |
| AI1 | Generative AI and LLMs: 0 hits for "language model", "hallucin" and "chatbot". | S07 treats AI as tabular prediction only. |
| AI2 | TRIPOD only (S07-R2 O3, S56-R2 O3). TRIPOD+AI, TRIPOD-LLM, PROBAST(+AI), CONSORT-AI and SPIRIT-AI are absent. | TRIPOD+AI supersedes TRIPOD 2015. |
| AI3 | Fairness within a population is absent. Only transfer between populations is covered. | Label bias (Obermeyer 2019). |
| AI4 | AI and image-based dietary assessment are absent from the Expert measurement spine. | Serious error in reviews (Ho 2020; Cofre 2025). No Indian-food validation was found. |
| AI5 | Conversational agents and generative-AI coaching are absent. | Meta-analytic evidence is mostly low quality (Singh 2023; Noh 2023). |
| AI6 | AI in evidence synthesis and disclosure duties are absent. | Joint Cochrane–Campbell–JBI–CEE statement (2025); PRISMA 2020; ICMJE. |
| AI7 | Indian governance of AI health tools is absent. | CDSCO guidance on medical device software under MDR-2017 (non-binding; MDR-2017 binds); ICMR AI guidelines (2023). |
| AI8 | Platform algorithms in the digital food environment are absent. | Gupta 2025 scoping review. |
| AI9 | Ethics of AI tools is absent. | Image-generator weight bias (Saumure 2025; Wiegand 2025). |

## 3. Decisions in the plan

- **No cap raised, no new subject, no new book.** S07 stays at Intermediate. The additions are what a
  public-health obesity expert must judge and govern, not what a data scientist builds. That keeps
  the front matter's rule.
- **Fewest lines.** Where an existing line was nearly right it is revised, not duplicated: S07-R2 O3,
  S09-R2 O4, S34-R3 O4, S42-R2 O3, S52-R3 O5, and S56-R2 O3, O4 and O5.
- **No volatile fact in a line.** The threshold figure, CDSCO dates and RAISE's version are all read
  at intake (`verify_at_intake: true`).
- **Level fit and chain rule.** R1 lines only recognise. S42-R1-A01 gives the R2 budget-impact lines
  and the R3 DCE line their anchor. S09-R2's revision anchors S09-R3-A01.

## 4. Entries (20: 12 new lines, 8 revisions; 14 rungs)

| Rung | Id | Kind | Gap |
|---|---|---|---|
| S42-R1 | A01 | concept | HE1, HE2 |
| S42-R2 | A01 | concept | HE1 |
| S42-R2 | A02 | skill | HE1 |
| S42-R2 | A03 | revise (O3, line 3149) | HE2 |
| S42-R3 | A01 | concept | HE3 |
| S07-R1 | A01 | concept | AI1 |
| S07-R2 | A01 | revise (O3, line 613) | AI2 |
| S07-R2 | A02 | concept | AI3 |
| S07-R2 | A03 | skill | AI1–AI3 |
| S09-R2 | A01 | revise (O4, line 749) | AI4 |
| S09-R3 | A01 | concept | AI4 |
| S34-R3 | A05 | revise (O4, line 2616) | AI5 |
| S06-R2 | A01 | concept | AI6 |
| S48-R2 | A05 | concept | AI7 |
| S52-R3 | A01 | revise (O5, line 3816) | AI6 |
| S38-R3 | A03 | concept | AI8 |
| S60-R2 | A01 | concept | AI9 |
| S56-R2 | A01 | revise (O3, line 4100) | AI2 |
| S56-R2 | A02 | revise (O4, line 4101) | AI7 |
| S56-R2 | A03 | revise (O5, line 4102) | AI6 |

**Which books pick them up.** None of these rungs is built. An R2 or R3 change also reaches the book
one rung below it, as that book's bridge. In book order: S48-R1 (#16, bridge to S48-R2), S06-R1 (#29),
S07-R1 (#30), S09-R1 (#38, bridge to S09-R2), S56-R1 (#52, bridge to S56-R2), S42-R1 (#57), S60-R1
(#60), S52-R2 (#67, bridge to S52-R3), S34-R2 (#97, bridge to S34-R3) and S38-R2 (#109, bridge to
S38-R3), then the rungs themselves. Book #6 (S52-R1) is not affected.

## 4a. Verification

An independent verifier re-opened the sources and checked level, chain, duplicates and volatile facts.
It found 17 defects: 3 errors, 7 should-fix, 7 minor. All were applied. The main ones: India's
national BIA guidelines (Prinja 2021) had been missed; "most Indian meals" was unsourced; the book list
was wrong; the CDSCO line stated a legal status from a non-binding guidance; the image-bias line
misread Wiegand 2025; S56-R2 still taught the superseded TRIPOD; and ICMJE authorship and the ICMR
guidelines belonged at S56-R2. That added three S56-R2 revisions. A second verifier confirmed 15 of the 17
fixes in full and 2 in the YAML only (the addendum's HE2 and HE3 cells, since corrected). It found 4
minor defects, all applied. Both reports are in `map/audit-2026-09/VERIFICATION-HE-AI.md`.

## 5. Not added, with reasons

- A new ML subject, or raising S07 above Intermediate. The front matter's cap stands.
- An S61 routing line for health-AI engineering. S61 already routes "deep learning and cloud
  infrastructure".
- Labour and productivity economics beyond reading level. S40-R2 and S61 already hold it.
- A claim that LLMs write weight-stigmatising text. No peer-reviewed evidence was found; one study
  (Front Public Health 2026) found no stigmatising language but did find demographic attribution bias.
