# What is in `sources/`, and what has been checked in it

Every file here was downloaded from India Code and read. The "verified" column lists the
provisions actually located in the text, not the provisions the file is assumed to contain.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `fss_act_2006.txt` | Food Safety and Standards Act 2006 (Act 34 of 2006), enacted 23 Aug 2006 | 24,104 | s.4 establishes FSSAI; s.23(1) packaged food must be labelled "in the manner as may be specified by regulations"; s.92 power to make regulations; s.93 regulations laid before Parliament |
| `constitution_current.txt` | Constitution of India, consolidated 2026 text (handle 123456789/618394) | 135,907 | Articles 21, 32, 47, 53, 79, 226, 245, 246, 279A |
| `constitution.txt` | **Do not cite.** An older India Code consolidation, newest amendment it names 2006 | 89,103 | Contains no Article 279A. Kept only because it is the worked example in Book 0 F3 |
| `nfsa_2013.txt` | National Food Security Act 2013 (Act 20 of 2013), 10 Sep 2013 | 7,679 | s.5, mid-day meal entitlement |
| `consumer_prot_2019.txt` | Consumer Protection Act 2019 (Act 35 of 2019), 9 Aug 2019 | 21,568 | Chapter III s.10, the Central Consumer Protection Authority |
| `bipm_si.txt` | BIPM's statement of the SI definition, in force from 20 May 2019 | 407 | The seven defining constants with their exact values; the relations Hz = s-1, J = kg m2 s-2 |
| `nist_sp811.txt` | NIST Guide to the SI, footnotes; page updated 18 Aug 2025 | 394 | calth = 4.184 J exactly; International Table calorie = 4.1868 J; the kilocalorie as the food-energy unit |
| `openstax_chemistry_2e.txt` | OpenStax Chemistry 2e (CC BY-NC-SA 4.0), verbatim excerpts from seven sections. **Excerpts, not the whole book** | 6,268 | 2.3 atom diameter 10-10 m vs nucleus 10-15 m, proton/neutron/electron masses and charges, amu; 2.4 molecular and empirical formula, the parenthetical definition of a chemical bond, diatomic molecules; 7.2 ionic vs covalent bonding, pure vs polar covalent, electronegativity; 7.5 bond energy, D(H-H) = 436 kJ, the HCl arithmetic -185 kJ, exothermic/endothermic in terms of bond strengths; 5.1 energy, heat, work, first law, heat capacity, specific heat and q = c x m x DeltaT, water 4.184 J/g degC, the Calorie; 5.2 calorimetry, system and surroundings, the bomb calorimeter and its benzoic-acid calibration, the nutritional-Calorie feature with 4/4/9 Cal per gram and the Atwater system; 5.3 enthalpy, standard enthalpy of combustion, Table 5.2 values |
| `openstax_biology_2e.txt` | OpenStax Biology 2e (CC BY-NC-SA 4.0), verbatim excerpts from nine sections. **Excerpts, not the whole book** | 5,106 | 4.1 the unified cell theory; 4.3 plasma membrane, cytoplasm, nucleus, mitochondria, ribosomes; 5.1 the fluid mosaic model, phospholipid head and tail, the bilayer; 5.3 active transport and its energy cost; 3.4 amino acids as monomers, shape determines function, denaturation, enzyme and substrate; 9.1 ligand, receptor, conformational change on binding, internal vs cell-surface receptors; 14.2 nucleotides, the four bases, the double helix, complementary pairing, antiparallel strands; 12.2 alleles, dominant and recessive, genotype and phenotype, the 3:1 ratio; 7.1 ATP as the cell's energy currency and its hydrolysis to ADP |
| `openstax_anatphys_2e.txt` | OpenStax Anatomy and Physiology 2e (CC BY-NC-SA 4.0), verbatim excerpts from ten sections. **Excerpts, not the whole book** | 6,745 | 24.1 metabolism, anabolism, catabolism, and the energy-balance statement; 24.2 glycolysis and the ATP yield; 24.3 triglyceride storage in adipose tissue and its release; 24.4 protein metabolism and the essential amino acids; 24.6 core temperature, the four heat-exchange routes, metabolic rate and BMR; 24.7 the nutritional Calorie, and the BMI cut-points; 23.7 what the small intestine absorbs and what it does not; 23.6 the liver, pancreas and gallbladder; 17.9 alpha and beta cells, insulin and glucagon; 17.1 how fast different hormones act |
| `openstax_college_physics_2e.txt` | OpenStax College Physics 2e (CC BY-NC-SA 4.0), verbatim excerpts from eight sections, plus a labelled block from University Physics. **Excerpts, not the whole book** | 3,896 | 7.1 the joule as the unit of work and energy; 7.6 the law of conservation of energy and the forms energy takes, including chemical; 14.1 heat against temperature and the SI unit of heat; 14.2 specific heat, Q = mc(Delta)T, and Table 14.1's water row 4186; 14.4 conduction, convection and radiation defined together; 14.5, 14.6, 14.7 each method in turn |
| `fao_food_energy.txt` | FAO Food and Nutrition Paper 77, *Food energy - methods of analysis and conversion factors*, 2003, chapter 3 | 1,610 | 3.2 bomb calorimetry as the measure of gross energy; 3.3 the cascade from ingested or gross energy through faecal, gaseous and urinary losses to metabolizable energy; 3.5.1 the Atwater general factors, 17 kJ/g (4.0 kcal/g) protein, 37 kJ/g (9.0 kcal/g) fat, 17 kJ/g (4.0 kcal/g) carbohydrate, with footnote 9's unrounded values |


