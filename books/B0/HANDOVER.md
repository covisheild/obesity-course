# Handover · Book 0 Part A (A1–A8)

Chat of 2026-09-20. Ran Tasks 1 to 4 of `PIPELINE.md` for Book 0 Part A and stopped there. The
compression pass was **not** run, by design: `claude.md` §12 and `PIPELINE.md` Task 5 require 5a,
5b and 5c to be three separate sessions, and running them here would have destroyed the method
while appearing to run it.

**A contract change was made in the same session, at the reader's direction**, and it is the
larger of the two things here. Every concept that teaches a mathematical technique now carries ten
practice problems at rising difficulty, unsolved in the text and answered in the appendix. It is
mandatory and the build blocks without it. `PARALLEL.md` reserves changes to `claude.md`,
`PIPELINE.md` and `check/**` for a between-rounds chat doing nothing else; this was that change,
made deliberately, and the section below records exactly what moved.

---

## What was written

| Section | Concept id | Name | Type | Status |
| --- | --- | --- | --- | --- |
| A1 | `B0-R0-C01` | Counting, place value, and what a calculator is actually doing | derivable | drafted |
| A2 | `B0-R0-C02` | Fractions | derivable | drafted |
| A3 | `B0-R0-C03` | Decimals, rounding, and significant figures | derivable | drafted |
| A4 | `B0-R0-C04` | Percentages, and the percentage of a percentage | derivable | drafted |
| A5 | `B0-R0-C05` | Ratios, rates and proportions | derivable | drafted |
| A6 | `B0-R0-C06` | Powers, roots and scientific notation | derivable | drafted |
| A7 | `B0-R0-C07` | Logarithms — what they are for before how they work | derivable | drafted |
| A8 | `B0-R0-C08` | Orders of magnitude and the back-of-envelope sanity check | derivable | drafted |

Book 0 is now **12 of 43 sections**, carrying **80 practice problems** across the eight new ones.
Build: `blocking 0, warnings 11`, and all eleven warnings are `reference not yet opened` — eight
new ones plus the three that were already there.

**Files written or changed.** Listed in full at the bottom.

---

## What is still unsourced, and why

**One textbook. Eight locators. That is the whole Part A backlog.**

Every one of the eight is `derivable`, so the specification requires a `textbook` anchor, and no
textbook is reachable from this authoring environment. `plan/INVENTORY-PILOT.md` established that
before any authoring started and called it structural rather than incidental; it is unchanged.

All eight therefore carry one reference to `pending_arithmetic_text`, added to
`check/references/library.bib` alongside the three placeholders already there, with
`opened: false`, `claim_located: false` and a note in `verified.note`. None can reach `verified`,
and therefore none can reach `released`, until somebody with library access opens one school-level
mathematics text and fills in eight chapter locators:

| Concept | Locator wanted |
| --- | --- |
| `B0-R0-C01` | chapter on place value and the base-ten system |
| `B0-R0-C02` | chapter on fractions and equivalent fractions |
| `B0-R0-C03` | chapter on decimals, rounding and significant figures |
| `B0-R0-C04` | chapter on percentages and percentage change |
| `B0-R0-C05` | chapter on ratio, proportion and rate |
| `B0-R0-C06` | chapter on indices, roots and standard form |
| `B0-R0-C07` | chapter on logarithms and logarithmic scales |
| `B0-R0-C08` | chapter on estimation and approximation |

**Say plainly what this anchor is and is not.** For a derivable concept the anchor is not the
evidence. The evidence is the derivation, and the reader can check every line of Part A with the
calculator the reader floor grants them. The anchor is the canonical text a specialist would be
pointed at, and the spec requires one. So this backlog is real and it is not urgent in the way
S48's three missing FSSAI instruments are.

**Nothing else in Part A is unsourced.** No claim about the world is made that is not either
derivable in front of the reader, or quoted from a file already in `sources/` and located by
searching it.

---

## Every number that needs re-checking, with its trigger

Twenty-one quoted figures now, from three files. The first eleven rows are in
`check/_build/numbers_register.csv`; the last six reach the corpus through practice problems, which
the register does not carry — see the note at the end of `DEFECTS.md`.

