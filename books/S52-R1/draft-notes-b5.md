# Draft notes, batch b5 (S52-R1 C13-C15)

Drafted 2 Oct 2026. Records: `check/records/S52/S52-R1-C13.yml`, `S52-R1-C14.yml`, `S52-R1-C15.yml`.
Figures (drawn by `draw.py --book S52-R1 --out` scratch; only my two copied in, both looked at as images):
`check/figures/s52-r1-c13-rows-kept.png`, `s52-r1-c14-island-counts.png` (+ `.spec.json`). C15 has a
`figure_note`.

State at hand-back: `code_gate.py --check` 0 failures on all three; `build.py --check` reports no blocking
problem and no warning naming C13, C14 or C15 (the blocking left belongs to records other batches are still
writing).

## Drill sets (11 each)

- **C13**: levels 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10. Three short moves (count, na.rm, drop_na), each with its
  own silent error: a code left as a number (999), a code that turns a column into text ("not recorded"),
  `drop_na()` on every column (keeps 34 of 344 because of `Comments`), an n taken from the row count.
  Figure: rows kept by four choices (344, 342, 333, 34).
- **C14**: levels 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10. Five functions, one move each; traps: silent NA from
  `factor()`, misspelt old level in `fct_recode()` (warning), labels swapped against the dictionary, and a
  two-way count read as a statement about where penguins live. Figure: island counts in `fct_infreq()` order.
- **C15**: levels 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10. Parsing by order, date as day count, subtraction, age;
  the three ways parsing fails (all NA; some silently wrong; spreadsheet day count from the wrong start) each
  get a diagnostic.

## Unsourced, self-supplied or worth an auditor's look

1. **C15, Excel day counts.** Data Carpentry says Excel "counts the days from a default of December 31,
   1899, and thus stores July 2, 2014 as the serial number 41822". Taken literally the two halves disagree by
   a day (`ymd("1899-12-31") + 41822` prints 2014-07-03). The record shows this with gate output, uses 30
   December 1899 because it reproduces the lesson's one example, says it was not checked before March 1900
   or for Mac files, and does not give the cause (no held source states it). R4DS 20.2.6 says "days since
   January 1, 1900", a third wording; not cited.
2. **C15, base `as.Date()` / difftime help pages are not held.** Date arithmetic is cited to R4DS 17.4.1
   ("when you subtract two dates, you get a difftime object") and shown by gate output. "A date plus a
   number is that many days later" rests on gate output only. The day count behind a Date (18720 for
   2021-04-03) is gate output plus R4DS 17.2.4 (offsets from 1970-01-01).
3. **C14, base `factor()` help page is not held**: `factor()` is cited to R4DS 16.2 (silent NA, alphabetical
   levels) and shown by gate output.
4. **C13 introduces `summarise()` and `n()`** (cited to their help pages) in one sentence, with "a later
   section uses it for groups". C16 owns `summarise()`; see notes-for-others. `across()` is not used
   (S52-R2 P1 per the amended map); per-column counts use `colSums(is.na())`, as C09 already did.
5. **C15, 365.25 and `floor()` for age**: flagged in the record as a rule of thumb that can be a day out at
   a birthday; exact calendar ages (lubridate intervals) are said to be not covered.
6. **Dates rule from two sources** (intake log-a finding 4): Broman & Woo's ISO 8601 and Data Carpentry's
   separate columns are given side by side, not merged.
7. **Tibble rounding**: several means print rounded (`4202.`, `201.`, `63.7`); the prose quotes the printed
   value and says the tibble rounds to fit, never a digit the output does not show.
8. C14's two-way table (species by island) is a ```table typed from the gate-filled `count(..., .drop =
   FALSE)` output; C14's island table likewise. C13's rows-kept table is from four gate-filled `nrow()`s.

## Self-check

Quotes: all found by the build; numbers in quotes stated (41822, 19.6 %). Non-code arithmetic recomputed in
Python: 185/3 = 61.67, 11/344 = 3.2 %, 168/333 = 50.5 %, 2+2+14+13 = 31, 4207.057 - 3877.206 = 329.851,
days 1970-01-01 to 2021-04-03 = 18720, 1899-12-30 to 2014-07-02 = 41822, median of 11, 14, 14, 18, 28 = 14.
Every printed number in prose was read off the gate output. §9: no weight language beyond made-up registers.
No `~` or `^` in prose. All examples on made-up registers say they are made up.
