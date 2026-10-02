# Defects · S58-R1

## Found by the compression pass

Holes the cold readers found that the original did not fill either, or that are errors in it (Task 5c, 2 Oct 2026). One block per restore batch; ids are the cold-read gap ids in compress/COLD-READ-GAPS.md. They go through the audit with everything else.

### Batch r1


Found by the compression pass (cold reader A, `COLD-READ-GAPS.md`). Each is something the original
does not fill either, an error, or an original sentence that could not come back without raising the
mean sentence length. Field names are those of `<S>-prose.yml`; "Ex" and "Figure" items sit outside
the prose files. Quotations are of the final text (`-final-prose.yml`) or, for exercises and
captions, of the record.

## C01

1. **A-01-1, definition.text.** "Around the text sit a title page, which carries the title, an
   abstract and a numbered list of references." Reads as if the title page carries all three.
   Close: reword so the title page, the abstract and the reference list are three items.
2. **A-01-2, Figure caption.** "in four general medical journals (1,297 articles, 1935 to 1985)".
   The source is now cited in the definition (Sollaci and Pereira, 2004), but the caption names
   neither the source nor the four journals. Close: cite the source in the caption and name the
   journals, from the paper.
3. **A-01-3, must_know[3].point / definition.** "Do not force a case report, a narrative review or an
   editorial into the four parts." None of these article types is defined; "original research
   article" only as "reports a study for the first time". Close: one dash-gloss for each type.
4. **A-01-4, Ex 3.** "tell her the one case where she should not use the four sections." The text
   gives three or four (case report, narrative review, editorial, meta-analysis). Close: make the
   exercise ask for the kinds of article, or name the one case the text means.
5. **A-01-5, Ex 2(d) / text.** "Waist was above the clinic's cut-off in 58 per cent of those
   measured, more than we expected." Nothing says what to do with a sentence that holds a result and
   its interpretation. Close: one sentence saying such a sentence is split, the number to the
   results and the reading to the discussion.
6. **A-01-6, Ex 2(b); also C04.** "at the level set in the protocol." "Protocol" is never defined.
   Close: a dash-gloss at first use (the original C04 definition's "the plan or protocol" is the
   nearest the text comes).

## C02

7. **A-02-1, definition.text.** "In the terms of Book 0's section on argument, ..." The ground floor
   never calls itself "Book 0" (A-00-2), so the reader must guess F4. Close: name the section as the
   built book renders it, or have the renderer do so.
8. **A-02-2, Figure caption.** "Adequate information on the treatment tested was in around 60 per
   cent of reports of clinical trials". "Clinical trial" and "adequate" are undefined. Close: a
   dash-gloss for each, from the source.
9. **A-02-3, Figure caption and must_know[3].point.** "Figures from one study cited by Chalmers and
   Glasziou (2009)." The original study is not named and no full reference is given. Close: name and
   cite the primary study (section 05 tells the reader to cite originals).
10. **A-02-4, Ex 3 in C02, C03, C04 and C06** (and C07, C08, C10, C12, other batches). "the section
    you chose for this book's build" / "the manuscript or thesis section you chose to rewrite for this
    book". The reader is never told to choose a section. Close: one instruction, early in the book
    (C01 or a preface), telling the reader to choose one section of their own manuscript or thesis
    to rebuild through the book.
11. **A-02-5, Ex 2 / text.** No diary-to-argument rewrite is shown, and the C/E/S marking has no rule
    for a sentence that is both a step and evidence. The restored must_know[2] "Finish the step:
    print the result of the comparison and say what it shows." covers a step that ends a paragraph
    only. Close: a short worked rewrite, or one sentence saying a step that carries a number is
    marked E and its step moves to the methods.

## C03

12. **A-03-1 (real half), Ex 4.** "You have three minutes and the NFHS-4 and NFHS-5 figures." No
    NFHS-5 figure is given in sections 01 to 03. Close: give the figures in the exercise, or point to
    the section that gives them.
13. **A-03-2, Ex 4.** NFHS-5 is not spelled out, and its years and population (2019-21, women 15-49)
    appear only in section 09 P6. Close: spell out at first mention with years and population.
14. **A-03-3, simplified_explanation.** "Second, does it answer "so what?" for someone who reads only
    that sentence?" No criterion and no worked example. Close: one criterion (it says why the finding
    matters to someone) and one passing and one failing example.
15. **A-03-4, definition.text against simplified_explanation.** Definition: "the context and the gap,
    what was done, the main result, and what it means" (four); plain terms, restored: "what was known,
    what was missing, what you did, what you found, and what it means" (five); Ex 3 asks for five.
    Close: make the definition's list five items to match.

## C04

16. **A-04-1, must_know[6].point.** "A new idea the data suggest is written as a hypothesis, and
    labelled as one." "Hypothesis" is now defined; how to label one is not shown. Close: one example
    sentence with the label.
17. **A-04-2, must_know[7].point.** "Name each limit, say which way it could push the answer, and say
    what would settle it." Judging the direction is never taught. Close: one worked example (a
    limitation and the direction it pushes the estimate).
