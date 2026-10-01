# Source intake log · S58-R1 · group A (scientific writing)

One pass, 2026-10-02 (sandbox clock 2026-10-01 UTC), against the seven group-A works in `READY.md`
"To obtain": ICMJE Preparing a Manuscript, Sollaci and Pereira 2004, Mensh and Kording 2017, OpenStax
*Writing Guide with Handbook*, Gopen and Swan 1990, the Federal Plain Language Guidelines, Barnett and
Doubleday 2020. Tool for every stored passage: `mcp__TinyFish__fetch_content` (markdown). Each result
was taken from this agent's own tool result (inline in the session transcript, or the harness's
saved tool-result file for large ones), JSON-decoded, and its `text` written unchanged to
`raw/A-<source>-<route>.txt`, with the rest of the result (url, final_url, title, where the result
came from) in a `.meta.json` beside it (`saveraw_A.py`, scratchpad). Every passage was cut by script
from that text as one contiguous `raw[i:j]`, located by unique start and end anchors or, for the Plain
Language PDF, by the raw file's line numbers (`build-A.py`); every written file was then re-parsed and
each passage tested as a whitespace-normalised substring of the raw fetch for the URL on its block's
FETCHED line (`verify-A.py`; `build-A.py` also writes `manifest-A.json`, every passage with its raw file and URL). No WebFetch output is stored; nothing was
fetched with curl, wget or a Python HTTP client. Identifiers were confirmed with the PubMed tools
(`convert_article_ids`, `get_article_metadata`). Nothing was committed; `sources/INDEX.yml`,
`library.bib` and `SOURCES.md` were not touched (entries are in `fragment-A.md`).

**Verbatim check: 33 of 33.** **Obtained: 7 of 7.** Five are whole texts (less references), two are
excerpts chosen to the inventory (ICMJE IV.A.1 and IV.A.3.a-k; the Plain Language sections).

| Source | URL fetched (stored passages) | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| ICMJE Recommendations, **IV.A** (not II.A) Preparing a Manuscript: 1 General Principles; 3.a-k Manuscript Sections. Version: "Updated January 2026" | https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html; https://www.icmje.org/recommendations/ (version line); https://www.icmje.org/recommendations/browse/manuscript-preparation/ (section heading); https://www.icmje.org/about-icmje/faqs/icmje-recommendations/ (reuse, citation) | 6 | 6/6 | No licence. FAQ: "Other organizations should not reprint in their own publications or post the ICMJE recommendations on their own websites, but are welcome to post a link to the freely available, periodically updated official version on www.ICMJE.org." | `icmje_2026_manuscript_preparation` |
| Sollaci and Pereira 2004 *J Med Libr Assoc* 92(3):364-7 (PMID 15243643, PMC442179) | https://pmc.ncbi.nlm.nih.gov/articles/PMC442179/ (the PMC OA S3 XML returned 404: not in the OA subset) | 2 | 2/2 | "Copyright © 2004, Medical Library Association" (PMC page) | `sollaci_pereira_2004_imrad` |
| Mensh and Kording 2017 *PLoS Comput Biol* 13(9):e1005619 (PMID 28957311, PMC5619685), and its correction e1005830 (PMC5679512) | https://pmc-oa-opendata.s3.amazonaws.com/PMC5619685.1/PMC5619685.1.xml; https://pmc-oa-opendata.s3.amazonaws.com/PMC5679512.1/PMC5679512.1.xml | 3 | 3/3 | "This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited." (CC BY 4.0 link) | `mensh_kording_2017_structuring_papers` |
| OpenStax *Writing Guide with Handbook* (2021; web version Apr 23, 2026): Handbook H2 Effective Paragraphs, H3 Clear and Effective Sentences, H7 opening; 6.6 opening; 3.6 Revising Common Sentence Patterns | https://openstax.org/details/books/writing-guide; https://openstax.org/books/writing-guide/pages/handbook; https://openstax.org/books/writing-guide/pages/6-6-editing-focus-subject-verb-agreement; https://openstax.org/books/writing-guide/pages/3-6-editing-focus-sentence-structure | 6 | 6/6 | "by OpenStax is licensed under Creative Commons Attribution-NonCommercial-ShareAlike License v4.0" (details page) | `openstax_writing_guide_handbook` |
| Gopen and Swan 1990 *Am Sci* 78(6):550-558 | https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf (PDF text layer; JSTOR not fetched) | 1 | 1/1 | Reprint's own line: "originally appeared in American Scientist, journal of Sigma Xi, copyright © 1990 by Sigma Xi, The Scientific Research Society. Reprinted with the permission of American Scientist." No open licence | `gopen_swan_1990_scientific_writing` |
| PLAIN, *Federal Plain Language Guidelines*, March 2011, Rev. 1 May 2011 | https://wid.org/wp-content/uploads/2022/03/FederalPLGuidelines.pdf (PDF text layer); https://www.plainlanguage.gov/guidelines/ (now redirects to digital.gov; one block, to record that) | 11 | 11/11 | None stated in the PDF. U.S. federal work (17 U.S.C. 105): this log's inference, not the document's statement | `plain_language_2011_guidelines` |
| Barnett and Doubleday 2020 *eLife* 9:e60080 (PMID 32701448, PMC7556863) | https://pmc-oa-opendata.s3.amazonaws.com/PMC7556863.1/PMC7556863.1.xml | 4 | 4/4 | "This article is distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use and redistribution provided that the original author and source are credited." (CC BY 4.0 link) | `barnett_doubleday_2020_acronyms` |

