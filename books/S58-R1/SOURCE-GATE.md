# Source gate · S58-R1 · Scientific writing, visualisation and public communication · Rung 1

Written 2 Oct 2026 at the source-collection stop (`CONDUCTOR.md` §2). Nothing is drafted until Harsh
releases this gate.

release: pending

## Needed

27 sources serve the 21 concepts (`READY.md`, `INVENTORY.md`). All 27 are now held (2 Oct 2026), plus three extras.

| Source | Concepts |
| --- | --- |
| NFHS-5 India Fact Sheet (held) | C08, C16, C21 |
| OpenStax *Contemporary Mathematics* §8.2 (held) | C16 |
| OpenStax *Introductory Business Statistics 2e* §2.1 (held) | C16 |
| Chalmers & Glasziou 2009 (held) | C02 |
| ICMJE Recommendations, section IV.A (version updated January 2026) | C01, C02, C03, C04, C07, C08, C13, C19, C20 |
| Sollaci & Pereira 2004 | C01 |
| Mensh & Kording 2017 | C02, C03, C04, C07, C09, C11, C12 |
| OpenStax *Writing Guide with Handbook* | C05, C06, C09 |
| Gopen & Swan 1990 | C06 |
| Federal Plain Language Guidelines 2011 | C06, C11 |
| Barnett & Doubleday 2020 | C07 |
| Cole 2015 | C08 |
| Lang & Altman, SAMPL | C08 |
| Kincaid et al. 1975 | C10 |
| Plavén-Sigray et al. 2017 | C10 |
| Rougier, Droettboom & Bourne 2014 | C13, C17, C18, C19, C20 |
| Wilke 2019, 15 chapters | C13–C20 |
| Bergstrom & West, proportional ink | C16 |
| Correll, Bertini & Franconeri 2020 | C16 |
| Heer & Bostock 2010 | C14 |
| Weissgerber et al. 2015 | C15 |
| Bateman et al. 2010 | C17 |
| Crameri, Shephard & Heron 2020 | C18 |
| Cumming, Fidler & Vaux 2007 | C19 |
| Cleveland & McGill 1984 | C14 (optional) |
| Tufte 2001 | C16, C17 (optional) |
| Flesch 1948 | C10 (optional) |

## Obtained

Every stored passage was re-checked as a whitespace-normalised substring of the saved fetch, by each intake
agent and again by the conductor with a separate script; the few chunks the conductor's script flagged were
header lines of the files, not passages.

