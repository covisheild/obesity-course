# S57-R1 intake, group a (learning-science papers): entries to merge

Three blocks for the conductor to paste into `sources/INDEX.yml` (under `files:`),
`check/references/library.bib` (append) and `sources/SOURCES.md` (a new section). Citekeys were
grepped in `sources/INDEX.yml` and `check/references/library.bib` on 2026-09-24: none exists.
Twelve files: eleven for the eleven assigned works (two of them abstract-only) plus one substitute
(`fisher_keil_2015_ioed`) for Rozenblit and Keil's unobtainable body.

## 1. `sources/INDEX.yml`, under `files:`

```yaml
  freeman_2014_active_learning:
    file: freeman_2014_active_learning.txt
    what: >-
      Freeman et al., PNAS 2014;111:8410 (PNAS open access option; no CC licence stated), publisher article
      page. Significance, abstract, introduction, Results with Table 1, Discussion, Materials and Methods.
      Supporting Information (Tables S1-S4, SI methods) NOT held
  deslauriers_2019_feeling_of_learning:
    file: deslauriers_2019_feeling_of_learning.txt
    what: >-
      Deslauriers et al., PNAS 2019;116:19251 (CC BY-NC-ND 4.0), PMC OA XML. Whole body: design, Tables 1-3,
      FOL vs TOL results, fluency and novice-metacognition analyses, the early-semester intervention. Figure bar
      values and SI Appendix NOT held
  newton_miah_2017_learning_styles:
    file: newton_miah_2017_learning_styles.txt
    what: >-
      Newton and Miah, Front Psychol 2017;8:444 (CC BY), publisher article page. Whole body (abstract to end of
      Discussion). In-text citations were dropped by the extraction; figures NOT held
  weinstein_2018_science_of_learning:
    file: weinstein_2018_science_of_learning.txt
    what: >-
      Weinstein, Madan and Sumeracki, Cogn Res Princ Implic 2018;3:2 (CC BY 4.0), PMC OA XML. Excerpts: licence,
      abstract, Table 1, figure captions, and the sections Spaced practice, Interleaving, Retrieval practice,
      Elaboration, Concrete examples. Introduction, Dual coding and Conclusion NOT held
  dunlosky_2013_learning_techniques:
    file: dunlosky_2013_learning_techniques.txt
    what: >-
      Dunlosky et al., Psychol Sci Public Interest 2013;14:4-58 (publisher copyright, free to read via APS),
      text layer of the published PDF from a third-party host (whz.de). Excerpts: summary, introduction,
      Tables 1-2; whole sections on elaborative interrogation, self-explanation, highlighting, rereading,
      practice testing, distributed practice; Closing Remarks with Table 4 (utility ratings). Summarization,
      keyword mnemonic, imagery, interleaving NOT held
  pashler_2008_learning_styles:
    file: pashler_2008_learning_styles.txt
    what: >-
      Pashler, McDaniel, Rohrer and Bjork, Psychol Sci Public Interest 2008;9:105-119 (publisher copyright).
      ABSTRACT ONLY, from the USF Digital Commons record: meshing hypothesis, the experimental criteria, "virtually
      no evidence". The body (crossover-interaction figures, the studies reviewed) is NOT held
  rozenblit_keil_2002_ioed:
    file: rozenblit_keil_2002_ioed.txt
    what: >-
      Rozenblit and Keil, Cogn Sci 2002;26:521-562 (PMC3062901, NIH author manuscript, not open access).
      ABSTRACT ONLY, from the NCBI efetch record. Studies 1-12 and the before/after ratings are NOT held; see
      fisher_keil_2015_ioed
  fisher_keil_2015_ioed:
    file: fisher_keil_2015_ioed.txt
    what: >-
      Fisher and Keil, Cognitive Science online first 2015, doi 10.1111/cogs.12280 (publisher copyright, author-lab
      copy). Three excerpts: abstract, the IOED paradigm paragraph (rating drops from Time 1 to Time 2, citing
      Rozenblit and Keil 2002), and one General Discussion paragraph. Substitute source for Rozenblit and Keil
  sweller_2019_cognitive_load:
    file: sweller_2019_cognitive_load.txt
    what: >-
      Sweller, van Merrienboer and Paas, Educ Psychol Rev 2019;31:261-292 (CC BY 4.0), publisher article page.
      Excerpts: abstract, introduction, short history (architecture, load categories, the seven 1998 effects),
      narrow limits of change, post-1998 effects through self-explanation, Conclusions. Table 1 NOT held
  agarwal_2021_retrieval_practice:
    file: agarwal_2021_retrieval_practice.txt
    what: >-
      Agarwal, Nunes and Blunt, Educ Psychol Rev 2021;33:1409-1453 (publisher copyright, "under exclusive licence
      to Springer"; NOT open access), text layer of the published PDF on the first author's site. Main text with
      Tables 1-4: 50 experiments, 49 effect sizes, distribution, moderators, recommendations. Appendix Table 5 NOT held
  roediger_karpicke_2006_testing_effect:
    file: roediger_karpicke_2006_testing_effect.txt
    what: >-
      Roediger and Karpicke, Psychol Sci 2006;17:249-255 (publisher copyright), text layer of the published PDF
      from a third-party host (gwern.net). Whole article text to the end of the General Discussion: Experiment 1
      (5-min, 2-day, 1-week) and Experiment 2 (SSSS/SSST/STTT) results, Tables 1-2. Figures NOT held
  cepeda_2008_spacing_ridgeline:
    file: cepeda_2008_spacing_ridgeline.txt
    what: >-
      Cepeda, Vul, Rohrer, Wixted and Pashler, Psychol Sci 2008;19:1095-1102, the authors' IN-PRESS MANUSCRIPT
      from ERIC (ED505660), not the published version. Whole text: optimal gaps 1, 11, 21, 21 days for RIs 7, 35,
      70, 350 days (recall), percentage gains, the fitted surface, Table 1, figure captions. Figure 3 values NOT held
```

