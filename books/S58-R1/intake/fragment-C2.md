# Fragment C2 · S58-R1 intake (graphical perception, axes, decoration, colour, error bars)

For the conductor to merge into `sources/INDEX.yml`, `check/references/library.bib` and `sources/SOURCES.md` in one
commit. Six new files for the six assigned works, plus one bonus file (Indian colour-vision-deficiency prevalence,
for C18), listed last and separable. Log: `books/S58-R1/intake/log-C2.md`. All seven citekeys were grepped in
`sources/INDEX.yml` and `check/references/library.bib` (none present) on 2026-10-02, at the start and again at the end.

## 1. `sources/INDEX.yml`

Seven new entries under `files:`.

```yaml
  correll_2020_truncating_yaxis:
    file: correll_2020_truncating_yaxis.txt
    what: >-
      Correll, Bertini & Franconeri, Truncating the Y-Axis: Threat or Menace?, CHI 2020: 1-12 (doi 10.1145/3313831.3376222),
      authors' arXiv version 1907.02035v2, PDF text layer. Whole running text from abstract to Conclusion with every
      figure caption except Fig 5; chart text inside figures, acknowledgments and references not held. Plus the arXiv
      abstract page and its licence page (arXiv non-exclusive distribution licence; not an open reuse licence)
  heer_bostock_2010_crowdsourcing_perception:
    file: heer_bostock_2010_crowdsourcing_perception.txt
    what: >-
      Heer & Bostock, Crowdsourcing graphical perception, CHI 2010: 203-212 (doi 10.1145/1753326.1753357), authors' copy on
      vis.stanford.edu, PDF text layer. Excerpts: abstract, introduction, Graphical Perception, Research Goals, Experiment 1A
      (Cleveland & McGill replication) and 1B (rectangular area) with Fig 3-5 captions, Findings; plus the lab paper page.
      Experiments 2-3, the MTurk and cost sections, figure contents and references not held. ACM copyright
  weissgerber_2015_beyond_bar_graphs:
    file: weissgerber_2015_beyond_bar_graphs.txt
    what: >-
      Weissgerber, Milic, Winham & Garovic, PLoS Biol 2015;13(4):e1002128 (PMC4406565; CC BY 4.0), PMC OA XML. Front matter,
      licence, abstract, whole body to Conclusions with Fig 1-3 captions and Box 1, and the S2 Fig legend; funding, other
      supporting-information entries and references not held
  bateman_2010_useful_junk:
    file: bateman_2010_useful_junk.txt
    what: >-
      Bateman et al., Useful junk?, CHI 2010: 2573-2582 (doi 10.1145/1753326.1753716), camera-ready PDF text layer from a
      third-party academic host (sites.stat.columbia.edu, Gelman's reading folder), not an author site. Abstract,
      introduction, methods, results, whole discussion, conclusion; Previous Work, figure contents and references not
      held; plus the first author's citation page. ACM copyright
  crameri_2020_misuse_colour:
    file: crameri_2020_misuse_colour.txt
    what: >-
      Crameri, Shephard & Heron, Nat Commun 2020;11:5444 (PMC7595127; CC BY 4.0), PMC OA XML. Licence, abstract and the whole
      body (introduction, Boxes 1-2, figure captions, the checks for an unscientific colour map, recommendations); Methods,
      back matter and references not held
  cumming_2007_error_bars:
    file: cumming_2007_error_bars.txt
    what: >-
      Cumming, Fidler & Vaux, J Cell Biol 2007;177(1):7-11 (PMC2064100; CC BY-NC-SA 4.0 after six months), PMC OA XML.
      Licence, abstract and the whole body with Table I, Rules 1-8 and Fig 1-7 captions; SD formula held as the XML's LaTeX
      source; funding line and references not held
  krishnamurthy_2021_cvd_india:
    file: krishnamurthy_2021_cvd_india.txt
    what: >-
      Krishnamurthy, Rangavittal, Chandrasekar & Narayanan, Indian J Ophthalmol 2021;69(8):2021-2025 (PMC8482944;
      CC BY-NC-SA 4.0), PMC OA XML. Licence, abstract, whole introduction, methods, results with Tables 1-2, discussion and
      conclusion; references not held. Boys aged 11-17 in Kanchipuram district only
```

## 2. `check/references/library.bib`

