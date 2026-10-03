# Draft notes, batch b4 (S52-R1 C10-C12)

Drafted 2 Oct 2026. Records: `check/records/S52/S52-R1-C10.yml`, `S52-R1-C11.yml`, `S52-R1-C12.yml`.
Figures (drawn by `draw.py --book S52-R1 --out` scratch, only my two copied in): `check/figures/s52-r1-c11-rows-left.png`,
`s52-r1-c12-bmi-cut-points.png` (+ `.spec.json`). Both looked at as images.

State at hand-back: `code_gate.py --check --no-cache` 0 failures on all three; `build.py --check` blocking 0,
and no warning names C10, C11 or C12 (others' records still missing at the time are not mine).

## Drill sets

- **C10**: not quantitative (inventory). No practice. Four exercises (design, critique, retrieval, teaching)
  and four retrieval items; `figure_note` (the products are a table and a text file).
- **C11**: 13 problems, levels 1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 8, 9, 10. Four verbs, each with its own silent
  trap (`== NA`, capital letters in a value, the English "or", the unassigned verb, sort direction); each
  trap gets a diagnostic. Figure: rows left after each pipe step (344, 176, 85).
- **C12**: 13 problems, levels 1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 8, 9, 10. One verb but many companion traps
  (units, case order, `.default` swallowing NA, stored value at a cut-point, round-half-even, overwriting a
  column, using a column before it exists). Figure: four made-up patients' BMI against the two NFHS-5
  cut-points, with patient 104 (no BMI) labelled.

## Unsourced or self-supplied

- C12: "1.6 has no exact binary form" is derivable and stated without a held source. The round() help page
  (held, quoted) supports the general point that the stored, not printed, number is what is rounded. The
  printed `24.999999999999996` is a gate-filled output, not a claim.
- C12: rounding BMI to one decimal before grouping is presented explicitly as a rule *chosen* because NFHS-5
  writes its cut-points to one decimal; the record says the fact sheet does not state its rounding rule.
- C10: Individual ID has 190 distinct values in 344 rows against the help page's "unique ID"; the record
  says the help page gives no reason and does not guess one. Species + Sample Number = 344 distinct.

## Things I am unsure of / decisions for reconcile

1. **BMI worked example on a made-up tibble.** The brief says worked examples use penguins_raw; BMI cannot be
   computed from the penguin file (no height), and the inventory requires BMI. C12 illustration 1-2 use a
   five-row made-up clinic register, said to be made up; illustration 3 is on penguins_raw.
2. **NFHS-5 cut-points** (`nfhs5_india_factsheet`, rows 87 and 89, kind `primary`, off-type and quoted) carry
   the 18.5 and 25.0 boundaries. Group labels are the ranges ("25 or more"), not the survey's words.
3. **Dictionary location**: C10 puts `penguins_raw_dictionary.csv` in `data-raw/`, typed by hand once, citing
   Wilson 4c ("raw data and metadata in a data directory"), and says no code ever writes to that folder.
   Check against C07's wording of the data-raw rule.
4. **`r norun`** is used once (C12 practice 3 prompt) to show code whose output the reader predicts, not for
   a personal path or install. If the conductor prefers, move that code into prose.
5. **The dplyr masking message** prints in every practice prompt that loads dplyr (gate-correct, but it is
   repeated noise on many pages).
6. **The help page's "statment"** (case_when) is quoted as spelled; noted in the reference.
7. C11 uses `count()` (C14/C16 territory) in two answers and C10 uses `count()` and `n_distinct()` (C19
   territory), each with a one-line gloss and a help-page citation.

## SELFCHECK

Quotes all found by the build; each number cited states its number (NFHS 18.5 / 25.0, "344 rows and 17
variables"). Every printed number in prose was read off the gate-filled output. Non-code arithmetic
recomputed: 24/52 = 0.4615, 24/47 = 0.5106, 27/52 = 0.519; 64/1.6^2 = 25 on paper. §9: no person-first
breach; "overweight or obese" appears only as the fact sheet's quoted label. No `~` or `^` in prose outside
code and notation-layer exponents (`1.6^2`, `kg/m^2`).
