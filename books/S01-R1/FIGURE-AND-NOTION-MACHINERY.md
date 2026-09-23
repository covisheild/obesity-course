# Figure and Notion machinery (23 September 2026)

Two standing instructions from Harsh, built into the repository so no book chat needs telling again.

## A. Figures: more of them, in the book's colours, correct and tied to the text

**Theme.** `check/figures/figspec.py` `palette_for(book_id)` takes the book's Part from
`map/BOOKS.yml`, the Part's hue from `check/pdf/series.yml`, and runs it through the same `theme()`
the PDF cover uses (`check/pdf/make_pdf.py`). Marks and text are darkened until they reach WCAG
contrast on white (4.5:1 for anything carrying text, 3:1 for axes). The second series is 150 degrees
round the wheel at a different lightness, and the third is the book's dark ink, dashed. Axes are
neutral grey and the grid is light grey. `style_for(book_id)` in `check/figures/draw.py` returns
the palette plus matplotlib rcParams: the PDF's own Inter face (unpacked once from the bundled WOFF
into gitignored `check/_build/fonts/` with fontTools, falling back to DejaVu Sans), light spines,
y-grid only, and 220 dpi on a white ground. S01-R1 comes out blue (hue 212), with primary #2066b6 at
5.8:1 and secondary #981a16 at 8.4:1. Book 0's twelve PNGs and their drawing functions are
unchanged; `python check/figures/draw.py` with no arguments still draws exactly those.

**Spec: the numbers have one source.** `figures[].spec` has been added to
`check/schema/concept.schema.json`, with a worked template in `check/schema/example.concept.yml`. It
holds:

- `kind`: line, scatter, bar or step.
- The data: `from_table` (the record's own ```table block, by index and columns) or `x` and `series`.
- `relations`: a `fit` such as `y = 92 - 0.5*x`, which can also be drawn, or a `check` such as
  `sum(y) = 91`.
- `labels`: text placed on the figure.
- `derived`: numbers the figure prints that the prose does not state, each with its arithmetic.

`python check/figures/draw.py --book <ID>` checks each spec, refuses to draw one that fails, and
draws the rest. It writes `<file>.spec.json` beside each PNG, holding a SHA-256 of the resolved spec
and the palette.

**Blocking build checks** (`check/build.py` calls `figspec.verify` and `figspec.stale`). The build
blocks when:

- a number the figure plots or prints is neither stated in the record's reader-facing text nor
  derived correctly. This covers data, labels, legend keys, axis titles, caption, alt text and
  relation constants. Digits and number words both count, exponents and log bases are ignored, and
  values are compared as absolute values.
- a `fit` misses a plotted point at the precision the point is written to.
- a `check` identity is false.
- a bar axis does not start at 0, or a log axis holds a value ≤ 0.
- the PNG's fingerprint does not match the current spec and text.
- a figure outside Book 0 has no spec.

Book 0's figures without specs get one grandfather warning. A section outside Book 0 with no figure
and no `figure_note` (new schema field) gets a warning while it is drafted and blocks at
`verified` or `released`.

**Rules written in:** `PIPELINE.md`:

- run order,
- the Task 2 drafter prompt,
- the Task 3 auditor prompt (open every PNG and recompute every plotted or printed value),
- a new "Figure plan" step after Task 5 and before Task 3, in which the conductor looks at every figure as an image,
- the Task 7 table.

Also written into `CONDUCTOR.md` (the run table is now 10 rows, plus a figures paragraph), `check/SELFCHECK.md` (items 15–18) and `claude.md` §4 "Figures" (plus its blocking and warning check lists).

**Proof** (dummy S01-R1 records in a scratch directory, since removed):

- The correct spec had 5 points from a table, `fit y = 92 - 0.5*x`, `check y[0] - y[-1] = 4`, and derived 4 and 5. `verify` returned no problems, and the build's `check()` gave 0 figure blocks. The figure drew in the S01 blue with Inter.
- The deliberately wrong spec had slope 0.6, a total of 5 and a caption saying 95 kg. The build's `check()` gave 5 blocks: caption 0.6 and 95 not in the text, relation constant 0.6 not in the text, the fit missing the points at x = 6 and x = 8, and the check false (left side 4).
- Editing the table after drawing made `stale` report the PNG as drawn from older text. Unedited, it reported the PNG as fresh.

**Build:** 0 blocking before and after. Warnings went from 211 to 222: one Book 0 grandfather line,
plus ten S01-R1 drafted sections that have no figure or `figure_note` yet. The figure plan step
clears those ten.

## B. Notion

`NOTION.md` (repo root) records:

- the tracker's ids: the dashboard page, the data source `collection://21657754-…`, and the child database "Book 0 · sections";
- its properties;
- a table mapping each pipeline step to Stage, Citations and the other properties. Compression now precedes the audit, so the order of the Stage options is historical.

The conductor updates the unit's row at every phase boundary, at the same moment as Harsh's one-line message, and at finish: Stage Released, Citations Verified, Blocker empty, Notes with the main commit. It also updates the dashboard's status line if the page has one. If Notion is unreachable, it never blocks the book: the gap goes in `STATE.md` and the row catches up at the next boundary. `NOTION.md` is referenced from `CONDUCTOR.md` §0 (step 7), §1 ("While running") and §3 (step 6), and from `PIPELINE.md` "Running a Part without waste" rule 10.

## Caveats

- The number check is a presence test. It proves every printed number is stated or derived in the
  text, not that it is the *right* one in the right place. The auditor's recompute covers that.
- Fit tolerance is half a unit in the last written place, so integer data pass a fit that rounds to
  them (y = 90.8 against a plotted 91).
- Signs are compared as absolute values.
- Word-number matching can flag a count in alt text ("five points") until it is stated or derived,
  for example with `{value: 5, from: "len(x)"}`.
- The fingerprint covers the spec, the text-derived data and the palette, not the drawing code.
  Bump `SPEC_VERSION` in `check/figures/figspec.py` when the drawing changes.
- The Notion property names are taken from the brief, not read from Notion. `NOTION.md` asks the
  first chat to confirm them.
