# Source intake log · S57-R1

One pass by three parallel intake agents, 2026-09-24/25, before drafting, against the 23 "To obtain" lines in
`READY.md`: group a (learning-science papers), group b (statistics, teaching guides, assessment, leadership) and
group c (Indian medical-education instruments). Tool for every stored passage: `mcp__TinyFish__fetch_content`. Its
result was saved by the harness to a file, decoded from JSON unchanged into `intake/raw/`, and every passage was cut
from that text by script (`raw[i:j]` between literal anchors; `intake/build-b.py`, `intake/build-c/build.py` and
group a's `build_a.py`). The written files were then re-parsed and each passage tested as a whitespace-normalised
substring of the raw fetch for the URL in its block heading. An omission is marked `[...]` in place, with a
`[NOTE]` saying what was left out. No WebFetch output is stored anywhere; nothing was fetched with curl, wget or a
Python HTTP client. Identifiers were confirmed with the PubMed tools (and Crossref or Europe PMC where noted). The
per-group logs, with fuller findings, are `intake/log-a.md`, `intake/log-b.md` and `intake/log-c.md`; the registry
entries merged into `sources/INDEX.yml`, `check/references/library.bib` and `sources/SOURCES.md` are in
`intake/fragment-a.md`, `-b.md` and `-c.md`.

**Verbatim check: 92 of 92** (group a 36, group b 19, group c 37; group c also 9 of 9 header quotes).

## Group a · learning-science papers

| Source | URL fetched (stored passages) | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Freeman et al. 2014 *PNAS* 111:8410 (PMID 24821756, PMC4060654) | https://www.pnas.org/doi/10.1073/pnas.1319030111 | 4 | 4/4 | "Freely available online through the PNAS open access option." (article page; no CC licence) | `freeman_2014_active_learning` |
| Deslauriers et al. 2019 *PNAS* 116:19251 (PMID 31484770, PMC6765278) | https://pmc-oa-opendata.s3.amazonaws.com/PMC6765278.1/PMC6765278.1.xml | 3 | 3/3 | "This open access article is distributed under Creative Commons Attribution-NonCommercial-NoDerivatives License 4.0 (CC BY-NC-ND)." | `deslauriers_2019_feeling_of_learning` |
| Agarwal, Nunes, Blunt 2021 *Educ Psychol Rev* 33:1409 (DOI 10.1007/s10648-021-09595-9) | https://pdf.poojaagarwal.com/Agarwal_etal_2021_EDPR.pdf (published PDF, first author's site) | 1 | 1/1 | "The Author(s), under exclusive licence to Springer Science+Business Media, LLC part of Springer Nature 2021" (PDF). **Not open access**: Springer page is a subscription preview | `agarwal_2021_retrieval_practice` |
| Weinstein, Madan, Sumeracki 2018 *Cogn Res* 3:2 (PMID 29399621, **PMC5780548**) | https://pmc-oa-opendata.s3.amazonaws.com/PMC5780548.1/PMC5780548.1.xml | 3 | 3/3 | "distributed under the terms of the Creative Commons Attribution 4.0 International License" | `weinstein_2018_science_of_learning` |
| Dunlosky et al. 2013 *PSPI* 14:4 (PMID 26173288) | https://www.whz.de/fileadmin/lehre/hochschuldidaktik/docs/dunloskiimprovingstudentlearning.pdf (published PDF, third-party host) | 5 | 5/5 | "© The Author(s) 2013 / Reprints and permission: sagepub.com/journalsPermissions.nav" (PDF); APS page offers it free to read | `dunlosky_2013_learning_techniques` |
| Pashler et al. 2008 *PSPI* 9:105 (PMID 26162104) | https://digitalcommons.usf.edu/psy_facpub/1765/ | 2 | 2/2 | none stated (repository record); publisher copyright | `pashler_2008_learning_styles` (**abstract only**) |
| Newton & Miah 2017 *Front Psychol* 8:444 (PMID 28396647, PMC5366351) | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00444/full | 2 | 2/2 | "distributed under the terms of the Creative Commons Attribution License (CC BY)" | `newton_miah_2017_learning_styles` |
| Rozenblit & Keil 2002 *Cogn Sci* 26:521 (PMID 21442007, PMC3062901, NIHMS268518) | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=3062901 | 3 | 3/3 | "© 2002 Published by Cognitive Science Society, Inc."; PMC flags "open-access no", "manuscript yes" | `rozenblit_keil_2002_ioed` (**abstract only**) |
| (substitute) Fisher & Keil, *Cognitive Science* online first 2015, doi 10.1111/cogs.12280 | https://cogdevlab.yale.edu/sites/default/files/files/Fisher2015.pdf (Keil lab copy) | 3 | 3/3 | "Copyright © 2015 Cognitive Science Society, Inc. All rights reserved." | `fisher_keil_2015_ioed` |
| Sweller, van Merriënboer, Paas 2019 *Educ Psychol Rev* 31:261 (DOI 10.1007/s10648-019-09465-5) | https://link.springer.com/article/10.1007/s10648-019-09465-5 | 6 | 6/6 | "Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License" | `sweller_2019_cognitive_load` |
| Roediger & Karpicke 2006 *Psychol Sci* 17:249 (PMID 16507066) | https://gwern.net/doc/psychology/spaced-repetition/2006-roediger.pdf (published PDF, third-party host) | 2 | 2/2 | "Copyright r 2006 Association for Psychological Science" (PDF footer; "r" is the © sign) | `roediger_karpicke_2006_testing_effect` |
| Cepeda et al. 2008 *Psychol Sci* 19:1095 (PMID 19076480, ERIC ED505660) | https://files.eric.ed.gov/fulltext/ED505660.pdf (authors' **in-press manuscript**) | 2 | 2/2 | none stated; ERIC record: "Its contents may differ from the final published version." | `cepeda_2008_spacing_ridgeline` |

## Group b · statistics, teaching guides, assessment, leadership

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| OpenStax *Introductory Statistics 2e* §1.4 Experimental Design and Ethics (appended to the held file) | https://openstax.org/books/introductory-statistics-2e/pages/1-4-experimental-design-and-ethics; details page re-read | 1 (whole page) | 1/1 | "by OpenStax is licensed under Creative Commons Attribution-NonCommercial-ShareAlike License v4.0" (details page, 2026-09-24; web version still "Jul 07, 2026") | `openstax_intro_stats_2e` (INDEX `what:` update, not a new entry) |
| Cochrane Handbook v6.5, ch. 6, Key Points and §6.5.1-6.5.1.2 | https://training.cochrane.org/handbook/current/chapter-06 (redirects to cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-06) | 2 | 2/2 | none in the extracted text; site footer "Copyright © 2026 The Cochrane Collaboration" (search snippet only) | `cochrane_handbook_ch06_v6_5` |
| Chatterjee & Corral 2017 *J Educ Perioper Med* 19(4):E610 | https://www.seahq.org/assets/docs/xix_4_chatterjee.pdf (publisher PDF text layer); PMC front matter via https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=5944406 | 3 | 3/3 | "© 2017 Society for Education in Anesthesia" (PMC front matter) | `chatterjee_corral_2017_objectives` |
| Adams 2015 *J Med Libr Assoc* 103(3):152-153 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4511057/ | 1 (whole article) | 1/1 | "Copyright: © 2015, Authors." (PMC page) | `adams_2015_bloom` |
| Hake 1998 *Am J Phys* 66(1):64-74, **abstract only** | https://api.crossref.org/works/10.1119/1.18809 (abstract string JSON-decoded) | 1 | 1/1 | publisher copyright (AAPT); none stated in the record | `hake_1998_normalized_gain` |
| Biggs 1996 *High Educ* 32(3):347-364, **abstract only** | https://link.springer.com/article/10.1007/BF00138871 | 1 | 1/1 | publisher copyright; page says "This is a preview of subscription content" | `biggs_1996_constructive_alignment` |
| Frich et al. 2015 *J Gen Intern Med* 30(5):656-674 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4395611.1/PMC4395611.1.xml | 6 | 6/6 | "© The Author(s) 2014 https://creativecommons.org/licenses/by/4.0/ Open Access This article is distributed under the terms of the Creative Commons Attribution License ..." | `frich_2015_physician_leadership` |
| Stoller 2020 *Chest* 159(3):1147-1154 (substitute for Kotter 1990) | https://pmc-oa-opendata.s3.amazonaws.com/PMC7501065.1/PMC7501065.1.xml | 4 | 4/4 | "© 2020 American College of Chest Physicians. Published by Elsevier Inc. All rights reserved." plus Elsevier's COVID-19 resource-centre permission (quoted in file) | `stoller_2020_leadership` |

## Group c · Indian medical-education instruments

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| MCI, *Competency based UG Curriculum for the IMG*, Vol. 1 (2018): title, copyright, contents, pp. 11-39 whole (roles, K/S/A/C domains, K/KH/S/SH/P levels, worked assessment examples, integration, definitions), first table head | https://nmc.org.in/storage/new/UG-Curriculum-Vol-I.pdf | 5 | 5/5 | "have received Copyright from the Register of Copyrights … Registration Number L-63913/2016. Reproducing any part of this document in any form must be with the prior written permission of the competent authorities of the Medical Council of India." (p. 7) | `mci_cbme_ug_curriculum_2018_vol1` |
| NMC, CBME Curriculum/Guidelines 2024 (12 Sep 2024) + UGMEB clarification (10 Oct 2024): sections 1-6, pp. 27-45 (Foundation Course, whole Assessment section), Annexure 4, How to use/levels, clarification | …/rules-regulation-nmc/YTW423v3EsCFdtPv3I5qZkaNNhuXfub42UZITDRM.pdf; …/fzR5SHdI5dNhLCPbGWQNS6WhYGVohp8FRY7AWh7t.pdf | 7 | 7/7 | None stated. NMC site disclaimer: copying authorised "for non-commercial purposes only"; other reproduction needs NMC's written permission | `nmc_cbme_2024` |
| NMC, *Graduate Medical Education Regulations, 2023* (Gazette 2 Jun 2023) + corrigendum (16 Jun 2023), English whole | …/rules-regulation-nmc/G83KmfBTvRKFfp99s6Vvjuuw3gJ7WM2ZP28Z3Zhk.pdf; …/QwhpGdAJfo2yFLcbox9qHeAAJ4ZVhjAxq2CU2YlG.pdf | 3 | 3/3 | None stated (Gazette); NMC site disclaimer as above | `nmc_gmer_2023` |
| MCI BoG, *Regulations on GME (Amendment), 2019* = GMER 1997 Part II: Chapter I whole, Ch. IV opening, Table 3, 9.1 Foundation Course, 11.1 assessment eligibility | https://nmc.org.in/19GraduateMedicalEducationRegulations1997Amendment04112019-2.pdf | 5 | 5/5 | None stated (Gazette); NMC site disclaimer as above | `mci_gmer_2019_amendment` |
| MCI, *Foundation Course for the UG Medical Education Program* (2019), CISP Module 1: sections 1-9 whole, lesson plans 4D and 4J | https://nmc.org.in/storage/new/FOUNDATION-COURSE-MBBS-17.07.2019.pdf | 5 | 5/5 | "All rights reserved. No pa rt of this publication/document may be reproduced … without the prior written permission from Medical Council of India, except for use in Curriculum Impl ementation Support Program … as well as in the case of brief quotations embodied in critical reviews and certain other non -commercial uses permitted by copyright law 2019." | `mci_foundation_course_2019` |
| NMC, *Medical Institutions (Qualifications of Faculty) Regulations, 2025* (Gazette 30 Jun 2025) + FAQ notice (28 Oct 2025): regs 1-2, 13-14, Tables E and F, FAQ Q5 | …/rules-regulation-nmc/QZSDeGu7WXS9MMI0dL5ZR1EbS48kLaFbvMTpww2B.pdf; …/iFB9GIjrd5y98IADDnFGyTzqgguiEYO5HI37Jh6L.pdf | 6 | 6/6 | None stated (Gazette); NMC site disclaimer as above | `nmc_miqf_2025` |
| NMC, *Teachers Eligibility Qualifications in Medical Institutions Regulations, 2022* (superseded): regs 1-2, Table 1A, repeal | …/rules-regulation-nmc/YTXtXo4jg8rF1oti1OoeyStBhePAQ5NoS3qVE16H.pdf | 3 | 3/3 | None stated (Gazette); NMC site disclaimer as above | `nmc_teq_2022` |
| Mahajan & Gupta, *Int J Appl Basic Med Res* 2024;14(2):71-77 (secondary; added as evidence for the currency finding) | https://pmc-oa-opendata.s3.amazonaws.com/PMC11189270.1/PMC11189270.1.xml | 3 | 3/3 | "distributed under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 License" | `mahajan_gupta_2024_gmer_cbme` |

All nmc.org.in PDF URLs in group c start `https://nmc.org.in/storage/cms/rules-regulation-nmc/` where shortened.

## Not obtained / needs Harsh

### Group a

| Item | Why not | What to download |
| --- | --- | --- |
| Pashler et al. 2008, body | SAGE bot-blocked; APS PDF links unreachable; an appstate.edu copy returned no text; academia.edu is behind sign-up | Open https://doi.org/10.1111/j.1539-6053.2009.01038.x in a browser, download the PDF (free via APS), and put it in `sources/` for transcription |
| Rozenblit & Keil 2002, body | Author manuscript not in the PMC OA subset; PMC page empty to the fetcher; Europe PMC REST 500 three times; Wiley bot-blocked | Open https://pmc.ncbi.nlm.nih.gov/articles/PMC3062901/ and save the page or its PDF |
| Cepeda et al. 2008, published version (optional) | Held text is the ERIC in-press manuscript; SAGE and lab PDFs unreachable | Only if the published figures must be checked: the PDF from https://doi.org/10.1111/j.1467-9280.2008.02209.x |
| Dunlosky 2013 and Roediger & Karpicke 2006 from the publisher (optional) | Held text is the published PDF, but from third-party hosts (whz.de, gwern.net) | Only if a publisher-served copy is required: the PDFs from their DOIs |

### Group b

| Work | Why not | What to download |
| --- | --- | --- |
| Kotter JP. What leaders really do. *Harv Bus Rev* 1990;68(3):103-111 (republished Dec 2001) | hbr.org returned only the metered teaser (standfirst and first paragraph); body behind HBR paywall | https://hbr.org/2001/12/what-leaders-really-do, saved as PDF or print-to-PDF from a logged-in/subscriber session (HBR reprint R0111F). Until then `stoller_2020_leadership` stands in (Table 1, "After Kotter"). An alternative open restatement exists in Amelung et al. (eds), *Handbook Integrated Care* (Springer open access, 2021), a box sourced "Kotter (2001)"; not filed |
| Biggs J. Enhancing teaching through constructive alignment. *High Educ* 1996;32:347-364, full text | Springer subscription content | https://link.springer.com/content/pdf/10.1007/BF00138871.pdf from an institutional login. A copy is posted at https://teaching.helsinki.fi/system/files/inline-files/Biggs1996_Article_EnhancingTeachingThroughConstr.pdf (University of Helsinki); not used, redistribution licence unstated. For C10 the abstract (held) plus Chatterjee's "constructive alignment" paragraph may suffice |
| Hake RR 1998, full text | pubs.aip.org returned bot_blocked; Hake's own copy at http://www.physics.indiana.edu/~sdi/ajpv3i.pdf unreachable (host down, Wayback unreachable from the session) | Only needed if the course quotes beyond the abstract: https://doi.org/10.1119/1.18809 (AIP PDF) from an institutional login, or Hake's copy if that host returns. Third-party uploads (stemteachersnyc.org, jgravesedu.com) were not used |

### Group c

- **CBME Guideline of 01.08.2023** (NMC Rules page, UGMEB item 2.2): TinyFish returned no text for
  https://nmc.org.in/storage/cms/rules-regulation-nmc/cFsc3VXVrfiWx8to0tPF8J5bKFLI9XIXfDaM0Vwl.pdf. The
  2024 document supersedes it, so it is **not needed** unless a claim is about 2023 specifically.
- **NMC's withdrawal circular of about 23 June 2023** (the "Guidelines under GMER 2023" circular, NMC News ID 502
  per Mahajan & Gupta). Not searched for on nmc.org.in. The finding rests on The Hindu's quotation of it,
  Mahajan & Gupta, and NMC's own listing. If the book states the withdrawal in NMC's words, Harsh (or a later
  session) should get the circular from nmc.org.in → Circulars/Public Notices, June 2023.

