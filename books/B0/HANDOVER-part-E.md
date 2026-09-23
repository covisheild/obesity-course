# Handover · Book 0 Part E (E1–E8)

Chat of 2026-09-23, branch `book0/part-E`, based on `997228b`. Ran Tasks 1 to 4 of `PIPELINE.md`
for Book 0 Part E, records `B0-R0-C31` to `C38`. Task 5, the compression pass, is recorded at the
end of this file if it ran; Task 6, the human read, is not started.

Build on handing over: **blocking 0, warnings 28** — the corpus baseline of 23 plus five on Part E,
every one of them an over-long sentence inside a verbatim block quotation that cannot be shortened
without misquoting the source.

---

## What was written

| Section | Record | Name | Type | Quantitative | Drill set |
| --- | --- | --- | --- | --- | ---: |
| E1 | `B0-R0-C31` | Atoms, molecules and bonds | empirical | no | — |
| E2 | `B0-R0-C32` | Chemical energy, combustion, and the bomb calorimeter | empirical | **yes** | 12 |
| E3 | `B0-R0-C33` | Conservation of energy, and a system with a boundary | **derivable** | **yes** | 8 |
| E4 | `B0-R0-C34` | Heat and temperature; how heat moves | empirical | **yes** | 8 |
| E5 | `B0-R0-C35` | The cell, membranes, proteins and receptors | empirical | no | — |
| E6 | `B0-R0-C36` | Metabolism as chemistry happening in a body | empirical | no | — |
| E7 | `B0-R0-C37` | Genes, DNA and inheritance in outline | empirical | no | — |
| E8 | `B0-R0-C38` | Organs and systems that matter for metabolism | empirical | no | — |

Book 0 is now **35 of 43 sections**. Sixty-six glossary rows were appended — more than Parts A to D
together, because Part E is where the course acquires its biological vocabulary.

---

## The contract change, and what it moved

**`empirical` now accepts a `textbook` anchor.** Made on Harsh's explicit instruction in the
chat, which is the exception `PARALLEL.md` allows; the reasoning is in `claude.md` §4 and the cost
is recorded in `MEASUREMENTS.md`.

Part E is the first Part that is neither mathematics nor law. A plasma membrane is not rebuildable
from the reader floor, so the concept cannot be `derivable` — §3 means that word literally. It is
not a finding with an effect size either, so requiring `primary` would have meant citing a research
paper for the existence of the cell, which is worse scholarship than citing a canonical text.

**What it cost.** A check that used to separate settled science from contested findings can no
longer do it, so the separation moved from the build to the audit. **The failure this permits is a
textbook anchor under a number**, and the audit of E5–E8 was scoped to hunt exactly that. It found
none in the final records: every figure in Part E comes from a statutory instrument, a conversion
factor, or a worked example in a chemistry text, and the measured quantities E6 and E8 wanted are
in the citation backlog below rather than in the prose.

If a later Part does ship a measured quantity resting on a textbook, the widening was too wide and
the next revision should carry a fourth concept type rather than a looser third.

---

## What the audit found, and it earned its place again

Three auditors, none auditing what it drafted, produced **57 defects across eight records**. All
were applied. The build saw none of them: both records in every batch passed `--check` with zero
blocking failures before the audit ran.

**The four worth carrying forward.**

1. **A true finding generalised into a false one.** The Part E source gate recorded that FAO 77 has
   no concept of *digestible energy* — true, the word is not in the report. That became "the
   report's cascade is two steps", which is false: §3.3 carries **net metabolizable energy** below
   ME. E2 then built a must-know point arming the reader to object in public to a three-step
   citation of FAO, which would have misfired against somebody citing the report correctly. A
   reader armed to object is harder to correct than a reader merely misinformed. Corrected in
   `READY-part-E.md`, `INVENTORY-part-E.md` and E2.