Drop the file in, add a row, and fill the verified column only with provisions you have found by
searching the file. An empty verified column is honest. A guessed one is the failure this whole
folder exists to prevent.

## How the five open-textbook files were obtained, and why that is written down

Added 23 September 2026 by the Book 0 Part E chat. The India Code files above are downloads. These
five are not, and the difference is worth stating because it changes what a quote check proves.

`PIPELINE.md` records NCBI Bookshelf and PubChem as CAPTCHA-gated and unreachable from a session.
Remeasured on 23 September 2026, that is no longer true: OpenStax, NCBI Bookshelf and FAO all
return their pages. Direct `curl` is still refused at the proxy for every host, which is probably
what the earlier note actually measured. **The distinction is the tool, not the host.**

**And not every tool that reaches a page can transcribe it.** Four of these files were first built
with WebFetch, whose extractor is a small model with a quote-length cap. Checked afterwards against
raw page text, 25 per cent of their supposedly verbatim passages had been quietly tidied: figure
markers dropped, whole sentences deleted mid-paragraph with no ellipsis, and in two cases a
sentence that does not exist on the page at all - a specific heat of water "for the liquid" welded
together out of two different sentences, and a table row with units imported from the column
header. Both looked exactly like quotations.

They were rebuilt with `mcp__TinyFish__fetch_content`, which returns the raw page with no model in
the loop, and every passage taken as a contiguous slice of it. The file built that way first time
scored 106 of 106 word for word; after the rebuild all five score 281 of 281.

**The rule that follows:** a source file is transcribed with a tool that has no model between the
page and the file. Use `mcp__TinyFish__fetch_content`. WebFetch is for reading a page, not for
quoting one, and a passage it returns must never be stored here as verbatim.

**What a quote check against these files proves, and what it does not.** It proves the words are in
the file and the file is a faithful slice of the page as fetched on 23 September 2026. It does not
prove the page still says that today, and it does not prove the passage is absent from the book
when the check fails - these are excerpts from named sections, so absence from the file is not
absence from the source. Each entry in `INDEX.yml` names the sections it holds for that reason.

## Known missing

