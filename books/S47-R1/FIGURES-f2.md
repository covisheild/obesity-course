# Figure plan · S47-R1 · batch f2 (C10–C18)

All figures drawn from specs; `python check/build.py --check`: 0 blocking. Every PNG opened and looked at.

**Tool gap (needs the conductor).** `check/figures/draw.py --book` does not apply the `{{n:key}}` substitution that
`build.py` applies, so any figure whose caption, alt text or data uses a number the prose writes only as
`{{n:key}}` (1,009; 18; 7) is refused as "not stated". The build itself, which substitutes, passes them. I drew
this batch with `/home/claude/scratch-fig-f2/draw_sub.py`, which loads the records, calls
`reader_checks.apply_numbers` as the build does, then calls the unchanged `figspec.verify` and `draw.draw_spec`.
It holds no figure data. Re-running plain `draw.py --book S47-R1` will print NOT DRAWN for these figures and leave
their PNGs alone. The PNGs stay valid, because the build's staleness hash matches.

## C10 · figure_note (unchanged)
A map of actors around one decision. The only counts are one study's interviews, which C13 draws.

## C11 · figure_note (unchanged)
A chain from Constitution to Act to notification. A flow diagram the tool cannot draw.

## C12 · figure_note (unchanged)
One sentence split into problem, cause, judgement and remedy. Its table already does this.

## C13 · 3 figures
- `s47-r1-c13-koon-issues.png`: Koon's seven issue counts. **Fixed:** the caption had claimed "the rest fell under
  other issues the review does not count separately", which is unsourced. It now says the seven counts add to
  37 and so do not cover all 52 articles. Check: `sum(y) = 37`, derived from 10+9+5+4+3+3+3.
- `s47-r1-c13-summan-interviews.png`: interviews by group. Check: `sum(y) = 18`. Integer axis (`y_range [0, 6]`).
- `s47-r1-c13-highest-lowest.png` (**new**): the toxic food environment at 77.5 and sinful behaviour at 50.5,
  against a 50 per cent line, to show that both are majorities. "Important" does not mean "the cause". The 50 is
  derived as 100/2.

## C14 · 2 figures
- `s47-r1-c14-model-share.png`: 0.08, 0.11, 0.18. Check: `1 - y[2] = 0.82`. The figure matches the text now held,
  including "beyond this book".
- `s47-r1-c14-four-measures.png` (**new**): support for four measures, 68.3, 63.0, 28.4 and 24.6, each tied to
  the account the text pairs it with.

## C15 · figure_note (unchanged)
A frame and its counter-frame, drawn as two columns of five slots.

## C16 · figure_note (unchanged)
The evidence premise and the value premise, drawn as an argument chain.

## C17 · 2 figures
- `s47-r1-c17-draft-and-rewrite.png`: draws from table block 2. Checks: 1+4 = 5 and 6+0 = 6. The cold-read fault
  (C17-1) is closed, because the compressed text now shows both the paragraph and its rewrite. The caption matches.
- `s47-r1-c17-range-to-top.png` (**new**): mark 2. The model's low end is 7 and its high end 30, and the draft
  wrote 30. Check: `y[2] = y[1]`.

## C18 · 2 figures
- `s47-r1-c18-drink-rates.png`: draws from table block 1. Checks: `y2[0] = 40` and `y1[0] + 12 = 40`. The caption
  matches the text, which says "a 2026 review" because the prose never names Summan.
- `s47-r1-c18-cess-folded.png` (**new**): line 4 of the draft. Before: 28 GST plus 12 cess makes 40. After: 40
  GST plus 0 cess makes 40. Checks: both sums, `y3[1] - y3[0] = 0`, and `y1[1] - y1[0] = 12`. The 0 is derived as
  12 - 12.
