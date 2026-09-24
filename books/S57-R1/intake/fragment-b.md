# Fragment b · S57-R1 intake (statistics, teaching guides, assessment, leadership)

For the conductor to merge into `sources/INDEX.yml`, `check/references/library.bib` and `sources/SOURCES.md`
in one commit. Seven new files and one extended file. Log: `books/S57-R1/intake/log-b.md`.

## 1. `sources/INDEX.yml`

One UPDATE (replace the existing `what:` of `openstax_intro_stats_2e`; `file:` unchanged) and seven new entries under `files:`.

```yaml
  openstax_intro_stats_2e:
    file: openstax_intro_stats_2e.txt
    what: >-
      OpenStax Introductory Statistics 2e, sections 1.1, 1.2, 2.3, 2.5, 2.7, 3.1-3.4, 7.1 - Part D's textbook anchor;
      4.1 (discrete probability distribution) and 4.2 (expected value and standard deviation) added 2026-09-24 for S02-R1;
      1.4 (experimental design and ethics: explanatory and response variables, treatments, lurking variables, random
      assignment, control group and placebo, blinding) added 2026-09-24 for S57-R1
  cochrane_handbook_ch06_v6_5:
    file: cochrane_handbook_ch06_v6_5.txt
    what: >-
      Cochrane Handbook for Systematic Reviews of Interventions v6.5 (2024), chapter 6 (last updated August 2023), excerpts:
      Key Points and citation line; 6.5.1 effect measures for continuous outcomes, 6.5.1.1 mean difference, 6.5.1.2
      standardized mean difference with MECIR Box 6.5.a, Hedges' g and Glass' delta. Formulae are images and are not held
  chatterjee_corral_2017_objectives:
    file: chatterjee_corral_2017_objectives.txt
    what: >-
      Chatterjee & Corral, J Educ Perioper Med 2017;19(4):E610 (PMC5944406), whole article text from the publisher's PDF
      text layer (tables flattened): learning goal vs objective, the five elements, SMART, verbs to avoid, one action per
      objective, Bloom levels with Table 2 verb lists, instructional alignment and constructive alignment; references omitted
  adams_2015_bloom:
    file: adams_2015_bloom.txt
    what: >-
      Adams, J Med Libr Assoc 2015;103(3):152-153 (PMC4511057), whole article except biography and references: Bloom's six
      original levels with examples, the revised levels remember/understand/apply/analyze/evaluate/create, the four
      knowledge types, action verbs and assessment
  hake_1998_normalized_gain:
    file: hake_1998_normalized_gain.txt
    what: >-
      Hake, Am J Phys 1998;66(1):64-74, ABSTRACT ONLY (publisher-deposited abstract from Crossref): definition of the average
      normalized gain <g> = (%post - %pre)/(100 - %pre); traditional <g> 0.23 +/- 0.04 (14 courses, N=2084) vs
      interactive-engagement 0.48 +/- 0.14 (48 courses, N=4458). Full paper not held
  biggs_1996_constructive_alignment:
    file: biggs_1996_constructive_alignment.txt
    what: >-
      Biggs, High Educ 1996;32(3):347-364, ABSTRACT ONLY (Springer article page): constructive alignment as constructivism
      guiding objectives, teaching/learning activities and assessment. Full paper paywalled, not held
  frich_2015_physician_leadership:
    file: frich_2015_physician_leadership.txt
    what: >-
      Frich et al., J Gen Intern Med 2015;30(5):656-674 (PMC4395611, CC BY 4.0), excerpts: licence, abstract, introduction,
      Data Analysis with Kirkpatrick's four levels (reaction, knowledge, behavioral change, system results) and Table 1,
      Table 2, Results on duration/aims/methods/evaluation outcomes, the whole Discussion. Table 3 omitted
  stoller_2020_leadership:
    file: stoller_2020_leadership.txt
    what: >-
      Stoller, Chest 2021;159(3):1147-1154 (PMC7501065), excerpts: licence, abstract, "The Ubiquity of the Need for
      Leadership" with Table 1 "Attributes of Managing vs Leading" (after Kotter 1990: planning and budgeting, organizing
      and staffing, controlling and solving vs setting direction, aligning people, motivating and inspiring). Held as the
      open substitute for Kotter's HBR article, which is paywalled and not held
```

## 2. `check/references/library.bib`

One UPDATE (replace the `note` of `openstax_intro_stats_2e`) and seven new entries.

