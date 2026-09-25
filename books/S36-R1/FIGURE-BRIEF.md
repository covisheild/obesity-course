# Figure planner brief · S36-R1 (PIPELINE.md "Figure plan")

Repository `/home/claude/obesity-course`, branch `book/S36-R1`. Do not commit. Edit only the records
in your range, and only their `figures:`, `figure_note` and `derived` entries — never their prose
(the compression pass has fixed it; a compression that removed a number a spec used is a spec to
fix, never a sentence to restore). Write figure files only under `check/figures/` with names
`s36-r1-cNN-<what>.png`.

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
- Run `python check/figures/draw.py --book S36-R1` (it redraws every S36-R1 figure; another planner
  runs it at the same time on other records, which is harmless) and `python check/build.py --check`
  until no record in your range blocks. Then open each of your PNGs with the Read tool and look:
  overlapping labels, a legend over the data, an unreadable axis, a line that says something the
  section does not. Fix the spec and redraw; never edit a PNG.

**This book is qualitative.** Most sections teach a practice, not a quantity. The drawing tool plots only data (bars, lines, points, curves, areas) and **must not be edited** (`check/**` is frozen mid-flight under `PARALLEL.md`). So a figure is right where the section has real numbers or counts in its own text (a talk share, hours of transcription, a time plan, counts of question types in a made-up guide, word counts before and after cleaning a transcript) and teaches something; never invent numbers to make a chart, and never draw a chart of a qualitative idea dressed up as data. Where no honest figure exists, the `figure_note` names the diagram a reader would want (a flow of steps, a spectrum) in one line. The C10 spec broke in the compression (its `from_table` block index); fix it.

Scratch in `/home/claude/scratch-fig-<batch>/`. Write `books/S36-R1/FIGURES-<batch>.md`: per
section, the figures (file, what it shows, the check that holds it) or the figure_note. Return at
most 150 words: figures per section, figure_notes, anything you could not make correct.
