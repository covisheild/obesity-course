# Draft notes · S58-R1 · batch b5 (C11, C12, C13)

Task 2 drafter, 2 Oct 2026. Records written:

- `check/records/S58/S58-R1-C11.yml` — Measuring a draft: words per sentence, a readability score, and what they cannot show (empirical, quantitative, 11 practice problems, 2 figures)
- `check/records/S58/S58-R1-C12.yml` — Cutting: deleting the words, sentences and paragraphs that do no work (derivable, 1 figure)
- `check/records/S58/S58-R1-C13.yml` — Showing a draft to a reader: the one-pass test (derivable, `figure_note`; carries the rung's `build` exercise)

Every quote was checked as a whitespace-normalised, case-folded substring of its file in `sources/`
(script in `/home/claude/scratch-s58-b5/qcheck.py`), and every illustration number's quote states its
value. Every equation in a `working` block (113 of them) was recomputed in Python
(`/home/claude/scratch-s58-b5/arith.py`); the hand syllable and word counts were recounted by script
(`ill.py`, `c12.py`).

Build (`check.build.check` on the whole corpus, last run after the final edits): **0 blocking**
overall, none for b5. Four warnings left on b5, all deliberate: the long quoted sentences in C11
practice 5 (Flesch's 43-word example, which is the point of the problem), C12 exercise 2 (the invented
draft to be cut) and C13's 28-word sealed one-message sentence.

Build quirk worth passing on: the arithmetic check takes its tolerance from the *fewest* decimals on
either side, so `11 divided by 7 = 1.5714` blocks. Write a division of whole numbers to full precision
(`11 divided by 7 = 1.571428571`) and round in the next line or in prose.

## Intake rulings applied (C11)

- FRE coefficient taken from Flesch: 1948 Formula A (".846 wl", per 100 words) and 1979 ("Multiply the
  average word length by 84.6"). **Kincaid 1975 is quoted only for the GL formula, the simplified GL
  (in a note), the 531 Navy personnel, the 18 passages, "*GL is grade level." and Appendix B's counting
  examples.** The .836 misprint is recorded in a reference note for the auditor and is **not** put
  before the reader.
- The name: the record says "The report calls the result GL ... Later writers call the formula the
  Flesch–Kincaid grade level (FKGL)", the later name quoted from Edwards 2022. It does not say the
  report "never" uses the name (only excerpts are held).
- Bands: taken from Flesch 1979 only ("0 to 30 college graduate", Plain English minimum 60). The 1948
  reprint's "0 to 20" is not used.
- "A low score does not make text clear": Plavén-Sigray's limits paragraph, plus the fitting samples
  (Flesch's children's test passages, "not the best criterion for general readability"; Kincaid's Navy
  personnel, "specifically for Navy use"; Flesch's "only up to about seventh grade").
- Edwards 2022 is cited once, for the later name, as secondary.

## Unsourced or the book's own (said so in the text where it reaches the reader)

- C11: "a grade level" is described as a school grade level; the record does not claim it equals an
  Indian class (the critique exercise says nothing has shown that it does).
- C11 must-know 5 (do not score a Hindi or Tamil translation): reasoning from the fitting passages
  being English; no held source says it in words. Refs point to the two fitting samples.
- C11 practice 9 uses Flesch 1979's "at least 80, or about 15 words per sentence and 1 1/2 syllables
  per word", which does not compute (64.7). The answer says the mismatch is shown and the wrong figure
  is not, and that the held copy is a retyped web page. **Auditor: confirm the quote and the reading.**
- C11 illustration 1: Flesch prints 92 for "John loves Mary."; the formula gives 91.0. The record says
  printed and computed scores can differ by a point and does not guess why.
- C12: "paste every deletion into a second file" is labelled "this book's advice, not a finding".
- C13: the four parts of a message (whom it is about, what was found, compared with what, how far it
  reaches) and "an added part is worse than a lost one" are the book's own reasoning. The extension of
  Mensh & Kording's Rule 2 from the writer to a guide or co-author is said to be the record's reasoning
  in the reference note.
- All three illustrations' drafts (the thesis sentence, the discussion paragraphs, the methods paragraph,
  the one-pass case with its readers) are labelled invented in the text.

## Practice-set size

C11: **11 problems** (levels 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10). Why: the technique has five moves that
compose (count, two averages, two formulas) plus one reverse, and the two traps that actually break real
scores (the counting rule for figures; per-word against per-100-words coefficients) each needed a problem
of its own.

## Figures

- `s58-r1-c11-score-lines.png` — FRE against ASL, one line per version's ASW (71/52, 44/31), the draft and
  Rewrite A as points, a reference line at Flesch's Plain English minimum 60.
- `s58-r1-c11-counting-rule.png` — grouped bars: the draft and Rewrite A, each scored with figures as one
  syllable (38.5, 71.0) and read aloud (1.1, 8.3).
- `s58-r1-c12-three-passes.png` — words left after each cutting pass (161, 124, 69, 49), from the
  record's table, with checks on each difference.
- C13: `figure_note` (the test is a procedure and a two-sentence comparison, already a table). No
  figure wanted beyond these.

All drawn by `python check/figures/draw.py --book S58-R1` (19 figures in the book, 0 problems at my last
run) and looked at as images.

## numbers.yml

No key added (file not edited). Keys used: `nfhs4_women_ow_ob_pct`, `nfhs5_women_ow_ob_pct`,
`nfhs5_women_ow_ob_urban_pct`, `nfhs5_women_ow_ob_rural_pct` (C11, C12), `nfhs5_men_ow_ob_pct`,
`nfhs4_men_ow_ob_pct` (C11 practice 6).

Numbers written literally that the reconciler may want in the registry if another section uses them:

| value | meaning | source |
| --- | --- | --- |
| 206.835, 1.015, 84.6 | FRE constant and coefficients (per word in sentence length; per syllable per word) | `flesch_1979_plain_english` ch. 2; `flesch_1948_readability_yardstick` Formula A (0.846 per 100 words) |
| 0.39, 11.8, 15.59 | FKGL coefficients and constant | `kincaid_1975_readability` Appendix B step 6 |
| 60 | Flesch's minimum FRE for Plain English | `flesch_1979_plain_english` ch. 2 |
| 709,577; 123; 1881-2015 | abstracts, journals, years scored by Plavén-Sigray et al. | `plavensigray_2017_readability` abstract |
| 14%, 22% | abstracts with FRE below 0 in 1960 and 2015 | `plavensigray_2017_readability` Discussion |
| 531; 18 | Navy personnel and passages behind the FKGL | `kincaid_1975_readability` Summary |
| 2021 | year NFHS-5 fieldwork ended (30 April 2021) | `nfhs5_india_factsheet` introduction |

## Notation rows needed

None. The records print no sign outside `check/notation.yml` in reader text (arithmetic is in words;
"≥" occurs only inside quotes). The abbreviations ASL, ASW, FRE and FKGL follow the brief's shared
notation and are expanded at first use in C11; if the Symbols page is ever to list abbreviations, these
four are the rows.

## Glossary rows (proposed; not in `prose/GLOSSARY.md`)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| average sentence length (ASL) | the number of words divided by the number of sentences | `S58-R1-C11` |
| average syllables per word (ASW) | the number of syllables divided by the number of words | `S58-R1-C11` |
| compressing (a draft) | keeping all the content and packing it into fewer, longer sentences; not the same as cutting | `S58-R1-C12` |
| cutting (a draft) | deleting words, sentences or paragraphs that do no work for the reader, largest unit first | `S58-R1-C12` |
| Flesch Reading Ease (FRE) | a score from word and sentence length, 206.835 minus 1.015 times ASL minus 84.6 times ASW; higher means easier | `S58-R1-C11` |
| Flesch–Kincaid grade level (FKGL) | a school grade predicted from word and sentence length, 0.39 times ASL plus 11.8 times ASW minus 15.59 | `S58-R1-C11` |
| one-pass test | a reader outside the work reads a draft once and writes what it argues, and you compare that with your own sentence | `S58-R1-C13` |
| readability formula | a formula that estimates how hard a passage is to read from counts of words, sentences and syllables | `S58-R1-C11` |
| syllable | one beat of a spoken word | `S58-R1-C11` |

## Notes for others

- **C03 (one message).** C12 and C13 call it "your one message" / "the one-message sentence", written
  first and kept. C13 compares it by four parts: whom or what the claim is about, what was found,
  compared with what, how far it reaches. If C03 names the parts differently, the reconciler should
  align C13 to C03's words.
- **C07 (the sentence).** C11's simplified explanation sends the reader to C07 for splitting long
  sentences, and C12's critique answer to C07 for the active voice. C07 should teach both.
- **C10 (paragraph).** C12 and the C13 build use "reverse outline" as "write the one point of each
  paragraph in the margin". C10 must define it in those terms.
- **C09 (numbers).** Nothing in b5 contradicts C09. C11 shows that figures dominate a readability score
  of a results paragraph; C09 should not say anything that implies a score is neutral to figures.
- **C23 (journey).** If it measures a paragraph: take FRE's 84.6 per syllable per word from Flesch (never
  Kincaid's Table 3, which prints .836), state the counting rule used for figures beside any score, and
  take bands from Flesch 1979. **C13 carries the rung's `build` exercise** (skill_ref S58-R1-K01): C23
  should not add a second `build`, or the reconciler should choose one.
- **Any section citing Flesch 1979:** the bib's publisher (Harper & Row, New York) is from general
  knowledge, as the bib note says.
- **The NFHS running case.** C11 and C12 use the women's 15-49 overweight-or-obese row only, with the
  rounds dated 2015-16 and 2019-21. C12 makes the point that "now" is wrong for NFHS-5 (fieldwork ended
  April 2021); later sections should not say "currently" of NFHS-5 figures.
