# Source gate · S47-R1 (Book 5)

release: pending

Updated 2026-10-02: Harsh supplied five PDFs (intake group H, verbatim 11/11). Still not obtained: General Clauses Act s.23 and the 2026 amendment to Notification 9/2025-CT(Rate).

Written 2026-10-01 after Task 1 (`INVENTORY.md`, `READY.md`, `COVERAGE.md`) and source intake
(`INTAKE.md`, four intake groups A–D, every stored passage re-checked verbatim: A 29/29, B 15/15,
C 30/30, D 30/30). Nothing is drafted until Harsh supplies the sources below or writes exactly
"Proceed with incomplete sources and start building the book" (`check/sourcegate.py`).

Projected size: 18 sections, `page_budget: 160` (about 8 pages a section plus answers).

## Needed

| Source | Concepts |
| --- | --- |
| Constitution of India (Arts 32, 73, 77, 107–112, 162, 226, 243G, 243W, 245, 246, 279A, 282; Seventh, Eleventh, Twelfth Schedules) | C02–C09, C18 |
| FSS Act 2006 (ss. 2, 92, 93); Consumer Protection Act 2019; DPDP Act 2023 and its commencement notice | C02–C04, C07, C09 |
| Held Book 4 releases (MSP, NMEO-Oilseeds, Poshan 2.0 guidelines) | C02, C08 |
| OpenStax *American Government* 4e §§ 8.4, 10.1, 16.1, 16.4 | C01, C10, C12, C15–C17 |
| OpenStax *Introduction to Political Science* § 1.2 (optional anchor) | C01 |
| Gilson (ed.) 2012 HPSR Reader, Part 1 §§ 4–5 | C01, C10 |
| Koon, Hawkins & Mayhew 2016 | C12–C15 |
| Barry et al. 2009 | C13, C14 |
| Summan et al. 2026 | C13, C18 |
| Walt et al. 2008; Gilson & Walt 2023 | C10 |
| Oxman et al. 2009 (SUPPORT 1); Cairney & Oliver 2017; Oliver & Cairney 2019 | C16, C17 |
| Allocation of Business Rules 1961; Transaction of Business Rules 1961 | C05 |
| How a Bill becomes an Act (Rajya Sabha booklet; PRS 2012); Pre-Legislative Consultation Policy 2014 | C06 |
| General Clauses Act 1897 s.23; one e-Gazette draft notification with its objection period | C07 |
| National Health Policy 2017 and its Cabinet approval | C08 |
| COTPA 2003 and the 2008 smoking-in-public-places rules; WHO FCTC | C11 |
| PIB 2163555 (56th GST Council) and its FAQ; CGST Act s.9; the rate notification for sugar-added drinks | C09, C18 |
| PIB 2105618 (edible-oil call); FSSAI Eat Right India page | C14, C15 |

## Obtained