Decision for Harsh (log-c caveats): the 2018 curriculum and the Foundation Course module carry MCI copyright lines
allowing reproduction only with permission (the module also allows "brief quotations embodied in critical reviews");
the Gazette instruments and the 2024 guidelines state no licence, and NMC's site disclaimer authorises copying "for
non-commercial purposes only". The files hold long verbatim runs for internal quote-checking; reader-facing text should
paraphrase and quote briefly. Harsh to confirm that this is acceptable for the repo.

## Corrections to READY.md found at intake (applied there)

- Weinstein et al. 2018 is **PMC5780548**, not PMC5780106.
- Agarwal et al. 2021 is **not** open access and not CC BY ("under exclusive licence to Springer"); obtained as the
  published PDF posted on the first author's site.
- Deslauriers et al. 2019 is CC BY-NC-ND 4.0.
- Roediger and Karpicke 2006 and Cepeda et al. 2008 were obtained from a session (third-party published PDF;
  in-press manuscript in ERIC), not from Harsh.
- Chatterjee and Corral 2017 is PMC5944406 (PDF-only in PMC); transcribed from the publisher's PDF.
- Currency (C14): GMER 2023 is in force; the curriculum in force is NMC's CBME Curriculum 2024; the Basic Course in
  Medical Education requirement sits in the Medical Institutions (Qualifications of Faculty) Regulations, 2025,
  which superseded TEQ 2022 (`nmc_teq_2022`, filed for history only, marked superseded).

