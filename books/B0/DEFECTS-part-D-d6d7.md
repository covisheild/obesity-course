# Defects · Book 0 Part D, D6–D7 (B0-R0-C29, B0-R0-C30)

Step 3 audit, 23 September 2026. Audited against `sources/openstax_intro_stats_2e.txt`,
`sources/jcgm_vim3.txt` and `sources/kiran_2022_muac_nc.txt` (resolved through `sources/INDEX.yml`),
`prose/GLOSSARY.md`, records C01–C28, `books/B0/INVENTORY-part-D.md` and `READY-part-D.md`. The
drafter's notes (`draft-notes-part-D-D6D7.md`) were checked as claims, not taken as facts. No record
was edited.

## What was checked and held

These checks came back clean. They are listed so the fix pass does not redo them.

- **Quotes.** All 17 `quote` strings, 14 in C29 and 3 in C30, are in the mapped files word for word
  once whitespace is normalised. `python3 check/build.py --check`, run on a scratch copy, gives 0
  blocking and no warning naming C29 or C30.
- **VIM quotations inside the prose.** These are the ones the build does not check. Each was
  compared with `jcgm_vim3.txt` and is verbatim, with the right entry number: 2.14, 2.15, 2.16,
  2.17 ("remains constant or varies in a predictable manner"), 2.19 ("varies in an unpredictable
  manner") and 4.14. Entry 2.13 is quoted accurately but cut short without saying so (D7-8). Entry
  2.18 is paraphrased correctly. Entry 4.28 (zero error) is paraphrased without its entry number.
  No word attributed to the VIM is missing from the file.
- **Kiran figures.** These match the file:
  - 282 participants, planned and enrolled;
  - 20% "according to NFHS-4";
  - absolute error 5% and 10% non-enrolment;
  - 83 in the 25–29.9 band and 15 at 30 or more (Table 2), so 98/282 = 0.34752;
  - men's body-mass-index standard deviation 3.9 (Table 1), for 131 men.

  The planned 282 can be rebuilt from the paper's own inputs: 2² × 0.2 × 0.8 ÷ 0.05² = 256, and
  256 × 1.1 = 281.6. The record makes no claim about that calculation.
- **Practice arithmetic, recomputed in Python.** C29 and C30 are correct on every line. The C29
  answers checked were:
  - L1 5;
  - L2 2 and 1;
  - L3 25;
  - L4 0.78;
  - L5 √131 = 11.4455, 0.3407, 0.17035;
  - L6 39, 1521;
  - L7 14.142, 3.5355, 71%;
  - L9 0.3475;
  - L10 44.7214, 0.8944, 1414.2136, 0.0283, and a factor of about 31.6.

  The C30 answers checked were:
  - L1 −6;
  - L2 3, 2, 4, 1, 5;
  - L3 mean 3 and range 4, then mean −0.6 and range 9;
  - L4 1.5 and 0.3;
  - L5 0.2, 0.04 and 1.2;
  - L7 60.0.

  The eight-number population works out correctly too: mean 5, squared deviations summing to 32,
  population standard deviation 2. The three hand samples are also correct: sums 18, 15, 17 and
  means 4.5, 3.75, 4.25.
- **D7 scales.** Scale A has 20 readings summing to 1210.0, mean 60.5 and error +0.5. Scale B has
  20 readings summing to 1198.5, mean 59.925, error −0.075, minimum 58.7 and maximum 60.7. Both
  sets can be regenerated with Python's `random.gauss`: A as (60.5, 0.05) with seed 42, B as (60.0,
  0.55) with seed 99. The notes give the seeds but not the spreads, so "reproducible from the
  stated seeds" is true only once the spreads are added.
- **Scope.** The square-root law is stated, shown and not derived. No normal curve, confidence
  interval or z-score is named, but see D6-6 for one that comes in unnamed. NFHS, VIM and DEXA are
  expanded at first use. The "accuracy of 100 g" sentence is quoted exactly.

---

## D6 · B0-R0-C29 · Sampling

### Sourcing and arithmetic errors

**D6-1** · `illustration.body`, `must_know[2]`, `practice[7]` (L8) answer, `practice[8]` (L9) answer · **error**
- *Claim.* "The sample's own statistic came out higher than the population figure it was meant to
  estimate." The 14.8-point gap "points at who was sampled, not at how many" and at "who was
  recruited". The illustration adds that four times the invitation "would not move that answer one
  step closer to the young adults of India".
- *Source.* The sample was never meant to estimate the NFHS figure. The paper's objective was "to
  determine the optimum cut-offs of MUAC and NC … in young adults". The 20% was an assumed
  prevalence used to size the study ("We calculated sample size using single proportion formula
  and considered the prevalence of overweight as 20% according to NFHS-4"). The paper's stated
  population is "young adults studying in a medical college". It does not claim to represent
  India.
- *What the source leaves open.* Nothing in the file separates volunteer selection from at least
  four other explanations of the gap, and all four are visible in the same file:
  1. Medical students are a different population from all Indian adults.
  2. The dates differ. NFHS-4 is 2015–16, the study was run July–September 2019, and NFHS-5
     (2019–21) is higher (D6-3).
  3. The definitions may differ. The record compares "25 or more" with NFHS "overweight", and the
     paper's abstract counts only 83 as overweight (D6-4).
  4. 20 is the authors' rounded planning value (D6-2).

  Saying which of these produced the gap is asserting a cause without a source.
- *Fix.* Drop "it was meant to estimate". Recast the 20% as a figure for a bigger, different
  population, used only to plan the sample size. In `must_know[2]` and the L8 answer, replace
  "points at who was sampled / recruited, not how many" with: "Size cannot tell you which of these
  produced the gap: a different population, a different year, a different definition, or who chose
  to come forward." That still teaches the section's point that size cannot fix bias, and it no
  longer asserts a cause.

**D6-2** · `illustration.body`, `illustration.analogy_breaks_when`, L8 answer · **error**
- *Claim.* NFHS-4's figure "was a prevalence of overweight of 20 per cent among young Indian
  adults". The record then calls it "the true 20 per cent" and says it is "the country whose young
  adults the 20 per cent figure describes".
- *Source.* The paper gives NFHS-4 as "19% in men and 21% in women" for "India". It names no age
  group. The 20 is the authors' planning value, not a figure NFHS printed. An NFHS figure is itself
  a survey estimate, so it is a statistic and not a parameter. A section that teaches the
  difference between the two calls it "true".
- *Fix.* Write "a planning figure of 20 per cent, which the authors took from NFHS-4's 19 per cent
  for men and 21 per cent for women". Delete "young" wherever it qualifies the NFHS population.
  Replace "the true 20 per cent" with "the survey's 20 per cent". Add one sentence: "NFHS is itself
  a sample survey, so its figure is an estimate too."

**D6-3** · `illustration.body`, `must_know[2]`, L8, L9 · **error (currency)**
- *Claim.* The record uses the NFHS-4 20% as the national figure and never says when it was
  measured.
- *Source.* The same file says: "(NFHS-4, 2015–16) and this has increased to 22.9% in men and 24%
  in women in NFHS—5 (2019–21)." The study ran July–September 2019.
- *Fix.* Date NFHS-4 (2015–16) at first mention. Add: "The next round, NFHS-5 (2019–21), found
  22.9 per cent in men and 24 per cent in women." Quote that sentence in `illustration.numbers`.

**D6-4** · `illustration.numbers` (value 83) · **error**
- *Claim.* 83 is "of the 282 students, with a body-mass index of 25 to 29.9 (overweight band,
  Table 2)", quoted as `83 (29.4%) were overweight`.
