# Drafter brief · S37-R1 (Task 2 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S37-R1`. Do not commit, push, fetch from the
web, or use GitHub tools. Write only the files named for you.

Read `claude.md`: "The one rule that matters", the whole authoring style sheet (§1–§11a), and
specification §1 and §4. Skip §12 and the rest of the specification. Read the two exemplar records
you are given before writing a word — they are the standard, and matching them matters more than
following the rules in the abstract. Read `check/SELFCHECK.md` (all items, including 4a).

Read `books/S37-R1/INVENTORY.md` (your concepts' rows: what each must cover, its Book 0 sections,
its sources, whether it is quantitative, what it serves), `books/S37-R1/READY.md` (including "After
intake") and `books/S37-R1/INTAKE.md` (the "For drafters" / "What a drafter must know" notes of each
group), and `sources/INDEX.yml` (which files and citekeys are held). Read only the source files your
concepts need.

This is **a subject book**: its reader has read Book 0 (records `check/records/B0/`) and may have
read Book 1 (S01-R1, energy balance; `check/records/S01/`). Do not re-teach what a Book 0 section in
your row teaches; name it where the reader needs it ("Book 0, F5" style, as the exemplars do) and
list it in `ground_floor_deps`. To see what a Book 0 section says, read only its `definition` and
`must_know` in `check/records/B0/<id>.yml`.

Write one YAML file per concept at `check/records/S37/<concept id>.yml` (subject `S37`, rung `1`,
`sequence` = the concept number), using `check/schema/example.concept.yml` as the template and
`check/schema/concept.schema.json` as the schema. `concept_deps` may name only earlier S37-R1
concepts (other batches are drafting them at the same time; rely on the inventory's row for what an
earlier concept covers, and do not re-teach it). `outcome_refs` / `bridge_ref` must carry the ids in
your row's "Serves" column, including amendment ids (`S37-R1-A01`, `S37-R2-A01`, `S37-R2-A02`).

**Quantitative concepts** (C04, C06, C07, C10, C13) get `practice[]` on the ladder in `claude.md`
§7a — levels 1-3 mechanical on bare numbers, 4-6 applied to a real quantity with its unit, 7-8
diagnostic on a worked answer that is wrong, 9-10 transfer from a claim in words. **Between three
and eighteen**, chosen from the technique; reach both ends of the ladder; one line in your notes on
why that number. Prompts carry no hint of the answer. Answers show every line. A problem quoting a
real figure names its citekey in `refs`; where no real figure exists, use bare numbers.

For every factual claim, quote the exact words from the file in `sources/` that carry it, and put
the file and section in the locator. The quote must state the number it is cited for. Never quote a
`[NOTE]` line or a file header — only source text. If no held file carries it, set `opened: false`,
say in `verified.note` which instrument is needed, and write the concept so it does not depend on
the unopened claim. Institutional records carry `review.as_of` and an event trigger (the next CCEA
MSP decision, the next duty notification, the next scheme revision).

Never tell the reader to open a file in `sources/`. Name the instrument by its own title and give
the public URL from `check/references/library.bib`.

## Facts intake established that you must honour

- **Not held:** Hawkes et al. 2020 (C15: `opened: false`; use WHO 2017's own terms — "do no harm",
  retrofit, de novo — and define "single-duty" and "working against the other burden" in plain words
  as this book's reading tool, not as anyone's official classification); PM POSHAN guidelines 2023
  (C12, C13: use `s37_pib_1812421`'s norms table; do not state Centre-State cost sharing); CACP "About
  us" (C08, C09: do not date CACP's founding or give its old name as fact; the Food Corporations Act
  1964 and DFPD's history are held).
- **FAO import dependency ratio** (C06): FAO's handbook defines it as imports ÷ (production + imports
  − exports), not imports ÷ consumption. Use FAO's definition as held. FAO's "waste" excludes household
  waste.
- **RBI farmer's-share papers** (C04): the tomato-onion-potato paper is **WP 08/2024**
  (`rbi_wp_2024_08_tops`); 07/2024 pulses; `rbi_wp_2024_fruits` (06); `rbi_wp_2024_poultry` (05).
  Vegetable breakdowns by intermediary exist only as chart images; use only the percentages stated
  in text (tomato 33.5, onion 36.2, potato 36.7 as held — check the file).
- **Edible oil duty** (C06, C10, C16): changed on 24 Sep 2026 (`s37_edible_oil_duty`). Use those rates,
  dated; the NMEO releases' duty figures are older.