| Figure | Where it is | Source and locator | Re-check trigger |
| --- | --- | --- | --- |
| 10,00,000 rupees, misleading food advertisement | C01, C07 | `fss_act_2006.txt` s.53 | next amendment to the Food Safety and Standards Act, 2006 |
| 5,00,000 rupees, sub-standard food | C01, C07 | `fss_act_2006.txt` s.51 | same |
| 5,00,000 rupees, food not of the nature or quality demanded | C01 exercise | `fss_act_2006.txt` s.50 | same |
| 25,000 rupees, the proviso to s.50 | C07 | `fss_act_2006.txt` proviso to s.50, read with s.31(2) | same |
| 3,00,000 rupees, misbranded food | C07 | `fss_act_2006.txt` s.52(1) | same |
| 450 kcal and 12 g protein, lower primary meal | C02, C04, C08 | `nfsa_2013.txt` Schedule II | next amendment to Schedule II of the National Food Security Act, 2013 |
| 700 kcal and 20 g protein, upper primary meal | C02, C04 | `nfsa_2013.txt` Schedule II | same |
| 500 kcal, take-home ration, 6 months to 3 years | C02 exercise | `nfsa_2013.txt` Schedule II | same |
| 800 kcal, malnourished child, 6 months to 6 years | C02 exercise | `nfsa_2013.txt` Schedule II | same |
| 5 kg per person per month, priority households | C03, C05 | `nfsa_2013.txt` s.3(1) | next amendment to s.3 |
| 35 kg per household per month, Antyodaya | C05 | `nfsa_2013.txt` proviso to s.3(1) | next amendment to s.3, **and** any change to what the Central Government specifies per State under the scheme |
| 600 kcal, take-home ration, pregnant woman or lactating mother | C02 practice 4 | `nfsa_2013.txt` Schedule II | next amendment to Schedule II |
| up to 75 per cent rural, up to 50 per cent urban coverage | C04 practice 4 | `nfsa_2013.txt` s.3(2) | next amendment to s.3 |
| 10,00,000 and 50,00,000 rupees, false or misleading advertisement | C01 practice 4, C07 practice 4 | `consumer_prot_2019.txt` s.21(2) and its proviso | next amendment to the Consumer Protection Act, 2019 |
| 1,00,00,000 rupees, District Commission jurisdiction | C01 practice 5, C06 practice 4, C07 practice 4 | `consumer_prot_2019.txt` s.34(1) | same |
| 10,00,00,000 rupees, State Commission jurisdiction | C01 practice 5, C06 practice 4, C07 practice 4 | `consumer_prot_2019.txt` s.47 | same |

**The trigger that matters most, and it is not in the table.** Both source copies are of unstated
and different vintage, and this was found by the audit rather than assumed:

- `fss_act_2006.txt` cites exactly one amending Act anywhere in it — **Act 13 of 2008, w.e.f.
  7 February 2008** — and nothing later.
- `nfsa_2013.txt` cites **no amendment at all**, so it reads as the Act as enacted in 2013.
- `consumer_prot_2019.txt` was checked the same way in the second pass and likewise cites none, so
  it reads as the Act as enacted in 2019.

Neither file says so on its face. `sources/SOURCES.md` now carries a "Vintage of each copy" section
recording it, appended rather than edited, per `PARALLEL.md`. C01 and C07 each carry one sentence
in `analogy_breaks_when` telling the reader these are the figures in this copy and that a later
section teaches how to check a copy's age.

**This is defect 11 in `DEFECTS.md` and it is the one to re-open first.** Part A reproduces, in
eight sections, exactly the failure that `B0-R0-C41` is built around. It is currently handled
honestly rather than fixed, and it is fixed only by obtaining a current copy of each Act.

---

## The glossary, and one correction owed between rounds

Eleven rows were appended to `prose/GLOSSARY.md` for the terms Part A teaches.

**Two existing rows now name the wrong record and were deliberately not changed.** With Part A
written, document order puts the first use of **denominator** in `B0-R0-C02` and of **precision**
in `B0-R0-C03`. Both rows say `B0-R0-C39`. `PARALLEL.md` makes changing an existing row a
between-rounds job, so it is left here:

1. `denominator` — "First taught in" becomes `B0-R0-C02`. The recorded plain words, "the number a
   percentage is a percentage of", describe a percentage and not a fraction. A2 teaches it as the
   number below the line, which is where the reader now first meets it, and A4 gives the recorded
   words verbatim at the point the percentage sense arrives. The row wants both senses.
