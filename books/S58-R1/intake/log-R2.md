# Source intake log · S58-R1 · group R2 (citing and referencing: reports and web pages)

One pass, 2 Oct 2026, to let the book format a citation to the NFHS-5 India Fact Sheet (Ministry of Health
and Family Welfare / IIPS). Group R held only Citing Medicine chapter 1 (journals); this group adds the
chapters for reports and web pages from the same public-domain work, under a new key.

Method as `INTAKE-BRIEF.md` and `log-R.md`: every fetch `mcp__TinyFish__fetch_content` (markdown). Each
result was taken from this agent's own tool results by `scratchpad/saveraw_R2.py` (saveraw_R.py pointed at
this agent's transcript: reads only results of fetch_content calls, JSON-decodes them and writes the `text`
field unchanged to `raw/R2-*.txt` with a `.meta.json`). Passages were cut by `intake/build-R2.py` as
`raw[i:j]` between anchor strings (offsets in `raw/R2-cutlog.json`); the script re-reads the written file
and tests every [TEXT] passage as a whitespace-normalised substring of its raw; a second check confirmed
each passage equals `raw[i:j]` exactly (36/36). Block 1 also cuts from group R's saved raws of the home page
and the Copyright Notice (no refetch). No WebFetch output stored; no curl, wget or Python HTTP. Nothing
committed; INDEX.yml, library.bib and SOURCES.md untouched (entries in `fragment-R2.md`).

**Verbatim check: 36 of 36. Filed: 1 source file, 7,986 words of passages. Obtained 1/1.**

| Source | URL fetched (stored passages) | Passages | Check | Licence as stated | Citekey |
| --- | --- | --- | --- | --- | --- |
| NLM, *Citing Medicine*, 2nd ed. (Patrias K, ed. Wendling D; 2007-): ch. 4 Scientific and Technical Reports part A; ch. 22 Books and Other Individual Titles on the Internet part A; ch. 25 Web Sites parts A and B (intro) | https://www.ncbi.nlm.nih.gov/books/NBK7280/; https://www.ncbi.nlm.nih.gov/books/NBK7269/; https://www.ncbi.nlm.nih.gov/books/NBK7274/; https://www.ncbi.nlm.nih.gov/books/NBK7256/ (contents) | 36 (4 blocks) | 36/36 | "This publication is in the public domain. For more information, see the Bookshelf Copyright Notice." Notice: "No permission is needed to reproduce or distribute this type of content, but the authoring institute or agency must be given appropriate attribution." | `nlm_citing_medicine_2007_reports_web` |

## What the NFHS-5 citation can stand on

- Which chapter: the fact sheet is a stand-alone document read online, so it is an Internet "book"
  (ch. 22 intro: online books include "technical reports" and a "single-page fact sheet"; ch. 4: "See also
  Chapter 18 and Chapter 22 for information on citing technical reports published in CD-ROM or on the
  Internet"; ch. 25: "Cite a book on a Web site according to Chapter 22"). Chapter 25 (homepage) applies only
  if the book cites the NFHS website itself.
- Shape, by example (ch. 22 ex. 7, organisation as author): "Kaiser Commission on Medicaid and the
  Uninsured. The uninsured and their access to health care [Internet]. Washington: Henry J. Kaiser Family
  Foundation; 2006 Oct [cited 2006 Nov 3]. 2 p. Available from: http://www.kff.org/...pdf". Ch. 22 ex. 49
  adds performing organisation in parentheses, government agency as publisher, Contract/Report No.
- Ch. 4: name both the sponsoring and the performing organisation and say which published; place followed
  by country for lesser-known cities; "Report No.: " if the document carries one.
- **No basic format line is printed in text**: the "general format ... including punctuation" in each
  chapter is an image (ch. 4 shows three empty captions for the three publication scenarios). The book
  must model the format on the held examples, or Harsh can read the image on the page by hand.
- Not held: the "Specific Rules" boxes, other examples, ch. 4 part B, ch. 22 parts B-C, ch. 25 part B rules.

## Tried, and terms

- `https://www.ncbi.nlm.nih.gov/books/n/citmed/ch4/` and `/ch25/`: reCAPTCHA page ("Checking your
  browser"), twice each (second with ttl 0). `/books/n/citmed/A38179/` and `/A59231/` (chapter IDs taken
  from the contents page's links): reCAPTCHA once each. Not retried. The NBK IDs (NBK7280, NBK7274,
  NBK7269) came from two `mcp__TinyFish__search` queries restricted to ncbi.nlm.nih.gov; those three pages
  were then read once each and returned the chapters. Chapter 22 was added beyond the two chapters asked
  for because chapters 4 and 25 both direct online reports to it.
- **For Harsh (terms):** the Bookshelf Copyright Notice forbids crawlers "to systematically retrieve
  content". Group R2 made three chapter reads, one contents-list read and six captcha-blocked attempts,
  each chosen by hand; this agent judged that not systematic retrieval. Together with group R that is now
  five Citing Medicine chapter/appendix pages read. If Harsh reads the notice more strictly, the same
  chapters can be re-taken by hand from the PDF links on NBK7280, NBK7269 and NBK7274.
