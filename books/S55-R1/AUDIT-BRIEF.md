# Auditor brief · S55-R1 (Task 3 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S55-R1`. Do not commit or push. You did not
draft, cut or restore these records. Another auditor is doing other sections at the same time:
touch only your own records and files.

Read `claude.md`: "The one rule that matters", §7a, §7b, §8, §9, §10, the "Figures" rules, and
specification §4. You are auditing, not rewriting. Your records are in `check/records/S55/`; they
already carry the compressed prose. Also read `books/S55-R1/DEFECTS.md` — the holes the
compression pass found, and the conductor's figure notes — and audit every item that concerns your
sections along with the rest (confirm, correct or withdraw each, with a reason). To see the section
as the reader meets it, read its part of `check/_build/S55-R1.md` (headings "### N · ...").

For every claim: open the file `sources/INDEX.yml` maps the citekey to, search it for the words the
record relies on, and **write those words into the record's `quote` field** (only `quote` fields
may be edited by you). The quote must state the number it is cited for. A claim that reads
plausibly and is not in the file is the failure you are looking for.

Then **recompute every practice answer and every exercise answer** in Python, line by line. Check
that each practice set climbs. Recompute every number each figure spec plots or labels and check
the figure says what the section says (`figures:` entries; the PNGs are in `check/figures/`).

Check currency: anything with a date, a rate, a requirement or a cut-point, against the instrument
held, and flag what needs re-checking against a newer one.

Check the teaching as a reader of Book 0 would meet it: terms or abbreviations used before they are
explained, a pronoun whose referent was cut, a sentence that contradicts another section of this
book, a must-know point that would not change what the reader does, a `boundary` point that is a
table-of-contents entry. Check `check/SELFCHECK.md`'s items.

Output **one file per section**, `books/S55-R1/defects/<RECORD-ID>.md`: a numbered list. For each —
the field, the claim, what the source (or the arithmetic) actually says, the smallest change that
fixes it, and a tag **error** / **gap** / **style**. Include the DEFECTS.md holes for the section,
renumbered into this list, each marked "(from compression hole n)". Mark any defect whose *kind*
you have seen in `books/B0/defects/` or `books/S01-R1/defects/` or `books/S02-R1/defects/` or `books/S36-R1/defects/` as **recurring**. Then run `python check/build.py --check`
(blocking must stay 0 for your records). Return at most 150 words: defects per section by tag.

**This book specifically.** It is a book about choosing research questions. Most of its teaching is
judgement, not arithmetic, so the audit's weight falls on: (1) every claim traceable to a held source
(`blackstone_2012` blocks 13-18, `jhangiani_2019_methods`, `cdc_ss1978_lesson1`, `aslam_emmanuel_2010`,
`morgan_peco_2018`, `ratan_2019`, `ioannidis_2016_useful`, `ioannidis_2014_waste`, `van_noorden_2017`,
`golosovsky_lariviere_2021`, `farrugia_2010`, `nowroozzadeh_2019`, `patsopoulos_2005`,
`chalmers_glasziou_2009`, `chalmers_2014_priorities`, `nicolaisen_frandsen_2019`), with no claim
stronger than its source; (2) **C06 above all**: every uncitedness or citation figure carries the
database, the cohort (publication years), the window and the document types exactly as its source
states them; second-hand figures (the 1990 *Science* 55%, the Larivière–Sugimoto figures, Morgan's
54%) are attributed as reported, not presented as primary; the map's sentence "most descriptive
cross-sectional studies are never cited" is nowhere stated as fact (Patsopoulos 2005 has no
cross-sectional category); check each bar label of the figure `s55-r1-c06-uncited-shares.png` against
the source (the conductor suspects the fifth, "letters, notes", misdescribes what Nicolaisen's 23%
counts); (3) the 85% waste figure only from `chalmers_glasziou_2009`, with its stated basis, and no
per-stage percentage (those exist only in a figure image); (4) nothing stated as fact that is not held:
NMC thesis rules, the Companies Act or CSR rules (C07 may name CSR only as a word), obesity cut-offs;
(5) consistency across sections: C07's who-is-waiting test and C08's scoring sheet must agree (the cold
read found C08 scoring answers 1 that C07 fails — DEFECTS.md), C02's and C03's names for the
how-common/describe question, C03's cross-sectional study against its "describe" questions; (6) every
illustrative candidate, person and remark marked as made up, and no illustration attributed to a real
study; (7) each `kind` correct: `blackstone_2012`, `jhangiani_2019_methods` and `cdc_ss1978_lesson1`
are textbooks; journal papers are `primary`; derivable records have at least one textbook reference;
(8) C02 and C08 drill sets: every answer recomputed or re-derived, ladder climbs, both ends reached, no
hint in prompts; C08's sheet is called the course's own working tool, never a validated instrument.
Licences: `van_noorden_2017`, the Lancet papers, JAMA and Springer items are not openly licensed —
flag any reproduced table, box or long passage. Scratch in `/home/claude/scratch-audit-<batch>/`.
