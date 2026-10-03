# Fixer brief · S58-R1 (Task 4 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S58-R1`. Do not commit or push. Other fixers
are working on other sections at the same time: edit only your own record
(`check/records/S58/<RECORD-ID>.yml`), its figure specs/PNGs (`check/figures/s58-r1-cNN-*`), and
your defect file. Never edit `sources/`, `sources/INDEX.yml`, `check/references/library.bib`,
`prose/GLOSSARY.md`, `check/build.py` or any other record; never fetch from the web. If a fix needs a
source that is not held, or a change to a shared file, write that under the defect and leave it open.

Read `books/S58-R1/defects/<RECORD-ID>.md` and the record it names. Read the parts of `claude.md`
the defects cite (and "The one rule that matters"), and nothing else of it. For a defect that
depends on what a source says, open the held file in `sources/` and check it yourself: auditors
can be wrong — if one is, write "withdrawn: <reason, with the source's words>" and change nothing.

Apply every other item. Rules while fixing: a claim without an opened source is not written down
as a fact; every number's `quote` must state that number; keep the reader's second person; keep
sentences short (one idea each) — the compression pass is done, so do not re-grow the section: fix
with the fewest words that close the defect, and prefer deleting a false sentence to adding a
qualifying one. Never cite a Book 0 section by record id in a way that bypasses the renderer
(write `B0-R0-Cnn`, `S01-R1-Cnn` or `S58-R1-Cnn` in backticks; the build prints them as "Book 0, B4" /
"Book 1, section 3" / "section 3"). Expand every abbreviation at first use in the section. If a fix changes a number a
figure uses, update the figure's spec and run `python check/figures/draw.py --book S58-R1`, then
look at the PNG with the Read tool.

Then run `python check/build.py --check` and fix until blocking is zero for this record (the
arithmetic check evaluates every equation: a blocking failure from it is a real slip). Recompute
every practice/exercise answer you touched in Python. Then run
`python check/build.py --subject S58-R1` and read **your section only** in `check/_build/S58-R1.md`
(heading "### N · ..."). Every place you have to read a sentence twice is a defect: fix it.

Under each defect in the defects file, write **one line starting exactly `Fixed:`, `Partly:` or
`Rejected:`** (the format `python check/defects.py S58-R1` reads; defects are the numbered items
`1. **...`): `Fixed:` what you changed; `Partly:` what you changed and who owns the rest (e.g. "the
rest needs a renderer change in a contract-change chat"); `Rejected:` why the text was right, with the
source's words. A defect the auditor already marked withdrawn still gets a `Rejected:` line saying so.
Return at most 150 words: fixed / partly / rejected counts, and anything left to others.

**Book-wide decisions (conductor, 3 Oct 2026) — apply them wherever your defects touch them, so
twenty-three fixers produce one book:**

1. **Reference lists.** The reference list printed after each section is made by the series' build
   software in a house style; it is not NLM style and its numbering is per section. That cannot be
   changed in this book (the renderer is shared and frozen). C05's fixer adds one short sentence to C05
   saying the book's own reference lists are printed in the series' house style and are not a model:
   the reader's references follow NLM as C05 teaches. Every other defect that asks for NLM-formatted
   rendered reference lists: `Partly:` — say so, and that the renderer change is owned by a
   contract-change chat. Citations and examples written in a record's own prose must follow C05.
2. **Figure tool limits.** A legend drawn beside direct labels, and the palette's two colours that
   turn the same grey (C22, and any two-series figure): `Partly:`, owned by a contract-change chat
   (`DEFECTS.md` FIG-1, FIG-2). Make the figure readable in grey through direct labels; say nothing in
   the prose that the figure contradicts.
3. **People-first wording.** Prose says "with overweight or obesity" (claude.md §9). The survey's
   indicator may be named in the survey's own words when quoted or when naming the indicator ("the
   NFHS indicator 'overweight or obese'"). Never "obesity" for "overweight or obesity". A sentence the
   book offers the reader to reuse (`reporting_sentence`, model answers) follows the same rule.
4. **Claim first, and where.** C02's rule (the claim before its evidence) governs a results paragraph
   and the abstract; C04's (the introduction ends on the question, the discussion opens with the
   answer) governs the sections around it. Where your section states either, say which part it
   governs, in one clause, so they never read as contradicting each other.
5. **What counts as kept (C13, C23).** A part of the one message is kept only if the reader's sentence
   carries it at the same strength: "obesity" for "overweight or obesity" is a change; "increasing" for
   a rise between two surveys overstates (two rounds are not a trend) and is a change. C13's worked pass
   must follow C08 and C23.
6. **Bars on a logarithmic axis.** Follow Wilke ch. 17 as held (a bar of a ratio on a log axis starts
   at 1). C15 changes to agree with C17; do not tell readers to avoid bars there.
7. **Lie Factor.** The general form is LF = (size of effect shown in the graphic) ÷ (size of effect in
   the data) (Tufte 1983, p. 57). The shortcut a ÷ (a − s) holds only for a rise from the starting value
   a with the axis starting at s; state that condition wherever the shortcut appears, and give the
   general form for a fall or a comparison of two groups.
8. **The build.** The build target (rewrite one section of your own manuscript or thesis) is set in
   the book's "How to read" page. The first exercise that refers to "the section you chose for this
   book's build" (C02) says so in one clause; later ones may refer back to it.
9. **Nothing from memory.** A claim no held file carries is deleted, not softened (e.g. "many journals
   follow ICMJE", "NFHS reports this share in each round", the NFHS-1/2 point). A procedure the book
   invents (the reverse outline as worded here, the figure sheet) opens "In this book, …" or is plainly
   the book's own advice, never attributed to a source.
10. **Abbreviations.** Expand at first use in each section, in the section's words: National Family
    Health Survey (NFHS), accredited social health activist (ASHA), standard deviation (SD), standard
    error (SE), confidence interval (CI), Flesch Reading Ease (FRE), average sentence length (ASL),
    average syllables per word (ASW), Lie Factor (LF), International Committee of Medical Journal
    Editors (ICMJE), body mass index (BMI). Drop one used only once or twice. C08's limit on
    abbreviations applies to a paper's nonstandard ones; say so if your defect touches it.
11. **Invented examples.** Every invented "before" text, reader, ward or dataset says once that it is
    invented ("a made-up draft", "an invented ward"). A figure or sentence that describes a worked
    example the text does not show is a defect: show the example in a few lines if it is what teaches,
    or cut the reference to it.
12. **Cross-references and concept_deps.** A pointer to another section names the section that teaches
    it, in backticks as a record id (`S58-R1-C08`), and that section is in `concept_deps` if it is earlier.

Scratch in `/home/claude/scratch-s58-fix-<RECORD-ID>/`. Several fixers run `draw.py` and
`build.py --subject S58-R1` at the same time (each takes 2–3 minutes); if the rendered file looks
truncated, re-run it.
