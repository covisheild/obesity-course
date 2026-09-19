# Handover · Book 0 Part A (A1–A8)

Chat of 2026-09-20. Ran Tasks 1 to 4 of `PIPELINE.md` for Book 0 Part A and stopped there. The
compression pass was **not** run, by design: `claude.md` §12 and `PIPELINE.md` Task 5 require 5a,
5b and 5c to be three separate sessions, and running them here would have destroyed the method
while appearing to run it.

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

Book 0 is now **12 of 43 sections**. Build: `blocking 0, warnings 11`, and all eleven warnings are
`reference not yet opened` — eight new ones plus the three that were already there.

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

Fifteen quoted figures, all from two files, all in `check/_build/numbers_register.csv`.

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

**The trigger that matters most, and it is not in the table.** Both source copies are of unstated
and different vintage, and this was found by the audit rather than assumed:

- `fss_act_2006.txt` cites exactly one amending Act anywhere in it — **Act 13 of 2008, w.e.f.
  7 February 2008** — and nothing later.
- `nfsa_2013.txt` cites **no amendment at all**, so it reads as the Act as enacted in 2013.

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
   eight, since Book 0 carries no `bridge_ref`.
3. **Then Part B, or Part F's remaining section F2.** Part A is now the whole of the arithmetic
   that Parts B to E stand on.
4. **Whenever a browser is to hand:** one school mathematics text, eight locators; and current
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
check/references/library.bib   one PENDING entry, pending_arithmetic_text
prose/GLOSSARY.md              eleven rows appended, plus the between-rounds note
sources/SOURCES.md             "Vintage of each copy" section appended
```

Nothing in `claude.md`, `PIPELINE.md`, `PARALLEL.md`, `map/**` or `check/build.py` was touched.
`check/_build/` is generated and is gitignored.
