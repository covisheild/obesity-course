# Source intake log · S58-R1 · group G (Cleveland & McGill 1984, graphical perception)

One pass, 2 Oct 2026. Task from the conductor: file Cleveland & McGill 1984 for concept C14 from the PDF Harsh
supplied by hand (JSTOR and the publisher's site may not be fetched automatically; READY.md listed it as
Harsh-only and optional). Nothing was fetched.

**Input:** `/root/.claude/uploads/f2099557-ac04-5a0f-a543-1cd2874da8af/4663e75d-10_1080_01621459_1984_10478080_pdf_--_Cleveland_William_S__McGill_Robert_--_Journal_of_the_American_Statistical_Association_387_79_--_American_--_doi_10_1080_01621459_1984_10478080_--_e5ab1f2936ff.pdf`,
25 pages (T&F cover page "downloaded by: [Michigan State University] On: 28 February 2015", then journal
pp. 531-554 as PDF pp. 2-25), 2,482,922 bytes, SHA-256
`804f08bebc1929d7eeabce9d55b9796d9a3b67d7b429b1f9956e8e91eab5def3`. Scanned pages with an OCR text layer
(Creator "Acrobat 5.0 Paper Capture Plug-in").

**Method.** `intake/extract-G.py` runs `pdftotext -layout` on the whole PDF and saves it unaltered as
`raw/G-cleveland_mcgill_1984-pdftotext.txt`. Because `-layout` prints the journal's two columns side by side
(a sentence in one column is interleaved line by line with the other), the same tool and mode were also run on
each page's left and right column separately (`pdftotext -layout -r 72 -x/-y/-W/-H`, gutter found per page from
`pdftotext -bbox` as the x with fewest word boxes in 300-360 pt) and saved as
`raw/G-cleveland_mcgill_1984-pdftotext-columns.txt`, each crop preceded by one marker line
`##### PDF page N, left|right column (x a-b pt) #####` written by the script. Word-multiset comparison of the two
raws: they differ only in words of figure labels and full-width captions split at the gutter; no body-text word
differs. `intake/build-G.py` cuts every passage as `raw[i:j]` of the columns raw between whitespace-flexible
start/end phrases (unique start asserted; a passage may not cross a page/column marker), writes
`sources/cleveland_mcgill_1984_graphical_perception.txt`, then re-reads the written file and checks each
[TEXT] passage (1) as a whitespace-normalised substring of the columns raw and (2) line by line against the
whole-page `-layout` raw. Offsets and pages per passage: `raw/G-cutlog.json`.

**Verbatim check: 39 of 39** against the columns raw; **39 of 39** with every line found in the whole-page
`-layout` raw. 10 blocks, 3,083 words of passages (about a fifth of the article's text; the figures, the
psychophysics, the bootstrap and bias analyses, sections 5.2-5.4 and references are not held).

| Source | File (not fetched) | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Cleveland WS, McGill R. Graphical perception: theory, experimentation, and application to the development of graphical methods. *J Am Stat Assoc* 1984;79(387):531-554, doi 10.1080/01621459.1984.10478080 | PDF supplied by Harsh (path above); T&F download, OCR text layer | 39 | 39/39 | Article p. 531: "© Journal of the American Statistical Association" (text layer "0 Journal ..."). T&F cover page: "This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden." Held as excerpts for private study and quotation | `cleveland_mcgill_1984_graphical_perception` |

## OCR check against the page images

Rendered with `pdftoppm -r 80` into the scratchpad (`G-p<N>-*.png`) and read; the exponents on p. 541 and two
lines on pp. 539-540 were also rendered at 200 dpi to be sure. Pages checked: cover (PDF 1), journal 531, 532,
535, 536, 537, 539, 540, 541, 542, 544, 545, 547, 552, 553 (PDF 2, 3, 6, 7, 8, 10, 11, 12, 13, 15, 16, 18, 23, 24).
Not image-checked: p. 538 (PDF 9; the 4.1 passage, no numbers). OCR errors found inside held passages (left
uncorrected in the passages; the correct reading is in a [NOTE] under each block):

| Page | Text layer | Page image |
| --- | --- | --- |
| 531 | `divided barcharts`; `0 Journal of the American Statistical Association` | divided bar charts; © Journal of ... |
| 535 | `an ordering of the I0`; `graphical f o r m` | 10; graphical *form* (italic) |
| 536 | `5 . Volume, curvature` | 5. Volume, curvature |
| 539 | `8 t x 11 page`; `s i = 10 x 10(i-l)'lz`; `.18to .83`; `56.2.Subjects` | 8½ × 11; s_i = 10 × 10^((i−1)/12); .18 to .83; 56.2. Subjects |
| 540 | `logz( I judged percent - true percent I + I/@.`; `least ac- curate (3.)` | log2(\|judged percent − true percent\| + 1/8); least accurate (5).) |
| 541 | `a factor of 2'.32 = 2.5`; `a factor of 2.97 = 1.96`; `greater than 4-`; `Figure l7` | 2^1.32 = 2.5; 2^.97 = 1.96; greater than 4.; Figure 17 |
| 544 | a lone `;` line in 4.5 | no mark on the page |
| 545 | `For\each` | For each |
| all | hyphens for em dashes (`perception-the`, `ranks-3, 5 , and 6-have`) | em dashes |

Every other number in the held passages matched the images: 55, 54, 20 graphs, 10 to 56.2, 10.0 to 99.7%, 51,
1/8, 3 of the 40, .05, 1.32, 2.5, .51, 1.4, 40%-250%, .97, 1.96, 2,550, 136, 4, 78% and 88% (in words), 5.3,
219, 4,080, 7.3, 25-50, 0 to 100%, 0 to 25 or 50%, 0 cm, 2.8 cm, 5.6 cm, "10 basic".

## The ranking as the paper states it (p. 536, image-checked)

"The following are the 10 elementary tasks in Figure 1, ordered from most to least accurate:
1. Position along a common scale 2. Positions along nonaligned scales 3. Length, direction, angle 4. Area
5. Volume, curvature 6. Shading, color saturation" — then (p. 537) "Three of the ranks—3, 5, and 6—have more than
one task; at the moment there is not enough information to separate the ties."

## Caveats for the book

- The ordering is the authors' hypothesis. Their two experiments test only position (common scale) against
  length (divided bar charts) and position against angle (pie charts); area, volume, curvature, shading and
  colour saturation are placed from psychophysics and reasoning, not from these experiments. Heer & Bostock
  2010 (held) is the replication.
- "1.96 times as accurate" (4.5) is the authors' wording for an error ratio of 2^.97 on the log2 scale; the
  paper also warns (p. 541, not held) that the two experiments' means should not be compared with each other.
- Within "position along a common scale", accuracy fell as the judged elements moved apart (Types 1-3, 0, 2.8,
  5.6 cm); the authors propose position be treated as a continuum.
- Who the subjects were (two groups, described on p. 539) is not held; only that 51 per experiment were analysed
  and that no difference was detected between the nontechnical and technical groups.

Nothing committed; `sources/INDEX.yml`, `check/references/library.bib` and `sources/SOURCES.md` untouched
(entries in `fragment-G.md`). Files written: `sources/cleveland_mcgill_1984_graphical_perception.txt`,
`books/S58-R1/intake/{extract-G.py, build-G.py, fragment-G.md, log-G.md}`,
`books/S58-R1/intake/raw/{G-cleveland_mcgill_1984-pdftotext.txt, G-cleveland_mcgill_1984-pdftotext-columns.txt, G-cutlog.json}`.
