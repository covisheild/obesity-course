# Book 0 · Part A concept inventory

Part A, sections A1 to A8, of `check/book0/OUTLINE.md`. Produced by the method in the
specification §5, adapted to Book 0: Book 0 has no rung outcomes of its own, so the terminal
requirements are the outline's own section descriptions plus everything the sections and subject
records above Part A presuppose about arithmetic.

Against frozen map `fc19c8bc-a216-4131-99fb-ebe3f19cec4a`.

---

## What the terminal requirements were, before regression

Three sources, and all three are files in this repository rather than judgement.

**1. The outline's own notes on Part A.** `check/book0/OUTLINE.md` carries a note against four of
the eight sections, and each note is a requirement: A1 "starts below fractions, deliberately";
A3 "where false precision begins"; A4 "the single commonest error in health reporting"; A5
"prepares every *per 1,000* and *per person-year* in the course"; A7 "needed for odds, pH, log
scales on every dose-response figure"; A8 "the habit that makes S01's competency test possible".

**2. What later Book 0 parts need from Part A.** Read from the outline in document order:

| Later section | Needs from Part A |
| --- | --- |
| B2 converting units as multiplication by one | A2 fractions, A5 ratio |
| B4 energy units: joule, kilojoule, calorie, kilocalorie | A5 ratio, A6 powers |
| B5 concentration units, mg/dL and mmol/L | A5 rate, A6 scientific notation |
| B6 body-size units, kg, m, cm, kg/m² | A6 powers and roots |
| C5 graphs: axes, scale, slope, intercept | A5 rate, A7 log scales |
| D1 what a probability is | A2 fractions, A4 percentages |
| D3 conditional probability through the two-way table | A2, A4, A5 |
| D5 average and spread | A3 rounding, A5 proportion |
| F1 reading a table (**written**, `B0-R0-C39`) | A4 percentage and denominator, A3 precision |

**3. What the two pilot subjects need.** From `plan/INVENTORY-PILOT.md`, Book 0 column:
S01 C04 needs **A5**; S01 C12 needs **A5**; S01 C13 needs **A5, A8**; S01 C16 needs **A4, A8**.
S48 needs nothing from Part A at all, which is the asymmetry the outline predicted.

---

## The regression, and where each chain stops

Each requirement above was regressed by asking, of every sentence, what a reader must already
hold for it to mean anything. The chains and their terminal points:

| Chain | Stops at |
| --- | --- |
| *per 1,000 person-years* → rate → division → what a quotient is → what a digit is worth | **the floor.** A1 is the last step before "can read, can use a calculator" |
| *kg/m²* → a power → repeated multiplication → multiplication | **A1**, and then the floor |
| *24.1 per cent of 42,100 women* → percentage → fraction with a denominator of one hundred → fraction | **A2**, and then A1 |
| *the figure is 24.1, not 24.13* → significant figures → decimal place → place value | **A1** |
| *the odds ratio is plotted on a log axis* → logarithm → power of ten | **A6** |
| *that number is impossible* → order of magnitude → power of ten, and rounding to one figure | **A6 and A3** |

No chain ended at "assume familiarity with", at a class-10 topic, or at a medical premise. Two
chains were followed and then cut for being unattached under §5 step 5: **long division as a
written procedure** (nothing in the corpus needs it — the floor grants a calculator) and
**prime factorisation** (nothing above it uses it). Both are recorded here so the next chat does
not re-derive and re-cut them.

---

## The inventory

Eight records, one per outline section, because the build ties a Book 0 record's `sequence` to a
section position in `check/book0/OUTLINE.md`. Type is `d` derivable, `e` empirical, `i`
institutional.