| Citekey | File |
| --- | --- |
| (held before) `constitution`, `fss_act_2006`, `consumer_prot_2019`, `dpdp_act_2023`, `dpdp_commencement_2025`, `s37_pib_msp_backgrounder`, `pib_2260617`, `pib_2061646`, `poshan2_guidelines_2022` | as in `sources/INDEX.yml` |
| `openstax_amgov_4e` | `sources/openstax_amgov_4e.txt` |
| `openstax_intro_polisci_1_2` | `sources/openstax_intro_polisci_1_2.txt` |
| `gilson_2012_hpsr_reader` | `sources/gilson_2012_hpsr_reader.txt` (WHO's abridged edition, Part 1 whole) |
| `koon_2016_framing` | `sources/koon_2016_framing.txt` |
| `barry_2009_metaphors` | `sources/barry_2009_metaphors.txt` (excerpts, audit quotation only) |
| `summan_2026_foodtax` | `sources/summan_2026_foodtax.txt` |
| `walt_2008_policy` | `sources/walt_2008_policy.txt` |
| `gilson_walt_2023` | `sources/gilson_walt_2023.txt` |
| `oxman_2009_support` | `sources/oxman_2009_support.txt` |
| `cairney_oliver_2017` | `sources/cairney_oliver_2017.txt` |
| `oliver_cairney_2019` | `sources/oliver_cairney_2019.txt` |
| `goi_aob_rules_1961` | `sources/goi_aob_rules_1961.txt` (amended to series no. 386, 22 Jul 2026) |
| `goi_tob_rules_1961` | `sources/goi_tob_rules_1961.txt` (amended to no. 75, 13 Jan 2025) |
| `rajyasabha_2005_legislative` | `sources/rajyasabha_2005_legislative.txt` |
| `prs_2012_parliament60` | `sources/prs_2012_parliament60.txt` |
| `pib_1797203` | `sources/pib_1797203.txt` (stands in for the consultation policy; does not give its 30 days) |
| `mohfw_2017_nhp` | `sources/mohfw_2017_nhp.txt` (NHSRC-hosted copy) |
| `pib_1513000` | `sources/pib_1513000.txt` (Cabinet approval of NHP 2017, 15 Mar 2017) |
| `cotpa_2003` | `sources/cotpa_2003.txt` (OCR of the Gazette scan; misreadings listed in its header) |
| `who_fctc_2003` | `sources/who_fctc_2003.txt` (Arts 5–8; India ratified 5 Feb 2004) |
| `pib_2163555` | `sources/pib_2163555.txt` |
| `pib_2168426` | `sources/pib_2168426.txt` (FAQ naming Notification 9/2025-CT(Rate)) |
| `cgst_act_2017` | `sources/cgst_act_2017.txt` (CBIC consolidation as on 30 Sep 2020) |
| `pib_2105618` | `sources/pib_2105618.txt` |
| `fssai_eat_right_india` | `sources/fssai_eat_right_india.txt` |

## Not obtained

| Source | Needed for | URL tried | Why not obtained | Provided |
| --- | --- | --- | --- | --- |
| Pre-Legislative Consultation Policy 2014, Legislative Department (the text, with its 30-day comment period) | C06 | https://legislative.gov.in/pre-legislative-consultation-policy/ ; https://lddashboard.legislative.gov.in/documents/pre-legislative-consultation-policy | Script-rendered site (heading only); dashboard host blocked at the proxy | yes: sources/plcp_2014.txt |
| General Clauses Act 1897, s.23 (rules made after previous publication) | C07 | https://www.legislative.gov.in/centralact/1890 ; https://thc.nic.in/Central%20Governmental%20Acts/General%20Clauses%20Act,%201897.pdf | Script-rendered; PDF without a text layer. India Code not used (its terms forbid automated access) | no |
| One draft notification from the e-Gazette with its objection period (e.g. an FSSAI draft regulation) | C07 | https://egazette.gov.in/Disclaimer.aspx | Site terms could not be read (page redirects to an error), so nothing was fetched | yes: sources/fssai_2018_packaging_regs.txt (the final FSSAI Packaging Regulations 2018, G.S.R. of 24 Dec 2018, whose preamble recites the draft of 19 Mar 2018 and its 30-day objection period; Harsh supplied a final notification, which shows the whole draft-to-final path) |
| Prohibition of Smoking in Public Places Rules 2008, G.S.R. 417(E) | C11 | https://ntcp.mohfw.gov.in/assets/document/Acts-Rules-Regulations/GSR-417(E).pdf | PDF without a text layer | yes: sources/mohfw_2008_smoking_rules.txt (Indian Kanoon print, not an official copy; see header) |
| CGST Notification No. 9/2025-Central Tax (Rate), 17 Sep 2025, entries for HSN 2202 | C18 | https://taxinformation.cbic.gov.in/view-pdf/1010436/ENG/Notifications | CBIC tax portal unreachable from the sandbox | yes: sources/cgst_notif_9_2025_rate.txt (Gazette copy 266209 supplied by Harsh) |
| The latest amendment to Notification 9/2025-CT(Rate) (one issued in 2026; a search snippet names 01/2026-CT(Rate), 30 Apr 2026), to confirm the HSN 2202 entries still stand | C18 | https://www.gstcouncil.gov.in/cgst-rate-notification (list stops at 08/2025 as served); taxinformation.cbic.gov.in (proxy error) | Not on the GST Council list as served; CBIC portal unreachable | no |
| CGST Act 2017, s.9 as currently amended | C18 | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter3/section9_v1.00.html | Unreachable (proxy error); only the 2020 consolidation is held | yes: sources/cgst_act_2017_s9_cbic.txt |

## Optional, not obtained (these do not hold the gate)

| Source | Would serve | Without it |
| --- | --- | --- |
| Pielke 2007, *The Honest Broker*, ch. 1–2 (CUP; paywall) | C17 | The four roles are not taught; C17 names only "honest broker" against "issue advocate", as Oliver & Cairney 2019 state them |
| Entman 1993, *J Commun* 43(4):51 (paywall) | C12 | The four framing functions are cited as Entman's, as reported by Koon et al. 2016 |
| Gollust, Niederdeppe & Barry 2013, *Am J Public Health* 103:e96 (paywall) | C14 | Only Barry 2009's survey (no experiment) shows beliefs about cause and policy support |
| Walt & Gilson 1994, *Health Policy Plan* 9:353 (paywall) | C10 | The triangle is cited from Walt et al. 2008 |
| Kim & Willis 2007, *J Health Commun* (paywall) | C13 | News-framing findings come from Barry 2009 and Koon 2016 |
| Kerala 2016 "fat tax" (budget speech 2016-17 or the Commercial Taxes circular; keralataxes.gov.in is geo-blocked outside India) | C18 | The Kerala case is not mentioned |
| Lok Sabha Unstarred Question 2110, 12 Dec 2025 (policy never evaluated) | C06 | Fetched, then withdrawn: sansad.in's terms page failed (HTTP 500), so its terms were never read. `pib_1797203` covers the point |

## Conductor's decisions at intake (for Harsh to overrule)

- **Reproduction bars, not access bars.** cabsec.gov.in (the two Business Rules), NTCP (COTPA), WHO
  (FCTC, the Gilson Reader), OUP (Walt 2008) and the Milbank Fund (Barry 2009) say "all rights
  reserved" or "not without permission". None forbids automated access (unlike India Code). They
  are held in the private repository for audit quotation only, as Van Noorden 2017 was in Book 7.
- **NHP 2017** held from NHSRC (MoHFW's own technical institution; its site permits reproduction
  with acknowledgement), since mohfw.gov.in was unreachable.
- **The 40% GST rate** is a combined slab; CGST s.9(1) caps the Union's share at 20%. The book will
  not say the Union levies 40%. Whether the rate still stands on 1 Oct 2026 is unverified until the
  notification and its 2026 amendment are held.

## Coverage gaps proposed as map amendments (Harsh accepts or refuses; nothing added meanwhile)

1. **SWOT analysis of a policy** (NMC MD Community Medicine, health-policy objective). Proposal: no
   amendment, or a one-line mention at S47-R2.
2. **Power as an analytic concept** (Buse et al. 3e ch. 2; Gilson Reader §5). Proposal: amend
   S47-R2 P1 to add "power, and the forms in which it is exercised".