## 2. `check/references/library.bib`, append

```bibtex
@article{freeman_2014_active_learning,
  title        = {Active learning increases student performance in science, engineering, and mathematics},
  author       = {Freeman, Scott and Eddy, Sarah L and McDonough, Miles and Smith, Michelle K and
                  Okoroafor, Nnadozie and Jordt, Hannah and Wenderoth, Mary Pat},
  journal      = {Proceedings of the National Academy of Sciences of the United States of America},
  year         = {2014},
  volume       = {111},
  number       = {23},
  pages        = {8410--8415},
  doi          = {10.1073/pnas.1319030111},
  note         = {PMID 24821756, PMC4060654. Freely available through the PNAS open access option;
                  no Creative Commons licence stated. Quoted from the publisher's article page; the
                  Supporting Information is not quoted},
  url          = {https://www.pnas.org/doi/10.1073/pnas.1319030111},
  urldate      = {2026-09-24}
}

@article{deslauriers_2019_feeling_of_learning,
  title        = {Measuring actual learning versus feeling of learning in response to being actively
                  engaged in the classroom},
  author       = {Deslauriers, Louis and McCarty, Logan S and Miller, Kelly and Callaghan, Kristina and
                  Kestin, Greg},
  journal      = {Proceedings of the National Academy of Sciences of the United States of America},
  year         = {2019},
  volume       = {116},
  number       = {39},
  pages        = {19251--19257},
  doi          = {10.1073/pnas.1821936116},
  note         = {PMID 31484770, PMC6765278. CC BY-NC-ND 4.0. Quoted from the PubMed Central
                  open-access text},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC6765278/},
  urldate      = {2026-09-24}
}

@article{newton_miah_2017_learning_styles,
  title        = {Evidence-based higher education -- is the learning styles `myth' important?},
  author       = {Newton, Philip M and Miah, Mahallad},
  journal      = {Frontiers in Psychology},
  year         = {2017},
  volume       = {8},
  pages        = {444},
  doi          = {10.3389/fpsyg.2017.00444},
  note         = {PMID 28396647, PMC5366351. CC BY. Quoted from the publisher's article page},
  url          = {https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00444/full},
  urldate      = {2026-09-24}
}

