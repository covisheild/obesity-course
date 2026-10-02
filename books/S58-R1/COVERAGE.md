# S58-R1 coverage against outside standards

Written at Task 1 (PIPELINE.md), after the inventory, on 2026-10-02. The map was audited once as a whole; this checks the rung at its own level against three standards opened now: an Indian curriculum (NMC, MD Community Medicine), a journal-editors' standard (ICMJE), and the contents of a standard visualisation textbook (Wilke). Rougier et al. 2014 and Mensh & Kording 2017 were also opened (https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833 and https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619); they are sources for the inventory, so they are not used as standards here, to keep the check from being circular. Only items a rung-1 book on writing and figures should hold, or should route, are listed.

**URLs opened.**
- NMC, *Guidelines for Competency Based Postgraduate Training Programme for MD in Community Medicine* (2022): opened as the text reproduced by Medical Dialogues, https://medicaldialogues.in/medical-courses/curriculum/nmc-guidelines-for-competency-based-training-programme-for-md-community-medicine-98528. The NMC's own PDF was not located on nmc.org.in in this session; a copy from nmc.org.in should replace this before any line here is cited.
- ICMJE Recommendations, Preparing a Manuscript for Submission to a Medical Journal: https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html
- Wilke CO, *Fundamentals of Data Visualization*, table of contents and chapter 17: https://clauswilke.com/dataviz/ and https://clauswilke.com/dataviz/proportional-ink.html

| Standard (URL opened) | Item | Here | Where |
| --- | --- | --- | --- |
| NMC MD Community Medicine (Medical Dialogues copy) | "training in scientific communication and medical writing" (programme goals) | covered | C01–C13 |
| NMC MD Community Medicine | "Do data collection, compilation, tabular and graphical presentation" | covered (graphical); gap 1 (tabular, as a made object) accepted 2 Oct 2026 → S58-R1-A01 | C14–C20, C22; C21 |
| NMC MD Community Medicine | "Develop communication skills to word reports and professional opinion" | covered (reports); deferred (professional opinion to a policy audience) | C02, C04, C07; S58-R2 (P5) |
| NMC MD Community Medicine | One poster presentation, one paper read at a conference, one research paper published, accepted or sent, before the examination | deferred (paper read aloud); gap 2 (poster) accepted 2 Oct 2026 → S58-R2-A01; gap 3 (choosing a journal, submitting, answering reviewers) accepted 2 Oct 2026 → S58-R2-A02 | S58-R2 (P3 as revised, R3, S58-R2-A02) |
| NMC MD Community Medicine | Thesis submitted six months before the examination | covered in part: the build target rewrites one section, which may be a thesis chapter | C13, C23 |
| NMC MD Community Medicine | Journal club: critical appreciation of research articles | deferred | S58-R2 (read, critique); S56 |
| NMC MD Community Medicine | Health education messages, IEC material, behaviour change communication | deferred | S58-R3 (public communication, `S58-R3-A01`, `A02`) |
| ICMJE §A.1 | IMRAD structure, and why it mirrors the process of discovery; other article types differ | covered | C01 |
| ICMJE §A.2 | Reporting guidelines (CONSORT, STROBE, PRISMA, STARD; SAGER) | deferred | S56-R1 ("reporting guidelines exist and are checklists for design") |
| ICMJE §A.3.a | Title: a distilled description; study design in the title; short title | covered | C03 |
| ICMJE §A.3.a | Author information, ORCID, disclaimers, sources of support, disclosure of relationships | deferred | S56 (authorship and ICMJE criteria) |
| ICMJE §A.3.b | Structured abstract: purpose, procedures, main findings with effect sizes, conclusions; abstract consistent with text | covered | C03 |
| ICMJE §A.3.c | Introduction: context, then the specific purpose or hypothesis; no results in it | covered | C04 |
| ICMJE §A.3.d | Methods detailed enough to judge and repeat; statistical methods | covered (purpose only); deferred (content) | C04; S56, S02-S04 |
| ICMJE §A.3.e | Results in logical sequence, main findings first; do not repeat tables in text | covered | C02, C04, C14 |
| ICMJE §A.3.e | Give absolute numbers alongside percentages | covered | C09 |
| ICMJE §A.3.e | Avoid nontechnical uses of "random", "normal", "significant", "correlations", "sample" | covered | C08 |
| ICMJE §A.3.f | Discussion: begin with the main findings, then mechanisms, context, limitations, implications | covered | C04 |
| ICMJE §A.3.g | References: original sources, numbered in order of citation (Vancouver), no predatory journals | gap 4 accepted 2 Oct 2026 → S58-R1-A02 | C05 (Book 0 F3 teaches checking a reference, not citing one) |
| ICMJE §A.3.h | Tables: self-explanatory title, short column headings, footnotes, measures of variation named | gap 1 accepted 2 Oct 2026 → S58-R1-A01 | C21 |
| ICMJE §A.3.i | Figures: legible when reduced, self-explanatory, explanations in the legend; permission for reused figures | covered (legibility, legend); gap 5 (permission and copyright for reused figures) accepted 2 Oct 2026 → S58-R2-A03 | C20, C22; S58-R2 |
| ICMJE §A.3.i | Image integrity: same lighting for before-and-after images, original blots deposited | deferred | S56 (research integrity); not a rung-1 plot skill |
| ICMJE §A.3.j | Units of measurement: metric, SI alongside local units | covered | C09 (Book 0 B1 carries SI) |
| ICMJE §A.3.k | Standard abbreviations only; none in the title; spelled out at first use | covered | C08 |
| Wilke ch. 2 | Aesthetics and types of data; scales map data to aesthetics | covered | C15 (Book 0 D4 carries types of variable) |
| Wilke ch. 3 | Coordinate systems and axes; nonlinear (log) axes | covered | C17 (Book 0 A7 and C5) |
| Wilke ch. 4, 19 | Colour scales; pitfalls; designing for colour-vision deficiency | covered | C19 |
| Wilke ch. 5-6 | Directory of visualisations; visualising amounts (bars, dot plots) | covered | C15 |
| Wilke ch. 7-9 | Visualising distributions (histograms, box plots, many distributions) | covered (recognise and choose); deferred (density, ECDF, q-q) | C16; S58-R2 (P2), S03 |
| Wilke ch. 10-11 | Proportions and nested proportions (pie, stacked bars, mosaic) | covered (pie against bars); deferred (nested) | C15; S58-R2 (P2) |
| Wilke ch. 12-14 | Associations (scatter), time series, trends and smoothing | covered (choose the mark); deferred (smoothing, fitted trends) | C15; S58-R2 (P2), S04 |
| Wilke ch. 15 | Geospatial data, choropleth maps, cartograms | deferred | S58-R2 (P2, "appropriate marks for data shape"); S54 for Indian district data |
| Wilke ch. 16 | Visualising uncertainty; frequency framing | deferred | S58-R2 (P4) |
| Wilke ch. 17 | The principle of proportional ink; bars from zero; log-scale bars from 1 | covered | C17 |
| Wilke ch. 18 | Overlapping points: transparency, jitter, 2-D histograms | covered (jitter for small n, in passing); deferred (the rest) | C16; S58-R2 |
| Wilke ch. 20 | Redundant coding; figures without legends | covered | C18, C20 |
| Wilke ch. 21 | Multi-panel figures, small multiples | deferred | S58-R2 (P2, R2) |
| Wilke ch. 22, 24 | Titles, captions, axis and legend titles; larger axis labels | covered | C20 |
| Wilke ch. 22.3 | Tables | gap 1 accepted 2 Oct 2026 → S58-R1-A01 | C21 |
| Wilke ch. 23, 25, 26 | Balance data and context; background grids; avoid line drawings; no 3-D | covered | C18 |
| Wilke ch. 27 | Image file formats: bitmap against vector, compression | covered | C22 |
| Wilke ch. 28 | Choosing software; reproducibility | covered (any tool); deferred (code) | C22; S52 |
| Wilke ch. 29 | Telling a story and making a point; one figure for the busy reader | covered | C14 |

