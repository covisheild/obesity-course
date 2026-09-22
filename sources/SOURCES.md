# What is in `sources/`, and what has been checked in it

Every file here was downloaded from India Code and read. The "verified" column lists the
provisions actually located in the text, not the provisions the file is assumed to contain.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `fss_act_2006.txt` | Food Safety and Standards Act 2006 (Act 34 of 2006), enacted 23 Aug 2006 | 24,104 | s.4 establishes FSSAI; s.23(1) packaged food must be labelled "in the manner as may be specified by regulations"; s.92 power to make regulations; s.93 regulations laid before Parliament |
| `constitution_current.txt` | Constitution of India, consolidated 2026 text (handle 123456789/618394) | 135,907 | Articles 21, 32, 47, 53, 79, 226, 245, 246, 279A |
| `constitution.txt` | **Do not cite.** An older India Code consolidation, latest amendment 2003 | 89,103 | Contains no Article 279A. Kept only because it is the worked example in Book 0 F3 |
| `nfsa_2013.txt` | National Food Security Act 2013 (Act 20 of 2013), 10 Sep 2013 | 7,679 | s.5, mid-day meal entitlement |
| `consumer_prot_2019.txt` | Consumer Protection Act 2019 (Act 35 of 2019), 9 Aug 2019 | 21,568 | Chapter III s.10, the Central Consumer Protection Authority |
| `bipm_si.txt` | BIPM's statement of the SI definition, in force from 20 May 2019 | 407 | The seven defining constants with their exact values; the relations Hz = s-1, J = kg m2 s-2 |
| `nist_sp811.txt` | NIST Guide to the SI, footnotes; page updated 18 Aug 2025 | 394 | calth = 4.184 J exactly; International Table calorie = 4.1868 J; the kilocalorie as the food-energy unit |
| `openstax_chemistry_2e.txt` | OpenStax Chemistry 2e (CC BY), verbatim excerpts from seven sections. **Excerpts, not the whole book** | 6,268 | 2.3 atom diameter 10-10 m vs nucleus 10-15 m, proton/neutron/electron masses and charges, amu; 2.4 molecular and empirical formula, the parenthetical definition of a chemical bond, diatomic molecules; 7.2 ionic vs covalent bonding, pure vs polar covalent, electronegativity; 7.5 bond energy, D(H-H) = 436 kJ, the HCl arithmetic -185 kJ, exothermic/endothermic in terms of bond strengths; 5.1 energy, heat, work, first law, heat capacity, specific heat and q = c x m x DeltaT, water 4.184 J/g degC, the Calorie; 5.2 calorimetry, system and surroundings, the bomb calorimeter and its benzoic-acid calibration, the nutritional-Calorie feature with 4/4/9 Cal per gram and the Atwater system; 5.3 enthalpy, standard enthalpy of combustion, Table 5.2 values |
| `openstax_biology_2e.txt` | OpenStax Biology 2e (CC BY), verbatim excerpts from nine sections. **Excerpts, not the whole book** | 5,106 | 4.1 the unified cell theory; 4.3 plasma membrane, cytoplasm, nucleus, mitochondria, ribosomes; 5.1 the fluid mosaic model, phospholipid head and tail, the bilayer; 5.3 active transport and its energy cost; 3.4 amino acids as monomers, shape determines function, denaturation, enzyme and substrate; 9.1 ligand, receptor, conformational change on binding, internal vs cell-surface receptors; 14.2 nucleotides, the four bases, the double helix, complementary pairing, antiparallel strands; 12.2 alleles, dominant and recessive, genotype and phenotype, the 3:1 ratio; 7.1 ATP as the cell's energy currency and its hydrolysis to ADP |
| `openstax_anatphys_2e.txt` | OpenStax Anatomy and Physiology 2e (CC BY), verbatim excerpts from ten sections. **Excerpts, not the whole book** | 6,745 | 24.1 metabolism, anabolism, catabolism, and the energy-balance statement; 24.2 glycolysis and the ATP yield; 24.3 triglyceride storage in adipose tissue and its release; 24.4 protein metabolism and the essential amino acids; 24.6 core temperature, the four heat-exchange routes, metabolic rate and BMR; 24.7 the nutritional Calorie, and the BMI cut-points; 23.7 what the small intestine absorbs and what it does not; 23.6 the liver, pancreas and gallbladder; 17.9 alpha and beta cells, insulin and glucagon; 17.1 how fast different hormones act |
| `openstax_college_physics_2e.txt` | OpenStax College Physics 2e (CC BY), verbatim excerpts from eight sections, plus a labelled block from University Physics. **Excerpts, not the whole book** | 3,896 | 7.1 the joule as the unit of work and energy; 7.6 the law of conservation of energy and the forms energy takes, including chemical; 14.1 heat against temperature and the SI unit of heat; 14.2 specific heat, Q = mc(Delta)T, and Table 14.1's water row 4186; 14.4 conduction, convection and radiation defined together; 14.5, 14.6, 14.7 each method in turn |
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
| `constitution.txt` | Latest amendment 2003 | **Do not cite**, per the row above |
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