2. **Outline labels and record ids overlap and nothing distinguishes them.** The inventory wrote
   "C9" for the ninth section of Part C, which is record `B0-R0-C23`; `B0-R0-C09` is Part B's "What
   a unit is". Two drafters read the label as the id, and E3 shipped a paragraph attributing to C9 a
   refusal that lives in `B0-R0-C23` — E6 inherited the same error. **The rule for later Parts: an
   inventory names a record by its id the first time it names it at all.** The namespaces overlap
   for thirty-eight of the forty-three sections.

3. **Two unsourced definitions in the field the reader reads.** E7 defined a gene and E8 defined a
   hormone, both from model knowledge, in `simplified_explanation`, while each record's own
   `verified.note` said the pack could not support it — and E8's note went further and falsely
   asserted it had not done so. That is §7b's named defect, and the false note is worse than the
   defect, because it is an audit trail that would have passed the next auditor. Both records had
   been drafted by sessions cut off by a rate limit before they could check their own work.

4. **E3 skipped steps in a derivation.** E3 is the only `derivable` concept in Part E, and §3 says a
   derivation that skips is worse than no derivation. Two skips closed in full.

---

## Three things about the build that the next Part will hit

None was changed. `check/build.py` is reserved, and only the §4 widening was instructed.

**1. The arithmetic checker's tolerance is `min(decimals shown)` across both sides, and it fails in
both directions.** With integers on the left it collapses to about one part in a billion, so
`4186 divided by 452 = 9.26` blocks and §7a's claim that a figure "does not have to be written to
full precision" is wrong in general. **With a decimal on the left it becomes absolute rather than
relative**, and E4 `practice[6]`'s `8316 divided by 4474.8 = 1.858` carried a tolerance of 0.1 — it
would have passed with `= 1.95`. So the check is exact-by-accident in one case and blind-by-accident
in the other. Both were worked around by writing bracketing and multiply-back checks, which read
better than the divisions did. The suggested fix, from the E3/E4 audit: compute the tolerance from
the right-hand side's decimals as `max(10 ** -places, abs(v) * 1e-9)`.

**2. The acronym check recognises only a parenthetical expansion.** It looks for `(ATP)` and does
not recognise "adenosine triphosphate, written ATP", which is the idiom §1 establishes for symbols
and which three Part E records used. A record following the style sheet therefore trips the check.
Worked around by giving ATP and ADP a parenthetical form at first use in document order.

**3. A blockquote whose lines break at a sentence boundary is measured as one long sentence.**
`_sentences()` splits on a full stop followed by a capital, and a continuation line beginning `> `
blocks the split, so two sentences and the `>` markers count as one. E5's exercise 2 prompt was
reported as a 27-word sentence and is two, of 15 and 12. Re-wrapping the YAML so the line break
falls inside a sentence fixes it and changes nothing the reader sees. Any blockquote in the corpus
with the same shape carries the same false positive.

---

## The ordering problem, and what the constraint bought

E2 teaches the bomb calorimeter, which measures energy by a temperature rise. Specific heat
capacity — the thing that turns a rise into an energy — is E4, two sections later. §10 rule 1
forbids a forward reference and the section numbers cannot move, because a record's id is its
outline position and inserting or reordering renumbers everything after it.

So E2 teaches the instrument as **calibrated**: burn something of known energy, measure the rise,
and the ratio is the calorimeter's energy equivalent in joules per degree. That is how bomb
calorimetry actually works, and it needs no specific heat at all. E4 then opens on the misconception
E2 can leave behind — that a bigger rise means more heat — and breaks it with a kilogram of steel
and a kilogram of water taking the same energy to different temperatures.

The constraint produced a better pair of sections than an unconstrained ordering would have, and it
is worth saying so, because the instinct on meeting it was to ask whether the outline could move.

---

## What the ground floor refuses, and Part E holds the line

Book 0 C9 (record `B0-R0-C23`) deliberately stops short of saying how much energy a kilogram of
change in a body holds, because that depends on what the change is made of. **No
kilocalories-per-kilogram-of-body figure appears anywhere in Part E.** E3 and E6 each carry the
refusal as a `trap` must-know point, and E2's transfer problems say explicitly that the number is
missing on purpose and must not be supplied from memory.

