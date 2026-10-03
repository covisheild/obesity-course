# S58-R1 intake, group A (scientific writing): entries to merge

Three blocks for the conductor to paste into `sources/INDEX.yml` (under `files:`),
`check/references/library.bib` (append) and `sources/SOURCES.md` (a new section). Seven files for
the seven assigned works. Citekeys were grepped in `sources/INDEX.yml` and
`check/references/library.bib` on 2026-10-02, at the start and again at the end of intake: none
exists. Grep again at merge, since S47-R1 and S52-R1 are adding keys on other branches.

## 1. `sources/INDEX.yml`, under `files:`

```yaml
  icmje_2026_manuscript_preparation:
    file: icmje_2026_manuscript_preparation.txt
    what: >-
      ICMJE Recommendations, updated January 2026, web version. Section IV.A (not II.A): IV.A.1 General
      Principles (IMRAD) and IV.A.3.a-k Manuscript Sections whole (title page, abstract, introduction, methods,
      results, discussion, references, tables, figures, units, abbreviations); version line; ICMJE FAQ on
      reprinting and citing. IV.A.2 Reporting Guidelines NOT held. Not openly licensed; FAQ asks others not to
      reprint or post - brief quotation only
  sollaci_pereira_2004_imrad:
    file: sollaci_pereira_2004_imrad.txt
    what: >-
      Sollaci and Pereira, J Med Libr Assoc 2004;92(3):364-7 (PMC442179; copyright Medical Library
      Association), PMC article page. Whole text: abstract, methods (n = 1,297, four journals, 1935-1985),
      results, discussion, figure captions. Figure values (images) and references NOT held
  mensh_kording_2017_structuring_papers:
    file: mensh_kording_2017_structuring_papers.txt
    what: >-
      Mensh and Kording, PLoS Comput Biol 2017;13(9):e1005619 (CC BY 4.0), PMC OA XML. Whole text: Overview,
      Introduction, Rules 1-10, Table 1 (rules and signs of violation), Fig 1 caption, Discussion; plus the
      correction notice (e1005830, Fig 1 key only). Fig 1 image, acknowledgement names and references NOT held
  openstax_writing_guide_handbook:
    file: openstax_writing_guide_handbook.txt
    what: >-
      OpenStax Writing Guide with Handbook (2021; web version Apr 23 2026; CC BY-NC-SA 4.0). Excerpts: Handbook
      H2 Effective Paragraphs (main point, topic sentence, supporting evidence); H3 Clear and Effective
      Sentences whole (emphasis, active voice, conciseness, parallelism, main and subordinate clauses); H7 verb
      definition; 6.6 subject and predicate defined; 3.6 doers and actions, wordiness. Example markup appears
      as literal "underline ... end underline"
  gopen_swan_1990_scientific_writing:
    file: gopen_swan_1990_scientific_writing.txt
    what: >-
      Gopen and Swan, Am Sci 1990;78(6):550-558 (copyright Sigma Xi), retyped reprint PDF on usenix.org (via
      Penn State Style for Students Online), text layer. Whole article (reader expectations, subject-verb
      separation, stress and topic positions, logical gaps, locating the action) without the bibliography. Not
      the typeset article: no page numbers, boxes or figures
  plain_language_2011_guidelines:
    file: plain_language_2011_guidelines.txt
    what: >-
      Federal Plain Language Guidelines, March 2011, Rev. 1 May 2011 (PLAIN; US government work, no licence
      line), third-party copy of the PDF on wid.org, text layer. Sections whole: use active voice, avoid hidden
      verbs, don't turn verbs into nouns, minimize abbreviations, short simple words, omit unnecessary words,
      same term consistently, short sentences, subject-verb-object close, topic sentence, one topic per
      paragraph. Two-column tables flattened
  barnett_doubleday_2020_acronyms:
    file: barnett_doubleday_2020_acronyms.txt
    what: >-
      Barnett and Doubleday, eLife 2020;9:e60080 (CC BY 4.0), PMC OA XML. Whole text: abstract, impact
      statement, Introduction with Box 1, Results with Table 1 (top 20 acronyms), Discussion, Methods with
      Tables 2-3, Limitations. Figures (images), references and Appendix 1 NOT held
```

## 2. `check/references/library.bib`, append