2. `precision` — "First taught in" becomes `B0-R0-C03`. The recorded words were used unchanged.

---

## Things the next chat would otherwise learn the hard way

**1. A worked calculation must be a fenced code block, not an indented one.** `build.py`'s
`_paragraphs` skips a block whose first character is `|`, `#` or a backtick fence, and measures
everything else as prose. An indented working block is therefore read as one enormous sentence and
produces a long-sentence warning per block. Fencing them removed about forty spurious warnings
across these eight records and changes nothing in the rendered booklet, which treats both as code.
The four records in `done/` never hit this because none of them shows a calculation.

**2. The sentence splitter needs a capital letter.** `_sentences` splits on a full stop followed by
whitespace and then `[A-Z"'(]`. A sentence beginning with a digit or with `10^3` does not split, so
three real sentences get measured as one 32-word monster. Write "Ten to the power three is…" rather
than "10^3 is…" at the start of a sentence. This is a measurement artefact, not a style rule, but
the fix reads better anyway.

**3. Any run of two to six capitals is reported as an unexpanded acronym.** `GUESS` as a marker in
a worked estimate tripped it, and so would `Schedule II`, because `II` matches. Use lower case in
working blocks (`<- a guess`), and write "the second schedule" in prose with the exact locator in
`illustration.numbers` and in the reference.

**4. Book 0 records live in two places and must be kept identical.** `check/records/B0/` is what
`build.py` reads; `done/` is what `README.md` and `claude.md` point a new chat at as the standard.
The four pre-existing records are byte-identical in both. The eight new ones were copied so they
stay that way. Nothing automates this.

**5. A Book 0 `sequence` is a section position in `check/book0/OUTLINE.md`, not a free integer.**
The build warns otherwise. A1 to A8 are positions 1 to 8, which is why the concept ids are
`B0-R0-C01` to `C08` and why F1, F3, F4 and F5 are `C39`, `C41`, `C42` and `C43`.

**6. `check/references/library.bib` had to be added to.** `PARALLEL.md` puts `check/**` off limits
mid-flight, but a citekey not in `library.bib` is a blocking failure, so a record cannot exist
without an entry. The added entry is a placeholder of exactly the kind already in the file, marked
PENDING. Read that rule as covering the machinery — `build.py`, the schema, the hard-word list,
the outline — and not the reference library or the records.

**7. Part A needs almost nothing from `sources/`, and what it uses is incidental.** Every one of
the eight is derivable. The statutes are there to give the arithmetic real Indian numbers and real
search strings, not to establish anything. That is worth knowing before anyone proposes waiting on
a source pack for Parts B to E: they will be the same.

**8. The audit earns its place, and reading the draft would not have found it.** Fourteen defects
in `DEFECTS.md`; five of them read as perfectly good prose and were wrong:
a search string that lands on the contents list rather than the section (1 and 9), a statutory
standard reported as what a child receives (3), "a ten-thousandth of a gram" where the arithmetic
gives a ten-millionth (5), "out by a factor of forty" where the true factor is six (6), and a
conditional statutory entitlement quoted as a flat one (7). Every one was found by opening the file
or redoing the sum.

**9. Two sections are long and are the obvious first candidates for 5a.** Reader-facing words,
excluding exercises: A4 is 1,401 and A8 is 1,459, against the pilot's roughly 1,000 a section. A7
is 1,504 but is carrying a genuinely new idea. The shortest is A2 at 1,168.

**10. Cowork cannot push.** Read-only GitHub connector; settled, see
`claude/storage-and-push-loop.md` in the project. Do not re-diagnose it. The files are handed over
for a local commit.

---

## What Part A is not, and where each thing went

Stated so nobody looks for it here: units and `kg/m²` are Part B; `kcal` and `kJ` are B4; graph
axes, slope and intercept are C5 (A7 teaches what a log axis *means*, not how to read a graph);
probability is D1; average and spread are D5; reading a table is F1 and is already written.

Two regression chains were followed to the floor and then cut under §5 step 5 as unattached:
**long division as a written procedure** (the reader floor grants a calculator) and **prime
factorisation** (nothing above it uses it). Recorded in `INVENTORY.md` so they are not re-derived.

---

## Suggested next steps, in order

1. **Human read, Task 6.** `python check/build.py --subject B0` and read Part A cold, end to end.
   The three questions in `PIPELINE.md` Task 6, and the third one hardest: does any claim make you
   want to check it yourself.
