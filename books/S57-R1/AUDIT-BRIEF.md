# Auditor brief · S57-R1 (Task 3 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S57-R1`. Do not commit or push. You did not
draft, cut or restore these records. Another auditor is doing other sections at the same time:
touch only your own records and files.

Read `claude.md`: "The one rule that matters", §7a, §7b, §8, §9, §10, the "Figures" rules, and
specification §4. You are auditing, not rewriting. Your records are in `check/records/S57/`; they
already carry the compressed prose. Also read `books/S57-R1/DEFECTS.md` — the holes the
compression pass found, and the conductor's figure notes — and audit every item that concerns your
sections along with the rest (confirm, correct or withdraw each, with a reason). To see the section
as the reader meets it, read its part of `check/_build/S57-R1.md` (headings "### N · ...").

For every claim: open the file `sources/INDEX.yml` maps the citekey to, search it for the words the
record relies on, and **write those words into the record's `quote` field** (only `quote` fields
may be edited by you). The quote must state the number it is cited for. A claim that reads
plausibly and is not in the file is the failure you are looking for.

Then **recompute every practice answer and every exercise answer** in Python, line by line. Check
that each practice set climbs. Recompute every number each figure spec plots or labels and check
the figure says what the section says (`figures:` entries; the PNGs are in `check/figures/`).

Check currency: anything with a date, a rate, a requirement or a cut-point, against the instrument
held, and flag what needs re-checking against a newer one.

Check the teaching as a reader of Book 0 only would meet it: terms or abbreviations used before they are
explained, a pronoun whose referent was cut, a sentence that contradicts another section of this
book, a must-know point that would not change what the reader does, a `boundary` point that is a
table-of-contents entry. Check `check/SELFCHECK.md`'s items.

Output **one file per section**, `books/S57-R1/defects/<RECORD-ID>.md`: a numbered list. For each —
the field, the claim, what the source (or the arithmetic) actually says, the smallest change that
fixes it, and a tag **error** / **gap** / **style**. Include the DEFECTS.md holes for the section,
renumbered into this list, each marked "(from compression hole n)". Mark any defect whose *kind*
you have seen in `books/B0/defects/`, `books/S01-R1/defects/` or `books/S02-R1/defects/` as **recurring**. Then run `python check/build.py --check`
(blocking must stay 0 for your records). Return at most 150 words: defects per section by tag.

**The amendments.** For every amendment id a record names in `outcome_refs` or `bridge_ref`
(`map/AMENDMENTS-v3.1.yml`; run `python check/amendments.py --rung S57-R1`), check that the record
actually teaches what the amendment says, at rung 1; naming the id is not serving it.

**This book specifically.** It is an empirical book about teaching, learning research and leading.
The errors to hunt are of the kind the Book 1 reader found (SELFCHECK 4a): a finding stated beyond
what was measured. For every study cited, check against the held text: the design (within- or
between-subjects, randomised or not, who the participants were), when the test was taken (end of
session vs days later), the size and direction of the result, and whether the record generalises
it further than the source does (e.g. from lab word lists to medical students; from Cepeda's
manuscript numbers to a planning rule). Numbers from Cepeda 2008 come from the authors' in-press
manuscript; Hake 1998 is held as its abstract only; the Cochrane SMD formula is an image (only its
definition in words is held); Kotter, Pashler 2008 and Rozenblit & Keil 2002 are held in full from
PDFs supplied by Harsh (ligatures ﬁ/ﬂ kept as extracted). The Indian instruments in force are the
NMC CBME Curriculum 2024, GMER 2023 and the Medical Institutions (Qualifications of Faculty)
Regulations 2025; check every clause, count and date against those files. A working definition the
book gives without a source (C16) must be labelled as the book's own and must not be passed off as
a finding. The build lists abbreviations used before anything expands them (MBBS, SSST, SMD, SD,
ASHA, RI, KH, SH, GMER, FOL, UGMEB, AETCOM, CRMI, PGMEB, SMART, …): flag each first use in your
sections that a Book 0 reader could not decode. The notation the book set for itself is in
`books/S57-R1/DRAFT-BRIEF.md` ("Notation"); flag drift across sections (gain vs normalised gain,
MD/SMD, "gap" vs "retention interval"). Scratch in `/home/claude/scratch-audit-<batch>/`.