@article{weinstein_2018_science_of_learning,
  title        = {Teaching the science of learning},
  author       = {Weinstein, Yana and Madan, Christopher R and Sumeracki, Megan A},
  journal      = {Cognitive Research: Principles and Implications},
  year         = {2018},
  volume       = {3},
  pages        = {2},
  doi          = {10.1186/s41235-017-0087-y},
  note         = {PMID 29399621, PMC5780548. CC BY 4.0. Quoted from the PubMed Central
                  open-access text},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC5780548/},
  urldate      = {2026-09-24}
}

@article{dunlosky_2013_learning_techniques,
  title        = {Improving students' learning with effective learning techniques: promising directions
                  from cognitive and educational psychology},
  author       = {Dunlosky, John and Rawson, Katherine A and Marsh, Elizabeth J and Nathan, Mitchell J and
                  Willingham, Daniel T},
  journal      = {Psychological Science in the Public Interest},
  year         = {2013},
  volume       = {14},
  number       = {1},
  pages        = {4--58},
  doi          = {10.1177/1529100612453266},
  note         = {PMID 26173288. Publisher copyright (the authors, 2013; SAGE); free to read via the
                  Association for Psychological Science. Quoted from the text of the published PDF,
                  read from a copy hosted by Westsaechsische Hochschule Zwickau because the
                  publisher's pages refused automated access},
  url          = {https://doi.org/10.1177/1529100612453266},
  urldate      = {2026-09-24}
}

@article{pashler_2008_learning_styles,
  title        = {Learning styles: concepts and evidence},
  author       = {Pashler, Harold and McDaniel, Mark and Rohrer, Doug and Bjork, Robert},
  journal      = {Psychological Science in the Public Interest},
  year         = {2008},
  volume       = {9},
  number       = {3},
  pages        = {105--119},
  doi          = {10.1111/j.1539-6053.2009.01038.x},
  note         = {PMID 26162104. Publisher copyright. Only the abstract is quoted, from the
                  University of South Florida Digital Commons record; the body was not obtained},
  url          = {https://doi.org/10.1111/j.1539-6053.2009.01038.x},
  urldate      = {2026-09-24}
}

@article{rozenblit_keil_2002_ioed,
  title        = {The misunderstood limits of folk science: an illusion of explanatory depth},
  author       = {Rozenblit, Leonid and Keil, Frank},
  journal      = {Cognitive Science},
  year         = {2002},
  volume       = {26},
  number       = {5},
  pages        = {521--562},
  doi          = {10.1207/s15516709cog2605_1},
  note         = {PMID 21442007, PMC3062901 (NIH author manuscript). Copyright Cognitive Science
                  Society. Only the abstract is quoted; the studies and their results were not
                  obtained},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC3062901/},
  urldate      = {2026-09-25}
}

@article{fisher_keil_2015_ioed,
  title        = {The curse of expertise: when more knowledge leads to miscalibrated explanatory insight},
  author       = {Fisher, Matthew and Keil, Frank C},
  journal      = {Cognitive Science},
  year         = {2015},
  doi          = {10.1111/cogs.12280},
  note         = {Online-first version; print volume and pages not confirmed. Copyright Cognitive
                  Science Society. Quoted from the online-first PDF hosted by the Keil laboratory at
                  Yale, for its statement of the illusion-of-explanatory-depth procedure and result},
  url          = {https://cogdevlab.yale.edu/sites/default/files/files/Fisher2015.pdf},
  urldate      = {2026-09-25}
}

@article{sweller_2019_cognitive_load,
  title        = {Cognitive architecture and instructional design: 20 years later},
  author       = {Sweller, John and van Merri{\"e}nboer, Jeroen J G and Paas, Fred},
  journal      = {Educational Psychology Review},
  year         = {2019},
  volume       = {31},
  number       = {2},
  pages        = {261--292},
  doi          = {10.1007/s10648-019-09465-5},
  note         = {CC BY 4.0. Quoted from the publisher's article page; its Table 1 is not quoted},
  url          = {https://link.springer.com/article/10.1007/s10648-019-09465-5},
  urldate      = {2026-09-24}
}

@article{agarwal_2021_retrieval_practice,
  title        = {Retrieval practice consistently benefits student learning: a systematic review of
                  applied research in schools and classrooms},
  author       = {Agarwal, Pooja K and Nunes, Ludmila D and Blunt, Janell R},
  journal      = {Educational Psychology Review},
  year         = {2021},
  volume       = {33},
  number       = {4},
  pages        = {1409--1453},
  doi          = {10.1007/s10648-021-09595-9},
  note         = {Publisher copyright (under exclusive licence to Springer); not open access. Quoted
                  from the published PDF posted on the first author's website},
  url          = {https://pdf.poojaagarwal.com/Agarwal_etal_2021_EDPR.pdf},
  urldate      = {2026-09-24}
}

@article{roediger_karpicke_2006_testing_effect,
  title        = {Test-enhanced learning: taking memory tests improves long-term retention},
  author       = {Roediger, Henry L, III and Karpicke, Jeffrey D},
  journal      = {Psychological Science},
  year         = {2006},
  volume       = {17},
  number       = {3},
  pages        = {249--255},
  doi          = {10.1111/j.1467-9280.2006.01693.x},
  note         = {PMID 16507066. Copyright Association for Psychological Science. Quoted from the
                  text of the published PDF, read from a copy hosted on gwern.net because the
                  publisher and the authors' laboratory pages were not reachable},
  url          = {https://doi.org/10.1111/j.1467-9280.2006.01693.x},
  urldate      = {2026-09-24}
}

@article{cepeda_2008_spacing_ridgeline,
  title        = {Spacing effects in learning: a temporal ridgeline of optimal retention},
  author       = {Cepeda, Nicholas J and Vul, Edward and Rohrer, Doug and Wixted, John T and
                  Pashler, Harold},
  journal      = {Psychological Science},
  year         = {2008},
  volume       = {19},
  number       = {11},
  pages        = {1095--1102},
  doi          = {10.1111/j.1467-9280.2008.02209.x},
  note         = {PMID 19076480; ERIC ED505660. Quoted from the authors' in-press manuscript as
                  deposited in ERIC, which it says may differ from the published version},
  url          = {https://files.eric.ed.gov/fulltext/ED505660.pdf},
  urldate      = {2026-09-24}
}
```

## 3. `sources/SOURCES.md`, a new section

```markdown
## Added by the S57-R1 source intake, group a (learning-science papers), 2026-09-24

Every passage was cut by script from the raw text the TinyFish `fetch_content` tool returned
(saved from the tool's own result file, not retyped) and re-checked as a whitespace-normalised
substring of that fetch: **36 of 36**. Log in `books/S57-R1/intake/log-a.md`. Three files rest on
copies not served by the publisher (Dunlosky 2013 and Roediger and Karpicke 2006: the published PDF
from a third-party host; Cepeda 2008: the authors' in-press manuscript in ERIC), and each header
says so. Two are abstract-only (Pashler 2008, Rozenblit and Keil 2002).

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `freeman_2014_active_learning.txt` | Freeman et al., *PNAS* 2014;111:8410 (PMC4060654), PNAS article page. PNAS open access option, no CC licence. **Most of the article; SI not held** | 5,323 | 225 studies; SMD 0.47 on exams and concept inventories (158 studies); failure odds ratio 1.95, risk ratio 1.5, failure 21.8% vs 33.8% (67 studies); 50th to 68th percentile; about 6% on exam scores; Table 1 Hedges' g by quality of controls (randomized 0.514); definitions of active learning and traditional lecturing; Hedges' g as the effect size |
| `deslauriers_2019_feeling_of_learning.txt` | Deslauriers et al., *PNAS* 2019;116:19251 (PMC6765278), PMC OA XML. CC BY-NC-ND 4.0. **Whole body** | 6,175 | Crossover randomized design, 149 students, identical materials; active groups 0.46 SD higher on the test of learning and 0.56 SD lower feeling of learning (Table 3); fluency and novice metacognition as causes; 20-min early-semester intervention; tests taken at the end of each class, not days later |
| `newton_miah_2017_learning_styles.txt` | Newton and Miah, *Front Psychol* 2017;8:444 (PMC5366351), Frontiers page. CC BY. **Whole body; in-text citations lost** | 6,179 | 114 UK HE academics; 58% agree learning in preferred style is better, 64% try to accommodate styles, 33% used them in the last 12 months; 31.6% would still plan to; trend 93% (2012), 76% (2014), 64% (US HE), 58% |
| `weinstein_2018_science_of_learning.txt` | Weinstein, Madan and Sumeracki, *Cogn Res* 2018;3:2 (PMC5780548), PMC OA XML. CC BY 4.0. **Excerpts** | 7,385 | Table 1 six strategies; spaced practice (Cepeda 2008 named: optimal gap contingent on retention interval; students feel less confident when spacing); interleaving; retrieval practice; elaboration and self-explanation; concrete examples |
| `dunlosky_2013_learning_techniques.txt` | Dunlosky et al., *PSPI* 2013;14:4 (PMID 26173288), published PDF text layer from a third-party host. Publisher copyright, free via APS. **Excerpts** | 25,557 | Table 1 ten techniques; utility ratings: practice testing and distributed practice high, elaborative interrogation and self-explanation moderate, highlighting and rereading low (each section's Overall assessment and Table 4); how utility was rated |
| `pashler_2008_learning_styles.txt` | Pashler et al., *PSPI* 2008;9:105, USF Digital Commons record. **Abstract only** | 1,038 | Meshing hypothesis defined; the criteria: groups by style, random assignment to methods, same final test, and the required interaction; "virtually no evidence" for it. The crossover figures and the studies reviewed are NOT held |
| `rozenblit_keil_2002_ioed.txt` | Rozenblit and Keil, *Cogn Sci* 2002;26:521 (PMC3062901, author manuscript), NCBI efetch record. **Abstract only** | 591 | Names the illusion of explanatory depth; stronger for explanatory than factual, procedural or narrative knowledge. The before/after ratings are NOT held |
| `fisher_keil_2015_ioed.txt` | Fisher and Keil, *Cognitive Science* online first 2015, doi 10.1111/cogs.12280, Keil lab PDF. **Three excerpts; substitute for Rozenblit and Keil** | 913 | IOED paradigm: rate, write explanation, re-rate; "a consistent drop from Time 1 to Time 2" (citing Rozenblit and Keil 2002); warned participants still show it |
| `sweller_2019_cognitive_load.txt` | Sweller, van Merriënboer and Paas, *Educ Psychol Rev* 2019;31:261, Springer page. CC BY 4.0. **Excerpts; Table 1 not held** | 6,735 | Working memory limited for novel information, limits disappear for information from long-term memory; intrinsic, extraneous, germane load; worked example effect; expertise reversal; guidance fading; self-explanation effect. No numeric working-memory capacity is stated |
| `agarwal_2021_retrieval_practice.txt` | Agarwal, Nunes and Blunt, *Educ Psychol Rev* 2021;33:1409, published PDF on the first author's site. Publisher copyright, **not open access**. **Main text; Appendix not held** | 10,875 | 50 classroom experiments, 49 effect sizes, n = 5374; 57% medium or large (28 of 49 d > 0.50), 16 large, 3 negative; 10 medical-school experiments; comparison conditions; recommendations |
| `roediger_karpicke_2006_testing_effect.txt` | Roediger and Karpicke, *Psychol Sci* 2006;17:249 (PMID 16507066), published PDF text layer from a third-party host. Publisher copyright. **Whole text** | 5,219 | Exp. 1: 5 min restudy 81% vs test 75%; 2 days test 68% vs 54%; 1 week 56% vs 42%. Exp. 2: 5 min SSSS 83%, SSST 78%, STTT 71%; 1 week STTT 61%, SSST 56%, SSSS 40%; forgetting 52%, 28%, 14%; SSSS most confident. PDF renders "=" as "5" |
| `cepeda_2008_spacing_ridgeline.txt` | Cepeda et al., *Psychol Sci* 2008;19:1095 (PMID 19076480), **in-press manuscript** from ERIC ED505660 | 4,833 | 1354 subjects, 26 gap x RI conditions (Table 1); optimal gaps 1, 11, 21, 21 days (recall) for RIs 7, 35, 70, 350 days; optimal vs zero gap +64% recall; fitted optimum 23 days = 7% of a 350-day RI; abstract: about 20% of delay for a few weeks, about 5% at one year |
```
