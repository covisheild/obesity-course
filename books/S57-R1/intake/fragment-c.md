# Intake fragment, group c (Indian medical-education instruments) · S57-R1

For the main thread to merge into `sources/INDEX.yml`, `check/references/library.bib` and `sources/SOURCES.md`
in one commit. Eight new citekeys; none collides with INDEX.yml or library.bib (grepped 2026-09-24). The eight
`sources/*.txt` files are written; `books/S57-R1/intake/build-c/build.py` regenerates them from the raw fetches
and `verify.py` rechecks them (37/37).

## INDEX.yml (`files:` entries)

```yaml
  mci_cbme_ug_curriculum_2018_vol1:
    file: mci_cbme_ug_curriculum_2018_vol1.txt
    what: >-
      MCI, Competency based Undergraduate Curriculum for the Indian Medical Graduate, Vol. 1 (2018), PDF text
      layer. Excerpts: title, copyright grant (p. 7), Vol. I contents, pp. 11-39 whole (preamble; IMG goals and
      the five roles with their competencies; domain K/S/A/C and level K/KH/S/SH/P coding; objectives, methods
      and assessment derived from a competency; integration; definitions), first table's headings. No subject
      tables. SUPERSEDED as the curriculum in force by nmc_cbme_2024; copyright MCI, reproduction by permission
  nmc_cbme_2024:
    file: nmc_cbme_2024.txt
    what: >-
      NMC, CBME Curriculum/Guidelines 2024 (letter of 12 Sep 2024) and the UGMEB clarification of 10 Oct 2024,
      PDF text layer. Excerpts: guideline sections 1-6 whole (goals, the seven IMG roles and competencies),
      pp. 27-45 whole (Foundation Course, phases, hours, teaching-learning elements, AETCOM, the whole Assessment
      section), Annexure 4, the curriculum's How to use / domains / levels (K/KH/SH/P), first table head, the
      clarification with corrigendum. No subject tables
  nmc_gmer_2023:
    file: nmc_gmer_2023.txt
    what: >-
      NMC, Graduate Medical Education Regulations, 2023 (Gazette 2 June 2023, No. 367) and corrigendum of
      16 June 2023, English text whole. Header records the currency check: notified, not withdrawn; the
      12 June 2023 guidelines circular was what was withdrawn
  mci_gmer_2019_amendment:
    file: mci_gmer_2019_amendment.txt
    what: >-
      MCI Board of Governors, Regulations on Graduate Medical Education (Amendment), 2019 (Gazette 6 Nov 2019),
      i.e. GMER 1997 Part II. Excerpts: notification, arrangement, Chapter I whole (IMG, five roles,
      competencies, training format, faculty development), Chapter IV opening, Table 3, clause 9.1 (Foundation
      Course), clause 11.1 (attendance, internal assessment). Historical for the curriculum
  mci_foundation_course_2019:
    file: mci_foundation_course_2019.txt
    what: >-
      MCI, Foundation Course for the Undergraduate Medical Education Program (2019), CISP Module 1, PDF text
      layer. Excerpts: title, rights statement, sections 1-9 whole (components, structure, outcomes FC 1.1-5.5
      with domain and level, assessment, faculty capacity, governance), lesson plans 4D and 4J. All rights
      reserved (MCI); one-month course, now two weeks under nmc_cbme_2024
  nmc_miqf_2025:
    file: nmc_miqf_2025.txt
    what: >-
      NMC, Medical Institutions (Qualifications of Faculty) Regulations, 2025 (Gazette 30 June 2025), superseding
      TEQ 2022, with the PGMEB FAQ notice of 28 Oct 2025. Excerpts: notification and regs 1-2(1)(k), regs 13-14
      (exemption from the Basic Course in Medical Education), Schedule Tables E and F whole, part of the
      dentistry table, FAQ notice and Q5. The instrument now requiring the Basic Course in Medical Education
  nmc_teq_2022:
    file: nmc_teq_2022.txt
    what: >-
      NMC, Teachers Eligibility Qualifications in Medical Institutions Regulations, 2022 (14 Feb 2022).
      SUPERSEDED on 30 June 2025 by nmc_miqf_2025. Excerpts: regs 1-2, Table 1A whole ("basic course in Medical
      Education Technology"), repeal clause. History only
  mahajan_gupta_2024_gmer_cbme:
    file: mahajan_gupta_2024_gmer_cbme.txt
    what: >-
      Mahajan and Gupta, Int J Appl Basic Med Res 2024;14(2):71-77 (CC BY-NC-SA 4.0), PMC XML. Excerpts:
      licence; introduction, Table 1, regulatory reforms, the IMG roles five to seven; supplementary exams and
      course duration (states GMER 2023 was never withdrawn). Secondary; evidence for the currency finding
```

