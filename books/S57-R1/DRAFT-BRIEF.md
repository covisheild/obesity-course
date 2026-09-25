# Drafter brief · S57-R1 (Task 2 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S57-R1`. Do not commit, push, fetch from the
web, or use GitHub tools. Write only the files named for you.

Read `claude.md`: "The one rule that matters", the whole authoring style sheet (§1–§11a), and
specification §1 and §4. Skip §12 and the rest of the specification. Read the two exemplar records
you are given before writing a word — they are the standard, and matching them matters more than
following the rules in the abstract.

Read `books/S57-R1/INVENTORY.md` (your concepts' rows: what each must cover, its Book 0 sections,
its sources, whether it is quantitative), `books/S57-R1/READY.md`, `books/S57-R1/INTAKE.md` and
`sources/INDEX.yml` (which source files and citekeys are held, and what each file does and does not
hold — read the header of every source file you cite). This is **a subject book** on teaching,
mentorship and leading; its reader has read Book 0 only (it does not depend on Books 1-2). Do not
re-teach what a Book 0 section in your row teaches; name it where the reader needs it (as the
exemplars do for earlier sections) and list it in `ground_floor_deps`. To see what a Book 0 section
actually says, read only its `definition` and `must_know` in `check/records/B0/<id>.yml`.

The reader is a medical graduate training in community medicine in India who will teach students,
residents and health workers, and later lead teams. Examples should come from that world (teaching
a batch of MBBS students, a session for ASHA workers, a journal club), and, where natural, from
obesity and nutrition, the series' subject.

Write one YAML file per concept at `check/records/S57/<concept id>.yml` (subject `S57`, rung `1`,
`sequence` = the concept number), using `check/schema/example.concept.yml` as the template and
`check/schema/concept.schema.json` as the schema. `concept_deps` may name only earlier S57-R1
concepts.

For every concept the inventory marks quantitative, write `practice[]` on the ladder in `claude.md`
§7a — levels 1-3 mechanical on bare numbers, 4-6 applied to a real quantity with its unit, 7-8
diagnostic on a worked answer that is wrong, 9-10 transfer from a claim in words. How many is your
judgement, **between three and eighteen** (claude.md §7a), chosen from
the technique and the number of moves that compose in it. The set must reach both ends of
the ladder, and say in one line in your notes why you chose the number. Prompts carry no hint of
the answer. Answers show every line. A problem quoting a real figure names its citekey in `refs`;
where no real figure exists, use bare numbers rather than inventing one.

For every factual claim, quote the exact words from the file in `sources/` that carry it, and put
the file and section in the locator. The quote must state the number it is cited for. If no held
file carries it, set `opened: false`, say in `verified.note` which instrument is needed, and write
the concept so it does not depend on the unopened claim. The source files mark which passages are
verbatim; never quote a `[NOTE]` line or a header.

**What intake found, which overrides the inventory where they differ:**
- C14: the instruments in force are the **NMC CBME Curriculum 2024** (`nmc_cbme_2024`: seven IMG
  roles, no "S" level, two-week Foundation Course) under **GMER 2023** (`nmc_gmer_2023`; the
  separate "Guidelines under GMER 2023" circular was withdrawn, the Regulations were not; the
  withdrawal circular itself is NOT held, so state only what the held files say, e.g. from
  `mahajan_gupta_2024_gmer_cbme`), and the faculty course requirement is in the **Medical
  Institutions (Qualifications of Faculty) Regulations 2025** (`nmc_miqf_2025`), which replaced TEQ
  2022 (`nmc_teq_2022`, superseded: cite only to say it was replaced). The 2018 curriculum and 2019
  Foundation Course module (`mci_cbme_ug_curriculum_2018_vol1`, `mci_foundation_course_2019`) are
  history; quote them sparingly (they carry MCI copyright lines).