18. **A-04-4, Ex 2.** The invented paper never states its question, so "as the answer to the
    introduction's question" needs an invented one. Close: give the question in the exercise, or
    allow a labelled blank for it as for the results.
19. **A-04-5, must_know[2].point and must_know[3].point.** "end on the question or research
    objective"; "when you wrote the protocol". Whether objective and question are one term (section
    08's one-term rule) is not said, and "protocol" is undefined (see 6). The original's "They hold
    only what was known when the plan or protocol was written." glosses protocol as the plan but
    needs its 27-word methods sentence before it, and the two raised the mean (15.13 → 15.37).
    Close: say whether question and objective are one thing; gloss protocol at first use.

## C05

20. **A-05-4, definition.text.** "Citing Medicine lists the elements in the order they appear." No
    formatted NLM reference is ever shown, so punctuation and initials are unknown and Ex 2 cannot be
    done as asked. Close: one complete NLM reference, as an example.
21. **A-05-5, definition.text.** "Journal titles are abbreviated as the NLM Catalog lists them." The
    reader has no access to the catalogue; Ex 2 needs "Archives of Disease in Childhood" abbreviated.
    Close: give the abbreviation in the exercise, or say how to look it up.
22. **A-05-6, Ex 2.** "13: e1002128" — the text covers only "the pages", not an article number in
    their place. Close: one sentence on article numbers.
23. **A-05-7, must_know[2].point.** "Search PubMed for "Retracted publication [pt]"". "[pt]" is
    unexplained (PubMed and reference manager are now glossed). Close: gloss "[pt]" as the
    publication-type tag.
24. **A-05-8, definition.text.** "Cite original research directly where you can". "Where you can" is
    never explained, and the book itself cites second-hand (section 02's figure; Book 0 D6's NFHS-4
    figures). Close: say when a second-hand citation is acceptable and how it is marked, and fix the
    book's own second-hand citations.
25. **A-05-S1, Ex 2 / must_know[6].point.** "et al." is never glossed. The original's definition
    sentence "Citing Medicine gives all authors, and shows an optional limit of three or six followed
    by "et al." or "and others"; the journal decides." implies it but raised the mean. Close: a
    dash-gloss, "et al. — and others".

## C06

26. **A-06-2, simplified_explanation.** "Its sign is a form of "to be" with a verb ending, usually, in
    -ed." Other endings (left, given) are never shown in the final text, and whether "out" in "were
    left out" is part of the verb is not covered anywhere. The original's definition sentence "The
    verb then takes a form of "to be" (is, was, were, has been) and a past participle, the form of the
    verb that follows "has" or "was" (measured, taken, given)." (31 words) shows the endings but raised
    the mean (11.70 → 12.00). Close: a shorter sentence naming the past participle and two irregular
    ones; one sentence on phrasal verbs.
27. **A-06-3, Ex 2 sentence 3.** "There were many households without a weighing scale." The
    who-or-what test gives "There"; "there" sentences and state-of-being verbs are not covered.
    Close: one sentence on "there" sentences (the subject follows the verb).
28. **A-06-5, must_know[3].point.** "When the test is unsure, ask whether the subject did the action
    or received it." No example of the test misleading; "The road was closed" (Ex 2) can be a state
    or a passive. Close: one example each way, and a line on the state reading.

### Batch r2


For the fixer. Each hole is a gap the cold reader (A) found that the full-length original does
not fill either, or that is an error or contradiction. Restoring cannot close any of them. "As it
stands" quotes the final text (`S58-R1-Cnn-final-prose.yml`), or the figure or exercise, which
the cut did not touch. Gap ids are from `COLD-READ-GAPS.md`. "(residual)" marks what is left
after a partial restore.

## C07

**H1** (A-07-1, residual) · figure caption. *As it stands:* "Gopen and Swan's first sentence has
42 words, 23 of them between subject and verb; their third has 62, with 27 between." *Wrong:*
the two sentences are never shown, so the counts cannot be checked or learned from. *Close:*
quote both sentences (in a block quote or `working` block) or cut them from the figure.

**H2** (A-07-2) · figure caption. *As it stands:* "The made-up survey sentence has 45 words, 41
between, before mending, and 27 words, 4 between, after." *Wrong:* neither version appears. It
was the section's only demonstration of the method. *Close:* show the before and after sentences.

**H3** (A-07-4) · `must_know[0].point`. *As it stands:* "Find the subject and the verb, and count
the words between them." *Wrong:* no rule for where the count starts and stops, or whether an
auxiliary such as "was" is part of the verb. Ex 2 depends on it. *Close:* one sentence that fixes
the count (for example, words after the subject's main word and before the first word of the
verb, auxiliary included).

**H4** (A-07-5, residual) · `must_know[5].point`. *As it stands:* "A chain of three or more nouns
makes the reader guess how they relate." *Wrong:* asserted with no example. *Close:* one short
example chain and its unpacked form.

## C08

