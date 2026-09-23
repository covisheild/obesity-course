# Source gate · S01-R1

Checked against `sources/`, `sources/INDEX.yml` and `sources/SOURCES.md` on 2026-09-23. The rule in `claude.md`: a line saying **no** stops the pipeline. Nothing below was fetched to write this list; URLs marked *confirm* were given from memory and must be checked when the source is fetched. Transcribe with `mcp__TinyFish__fetch_content`, never WebFetch (`sources/SOURCES.md`).

## Held

| Work, section | Kind | File | Obtained | Concepts |
| --- | --- | --- | --- | --- |
| OpenStax Anatomy and Physiology 2e §24.1 (catabolic/anabolic balance paragraph), §24.3 (triglyceride in adipose tissue) | textbook | `openstax_anatphys_2e.txt` | **yes** | C01, C05 |
| OpenStax Anatomy and Physiology 2e §24.6 (BMR definition only; its 70/20/10 percentages are uncited and not usable) | textbook | `openstax_anatphys_2e.txt` | **yes** | C04 |
| OpenStax Anatomy and Physiology 2e §24.7 (the 3,500 calories per pound paragraph, marked do-not-cite in the file; used only as a specimen to diagnose) | textbook | `openstax_anatphys_2e.txt` | **yes** | C07 |
| OpenStax Chemistry 2e §5.1 (first law), §5.2 (nutritional Calorie) | textbook | `openstax_chemistry_2e.txt` | **yes** | C05, C06 |
| OpenStax College Physics 2e §7.6 (conservation of energy) | textbook | `openstax_college_physics_2e.txt` | **yes** | C05 (spare anchor) |
| FAO Food and Nutrition Paper 77 (2003) ch. 3, §3.5.1 (fat 37 kJ/g, 9.0 kcal/g) | consensus_statement | `fao_food_energy.txt` | **yes** | C02 |
| NIST Guide to the SI, calorie footnotes (thermochemical calorie = 4.184 J) | instrument | `nist_sp811.txt` | **yes** | C02 |

## Intake, 2026-09-23

Taken in by the S01-R1 source intake (log: `INTAKE.md`). Identifiers confirmed against PubMed; two
PMCIDs above were wrong. Every stored passage was cut from the raw TinyFish fetch and re-checked
against it: 118 of 118; Hall 2008, from Harsh's PDF, 17 of 17 against its text layer (135 of 135).