Related, and recorded as a clause-level refusal in `READY-part-E.md` and inline in the source file:
**A&P §24.7 may not be cited for anything quantitative.** It states that 3,500 extra calories adds
one pound and then compounds that to one pound per 18 days and 20 pounds a year. The second step is
refused whatever evidence appears for the first, which is why the refusal is written against the
clause and not against the file.

---

## The citation backlog, and it is all measured quantities

Every one of these was wanted, none was taken from a textbook that states it flat, and each needs
primary evidence or an instrument:

| Figure | Wanted for | What would settle it |
| --- | --- | --- |
| Each organ's share of resting energy expenditure | E8, and it is the figure that section most wanted | Primary studies combining organ mass by MRI with organ-specific metabolic rates, or a systematic review |
| Fraction of catabolic energy reaching ATP, and the fraction leaving as heat | E6 | Primary review of substrate oxidation efficiency and P/O ratios |
| Size of the liver and muscle glycogen stores, and how long each lasts | E6 | 13C magnetic resonance spectroscopy studies |
| A whole-calorimeter energy equivalent in J/°C | E2 — every calorimeter constant in the section is invented and flagged as such in all ten places it appears | A published calibration figure: ASTM D240 or ISO 9831 worked example, or an instrument manual |
| A bomb-calorimetry result on an Indian food | E2 — every real figure it works on is a statutory standard or a conversion factor | ICMR-NIN Indian Food Composition Tables 2017 |
| Proportion of a typical Indian meal's gross energy actually absorbed | E6 | Controlled feeding studies with faecal and urinary energy collection |
| Fibre content of common Indian foods | E6, to make the onion example quantitative | ICMR-NIN Indian Food Composition Tables 2017 |

Deliberately **not** on this list: the alpha and beta cells' share of an islet, which no rung in the
map needs; and the normal range of blood glucose, which is a diagnostic cut-point and therefore
`institutional` rather than empirical, and does not belong in Book 0 at all.

---

## One decision left open, and it is above the record level

**`fao_food_energy_2003` cannot appear in `definition.references` for E2.** Its kind is
`consensus_statement`; `KIND_FOR_TYPE` admits only textbook, primary and systematic_review on an
`empirical` concept. And `Cites.mark` builds the reader's numbered reference list from
`definition.references` alone. So the assembled Part E reference list contains **no entry for FAO
77, the National Food Security Act, the FSSAI regulations or NIST** — every one of the four sources
carrying the half of E2 that matters in a meeting.

`claude.md` §4 already points at the answer: it says in as many words that Atwater's 4/9/4 is
`institutional`, because a body adopted those rounded values and can revise them. E2 was drafted as
one `empirical` concept carrying institutional content, and that is what produced the collision.

Two routes, and one to refuse:

- **Split** E2's Atwater and cascade material into its own `institutional` concept, taking
  `stability: short` and the event trigger with it. This needs a new outline section, which
  renumbers everything after it — so it is a decision for Harsh, not a chat.
- **Re-type** E2 as `institutional` and re-anchor the bomb calorimeter from the textbook side.
- **Refuse:** widening the empirical kinds to admit `consensus_statement`. That would let any
  professional-body statement stand behind any empirical claim in the corpus, which is the
  distinction §4 exists to hold.

Doing nothing means the reader never gets a citation for half the section. The `AUDIT NOTE` on
E2's last definition reference states the question as open rather than settled, so the next person
meets it rather than inheriting a note that says the gap is fine.

---

## How the sources were obtained, and the finding that came with it

`PIPELINE.md`'s source-gate section records NCBI Bookshelf and PubChem as CAPTCHA-gated and
unreachable from a session. **That is out of date** — OpenStax, NCBI Bookshelf and FAO all return
their pages. Direct `curl` is still refused at the proxy for every host, which is probably what the
earlier note measured. `PIPELINE.md` was not edited; `PARALLEL.md` reserves it.