- *Source.* That string occurs once, in the **abstract**. The abstract's own first paragraph defines
  overweight as "BMI ≥25 kg/m2". The quote therefore says 83 people had an index of 25 or more,
  which is not the band the unit claims. Table 2 puts 83 at 25–29.9 and 15 at 30 or more. The paper
  contradicts itself here. Anyone who opens the abstract reads that 29.4% were overweight, not 34.8%.
  This is a seventh inconsistency, and the source file's header lists only six.
- *Fix.* Quote the Table 2 row instead: `Overweight (25–29.9 kg/m2) 83 (29.4)`. Add one sentence to
  the illustration: "The abstract gives 83, 29.4 per cent, as 'overweight'. Table 2 shows another 15
  at 30 or more, so 98 have an index of 25 or more." Tell the main thread to add the item to the
  source file's header, since only the main thread may edit it.

**D6-5** · `illustration.numbers`, `must_know[2]` · **error (numbers rule)**

Each entry was checked against the new rule that a quote must state its own number:

| Entry | States its number? | Carries the claim? |
| --- | --- | --- |
| 20 | yes | the value, yes; the population description, no (D6-2) |
| 282 | yes | "planned" yes. "Enrolled" needs `We enrolled 282 medical students`. |
| 83 | yes | **no**: the quote defines the band as 25 or more, not 25–29.9 (D6-4) |
| 15 | yes (`Obese (≥30 kg/m2) 15 (5.3)`, a flattened table row) | yes |

**Missing entries, all of them derived and none marked as derived:**
- **98**, computed as 83 + 15;
- **34.8 per cent**, computed as 98 ÷ 282. The paper never prints it. `must_know[2]` cites
  `kiran_2022_muac_nc` for "34.8 per cent" as if the paper stated it.
- **5,000, 0.633 and 0.317**, which are simulation outputs;
- **14.8 or "fifteen" percentage points**, computed as 34.8 − 20.

*Fix.* Add each of these as an entry marked derived, with its method: "83 plus 15 from Table 2",
"98 divided by 282", "34.8 minus 20", and "simulation, Python `random`, seed 110" (see D6-13). In
`must_know[2]`, write "worked out from Table 2 as 34.8 per cent".

**D6-6** · `must_know[2]`, L8 answer, L9 answer, `illustration.body` · **error**
- *Claim.* "Fifteen percentage points is far more than sampling variation at this sample size could
  plausibly produce". "Sampling variation at this sample size is far too small to explain a gap that
  size". "The square-root law says sampling variation alone is very unlikely to produce a gap this
  large". The record also says a random 282 "already sits fairly close to the true 20 per cent".
- *What the arithmetic says.* None of this is computed in the record, and the reader cannot compute
  it. It needs the spread of a yes/no proportion, √(p(1−p)/n) = √(0.2 × 0.8 ÷ 282) = 0.0238, which
  puts the gap at about 6.2 of those spreads. Neither that formula nor the idea that a proportion is
  an average of 0s and 1s is taught in D5 or D6. "Very unlikely" and "plausibly" are judgements
  about tail probability, which belong to the normal curve, and the inventory keeps that for S03.
  In a transfer problem (L9), the one step that would support the answer is skipped.
- *Fix.* Delete the likelihood sentences. Keep only what the square-root law can support: "a
  bigger sample shrinks the scatter; it cannot say what caused a gap". If a size comparison is
  wanted, teach the proportion's spread explicitly and show the working, but the inventory places
  that beyond D6.

**D6-7** · L8 answer · **error**
- *Claim.* "The first two lines are just the study's own reported numbers."
- *Source.* Line 1's "98 of 282, 34.8%" is not reported anywhere in the paper; it is worked out from
  Table 2, and the abstract says 29.4%. Line 2's "NFHS-4 gives 20% for young adults nationally" is
  not reported either: the paper gives 19% and 21% with no age group. So the answer vouches for two
  wrong lines inside a problem that is meant to diagnose a wrong worked answer.
- *Fix.* Write: "Line 1 is worked out from Table 2 and is right. Line 2 is loose: the paper gives
  19 and 21 per cent for all adults, and the authors rounded to 20 for planning." Or make line 2
  one of the planted errors.

**D6-8** · L6 answer · **error**
- *Claim.* "That is because the sample size has to be squared to get there."
- *Arithmetic.* The sample size is never squared. It grows with the square of the factor by which
  the spread shrinks. Going from 0.3407 to 0.1 shrinks the spread 3.41 times. 3.41² = 11.61, and
  131 × 11.61 = 1,521.
- *Fix.* Replace the sentence with: "To shrink the spread 3.4 times you need 3.4 × 3.4, about 11.6
  times as many people: 131 × 11.6 is about 1,521." Show that line in a working block.

**D6-9** · L5 prompt and answer · **error**
- *Claim.* The prompt says Kiran "actually measured 131 men". The answer gives "a spread of about
  0.34 kg/m² around whatever the true average is for the population these 131 men were drawn
  from".
