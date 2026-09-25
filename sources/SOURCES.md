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

## Added by the S36-R1 source intake, 2026-09-24

Same method as S02-R1: TinyFish `fetch_content` only, each passage a contiguous slice of the saved
raw result, re-checked as a whitespace-normalised substring of that fetch: **21 of 21**. Log in
`books/S36-R1/INTAKE.md`. Most files hold whole articles as one run, not excerpts.

**Three files are OCR, not text.** Kitzinger 1995, Britten 1995 and Pope & Mays 1995 exist in PMC
only as scanned pages. Europe PMC's PDF of the scans carries an OCR text layer, and that is what the
three files hold. The OCR has dropped nearly every space between words and has visible misreadings,
so a quote must be written unspaced to pass the check, and a person must check each one against the
page image. Passing the machine check proves only that the OCR says it.

**Licences.** DeJonckheere & Vaughn is CC BY-NC 4.0. McMullin is copyright ISTR, shown in PMC under
PMC's time-limited COVID-19 permission, which is not an open licence. The five BMJ articles show no
licence statement on their PMC pages: free to read, short quotation only. ICMR permits
non-commercial use with acknowledgement.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `dejonckheere_vaughn_2019.txt` | DeJonckheere and Vaughn, *Fam Med Community Health* 2019;7:e000057 (PMC6910737), PMC OA XML. CC BY-NC 4.0. **Whole body**, Tables 1-6 as text; Figure 1 (image) and the appendix guide not held | 5,215 | Eleven steps (Table 3); audio-recording suggestions (Table 4); grand tour, core and follow-up questions (Table 5); probing techniques: wait time, echo, verbal agreement, expansion, explanation (Table 6); "start with an easy, context-setting question"; pilot testing the guide; memoing; "prioritising listening over talking". **No sentence saying the participant should do most of the talking** |
| `pope_ziebland_mays_2000.txt` | Pope, Ziebland and Mays, *BMJ* 2000;320:114 (PMC1117368), PMC page. **Whole article** without references. No licence stated | 2,465 | Transcribing one interview "takes several hours and can generate 20-40 pages"; transcripts as raw data; analysis begins during collection; deviant or negative cases; "expressing results in relative frequencies may be misleading"; indexing; constant comparison; framework approach |
| `mays_pope_2000.txt` | Mays and Pope, *BMJ* 2000;320:50 (PMC1117321), PMC page. **Whole article** without references. No licence stated | 2,376 | Triangulation; respondent validation; clear exposition of methods; reflexivity; attention to negative cases ("deviant case analysis"); fair dealing; the box of quality questions ("more than convenience sampling") |
| `green_britten_1998.txt` | Green and Britten, *BMJ* 1998;316:1230 (PMC1112988), PMC page. **Whole article** without references. No licence stated | 1,421 | Qualitative research addresses questions different from clinical epidemiology's; "different research questions require different kinds of research"; generalisability "conceptual rather than numerical"; anecdote against rigorous qualitative research |
| `mcmullin_2023.txt` | McMullin, *Voluntas* 2023;34:140 (PMC8432276), PMC OA XML. PMC COVID-19 permission, **not CC**. **Whole body** without appendix and references | 4,741 | Naturalized against denaturalized transcription; three to eight hours per hour of audio; intelligent verbatim; the framework (before transcribing, whether to transcribe, how, who, writing about it); 41% of *Voluntas* interview papers do not mention transcription. Translation only in passing |
| `icmr_ethical_guidelines_2017.txt` | ICMR *National Ethical Guidelines* 2017, PDF text layer. Non-commercial use with acknowledgement. **Excerpts** | 9,266 | Table 2.1 risk categories ("routine questioning or history taking" as minimal risk); 2.2.2 audio-visual recording of consent "in certain clinical trials as notified by CDSCO"; 3.5.1 authorship of course research (not review); Table 4.2 exemption, expedited, full review; 4.8.3 "A researcher cannot decide" the review category; 5.2 and Box 5.1 essential information; 5.4 documentation; 5.7 waiver; Section 9 whole, including EC permission for audio/video recording |
| `kitzinger_1995.txt` | Kitzinger, *BMJ* 1995;311:299 (PMC2550365). **OCR text layer** of scans, whole article. No licence stated | (OCR, unspaced) | Title and headings located: rationale and uses of focus groups; sampling and group composition; running the groups; analysis and writing up; the sampling-advantages box (people who cannot read or write); seven main aims. Not checked against the page image |
| `britten_1995.txt` | Britten, *BMJ* 1995;311:251 (PMC2550292). **OCR text layer** of scans, whole article. Licence not seen | (OCR, unspaced) | Box 1 types of interviews; Box 2 question types; Box 3 Whyte's directiveness scale; Box 4 control; Box 5 pitfalls; "Researcher as research instrument"; recording interviews. Not checked against the page image |
| `pope_mays_1995.txt` | Pope and Mays, *BMJ* 1995;311:42 (PMC2550091). **OCR text layer** of scans, whole article. No licence stated | (OCR, unspaced) | Box 1 glossary; Box 2 the overstated dichotomy; Box 3 two-stage tonsillectomy investigation. Not checked against the page image |

