# Drafter brief · S47-R1 (Task 2 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S47-R1`. Do not commit, push, switch branches,
fetch from the web, or use GitHub tools. Write only the files named for you. **No `rm` anywhere in
the repository**; absolute paths only.

Read `claude.md`: "The one rule that matters", the whole authoring style sheet (§1–§11a, including
§4a), and specification §1 and §4. Skip §12 and the rest of the specification. Read
`check/SELFCHECK.md`. Read the exemplar records named in your prompt before writing a word — they are
the standard, and matching them matters more than following the rules in the abstract. They were
frozen before the 28 Sep reader checks, so they lack `retrieval` exercises and `{{n:key}}` numbers;
**this book must have both** (`check/reader_checks.py` blocks new books without them).

Read `books/S47-R1/INVENTORY.md` (the header paragraph and your concepts' rows: what each must
cover, its Book 0 sections, its sources, whether it is quantitative), `books/S47-R1/SOURCE-GATE.md`
(what is held, the conductor's decisions) and `sources/INDEX.yml`. This is **a subject book**: its
reader has read Book 0. Do not re-teach what a Book 0 section in your row teaches (F5 `C43` already
teaches legislature/executive/courts, statute/rule/regulation/notification, the Seventh Schedule's
lists, FSSAI's s.92 power and "look for the statute behind a programme"); name it where the reader
needs it and list it in `ground_floor_deps`. To see what a Book 0 section says, read only its
`definition` and `must_know` in `check/records/B0/<id>.yml`. Where your row points to Book 4
(S37-R1), read only the `definition` of that record and give the one fact you need from a held source.

Write one YAML file per concept at `check/records/S47/<concept id>.yml` (subject `S47`, rung `1`,
`sequence` = the concept number), using `check/schema/example.concept.yml` as the template and
`check/schema/concept.schema.json` as the schema. `concept_deps` may name only earlier S47-R1
concepts.

## Drill sets
Quantitative concepts: C11, C15, C17. Write `practice[]` on the ladder in `claude.md` §7a, **three to
eighteen**, chosen from the technique. In this book the "numbers" of the ladder are proposals,
sentences and documents: levels 1-3 mechanical on a bare proposal or sentence (name the instrument,
the list entry, the body; label problem/cause/judgement/remedy; sort informing vs campaigning); 4-6
applied to a real Indian proposal or text from the held sources; 7-8 diagnostic on a worked answer
that is wrong (the minister named instead of the regulator; a scheme mistaken for a law; a frame
mislabelled; a "neutral" paragraph that campaigns); 9-10 transfer from a claim in words (a press line
to trace, a speech to frame, a report sentence to classify and rewrite). Reach both ends of the
ladder; say in one line in your notes why the number. Prompts carry no hint of the answer; answers
show every step. A problem quoting a real document names its citekey in `refs`.

## Sources
For every factual claim, quote the exact words from the file in `sources/` that carry it, with file
and block in the locator. A quote carrying a number must state that number. Never quote a `[NOTE]`
line or a header. If no held file carries a claim, set `opened: false`, say in `verified.note` which
instrument is needed, and write the concept so it does not depend on it — or leave it out.
Read each file's header before quoting it. Book-specific cautions:

- **Constitution**: `constitution` resolves to `constitution_current.txt` (not `constitution.txt`).
- **OpenStax American Government 4e** (`openstax_amgov_4e`, CC BY-NC-SA 4.0) is the textbook for the
  derivable concepts (C01, C10, C12, C15–C17); it is a **US** text: use it for concepts (the stages
  model, interest groups, framing, priming, agenda setting, policy analysts vs advocates), never for
  facts about India. `openstax_intro_polisci_1_2` is a second textbook anchor for C01.
- **Gilson 2012 Reader** (`gilson_2012_hpsr_reader`, © WHO, all rights reserved): its text layer mixes
  two columns; quote short phrases only and only where the run is clean; prefer Walt 2008.
- **Barry 2009** (© Milbank Fund, excerpts): tables come out one cell per line; check any figure.
  US survey, late 2006–early 2007, N = 1,009 — every finding carries its country, years and sample.
- **Koon 2016** states Entman's four functions: cite them as "Entman's, as reported by Koon et al."
  (Entman 1993 is not held).
- **Pielke 2007 is not held.** C17 does not teach his four roles. It names the contrast "honest
  broker" against "issue advocate" as Oliver & Cairney 2019 state it, and may note that Cairney &
  Oliver 2017 describe the honest broker differently.
- **Gollust 2013 is not held**: no experimental evidence on framing and policy support beyond what
  Koon 2016 or Barry 2009 state.
- **COTPA** (`cotpa_2003`) is OCR of a Gazette scan; section numbers are misread in places (header
  lists them). The 2008 Smoking Rules (`mohfw_2008_smoking_rules`) are an Indian Kanoon print, not
  an official copy: cite as the Rules, quote as held.
- **GST**: the Council recommends (Art. 279A; `pib_2163555`); the Central Government notifies under
  CGST Act s.9(1) (`cgst_act_2017_s9_cbic`), which caps the central rate at 20%. Sugar-added and
  aerated drinks (heading 2202) are in Schedule III - 20% of Notification 9/2025-CT(Rate)
  (`cgst_notif_9_2025_rate`, in force 22 Sep 2025), entries re-stated by 01/2026-CT(Rate)
  (`cgst_notif_1_2026_rate`, in force 1 May 2026). The **40%** is the combined slab as PIB 2163555
  states it; never write that the Union levies 40%. The State Acts (SGST) are not held: say only what
  PIB 2163555 says about the State share. Amendment 19/2025 is not held; date the rate "as amended
  by 01/2026-CT(Rate), in force 1 May 2026".
- **Pre-Legislative Consultation Policy** (`plcp_2014`): a minimum of thirty days; it is a policy of
  the Union, not a law. `pib_1797203` adds the government's statements about it.
- **Rule-making**: `general_clauses_act_1897` s.23 is the default procedure where an Act asks for
  "previous publication"; `fssai_2018_packaging_regs` is the worked case (draft of 19 Mar 2018,
  30 days for objections, objections considered, final regulations of Dec 2018).
- **Allocation of Business Rules** (`goi_aob_rules_1961`, amended to series no. 386, 22 Jul 2026):
  the departments are listed in the **First** Schedule and their subjects in the **Second**. Food
  safety (FSS Act 2006) sits with the Department of Health and Family Welfare, Second Schedule.
- **How a Bill becomes an Act**: `rajyasabha_2005_legislative` is dated February 2005;
  `prs_2012_parliament60`'s private members' Bill figures are as of 2012 — state each with its date.
- **NHP 2017** (`mohfw_2017_nhp`, NHSRC copy): Cabinet approval on 15 March 2017 rests on
  `pib_1513000`, not on the policy's own text.
- **Edible-oil call** (`pib_2105618`): the PM's words in Mann Ki Baat, 23 Feb 2025.
- Copyright-restricted sources (`barry_2009_metaphors`, `walt_2008_policy`, `who_fctc_2003`,
  `gilson_2012_hpsr_reader`, `goi_aob_rules_1961`, `goi_tob_rules_1961`, `cotpa_2003`): short phrases
  for audit; never a table or box reproduced.
- **Not held, so not stated**: the Kerala 2016 food tax; Lok Sabha question answers; any claim about
  how often States copy each other's food taxes; SWOT; "power" as a framework (both are proposed map
  amendments awaiting Harsh, not this book's content).

**Reference kinds.** Derivable concepts need at least one `textbook` reference (the two OpenStax
books; the Gilson Reader is a WHO reader: use kind `textbook` only if the schema's definition fits a
methods reader, else `primary`, and say which in your notes). Journal papers are `primary` or
`systematic_review`. Instruments are `instrument`. **Never relabel a source's kind to satisfy the
build** (handover §7, Book 3): if a derivable concept has no textbook that carries it, say so in
your notes and the conductor decides.

## Examples and the running setting
One running setting shared by every batch: **you are a postgraduate in community medicine at a
medical college in Chhattisgarh. Your department wants to propose action on obesity among school
children and young adults in the district. You must work out, for each idea, who would have to act,
under what power, and how to write about it.** The three running proposals, used across sections:
(1) a higher tax on sugar-sweetened drinks (Union and States, through the GST Council); (2) a rule
on what school canteens may sell (find whose subject it is — do not assert an answer the held sources
do not carry); (3) a warning label on packaged foods high in sugar, salt or fat (FSSAI regulation;
S48-R1 owns the detail, here it is only a tracing example). Any person, meeting, memo or quoted
remark you invent is an illustration and the prose says so the first time in each section
("suppose…", "a made-up memo"). Never invent a statistic or attribute an invented sentence to a real
person or body. Real Indian texts for framing come only from held sources (PIB releases, FSSAI Eat
Right India page, NHP 2017).

## Scope
Routed to S47-R2 and named in one line, not taught: Kingdon's multiple streams, the advocacy
coalition framework, punctuated equilibrium, the Walt–Gilson triangle as theory, the tobacco
precedent as a template with its limits, the Overton window, the four-page brief, the WHO/UNICEF
interference frameworks. Routed to S48-R1: the food-regulator map, Article 47, the front-of-pack
dispute, trans fat, courts as a lever. Routed to S37-R1 (pointer only): MSP/CACP, NFSA/PDS, PM POSHAN
and Poshan 2.0. Routed to S39: corporate political activity. Routed to S50: implementation.

## Mechanics
Never tell the reader to open a file in `sources/`. Name the instrument by its own title and give
the public URL from `check/references/library.bib`.

A `boundary` must-know point names a limit of the technique — when the tool stops being trustworthy
and what the reader should do then. Never a table-of-contents entry.

Prose fields are literal blocks (`|`), never folded (`>`). Columns go in a ```` ```table ```` block.
Display arithmetic (if any) in a ```` ```working ```` block. Introduce an operator in words beside
its symbol the first time. Use `illustrations` (a list) where one illustration does not teach enough.

**Retrieval**: every section carries at least one `retrieval` exercise (from-memory prompt, answered
in the appendix). **Numbers**: a number reused in another section is written `{{n:key}}` from
`books/S47-R1/numbers.yml`; if you need a new key, do not edit the file: propose it in your notes
(key, value, source, which sections) and use the literal value meanwhile. You may add
`common_misreading` and, where the section's output is a written note, `reporting_sentence`.

**Figures**: every section gets at least one, unless one line in `figure_note` says why a figure would
teach nothing the prose does not. This book is qualitative; honest data charts are few. Read
`claude.md` §4 "Figures"; declare each as a `figures:` entry with a `spec` as in
`check/schema/example.concept.yml` (file names `s47-r1-cNN-<what>.png`), and run
`python check/figures/draw.py --book S47-R1`. **Do not edit `check/figures/draw.py`, `figspec.py` or
anything under `check/`.** If the figure you want is a diagram the tool does not draw (a chain of
authority, a flow from draft to final notification), write a `figure_note` and describe the wanted
diagram in your notes.

**Scratch**: helper scripts in `/home/claude/scratch-S47-<your batch>/` only.

**Glossary**: do not edit `prose/GLOSSARY.md`. Put each new term's proposed row (same columns as that
file; read its header and a few rows) in your notes under "Glossary rows". If the term is already
glossed, use the existing sense.

**Notes for other batches**: if another batch's section needs a change, do not edit it; write to
`books/S47-R1/notes-for-others-<your batch>.md` (section, what, why).

Before you hand back, check your own work as the auditor will. Run `python check/build.py --check`
until blocking is zero for your records (others are writing other S47 records at the same time;
ignore failures in files not yours). Recompute every practice answer independently. For every quote,
confirm by script that it is in the source file and states the number it is cited for. Check each
item of `check/SELFCHECK.md`, including 4a (does the model or rule apply to this case?).

Write your notes to `books/S47-R1/draft-notes-<your batch>.md`: records written, anything unsourced,
why each practice-set size, figures wanted, glossary rows, numbers keys proposed. Then return at most
150 words.