- *The problem.* The 131 men volunteered. They were not drawn at random from any population. The
  section's own boundary point says the law "describes only how a random sample's answer scatters".
  L5 teaches exactly the misuse the section warns against. It also feeds in 3.9, which is a sample
  standard deviation (divided by n − 1 under D5's rule), as the population spread without saying
  so. L4 handles this correctly with "suppose … a population with that same spread". L6 reuses 3.9
  as "a population's spread" with no `refs` and no "suppose".
- *Fix.* Change the L5 prompt to: "Suppose a random sample of 131 men is drawn from a population
  whose spread is 3.9 kg/m², the figure Kiran and colleagues report." Put "Suppose" into L6 and add
  `refs: kiran_2022_muac_nc`.

**D6-10** · L10 prompt and answer · **error (sourcing)**
- *Claim.* "a country of more than 1.4 billion".
- *Source.* No file in `sources/` holds a population figure, and the problem carries no `refs`.
  §7a says real figures or none. The answer also never makes the point the record's own reference
  supports, "population size is not a factor in determining the sample size" (OpenStax 1.2).
  Population size does not appear anywhere in the square-root law.
- *Fix.* Change the prompt to "a country of well over a billion people", or bare "a whole
  country". Add to the answer: "Notice that the country's size appears nowhere in the working. The
  spread of a random sample's average depends on the sample's size, not on the population's."

**D6-11** · `illustration.body` · **error**
- *Claim.* "They chose to volunteer, which makes this a convenience sample."
- *Source.* The anchor names that as a different problem: "Self-selected samples: Responses only by
  people who choose to respond … are often unreliable" (1.2). Convenience sampling is "using results
  that are readily available." The Kiran sample is both: one convenient college, and students who
  chose to come forward. The reason the record gives is the anchor's definition of self-selection.
- *Fix.* Write: "They chose to come forward, which the anchor calls a self-selected sample, from the
  one college that was convenient to the researchers. Either way, nobody drew them by chance."

**D6-12** · `illustration.analogy_breaks_when`, paragraph 2 · **error (minor)**
- *Claim.* "Most surveys of one village or one ward work this way, because the whole population
  there is small and fully counted."
- *Problem.* "Most" has no source. The reason is also wrong. A population that is fully counted is
  a census, not a sample. Surveys draw without replacement whatever the population's size. What
  smallness changes is how much that matters: "becomes a mathematical issue only when the
  population is small" (anchor, 1.2).
- *Fix.* Write: "Real surveys never ask the same person twice, so they sample without replacement.
  That matters only when the sample is a large share of a small population, such as one village.
  There the scatter is a little less than the law predicts."

**D6-13** · `illustration.body` (the simulation) · **style**
- *Result of rerunning it.* 5,000 samples of 10, then 5,000 of 40, with replacement, from 2, 4,
  4, 4, 5, 5, 7, 9, seed 110:

| Generator | Spread, samples of 10 | Spread, samples of 40 |
| --- | --- | --- |
| Python `random`: `random.seed(110)`, one `random.choice` per draw, the 10s then the 40s from one stream | **0.63304** | **0.31652** |
| numpy `default_rng(110)`, `choice`, any of the orderings tried | 0.6228 | 0.3188 |
| numpy legacy `np.random.seed(110)` | 0.6329 | 0.3181 |
| Python `random.choices(k=…)` | 0.6445 | 0.3165 |

  The stated 0.633 and 0.317 are reproduced **only by the Python `random` module with one
  `random.choice` per draw**. numpy's default generator does not reproduce them. Dividing the
  spread of the 5,000 means by 5,000 or by 4,999 makes no difference to three places.
- *Consistency of "spread".* Consistent. The record takes the population spread as 2, dividing by
  8, and says why ("the whole population, not a sample from it"). That is D5's population rule.
  The theory values are 2 ÷ √10 = 0.6325 and 2 ÷ √40 = 0.3162, and the simulation matches them. With
  D5's sample rule (÷ 7 gives 2.138) the theory would be 0.676 and 0.338, and the simulation does
  not match those. The only gap is that the record never shows 2 ÷ √10 or 2 ÷ √40, so the reader sees
  the ratio halve but never sees the simulation agree with the law directly.
- *Fix.* Add a working block with "2 divided by the square root of 10 = 0.632" and "2 divided by the
  square root of 40 = 0.316". Write the generator, the seed and the draw method into the record,
  not only the notes, because the figure has to read its numbers from the record.

**D6-14** · `definition.references` · **style (sourcing)**
- The quote "population size is not a factor in determining the sample size" backs no sentence in
  `definition.text`. The definition never mentions population size. Either add the sentence or
  move the reference to L10.
- The quote "is called the standard error of the mean" is a fragment with no subject. In the file
  it follows a formula the text extraction lost (7.1). The file header says to quote running prose,
  never a formula. Use 1.2 instead: "The standard error of the mean is an example of a standard
  error. It is a special standard deviation and is known as the standard deviation of the sampling
  distribution of the mean."
- The quote "for a biased sampling technique, even a large sample runs the risk of not being
  representative" backs "runs the risk". The definition says the gap "is fixed" and enlarging
  "does not close" it. The anchor supports the stronger reading at 1.2: "Be aware that many large
  samples are biased." It also defines sampling bias ("a sampling bias is created when … some
  members of the population are not as likely to be chosen as others"). Quote those.

### Floor

**D6-15** · whole record · **floor**
- *Claim.* The record uses "a biased one" (`must_know[0]`) and "a biased sample" (retrieval 3).
  D7 then leans on "the same word this book has already used for a biased sample" and on "Sampling
  bias, from the section before this one".
- *Problem.* D6 never defines *bias* or *sampling bias*, and no record C01–C28 does either. The
  inventory's risk list requires the glossary row, or D7, to cover both senses. The draft notes'
  glossary table has no *sampling bias* row.
- *Fix.* Add one sentence to `definition.text`: "When some members of the population are more
  likely to be chosen than others, the sample has a sampling bias." Quote the anchor's 1.2 sentence.
  Add a *bias* row to the glossary inbox that covers both senses.

**D6-16** · `definition.text`, `simplified_explanation`, `illustration.body` · **floor (define or point)**
- *Claim.* "Spread" is used throughout and tied to "standard deviation" only once, in brackets in
  the L1 prompt.
- *Problem.* D5 also calls the interquartile range a spread ("describes the spread of the middle
  half"). The square-root law holds for the standard deviation only.
- *Fix.* At first use in `definition.text`, write: "its spread, meaning its standard deviation as
  the section on average and spread taught it".

**D6-17** · `illustration.body`, L9 answer · **floor (an equation without its sentence)**
- `83 plus 15 = 98` comes before any words saying what 83 and 15 are. Nowhere in the prose, nor in
  the L9 answer, is the reader told that 83 had an index of 25 to 29.9 and 15 had 30 or more. The
  two numbers appear from nowhere.
- `2 divided by 2 = 1` follows "the square-root law says how big it typically is". The sentence
  does not say that one 2 is the population's spread and the other is the square root of 4.
- *Fix.* Put these sentences before the working: "Table 2 puts 83 students at an index of 25 to
  29.9 and 15 at 30 or more. Add them." And: "Divide the population's spread, 2, by the square root
  of 4, which is 2."

### Style, ladder and must-know

**D6-18** · practice prompts · **style (hint in the prompt)**
- L1 names the method ("using the square-root law").
- L5 says "without working out a second square root", with 524 = 4 × 131, which hands over the
  shortcut.
- *Fix.* Delete both phrases. In L5, ask for the spread at 524 directly and let the reader find the
  shortcut.

**D6-19** · L8, L9 · **style (§7a: the prompt is solved in the text)**
- The illustration already works L8's "tempting next line" (1,128 volunteers). It also computes
  83 + 15 and argues the same conclusion. L9 then reruns the same arithmetic. The diagnostic
  problem is answered on the page before it.
- *Fix.* Give L8 a different broken step, such as the standard deviation and standard error mix-up
  in D6-25. Or cut the 1,128 paragraph from the illustration.

**D6-20** · `simplified_explanation`, `illustration.body` · **style**
- *Claim.* "That is the only time this book uses that name" and "This book uses that name once,
  here".
- *Problem.* "Standard error of the mean" appears three times in the record: in the definition, in
  the simplified explanation and in the illustration.
- *Fix.* Keep the definition's use and delete both "only once" sentences.

**D6-21** · `must_know` · **style**
- Points 2, 5 and 6 carry one move three times: ask how the sample was chosen before asking how
  big it is. Point 7 carries it again for teaching. That is padding (§5).
- Point 3 is tagged `bearing: clinical`, but nothing in it changes what anyone does with a patient.
  It is `methodological`. It also needs rewriting under D6-1 and D6-6.
- The one number that changes a study design is missing: four times the people for half the
  spread, so every halving costs four times as many.
- *Fix.* Merge 2, 5 and 6 into one point. Retag point 3. Add a `number` point for the four-times
  rule.

**D6-22** · L9 · **style (§9)**
- The prompt's line, "medical students are far more overweight", describes people by a weight
  adjective. It is fine as a claim for the reader to take apart. The answer never rewrites it,
  though, and uses "run heavier" itself.
- *Fix.* Add one line to the answer: "Said carefully: a larger share of these students had a
  body-mass index of 25 or more." Use that form in place of "run heavier".

**D6-23** · `simplified_explanation`, `definition.text`, `illustration.body` · **style (loose claims)**
- "Sampling variation shrinks … by a fixed amount". It shrinks by a fixed rule, in proportion. It
  does not shrink by an amount.
- "How good that guess is depends entirely on how the sample was put together". Size matters too,
  and that is the section's own point.
- "a bigger convenience sample is a more confident wrong answer". The anchor says convenience
  results "may be very good in some cases and highly biased in others". Say "possibly wrong answer,
  and size cannot tell you which".
- "the study already used in the two sections before this one". It was used in three: D3, D4 and
  D5.

**D6-24** · `provenance.bridge_ref` · **style (the build warns)**
- The field is empty. The inventory's bridge table names D6 for S03 rung 1 (parameter, statistic,
  estimate) and S03 rung 2 (the sampling distribution as something the reader has seen).
- The draft notes misreport that table as naming "confidence-interval material". It does not.
- *Fix.* Fill both entries, or record who decided to defer them.

**D6-25** · `practice` · **style (a failure mode the ladder misses)**
- Ten problems across 3, 3, 2 and 2 do climb all four bands. The one failure a reader will meet
  weekly is missing, though: **confusing the standard deviation with the standard error**.
- Problem suggested for level 7: a colleague writes that since the men's mean body-mass index is
  24.2 with a standard deviation of 3.9, "the true mean for these men lies between 20.3 and 28.1".
  The broken step is reading the spread of people as the uncertainty in the average.
- The reverse mistake is a table printing mean ± standard error so that the people look alike.
  That also connects back to D5, where the average is not the person.
- *Fix.* Add this as an eleventh problem, within the 10–12 the inventory expected.

---

## D7 · B0-R0-C30 · Random and systematic error

### Sourcing and arithmetic errors

**D7-1** · `illustration.body` (last paragraph), `must_know[5]` · **error**
- *Claim.* "The paper also names dual energy X-ray absorptiometry, DEXA, as the gold standard for
  measuring body fat, while using bioimpedance instead." The must-know point builds on that: "A
  paper may measure something with one method while naming a different method the gold standard."
- *Source.* "The gold standard to assess ‘fatness’ or PBF is by dual energy X-Ray absorptiometry
  scan (DEXA Scan) **and body composition analysis using BIA machines**." The introduction groups
  them the same way: "more accurate research grade methods … include body composition using BIA
  and DEXA". The limitations section calls the authors' own bioimpedance reference "the gold
  standard based on body-composition".
- *Why it matters.* The paper does not name a different method from the one it used. The record's
  contrast also implies that bioimpedance is the lesser method, which is a claim about direction
  that no held source makes. The inventory's brief has the same misreading ("the method it names as
  the gold standard"), and the drafter followed it.
- *Fix.* Delete the DEXA paragraph and `must_know[5]`. If the point is kept, it has to be what the
  paper actually says: "The paper calls both DEXA and bioimpedance the gold standard, and reports
  no comparison between them or against anything else." Correct the inventory's D7 row too.

**D7-2** · `illustration.body`, `simplified_explanation`, `exercises[1]`, L9 answer, `must_know[6]` · **error**
- *Claim.* Scale A "sits further from the truth on average than scale B ever does". The record also
  says:
  - "accurate on average without being especially precise";
  - "The loose, centred scatter is accurate on average but not precise";
  - "A small average error, close to zero … supports the new scale being more accurate";
  - "How close is that agreement to the truth? That is accuracy."
- *The VIM.* That average-closeness is **trueness**, entry 2.14. The record quotes 2.14 and then
  calls it accuracy. The VIM forbids exactly that. 2.13 Note 2 says "measurement accuracy" should
  not be used for measurement trueness. 2.14 Note 3 says "Measurement accuracy" should not be used
  for "measurement trueness". 2.13 Note 1 says "more accurate when it offers a smaller measurement
  error", which is per reading.
- *Arithmetic.* Reading by reading, scale B is **not** more accurate:

| | Error range (kg) | Mean distance from 60.0 (kg) | Root-mean-square error (kg) | Readings more than 0.5 off |
| --- | --- | --- | --- | --- |
| Scale A | 0.4 to 0.6 | 0.500 | 0.502 | 2 |
| Scale B | −1.3 to 0.7 | 0.425 | 0.507 | 6 |

  "Than scale B ever does" is false. B's 58.7 is 1.3 kg from the truth.
- *Fix.* In each place listed, "accurate on average" becomes "true on average, which the VIM calls
  trueness". Rewrite the sentence as: "Yet its average sits further from the truth than scale B's
  average does." Add: "Accuracy, for one reading, needs both: small scatter and no push." Keep the
  target drawing in the teaching exercise and label the loose, centred target "true, not precise".

**D7-3** · `illustration.body` · **error**
- "Scale A's twenty readings … sit inside a tenth of a kilogram of each other." The readings run
  from 60.4 to 60.6, so the largest gap between two readings is **0.2** kg. The statement holds
  only for each reading's distance from the mean.
- Scale B's average is "within a tenth of a kilogram of the true 60.0, even though no single reading
  landed that close". **Two readings are exactly 60.0**, the 5th and the 12th.
- "That is fine resolution and tight agreement between repeats". Readings that cluster tell you
  nothing about resolution. On a display that steps in 0.1 kg, tight readings can be the display
  hiding scatter smaller than one step. That mix-up is the one this section exists to prevent.
- *Fix.* Change the first to "within a tenth of a kilogram of their own average". Change the second
  to "even though most single readings landed further away". Delete "fine resolution and".

**D7-4** · `illustration.body` · **error (stated conditions not marked)**
- *Claim.* "This scale has a zero error: put nothing on it and it would already read 0.5
  kilograms."
- *Problem.* Readings at a single load of 60 kg cannot tell a zero error apart from an error that
  grows with load. The record's own `analogy_breaks_when` says "An instrument that reads true at 60
  kilograms can drift at 120." A zero error is a condition the author sets, not a conclusion from
  these readings. The kitchen scale in the simplified explanation is marked correctly with "Say".
  This one is not.
- *Fix.* Write: "Say the cause is a zero error, so that with nothing on it the scale already reads
  0.5 kilograms. These twenty readings, all at one weight, could not show that by themselves."

**D7-5** · `illustration.body` paragraph 2, L8 answer, `must_know[2]` · **error**
- *Claim.* A hundred grams "is the smallest change the scale's display can show, which is exactly
  what resolution (VIM 4.14) means. … So the true sentence is that the scale's resolution was 100
  grams." In L8: "A figure given as '100 g' in a methods section is a resolution (VIM 4.14) … That
  is true even with no comparison."
- *Source.*
  - The paper says only that weight was "recorded with accuracy of 100 g". That is the step the
    readings were **recorded** in. It does not state the scale's resolution.
  - VIM 4.14 is "smallest change in a quantity being measured that causes a perceptible change in
    the corresponding indication". Its Note says resolution "can depend on … noise … or friction".
    It is therefore not the display step, which is resolution of a displaying device, VIM 4.15, not
    held.
  - L8's general rule is false. A figure in grams can be a genuine accuracy specification. What
    tells the reader which kind this one is: the wording "recorded with", and the absence of any
    check against a known weight.
- The distinction from accuracy is right and should stay.
- *Fix.* Illustration: "A hundred grams is the step the weights were written down in. No reading can
  show a change smaller than that, which is a statement about resolution (VIM 4.14). It is not a
  measured closeness to a true value." In L8: "Here, 'recorded with' and the lack of any check
  against a known weight make it a recording step. A figure in grams is not a resolution just
  because it is in grams." In `must_know[2]`, change "Very often" to "Often".

**D7-6** · L6 prompt · **error (misquote)**
- *Claim.* "Kiran and colleagues state that weight was recorded with a resolution of 100 g."
- *Source.* They say "accuracy". The prompt puts the record's own reading into the authors' words,
  a problem away from L8, which turns on exactly that wording. It also attaches an invented student
  reading (68.3 kg against 68.0 kg) to the real scale, under `refs: kiran_2022_muac_nc`.
- *Fix.* Write: "Kiran and colleagues' scale recorded weight in steps of 100 g. Suppose one
  student's weight is recorded as 68.3 kg and a reference scale gives 68.0 kg."

**D7-7** · `definition.references` · **error (sourcing)**
- *Claim.* The two OpenStax quotes are "The actual process of sampling causes sampling errors" and
  "A defective counting device can cause a nonsampling error".
- *Problem.* They back no sentence in `definition.text`. The definition never mentions sampling
  error, nonsampling error or a faulty device. The OpenStax file has nothing on systematic or random
  measurement error. A search for "measurement error", "systematic" and "random error" finds only
  sampling methods. So the definition carries references that do not support it.
- *Fix.* Add the sentence those quotes do support: "Some error has nothing to do with how the sample
  was drawn. A faulty instrument is one source: the anchor calls this a nonsampling error." That
  also links D7 back to D6.

**D7-8** · `definition.text` (VIM quotations) · **style (accuracy of quotation)**
- VIM 2.13 is quoted as "closeness of agreement between a measured quantity value and a true quantity
  value". The VIM continues "**of a measurand**". The words are in the file, but the quotation stops
  in the middle of the definition and does not say so.
- 2.16 is introduced as the VIM giving "this in its own words", after the record's "minus the value
  that is actually true". The VIM's words are "a **reference** quantity value", and its Note 1 says
  why that matters.
- The zero error in the simplified explanation paraphrases VIM 4.28 and gives no entry number.
- Every other VIM quotation is verbatim, with the right entry number.
- *Fix.* Add "…" or "of the thing being measured" to 2.13. Write "the value that is actually true,
  or in practice a trusted reference value" before 2.16. Name 4.28 beside "zero error".

**D7-9** · `must_know[].refs`, `practice[].refs` · **style (sourcing)**
- *The notes' claim.* `jcgm_vim3` is attached to "four of the seven" must-know points.
- *The record.* It is attached to **two**: points 2 and 3. Point 4 cites "VIM 2.15" in words with no
  `refs`. The L9 answer cites VIM 4.14 and 2.13 with no `refs`. Only L8 carries the key among the
  practice problems. So the VIM reaches the reader's reference list only through three places.
- *Fix.* Add `jcgm_vim3` to `must_know[3]` and to L9.

**D7-10** · L7 answer · **error (diagnostic logic)**
- *Claim.* "The step that broke is the third line." The same answer then says "'averaging reduces
  error' is a true and useful rule, and it is stated correctly in the third line." It then says:
  "The true weight is 60.0 kg."
- *Problem.* The answer names a line as broken and then calls it correct. What 60.5 − 0.5 gives is
  the corrected estimate, not the true weight. The average still carries some random error.
- *Fix.* Write: "Line 3 states a rule that is true of random error as if it held for all error. That
  is the break." And: "Corrected for the known zero error, the best estimate is 60.0 kg."

### Floor

**D7-11** · `definition.text`, `simplified_explanation` · **floor (glossary and order)**
- *Order.* The brief requires *precision* to arrive in the glossary's words and then be sharpened.
  In the rendered order, `definition.text` comes first and introduces precision in VIM 2.15's words
  ("Precision is about the size of the random error alone"). The glossary's words appear only after
  it, in the simplified explanation.
- *The claim about the book.* "This book already uses precision for how tightly a measurement pins
  the number down." Those words appear in **no** record from C01 to C29. C03 used *precision* for
  the number of digits a figure can defend ("a precision you can defend", "false precision"). That
  digits sense is what D7 now calls **resolution**. So the book's *precision* changes meaning
  without saying so, which is a term taught twice in different words.
- *Fix.* Open the precision paragraph in `definition.text` with the glossary's words. Add one sentence:
  "The section on significant figures used precision for how many digits a figure can defend. The
  VIM splits that idea: the digits an instrument can show are its resolution, and how closely its
  repeats agree is its precision." Report the glossary gap to the main thread, since the recorded
  words were never actually given to the reader.

**D7-12** · L3 and L5 answers · **floor (a move not taught)**
- *Claim.* L3 writes `-3 plus 4 plus -5 plus 2 plus -1 = -3` and `4 minus -5 = 9`. L5 writes
  `-0.6 plus 0.6 plus -0.1 …` and `0.6 minus -0.6 = 1.2`.
- *Problem.* No record from C01 to C28 adds a negative number or subtracts one. A search finds no
  "plus -" and no "minus -". Earlier records only produce negatives by subtracting and divide them.
- *Fix.* Add one line to L3's answer before the range: "Subtracting a negative number adds its size.
  On a number line, the distance from −5 up to 4 is 5 plus 4, which is 9."

**D7-13** · L5, `exercises[0]`, `illustration.body` · **floor (units and terms of art)**
- **°C**: no earlier record introduces degrees Celsius.
- **mmHg**: never introduced and never expanded.
- **bioimpedance**: never defined anywhere from C01 to C30.
- **calibration, calibrated**: used as a term of art ("badly calibrated instrument", "calibration
  weight") and never defined.
- **gold standard**: undefined, as well as misread (D7-1).
- *Fix.* Name the unit in words at first use: "degrees Celsius, written °C", and "millimetres of
  mercury, written mmHg, the unit blood pressure is read in". Give *calibrate* an inline dash
  definition: "checking an instrument against a weight or value already known to be right". The
  other two disappear if D7-1's fix deletes the paragraph.

**D7-14** · `definition.text`, `simplified_explanation`, `must_know[1]` · **floor (points at a definition that does not exist)**
- *Claim.* D7 ties sampling bias and measurement bias together as the inventory asks: "the same word
  for the same shape of problem". That part is done correctly.
- *Problem.* It points back at "the same word this book has already used for a biased sample" and at
  "Sampling bias, from the section before this one". D6 never defines either (D6-15).
- *Fix.* D6-15 fixes this. In D7, also name the anchor's sense in one clause: "a sample in which
  some members were more likely to be chosen than others".

### Style, ladder and currency

**D7-15** · `practice` · **style (§7a bands)**
- *Transfer band.* L9 ("There is nothing to compute") and L10 ("There is no arithmetic to run")
  compute nothing. §7a says the transfer reader "decides what to compute, computes it, and then says
  what the answer does not establish". A transfer band with no computation has not been climbed.
- *Mechanical band.* L3 sits at level 3 but asks for a mean, a range and an interpretation. That is
  applied work, not one step. L2 is L1's move repeated five times.
- *Fix.* L9: give the old scale's and the new scale's readings of a known 50.00 kg weight, the new
  one showing an extra decimal place. The reader computes both average errors and then says what
  the extra digit does not show. L10: give paired readings from two observers on the same five
  people. The reader computes the mean difference and says what one observer alone could not have
  shown. Move L3 to level 4.

**D7-16** · practice prompts · **style (hints, and prompts solved in the text)**
- L3 defines range inside the prompt ("the largest minus the smallest").
- L6 calls the figure "resolution" and asks whether it tells you, "on its own", which kind of error
  this is. That is the answer's shape.
- L10's parenthesis ("rightly call it a strength … minimum inter-observer variation") hands over
  both halves of the answer. It also calls Kiran's claim "something similar" to "no measurement
  error", which the paper does not say.
- L7 reruns the illustration's scale A (60.5, 0.5, 60.0), and L8 reruns the illustration's first
  paragraph. The illustration answers both diagnostic problems before the reader gets to them.
- *Fix.* Remove the definition from L3. Reword L6 as in D7-6. Cut L10's parenthesis to the bare
  quote. Change L7's numbers and instrument, for example a thermometer. For L8, use the paper's
  other misused word: "Neck circumference was measured … with 1 mm precision". That is real, it is
  in the file, and the illustration does not solve it.

**D7-17** · `simplified_explanation`, `must_know[2]` · **style (§1)**
- "Its error is simply what it says minus what is actually true" and "Resolution is simply the
  smallest step". §1 bans "simply" when it describes the very step being taught.
- "Very often that figure is really its resolution" is a claim about frequency with no source.
- *Fix.* Delete "simply" in both places. Change "Very often" to "Often".

**D7-18** · `illustration.body` · **style (§4: show every line)**
- `1210.0 divided by 20` and `1198.5 divided by 20` both appear with no sum shown. The reader has to
  add twenty numbers unseen. Both sums are correct.
- *Fix.* Add the sum line, or use a two-row subtotal, one per printed row: 604.9 + 605.1 = 1210.0 for A, and 598.5 + 600.0 = 1198.5 for B.

**D7-19** · `definition.text`, `simplified_explanation`, `must_know` · **style (a gap in what is taught)**
- The record says repeating the measurement cannot remove a systematic error. It never says what
  does: a **correction**. The source pack holds exactly this. VIM 2.17 Note 2 says "A correction can
  be applied to compensate for a known systematic measurement error", and entry 2.53 defines
  correction.
- L7 applies a correction (60.5 − 0.5) without naming it. As written, the reader leaves thinking
  bias cannot be fixed at all.
- *Fix.* Add one sentence and one move point: "Once a systematic error is known, subtract it. The
  VIM calls this a correction (2.53). Finding it out needs a known weight, not more readings."

**D7-20** · `illustration.body`, `must_know[4]`, L10 answer · **style**
- *Claim.* Differences between observers are "a real source of random error".
- *Problem.* Each observer's habit is a systematic error in that observer's readings. It only looks
  random across a pool of observers. The section's own point about the single observer is the same
  fact seen from the other side, and saying so makes the section tighter.
- *Fix.* Write: "Differences between observers are each observer's own systematic habit. Mixed
  across many observers, they scatter like random error. With one observer, they become one
  systematic error that reaches every reading."

**D7-21** · `exercises[0]` answer · **style (currency, unsourced)**
- *Claim.* "such as a properly calibrated mercury gauge".
- *Problem.* The record names a particular reference device with no source for it. Mercury blood
  pressure instruments are being phased out internationally. That was not checked against any held
  source, and it is exactly why the device should not be named without one.
- *Fix.* Write "a reference device already shown to be accurate".

**D7-22** · `definition.text` · **style (currency)**
- The prose says "the VIM" and never gives the edition. The source is the 3rd edition, JCGM
  200:2012, online version updated 29 April 2017. These meanings were decided by a body, and the
  record's review trigger (2031) ignores that a new edition could change them.
- *Fix.* Name "3rd edition, 2012" at first mention. Record "next VIM edition" as an event to review
  on.

**D7-23** · `provenance.bridge_ref` · **style (the build warns)**
- The field is empty. The inventory names D7 for S08 rung 1: error is not bias, and random against
  systematic on a weighing scale. The draft notes say the inventory names "classical/Berkson error"
  here. It does not. The inventory puts Berkson error in S08 rung 2, explicitly outside D7.
- *Fix.* Fill the entry, or record the decision to defer it.

**D7-24** · `practice` · **style (failure modes the ladder misses)**
- The notes asked whether a third failure mode exists for D7. Three do, and the record commits two
  of them itself (D7-2 and D7-3):
  1. **Trueness mistaken for accuracy.** A small average error is read as every reading being
     close.
  2. **A coarse display mistaken for precision.** Identical readings on a 100 g display look
     perfectly precise because the scatter is smaller than one step.
  3. **A correction applied the wrong way.** The error is taken as true minus measured, or a zero
     error is added instead of subtracted, which doubles it. This also drills the sign convention
     from L1.
- *Fix.* Add two problems at levels 7 and 8, taking the set to 12. That is within the inventory's
  10–12 and the build's 3–18.

---

## Verdicts

**B0-R0-C29 (D6).** The teaching of the square-root law is correct and well built. The definitions
quote the anchor accurately. Every practice sum is right. The simulation's 0.633 and 0.317 are
genuine, but only Python's `random` module reproduces them, not numpy's default generator. The
record uses "spread" consistently with D5's population rule. The section's use of real material
fails, though, and it fails in the place the inventory warned about. The record turns a planning
assumption into "the population figure it was meant to estimate". It describes NFHS-4's figure for
all adults as a "true" figure for "young Indian adults", in the section that teaches that a survey
figure is a statistic. It ignores the NFHS-5 figures sitting in the same source file. It attributes
the gap to volunteer selection with no source, backed by a "very unlikely" that the reader has no
tool to compute. Its own quote for 83 comes from an abstract that counts those 83 as the whole
group with an index of 25 or more, so a reader who opens the paper finds 29.4 per cent, not 34.8.
Fix D6-1 to D6-12 and define *bias* (D6-15) before this record is used. The ladder climbs properly
but needs a standard-deviation-against-standard-error problem.

**B0-R0-C30 (D7).** Every word the record attributes to the VIM is in the file, under the right
entry number, which was the main risk the build could not catch. The scale arithmetic is right.
The central contrast is wrong, though. Having quoted the VIM keeping accuracy and trueness apart
"on purpose", the record calls scale B's close average "accuracy". It says scale A sits further
from the truth than scale B "ever does", which the readings refute. It also misdescribes both
scales in ways the numbers contradict. It concludes a zero error that one load cannot show. It
misreads Kiran on the gold standard: the paper names bioimpedance alongside DEXA. It overstates the
100 g sentence as the scale's resolution, and L6 misquotes that sentence. Its definition references
support nothing in the definition. On the floor, *precision* arrives in VIM words before the
glossary's words, and those glossary words appear nowhere earlier in the book. Negative-number
moves, °C, mmHg, bioimpedance and calibration are all used untaught. Neither transfer problem
computes anything. With D7-1 to D7-7, D7-10 and D7-11 fixed, and a correction and two more
diagnostic problems added, it will do the job S08 rung 1 needs from it.

**Count.** 49 defects: 20 error, 7 floor, 22 style. D6 has 25 (12 error, 3 floor, 10 style) and D7
has 24 (8 error, 4 floor, 12 style).

---

## Resolution (fix pass)

Task 4 fix pass, 23 September 2026. `python3 check/build.py --check` gives 0 blocking and no
warning naming B0-R0-C29 or B0-R0-C30. Only these two records and this defects file were edited.

### D6 · B0-R0-C29

- D6-1 — fixed. Dropped "meant to estimate"; the four candidate explanations (different
  population, different year, different definition, who came forward) now stand side by side with
  no cause asserted, in the illustration, `must_know[2]` and the L8 answer.
- D6-2 — fixed. "Planning figure of 20 per cent" taken from NFHS-4's 19/21 per cent; "young"
  dropped from the NFHS population; "the true 20 per cent" replaced; NFHS named as itself a survey
  estimate.
- D6-3 — fixed. NFHS-4 dated 2015-16 at first mention; NFHS-5 (2019-21, 22.9/24 per cent) added and
  quoted in `illustration.numbers`.
- D6-4 — fixed. The 83 quote now comes from Table 2's row, not the abstract; a sentence explains
  the abstract's 29.4 per cent versus the 34.8 per cent built from Table 2's two bands.
- D6-5 — fixed. 98, 34.8%, 14.8 points, 0.633 and 0.317 are all registered in `illustration.numbers`
  with `derived:` fields stating the arithmetic or simulation method.
- D6-6 — fixed. "Very unlikely", "plausibly" and "already sits fairly close to the true 20 per
  cent" are removed; the record now says only that size shrinks scatter and cannot say what caused
  the gap.
- D6-7 — fixed. L8's answer now calls line 1 right (worked from Table 2) and line 2 loose (19/21
  per cent, all adults, rounded to 20 for planning), rather than vouching for both as "the study's
  own reported numbers".
- D6-8 — fixed. L6's answer now says the sample size is never squared; what is squared is the
  factor by which the spread must shrink (3.4 x 3.4 ~ 11.6; 131 x 11.6 ~ 1,521).
- D6-9 — fixed. L5's prompt now opens "Suppose a random sample of 131 men is drawn from a
  population whose spread is 3.9 kg/m2..."; L6 also carries "Suppose" and `refs: kiran_2022_muac_nc`.
- D6-10 — fixed. "1.4 billion" removed; the prompt now says "a country of more than a billion
  people" and the answer adds "the country's size appears nowhere in this working. The spread of a
  random sample's average depends on the sample's own size, not on the size of the population."
- D6-11 — fixed. Illustration now reads: "They chose to come forward, which the anchor calls a
  self-selected sample, from the one college that was convenient to the researchers. Either way,
  nobody drew them by chance."
- D6-12 — fixed. `analogy_breaks_when` now says real surveys sample without replacement, and that
  this matters only when the sample is a large share of a small population (a village), not that
  small populations are "fully counted".
- D6-13 — fixed. A working block shows 2/sqrt(10) = 0.6325 and 2/sqrt(40) = 0.3162 beside the
  simulated 0.633 and 0.317; the generator (Python's `random` module), the seed (110) and the draw
  order (10s then 40s, one continuous run) are stated in the record itself, not only in notes.
- D6-14 — fixed. The unsupported "population size is not a factor" quote now backs a sentence in
  L10's answer. The mis-cut "standard error of the mean" quote is replaced with the full sentence
  from s.2.7. New references were added for "Be aware that many large samples are biased" and the
  anchor's sampling-bias definition.
- D6-15 — fixed. `definition.text` adds: "When some members of the population are more likely to
  be chosen than others, the sample has a sampling bias," quoting the anchor's s.1.2 definition
  directly. (The glossary-inbox row is outside this record's files and was not added; noted for the
  main thread.)
- D6-16 — fixed. First use of "spread" in `definition.text` now reads "its spread, meaning its
  standard deviation as the section on average and spread taught it."
- D6-17 — fixed. Both working lines now have their sentence first: what 83 and 15 are (Table 2's
  two bands) before `83 plus 15 = 98`, and what the two 2s are before `2 divided by 2 = 1`.
- D6-18 — fixed. "using the square-root law" (L1) and "without working out a second square root"
  (L5) are both deleted.
- D6-19 — fixed differently. Rather than reworking L8's broken step, the illustration's "tempting
  next line" (1,128 volunteers) paragraph was cut entirely, so L8 and L9 are no longer pre-solved in
  the prose; a new, unrelated level-7 problem (standard deviation read as the spread of the mean)
  was added to strengthen the ladder per D6-25.
- D6-20 — fixed. Both "only once"/"only time this book uses that name" sentences are deleted.
- D6-21 — fixed. Points 2, 5 and 6 merged into one; the mistagged `bearing: clinical` point is now
  `methodological`; a new point states the four-times-people-for-half-spread rule.
- D6-22 — fixed. L9's answer adds: "Said carefully: a larger share of these students had a
  body-mass index of 25 or more," replacing "run heavier".
- D6-23 — fixed. "Shrinks by a fixed amount" -> "following a fixed rule rather than a fixed
  amount"; "depends entirely on how the sample was put together" -> "depends on" (with sample size
  addressed in the square-root-law paragraphs that follow, rather than merged into the same
  sentence — fixed differently on this point); "a more confident wrong answer" -> "a more confident
  answer that may or may not be right, and its size cannot tell you which"; "the two sections before
  this one" removed (no longer present).
- D6-24 — fixed. `provenance.bridge_ref` filled with the S03 rung 1 (parameter/statistic/estimate)
  and rung 2 (sampling distribution) entries from the inventory's bridge table.
- D6-25 — fixed. An eleventh problem, at level 7, has a colleague misreading a standard deviation
  of 3.9 as if it bounded "the true mean"; the answer separates the spread of individuals from the
  spread of an average.

### D7 · B0-R0-C30

- D7-1 — fixed. The DEXA/bioimpedance paragraph and `must_know[5]` are deleted entirely (the audit's
  offered alternative to rewriting them), which also removes the undefined "bioimpedance" and "gold
  standard" terms flagged in D7-13.
- D7-2 — fixed. Every "more accurate"/"accurate on average" claim about the scales is corrected to
  "true on average" / trueness (VIM 2.14); the illustration now says scale A's average sits further
  from the truth than scale B's; the teaching exercise's two targets are labelled "precise, not
  true" and "true, not precise"; `must_know[6]` and the rewritten L9 transfer problem both use
  trueness correctly.
- D7-3 — fixed. "Sit inside a tenth of a kilogram of each other" -> "within a tenth of a kilogram of
  their own average"; "no single reading landed that close" -> "even though most single readings
  landed further away" (two of Scale B's readings are exactly 60.0); "fine resolution and" deleted.
- D7-4 — fixed. The zero-error paragraph now opens "Say the cause is a zero error..." and adds "These
  twenty readings, all at one weight, could not show that by themselves," matching the record's own
  `analogy_breaks_when` caveat about a single load.
- D7-5 — fixed. Illustration now reads "A hundred grams is the step the weights were written down
  in... which is a statement about resolution (VIM 4.14). It is not a measured closeness to a true
  value." L8 (rewritten under D7-16, see below) drops the false "always a resolution" generalisation.
  `must_know[2]` changes "Very often" to "Often".
- D7-6 — fixed. L6's prompt now reads "Kiran and colleagues' scale recorded weight in steps of
  100 g. Suppose one student's weight is recorded as 68.3 kg...", no longer putting "resolution"
  into the authors' mouths.
- D7-7 — fixed. `definition.text` adds "Some error has nothing to do with how the sample was drawn.
  A faulty instrument is one source: the anchor calls this a nonsampling error," which the two
  existing OpenStax quotes now support.
- D7-8 — fixed. VIM 2.13 is quoted whole, through "...of a measurand"; the 2.16 paraphrase is
  replaced with the VIM's own "reference quantity value" wording; the zero error sentence now names
  VIM 4.28 directly.
- D7-9 — fixed. `jcgm_vim3` added to `must_know[3]`'s refs and to the rewritten L9's refs (L9 cites
  VIM 2.14 and 4.14 in its answer).
- D7-10 — fixed. L7 was rewritten (thermometer/boiling-water, under D7-16) so the diagnostic no
  longer calls a correct step "broken" and then vouches for it; its answer separately states "Line 3
  states a rule true of random error as if it held for all error" and gives the corrected estimate,
  not "the true weight".
- D7-11 — fixed differently. The book's own prior use of "precision" (C03, for the number of digits
  a figure can defend) opens the paragraph, since no record C01-C29 actually uses the glossary's
  exact "how tightly a measurement pins the number down" wording; the glossary's phrase is then
  introduced honestly (not attributed to earlier use) and narrowed to the VIM's sense. This meets
  M10's substance — glossary sense before VIM sense, resolution named separately — without asserting
  a false claim about the book's own history. The glossary-row gap itself is outside this record's
  files and is reported to the main thread, unchanged from the audit's finding.