**The finding worth keeping is a different one, and it nearly got past.** Four of the five source
files were first built with WebFetch, whose extractor is a small model with a quote-length cap.
Checked afterwards against raw page text, **a quarter of their supposedly verbatim passages had
been quietly tidied**: figure markers dropped, whole sentences deleted mid-paragraph with no
ellipsis, and two passages that do not exist on the page at all — a specific heat of water "for the
liquid" welded out of two different sentences, and a table row with units imported from the column
header. Both read as quotations, and **both would have passed the build's quote check, because that
check searches the source file and the file was what had been smoothed.**

They were rebuilt from raw page text with `mcp__TinyFish__fetch_content`, which has no model in the
loop. The one file built that way first time scored 106 of 106 word for word; after the rebuild all
five score **281 of 281**. The rule is now in `sources/SOURCES.md`: a source file is transcribed
with a tool that has no model between the page and the file, and WebFetch is for reading a page,
not for quoting one.

---

## Figures wanted, none drawn

Named by the drafters and left for a decision, in the order they would earn their place:

1. **E4, same energy, different rise.** Two thermometers over a 1 kg steel tawa and 1 kg of water,
   each given 4,186 J, reading rises of 9.26 °C and 1.00 °C. The one place in Part E where a picture
   beats the arithmetic, because the point is a comparison the eye makes instantly.
2. **E3, the four boundaries.** One kitchen scene with four dotted lines overlaid, the crossing
   arrows carrying the numbers already in the illustration, and a table giving the change inside
   each line: +42,000, +53,000, −7,000 and 0 joules. All four on one drawing at once is the content.
3. **E8, the loop with the brain outside it.** Blood sugar high, beta cell, insulin, stores fill;
   blood sugar low, alpha cell, glucagon, stores empty — and the brain drawn outside the circle,
   taking glucose by an arrow that does not pass through insulin. Without that arrow the figure is
   decoration.
4. **E2, the cascade as one downward bar**, gross energy at the top with faecal, gaseous and urinary
   slices taken off it. **No sizes on the slices** — FAO 77 gives none, and drawing them to any
   scale would invent a statistic. The caption has to say the widths are not to scale.
5. **E1, break then make**; **E2, the calorimeter cut away**; **E2, two thermometer faces**;
   **E6, the coin loop**; **E6, the plate and the gut wall**; **E8, two roads out of the gut**.

---

## Files written and changed

**New**

```
check/records/B0/B0-R0-C31.yml … C38.yml     the eight records
books/B0/INVENTORY-part-E.md
books/B0/READY-part-E.md
books/B0/DEFECTS-part-E-e1e2.md
books/B0/DEFECTS-part-E-e3e4.md
books/B0/DEFECTS-part-E-e5e8.md
books/B0/HANDOVER-part-E.md
sources/openstax_chemistry_2e.txt            6,268 words
sources/openstax_biology_2e.txt              5,106 words
sources/openstax_anatphys_2e.txt             6,745 words
sources/openstax_college_physics_2e.txt      3,896 words
sources/fao_food_energy.txt                  1,610 words
```

**Changed**

```
check/build.py           KIND_FOR_TYPE only - empirical now accepts textbook
claude.md                §4 settled science, and the note in §7b that it does not soften the block
MEASUREMENTS.md          the taxonomy episode, and what a session can retrieve, remeasured
sources/INDEX.yml        five entries
sources/SOURCES.md       five rows, five vintage rows, and how the open-textbook files were obtained
sources/openstax_anatphys_2e.txt   a [NOTE] DO NOT CITE block under §24.7
check/references/library.bib       five entries
prose/GLOSSARY.md        sixty-six rows appended
```

`PIPELINE.md`, `PARALLEL.md`, `map/**`, `check/schema/**` and every record outside C31–C38 were not
touched.
