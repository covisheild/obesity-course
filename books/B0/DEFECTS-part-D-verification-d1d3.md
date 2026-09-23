# Verification of the fix pass · Book 0 Part D, D1–D3 (B0-R0-C24, C25, C26)

This checks the "## Resolution (fix pass)" section of `DEFECTS-part-D-d1d3.md`, which marks all 63
items closed. The records were read as they now stand, against `DECISIONS-part-D-fix.md` (M1–M15)
and against `sources/`. Verified 2026-09-23. No records were edited.

**The fixer's "all closed" does not hold: 53 are closed, 8 partly, and 2 not closed.** Twenty-seven
new or still-open defects are listed below: 13 error, 1 floor and 13 style (C24 3/0/3, C25 2/0/4,
C26 8/1/6). One of the errors is
arithmetic, and one is a claim that the arithmetic contradicts.

## What was run

- **Arithmetic.** Every `working` line in the three records was parsed and recomputed in Python:
  C24 28, C25 37, C26 86. All 151 are correct. Three lines in C26 could not be parsed. Two are
  correct. The third is the deliberately wrong step in the level 8 prompt (45/52 is 0.8654, which
  rounds to 87). The arithmetic errors below (V3-1, V3-2) are in prose sentences.
- **Quotes.** Every definition quote and every `illustration.numbers` quote was searched for in
  the file `sources/INDEX.yml` maps its citekey to, normalised as the build normalises. All 34 are
  present, including the new `openstax_contemporary_math` quote.
- **Derived values.** Every `derived:` value was recomputed: 52, 79, 89, 36, 6, 66 and 23 are all
  correct.
- **Build.** `build.py --check` gives 0 blocking, and no warnings name C24, C25 or C26.
- **The M1 table.** Every row of Kiran Table 3 was tested under ordinary rounding and under
  truncation.
  - Four rows whose group sizes nobody disputes divide back only under ordinary rounding. So the
    paper rounds in the ordinary way, and M1's inference, that the men's arm row fits 42 against 89
    and not 52 against 79, stands.
  - Two sentences built on it overstate it (V3-2, V3-3).
  - The neck row fits both splits (V3-5).

## The numbers rule: every `illustration.numbers` entry

| Record | Value | Verdict | Note |
| --- | --- | --- | --- |
| C24 | 75, 50, 5 | pass | each quote states the number in words |
| C25 | 75 | pass | |
| C26 | 131, 282 | pass | "We enrolled 282 medical students (131, 46.5% males" states both |
| C26 | 42, 10, 86, 74, 31.3, 20 | pass | each quote states its number |
| C26 | 52 (derived) | partial | the derivation is right, but the quote carries the 42 row only. The 10 it adds is counted from the Obese row, which is not quoted (V3-8) |
| C26 | 79 (derived) | **fail** | its quote is the Obese row, which is not the passage 79 was counted from (131 in Results, minus 52) (V3-8) |
| C26 | 89, 36, 6, 66, 23 (derived) | pass | the derivations are correct and the quotes are passages counted from |
| C26 | 59, 72, 61 %, 32 % | **missing** | computed from the paper in the illustration, and not registered as M13 requires (V3-8) |

## Status of every audit item

| ID | Status | Note |
| --- | --- | --- |
| D1-1 | partly | The new anchor is quoted once ("odds as a ratio of probabilities"). M3 also asks for the anchor's definition of odds, and that is not quoted (V1-3) |
| D1-2 | closed | |
| D1-3 | partly | The national-ceiling sentence is added. A contradicting clause stays in the same answer (V1-1) |
| D1-4 – D1-19 | closed | D1-5 leaves a dangling "they" (V1-4) |
| D2-1, D2-2 | closed | |
| D2-3 | partly | The signpost quote is replaced. The addition rule is still neither quoted nor noted, and the note contradicts reference 4 (V2-2) |
| D2-4 | closed | |
| D2-5 | **not closed** | "They live in a household of four" still derives a household bound from a ceiling on persons, which M2 forbids (V2-1) |
| D2-6, D2-7 | closed | |
| D2-8 | partly | The expected-count sentence is added, but the answer still calls 2.25 "impossible" (V2-3) |
| D2-9 – D2-15 | closed | |
| D3-1 | partly | The M1 rebuild is done and leads with the failure. Two sentences overstate it (V3-2, V3-3) |
| D3-2, D3-3 | closed | |
| D3-4 | **not closed** | Re-broken by the new numbers: "fell by about a third … prevalence fell by more than half" is wrong for 61→45 and 32→20 (V3-1) |
| D3-5 – D3-10 | closed | Youden's index is gone, with 0 hits. The body-fat problem now settles 185 by the paper's own sums |
| D3-11 | partly | It opens "86 per cent of what?" and then asserts which figure it is anyway (V3-6) |
| D3-12 | closed | The arm and neck figures are no longer mixed. The new neck answer draws a false inference (V3-5) |
| D3-13 | closed | Rows are the test result and columns the condition, throughout the prose, the tables and the retrieval items |
| D3-14 | closed | |
| D3-15 | partly | "Stand in for" is gone. A mismatched comparison replaces it (V3-4) |
| D3-16 | partly | The 20 per cent is tied back to the NFHS-4 planning figure, against M1 (V3-4) |
| D3-17 | closed | All three diagnostic problems now contain a genuine wrong worked answer and name the broken step |
| D3-18 | closed (structure) | Level 9 and level 10 now start from claims in words and compute something. Both have content defects (V3-5, V3-7) |
| D3-19 – D3-29 | closed | D3-19's fix creates a new duplication (V3-9) |