- FSSAI Labelling and Display Regulations 2020
- FSSAI draft amendment on front-of-pack labelling, and the comment record
- The notification capping industrial trans fat at 2%
- The Supreme Court order of 10 September 2026
- General Clauses Act 1897
- Government of India (Allocation of Business) Rules 1961

**Needs a person with a browser, and why.** Everything above that is a PDF cannot be obtained
from inside a session: PDFs fetch but yield no extractable text, so there is nothing to store and
nothing a quote can be checked against. CAPTCHA-gated hosts (NCBI Bookshelf, PubChem) and direct
downloads through the proxy fail the same way. Retrieving these is a five-minute job in a browser
and is the one step of this pipeline that still needs a human.

Blocking Book 0 Part B specifically:

| Wanted for | Source | Why it is stuck |
| --- | --- | --- |
| B4, the Indian labelling requirement | FSS (Labelling and Display) Regulations, compendium Version VIII, 09.09.2025, on fssai.gov.in | PDF, no text extraction |
| B5, mg/dL to mmol/L | A molar mass for glucose and cholesterol from IUPAC, PubChem or a clinical chemistry reference | PubChem is gated; needs an HTML or text source |

## Vintage of each copy

Added 2026-09-20 by the Book 0 Part A chat, which needed figures out of two of these files and
found that nothing in the table above records how current any copy is. The column that matters for
an institutional number is not when the Act was passed. It is what the copy in this folder says
about changes made since.

Read by searching each file for every occurrence of `by Act N of YYYY` and taking the newest.

| File | Newest change the copy itself names | What that means for a figure taken out of it |
| --- | --- | --- |
| `fss_act_2006.txt` | **Act 13 of 2008**, with effect from 7 February 2008. One amending Act, cited in three footnotes. Nothing later anywhere in the file | Every penalty figure in it is as at 2008 on the face of this copy. Quote it as what this copy says, not as the penalty in force |
| `nfsa_2013.txt` | **None.** The file carries no amendment footnote at all, so it reads as the Act as enacted in 2013 | Schedule I's prices were fixed for three years from commencement and that window closed in 2016; the file says nothing about what replaced them. Schedule II's nutritional standards carry no such clock in the text |
| `constitution_current.txt` | Consolidated 2026 text, per the row above; contains Article 279A | Usable |
| `constitution.txt` | Newest amendment it names: 2006 | **Do not cite**, per the row above |
| `consumer_prot_2019.txt` | **None.** Checked the same way on 2026-09-20 and the file carries no amendment footnote, so it reads as the Act as enacted in 2019 | Quote s.21, s.34, s.47 and s.58 figures as what this copy says |
| `bipm_si.txt` | The 2019 revision, named on the page itself. BIPM revises the SI by CGPM resolution, so the trigger is the next CGPM | Usable. The defining constants are exact by definition and do not drift |
| `nist_sp811.txt` | Page updated 18 August 2025 | Usable. The calorie definitions are fixed conversions, not measurements |
| `openstax_chemistry_2e.txt` | Second edition ("2e"), named on every page; fetched 23 September 2026 | Usable. Settled undergraduate chemistry, and the constants in it are definitions or long-stable measurements. The risk here is not vintage but coverage: the file holds excerpts from seven sections, so absence from it is not absence from the book |
| `openstax_biology_2e.txt` | Second edition, named on every page; fetched 23 September 2026 | Usable, with the same coverage caveat: excerpts from nine sections |
| `openstax_anatphys_2e.txt` | Second edition, named on every page; fetched 23 September 2026 | Usable for structure and function. **Not usable for any number.** Every figure in it is stated flat with no study named, and its diabetes and obesity prevalence figures are a 2010 CDC vintage that is now well out of date |
| `openstax_college_physics_2e.txt` | Second edition, named on every page; fetched 23 September 2026 | Usable. The constants are definitions or long-stable measurements |
| `fao_food_energy.txt` | The 2003 report, unrevised; fetched 23 September 2026 | Usable, and it is an adopted convention rather than a measurement. Trigger: the next FAO or WHO revision of the food-energy conversion factors |

