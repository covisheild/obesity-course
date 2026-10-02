# Draft notes · S58-R1 · batch b2 (C04, C05)

Task 2 drafter, 2 Oct 2026. Brief: `books/S58-R1/DRAFT-BRIEF.md`. Exemplars: S57-R1-C10 (derivable),
S57-R1-C14 (institutional).

## Records written

- `check/records/S58/S58-R1-C04.yml` — The argument across sections: from the gap to the answer and
  its limits (derivable). 25 definition references (Mensh & Kording Rules 6-9 and Table 1; ICMJE
  IV.A.3.c-f; NFHS-5 fact sheet for the running case), two illustrations (a heading-list plan
  rewritten as a claim-per-paragraph outline on the NFHS-5 rows; seven invented draft sentences
  sorted into their sections), 9 must-know points, `common_misreading`, `reporting_sentence`, four
  exercises (retrieval, critique with skill_ref S58-R1-K01, design, teaching), 4 retrieval items.
- `check/records/S58/S58-R1-C05.yml` — Citing and referencing (institutional). 36 definition
  references (ICMJE IV.A.3.g; NLM Citing Medicine ch. 1 and the NLM Samples page; Rougier 2014's
  own citation line; Mensh & Kording's copyright line; Sollaci & Pereira for the "Vancouver Group"
  name), three illustrations (the journal's "Citation" line rebuilt in NLM format element by
  element; numbering by first mention with a table-only source; cite what you read and the version
  you saw: NFHS-5 row 88 and the Kording/Mensh preprint against the published paper), 9 must-know
  points, `common_misreading`, `reporting_sentence`, four exercises (retrieval, critique,
  interpretation, teaching), 4 retrieval items.

`python check/build.py` checks (run through `build.check`, filtered to these two records, after the
last substantive edit): 0 blocking; warnings left are "paradigm" on the hard-word list in C05's
critique exercise, which is the title of Weissgerber et al. 2015 and cannot be changed, and one
definition sentence since split. Every quote (80) was checked by script as a whitespace-normalised substring of the source file
with the file's header and `[NOTE]` lines removed: 80/80. Numbers quoted under `illustrations[].numbers`
each state their value. No arithmetic in either record (neither is quantitative), so no `working`
block and no practice set.

## Anything unsourced, or resting on something the auditor should look at

- **C05, journal abbreviations.** "PLoS Comput Biol", "Arch Dis Child" and "PLoS Biol" are not
  stated as NLM Catalog abbreviations by any held passage. The record tells the reader to confirm
  each in the NLM Catalog and never asserts the Catalog's form. "PLoS Comput Biol" is the
  journal's own printing (Rougier citation line, quoted).
- **C05, "e1003833 where the pages go".** NLM's specific rule for electronic article numbers is in
  the "Specific Rules" boxes, which are NOT held. The record says only that the journal's line puts
  e1003833 where a page range would go, and that yours does too.
- **C05, the critique exercise's bibliographic data** (Cole 2015: 100(7):608-609; Weissgerber 2015:
  four authors, 13(4):e1002128) come from `library.bib` (PubMed-confirmed at intake); no held
  passage states them. They are metadata, not statistics.
- **C05, the published Mensh & Kording paper.** Journal and year: year from the quoted copyright
  line ("© 2017 Mensh, Kording"); journal from the DOI and the bibliography (no held passage names
  the journal). That the preprint and the paper share a title rests on the NLM sample entry and the
  bibliography's title.
- **C05, glosses with no held definition:** "predatory or pseudo-journals" (said in the record to be
  this book's gloss, because ICMJE's section does not define them), "preprint", "retracted",
  "review article", "DOI". All are plain-words glosses, not factual claims.
- **C05, "Vancouver".** Sollaci & Pereira is quoted only for the committee's former name. No held
  source says journals call the style "Vancouver", so the record does not say it; it says "if a
  journal asks for Vancouver references, read its instructions with this section open". The
  inventory's "(Vancouver, the ICMJE convention)" is therefore taught as advice, not as a fact.
- **C05, the inventory's "free reference manager named in passing"** is not done: no held source
  names one or says it is free. The record describes what a reference manager does and warns what
  it cannot do.
- **C04, "Introduction 2" and "Discussion 2/4" of the outline** are left as bracketed instructions:
  the record does not invent literature claims, explanations or policy meaning for the NFHS
  finding.
- **C04, must-know point 3 (dispute)**: Mensh & Kording's last introduction paragraph summarises
  results; ICMJE IV.A.3.c says not to include data or conclusions from the work. Both quoted.

## Practice sets

None: neither C04 nor C05 is quantitative.

## Figures

Both records carry a `figure_note` instead of a figure; `draw.py` draws only line, scatter, bar and
step. Figures wanted, if a diagram kind is ever added:

- **C04: the paper's argument as a funnel and its mirror** (broad, narrow, broad): Introduction
  narrowing from field to gap to question; Methods and Results as a column of claim boxes, each
  arrowing into the next; Discussion widening from the answer to explanations, limits, meaning.
  Labels taken from the outline table in illustration 1 (no numbers). Mensh & Kording's Fig 1 is
  the model (CC BY 4.0; its image is not held, only the caption).
- **C05: one reference, annotated.** The NLM entry "Rougier NP, Droettboom M, Bourne PE. Ten simple
  rules for better figures. PLoS Comput Biol. 2014 Sep 11;10(9):e1003833." with a bracket and a
  label under each element (authors, title, journal, date, volume, issue, pages) and each
  punctuation mark called out. Numbers: 2014, 11, 10, 9, e1003833, all in the record.