2. **Compression pass on A4 and A8 first**, as three separate sessions each, per §12. A8 has no
   `bridge_ref` dependents, so its own exercises are a sufficient test set; the same is true of all
   eight, since Book 0 carries no `bridge_ref`. The practice sets are out of scope for the cut and
   are the test material for 5b, which is a better use of them than they had before.
3. **Retrofit the rule to Parts B, C and D as they are written.** Nothing needs retrofitting now:
   the only other written records are Part F, which is not quantitative. The first Part B record
   will block until its ten are written, which is the rule working.
4. **Then Part B, or Part F's remaining section F2.** Part A is now the whole of the arithmetic
   that Parts B to E stand on.
5. **Whenever a browser is to hand:** one school mathematics text, eight locators; and current
   copies of the Food Safety and Standards Act, 2006 and the National Food Security Act, 2013.

---

## Files written and changed

**New**

```
check/records/B0/B0-R0-C01.yml   done/B0-R0-C01.yml
check/records/B0/B0-R0-C02.yml   done/B0-R0-C02.yml
check/records/B0/B0-R0-C03.yml   done/B0-R0-C03.yml
check/records/B0/B0-R0-C04.yml   done/B0-R0-C04.yml
check/records/B0/B0-R0-C05.yml   done/B0-R0-C05.yml
check/records/B0/B0-R0-C06.yml   done/B0-R0-C06.yml
check/records/B0/B0-R0-C07.yml   done/B0-R0-C07.yml
check/records/B0/B0-R0-C08.yml   done/B0-R0-C08.yml
books/B0/INVENTORY.md
books/B0/READY.md
books/B0/DEFECTS.md
books/B0/HANDOVER.md
```

**Changed**

```
claude.md                          new section 7a; section 8 blocking checks; section 12;
                                   the division-of-work table and the step 3 note
PIPELINE.md                        Tasks 1, 2, 3, 5a and 5b
check/build.py                     practice checks, rendering, readability sweep, report table
check/schema/concept.schema.json   practice[] and quantitative
check/schema/example.concept.yml   the practice template
check/references/library.bib       one PENDING entry, pending_arithmetic_text
prose/GLOSSARY.md                  eleven rows appended, plus the between-rounds note
sources/SOURCES.md                 "Vintage of each copy" section appended, and the Consumer
                                   Protection Act row filled in
```

`PARALLEL.md`, `map/**` and the frozen map were not touched. The first five rows above are the
between-rounds contract change described at the top of this file; everything else is ordinary
Part A work.
`check/_build/` is generated and is gitignored.

---

## The practice-set rule: what changed, and where

Added to the contract in this session. A concept that teaches a technique the reader has to be
able to **carry out** now carries exactly ten practice problems. The reasoning, in one line: a
section can be read, agreed with, and found impossible to use twenty minutes later, and ten
problems is the cheapest thing in the method that closes that gap.

### The six places it landed

| File | What went in |
| --- | --- |
| `claude.md` §7a | The rule, the difficulty ladder, and how to write them. New section |
| `claude.md` §8 blocking checks | Two new blocking conditions, and practice citekeys added to the library check |
| `claude.md` §12 and division-of-work table | The compression pass may not touch the practice set; step 2 writes it; step 3 recomputes it |
| `check/schema/concept.schema.json` | `practice[]` with `level`, `prompt`, `answer`, `refs`; and a `quantitative` boolean |
| `check/schema/example.concept.yml` | The template, with one problem from each band |
| `check/build.py` | The blocking checks, the rendering, the readability sweep over practice prose, and a practice-set table in the check report |
| `PIPELINE.md` | Task 1 names the column, Task 2 writes the ten, Task 3 recomputes them, 5a may not cut them, 5b works them |

### How "which concepts" is decided, and why it is not left to the author

`quantitative: true` in the record says so outright. Left out, the build derives it: **a Book 0
record in Part A, B, C or D is quantitative; one in E or F is not.** That set is read off
`check/book0/OUTLINE.md` and lives in `MATHEMATICAL_PARTS` in `build.py`.

The derivation is the point. An author who forgets the field still gets blocked, so the rule
cannot be dodged by omission — only by writing `quantitative: false` on purpose, which is visible
in a diff. Subject records default to false and opt in explicitly.

