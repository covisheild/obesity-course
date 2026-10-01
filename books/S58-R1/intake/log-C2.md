# Source intake log · S58-R1 · group C2 (graphical perception, axes, decoration, colour, error bars)

One pass, 2026-10-02. Every stored passage was cut by script (`books/S58-R1/intake/build-C2.py`) as `raw[i:j]`, a run
of whole lines or a marker-to-marker span, from a saved `mcp__TinyFish__fetch_content` result in
`books/S58-R1/intake/raw/` (files prefixed `C2-`). Each raw file is the result's `text` field, JSON-decoded unchanged and
written out by script from the session's own saved tool results; a `.meta.json` beside it records the URL, final URL,
title, outbound links where requested, and the tool call id. The written source files were then re-parsed by
`books/S58-R1/intake/verify-C2.py` and each passage tested as a whitespace-normalised substring of the raw fetch for the
URL in its block heading; the same script checks that the key quotes each header promises sit inside a passage. No
WebFetch output is stored; nothing was fetched with curl, wget or Python HTTP. Identifiers: PubMed tools
(`convert_article_ids`, `get_article_metadata`) for the four PMC articles; Crossref records
(api.crossref.org/works/<doi>, saved as raw) for the pages of the three CHI papers. The ACM Digital Library and JSTOR
were not fetched.

**Verbatim check: 53 of 53 passages** (six assigned works 48, bonus 5). **Key-quote check: 34 of 34.**

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Correll, Bertini & Franconeri 2020, *Truncating the Y-Axis: Threat or Menace?*, CHI 2020: 1-12 | https://arxiv.org/pdf/1907.02035v2 (text layer); https://arxiv.org/abs/1907.02035; http://arxiv.org/licenses/nonexclusive-distrib/1.0/ | 13 | 13/13 | arXiv page links "view license" to the arXiv non-exclusive distribution licence: "I grant arXiv.org a perpetual, non-exclusive license to distribute this article." Crossref lists ACM's copyright policy for the CHI version | `correll_2020_truncating_yaxis` |
| Heer & Bostock 2010, *Crowdsourcing graphical perception*, CHI 2010: 203-212 | http://vis.stanford.edu/files/2010-MTurk-CHI.pdf (authors' lab copy, text layer); http://vis.stanford.edu/papers/crowdsourcing-graphical-perception | 11 | 11/11 | "Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee ..." / "Copyright 2010 ACM" (paper's own notice) | `heer_bostock_2010_crowdsourcing_perception` |
| Weissgerber, Milic, Winham & Garovic 2015, *PLoS Biol* 13:e1002128 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4406565.1/PMC4406565.1.xml | 5 | 5/5 | "© 2015 Weissgerber et al" + creativecommons.org/licenses/by/4.0/ "This is an open-access article distributed under the terms of the Creative Commons Attribution License ..." | `weissgerber_2015_beyond_bar_graphs` |
| Bateman et al. 2010, *Useful junk?*, CHI 2010: 2573-2582 | https://sites.stat.columbia.edu/gelman/communication/Bateman2010.pdf (third-party academic host, text layer); first author's page https://scottbateman.github.io/publication/2010-01-01-Useful-junk-The-effects-of-visual-embellishment-on-comprehension-and-memorability-of-charts | 13 | 13/13 | "Permission to make digital or hard copies ... for personal or classroom use is granted without fee ..." / "Copyright 2010 ACM" (paper's own notice) | `bateman_2010_useful_junk` |
| Crameri, Shephard & Heron 2020, *Nat Commun* 11:5444 | https://pmc-oa-opendata.s3.amazonaws.com/PMC7595127.1/PMC7595127.1.xml | 3 | 3/3 | "© The Author(s) 2020" + "Open Access This article is licensed under a Creative Commons Attribution 4.0 International License ..." | `crameri_2020_misuse_colour` |
| Cumming, Fidler & Vaux 2007, *J Cell Biol* 177:7-11 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2064100.1/PMC2064100.1.xml | 3 | 3/3 | "Copyright © 2007, The Rockefeller University Press" ... "After six months it is available under a Creative Commons License (Attribution–Noncommercial–Share Alike 4.0 Unported license ...)" | `cumming_2007_error_bars` |
| **Bonus (C18):** Krishnamurthy et al. 2021, *Indian J Ophthalmol* 69:2021-2025, CVD in school boys, Kanchipuram | https://pmc-oa-opendata.s3.amazonaws.com/PMC8482944.1/PMC8482944.1.xml | 5 | 5/5 | "Copyright: © 2021 Indian Journal of Ophthalmology" + "distributed under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 License ..." | `krishnamurthy_2021_cvd_india` |