Totals: **53 closed, 8 partly, 2 not closed.**

---

## New or still-open defects

### C24 (D1)

**V1-1** · `practice[8]` (L9) answer ¶3 · **error (M2)** · still open from D1-3
Problem: "It does not tell you the actual number of people covered here, because that needs the
district's population count as well as the ceiling." This says the ceiling times the district's
population gives the local figure. The next paragraph says the ceiling "says nothing about this
place in particular". The two contradict each other.
Fix: cut the clause from "because" to the end: "It does not tell you how many people are actually
covered here."

**V1-2** · `exercises[0].answer` ¶3 · **error (new; contradicts must_know[1] and M3)**
Problem: "The two look interchangeable right up until the figures move away from the middle of
the scale." Odds and probability are close only near 0. At the middle they are already a factor
of two apart (0.5 against 1).
Fix: "The two are close only for rare events. At one half they are already a factor of two
apart."

**V1-3** · `definition.references` (odds) · **error (sourcing)** · still open from D1-1
Problem: M3 asks for a quote for the definition of odds and a second for "odds as a ratio of
probabilities". Only the second is quoted. The anchor's defining sentence is plain prose and is
present in the file.
Fix: add a reference quoting "is called the odds for (or odds in favor of) the event". Optionally
add "odds can be any (non-negative) number" under ¶4's "Probability and odds … are not the same
number". Both are in the file verbatim.

**V1-4** · `illustration.analogy_breaks_when` ¶2 · **style (new)**
Problem: "Near 0 they are almost the same number". "They" has no antecedent, because the paragraph
before is about the Act's ceilings.
Fix: "Odds and probability are almost the same number near 0".

**V1-5** · `definition.text` ¶1 · **style (new)**
Problem: "That share has a name: the relative frequency." This makes the probability equal to the
relative frequency. The anchor makes it the *long-term* relative frequency. `definition.text` is
the one field held to technical exactness.
Fix: "It is the long-run relative frequency: the fraction of all the tries in which it happened,
as the tries go on and on."

**V1-6** · `simplified_explanation` ¶6 · **style (carried over, missed in the audit)**
Problem: "because it comes up in almost every study you will read" is an unsourced superlative.
Fix: "because you will meet it in many of the studies you read".

### C25 (D2)

**V2-1** · `practice[12]` (L10) prompt and answer · **error (M2)** · D2-5 not closed
Problem: "Pick one rural person at random. They live in a household of four." That conditions on
the size of the household. The 0.75 caps coverage across *all* rural people. It does not cap the
share of people in four-person households, which could all be covered with the national ceiling
still met. So "At least 0.25, not about 0.68" and "bounded by the household ceiling itself" do not
follow. M2: "no bound on a household of four may be derived from a ceiling on persons".
Fix: keep the collapse to one household-level question and drop the bound. Replace the last
working block and "At least 0.25, not about 0.68" with: "So it is one chance, not four. The Act's
75 per cent is a ceiling on all rural people together. It gives no figure for households of four
in particular, so the report's 'high' has nothing under it."

**V2-2** · `definition.references[2].verified.note`; `references[3]` · **error (sourcing, minor)** · still open from D2-3
Problem: reference 4 is located to "the addition rule". Its quote states only that P(A AND B) = 0
for mutually exclusive events, not the addition in ¶3 ("P(A or B) equals P(A) plus P(B)"). The
note says the mutually-exclusive test is given "only as symbols … so … not quoted", but references
2 and 4 quote it. The addition rule is covered by neither a quote nor the note.
Fix: in the note, replace "the mutually-exclusive test" with "the addition rule", and add "the
addition rule is derived in the record". Relocate reference 4 to "(mutually exclusive means no
overlap)".

**V2-3** · `practice[10]` (L8) answer · **style** · still open from D2-8
Problem: the answer says "2.25 already cannot be right", "not because of the impossible one" and
"the impossible total is the signal". Then it says "The 2.25 is not meaningless … a real number".
The answer contradicts itself.
Fix: "2.25 already cannot be a probability"; "not because of the 2.25"; "a total above 1 is the
signal".

