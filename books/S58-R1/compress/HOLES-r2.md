# S58-R1 compression-pass holes, batch r2 (C07 to C12)

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
