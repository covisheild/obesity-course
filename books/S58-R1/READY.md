# Source gate · S58-R1

Checked against `sources/`, `sources/INDEX.yml` and `sources/SOURCES.md` on 2026-10-02. The rule in `claude.md`: a line saying **no** stops the pipeline. Transcribe at intake with `mcp__TinyFish__fetch_content`, never WebFetch (`sources/SOURCES.md`). No S58 amendment in `map/AMENDMENTS-v3.1.yml` is marked `verify_at_intake` (S58-R3-A01 to A04 are all `false`), so none is added. Nothing on scientific writing, readability or data visualisation is held; four held files serve this book in part.

Task 1 opened four of the sources below with TinyFish to check coverage (`COVERAGE.md`): the ICMJE manuscript-preparation page, Rougier et al. 2014, Mensh & Kording 2017, and Wilke's contents page and chapter 17. Opening them is not intake: none is transcribed into `sources/`, so each still says **no**. Identifiers marked "(PubMed)" were confirmed with the PubMed ID converter on 2026-10-02; every other URL is the one expected and is "to confirm at intake".

**Renumbered 2 Oct 2026** (concepts C05 and C21 added for amendments S58-R1-A02 and S58-R1-A01; old C05–C19 are now C06–C20, old C20 is C22, old C21 is C23; table in `INVENTORY.md`). The concept columns below use the new numbers; the "Obtained" columns are as at Task 1 (all sources are now held: `SOURCE-GATE.md`).

## Held

| Work, section | Kind | File (key) | Obtained | Concepts |
| --- | --- | --- | --- | --- |
| NFHS-5 (2019-21) India Fact Sheet, indicators 88-89 (women and men 15-49 overweight or obese; urban, rural, total; NFHS-4 total) | instrument (survey report) | `nfhs5_india_factsheet.txt` (`nfhs5_india_factsheet`) | **yes** | C09, C17, C23 |
| OpenStax *Contemporary Mathematics* §8.2, Misleading Graphs ("vertical axes that don't start at zero") | textbook | `openstax_contemporary_math_8_2.txt` (`openstax_contemporary_math`) | **yes** | C17 |
| OpenStax *Introductory Business Statistics 2e* §2.1, How NOT to Lie with Statistics (units and scale of an axis) | textbook | `openstax_business_stats_2_1.txt` (`openstax_business_stats_2e`) | **yes** | C17 |
| Chalmers I, Glasziou P. Avoidable waste in the production and reporting of research evidence. *Lancet* 2009;374:86 ("biased or unusable reports") | primary (analysis) | `chalmers_glasziou_2009.txt` (`chalmers_glasziou_2009`; audit quotation only) | **yes** | C02 |

## To obtain: open HTML or open PDF, reachable from a session

