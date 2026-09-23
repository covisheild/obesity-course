# Defects · Book 0 Part D, D1–D3 (B0-R0-C24, C25, C26)

Audit of the three records against `sources/` and against a recomputation of every figure.
Audited 2026-09-23. Records were not edited.

**Conventions.** List indices are zero-based, as in the YAML: `practice[5]` is the sixth problem.
The level is given beside it so nobody has to count. Severity is **error** (wrong, unsourced,
or breaks the brief or §7a), **floor** (one of the six operational tests), or **style**.

**What was run.**

- Every `working` line in the three records was parsed and recomputed in Python: 135 equations,
  and all 135 are correct. The arithmetic errors below are all in prose sentences *about* the
  arithmetic, which the build's equation check cannot see.
- Every `quote` was searched for in the file that `sources/INDEX.yml` maps its citekey to, with
  whitespace and case normalised as the build does. All are present, and `build.py --check`
  reports 0 blocking lines for C24–C26. Being present is not the same as carrying the claim.
  The failures below are quotes that are in the file and do not say what the record needs them to.
- D3's table was rebuilt from Kiran Table 2 and Table 3. Then every row of Table 3 was tested for
  whether *any* whole-number count could produce its printed sensitivity, specificity and Youden's
  index. The result is D3-1.

---

## The numbers rule (incoming): every `illustration.numbers` entry

| Record | Entry | Value | Verdict | Why |
| --- | --- | --- | --- | --- |
| C24 | numbers[0] | 75 | pass | quote states "seventy-five per cent." |
| C24 | numbers[1] | 50 | pass | quote states "fifty per cent." |
| C25 | numbers[0] | 75 | pass | quote states "seventy-five per cent." |
| C25 | numbers[1] | `household` | **fail** | not a number, and its quote ("Every person belonging to priority households") states none. See D2-13 |
| C26 | numbers[0] | 131 | **fail** | the quote "Men (n = 131) (%)" is a table column heading, which is the form the rule excludes. The locator "s.3.1 of the study's Table 2" names a section the paper does not have. See D3-26 |
| C26 | numbers[1] | 52 | **fail** | the quote states 83, 29.4, 42 and 32.1, and not 52. The value is computed as 42 + 10 and is not marked as derived. See D3-7 |
| C26 | numbers[2] | 10 | pass | the flattened Table 2 row states 10 in the men's cell |
| C26 | numbers[3] | 86 | pass | states "sensitivity: 86%". The unit says Table 3 but the quote is from the abstract (D3-26) |
| C26 | numbers[4] | 74 | pass | states "specificity: 74%". Same locator slip |
| C26 | numbers[5] | 20 | pass | states "20%" |

The schema on this branch has `additionalProperties: false` on a numbers item, so there is no
field to mark a number as derived. The fixes below say "mark as derived" and mean whatever field
the incoming rule adds.

---

## D1 · B0-R0-C24 What a probability is

**D1-1** · C24 · `definition.text` ¶4 (odds) · **error (sourcing)**
Claim: "odds equal p divided by (1 minus p)", given as part of the defined content.
Source: the word *odds* does not occur anywhere in `openstax_intro_stats_2e.txt` (0 hits), and no
other held file defines it. No reference sits under this paragraph. It is the only paragraph of the
definition with no text behind it, and it is also the section's named trap.
Fix: add a note to `verified.note`: "odds: not in the held anchor; definition drafted, source
outstanding". Add the missing instrument, an open text that defines odds, to `READY-part-D.md` as
**no**. Do not attach an OpenStax quote to it.

**D1-2** · C24 · `definition.references[1].quote` · **error (sourcing)**
Claim: this reference backs ¶2, "the probability of an event is the count of outcomes in the event,
divided by the count of outcomes in the whole sample space".
Source: the quote "Equally likely means that each outcome of an experiment occurs with equal
probability" defines *equally likely* and says nothing about counting. The rule is five lines further
on in the same file: "count the number of outcomes for event *A* and divide by the total number of
outcomes in the sample space". ¶1 (sample space, outcome, event) and ¶3 (the complement adds to 1)
are in the file too, and neither is quoted.
Fix: replace quote 2 with "count the number of outcomes for event *A* and divide by the total number
of outcomes in the sample space". Copy it as stored, with the asterisks. Add "The sample space of an
experiment is the set of all possible outcomes." and "An event is any combination of outcomes."
Both are plain running prose in s.3.1.

**D1-3** · C24 · `exercises[0].answer`; `practice[8]` (L9) prompt and answer · **error (sourcing)**
Claim: "up to three in four rural people **here** can be covered". Also "three in four rural people
here are covered … the note's figure matches the Act's ceiling exactly".
Source: s.3(2) puts the 75 per cent on "the rural population". s.9 then hands "the percentage
coverage … for each State" to the Central Government, "subject to" s.3(2). Nothing in the Act fixes
a share for a block, a district or "here". The State figures are not in `sources/`. The Act's
ceiling is a national figure, and it is not a local one.
Fix: in the exercise answer, change "rural people here" to "of India's rural population". In the
practice[8] answer, add one sentence: "And the 75 per cent is a national ceiling. The Act leaves
each State's share to the Central Government under section 9, so it says nothing about this place
in particular."

**D1-4** · C24 · `illustration.body` ¶ after the urban odds · **error**
Claim: "A reader who thinks it [odds of one] means 'half the time' has understood odds and
forgotten they are not the probability."
Arithmetic: odds of 1 give 1 ÷ (1 + 1) = 0.5, which *is* half the time. The reader the sentence
scolds is right.
Fix: "A reader who hears 'odds of one' as 'always' has read the odds as a probability. Odds of one
mean half the time."

**D1-5** · C24 · `illustration.analogy_breaks_when` ¶2–3 · **error**
Claim: odds and probability "pull apart faster the closer either one gets to the ends of the
scale". Also: "That is why studies of rare events report odds instead of probability."
Arithmetic: near 0 they are almost the same number. p = 0.01 gives odds 0.0101, and p = 0.02 gives
odds 0.0204. They pull apart only near 1. So the rare-event sentence has it backwards: for rare
events odds and probability almost agree. The reason it gives is also unsourced.
Fix: "Near 0 they are almost the same number: 0.01 gives odds of 0.0101. Near 1 they pull apart:
0.99 gives 99, and 0.999 gives 999." Delete the rare-events sentence.

