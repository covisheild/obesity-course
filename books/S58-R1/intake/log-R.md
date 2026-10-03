# Source intake log · S58-R1 · group R (citing and referencing: the Vancouver details)

One pass, 2 Oct 2026, after Harsh accepted the five coverage gaps (COVERAGE.md) and placed "citing and
referencing" in S58-R1 as a new concept. ICMJE section IV.A.3.g (held, `icmje_2026_manuscript_preparation`)
gives the principles and points to "the NLM's Sample References webpage" and "the NLM's Citing Medicine,
2nd edition" for the format; this group takes in that one open source for the format details.

Method as `INTAKE-BRIEF.md`: every fetch `mcp__TinyFish__fetch_content` (markdown). Each result was taken
from this agent's own tool results (inline in the transcript, or the harness's saved tool-result file) by
`scratchpad/saveraw_R.py` (same logic as `saveraw_F.py`: reads only results of fetch_content calls,
JSON-decodes them and writes the `text` field unchanged to `raw/R-*.txt` with a `.meta.json`). Passages were
cut by `intake/build-R.py` as `raw[i:j]` between anchor strings (offsets in `raw/R-cutlog.json`); the same
script re-reads the written file from disk and tests every [TEXT] passage as a whitespace-normalised
substring of the raw named in its block. No WebFetch output stored; nothing fetched with curl, wget or a
Python HTTP client. Nothing committed; INDEX.yml, library.bib and SOURCES.md untouched (entries in
`fragment-R.md`).

**Verbatim check: 19 of 19. Filed: 1 source, 2,609 words of passages. Obtained 1/1.**

| Source | URL fetched (stored passages) | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| NLM, *Citing Medicine*, 2nd ed. (Patrias K, ed. Wendling D; 2007-), ch. 1 Journals part A, appendix B opening; plus NLM *Samples of Formatted References* (separate page) | https://www.ncbi.nlm.nih.gov/books/NBK7256/; https://www.ncbi.nlm.nih.gov/books/about/copyright/; https://www.ncbi.nlm.nih.gov/books/NBK7282/; https://www.ncbi.nlm.nih.gov/books/NBK7253/; https://www.nlm.nih.gov/bsd/uniform_requirements.html | 19 (5 blocks) | 19/19 | Book page: "This publication is in the public domain. For more information, see the Bookshelf Copyright Notice." Notice: U.S. government content, "No permission is needed to reproduce or distribute this type of content, but the authoring institute or agency must be given appropriate attribution." Sample References page: no licence on the page (NLM web page) | `nlm_citing_medicine_2007` |

## What C-referencing can now stand on

- Format, by example: "Petitti DB, Crooks VC, Buckwalter JG, Chiu V. Blood pressure levels before dementia.
  Arch Neurol. 2005 Jan;62(1):112-6." (Citing Medicine example 1; Sample References item 1 is the same shape).
- Authors: surname first, "a maximum of two initials", "Give all authors, regardless of the number";
  optional limit to 3 or 6 then "et al." (example 3). The Sample References page says "List the first six
  authors, followed by et al." with "(Note: NLM now lists all authors.)": the book should say journals
  decide, and name both.
- Article title: capitalise only the first word, proper nouns and acronyms. Journal title: abbreviated (ISO 4),
  look the abbreviation up in the NLM Catalog first (appendix B); ICMJE §3.g says the same ("MEDLINE",
  nlmcatalog/journals).
- Date;volume(issue):pages, with "123-125 becomes 123-5"; "Cite the version you saw"; a preprint is marked
  "[Preprint]" (Sample References item 34, with arXiv and bioRxiv examples).
- Not held: the format diagram (an image on the page), the collapsed "Specific Rules" boxes, chapter 14
  (manuscripts and preprints) and chapter 23 (journals on the Internet). Not needed for a rung-1 concept.

## Tried, and terms

- First fetch of NBK7282 returned a reCAPTCHA page ("Checking your browser"); a second single fetch
  (ttl 0) returned the chapter. `Bookshelf_NBK7282.pdf`: `target_unreachable`. Not retried further.
- **For Harsh (terms):** the Bookshelf Copyright Notice says "Crawlers and other automated processes may
  NOT be used to systematically retrieve content from the Bookshelf web site." This intake made five single
  page reads chosen by hand (contents page twice, once to list links; chapter 1 twice because of the
  captcha; appendix B; the notice), which this agent judged not to be systematic retrieval; robots.txt for
  User-agent * disallows only `/books/?term=` under /books. The content is public domain. If Harsh reads
  the notice more strictly, the chapter can be re-taken by hand from the PDF link on NBK7282.
