# Source intake log · S02-R1

One pass, 2026-09-24, before drafting, against the eleven "To obtain" lines in `READY.md`. Tool for every stored
passage: `mcp__TinyFish__fetch_content`. Its result was saved by the harness to a file, decoded from JSON unchanged,
and every passage was cut from that text by script (`raw[i:j]`). The written files were then re-parsed and each
passage tested as a whitespace-normalised substring of the raw fetch for the URL in its block heading. An omission is
marked `[...]` in place, with a `[NOTE]` saying what was left out. Textbook sections are stored as runs of whole
subsections (definitions, rules, theorems, worked examples and Try It items), with exercise sets left out. No
WebFetch output is stored anywhere; nothing was fetched with curl, wget or a Python HTTP client. Chow and Hall 2008's
identifiers were confirmed with the PubMed tool (`get_article_metadata`).

**Verbatim check: 63 of 63** (textbooks 35, papers and reports 28). A textbook "passage" here is one run between two
`[...]` marks, so most are whole subsections, several thousand words long.

**Equations.** Six equations were obtained as text, all from MathML in a paper's JATS XML (Thomas 2013: 1;
Polidori 2016: Equations 1-5). Each is stored as the MathML itself, verbatim (it passes the check above), followed by a
`[NOTE]` plain-text rendering made by a deterministic script: `mi`/`mn`/`mo` written as they stand, `msub` as
`base_sub`, `msup` as `base^sup`, `mfrac` as `(numerator/denominator)`, `munderover` on an integral sign as
`∫_lower^upper`. No model read an equation. The rendering is labelled as the file's notation, not the source's. The
MathML came from a second fetch of the same XML in TinyFish's `html` format, because the default markdown format
strips the tags and flattens the equation to a run of characters. No equation was taken from an image.

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| OpenStax *Calculus Volume 1*, §1.5, 3.2, 3.3, 3.4, 3.9, 4.3, 4.5, 5.1, 5.2, 5.3, 5.4, 6.8 | https://openstax.org/books/calculus-volume-1/pages/<section-slug>, twelve pages | 13 | 13/13 | "by OpenStax is licensed under Creative Commons Attribution-NonCommercial-ShareAlike License v4.0" (details page) | `openstax_calculus_v1_s02` (new; file `openstax_calculus_v1_s02.txt`) |
| OpenStax *Calculus Volume 2*, §4.1, 4.2 | https://openstax.org/books/calculus-volume-2/pages/4-1-basics-of-differential-equations and …/4-2-direction-fields-and-numerical-methods | 2 | 2/2 | "Calculus Volumes 1, 2, and 3 are licensed under an Attribution-NonCommercial-Sharealike 4.0 International License (CC BY-NC-SA)" (details page) | `openstax_calculus_v2` (new) |
| OpenStax *College Algebra 2e*, §7.5 | https://openstax.org/books/college-algebra-2e/pages/7-5-matrices-and-matrix-operations | 1 | 1/1 | "by OpenStax is licensed under Creative Commons Attribution-NonCommercial-ShareAlike License v4.0" (details page) | `openstax_college_algebra_2e_7_5` (new; file `openstax_college_algebra_2e_7_5.txt`) |
| Austin, *Understanding Linear Algebra*, §2.1, 2.2, and the TeX macros | https://understandinglinearalgebra.org/sec-vectors-lin-combs.html, …/sec-matrices-lin-combs.html, …/frontmatter.html | 12 | 12/12 | "This work is licensed under a Creative Commons Attribution 4.0 International License." (home page, understandinglinearalgebra.org/home.html) | `austin_ula` (new) |
| OpenStax *Introductory Statistics 2e*, §4.1, 4.2 (extends the held file) | https://openstax.org/books/introductory-statistics-2e/pages/4-1-probability-distribution-function-pdf-for-a-discrete-random-variable and …/4-2-mean-or-expected-value-and-standard-deviation | 2 | 2/2 | "by OpenStax is licensed under Creative Commons Attribution-NonCommercial-ShareAlike License v4.0" (details page, re-read; web version still "Jul 07, 2026") | `openstax_intro_stats_2e` |
| Diez, Çetinkaya-Rundel, Barr, *OpenIntro Statistics* 4e: title page, ch. 3 contents, §3.1.5, §3.4, §3.5 | https://www.openintro.org/go?id=os4_for_screen_reader&referrer=/book/os/index.php (the book page's screen-reader PDF; its text layer) | 5 | 5/5 | PDF: "This textbook is also available under a Creative Commons license"; openintro.org/license: "released under a Creative Commons BY-SA 3.0 license"; Open Textbook Library: "Attribution-ShareAlike CC BY-SA" | `openintro_stats_4e` (new) |
| Chow & Hall 2008 *PLoS Comput Biol* 4:e1000045: licence, abstract, Results passages in words | https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000045 | 9 | 9/9 | "distributed under the terms of the Creative Commons Public Domain declaration …" (article page); PMC XML links CC0 1.0 | `chow_hall_2008` (new) |
| FAO/WHO/UNU 2004 ch. 5, Table 5.2 and the sentences before it (extends the held file) | https://www.fao.org/4/y5686e/y5686e07.htm; title page https://www.fao.org/4/y5686e/y5686e00.htm re-read | 2 | 2/2 | "All rights reserved. Reproduction and dissemination of material in this information product for educational or other non-commercial purposes are authorized without any prior written permission from the copyright holders provided the source is fully acknowledged." (title page, unchanged) | `fao_who_unu_2004` |
| Thomas et al. 2013, the Methods equation (extends the held file) | https://pmc-oa-opendata.s3.amazonaws.com/PMC4024447.1/PMC4024447.1.xml (markdown for prose; html for the MathML) | 3 (1 MathML) | 3/3 | "This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law." (in the XML, as for the held .txt) | `thomas_2013_3500kcal` |
| Polidori et al. 2016, Equations 1-5 and their Methods prose (extends the held file) | https://pmc-oa-opendata.s3.amazonaws.com/PMC5108589.1/PMC5108589.1.xml (markdown for prose; html for the MathML) | 14 (5 MathML) | 14/14 | same text-mining line, in the XML | `polidori_2016` |

