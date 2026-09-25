# Source intake log · S57-R1 · group c (Indian medical-education instruments)

One pass, 2026-09-24/25, against the four NMC/MCI lines in `READY.md` ("PDF or paywalled"). Tool for every stored
passage: `mcp__TinyFish__fetch_content` on the direct PDF URLs linked from nmc.org.in's UG Curriculum and Rules &
Regulations pages. **Every PDF returned its text layer**, so nothing had to go to Harsh as a download. The result
was saved unchanged to `books/S57-R1/intake/raw/` (from the harness's saved tool output or, for small results,
from this session's transcript, decoded from JSON unchanged). Every passage was then cut from that text by script
(`intake/build-c/build.py`, `raw[i:j]` between literal start and end markers) and the written files were re-parsed
and checked by `intake/build-c/verify.py`: each `[TEXT]` block must be a whitespace-normalised substring of the raw
fetch for the URL in its heading. The evidence quoted in headers is cut the same way. No WebFetch, curl, wget or
Python HTTP. The Mahajan and Gupta identifiers were confirmed with PubMed (`get_article_metadata`, PMID 38912356).

**Verbatim check: 37 of 37 passages; 9 of 9 header quotes.**

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

All nmc.org.in PDF URLs start `https://nmc.org.in/storage/cms/rules-regulation-nmc/` where shortened. The PDF host
redirected to bare IP addresses (3.111.69.97, 15.252.14.152), which served the files. Also fetched and kept as raw
evidence, not filed: the NMC Rules & Regulations page and UG Curriculum page (2026-09-24), NMC's disclaimer and
terms-of-use pages (2026-09-25), The Hindu of 26 June 2023 on the withdrawal.

## What was found (the currency questions in READY.md)

1. **Which Graduate Medical Education Regulations are in force: GMER 2023.** Notified in the Gazette on 2 June
   2023 (No. 367), corrigendum 16 June 2023. Not withdrawn or held in abeyance on any evidence found: NMC's Rules
   & Regulations page (24 Sep 2026) lists it and its corrigendum with no abeyance entry; Mahajan & Gupta 2024 say
   it was "gazette notified and never withdrawn". What NMC withdrew, on 23 June 2023, was the separate circular of
   12 June 2023 issuing "Guidelines under Graduate Medical Education Regulations 2023" (The Hindu quotes the
   circular; Mahajan & Gupta date it). GMER 2023 is short and names no IMG roles, Foundation Course or level
   coding. Those now live in NMC's **CBME Curriculum/Guidelines 2024** (12 Sep 2024), issued under GMER 2023.
   Evidence quoted in the header of `sources/nmc_gmer_2023.txt`.
2. **The 2018 curriculum is not the current one.** The CBME Curriculum 2024 has **seven** IMG roles (adds
   Critical Thinker and Researcher to the five of 2018/2019). Its levels table lists K, KH, SH and P, with "S -
   Shows" gone. The Foundation Course is now **two weeks / 80 hours** (it was one month / 175 hours in 2019).
   Inventory C14 says "Competency-based curriculum as adopted by MCI/NMC (2019 onward)". That still holds, but
   the roles count and the Foundation Course length must come from the 2024 document.
3. **The faculty-course instrument is the Medical Institutions (Qualifications of Faculty) Regulations, 2025**
   (30 June 2025), which superseded TEQ 2022. Precise rule: in broad specialties, Associate Professors and
   Professors "shall be required to undergo Basic Course in Medical Education provided their broad specialty
   subject is covered under undergraduate training" and must have completed the Basic Course in Biomedical
   Research. The Assistant Professor row lists neither course. Regulation 14 exempts super-specialty faculty and
   faculty in specialties outside the UG curriculum, and gives institutes of national importance a two-year
   catch-up. TEQ 2022 called it the "basic course in Medical Education Technology". "Medical teachers must
   complete a basic course" is therefore too broad as a claim. It applies to promotion to Associate Professor and
   above.

## Not obtained, and what Harsh would need

- **CBME Guideline of 01.08.2023** (NMC Rules page, UGMEB item 2.2): TinyFish returned no text for
  https://nmc.org.in/storage/cms/rules-regulation-nmc/cFsc3VXVrfiWx8to0tPF8J5bKFLI9XIXfDaM0Vwl.pdf. The
  2024 document supersedes it, so it is **not needed** unless a claim is about 2023 specifically.
- **NMC's withdrawal circular of about 23 June 2023** (the "Guidelines under GMER 2023" circular, NMC News ID 502
  per Mahajan & Gupta). Not searched for on nmc.org.in. The finding rests on The Hindu's quotation of it,
  Mahajan & Gupta, and NMC's own listing. If the book states the withdrawal in NMC's words, Harsh (or a later
  session) should get the circular from nmc.org.in → Circulars/Public Notices, June 2023.

## Caveats and decisions for Harsh

- **Copyright.** The 2018 curriculum and the Foundation Course module carry MCI copyright lines that allow
  reproduction only with permission (the module also allows "brief quotations embodied in critical reviews").
  The Gazette instruments and the 2024 guidelines state no licence. NMC's site disclaimer authorises copying
  "for non-commercial purposes only". The files hold long verbatim runs for internal quote-checking. Reader-facing
  text should paraphrase and quote briefly. Harsh to confirm that this is acceptable for the repo.
- The text layers keep PDF artefacts ("Gra duate", "m i nimum"). A drafter's `quote` must copy them as they stand
  or use a clean run. The build's check normalises whitespace but not split words.
- `mahajan_gupta_2024_gmer_cbme` is an addition not named in READY.md. It is filed as secondary evidence for the
  currency finding and should not be cited for what an instrument says.
- `nmc_teq_2022` is superseded and filed for history only. The main thread may prefer to leave it out of the
  merge. The `what:` line and the header say it is superseded.
- Not checked: whether any NMC notice after 12 Sep 2024 amends the CBME 2024 roles or levels. The Rules page on
  24 Sep 2026 lists nothing later for the UG curriculum. The event trigger for C14 is the next NMC curriculum or
  GMER notice.