```bibtex
@misc{icmje_2026_manuscript_preparation,
  title        = {Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly
                  Work in Medical Journals. {IV.A}: Preparing a Manuscript for Submission to a
                  Medical Journal},
  author       = {{International Committee of Medical Journal Editors}},
  year         = {2026},
  note         = {Updated January 2026. Section IV.A.1 (General Principles) and IV.A.3.a-k
                  (Manuscript Sections) quoted from the web version. Not openly licensed: ICMJE asks
                  other organizations not to reprint or post the Recommendations and to link to
                  icmje.org instead},
  howpublished = {ICMJE website},
  url          = {https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html},
  urldate      = {2026-10-02}
}

@article{sollaci_pereira_2004_imrad,
  title        = {The introduction, methods, results, and discussion ({IMRAD}) structure: a fifty-year
                  survey},
  author       = {Sollaci, Luciana B and Pereira, Mauricio G},
  journal      = {Journal of the Medical Library Association},
  year         = {2004},
  volume       = {92},
  number       = {3},
  pages        = {364--367},
  note         = {PMID 15243643, PMC442179. Copyright 2004 Medical Library Association; free to read
                  in PubMed Central, not in its open-access subset. Pages as in PubMed (the PMC page
                  header reads 364-371). Quoted from the PubMed Central article page},
  url          = {https://pmc.ncbi.nlm.nih.gov/articles/PMC442179/},
  urldate      = {2026-10-02}
}

@article{mensh_kording_2017_structuring_papers,
  title        = {Ten simple rules for structuring papers},
  author       = {Mensh, Brett and Kording, Konrad},
  journal      = {PLoS Computational Biology},
  year         = {2017},
  volume       = {13},
  number       = {9},
  pages        = {e1005619},
  doi          = {10.1371/journal.pcbi.1005619},
  note         = {PMID 28957311, PMC5619685. CC BY 4.0. Correction (Fig 1 key) in PLoS Comput Biol
                  2017;13(11):e1005830. Quoted from the PubMed Central open-access text},
  url          = {https://doi.org/10.1371/journal.pcbi.1005619},
  urldate      = {2026-10-02}
}

@book{openstax_writing_guide_handbook,
  title        = {Writing Guide with Handbook},
  author       = {Robinson, Michelle Bachelor and Jerskey, Maria and Fulwiler, Toby},
  publisher    = {OpenStax, Rice University},
  address      = {Houston, Texas},
  year         = {2021},
  note         = {Licensed CC BY-NC-SA 4.0. Published 21 December 2021; web version last updated
                  23 April 2026. Digital PDF ISBN 978-1-951693-47-3. Handbook sections H2 (Effective
                  Paragraphs), H3 (Clear and Effective Sentences) and H7, and sections 3.6 and 6.6
                  quoted},
  url          = {https://openstax.org/books/writing-guide/pages/handbook},
  urldate      = {2026-10-02}
}

@article{gopen_swan_1990_scientific_writing,
  title        = {The science of scientific writing},
  author       = {Gopen, George D and Swan, Judith A},
  journal      = {American Scientist},
  year         = {1990},
  volume       = {78},
  number       = {6},
  pages        = {550--558},
  note         = {Copyright 1990 Sigma Xi, The Scientific Research Society. Quoted from a retyped
                  reprint "with the permission of American Scientist" (no page numbers), publicly
                  posted on usenix.org},
  url          = {https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf},
  urldate      = {2026-10-02}
}

@manual{plain_language_2011_guidelines,
  title        = {Federal Plain Language Guidelines},
  author       = {{Plain Language Action and Information Network}},
  year         = {2011},
  note         = {March 2011, Revision 1, May 2011. U.S. federal government work; the document states
                  no copyright or licence. The plainlanguage.gov copy is offline (the site redirects
                  to digital.gov); quoted from the 2011 PDF as reposted by the World Institute on
                  Disability. Sections III.a-III.c quoted with the document's page numbers},
  url          = {https://wid.org/wp-content/uploads/2022/03/FederalPLGuidelines.pdf},
  urldate      = {2026-10-02}
}

@article{barnett_doubleday_2020_acronyms,
  title        = {The growth of acronyms in the scientific literature},
  author       = {Barnett, Adrian and Doubleday, Zoe},
  journal      = {eLife},
  year         = {2020},
  volume       = {9},
  pages        = {e60080},
  doi          = {10.7554/eLife.60080},
  note         = {PMID 32701448, PMC7556863. CC BY 4.0. Quoted from the PubMed Central open-access
                  text},
  url          = {https://doi.org/10.7554/eLife.60080},
  urldate      = {2026-10-02}
}
```

## 3. `sources/SOURCES.md`, a new section