**H5** (A-08-2) · `must_know[1].point`. *As it stands:* "The fact sheet's adult rows give the
two together ..." *Wrong:* "the fact sheet" is never introduced (what NFHS-5 is, and that it
publishes fact sheets). *Close:* introduce NFHS-5 and its fact sheet at first use in the book,
or point to the section that does.

**H6** (A-08-3) · `must_know[5].point`, `must_know[6].point`. *As it stands:* "as in a report that
ASHAs or patients will read"; "such as ASHA". *Wrong:* ASHA is never spelled out, in the section
whose rule is to spell out at first mention. *Close:* "Accredited Social Health Activist (ASHA)"
at first mention.

**H7** (A-08-4) · `definition.text`, `must_know[4].point`. *As it stands:* "'Significant', 'random',
'normal' and 'correlation' make a statistical claim ... If you ran no test, ..." *Wrong:* none of
these words, nor "test", is defined anywhere the reader has reached (also ground-floor A-00-5).
*Close:* a one-line statistical sense for each, or a pointer to where the course teaches it.

**H8** (A-08-5) · `definition.text` against `must_know[4].point` and Ex 1. *As it stands:* the
definition lists five words including "sample"; the must-know lists four. *Wrong:* inconsistent,
and the reader read it twice. *Close:* make the lists agree.

**H9** (A-08-6, residual) · `definition.text`. *As it stands:* "An abbreviation is a shortened form
of a word or phrase." and "Barnett and Doubleday (2020) counted acronyms, which they defined as
...". *Wrong:* it never says that an acronym is a kind of abbreviation, or that "short form" in
the plain-terms text means abbreviation. That breaks the section's own one-term rule. *Close:*
one sentence relating the three terms, and one term used in the plain-terms text.

**H10** (A-08-8) · `definition.text`, `must_know[5].point`. *As it stands:* "published from 1950 to
2019"; the figure's "0.4 in 1956"; "only in English-language titles and abstracts". *Wrong:*
abstracts start in 1956 and titles in 1950 without explanation. "English-language" is stated only
in the must-know. *Close:* state why the abstract series starts later (if the source says), and
give the language restriction where the study is described.

## C09

**H11** (A-09-3) · practice problem 6. *As it stands:* "Then use Cole's suggestion for comparing
groups to decide how many decimal places the two percentages need." *Wrong:* no such suggestion
is in the section. *Close:* state Cole's suggestion in the definition or table, or rewrite P6.

**H12** (A-09-4) · table and `definition.text`. *As it stands:* "risk ratio or odds ratio"; "P
value". *Wrong:* neither is defined anywhere the reader has reached. *Close:* one-line meanings,
or a pointer to where the course teaches them.

**H13** (A-09-5) · `definition.text`. *As it stands:* "They ask for P values as equalities, to one
or two decimal places." *Wrong:* "equalities" is unexplained (P = 0.03, not P < 0.05), and there
is no rule for choosing one or two places. *Close:* a short example and the choice rule from
SAMPL.

**H14** (A-09-6) · table, mean row. *As it stands:* "enough decimal places to give the standard
deviation (SD) two significant figures". *Wrong:* worded in decimal places, so it gives no answer
when the SD is 10 or more, or in grams (P4's 11.46, P7). *Close:* word it in significant figures
or the place value of the rounding.

**H15** (A-09-7) · table and P8. *As it stands:* "or the standard error (SE) one"; P8 "give it by
his SE rule for a sample of 100 and for a sample of 10,000. Say which you would print". *Wrong:*
SE = SD/√n is not given. SE 0.98 for n = 100 rounds across a decimal place. No basis for choosing
the SD or SE rule is given. *Close:* state the SE formula (or point to D6) and say when each
rule applies.

**H16** (A-09-8) · table and P6. *As it stands:* the rule of four is stated "for risk ratio or odds
ratio"; P6 applies it to "the urban figure as a ratio of the rural one". *Wrong:* the reader is not
told a ratio of two percentages falls under the rule. *Close:* say that the rule covers any ratio,
or that a ratio of two prevalences is a risk ratio.

**H17** (A-09-9) · Ex 2 and P7. *As it stands:* "Mean age was 13.4782 years ± 1.2066"; "(95% CI 2.95
to 3.15)". *Wrong:* "±" and "CI" are never explained. In Ex 2 the reader cannot tell whether
1.2066 is the SD or the SE. *Close:* explain both symbols, and either say Ex 2's figure is
unlabelled on purpose or label it.

**H18** (A-09-10) · Ex 2. *As it stands:* "Girls had 9.2 per cent more overweight than boys". *Wrong:*
from 11 of 42 and 6 of 45 the gap is 12.9 points, or a 96 per cent relative rise. 9.2 matches
neither. If it is a planted error, the exercise does not say so. *Close:* confirm the intent and
either make 9.2 derivable or correct it.

**H19** (A-09-11, residual) · `definition.text`, table lead-in. *As it stands:* "Cole's rules for
how many digits to report ...". *Wrong:* Cole is cited only in C05's reference list, not here.
*Close:* cite Cole (2015) at first use in C09.