```bibtex
  note         = {Licensed CC BY-NC-SA 4.0. Published 13 December 2023; web version last updated
                  7 July 2026. ISBN 978-1-711472-57-7. Sections 1.1, 1.2, 1.4, 2.3, 2.5, 2.7,
                  3.1-3.4, 4.1, 4.2 and 7.1 held and quoted. Anchor for Book 0 Part D},

@incollection{cochrane_handbook_ch06_v6_5,
  title        = {Chapter 6: Choosing effect measures and computing estimates of effect},
  author       = {Higgins, Julian PT and Li, Tianjing and Deeks, Jonathan J},
  editor       = {Higgins, Julian PT and Thomas, James and Chandler, Jacqueline and Cumpston, Miranda
                  and Li, Tianjing and Page, Matthew J and Welch, Vivian A},
  booktitle    = {Cochrane Handbook for Systematic Reviews of Interventions, version 6.5},
  publisher    = {Cochrane},
  year         = {2024},
  note         = {Chapter last updated August 2023. Free to read online; no open licence stated
                  (Cochrane copyright). Section 6.5.1 (mean difference, standardized mean
                  difference) quoted; the chapter's formulae are images and none is quoted},
  url          = {https://training.cochrane.org/handbook/current/chapter-06},
  urldate      = {2026-09-24}
}

@article{chatterjee_corral_2017_objectives,
  title        = {How to write well-defined learning objectives},
  author       = {Chatterjee, Debnath and Corral, Janet},
  journal      = {Journal of Education in Perioperative Medicine},
  year         = {2017},
  volume       = {19},
  number       = {4},
  pages        = {E610},
  note         = {PMID 29766034, PMC5944406. Copyright 2017 Society for Education in
                  Anesthesia; free to read, no open licence. Quoted from the publisher's PDF},
  url          = {https://www.seahq.org/assets/docs/xix_4_chatterjee.pdf},
  urldate      = {2026-09-24}
}

@article{adams_2015_bloom,
  title        = {Bloom's taxonomy of cognitive learning objectives},
  author       = {Adams, Nancy E},
  journal      = {Journal of the Medical Library Association},
  year         = {2015},
  volume       = {103},
  number       = {3},
  pages        = {152--153},
  doi          = {10.3163/1536-5050.103.3.010},
  note         = {PMID 26213509, PMC4511057. Copyright 2015, the author; free to read in PMC,
                  no open licence stated},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC4511057/},
  urldate      = {2026-09-24}
}

@article{hake_1998_normalized_gain,
  title        = {Interactive-engagement versus traditional methods: a six-thousand-student survey
                  of mechanics test data for introductory physics courses},
  author       = {Hake, Richard R},
  journal      = {American Journal of Physics},
  year         = {1998},
  volume       = {66},
  number       = {1},
  pages        = {64--74},
  doi          = {10.1119/1.18809},
  note         = {Publisher copyright (American Association of Physics Teachers). Only the
                  abstract was read and is quoted (as deposited by the publisher with Crossref);
                  the full paper was not obtained},
  url          = {https://doi.org/10.1119/1.18809},
  urldate      = {2026-09-25}
}

@article{biggs_1996_constructive_alignment,
  title        = {Enhancing teaching through constructive alignment},
  author       = {Biggs, John},
  journal      = {Higher Education},
  year         = {1996},
  volume       = {32},
  number       = {3},
  pages        = {347--364},
  doi          = {10.1007/BF00138871},
  note         = {Publisher copyright (Kluwer, now Springer); subscription content. Only the
                  abstract, shown free on the publisher's page, was read and is quoted},
  url          = {https://link.springer.com/article/10.1007/BF00138871},
  urldate      = {2026-09-24}
}

@article{frich_2015_physician_leadership,
  title        = {Leadership development programs for physicians: a systematic review},
  author       = {Frich, Jan C and Brewster, Amanda L and Cherlin, Emily J and Bradley, Elizabeth H},
  journal      = {Journal of General Internal Medicine},
  year         = {2015},
  volume       = {30},
  number       = {5},
  pages        = {656--674},
  doi          = {10.1007/s11606-014-3141-1},
  note         = {PMID 25527339, PMC4395611. Open access under CC BY 4.0. Quoted from the PMC
                  open-access text},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC4395611/},
  urldate      = {2026-09-24}
}

@article{stoller_2020_leadership,
  title        = {Leadership essentials for CHEST medicine professionals: models, attributes, and
                  styles},
  author       = {Stoller, James K},
  journal      = {Chest},
  year         = {2021},
  volume       = {159},
  number       = {3},
  pages        = {1147--1154},
  doi          = {10.1016/j.chest.2020.09.095},
  note         = {PMID 32956716, PMC7501065. Copyright 2020 American College of Chest Physicians,
                  all rights reserved; in PMC under Elsevier's COVID-19 resource-centre permission.
                  Its Table 1 (managing vs leading) is adapted from Kotter, What leaders really do,
                  Harv Bus Rev 1990;68(3):103-111},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC7501065/},
  urldate      = {2026-09-25}
}
```