**V2-4** · `illustration.body` ¶1 · **style (M2)**
Problem: "Treat 0.75 as the probability, at most, that a given rural person is covered". M2 says
it holds only for a person picked at random from all of rural India. "A given" person reads as a
particular one, which C24's own boundary point forbids.
Fix: "a rural person picked at random".

**V2-5** · `illustration.numbers` · **style**
Problem: the illustration uses s.3(1)'s five kilograms, and C25 does not register it. C24
registers the same figure.
Fix: copy C24's `numbers[2]` entry.

**V2-6** · `exercises[1].answer` ¶3 · **style**
Problem: "P(both covered) is 0.75" drops the "at most" that C24's must_know[3] requires.
Fix: "is at most 0.75".

### C26 (D3)

**V3-1** · `illustration.analogy_breaks_when` ¶2 · **error (arithmetic)** · D3-4 not closed
Problem: "The positive predictive value fell by about a third, from 61 to 45 per cent, while the
prevalence fell by more than half."
Recomputed: 0.4526 ÷ 0.6102 = 0.742, a fall of about a quarter. The prevalence went from 42/131 =
32.1 per cent to 20 per cent, a fall of 38 per cent, not more than half.
Fix: "fell by about a quarter, from 61 to 45 per cent, while the prevalence fell from 32 to 20
per cent."

**V3-2** · `illustration.body` ("It is the only whole-person table that reproduces both 86 and 74 exactly"; "Both land exactly, with nothing left over"); `practice[5]` ("Both land exactly") · **error (claim contradicted by arithmetic)**
Problem: 39 different splits of the 131 men reproduce 86 and 74 as whole counts. For example, 43
against 88 gives 37/43 = 86.0 and 65/88 = 73.9. The true claim is narrower. Among the groups the
paper actually prints (52 and 42), only 42 against 89 works, and within it only 36 and 66 do.
"Exactly" and "nothing left over" are also wrong: 36/42 is 85.7, which *rounds* to 86.
M1's own wording ("the only whole-person table that fits them") carries the same slip.
Fix: "It is the only whole-person table, built on a group the paper actually prints, that rounds
back to both 86 and 74." Replace "Both land exactly, with nothing left over" with "Both round back
to the printed figure", in both places.

