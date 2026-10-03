# S58-R1 — handover (Scientific writing, visualisation and public communication · Rung 1, Book 9)

Frozen at version 1.0, 3 Oct 2026. 23 sections (two added by Harsh's accepted map amendments
S58-R1-A01 and A02), about 207-page PDF, 28 figures (5 sections with a figure_note), 38 practice
problems in 3 drill sets (C09 13, C11 11, C17 14), 112 glossary rows added (`subject` given a second
sense). Build: blocking 0, warnings 232 corpus-wide. 266 audit and rendered-page defects: 193 fixed,
45 partly (the remainder deferred to a contract-change chat, below), 28 rejected (mostly already
withdrawn by the auditors); every one verified closed (`check/defects.py S58-R1`: 0).

## What was written
The paper's parts and IMRAD (C01); a paper as an argument (C02); the one message (C03); the argument
across sections (C04); citing and referencing in NLM/Vancouver style (C05, amendment A02); parts of a
sentence (C06); the sentence as the unit of clarity, after Gopen & Swan (C07); words, terms and
abbreviations (C08); numbers in a sentence, after Cole and SAMPL (C09, drill set); one idea per
paragraph and the reverse outline (C10); readability measures, Flesch Reading Ease from Flesch's own
.846 and the grade-level formula from Kincaid 1975 (C11, drill set); cutting (C12); the one-pass test,
which carries the rung's build (C13); a figure makes one claim (C14); choosing the mark, after
Cleveland & McGill and Heer & Bostock (C15); show the data (C16); honest axes and the Lie Factor,
after Tufte 1983 and Correll 2020 (C17, drill set); decoration (C18); colour (C19); words on a figure,
error bars after Cumming, Fidler & Vaux (C20); a table that stands alone (C21, amendment A01); making
the plot, tool-free after Wilke's Preface (C22); the journey, one NFHS-5 finding from the fact sheet to
a paragraph, a table and a figure (C23).

## Deferred, with triggers (no open factual error)
All need a contract-change chat (`check/**` is frozen while books run); none is a factual error.
- **RENDER-1, reference lists:** printed in the series' house style, not the NLM style C05 teaches;
  one entry per cited passage (396 entries), numbers repeated in one bracket, `library.bib` notes
  printed. C05 tells the reader the book's own lists are house style. Fix in `check/build.py`.
- **RENDER-2, missing glyphs:** the bundled Inter faces have no √, ≈ or superscript minus and the
  Inter font stacks in `check/pdf/style.css` have no fallback that does, so those signs print blank
  in tables, captions and every book's Symbols page ("the value:   9 = 3"). Add "DejaVu Sans" to the
  Inter stacks. In this book the C15 caption was reworded to avoid ≈.
- **FIG-1/FIG-2/FIG-6, figure tool:** a legend is always drawn for two or more series even beside
  direct labels; for hue 330 the two series colours have the same grey (85 vs 87 of 255), against
  `palette_for`'s own design note; a one-series fill is the saturated primary with no option. This
  book's own figures therefore break two rules it teaches (C18 delete a redundant key; C19 lightness).
  They read in grey through direct labels. Fix in `check/figures/figspec.py`/`draw.py`.
- **RENDER-3 to RENDER-6:** URLs hyphenated mid-word, two table header styles and narrow columns that
  break words, larger type for appendix lists, page-break faults (DEFECTS.md).
- **Compression tooling:** `restore.py` brings back a working block when any earlier prose in the
  field is restored, not only its own paragraph (C22, restore batch r4); the assembled `-pass1.md`
  files print `{{n:key}}` raw, which the cold readers counted as gaps.

## Sources to re-check
- NFHS-5 figures throughout (registry `books/S58-R1/numbers.yml`): when NFHS-6 is published.
- ICMJE Recommendations (updated January 2026), section IV.A: at the next ICMJE update. ICMJE asks
  others not to reprint its Recommendations; the book quotes briefly and links.
- Federal Plain Language Guidelines (2011) were taken from a third-party copy of the PDF
  (plainlanguage.gov was offline); Gopen & Swan 1990 from a retyped reprint without page numbers;
  Bateman 2010 from a camera-ready PDF on a course reading folder; Correll 2020 is the arXiv preprint.
- Flesch 1948 is held as a retyped public-domain reprint (ERIC ED506404, accepted by Harsh 2 Oct 2026).
  It settles the coefficient: Flesch printed .846; Kincaid 1975's Table 3 ".836" is a misprint, and the
  book takes the Reading Ease formula from Flesch. The reprint prints the "Very difficult" band as
  "0 to 20"; the book takes the bands from Flesch 1979.
- Tufte is held as the 1983 first edition (tenth printing 1990), cited with its page numbers; Harsh's
  copy is from a shadow library; excerpts only. Cleveland & McGill 1984 is Harsh's PDF (publisher
  copyright), excerpts only. Kincaid 1975 is the UCF STARS PDF Harsh supplied.
- NCBI Bookshelf (Citing Medicine) and UCF STARS were read by single page fetches; their terms bar
  systematic automated retrieval, which this was not (Harsh to confirm he is content).

## Process notes
Claimed 2 Oct 2026 as the third book at once (S47-R1 at its gate, S52-R1 in flight). Source gate:
Harsh supplied Kincaid 1975, Cleveland & McGill 1984 and Tufte; accepted the Flesch 1948 reprint; and
accepted all five coverage gaps as amendments (S58-R1-A01, A02; S58-R2-A01 to A03, written into
`map/AMENDMENTS-v3.1.yml` on this branch). Two usage-limit stops (a drafter and the first fix wave)
were resumed from committed work-in-progress. Cold read: 146 gaps (two readers), 47 restored, about 90
holes to the audit. A fresh reader of the rendered PDF found 53 items: 22 record-level (fixed and
verified), the rest renderer items above.