Section numbers confirmed. OpenIntro Statistics 4e: random variables are **§3.4 "Random variables"**, pp. 128-139, with
3.4.1 Expectation, 3.4.2 Variability in random variables, 3.4.3 Linear combinations of random variables, 3.4.4
Variability in linear combinations of random variables (the PDF's contents list, held in the file). §3.5 is
"Continuous distributions", so the reviewer's "3.4–3.5" covers expectation and variance (3.4) and probability as
area (3.5); both are held. Understanding Linear Algebra: matrix-vector multiplication is subsection 2.2.2, as
`READY.md` says, on the pages fetched 2026-09-24.

## Equations obtained as text (converted from MathML)

| Paper | Equation | Plain-text rendering (the file's notation) |
| --- | --- | --- |
| Thomas 2013 | Methods, unnumbered | `W(t) = W_0 - ΔEB (t/3500)` |
| Polidori 2016 | Equation 1 | `ΔEI_i = ρ (dBW_i/dt) + ε(BW_i − BW_0) + (Δδ/(1 − β)) BW_0 + UGE` |
| Polidori 2016 | Equation 2 | `ρ = ((η_FM + ρ_FM + αη_FFM + αρ_FFM)/((1 − β)(1 + α)))` |
| Polidori 2016 | Equation 3 | `ε = (1/(1 − β)) [ ((γ_F + αγ_L)/(1 + α)) + δ_0 + Δδ].` |
| Polidori 2016 | Equation 4 | `ΔEI(t) = − k_P × ΔBW(t)` |
| Polidori 2016 | Equation 5 | `ΔEI(t) = − k_P × ΔBW(t) − k_I ∫_0^t ΔBW(τ)dτ` |

FAO/WHO/UNU Table 5.2 is held as the page's own text, not MathML: each equation is a cell such as
`15.057kg + 692.2` (kcal/day, men 18-30).

## Not obtained

| Source | Why | Where Harsh can get it |
| --- | --- | --- |
| Chow & Hall 2008, Equations 1 and 2 (and every other numbered equation) | Images only. The article page drops them; the PLoS JATS XML and the PMC XML (PMC2266991.1) carry each `<disp-formula>` as a `<graphic>`, with no MathML or TeX. The prose that states them in words is held | Equation 1: https://journals.plos.org/ploscompbiol/article/file?type=thumbnail&id=10.1371/journal.pcbi.1000045.e001 · Equation 2: …journal.pcbi.1000045.e002 · the article PDF from https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000045. Needs copying symbol by symbol and a second reader |
| Hall 2008 *Int J Obes* 32:573, the two equations | Images in Harsh's author-manuscript PDF. The PMC Article Dataset has no XML for PMC2376744 (HTTP 404); Europe PMC fullTextXML returns HTTP 500 and its PDF route HTTP 403; pmc.ncbi.nlm.nih.gov is reCAPTCHA-gated to the fetch tool | Harsh's PDF (NIHMS47767), or https://pmc.ncbi.nlm.nih.gov/articles/PMC2376744/. Needs copying symbol by symbol and a second reader |

## Caveats found during intake

- **New keys, and Book 0's unheld keys left as they were (conductor's decision).** Book 0 cites
  `openstax_calculus_v1` and `openstax_college_algebra_2e` with no file, in ten records that carry no `quote`
  (B0-R0-C21, C22, C23; B0-R0-C07, C15-C20). Mapping a file to either key turned the quote check on for them and took the
  build from blocking 0 to 10 when tested. Book 0 is frozen, so the S02-R1 excerpts are filed under new keys,
  `openstax_calculus_v1_s02` and `openstax_college_algebra_2e_7_5`, after the section-suffix precedent of
  `openstax_contemporary_math_7_7`. Both are mapped in `INDEX.yml`, so every S02 quote under them is machine-checked.
  Book 0's two keys are unchanged: no file, and `.bib` entries identical to HEAD.
- **OpenStax mathematics is flattened** (inline formulas doubled and run together, display equations one symbol per
  line). The headers say so: quote prose, never a formula.
- **OpenIntro licence version.** The PDF names no version. The publisher's licence page says CC BY-SA 3.0, and the Open
  Textbook Library says CC BY-SA with no version. Recorded as 3.0 on the publisher's page. Its terms also forbid
  titling a derivative as an OpenIntro product.
- **Understanding Linear Algebra renumbering.** The home page says the August 2026 revision "may affect the numbering of
  subsections". Numbers are recorded as printed on 2026-09-24; cite by title as well.
- **Polidori Equation 3.** The MathML writes the coefficients γ_F and γ_L, while the prose beside it names γFFM and
  γFM. Stored as fetched and flagged in the file.
- **Polidori's measurement interval is resolved.** The XML reads "t = (N−1)*T" (the markdown fetch had escaped the
  asterisk as `\*`). With N = 2, the interval is T = 52 days. This closes the caveat in the S01-R1 log.
