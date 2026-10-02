# Auditor brief · S47-R1 (Task 3 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S47-R1`. Do not commit or push. You did not
draft, cut or restore these records. Another auditor is doing other sections at the same time:
touch only your own records and files.

Read `claude.md`: "The one rule that matters", §7a, §7b, §8, §9, §10, the "Figures" rules, and
specification §4. You are auditing, not rewriting. Your records are in `check/records/S47/`; they
already carry the compressed prose. Also read `books/S47-R1/DEFECTS.md` — the holes the
compression pass found, and the conductor's figure notes — and audit every item that concerns your
sections along with the rest (confirm, correct or withdraw each, with a reason). To see the section
as the reader meets it, read its part of `check/_build/S47-R1.md` (headings "### N · ...").

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

Output **one file per section**, `books/S47-R1/defects/<RECORD-ID>.md`: a numbered list. For each —
the field, the claim, what the source (or the arithmetic) actually says, the smallest change that
fixes it, and a tag **error** / **gap** / **style**. Include the DEFECTS.md holes for the section,
renumbered into this list, each marked "(from compression hole n)". Mark any defect whose *kind*
you have seen in `books/B0/defects/` or `books/S01-R1/defects/` or `books/S02-R1/defects/` or `books/S36-R1/defects/`, `books/S37-R1/defects/`, `books/S55-R1/defects/` or `books/S57-R1/defects/` as **recurring**. Then run `python check/build.py --check`
(blocking must stay 0 for your records). Return at most 150 words: defects per section by tag.

**Book-specific additions (S47-R1).** Every defect ends with a disposition line left blank for the
fixer: `Fixed:` / `Partly:` / `Rejected:` and later `Verified:` (`check/defects.py`); write each defect
so it can carry those lines. Numbers written `{{n:key}}` are substituted from
`books/S47-R1/numbers.yml`; check the key's value and citekey against the source too. Figures are
redrawn with `python books/S47-R1/draw_figures.py` (it applies the numbers registry; plain `draw.py`
does not), never by editing a PNG. The build reports abbreviations used before they are expanded
(PIB, FSSAI, PRS, PLCP, CBIC, FCTC, ...): list each one that a reader meets unexpanded in your sections.

**This book specifically.** It teaches who decides an Indian policy, under what power, and how
public arguments are framed. The audit's weight falls on: (1) every institutional claim traceable to
a held instrument, with no claim stronger than its source — Articles of the Constitution
(`constitution` = `constitution_current.txt`), the FSS Act, the Allocation and Transaction of Business
Rules (First Schedule lists departments, Second their subjects), the General Clauses Act s.23 (its
words are "rules or bye-laws"; do not let a record claim it governs FSSAI regulations unless a held
source says so), the PLCP (thirty days; a policy, not a law), the Rajya Sabha booklet (dated 2005),
PRS 2012 (dated); (2) **the GST case above all**: the Council recommends (Art. 279A, PIB 2163555);
CGST s.9(1) caps the central rate at 20%; heading 2202 drinks in Schedule III - 20% of 9/2025-CT(Rate)
as amended by 01/2026-CT(Rate) (in force 1 May 2026; 19/2025 not held); the 40% is the combined rate
as PIB states; nothing about State GST Acts beyond what PIB states; any "cess" figure must be in a held
source; the vote arithmetic (one-third Centre, two-thirds States, three-fourths to pass) exactly as Art.
279A states; (3) the school-canteen case never resolved beyond held sources; State bodies of
Chhattisgarh not named as fact (not held); C07-6 suspected error: whether State food-safety rules are
laid before Parliament or the State Legislature (FSS Act s.94(3)); (4) framing evidence (Koon 2016,
Barry 2009, Summan 2026): each finding with its country, years, sample and design; Entman's functions
attributed "as reported by Koon et al."; no claim from Gollust 2013, Pielke 2007 or Varghese 2024
(the latter only as Summan reports it); Barry's percentages and R-squared values checked cell by cell;
(5) C17: honest broker vs issue advocate only as Oliver & Cairney 2019 state it; Pielke's four roles
not taught; (6) OpenStax American Government is a US text — flag any use of it for a fact about India;
(7) every invented person, memo or remark marked as made up the first time in each section, and no
invented sentence attributed to a real body; the FSSAI tagline only in Hindi as quoted; (8) the three
drill sets (C11, C15, C17): every answer re-derived, ladder climbs 1→10, both ends reached, no hint in
prompts, no exercise answered in advance by another section's text; (9) `kind`s correct (OpenStax and
the Gilson Reader as textbook; journal papers primary or systematic_review; instruments instrument;
PLCP/Rajya Sabha booklet guideline is accepted) — never relabel to pass; (10) licences: Barry 2009,
Walt 2008, WHO FCTC, the Gilson Reader, the Business Rules and COTPA are all rights reserved or
restricted — flag any reproduced table, box or long passage. Scratch in
`/home/claude/scratch-audit-<batch>/`.
