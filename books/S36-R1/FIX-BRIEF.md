# Fixer brief · S36-R1 (Task 4 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S36-R1`. Do not commit or push. Other fixers
are working on other sections at the same time: edit only your own record
(`check/records/S36/<RECORD-ID>.yml`), its figure specs/PNGs (`check/figures/s36-r1-cNN-*`), and
your defect file. Never edit `sources/`, `sources/INDEX.yml`, `check/references/library.bib`,
`prose/GLOSSARY.md`, `check/build.py` or any other record; never fetch from the web. If a fix needs a
source that is not held, or a change to a shared file, write that under the defect and leave it open.

Read `books/S36-R1/defects/<RECORD-ID>.md` and the record it names. Read the parts of `claude.md`
the defects cite (and "The one rule that matters"), and nothing else of it. For a defect that
depends on what a source says, open the held file in `sources/` and check it yourself: auditors
can be wrong — if one is, write "withdrawn: <reason, with the source's words>" and change nothing.

Apply every other item. Rules while fixing: a claim without an opened source is not written down
as a fact; every number's `quote` must state that number; keep the reader's second person; keep
sentences short (one idea each) — the compression pass is done, so do not re-grow the section: fix
with the fewest words that close the defect, and prefer deleting a false sentence to adding a
qualifying one. Never cite a Book 0 section by record id in a way that bypasses the renderer
(write `B0-R0-Cnn`, `S01-R1-Cnn` or `S36-R1-Cnn` in backticks; the build prints them as "Book 0, B4" /
"Book 1, section 3" / "section 3"). Expand every abbreviation at first use in the section. If a fix changes a number a
figure uses, update the figure's spec and run `python check/figures/draw.py --book S36-R1`, then
look at the PNG with the Read tool.

Then run `python check/build.py --check` and fix until blocking is zero for this record (the
arithmetic check evaluates every equation: a blocking failure from it is a real slip). Recompute
every practice/exercise answer you touched in Python. Then run
`python check/build.py --subject S36-R1` and read **your section only** in `check/_build/S36-R1.md`
(heading "### N · ..."). Every place you have to read a sentence twice is a defect: fix it.

Under each defect in the defects file, write one line starting "Fixer:": what you changed (or
"withdrawn: ..." / "open: needs ..."). Return at most 150 words: fixed / withdrawn / open counts,
and anything open.

**Book-wide decisions (conductor, 24 Sep 2026) — apply them wherever your defects touch them, so
fourteen fixers produce one book:**

1. **Confidentiality.** C07 is the book's statement: you promise confidentiality with its stated
   limits (what ICMR 2017 lists), never absolute secrecy. No section may tell the reader to promise
   "nothing said will reach the clinic" or "nothing will ever be shared"; say instead what will not
   be passed on to the clinic staff and name the limits once, pointing to `S36-R1-C07`.
2. **Consent records and names.** The signed consent form carries the person's name and is kept
   apart from the recording and transcript; transcripts and notes carry a label only (`R1`). Any
   section that says otherwise follows this.
3. **"Code" and "label".** A code is a short label written beside a passage while reading
   (`S36-R1-C12`). The stand-in for a person's name (`R1`) is a "label", never a "code".
4. **Open and closed.** A question whose answer is a number, a yes or no, or a choice from a list
   is closed — "how often", "how many", "how long" included. A question that asks for an account in
   the respondent's words is open. `S36-R1-C05` states this rule; every practice answer and every
   example in the book follows it.
5. **The gate.** The respondent speaks more than you do: your share of all words in the transcript
   is under 50 per cent. Words, not turns.
6. **Unsourced claims.** Where a defect finds no held source for a claim (the evidence hierarchy,
   "keep the transcript in the language spoken", a rule firmer than its source), delete it or
   soften it to what a held source says; never keep it as fact. A claim that is the book's own
   reasoning must read as reasoning ("because..."), not as a finding.
7. **Where sources disagree** (focus-group size: Kitzinger four to eight; Blackstone reports other
   ranges), say that they differ and give each with its source.
8. **Abbreviations.** Expand at first use in each section: ethics committee (EC), non-communicable
   disease (NCD), randomised controlled trial. Do not name the Digital Personal Data Protection Act
   2023 (not held; Harsh's decision pending).
9. **Kinds.** Only `blackstone_2012` is `textbook`; journal papers `primary`; ICMR `guideline`.

Scratch in `/home/claude/scratch-fix-<RECORD-ID>/`. Several fixers run `draw.py` and
`build.py --subject S36-R1` at the same time; if the rendered file looks truncated, re-run it.