- **FAO Table 5.2, the ≥ 60 rows.** The age band comes through as "³ 60" (a Symbol-font ≥). The file's note says to
  read it as ≥ 60 and to check the PDF before quoting that row. The column "see" is not expanded on the page.
- **Thomas 2013's equation** uses a hyphen-minus in its MathML (`W_0 - ΔEB (t/3500)`), where Polidori's uses a true
  minus. This is as fetched.
- **Older `.bib` entries** (`openstax_chemistry_2e`, `openstax_biology_2e`, `openstax_anatphys_2e`,
  `openstax_college_physics_2e`, `fao_food_energy_2003`) carry `sources/…txt` paths in their `note` field. They
  were not written by this intake and were left alone. The six entries this intake wrote or edited carry none.

## Addendum, 2026-09-24: audit follow-up (Polidori extension; ICMR-NIN 2024)

Same method as above: TinyFish `fetch_content` only, raw results saved from the tool's own result files to
`/home/claude/intake-s02b/` (`fetch1.json`: the PMC5108589 .txt and .xml in markdown format, and the ICMR-NIN
2024 page; `fetch2_xml_html.json`: the .xml in html format, for the MathML), passages cut by script
(`cut_polidori.py`), no WebFetch text stored, no curl, wget or Python HTTP.

**Polidori 2016, blocks 14-17** (for defects C01 items 3, 4, 6, 12; C16; C17), from
https://pmc-oa-opendata.s3.amazonaws.com/PMC5108589.1/PMC5108589.1.xml:

| Block | What | Passage (start) |
| --- | --- | --- |
| 14 | Methods, β | "The parameter β accounts for the adaptation of energy expenditure during a diet perturbation, ΔEI, …" (one sentence; the η sentence after it omitted) |
| 15 | Methods, UGE as energy | "The parameter UGE represents the energy losses as a result of increased urinary excretion of glucose with canagliflozin treatment. Model parameter values are given in Table 1." |
| 16 | Table 1, three slices | caption and header; δ0 10 kcal/kg/d "Physical activity at baseline", Δδ 0 kcal/kg/d; β 0.24 "Dietary and adaptive thermogenesis", UGE 360 kcal/d |
| 17 | Results, fitted k_P | the paragraph ending "(as defined by Equation 4 with the parameter kP = 95 kcal/day per kg) mimics …" |

δ was already defined in prose in block 12 ("The baseline physical activity parameter was δ0 and Δδ represents
changes in physical activity …"); the paper has no other defining sentence, so block 16's Table 1 rows are the
addition. The paper states UGE as energy only in Table 1 (360 kcal/d); it gives **no per-gram conversion**
from the ~90 g/day, and the file supplies none.

**Verbatim check, whole file** (`verify_polidori.py`, every block 1-17 against the fresh fetch for its URL):
**35 of 35** (blocks 1-10: 15 against the .txt; blocks 11-13: 14, five of them MathML; blocks 14-17: 6). The
MathML re-converts to the same five renderings as before. `INDEX.yml` and `SOURCES.md` rows updated; no
`.bib` change.

**ICMR-NIN 2024: not obtained.** https://nin.res.in/RDA_short_Report_2024.html (the "Short Report New" link on
the nin.res.in home page) was fetched in markdown and html: it is a price list for the printed "Short Summary
of RDA" (₹150) and the full RDA book (₹400), with the 2020 citation, and links no PDF. The "Full Book" link
(RDA_Full_Report_2024.html) is the same list. Guessed paths `…/RDA_short_Report_2024.pdf`,
`…/downloads/RDA_short_Report_2024.pdf` and `…/rdabook/RDA_short_Report_2024.pdf` were unreachable. Web
search found only unofficial copies (a Scribd upload, whose page returned no document text; coaching-class
slides), which were not used or filed. So no new citekey. The 2024 vs 2020 comparison (the 10-12%
overestimate, the two 5% BMR cuts, PAL 1.53 → 1.40) is **unchecked**; the book's figures rest on
`icmr_nin_2020_brief` as before. To settle it, Harsh needs the printed Short Summary (ICMR-NIN publications
counter) or an official PDF.