| Work, section | Kind | Obtained | Where to get it | Format | Licence (to confirm) | Concepts |
| --- | --- | --- | --- | --- | --- | --- |
| ICMJE. *Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals*, §II.A Preparing a Manuscript: 1 General principles (IMRAD), 3.a-k Manuscript sections (title, abstract, introduction, results, discussion, tables, figures, units, abbreviations). Record the version date at intake | guideline | no (opened at Task 1) | https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html | HTML | ICMJE copyright; free to reproduce for non-commercial education (to confirm) | C01, C02, C03, C04, C05, C08, C09, C14, C20, C21, C22 |
| Sollaci LB, Pereira MG. The introduction, methods, results, and discussion (IMRAD) structure: a fifty-year survey. *J Med Libr Assoc* 2004;92(3):364-367 | primary | no | PMID 15243643 (PubMed); PMC copy to confirm | HTML | free to read | C01 |
| Mensh B, Kording K. Ten simple rules for structuring papers. *PLoS Comput Biol* 2017;13(9):e1005619 | textbook (guidance paper) | no (opened at Task 1) | PMC5619685 (PubMed); https://doi.org/10.1371/journal.pcbi.1005619 | HTML | CC BY 4.0 (PLOS default; to confirm) | C02, C03, C04, C08, C10, C12, C13 |
| OpenStax. *Writing Guide with Handbook* (2021): handbook sections on sentence structure (subject, verb, clause, voice) and on paragraphs (topic sentence, development); exact sections to identify at intake | textbook | no | https://openstax.org/books/writing-guide/pages/1-unit-introduction | HTML | CC BY-NC-SA 4.0 (stated on the preface page opened at Task 1) | C06, C07, C10 |
| Gopen GD, Swan JA. The science of scientific writing. *Am Sci* 1990;78(6):550-558 | textbook (canonical paper) | no | public PDF on a third-party host, https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf; author's page https://georgegopen.com/scientific-writing-articles/. JSTOR copy (stable 29774235) not to be fetched: see terms below | PDF | Sigma Xi copyright | C07 |
| U.S. Plain Language Action and Information Network. *Federal Plain Language Guidelines*, rev. 1 (May 2011): the sections on active voice, short words, omitting unnecessary words and short sentences (headings to confirm) | guideline | no | https://www.plainlanguage.gov/guidelines/ (site availability to confirm; the 2011 PDF is the stable form) | HTML / PDF | U.S. government work, public domain | C07, C12 |
| Barnett A, Doubleday Z. The growth of acronyms in the scientific literature. *eLife* 2020;9:e60080 | primary | no | PMC7556863 (PubMed) | HTML | CC BY 4.0 (to confirm) | C08 |
| Cole TJ. Too many digits: the presentation of numerical data. *Arch Dis Child* 2015;100(7):608-609 | textbook (guidance paper) | no | PMC4483789 (PubMed) | HTML | open access, CC BY (to confirm) | C09 |
| Lang TA, Altman DG. Basic statistical reporting for articles published in biomedical journals: the "Statistical Analyses and Methods in the Published Literature" or SAMPL guidelines. *Int J Nurs Stud* 2015;52(1):5-9 | guideline | no | EQUATOR page and PDF, https://www.equator-network.org/reporting-guidelines/sampl/ | PDF | free to read | C09 |
| Kincaid JP, Fishburne RP, Rogers RL, Chissom BS. *Derivation of New Readability Formulas (Automated Readability Index, Fog Count and Flesch Reading Ease Formula) for Navy Enlisted Personnel*. Research Branch Report 8-75, Naval Technical Training Command, 1975: the Flesch Reading Ease and Flesch-Kincaid grade formulas | textbook (canonical report) | no | https://apps.dtic.mil/sti/citations/ADA006655; ERIC ED108134, https://eric.ed.gov/?id=ED108134 | PDF (scan; OCR to check) | U.S. government work, public domain | C11 |
| Plavén-Sigray P, Matheson GJ, Schiffler BC, Thompson WH. The readability of scientific texts is decreasing over time. *eLife* 2017;6:e27725 | primary | no | PMC5584989 (PubMed) | HTML | CC BY 4.0 (to confirm) | C11 |
| Rougier NP, Droettboom M, Bourne PE. Ten simple rules for better figures. *PLoS Comput Biol* 2014;10(9):e1003833 | textbook (guidance paper) | no (opened at Task 1) | PMC4161295 (PubMed) | HTML | CC BY 4.0 (to confirm) | C14, C18, C19, C20, C22 |
| Wilke CO. *Fundamentals of Data Visualization*. O'Reilly, 2019; author's manuscript online: ch. 3, 4, 5, 7, 9, 17, 19, 20, 22, 23, 24, 26, 27, 28, 29 | textbook | no (contents and ch. 17 opened at Task 1) | https://clauswilke.com/dataviz/ | HTML | CC BY-NC-ND 4.0 (stated on the site's welcome page) | C14, C15, C16, C17, C18, C19, C20, C21, C22 |
| Bergstrom CT, West JD. The principle of proportional ink (2016) | textbook (teaching page) | no | https://callingbullshit.org/tools/tools_proportional_ink.html (cited by Wilke ch. 17) | HTML | to confirm | C17 |
| Correll M, Bertini E, Franconeri S. Truncating the y-axis: threat or menace? *Proc CHI 2020*: 1-12 | primary | no | arXiv 1907.02035, https://arxiv.org/abs/1907.02035 (use arXiv, not the ACM Digital Library) | PDF / HTML | arXiv licence to confirm | C17 |
| Heer J, Bostock M. Crowdsourcing graphical perception: using Mechanical Turk to assess visualization design. *Proc CHI 2010* (pages to confirm) | primary | no | https://doi.org/10.1145/1753326.1753357; authors' open PDF to locate at intake (not the ACM Digital Library) | PDF | publisher copyright; author copy | C15 |
| Weissgerber TL, Milic NM, Winham SJ, Garovic VD. Beyond bar and line graphs: time for a new data presentation paradigm. *PLoS Biol* 2015;13(4):e1002128 | primary | no | PMC4406565 (PubMed) | HTML | CC BY 4.0 (to confirm) | C16 |
| Bateman S, Mandryk RL, Gutwin C, Genest A, McDine D, Brooks C. Useful junk? The effects of visual embellishment on comprehension and memorability of charts. *Proc CHI 2010* (pages to confirm) | primary | no | https://doi.org/10.1145/1753326.1753716; authors' open PDF to locate at intake | PDF | publisher copyright; author copy | C18 |
| Crameri F, Shephard GE, Heron PJ. The misuse of colour in science communication. *Nat Commun* 2020;11:5444 | primary (review) | no | PMC7595127 (PubMed) | HTML | CC BY 4.0 (to confirm) | C19 |
| Cumming G, Fidler F, Vaux DL. Error bars in experimental biology. *J Cell Biol* 2007;177(1):7-11 | textbook (guidance paper) | no | PMC2064100 (PubMed) | HTML | free to read; licence to confirm | C20 |
| NLM. *Citing Medicine*, 2nd ed. (Patrias K, ed.; NCBI Bookshelf NBK7256): ch. 1 Journals, part A, journal articles; with NLM Sample References (added 2 Oct 2026 for the new concept C05, amendment S58-R1-A02) | guideline | **yes** (2 Oct 2026, group R: `nlm_citing_medicine_2007`, 19/19 verbatim) | https://www.ncbi.nlm.nih.gov/books/NBK7282/ | HTML | public domain (stated on the book page) | C05 |