## library.bib entries

```bibtex
@misc{mci_cbme_ug_curriculum_2018_vol1,
  title        = {Competency Based Undergraduate Curriculum for the Indian Medical Graduate, Volume {I}},
  author       = {{Medical Council of India}},
  year         = {2018},
  note         = {Issued by the Board of Governors in supersession of the Medical Council of India;
                  implemented for MBBS batches from August 2019. Section 1 gives the five roles of the
                  Indian Medical Graduate; the Manual defines domains (K/S/A/C) and levels (K, KH, S, SH,
                  P). Copyright MCI (Registration L-63913/2016); reproduction requires prior written
                  permission. Superseded by the NMC CBME Curriculum 2024},
  howpublished = {National Medical Commission},
  url          = {https://nmc.org.in/storage/new/UG-Curriculum-Vol-I.pdf},
  urldate      = {2026-09-24}
}

@misc{nmc_cbme_2024,
  title        = {Guidelines for Competency Based Medical Education ({CBME}) Curriculum 2024},
  author       = {{National Medical Commission, Undergraduate Medical Education Board}},
  year         = {2024},
  note         = {Letter No. D-11011/500/2024-AcademicCell, 12 September 2024, enclosing the Competency
                  Based Undergraduate Curriculum for the Indian Medical Graduate 2024; additional
                  clarification and corrigendum of 10 October 2024. Seven roles of the Indian Medical
                  Graduate; Foundation Course; assessment. No licence stated},
  howpublished = {National Medical Commission},
  url          = {https://nmc.org.in/storage/cms/rules-regulation-nmc/YTW423v3EsCFdtPv3I5qZkaNNhuXfub42UZITDRM.pdf},
  urldate      = {2026-09-24}
}

@misc{nmc_gmer_2023,
  title        = {Graduate Medical Education Regulations, 2023},
  author       = {{National Medical Commission}},
  year         = {2023},
  note         = {Notification No. U-14021-8-2023-UGMEB, 2 June 2023, Gazette of India, Extraordinary,
                  Part III Section 4, No. 367; corrigendum of 16 June 2023 (No. 421). In force; the
                  separate guidelines circular of 12 June 2023 was withdrawn. No licence stated},
  howpublished = {Gazette of India},
  url          = {https://nmc.org.in/storage/cms/rules-regulation-nmc/G83KmfBTvRKFfp99s6Vvjuuw3gJ7WM2ZP28Z3Zhk.pdf},
  urldate      = {2026-09-24}
}

@misc{mci_gmer_2019_amendment,
  title        = {Regulations on Graduate Medical Education (Amendment), 2019},
  author       = {{Board of Governors in super-session of Medical Council of India}},
  year         = {2019},
  note         = {Notification No. MCI-34(41)/2019-Med./161726, 4 November 2019, Gazette of India,
                  Extraordinary, Part III Section 4, No. 390. Adds Part II to the Regulations on Graduate
                  Medical Education, 1997, for MBBS batches from 2019-20: the Indian Medical Graduate, five
                  roles, Foundation Course, assessment. No licence stated},
  howpublished = {Gazette of India},
  url          = {https://nmc.org.in/19GraduateMedicalEducationRegulations1997Amendment04112019-2.pdf},
  urldate      = {2026-09-24}
}

@misc{mci_foundation_course_2019,
  title        = {Foundation Course for the Undergraduate Medical Education Program},
  author       = {{Medical Council of India}},
  year         = {2019},
  note         = {Curriculum Implementation Support Program, Module 1; pp. 1-46; file dated 17 July 2019.
                  All rights reserved, Medical Council of India; brief quotation permitted},
  howpublished = {National Medical Commission},
  url          = {https://nmc.org.in/storage/new/FOUNDATION-COURSE-MBBS-17.07.2019.pdf},
  urldate      = {2026-09-24}
}

@misc{nmc_miqf_2025,
  title        = {Medical Institutions (Qualifications of Faculty) Regulations, 2025},
  author       = {{National Medical Commission}},
  year         = {2025},
  note         = {Notification F. No. N-P051(12)/18/2024-PGMEB-NMC, 30 June 2025, Gazette of India,
                  Extraordinary, Part III Section 4; supersedes the Teachers Eligibility Qualifications in
                  Medical Institutions Regulations, 2022. Regulation 14 and Schedule Table E: the Basic
                  Course in Medical Education and the Basic Course in Biomedical Research. No licence stated},
  howpublished = {Gazette of India},
  url          = {https://nmc.org.in/storage/cms/rules-regulation-nmc/QZSDeGu7WXS9MMI0dL5ZR1EbS48kLaFbvMTpww2B.pdf},
  urldate      = {2026-09-24}
}

@misc{nmc_teq_2022,
  title        = {Teachers Eligibility Qualifications in Medical Institutions Regulations, 2022},
  author       = {{National Medical Commission}},
  year         = {2022},
  note         = {Notification F. No. NMC/MCI-23(I)/2021-MED., 14 February 2022; Gazette of India, Part III
                  Section 4, 22 February 2022. Superseded on 30 June 2025 by the Medical Institutions
                  (Qualifications of Faculty) Regulations, 2025. No licence stated},
  howpublished = {Gazette of India},
  url          = {https://nmc.org.in/storage/cms/rules-regulation-nmc/YTXtXo4jg8rF1oti1OoeyStBhePAQ5NoS3qVE16H.pdf},
  urldate      = {2026-09-24}
}

@article{mahajan_gupta_2024_gmer_cbme,
  title        = {Periodically modified regulatory reforms for implementation of competency-driven
                  undergraduate medical curriculum in {India}: a comparative analysis},
  author       = {Mahajan, Rajiv and Gupta, Kapil},
  journal      = {International Journal of Applied and Basic Medical Research},
  year         = {2024},
  volume       = {14},
  number       = {2},
  pages        = {71--77},
  doi          = {10.4103/ijabmr.ijabmr_205_24},
  note         = {Editorial. PMID 38912356, PMC11189270. CC BY-NC-SA 4.0},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC11189270/},
  urldate      = {2026-09-24}
}
```