- D7-12 — fixed. L3's and L5's answers now show the subtracting-a-negative step in full, with a
  number-line reason, before using it.
- D7-13 — fixed. mmHg and degrees Celsius (°C) are named in plain words at first use; "calibration
  weight" is given an inline dash definition; bioimpedance and "gold standard" are removed by D7-1's
  fix.
- D7-14 — fixed. D7 now names the anchor's sampling-bias sense directly ("a sample in which some
  members were more likely to be chosen than others") rather than pointing at a definition D6 did
  not yet carry; D6-15 supplies that definition on the D6 side.
- D7-15 — fixed. L9 and L10 were rewritten as real transfer problems that compute something (old vs.
  new scale average error; two observers' mean difference) and then say what the computation does
  not establish; L3 was moved to level 4 and no longer bundles mean, range and interpretation into
  one "mechanical" step.
- D7-16 — fixed. L3's inline definition of range is removed; L6 no longer asks "on its own" using
  the word "resolution" as a giveaway (reworded per D7-6); L10's parenthetical hand-holding is cut
  to a bare second quote (and later trimmed further for readability, see below); L7 now uses a
  thermometer instead of re-running the illustration's scale A; L8 now uses the paper's real "1 mm
  precision" neck-circumference line instead of re-running the illustration's own working.
- D7-17 — fixed. Both "simply" instances are removed (one replaced with "not simply more readings");
  "Very often" -> "Often" in `must_know[2]`.
- D7-18 — fixed. Both averages now show their sum first: `604.9 plus 605.1 = 1210.0` and `598.5 plus
  600.0 = 1198.5`, each followed by the division.
- D7-19 — fixed. `definition.text` and `must_know` add the correction: "Once a systematic error's
  size is known, subtract it. The VIM calls this a correction (2.53)"; a new level-8 diagnostic
  problem drills applying a correction the wrong way (adding instead of subtracting a zero error).
- D7-20 — fixed. `illustration.body`'s observer paragraph already read "Differences between
  observers are each observer's own systematic habit... Mixed across many observers, those habits
  scatter like random error." `must_know[4]`, which still called cross-observer disagreement "a real
  source of random error" outright, was brought into line with the same wording during this
  Resolution check.
- D7-21 — fixed. "A properly calibrated mercury gauge" -> "a reference device already shown to be
  accurate".
- D7-22 — fixed. `definition.text` now names "the VIM (3rd edition, 2012)" at first mention; the
  review trigger notes a new VIM edition as a reason to re-check.
- D7-23 — fixed. `provenance.bridge_ref` filled with the inventory's S08 rung 1 entry (error is not
  bias; random against systematic on a weighing scale).