```markdown
## Added by the S58-R1 source intake, group A (scientific writing), 2026-10-02

Every passage was cut by script (`books/S58-R1/intake/build-A.py`) from the raw text the TinyFish
`fetch_content` tool returned (saved from the tool's own result, not retyped) and re-checked as a
whitespace-normalised substring of that fetch (`verify-A.py`): **33 of 33**. Log in
`books/S58-R1/intake/log-A.md`. Two files rest on copies not served by the original publisher (Gopen
and Swan: a retyped reprint on usenix.org; the Plain Language Guidelines: the 2011 PDF reposted by
the World Institute on Disability, since plainlanguage.gov is offline), and each header says so. The
ICMJE section is IV.A, not II.A as READY.md had it.

| File | What it is | Words | Verified in it |
| --- | --- | --- | --- |
| `icmje_2026_manuscript_preparation.txt` | ICMJE Recommendations, updated January 2026, IV.A.1 and IV.A.3.a-k (web version), with the ICMJE FAQ on reprinting and citing. **Excerpts**; not openly licensed | 4,577 | IMRAD "not an arbitrary publication format but a reflection of the process of scientific discovery"; abstract: context, purpose, basic procedures, main findings, principal conclusions, "information in abstracts often differs from that in the text"; results "giving the main or most important findings first", "absolute numbers from which the derivatives were calculated", "do not duplicate data in graphs and tables", nontechnical uses of "random", "normal", "significant", "correlations", "sample"; discussion begins by summarizing main findings, then mechanisms, limitations, implications; figures legible when reduced and self-explanatory; abbreviations spelled out at first mention, none in the title |
| `sollaci_pereira_2004_imrad.txt` | Sollaci and Pereira 2004, *J Med Libr Assoc* 92:364, PMC page. **Whole text** except references | 2,047 | 1,297 original articles, BMJ, JAMA, Lancet, NEJM, 1935-1985; none IMRAD in 1935; over 10% by 1950; over 80% in the 1970s; the only pattern in original papers in the 1980s; NEJM fully adopted 1975, BMJ 1980, JAMA and Lancet 1985; kappa 0.95; editors credited with the spread |
| `mensh_kording_2017_structuring_papers.txt` | Mensh and Kording 2017, *PLoS Comput Biol* 13:e1005619, PMC OA XML. **Whole text** except acknowledgement names and references | 4,646 | Rule 1 single message, title; Rule 2 naive reader, define terms, avoid abbreviations; Rule 3 context-content-conclusion and the chronological-structure passage ("They do not care about the chronological path by which you reached a result"); Rule 4 zig-zag, parallelism, same word for the same concept; Rules 5-8 abstract, introduction gap, results as declarative statements, discussion; Rule 9 outline one sentence per paragraph; Rule 10 feedback, Table 1 signs of violation |
| `openstax_writing_guide_handbook.txt` | OpenStax *Writing Guide with Handbook* (CC BY-NC-SA 4.0): Handbook H2 (Effective Paragraphs), H3 (Clear and Effective Sentences), H7 opening; 6.6 opening; 3.6 Revising Common Sentence Patterns. **Excerpts** | 4,262 | "The main point of the paragraph is usually expressed in a topic sentence"; end of a sentence most emphatic; active and passive voice defined; main (independent) and subordinate (dependent) clause; "The subject of a sentence names something. The predicate contains the verb"; a verb "expresses an action, an occurrence, or a state of being"; doer and action; the 49-16-8-3-word "Omit needless words" example |
| `gopen_swan_1990_scientific_writing.txt` | Gopen and Swan 1990, *Am Sci* 78:550, retyped reprint (usenix.org PDF text layer). **Whole article** except bibliography | 8,313 | Reader expectations; grammatical subject followed soon by its verb; stress position (new, emphasised material at the end); topic position (old information first, linkage backward); perceiving logical gaps; action in the verb |
| `plain_language_2011_guidelines.txt` | PLAIN, *Federal Plain Language Guidelines*, March 2011, Rev. 1 May 2011 (wid.org copy of the PDF). **Excerpts**: eleven sections whole | 5,532 | Active voice defined with passive/active pairs; hidden verbs and verbs turned into nouns; minimize abbreviations; short simple words; omit unnecessary words; same term consistently; short sentences; subject, verb and object close together; topic sentence; one topic per paragraph |
| `barnett_doubleday_2020_acronyms.txt` | Barnett and Doubleday 2020, *eLife* 9:e60080, PMC OA XML. **Whole text** except references and appendix | 4,151 | 24,873,372 titles, 18,249,091 abstracts, 1950-2019; 1,112,345 unique acronyms; acronyms per 100 words 0.7 to 2.4 (titles, 1950-2019) and 0.4 to 4.1 (abstracts, 1956-2019); at least one acronym in 19% of titles and 73% of abstracts; 30% used once, 49% two to ten times; 0.2% over 10,000 times; 11% re-used within a year; title length 9.0 to 14.6 words; abstract length 128 to 220 words; Table 1 top 20 (DNA 2,443,760) |
```
