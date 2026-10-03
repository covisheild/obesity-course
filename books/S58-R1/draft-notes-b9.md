# Draft notes · S58-R1 · batch b9 (C22, C23)

Task 2 drafter, 2 Oct 2026. Exemplars: S57-R1-C10, S57-R1-C12. Both records `drafted`.

## Records written

| Record | Name | Type | Figures | Retrieval exercise | Optional blocks |
| --- | --- | --- | --- | --- | --- |
| `check/records/S58/S58-R1-C22.yml` | Making the plot: from a table of numbers to a finished figure | derivable | `s58-r1-c22-anaemia-two-rounds.png` | yes | `common_misreading`, `reporting_sentence` |
| `check/records/S58/S58-R1-C23.yml` | One finding, from the fact sheet to a paragraph a colleague can restate (`journey: true`) | derivable | `s58-r1-c23-rise-from-zero.png`, `s58-r1-c23-three-drafts.png` | yes | `common_misreading`, `reporting_sentence` |

C22: nine decisions in a fixed order (claim, mark, axis, words; defaults, colour, caption, saving, checks),
content before design after Wilke ch. 28 §28.3; taught tool-free; Wilke's Preface on Excel ("not
recommended for figure preparation") and on hand edits; a "figure sheet" (this book's name for Wilke's
"careful notes", said so) as the written record; vector against bitmap and pdf/png/never jpeg from Wilke
ch. 27; ICMJE §IV.A.3.i for legibility and journal image instructions; plotting code routed to "the
course's book on R and reproducibility" (S52). Worked case: NFHS-5 anaemia rows 92, 95-98 (a genuine
figure-sized set: five groups, two rounds, "rose in every group"), from an invented default chart. Exercises:
retrieval, critique (K02), design (K02), teaching (first-year resident).

C23 journey, in working order: question and data limits; C03's one message reused verbatim; an invented
diary paragraph (different from C02's) to the claim draft; numbers (points, no counts, Cole's range rule:
range 5.1 for the totals, 14.3 for the table, one decimal kept in both with Cole's "recommendations not
requirements"); FRE/FKGL of three drafts (figures as one syllable, as C11); cut in C12's order; C21's
table reused; the figure by C22's steps with a Lie Factor check of a program axis at 18 (women 7.9, men
21); **the paper keeps the table**, the figure goes to the talk (C14's rule: four totals are a sentence's
job; ICMJE no duplication); the paragraph then cites Table 1 and gives the two rises only; the reference
(honest gap, below); a one-pass test with two invented readers; seven "does not mean" lines. **No `build`
exercise** (C13 holds it): exercises are retrieval, critique (press line "up 17%"), teaching (journalist),
design (K01).

## Anything unsourced, or the book's own

- **The NFHS fact sheet's NLM reference is NOT formatted.** No held passage gives NLM's rules for a report
  or web document (`nlm_citing_medicine_2007` header: chapter 1 part A, appendix B opening, two Sample items
  only). C23 says so, quotes Citing Medicine's own line that journal references omit place and publisher
  which book references carry, lists the elements the fact sheet's cover prints (and that place and year
  of publication are not on the cover), points to NBK7256, and tells the reader to mark entry 1 unchecked.
  NLM's suggested citation for Citing Medicine itself is quoted only to show what an Internet document
  carries; no entry is built from it. **To close this:** take Citing Medicine's chapter on reports (and/or
  Internet documents) at intake, then C23 ill. 4 can show the finished entry.
- All drafts, readers' sentences, the default chart, the colleague's figure sheet and the programme-officer
  readership are invented and labelled so. The program axis "at 18" is a supposition, said so.
- "Figure sheet" is this book's term (definition says "In this book").
- C23 teaching answer avoids any claim about the survey's precision: the fact sheet prints no counts or
  margins of error.
- Syllable counts are hand judgements (India 3, nutritional 4, individuals 5, comparison 4, respectively
  4, obesity 4, percentage 3), listed in the text so a reader can recount.

## Practice-set size

Neither record is quantitative; no `practice[]`. C23 uses C09/C11/C17 techniques in `working` blocks;
every line (32) recomputed in Python.

## Figures (all drawn by `draw.py --book S58-R1`, 22 figures, 0 problems; each PNG looked at)

- `s58-r1-c22-anaemia-two-rounds.png`: five groups x two rounds, bars from 0 to 80, round names written
  over the first pair; checks on the five rises (8.5, 5.0, 3.9, 1.9, 2.3).
- `s58-r1-c23-rise-from-zero.png`: women/men, NFHS-4/NFHS-5, bars from zero, value labels. **Overlaps
  C17's `s58-r1-c17-bars-from-zero.png`** (same four values, same grouping). The journey needs its own
  drawn figure; the reconciler may prefer to cut one.
