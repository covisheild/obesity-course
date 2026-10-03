# Drafter brief · S58-R1 (Task 2 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S58-R1`. Do not commit, push, fetch from the
web, or use GitHub tools. Write only the files named for you. Absolute paths only. Never `rm` anything
in the repository.

Read `claude.md`: "The one rule that matters", the whole authoring style sheet (§1–§11a, **including
§4a**, added 28 Sep 2026), and specification §1 and §4. Skip §12 and the rest of the specification.
Read the two exemplar records you are given before writing a word — they are the standard for voice,
depth and structure, and matching them matters more than following the rules in the abstract. The
exemplars were written before 28 Sep 2026, so they lack what §4a now requires of a new book (below):
add it.

Read `books/S58-R1/INVENTORY.md` (your concepts' rows: what each must cover, its Book 0 sections,
its sources, whether it is quantitative, the outcomes it serves), `books/S58-R1/SOURCE-GATE.md`,
`books/S58-R1/READY.md` and `sources/INDEX.yml` (which source files and citekeys are held, and what
each file does and does not hold — read the header of every source file you cite). **The inventory
was renumbered on 2 Oct 2026** (two concepts added): the intake logs, intake scripts and the
`sources/` file headers use the OLD concept numbers. The old-to-new table is at the end of
`INVENTORY.md`; read them through it.

This is **a subject book** on scientific writing and figures. Its reader has read Book 0 only. Do not
re-teach what a Book 0 section in your row teaches; name it where the reader needs it (as the
exemplars do) and list it in `ground_floor_deps`. To see what a Book 0 section says, read only its
`definition` and `must_know` in `check/records/B0/<id>.yml`.

The reader is a medical graduate training in community medicine in India who will write a thesis,
papers and reports, and draw figures from survey and clinic data. Examples come from that world (a
thesis chapter, an NFHS table, a district survey, a clinic audit), and, where natural, from obesity and
nutrition. The running case across sections is the NFHS-5 overweight-or-obese indicator; its numbers
are in `books/S58-R1/numbers.yml` — write them as `{{n:key}}`, never retyped (claude.md §4a). **Do not edit
`numbers.yml`** (other batches run at once): if another number will be shared across sections, write it
literally and list it in your notes (value, meaning, citekey or arithmetic); the reconciler (Task 2b)
moves it into the registry.

Write one YAML file per concept at `check/records/S58/<concept id>.yml` (subject `S58`, rung `1`,
`sequence` = the concept number), using `check/schema/example.concept.yml` as the template and
`check/schema/concept.schema.json` as the schema. `concept_deps` may name only earlier S58-R1
concepts.

**New-book requirements (claude.md §4a; `check/reader_checks.py` blocks or warns on them):**
- at least one exercise of `type: retrieval` per record (a from-memory prompt, answered);
- no phrase listed in `check/banned_phrases.yml`; "recall" only for something earlier;
- no version history anywhere in a record;
- every symbol you introduce has a row in `check/notation.yml` — do not edit that file (shared); list
  the rows you need in your notes;
- where it teaches, use `common_misreading` (the tempting wrong reading, refuted) and, since this
  rung's build target is a paper section, `reporting_sentence` (a sentence the reader can use as it
  stands) — both optional, use them where they earn their place.

For every concept the inventory marks quantitative (C09, C11, C17), write `practice[]` on the ladder
in `claude.md` §7a — levels 1-3 mechanical on bare numbers, 4-6 applied to a real quantity with its
unit, 7-8 diagnostic on a worked answer that is wrong, 9-10 transfer from a claim in words. How many is
your judgement, **between three and eighteen**, chosen from the technique and the number of moves that
compose in it. The set must reach both ends of the ladder; say in one line in your notes why you chose
the number. Prompts carry no hint of the answer. Answers show every line. A problem quoting a real
figure names its citekey in `refs`; where no real figure exists, use bare numbers rather than inventing
one.

For every factual claim, quote the exact words from the file in `sources/` that carry it, and put the
file and section in the locator. The quote must state the number it is cited for. If no held file
carries it, set `opened: false`, say in `verified.note` which instrument is needed, and write the
concept so it does not depend on the unopened claim. Never quote a `[NOTE]` line or a header; quote
only the passages. PDF-derived files keep OCR artefacts and ligatures as extracted: a quote must copy
the passage exactly, so prefer passages that extracted cleanly; where the file's `[NOTE]` gives the
true reading of a garbled passage, do not quote the garbled text for that point.

