# Draft notes, batch b8 (S58-R1 C19, C20, C21)

Drafted 2 Oct 2026 by a Task 2 drafter (Opus 5.5) to `DRAFT-BRIEF.md`. Status of all three: `drafted`.

## Records written

| Record | Name | Type | Figures |
| --- | --- | --- | --- |
| `check/records/S58/S58-R1-C19.yml` | Colour: for meaning only, readable by everyone, and in grey | empirical | `s58-r1-c19-cvd-boys.png` |
| `check/records/S58/S58-R1-C20.yml` | Words on a figure: axis titles with units, direct labels, and a caption that stands alone | derivable | `s58-r1-c20-three-error-bars.png` |
| `check/records/S58/S58-R1-C21.yml` | Making a table that stands alone (amendment S58-R1-A01) | derivable | none: `figure_note` |

Each has a `retrieval` exercise, `retrieval_items`, `common_misreading` and `reporting_sentence`. None is
quantitative (inventory: "no"), so none carries `practice[]`; no practice-set size to justify. C20 and C21
each carry one worked-number exercise (C20 interpretation: SE back to SD; C21 interpretation: SD or SE
from n), recomputed in Python.

Build: `check/build.py`'s own `check()` run on the B0 and S58 records (a scratch wrapper, because
the full `--check` prints only the first 15 blocks and several drafters' builds were running at
once): **0 blocking**. Three warnings remain on these records: one 26-word sentence in C19 exercise 4's
answer and C21 exercise 2's answer, and C21 exercise 2's prompt, whose long sentence is the bad
heading the exercise asks the reader to cut.

Every quote was checked as a whitespace-normalised, case-folded substring of its source file, and every
illustration number with the build's own `_states_value` (scratch script, 0 failures). Every `working`
line was recomputed in Python.

## Anything unsourced, or resting on my own inference

- Nothing rests on an unopened source; every reference has `opened: true` against a held file.
- C21 illustration 1: Krishnamurthy's Results text gives "21422 ... and 53564 ... in public and private
  schools, respectively", while Table 1 labels 21422 Private and 53564 Public. That they disagree is
  read off the two quotes. That the sentence is "probably" the slip is my inference (the text's own
  percentages, public 2.87 and private 2.50, match the table's labels); the record says "probably" and
  the reference note says so.
- C21 interpretation exercise: that "13.75 ± 1.91" must be an SD is arithmetic (1.91 as an SE would give
  an SD of 523 years), not a statement of the authors.
- C20: "one inch is 2.54 cm" is a unit definition, written without a citation; the 8 to 13 cm is
  Wilke's "three to five inches" converted in a `working` block.
- C19: the claim that a grey copy keeps only lightness rests on Crameri (Box 1 rods; the grey-scale
  sentence) and Wilke ch. 20 (desaturated iris figure). No simulator or tool is named, because none is
  named in a held source.

## Figures

- C19 `s58-r1-c19-cvd-boys.png`: bars from illustration 3's table (Krishnamurthy Table 1: rural 1.79,
  urban 3.17, all 2.76 per cent of boys) with a dashed reference line at the cited worldwide estimate
  for men, 8 per cent. Drawn, looked at.
- C20 `s58-r1-c20-three-error-bars.png`: one arm of the SD (12.0), SE (6.93) and approximate 95% CI
  (27.7) bars for Cumming's three values, from illustration 2's second table; checks
  `y[0]/y[1] = 1.732` and `y[2]/y[1] = 4`. Drawn, looked at. A figure that drew the three error bars
  themselves around the mean of 40.0 would be better; `draw.py` has no error-bar kind, so the arm
  lengths are drawn as bars instead.
