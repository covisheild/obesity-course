# Auditor brief · S02-R1 (Task 3 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S02-R1`. Do not commit or push. You did not
draft, cut or restore these records. Another auditor is doing other sections at the same time:
touch only your own records and files.

Read `claude.md`: "The one rule that matters", §7a, §7b, §8, §9, §10, the "Figures" rules, and
specification §4. You are auditing, not rewriting. Your records are in `check/records/S02/`; they
already carry the compressed prose. Also read `books/S02-R1/DEFECTS.md` — the holes the
compression pass found, and the conductor's figure notes — and audit every item that concerns your
sections along with the rest (confirm, correct or withdraw each, with a reason). To see the section
as the reader meets it, read its part of `check/_build/S02-R1.md` (headings "### N · ...").

For every claim: open the file `sources/INDEX.yml` maps the citekey to, search it for the words the
record relies on, and **write those words into the record's `quote` field** (only `quote` fields
may be edited by you). The quote must state the number it is cited for. A claim that reads
plausibly and is not in the file is the failure you are looking for.

Then **recompute every practice answer and every exercise answer** in Python, line by line. Check
that each practice set climbs. Recompute every number each figure spec plots or labels and check
the figure says what the section says (`figures:` entries; the PNGs are in `check/figures/`).

Check currency: anything with a date, a rate, a requirement or a cut-point, against the instrument
held, and flag what needs re-checking against a newer one.

Check the teaching as a reader of Book 0 and Book 1 (S01-R1, `check/records/S01/`) would meet it: terms or abbreviations used before they are
explained, a pronoun whose referent was cut, a sentence that contradicts another section of this
book, a must-know point that would not change what the reader does, a `boundary` point that is a
table-of-contents entry. Check `check/SELFCHECK.md`'s items.

Output **one file per section**, `books/S02-R1/defects/<RECORD-ID>.md`: a numbered list. For each —
the field, the claim, what the source (or the arithmetic) actually says, the smallest change that
fixes it, and a tag **error** / **gap** / **style**. Include the DEFECTS.md holes for the section,
renumbered into this list, each marked "(from compression hole n)". Mark any defect whose *kind*
you have seen in `books/B0/defects/` or `books/S01-R1/defects/` as **recurring**. Then run `python check/build.py --check`
(blocking must stay 0 for your records). Return at most 150 words: defects per section by tag.

**This book specifically.** It is a mathematics book: every derivation, rule and worked answer must
be mathematically right as stated (signs, domains, units of rate constants, the exact form of a
rule), not only arithmetically right; check each against the held textbook section where one is
cited (`openstax_calculus_v1_s02`, `openstax_calculus_v2`, `openstax_college_algebra_2e_7_5`,
`austin_ula`, `openstax_intro_stats_2e`, `openintro_stats_4e`). Equations quoted from Polidori 2016
and Thomas 2013 were converted from MathML: compare each with the `[MATHML]` block in its source
file. The drill sets are 3–25 problems each (`books/S02-R1/book.yml` `practice_max: 25`); judge the
size by the technique. The notation the book set for itself is in `books/S02-R1/DRAFT-BRIEF.md`
("Notation"); flag every drift from it across sections (ES as a rate vs a stock, k's sign, EO vs EE,
subscripts). Scratch in `/home/claude/scratch-audit-<batch>/`.
