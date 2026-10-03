# S58-R1 intake, group B (numbers and readability): entries to merge

Three blocks for the conductor to paste into `sources/INDEX.yml` (under `files:`),
`check/references/library.bib` (append) and `sources/SOURCES.md` (a new section). Four files: Cole 2015,
Lang and Altman's SAMPL guidelines (the EQUATOR PDF), Plavén-Sigray et al. 2017, and one **fallback**,
Edwards et al. 2022, filed only because Kincaid et al. 1975 could not be opened (see `log-B.md`).
**Kincaid 1975 has no entry here**: nothing was obtained, so no key is filed. Citekeys were grepped in
`sources/INDEX.yml`, `check/references/library.bib` and the other S58 fragments on 2026-10-02, at the
start and again at the end of intake: none exists. Grep again at merge (S47-R1 and S52-R1 are adding keys on
other branches). Log: `books/S58-R1/intake/log-B.md`.

## 1. `sources/INDEX.yml`, under `files:`

```yaml
  cole_2015_too_many_digits:
    file: cole_2015_too_many_digits.txt
    what: >-
      Cole, Arch Dis Child 2015;100(7):608-9 (PMC4483789; CC BY 4.0), PMC OA XML. Whole body text (decimal
      places vs significant digits, EASE 2-3 effective digits, OR 22.68 example, birth weight g vs kg, rule of
      four, percentages, full precision until reporting) and Table 1 rounding rules for summary statistics in
      full. Reference callouts run into the text as bare digits; references NOT held
  lang_altman_2013_sampl:
    file: lang_altman_2013_sampl.txt
    what: >-
      Lang and Altman, SAMPL Guidelines, the 2013 PDF linked by EQUATOR (Science Editors' Handbook version;
      reprint free with citation), PDF text layer. Excerpts: title, reprint statement, the two guiding
      principles, Reporting numbers and descriptive statistics, Reporting risk, rates and ratios, Reporting
      hypothesis tests, each whole. The Int J Nurs Stud 2015 journal version was NOT opened
  plavensigray_2017_readability:
    file: plavensigray_2017_readability.txt
    what: >-
      Plaven-Sigray, Matheson, Schiffler and Thompson, eLife 2017;6:e27725 (PMC5584989; CC BY 4.0), PMC OA
      XML. Excerpts: abstract, impact statement, Introduction paras 1-2, Results (yearly FRE/NDC trend, Tables
      1-2, abstract vs full text, authors and jargon hypotheses), Discussion whole, preprocessing and
      FRE methods with the FRE formula as MathML. Figure captions, NDC formula, references NOT held
  edwards_2022_readability_formulas:
    file: edwards_2022_readability_formulas.txt
    what: >-
      FALLBACK for Kincaid 1975 (not obtained). Edwards et al., Surg Neurol Int 2022;13:401 (PMC9479524; CC
      BY-NC-SA 4.0), PMC OA XML. Excerpts: the seven Flesch Reading Ease bands (citing Flesch 1948), the FKGL
      and FRE formulas in words, reference entries 10 and 15. A secondary restatement, not checked against
      Flesch 1948 or Kincaid 1975
```

## 2. `check/references/library.bib`, append

