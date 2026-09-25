# S57-R1 draft notes · batch b7 (C14, C15, C16)

Drafter: Opus 5.5, 2026-09-25. Resumed after an interrupted run: C14 existed as an unchecked
partial draft and was kept and finished; C15 and C16 were written new. Every self-check below was
run on all three as if new.

## Records written

- `check/records/S57/S57-R1-C14.yml` — institutional. Where teaching sits in Indian medical
  education: GMER 2023 (regulation) over the CBME Curriculum 2024 (guideline, letter of 12 Sep
  2024); the seven IMG roles; Foundation Course 2 weeks / 80 hours; AETCOM longitudinal, 75%
  attendance; large-group cap one third; mentor 1:3; Basic Course in Medical Education tied by
  MIQF 2025 Table E to Professor and Associate Professor posts in UG-taught broad specialties,
  with regulation 14 exemptions; TEQ 2022 cited only as superseded. C10's K/KH/SH/P levels get a
  one-sentence pointer only. Changes made on resume: added the mentor-allotment / "till he
  completes CRMI" reference (a must-know point claimed it with no quote), the CRMI expansion, the
  "two third" small-group sentence behind the teaching exercise; reworded "does not print the
  evidence" to "the paragraph that sets it cites no study" (that page is held whole); noted that
  role c is worded "Communicate with..." in the 2024 guideline; added the pointer to C10 in the
  first paragraph. `figure_note` kept.
- `check/records/S57/S57-R1-C15.yml` — empirical. Leading people is a craft of its own: leading
  (Frich's one-line understanding) is a different competency from the work (Stoller; Kotter's "not
  charisma", both flagged as argued, not measured); Frich 2015 as the evidence that it is taught
  and how thin the test of it is (45 studies, all positive, 4 with a comparison group, no pooled
  effect size, publication bias expected); what would answer it; the three things a leader builds
  and the "what happens the day you leave?" test; professional body and civil society
  organisation in one line each, named ones routed to the next book. It points to C13 for the
  levels and does not redraw C13's level counts; its figure is Frich's Table 2 evaluation designs.
- `check/records/S57/S57-R1-C16.yml` — derivable. Words for how a team works: Kotter's three
  management and three leadership activities in pairs (quoted from the now-held HBR reprint, not
  Stoller), credibility as the trust part of aligning, "strong leadership with weak management is
  no better", then working definitions of authority and power, delegation matched to person and
  task, role clarity (who decides / does / is consulted), conflict about the work against conflict
  about the person. Diagnosis and practice routed to the next book (S57-R2), running a team to
  S57-R3. `figure_note`.

Provenance: C14 O1, A01 / P03. C15 A01, O1 / P05, R3. C16 A01 / S57-R2-A01, S57-R2-A02.
concept_deps: C15 on C01, C02, C13, C14; C16 on C15.

## Anything unsourced, and decisions for the conductor

- **C16's working definitions have no source.** Kotter defines management and leadership and uses
  "authority to delegate", but does not define power against authority, delegation matched to
  the person, role clarity, or the two kinds of conflict. The record says in its definition that
  these are the book's working definitions, "built from the words themselves, not taken from a
  study", keeps every claim about them non-empirical (no "usually", no "makes it worse"), and
  routes the evidence to S57-R2. READY.md already records that situational leadership, RACI and
  task/relationship conflict sources (de Wit, Greer & Jehn 2012) are S57-R2's to obtain. The
  names "RACI" and "situational leadership" are deliberately not used.
- **C15's definitions of teaching lineage, team, institution, professional body and civil society
  organisation are the book's own**, stated as such (the verified note on the last Kotter
  reference says so). The map's claim that civil society food-policy organisations are "short of
  technical capacity and very receptive" (S57-R2 P5) is not made: no source is held.
- **Trust.** The map says leadership is "direction, alignment, trust"; Kotter's third activity is
  motivating and inspiring, and trust enters only as credibility inside aligning. C16 follows
  Kotter and says the trust gloss is the record's own.
- **Frich's "four" against "five" comparison-group studies:** C15 uses four (abstract and Table 2),
  as C13 does, and its note points to C13's exercise on the disagreement.
- **C15 quotes Frich's conclusion without "significantly"** in the prose (the review pooled
  nothing); the reference note says why.
- **Stoller** is cited as `primary` (a narrative review; the S01 exemplar treats Hall & Guo's
  narrative review the same way). If the conductor prefers another kind, only the `kind` field
  changes.
- **Kotter copyright:** all rights reserved, no reuse licence. Quotes are short sentences; the
  Kodak case is paraphrased with its numbers quoted in `numbers`. The rest is paraphrase.
- **C14 open question kept as open:** whether the Basic Course must be done before promotion or
  may follow it (Table E says "shall be required to undergo" against "have completed" for the
  research course). The FAQ Q5 held in the file answers only for the Note 2 route (within two
  years of appointment), so C14 still tells the reader to ask NMC in writing.
