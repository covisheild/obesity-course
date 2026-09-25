# Auditor brief · S37-R1 (Task 3 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S37-R1`. Do not commit or push. You did not
draft, cut or restore these records. Another auditor is doing other sections at the same time:
touch only your own records and files.

Read `claude.md`: "The one rule that matters", §7a, §7b, §8, §9, §10, the "Figures" rules, and
specification §4. You are auditing, not rewriting. Your records are in `check/records/S37/`; they
already carry the compressed prose. Also read `books/S37-R1/DEFECTS.md` and the compression holes it points to
(`books/S37-R1/compress/HOLES-r1.md`, `HOLES-r2.md`, `HOLES-r3.md`), and audit every item that concerns your
sections along with the rest (confirm, correct or withdraw each, with a reason). To see the section
as the reader meets it, read its part of `check/_build/S37-R1.md` (headings "### N · ...").

For every claim: open the file `sources/INDEX.yml` maps the citekey to, search it for the words the
record relies on, and **write those words into the record's `quote` field** (only `quote` fields
may be edited by you). The quote must state the number it is cited for. A claim that reads
plausibly and is not in the file is the failure you are looking for.

Then **recompute every practice answer and every exercise answer** in Python, line by line. Check
that each practice set climbs. Recompute every number each figure spec plots or labels and check
the figure says what the section says (`figures:` entries; the PNGs are in `check/figures/`).

Check currency: anything with a date, a rate, a requirement or a cut-point, against the instrument
held, and flag what needs re-checking against a newer one.

Check the teaching as a reader of Book 0 (`check/records/B0/`) would meet it: terms or abbreviations used before they are
explained, a pronoun whose referent was cut, a sentence that contradicts another section of this
book, a must-know point that would not change what the reader does, a `boundary` point that is a
table-of-contents entry. Check `check/SELFCHECK.md`'s items.

Output **one file per section**, `books/S37-R1/defects/<RECORD-ID>.md`: a numbered list. For each —
the field, the claim, what the source (or the arithmetic) actually says, the smallest change that
fixes it, and a tag **error** / **gap** / **style**. Include the DEFECTS.md holes for the section,
renumbered into this list, each marked "(from compression hole n)". Mark any defect whose *kind*
you have seen in `books/B0/defects/` or `books/S01-R1/defects/` or `books/S02-R1/defects/` as **recurring**. Then run `python check/build.py --check`
(blocking must stay 0 for your records). Return at most 150 words: defects per section by tag.

**This book specifically.** It is an institutional and empirical book on Indian food policy, so
most defects will be claims that go beyond their source: a figure given without its year, season or
body; a figure measured for one crop, group, year or place applied to another (SELFCHECK 4a); a scheme
described from memory rather than from the held text; lakh/crore conversions; an as-of date that
has moved (MSP, FRP, edible oil duty changed 24 Sep 2026, economic cost). Read the "Facts intake
established" list in `books/S37-R1/DRAFT-BRIEF.md` and check each record honours it. Withdrawn and
not held: `eca_1955`, `food_corporations_act_1964`, Hawkes 2020, the PM POSHAN 2023 guidelines, CACP's
"About us"; nothing may rest on them. **`build.py` does not check quotes inside `illustrations[]`**:
check every quote and number there by hand against its file. Check the book is consistent with itself
across sections: the eight stages of C01 against the map in C16 and the method in C17; C05's
food-environment elements against C17's reading of campaigns and labels; the double-duty vocabulary
of C15 against C12-C14; C12 and C13 on the anganwadi norms revision. Conductor's figure notes: the
C06 pulses-identity bar "Rise in stocks, taken off" at -615 needs its sign convention stated in the
text; C16's 2024 duty bar comes from a release that says "import duty", not "basic customs duty".
The drill sets are 3-18 problems. Scratch in `/home/claude/scratch-audit-<batch>/`.