**Obtained: 6 of 6** assigned works, plus the bonus. Each file's header says exactly what is held and what is not.

## What each serves

- **C14** (marks the eye reads accurately): Heer & Bostock, Experiment 1A replicates Cleveland & McGill's ranking (position
  over length; angle and area worse than position) and Experiment 1B (rectangular area). Cleveland & McGill 1984 itself
  stays Harsh-only; the inventory's fallback (Heer & Bostock plus Wilke) is now half in hand.
- **C15** (show the data): Weissgerber, whole body, with the 703-paper review numbers and Fig 1's "Many different datasets
  can lead to the same bar graph".
- **C16** (honest axes, measured): Correll, all three experiments with their F statistics, the Fig 1 Fox News example
  (6 times taller for a 1.13 ratio), and the guideline debate, which quotes Bergstrom & West's proportional-ink passage
  (a secondary quotation: cite Bergstrom & West from their own page, filed by another group as
  `bergstrom_west_2016_proportional_ink`, not from Correll).
- **C17** (decoration): Bateman, results and the whole discussion, including the authors' own caution against
  generalising and their "The wider problem of bias in charts" section.
- **C18** (colour): Crameri, whole body, with the "0.5% of women and 8% of men" estimate (stated as a general estimate
  citing refs 24-25, not measured by the authors). Bonus: Krishnamurthy 2021 gives an Indian measured prevalence, 2.76%
  (95% CI 2.65-2.88) in 74,986 boys aged 11-17 in one Tamil Nadu district; boys only, so it supports "about 3 in 100
  boys in one Indian district", not a population rate.
- **C19** (words on a figure; error bars): Cumming, whole body with Table I and Rules 1-8.

## Decisions and caveats for Harsh

1. **Bateman 2010 is from a third-party host, not the authors' own copy.** The brief asked for the authors' open PDF. The
   first author's publication page (scottbateman.github.io) gives the citation only, with no PDF; the University of
   Saskatchewan lab pages for Mandryk and Gutwin load their publication lists by script and show no file; the lab's former
   upload URL `https://hci.usask.ca/uploads/173-pap0161-bateman.pdf` and its Wayback copy both returned
   `target_unreachable`. The copy filed is the camera-ready PDF (PDF title "Microsoft Word - pap0297-bateman3.doc", CHI 2010
   footers on every page, pages 2573-2582 matching Crossref) posted in Andrew Gelman's "communication" reading folder at
   Columbia statistics, the same kind of public third-party copy READY.md already accepts for Gopen & Swan. **Harsh to
   decide:** accept it, or download the ACM DL version himself (https://doi.org/10.1145/1753326.1753716) and drop it in
   `sources/`; the passages should match apart from text-layer spacing.
2. **Correll is the arXiv v2 preprint, not the ACM typeset paper.** Its licence is arXiv's minimal distribution licence,
   not an open reuse licence, so quote briefly. Locators should be section names (the CHI page numbers are not in the
   arXiv text).
3. **Text-layer artefacts** (ligatures, hyphenation, stray spaces such as "fo r" in Bateman, flattened subscripts such as
   "t 19=0.84") are kept verbatim, so a `quote` field must copy them exactly as they stand in the file.
4. **Not stored:** figure images and the chart text inside figures in all four PDFs; Heer & Bostock Experiments 2-3 and the
   MTurk cost sections; Bateman's Previous Work section; Crameri's Methods (the CIEDE2000 formula).
5. **Cumming's SD formula** is held as the LaTeX source the PMC XML carries, transcribed by the extractor; no equation
   was retyped.
6. Citekeys grepped in `sources/INDEX.yml` and `check/references/library.bib` at the start and again at the end (none
   present). Two other book chats are adding sources on unpublished branches; the keys are long and specific, but the
   conductor should grep once more on merge.

## Files written

- `sources/correll_2020_truncating_yaxis.txt`, `sources/heer_bostock_2010_crowdsourcing_perception.txt`,
  `sources/weissgerber_2015_beyond_bar_graphs.txt`, `sources/bateman_2010_useful_junk.txt`,
  `sources/crameri_2020_misuse_colour.txt`, `sources/cumming_2007_error_bars.txt`,
  `sources/krishnamurthy_2021_cvd_india.txt` (bonus)
- `books/S58-R1/intake/build-C2.py`, `verify-C2.py`, `manifest-C2.json`, `fragment-C2.md`, this log
- `books/S58-R1/intake/raw/C2-*.txt` with `.meta.json` (15 raw fetches, including three Crossref records used only to confirm
  pages, and the selector-scoped arXiv fetch that carries the licence link)