**H20** (A-09 symbols) · whole section. *As it stands:* "P values" and "p = 0.000" (while D1 used p
for a probability); "P < 0.001"; "the rule of four"; "lakh" defined only in P12. *Wrong:* P and
p are both used for one thing. "<" is unexplained. "Rule of four" can be misread as four
significant figures. "Lakh" first appears in P12. *Close:* one symbol for the P value, a gloss of
"<" (D4 glosses only "≥"), and lakh defined where it is first needed.

## C10

**H21** (A-10-1, residual) · `definition.text`. *As it stands:* "Mensh and Kording call this
shape context, content, conclusion." *Wrong:* Mensh and Kording are introduced only in C02 and C03
of the original, and no C02–C09 cut keeps their name. *Close:* the C02 restorer or the conductor
restores their introduction in C02. Otherwise cite them here.

**H22** (A-10-2, residual) · `must_know[3].point`. *As it stands:* "The two shapes of a one-point
paragraph, point first and answer last, are both sound." *Wrong:* "answer last" is never defined.
The definition now puts the topic sentence first, so the second shape reads as a contradiction.
*Close:* one sentence defining the answer-last shape (question or evidence first, point at the
end).

**H23** (A-10-3) · Ex 1 against `must_know[1].point`. *As it stands:* Ex 1 "what are the three
things it can tell you to do with a paragraph?"; must-know "Split ... Merge ... Move or cut".
*Wrong:* three against four. *Close:* make them agree.

**H24** (A-10-4) · figure caption. *As it stands:* "The made-up paragraph before the rewrite
changes topic 6 times; the rewrite changes 2 times". *Wrong:* the paragraph is not shown. If it is
Ex 2's paragraph, its topics run 1, 3, 2, 3, 1, 2, 3, not the figure's 1, 3, 2, 1, 3, 2, 1.
Either way, the figure would also give away Ex 2's answer. *Close:* show the figure's paragraph,
or redraw the figure from a different paragraph.

## C11

**H25** (A-11-1) · `definition.text`. *As it stands:* "A syllable is one beat of a spoken word".
*Wrong:* no rule for doubtful words, abbreviations, "%" or numerals. P5, P7 and P10 depend on
it. *Close:* a short counting convention, with the figures rule pointing to `must_know[1]`.

**H26** (A-11-2) · both figure captions. *As it stands:* "71/52 for the 52-word draft, 44/31 for
Rewrite A". *Wrong:* the draft and Rewrite A are not shown, and Rewrite B is named only in a
must-know sentence the cut removed. *Close:* show the draft and Rewrite A, or name them as the
sentences of another section.

**H27** (A-11-3, residual) · first figure caption. *As it stands:* "above Flesch's Plain English
minimum of 60". *Wrong:* stated only in a caption, with no source, yet P9 depends on it. *Close:*
state the threshold, with its source (Flesch 1979), in the definition.

**H28** (A-11-4) · second figure caption and `must_know[1].point`. *As it stands:* "scored under
Flesch's two rules for figures". *Wrong:* "figures" means numerals here and charts elsewhere in
the book, and the two sentences are not shown. *Close:* say "numerals" (or "numbers written as
digits"), and show the sentences (see H26).

**H29** (A-11-5) · P5 and P6. *As it stands:* "Flesch (1979) gives this sentence a score of 32."
*Wrong:* 43 words and 67 syllables give 31.4, and 66 give 33.3, so 32 comes from neither. P6
("it still has 67 syllables") gives away P5's count. *Close:* check Flesch's own count and say how
he got 32, then move the syllable count out of P6's stem.

**H30** (A-11-7, residual) · `must_know[1].point`. *As it stands:* "and one large study dropped
them". *Wrong:* the study is never identified. *Close:* name it (presumably Plavén-Sigray and
colleagues, 2017; verify against the source).

**H31** (A-11-8) · `definition.text` and Ex 2. *As it stands:* "Its result is a school grade
level."; Ex 2 "completed class 11". *Wrong:* the text never says whether a US school grade maps
onto an Indian class. *Close:* one sentence on the equivalence, or why it does not hold.

**H32** (A-11 symbols, residual) · figure caption and P10. *As it stands:* "71/52", "44/31", "1 1/2
syllables per word", "Rewrite A". *Wrong:* fraction notation is used without comment, and Rewrite
A is never explained. *Close:* write the ratios in words or as decimals, and see H26.

## C12

**H33** (A-12-1) · figure caption. *As it stands:* "The invented discussion draft, cut in three
passes." *Wrong:* the draft is not shown. *Close:* show the draft, or base the figure on Ex 2's
paragraph.

**H34** (A-12-2) · `must_know[3].point`. *As it stands:* "Before you delete any word, ask whether
the claim gets wider without it." *Wrong:* never demonstrated. The original's "A qualifier such
as an age range, a year, a place or 'or obese' looks like padding." was tried. It failed
validation (mean sentence 12.64 to 12.71), and even restored it does not demonstrate the test.
*Close:* one worked example of a word whose deletion widens the claim. A shorter sentence than
the original's would also keep the mean down.

