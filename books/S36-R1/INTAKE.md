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