## Sections identified at intake

- **ICMJE.** The manuscript-preparation material is Section **IV** ("IV. Manuscript Preparation and
  Submission"), part A. READY.md and the brief call it II.A; Section II is Roles and Responsibilities
  (the page itself cross-refers to "section II.E" for protection of participants). Concepts should
  cite IV.A.1 and IV.A.3.a-k. INVENTORY.md's "§A.3.e", "§A.3.k" and so on are right once prefixed IV.
- **OpenStax Writing Guide.** The Handbook is one web page (H1-H13). Paragraph structure is H2 >
  Effective Paragraphs > Developing a Main Point (topic sentence) and Supporting Evidence and Analysis
  (development). Sentence structure is H3 Clear and Effective Sentences: Active Voice, Conciseness,
  and Variety (simple, compound, complex sentences, which define main and subordinate clauses). The
  Handbook does not define "subject" by itself; the chapter section 6.6 does ("The subject of a
  sentence names something. The predicate contains the verb ..."), and H7 opens with the verb
  definition. Section 3.6 gives the "doer"/"action" rewrite and the 49-to-3-word wordiness example.
- **Plain Language Guidelines.** The four sections the prompt names are III.a.1.i Use active voice
  (pp. 20-21), III.a.3.i Use short, simple words (pp. 36-37), III.a.3.ii Omit unnecessary words
  (pp. 38-40) and III.b.1 Write short sentences (pp. 50-51). Also held, because C06, C07, C09 and C11
  name them: hidden verbs, verbs into nouns, minimize abbreviations, same term consistently,
  subject-verb-object close together, topic sentence, one topic per paragraph.

## Things that need Harsh

1. **ICMJE reuse.** READY.md's licence guess ("free to reproduce for non-commercial education") is
   not what ICMJE says: its FAQ asks other organizations not to reprint or post the Recommendations,
   only to link. The file is held for audit quotation. The book should quote short phrases and link
   to icmje.org, not reproduce sections. Harsh's call whether that is acceptable or whether to ask
   ICMJE.
2. **Gopen and Swan** is held from a retyped reprint (usenix.org, via Penn State), not the typeset
   *American Scientist* pages: wording is the article's, but there are no page numbers and no boxes.
   If page locators are wanted, Harsh would download the JSTOR copy by hand
   (https://www.jstor.org/stable/29774235) or the author's page copy
   (https://georgegopen.com/scientific-writing-articles/, not tried).
3. **Plain Language Guidelines**: plainlanguage.gov is offline (redirects to digital.gov; GSA's GitHub
   archive is read-only and its PDF path was unreachable). The copy held is the 2011 Rev. 1 PDF as
   reposted by the World Institute on Disability. If Harsh prefers a government-hosted copy, the GSA
   archive (https://github.com/GSA/plainlanguage.gov) holds the later web versions of the
   guidelines as Markdown pages; they were listed but not fetched or compared with the 2011 PDF.
4. **Sollaci and Pereira pages**: PubMed says 364-7, the PMC page header 364-371. Cited as PubMed.

## Not obtained

Nothing in group A. Not used: the ICMJE PDF (web version used instead; same content, the official
version per the FAQ); Gopen and Swan on JSTOR (forbidden to fetch).