- C13/C15: Kirkpatrick's levels are held only in Frich 2015's wording ("reaction, knowledge,
  behavioral change, system results") — use that wording when quoting. **Kotter is now held**
  (`kotter_1990_what_leaders_do`, the 2001 HBR reprint, supplied by Harsh): quote Kotter in his own words;
  Stoller 2020 (`stoller_2020_leadership`) is a physician-leadership adaptation "after Kotter", cite it as Stoller's.
- C06: **Pashler 2008 is now held in full** (body, the crossover-interaction criterion, the acceptable and
  unacceptable patterns of Figure 1 described in text; the plotted panels are not held). A 2×2 table of
  means that illustrates the criterion must still be labelled as invented numbers, not data.
- C07: **Rozenblit & Keil 2002 is now held in full** (author manuscript: Studies 1-12, statistics, Table 8;
  mean ratings exist only as graphs, so no mean rating can be quoted). `fisher_keil_2015_ioed` restates it.
- The PDF-derived files keep ligatures (ﬁ, ﬂ) as extracted: a quote must copy them exactly.
- C01: Deslauriers 2019's test of learning was taken at the end of the class period, not days later;
  it shows the gap between feeling of learning and measured learning, not long-term retention.
  Its licence is CC BY-NC-ND: quote, never adapt its figures or tables into a new figure.
- C02/C12: the Cochrane Handbook's SMD formula is an image; only its definitions in words are held.
  Hake 1998 is held as its abstract only (it defines the average normalised gain in words).
- Roediger & Karpicke 2006 and Dunlosky 2013 are held from the published PDFs; Cepeda 2008 from the
  authors' in-press manuscript (say "the authors' manuscript" if a number could differ).

**Notation, shared by every batch so the book reads as one:** test scores as percentages of the
maximum (0-100%) unless a source uses raw marks; pre-test score `pre`, post-test `post`, a delayed
test `delayed`; raw gain `post - pre` in percentage points; normalised gain `g = (post - pre) / (100 - pre)`
as a fraction; mean difference between two groups `MD`; standardised mean difference `SMD` (Cochrane's
term; mention that many papers call it Cohen's d or an effect size `d` only if a held file says so);
standard deviation `SD`. Time between study and test is the "retention interval"; time between two
study sessions is the "gap". Introduce every symbol in words at first use.

Never tell the reader to open a file in `sources/`. Name the instrument by its own title and give
the public URL from `check/references/library.bib`.

A `boundary` must-know point names a limit of the technique — when the tool stops being trustworthy
and what the reader should do then. Never a table-of-contents entry ("This section gets you...").

Prose fields are literal blocks (`|`), never folded (`>`). Columns go in a ```` ```table ```` block.
Display arithmetic goes in a ```` ```working ```` block, never indented. Write exponents as `10^7`
and logarithms as `log10`; no markup. Introduce an operator in words beside its symbol the first
time. Use `illustrations` (a list) where one illustration does not do the teaching. **Figures:** every section gets at least one, unless one line in `figure_note` says why a figure
would teach nothing the prose does not; a quantitative section gets a figure of its worked
relationship. Read `claude.md` §4, "Figures", and declare each as a `figures:` entry with a `spec`
as in `check/schema/example.concept.yml` (file names `s57-r1-cNN-<what>.png`). Run
`python check/figures/draw.py --book S57-R1` to see that each spec passes; never draw by hand. **Do not edit
`check/figures/draw.py` or `figspec.py`**: other drafters run it at the same time. If the figure you
want needs a kind the tool does not draw (a curve from a formula, a shaded area under a curve, a
tangent line), declare the nearest kind it does draw, or leave a `figure_note` and describe the
wanted figure with its numbers in your notes; the figure planner extends the tool once.

**Scratch:** any helper script or scratch file goes in `/home/claude/scratch-<your batch>/`, never a
shared name.

**Glossary:** do not edit `prose/GLOSSARY.md`. Put every new term's proposed row (same columns as
that file; read its header and a few rows) in your notes file under "Glossary rows". Check that the
term is not already glossed there; if it is, use the existing sense.

Before you hand back, check your own work as the auditor will. Run `python check/build.py --check`
until blocking is zero for your records (other drafters are writing other S57 records at the same
time; ignore failures in files that are not yours). Recompute every practice answer in Python, not
by reading it. For every quote, confirm it is in the source file and states the number it is cited
for. Check each item of `check/SELFCHECK.md`.

Write your notes to `books/S57-R1/draft-notes-<your batch>.md`: records written, anything
unsourced, why each practice-set size, figures wanted, glossary rows. Then return at most 150 words.