**Textbook added the same day (S36-R1, second intake).** A research-methods textbook was added so that
derivable records can cite a `textbook` reference. The BMJ methods papers are articles, not textbooks.
Same method: **12 of 12** passages verbatim against the fetch.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `blackstone_2012.txt` | *Principles of Sociological Inquiry: Qualitative and Quantitative Methods* v1.0, Saylor Academy 2012 (Amy Blackstone; the Saylor edition omits her name at her request). CC BY-NC-SA 3.0 (licence page). One page per section, fetched with body scope. **Excerpts: eleven whole sections, exercises omitted** | 28,440 | 1.2 qualitative methods "yield results such as words or pictures", quantitative "can be represented by and condensed into numbers", "complementary rather than competing"; 2.3 inductive and deductive; 3.1 IRBs; 3.2 informed consent, anonymity and confidentiality; 5.2 idiographic and nomothetic; 7.2 purposive, snowball, quota and convenience samples (Table 7.1); 9.1 when to interview; 9.2 interview guide, open-ended and non-leading questions, recording, transcription, open and focused coding (Table 9.1); 9.4 power, location, rapport; 12.1 focus groups (Table 12.1). Figures (the sample consent form and the two interview guides) are images and not held. **Chapter 4 added 2026-09-25 by the S55-R1 intake** (see below) |

**Indian data-protection law added (S36-R1 v1.1, 24-25 September 2026).** For C07, recording and
privacy in an interview. Same method: TinyFish `fetch_content` only, passages cut by script. **4 of
4** runs verbatim against the fetch. India Code was unreachable for the tool; all three are the
Gazette PDFs on meity.gov.in. None states a licence: Government of India legislation, nothing assumed.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `dpdp_act_2023.txt` | Digital Personal Data Protection Act 2023 (Act 22 of 2023), Gazette of 11 August 2023, PDF text layer. **Whole Act as enacted**, not consolidated | 11,243 | s.2 definitions ("Data Fiduciary" (i), "Data Principal" (j), "personal data" (t), "processing" (x), "child" (f)); s.3 application; s.5 notice; s.6 consent and withdrawal; s.8(5) security safeguards, s.8(7) erasure; s.9 children; s.17(2)(b) research, archiving or statistical purposes; s.44(3) amending RTI Act s.8(1)(j) |
| `dpdp_commencement_2025.txt` | MeitY G.S.R. 843(E), 13 November 2025, s.1(2) commencement. **Whole notification**, Hindi and English | 944 | (a) on publication: s.1(2), s.2, ss.18-26, 35, 38-43, s.44(1) and (3); (b) one year from publication: s.6(9), s.27(1)(d); (c) eighteen months: ss.3-5, s.6(1)-(8) and (10), ss.7-17, s.27 except (1)(d), ss.28-34, 36, 37, s.44(2) |
| `dpdp_rules_2025.txt` | DPDP Rules 2025, G.S.R. 846(E), 13 November 2025, PDF text layer. **Whole English text**, Hindi version omitted | 10,906 | rule 1 commencement (rules 1, 2, 17-21 on publication; rule 4 after one year; rules 3, 5-16, 22, 23 after eighteen months); rule 3 notice; rule 6 security safeguards; rule 8 erasure; rule 10 children's verifiable consent; rule 16 research exemption; Second Schedule standards (a)-(h) |


**25 Sep 2026 (S36-R1):** the OCR files `kitzinger_1995`, `britten_1995`, `pope_mays_1995` were checked against PDFs Harsh downloaded from PMC (bmj00603-0031, bmj00602-0049, bmj00599-0046): every quote the book takes from them matches those PDFs' text and page images.


## Added by the S55-R1 source intake, 2026-09-25

Same method as S02-R1 and S36-R1: TinyFish `fetch_content` only, each passage a contiguous slice of
the saved raw result, re-checked as a whitespace-normalised substring of that fetch: **31 of 31**
(25 runs in the twelve new files, 6 in Blackstone chapter 4). Log in `books/S55-R1/INTAKE.md`. Most
files hold whole articles as one run.

**Licences.** Jhangiani and Ratan are CC BY-NC-SA 4.0; Aslam is CC BY 2.0; Ioannidis 2016 and
Golosovsky & Larivière are CC BY 4.0. The CDC pages state no licence; CDC's own reuse page, held in
the file, says most of its web material is public domain, with exceptions for third-party material
and images. Morgan 2018 (EPA author manuscript), Farrugia 2010 and Nowroozzadeh 2019 state no open
licence. Ioannidis 2014 is a Lancet author manuscript, "available for text mining" and fair use only.
**Van Noorden 2017 is all rights reserved**: held for audit quotation only. India Code's terms of use
allow personal, non-commercial use and forbid automated access without permission; see the file
header and the intake log.

**Van Noorden 2017 is a news feature.** Its uncitedness figures come from an analysis Larivière and
Sugimoto ran on Web of Science for the feature. They are not peer-reviewed primary data, and the
file says so. Golosovsky & Larivière's 12% to 70% range is their report of Sugimoto & Larivière
(2018), a book that is not held.

