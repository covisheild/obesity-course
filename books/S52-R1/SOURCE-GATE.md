# Source gate · S52-R1 (Book 6: R, reproducibility engineering and data management · Rung 1)

release: pending

Written 2 Oct 2026 after inventory (`INVENTORY.md`, 22 concepts) and source intake (`intake/log-a.md`, `log-b.md`,
`log-c.md`). Verbatim check by the intake agents 98/98 + 96/96 + 26/26 (group c, a, b); re-checked by the conductor
as substrings of the raw fetches: 219 of 220, the other being a header line that matches the CSV itself.
Projected length: `page_budget` 240 pages (22 sections). Coverage gaps and the dataset choice are in the message to Harsh.

## Needed

Every source `READY.md` lists: R for Data Science 2e; *An Introduction to R*; *R Language Definition* (optional);
Software Carpentry R lesson; Data Carpentry spreadsheet lesson (optional); tidyverse style guide; Wickham 2014;
Broman & Woo 2018; Ziemann et al. 2016; Herndon, Ash & Pollin; PHE statement 2020; Trisovic et al. 2022; Peng 2011;
Sandve et al. 2013; Wilson et al. 2017; version-matched package help pages; changelogs for later versions; the
dataset for the build (Harsh's decision). Optional: Bruford et al. 2020; the NMC MD Community Medicine guideline.

## Obtained

| Citekey | File | Concepts |
| --- | --- | --- |
| `r4ds_2e` | `sources/r4ds_2e.txt` | C02–C09, C11–C18, C21, C22 |
| `r_intro_manual` | `sources/r_intro_manual.txt` | C02–C06, C13 |
| `r_lang_def` | `sources/r_lang_def.txt` | C03–C05 |
| `swc_r_gapminder` | `sources/swc_r_gapminder.txt` | C02, C04, C07, C11, C14, C18 |
| `dc_spreadsheets` | `sources/dc_spreadsheets.txt` | C08, C15, C19 |
| `tidyverse_style` | `sources/tidyverse_style.txt` | C03 |
| `wickham_2014_tidy` | `sources/wickham_2014_tidy.txt` | C08, C17 |
| `broman_woo_2018` | `sources/broman_woo_2018.txt` | C01, C08, C09, C10, C15 |
| `ziemann_2016` | `sources/ziemann_2016.txt` | C01, C15 |
| `herndon_2013_wp322` | `sources/herndon_2013_wp322.txt` | C01 |
| `phe_2020_delayed` | `sources/phe_2020_delayed.txt` | C01 |
| `trisovic_2022` | `sources/trisovic_2022.txt` | C20, C21 |
| `peng_2011` | `sources/peng_2011.txt` | C20 |
| `sandve_2013` | `sources/sandve_2013.txt` | C10, C18–C21 |
| `wilson_2017` | `sources/wilson_2017.txt` | C07, C10, C19, C21, C22 |
| `tidyverse_news_s52r1` | `sources/tidyverse_news_s52r1.txt` | C06, C21 |
| `horst_2020_palmerpenguins` | `sources/horst_2020_palmerpenguins.txt` | C22 and worked examples |
| `rdocs_s52r1_base` | `sources/rdocs_s52r1_base.txt` | C04–C19, C21 (help pages) |
| `rdocs_s52r1_utils` | `sources/rdocs_s52r1_utils.txt` | C04–C19, C21 (help pages) |
| `rdocs_s52r1_stats` | `sources/rdocs_s52r1_stats.txt` | C04–C19, C21 (help pages) |
| `rdocs_s52r1_dplyr` | `sources/rdocs_s52r1_dplyr.txt` | C04–C19, C21 (help pages) |
| `rdocs_s52r1_tidyr` | `sources/rdocs_s52r1_tidyr.txt` | C04–C19, C21 (help pages) |
| `rdocs_s52r1_readr` | `sources/rdocs_s52r1_readr.txt` | C04–C19, C21 (help pages) |
| `rdocs_s52r1_readxl` | `sources/rdocs_s52r1_readxl.txt` | C04–C19, C21 (help pages) |
| `rdocs_s52r1_haven` | `sources/rdocs_s52r1_haven.txt` | C04–C19, C21 (help pages) |
| `rdocs_s52r1_ggplot2` | `sources/rdocs_s52r1_ggplot2.txt` | C04–C19, C21 (help pages) |
| `rdocs_s52r1_forcats` | `sources/rdocs_s52r1_forcats.txt` | C04–C19, C21 (help pages) |
| `rdocs_s52r1_lubridate` | `sources/rdocs_s52r1_lubridate.txt` | C04–C19, C21 (help pages) |
| `rdocs_s52r1_stringr` | `sources/rdocs_s52r1_stringr.txt` | C04–C19, C21 (help pages) |
| `rdocs_s52r1_here` | `sources/rdocs_s52r1_here.txt` | C04–C19, C21 (help pages) |

## Not obtained

Nothing the claims need is missing; these rows are what differs from the published or intended version. Each says
what is held instead.

| Source | Needed for | URL tried | Why not obtained | Provided |
| --- | --- | --- | --- | --- |
| Herndon, Ash & Pollin 2014, *Camb J Econ* 38:257, the journal article | C01 | https://academic.oup.com/cje (article page via doi.org) | publisher page "bot_blocked". **Held instead:** PERI Working Paper 322 (April 2013, revised), which states the spreadsheet error ("lines 30 to 44 instead of lines 30 to 49") | yes: sources/herndon_2014_cje.txt |
| Broman & Woo 2018, *Am Stat* 72:2, the typeset journal article | C01, C08–C10, C15 | https://www.tandfonline.com/doi/full/10.1080/00031305.2017.1375989 | publisher page "bot_blocked". **Held instead:** the authors' own manuscript (CC BY), kbroman.org and PeerJ Preprints 6:e3183v2; wording may differ slightly from print | no |
| NHANES 2021-2023 `BMX_L.xpt` (1.5 MB) and `DEMO_L.xpt` (2.5 MB) with their codebooks | C22 and the build, **only if Harsh chooses dataset A** | https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Examination&Cycle=2021-2023 | the host refuses downloads from the sandbox (CONNECT 403); the data page was readable | yes: sources/nchs_nhanes_2021_2023_bmx_demo.txt |
| Bruford et al. 2020, *Nat Genet* 52:754, HGNC gene nomenclature guidelines | C01 (optional: only to say the gene symbols were later renamed) | https://www.nature.com/articles/s41588-020-0669-3 | paywalled | yes: sources/bruford_2020_hgnc.txt |
| NMC, *Guidelines for competency based postgraduate training programme for MD in Community Medicine* | C09 (optional: the curriculum's software line) | https://nmc.org.in/storage/new/MD-Community-Medicine.pdf | opened for `COVERAGE.md`, not filed; no date on the document | yes: sources/nmc_pg_md_community_medicine.txt |

## Supplied by Harsh, 2 Oct 2026

Harsh attached the Herndon et al. 2014 journal PDF, Bruford et al. 2020, the NMC MD Community Medicine
guideline, NHANES 2021-2023 `BMX_L.xpt` and `DEMO_L.xpt`, and the two codebooks printed to PDF. Filed by intake
group d (`intake/log-d.md`): 31/31 passages verbatim, every cited number checked against the page image; data
files byte-identical (MD5 ab25a36296e5b61881d42fef61c06b84, 14555b1f4e3c909172e900f63a2ecd03); BMX_L 8860 x 22,
DEMO_L 11933 x 27, 6064 BMX rows aged 20 or over after the join (recomputed by the conductor); all 155 printed
codebook counts match the data. Conductor re-check of the passages: 31/31. Still not provided: the typeset
Broman & Woo article (the authors' manuscript is held). A Kincaid et al. 1975 PDF came in the same upload; it is
Book 9's (S58-R1) source, already filed there, and is not used here.

## Decisions for Harsh (also in the message)

1. Build dataset: A (NHANES, you download two files), B (palmerpenguins `penguins_raw.csv`, held, CC0), or C (NFHS-5 district table, not reachable).
2. Accept outputs from R 4.3.3 and the tidyverse as installed here (ggplot2 3.4.4; newest is 4.0.3), stated in the book.
3. Coverage gaps (iteration; regular expressions) as proposed S52-R2 amendments: accept or refuse.