**H35** (A-12-3) · Ex 2. *As it stands:* "by deleting words only ... Do not rewrite or join
sentences." *Wrong:* it does not say whether a capital letter may change, or a whole clause may go.
*Close:* state both in the exercise.

**H36** (A-12-4) · Ex 2 against C07 `must_know[4].point`. *As it stands:* C07 "name the doer of
every step a reviewer would judge"; C12 Ex 2 deletion only, so "Each ... participant was weighed"
keeps no doer. *Wrong:* the two rules conflict, and the reader cannot tell which wins. *Close:* say
in Ex 2 that naming the doer is a rewrite, outside this exercise, or pick a sentence where the
doer does not matter.

### Batch r3


These are gaps the restore could not close. In most, the full-length original does not fill the
gap either, or the gap is an error or a contradiction. In four, the original's sentence exists but
could not come back without raising the mean sentence length above the original's (marked
**dropped for the mean**). All are for the fixer, and they go back through the audit.
"Field" is the record field. "Exercise" and "Problem" mean fields the compression pass does not
touch. Gap ids are from `COLD-READ-GAPS.md`.

## C13

**H-13-1** (B-13-1). `illustration.body`, the third rule of the pass.
- As it stands: "Every part is there and nothing is added. The draft passes."
- What is wrong: the second reader's sentence ("Overweight among women of 15 to 49 ...") drops
  "India", but the table fails the first reader for dropping the age range from "about whom".
- What would close it: make "India" survive in the second reader's sentence, or say which parts
  of "about whom" must survive.

**H-13-2** (B-13-2). `illustration.body`, the comparison table.
- As it stands: "| about whom | ... | Indian women | age range lost |" and "| what was found | commoner in
  NFHS-5 than in NFHS-4 | increasing | kept |".
- What is wrong: the reader's "Obesity" for "overweight or obesity" goes unflagged, though C08 forbids
  the swap. "Increasing" is marked kept for a two-survey comparison. There is no rule for "kept".
- What would close it: flag the outcome change in the table, and state in the definition what
  counts as a part kept.

**H-13-3** (B-13-3). `definition.text`, step 4.
- As it stands: "... compared with what, and how far it reaches."
- What is missing: "how far it reaches" is never defined. Only the table shows it means the
  claim's limits.
- What would close it: one sentence defining it, with C03's term if C03 has one.

**H-13-4** (B-13-4). Exercise 2, step 4 (also C11 `must_know`).
- As it stands: "Score each paragraph for readability with one program ..."
- What is missing: no program is named here or in C11, which teaches only hand formulas.
- What would close it: name a freely available tool and the score it reports, or tell the reader
  to use C11's hand formula.

## C14

**H-14-2** (B-14-2). Figure caption. The same issue recurs in C15 and C22.
- As it stands: "Source: NFHS-5 India Fact Sheet, indicators 88 and 89."
- What is missing: the reader is never told that the fact sheet numbers its indicators.
- What would close it: one sentence at the first use, saying how fact-sheet indicators are numbered.

**H-14-3** (B-14-3). Exercise 4.
- As it stands: "... wants to keep all eight NFHS bars in one figure ..."
- What is wrong: the figure has four bars. "Eight" (women and men × urban and rural × two rounds?)
  is never introduced.
- What would close it: say what the eight values are, or change the number to match a figure the reader has seen.