**Farrugia 2010's text layer is damaged.** Spaces fall inside words in the running text ("m edicine",
"FIN E R"). A correctly spelled quotation of the running text will fail the check. Its Boxes 1-3
(FINER, PICOT, tips) are clean.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `blackstone_2012.txt` (extended) | Blackstone 2012, **chapter 4 appended** as blocks 13-18: chapter introduction and 4.1-4.5, each without exercises | +8,169 | 4.1 starting where you already are; 4.2 empirical against ethical questions; 4.4 the five features of a strong research question ("written in the form of a question, clearly focused, beyond yes/no, more than one plausible answer, and consider relationships among concepts") and Table 4.2, sample questions with strengths, weaknesses and alternatives; 4.5 feasibility (identity, access, time and money) and the library |
| `jhangiani_2019_methods.txt` | Jhangiani, Chiang, Cuttler & Leighton, *Research Methods in Psychology* 4e (KPU 2019), CC BY-NC-SA 4.0. **One whole chapter**, "Generating Good Research Questions" (Pressbooks numbers it 9; `READY.md` calls it 2.3) | 1,829 | Empirically testable questions "expressed in terms of a single variable or relationship between variables"; looking at the discussion section of a recent article; causes, effects, types of people, types of situations; interestingness (answer in doubt, fills a gap, practical implications); feasibility (time, money, equipment, skill, access to participants) |
| `cdc_ss1978_lesson1.txt` | CDC, *Principles of Epidemiology in Public Health Practice* 3e (SS1978), Lesson 1 §6 and §7 (archive pages, last reviewed 18 May 2012; book published October 2006, updated November 2011), exercises omitted, with CDC's reuse page. **Excerpts** | 6,442 | §6 time, place and person; §7 the comparison group as the key feature of analytic epidemiology; exposure and health outcome; experimental against observational studies; cohort, case-control and cross-sectional studies, and why the cross-sectional study "usually cannot disentangle risk factors for occurrence of disease (incidence) from risk factors for survival with the disease" |
| `aslam_emmanuel_2010.txt` | Aslam & Emmanuel, *Indian J Sex Transm Dis AIDS* 2010;31:47 (PMC3140151), PMC OA XML, CC BY 2.0. **Whole article** without references | 2,264 | Background and foreground questions; PICO, with Table 1 (PICO and FINER); the otitis media worked example; characteristics of a good research question |
| `morgan_peco_2018.txt` | Morgan, Whaley, Thayer & Schünemann, *Environ Int* 2018;121:1027 (PMC6908441), EPA author manuscript, Europe PMC PDF text layer. No licence stated. **Whole manuscript**; Figure 1 not held | 4,594 | PECO (population, exposure, comparator, outcome) as the exposure analogue of PICO; five scenarios with P/E/C/O examples on hearing impairment; Table 1; "54%" of 313 studies not reporting the four PICO components (their citation) |
| `ratan_2019.txt` | Ratan, Anand & Ratan, *J Indian Assoc Pediatr Surg* 2019;24:15 (PMC6322175), PMC page, CC BY-NC-SA 4.0. **Whole article** without references; Tables 1-2 are images, not held | 2,879 | FINERMAPS, letter by letter; types of research question (existence, description and classification, composition, relationship, comparative, causality); steps to develop a question; research question and study design (incidence leads to a survey, risk factors to case-control or cohort). **No PICO** |
| `ioannidis_2016_useful.txt` | Ioannidis, *PLoS Med* 2016;13:e1002049 (PMC4915619), PMC page, CC BY 4.0. **Whole essay** without references | 3,484 | Summary points; Table 1, the features and questions to ask; problem base; context placement and information gain; pragmatism; patient centeredness; value for money; feasibility; transparency; Table 2's estimates are the author's |
| `ioannidis_2014_waste.txt` | Ioannidis et al., *Lancet* 2014;383:166 (PMC4697939), HHS author manuscript, PMC OA XML. Text mining and fair use only. **Whole body** without references | 5,917 | "Problem 2: poor utility of information"; "Problem 4: insufficient consideration of other evidence"; options for improvement; Panels 1-2 |
| `van_noorden_2017.txt` | Van Noorden, *Nature* 2017;552:162, news feature, publisher PDF text layer. **All rights reserved.** Whole, with its correction | 2,654 | The 1990 *Science* claim (Hamilton) and Pendlebury's 1991 correction as the feature reports them; the Larivière–Sugimoto Web of Science figures; database coverage; uncited is not useless; the correction removing the data link |
| `golosovsky_lariviere_2021.txt` | Golosovsky & Larivière, *Quant Sci Stud* 2021;2:899, Montréal repository copy of the published PDF, CC BY 4.0. **Whole article** to the data statement, references omitted | 5,670 | The uncitedness ratio and its dependence on time since publication; the 12%-70% range attributed to Sugimoto & Larivière 2018; the Poisson model. Equations flattened; figures not held |
| `farrugia_2010.txt` (optional) | Farrugia et al., *Can J Surg* 2010;53:278 (PMC2912019), Europe PMC PDF text layer. No licence. **Whole article**; running text damaged | 3,823 | Box 1 FINER criteria; Box 2 PICOT (T for time); Box 3 tips; research hypothesis and objectives |
| `nowroozzadeh_2019.txt` (optional) | Nowroozzadeh & Salehi-Marzijarani, *J Gen Intern Med* 2019;34:2695 (PMC6854350), Europe PMC PDF text layer. No open licence. **Whole letter** | 1,275 | Web of Science uncitedness in five top general medical journals (anonymised A-E) for 1990, 2000, 2010 and 2015 cohorts; five-year uncitedness falling from 8.3 (1990) to 0.7 (2010) |

**Vintage.** The Pressbooks and Saylor books are revised in place (recheck the page). The CDC lesson is
an archived page (last reviewed 18 May 2012).
The Companies Act s.135 was fetched from India Code and then withdrawn by the conductor: India Code's
Term of Use forbids automated access without written permission. Not held.