**V3-3** · `illustration.body` ("belong to the 42 men"; "That mismatch is real. It is the paper's, not a mistake in this rebuild."); `practice[6]` ("carries the same mislabelling problem") · **error (inference stated as fact)**
Problem: that the percentages come from the 42 men is an inference from rounding, and a strong
one. The illustration states it as a finding. It also never says the check assumes ordinary
rounding. Under truncation 45/52 and 59/79 *do* give 86 and 74. The evidence that the paper
rounds normally is in the paper: four rows with undisputed groups (women's waist, men's and women's
body fat on the arm, men's body fat on the neck) divide back only under ordinary rounding.
Fix: change "belong to" to "fit". Replace "That mismatch is real. It is the paper's…" with "Every
other row of Table 3 divides back under ordinary rounding, so the paper rounds that way. On that
rounding this row fits the 42 and not the 52." In practice[6], write "appears to carry".

**V3-4** · `illustration.body` ("That is well above the study's own planning figure, 20 per cent"; "One in five is the study's own planning assumption"); `exercises[0].answer` ("Applied to the study's own planning assumption of 20 per cent"); `practice[12]` answer ("at the study's own planning prevalence of one in five") · **error (M1, M12; group mismatch)**
Problem: M1 says the re-application uses *stated conditions*, "Not the NFHS-4 figure". The fixer
tied one in five back to the planning figure. That figure is also a different group. The paper
planned on 20 per cent "overweight" from NFHS-4, which is an index of 25 or more. The table's
condition is now the 25–29.9 band. Comparing 32 per cent in the band against a 20 per cent
25-or-more figure compares two definitions (the 25-or-more share among the men is 39.7 per cent).
Fix: in the illustration, delete the "well above the planning figure" sentence and write "One in
five is a stated condition, chosen for the arithmetic." In the exercise, write "In a group where
one in five is in the band". In the L10 answer, write "in a stated group where one in five is at
25 or more".

**V3-5** · `practice[12]` (L10) prompt ("It uses the same 52-against-79 split tried earlier in this section") and answer ("Unlike the arm cut-off, the neck row's own label does match the group its numbers were computed on") · **error (false inference; unsupported premise)**
Problem: the neck row's 81 and 71 fit 52 against 79 (42, 56) *and* 42 against 89 (34, 63).
Fitting one split proves nothing. The men's arm row and both women's rows fit only the band, so
the band is the likelier group here too. The prompt states as given a split nobody knows.
Fix: delete the prompt sentence. In the answer, replace the "does match" sentence with "Both 52
against 79 and 42 against 89 round back to 81 and 71, so this row alone cannot say which group the
paper used." Add the band figure beside the 65 per cent: 34 of 60 flagged, about 57 per cent. The
lesson is that the figure moves with the group.

**V3-6** · `exercises[0].answer` ¶2 · **error** · still open from D3-11
Problem: the answer opens "Eighty-six per cent of what? 'Accurate' could mean three different
figures." It then asserts "It is the share of people who truly are in the higher band whom the test
catches." "The higher band" is also meaningless to a health secretary.
Fix: "If it is the sensitivity — the share of people who have the condition whom the test catches
— then it says nothing yet about how often a positive result is right."

**V3-7** · `practice[11]` (L9) prompt and answer · **error**
Problems:
- (a) The claim is about "men with a body-mass index of 25 or more", but the answer computes for
  the 25–29.9 band.
- (b) "In the officer's own district, about one in three men are thought to fall in the … band" is
  an invented statistic set in a real-sounding place (§7a).
- (c) "The two numbers are close by chance" contradicts the next sentence, which gives the reason:
  one in three is close to the students' 32 per cent.

Fix:
- (a) Put the claim in the band.
- (b) Write "Suppose one in three men in the district were in the band".
- (c) Replace "close by chance" with "close because one in three is close to the students' 32 per
  cent. At a different share it would not be".

**V3-8** · `illustration.numbers` · **error (M13)**
Problem: numbers[79]'s quote (the Obese row) is not the passage 79 was counted from. numbers[52]'s
quote carries only the 42 of 42 + 10. Also, 59, 72, 61 per cent (36/59) and 32 per cent (42/131)
are computed from the paper in the illustration and are not registered.
Fix: requote 79 to "We enrolled 282 medical students (131, 46.5% males". Add 59, 72, 61 and 32 with
`derived:` lines (36 + 23; 6 + 66; 36 ÷ 59; 42 ÷ 131).

**V3-9** · `practice[10]` (L8) · **style (new duplication)**
Problem: the illustration already divides 44/52 and 45/52 and says neither is 86. The diagnostic's
answer is printed above its prompt.
Fix: rebase it on a row the reader has not divided back, for example the men's waist row. Worked
wrong answer: "0.85 × 41 = 34.85, so 34 caught; 34/41 rounds to 85." The broken step is rounding
34.85 down, since 34/41 is 82.9 and 35/41 is 85.4.

**V3-10** · `exercises[1].answer` · **style**
Problem: "Two independent places agree on 28". Three agree: the methods, Table 2 and Table 3
("≥28%").
Fix: "Three places agree on 28".

**V3-11** · `exercises[1].prompt` · **floor (test 3)**
Problem: "body fat measured by bio-impedance" is a term of art with no gloss. D7 comes later.
Fix: "body fat measured by a machine that passes a small current through the body", or drop the
phrase.

**V3-12** · `simplified_explanation` ¶5–6 · **style**
Problem: "Four names cover almost every screening result you will meet", and then five are given
(the negative predictive value was added).
Fix: "Five names".

**V3-13** · `illustration.body` ("That is why it earns the name 'best estimate'") · **style**
Problem: the name is quoted as if introduced, and nothing in this version introduces it.
Fix: "That is why it is the best estimate here."

**V3-14** · `must_know[6]` · **style**
Problem: "A shared total or a row's own label can settle which figure…". The section's lesson,
must_know[4], is that a row's label is not proof.
Fix: "A shared total, or rows that must add up, can settle…".

**V3-15** · `practice[8]` (L7) answer · **style**
Problem: "a gap of one and a half percentage points". It is 40.07 − 38.7 = 1.37. Also, "both in the
high thirties and forties" is garbled.
Fix: "about 1.4 percentage points"; "both round to about 40".

Not a defect, noted: C26's drill set is now 13 problems, against the inventory's expectation of
14–16. The inventory calls these expectations, not targets, and the ladder climbs all four bands.

---

## Verdicts

**C24 (D1).** Nearly done. The odds errors are gone and the new anchor is real and quoted, but one
sentence in the journalist answer still says odds and probability part "away from the middle"
(V1-2), and the level 9 answer still carries a clause that applies the national ceiling to a
district (V1-1).

**C25 (D2).** One real defect remains. The level 10 problem still takes a household-of-four bound
from a ceiling on persons, which M2 forbids (V2-1). Everything else is small.

**C26 (D3).** The rebuild is right in substance, and the ladder and rows/columns are fixed. It is
not releasable yet:
- two statements are false by arithmetic ("only whole-person table", V3-2; "fell by about a
  third … more than half", V3-1);
- the neck-row answer draws a conclusion its own numbers cannot support (V3-5);
- the one-in-five re-application was tied back to the planning figure against M1 (V3-4).