**D1-6** · C24 · `must_know[1]` · **error**
Claim: "Near the ends of the scale they pull apart fast. A probability change from 0.5 to 0.6
barely moves the odds."
Arithmetic: 0.5 to 0.6 moves the odds from 1 to 1.5, a rise of half, while the probability rose by a
fifth. That is not "barely". It is also wrong at the low end, as in D1-5. The point is right only
for probabilities near 1. The illustration's "0.6 gives odds of 1.5, barely different" has the same
slip.
Fix: "Near 0, odds and probability are almost the same number. Above one half they pull apart,
and near 1 they pull apart fast: 0.99 to 0.999 multiplies the odds by ten." Change "barely
different" in the illustration to "already half as much again".

**D1-7** · C24 · `practice[5]` (L6) answer, last two sentences · **error**
Claim: "A modest difference in probability near the middle of the scale can become a large
difference once converted to odds. The reverse holds nearer the ends of the scale."
Arithmetic: near 1 the stretching is stronger, not reversed (0.98 against 0.99 gives odds of 49
against 99). The sentence also contradicts `must_know[1]`, which says the two move "almost together"
near the middle.
Fix: "The stretching grows as the probabilities approach 1. Near 0 it almost vanishes."

**D1-8** · C24 · `practice[6]` (L7) answer ¶2 · **error**
Claim: "Here 0.25 is only the probability by coincidence at one particular value — it is not a
rule."
Arithmetic: odds equal probability only at p = 0. At every other value the odds are larger. There
is no value where 0.25 odds is a 0.25 probability.
Fix: "Odds and probability are equal only at zero. At every other value the odds are the larger
number."

**D1-9** · C24 · `must_know[5]` · **error**
Claim: "'Odds of three to one' and 'a probability of three to one' are two different sentences.
Only the second one means what most people will hear."
Problem: "a probability of three to one" is not a probability. The sentence teaches the confusion
it warns against.
Fix: "'Odds of three to one' means three chances in four. Say 'three in four' and the journalist
hears it right."

**D1-10** · C24 · `must_know[2]`; `simplified_explanation` ¶5 · **error (bound breached)**
Claim: "Every paper reporting a case-control study or a logistic regression reports odds, never
probability … Convert to probability in your head … before you repeat a figure."
Problem: those papers report *odds ratios*, not odds. An odds ratio cannot be turned into a
probability without a baseline risk. A reader who runs 2.5 ÷ 3.5 on an odds ratio of 2.5 gets a
wrong number. So the instruction breaches the inventory's bound ("drills the conversion both ways,
and stops"). "Never probability" also overstates the case. *Case-control study* and *logistic
regression* are terms of art with no definition and no pointer (floor test 3).
Fix: cut `must_know[2]`. In ¶5 replace the last sentence with "Many papers you will read later
report odds rather than probabilities. Learn to move between the two now."

**D1-11** · C24 · whole record · **error (coverage)**
Claim missing: the inventory's sentence "A probability is a proportion you work out before the
draw … must be said". The word *proportion* does not appear in C24. The bridge from A5 (glossary:
"a part out of the whole it came from, never more than one") is never made.
Fix: add it as the first sentence of `simplified_explanation`, in the glossary's words: "A
probability is a proportion — a part out of the whole it came from, never more than one — worked
out before the draw instead of after it."

**D1-12** · C24 · `retrieval_items[0].a` · **error**
Claim: "Probability is the count of outcomes in an event divided by the count in the whole sample
space."
Problem: that holds only when the outcomes are equally likely, which the definition says and the
card drops. It is the one line the reader will memorise.
Fix: insert "When every outcome is equally likely," at the start.

**D1-13** · C24 · `illustration.numbers[*].as_of` · **error (currency)**
Claim: `as_of: '2026-09-23'` on the 75 and 50 per cent figures.
Source: `SOURCES.md` records that `nfsa_2013.txt` "carries no amendment footnote at all, so it reads
as the Act as enacted in 2013". Nobody checked the figures as current on 2026-09-23. They were
read from the enacted text.
Fix: set `as_of` to the text's own date and say so in the unit. Before release, re-check s.3(2) and
s.9 against the current India Code consolidation. The same applies to C25 numbers[0].

**D1-14** · C24 · `illustration.body` ("Turn odds back into a probability with p equals odds divided by (1 plus odds)"); `practice[1]` answer · **floor (test 5)**
The inverse formula is stated and never derived. Getting it by rearranging needs the letter
collected from both sides and taken outside a bracket. C15–C17 do not show that move: C16 does the
same thing to both sides with the unknown on one side only.
Fix: derive it by parts, using only A5. "Odds of 1.5 mean 1.5 parts for to 1 part against, 2.5
parts in all. So the probability is 1.5 divided by 2.5." Then state the rule in words.

**D1-15** · C24 · `definition.text` uses *p*; `illustration.body` introduces *P(A)* · **style**
Two notations for one thing, and nothing links them.
Fix: in the illustration, add "P(A) — the p of the definition, for this event".

**D1-16** · C24 · `illustration.analogy_breaks_when` ¶1 · **style**
"Treat 0.75 and 0.25 as the largest and smallest that could be true" reads as P(covered) lying
between 0.25 and 0.75.
Fix: "Treat 0.75 as the largest the chance of being covered could be, and 0.25 as the smallest the
chance of not being covered could be."

**D1-17** · C24 · `illustration.body` ¶1 · **style**
The illustration uses "five kilograms … per person per month" (s.3(1)), and the number is not
registered in `illustration.numbers`.
Fix: add it, with the quote "five kilograms of foodgrains per person per month".

