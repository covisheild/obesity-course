# Figure planner brief · S52-R1 (PIPELINE.md "Figure plan")

Repository `/home/claude/work/obesity-course`, branch `book/S52-R1`. Do not commit. Edit only the records
in your range, and only their `figures:`, `figure_note` and `derived` entries — never their prose
(the compression pass has fixed it; a compression that removed a number a spec used is a spec to
fix, never a sentence to restore). Write figure files only under `check/figures/` with names
`s52-r1-cNN-<what>.png`.

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
- Run `python check/figures/draw.py --book S52-R1` (it redraws every S52-R1 figure; another planner
  runs it at the same time on other records, which is harmless) and `python check/build.py --check`
  until no record in your range blocks. Then open each of your PNGs with the Read tool and look:
  overlapping labels, a legend over the data, an unreadable axis, a line that says something the
  section does not. Fix the spec and redraw; never edit a PNG.

Scratch in `/tmp/claude-0/scratch-fig-<batch>/`. Write `books/S52-R1/FIGURES-<batch>.md`: per
section, the figures (file, what it shows, the check that holds it) or the figure_note. Return at
most 150 words: figures per section, figure_notes, anything you could not make correct.

**This book (S52-R1) teaches R.** Good figures are the data a section's code computes: counts, missing-value
tallies, rows left after each step, group summaries, bin counts, a join's row counts, BMI against cut-points.
Every number a figure plots must appear in the record's prose, a table, or a gate-filled output block (copy it
into a ```table block if the spec needs one; never retype a number that is not printed somewhere in the record).
Never a ggplot screenshot: figures are drawn only by check/figures/draw.py. The cold reader found figure
captions citing "the first illustration", "the second example's pipe" or "the example" that the reader cannot
identify (C11, C12, C16, C18, C19): make every caption name what it shows in the section's own words. Known
items: C11 bar label needs a redraw (reconciler note). R4DS and Broman & Woo's typeset article are
CC BY-NC-ND: do not redraw their figures.