## 3. `sources/SOURCES.md`

Replace the existing `openstax_intro_stats_2e.txt` row with the first line below; append the other seven rows to the latest table
(word counts are `wc -w` of the file, header included).

```markdown
| `openstax_intro_stats_2e.txt` | OpenStax *Introductory Statistics 2e* (2023; web version updated 7 Jul 2026), thirteen sections: 1.1, 1.2, 2.3, 2.5, 2.7, 3.1, 3.2, 3.3, 3.4, 7.1; 4.1, 4.2 added 2026-09-24 by the S02-R1 intake; 1.4 added 2026-09-24 by the S57-R1 intake | 36,890 | Probability as "long-term relative frequency" (3.1); the independence conditions (3.2); "the larger the sample, the smaller the sampling error" and sampling bias (1.2); the median (2.5); the standard deviation and n minus 1 (2.7); "divided by the square root of n" (7.1); explanatory and response variables, treatments, lurking variables, "random assignment of experimental units to treatment groups", control group and placebo, blinding and double-blind, IRB and informed consent (1.4). Mathematical typesetting is garbled by extraction; quote prose only |
| `cochrane_handbook_ch06_v6_5.txt` | Cochrane Handbook v6.5 (2024), ch. 6 (updated Aug 2023), Key Points and §6.5.1-6.5.1.2. Free to read, no open licence. **Excerpts; no formula held** | 1,930 | MD as "the absolute difference between the mean value in two groups"; SMD "relative to the between-participant variability"; "the same proportion of the standard deviation (SD) will have the same SMD"; direction of scales (MECIR C61); SMD in Cochrane = Hedges' (adjusted) g with pooled SD; Glass' delta uses the comparator SD |
| `chatterjee_corral_2017_objectives.txt` | Chatterjee & Corral, *J Educ Perioper Med* 2017;19:E610 (PMC5944406), publisher's PDF text layer. © Society for Education in Anesthesia. Whole text except references | 3,067 | Goal vs objective; "who, will do, how much or how well, of what, by when"; SMART; "understand, know, learn, appreciate ... should be avoided"; one action per objective; Bloom levels and Table 2 verb lists (flattened); instructional alignment (the Golden Triangle); "Constructive alignment underscores ..." |
| `adams_2015_bloom.txt` | Adams, *J Med Libr Assoc* 2015;103:152 (PMC4511057). © the author. Whole text except biography and references | 1,526 | The six original levels with examples; revised levels "remember, understand, apply, analyze, evaluate, and create"; four knowledge types; action verbs indicate the assessment method; objectives concentrate at the lower levels |
| `hake_1998_normalized_gain.txt` | Hake, *Am J Phys* 1998;66:64. **Abstract only** (Crossref, publisher-deposited) | 483 | 〈g〉 "defined as the ratio of the actual average gain (%〈post〉−%〈pre〉) to the maximum possible average gain (100−%〈pre〉)"; T courses 0.23±0.04 (N=2084), IE courses 0.48±0.14 (N=4458) |
| `biggs_1996_constructive_alignment.txt` | Biggs, *High Educ* 1996;32:347. **Abstract only** (Springer page); paper paywalled | 415 | "Constructive alignment" as "a marriage of the two thrusts"; objectives as performances, activities to elicit them, assessment aligned |
| `frich_2015_physician_leadership.txt` | Frich et al., *J Gen Intern Med* 2015;30:656 (PMC4395611), CC BY 4.0. **Excerpts; Table 3 omitted** | 3,515 | 45 studies; Kirkpatrick levels "reaction (Level 1), knowledge (Level 2), behavioral change (Level 3), and system results (Level 4)" and Table 1's 1-4B typology; Level 1 in 25, 2A in 36, 2B in 7, 3A in 10, 3B in 2, system level in 6; comparison group in few studies; leadership vs management sentence citing Yukl |
| `stoller_2020_leadership.txt` | Stoller, *Chest* 2021;159:1147 (PMC7501065). © ACCP/Elsevier, PMC COVID-19 permission. **Excerpts.** Open substitute for Kotter 1990 (HBR, paywalled) | 1,171 | Table 1 "Attributes of Managing vs Leading", "After Kotter": planning and budgeting / organizing and staffing / controlling and solving vs vision and setting direction / aligning people / motivating and inspiring; "leadership competencies can be developed"; "small l" and "big L" leadership |
```

Suggested note under the table: "Added 2026-09-24/25 by the S57-R1 intake (group b). Kotter 1990 and the full texts of Hake 1998 and Biggs 1996 were not obtained; see `books/S57-R1/intake/log-b.md`."