```bibtex
@inproceedings{correll_2020_truncating_yaxis,
  title        = {Truncating the Y-Axis: Threat or Menace?},
  author       = {Correll, Michael and Bertini, Enrico and Franconeri, Steven},
  booktitle    = {Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems},
  publisher    = {ACM},
  year         = {2020},
  pages        = {1--12},
  doi          = {10.1145/3313831.3376222},
  note         = {arXiv:1907.02035v2 (authors' version, 8 Jan 2020), quoted from the arXiv PDF text layer.
                  arXiv non-exclusive distribution licence; publisher copyright for the CHI version},
  url          = {https://arxiv.org/abs/1907.02035},
  urldate      = {2026-10-02}
}

@inproceedings{heer_bostock_2010_crowdsourcing_perception,
  title        = {Crowdsourcing graphical perception: using Mechanical Turk to assess visualization design},
  author       = {Heer, Jeffrey and Bostock, Michael},
  booktitle    = {Proceedings of the SIGCHI Conference on Human Factors in Computing Systems},
  publisher    = {ACM},
  year         = {2010},
  pages        = {203--212},
  doi          = {10.1145/1753326.1753357},
  note         = {Copyright 2010 ACM. Quoted from the authors' copy on the Stanford Visualization Group site
                  (PDF text layer)},
  url          = {http://vis.stanford.edu/files/2010-MTurk-CHI.pdf},
  urldate      = {2026-10-02}
}

@article{weissgerber_2015_beyond_bar_graphs,
  title        = {Beyond bar and line graphs: time for a new data presentation paradigm},
  author       = {Weissgerber, Tracey L and Milic, Natasa M and Winham, Stacey J and Garovic, Vesna D},
  journal      = {PLoS Biology},
  year         = {2015},
  volume       = {13},
  number       = {4},
  pages        = {e1002128},
  doi          = {10.1371/journal.pbio.1002128},
  note         = {PMID 25901488, PMC4406565. Open access under CC BY 4.0. Quoted from the PMC
                  open-access text},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC4406565/},
  urldate      = {2026-10-02}
}

@inproceedings{bateman_2010_useful_junk,
  title        = {Useful junk? The effects of visual embellishment on comprehension and memorability of charts},
  author       = {Bateman, Scott and Mandryk, Regan L and Gutwin, Carl and Genest, Aaron and McDine, David and Brooks, Christopher},
  booktitle    = {Proceedings of the SIGCHI Conference on Human Factors in Computing Systems},
  publisher    = {ACM},
  year         = {2010},
  pages        = {2573--2582},
  doi          = {10.1145/1753326.1753716},
  note         = {Copyright 2010 ACM. Quoted from the camera-ready PDF as publicly posted at
                  sites.stat.columbia.edu/gelman/communication/Bateman2010.pdf (not an author site)},
  url          = {https://doi.org/10.1145/1753326.1753716},
  urldate      = {2026-10-02}
}

@article{crameri_2020_misuse_colour,
  title        = {The misuse of colour in science communication},
  author       = {Crameri, Fabio and Shephard, Grace E and Heron, Philip J},
  journal      = {Nature Communications},
  year         = {2020},
  volume       = {11},
  number       = {1},
  pages        = {5444},
  doi          = {10.1038/s41467-020-19160-7},
  note         = {PMID 33116149, PMC7595127. Open access under CC BY 4.0. Quoted from the PMC
                  open-access text},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC7595127/},
  urldate      = {2026-10-02}
}

@article{cumming_2007_error_bars,
  title        = {Error bars in experimental biology},
  author       = {Cumming, Geoff and Fidler, Fiona and Vaux, David L},
  journal      = {The Journal of Cell Biology},
  year         = {2007},
  volume       = {177},
  number       = {1},
  pages        = {7--11},
  doi          = {10.1083/jcb.200611141},
  note         = {PMID 17420288, PMC2064100. CC BY-NC-SA 4.0 (after the first six months). Quoted from
                  the PMC open-access text},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC2064100/},
  urldate      = {2026-10-02}
}

@article{krishnamurthy_2021_cvd_india,
  title        = {Prevalence of color vision deficiency among school-going boys in South India},
  author       = {Krishnamurthy, Sruthi Sree and Rangavittal, Subhiksha and Chandrasekar, Ambika and Narayanan, Anuradha},
  journal      = {Indian Journal of Ophthalmology},
  year         = {2021},
  volume       = {69},
  number       = {8},
  pages        = {2021--2025},
  doi          = {10.4103/ijo.IJO_3208_20},
  note         = {PMID 34304169, PMC8482944. Open access under CC BY-NC-SA 4.0. Quoted from the PMC
                  open-access text},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC8482944/},
  urldate      = {2026-10-02}
}
```

## 3. `sources/SOURCES.md`

Append to the latest table (word counts are `wc -w` of the file, header included).