### Added 2026-09-25 from PDFs supplied by Harsh

The four **Harsh only** lines in `books/S55-R1/READY.md`. Harsh downloaded them in a browser from
subscription sites. The "raw fetch" is each PDF's own text layer from `pdftotext` (poppler 24.02.0),
saved unchanged outside the repository. The running text comes from the default mode. Patsopoulos
Tables 1–2 and Nicolaisen Tables 1–3 and 6 come from `-layout`, which keeps table rows together. Every
passage is a contiguous slice of that text, re-checked by `verify.py`: **38 of 38** in the four
files (65 of 65 for the whole S55-R1 intake). **Excerpts only**, and every omission is listed in
each header. **None is openly licensed.** Each is held as a subscription copy supplied by Harsh,
for short quotation at audit only; no table or figure is to be reproduced. The Lancet prints carry
Elsevier's site notice, which reserves "text and data mining, AI training, and similar
technologies"; see the intake log. Page chrome from the two browser prints (date line, URL, page
counter, menus, reference link labels) lies outside every run.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `patsopoulos_2005.txt` | Patsopoulos, Analatos & Ioannidis, *JAMA* 2005;293:2362 (PMID 15900006), publisher PDF. "©2005 American Medical Association. All rights reserved." **Excerpts**: opening, abstract, methods, results, Tables 1–2, comment and caveats; figures and references omitted | 2,916 | ISI Science Citation Index (Web of Science); designs found by title words; 2,646 eligible articles from 1991 and 2001; citations to the end of the second year after publication, and totals to 10 December 2004; Table 1 median 2-year citations by design (meta-analysis 5 and 9, RCT 4 and 6, cohort 3 and 5, case-control 3 and 4, case report 0 and 1, nonsystematic review 2 and 4, decision or cost-effectiveness 4 and 4, for 1991 and 2001); share with more than 10 citations in 2 years; self-citations not excluded. **No cross-sectional category** |
| `chalmers_glasziou_2009.txt` | Chalmers & Glasziou, *Lancet* 2009;374:86 (PMID 19525005), browser print of the full-text page. Elsevier site notice, all rights reserved. **Excerpts**: body text and Panel; the figure is an image and is not held | 2,469 | Four stages (questions, design and methods, publication, reports); "the roughly 50% loss at stages 2, 3, and 4 would lead to a greater than 85% loss"; mainly clinical-trial evidence, "reasonable to assume" it applies to other research; 53% of abstracts published in full after 9 years; osteoarthritis priorities (9% of patients wanted drug research, over 80% of trials were drug trials); the Panel's recommendations |
| `chalmers_2014_priorities.txt` | Chalmers, Bracken, Djulbegovic et al., *Lancet* 2014;383:156 (PMID 24411644), browser print. Elsevier site notice, all rights reserved. **Excerpts**; figures and tables not held | 3,878 | Summary and the four recommendations; priority-setting steps (Panel 1); burden-of-disease mismatches; waste when users' needs are ignored; the Figure 2 caption (the figure's counts are an image); users rarely involved in agenda setting; fewer than a quarter of previous trials cited; less than half aware of reviews; closing recommendations with Panel 3 (James Lind Alliance shared priorities) |
| `nicolaisen_frandsen_2019.txt` | Nicolaisen & Frandsen, *Scientometrics* 2019;119:1227 (not in PubMed), publisher PDF. "© Akadémiai Kiadó, Budapest, Hungary 2019"; no licence. **Excerpts**: abstract, introduction, method, results, discussion, Tables 1–3, the Medicine rows of Table 6 | 3,530 | Scopus; publications of 1996–2015; open window to 6 December 2018; seven document types; uncitedness ratio for Medicine 0.23 over all seven types (articles 0.18, reviews 0.18, letters 0.44, notes 0.64); all 27 subject areas (Table 3); ratios by year for Medicine; "uncited" means zero citations in Scopus |

## Added by the S37-R1 intake, 24 September 2026

