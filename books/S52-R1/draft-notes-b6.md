# Draft notes, batch b6 (S52-R1 C16-C18)

Drafted 2-3 Oct 2026. Records: `check/records/S52/S52-R1-C16.yml`, `S52-R1-C17.yml`, `S52-R1-C18.yml`.
Figures (drawn by `draw.py --book S52-R1 --out` scratch; only my three copied in, with `.spec.json`):
`check/figures/s52-r1-c16-mass-by-species.png`, `s52-r1-c17-nhanes-join-rows.png`,
`s52-r1-c18-mass-histogram.png`. All three looked at as images (bars from zero, labels clear).

State at hand-back: `code_gate.py --check` 0 failures on all three (14, 13, 13 sessions);
`build.py --check` blocking 0 (148 records). Remaining warnings on my records are seven sentences of
26-34 words in exercises and practice (listed in `check_report.md`), no grade or structure warnings.

## Drill sets

- **C16**: 12 problems, levels 1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 9, 10. One verb, but three silent traps
  (n() counts rows not values used; leftover grouping changes a percentage's denominator; quartile
  rules differ between Book 0, R type 7 and SPSS type 6) plus writing the table by code.
- **C17**: 11 problems, levels 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10. Two moves (reshape, join), each with
  its silent failure (mixed-unit value column; duplicate key; natural join on a shared `year`; key
  type mismatch, the last marked `error`).
- **C18**: 12 problems, levels 1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 9, 10. Plots print no text, so levels 1-3
  are reading code and bin-edge reasoning (non-code answers recomputed by hand: 2/3 and 2/2/1 values
  per bin), and the gate-checkable evidence is the warnings ("Removed 2 rows") and companion
  summaries.
- Each record also has a calculation, a critique and a retrieval exercise (C16 and C18 a teaching
  one too), and four or five retrieval items.

## Sources and claims worth an auditor's look

1. **quantile() and NA**: the definition says `quantile()`/`IQR()` stop with an error on NA without
   `na.rm`. The help page's Arguments sentence is quoted; the exact error text was confirmed by running
   R 4.3.3 in the sandbox (stated in the reference note).
2. **SPSS uses type 6**: quoted from the quantile help page only ("This is used by Minitab and by
   SPSS."); the prose says "said to be SPSS's" in the table and does not claim to have tested SPSS.
   Book 0's halves method agreeing with type 6 is shown on the nine made-up heights only, and said not
   to be a rule.
3. **ggplot2 rendering claims** (C18): the pinkish-red points and the legend "colour: blue" were seen
   on a PNG rendered in the sandbox (3.4.4); the source for the rule is the SWC tip ("should work, but
   it doesn't") and R4DS 1.5.1 (map vs set). `geom_point()`, `geom_bar()` and `labs()` help pages are
   not held; R4DS ch. 1 is cited for what a geom is (CC BY-NC-ND, quoted briefly only).
4. **Version notes** (C18): ggplot2 4.0.0 default bin boundary and 3.5.0 `ggsave()` directory change
   quoted from `tidyverse_news_s52r1`; neither tested (sandbox has 3.4.4). The record says bins left on
   defaults "can change shape" on a newer version, no more.
5. **NHANES** (C17, C18 L10): every summary is said to be unweighted and to estimate nothing about the
   US population, with the BMX_L "Sample weights" sentence quoted. RIAGENDR 1 = male, 2 = female from the
   codebook table. Standing height "2 years and older" and recumbent length "birth through 47 months"
   (C17 L6) are in the BMX_L documentation block (cited by `refs`, not quoted in the definition).
6. **R4DS quote with a code break** (C16, C17): the held R4DS text breaks sentences around code
   spans, so two quotes end or start mid-sentence ("...include a count (" and ", it fills in the new
   variables with missing values."); the notes say so.
7. "Gorman, Williams and Fraser" in a ggplot caption string (code) comes from the horst file header.

## Decisions and things I am unsure of

- **Output folder**: the gate's scratch project has no `output/`, so every block that writes there
  first runs `dir.create(here::here("output"), showWarnings = FALSE)`, with one sentence saying the
  reader's own project already has it. C18 ties this to the ggplot2 3.5.0 change. If C07/C21 prefer
  another idiom, reconcile.
- **Short species names**: C16 and C18 illustrations remake C12's `case_when()` short names in the
  session (pointing back to the section on making new columns); practice prompts use the raw file's
  long names to keep each prompt short.
- **Histogram bins**: C18 uses `closed = "left"` so that a dplyr `floor()` count reproduces the bars
  exactly (left-closed both ways); the default right-closed rule is taught and drilled (L3). The figure
  is drawn from that count table, per the brief.
- **numbers.yml**: added `demo_rows` (11933), used in C17 prose; b7 had already added
  `nhanes_adults_rows` (6064), which C17 uses. 8860 uses the existing `bmx_rows`. Numbers inside tables
  and the `working` block are typed literally (figspec reads the table).
- C16's critique answer names "the section on running a whole script with one command" (C21) as a
  later section with a gloss, not a recall.
