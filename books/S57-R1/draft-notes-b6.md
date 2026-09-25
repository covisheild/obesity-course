# Draft notes · S57-R1 · batch b6 (C12, C13)

Resumed after an interrupted run. C12 existed as an unchecked draft and was re-checked in full;
C13 was written new. `python check/build.py --check`: blocking 0, and no warnings for either record
(2026-09-25). `python check/figures/draw.py --book S57-R1`: 0 problems. Every practice answer and
illustration line in C12 was recomputed in Python (`/home/claude/scratch-b6/verify12.py`),
including a Gale-Ryser check that the item table is consistent with the ten learners' scores. C13's
four divisions were recomputed as well.

## Records written

- `check/records/S57/S57-R1-C12.yml`: Measuring what changed: pre-test, post-test, gain
  (derivable, quantitative, 14 practice problems). Changes on resume: `bridge_ref` set to
  `S57-R2-R2`, `S57-R2-B2` (it was empty); invented scores in practice prompts now said to be made
  up; the algebra from `post = pre + 0.5 × (100 − pre)` to `post = 50 + 0.5 × pre` is now shown
  step by step; the Hake "±0.14 (std dev)" reading is marked as the natural reading, not stated by
  the abstract; the figure's two labels moved off the lines; seven long sentences split.
- `check/records/S57/S57-R1-C13.yml`: Liking a session is not learning from it (derivable, not
  quantitative). Two illustrations: sorting an end-of-session feedback form (made up, and said to
  be) by level, then reading Frich 2015's counts of which levels 45 studies measured.

## Sourcing, and anything unsourced

- Kirkpatrick's levels are quoted only in Frich's wording ("reaction ..., knowledge ...,
  behavioral change ..., and system results"), as the brief directs. Kirkpatrick's own book is not
  held. Stoller and Kotter are not used.
- C13 is derivable, so its required textbook anchor is OpenStax §1.4's definition of a response
  variable. The step "each level is a different response variable" is the record's own argument,
  not attributed; the reference note says so.
- Frich disagrees with itself on comparison groups: the abstract and Table 2 say four, and the
  Results text says "Only five studies" but cites four reference numbers. C13's interpretation
  exercise is built on this. Nothing else rests on it.
- Hake 1998 is held as the abstract only. C12 quotes only the abstract. The reading of the ±0.04 and
  ±0.14 as spreads among course gains is the natural one (each course has one class gain), but the
  abstract does not say it. The record says so where it uses that reading.
- C12 level 5 uses Deslauriers Table 1's spring Group A Force Concept Inventory pretest, 23.3 of 30.
  It says the study reported no post-test on that instrument. That is true of the held text.
- ASHA is expanded as "Accredited Social Health Activist" in C13 without a source. It is a name,
  not a claim. C12 uses "ASHA workers" in practice problems before C13, so if the acronym check
  wants the expansion at first use, it may belong in an earlier record (C11 or C12). Conductor's
  call.

## Practice-set size

- C12: 14 problems (levels 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10). The top of the inventory's
  8-14 range, because the technique composes several moves: raw gain, SD of gains, normalised gain
  both ways (forward, and pre or post from g), class gain against the mean of learners' gains,
  proportion reaching a standard, per-item proportions, and share of gain kept at delay. Each gets
  at least one problem, and the direction is reversed twice.
- C13: not quantitative, no practice set.

## Figures

- `s57-r1-c12-pre-post.png`: a scatter of the ten students' pre- against post-test scores, with
  the no-change line and the line for a gain of 0.5 (`post = 50 + 0.5 × pre`). Drawn, and looked
  at.
- `s57-r1-c13-levels-measured.png`: bars showing how many of Frich's 45 studies reported each
  level (25, 36, 7, 10, 2, 6). Frich is CC BY 4.0, so a new figure from its counts is allowed.
  Level 4 is one bar, the six articles the Results text gives, because its 4A/4B split exists only
  as table cells. Drawn, and looked at.
- No figure wanted beyond these.

## Glossary rows (proposed; not added to prose/GLOSSARY.md)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| class normalised gain | the normalised gain worked out from a class's mean pre-test and mean post-test, as Hake defines it; not the mean of each learner's own gain | `S57-R1-C12` |
| delayed test | the same test, on a parallel form, taken after a stated wait, the retention interval | `S57-R1-C12` |
| Kirkpatrick's levels | four things an evaluation of teaching can measure: reaction, knowledge, behavioural change, system results | `S57-R1-C13` |
| normalised gain | the raw gain divided by the room to gain, (post − pre) ÷ (100 − pre); a fraction with no unit | `S57-R1-C12` |
| objective (of an outcome measure) | measured by a test, an observation or a record, as against stated by the learner (Frich's B levels) | `S57-R1-C13` |
| proportion correct (on an item) | the number who answered one question correctly, divided by the number who answered it | `S57-R1-C12` |
| raw gain | post-test minus pre-test, in percentage points | `S57-R1-C12` |
| reaction | how learners feel about a session and how satisfied they are with it: Kirkpatrick's Level 1 | `S57-R1-C13` |
| response variable | the quantity a study measures to see what a treatment changed | `S57-R1-C13` |
| room to gain | 100 − pre: the most a learner could gain | `S57-R1-C12` |
| subjective (of an outcome measure) | stated by the learner or someone near them, as an opinion or a rating (Frich's A levels) | `S57-R1-C13` |

Checked: none of these terms is already in `prose/GLOSSARY.md`. "ceiling" is glossed there for a
saturating shape. C12 does not use that word for the top of a test's scale.