## SOURCES.md rows

```markdown
| `mci_cbme_ug_curriculum_2018_vol1.txt` | MCI, *Competency based Undergraduate Curriculum for the Indian Medical Graduate*, Vol. 1 (2018), PDF text layer via TinyFish. Copyright MCI, reproduction by permission. **Excerpts; superseded by the 2024 curriculum** | 6,693 | Section 1 extract of the GMER: IMG definition, national and institutional goals, roles 2.3.1-2.3.5 (clinician; leader and member of the health care team and system; communicator; lifelong learner; professional) and competencies 3.1-3.5; Section 2: domains Knowledge/Skill/Attitude/Communication, levels K, KH, SH, P, "‘perform’ indicates independent performance without su pervision and is required ra rely in the pre-internship period" (spacing as in the text layer), core Y/N; the competency-table legend (level "based on the Miller’s pyramid"); PA42.3 worked into four objectives, methods and assessment items; integration by alignment, sharing/correlation "not to exceed 20%"; "Assessment will continue to be subject based"; definitions of goal, competency, objective; levels table K/KH/S/SH/P |
| `nmc_cbme_2024.txt` | NMC, CBME Curriculum/Guidelines 2024 (12 Sep 2024) with the UGMEB clarification of 10 Oct 2024, PDF text layer via TinyFish. No licence stated. **Excerpts** | 12,744 | Preamble places it after GMER 2023; seven IMG roles a-g (adds Critical Thinker, Researcher) with competencies; Foundation Course required, phase I "including F oundation Course of two weeks", goal "to prepare a learner to study medicine effectively", objectives, 75% attendance; Annexure 4 Foundation Course 80 hours; large group teaching "shall not exceed one third"; AETCOM longitudinal; integration about 20%; internal assessment not added to summative, 50% combined/40% separate for eligibility; university exam pass 50% cumulative and 40% separately; MCQs given a minimum 20% weightage of each theory paper; levels table K, KH, SH, P (no S); clarification's corrigendum items 1-8 |
| `nmc_gmer_2023.txt` | NMC, *Graduate Medical Education Regulations, 2023*, Gazette 2 June 2023 (No. 367) and corrigendum 16 June 2023, English text whole, PDF text layer via TinyFish. No licence stated | 3,633 | Preamble goals 1-11 (incl. "leading partner in healthcare teams", AETCOM); ch. II duties incl. "competency-based medical education" and self-directed learning; ch. V clause 20 UGMEB publishes the model curriculum, clause 21 four attempts / nine years; ch. VI clause 24 faculty development (group dynamics, small group teaching, team leaders); header: in force, only the 12 June 2023 guidelines circular withdrawn, with quoted evidence |
| `mci_gmer_2019_amendment.txt` | MCI Board of Governors, *Regulations on Graduate Medical Education (Amendment), 2019* (GMER 1997 Part II), Gazette 6 Nov 2019, PDF text layer via TinyFish. No licence stated. **Excerpts; historical** | 9,186 | 2 IMG defined; 2.3 five roles; 3.1-3.5 competencies; 4.1.1 Foundation Course; 4.1.3 small group and case-based learning; 4.1.8 formative and summative assessment; 4.2 faculty development programmes; Table 3 Foundation Course 175 hours (one month); 9.1 Foundation Course goal and objectives; 11.1 attendance 75%/80%, internal assessment 50% combined, 40% separately |
| `mci_foundation_course_2019.txt` | MCI, *Foundation Course for the Undergraduate Medical Education Program* (2019), CISP Module 1, PDF text layer via TinyFish. All rights reserved (MCI). **Excerpts** | 3,811 | Purpose and components; Table 1, 175 hours; outcomes FC 1.1-5.5 with domain and level (FC 1.2 "Roles of an Indian Medical Graduate", FC 4.12-4.15 learning, SDL, collaborative learning); section 7 Foundation Course does NOT count towards internal assessment; section 8 faculty capacity; 4D team aspects (shared goals, communication, leadership, role clarity, trust); 4J objective "To identify and maximize one’s learning style" |
| `nmc_miqf_2025.txt` | NMC, *Medical Institutions (Qualifications of Faculty) Regulations, 2025*, Gazette 30 June 2025, with the PGMEB FAQ notice of 28 Oct 2025, PDF text layer via TinyFish. No licence stated. **Excerpts** | 3,200 | Supersedes TEQ 2022; reg 14 exemptions from the Basic Course in Medical Education; Table E: Professor and Associate Professor "shall be required to undergo Basic Course in Medical Education provided their broad specialty subject is covered under undergraduate training" and have completed the Basic Course in Biomedical Research; Assistant Professor row lists neither; Table F (super specialties) BCBR only; FAQ Q5 both courses within two years for Note 2 appointees |
| `nmc_teq_2022.txt` | NMC, *Teachers Eligibility Qualifications in Medical Institutions Regulations, 2022*, PDF text layer via TinyFish. **Superseded 30 June 2025; history only** | 971 | Table 1A: Professor and Associate Professor "Should have completed the basic course in Medical Education Technology from Institutions designated by NMC" and the basic course in Biomedical Research; clause 16 repeals the 1998 regulations |
| `mahajan_gupta_2024_gmer_cbme.txt` | Mahajan and Gupta, *Int J Appl Basic Med Res* 2024;14(2):71-77 (PMC11189270), PMC XML. CC BY-NC-SA 4.0. **Excerpts; secondary** | 2,711 | Table 1 of NMC curriculum modules; GMER 1997 / GMER 2019 / CBME Guidelines 2023 lineage; "Guidelines under GMER 2023" withdrawn 23 June 2023; IMG roles five (2019) to seven (2023); GMER 2023 "gazette notified and never withdrawn, remain in force" |
```

Paragraph for SOURCES.md, below the table (group c, 2026-09-24):

```markdown
**S57-R1 intake, group c (Indian medical-education instruments), 2026-09-24.** Eight files, all cut by script
from TinyFish fetches of the PDFs' text layers on nmc.org.in (and one PMC XML); verbatim check 37 of 37. Currency
found: the Graduate Medical Education Regulations, 2023 (Gazette 2 June 2023) are in force; only the 12 June
2023 "Guidelines under GMER 2023" circular was withdrawn. The curriculum in force is NMC's CBME Curriculum 2024
(12 Sep 2024), not the 2018 volumes, which are held for history. The faculty-course requirement now sits in the
Medical Institutions (Qualifications of Faculty) Regulations, 2025, which superseded TEQ 2022 on 30 June 2025.
Two of the eight (the 2018 curriculum and the Foundation Course module) carry MCI copyright lines restricting
reproduction; the others state no licence and fall under NMC's site disclaimer (non-commercial copying). Log:
`books/S57-R1/intake/log-c.md`.
```
