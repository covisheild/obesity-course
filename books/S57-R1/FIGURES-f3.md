# S57-R1 figure plan, batch f3 (C12-C16)

All figures drawn by `python check/figures/draw.py --book S57-R1`. `python check/build.py --check`
shows no blocking item in C12-C16. Each PNG was opened and looked at after its last redraw.

## C12 Measuring what changed: pre-test, post-test, gain

- `s57-r1-c12-pre-post.png`: the ten invented learners' pre against post, with the no-change line
  post = pre, the line of normalised gain 0.5 (post = 50 + 0.5 × pre), and the 100% ceiling. F and H
  are labelled. Check: derived 50 = 0.5 × 100; `check`s that (50 + 0.5·pre − pre)/(100 − pre) = 0.5
  at pre 20 and 60, F's g = 0.25, H's g = 1. Redrawn this pass: the H label was moved and the ceiling
  label shortened so they no longer crowd; the alt text now says "dashed" line, not "dotted".
- `s57-r1-c12-class-over-time.png` (new): the class mean and the % at or above 80%, at pre, post and
  delayed (46/75/66; 10/50/40). Checks: 75 − 46 = 29, 66 − 46 = 20, 20/29 = 0.69.
- `s57-r1-c12-items.png` (new): right answers per item before and after, from the item table (Q1-Q10).
  Check: item 10 moved by 1.
- `s57-r1-c12-hake.png` (new): Hake's class gains, 0.23 for 14 traditional courses and 0.48 for 48
  interactive-engagement courses. The SDs are in the caption, not drawn. Check: 14 + 48 = 62.

## C13 Liking a session is not learning from it

- `s57-r1-c13-levels-measured.png`: Frich's counts of studies at each level. Checks added: 36/45 = 0.8,
  7/45 = 0.156.
- `s57-r1-c13-form-by-level.png` (new): the invented form's five items by level: 3 at Level 1,
  2 at 2A, and none at 2B, 3 or 4. Derived: 5 = 3 + 2, 0 = 5 − 3 − 2; check sum = 5.

## C14 Where teaching sits in Indian medical education

- `s57-r1-c14-img-roles.png` (new; replaces the figure_note): the number of IMG roles in each list.
  The 2019 regulation has 5, the CBME 2024 guidelines §5 have 7, and the manual's extract in the same
  document has 5. Derived 2 = 7 − 5; check y[1] − y[2] = 2.

## C15 Leading people is a craft of its own

- `s57-r1-c15-study-designs.png`: Frich's Table 2 designs, 22/23/4. Checks: 22 + 23 = 45, and
  45 − 4 = 41 (added).
- `s57-r1-c15-mentees.png` (new): cumulative mentees at 3 a year over the example's 5 years, from 0 to
  15, with the fit y = 3x drawn. Derived: 0 = 15 − 3·5, 6, 9 and 12.

## C16 Words for how a team works

- `s57-r1-c16-crandall-reach.png` (new; replaces the figure_note): the people Crandall's aligning
  reached, in Kotter's account. 12 direct reports weekly, 80 to 100 monthly (drawn at 100, labelled
  "80 to 100"), and all 1,500 employees as the yearly goal, on a linear scale. Derived 15 = 1500/100;
  check y[2]/y[1] = 15.

## Caveats

- The C16 monthly bar is drawn at the upper end (100) of Kotter's 80 to 100. The caption and the bar
  label both say so.
- The C13 form-by-level figure is modest: it draws what the prose says in one sentence ("nothing
  reaches 2B"). Harsh may prefer to drop it.
- C13's form figure groups Level 3 and Level 4 without A/B, which matches the prose ("not Level 3
  either").