## Harsh's PDFs (2026-09-25)

Harsh supplied three PDFs he downloaded himself. Each was copied unchanged into `intake/raw/` and its text layer
extracted with `pdftotext` (poppler, default reading-order mode). `pdftotext -layout` was also run (kept as
`*.layout.txt`, **not used**): for Pashler and Kotter it set the two columns side by side on each line, and for
Rozenblit and Keil it added only indentation. The default-mode `.txt` is the raw every passage is checked against. The
raw was not corrected: ligatures (ﬁ, ﬂ) stay as extracted, line-end hyphenated words stay joined as pdftotext joined
them, and running heads and footers stay inside passages. Every file header says so. Passages were cut by
`intake/build-harsh.py` (`raw[i:j]` between literal anchors; manifest `intake/manifest-harsh.json`) and re-checked by
`intake/verify-harsh.py` as whitespace-normalised substrings of the raw named in each block heading.
Reference lists are not held.

**Verbatim check: 29 of 29** (24 new blocks, plus the 5 earlier blocks from the USF record and efetch, re-checked).

| Source | PDF (raw) | Held | Blocks | Check | Copyright as printed | Citekey |
| --- | --- | --- | --- | --- | --- | --- |
| Pashler, McDaniel, Rohrer, Bjork, *PSPI* 9(3):105-119 | `raw/pashler_2008_learning_styles-harsh.pdf` → `-harsh.txt` (15 pp.; SAGE download filename) | whole body: the crossover criterion, Fig. 1 caption and in-figure text (acceptable A-C, unacceptable D-I), Fig. 2 caption, review, ATI literature, conclusions, Summary. Figure panels (scattered axis labels), acknowledgments and references omitted | 5 new (4-8) + 2 kept | 7/7 | "Copyright r 2009 Association for Psychological Science" ("r" is ©) | `pashler_2008_learning_styles` (extended) |
| Rozenblit & Keil, *Cogn Sci* 26(5):521-562, NIH author manuscript | `raw/rozenblit_keil_2002_ioed-harsh-nihms268518.pdf` → `.txt` (47 pp.; PMC) | title through General discussion (Studies 1-12, methods, results with ANOVA statistics), captions of Figs. 1-6, Table 8. Tables 1-7 (scrambled cells), appendices, acknowledgments and references omitted | 7 new (4-10) + 3 kept | 10/10 | "© 2002 Published by Cognitive Science Society, Inc." | `rozenblit_keil_2002_ioed` (extended) |
| Kotter, "What Leaders Really Do", *HBR* 1990; Best of HBR reprint Dec 2001 (R0111F) | `raw/kotter_1990_what_leaders_do-harsh.pdf` → `-harsh.txt` (9 pp., printed pp. 3-11) | whole article with the 2001 editor's introduction, author note, three case boxes, three pull quotes. Only the ordering lines after the reprint number omitted | 12 | 12/12 | "COPYRIGHT © 2001 HARVARD BUSINESS SCHOOL PUBLISHING CORPORATION. ALL RIGHTS RESERVED." Held for private study and quotation only | `kotter_1990_what_leaders_do` (new) |

