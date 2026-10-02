# Cold-read gaps · S58-R1 (Task 5, step 5b)

Two cold readers, 2 Oct 2026. Reader A read the 17 released Book 0 sections and then sections C01–C12
(cut text, `-pass1.md`) from `/tmp/coldread-a/`; reader B read the same Book 0 sections and C01–C12 as
earlier text, then tested C13–C23 from `/tmp/coldread-b/`. Neither could reach the originals. The
sandbox would not let them save files, so their reports came back as replies; the gap lists are copied
here by the conductor (wording condensed, quotations kept). Section numbers are concept numbers
(section 05 = S58-R1-C05). Totals: A 75 gaps (C01–C12), B 71 (C13–C23).

## Two artifacts of the cold-read files, not of the book (conductor's check needed, not restore)

1. **`{{n:key}}` placeholders printed raw.** The assembled `-pass1.md` files do not run the numbers
   registry substitution, so every NFHS figure written as `{{n:...}}` appeared as a raw token. Gaps that
   exist only because of this: A-03-1 (in part), A-08-1, A-09-1, A-09-2, A-10-6, A-11-6, B-14-1, B-17-1,
   B-20-5, B-21-1, B-22-4, B-23-2, and the placeholder lines in the symbol lists. Restorers: treat these
   as artifacts; the conductor confirms that the build substitutes every key and that no key is unknown.
   A-03-1's other half (no NFHS-5 figure is ever given in sections 01–03) is real.
2. **Record ids in the text** (`S58-R1-C04` in section 10, `B0-R0-C40` in section 15): the renderer
   prints these as "section 4" / "Book 0, F2" in the built book; the conductor confirms in the build.
   Gaps A-10-5, B-15-1 are artifacts if the build renders them.

## Reader A (C01–C12)

### Section 01
- A-01-1 "Around the text sit a title page, which carries the title, an abstract and a numbered list of references." Reads as if the title page carries all three; only plain terms settles it. Read twice.
- A-01-2 Figure: "at the three years the paper's text states: none in 1935, 20 per cent in 1955, all of them in 1985." The source paper and the four journals are never named; the claim cannot be checked.
- A-01-3 "a case report, a narrative review or an editorial… a meta-analysis may need a different format." None of these article types is defined, nor "original research article" beyond "reports a study for the first time".
- A-01-4 Ex 3 asks for "the one case" where she should not use the four sections; the text gives three or four.
- A-01-5 Ex 2(d) "Waist was above the clinic's cut-off in 58 per cent of those measured, more than we expected." Nothing says what to do with a sentence holding a result and its interpretation (split it).
- A-01-6 Ex 2(b) "at the level set in the protocol." "Protocol" never defined (also A-04-5).

### Section 02
- A-02-1 "In the terms of Book 0's section on argument" — the ground floor never calls itself "Book 0"; mapping to F4 is a guess.
- A-02-2 Figure: "Adequate information on the treatment tested was in around 60 per cent of reports of clinical trials" — "clinical trial" and "adequate" undefined; the figure's link to the section's claim is not stated.
- A-02-3 "Figures from one study cited by Chalmers and Glasziou (2009)." The original study is not named; no full reference.
- A-02-4 Ex 3 "the section you chose for this book's build." First time the phrase appears; the reader was never told to choose a section. Recurs in sections 03, 04, 06, 07, 08, 10, 12: every design exercise rests on an instruction the reader never received.
- A-02-5 Ex 2 "Rewrite it as an argument." No diary-to-argument rewrite is ever shown; the C/E/S scheme has no rule for a sentence that is both a step and evidence.

### Section 03
- A-03-1 Ex 4 "You have three minutes and the NFHS-4 and NFHS-5 figures." No NFHS-5 figure is given anywhere in sections 01–03 (and later only as placeholders: artifact 1).
- A-03-2 "the NFHS-4 and NFHS-5 figures." NFHS-5 appears with no years, population or measure; those (2019-21, women 15-49) appear only in section 09 P6. NFHS-5 is not spelled out.
- A-03-3 "does it answer 'so what?' for someone who reads only that sentence?" No criterion and no worked example for this test.
- A-03-4 Four abstract parts ("the context and the gap, what was done, the main result, and what it means") against Ex 3's "an abstract of five sentences, one for each part". Read twice.