| Citekey | File |
| --- | --- |
| `nfhs5_india_factsheet`, `openstax_contemporary_math`, `openstax_business_stats_2e`, `chalmers_glasziou_2009` | held before this book |
| `icmje_2026_manuscript_preparation` | `sources/icmje_2026_manuscript_preparation.txt` |
| `sollaci_pereira_2004_imrad` | `sources/sollaci_pereira_2004_imrad.txt` |
| `mensh_kording_2017_structuring_papers` | `sources/mensh_kording_2017_structuring_papers.txt` |
| `openstax_writing_guide_handbook` | `sources/openstax_writing_guide_handbook.txt` |
| `gopen_swan_1990_scientific_writing` | `sources/gopen_swan_1990_scientific_writing.txt` |
| `plain_language_2011_guidelines` | `sources/plain_language_2011_guidelines.txt` |
| `barnett_doubleday_2020_acronyms` | `sources/barnett_doubleday_2020_acronyms.txt` |
| `cole_2015_too_many_digits` | `sources/cole_2015_too_many_digits.txt` |
| `lang_altman_2013_sampl` | `sources/lang_altman_2013_sampl.txt` |
| `plavensigray_2017_readability` | `sources/plavensigray_2017_readability.txt` |
| `rougier_2014_ten_rules_figures` | `sources/rougier_2014_ten_rules_figures.txt` |
| `wilke_2019_dataviz_ch03` … `ch29`, `wilke_2019_dataviz_preface` | `sources/wilke_2019_dataviz_*.txt` |
| `bergstrom_west_2016_proportional_ink` | `sources/bergstrom_west_2016_proportional_ink.txt` |
| `correll_2020_truncating_yaxis` | `sources/correll_2020_truncating_yaxis.txt` |
| `heer_bostock_2010_crowdsourcing_perception` | `sources/heer_bostock_2010_crowdsourcing_perception.txt` |
| `weissgerber_2015_beyond_bar_graphs` | `sources/weissgerber_2015_beyond_bar_graphs.txt` |
| `bateman_2010_useful_junk` | `sources/bateman_2010_useful_junk.txt` |
| `crameri_2020_misuse_colour` | `sources/crameri_2020_misuse_colour.txt` |
| `cumming_2007_error_bars` | `sources/cumming_2007_error_bars.txt` |
| `kincaid_1975_readability` (supplied by Harsh 2 Oct 2026: the UCF STARS PDF with a text layer; Table 3 and the Flesch counting rules checked against page images) | `sources/kincaid_1975_readability.txt` |
| `cleveland_mcgill_1984_graphical_perception` (supplied by Harsh 2 Oct 2026; OCR text layer; every page carrying a held number or the ranking checked against its image) | `sources/cleveland_mcgill_1984_graphical_perception.txt` |
| `tufte_1983_visual_display` (supplied by Harsh 2 Oct 2026; the copy is the **first edition**, 1983, tenth printing 1990, not the 2001 second edition; every held page checked against its image) | `sources/tufte_1983_visual_display.txt` |
| `flesch_1948_readability_yardstick` (Harsh could not download the APA original and asked for alternatives; found as a retyped public-domain reprint in DuBay's *The Classic Readability Studies*, ERIC ED506404) | `sources/flesch_1948_readability_yardstick.txt` |
| Extra: `flesch_1979_plain_english` (Flesch's own *How to Write Plain English*, ch. 2: the formula as "multiply the average word length by 84.6" and the score bands) | `sources/flesch_1979_plain_english.txt` |
| Extra, not in the list: `krishnamurthy_2021_cvd_india` (colour-vision deficiency in boys in one Tamil Nadu district, for C18) | `sources/krishnamurthy_2021_cvd_india.txt` |
| Fallback for Kincaid: `edwards_2022_readability_formulas` (secondary restatement of the Flesch formulas) | `sources/edwards_2022_readability_formulas.txt` |

Caveats on obtained sources: ICMJE asks others not to reprint or post the Recommendations, so the file is a
set of short excerpts and the book quotes briefly and links; Gopen & Swan is a retyped reprint with no page
numbers; the Plain Language Guidelines come from a copy of the 2011 PDF on wid.org because plainlanguage.gov
was offline; SAMPL is the 2013 PDF EQUATOR links to, not the 2015 journal version; Bateman 2010 is a camera-ready
PDF on a statistics reading folder (no authors' own copy found); Correll 2020 is the arXiv v2 preprint under arXiv's
distribution licence only; Bergstrom & West's page states no licence; Wilke is CC BY-NC-ND 4.0, held verbatim.

## Not obtained

Every row is now provided. Kincaid 1975, Cleveland & McGill 1984 and Tufte were supplied by Harsh on 2 Oct 2026. Flesch 1948
could not be downloaded; at Harsh's instruction ("search for its alternatives") the article itself was found as a retyped
public-domain reprint (ERIC ED506404). It settles the coefficient: Flesch printed .846, so Kincaid's Table 3 ".836" is a
misprint. Release is still pending until Harsh confirms the reprint is acceptable.

| Source | Needed for | URL tried | Why not obtained | Provided |
| --- | --- | --- | --- | --- |
| Kincaid et al. 1975 | C10 | https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=1055&context=istlibrary | scan without a text layer at fetch | yes: sources/kincaid_1975_readability.txt |
| Flesch 1948, A new readability yardstick | C10 | https://doi.org/10.1037/h0057532 | paywall (APA / Ovid) | yes: sources/flesch_1948_readability_yardstick.txt |
| Cleveland & McGill 1984 | C14 | https://doi.org/10.1080/01621459.1984.10478080 | paywall; JSTOR terms | yes: sources/cleveland_mcgill_1984_graphical_perception.txt |
| Tufte, The Visual Display of Quantitative Information | C16, C17 | https://archive.org/details/visualdisplayofq00tuft | print book | yes: sources/tufte_1983_visual_display.txt |