| Concept id | Section | Name | Type | What it must cover | Source it needs |
| --- | --- | --- | --- | --- | --- |
| `B0-R0-C01` | A1 | Counting, place value, and what a calculator is actually doing | d | A digit's value comes from where it sits; the Indian lakh-crore grouping against the international thousand-million one; what a calculator does and does not check | **None external.** Derivable. Illustration anchored on the penalty figures in `sources/fss_act_2006.txt` |
| `B0-R0-C02` | A2 | Fractions | d | A fraction as a division not yet done; numerator and denominator; equivalent fractions; that two fractions of different wholes cannot be compared or added | **None external.** Derivable. Illustration anchored on Schedule II of `sources/nfsa_2013.txt` |
| `B0-R0-C03` | A3 | Decimals, rounding, and significant figures | d | A decimal as a fraction of ten, a hundred, a thousand; rounding; significant figures; that a calculator prints more digits than the inputs earned | **None external.** Derivable. Illustration anchored on s.3(1) of `sources/nfsa_2013.txt` |
| `B0-R0-C04` | A4 | Percentages, and the percentage of a percentage | d | Per cent as a fraction of one hundred; percentage change; percentage point against per cent; relative against absolute; a percentage of a percentage | **None external.** Derivable. Illustration anchored on Schedule II of `sources/nfsa_2013.txt` |
| `B0-R0-C05` | A5 | Ratios, rates and proportions | d | Ratio, proportion and rate as three different things; "per" as division; why the denominator and the time have to be said aloud; per 1,000 and per 100,000 | **None external.** Derivable. Illustration anchored on s.3(1) of `sources/nfsa_2013.txt` |
| `B0-R0-C06` | A6 | Powers, roots and scientific notation | d | A power as repeated multiplication; the exponent; powers of ten; negative powers; square root as the inverse; scientific notation | **None external.** Derivable. Illustration anchored on the lakh and crore grouping established in A1 |
| `B0-R0-C07` | A7 | Logarithms — what they are for before how they work | d | What a logarithm is for before what it is; log base ten as the power of ten; reading a log axis; equal distance means equal multiple | **None external.** Derivable. Illustration anchored on the penalty ladder in `sources/fss_act_2006.txt` |
| `B0-R0-C08` | A8 | Orders of magnitude and the back-of-envelope sanity check | d | Round every input to one figure; count the powers of ten; the answer is a range; mark every assumed input as a guess; what the check catches and what it misses | **None external.** Derivable. Illustration anchored on Schedule II of `sources/nfsa_2013.txt`; the population and school-day inputs are the reader's own labelled guesses |

**All eight are derivable, and this is the point worth stating plainly rather than papering
over.** A derivable concept is built from the reader floor by argument, and the reader can check
every line of Part A with the calculator the floor grants them. None of the eight needs an
external source to establish its content, and none has been given one.

What every derivable concept does need, under the specification §4, is a `textbook` anchor: the
canonical text a specialist would point at. **No textbook is reachable from this authoring
environment.** The same constraint produced `pending_data_presentation_text`,
`pending_scholarly_method_text` and `pending_logic_text` in the three drafted records in `done/`,
and it produces one more here. Every Part A record therefore carries a single reference with
`opened: false`, a locator naming the chapter that will have to be found, and a note saying so.
This is the citation backlog, not a citation.

**No figure in Part A is invented and then dressed as a fact.** Every quoted figure is one of
two kinds, and the record says which:

- **Quoted from an opened file in `sources/`**, listed in `illustration.numbers` with its unit and
  citekey so the numbers register can audit it. These are the mid-day meal and take-home ration
  standards in Schedule II of the National Food Security Act, 2013, the foodgrain entitlements in
  its section 3(1), and the penalty ceilings in sections 50 to 53 of the Food Safety and Standards
  Act, 2006.
- **A teaching example, framed in the text as an example**, and deliberately kept out of
  `illustration.numbers` so it can never be mistaken for a measurement. `B0-R0-C39` set this
  precedent with its two-state table, whose `numbers` list is empty.

---

## Ordering

Topologically sorted on the chains above, and it matches the outline's own order, so no
resequencing was needed.

```
A1 ──┬── A2 ── A3 ─────┬── A4 ── A5
     │                 │
     └── A6 ── A7      └── A8
              (A8 also needs A6 and A3)
```

`concept_deps` is set accordingly and the build checks it for forward references. `sequence`
runs 1 to 8, which are the section positions A1 to A8 hold in the outline.

---

## What Part A does not contain, and where it went instead

Stated so the next chat does not look for it here.

| Not here | Where it belongs |
| --- | --- |
| kg, m, kg/m², and what a unit is | Part B. A6 teaches the power; B6 teaches the unit |
| kcal and kJ | B4 |
| Graph axes, slope, intercept | C5. A7 teaches what a log axis means, not how to read a graph |
| Probability | D1. A2 and A4 are its arithmetic, not its content |
| Average and spread | D5 |
| Reading a table | F1, written, `B0-R0-C39` |
