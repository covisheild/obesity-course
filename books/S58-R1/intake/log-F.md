# Source intake log · S58-R1 · group F (Flesch Reading Ease: the original coefficient and bands)

One pass, 2 Oct 2026. Task from the conductor: Flesch 1948 (*J Appl Psychol* 32:221-233) is paywalled and
Harsh could not download it; held sources disagree on the old Reading Ease formula's syllable coefficient
(Kincaid et al. 1975 Table 3 prints ".836 (syllables/100 words)"; Plavén-Sigray 2017 and Edwards 2022 print
84.6 x syllables/word). Find the best lawful alternative that settles which coefficient Flesch published, and
his own interpretation bands.

Method as `INTAKE-BRIEF.md`: every fetch `mcp__TinyFish__fetch_content` (markdown); search with
`mcp__TinyFish__search`. Each result was taken from this agent's own tool results (the harness's saved
tool-result file, or inline in the transcript) by `scratchpad/saveraw_F.py`, which reads only results of
fetch_content calls, JSON-decodes them and writes the `text` field unchanged to `raw/F-*.txt` with a
`.meta.json` (url, final_url, title, source of the result). Passages were cut by `intake/build-F.py` as
`raw[i:j]` between anchor strings (offsets in `raw/F-cutlog.json`); `intake/verify-F.py` re-parses the
written files and tests each [TEXT] passage as a whitespace-normalised substring of the raw fetch for the
URL in its block heading, and checks the coefficient strings are present. No WebFetch output stored;
nothing fetched with curl, wget or a Python HTTP client. Not fetched: JSTOR, APA PsycNET, Sci-Hub, LibGen,
Anna's Archive or any shadow library. Flesch 1948 identifiers confirmed with `mcp__PubMed__get_article_metadata`
(PMID 18867058, DOI 10.1037/h0057532). Nothing committed; INDEX.yml, library.bib and SOURCES.md untouched
(entries in `fragment-F.md`).

**Verbatim check: 9 of 9** (flesch_1948 5, flesch_1979 4). **Filed: 2 sources.**

| Source | URL fetched (stored passages) | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Flesch 1948, "A New Readability Yardstick", **retyped reprint** in DuBay (ed.), *The Classic Readability Studies* (2007), pp. 99-111, plus DuBay's introduction pp. 96-98 | https://files.eric.ed.gov/fulltext/ED506404.pdf (PDF text layer); https://eric.ed.gov/?id=ED506404; https://eric.ed.gov/?copyright | 5 | 5/5 | ERIC abstract: "The articles reprinted here (all in the public domain) are the following: ..." (incl. Flesch 1948). PDF: "Introductions © 2006 William H. DuBay. All Rights Reserved." ERIC: works "used by ERIC with permission"; robots.txt disallows nothing | `flesch_1948_readability_yardstick` |
| Flesch 1979, *How to Write Plain English*, ch. 2 "Let's Start With the Formula", whole | https://pages.stern.nyu.edu/~wstarbuc/Writing/Flesch.htm; https://pages.stern.nyu.edu/~wstarbuc/Writing/ (listing); https://web.archive.org/web/2016/http://www.mang.canterbury.ac.nz/writing_guide/writing/flesch.shtml (resolved to the 2017-01-12 snapshot) | 4 | 4/4 | None stated on either page; in-copyright book reproduced on third-party educational pages. robots.txt (NYU Stern) excludes only another user's directory | `flesch_1979_plain_english` |

## Finding: which coefficient Flesch published

**84.6 per syllable per word (.846 per syllable per 100 words). Kincaid 1975's .836 is best treated as a
misprint in that report.** Evidence, all in Flesch's own words:

1. Flesch 1948 (reprint), Findings: "Formula A (for predicting "reading ease"): RE = 206.835 - .846 wl -
   1.015 sl", wl = "word length (syllables per 100 words)". Repeated in "The Formulas Restated", Step 7.