**What intake found, which overrides the inventory where they differ** (new concept numbers):
- **C11 readability.** The Flesch Reading Ease formula comes from Flesch himself:
  `flesch_1948_readability_yardstick` (a retyped public-domain reprint: "RE = 206.835 - .846 wl -
  1.015 sl", wl = syllables per 100 words, sl = words per sentence) and `flesch_1979_plain_english`
  ("Multiply the average word length by 84.6"; score bands 0-30 to 90-100). **Kincaid 1975's Table 3
  prints ".836": a misprint** — quote `kincaid_1975_readability` only for the grade-level formula
  (".39 (words/sentence) + 11.8 (syllables/word) – 15.59"), the simplified one, the 531 Navy personnel,
  and the counting rules (Appendix B). The report never uses the name "Flesch-Kincaid"; say later
  writers call its formula that. The 1948 reprint prints the "Very Difficult" band as "0 to 20"; take
  the bands from Flesch 1979 or say the copies differ. `edwards_2022_readability_formulas` is secondary.
  A low score does not make text clear: say so with `plavensigray_2017_readability` and the formulas'
  fitting samples (Navy personnel, Flesch's own test passages) as the limit.
- **C05 referencing:** ICMJE §IV.A.3.g (`icmje_2026_manuscript_preparation`) and NLM *Citing
  Medicine* (`nlm_citing_medicine_2007`). **ICMJE asks others not to reprint its Recommendations:
  quote briefly and link**, everywhere in the book. Its section is IV.A, not II.A.
- **C09 numbers:** Cole 2015 and SAMPL (`lang_altman_2013_sampl`, the 2013 PDF EQUATOR links to, not
  the 2015 journal version) give different rules for rounding P values: show both, attributed.
- **C15 marks:** `cleveland_mcgill_1984_graphical_perception` is now held: its ranking of elementary
  perceptual tasks is the authors' hypothesis; their experiments test only position against length and
  position against angle. Heer & Bostock 2010 replicate. Several OCR errors are listed in the file's
  `[NOTE]`s.
- **C17 and C18:** `tufte_1983_visual_display` is held — the **first edition, 1983** (tenth printing
  1990), not the 2001 second edition: cite it as 1983 with its page numbers. Lie Factor (p. 57): "size
  of effect shown in graphic" over "size of effect in data", "greater than 1.05 or less than .95
  indicate substantial distortion", the fuel-economy example 783/53 = 14.8; data-ink and the data-ink
  ratio; Tufte gives no one-line definition of chartjunk (it is introduced on p. 107). The formulas in
  the file were transcribed from page images in `[NOTE]`s: quote the passage text, set the formula in a
  `working` block in your own notation. `correll_2020_truncating_yaxis` is an arXiv preprint under
  arXiv's distribution licence only: quote briefly, locate by section heading.
  `bergstrom_west_2016_proportional_ink` states no licence and no date (the year is Wilke's).
- **C14–C22, Wilke:** `wilke_2019_dataviz_*` is CC BY-NC-ND 4.0 — quote; never adapt its figures or
  tables into a new figure. **C22 follows Wilke's Preface**: it says Excel is "not recommended for
  figure preparation"; teach the procedure tool-free, say a spreadsheet's defaults need heavy changing,
  and route plotting code to the R book (S52). C21 (tables) rests on ICMJE §3.h and Wilke ch. 22,
  "Tables".
- **C19 colour:** `krishnamurthy_2021_cvd_india` measured boys aged 11-17 in one Tamil Nadu district:
  it is not a rate for India; say what it is.
- **C07:** Gopen & Swan is a retyped reprint with no page numbers: locate by section. The Plain
  Language Guidelines are the 2011 PDF from a third-party copy (plainlanguage.gov was offline).
- **C18:** Bateman 2010 is a camera-ready PDF on a course reading folder; quote as the CHI paper.

**Notation, shared by every batch so the book reads as one:** words per sentence = "average sentence
length" (ASL); syllables per word = "average syllables per word" (ASW); Flesch Reading Ease score
"FRE"; the grade-level formula "the Flesch–Kincaid grade level" (FKGL) with the naming caveat above;
Lie Factor "LF"; a percentage-point difference written out in words ("3.4 percentage points"), never
"pp"; per cent written "per cent" in prose and "%" in tables and figures. Introduce every symbol in
words at first use.

Never tell the reader to open a file in `sources/`. Name the instrument by its own title and give
the public URL from `check/references/library.bib`.

A `boundary` must-know point names a limit of the technique — when the tool stops being trustworthy
and what the reader should do then. Never a table-of-contents entry ("This section gets you...").

Prose fields are literal blocks (`|`), never folded (`>`). Columns go in a ```` ```table ```` block.
Display arithmetic goes in a ```` ```working ```` block, never indented. Write exponents as `10^7`
and logarithms as `log10`; no markup. Introduce an operator in words beside its symbol the first
time. A writing book shows writing: a before-and-after pair of a paragraph or sentence goes in a
quoted block or a two-column table, and the "before" is labelled as invented unless it is quoted from a
held source. **Figures:** every section gets at least one, unless one line in `figure_note` says why a
figure would teach nothing the prose does not; a quantitative section gets a figure of its worked
relationship (C17: the same data drawn with a zero and a truncated baseline is the obvious one). Read
`claude.md` §4, "Figures", and declare each as a `figures:` entry with a `spec` as in
`check/schema/example.concept.yml` (file names `s58-r1-cNN-<what>.png`). Run
`python check/figures/draw.py --book S58-R1` to see that each spec passes; never draw by hand. **Do not
edit `check/figures/draw.py` or `figspec.py`**: other drafters run it at the same time. If the figure
you want needs a kind the tool does not draw, declare the nearest kind it does draw, or leave a
`figure_note` and describe the wanted figure with its numbers in your notes.

**Scratch:** any helper script or scratch file goes in `/home/claude/scratch-s58-<your batch>/`, never
a shared name, never in the repository.

**Glossary:** do not edit `prose/GLOSSARY.md`. Put every new term's proposed row (same columns as
that file; read its header and a few rows) in your notes file under "Glossary rows". Check that the
term is not already glossed there; if it is, use the existing sense.

Before you hand back, check your own work as the auditor will. Run `python check/build.py --check`
(it takes about three minutes) until blocking is zero for your records (other drafters are writing
other S58 records at the same time; ignore failures in files that are not yours). Recompute every
practice answer and every number in a `working` block in Python, not by reading it. For every quote,
confirm it is in the source file's passages and states the number it is cited for. Check each item of
`check/SELFCHECK.md`, including 4a, 4b, 6a, 14a and 20-22.

Write your notes to `books/S58-R1/draft-notes-<your batch>.md`: records written, anything unsourced,
why each practice-set size, figures wanted, numbers.yml keys added, notation rows needed, glossary
rows, and **notes for others** (anything another section must say or must not contradict). Then
return at most 150 words.
