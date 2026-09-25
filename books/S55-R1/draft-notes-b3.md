# S55-R1 draft notes, batch b3 (C05, C06)

## Records written

- `check/records/S55/S55-R1-C05.yml`: A question whose answer would change something (derivable)
- `check/records/S55/S55-R1-C06.yml`: What happens to studies once published: citation, uncitedness and use (empirical)

`python check/build.py --check`: blocking 0, no warnings for either record (run 2026-09-25, after
C01, C03, C04 and C07 were on disk; C05 lists C02 in `concept_deps`, which blocked until C02
landed). `python check/figures/draw.py --book S55-R1`: 0 problems.

## Sources and support

- **C05** textbook anchor: `jhangiani_2019_methods` (interestingness: answer in doubt, fills a gap,
  practical implications; refining a studied question). Primary: `ioannidis_2016_useful` (useful
  research = better decision; Table 1 problem base, context placement, information gain; useful
  whatever the result; questions lose importance), `ioannidis_2014_waste` (duplicative studies,
  design in isolation). Ioannidis's "85%" is not stated. Blackstone ch. 4 not needed.
- **C06** every figure carries database, year of publication and window, each quoted:
  - 55%, items published 1981 to 1985, 5-year window (1990 Science report, through Van Noorden).
    **The feature does not name the database the 1990 report used; the record says so.**
  - 4%, biomedical research articles and reviews published 2006, Web of Science, to December 2017.
    "Today" in the feature is read as its date, 14 December 2017 (quoted page foot).
  - 21%, 39 million papers of all fields 1900 to 2015, Web of Science, to December 2017.
  - 12%, medical-science papers of 1990, 27-year window, from Golosovsky and Larivière reporting
    Sugimoto and Larivière 2018 (not held). **The held text does not name the database for this
    figure; the record says "not named in the paper that reports it".** The inventory's "Web of
    Science" for it is not written.
  - Nowroozzadeh 2019 (five journals, Web of Science): 46.0 / 16.1 / 8.3 for 1990 papers and
    18.9 / 2.7 / 0.7 for 2010 papers, first year, second year, five years. The letter prints no unit;
    read as per cent from its chart axis ("Uncited articles, percent"); noted in the record.
  - The reader is told the Larivière–Sugimoto figures reach us through a news feature whose chart
    data were withdrawn, and through a book the course has not checked.
- The O3 sentence appears only as a quoted sentence "from the outline this course was planned
  from", tested against the table and shown to have no row. "No open study was found that counts
  citations by study design" is a statement of the intake's search, not a sourced claim.
- Not used: Patsopoulos 2005, Chalmers & Glasziou, the "85%", Farrugia, NMC regulations.
- Van Noorden (all rights reserved), Ioannidis 2014 and Nowroozzadeh (no open licence): short
  quotations only; no chart or table reproduced. The C06 figure plots six numbers from
  Nowroozzadeh's running text (not its figures), redrawn by `draw.py`. **Harsh / conductor may want
  to confirm that plotting six numbers from an unlicensed letter's text is acceptable as fact
  reuse.**

## Judgements for the conductor

- C05's third test ("would the answer change anything?") overlaps C07's who-is-waiting test. C05
  stops at "write each answer and what someone would do"; it does not ask who, and names no
  later section. C07 already cites C05.
- C06 must-know 6 (claims about citation by design) carries no `refs`; it rests on the absence of
  a study, which no source can carry.
- C06 illustration 2 reads "in the second year" as year 2 on the x axis; the letter's wording
  ("in the first year of publication", "in the second year", "at five years after publication")
  is followed in the prose. The drawn line joins three points only; it implies nothing between them
  but a reader may read it so.

## Practice-set sizes

Neither concept is quantitative (inventory: C05 no, C06 no); `quantitative: false`, no `practice[]`.

## Figures

- C05: `figure_note` (the two-by-two is a four-cell table with reasons; a drawing would repeat it).
  If the figure planner wants one: a 2 x 2 grid, "answerable by you" against "worth answering",
  with Q1–Q4 placed in their cells. `draw.py` has no grid kind.
- C06: `s55-r1-c06-window.png`, line chart from the illustration's second table (block 1): mean
  share uncited by year after publication (1, 2, 5), papers of 1990 and of 2010, five journals, Web
  of Science. Looked at: correct values, bars n/a, x ticks at half-years (1.5, 2.5 ...) are the
  tool's default and slightly odd for whole years.

## Arithmetic recomputed

- 46.0 ÷ 8.3 = 5.542, printed as 5.5 and "five and a half times" (Python).

## Glossary rows (proposed; none of these is in `prose/GLOSSARY.md`)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| citation | an entry in the reference list of a later published work that points to an earlier one | `S55-R1-C06` |
| citation database | a database that records the reference lists of the journals it indexes and counts the citations to each paper it holds | `S55-R1-C06` |
| citation window | how long after publication the counting of citations runs | `S55-R1-C06` |
| context placement | Ioannidis's feature: earlier evidence has been assessed before the new study is planned | `S55-R1-C05` |
| information gain | Ioannidis's feature: the study is large and long enough to tell us something | `S55-R1-C05` |
| problem base | Ioannidis's feature: the health problem is big or important enough to fix | `S55-R1-C05` |
| uncited | (of a paper) no citation found to it in a given database by a given date | `S55-R1-C06` |
| uncitedness ratio | the share of a set of papers still uncited at the end of the citation window (Golosovsky and Larivière's term) | `S55-R1-C06` |
| worth answering | (of a research question) the answer is in doubt, not already known, and would change what someone decides or does | `S55-R1-C05` |