**Gaps proposed to Harsh** (in the source-gate message; never added without his word). **All five accepted by Harsh on 2 Oct 2026** and written to `map/AMENDMENTS-v3.1.yml` (block "ADDITION of 2 Oct 2026", drafter S58COV); placement is his:

1. **Making a table.** NMC asks for "tabular and graphical presentation"; ICMJE §A.3.h and Wilke §22.3 set rules for a table (stand-alone title, short headings, footnotes, measures of variation named). The map's S58 rungs name figures only; Book 0 F1 teaches reading a table, not making one. Proposed amendment: S58-R1 skill "Make a table that stands alone: title, units, counts and footnotes", served by a concept beside C20. **Accepted 2 Oct 2026 → S58-R1-A01** (as a concept): concept C21, beside C20.
2. **The poster.** NMC requires one poster presentation before the examination. S58-R2 P3 covers a talk, not a poster. Proposed amendment: add the poster to S58-R2 P3. **Accepted 2 Oct 2026 → S58-R2-A01** (revise of P3, map line 4236).
3. **Submitting and revising.** NMC requires a paper published, accepted or sent; S58-R2's build ("accepted without language revision") presupposes choosing a journal, following its instructions, and answering reviewers, which no rung names. Proposed amendment: S58-R2 concept on choosing a journal (scope, indexing, predatory journals), the cover letter, and the point-by-point response to reviewers. **Accepted 2 Oct 2026 → S58-R2-A02** (new S58-R2 concept).
4. **Citing and referencing.** ICMJE §A.3.g: original sources, numbered in order of citation, MEDLINE journal abbreviations, no predatory or pseudo-journals. Book 0 F3 teaches checking a reference; no rung teaches citing one or using a reference manager. Proposed amendment: S58-R1 or S56-R1 concept; Harsh to choose the home. **Accepted 2 Oct 2026 → S58-R1-A02**: S58-R1, concept C05 (Vancouver/ICMJE style, original sources, preprints marked, no predatory or pseudo-journals, a reference manager in passing); format details from NLM *Citing Medicine* (`nlm_citing_medicine_2007`).
5. **Permission to reuse a figure.** ICMJE §A.3.i requires written permission for a previously published figure; S58-R3's gate expects your figures in other people's slides "with attribution", which assumes the reader knows licences (CC BY against all rights reserved). Proposed amendment: one line in S58-R2 (licensing your own figures and reusing others'). **Accepted 2 Oct 2026 → S58-R2-A03** (one S58-R2 line: CC BY against all rights reserved, ICMJE §A.3.i permission).

**Not a gap, but for Harsh.** S58-R2 P1 states as fact that "most rejected Indian manuscripts are rejected for writing and framing rather than for science". No source is attached in the map, and this inventory does not assert it. It needs a source at S58-R2 intake, or rewording.
