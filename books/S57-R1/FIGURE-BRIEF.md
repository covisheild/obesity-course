# Figure planner brief · S57-R1 (PIPELINE.md "Figure plan")

Repository `/home/claude/obesity-course`, branch `book/S57-R1`. Do not commit. Edit only the records
in your range, and only their `figures:`, `figure_note` and `derived` entries — never their prose
(the compression pass has fixed it; a compression that removed a number a spec used is a spec to
fix, never a sentence to restore). Write figure files only under `check/figures/` with names
`s57-r1-cNN-<what>.png`.

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
- Run `python check/figures/draw.py --book S57-R1` (it redraws every S57-R1 figure; another planner
  runs it at the same time on other records, which is harmless) and `python check/build.py --check`
  until no record in your range blocks. Then open each of your PNGs with the Read tool and look:
  overlapping labels, a legend over the data, an unreadable axis, a line that says something the
  section does not. Fix the spec and redraw; never edit a PNG.

Scratch in `/home/claude/scratch-fig-<batch>/`. Write `books/S57-R1/FIGURES-<batch>.md`: per
section, the figures (file, what it shows, the check that holds it) or the figure_note. Return at
most 150 words: figures per section, figure_notes, anything you could not make correct.

**This book (S57-R1) is mostly not mathematical.** Good figures here are data from held sources
(a study's two group means, Frich's counts, Cepeda's gap-by-retention results, a schedule on a
timeline, a session plan's minutes as bars) or a worked example's own numbers. Never invent data
to have a figure; an invented illustrative table already in the prose (labelled as invented) may be
drawn, with the caption saying the numbers are invented. Deslauriers 2019 is CC BY-NC-ND: do not
redraw its figures or tables. Mean sentence length of the prose is fixed by the compression pass;
captions and alt text are yours but keep them short.
