# Auditor brief · S36-R1 (Task 3 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S36-R1`. Do not commit or push. You did not
draft, cut or restore these records. Another auditor is doing other sections at the same time:
touch only your own records and files.

Read `claude.md`: "The one rule that matters", §7a, §7b, §8, §9, §10, the "Figures" rules, and
specification §4. You are auditing, not rewriting. Your records are in `check/records/S36/`; they
already carry the compressed prose. Also read `books/S36-R1/DEFECTS.md` — the holes the
compression pass found, and the conductor's figure notes — and audit every item that concerns your
sections along with the rest (confirm, correct or withdraw each, with a reason). To see the section
as the reader meets it, read its part of `check/_build/S36-R1.md` (headings "### N · ...").

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

Output **one file per section**, `books/S36-R1/defects/<RECORD-ID>.md`: a numbered list. For each —
the field, the claim, what the source (or the arithmetic) actually says, the smallest change that
fixes it, and a tag **error** / **gap** / **style**. Include the DEFECTS.md holes for the section,
renumbered into this list, each marked "(from compression hole n)". Mark any defect whose *kind*
you have seen in `books/B0/defects/` or `books/S01-R1/defects/` or `books/S02-R1/defects/` as **recurring**. Then run `python check/build.py --check`
(blocking must stay 0 for your records). Return at most 150 words: defects per section by tag.

**This book specifically.** It is a qualitative-methods book. Most of its teaching is practice,
not arithmetic, so the audit's weight falls on: (1) every methodological claim traceable to a held
source (`dejonckheere_vaughn_2019`, `pope_ziebland_mays_2000`, `mays_pope_2000`,
`green_britten_1998`, `mcmullin_2023`, `blackstone_2012`, `icmr_ethical_guidelines_2017`, and the OCR
files `kitzinger_1995`, `britten_1995`, `pope_mays_1995`), with no claim stronger than its source
(for example a group size or a transcription time given as a rule when the source gives a range or
an example); (2) where two held sources disagree (Kitzinger vs Blackstone on focus-group size), the
text says they differ; (3) C07's statements against the ICMR 2017 text exactly (section numbers,
what the guidelines require, and no assertion the guidelines do not make about a learner's pilot);
(4) consistency of the running example and of advice across sections (confidentiality promises,
consent records, what a "code" and a "label" are, the gate at half the words); (5) every
illustrative exchange marked as made up, and no illustrative line attributed to a real study; (6)
each `kind` correct: only `blackstone_2012` is a textbook; journal papers are `primary`; ICMR is
`guideline`. OCR quotes: check each is in the file as written; you cannot see the page images, so
list in your defect file any OCR quote whose OCR text looks garbled enough that the words may
differ on the page. Scratch in `/home/claude/scratch-audit-<batch>/`.