**D1-18** · C24 · `illustration.body` ("Suppose a district report says … two to one against") · **style**
An invented figure, dressed as a district report (§7a: "never invent a statistic to make a problem
feel applied").
Fix: "Suppose you read that the odds are two to one against."

**D1-19** · C24 · `simplified_explanation` ("one of the commonest mistakes in reading a medical paper"); `must_know[0]` ("the single commonest slip in this section") · **style**
Unsourced superlatives. The second one has "this section" as its subject.
Fix: cut "one of the commonest mistakes…". In must_know[0], write "a common slip".

---

## D2 · B0-R0-C25 Counting outcomes; independence

**D2-1** · C25 · `illustration.body` ("at least one" ¶) · **error (arithmetic)**
Claim: "That runs to seven cases before you even reach 'all three'."
Arithmetic: the ways of "at least one of three" number 2 × 2 × 2 − 1 = 7 *including* "all three"
(3 with exactly one, 3 with exactly two, 1 with all three). Six come before it.
Fix: "That runs to seven cases, 'all three' among them."

**D2-2** · C25 · `illustration.body` last ¶ · **error (arithmetic)**
Claim: "One subtraction and two multiplications did the work."
Arithmetic: the working shows two subtractions (1 − 0.75 and 1 − 0.015625) and two
multiplications.
Fix: "Two subtractions and two multiplications".

**D2-3** · C25 · `definition.references[2].quote` · **error (sourcing)**
Claim: this reference backs the multiplying rule, the adding rule, 2 to the power n and "at least
one through the complement".
Source: the quote "there are two rules to consider when determining if two events are independent
or dependent and if they are mutually exclusive or not" is a signpost sentence. It states neither
rule. The anchor states the rules only as formulas (s.3.3), not in running prose. It never states
2 to the power n, and it has "at least one" only as a worked example (s.3.2). The strongest
running-prose support for ¶2's "checked, not assumed" is not quoted: "**assume they are dependent
until you can show otherwise**" (s.3.2).
Fix: replace quote 3 with "assume they are dependent until you can show otherwise". Add "If *A* and
*B* are mutually exclusive, then *P*(*A* AND *B*) = 0." as stored. In `verified.note`, say the
product rule, 2 to the power n and the complement route are derived in the record, not located in
the anchor.

**D2-4** · C25 · `practice[11]` (L9) prompt ("from a rural block"); `practice[12]` (L10) prompt and answer ("in this district") · **error (sourcing)**
The same defect as D1-3. The 0.75 bounds "the rural population" of the country, and s.9 sets each
State's share separately. It is not a ceiling for a block or a district, so a block's two residents
are not two draws from a 0.75 population.
Fix: in L9, drop "from a rural block" and use "two rural residents picked at random". In the L10
answer, add: "A district report cannot quote section 3(2) as a district ceiling. The 75 per cent is
national."

**D2-5** · C25 · `practice[12]` (L10) answer ("At least 0.25, not about 0.68") · **error**
Claim: for "a household of four", the chance that at least one member is not covered is at least
0.25.
Problem: 0.75 caps the share of *persons* covered. It does not cap the share of four-person
*households* covered. If larger households were covered more often, more than 75 per cent of them
could be covered with the person-level ceiling still met. The bound holds only when the household
is reached by picking a rural *person* at random and looking at their household.
Fix: prompt: "Pick one rural person at random. They live in a household of four. The report
concludes…". The answer then stands as written.

**D2-6** · C25 · `practice[11]` (L9) prompt · **error**
Claim: "Two beneficiaries are picked at random … the chance both are covered is 0.5625."
Problem: a beneficiary is by definition covered, so the chance is 1. The prompt contradicts itself.
Fix: "Two rural residents".

**D2-7** · C25 · `definition.text` ¶2 and ¶3 · **floor (test 1)**
*P(A and B)* and *P(A or B)* appear in the definition, and nothing says them in words. C24 named
only P(A).
Fix: at first use, "P(A and B), the probability that A and B both happen".

**D2-8** · C25 · `practice[10]` (L8) answer · **style**
The broken answer's last line changes the question. It says "at most 2.25 of the three are
covered", which is a count, and 3 × 0.75 = 2.25 is a correct ceiling on the *average number*
covered. The answer calls 2.25 "impossible" and misses the switch, and the switch is the reason the
wrong answer looks reasonable.
Fix: add "Adding the three gives the most people you would expect covered on average, 2.25. That is
a real number, and it answers a different question. It is not the chance that at least one is
covered."

**D2-9** · C25 · `simplified_explanation` ¶4 ("does knowing one changed the odds of the other?"); `exercises[1].answer` ("change the odds of the other") · **style (term drift, §10.2)**
*Odds* is used in its loose everyday sense one section after C24 made it a technical number. There
is also a grammar slip ("changed").
Fix: "does knowing one change the chance of the other?" in both places.

**D2-10** · C25 · `practice[6]` (L5) prompt · **style (hint)**
"Then explain why the calculation is different from the previous problem" tells the reader it is
different.
Fix: "Then compare your answer with the previous problem's."

**D2-11** · C25 · `practice[9]` (L7) prompt, worked line 3 · **style (hint)**
"treating the two as independent, P(both covered) = …" labels the broken assumption inside the
worked answer, so the diagnosis is handed over.
Fix: line 3 becomes "P(both covered) = 0.75 times 0.75".

**D2-12** · C25 · `practice[9]`, `practice[10]` · **style**
Both use the Act's 0.75 and carry no `refs`.
Fix: add `refs: [nfsa_2013]`.

**D2-13** · C25 · `illustration.numbers[1]` · **style (fails incoming rule)**
`value: household` is not a number.
Fix: remove the entry. The household point is carried by the prose and by `refs`.

**D2-14** · C25 · `definition.text` ¶2–3 · **style**
The product rule is stated twice in consecutive paragraphs.
Fix: delete the first sentence of ¶3.

**D2-15** · C25 · `simplified_explanation` ¶1 · **style (§10.5)**
The first sentence does not say the section stands on C24.
Fix: "This section stands on the last one: a probability, and its complement."

---

## D3 · B0-R0-C26 Conditional probability through the two-way table

**D3-1** · C26 · `illustration.body` ¶2–4; `analogy_breaks_when` ¶1; `practice[5]`, `[6]`, `[8]` · **error (sourcing and arithmetic — the most serious in the batch)**
Claim: "It prints how well the 31.3 centimetre cut-off catches the 52 men with the larger index:
86 per cent … 74 per cent of the 79." The rebuilt 45 / 21 / 7 / 58 table is presented as "a best
estimate" of the paper's table.
Recomputed: **no whole number of men out of 52 rounds to 86 per cent** (44/52 = 84.6, 45/52 =
86.5 → 87). **No whole number out of 79 rounds to 74 per cent** (58/79 = 73.4, 59/79 = 74.7 → 75).
Under truncation instead of rounding, the counts would be 45 and 59, not 45 and 58, and their
Youden's index is 0.61, not the printed 0.60. So the printed 86 and 74 cannot have come from groups
of 52 and 79 under any single convention.

They do fit 42 and 89 exactly: 36/42 = 85.7 → 86, 66/89 = 74.2 → 74, and the index is 0.599 →
0.60. 42 is the paper's "Overweight (25–29.9)" row alone, with the 10 in the obese row among the
negatives. The same holds for every overweight row of Table 3. The women's arm and neck rows cannot
come from 46 women (41 + 5), and all four overweight rows fit 42 men or 41 women. Every other row of
Table 3 fits its own group sizes: waist 41/90 and 68/83, body fat 71/60 and 114/37.

So the paper's label ("BMI ≥ 25") and its own percentages disagree. The whole applied band of D3
stands on the label.
Fix, smallest: keep the 52/79 table as the teaching table. Say in the illustration and in
`analogy_breaks_when` that the paper never gives 52 (it is 42 + 10). Say that no whole count of 52
or 79 reproduces 86 and 74, so these cannot be the paper's own counts. Say that the percentages fit
the 42 men of the 25–29.9 row, so this table is a reconstruction under the paper's label, not the
paper's table. That is a better lesson than the one it replaces.
Main-thread decision: whether to switch to 42/89 instead (36 / 23 / 6 / 66, positive predictive
value 36/59 = 61 per cent, prevalence 32 per cent). That is also an inference, and must be labelled
one. The 1,000-men re-application uses only 86 and 74 and is unaffected either way.

**D3-2** · C26 · `illustration.body` ¶ after the back-check · **error (arithmetic)**
Claim: "two of its four cells could each be one person either way without the rebuild changing
which whole-number percentage they round to."
Arithmetic: 44/52 = 84.6 → 85, 46/52 = 88.5 → 88, 57/79 = 72.2 → 72, 59/79 = 74.7 → 75. Every
one-person move changes the rounded percentage. And no choice gives 86 and 74 (D3-1).
Fix: "No whole number of the 52 gives exactly 86 per cent, and no whole number of the 79 gives
74. The paper's two percentages cannot be recovered as whole people from these totals."

**D3-3** · C26 · `practice[8]` (L6) answer · **error**
Claim: "86.5 rounds up past 86, and 73.4 rounds down past 74."
Arithmetic: 73.4 is below 74 and rounds to 73. The conclusion ("enough to lose the exact figure")
also understates the finding: no count at all reproduces the pair.
Fix: "86.5 rounds to 87 and 73.4 to 73. Try 44 and 59 instead: they give 85 and 75. No whole count
gives back 86 and 74, which tells you these totals are not the ones the paper divided by."

**D3-4** · C26 · `illustration.analogy_breaks_when` ¶2; `practice[12]` (L9) answer · **error (arithmetic)**
Claim: "the positive predictive value nearly halved".
Arithmetic: 0.4526 ÷ 0.6818 = 0.66, a fall of about a third. What halved was the prevalence (40 to
20 per cent).
Fix: "fell by about a third, from 68 to 45 per cent, while the prevalence halved".

**D3-5** · C26 · `illustration.body` ¶5 ("The paper does print a check on its own two percentages … Youden's index"); `must_know[4]`; `retrieval_items[2]` · **error (sourcing)**
Claim: the Youden's index is a check the paper prints on its own two percentages, and "a mismatch
… flags an error". must_know[4] says to use it "to catch a typo before you trust either number".
Source: the paper says the index is how it *chose* each cut-off: "cut-offs points identified using
Youden index (J statistic). It is a single statistic that captures the performance of a diagnostic
test". It is not a check. And as a check it gives false comfort here: the row the section rests on
passes it (0.86 + 0.74 − 1 = 0.60) while its percentages cannot come from 52 and 79 whole men
(D3-1). Sensitivity and specificity are two separate measurements, so "consistent with each other"
means nothing.
Fix: see the Youden verdict below. Remove it from the illustration, `must_know[4]` and
`retrieval_items[2]`. Rewrite must_know[4] around the check that does work: "Divide back. If no
whole number of people gives the printed percentage, the total you are dividing by is not the
paper's."

**D3-6** · C26 · `practice[10]` (L7, body fat) answer · **error (misdescribes the paper)**
Claim: "recomputation alone cannot tell you which is right", because "rounding to one decimal place
hides a difference that small from both directions."
Source and arithmetic: the paper settles it. Table 2 gives 71 men + 114 women = 185, and the
results text says "71 (54.2) men and 114 (75.5%) women participants had excess of PBF". Table 2's
normal row gives 97 + 185 = 282, whereas 97 + 186 = 283. The rounding claim is also wrong. One
decimal place separates them (65.6 against 66.0). It is the abstract's whole-number "66%" that
cannot, because 185/282 also rounds to 66.
Fix: "The percentages cannot settle it: the abstract rounds to a whole number, and 185 rounds to 66
too. The paper's own sums can. 71 men plus 114 women is 185, and 97 plus 185 is 282. The abstract's
186 is the slip." The prompt's "185 (65.6%)" should read "185 (65.6)", as Table 2 prints it.

**D3-7** · C26 · `illustration.body` ¶2 ("The study's own count: 52 of the 131 men"); `illustration.numbers[1]` · **error (sourcing; fails incoming rule)**
The paper never prints 52. Table 2 prints 42 (25–29.9) and 10 (30 or more).
Fix: "Table 2 gives 42 men from 25 to 29.9 and 10 at 30 or more." Add a working line, 42 plus 10
= 52. Register 42 with the Overweight-row quote, re-quote 10 as it is, and mark 52 as derived
(42 + 10, Table 2, men).

**D3-8** · C26 · `illustration.body` ¶3 ("round the widest part of the upper arm") · **error (sourcing)**
Source (methods): measured "at the midpoint of the tip of the shoulder (acromion process) and tip
of the elbow (olecranon process)". That is the midpoint, not the widest part.
Fix: "halfway between the tip of the shoulder and the tip of the elbow".

**D3-9** · C26 · `exercises[0].answer` ("this college's own students, about 40 per cent"); `practice[12]` (L9) prompt ("Its own college sample ran higher, at 40 per cent"); `practice[14]` (L10) answer ("40 per cent among medical students") · **error (misattributed figure)**
Arithmetic: 40 per cent (52/131 = 39.7) is the men only. The whole sample was 98/282 = 34.8 per
cent.
Fix: "among the 131 men" in all three places.

**D3-10** · C26 · `must_know[3]` (boundary); `simplified_explanation` ¶5 ("belong mostly to the test"); `practice[14]` answer ("Sensitivity is the one figure that does travel reasonably well across groups") · **error (unsourced empirical claim; contradicts the record)**
Claim: sensitivity and specificity are "properties of the test, roughly stable across settings".
Problem: no held source says so. It is an empirical claim about tests in general, and the record's
own `practice[12]` answer says the opposite ("that is an assumption, not something the arithmetic
proves"). As a boundary point it names the wrong limit.
Fix: rewrite must_know[3]: "The positive predictive value belongs to the group tested, not to the
test. Carrying sensitivity and specificity to a new group is itself an assumption. Say so whenever
you do it." In the simplified explanation, cut "mostly" and make the same concession. In
practice[14], delete the sentence.

**D3-11** · C26 · `exercises[0].answer` (health secretary) · **error (Kiran used as evidence about screening; contradicts must_know[5])**
Claims: "Eighty-six per cent is not the share of positive results that are correct; it is the share
… whom the test catches." Also "the second one is usually smaller". Also "At a prevalence closer to
the general young-adult population, about 20 per cent, the same test's positive results were right
closer to 45 times in 100."
Problems: (a) "86 per cent accurate" does not say which figure is meant. must_know[5] says exactly
that ("none of the three can be recovered from that one word"). The rebuilt table's overall share
correct is (45 + 58)/131 = 79 per cent, not 86. (b) "Usually smaller" is unsupported, since it
depends on prevalence. (c) The 45 per cent is a projection onto a planning assumption. Written as
what the test's results "were" in "the general young-adult population", it becomes a claim about
screening, which the inventory forbids.
Fix: open with "Eighty-six per cent of what? 'Accurate' could mean three different figures." Keep
the 68 and 45 as the arithmetic of the teaching table: "in a group where two in five have it … in
one where one in five has it". Drop "general young-adult population" and "usually".

**D3-12** · C26 · `practice[14]` (L10) answer · **error**
Claim: in answer to a note about *neck* circumference, "the same test's positive predictive value
fell from about 68 per cent to about 45 per cent to about 27 per cent". It also gives "81 to 86 per
cent … for a similar men's overweight cut-off".
Problem: those three positive predictive values are the *arm* cut-off's. 81 is the neck figure and
86 the arm figure, run together as one range.
Fix: compute the neck figures, which also answers D3-18's "computes nothing". With sensitivity 81
and specificity 71: among 52/79, 42.12 ÷ (42.12 + 22.91) = 65 per cent; in 1,000 at 20 per cent,
162 ÷ (162 + 232) = 41 per cent.

**D3-13** · C26 · rows against columns: `simplified_explanation` ¶2–3; `illustration.body` ("Sort the 131 men down one side by … index"; "Take the column of men with an arm of 31.3 … 66"; "Take the row of men with an index of 25 or more — 52"); `practice[1]`, `[2]`, `[3]`, `[6]`, `[7]` answers; `retrieval_items[1]` · **error (teaches rows and columns backwards)**
Every sentence puts the true condition down the rows and the test result across the columns
("divides by the row of people who have the condition"; "the column of flagged men totals 66").
All five tables do the opposite: test result in the rows, condition in the columns. The section
that teaches a two-way table from nothing, before F1, calls every row a column and every column a
row, at least a dozen times.
Fix: transpose the five tables (illustration ×2, practice[0], practice[5], practice[12]) so the
rows are the condition and the columns the test. No sentence then needs to change.

**D3-14** · C26 · `definition.text` ¶3–4 (sensitivity, specificity, positive predictive value, prevalence, and the prevalence effect) · **error (sourcing)**
None of these terms occurs in `openstax_intro_stats_2e.txt` (0 hits for sensitivity, specificity,
predictive, prevalence). Kiran uses the words without defining them. No quote sits under half the
definition, and `READY-part-D.md` lists no source for screening vocabulary.
Fix: in `verified.note`, record that ¶3–4 are defined in the record as cell-over-total and not
located in the anchor. Add the missing instrument to READY as **no**.

**D3-15** · C26 · `illustration.body` ("About 40 per cent, which is far higher than in the wider population these medical students stand in for") · **error**
The students were volunteers from one college, and the paper names that as its main limitation
("single centre measurements consisting of only young adults"). They stand in for no wider
population. The 20 per cent is a planning assumption for all adults, and the paper's own
introduction gives 19 per cent for men. It is not a measurement of a comparable group. The
sentence also runs ahead of D6.
Fix: "About 40 per cent. Before it measured anyone, the paper planned on 20 per cent, a national
survey figure for all adults."

**D3-16** · C26 · `exercises[0].answer`, `illustration.body`, `numbers[5]` · **error (currency)**
The 20 per cent is NFHS-4 (2015–16). The same Kiran file already gives NFHS-5 (2019–21): 22.9 per
cent in men and 24 per cent in women. NFHS-6 must be checked, and it is not held. Wherever the
record treats 20 per cent as a population prevalence (see D3-11 and D3-15), that is out of date.
Where it is described as the paper's planning figure, it is correct and stays.
Separately, BMI ≥ 25 is the WHO cut-off the paper uses. Indian guidance uses different cut-points
for Asian Indians. That guidance is not in `sources/` and must be obtained before any sentence
treats 25 as India's line. The record does not do so now. Keep it that way.

**D3-17** · C26 · `practice[9]`, `[10]`, `[11]` (the diagnostic band, L7, L7, L8) · **error (§7a ladder)**
None of the three contains a worked answer that is wrong, and no answer names a broken step. They
are consistency checks. The build cannot see this, and C26's diagnostic band is empty in substance.
Fix: recast each as a wrong worked answer. For example [9]: "The abstract says 113 had abdominal
obesity, which is 38.7 per cent of 282, so 113 is the count." [10]: "Both 185 and 186 round to 66
per cent, so nothing in the paper can decide between them." Replace [11] (the Youden problem) with
the finding of D3-1: "86 per cent of 52 is 44.72, so 45 of the 52 men were caught." The reader
divides back, gets 87 per cent, and says why the rebuild looked right.

**D3-18** · C26 · `practice[12]`, `[13]` (L9), `[14]` (L10) (the transfer band) · **error (§7a ladder; hints)**
[12] and [13] are not claims in words. They are computations set out in full. [12] repeats the
illustration's 1,000-men working line for line, so its answer is printed above the prompt. [13]
differs from it only in its digits, and its prompt gives the result away ("chosen only to extend
the pattern"). [14] is a claim in words and computes nothing.
Fix: recast [12] as a sentence, for example: "A district officer says: 'The tape was right two
times in three in Mangaluru, so it will be right two times in three here.'" Make [14] compute the
neck figures (D3-12). Cut [13], or keep it as a level 5 applied problem with the hint removed.

**D3-19** · C26 · `practice[5]`, `[6]` (L5); `practice[8]` and `[11]` prompts; `exercises[1]` · **style (hints and duplication)**
[5] and [6] reproduce the illustration's rebuild and positive predictive value exactly. [8]'s
prompt ("Say what the comparison shows about rebuilding…") and [11]'s ("Use the table's own
Youden's index to say…") restate the method. `exercises[1]` (113 against 109) duplicates
`practice[9]`.
Fix: give [5]/[6] the women's arm row (88/83, 41 + 5 = 46 women, 105 without). The reader then
meets D3-1's problem for themselves. Strip the method from the prompts, and move exercises[1] onto
the women's body-fat cut-off inconsistency (abstract "women: ≥30%", methods and Table 2/3
"≥28%").

**D3-20** · C26 · `practice[10]` prompt ("PBF"); `practice[9]` prompt ("abdominal obesity") · **floor (tests 3 and acronym order)**
*PBF* is used unexpanded. In document order its first expansion is in C27 (the rendered B0.md,
line 7548, against first use at line 7447). *Abdominal obesity* is a term of art with no gloss.
Fix: "higher percent body fat (PBF) — the paper's label" and "abdominal obesity — the paper's label
for a waist of 90 cm or more in men and 80 cm or more in women".

**D3-21** · C26 · `practice[7]` (L6) prompt ("the negative predictive value") · **floor (test 3)**
A new term of art is introduced only inside a practice prompt. It is not in the definition, not in
the simplified explanation, and not in the drafter's glossary list.
Fix: add one sentence to `simplified_explanation` after the positive predictive value: "Its mirror
is the negative predictive value, the share of negative results that are right." Add it to the
glossary inbox.

**D3-22** · C26 · whole record · **error (coverage)**
The inventory (D2 note) and the bridge table (S03 r1, independence: "D2, D3") require D3 to restate
independence with a condition. C26 never mentions independence.
Fix: one sentence in `simplified_explanation`: "If P(A given B) equals P(A), knowing B tells you
nothing about A. That is the independence of the last section, written with a condition." Add one
line to `practice[2]` asking whether test and condition are independent in the invented table:
P(positive) = 25/100 = 0.25, against P(positive given present) = 0.75, so they are not.

**D3-23** · C26 · `practice[14]` prompt ("identifies overweight men"); `simplified_explanation` ¶4 ("the truly-affected", "the truly-unaffected") · **style (§9)**
Condition-first construction. "The truly-affected" is the same shape as "the obese".
Fix: "men with a body-mass index of 25 or more"; "people who truly have it", "people who do not".

**D3-24** · C26 · `definition.text` ("Four ratios, each one cell divided by one total"); `practice[2]` answer; `retrieval_items[1]`; "top count / bottom number" throughout · **style (glossary)**
The glossary gives *ratio* (C05) as "two quantities of the same kind set side by side". These four
are *proportions* ("a part out of the whole it came from"). Prevalence is also not "one cell
divided by one total": it is a margin total over the grand total. The record avoids the glossary's
*numerator* and *denominator* in favour of "top count" and "bottom number". The inventory asked for
"the same idea with a name". The anchor's own term, *contingency table*, sits in the reference
quote and is never given to the reader.
Fix: "Four proportions, each a count divided by a total". Use "denominator" at first mention of
the dividing total. Add "also called a contingency table" at first use of two-way table.

**D3-25** · C26 · `practice[11]`, `practice[13]` · **style**
Both quote real Kiran figures (81/71/0.52; 86/74) with no `refs`.
Fix: `refs: [kiran_2022_muac_nc]`.

**D3-26** · C26 · `illustration.numbers[0]`, `[3]`, `[4]`; missing entries · **style (numbers register)**
numbers[0]: the quote is a column heading and the locator "s.3.1" does not exist. Use the running
text "We enrolled 282 medical students (131, 46.5% males", locator "Results". numbers[3]/[4]: the
unit says Table 3 but the quote is the abstract, so say "abstract; Table 3 agrees". Missing: 42,
282, 31.3, and 0.60 if Youden's index stays.

**D3-27** · C26 · `illustration.body` ("Prevalence is simply how many") · **style (§1)**
"Simply" is used about a term first taught in this section.
Fix: delete "simply".

**D3-28** · C26 · `illustration.body` ("To fill in the table, treat those two percentages as counts") · **style**
The percentages are applied *to* counts. They are not treated as counts.
Fix: "apply those two percentages to the two totals".

**D3-29** · C26 · `must_know[6]` bearing; `must_know[0]` ("the single commonest error") · **style**
must_know[6] changes what the reader accepts as evidence, so its bearing is `methodological`, not
`teaching`. must_know[0]'s superlative is unsourced.
Fix: change the bearing. Write "a common error".

---

## Youden's index — verdict: it should go

It fails on every count that matters. It is outside the inventory's vocabulary, and it is a fifth
term of art in the section that already carries the most. The record misdescribes it: the paper
uses it to *choose* the cut-off, and the record calls it a check on the two percentages (D3-5). As
a "consistency check" it is empty, because sensitivity and specificity are separate measurements,
and in this paper it gives false comfort. The row D3 is built on passes the Youden arithmetic
exactly while its percentages cannot have come from the group sizes the record uses (D3-1).
must_know[4] and retrieval_items[2] would send the reader into every future paper trusting a check
that does not check.

The one thing it does, deciding the neck-row 82 against 71, is a single diagnostic problem, and the
count-consistency finding makes a better one. Remove it from the illustration, must_know[4] and
retrieval_items[2]. Replace practice[11] as in D3-17. Keep it out of the glossary inbox.

## Odds (D1) — verdict

The conversion is taught correctly in both directions, and every conversion in the working is
right. The prose around it is not. It says odds and probability diverge "at both ends" when they
converge near 0 (D1-5, D1-6, D1-7). Two sentences state falsehoods about when odds equal
probability (D1-4, D1-8). And the bound is breached in spirit: the must-know that sends the reader
to convert case-control and logistic-regression figures is advice about odds ratios, which cannot
be converted without a baseline (D1-10). The definition of odds itself has no source (D1-1).

---

## Verdicts

**C24 (D1).** The arithmetic is sound: every conversion recomputes, and the drill set climbs all
four bands, with genuine wrong worked answers at levels 7 and 8. The trouble is the sentences
*about* odds. Five of them are false: odds of one is not half the time, odds diverge at both ends,
rare-event studies use odds because odds diverge, 0.25 odds equal 0.25 probability "by
coincidence", and "a probability of three to one". One must-know would have the reader
mis-convert odds ratios. The odds definition has no source in the pack, and the inventory's
required sentence tying probability to A5's proportion is missing. It also carries the NFSA
national ceiling into "here" and "this block". It needs one careful pass on the odds prose and the
sourcing note. The structure can stay.

**C25 (D2).** The strongest of the three. The household trap is real, correctly sourced to s.3(1),
and well built. The ladder is sound, and all 37 working lines are correct. The defects are two
prose miscounts (seven cases, one subtraction), a signpost quote that does not carry the rules it
sits under, and a transfer problem whose household-level bound does not follow from a
person-level ceiling. "Beneficiaries", "rural block" and "district" misuse the Act's scope. Small
fixes throughout. Nothing structural.

**C26 (D3).** Not releasable as it stands, though its computations are all correct line by line.
Three things are wrong at the root. First, every sentence names rows as columns and columns as
rows, in the section that teaches the two-way table from nothing (D3-13). Second, the rebuilt table
rests on a group of 52 that the paper's own percentages rule out (D3-1), while the record tells
the reader the paper printed 52 and that its rebuild is off by at most a person. Third, the
diagnostic and transfer bands are consistency checks and restated worked examples, not wrong
answers and claims in words (D3-17, D3-18). Several sentences also cross from computing with the
paper into claims about screening and about test stability (D3-10, D3-11, D3-15), which the
inventory forbids. The PBF answer misreads the paper it quotes (D3-6), and Youden's index should go.
The fixes are mostly deletions and a transposition, but D3-1 needs a main-thread decision before
the applied band is redrafted.

---

## Resolution (fix pass)

Applied 2026-09-23, against `DECISIONS-part-D-fix.md` M1–M15, which override this audit's
"smallest fix" wherever the two differ (mainly D3-1 through D3-5, D3-9, D3-17 and D3-18, all
absorbed into M1's rebuild). "Fixed differently" means the defect is gone but not by the literal
sentence the audit proposed — usually because a later, larger rewrite (M1's table rebuild, or the
M15 sentence-splitting pass) overtook the smaller local edit, or because the offending sentence
was cut outright rather than reworded.

**Numbers rule (incoming table).** C25 numbers[1] (`household`) — fixed, entry removed (D2-13).
C26 numbers[0] — fixed, requoted to the Results running text with locator "Results", not the
non-existent "s.3.1" (D3-26). C26 numbers[1] (52) — fixed, now carries `derived: '42 in the
25-to-29.9 band plus 10 at 30 or more, Table 2, men'` (D3-7). C26 numbers[3]/[4] (86/74) — fixed,
unit now says "Abstract" where the quote is from (D3-26).

**D1 (C24).**
- D1-1 — fixed differently: rather than a `verified.note` flagging odds as unsourced, M3 supplies
  a real anchor (`openstax_contemporary_math`, s.7.7) and the definition now cites it.
- D1-2 — fixed. Reference 2 replaced with the counting-rule quote; sample-space, event and
  complement quotes added.
- D1-3 — fixed. Exercise answer says "of India's rural population"; practice (L9) answer adds the
  national-ceiling sentence.
- D1-4 — fixed, "odds of one mean half the time" language in place.
- D1-5 — fixed as specified (near-0/near-1 sentence rewritten; rare-events sentence cut).
- D1-6 — fixed differently: must_know[1] rewritten as specified, but the "barely different"
  clause in the illustration was cut outright rather than reworded to "already half as much
  again".
- D1-7 — fixed, practice (L6) answer now says the stretching grows near 1 and vanishes near 0.
- D1-8 — fixed, practice (L7) answer states odds and probability are equal only at zero.
- D1-9 — fixed, must_know rewritten to "three chances in four... three in four".
- D1-10 — fixed, must_know[2] cut; simplified_explanation ¶5 replaced.
- D1-11 — fixed differently: the proportion sentence opens `simplified_explanation`, split
  across three short sentences for M15 rather than the audit's one long sentence.
- D1-12 — fixed, retrieval_items[0].a now opens "When every outcome is equally likely,".
- D1-13 — fixed, `as_of` set to '2013' on both C24 entries (and C25's).
- D1-14 — fixed, the inverse-odds rule is derived by parts in the illustration before being
  stated; practice (L2) reuses the now-derived rule, which is normal practice-item use, not a
  fresh unsourced step.
- D1-15 — fixed, "P(A) is the p of the definition, for this particular event" added.
- D1-16 — fixed verbatim.
- D1-17 — fixed, the 5 kg/person/month figure quoted and registered in numbers[].
- D1-18 — fixed, "Suppose you read that the odds are two to one against" — invented district
  report removed.
- D1-19 — fixed, both superlatives replaced with "a common mistake" / "a common slip".

**D2 (C25).**
- D2-1 — fixed verbatim ("seven cases, 'all three' among them").
- D2-2 — fixed verbatim ("Two subtractions and two multiplications").
- D2-3 — fixed, reference 3 replaced with "assume they are dependent until you can show
  otherwise"; the mutually-exclusive quote added as reference 4; `verified.note` added.
- D2-4 — fixed, "rural residents" in place of "rural block"/"beneficiaries"; L10 answer adds the
  national-ceiling sentence.
- D2-5 — fixed, L10 prompt now picks one person and asks about their household of four.
- D2-6 — fixed, "beneficiaries" replaced with "rural residents".
- D2-7 — fixed, both P(A and B) and P(A or B) glossed in words at first use.
- D2-8 — fixed verbatim, the 2.25-is-a-different-question sentence added to the L8 answer.
- D2-9 — fixed, "change the chance of the other" in both the simplified explanation and the
  exercise answer; no remaining loose "odds" usage.
- D2-10 — fixed, hint replaced with "compare your answer with the previous problem's".
- D2-11 — fixed, the labelled "treating the two as independent" clause removed from the worked
  line.
- D2-12 — fixed, both items carry `refs: [nfsa_2013]`.
- D2-13 — fixed, the `household` entry removed from numbers[].
- D2-14 — fixed, the duplicate product-rule sentence removed.
- D2-15 — fixed verbatim.

**D3 (C26) — mostly superseded by M1's rebuild around the 42-vs-89 table.**
- D3-1 — fixed differently, by the stronger main-thread option: the illustration leads with the
  52-vs-79 failure (no whole count of 52 gives 86 per cent, none of 79 gives 74), then moves to
  the 42-vs-89 table (36/6/23/66) as the reconstruction, labelled throughout as rebuilt, not
  printed. Youden's index removed everywhere per the standing verdict.
- D3-2 — fixed, the "one person either way" claim replaced with the correct "no whole number of
  52 or 79 reproduces 86 and 74" statement.
- D3-3 — fixed differently: the correct rounding fact (0.8654 → 87, not 86) now appears as a
  diagnostic-band (L8) wrong-worked-answer per D3-17/M1, not as the old L6 applied answer, which
  no longer exists in that form.
- D3-4 — fixed with the new table's numbers: "fell by about a third, from 61 to 45 per cent,
  while the prevalence fell by more than half" (the old table's 68/45/40/20 figures are gone
  under M1).
- D3-5 — fixed per the Youden verdict: removed from the illustration, must_know (now "Divide
  back..."), and retrieval_items (now the divide-back check).
- D3-6 — fixed, using the paper's own row sums (71+114=185, 97+185=282, 97+186=283) rather than
  the wrong "rounding hides it" claim; relocated into the diagnostic band as a wrong-worked-answer
  (also serving D3-17).
- D3-7 — fixed, "Table 2 gives 42 men... and 10 more" plus a 42+10=52 working line; 52 registered
  as `derived`.
- D3-8 — fixed differently: the false "widest part of the upper arm" measurement-site sentence
  was cut in the M1 rewrite rather than corrected in place; no description of the measurement
  site remains in the illustration.
- D3-9 — fixed differently: the old 40 per cent / 34.8 per cent figures are gone under M1's
  rebuild (the new figures are 32 per cent among men, 61 and 45 per cent PPV); wherever a
  men-only share is now quoted it is labelled "among the 131 men".
- D3-10 — fixed, must_know rewritten to "belongs to the group tested, not to the test... itself
  an assumption"; the "travels reasonably well" sentence removed from the transfer answer.
- D3-11 — fixed, exercise answer now opens "Eighty-six per cent of what?", drops "general
  young-adult population" and "usually", and uses the new 32/61/45 figures.
- D3-12 — fixed, computed directly: 65 per cent among the 52-vs-79 group, 41 per cent at the
  study's own one-in-five planning figure, and the text-vs-table 82/71 discrepancy is named.
- D3-13 — fixed by rewriting to one consistent convention throughout (rows = test result,
  columns = condition), matching the paper's own tables, rather than transposing the old five
  tables in place — all tables in the rewritten record use this convention.
- D3-14 — fixed, `verified.note` on the contingency-table reference records that sensitivity,
  specificity, PPV and prevalence are defined in the record and not located in the anchor.
- D3-15 — fixed, "the study's own planning figure... before it measured anyone" replaces the
  "stand in for a wider population" claim.
- D3-16 — fixed: wherever 20 per cent appears it is now framed as the paper's own planning
  assumption from NFHS-4, never as a current population fact.
- D3-17 — fixed, all three diagnostic items (abdominal obesity 113/109, PBF 185/186, and the
  86-per-cent-of-52 rounding slip replacing the Youden problem) are now genuine wrong
  worked-answers with a named broken step.
- D3-18 — fixed, the transfer band is now a district officer's claim in words (L9, computes the
  PPV at a one-in-three share) and a neck-circumference claim in words (L10, computes 65 per cent
  and 41 per cent); the old line-for-line repeat item was cut rather than kept at L5.
- D3-19 — fixed, L5/L5 now use the women's arm row (46 vs 105) instead of repeating the
  illustration; exercises[1] now covers the women's body-fat cut-off inconsistency (28 vs 30 per
  cent) instead of duplicating the abdominal-obesity practice item.
- D3-20 — fixed, "higher percent body fat (PBF)" and "abdominal obesity — the paper's label for a
  waist of 90 cm or more in men and 80 cm or more in women" both glossed at first use.
- D3-21 — fixed, the negative predictive value is glossed in `simplified_explanation` before the
  practice item that uses it.
- D3-22 — fixed, `simplified_explanation` restates independence with a condition, and the
  invented 100-person table's first practice item now checks P(positive)=0.25 against
  P(positive|present)=0.75 and reports they are not independent.
- D3-23 — fixed, "identifies men with a body-mass index of 25 or more" and "people who truly
  have it" / "who truly do not have it" replace the condition-first constructions.
- D3-24 — fixed, "Four proportions, each a count divided by a total"; "denominator" introduced at
  first mention of the dividing total; "also called a contingency table" added at first use of
  two-way table. The informal "top count"/"bottom number" phrasing is kept alongside it elsewhere
  in the prose, which the fix did not ask to remove.
- D3-25 — fixed. `refs: [kiran_2022_muac_nc]` added not only to the two items the audit named but
  to every practice item quoting real Kiran figures (the women's-row discovery, both diagnostic
  items, and both transfer items), which the fix pass treated as the same defect recurring under
  M1's new item set.
- D3-26 — fixed, numbers[0] requoted to the Results text with locator "Results"; 42, 282 and 31.3
  are all registered; 0.60 (Youden) is not, since Youden's index does not stay.
- D3-27 — fixed differently: "simply" is not reintroduced; the whole prevalence passage was
  rewritten under M1 rather than edited in place.
- D3-28 — fixed, "It applies two rounded percentages to two counts" replaces "treat those two
  percentages as counts".
- D3-29 — fixed differently: the must-know list was rewritten under M1/D3-5 rather than
  relabelled in place; no point in the final list carries a `teaching` bearing where a
  `methodological` one belongs, and the surviving superlative ("the single commonest error") is
  gone, replaced by "a common error in reading a screening result".

**Youden's index** — removed from all three records (C24, C25, C26 all checked; zero hits).

**Odds (D1) verdict** — resolved by the D1 items above plus M3's new anchor; every remaining odds
sentence in C24 was re-checked against `openstax_contemporary_math` or against direct arithmetic.

**Warnings, before and after.** The audit's own count (`DECISIONS-part-D-fix.md` M15) was 99
sentence-length/reading-grade warnings across C24, C25 and C26 combined at the draft this audit
reviewed. After the fix pass, `check/build.py --check` reports 0 blocking lines and 0 warnings on
all three records (C24, C25, C26); the corpus-wide run reports 0 blocking and 49 warnings total,
none of them naming C24, C25 or C26. Arithmetic (`check_arithmetic`) and quotes (`check_quotes`)
were also checked in isolation for all three records and returned no errors and no missing
quotes.

**Not fixed.** Nothing in this batch was left unfixed. Two items outside this pass's scope are
carried forward as the audit itself flagged them, not as open defects: the pre-release re-check
of NFSA s.3(2)/s.9 against the current India Code consolidation (D1-13), and obtaining India-specific
BMI cut-point guidance before any sentence could treat 25 as India's own line (D3-16) — the record
does not make that claim now, so nothing needs to change until that source exists.