**H-14-4** (B-14-4). `must_know[4].point`. **Dropped for the mean.**
- As it stands: "Do not lift a figure from your paper onto a slide." The reason was restored to the definition.
- What is missing: what to change on the slide. The original has it in a 25-word sentence ("Make
  the slide version again, with fewer elements, thicker lines and bigger text, because it will be
  seen from a distance for a few seconds."), and that sentence raises C14's mean above the original's.
- What would close it: the fixer splits that sentence into two, or accepts it in place of a longer cut.

## C15

**H-15-3** (B-15-3). `definition.text`, and Exercise 1.
- As it stands: "Length, direction and angle share third place, then area." Exercise 1 asks for "the first four places".
- What is wrong: with the tie, it is unclear whether area is fourth or sixth, so Exercise 1 has no
  single answer. No chart in the section shows judging direction.
- What would close it: say whether places are counted by rank or by item, and reword Exercise 1 to
  match. Add one example of a direction judgment, such as a slope.

**H-15-4** (B-15-4). `definition.text`.
- As it stands: "First comes position along a common scale, then positions along scales not lined up."
- What is missing: no example of scales not lined up, such as small multiples with separate axes.
- What would close it: one example sentence.

**H-15-7** (B-15-7). Exercise 3.
- As it stands: "name the shape of the numbers from the table in this section".
- What is wrong: the section has no table. The five shapes are a list in the definition and must-know.
- What would close it: point the exercise at the list, or add the shape-to-mark table.

**H-15-8** (B-15-8). `must_know[6].point`, against C17 `must_know[5]`.
- As it stands: "When the value axis cannot start at zero, as on a logarithmic axis, draw dots, not bars."
  C17 says: "Draw a ratio on a logarithmic axis, with bars from 1."
- What is wrong: the two sections contradict each other.
- What would close it: state the case once. Bars from 1 for ratios, dots otherwise on a log axis,
  or whichever the sources support. Then make both sections agree.

**H-15-9** (B-15-9). Exercise 2.
- As it stands: "stunted 35.5%, wasted 19.3%, underweight 32.1% and overweight 3.4% ... indicators 81, 82, 84 and 85".
- What is missing: stunted, wasted and underweight are never defined. The restored must-know now says
  that the categories overlap.
- What would close it: a one-line gloss of each term in the exercise, or a pointer to where the book defines them.

## C16

**H-16-1** (B-16-1). `definition.text`. **Dropped for the mean.**
- As it stands: "Many different sets of values give the same bar and the same error bar."
- What is missing: what an error bar is. The original's sentence ("It usually adds an error bar for
  the standard deviation, or for the standard error of the mean (`B0-R0-C29`).") says only what it
  stands for. It could not come back with B-16-5's restore without raising the mean. Error bars are
  defined only in C20.
- What would close it: a short definition here ("a line above and below the bar's top, as long as
  ..."), or a pointer forward to C20.

**H-16-2** (B-16-2). Figure captions.
- As it stands: "each ward's standard deviation is 14.3 minutes" and "Ward 1 climbs evenly from 10 to 50 minutes."
- What is missing: the 24 values are only in the figure spec (`check/records/S58/S58-R1-C16.yml`), and
  14.3 is correct for them (sample SD 14.29, 14.28 and 14.25). Ward 1 is not evenly spaced
  (10, 15, 21, 27, 33, 39, 45, 50). Evenly spaced 10 to 50 gives SD 14.0, so the reader cannot
  reconstruct the figure.
- What would close it: list the values in the caption or a table, and say "nearly evenly".

**H-16-3** (B-16-3). The second figure.
- As it stands: "joined in that order" / "against adult number 1 to 8".
- What is wrong: the definition has just defined a strip chart, with one column of dots per group
  and jitter. The only drawn example is a rank plot that joins unrelated people with lines, which
  the must-know reserves for paired measurements.
- What would close it: redraw it as a strip chart (three columns of jittered dots with a mean line).

**H-16-4** (B-16-4). `must_know[2].point`. **Dropped for the mean.**
- As it stands: "A box plot is a summary too."
- What is missing: what a box plot is. The original's definition sentence ("With more values, a box
  plot shows the median, a box around the middle half of the values, and whiskers beyond it, with
  far values drawn as single dots.", 29 words) raises C16's mean above the original's.
- What would close it: split that sentence, or accept it in place of a longer cut.

**H-16-6** (B-16-6). Exercise 1, and `must_know[4].point`.
- As it stands: "Which chart do Weissgerber and colleagues recommend for small groups, and why not a box plot?"
  The must-know reads "A systematic review covered 703 papers ...".
- What is missing: the text never attributes the review, or a recommendation, to Weissgerber and colleagues.
- What would close it: name the review's authors and year where it is described, and state their recommendation.

## C17

**H-17-2** (B-17-2, B-17-4). `definition.text` and `must_know[1].point`.
- As it stands: "work out a ÷ (a − s) with the smaller bar". In the original, the definition also says
  "the LF comes to a ÷ (a − s), as the second illustration shows".
- What is missing: the derivation. No illustration shows it, and it needs dividing fractions, which
  Book 0 does not teach. The drawn and data ratios are defined, but their use is never stated
  (LF = (drawn ratio − 1) ÷ (data ratio − 1)).
- What would close it: a worked derivation from the percentage-change definition through the two
  ratios to a ÷ (a − s), and the cross-reference fixed.

**H-17-3** (B-17-3). `definition.text` and `must_know[1].point`. **An error.**
- As it stands: "a the smaller", with "the change divided by the value it started from".
- What is wrong: the shortcut assumes the smaller bar is the start. For a fall (24.0 to 20.6, axis
  at 20) the LF is 6.0, not 34.3. For urban against rural, nothing says which bar is the start.
- What would close it: state the shortcut for the starting value, or restrict it to rises, and say
  how to choose the start for a comparison of two groups.

**H-17-5** (B-17-5). `definition.text`.
- As it stands: "On a logarithmic axis a bar stands for a ratio, and it starts at 1."
- What is missing: why 1, which is no difference. A ratio below 1 drawn downward is never shown. The
  restored must-know now gives the equal-and-opposite lesson.
- What would close it: one sentence on why 1, and Problem 5's answer or a figure showing a bar below 1.

**H-17-6** (B-17-6). Problems 5 and 10.
- As it stands: "in units of log10".
- What is missing: log10 is never taught or glossed.
- What would close it: a gloss at first use, or a pointer to where Book 0 teaches it.

**H-17-7** (B-17-7). `must_know[3].point`.
- As it stands: "Shading counts as ink."
- What is missing: "ink" is not defined until C18. The principle of proportional ink only implies it.
- What would close it: one sentence in the definition saying what ink means here.

**H-17-11** (B-17-11). Problem 7.
- As it stands: "the 2014 bar uses about 2.7 times as much ink".
- What is missing: the answer assumes equal bar widths and does not say so.
- What would close it: add "with bars of equal width".

## C18

**H-18-2** (B-18-2). `definition.text` and `must_know[4]`, `must_know[5]`. **Dropped for the mean.**
- As it stands: "'Useful junk?' found that cartoon charts ..." and "Holmes charts" (caption).
- What is missing: who Holmes is, and that "Useful junk?" is Bateman and colleagues (2010). The
  original's sentence ("Bateman and colleagues (2010) showed 20 people charts by the graphic artist
  Nigel Holmes, ...", 25 words) raises C18's mean above the original's. Even that sentence never
  ties the title to the authors.
- What would close it: give the full title and authors once, and split the Bateman sentence.

**H-18-3** (B-18-3). `definition.text` and `must_know[2]`.
- As it stands: "Context is non-data ink, and it stays (Wilke)." and "in Wilke's example".
- What is missing: Wilke is never identified (author and book), and C21's "Wilke's rule" depends on it.
- What would close it: the full citation at first use, which is C14 if its restored Wilke line stays.

**H-18-4** (B-18-4). `definition.text` and `must_know[2].point`.
- As it stands: "A 3-D effect on flat data" and "Never draw flat data in 3-D."
- What is missing: "flat data" is undefined. It means values that vary on one dimension only.
- What would close it: a gloss at first use.

**H-18-5** (B-18-5). Exercise 2.
- As it stands: "List what you would change, in the order you would change it".
- What is missing: no order is taught here beyond "Do this before you change anything else". The order arrives in C22.
- What would close it: teach the order here, or drop "in the order" from the exercise.

**H-18-6** (B-18-6). Book-wide; C14 `definition.text` against C18 `definition.text`.
- As it stands: C14 says "journals call it the figure legend" (the caption). C18 says "a legend, the
  key that says which colour is which".
- What is wrong: one word has two meanings, and C20 and C22 use both.
- What would close it: pick one term for the caption and one for the key, and use them throughout.

### Batch r4


Found by the compression pass (cold reader B, `COLD-READ-GAPS.md`). Each is something the original
does not fill either, an error, or an original sentence that could not come back without raising the
mean sentence length (or, item 12, without tripping a tool conflict). Field names are those of
`<S>-prose.yml`; "Ex" and "Figure" items sit outside the prose files. Quotations are of the final text
(`-final-prose.yml`) or, for exercises and captions, of the record.

## C19

1. **B-19-1, definition.text / Ex 1.** "Or it picks out one element against others drawn in grey."
   Ex 1 asks for "the kind of colour scale each job takes"; the third job has no named scale.
   Close: name what the highlight job uses (one strong colour against grey) in the definition, or
   reword Ex 1 to ask for the scale for the first two jobs only.
2. **B-19-2, definition.text.** "It separates groups that have no order, using a qualitative scale".
   Groups that do have an order (Ex 2's four age groups) are covered nowhere. Close: one sentence
   saying which scale ordered groups take.
3. **B-19-4, must_know[7].point.** "When you review a colleague's map or heat map ... Is there a colour
   bar?" Neither "heat map" nor "colour bar" is defined. Close: a dash-gloss for each at first use.
4. **B-19-6, definition.text.** "a small set of colours that look clearly different from each other
   and equally strong." "Equally strong" is undefined, and lightness is never set against hue, which
   the red-green rule depends on. Close: define strength (saturation) and hue in a clause each.

## C20

5. **B-20-2, definition.text.** "or a 95% confidence interval (CI). When n is 10 or more, it is
   approximately the mean plus or minus 2 SE." A recipe, not a meaning. The original's "A 95% CI is a
   range worked out from the sample so that, if the study were repeated many times, 95 per cent of
   such ranges would contain the true mean of the population." fills it but raised the mean
   sentence length. Close: restore it as two shorter sentences, or after another cut in C20.
6. **B-20-3, Figure caption / definition.text.** "27.7 for an approximate 95% confidence interval (4
   times the standard error, their rule for three values)" against "When n is 10 or more, it is
   approximately the mean plus or minus 2 SE." Nothing covers n from 4 to 9. Close: one sentence
   saying the multiplier falls from about 4 at n = 3 towards 2 by n = 10, with the source.
7. **B-20-4, must_know[7].point.** "Bars on the same group measured at different times cannot show
   whether the group changed (Cumming's Rule 8)." The rule number means nothing to the reader, and
   the per-person interval is never shown. Close: cite Cumming, Fidler and Vaux (2007) by name and
   drop "Rule 8", or give a three-person example of the change interval.
8. **B-20-6, Ex 3.** "Error bars represent variation. *p<0.05." The P value and the asterisk
   convention are taught nowhere (A-00-5 also). Close: a one-line gloss of the convention in the
   exercise, or a pointer to where P values are taught.

## C21

9. **B-21-2, simplified_explanation / must_know[7].point.** "Numbers line up on the right and keep the
   same number of decimal places." against "Give each value the digits it needs, and line the column
   up on the decimal point." No rule for which wins. Close: say right alignment holds when the
   decimal places are the same, and decimal-point alignment when they differ.
10. **B-21-4, Ex 2.** "measured in grams per decilitre (g/dl)". Litre and deci- are not taught (floor
    test 2). Close: one clause, "a decilitre is a tenth of a litre", with litre glossed.
11. **B-21-5, definition.text.** "Explanations, exclusions and nonstandard abbreviations go in
    footnotes". Nothing says which abbreviations are standard. Close: name the authority (the
    journal's list) or give two examples of each.

## C22

12. **B-22-5, illustration.body / caption.** "Here: between NFHS-4 and NFHS-5, the share with anaemia
    rose in every group." and the caption's "in every group the India fact sheet reports". (a) The
    reader cannot tell the claim covers the rows left out of the table. The original's "The fact
    sheet's rows for non-pregnant and pregnant women rose too. They are left out because the row for
    all women contains them, ..." fills it, but restoring it brings back the Lie Factor working block
    without its introduction (tool conflict, `RESTORE-DECISIONS-r4.md`). (b) A rise of 29.2 to 31.1 is
    called a rise with no way, taught anywhere, to check it against sampling variation. Close: (a)
    restore once the tool is fixed; (b) a sentence saying the claim is descriptive and the confidence
    intervals in the full NFHS report are where to check it, or soften "rose" for the small rises.
13. **B-22-1, Ex 1 / illustration.body.** "list the nine decisions for making a figure" against the
    worked sheet's ten rows, one of them "data". Close: drop the data row into the claim row, or say
    the sheet records the data as well as the nine decisions.
14. **B-22-2, illustration.body (sheet) / section 18.** "legend names the rounds" against section 18's
    "delete the legend" and the sheet's own "each round named over the first pair". Close: choose one;
    direct labels fit section 18 and step 6.
15. **B-22-6 and B-22-3, illustration.body / caption.** "Bars show the per cent anaemic, by each
    group's own haemoglobin cut-off". The restored rows give 11.0 g/dl for children and 13.0 for men;
    the women's cut-offs (non-pregnant 12.0, pregnant 11.0, in C21 Ex 2 only in part) are given
    nowhere. Also "save a vector graphic, such as a pdf ... a png where a bitmap is required, and
    never a jpeg": pdf, png and jpeg are never named as kinds of file. Close: one clause for the
    women's cut-offs from the fact sheet's footnote 22; a dash-gloss saying png and jpeg are bitmaps
    and pdf can hold a vector graphic.

## C23

16. **B-23-1, Figure caption.** "the diary 61.6, the claim draft 79.7, after the cut 86.7". The three
    drafts are never shown; the section has no worked journey. Close: an illustration carrying the
    finding through the nine steps, with the three drafts.
17. **B-23-3, must_know[6].point.** "Format each kind of source from its own chapter of Citing
    Medicine." Only the journal-article format was taught. The original's "A fact sheet read online is
    not a journal article: it follows the chapter on titles on the Internet." raised the mean sentence
    length and was not restored. Close: restore it, and show one formatted Internet entry.
18. **B-23-4, Ex 3.** "say how sure you are". No tool for uncertainty is taught, and the NFHS sample
    size appears only as a placeholder. Close: tie it to the CI of item 5, or reword the exercise.
19. **B-23-6, simplified_explanation (error).** "The result is the share of Indian adults with
    overweight or obesity in two national surveys." Drops the 15-49 range, and 15-17-year-olds are not
    adults (also sections 14 and 17). Close: "Indian women and men aged 15 to 49".
20. **B-23-7, Ex 2.** "Obesity in Indian women up 17%" needs 20.6 and 24.0, carried from section 17;
    the section never prints the finding's numbers. Close: print the two figures in the plain terms or
    the illustration of item 16.

## Symbols (reader B's list, as it touches C19 to C23)

21. **C20 Ex 2, C21 must_know[3].point and Ex 3, C21 Ex 2, C22 rows.** "±" is glossed once (earlier)
    and "<" never. Close: gloss each at first use in these sections ("plus or minus", "below").
22. **C20 definition.text and Ex 2.** "the standard error of the mean (SE)" against "SEM is the
    standard error of the mean". Two abbreviations for one term, against section 08's one-term rule.
    Close: use SE throughout and say journals also write SEM.
23. **C20, C21, C22.** "title" means the caption's opening (C20), text across the drawing (C22) and the
    table heading (C21). Close: say once that a figure's title sits in its caption and a table's above
    the table.
24. **C19 definition.text / section 18.** "Colour that does none of these jobs is ornament." against
    section 18's "decoration". Close: one term in both.
25. **C20 Ex 3 / C22 illustration.body.** "a side axis titled 'BMI'" against "the value axis". Close:
    one term, glossed once.