- D7-24 — fixed. Two problems were added, taking the ladder from 10 to 12: a level-7 diagnostic
  (trueness mistaken for accuracy — a good average read as every reading being close) and a level-8
  diagnostic (a correction applied the wrong way, adding rather than subtracting a known zero
  error). The third failure mode the audit named, a coarse display mistaken for precision, is
  already covered by D7-2/D7-3's fixes to the illustration itself rather than a separate practice
  problem.

### Readability

Beyond the 49 numbered defects, the fix pass also cleared every sentence-length, paragraph-length
and reading-grade warning the build reported against these two records (a long L10 prompt and
answer in C30 needed several rounds of simplification to reach the 9.0 grade ceiling without
dropping the real Kiran quote it is built on). Both records now report 0 warnings under their own
IDs.

### Figures for the main thread's illustrations

**(a) D6 (B0-R0-C29), sampling simulation, as the record prints it:**
- Population: 2, 4, 4, 4, 5, 5, 7, 9 (mean 5, population standard deviation 2).
- Sample sizes: 10 and 40 (drawn with replacement from the population above).
- Number of samples: 5,000 of size 10, then 5,000 of size 40, drawn from one continuous run.
- Method: Python's `random` module, `random.seed(110)` called once, one `random.choice` call per
  draw, the 5,000 samples of size 10 drawn first and the 5,000 samples of size 40 drawn straight
  after.
- Theoretical spreads (square-root law): 2 / sqrt(10) = 0.6325; 2 / sqrt(40) = 0.3162.
- Simulated spreads, as printed: **0.633** (samples of 10) and **0.317** (samples of 40).

**(b) D7 (B0-R0-C30), the two scales' twenty readings and the true weight, as the record prints
them:**
- True weight (calibration weight): **60.0 kg**.
- Scale A readings (kg): 60.5, 60.5, 60.5, 60.5, 60.5, 60.4, 60.5, 60.5, 60.5, 60.5, 60.5, 60.6,
  60.5, 60.5, 60.5, 60.4, 60.5, 60.6, 60.5, 60.5 (sum 1210.0, mean 60.5, error +0.5).
- Scale B readings (kg): 59.7, 60.2, 60.2, 60.4, 60.0, 59.6, 59.4, 60.6, 58.7, 59.7, 59.4, 60.0,
  59.7, 59.7, 60.4, 59.7, 59.4, 60.5, 60.5, 60.7 (sum 1198.5, mean 59.925, error -0.075; worst single
  reading 58.7, 1.3 kg off).
