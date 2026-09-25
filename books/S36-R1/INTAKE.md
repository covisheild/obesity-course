# Source intake log · S36-R1

One pass on 2026-09-24, before drafting, against the nine "To obtain" lines and the one optional line in `READY.md`.
Every stored passage was fetched with `mcp__TinyFish__fetch_content`. Each result was taken from the tool's own
result record (the session transcript, or the harness's saved result file for large results), decoded from JSON
unchanged and saved to the scratchpad as `intake-raw/<citekey>.txt`. Every passage was cut from that text by
script as a contiguous slice (`raw[i:j]`). The written files were then re-parsed, and each `[TEXT]` run was tested
as a whitespace-normalised substring of the raw fetch. No omission falls inside a run. What lies between runs is
listed in each file's header. No WebFetch output is stored anywhere, and nothing was fetched with curl, wget or a
Python HTTP client. All nine articles' PMIDs, PMCIDs and DOIs were confirmed with the PubMed tool
(`get_article_metadata`).

**Verbatim check: 21 of 21.** Most runs are whole articles, so a passage here is often several thousand words.
There are 13 runs across the six text sources and 1 run in each of the three OCR files. Of those 21, 4 are
DeJonckheere & Vaughn, 1 each Pope/Ziebland/Mays, Mays & Pope and Green & Britten, 4 McMullin, 7 ICMR, and 1 each
Kitzinger, Britten and Pope & Mays 1995.

**PMC pages were unreliable for the tool.** The same article page returned full text on one call, then
`empty_content` or a "Cookies must be enabled" wall on the next. Where the page failed, the PMC Open Access XML
was used instead (DeJonckheere & Vaughn; McMullin). For the three BMJ 1998/2000 articles the page came through as
markdown, and the file is cut from that.

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| DeJonckheere & Vaughn 2019 *Fam Med Community Health* 7:e000057: licence, abstract, whole body with Tables 1–6, end matter | https://pmc-oa-opendata.s3.amazonaws.com/PMC6910737.1/PMC6910737.1.xml (the PMC page returned no content) | 4 | 4/4 | "© Author(s) (or their employer(s)) 2019. Re-use permitted under CC BY-NC. No commercial re-use." … "Creative Commons Attribution Non Commercial (CC BY-NC 4.0) license" (PMC XML) | `dejonckheere_vaughn_2019` (new) |
| Pope, Ziebland & Mays 2000 *BMJ* 320:114: whole article, references omitted | https://pmc.ncbi.nlm.nih.gov/articles/PMC1117368/ (markdown, third try); the Europe PMC PDF text layer was also fetched, and its wording agrees | 1 | 1/1 | none on the page as returned; the PDF footer reads only "BMJ VOLUME 320 8 JANUARY 2000 www.bmj.com" | `pope_ziebland_mays_2000` (new) |
| Mays & Pope 2000 *BMJ* 320:50: whole article, references omitted | https://pmc.ncbi.nlm.nih.gov/articles/PMC1117321/ | 1 | 1/1 | none on the page as returned | `mays_pope_2000` (new) |
| Green & Britten 1998 *BMJ* 316:1230: whole article, references omitted | https://pmc.ncbi.nlm.nih.gov/articles/PMC1112988/ | 1 | 1/1 | none on the page as returned | `green_britten_1998` (new) |
| McMullin 2023 *Voluntas* 34:140: rights, abstract, whole body, notes | https://pmc-oa-opendata.s3.amazonaws.com/PMC8432276.1/PMC8432276.1.xml (the PMC page returned no content; link.springer.com shows the abstract only) | 4 | 4/4 | "© International Society for Third-Sector Research 2021 … made available via the PMC Open Access Subset … These permissions are granted for the duration of the World Health Organization (WHO) declaration of COVID-19 as a global pandemic." (PMC XML) | `mcmullin_2023` (new) |
| ICMR *National Ethical Guidelines* 2017: title and copyright page, contents, 2.1.4–2.3, 3.4–3.5.1, 4.8 with Table 4.2, Section 5 whole, Section 9 whole | https://www.icmr.gov.in/icmrobject/custom_data/pdf/resource-guidelines/ICMR_Ethical_Guidelines_2017.pdf (the PDF's own text layer) | 7 | 7/7 | "© Copyright Indian Council of Medical Research The use of content from this book is permitted for all non-commercial purposes giving full acknowledgement to ICMR" (copyright page) | `icmr_ethical_guidelines_2017` (new) |
| Kitzinger 1995 *BMJ* 311:299, whole article, **OCR** | https://europepmc.org/api/getPdf?pmcid=PMC2550365 | 1 | 1/1 | none on the PMC page (abstract, "Full text: PDF", references) | `kitzinger_1995` (new) |
| Britten 1995 *BMJ* 311:251, whole article, **OCR** | https://europepmc.org/api/getPdf?pmcid=PMC2550292 | 1 | 1/1 | not seen: the PMC page did not load for the tool | `britten_1995` (new) |
| Pope & Mays 1995 *BMJ* 311:42, whole article, **OCR** | https://europepmc.org/api/getPdf?pmcid=PMC2550091 | 1 | 1/1 | none on the PMC page: a link labelled "PMC Copyright notice", no licence text | `pope_mays_1995` (new) |

## The three scanned 1995 papers: OCR outcome

Europe PMC's `getPdf` route returned an OCR text layer for all three scans, covering the whole of each article.
The pages also carry the tail of the article before and, for Pope & Mays, a short piece after, and those were cut
away. The layer is usable but poor.

- **Spaces are gone.** Almost every space between words has been dropped ("Focusgroupsareaformofgroupinterview").
  The quote check normalises only whitespace and case, so a drafter's quote passes only if it is written unspaced,
  as in the file. A spaced, correct quotation will fail the check.
- **OCR misreadings are visible** ("COMPOSrITON", "voLuME", "medicaljournai", "BMJh"), and part of page 44 of
  Pope & Mays is a line of symbols.
- **Reading order is the layer's.** Margin notes, boxes and running heads are interleaved with the columns.

Each file's header says it is an OCR text layer of page images and that every quote must be checked by a person
against the page image. A machine pass proves only that the OCR says it. The headings and box titles named in
`SOURCES.md` were found in the OCR, and nothing in these files has yet been read against the images.

## Findings for the gate

- **C11 (talk share).** DeJonckheere & Vaughn do **not** say in words that the participant should do most of the
  talking. The nearest statements are "we recommend: prioritising listening over talking" (Conclusions), the
  DiCicco-Bloom and Crabtree quotation "the goal of the interviewer is to encourage the interviewee to share as much
  information as possible, unselfconsciously and in his or her own words" (Continuing the interview), and "Listening
  is the key to successful interviewing" (Active listening). As `READY.md` provides, C11 rests on the map's gate and
  Book 0 A4 and A5. These lines may be cited as context, not as the rule.
- **C07 (ICMR).** `READY.md`'s pointers need correcting against the text. **3.5.1 is about authorship**: research
  done "as part of a mandatory requirement of a course/fellowship/training programme including student research
  should have the candidate as the primary author". It says nothing about review. **2.2.2 is on recording the
  consent process** "in certain clinical trials as notified by CDSCO", not on recording interviews. What bears on a
  learner's pilot is:
  - Table 2.1, where "research involving routine questioning or history taking" is an example of minimal risk;
  - Table 4.2, where exemption covers "less than minimal risk where there are no linked identifiers", and an
    audio-recorded named interview is not obviously that;
  - 4.8.3, "A researcher cannot decide that her/his proposal falls in the exempted, expedited or full review
    category. All research proposals must be submitted to the EC";
  - Section 9's requirement of "prior permission from the EC with justifiable reasons for audio/…" recording.

  No sentence in the held sections exempts course or practice interviews.
- **C10 (translation).** McMullin says little on translation: transcription as translating audio into text, and
  one quoted example "recorded, translated, and transcribed verbatim". Nothing supports "transcribe in the language
  spoken, translate afterwards, keep the original". That point has no anchor in the held sources.
- **C09 cues.** Bergen & Labonté 2020 has no open copy. Europe PMC says "Subscription required" and the article
  is not in PMC. OpenAlex gives `oa_status` "closed" and `any_repository_has_fulltext` false. Nothing was filed.
  C09 cannot list named cues of social desirability from a held source.

## Not obtained

| Source | Why | Where Harsh can get it |
| --- | --- | --- |
| Bergen & Labonté 2020 *Qual Health Res* 30:783 (optional) | Paywalled; no author manuscript in any repository (OpenAlex, Europe PMC, 2026-09-24) | Publisher, https://doi.org/10.1177/1049732319889354, or the authors |
| DeJonckheere & Vaughn 2019, Figure 1 and supplementary appendix A (the sample interview guide) | Figure 1 is an image; the appendix is a separate supplementary file, not fetched | The PMC article page |
| Page-image check of the three OCR files | Needs a person to read the scans | The PDF on each PMC article page |

## Caveats found during intake

- **McMullin's licence is not open.** `READY.md` recorded "open access (Europe PMC)". PMC's own XML shows a
  COVID-19 collection permission, time-limited to the WHO pandemic declaration, over an ISTR copyright, and the
  publisher's page is subscription-only. Short quotation for audit is unaffected. Whether the permission still
  runs is Harsh's decision. WHO ended the COVID-19 public-health emergency in May 2023; that is general knowledge
  and was not fetched at intake.
- **BMJ licences.** For the five BMJ articles, the PMC page as returned carries no licence and no copyright line.
  They are recorded as "none stated", not assumed open. Boxes and tables are not to be reproduced.
- **DeJonckheere & Vaughn's XML flattening** runs citation numbers onto words ("research.8") and splits one
  quotation across a line. The file header says so.
- **ICMR text layer.** Line breaks, page numbers and running heads remain inside the runs. Bulleted lines carry TAB
  characters between words, and some words are split ("Address ing"). Boxes are interleaved out of visual order:
  3.5.1's course sentence begins "Research performed" before Box 3.3 and continues after it.
- **Raw fetches** are in the session scratchpad (`intake-raw/`), not in the repository, as for S02-R1.

## Addendum, 2026-09-24: a research-methods textbook (`blackstone_2012`)

Asked for by the conductor: derivable records need a `textbook` reference, and the BMJ methods papers are
articles. The method is the same as above (TinyFish `fetch_content` only, raw saved to `intake-raw/blackstone_2012__<section>.txt`,
passages cut by script, re-checked). **Verbatim check: 12 of 12.**

| Source | URL fetched | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| *Principles of Sociological Inquiry: Qualitative and Quantitative Methods* v1.0 (Saylor Academy 2012; Amy Blackstone): licence page; sections 1.1, 1.2, 2.3, 3.1, 3.2, 5.2, 7.2, 9.1, 9.2, 9.4, 12.1, each whole without its exercises | https://saylordotorg.github.io/text_principles-of-sociological-inquiry-qualitative-and-quantitative-methods/ and one page per section (markdown, `include_selectors: ["body"]`) | 12 | 12/12 | "This text was adapted by Saylor Academy under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License without attribution as requested by the work's original creator or licensor." (licence page) | `blackstone_2012` (new) |

- **Edition.** The first choice, the University of Minnesota edition (open.lib.umn.edu/sociologicalinquiry),
  returned HTTP 404 on every path tried. Saylor Academy's own HTML copy of the 2012 book was used instead.
- **Author attribution.** The Saylor edition names no author, at the creator's request. The author is Amy
  Blackstone, going by the UMN and LibreTexts editions; the LibreTexts one was seen only as a search result.
  Her own name appears in the text as a citation ("Uggen & Blackstone, 2004"). The `.bib` gives her as author,
  and its note records the caveat.
- **Extraction.** Unscoped markdown silently dropped headings, lists and the Learning Objectives and Key
  Takeaways boxes. For example, 1.2's "the following considerations:" was followed by nothing. Every
  section was therefore refetched scoped to `body`, which returns them. Glossary definitions and footnotes
  are run into the text, as the header warns.
- **Not held.** Figures (Figure 3.6 sample consent form; Figures 9.4 and 9.5 sample interview guides) are
  images. 9.3 (quantitative interviews), the chapter introductions and all exercise sets were not taken.

## v1.1, 2026-09-24/25: Indian data-protection law for C07

Asked for so that C07 (consent, recording and privacy) can teach the DPDP Act and Rules alongside ICMR. The
method is the same as above. TinyFish `fetch_content` was the only tool used. Each result was decoded
unchanged from the session's tool-result record into `intake-raw/<citekey>.txt`, and every run was cut by
script as `raw[i:j]` and re-tested against the raw text. **Verbatim check: 4 of 4.** All four runs are also
exact byte substrings of the raw fetch. The session crossed midnight, so the Act was fetched on 25
September; the other two were fetched on 24 September.

| Source | URL fetched | Runs | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| Digital Personal Data Protection Act 2023 (Act 22 of 2023), Gazette of India Extraordinary Part II s.1 No. 25, 11 Aug 2023: whole Act as enacted, ss.1-44 and the Schedule | https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf (PDF text layer) | 1 | 1/1 | none stated | `dpdp_act_2023` (new) |
| G.S.R. 843(E), 13 Nov 2025, MeitY, commencement under s.1(2), Gazette No. 757: whole, Hindi and English | https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf (PDF text layer) | 1 | 1/1 | none stated | `dpdp_commencement_2025` (new) |
| DPDP Rules 2025, G.S.R. 846(E), 13 Nov 2025, Gazette No. 760: masthead lines, and the whole English text (rules 1-23 and Schedules I-VII); Hindi version omitted | https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf (PDF text layer) | 2 | 2/2 | none stated | `dpdp_rules_2025` (new) |

- **Host.** India Code (`indiacode.nic.in`, handle 123456789/22037) returned `target_unreachable` on two
  paths. The Act is therefore the Gazette copy hosted by MeitY. It is the text **as enacted**, not a
  consolidation, and no search was made for later amendments.
- **Commencement exists and is held.** G.S.R. 843(E) is a separate Gazette issue (No. 757), not the one that
  carries the Rules (No. 760). It appoints three stages: on publication, after one year, and after eighteen
  months. Neither notification gives calendar dates for the later stages. See `DPDP-FACTS.md` §1.
- **Hindi text layers are garbled** in both 2025 notifications, with conjuncts decomposed by a legacy
  font mapping. The commencement file holds the Hindi because the run is the whole fetch. The Rules file
  omits it. Quote the English only.
- **Layout.** In the Act, marginal notes and the citations of other Acts print at the foot of each page's
  text, so a quote that crosses a page needs "…". The Schedule's table comes out column by column. The
  Rules' tables are flattened.
- **Licence.** None of the three documents states a licence or copyright. They are recorded as Government
  of India legislation, with nothing assumed.

**Findings for the gate (C07).** Details and exact words are in `DPDP-FACTS.md`.

- On 24 September 2026 only the definitions (s.2), the Board provisions and a few others are in force.
  Notice (s.5), consent and withdrawal (s.6(1)-(8), (10)), the Fiduciary's duties (s.8), children (s.9)
  and the exemptions (s.17, including the research exemption s.17(2)(b)) come in at eighteen months. So do
  Rules 3, 5-16 (rule 16 and the Second Schedule among them). C07 must not present these as current duties.
- "Research" is not defined in the Act or the Rules. Nothing in either says whether a student's practice
  interview is research, or whether it falls under the "personal or domestic purpose" exclusion
  (s.3(c)(i)).
- The Act does not require written consent. The written-consent rule C07 now teaches is ICMR's, and it
  should stay attributed to ICMR.
