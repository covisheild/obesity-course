# Source intake log · S47-R1

One pass on 2026-10-01, before drafting, by four intake subagents (A journal articles, B open textbooks, C Union procedure, D tobacco, GST and framing texts), to `books/S47-R1/INTAKE-BRIEF.md`. Every stored passage was fetched with `mcp__TinyFish__fetch_content`, saved unchanged, and cut by script as a contiguous slice; each group's `verify.py` re-parsed the written files and tested every `[TEXT]` run as a whitespace-normalised substring of the raw fetch. The conductor re-ran all four: **A 29/29, B 15/15, C 30/30, D 30/30.** Registries (`sources/INDEX.yml`, `check/references/library.bib`, `sources/SOURCES.md`) merged by the conductor in one commit; `parallel.py registries` 0 problems; `build.py --check` blocking 0.

Withdrawn by the conductor: `ls_2025_q2110_plcp` (Lok Sabha USQ 2110), fetched before sansad.in's terms could be read (terms page HTTP 500). Not committed.

Gate, not obtained items and conductor decisions: `SOURCE-GATE.md`.

## Group A · journal articles

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Koon, Hawkins & Mayhew 2016 *Health Policy Plan* 31:801: licence; abstract; Key Messages, whole body with Tables 1–3, Appendix | https://pmc-oa-opendata.s3.amazonaws.com/PMC4916318.1/PMC4916318.1.xml | 3 | 3/3 | "© The Author 2016. Published by Oxford University Press … This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/) …" (PMC XML) | `koon_2016_framing` (new) |
| Barry et al. 2009 *Milbank Q* 87:7: copyright line; abstract; Data and Methods to Study Results with Tables 1–5; Discussion; Appendix | https://pmc.ncbi.nlm.nih.gov/articles/PMC2879183/ (whole page, and once scoped to the front matter) | 5 | 5/5 | "© 2009 Milbank Memorial Fund" and a link "PMC Copyright notice" (PMC page). No open licence; not in the PMC OA subset. Quotation for audit only | `barry_2009_metaphors` (new) |
| Summan et al. 2026 *Health Policy Plan* 41:1416: licence; abstract; Key messages, whole body with Tables 1–3, end statements | https://pmc-oa-opendata.s3.amazonaws.com/PMC13586620.1/PMC13586620.1.xml | 3 | 3/3 | "© The Author(s) 2026. Published by Oxford University Press … Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/) …" (PMC XML) | `summan_2026_foodtax` (new) |
| Walt et al. 2008 *Health Policy Plan* 23:308: copyright statement; abstract; Key messages, whole body, Endnote | https://pmc-oa-opendata.s3.amazonaws.com/PMC2515406.1/PMC2515406.1.xml | 3 | 3/3 | "© The Author 2008; all rights reserved. … The online version of this article has been published under an open access model. Users are entitled to use, reproduce, disseminate, or display the open access version of this article for non-commercial purposes provided that …" (PMC XML). Not CC | `walt_2008_policy` (new) |
| Oxman et al. 2009 *Health Res Policy Syst* 7(Suppl 1):S1: licence; abstract; whole body with Tables 1–2 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3271820.1/PMC3271820.1.xml | 3 | 3/3 | "Copyright ©2009 Oxman et al; licensee BioMed Central Ltd. … Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0) …" (PMC XML). CC BY 2.0 | `oxman_2009_support` (new) |
| Cairney & Oliver 2017 *Health Res Policy Syst* 15:35: licence; abstract; whole body with Table 1, declarations | https://pmc-oa-opendata.s3.amazonaws.com/PMC5407004.1/PMC5407004.1.xml | 3 | 3/3 | "© The Author(s). 2017 … Creative Commons Attribution 4.0 International License …" (PMC XML) | `cairney_oliver_2017` (new) |
| Oliver & Cairney 2019 *Palgrave Commun* 5:21: rights; citation and dates; abstract; whole body; Tables 1–2 | https://www.nature.com/articles/s41599-019-0232-y, `.../tables/1`, `.../tables/2` | 6 | 6/6 | "Open Access This article is licensed under a Creative Commons Attribution 4.0 International License …" (article page) | `oliver_cairney_2019` (new) |
| *Optional.* Gilson & Walt 2023 *IJHPM* 12:8223: licence; abstract; whole text | https://pmc-oa-opendata.s3.amazonaws.com/PMC10843444.1/PMC10843444.1.xml | 3 | 3/3 | "© 2023 The Author(s); Published by Kerman University of Medical Sciences … Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0) …" (PMC XML) | `gilson_walt_2023` (new) |

### Findings for the conductor