- C21: `figure_note` (a chart of the table's numbers would break the one-home rule the section teaches).

## numbers.yml keys added

None (the brief forbids editing it). Numbers written literally that another section is likely to share:

| Proposed key | Value | Meaning | Source |
| --- | --- | --- | --- |
| `nfhs5_women_interviewed` | 724,115 | women about whom NFHS-5 gathered information (interviewed), India | `nfhs5_india_factsheet`, introduction: "gathered information from 636,699 households, 724,115 women, and 101,839 men" |
| `nfhs5_men_interviewed` | 101,839 | men, the same | same |
| `cvd_kanchipuram_boys_n` | 74986 | boys aged 11-17 screened for colour-vision deficiency, Kanchipuram district | `krishnamurthy_2021_cvd_india`, Table 1 total row |
| `cvd_kanchipuram_boys_cases` | 2073 | of them, deficiency confirmed | same |
| `cvd_kanchipuram_boys_pct` | 2.76 | per cent | same |
| `cvd_world_men_pct` | 8 | general worldwide estimate cited for men | `crameri_2020_misuse_colour` |

The Krishnamurthy rows (21911/392/1.79 rural, 53075/1681/3.17 urban) are used in both C19 and C21; the
reconciler may register them too. C20 and C21 both use 724,115 and 101,839.

## Notation rows needed

None new. The records print √ (C20, C21), ± (C20 prompt, C21 prompt and must-know) and %; all have rows
in `check/notation.yml`. C21 deliberately uses letters, not †/‡, for footnote marks, so no new rows.

## Glossary rows (proposed; none is in `prose/GLOSSARY.md` yet)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| axis title | the words along an axis naming the quantity it shows and its unit | `S58-R1-C20` |
| colour bar | the strip, like an axis, that shows which colour stands for which value | `S58-R1-C19` |
| colour-vision deficiency | a reduced ability to tell certain colours apart, most often red from green | `S58-R1-C19` |
| colour-vision-deficiency simulator | a program that redraws an image as a reader with a given deficiency would see it | `S58-R1-C19` |
| confidence interval, 95% (CI) | a range worked out from the sample so that, if the study were repeated many times, 95 per cent of such ranges would contain the population's true mean | `S58-R1-C20` |
| diverging colour scale | two sequential scales joined at a light middle colour placed at a value that means something, such as zero | `S58-R1-C19` |
| error bar | a line drawn through a value, usually a mean, to show a range around it; descriptive (range, SD) or inferential (SE, CI) | `S58-R1-C20` (unless C16 glosses it first) |
| footnote (of a table) | a note under a table, marked with a letter or symbol, carrying explanations, exclusions and abbreviations | `S58-R1-C21` |
| greyscale copy | a figure with its colour removed, keeping only how light or dark each colour is | `S58-R1-C19` |
| hue | the name of a colour: red, green, blue | `S58-R1-C19` |
| n (in a caption) | the number of independent people or units measured, not the number of measurements | `S58-R1-C20` |
| perceptually uniform (colour scale) | the same step in the data looks like the same step in colour anywhere along the scale | `S58-R1-C19` |
| qualitative colour scale | a small set of colours that look clearly different and equally strong, for groups with no order | `S58-R1-C19` |
| replicate | a repeated measurement of the same person or sample; replicates count once in n | `S58-R1-C20` |
| sequential colour scale | colours running from light to dark, for a value from low to high | `S58-R1-C19` |
| tick label | a value printed along an axis | `S58-R1-C20` |

"Caption" (journals' "figure legend") is `S58-R1-C14`'s, and C20 uses it in C14's sense. "Legend" (the
key) and "direct label" should be glossed by C18; C19 and C20 use them in that sense. "Standard error of
the mean" is already glossed (`B0-R0-C29`); C20 uses it unchanged.

## Notes for others

- **Everyone citing the NFHS fact sheet in a definition reference:** `kind: dataset` blocks in the build
  ("not a recognised kind": `KIND_FOR_TYPE` has no `dataset`). C19 uses `kind: instrument`.
- **Arithmetic gate:** a `working` line whose left side has no decimals is compared exactly (to 1e-9
  relative), so "2073 divided by 74986 = 0.0276" blocks. Write such a quotient in words ("is 0.0276,
  to four decimal places") or to full precision.
- The BMI cut-off "25.0 kg/m^2" is written literally in C20 and C21 (and in C14); the reconciler may
  register it.

- **C18** must teach direct labelling and use "legend" for the key: C19 illustration 1 says "This is the
  direct labelling of the last section", and C20 cites `S58-R1-C18` for it.
- **C14**: C20 illustration 1 starts from C14's caption sentence for the NFHS urban/rural figure and
  finishes it (axis titles, exclusion of pregnant women, n, source). C20 writes the finding people-first,
  "had overweight or obesity"; C14 writes "were overweight or obese". The reconciler should pick one
  wording for the book (claude.md §9 points to the people-first one).
- **C16** is in C20's `concept_deps`. C20 defines range and SD as descriptive bars and SE and 95% CI as
  inferential (Cumming); C16 should not call an SE bar a measure of spread.
- **C09** already expands SD and SE; C20 re-expands them in its definition, which is harmless.
- **C09, C17, C22, C23**: the NFHS fact sheet gives no counts per row; its 724,115 women and 101,839 men
  are the numbers **interviewed**, not the number weighed and measured. Do not print either as the n of
  the BMI rows (C20 and C21 both say so).
- **C22** (making the plot) should keep C19's two tests in the same words: "in grey" and "through a
  colour-vision-deficiency simulator"; and C20's size check, shrinking the figure to about 8 to 13 cm
  wide (Wilke's three to five inches).
- **C23** (journey): C21 illustration 2 builds the NFHS-5 overweight-or-obesity rows as a table that
  stands alone (title, columns NFHS-5 urban/rural/total and NFHS-4 total, footnote a for the exclusion,
  "counts not given in the source", source line). The journey can reuse it; it must keep the C14/C21
  rule that a paper shows these rows as a table or a figure, not both.
- Anyone quoting colour-vision deficiency: Krishnamurthy 2021 is boys aged 11-17 in one Tamil Nadu
  district (block range 1.12 to 3.40 per cent); the 8 per cent and 0.5 per cent are a general worldwide
  estimate Crameri cite, not measure. The authors' "17 million boys" is an extrapolation; C19 says so.
- Reproductions: C21 reprints four columns of Krishnamurthy's Table 1 (CC BY-NC-SA 4.0) with
  attribution; Wilke (CC BY-NC-ND) and ICMJE (no reprinting) are quoted briefly only.
