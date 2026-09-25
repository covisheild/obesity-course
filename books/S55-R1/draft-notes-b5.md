# S55-R1 draft notes, batch b5 (revision: C02, C05, C06, C07)

This revision uses four sources taken in after the first drafts: `patsopoulos_2005`,
`chalmers_glasziou_2009`, `chalmers_2014_priorities` and `nicolaisen_frandsen_2019`. All four are
publisher copyright, so each quote is a phrase, a sentence or one table row. No quote comes from a
header or a `[NOTE]` line.

## What changed

**C06 (citation, uncitedness and use)**
- Nowroozzadeh 2019 is removed from the record, from the definition, illustration, must_know,
  exercise answers and figure alike. The letter prints its rates without a unit (the only unit is
  the chart axis). Kept nowhere, because its text gives no number in a stated unit.
- Added Nicolaisen & Frandsen 2019: Scopus, seven document types, papers of 1996 to 2015, citations
  counted to 6 December 2018 (an open window). Stated as the source states them, as uncitedness
  ratios: medicine, all seven types, 0.23 (Table 1 row); medical articles 0.18 and medical notes
  0.64 (Table 6, Medicine Total row, columns named in the ref note). Table 2 gives the same values
  in brackets, but the build's number reader skips a bracketed number, so Table 6 is quoted. The
  "about 22 years / about 3" for 1996 and 2015 papers is my arithmetic from the dates, not a quote.
- Added Patsopoulos 2005: Science Citation Index in Web of Science, 2646 articles of 1991 and 2001,
  design taken from the title, median citations to the end of the 2nd year after publication.
  Case reports lowest ("negligible citations"). **No cross-sectional category**, so the map's O3
  sentence stays unmeasured. The definition, the simplified explanation, illustration 1, the dispute
  must_know, the critique answer and a new retrieval item all say exactly that. The old line "no
  open study counts citations by design" is gone everywhere.
- Illustration 1's table: the Nowroozzadeh rows (8.3%, 0.7%) are replaced by the two Scopus rows.
  Illustration 2 (the Nowroozzadeh window example) is replaced by a table of Patsopoulos's 2-year
  medians for five designs (meta-analysis, randomised trial, cohort, case-control, case report),
  1991 and 2001. Each of the 10 numbers carries its table-row quote. It also shows one derived floor:
  a median of 0 for case reports of 1991 means at least half had no citation in 2 years.
- Figure: `s55-r1-c06-window.png` is replaced by `s55-r1-c06-medians-by-design.png`, a bar chart
  drawn from illustration 2's table (block 1), with value labels. I looked at the PNG: bars start at
  zero, and the numbers and labels match the table, the caption and the alt text. **The old
  `s55-r1-c06-window.png` and `.spec.json` are still tracked in `check/figures/`, and no record uses
  them now.** I left them in place because I was told to edit only these records. Delete them at
  commit.
- `ground_floor_deps` gains B0-R0-C28 (average and spread), for the median.
- Last must_know (boundary) and the teaching answer now say Web of Science and Scopus, not "one
  database".

**C05 (a question whose answer would change something):** a short paragraph in the definition and
two sentences in the simplified explanation give Chalmers & Glasziou 2009's estimate with its basis,
quoted from that file (not via Ioannidis 2016). The four stages are named. The estimate is: if the
losses they found apply generally, "the roughly 50% loss at stages 2, 3, and 4 would lead to a
greater than 85% loss". The evidence is mainly from clinical trials, and stage 1, the choice of
question, is not in that arithmetic. No per-stage percentage from the figure is stated. Ioannidis
2014's point is added in prose, "insufficient consideration ... to both previous and continuing
studies", with the existing "designed, done, and discussed in isolation" quote. Three Chalmers refs
and one Ioannidis ref are added.

**C07 (who is waiting):** two sentences in the definition and two in the simplified explanation
cite Chalmers et al. 2014. Clinicians and patients are the principal users of clinical and
epidemiological research, and they are often frustrated by the mismatch between their uncertainties
and what researchers study. Users of research are only rarely involved in setting research agendas.
Three refs are added.

**C02 (Morgan 54% of 313):** I kept it, with plain attribution: "Morgan and colleagues report, from an
earlier review they cite, that ... This course has not read that review." I kept it because the move
it supports (find the PICO parts yourself) stands without the number, and the ref note already
names the review that was not opened.

## Checks
- `python3 check/figures/draw.py --book S55-R1`: 3 figures, 0 problems.
- `python3 check/build.py --check`: blocking 0. No new warning on these four records. The C02 and C07
  long-sentence warnings were already there: each is a one-sentence research question quoted whole.
- The build checks numbers only in a singular `illustration`, so I checked each quote in the four
  records myself (`/home/claude/scratch-b5/qcheck.py`). Every definition quote and every
  illustration number's quote is in its source file, and every number is stated in its quote.
  Result: 0 problems.

## For the conductor
- **Copyright:** the Patsopoulos figure plots 10 of Table 1's median cells, for five of its seven
  designs. It is a selection of facts, not the table, but the file says to reproduce no table or
  figure. If you judge 10 cells too many, cut the figure to 2001 only, or to meta-analysis vs case
  report.
- Scopus's owner is not in any held text, so it is not named.

## Glossary rows (proposed; not in `prose/GLOSSARY.md`)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| case report | a report that describes one patient, or a few | `S55-R1-C06` |
| meta-analysis | a study that combines the results of earlier studies of the same question into one answer | `S55-R1-C06` |
| open citation window | citations counted up to one fixed date, so older papers have had longer to be cited than younger ones | `S55-R1-C06` |