Transcribed with TinyFish fetch_content only; every passage is a contiguous slice of the saved raw fetch, re-checked by the conductor (314/314). Log: `books/S37-R1/INTAKE.md`.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `hlpe_2017.txt` | HLPE Report 12, *Nutrition and food systems* (CFS HLPE, September 2017), PDF text layer. **Excerpts** | 3,748 | Reproduction statement ("publicly available ... Non-commercial uses will be authorized free of charge, upon request"); Summary para 2 food-system definition and the three constituent elements; paras 3-5 supply chain, food environment, consumer behaviour; paras 22-27 five driver categories; para 28 points for intervention; s.1.1 the definition quoted from HLPE 2014a and the sustainable food system; 1.2 driver lists; 1.2.1 supply-chain steps; Figure 1 caption and labels (layout not recoverable); 1.2.2 Definition 1 food environment, its four components, key elements, footnote 9 food entry points incl. schools, hospital and public canteens; opening paragraph of availability, economic access, promotion, quality and safety |
| `wcrf_nourishing.txt` | WCRF International, NOURISHING framework page and policy-database level-one page | 773 | Framework developed in 2013; three domains (food environment, food system, behaviour change communication); ten policy areas by letter under their domains (N O U R I S under food environment, H under food system, I N G under behaviour change communication). No licence statement on either page |
| `fao_fbs_handbook_2001.txt` | FAO, *Food Balance Sheets: a handbook* (2001), HTML edition. **Excerpts** | 3,245 | Ch.I: supply = production + imports adjusted for stock changes; utilization side; per caput supply; FBS measure supply not consumption; food derived as a residual. Ch.II: 2. stock increase shown "-", decrease "+"; 4. three supply concepts, (c) "Production + imports - exports + changes in stocks (decrease or increase) = supply for domestic utilization", adopted by FAO; 9. waste = storage and transport losses, household waste excluded, post-harvest fruit and vegetable losses 25-40 per cent in many countries; 11. food reaching the consumer; 12. per caput in kg/year, g/day, kcal/day, "1 calorie = 4.19 kilojoules". Ch.IV: IDR = imports / (production + imports - exports) x 100; SSR = production / (same) x 100; not complements. No licence statement on the pages |
| `unep_fwi_2024.txt` | UNEP *Food Waste Index Report 2024* (March 2024), PDF text layer. **Excerpts** | 3,665 | Reproduction for educational or non-profit use permitted with acknowledgement; definitions of food waste, food, edible and inedible parts, food loss ("up to, and excluding, the retail level"); confidence ratings (high, medium, low and very low) defined; Table 3 household 81/88/86 kg by income group; 2022: 1.05 billion t, 132 kg/cap/yr, household 79 kg and 631 Mt (Table 23); India: 7 medium-confidence subnational household datapoints (Table 13; Table 16, seven datapoints from six cities, 20-88 kg); Annex 3 India household 55 kg/capita/year, 78 192 338 t/year, Medium confidence |
| `who_double_duty_2017.txt` | WHO, *Double-duty actions for nutrition: policy brief* (2017, WHO/NMH/NHD/17.2), PDF text layer. Prose nearly whole | 3,160 | CC BY-NC-SA 3.0 IGO; 2014 and 2016 global figures (462 million adults underweight, 1.9 billion overweight or obese, 155 million children stunted, 41 million overweight); the double burden defined at individual, household and population levels; double-duty actions defined; shared drivers (biology, environments, socioeconomics); shared platforms; three levels: do no harm, retrofit, de-novo; five candidates incl. school food policies; Corinna Hawkes lead author. The terms "single-duty" and "working against" are not in it |
| `swinburn_2019_syndemic.txt` | Swinburn et al., The Global Syndemic Lancet Commission, *Lancet* 2019;393:791-846. **Excerpts** | 1,902 | © 2019 Elsevier, all rights reserved; published 27 January 2019; the three pandemics "obesity, undernutrition, and climate change" as The Global Syndemic, "a syndemic, or synergy of epidemics, because they co-occur in time and place, interact with each other to produce complex sequelae, and share common underlying societal drivers"; policy inertia; major driving systems food and agriculture, transportation, urban design, land use; double- or triple-duty actions; original syndemic definition with three characteristics (Introduction); deep drivers |
| `popkin_2012_transition.txt` | Popkin, Adair, Ng, *Nutr Rev* 2012;70:3-21, NIH author manuscript (PMC3257829). **Excerpts** | 1,120 | Text-mining and fair-use statement; abstract (manuscript wording): diets shifting from the 1970s to processed foods, eating away from home, edible oils, sugar-sweetened beverages; Introduction: cheap vegetable oils; "a dramatic shift in stages"; nearly 1.5 billion overweight or obese adults in 2008; projection 2.16 billion overweight and 1.12 billion obese by 2030; India named for diabetes and impaired fasting glucose. No numbered stages or patterns |
| `nfhs5_india_factsheet.txt` | NFHS-5 (2019-21) India Fact Sheet, IIPS and MoHFW (DHS Program copy). **Excerpts** | 992 | Fieldwork 17 June 2019 to 30 April 2021; 636,699 households; indicators 81-98, NFHS-5 total (NFHS-4 total): stunted 35.5 (38.4), wasted 19.3 (21.0), severely wasted 7.7 (7.5), underweight 32.1 (35.8), child overweight 3.4 (2.1); women BMI <18.5 18.7 (22.9), men 16.2 (20.2); women overweight or obese 24.0 (20.6), men 22.9 (18.9); anaemia children 6-59 months 67.1 (58.6), all women 15-49 57.0 (53.1), men 15-49 25.0 (22.7); footnotes 18-22 define the SD and haemoglobin cut-offs. No licence statement |
| `pib_2082323.txt` | PIB release 2082323, 6 Dec 2024, PM POSHAN (Lok Sabha reply). Whole text | 878 | PM POSHAN approved 2021-22 to 2025-26 for hot cooked meal in Government and Government-aided schools; Balvatika inclusion; Tithi Bhojan, nutrition gardens, social audit, "vocal for local" menus within the nutrition and food norms; responsibility lies with States/UTs. No beneficiary or tonnage figures |
| `pib_2251769.txt` | PIB backgrounder 2251769, 14 Apr 2026, Mission Poshan 2.0. Whole text | 3,613 | ICDS launched 1975; POSHAN Abhiyaan launched 8 Mar 2018; Mission Poshan 2.0 subsumed Anganwadi Services, Scheme for Adolescent Girls, POSHAN Abhiyaan; supplementary nutrition per NFSA Schedule II, norms "revised in January 2023" (numbers not given); as on March 2026 14,03,170 AWCs and 8,95,29,425 beneficiaries tracked; 2 lakh AWCs sanctioned for Saksham upgradation; Poshan Maah 2025 theme included reducing sugar and oil to address obesity |
| `pib_1980689.txt` | PIB release 1980689, 29 Nov 2023, PMGKAY Cabinet decision. Whole text | 1,017 | Free foodgrains to about 81.35 crore beneficiaries for five years from 1 Jan 2024; about Rs 11.80 lakh crore; over 5 lakh Fair Price Shops; ONORC portability; economic cost of 35 kg rice Rs 1371 and 35 kg wheat Rs 946 |
| `pib_1847548.txt` | PIB release 1847548, 2 Aug 2022, Saksham Anganwadi and Poshan 2.0 guidelines issued. Whole text | 626 | Scheme period 2021-22 to 2025-26; SNP for children 6 months-6 years, PWLM, adolescent girls 14-18 in Aspirational Districts and NER; the four verticals and objectives |
| `s37_pib_1812421.txt` | PIB release 1812421, 1 Apr 2022, PM POSHAN (Lok Sabha reply). Whole text; stands in for the PM POSHAN guidelines, which could not be fetched | 1,144 | Nutrition norm per child per day 450 kcal/12 g protein (primary), 700 kcal/20 g (upper primary); food norms 100/150 g foodgrains, 20/30 g pulses, 50/75 g vegetables, 5/7.5 g oil and fat; 11.80 crore children in 11.20 lakh schools; BE 2021-22 Rs 11,500 crore, RE Rs 10,233.75 crore; POSHAN Abhiyaan targets |
| `poshan2_guidelines_2022.txt` | MoWCD, Mission Saksham Anganwadi and Poshan 2.0 Scheme Guidelines (2022). **Excerpts** | 2,773 | Issued under NFSA ss. 4(a), 5(1)(a), 6, 7; funding pattern (general 60:40, SN 50:50 for States with legislature; 90:10 NE/Himalayan; 100:0 UTs without legislature); SN at 14 lakh AWCs, minimum 300 days a year; THR for PW&LM, children 6-36 months, SAM children, adolescent girls; HCM and morning snacks for 3-6 years; norms per beneficiary per day: children 500 kcal/12-15 g, SAM 800/20-25, PW&NM 600/18-20, AG 600/18-20 ("under revision"); cost Rs 8.00/12.00/9.50/9.50; THR not raw ration; jaggery not white sugar; millets at least once a week |
| `ifct_2017.txt` | ICMR-NIN, Indian Food Composition Tables 2017 (Longvah et al.). **Excerpts** | 1,706 | Energy in kJ on the Atwater basis, 1 kcal = 4.18 kJ; Table 4 factors 17/37/17/8/29 kJ per g; Table 1 per 100 g: rice raw milled protein 7.94 g, energy 1491 kJ; atta 10.57, 1340; whole wheat 10.59, 1347; red gram dal 21.70, 1384; Bengal gram dal 21.55, 1377; jowar 9.97, 1398; bajra 10.96, 1456; ragi 7.16, 1342 (all cereals A001-A024, legumes B001-B022) |
| `dfpd_pds.txt` | DFPD Annual Report 2025-26. **Excerpts** | 3,324 | Food Department 1942; FCI set up 1965 under the Food Corporations Act 1964; PDS from the 1960s; TPDS from June 1997; AAY from Dec 2000, ceiling 2.5 crore households; NFSA in force 5 Jul 2013, 75%/50% coverage, 35 kg/AAY household, 5 kg/PHH person; about 20.5 crore ration cards, 5.51 lakh FPSs; 2025-26 allocation 595.05 lakh MT (table grand total 607.40), TPDS 554.11, PM POSHAN 22.31, WBNP 23.05; PM POSHAN and WBNP allocation/offtake 2022-23 to 2025-26; DCP subsidy = economic cost minus CIP; food subsidy released 2021-22 to 2025-26 (Rs 1,99,500 crore in 2024-25) |
| `pib_2260617.txt` | PIB 2260617, Cabinet approves kharif MSP for KMS 2026-27 (13 May 2026), whole release | 1,078 | 14 kharif crops' MSP, cost and margin for 2026-27 with 2025-26 and 2013-14 comparisons (paddy common 2441, cost 1627, 50%); cost definition footnote; "at least 1.5 times of the All-India weighted average cost of production"; paddy procurement 8418 LMT (2014-15 to 2025-26) vs 4590 LMT (2004-05 to 2013-14) |
| `pib_rabi_msp.txt` | PIB PRID 2173567, Cabinet approves rabi MSP for RMS 2026-27 (1 Oct 2025), whole release | 749 | Wheat MSP 2585, cost 1239, margin 109%, previous 2425; barley, gram, lentil, rapeseed-mustard, safflower rows; the 1.5 times rule |
| `pib_sugarcane_frp.txt` | PIB 2258113, sugarcane FRP for sugar season 2026-27 (5 May 2026), whole release | 710 | FRP Rs 365/qtl at 10.25% basic recovery, premium/reduction Rs 3.56 per 0.1%; Rs 338.3 floor below 9.5%; cost A2+FL Rs 182/qtl, FRP 100.5% above it; 2.81% above 2025-26; set on CACP recommendation; applicable from 1 Oct 2026 |
| `s37_pib_msp_backgrounder.txt` | PIB backgrounder 155448, "Minimum Support Prices: From Safety Net to Self-Sufficiency" (10 Oct 2025), nearly whole | 2,703 | MSP for 22 mandated crops on CACP recommendation; factors CACP considers incl. a minimum 50% margin; cost concept; 1.5 times since 2018-19; RMS 2026-27 and KMS 2025-26 MSP tables; cereals procured by FCI and state agencies, pulses/oilseeds under PM-AASHA via NAFED/NCCF, cotton and jute via CCI/JCI; foodgrain procurement 761.40 LMT (2014-15) to 1,175 LMT (2024-25). Does not give CACP's founding year |
| `fci_about.txt` | FCI "About us" paragraph as served (Hindi only) | 408 | FCI set up under the Food Corporations Act 1964 for price support operations, PDS distribution, and operational and buffer stocks (Hindi text; gloss in a [NOTE] only) |
| `s37_edible_oil_duty.txt` | PIB 2314297 (24 Sep 2026) and 2135774 (11 Jun 2025) on BCD on crude edible oils, both whole | 1,432 | From 24 Sep 2026 BCD on crude sunflower oil Nil, on crude soybean and crude palm oil 5% (from 10%), 19.25% crude-refined differential; in June 2025 BCD cut from 20% to 10%; import duty as a component of landed cost |
| `s37_economic_cost_grain.txt` | DFPD Foodgrains Bulletin Dec 2025 (PDF text) excerpts + DFPD Year End Review 2025 (PIB 2210211) excerpts | 2,269 | Definitions of acquisition, distribution and economic cost and CIP; economic cost 2025-26 (BE) rice Rs 4173.34, wheat Rs 2980.06 per quintal, with pool cost, procurement incidental and distribution cost; 2024-25 (RE) 4042.15 / 2850.19; CIP zero for NFSA since 1 Jan 2023; Tide Over CIP 830/610; subsidy 100% of economic cost; earlier NFSA prices Rs 3/2/1 per kg; RMS 2025-26 wheat procurement 300.35 LMT; wheat stock limits of 27 May 2025 (traders 2000 MT, retailers 8 MT) |
| `pib_2061646.txt` | PIB 2061646, Cabinet approves NMEO-Oilseeds 2024-25 to 2030-31 (3 Oct 2024), whole release | 975 | Outlay Rs 10,103 crore; primary oilseeds 39 Mt (2022-23) to 69.7 Mt by 2030-31; edible oil 25.45 Mt meeting about 72% of requirement; imports "57% of its domestic demand"; NMEO-OP Rs 11,040 crore (2021); "20% import duty on edible oils" as of Oct 2024 |
| `pib_2200287.txt` | PIB backgrounder 2200287, National Mission on Edible Oils (8 Dec 2025), whole | 3,484 | Production 12.18 Mt and imports 15.66 Mt (2023-24), domestic production meets 44% of demand; import dependence 63.2% (2015-16) to 56.25% (2023-24); per capita consumption 10.58 kg rural, 11.78 kg urban (2022-23); NMEO-OP targets and viability price; oil palm 6.20 lakh ha; NMEO-OS targets; duties as then stated |
| `pib_millets.txt` | PIB backgrounder "Shree Anna for Shreshta Bharat" (8 Aug 2025, PDF text) excerpts + PIB 2290630 (28 Jul 2026) millet bullets | 2,163 | UN International Year of Millets 2023 at India's request; India 38.4% of global production; 180.15 lakh t in 2024-25; Nutri-Cereals sub-mission of NFSM (28 States, 2 UTs); PM-RKVY; PLISMBP Rs 800 crore; millets in PDS in place of wheat or rice on a state's request; exports 89,164.96 t (2024-25); 2026 reply: "special thrust" to millets through NFSNM |
| `rbi_wp_2024_08_tops.txt` | RBI Working Paper **08**/2024 (not 06), *Vegetables Inflation in India: tomato, onion, potato*, RBI HTML text. **Excerpts** | 2,865 | Abstract: farmers' share "around 33 per cent for tomato, 36 per cent for onion and 37 per cent for potato"; food 45.9 per cent of the CPI basket; APMCs fix mandi fees and commission charges; tomato 33.5 per cent (traders' mark-up 21.3, traders' margin 5.3); onion 36.2 per cent, traders 17.6, wholesalers 15.0, retailer 31.3, mandi fee 1 per cent and commission 4 per cent; potato 36.7 per cent, cold storage and commission agents at primary and secondary mandis; tomato Table 1 of production and consumption centres |
| `rbi_wp_2024_07_pulses.txt` | RBI Working Paper 07/2024, *Pulses Inflation in India: gram, tur, moong*, RBI HTML text. **Excerpts** | 1,526 | Farmers' share gram ~75, moong ~70, tur ~65 per cent; institutional (NAFED) and non-institutional channels (traders, wholesalers, commission agents, millers, retailers); Table 2 whole: mandi price Rs 53/72/77 per kg against DoCA retail Rs 71/111/110 (May 2023), market fee 0.8-1.5 per cent and arthia commission 2 per cent, retailer mark-up 8/14/14 per cent |
| `rbi_wp_2024_fruits.txt` | RBI Working Paper 06/2024, *Price Dynamics and Value Chain of Fruits: grapes, bananas, mangoes*, RBI HTML text. **Excerpts** | 1,832 | Abstract: bananas 31, grapes 35, mangoes 43 per cent; grapes ~35 per cent domestic vs 21 per cent export; banana 30.8 per cent (Jalgaon to Delhi); mango Table 7 (farmgate Rs 62-67/kg, 42-43 per cent; retailer 27 per cent; retail Rs 149-155, April 2021); mango-pulp Table 8 (46-47 per cent) |
| `rbi_wp_2024_poultry.txt` | RBI Working Paper 05/2024, *Livestock and Poultry Inflation in India: milk, poultry meat, eggs*, RBI HTML text. **Excerpts** | 1,590 | Milk 70, eggs 75 per cent, poultry meat 56 per cent to farmers and integrators; Table 2 milk mark-ups (three dairies, Dec 2022 / Mar 2023, 69-71 per cent to farmers); Table 3 poultry bird Rs 100 farm gate vs Rs 180 retail (55.5 per cent), eggs 69 per cent (Delhi, Apr 2021) and 89 per cent (Pune, Dec 2022); egg three-year average 75.2 per cent |
| `pib_2151371.txt` | PIB release 2151371, 1 Aug 2025, MoFPI Rajya Sabha reply on the NABCONS post-harvest loss study (reference 2020-22, 54 crops). **Whole release** | 1,702 | Study commissioned 2022 with reference year 2020-22; stages assessed; Annexure-I production in '000 MT 2020-21 to 2024-25; Table-1 quantity lost (million MT): cereals 12.49, pulses 1.37, oilseeds 2.11, fruits 7.36, vegetables 11.97, plantation crops 30.59, livestock produce 3.01 (eggs row 7363.00, unit not stated); Table-2 % loss farm/market, e.g. paddy 4.16/0.61, wheat 3.61/0.56, tomato 8.37/3.25, guava 11.59/3.46, milk 0.54/0.33 |
| `pib_2097601.txt` | PIB release 2097601, 30 Jan 2025, MoSPI, HCES 2023-24. **Whole release** | 2,614 | MPCE Rs 4,122 rural and Rs 6,996 urban (2023-24), Rs 3,773 and 6,459 (2022-23); food about 47 per cent rural and 40 per cent urban of MPCE in 2023-24; beverages, refreshments and processed food 9.84 rural and 11.09 urban; milk 8.44/7.19; vegetables 6.03/4.12; cereals and cereal substitutes about 4.99 rural; Gini 0.237 rural, 0.284 urban; Tables 1-7 |
| `hces_2023_24_press_note.txt` | MoSPI press note, HCES 2023-24, 27 Dec 2024 (PDF text layer). **Excerpts** | 1,986 | Non-food 53 per cent rural and 60 per cent urban of MPCE; Table 1 MPCE incl. 2011-12 (Rs 1,430 / 2,630); Figures 4 and 5 data labels: eight food groups' share of MPCE, rural and urban, 2022-23 and 2023-24 (e.g. cereals 4.91 to 4.99 rural, 3.62 to 3.76 urban) |
| `hces_2022_23_factsheet.txt` | MoSPI Fact Sheet, HCES 2022-23 (PDF text layer). **Excerpts** | 1,766 | 2,61,746 households surveyed; Statement 1 food share 46 rural, 39 urban; Statement 3 cereals' share of MPCE 22.23 (1999-00) to 4.91 (2022-23) rural, 12.39 to 3.64 urban; food share 59.40 to 46.38 rural, 48.06 to 39.17 urban; Statement 5 fifteen item groups, Rs and %; Statements 6 and 7 item-group composition 1999-00, 2004-05, 2009-10, 2011-12, 2022-23 (beverages and processed food 4.19 to 9.62 rural, 6.35 to 10.64 urban) |
| `econ_survey_tab_1_19.txt` | Economic Survey 2025-26, Statistical Appendix Table 1.19, per capita net availability of foodgrains (PDF text layer). **Whole table** | 829 | 2020-21 to 2022-23: foodgrains 511.7, 514.6, 568.8 g/day; cereals 521.7 and pulses 47.1 g/day in 2022-23; production, net imports, change in stocks, net availability; definition of net availability (gross production minus seed, feed and wastage, minus exports plus imports, minus change in stocks), divided by population and 365; financial-year series not comparable with the old calendar-year one; "not strictly representative of actual level of consumption" |
| `enam_about.txt` | e-NAM portal pages: FAQs, APMCs, Farmers, Traders, Mandi Board. **Excerpts** | 1,229 | e-NAM "not a parallel marketing structure" but a network of physical mandis; three APMC-Act reforms (unified licence, single-point levy, e-auction); APMC and APMC yard defined; 1522 markets, 23 states and 4 UTs; SFAC lead agency; 27 mandi boards. Commission agents not described |
| `openstax_prealgebra_2e_ch6.txt` | OpenStax Prealgebra 2e (CC BY-NC-SA 4.0), chapter 6 sections 6.1-6.3, each without its exercise set, plus the details page (added 25 Sep 2026). **Excerpts** | 8,397 | 6.1 "A percent is a ratio whose denominator is 100"; converting percents to decimals and back; 6.2 the tip example naming the base ("we multiplied the percent by the base"), percent of, base-finding and what-percent equations, percent increase and decrease each "of the original amount"; 6.3 sales tax as a percent of the purchase price added to it, "convert the sales tax rate from a percent to a decimal number", commission, discount off the original price, mark-up "usually calculated as a percent of the wholesale price", list price = wholesale price + mark-up; details page: published 11 Mar 2020, web version 29 Jun 2026, licence line |