- **Glossary collision:** "power" is already glossed in its Book 0 sense (B0-R0-C06, repeated
  multiplication). C16 uses it for power over people. Proposed row below as a separate term;
  the conductor may prefer a numbered second sense at the merge.

## Practice sets

None: the inventory marks C14, C15 and C16 not quantitative (`quantitative: false`). The only
arithmetic is one-line counts in C15's illustrations (22 plus 23 = 45; 45 minus 4 = 41;
3 times 5 = 15) and C14's "eleven days" (23 minus 12), recomputed in Python.

## Figures

- `s57-r1-c15-study-designs.png` — bar chart from C15's own table (Frich Table 2 evaluation
  designs: 22, 23, 4), with `check: y[0] + y[1] = 45`; the caption says the 4 are among the 45.
  Drawn by `draw.py --book S57-R1` (16 figures, 0 problems) and looked at as an image.
- C14 and C16 carry a `figure_note`. No new drawing kind is wanted.

## Self-check (check/SELFCHECK.md)

- `python check/build.py --check`: blocking 0 overall; no blocking and no warning line names C14,
  C15 or C16 (sentence-length warnings fixed).
- All 75 quotes in the three records found in their source files by a separate script, each in
  the body of the file, none from a header or a `[NOTE]` line; ligatures copied as held
  ("signiﬁcant", "stafﬁng", "qualiﬁed", "ﬁrst"). Every number in `numbers` states its value in
  its quote or carries `derived`.
- Bounds, §9 language (no weight language beyond "weighing and measuring children"), pointers
  (C15 names C01/C02/C13/C14 by description and lists them), terms defined at first use, no
  repository path in reader text.

## Glossary rows (proposed; none of these is in prose/GLOSSARY.md except "power", see above)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| AETCOM | the CBME Curriculum 2024's module on Attitude, Ethics and Communication, running through all the years of the course | `S57-R1-C14` |
| aligning people | Kotter: communicating the direction to everyone who can help carry it out or block it, so that they understand it and are committed to it | `S57-R1-C16` |
| authority | the right to decide or direct that comes with a post, given by a rule or handed on by someone who holds it | `S57-R1-C16` |
| Basic Course in Medical Education | the teaching course the 2025 faculty regulations tie to Associate Professor and Professor posts in most MD and MS subjects | `S57-R1-C14` |
| civil society organisation | a group formed by citizens, outside government and outside business, to work for a public cause | `S57-R1-C15` |
| conflict about the person | friction over who someone is: blame, dislike, a remark about their character or motives | `S57-R1-C16` |
| conflict about the work | disagreement over what to do, how to do it, or on what evidence | `S57-R1-C16` |
| controlling and problem solving | Kotter: monitoring results against the plan, finding where they depart from it, and fixing that | `S57-R1-C16` |
| credibility | Kotter: whether people believe the message, resting on the messenger's record, integrity and the match between words and deeds | `S57-R1-C16` |
| CRMI | compulsory rotating medical internship, the year after the MBBS examinations | `S57-R1-C14` |
| delegation | handing a task, and the authority it needs, to another person while you stay answerable for the result | `S57-R1-C16` |
| Foundation Course | the two weeks, 80 teaching hours, that open Phase I of the MBBS course | `S57-R1-C14` |
| guideline (NMC) | a document NMC's board issues by letter and puts on its website, under a Gazette-notified regulation | `S57-R1-C14` |
| Indian Medical Graduate (IMG) | the doctor the MBBS course is meant to produce; the CBME Curriculum 2024 gives the IMG seven roles | `S57-R1-C14` |
| institution that outlives you | a standing group, with written terms, roles and a named successor, that keeps working after you leave | `S57-R1-C15` |
| leadership | Kotter: coping with change, by setting a direction, aligning people, and motivating and inspiring | `S57-R1-C16` (first met as "leading", `S57-R1-C15`) |
| management | Kotter: coping with complexity, by planning and budgeting, organizing and staffing, and controlling and problem solving | `S57-R1-C16` |
| motivating and inspiring | Kotter: keeping people moving in the direction, despite obstacles, by appealing to their needs, values and emotions | `S57-R1-C16` |
| organizing and staffing | Kotter: a structure of jobs, filled with qualified people, the plan communicated and responsibility delegated | `S57-R1-C16` |
| planning and budgeting | Kotter: setting targets, detailed steps to reach them, and resources allocated to the steps | `S57-R1-C16` |
| power (over people) | the capacity to get things done through other people, from any source, authority being only one | `S57-R1-C16` |
| professional body | an association whose members share one profession or discipline | `S57-R1-C15` |
| role clarity | a written statement, for each decision or piece of work, of who decides, who does it, and who is consulted first | `S57-R1-C16` |
| setting a direction | Kotter: developing a vision of the future, often the distant future, with strategies for the changes it needs | `S57-R1-C16` |
| supersession | the new instrument taking the old one's place | `S57-R1-C14` |
| teaching lineage | the people you teach, and the people they go on to teach | `S57-R1-C15` |
| team you run | a set of people whose work on one job you direct, for as long as the job lasts | `S57-R1-C15` |