```bibtex
@article{cole_2015_too_many_digits,
  title        = {Too many digits: the presentation of numerical data},
  author       = {Cole, T J},
  journal      = {Archives of Disease in Childhood},
  year         = {2015},
  volume       = {100},
  number       = {7},
  pages        = {608--609},
  doi          = {10.1136/archdischild-2014-307149},
  note         = {PMID 25877157, PMC4483789. Licensed CC BY 4.0. Quoted from the PMC Open Access
                  XML: the whole body text and Table 1 (rounding rules for summary statistics)},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC4483789/},
  urldate      = {2026-10-02}
}

@misc{lang_altman_2013_sampl,
  title        = {Basic Statistical Reporting for Articles Published in Biomedical Journals: The
                  ``Statistical Analyses and Methods in the Published Literature'' or The SAMPL Guidelines},
  author       = {Lang, Thomas A and Altman, Douglas G},
  year         = {2013},
  howpublished = {EQUATOR Network PDF; also in Smart P, Maisonneuve H, Polderman A (eds), Science
                  Editors' Handbook, European Association of Science Editors, 2013},
  note         = {"This document may be reprinted without charge but must include the original
                  citation." Quoted from the PDF the EQUATOR Network links: guiding principles, reporting
                  numbers and descriptive statistics, risk, rates and ratios, hypothesis tests. Also
                  published as Int J Nurs Stud 2015;52(1):5-9 (PMID 25441757,
                  doi:10.1016/j.ijnurstu.2014.09.006); that version was not consulted},
  url          = {https://www.equator-network.org/wp-content/uploads/2013/07/SAMPL-Guidelines-6-27-13.pdf},
  urldate      = {2026-10-02}
}

@article{plavensigray_2017_readability,
  title        = {The readability of scientific texts is decreasing over time},
  author       = {Plav{\'e}n-Sigray, Pontus and Matheson, Granville James and Schiffler, Bj{\"o}rn Christian
                  and Thompson, William Hedley},
  journal      = {eLife},
  year         = {2017},
  volume       = {6},
  pages        = {e27725},
  doi          = {10.7554/eLife.27725},
  note         = {PMID 28873054, PMC5584989. Licensed CC BY 4.0. Quoted from the PMC Open Access
                  XML; figures (images), the New Dale-Chall formula and the word-list methods are not quoted},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC5584989/},
  urldate      = {2026-10-02}
}

@article{edwards_2022_readability_formulas,
  title        = {Academics versus the Internet: Evaluating the readability of patient education
                  materials for cerebrovascular conditions from major academic centers},
  author       = {Edwards, Caleb Simpeh and Ammanuel, Simon Gashaw and Silva, Ogonna N Nnamani and
                  Greeneway, Garret P and Bunch, Katherine M and Meisner, Lars W and Page, Paul S and
                  Ahmed, Azam S},
  journal      = {Surgical Neurology International},
  year         = {2022},
  volume       = {13},
  pages        = {401},
  doi          = {10.25259/SNI_502_2022},
  note         = {PMID 36128118, PMC9479524. Licensed CC BY-NC-SA 4.0. Quoted only for its restatement
                  of the Flesch Reading Ease bands (which it attributes to Flesch 1948) and of the
                  Flesch-Kincaid grade and Reading Ease formulas; stands in for Kincaid et al. 1975,
                  which was not obtained},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC9479524/},
  urldate      = {2026-10-02}
}
```

## 3. `sources/SOURCES.md`, new section (same columns as the main table)

```markdown
## S58-R1 intake, group B: numbers and readability (2 Oct 2026)

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `cole_2015_too_many_digits.txt` | Cole, *Arch Dis Child* 2015;100:608-9 (PMC4483789), PMC OA XML. CC BY 4.0. **Whole body and Table 1; no references** | 2,467 | Decimal places vs significant digits defined; EASE "2–3 effective digits"; OR 22.68 (95% CI 7.51 to 73.67) rounded to 23 (7.5 to 74); birth weight 3465.31±51.36 g (six significant digits) vs 3.05±0.57 kg; rule of four; percentage rule by range across groups; "intermediate calculations are carried out to full precision"; Table 1 rules for mean, percentage, mean difference, regression and correlation coefficients, risk ratio, SD, SE, CI, test statistics, p value. Superscript callouts appear as bare digits |
| `lang_altman_2013_sampl.txt` | Lang and Altman, SAMPL Guidelines, 2013 PDF linked by EQUATOR (reprint free with citation). **Excerpts** | 1,522 | Two guiding principles (ICMJE "enough detail ... to verify"; numerators and denominators of percentages); "round to a reasonable extent", mean age to the nearest year; total sample and group sizes; mean (SD) not mean ± SD; SE not for variability; rates with numerator, denominator, period, unit multiplier; P values as equalities to one or two decimal places, smallest P <0.001. Journal version (Int J Nurs Stud 2015) not opened |
| `plavensigray_2017_readability.txt` | Plavén-Sigray et al., *eLife* 2017;6:e27725 (PMC5584989), PMC OA XML. CC BY 4.0. **Excerpts** | 3,909 | 709,577 abstracts, 123 journals, 1881-2015; yearly FRE r = -0.93; Table 1 (FRE year beta -0.19 in M2) and Table 2 (authors); abstract vs full text FRE r = 0.60; jargon list 2,138 words, r = 0.96; FRE 100 = 10- to 11-year-old, 0-30 college graduates; FRE below 0 in 14% (1960) and 22% (2015); limits of formulas; FRE formula as MathML; syllable-counting method |
| `edwards_2022_readability_formulas.txt` | **Fallback** for Kincaid 1975. Edwards et al., *Surg Neurol Int* 2022;13:401 (PMC9479524), PMC OA XML. CC BY-NC-SA 4.0. **Excerpts** | 887 | FRE bands 100–91 very easy to 30–0 very difficult (citing Flesch 1948); FKGL = (0.39 × words per sentence) + (11.8 × syllables per word) − 15.59 and FRE = 206.835 − 1.015 × (words/sentences) − 84.6 × (syllables/words), in words. Secondary: not checked against the originals |
```