## numbers.yml keys

Used, none added: `nfhs5_women_ow_ob_pct`, `nfhs4_women_ow_ob_pct`, `nfhs5_men_ow_ob_pct`,
`nfhs4_men_ow_ob_pct`, `nfhs5_women_ow_ob_urban_pct`, `nfhs5_women_ow_ob_rural_pct`,
`nfhs5_men_ow_ob_urban_pct`, `nfhs5_men_ow_ob_rural_pct`.

Numbers written literally that another section may share (for the reconciler, Task 2b):

| value | meaning | source |
| --- | --- | --- |
| 25.0 | kg/m^2, the BMI at or above which the fact sheet counts an adult overweight or obese | `nfhs5_india_factsheet`, indicators 88-89 |
| 33.2, 19.7, 24.0, 20.6 | the four numbers of indicator 88 as read across the row (C05 illustration 3 prints them literally, as the row reads, because the point is reading the row) | `nfhs5_india_factsheet` |
| 2014 Sep 11; 10(9); e1003833 | Rougier et al. 2014 publication date, volume, issue, article number | `rougier_2014_ten_rules_figures` (citation line and date line) |

## Notation rows needed

None. Neither record prints a sign, Greek letter or marked letter outside quotes (`kg/m^2` is a
unit, typeset by the build; "≥" appears only inside audit quotes).

## Glossary rows (proposed; `prose/GLOSSARY.md` not edited)

Checked against the glossary on 2 Oct 2026. "objective" is glossed there in two other senses (S57:
learning objective; S57-R1-C13: of how an outcome is measured), so C04 writes **research
objective** throughout. "reference" (B0-R0-C41) and "citation" (S55-R1-C06, an entry in a later
work's reference list) are used in their existing senses; C05 avoids defining "citation" anew and
calls the in-text mark a reference number. "protocol" is glossed in S55-R1-C02; C04 writes "the plan
or protocol", which glosses itself for a reader of Book 0 only.

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| gap (in a paper's introduction) | what is not yet known, which the introduction narrows to and the study sets out to fill | `S58-R1-C04` |
| hypothesis | a statement the study is designed to support or refute | `S58-R1-C04` |
| limitation (of a study) | a way the study's design or data could make its answer wrong, or narrower than it looks | `S58-R1-C04` |
| outline (of a paper) | the argument written before the prose: one sentence for each planned paragraph, each sentence the claim that paragraph will make | `S58-R1-C04` |
| research objective | what the study sets out to find, stated at the end of the introduction | `S58-R1-C04` |
| preprint | a paper posted publicly before a journal has checked and accepted it | `S58-R1-C05` |
| predatory or pseudo-journal | (this book's gloss; ICMJE does not define it in the section read) a journal that presents itself as checking what it publishes and does not | `S58-R1-C05` |
| reference list | the numbered list at the end of a paper, one entry for each source cited | `S58-R1-C05` |
| reference manager | a program that stores your references once and types out the numbered list for you | `S58-R1-C05` |
| retracted (article) | withdrawn by the journal after publication | `S58-R1-C05` |
| review article | a paper that summarises other studies | `S58-R1-C05` |
| DOI | a paper's permanent identifier, printed as doi: followed by a code | `S58-R1-C05` |

If b1 (C01-C03) glosses "hypothesis", "abstract", "IMRaD" or "claim" first, C04's inline gloss of
"hypothesis" should be dropped by the reconciler and its sense checked against b1's. C04 uses
"claim" and "the central claim" without a gloss, relying on C02 and C03.

## Notes for others

- **C01 (b1).** Sollaci & Pereira's page range: the PMC front matter (quotable) prints
  "364–371"; the file's `[NOTE]` says PubMed gives "364-7". If C01's reference list or any
  reference for Sollaci prints pages, the two disagree and need settling against the article
  itself. C05 does not use Sollaci's pages.
- **C01-C03 (b1).** C04 expands ICMJE again in its second illustration, in case C01 does not;
  the reconciler should keep the first expansion in document order and drop the later one.
  C04 assumes C02 has taught "a paper is an argument, not a diary of activities" and C03 the one
  central claim; it does not re-teach either.
- **C10 (paragraph).** C04 already teaches, from Mensh & Kording Rule 7, that a results paragraph
  opens with its question and ends with its answer. C10 should point back to C04 rather than
  re-teach that, and keep the context-content-conclusion scheme as its own.
- **C21 (table) and C23 (journey).** C05 teaches the in-text numbering, including that a reference
  cited only in a table is numbered where the text first mentions the table. C21 should not
  contradict it.
- **C23 (journey).** The inventory asks to "cite the fact sheet as a numbered reference in NLM
  format". **NLM's format for a report or a web document is not held**: only Citing Medicine ch. 1
  (journal articles), appendix B and two items of the Samples page are in
  `sources/nlm_citing_medicine_2007.txt`. C05 says so ("A book, a report such as the NFHS fact
  sheet ... follows other chapters of Citing Medicine, which this section does not teach"). C23
  needs either Citing Medicine ch. 2 (books) or ch. 22-25 (Internet documents), or the Samples
  page's items for reports/Internet material, taken at intake, or it should give the reference in
  a form it marks as not checked against NLM.
- **C09 (numbers) and C23.** C04 and C05 print the NFHS-5 shares as "per cent of women aged 15-49"
  and state no percentage-point difference (C09 teaches that). The rise is described in words
  ("rose", "higher"), never as a difference.
- **Next rung.** C05 routes recognising a predatory journal, and choosing a journal, to S58-R2
  (S58-R2-A02); it says only "taught at the next rung".
