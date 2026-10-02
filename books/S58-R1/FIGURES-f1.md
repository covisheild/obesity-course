# Figure plan, batch f1 (S58-R1-C01 to C06)

Drawn by `python check/figures/draw.py --book S58-R1`; `python check/build.py --check` shows no
blocking item for C01-C06 (the 5 remaining blocks are C18 and C22, other batches). Every PNG below
was opened and looked at, and converted to greyscale (PIL `convert("L")`, copies in
`/home/claude/scratch-s58-fig-f1/`). All three are single-series, so the primary/secondary
greyscale merge does not arise; marks and labels read clearly in grey.

## C01 · What a research paper is
- `s58-r1-c01-imrad-adoption.png` (scatter, unjoined points): share of original articles in IMRAD,
  0 in 1935, 20 in 1955, 100 in 1985 (Sollaci and Pereira 2004). Numbers from illustration 2's
  prose; 100 is stated there ("100 per cent"). Changes: y_range [-5, 106] so the 1935 and 1985
  points no longer sit on the frame (RECONCILE cosmetic note; y_range is display only, not a
  number the figure states); labels moved beside their points; caption now states the finding
  first and names the source and the four journals (closes DEFECTS A-01-2). The 1970s "over 80
  per cent" is not plotted, since it names no year; the caption says so.

## C02 · A paper is an argument
- `s58-r1-c02-unusable-reports.png` (bars from zero, value labels): 60 vs 90 per cent of trials
  with adequate information on the treatment. Added a dashed reference line at 90 and a direct
  label "30 points known but not reported" in the gap above the first bar. Check
  `y[1] - y[0] = 30` holds. Caption now glosses "adequate" in the prose's own terms (what the
  treatment was and how it was given; DEFECTS A-02-2, partly) and says the figures are not
  Chalmers and Glasziou's own measurement. A-02-3 (name the primary study) is left open: the
  record does not hold that study, so the caption cannot name it.
- Not drawn: the critique exercise's register counts (640, 410, 152, 96) would hand the reader
  the exercise's answer. The NFHS change in illustration 1 is held only as `{{n:}}` keys.

## C03 · The one message
- figure_note kept: the section's work is one sentence, a title and an abstract; its NFHS numbers
  are `{{n:}}` keys and its only literal counts (36 characters against 40) teach nothing as a chart.

## C04 · The argument across sections
- figure_note rewritten (the old one wrongly said a chart would need made-up numbers): the figure
  the section wants is the funnel-and-mirror diagram of the moves, which draw.py cannot draw; the
  outline table lays the moves out; its NFHS numbers are number-file keys a spec cannot use
  (C14 draws the urban-rural comparison).

## C05 · Citing and referencing
- New: `s58-r1-c05-first-mention-numbers.png` (bars from zero, categorical x, value labels): the
  reference number printed in each of the five sentences of illustration 2's made-up draft, 1, 2,
  1, 3, 4 (A, B, A again, D via Table 1, C). Check `y[2] = y[0]` (a source keeps its first
  number). Caption says the draft is made up. A scatter was tried first; its numeric x printed
  half-sentence ticks (1.5, 2.5), so it became a categorical bar chart. The old figure_note was
  removed.
- Not drawable: the annotated reference (RECONCILE C05 wish); the element table carries it.

## C06 · The parts of a sentence
- figure_note rewritten: the section teaches by marking sentences in the text; draw.py cannot draw
  a marked-up sentence (RECONCILE C06 wish), and its one count (13 words) is a single number;
  C07 charts the subject-verb gap in four sentences.
