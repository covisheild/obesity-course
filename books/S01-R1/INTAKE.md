# Source intake log · S01-R1

One pass, 2026-09-23, before drafting. Tool for every stored passage: `mcp__TinyFish__fetch_content`.
Its result was saved by the harness to a file, decoded from JSON unchanged, and every passage was cut
from that text by script (`raw[i:j]`). The written files were then re-parsed and each passage tested
as a whitespace-normalised substring of the raw fetch. An omission inside a paragraph is marked
`[...]` in place, and the builder adds the mark automatically wherever text is left on the same line.
Identifiers were confirmed with the PubMed tools (`lookup_article_by_citation`, `search_articles`,
`get_article_metadata`). No WebFetch output is stored anywhere.

**Verbatim check: 146 of 146** (102 in the first pass, 16 for Hall 2012 in the second, 17 for Hall 2008 from Harsh's PDF, 11 added after the C09/C10 audit).

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Hall et al. 2011 *Lancet* | https://pmc-oa-opendata.s3.amazonaws.com/PMC3880593.1/PMC3880593.1.txt | 9 | 9/9 | "available for text mining ... fair use" (NIH author manuscript) | `hall_2011_lancet` |
| Hall & Guo 2017 *Gastroenterology* | …/PMC5568065.1/PMC5568065.1.txt | 15 | 15/15 | same | `hall_guo_2017` |
| Thomas et al. 2013 *Int J Obes* | …/PMC4024447.1/PMC4024447.1.txt | 8 | 8/8 | same | `thomas_2013_3500kcal` |
| Rosenbaum & Leibel 2010 *Int J Obes* | …/PMC3673773.1/PMC3673773.1.txt | 4 | 4/4 | same | `rosenbaum_leibel_2010` |
| Polidori et al. 2016 *Obesity* | …/PMC5108589.1/PMC5108589.1.txt | 6 | 6/6 | same | `polidori_2016` |
| Hall 2008 *Int J Obes* (PDF supplied by Harsh) | Author-manuscript PDF NIHMS47767, text layer by `pdftotext` (reading order), raw extraction saved in scratch and sliced by script | 17 | 17/17 | the PDF states none; headed "NIH Public Access / Author Manuscript" | `hall_2008_ijo` |
| Hall et al. 2012 *AJCN* (second attempt) | https://europepmc.org/articles/PMC3302369?pdf=render (redirects to europepmc.org/api/getPdf?pmcid=PMC3302369); publisher PDF text layer | 16 | 16/16 | "© 2012 American Society for Nutrition" (printed as "/C2112012"); free to read, not licensed | `hall_2012_ajcn` |
| FAO/WHO/UNU 2004 | https://www.fao.org/4/y5686e/y5686e00.htm, y5686e04.htm, y5686e07.htm | 25 | 25/25 | "All rights reserved"; non-commercial educational reproduction authorised with acknowledgement | `fao_who_unu_2004` |
| BIPM SI prefixes | https://www.bipm.org/en/measurement-units/si-prefixes | 2 | 2/2 | none in the page text | `bipm_si_prefixes` |
| NIST SP 811 B.8 + footnotes | https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8 and …/nist-guide-si-footnotes | 5 | 5/5 | none in the page text | `nist_sp811_pound` |
| FTC *Gut Check* 2014 | https://www.ftc.gov/business-guidance/resources/gut-check-reference-guide-media-spotting-false-weight-loss-claims | 11 | 11/11 | none in the page text | `ftc_gut_check_2014` |
| ICMR-NIN 2020 *Brief Note* (PDF text layer) | https://www.nin.res.in/rdabook/brief_note.pdf | 7 | 7/7 | none in the PDF text; NIN site footer: "© 2018, All Rights Reserved" | `icmr_nin_2020_brief` |
| MoSPI NSS Report 594 (PDF text layer) | https://www.mospi.gov.in/sites/default/files/publication_reports/Nutritional_Intake_in_India_L.pdf | 10 | 10/10 | none in the PDF text | `nss_594_2025` |

## Not obtained

| Source | Why | Where Harsh can get it |
| --- | --- | --- |
| ICMR-NIN 2020 full report | Sold in print only (Rs 400) | https://www.nin.res.in/RDA_Full_Report_2024.html |
| NSS Report 560 (2011-12) | Not attempted after the successor, Report 594, was found; its Table 3.14 gives the 2011-12 figures | https://mospi.gov.in/ (publications, NSS reports), if 560 itself is wanted |

## Caveats found during intake

- **The five papers are NIH author manuscripts**, not the typeset articles. The wording can differ slightly
  from the journal version. None is open-licensed.
- **READY.md had two wrong PMCIDs.** Thomas 2013 is PMC4024447 (PMC3859816 is Hall and Chow 2013). Polidori 2016
  is PMC5108589. READY.md's author list for Thomas 2013 was also wrong; corrected there.
- **Hall 2011 does not give "24 kcal/day per kg"**. It gives 100 kJ per day per kg, and 10 kcal per day per
  pound. **It does not give adipose tissue's per-kg energy** (the ~7,700 kcal/kg in C02); it gives body fat
  39·5 MJ/kg and lean 7·6 MJ/kg. The adipose figure needs Hall 2008.
- **Thomas 2013 names Wishnofsky 1958 as the rule's source** but does not say how it was derived.
- **Hall 2011's glycogen paragraph** says stored glycogen carries intracellular water and weight changes with
  diet composition. None of the held files states that *early* weight loss is mostly glycogen and water, which
  C08 wants. That is Hall 2008.
- **ICMR-NIN brief note** says BMR is "measured directly (using DLW or HRM methods)". That is wrong (those measure
  total expenditure); flagged in the file header.
- **NSS 594 energy figures** come from household consumption converted with a nutrient table revised in 2025.
  They are not measured individual intake, and the change of table affects the comparison with 2011-12.
- **FTC example ads are the FTC's own illustrations** (for example "FatFoe"). They are not a real published claim,
  so C08's "real claim" is still Harsh's decision.
- **BIPM exponents** come through without superscript ("106" means 10^6); flagged in the header.
- The NIST footnote identified as footnote 22 is identified **by its position on the page**, because the page
  prints no footnote numbers.

## Second attempt, 2026-09-23

Routes tried for the two missing papers: OpenAlex and Semantic Scholar open-access locations (Hall 2008:
only PMC; Hall 2012: PMC and an OUP PDF, which is unreachable); S3 prefix listings of `pmc-oa-opendata`
(neither PMCID present); Europe PMC abstract, render, getPdf, ptpmcrender and fulltextRepo routes; the
NIHMS47767 route on PMC; academic.oup.com article-lookup (bot-blocked). **Hall 2012 obtained** through
Europe PMC's PDF render (publisher version). **Hall 2008 not obtained.** The coordinator's DOI for Hall
2012 (10.3945/ajcn.111.028977) returns 404 at OpenAlex; the PubMed-confirmed DOI is 10.3945/ajcn.112.036350.

Hall 2012 caveats: a consensus statement funded by the ASN and ILSI North America, not editorially peer
reviewed by the journal (its own footnotes); the text layer keeps line-end hyphens and ligatures, so quotes
must copy them as they stand in the file.

## Harsh's PDFs, 2026-09-23

- **Hall 2008**: filed from the author-manuscript PDF he supplied (not a TinyFish fetch, since no session route
  reached it). Text via `pdftotext`; the layout mode was rejected because it put the margin watermark inside
  paragraphs. PMID, PMCID and DOI confirmed via PubMed. The paper's two equations are images and absent. It gives
  no adipose lipid fraction of its own (only the 87% the rule assumes), and does not say early loss is mostly
  glycogen and water. It prints "32.2 kJ/kg" once for MJ/kg.
- **Hall 2012**: Harsh's PDF is the same typeset publisher version as the filed copy; all 16 filed passages agree
  with its text layer once ligatures, hyphenation, spacing and punctuation are set aside. Noted in the file header;
  not re-filed.

## Extension after the C09/C10 audit, 2026-09-23

The auditor read Polidori 2016 in full on PMC and relied on passages the held file lacked. All came from the
same saved raw fetch (PMC Article Dataset text), sliced by script and re-verified.

| File | Passages added | Check | What they carry |
| --- | --- | --- | --- |
| `polidori_2016.txt` | 9 | 15/15 (file) | Methods inputs and measurement interval; trial weight "several kilograms lower" and ~350 kcal/day; commercial-programme plateau (Figure 3, not the trial); range of weight losses and individual variability; expenditure not measured; group means only; reference 1 (Leibel et al. 1995, source of the ~30 kcal/kg/day) |
| `rosenbaum_leibel_2010.txt` | 1 | 5/5 (file) | 80%-90% regain; maintainers need lifelong attention |
| `hall_guo_2017.txt` | 1 | 16/16 (file) | Individual variation in weight change under supervised exercise |

Caveats: the Methods clause gives "T = 52 was the number of days between measurements" after a formula the
extraction flattened; check the typeset article before telling a reader the interval. The "~8 month plateau"
and "~5 kg" passage is about a commercial weight-loss programme (reference 19), not the canagliflozin trial.
Polidori does not give the trial's mean loss as a number beyond "several kilograms lower".
