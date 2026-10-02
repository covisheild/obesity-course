# Figure planner brief · S58-R1 (PIPELINE.md "Figure plan")

Repository `/home/claude/obesity-course`, branch `book/S58-R1`. Do not commit. Edit only the records
in your range, and only their `figures:`, `figure_note` and `derived` entries — never their prose
(the compression pass has fixed it; a compression that removed a number a spec used is a spec to
fix, never a sentence to restore). Write figure files only under `check/figures/` with names
`s58-r1-cNN-<what>.png`.

Read `claude.md` §4 "Figures" (it now documents `curves`, `areas`, `refs`, negative bars and
per-series colours) and `check/schema/example.concept.yml` (its `figures:` block). Then, for each
record in your range, which now carries its compressed text:

- **At least one figure a section; more is welcome** (Harsh's standing instruction: more figures
  than Book 0, each mathematically correct and matching its text). Where a figure would teach
  nothing the prose does not, write one line in `figure_note` instead. A quantitative section
  always gets a figure of its worked relationship: the curve its formula draws, the area its
  integral is, the point where a rate is zero, the weighted sum's parts.
- Start from the drafter's specs. Each figure is a `figures:` entry with a `spec`: data from the
  record's own ```table block where there is one (`from_table`), otherwise listed in the spec; every
  number it plots or prints (data, labels, caption, alt text, axis titles, constants, endpoints)
  stated in the record's prose or worked out under `derived`; every relationship drawn a `fit`,
  `curve`, `area` or `check`. The caption says what the reader should see, in the section's terms.
- Run `python check/figures/draw.py --book S58-R1` (it redraws every S58-R1 figure; another planner
  runs it at the same time on other records, which is harmless) and `python check/build.py --check`
  until no record in your range blocks. Then open each of your PNGs with the Read tool and look:
  overlapping labels, a legend over the data, an unreadable axis, a line that says something the
  section does not. Fix the spec and redraw; never edit a PNG.

Scratch in `/home/claude/scratch-s58-fig-<batch>/`. Write `books/S58-R1/FIGURES-<batch>.md`: per
section, the figures (file, what it shows, the check that holds it) or the figure_note. Return at
most 150 words: figures per section, figure_notes, anything you could not make correct.

**This book (S58-R1) is mostly not mathematical.** Good figures here are data from held sources
(a study's two group means, Frich's counts, Cepeda's gap-by-retention results, a schedule on a
timeline, a session plan's minutes as bars) or a worked example's own numbers. Never invent data
to have a figure; an invented illustrative table already in the prose (labelled as invented) may be
drawn, with the caption saying the numbers are invented. Deslauriers 2019 is CC BY-NC-ND: do not
redraw its figures or tables. Mean sentence length of the prose is fixed by the compression pass;
captions and alt text are yours but keep them short.

## S58-R1 specifics
- Read `books/S58-R1/RECONCILE.md`, section "For the figure planner" (figure wishes the tool cannot
  draw; the greyscale problem) and `books/S58-R1/DEFECTS.md` only for figure-related holes in your
  range (e.g. a figure describing a worked example the compressed text no longer shows: fix the
  figure or its caption so it says only what the text gives; never restore prose).
- **Greyscale.** For this book's hue the palette's primary (#b6206b) and secondary (#138613) have
  the same greyscale lightness (both about 85 of 255), so two-series figures merge in grey — what C19
  teaches against. This is a fault in `check/figures/figspec.py` `palette_for` (a contract file,
  frozen while books run; the conductor reports it). Do not pick colours by hand and do not edit
  `draw.py` or `figspec.py`. Instead, where a figure has two series, make it readable without
  colour: direct labels on the marks or line ends, different markers where the spec allows, or one
  series per panel/figure; or use the tertiary series (dark ink, dashed) as the second where the spec
  lets you order series. Convert each such PNG to greyscale in Python (PIL `convert("L")`), look at it,
  and record the result in your FIGURES file.
- `draw.py` does not substitute `{{n:key}}`: a number a spec uses must appear literally in the
  record's prose (outside the placeholder) or be worked out under `derived`. The build blocks
  `kind: dataset` references; use the kinds the build accepts.
- Blocking now (build after compression): S58-R1-C18 `s58-r1-c18-where-they-looked.png` (caption
  states 2010 not in the text) and S58-R1-C22 `s58-r1-c22-anaemia-two-rounds.png` (differences 8.5,
  3.9, 1.9, 2.3 not in the text): fix by `derived` entries or by changing the spec, not the prose.
- The book is about honest figures: every figure must itself pass the book's rules (zero-based bars,
  axis titles with units, direct labels where possible, a caption that states the finding, no
  decoration, colour only for meaning). A figure that breaks a rule the book teaches is a defect.