Findings:

- **Pashler's printed citation.** The PDF prints "Volume 9—Number 3", pages 105-119, and a 2009 copyright; it prints
  no issue date. The catalogue year (PubMed, USF) is 2008; the DOI stem is 2009. Citekey and bib year stay 2008, and the
  file header and bib note record the 2009 copyright.
- **Rozenblit & Keil numbers.** The mean self-ratings at T1-T5 are plotted (Figs. 3-6), not printed. The text
  gives the tests: Study 1 (16 Yale graduate students) time F(4, 56) = 16.195, p < .001, η2 = .536, T1 vs T2, T3, T4
  all p < .002; Study 2 (33 undergraduates) F(4, 124) = 38.9, p < .001. Table 8 summarises the domains: facts, a
  smaller drop; procedures and narratives, no drop; natural phenomena, the same as devices; the explicit warning in
  Study 6 still gives a significant drop, but not as big. A claim needing a mean rating value cannot be quoted from
  this file.
- **Kotter.** The text held is the 2001 reprint. The 1990 volume, issue and pages (68(3):103-111) are not printed on
  it; they come from READY.md and were not re-verified here. The reprint's own 2001 volume and pages are not printed
  either.
- **Ligatures.** A record quoting these files must copy the ligature characters as they stand ("signiﬁcant",
  "ﬁrst"), or the build's quote check (whitespace-normalised, lower-cased, no ligature folding) will not find the words.
- Registries updated directly: `sources/INDEX.yml` (`what:` for pashler, rozenblit and stoller; new kotter entry),
  `check/references/library.bib` (pashler and rozenblit notes; new `@article{kotter_1990_what_leaders_do}`, year
  1990, reprint and copyright in the note, no repository path), `sources/SOURCES.md`, `READY.md` (three lines to
  yes, and a gate note). The stoller bib note did not claim Kotter was unavailable and is unchanged.