### Section 04
- A-04-1 "A new idea the data suggest is written as a hypothesis, and labelled as one." "Hypothesis" undefined; no example of the label.
- A-04-2 "say which way it could push the answer" — judging the direction a limitation pushes the answer is never taught.
- A-04-3 "each of the four main sections does one job" — the definition gives only introduction and discussion; methods and results appear only in plain terms. Read twice.
- A-04-4 Ex 2: the invented paper never states its question, so "as the answer to the introduction's question" needs an invented question.
- A-04-5 "end on the question or research objective"; "when you wrote the protocol." Is objective the same as question (section 08's one-term rule)? "Protocol" undefined.

### Section 05
- A-05-1 "The first is the Recommendations of the International Committee of Medical Journal Editors…" — "the first" of what? No antecedent. Read twice.
- A-05-2 "Do not cite articles in predatory or pseudo-journals." Never defined; no way given to spot one.
- A-05-3 "Mark a preprint as a preprint." "Preprint" never defined.
- A-05-4 "Citing Medicine lists the elements in the order they appear." No formatted NLM reference is ever shown; punctuation and initials unknown; Ex 2 cannot be completed as asked.
- A-05-5 "Journal titles are abbreviated as the NLM Catalog lists them." No access to the catalogue; "Arch Dis Child" is a guess.
- A-05-6 "13: e1002128" — the text covers only "the pages", not an article number in their place.
- A-05-7 "Search PubMed for 'Retracted publication [pt]'" — PubMed never introduced; "[pt]" unexplained; "reference manager" undefined.
- A-05-8 "Cite original research directly where you can." The book itself cites second-hand (section 02's figure; Book 0 D6's NFHS-4 figures); "where you can" never explained.
- Symbols: "[pt]", "et al.", "e1002128" unexplained. P, Q, R, S name sources in Ex 3 (P was probability in D1, becomes the P value in 09; S was "step" in 02). "(1)" is a reference number here, a sentence label in section 10.

### Section 06
- A-06-1 "Voice says which of them is the subject." "Them" ambiguous. Read twice.
- A-06-2 "a verb ending, usually, in -ed." Other endings (left, given) never shown; whether "out" in "were left out" is part of the verb is unclear.
- A-06-3 "There were many households without a weighing scale." The who-or-what test gives "There"; "there" sentences and state-of-being verbs never covered.
- A-06-4 "subordinate clause" — used in the must-know points, never defined.
- A-06-5 "When the test is unsure…" — no example of the test misleading; "The road was closed" could be a state or a passive.

### Section 07
- A-07-1 Figure: "Gopen and Swan's first sentence has 42 words" — Gopen and Swan uncited; their sentences never shown.
- A-07-2 Figure: "The made-up survey sentence has 45 words… before mending" — neither version appears in the text; it was the only demonstration of the method.
- A-07-3 Ex 1 "Where does a reader look for the link to what came before?" The text says only "old information first"; the start position is never named.
- A-07-4 "count the words between them" — no rule for where the count starts or whether "was" belongs to the verb.
- A-07-5 "A chain of three or more nouns makes the reader guess"; "they stop working when followed blindly." Both asserted without an example.

### Section 08
- A-08-1 Placeholders (artifact 1); the 25 cut-off could be guessed from D4.
- A-08-2 "the NFHS-5 row… The fact sheet's adult rows" — the fact sheet is never introduced.
- A-08-3 "such as ASHA" — ASHA never spelled out, in the section that requires spelling out at first mention.
- A-08-4 "'Significant', 'random', 'normal' and 'correlation' make a statistical claim… If you ran no test" — normal, significant, correlation and test are never defined anywhere.
- A-08-5 The definition lists five statistical words; the must-know and Ex 1 list four, dropping "sample". Read twice.
- A-08-6 "abbreviation", "short form" and "acronym" (defined narrowly) used without saying whether they are one thing — breaks the section's own one-term rule.
- A-08-7 "Keep no more than three." Three per what, on whose authority?
- A-08-8 Titles counted from 1950, abstracts from 1956, unexplained; "English-language" appears only in the must-know.

### Section 09
- A-09-1, A-09-2 Placeholders in must-know and P6 (artifact 1).
- A-09-3 P6 "use Cole's suggestion for comparing groups" — no such suggestion appears in the section.
- A-09-4 "risk ratio or odds ratio"; "P value" — neither is defined anywhere in the files.
- A-09-5 "P values as equalities, to one or two decimal places" — "equalities" unexplained; no rule for choosing one or two places.
- A-09-6 "enough decimal places to give the standard deviation (SD) two significant figures" — worded in decimal places, so it fails when the SD is 10 or more, or in grams (P4, P7).
- A-09-7 P8 "his SE rule… Say which you would print" — SE = SD/√n not given here (brought from D6); SE 0.98 rounds across a decimal place; no basis for choosing the SD or the SE rule.
- A-09-8 P6 applies the rule of four to a ratio of two percentages; the rule was stated only for risk and odds ratios.
- A-09-9 "± 1.2066"; "(95% CI 2.95 to 3.15)" — "±" and "CI" never explained; in Ex 2 the reader cannot tell whether 1.2066 is the SD or the SE.
- A-09-10 "Girls had 9.2 per cent more overweight than boys" — 9.2 cannot be derived from the given counts (12.9 points; 96 per cent relative). Planted error or a fault? Read three times.
- A-09-11 "Cole's rules" — Cole not cited in this section; "n = 87" uses n without defining it.
- Symbols: "±", "95% CI", "<" unexplained (only "≥" explained, D4); n undefined; P and p both used for the P value, while in D1 p was a probability; "rule of four" misreadable as four significant figures; "lakh" defined only in P12.

### Section 10
- A-10-1 "context, content, conclusion" — none of the three parts explained; Mensh and Kording not cited.
- A-10-2 Topic sentence, "context, content, conclusion" and "point first and answer last" — does the topic sentence come first or last? "Answer last" undefined. Read twice.
- A-10-3 Ex 1 asks for "three things" (what a reverse outline tells you to do); the must-know and Ex 3 give four.
- A-10-4 Figure: "The made-up paragraph before the rewrite changes topic 6 times" — the paragraph is not shown.
- A-10-5 "`S58-R1-C04`" — a code instead of a section name (artifact 2 if the build renders it).
- A-10-6 Ex 2 placeholders (artifact 1).

### Section 11
- A-11-1 "A syllable is one beat of a spoken word" — no rules for doubtful words, abbreviations, "%" or numerals.
- A-11-2 Figure: "71/52 for the 52-word draft, 44/31 for Rewrite A" — the texts are not shown; no Rewrite B.
- A-11-3 "Flesch's Plain English minimum of 60" — only in a caption, yet P9 depends on it; what the scale means is never given.
- A-11-4 "two rules for figures" — "figures" means numerals here, charts elsewhere; the two sentences are not shown. Read twice.
- A-11-5 P5 "Flesch (1979) gives this sentence a score of 32" — 67 syllables give 31.4, 66 give 33.3; 32 from neither. P6 also gives away P5's answer.
- A-11-6 P7 placeholders (artifact 1).
- A-11-7 "abstracts have grown harder to read"; "one large study dropped them"; "709,577 abstracts" — none cited.
- A-11-8 "a school grade level" against "class 11" — the equivalence is never addressed.
- Symbols: "71/52", "1 1/2" fraction notation without comment; 84.6 and 0.846 are two coefficients for one term, and P4 needs 0.846, which appears only in the must-know; "Rewrite A" never explained.

### Section 12
- A-12-1 Figure: "The invented discussion draft, cut in three passes" — the draft is not shown.
- A-12-2 "ask whether the claim gets wider without it" — never demonstrated.
- A-12-3 Ex 2 "by deleting words only… Do not rewrite" — is changing a capital letter allowed? Deleting a whole clause?
- A-12-4 Section 07 says to name the doer of every methods step a reviewer would judge; section 12 allows deletion only, so "Each participant was weighed" stays without a doer. Which rule wins?

### Ground floor (not counted; for the conductor, Book 0 is frozen)
- A-00-1 Book 0 points to sections the reader did not get (A1, powers, functions, counting, the section before C2, D2): expected, only the `ground_floor_deps` sections were released.
- A-00-2 Book 0 never calls itself "Book 0" in its text (the PDF's title does).
- A-00-3 Code blocks in A3 (problems 2, 3) and A7 closed with "```working" instead of "```" in the released files (check whether this is the release tool or Book 0).
- A-00-4 B1 must-know "It is not a measurement at all" has no antecedent.
- A-00-5 P values, odds ratios, risk ratios, confidence intervals, tests, significance, correlation and "normal" are never taught in the sections released.

## Reader B (C13–C23)

### Section 13
- B-13-1 "Every part is there and nothing is added. The draft passes." The second reader dropped "India" and both survey names; section 13 elsewhere flags a lost age range as a failure: how strict is "every part"?
- B-13-2 "| what was found | ... | increasing | kept |" — the first reader's "Obesity" for "overweight or obesity" is not flagged though section 08 forbids it; "commoner in one survey" becoming "increasing" marked kept; no rule for what counts as kept.
- B-13-3 "how far it reaches" — never defined; only the example shows it means the claim's limits.
- B-13-4 "Score each paragraph for readability with one program" — no program named; section 11 taught only the hand formulas.

### Section 14
- B-14-1 Caption placeholders (artifact 1).
- B-14-2 "indicators 88 and 89" — indicator numbering never explained (here, 15, 22).
- B-14-3 "all eight NFHS bars" — the figure has four bars; "eight" never introduced; may one claim span subgroups?
- B-14-4 "Do not lift a figure from your paper onto a slide." No reason given, nothing on what to change.
- B-14-5 "The journal's instructions to authors set the actual limit" — limit of what?

### Section 15
- B-15-1 "(`B0-R0-C40`)" (artifact 2 if rendered).
- B-15-2 "named ten" — only six listed.
- B-15-3 "Length, direction and angle share third place, then area." With the tie, is area fourth or sixth? Ex 1 asks for "the first four places". No chart shows judging "direction".
- B-15-4 "positions along scales not lined up" — never illustrated.
- B-15-5 "Many values from each group take a chart of their distribution." No chart named here; strip charts and box plots arrive only in section 16.
- B-15-6 Stacked bars listed as a proper choice for parts of a whole, then a must-know says to replace them, with no reason.
- B-15-7 Ex 3 "from the table in this section" — there is no table in the section.
- B-15-8 "as on a logarithmic axis, draw dots, not bars" — contradicts section 17's "bars from 1".
- B-15-9 "stunted 35.5%, wasted 19.3%, underweight 32.1% ... indicators 81, 82, 84 and 85" — terms undefined; cannot tell whether categories overlap or a slice is missing.

### Section 16
- B-16-1 "the same error bar" — error bars not defined until section 20.
- B-16-2 "each ward's standard deviation is 14.3 minutes" — values not listed; evenly spaced 10–50 give SD 14.0, not 14.3; cannot reconstruct.
- B-16-3 "joined in that order" / "against adult number 1 to 8" — the only drawn example is not the strip chart just defined, and joins unrelated people with lines, which the must-know reserves for paired measurements.
- B-16-4 "A box plot is a summary too." A box plot is never described.
- B-16-5 "And it is for measured quantities." Never says why bars of shares are fine but bars of means are not.
- B-16-6 Ex 1 attributes to Weissgerber a recommendation and a box-plot criticism the text never makes; the review of 703 papers is unattributed.

### Section 17
- B-17-1 Problems 6, 8, 9, 10 placeholders (artifact 1).
- B-17-2 "work out a ÷ (a − s)" — asserted, never derived; the derivation needs dividing fractions, never taught in Book 0.
- B-17-3 "a the smaller" with "the value it started from" — the shortcut assumes the smaller bar is the start; for a fall (24.0 to 20.6 from an axis at 20) LF is 6.0, not 34.3; never says which bar is the start for urban against rural.
- B-17-4 Drawn and data ratios defined, but their purpose never stated; LF = (drawn ratio − 1) ÷ (data ratio − 1) never given.
- B-17-5 "a bar stands for a ratio, and it starts at 1" — why 1 never said; a bar below 1 going downward never shown; the equal-and-opposite lesson behind P5 never stated.
- B-17-6 "units of log10" — notation new.
- B-17-7 "Shading counts as ink." — "ink" not defined until section 18.
- B-17-8 "So state the axis start in the caption" — "So" refers back to nothing on the page.
- B-17-9 "Truncation makes readers judge a difference as more severe." No source given; Correll appears only in P13, and P13's "cannot claim" asks for something never set up.
- B-17-10 "only a 4.6% increase ... (ratio of 1.13 to 1)" — no tax rates given; the reader must work out that this is percentage points.
- B-17-11 "2.7 times as much ink" (P7) — equal bar widths assumed, not stated.

### Section 18
- B-18-1 "chartjunk" (Ex 3) — never defined.
- B-18-2 "Holmes charts" and "'Useful junk?'" — never says this is Bateman (2010), nor who Holmes is.
- B-18-3 "(Wilke)" — never identified; "Wilke's rule" in section 21 depends on him.
- B-18-4 "Never draw flat data in 3-D." No reason; "flat data" undefined.
- B-18-5 Ex 2 asks for an order of changes; no order is taught until section 22.
- B-18-6 "delete the legend" — in section 14 "legend" meant the caption; resolved only in section 20.

### Section 19
- B-19-1 The third job (highlight) has no named scale, yet Ex 1 asks for one for each job.
- B-19-2 "groups that have no order" — ordered groups (the age groups in Ex 2) not covered.
- B-19-3 "A rainbow fits none of them." No reason given.
- B-19-4 "colour bar", "heat map" undefined; Crameri first appears inside a must-know, with no source.
- B-19-5 "stops being safe on thin lines and small points" — no mechanism.
- B-19-6 "equally strong" and "lightness" undefined, never distinguished from hue.

### Section 20
- B-20-1 "the SD divided by the square root of n" — n used before defined.
- B-20-2 "95% confidence interval (CI) ... approximately the mean plus or minus 2 SE" — a recipe, not what the interval means.
- B-20-3 "4 times the standard error, their rule for three values" conflicts with "2 SE for n ≥ 10"; nothing covers n from 4 to 9.
- B-20-4 "Cumming's Rule 8" — the rule number is opaque; the per-person interval never shown.
- B-20-5 Placeholder width (artifact 1).
- B-20-6 "*p<0.05" (Ex 3) — the P value and the asterisk convention never taught.

### Section 21
- B-21-1 Placeholder (artifact 1).
- B-21-2 Right alignment and decimal-point alignment both given as rules; which wins for a column of mixed digits?
- B-21-3 Women's NFHS-5 anaemia is 57.2 here and 57.0 in section 22; only the long heading implies 57.2 is non-pregnant women.
- B-21-4 "g/dl" — litre and deci- never taught.
- B-21-5 "nonstandard abbreviations go in footnotes" — no list of which are standard.

### Section 22
- B-22-1 "Nine decisions", but the worked sheet has ten rows, including "data".
- B-22-2 "legend names the rounds" conflicts with section 18's "delete the legend" and the sheet's own direct labels.
- B-22-3 "vector graphic ... bitmap ... never a jpeg" — none defined; no reason.
- B-22-4 Placeholder (artifact 1).
- B-22-5 "rose in every group the fact sheet reports" — covers rows left out of the table; a rise of 29.2 to 31.1 called a rise with no way, taught anywhere, to check it against sampling variation.
- B-22-6 "each group's own haemoglobin cut-off" — the cut-offs for children and for ages 15–19 not given.

### Section 23
- B-23-1 "the diary 61.6, the claim draft 79.7, after the cut 86.7" — the three drafts are never shown; the section has no worked journey.
- B-23-2 Placeholder (artifact 1).
- B-23-3 "Format each kind of source from its own chapter of Citing Medicine" — only the journal-article format was taught.
- B-23-4 "say how sure you are" — no tool taught; the NFHS sample size appears only as a placeholder.
- B-23-5 "Never make one by multiplying a percentage by the survey's total sample." Never explained.
- B-23-6 "Indian adults with overweight or obesity" — drops the 15–49 range; calling 15–17-year-olds "adults" happens here and in sections 14, 17.
- B-23-7 The section never prints the finding's numbers, so Ex 2 needs 20.6 and 24.0 carried from section 17.

### Reader B, symbols and double meanings
- Unexplained: log10 (17); n (20, and 09); CI and "95%"; "±" glossed once; "<" never glossed; "*" on a p value and p itself; g/dl; SEM defined only inside an exercise.
- Two meanings: s (axis start in 17, speed in Book 0 C2); a (smaller bar in 17, acceleration-like letter in C2); legend (caption in 14 and 20, colour key in 18, 19, 22); title (caption opening in 20, text across the drawing in 22, table heading in 21); SE and SEM (two names); decoration and ornament; value axis and side axis; 57.2 and 57.0; "4.6%" (points written as per cent); "17%" (a relative rise of 16.5%); "adults" for 15–49; two different nine-step lists (22 and 23), section 22's sheet has ten rows; "ten" tasks with six listed; bars on a log axis (15 says dots, 17 says bars from 1).