- **C12: yes.** Koon et al. 2016 state Entman's four functions in their Theory section: "frames
  highlight certain aspects of a problematic situation, while obscuring others in order to define
  problems, diagnose causes, make moral judgments and suggest remedies (Entman 1993)". They say it
  again later: "frames can be classified based on whether they define, diagnose, judge or prescribe
  (Entman 1993)". So C12 can cite the four functions as "Entman's, as reported by Koon et al."
- **C17: no.** Neither paper lists Pielke's four roles. Cairney & Oliver 2017 names two: "the
  'pure scientist' providing evidence with little thought for its application and the 'honest
  broker' prepared to engage with stakeholders to define policy problems [28]" (ref. 28 = Pielke,
  *The honest broker*, 2007). Oliver & Cairney 2019 names two: the tip "Decide if you want to be an
  'issue advocate' or 'honest broker'", with the honest broker as one who disseminates research
  "honestly, clearly, and in a timely fashion … (Pielke, 2007)". Across the two papers, three of
  Pielke's names appear (pure scientist, issue advocate, honest broker). "Science arbiter" appears
  in neither. **The two papers also describe the honest broker differently**: in 2017 the broker
  engages stakeholders, and in 2019 the broker disseminates while others use the evidence. Without
  Pielke himself (Harsh only), C17 should name the two-way contrast (honest broker against issue
  advocate) from Oliver & Cairney 2019, not the four roles.
- **Summan 2026: the citation is correct as READY.md states it.** PubMed (PMID 42480499) gives the
  same authors, title, *Health Policy Plan* 41(8):1416–1428 and doi 10.1093/heapol/czag093. PubMed
  dates it 18 Sep 2026.
- **Oliver & Cairney 2019 confirmed**: *Palgrave Commun* 5, 21 (2019), doi
  10.1057/s41599-019-0232-y, published 19 Feb 2019, CC BY 4.0. The journal is now *Humanities and
  Social Sciences Communications*. A correction (*Palgrave Commun* 6, 48, 2020) fixes one reference
  entry only (Quarmby 2018) and does not touch the text.
