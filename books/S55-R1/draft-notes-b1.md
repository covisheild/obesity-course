# S55-R1 draft notes · batch b1 (C01, C02)

## Records written

- `check/records/S55/S55-R1-C01.yml`: A research question is a choice (derivable, not quantitative).
- `check/records/S55/S55-R1-C02.yml`: Population, exposure, outcome: a question in one sentence
  (derivable, quantitative, 10 practice problems).

`python check/build.py --check --subject S55`: no blocking line for C01 or C02. The remaining blocks
belong to C07 and C08 (other batches).

## Sources and what is not sourced

- Textbook anchors: `blackstone_2012` ch. 4 (4.1, 4.4), `jhangiani_2019_methods`, and
  `cdc_ss1978_lesson1` (§6 time, place, person; §7 exposure, outcome, comparison group). Primary:
  `aslam_emmanuel_2010` (PICO, one main question, selecting among several questions) and
  `morgan_peco_2018` (PECO, the move from PICO to PECO, search criteria, the 54% of 313 figure).
  Every quote passes the build's source check.
- **The 54% of 313 figure** (C02 must-know, `number`) is Morgan et al.'s report of an earlier review
  (Thabane et al. 2009, not held and not opened). The record states it only as Morgan and
  colleagues' report and says so in `verified.note`. Cut it if the conductor wants only figures
  from sources that were themselves opened.
- **C01 routes.** The four routes (named by a guide, set by data at hand, borrowed from a paper's
  future-research line, picked for speed) are reasoned, with no share claimed. Two of them are
  supported as *recommended sources of questions*: Blackstone's "starting where you are" and
  Jhangiani's discussion-section advice. C01 says these routes are fine sources of candidates, and
  that the fault is keeping the first one without comparing. Nothing about NMC rules, theses, or
  who assigns a question is stated. "Assigned by a guide" is shown only as a made-up event.
- Farrugia, Ratan, Ioannidis, Van Noorden and the rest are not used in b1.
- Every question, draft, protocol line and meeting remark is made up, and each section says so
  where it first appears. Place names (Raipur, Durg, Bilaspur, Korba) carry no claim. No statistic
  about the world appears outside the Morgan figure.

## Practice set size (C02)

10 problems, one at each level from 1 to 10. There are three moves: label the parts; write a fenced
sentence, with one reversal at level 6 that goes from a finding back to its question; and break a
wrong labelling. Each move needs its PICO/PECO and how-common variants covered. Ten covers them
without repeating a move.

## Figures

- C01: `figure_note`. The routes have no measured shares, so any chart would invent counts.
- C02: `s55-r1-c02-parts-named.png`, a bar chart drawn from the illustration's count table. It shows
  the five made-up drafts against their rewrites, counted by part named. Drawn by `draw.py`, 0
  problems, and checked by eye. The counts were recomputed in Python from the two marking tables.
  C02 is quantitative in the §7a sense, but its technique is not arithmetic. Like S36-R1-C05, its
  figure shows the worked relationship as a before-and-after tally. No new figure kind is needed.

## Warnings left on purpose

C02 has sentence-length warnings (28–46 words) that come only from the one-sentence PECO questions
themselves, in practice prompts and answers and in exercise 1. A fenced four-part question is one
sentence by design, so splitting it would defeat the skill being taught. All other prose warnings
were fixed.

## For the conductor / other batches

- **"outcome" clash.** `prose/GLOSSARY.md` has "outcome" as "one member of the sample space"
  (`B0-R0-C24`). C02 teaches a second sense, and says so inline in the simplified explanation and in
  a retrieval item. C02 lists `B0-R0-C24` in `ground_floor_deps` for that pointer. The glossary row
  needs a numbered sense 2 (proposed below).
- **Terms C03 onward should reuse.** "how-common question" (population and outcome, no exposure).
  "fence": a population fenced by place, person and time. "comparison", not "comparator" or
  "control". "exposure", which becomes "intervention" when given on purpose. C03's "describe"
  question is the same thing as C02's "how-common question", so C03 should say so, or the two
  names need merging.
- C02 already names the searching use of the one sentence and routes the search to later ("you build
  the search from these same parts"). `bridge_ref: [S55-R2-P03]`.
- C02 practice 9 says that why two groups differ "needs its own kind of study". That is the only
  point where it touches C03, and it teaches no design.

## Glossary rows (proposed; not added to `prose/GLOSSARY.md`)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| comparison (in a research question) | the group, or level of exposure, that the exposed group is set against; some sources call it the control or the comparator | `S55-R1-C02` |
| exposure | what differs between the people being compared: something they have, do or meet | `S55-R1-C02` |
| how-common question | a research question with a population and an outcome and no exposure; it asks how common or how large the outcome is | `S55-R1-C02` |
| intervention | an exposure given on purpose, by a researcher or a programme, as the thing being tested | `S55-R1-C02` |
| outcome | (1) one member of the sample space `B0-R0-C24`; (2) in a research question, what is measured to answer it `S55-R1-C02` | `B0-R0-C24`, `S55-R1-C02` |
| PECO | population, exposure, comparison, outcome: the four parts of a question about an exposure people meet in ordinary life | `S55-R1-C02` |
| PICO | population, intervention, comparison, outcome: the four parts of a question about something given on purpose | `S55-R1-C02` |
| research question | a sentence that asks one thing a study will find out about a topic | `S55-R1-C01` |
| research topic | an area of interest, such as obesity in adolescents; not yet a question | `S55-R1-C01` |