- **Economic cost of grain** (C10): 2025-26 (BE) from `s37_economic_cost_grain`; the central issue price
  is now zero under PMGKAY; take the date it became zero only from the held text (`pib_1980689`,
  `s37_economic_cost_grain`, `dfpd_pds`), not from memory.
- **DFPD allocation** (C14): `dfpd_pds` text says 595.05 lakh MT for 2025-26 but its own table totals
  607.40; quote the table and say which figure, or avoid the total.
- **The two A01 PIB releases** carry no PDS scale: anganwadi scale from `pib_2251769`; persons from
  `pib_1980689`; tonnes from `dfpd_pds`.
- **Anganwadi norms** (C12, C13): the held 2022 guidelines' supplementary-nutrition table is marked
  "under revision" (revised January 2023 per PIB; revised numbers not held). Quote it as the 2022
  table and say it was under revision.
- **IFCT 2017** (C13): energy in **kJ only**; IFCT converts with 1 kcal = 4.18 kJ. Work in kJ, or, if
  converting to kcal, say which factor and why (Book 0 B4 teaches 4.184); never mix silently.
- **NFHS-5** (C15): adult rows are ages 15–49; only "overweight or obese" for adults.
- **UNEP 2024** (C02): India 55 kg per capita per year household food waste, "medium" confidence,
  from few datapoints — say so.
- **Popkin 2012** (C07): author manuscript; no numbered stages. Forward pointer only.
- **ECA 1955** (C16): the held s.3 does not use the words "stock limits"; describe what the text says.
- **HCES 2023-24** food-group shares are held only as chart labels in the press note; say what level
  of detail is held.
- **No Union "millet mission"** is named as such in the held PIB texts: name what they do say.

## Shared conventions, so the book reads as one

- Money: "Rs" (as the sources write it) with the amount; "per quintal" introduced once as 100 kg.
  Indian numbering (lakh, crore) as the sources give it, with the international equivalent in words
  at first use in each section ("81.35 crore, that is 813.5 million").
- Every official figure carries its year or season and the body that states it ("MSP for kharif
  marketing season 2026-27, CCEA, 13 May 2026").
- Terms: "food system", "food environment", "supply chain" (this rung) vs "value chain" (named, left
  to rung 2), "farm-gate price", "farmer's share of the consumer rupee", "margin", "MSP", "procurement",
  "central pool", "PDS" / "TPDS", "NFSA", "PM POSHAN", "anganwadi", "take-home ration (THR)", "hot
  cooked meal (HCM)", "double burden", "double-duty action". Expand every acronym at first use in
  each section.
- Anything the inventory routes to S37-R2 is named and routed in one line, not taught.

## Style

A `boundary` must-know point names a limit of the technique — when the tool stops being trustworthy
and what the reader should do then. Never a table-of-contents entry ("This section gets you...").
Prose fields are literal blocks (`|`), never folded (`>`). Columns go in a ```` ```table ```` block.
Display arithmetic goes in a ```` ```working ```` block, never indented. Introduce an operator in words
beside its symbol the first time. Use `illustrations` (a list) where one illustration does not do the
teaching. SELFCHECK 4a applies with force here: a figure measured for one group, crop, year or place
is not applied to another without saying so.

**Figures:** every section gets at least one, unless one line in `figure_note` says why a figure would
teach nothing the prose does not; a quantitative section gets a figure of its worked relationship.
Read `claude.md` §4, "Figures", and declare each as a `figures:` entry with a `spec` as in
`check/schema/example.concept.yml` (file names `s37-r1-cNN-<what>.png`). Run
`python check/figures/draw.py --book S37-R1` to see that each spec passes; never draw by hand. **Do not
edit `check/figures/draw.py` or `figspec.py`.** If the figure you want needs a kind the tool does not
draw (for example a flow diagram of a chain), leave a `figure_note` and describe the wanted figure with
its data in your notes; the figure planner deals with it.

**Scratch:** helper scripts go in `/home/claude/scratch-<your batch>/`, never a shared name.

**Glossary:** do not edit `prose/GLOSSARY.md`. Put every new term's proposed row (same columns as that
file; read its header and a few rows) in your notes under "Glossary rows". If the term is already
glossed there, use the existing sense.

Before you hand back, check your own work as the auditor will. Run `python check/build.py --check`
until blocking is zero for your records (other drafters are writing other S37 records at the same
time; ignore failures in files that are not yours). Recompute every practice answer and every number
in a `working` block in Python. For every quote, confirm it is in the source file and states the number
it is cited for. Check each item of `check/SELFCHECK.md`.

Write your notes to `books/S37-R1/draft-notes-<your batch>.md`: records written, anything unsourced,
why each practice-set size, figures wanted, glossary rows. Then return at most 150 words.