2. The same paragraph prints the untransformed regression, "C75 = .0846 wl + .1015 sl – 5.6835", and
   explains the transformation (x10, signs reversed, score 100 = fourth grade completed). 150 - 10 x C75 =
   206.835 - .846 wl - 1.015 sl exactly, so .0846, .846 and 206.835 are mutually consistent; a single
   retyping error cannot produce that.
3. Flesch's printed worked scores (Tables 4 and 7), recomputed by `build-F.py`: New Yorker 1946 61 (.846
   gives 61.3; .836 gives 62.8), Reader's Digest 68 (67.9; 69.4), New Yorker 1947 66 (65.9; 67.3), Life 46
   (44.9; 46.6, inputs rounded). Three match .846, none matches .836.
4. Flesch 1979, in the first person: "Multiply the average word length by 84.6."

Residual caveat: the 1948 text is DuBay's retyping, not the APA page image (other retyping slips are visible,
listed in the file header). Points 2-4 do not depend on the reprint's accuracy for this one number. If Harsh
ever obtains the APA PDF, check p. 225 ff. against block 5; no other action needed.

## Finding: the bands

- **Flesch 1948 Table 5** (the "description of style" bands, his own): Very Difficult / Difficult 30-50 /
  Fairly difficult 50-60 / Standard 60-70 / Fairly easy 70-80 / Easy 80-90 / Very easy 90-100, with typical
  magazine, syllables per 100 words and sentence length. **As reprinted, the first row reads "0 to 20"**,
  leaving 20-30 unassigned. DuBay's introduction (two tables from Flesch 1949) and Flesch 1979 both give
  0-30. Probably a retyping slip; not provable from this copy. Drafter: cite 0-30 to Flesch 1979 (grade
  bands) or DuBay, or state what the reprint prints.
- **Flesch 1979**: score to school level, 90-100 5th grade; 80-90 6th; 70-80 7th; 60-70 8th and 9th; 50-60
  10th to 12th; 30-50 college; 0-30 college graduate. Plain English minimum 60.
- DuBay's 1949 table (block 4) has its own misprint, "30 to 40" for Difficult.

## Tried, not filed

- **DuBay 2004, *The Principles of Readability*** (ERIC ED490073; https://files.eric.ed.gov/fulltext/ED490073.pdf
  and the record page): fetched and raw saved (`raw/F-dubay_2004-*`), not filed. It restates 84.6 x ASW and
  the 1949 table ("Flesch (1949, p. 149)"), the same material as DuBay's introduction in ED506404, which is
  filed together with the 1948 article itself. "© 2004 William H. DuBay. All Rights Reserved."
- **The live Canterbury page** http://www.mang.canterbury.ac.nz/writing_guide/writing/flesch.shtml:
  `invalid_url` (site gone); the Wayback snapshot was used.
- **Flesch, *The Art of Readable Writing* (1949)**: an archive.org copy exists in the Digital Library of India
  collection (archive.org/details/in.ernet.dli.2015.275839). Not fetched: an in-copyright 1949 book in a
  mass-scan collection, with no clear lawful-hosting basis. It is the source of DuBay's "p. 149" table.
- **Flesch 1948 original** (APA, doi 10.1037/h0057532): not fetched (paywalled; APA PsycNET and JSTOR
  excluded). An academia.edu upload of the DuBay collection was seen in search results and not used (ERIC is
  the lawful host).

## For Harsh / the conductor

1. Update the Kincaid file header and its INDEX `what:` ("not settled"; "Flesch 1948 (not held)") to point
   to `flesch_1948_readability_yardstick` (fragment-F.md says so). This agent left them untouched.
2. C10 can now state FRE = 206.835 - 1.015 (words/sentence) - 84.6 (syllables/word), citing Flesch 1948 (via
   the ERIC reprint) and Flesch 1979, and note that Kincaid 1975 prints .836 per 100 words.
3. Publisher of the 1979 book (Harper & Row, New York) is from general knowledge, not from a fetched page:
   confirm before printing.
4. Neither 1979 web copy states a licence: brief quotation only.