This is also why **the four finished Part F records were not touched**. F1, F3, F4 and F5 are
Part F, so they are not quantitative, so they owe nothing. `B0-R0-C39` teaches you to read a
table; it does not teach a technique you perform.

### How "progressive" is made checkable

Each problem carries a `level` from 1 to 10 and the build blocks unless the ten levels are exactly
1 to 10 with each used once. Without that, "progressive difficulty" is a matter of taste and the
failure mode is ten level-2 problems with different numbers. The bands:

| Level | Band | What the problem is for |
| --- | --- | --- |
| 1–3 | mechanical | The move on bare numbers. The reader's hands learning it |
| 4–6 | applied | A real quantity, unit and label kept attached |
| 7–8 | diagnostic | A worked answer that is **wrong**; find the step that broke. This is the band that transfers to reviewing other people's work |
| 9–10 | transfer | A claim in words; choose the technique, then say what the answer does **not** establish |

The build cannot check the *bands*, only the levels, so a set that numbers ten mechanical problems
1 to 10 will pass. That is a real hole and the audit is what closes it — `PIPELINE.md` Task 3 now
says to check that each set actually climbs.

### Where the eighty problems came from

This was the question worth answering before writing any of them. Three sources and no fourth:

1. **Figures already opened in `sources/`.** The National Food Security Act, 2013 — Schedule II
   meal and ration standards, s.3(1) entitlements, and s.3(2)'s "up to 75 per cent of the rural
   population and up to 50 per cent of the urban population", which is new to the corpus and is
   the best percentage material in the pack. The Food Safety and Standards Act, 2006 penalty
   ceilings. And the Consumer Protection Act, 2019, which was sitting unused: s.21(2) ten lakh and
   fifty lakh, s.34 one crore, s.47 ten crore. Those last three are exactly 10^6, 10^7 and 10^8,
   which makes them the cleanest logarithm material in the repository.
2. **Bare numbers**, for levels 1 to 3, which need no source at all. Arithmetic is derivable and
   the reader checks it with the calculator the floor grants them.
3. **Stated problem conditions** — "a block has 250 households" — which are conditions of a made-up
   question and make no claim about the world.

**What was not used, deliberately.** No invented prevalence, no invented survey figure, no
plausible-sounding Indian statistic. Where a problem needs a number nobody has, it is marked in
the working as a guess, which is A8's whole method, or named in the answer as made up to show the
move. Defect 15 in `DEFECTS.md` is what happens when this slips: a protein figure was taken off
the bottom of a Schedule II range and divided as though it were exact.

### What a future chat should know before writing a practice set

- **Fence every worked block, and put no blank line inside a fence.** `build.py` skips a block
  starting with a backtick fence, but it splits blocks on blank lines, so a fence containing one
  becomes two blocks and only the first is skipped. The second is then measured as prose and
  reported as a 30-word sentence.
- **A blockquote line counts its `>` as a word**, and the sentence splitter will not break after a
  full stop that is followed by `>`. So a two-sentence quote is measured as one long sentence. Keep
  a quoted claim to a single sentence under about 22 words.
- **Sentences beginning with a digit or `10^3` do not split**, so three sentences get measured as
  one. Write "Ten to the power three is…" at the start of a sentence.
- **Level 9 and 10 answers run long.** They carry a computation and then a boundary, and the
  boundary is the half that matters. Expect 120 to 190 words and do not compress them away: §12
  now forbids the compression pass from touching the practice set at all.
- **The numbers register does not see practice figures.** It is built from
  `illustration.numbers` only. A practice problem names its citekey in `refs` and the build checks
  it against `library.bib`, but no value or unit reaches the register, so it under-reports Part A
  by eighteen figures. Closing this is a between-rounds job; the cheapest fix is to have
  `reports()` walk `practice[].refs`. Recorded at the end of `DEFECTS.md`.

### What this rule costs

Part A reader-facing prose roughly doubled. Before the practice sets it was about 1,170 to 1,500
words a section; the eighty problems add roughly 800 to 1,100 words a section on top, most of it
in the appendix rather than in the reading path. The sections themselves grew by the ten prompts
only, which is 100 to 150 words.

That asymmetry is worth keeping in view when the compression pass runs. The thing a reader has to
read did not grow much. The thing they have to do grew a lot, and none of it is compressible.
