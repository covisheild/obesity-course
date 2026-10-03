# Auditor brief · S58-R1 (Task 3 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S58-R1`. Do not commit or push. You did not
draft, cut or restore these records. Another auditor is doing other sections at the same time:
touch only your own records and files.

Read `claude.md`: "The one rule that matters", §7a, §7b, §8, §9, §10, the "Figures" rules, and
specification §4. You are auditing, not rewriting. Your records are in `check/records/S58/`; they
already carry the compressed prose. Also read `books/S58-R1/DEFECTS.md` — the holes the
compression pass found, and the conductor's figure notes — and audit every item that concerns your
sections along with the rest (confirm, correct or withdraw each, with a reason). To see the section
as the reader meets it, read its part of `check/_build/S58-R1.md` (headings "### N · ...").

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

Output **one file per section**, `books/S58-R1/defects/<RECORD-ID>.md`: a numbered list. For each —
the field, the claim, what the source (or the arithmetic) actually says, the smallest change that
fixes it, and a tag **error** / **gap** / **style**. Include the DEFECTS.md holes for the section,
renumbered into this list, each marked "(from compression hole n)". Mark any defect whose *kind*
you have seen in `books/B0/defects/`, `books/S01-R1/defects/` or `books/S02-R1/defects/` as **recurring**. Then run `python check/build.py --check`
(blocking must stay 0 for your records). Return at most 150 words: defects per section by tag.

**The amendments.** For every amendment id a record names in `outcome_refs` or `bridge_ref`
(`map/AMENDMENTS-v3.1.yml`; run `python check/amendments.py --rung S58-R1`), check that the record
actually teaches what the amendment says, at rung 1; naming the id is not serving it.

**This book specifically.** It teaches scientific writing and honest figures, so its own text and
figures must obey what it teaches, and its worked numbers are the reader's only model: recompute every
count (words, sentences, syllables, words between subject and verb), every Flesch score and grade, every
Lie Factor, percentage, percentage-point difference, SD/SE/CI and rounding, from the text as printed. Read
`books/S58-R1/DRAFT-BRIEF.md` ("What intake found" and "Notation") — it records which sources say what:
Flesch printed .846 (84.6 per syllable-per-word) and Kincaid 1975's ".836" is a misprint; Kincaid is
cited only for the grade-level formula; the name "Flesch–Kincaid" is later writers'; Tufte is the 1983
first edition (cite page numbers from that file); Cleveland & McGill's ranking is a hypothesis tested
only for position vs length and vs angle; ICMJE is section IV.A and is quoted briefly; Wilke is
CC BY-NC-ND (quoted, never adapted); Krishnamurthy 2021 is boys in one district; SAMPL is the 2013 PDF.
Several PDF-derived files carry OCR errors listed in their `[NOTE]`s: a quote must not rely on a garbled
passage. The reconciler changed "overweight or obese" to "with overweight or obesity" in prose (claude.md
§9); quotes and the NFHS indicator name keep the source's words — check none was altered inside a quote.
A worked "before" text the book invented must be labelled as invented; a figure or sentence describing a
worked example the compressed text no longer shows is a defect (the cold readers found several: see
DEFECTS.md). Check the numbers registry (`books/S58-R1/numbers.yml`) values against their sources. Check
the reference list each record ends with: every reference formatted to the NLM style the book teaches
(C05), or the book contradicts itself. Scratch in `/home/claude/scratch-s58-audit-<batch>/`.