```markdown
| `correll_2020_truncating_yaxis.txt` | Correll, Bertini & Franconeri, CHI 2020: 1-12 (doi 10.1145/3313831.3376222), authors' arXiv v2 PDF text layer; arXiv non-exclusive distribution licence. **Whole running text, abstract to Conclusion; chart text inside figures, Fig 5 caption and references not held** | 8,720 | Truncation "over-emphasizing minute differences"; Fig 1 caption: Fox News bar "6 times taller" for "a 4.6% increase in tax rate (ratio of 1.13 to 1)"; the guideline debate (Huff, Brinton, Cairo, Bergstrom & West's proportional ink, Tufte, Skelton); Exp 1 (n = 40): truncation raised perceived severity "(F(2,76) = 89, p < 0.0001)", no bar-vs-line difference "(F(1,38) = 0.5, p = 0.50)", 25% start adds 0.36 on a 1-5 scale; Exp 2 (n = 32): broken-axis and gradient designs did not remove the bias; Exp 3 (n = 25): bias persisted although trend estimates were accurate "(F(1,20) = 0.002, p = 0.96)"; Discussion rejects an "honest"/"dishonest" dichotomy |
| `heer_bostock_2010_crowdsourcing_perception.txt` | Heer & Bostock, CHI 2010: 203-212 (doi 10.1145/1753326.1753357), authors' PDF from vis.stanford.edu, text layer. © 2010 ACM. **Excerpts** | 4,629 | Graphical perception defined (after Cleveland); Exp 1A replicates Cleveland & McGill on MTurk, N=50 per chart, "only 14 out of 3,481 were incorrect (0.4%)"; log absolute error measure; "The ranking of types by accuracy is consistent between the two experiments"; position beat length; area worse than angle, both worse than position; Exp 1B rectangles of aspect ratio 1 judged worst; Findings: gridlines at least 8 pixels apart, chart heights beyond 80 pixels add little |
| `weissgerber_2015_beyond_bar_graphs.txt` | Weissgerber et al., *PLoS Biol* 2015;13:e1002128 (PMC4406565), PMC OA XML. CC BY 4.0. **Whole body; funding, most supporting-information entries and references not held** | 4,042 | Review of 703 physiology papers; "85.6% of papers included at least one bar graph"; "Many different datasets can lead to the same bar graph" (Fig 1); paired data hidden by bars (Fig 2); mean ± SE vs ± SD vs scatterplot (Fig 3); small samples (minimum group size median four); "78.1% of studies performed only parametric analyses"; three recommendations: show full data for small samples, change journal policies, train investigators |
| `bateman_2010_useful_junk.txt` | Bateman et al., CHI 2010: 2573-2582 (doi 10.1145/1753326.1753716), camera-ready PDF text layer from a third-party academic host (Columbia statistics, Gelman's reading folder). © 2010 ACM. **Excerpts; Previous Work and references not held** | 6,821 | 20 participants, 14 Holmes charts against plain versions; description accuracy no different (subject t19=0.84, p=.412; trend t19=0.23, p=.818); value message seen more in Holmes charts (t19=3.37, p=.003); recall after 2-3 weeks better for Holmes charts (subject t9=2.56, p=.015; value message t9=2.41, p=.020), no difference after five minutes except the value message; preferences; the authors' caution ("we do not advocate this strategy as a general principle"); minimalist charts are not free from bias |
| `crameri_2020_misuse_colour.txt` | Crameri, Shephard & Heron, *Nat Commun* 2020;11:5444 (PMC7595127), PMC OA XML. CC BY 4.0. **Whole body; Methods and references not held** | 5,216 | Rainbow and red-green colour maps distort data and exclude readers; "worldwide 0.5% of women and 8% of men are subject to a colour-vision deficiency"; perceptual uniformity and order; greyscale readability; colour-map classes (sequential, diverging, multi-sequential, cyclic); four checks for an unscientific colour map; Box 2 list of scientifically derived colour maps (viridis, cividis, ColorBrewer and others) |
| `cumming_2007_error_bars.txt` | Cumming, Fidler & Vaux, *J Cell Biol* 2007;177:7 (PMC2064100), PMC OA XML. CC BY-NC-SA 4.0. **Whole body; references not held** | 5,003 | Table I: range and SD descriptive, SE and CI inferential, with formulas (SE = SD/√n); Rule 1 "always describe in the figure legends what they are"; Rule 2 state n in the legend; replicates are not independent n; SE bars doubled approximate a 95% CI when n is 10 or more, ×4 when n = 3; overlap rules for SE and CI bars (Rules 6-7); repeated measures (Rule 8) |
| `krishnamurthy_2021_cvd_india.txt` | Krishnamurthy et al., *Indian J Ophthalmol* 2021;69:2021 (PMC8482944), PMC OA XML. CC BY-NC-SA 4.0. **Whole text except references** | 3,908 | 74,986 boys aged 11-17 in Kanchipuram district screened (Dalton's plates, confirmed with Ishihara); prevalence of colour-vision deficiency "2.76% (n = 2073; 95% confidence interval [CI]: 2.65–2.88)"; urban 3.17% vs rural 1.79%; worldwide figure in the introduction "around 8% in men and 0.5% in women"; boys only, one district |
```