| Work, section | Kind | Obtained | File, citekey | Confirmed URL | Concepts |
| --- | --- | --- | --- | --- | --- |
| Hall KD. *Int J Obes* 2008;32:573 (PMID 17848938, PMC2376744, NIHMS47767, doi:10.1038/sj.ijo.0803720) | primary | **yes**: author-manuscript PDF supplied by Harsh 2026-09-23 (no session route reached it), text layer via pdftotext | `hall_2008_ijo.txt`, `hall_2008_ijo` | https://pmc.ncbi.nlm.nih.gov/articles/PMC2376744/ | C01, C02, C07, C08 |
| Hall KD et al. *Am J Clin Nutr* 2012;95:989 (PMID 22434603, PMC3302369, doi:10.3945/ajcn.112.036350) | primary (review) | **yes** (second attempt): publisher PDF text layer | `hall_2012_ajcn.txt`, `hall_2012_ajcn` | https://pmc.ncbi.nlm.nih.gov/articles/PMC3302369/; text via https://europepmc.org/articles/PMC3302369?pdf=render | C04, C05, C06, C09 |
| Hall KD, Guo J. *Gastroenterology* 2017;152:1718 (PMC5568065) | primary (review) | **yes** | `hall_guo_2017.txt`, `hall_guo_2017` | https://pmc.ncbi.nlm.nih.gov/articles/PMC5568065/ (text from the PMC Article Dataset) | C04, C06, C09, C10 |
| Hall KD, Sacks G, Chandramohan D, Chow CC, Wang YC, Gortmaker SL, Swinburn BA. *Lancet* 2011;378:826 (PMC3880593) | primary | **yes** | `hall_2011_lancet.txt`, `hall_2011_lancet` | https://pmc.ncbi.nlm.nih.gov/articles/PMC3880593/ | C02 (39·5 MJ/kg fat, 7·6 MJ/kg lean, citing Hall 2008), C07, C08 (glycogen and water) |
| Thomas DM, **Martin CK, Lettieri S, Bredlau C, Kaiser K, Church T, Bouchard C,** Heymsfield SB. *Int J Obes* 2013;37:1611 (**PMC4024447**, not PMC3859816, which is Hall and Chow 2013) | primary (commentary) | **yes** | `thomas_2013_3500kcal.txt`, `thomas_2013_3500kcal` | https://pmc.ncbi.nlm.nih.gov/articles/PMC4024447/ | C07 |
| Rosenbaum M, Leibel RL. *Int J Obes* 2010;34 Suppl 1:S47 (PMC3673773) | primary (review) | **yes** | `rosenbaum_leibel_2010.txt`, `rosenbaum_leibel_2010` | https://pmc.ncbi.nlm.nih.gov/articles/PMC3673773/ | C09 |
| Polidori D et al. *Obesity* 2016;24:2289 (**PMC5108589**, not PMC5098077) | primary | **yes** | `polidori_2016.txt`, `polidori_2016` | https://pmc.ncbi.nlm.nih.gov/articles/PMC5108589/ | C03 (self-report), C09 |
| FAO/WHO/UNU. *Human energy requirements*, 2004, chapter 2 and chapter 5 pages | consensus_statement | **yes** | `fao_who_unu_2004.txt`, `fao_who_unu_2004` | https://www.fao.org/4/y5686e/y5686e00.htm (chapters at y5686e04.htm and y5686e07.htm) | C03, C04 |
| ICMR-NIN 2020, energy requirement | guideline | **partly**: the ICMR-NIN *Brief Note* (PDF text layer), not the full report | `icmr_nin_2020_brief.txt`, `icmr_nin_2020_brief` | https://www.nin.res.in/rdabook/brief_note.pdf. The full report is sold in print (Rs 400, pre-payment) per https://www.nin.res.in/RDA_Full_Report_2024.html; no free download found | C03, C04 |
| MoSPI per-capita kcal/day | primary (survey) | **yes, the successor**: NSS Report 594 (HCES 2022-23 & 2023-24), whose Table 3.14 also gives 2011-12. Report 560 itself not held | `nss_594_nutritional_intake.txt`, `nss_594_2025` | https://www.mospi.gov.in/sites/default/files/publication_reports/Nutritional_Intake_in_India_L.pdf | C03 |
| BIPM SI prefixes (mega) | instrument | **yes** | `bipm_si_prefixes.txt`, `bipm_si_prefixes` | https://www.bipm.org/en/measurement-units/si-prefixes | C02 |
| NIST SP 811 App. B.8, pound = 0.453 592 37 kg exactly | instrument | **yes** | `nist_sp811_pound.txt`, `nist_sp811_pound` | https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8 and the footnotes page | C07 |
| A published claim that breaks conservation | specimen | **partly**: the US FTC's list of claims it names false (real, authoritative text); its example ads are the FTC's own illustrations, not a real ad found in the wild | `ftc_gut_check_2014.txt`, `ftc_gut_check_2014` | https://www.ftc.gov/business-guidance/resources/gut-check-reference-guide-media-spotting-false-weight-loss-claims | C08 |

## Gate

**Every line now says yes or partly.** No source line blocks. What the held sources do and do not give:

- **C01, C02**: Hall 2008 gives fat mass change 39.5 MJ/kg, lean mass change 7.6 MJ/kg, and says fat mass change
  is not adipose tissue, which includes fluid and protein. It gives **no adipose lipid fraction of its own**: the
  only figure is the 87% fat assumed by the rule's derivation (Wishnofsky 1958), and the paper's point is that
  this assumption is wrong. A per-kg energy for adipose tissue (the ~7,700 kcal/kg of the inventory) is stated
  only as the rule itself (3500 kcal per pound, 32.2 MJ per kg). The drafter must present ~7,700 kcal/kg as the
  rule's figure, not as a measured property of adipose tissue.
- **C07**: the rule's derivation is now sourced (Hall 2008, block 3).
- **C08**: Hall 2008 says glycogen's effects on weight loss "typically occur within the first week"; Hall 2012 says
  water is bonded to glycogen. Neither says early loss is *mostly* glycogen and water; the drafter should not say
  so. A real published claim is still Harsh's choice (the FTC examples are illustrations).
- **ICMR-NIN**: the brief note only; the full 2020 report is print-only.
