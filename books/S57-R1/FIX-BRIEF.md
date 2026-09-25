# Fixer brief · S57-R1 (Task 4 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S57-R1`. Do not commit or push. Other fixers
are working on other sections at the same time: edit only your own record
(`check/records/S57/<RECORD-ID>.yml`), its figure specs/PNGs (`check/figures/s57-r1-cNN-*`), and
your defect file. Never edit `sources/`, `sources/INDEX.yml`, `check/references/library.bib`,
`prose/GLOSSARY.md`, `check/build.py` or any other record; never fetch from the web. If a fix needs a
source that is not held, or a change to a shared file, write that under the defect and leave it open.

Read `books/S57-R1/defects/<RECORD-ID>.md` and the record it names. Read the parts of `claude.md`
the defects cite (and "The one rule that matters"), and nothing else of it. For a defect that
depends on what a source says, open the held file in `sources/` and check it yourself: auditors
can be wrong — if one is, write "withdrawn: <reason, with the source's words>" and change nothing.

Apply every other item. Rules while fixing: a claim without an opened source is not written down
as a fact; every number's `quote` must state that number; keep the reader's second person; keep
sentences short (one idea each) — the compression pass is done, so do not re-grow the section: fix
with the fewest words that close the defect, and prefer deleting a false sentence to adding a
qualifying one. Never cite a Book 0 section by record id in a way that bypasses the renderer
(write `B0-R0-Cnn`, `S01-R1-Cnn` or `S57-R1-Cnn` in backticks; the build prints them as "Book 0, B4" /
"Book 1, section 3" / "section 3"). Expand every abbreviation at first use in the section. If a fix changes a number a
figure uses, update the figure's spec and run `python check/figures/draw.py --book S57-R1`, then
look at the PNG with the Read tool.

Then run `python check/build.py --check` and fix until blocking is zero for this record (the
arithmetic check evaluates every equation: a blocking failure from it is a real slip). Recompute
every practice/exercise answer you touched in Python. Then run
`python check/build.py --subject S57-R1` and read **your section only** in `check/_build/S57-R1.md`
(heading "### N · ..."). Every place you have to read a sentence twice is a defect: fix it.

Under each defect in the defects file, write one line starting "Fixer:": what you changed (or
"withdrawn: ..." / "open: needs ..."). Return at most 150 words: fixed / withdrawn / open counts,
and anything open.

**Book-wide decisions (conductor, 25 Sep 2026) — apply them wherever your defects touch them, so
sixteen fixers produce one book:**

1. **Learning vs performance.** C01 defines learning as a lasting change shown on a test taken
   later. A test taken at the end of the same session (Deslauriers 2019's test of learning, a
   five-minute test) measures performance then, not learning in C01's sense: say "scored at the end
   of the class", never "learned more", unless the source measured later.
2. **Say what was measured, no further.** State each study's design as the held text gives it
   (Deslauriers: every student had both an active class and a lecture; Roediger & Karpicke
   Experiment 1 within-subjects; Agarwal: 19 comparisons were retrieval against rereading), and do
   not carry a finding to a population, task or setting the source did not test. Where the book
   extends a finding, say "this book suggests", in one short clause.
3. **Evidence words.** Rereading and highlighting are "low utility" (Dunlosky); for learning-styles
   matching there is "no adequate evidence" (Pashler). Never "do not work" or "proven false".
4. **Cepeda 2008.** Numbers are from the authors' in-press manuscript: say so once in C04. The
   350-day best gap and any planning share (percent of the retention interval) must be one number
   everywhere, prose and figure, taken from the held file; a share derived by the book is labelled
   as derived.
5. **Nothing from memory.** A claim no held file carries is deleted, not softened (e.g. a
   meta-analysis the source file does not hold). Working definitions the book gives without a
   source (C16: power, authority, delegation, role clarity, kinds of conflict) open with
   "In this book, …" so the reader can see they are the book's own.
6. **Abbreviations.** Expand at first use in each section, in the section's own words: standardised
   mean difference (SMD), standard deviation (SD), accredited social health activist (ASHA),
   retention interval (write it out; do not use "RI"), Graduate Medical Education Regulations
   (GMER), Competency Based Medical Education (CBME), feeling of learning (FOL). `MD` in this book is
   the mean difference; the degree is written "the postgraduate MD degree" at most once, or avoided.
   Drop an abbreviation the section uses only once or twice.
7. **Figures.** C13 `form-by-level` is dropped (remove its entry and PNG). A figure whose numbers
   change is redrawn from its spec and looked at. The C16 Crandall bar for "80 to 100" is labelled
   as the upper end, or the figure compares like with like.
8. **Cross-references.** A pointer to another section must name the section that actually teaches
   the thing (retention interval: section 1; testing effect numbers: the experiment named).

Scratch in `/home/claude/scratch-fix-<RECORD-ID>/`. Several fixers run `draw.py` and
`build.py --subject S57-R1` at the same time; if the rendered file looks truncated, re-run it.