- **Gilson & Walt 2023 confirmed**, with its full title "… Comment on 'Modelling the Health Policy
  Process: One Size Fits All or Horses for Courses'". It calls the triangle the "Health Policy
  Analysis Triangle (HPAT)" but **does not list its four elements**. For content, context, process
  and actors, cite Walt et al. 2008 ("Frameworks": "neglecting actors, context and processes … all
  four of these elements") or Summan 2026 Table 2.
- **Licences to note.** Walt 2008 is not CC. It is OUP's non-commercial open access, and the
  copyright line reads "all rights reserved". Oxman 2009 is CC BY 2.0, not 4.0. Barry 2009 is ©
  Milbank Memorial Fund with no open licence: quotation for audit only.
- **Barry 2009, what is held for C13/C14**: sample, country and dates (US, Knowledge Networks web
  panel, late 2006 to early 2007, N = 1,009, completion 75%); the seven metaphors with their
  survey wording; Table 2 (share who saw each as an important explanation); Table 3 (support for
  sixteen policies); Tables 4–5 (regressions). The tables come out one cell per line, so check any
  figure against the PMC page before printing it.

## Group B · open textbooks

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| OpenStax *American Government* **4e**: details page; site licence line; 16.1, 16.4, 10.1, 8.4 whole; Key Terms ch. 8, 10, 16 | https://openstax.org/details/books/american-government-4e; https://openstax.org/books/american-government-4e/pages/16-1-what-is-public-policy (main and footer scope), `.../16-4-policymakers`, `.../10-1-interest-groups-defined`, `.../8-4-the-impact-of-the-media`, `.../8-key-terms`, `.../10-key-terms`, `.../16-key-terms` (main scope) | 9 | 9/9 | "by OpenStax is licensed under Creative Commons Attribution-NonCommercial-ShareAlike License v4.0" (details page); footer: "Except where otherwise noted, textbooks on this site are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY NC-SA) license." | `openstax_amgov_4e` (new) |
| *Optional.* OpenStax *Introduction to Political Science* §1.2 whole; details page | https://openstax.org/details/books/introduction-political-science; https://openstax.org/books/introduction-political-science/pages/1-2-public-policy-public-interest-and-power (main scope) | 2 | 2/2 | "by OpenStax is licensed under Creative Commons Attribution-NonCommercial-ShareAlike License v4.0" (details page) | `openstax_intro_polisci_1_2` (new) |
| *Optional.* Gilson (ed.) 2012 Reader, Part 1 §4 Health policy, §5 Health policy analysis (Policy actors; focus and forms), abridged version; copyright pages of abridged and full versions | https://ahpsr.who.int/docs/librariesprovider11/publications/supplementary-material/alliancehpsr_abridgedversionreaderonline.pdf?sfvrsn=c7b5f0a3_5 (PDF text layer); https://iris.who.int/server/api/core/bitstreams/fe70fd12-7a32-4e52-893f-9f1942258789/content (IRIS extracted text of the full Reader's 18-page front matter); WHO terms https://www.who.int/about/policies/terms-of-use | 4 | 4/4 | "© World Health Organization 2012 / All rights reserved." Permission requests "whether for sale or for noncommercial distribution" to WHO Press. **Not open** | `gilson_2012_hpsr_reader` (new) |

## Group C · Union procedure

| Source | URL fetched | Passages | Check n/n | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Allocation of Business Rules 1961, as amended upto Amendment Series no. 386 dated 22 July 2026: title, Order and rules 1–4, First Schedule, eight Second Schedule entries; cabsec terms | https://cabsec.gov.in/writereaddata/allocationbusinessrule/completeaobrules/english/1_Upload_4265.pdf; https://cabsec.gov.in/footercontent/websitepolicies/; https://cabsec.gov.in/footercontent/termsandconditions/ | 13 | 13/13 | "Contents of this website may not be reproduced partially or fully, without due permission from Cabinet Secretariat. If referred to as a part of another website, the source must be appropriately acknowledged." Terms: "should not be construed as a statement of law or used for any legal purposes" | `goi_aob_rules_1961` (new) |
| Transaction of Business Rules 1961, as amended upto Amendment Series no. 75 dated 13 January 2025: title, rules 1–12, Second Schedule | https://cabsec.gov.in/writereaddata/transactionofbusinessrulescomplete/completeaobrules/english/1_Upload_3983.pdf | 4 | 4/4 | as above (cabsec) | `goi_tob_rules_1961` (new) |
| Rajya Sabha Secretariat 2005, Legislative Procedure in the Rajya Sabha, whole; sansad.in RS terms | https://cms.rajyasabha.nic.in/UploadedFiles/Procedure/PracticeAndProcedure/English/6/legislative_procedure.pdf; https://sansad.in/rs/termsAndConditions | 2 | 2/2 | "©RAJYA SABHA SECRETARIAT, NEW DELHI" (booklet); site T&C "apply to the entire content published on this website", no reuse terms stated | `rajyasabha_2005_legislative` (new) |
| PRS 2012, Indian Parliament at 60 years, whole; footer; disclaimer | https://prsindia.org/articles-by-prs-team/indian-parliament-at-60-years-facts-statistics; https://prsindia.org/aboutus/disclaimer | 3 | 3/3 | "PRS Legislative Research is licensed under a Creative Commons Attribution 4.0 International License" (footer, which also says "Copyright © 2026 prsindia.org All Rights Reserved.") | `prs_2012_parliament60` (new) |
| PIB 1797203, Adherence to PLCP, whole | https://www.pib.gov.in/PressReleasePage.aspx?PRID=1797203 | 1 | 1/1 | none on the release; pib.gov.in/CopyRight.aspx 404 | `pib_1797203` (new) |
| National Health Policy 2017: §1–§3.2, §26–28; NHSRC copyright and terms | https://nhsrcindia.org/sites/default/files/2021-07/National%20Health%20Policy%202017%20%28English%29%20.pdf; https://nhsrcindia.org/copyright-policy; https://nhsrcindia.org/terms-conditions | 4 | 4/4 | NHSRC: "Material featured on this site may be reproduced free of charge in any format or media without requiring specific permission ... the source must be prominently acknowledged." | `mohfw_2017_nhp` (new) |
| PIB 1513000, MoHFW Year Ender 2017: NHP and NNM sections | https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1513000 | 2 | 2/2 | none on the release | `pib_1513000` (new) |

### Notes for the conductor

- READY.md row 30 asks for the "First Schedule" entries of named departments; in the rules the First
  Schedule only lists Ministries/Departments, and the subjects are in the **Second Schedule**. Both held.
  "Food safety" sits in the Department of Health and Family Welfare, Second Schedule item 3(a) "The Food
  Safety and Standards Act, 2006".
- cabsec's copyright policy says no reproduction "without due permission". Quote briefly with attribution.
- The Rajya Sabha booklet dates from 2005 and PRS's private-member figures from 2012. State them with
  their dates.
- The Lok Sabha terms page could not be read (HTTP 500). The answer was fetched by the earlier run
  before this was known. Keep it or drop it; it is also backed by `pib_1797203`.
- NHP's own text does not state its approval. Cabinet approval on 15 March 2017 rests on `pib_1513000`.

## Group D · tobacco, GST, framing texts

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| COTPA 2003 as enacted (whole), S.O. 238(E), NTCP list and terms | https://ntcp.mohfw.gov.in/assets/document/Acts-Rules-Regulations/COTPA-2003-English-Version.pdf; `.../SO-238(E).pdf`; https://ntcp.mohfw.gov.in/cigarettes_and_other_tobacco_products; https://ntcp.mohfw.gov.in/website_policies | 5 | 5/5 | "This contents of this Portal may not be reproduced partially or fully, without due permission from MoHFW, Govt. of India. If referred to as a part of another publication, the source must be appropriately acknowledged." (NTCP website policies); footer "Copyright © 2021. CHI. All Right Reserved." | `cotpa_2003` (new) |
| WHO FCTC Arts 5-8, copyright notice; UNTC status and India row; FCTC Parties page | https://iris.who.int/server/api/core/bitstreams/264104b3-241a-4e48-88f9-aa7120779ffc/content; https://treaties.un.org/Pages/ViewDetails.aspx?src=TREATY&mtdsg_no=IX-4&chapter=9&clang=_en (table scope); https://fctc.who.int/who-fctc/overview/parties | 6 | 6/6 | "© World Health Organization 2003, updated reprint 2004, 2005 All rights reserved." (PDF); publication page "All rights reserved"; UN terms: personal, non-commercial use | `who_fctc_2003` (new) |
| PIB 2163555, body, Annexure I and II beverage rows, closing note; PIB copyright policy | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2163555; https://www.pib.gov.in/Content/102_2_Copyright-Policy.aspx | 7 | 7/7 | "Material featured on this website may be reproduced free of charge and there is no need for any prior approval for using the content." (PIB Copyright Policy) | `pib_2163555` (new) |
| PIB 2168426, whole | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2168426 | 2 | 2/2 | as above | `pib_2168426` (new) |
| CGST Act 2017, cover, s.1, s.9, fn 17 | https://cbic-gst.gov.in/pdf/CGST-Act-Updated-30092020.pdf | 4 | 4/4 | None for reproduction. CBIC terms: "should not be construed as a statement of law or used for any legal purposes"; the PDF says it "has no legal binding or force" | `cgst_act_2017` (new) |
| PIB 2105618 (PM, Mann Ki Baat 119), whole | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2105618 | 2 | 2/2 | PIB Copyright Policy, as above | `pib_2105618` (new) |
| FSSAI Eat Right India pages, whole; FSSAI copyright policy | https://fssai.gov.in/eat-right-india; https://eatrightindia.gov.in/eatrightindia.jsp; https://eatrightindia.gov.in/whyeat-right.jsp; https://fssai.gov.in/website-policies | 4 | 4/4 | "Material featured on this site may be reproduced free of charge in any format or media without requiring specific permission." (FSSAI Website Policies) | `fssai_eat_right_india` (new) |

Constitution Art. 279A: present in the held `constitution_current.txt` (line 12077: "279A. Goods
and Services Tax Council.—(1) The President shall, ..."; clauses (2) membership and (4)
recommendations checked). It was not re-fetched.

### Caveats and decisions for the conductor

1. **NTCP's copying bar (COTPA).** Automated access is not barred. But MoHFW's NTCP policy says
   the portal's contents "may not be reproduced partially or fully, without due permission". The
   Act is a Gazette text. Copyright Act s.52(1)(q) is general knowledge and was not fetched. The file
   is written and the conductor decides whether it stands, as with the Companies Act precedent in
   S55.
2. **C18's "40%" needs two numbers.** CGST Act s.9(1) caps the central rate at 20%. The 40% in
   PIB 2163555 is the combined GST slab (CGST + SGST, or IGST). A note must not say that the
   Union levies 40%.
3. **Recommendation vs law.** PIB 2163555 says the notifications "alone shall have the force of
   law". The notification (9/2025-CT(R)) is named officially in PIB 2168426 but is not held. A
   search result (not opened) shows 01/2026-CT(R) of 30 Apr 2026 amending 9/2025. Whether the
   beverage rate still stands on 1 Oct 2026 is **unverified**.
4. **READY.md wording.** READY.md gives the CGST Act link as `CGST-bill-e.html`. It is now a 404.
   The CBIC consolidation stored here is as on 30 Sep 2020. Later amendments to s.9 are not
   checked.
5. **COTPA and FCTC texts are imperfect.** COTPA is OCR of a scan, and several section numbers are
   misread (listed in the file). The FCTC text is all rights reserved. It is for quotation and
   citation only.
6. **The edible-oil call.** The PRID found is 2105618, the PM's own words in Mann Ki Baat, 23 Feb
   2025. The call was first made at the National Games opening in Dehradun (Jan 2025). That speech
   is not held.