- `s58-r1-c23-three-drafts.png`: FRE of the three drafts (61.6, 79.7, 86.7) with Flesch's 60 as a
  reference line: the diary passes it.
- **Palette problem for the conductor (affects C19's teaching, and C14, C17, C22, C23 figures):** the
  S58-R1 palette's `primary` #b6206b and `secondary` #138613 have relative luminance 0.12 and 0.17
  (contrast about 1.3:1), so two-series figures nearly merge in grey, the test C19 and C22 tell readers to
  run. C22's text therefore does not claim its colours differ in lightness on the drawn figure; it makes
  position (NFHS-4 always left) and labels carry the rounds. A palette fix in `style_for` would need
  every S58 figure redrawn; I did not touch `draw.py`.

## numbers.yml

No key added. Used: all ten existing keys. Literal numbers another section shares (for the reconciler):

| Value | Meaning | Source |
| --- | --- | --- |
| 25.0 | kg/m^2, the BMI cut-off of indicators 88-89 | `nfhs5_india_factsheet` (also literal in C08, C14, C20, C21) |
| 5.1 | range of the four totals, 24.0 − 18.9 | arithmetic (also C09) |
| 14.3 | range of the table's eight values, 33.2 − 18.9 | arithmetic |
| 7.92; 21.0 | LF of women's and men's bars drawn from an axis at 18 | 20.6 ÷ 2.6; 18.9 ÷ 0.9 (C17 has 7.92 for women) |
| 0.165 | relative rise, women (about 17 per cent) | 3.4 ÷ 20.6 (also C09) |
| 724,115 | women NFHS-5 gathered information from | `nfhs5_india_factsheet` (also C09, C20, C21) |
| 58.6/67.1, 54.1/59.1, 53.1/57.0, 29.2/31.1, 22.7/25.0 | anaemia NFHS-4/NFHS-5, indicators 92, 96, 95, 98, 97 | `nfhs5_india_factsheet` (C21's exercise uses rows 93 and 97) |

## Notation rows needed

None new. Signs printed: ÷ and − (C23, C22, rows exist), ≥ only inside fact-sheet quotes, `<` only inside
quotes. LF expanded as "Lie Factor (LF)" at first use in each record; ASL, ASW, FRE, FKGL appear in C23's
table headers only after C11 has expanded them (C23 writes "Flesch Reading Ease" in its figure).

## Glossary rows (proposed; `prose/GLOSSARY.md` not edited)

"resolution" (B0-R0-C30) and "vector" (S02-R1-C10) exist in other senses, so C22 never uses either bare:
it writes "vector graphic" and avoids "resolution".

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| default (of a program) | a setting a program uses when you have not chosen one | `S58-R1-C22` |
| figure sheet | (this book's term) the written list of the decisions for one figure, kept beside its data | `S58-R1-C22` |
| bitmap | an image saved as a grid of coloured dots, called pixels | `S58-R1-C22` |
| vector graphic | an image saved as the shapes themselves, redrawn at any size without losing sharpness | `S58-R1-C22` |
| anaemic (as the NFHS fact sheet counts it) | haemoglobin below the cut-off the fact sheet gives for the person's group | `S58-R1-C22` (C21's exercise glosses haemoglobin first) |
| journey (of a finding) | the order of work that carries one result from its source to a paragraph a reader can restate | `S58-R1-C23` |

## Notes for others

- **C14/C21 consistency kept:** the journey makes both a table and a figure, then keeps the table (four
  totals are a sentence's job; readers need eight exact values); the figure goes to the talk. Its final
  paragraph gives the claim and the two rises and cites Table 1, without reading out the levels.
- **Wording:** C23 reuses C03's one message verbatim ("were overweight or obese") and C21's table title
  ("with overweight or obesity"); the final paragraph ends "had a body mass index of 25.0 kg/m^2 or
  more". If the reconciler settles the person-first wording (b8's note), change C23 with the rest.
- **C23 adds one "does not mean" line no earlier section states:** two estimates (3.4 and 4.0 points) do
  not show that men's share rose faster. Nothing earlier contradicts it.
- **Digits:** C23 notes that Cole's range rule would give whole numbers for C21's eight-value table
  (range 14.3) and keeps one decimal on Cole's "recommendations not requirements". C21 should not say the
  rule requires one decimal there.
- **C22 routes plotting code to S52** in the words "the course's book on R and reproducibility" (S52-R1,
  not started). No section ID is named, so no forward-reference check fires.
- **C22 relies on C19's "in grey" and "colour-vision-deficiency simulator" and C20's 8 to 13 cm** in
  those words.
- **Build:** `check.build.check()` over all records after the last edit: 0 blocking overall; two
  sentence-length warnings left on b9 (C22's 26-word column-reading sentence; C23's quoted
  journalist sentence, 28 words, kept whole so she can quote it).