This does not make any of these files wrong. It makes the date on them knowable, which is the whole
point of Book 0 F3, and it was not knowable from this file before.

## Added by the Book 0 Part D chat, 2026-09-23

Fetched whole with the TinyFish `fetch_content` tool, which returns page text without a
summarising model in between. Direct downloads from the sandbox are refused at the proxy for all
three hosts. Full account of the route in `books/B0/READY-part-D.md`.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `openstax_intro_stats_2e.txt` | OpenStax *Introductory Statistics 2e* (2023; web version updated 7 Jul 2026), twelve sections: 1.1, 1.2, 2.3, 2.5, 2.7, 3.1, 3.2, 3.3, 3.4, 7.1, and 4.1, 4.2 added 2026-09-24 by the S02-R1 intake | 30,703 | Probability as "long-term relative frequency" (3.1); the independence conditions (3.2); "the larger the sample, the smaller the sampling error" and sampling bias (1.2); the median (2.5); the standard deviation and n minus 1 (2.7); "divided by the square root of n" (7.1). Mathematical typesetting is garbled by extraction; quote prose only |
| `jcgm_vim3.txt` | JCGM 200:2012, the International vocabulary of metrology (VIM3), online edition updated 29 Apr 2017; entries 2.11, 2.13–2.21, 2.53, 4.14, 4.28 only | 1,700 | Measurement error (2.16), systematic (2.17) and random (2.19) error, accuracy (2.13), trueness (2.14), precision (2.15), resolution (4.14), zero error (4.28). The one-line definition of 2.16 came through WebFetch, asked for verbatim, because TinyFish's extractor dropped it |
| `kiran_2022_muac_nc.txt` | Kiran, Harshitha and Bhargava, *Heliyon* 2022;8:e12173 (PMC9791811), full text with tables, via the Europe PMC full-text service | 4,863 | Tables 1–4. **Eight internal inconsistencies in the paper itself**, listed in the file header — they are in the published paper, not introduced by this copy |

| `openstax_contemporary_math_7_7.txt` | OpenStax *Contemporary Mathematics* (2023; web version updated 23 Apr 2026), section 7.7 *What Are the Odds?* only | 1,691 | Odds for an event as the ratio of outcomes in it to outcomes not in it; odds as a ratio of probabilities; probabilities between zero and one, odds any non-negative number. Added after the D1 audit found odds defined from no source |

**Vintage.** The OpenStax web version is revised in place; the date to recheck against is the
"web version last updated" line on its details page. The VIM3 online edition is frozen at 2017; the
trigger is a VIM4 publication by the JCGM. The Kiran paper is a published article; the trigger is
an erratum or correction notice.

## Added by the S01-R1 source intake, 2026-09-23

