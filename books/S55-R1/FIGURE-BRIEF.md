# Figure planner brief · S55-R1 (PIPELINE.md "Figure plan")

Repository `/home/claude/obesity-course`, branch `book/S55-R1`. Do not commit. Edit only the records
in your range, and only their `figures:`, `figure_note` and `derived` entries — never their prose
(the compression pass has fixed it; a compression that removed a number a spec used is a spec to
fix, never a sentence to restore). Write figure files only under `check/figures/` with names
`s55-r1-cNN-<what>.png`.

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
- Run `python check/figures/draw.py --book S55-R1` (it redraws every S55-R1 figure; another planner
  runs it at the same time on other records, which is harmless) and `python check/build.py --check`
  until no record in your range blocks. Then open each of your PNGs with the Read tool and look:
  overlapping labels, a legend over the data, an unreadable axis, a line that says something the
  section does not. Fix the spec and redraw; never edit a PNG.

**This book is mostly qualitative.** Most sections teach a decision, not a quantity. The drawing tool plots only data (bars, lines, points, curves, areas) and **must not be edited** (`check/**` is frozen mid-flight under `PARALLEL.md`). A figure is right where the section has real numbers in its own text and teaches something: C06's citation figures (each with its database, cohort and window, as the text states them), C08's scores on the course's own sheet, C02's counts from its own worked material. Never invent numbers to make a chart, and never draw a qualitative idea dressed up as data. Where no honest figure exists, the `figure_note` names the diagram a reader would want in one line. **Known faults from the cold read** (books/S55-R1/DEFECTS.md): C02's and C08's figures describe worked examples that are not in the compressed text — make each figure's caption, alt text and data match what the text now holds, or replace the figure with one the text supports; never restore prose to fit a figure.

Scratch in `/home/claude/scratch-fig-<batch>/`. Write `books/S55-R1/FIGURES-<batch>.md`: per
section, the figures (file, what it shows, the check that holds it) or the figure_note. Return at
most 150 words: figures per section, figure_notes, anything you could not make correct.