## To obtain: paywalled or print, which only Harsh can get

| Work, section | Kind | Obtained | Where to get it | Format | Licence | Concepts |
| --- | --- | --- | --- | --- | --- | --- |
| Cleveland WS, McGill R. Graphical perception: theory, experimentation, and application to the development of graphical methods. *J Am Stat Assoc* 1984;79(387):531-554 | primary | no | https://doi.org/10.1080/01621459.1984.10478080 (paywalled; JSTOR) | PDF | publisher copyright | C15 (Heer & Bostock replicates the ranking; C15 can stand on Heer & Bostock plus Wilke if this is not obtained) |
| Tufte ER. *The Visual Display of Quantitative Information*, 2nd ed. Graphics Press, 2001: the Lie Factor and the data-ink ratio (pages to locate) | textbook | no | print only | print | publisher copyright | C17, C18 (optional: both concepts stand on Wilke and Bergstrom & West; the names "Lie Factor" and "data-ink" are written only if this is opened) |
| Flesch R. A new readability yardstick. *J Appl Psychol* 1948;32(3):221-233 | primary | no | https://doi.org/10.1037/h0057532 (paywalled, APA) | PDF | publisher copyright | C11 (optional: Kincaid 1975 states the Reading Ease formula) |

## Portals whose terms forbid automated access

- **JSTOR** (Gopen & Swan's stable copy; Cleveland & McGill): JSTOR's terms prohibit automated downloading. Use the public copies named above, or Harsh downloads by hand.
- **ACM Digital Library** (Correll 2020, Heer & Bostock 2010, Bateman 2010): its terms restrict automated and systematic downloading. Use arXiv or the authors' own copies.
- No Indian statute or government portal is needed for this book, so India Code does not arise.

## Gate

**Written by Task 1:** Blocked: 23 lines say no (20 open, 3 Harsh-only). Four held files serve C02, C09, C17 and C23 in part. Of the 23, three are optional (Tufte, Flesch, Cleveland & McGill), each with a named fallback already in the list; the other 20 are needed. An Indian study of colour-vision deficiency prevalence (for C19's Indian context) was not searched for; intake may add one from PMC.