Every passage was cut programmatically from the raw text the TinyFish `fetch_content` tool
returned (saved from the tool's own result file, not retyped), and re-checked afterwards as a
whitespace-normalised substring of that fetch: 118 of 118. Hall 2008, supplied by Harsh as a PDF,
was checked the same way against its pdftotext extraction: 17 of 17. Eleven passages added to three files
after the C09/C10 audit bring the total to 146 of 146. Log in `books/S01-R1/INTAKE.md`.

**How the journal papers were reached, and what that means.** `pmc.ncbi.nlm.nih.gov` now answers
TinyFish with a reCAPTCHA page, the Europe PMC full-text service returns HTTP 500 for articles
outside the open-access subset, and the publishers (nature.com, OUP, Elsevier) paywall or
bot-block. NCBI's own PMC Article Dataset on AWS (`pmc-oa-opendata.s3.amazonaws.com`) serves each
article's plain text and is reachable. What it serves for these five is the **NIH author
manuscript**, not the typeset article, and its licence line says: "This file is available for text
mining. It may also be used consistent with the principles of fair use under the copyright law."
None of the five is open-licensed. Hall 2008 and Hall et al. 2012 are not in that dataset. Hall et al.
2012 was later obtained as the publisher PDF through Europe PMC's PDF render
(`europepmc.org/articles/PMC3302369?pdf=render`); the same route returns an error for Hall 2008,
which Harsh then supplied as the author-manuscript PDF.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `hall_2011_lancet.txt` | Hall et al., *Lancet* 2011;378:826 (PMC3880593), author manuscript. Excerpts, not complete | 1822 | Energy per kg change of body fat 39·5 MJ and 7·6 MJ per kg lean mass; the 3500 kcal per pound rule named and its origin in estimating the energy content of weight lost; 2 MJ/day cut predicting 22 kg in year one under the static rule, about double the model; intracellular water with stored glycogen; rule of thumb 100 kJ per day per kg; half times of about 1 year |
| `hall_guo_2017.txt` | Hall and Guo, *Gastroenterology* 2017;152:1718 (PMC5568065), author manuscript. Excerpts | 2123 | Energy balance "does not provide a causal explanation"; 3 components of expenditure; thermic effect about 10% of intake; metabolic adaptation; intake rises about 100 kcal/d per kg lost; expenditure slope about 20–30 kcal/d per kg; static, settling point, set point models; body fat as several months of expenditure. **Added 2026-09-23 after the C09/C10 audit:** individual weight changes are highly variable even when exercise is supervised; exercise compensated by intake and non-exercise activity |
| `thomas_2013_3500kcal.txt` | Thomas et al., *Int J Obes* 2013;37:1611 (PMC4024447), author manuscript. Excerpts | 1136 | "Wishnofsky's Rule" (keywords); 3500 kcal per pound (about 0.45 kg) attributed to reference 3, Wishnofsky 1958; 103 adults; lost 20.1±11.3 lb against 27.6±16.0 lb predicted. Does **not** describe how Wishnofsky derived the rule. **Added 2026-09-24 (S02-R1):** the Methods equation W(t) = W_0 - ΔEB (t/3500) as MathML with a plain-text rendering |
| `rosenbaum_leibel_2010.txt` | Rosenbaum and Leibel, *Int J Obes* 2010;34 Suppl 1:S47 (PMC3673773), author manuscript. Excerpts | 1180 | 20%–25% fall in 24-hour expenditure after 10% or greater loss; 10–15% below that predicted from fat and lean mass; ~300–400 fewer calories per day; over 100,000 kcal stored in a 70-kg man. **Added 2026-09-23 after the C09/C10 audit:** 80%-90% return to their previous weight percentiles; maintenance of a reduced body fatness will probably require a lifetime of meticulous attention to intake and expenditure |
| `polidori_2016.txt` | Polidori et al., *Obesity* 2016;24:2289 (PMC5108589), author manuscript. Excerpts | 3688 | ~100 kcal/day per kg of lost weight; against ~30 kcal/kg/day in expenditure; self-reported intake inaccurate. **Added 2026-09-23 after the C09/C10 audit:** trial weight reached a new equilibrium "several kilograms lower", intake up ~350 kcal/day at steady state; placebo loss under 1 kg; energy expenditure not directly measured; group means only, individual variability not characterised; proportional controller not known valid "for a range of weight losses"; Methods clause "T = 52 was the number of days between measurements" (resolved 2026-09-24 from the XML: t = (N−1)*T with N = 2, so 52 days); **added 2026-09-24 (S02-R1):** Equations 1-5 as MathML with plain-text renderings, and the prose defining ρ, ε, k_P, k_I; **added 2026-09-24 (S02-R1 audit follow-up):** β "accounts for the adaptation of energy expenditure during a diet perturbation"; UGE "represents the energy losses" of glucose in urine; Table 1 rows δ0 10 kcal/kg/d, Δδ 0, β 0.24, UGE 360 kcal/d (no per-gram conversion stated); fitted kP = 95 kcal/day per kg (Results); commercial programme (not the trial): plateau at ~8 months with intake back within 100 kcal/day of baseline; reference 1 is Leibel, Rosenbaum and Hirsch 1995 (NEJM), the source of the ~30 kcal/kg/day |
| `fao_who_unu_2004.txt` | FAO/WHO/UNU, *Human energy requirements*, FAO Food and Nutrition Technical Report Series 1 (2004), HTML edition. Excerpts from the chapter 2 and chapter 5 pages. "All rights reserved", non-commercial educational reproduction authorised with acknowledgement | 2227 | Definition of energy requirement; BMR 45 to 70 percent of TEE; metabolic response to food about 10 percent of BMR; DLW measures TEE over usually 10 to 14 days; gender, age and body weight as main determinants; PAL = TEE/BMR; sustainable PAL about 1.40 to 2.40; 1 kcal = 4.184 kJ; worked example 1 975 kcal for a 55 kg woman. **Added 2026-09-24 (S02-R1):** Table 5.2, Schofield's BMR equations by sex and age band (e.g. men 18-30: 15.057kg + 692.2 kcal/day), and the consultation's reason for keeping them |
| `hall_2008_ijo.txt` | Hall, *Int J Obes* 2008;32:573 (PMC2376744). NIH author-manuscript PDF (NIHMS47767) **supplied by Harsh** 2026-09-23; its text layer via pdftotext. Excerpts. The PDF states no licence | 2737 | Rule of 3500 kcal per pound, or 32.2 MJ per kg; its origin in a calculation assuming loss of adipose tissue of 87% fat (refs 1, 2); glycogen, protein and fat at 17.6, 19.7 and 39.5 MJ/kg; fat mass change 39.5 MJ/kg, not the same as adipose tissue, which includes fluid and protein; lean mass change 7.6 MJ/kg (h = 1.6 g water per g protein); glycogen's effects on weight loss typically within the first week; 24.7 MJ per kg for a 15 kg loss at 20 kg initial fat. Does **not** state its own adipose lipid fraction, or that early loss is mostly glycogen and water. Equations absent (images) |
| `hall_2012_ajcn.txt` | Hall et al., *Am J Clin Nutr* 2012;95:989 (PMC3302369), **publisher PDF** text layer via Europe PMC's PDF render (obtained on a second attempt). Excerpts. "© 2012 American Society for Nutrition"; free to read, not open-licensed. Consensus statement funded by ASN and ILSI North America | 2419 | The energy balance equation (ES = EI – EO) as the first law; REE about two-thirds of EO; TEF, AEE; water bound to glycogen; body fat energy content much higher than lean; passive and active compensation; the panel's recommendation that the 3500 kcal per pound rule no longer be used; rule of thumb 10 kcal/d per lb; DLW precision ~5%. Hyphenation and ligatures as in the PDF |
| `bipm_si_prefixes.txt` | BIPM SI prefixes page, whole table | 503 | kilo, mega, giga rows. Exponents lose their superscript in extraction ("106" is 10^6); read the header |
| `nist_sp811_pound.txt` | NIST SP 811 Appendix B.8 pound row, and the footnote with the exact factor | 456 | Pound (avoirdupois) 4.535 924 E-01 kg in B.8; exact 4.535 923 7 E-01 in the footnote; footnotes page updated 18 August 2025 |
| `ftc_gut_check_2014.txt` | US FTC, *Gut Check* (January 2014). Excerpts. No licence statement on the page | 830 | The seven claims; "Meaningful weight loss requires taking in fewer calories than you use"; claims 2 and 7 reasoning. Its example ads are the FTC's own illustrations, **not real published ads** |
| `icmr_nin_2020_brief.txt` | ICMR-NIN *Brief Note* on Nutrient Requirements for Indians 2020, PDF text layer. The summary note, **not** the full 2020 report | 1036 | TEE = BMR X PAL; sedentary PAL 1.53 to 1.40; BMR reduced a further 5%; requirement lower by 3 to 8 kcal/kg/day; sedentary man 65 kg 2110 kcal/d, woman 55 kg 1660 kcal/d. Its line that BMR is "measured directly (using DLW or HRM methods)" is wrong; do not cite it for that |
| `nss_594_nutritional_intake.txt` | MoSPI NSS Report 594, *Nutritional Intake in India 2022-23 & 2023-24* (2025), PDF text layer. Successor to Report 560, which is **not** held | 1453 | All-India per capita kcal/day 2233 rural, 2250 urban (2022-23), 2212 and 2240 (2023-24); Table 3.14 with 2011-12 at 2233 rural, 2206 urban; energy computed from a nutrient conversion table revised in 2025 |

**Vintage.** The five papers are published articles; the trigger is an erratum or retraction
(Europe PMC lists an erratum for Hall et al. 2012, Am J Clin Nutr 2012;96:448; the erratum is not held). FAO/WHO/UNU 2004 is the current
joint report; the trigger is a new expert consultation. ICMR-NIN 2020 is superseded when ICMR-NIN
revises its requirements. NSS 594 covers 2022-24; the trigger is the next HCES nutritional-intake
report. The BIPM prefix table was last extended in 2022 (CGPM Resolution 3); NIST SP 811's
footnotes page was updated 18 August 2025.

## Added by the S02-R1 source intake, 2026-09-24

Every passage was cut by script from the raw text the TinyFish `fetch_content` tool returned
(saved from the tool's own result file, not retyped) and re-checked afterwards as a
whitespace-normalised substring of that fetch: **63 of 63**. Log in `books/S02-R1/INTAKE.md`.

**Equations.** Where a paper's JATS XML carries MathML (Thomas 2013, Polidori 2016), the equation is
stored as that MathML, verbatim, from a fetch of the XML in TinyFish's html format, with a plain-text
rendering made by a deterministic script and marked as the file's notation, not the source's. Where
an equation is an image (every equation in Chow and Hall 2008; both in Hall 2008), nothing was
transcribed; the image links are in the file and in the intake log.

**New keys, not Book 0's.** Book 0 cites `openstax_calculus_v1` and `openstax_college_algebra_2e`
with no file, and ten of its records carry no quote; mapping a file to either key would turn the
quote check on for them and block the build (tested: blocking 0 to 10). Book 0 is frozen, so by the
conductor's decision the S02-R1 excerpts are filed under new keys, `openstax_calculus_v1_s02` and
`openstax_college_algebra_2e_7_5` (the section-suffix precedent of `openstax_contemporary_math_7_7`),
both mapped and checked. Book 0's two keys are left exactly as they were, with no file.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `openstax_calculus_v1_s02.txt` | OpenStax *Calculus Volume 1* (CC BY-NC-SA 4.0; web version updated 15 Jul 2026), the S02-R1 excerpt set: sections 1.5, 3.2, 3.3, 3.4, 3.9, 4.3, 4.5, 5.1, 5.2, 5.3, 5.4, 6.8, some subsections omitted (header). **Excerpts.** Key `openstax_calculus_v1_s02` | 35,368 | The number e and properties of logarithms (1.5); higher-order derivatives (3.2); constant, power, sum, difference, constant-multiple and product rules (3.3); amount of change formula and population change (3.4); derivatives of e^x and ln x (3.9); Fermat's theorem and critical points (4.3); concavity and the second derivative test (4.5); sigma notation and Riemann sums (5.1); net signed area and average value (5.2); both parts of the fundamental theorem (5.3); net change theorem (5.4); growth and decay models, doubling time and half-life (6.8). Formulas are flattened; quote prose |
| `openstax_calculus_v2.txt` | OpenStax *Calculus Volume 2* (CC BY-NC-SA 4.0; web version updated 15 Jul 2026), sections 4.1 and 4.2 whole, without exercises | 5,927 | Verifying a solution; general and particular solutions; initial-value problems (4.1); direction fields, equilibrium solutions and their stability, Euler's method and step size (4.2) |
| `openstax_college_algebra_2e_7_5.txt` | OpenStax *College Algebra 2e* (CC BY-NC-SA 4.0; web version updated 12 Jun 2026), section 7.5 only. Key `openstax_college_algebra_2e_7_5` | 4,470 | Dimensions of a matrix, row and column matrices; sum and difference; scalar multiples; the product of two matrices. Matrices are flattened by the extraction |
| `austin_ula.txt` | Austin, *Understanding Linear Algebra* (CC BY 4.0; online edition dated 15 Aug 2026), sections 2.1 and 2.2 without exercises, and the book's TeX macros | 7,734 | Vectors, scalar multiplication, vector addition; linear combination (Definition 2.1.10); matrix-vector multiplication as a linear combination of columns (Definition 2.2.3); linearity (Proposition 2.2.6); matrix-matrix products (Definition 2.2.10). Mathematics is TeX source. The author warns the August 2026 revision may have renumbered subsections |
| `openintro_stats_4e.txt` | Diez, Çetinkaya-Rundel, Barr, *OpenIntro Statistics* 4th ed. (2019; PDF updated 21 Oct 2022), screen-reader PDF text layer. CC BY-SA 3.0 per the publisher's licence page (the PDF itself names no version). **Excerpts** | 6,391 | Section number confirmed: 3.4 "Random variables" (pp. 128-139). The three rules for a probability distribution (3.1.5); random variable, expected value, general variance formula (3.4.1-3.4.2); linear combinations of random variables and their variability (3.4.3-3.4.4); continuous distributions, probability as area (3.5) |
| `chow_hall_2008.txt` | Chow and Hall, *PLoS Comput Biol* 2008;4:e1000045 (PMC2266991), article page. Public domain. **Excerpts; no equation held** | 2,345 | Equation 1 as conservation of energy and Equation 2 as its rate form, in words, with I = dQ/dt, E = dW/dt and ρM the energy density of mass change; ρF = 39.5, ρG = 17.6, ρP = 19.7 MJ/kg; the linearised one-dimensional model; fixed points as where time derivatives are zero, nullclines, stability. **Every equation is an image and none is held** |

Extended the same day: `openstax_intro_stats_2e.txt` (4.1, 4.2 appended), `fao_who_unu_2004.txt`
(block 9, Table 5.2), `thomas_2013_3500kcal.txt` (block 7, the Methods equation) and
`polidori_2016.txt` (blocks 11-13, Equations 1-5); their rows above are updated. `hall_2008_ijo.txt`
is unchanged: its two equations are images and were not obtained as text.

**Follow-up, 2026-09-24 (after the S02-R1 audit).** `polidori_2016.txt` gained blocks 14-17 (β, the UGE
term as energy, Table 1 rows, the fitted kP = 95), cut by script from a fresh TinyFish fetch of the same
XML; whole-file verbatim check **35 of 35**. ICMR-NIN's "Revised Short Summary Report-2024" was looked for
and **not obtained**: https://nin.res.in/RDA_short_Report_2024.html (the "Short Report New" link on
nin.res.in) is a price list for the printed *Short Summary of RDA* (₹150) and links no PDF; guessed PDF
paths on nin.res.in were unreachable; the only copies found are unofficial uploads (Scribd, coaching
slides), not filed. `icmr_nin_2020_brief` stays the held instrument; whether the 2024 summary repeats its
BMR cuts and 1.53 → 1.40 is unchecked. Log in `books/S02-R1/INTAKE.md`.

**Vintage.** OpenStax web versions are revised in place; recheck the "Web Version Last Updated"
line on each details page. *Understanding Linear Algebra* is revised in place too (dated 15 August
2026 when fetched; its numbering may shift). OpenIntro's fourth-edition PDF is dated 21 October
2022; the trigger is a fifth edition. Chow and Hall 2008 is a published article; the trigger is a
correction notice.
