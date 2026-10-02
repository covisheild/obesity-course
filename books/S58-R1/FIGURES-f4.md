# Figures, batch f4 (S58-R1-C19 to C23)

Run 3 Oct 2026: `draw.py --book S58-R1` drew 29 figures, 0 problems. `build.py --check` shows no
block in C19 to C23. The remaining S58 blocks are stale PNGs in C11, C16 and C17, which belong to
other batches. Every PNG below was opened and looked at. The two-series and curve figures were also
looked at in greyscale (PIL `convert("L")`).

## C19
- `s58-r1-c19-cvd-boys.png`: Krishnamurthy's rural, urban and all-schools per cent as bars from zero
  (`from_table` block 0, column 3), each with its value printed on it, and a dashed ref at 8 for the
  worldwide estimate for men. The caption is rewritten so the finding comes first ("about one boy
  in 36", which is in the text). It has one series, so greyscale is not an issue.
- Tried and dropped: a band for the block range from 1.12 to 3.40. It added a legend ("per cent")
  and its edge line struck through the 3.17 label.

## C20
- `s58-r1-c20-three-error-bars.png` (unchanged): the arm lengths 12.0, 6.93 and 27.7 as bars. Its
  checks are `y[0]/y[1] = 1.732` and `y[2]/y[1] = 4`.
- **New** `s58-r1-c20-se-shrinks.png`: the curve `y = 12.0 / sqrt(x)` from n = 3 to 40, tied to the
  points (3, 6.93) and (40, 1.90), with a ref at the SD of 12.0. The 1.90 is derived as 12.0 / 6.32
  (6.32 is the text's √40). The caption says the SD is held at 12.0 as an assumption. In grey, the
  curve (mid-grey, dashed) and the SD ref (black, dashed) carry direct labels.

## C21
- figure_note kept: the section teaches tables, and a chart of the same numbers would show one
  result twice.

## C22 (was blocking)
- `s58-r1-c22-anaemia-two-rounds.png`: the blocking differences now sit under `derived` (8.5, 5.0,
  3.9, 1.9 and 2.3, each worked as NFHS-5 minus NFHS-4), and the five `check`s hold.
- The caption now reads "in each of the five groups shown, by 1.9 to 8.5 percentage points".
  DEFECTS 12a: the old wording claimed the rows that were left out.
- The series are unnamed, so there is no legend, and each bar's value is printed on it.
- Greyscale: the two series come out at 85 and 87 of 255, the same grey. The figure still reads in
  grey, because NFHS-4 is always on the left, "NFHS-4" and "NFHS-5" are named over the first pair,
  and every bar carries its value.

## C23
- `s58-r1-c23-three-drafts.png`: now `from_table` (block 0, FRE column). The ref label covered the
  third bar, so the line is now explained by a note in the empty top-left corner. The caption now
  leads with the finding ("The worst draft passes").
- **New** `s58-r1-c23-sentences-and-words.png`: a scatter of ASL against ASW for the three drafts
  (`from_table` block 0, columns 4 and 5), with each point labelled directly. It shows that the cut
  has longer sentences but shorter words. The caption says that, as points, neither axis starts at
  zero.

## Not fixable within the brief
- C22's step 6 and its figure sheet ask for two colours that differ in lightness. Its figure cannot
  do that until `figspec.palette_for` is fixed, and that file is frozen.
