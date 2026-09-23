# Part D · main-thread decisions for the fix pass (Task 4)

Made by the orchestrating chat on 2026-09-23 after reading the three audit reports
(`DEFECTS-part-D-d1d3.md`, `-d4d5.md`, `-d6d7.md`) and re-checking the load-bearing claims itself.
They settle every item the audits handed to the main thread. Fixers apply them as written.

**M1 · D3's table (D3-1, D3-2, D3-5).** Verified: no whole number of 52 gives 86 per cent (45/52 =
86.5) and no whole number of 79 gives 74 (58/79 = 73.4, 59/79 = 74.7). The printed 86 and 74 fit
36 of 42 and 66 of 89: the paper's "overweight" row compared the 42 men in the 25 to 29.9 band
against the other 89 men, the 10 men at 30 or more among them. Women fit the same way (36 of 41,
91 of 110). So:
- Lead the D3 illustration with this failure, per §4 "lead with the failure": try the label's
  group (52 against 79), find the counts will not come out whole, find the group that does. That is
  a denominator question, which is what the section teaches.
- Then the table on 42 against 89: 36 / 6 / 23 / 66. Positive predictive value 36 of 59, about
  61 per cent. Say plainly it is rebuilt from rounded percentages and is the only whole-person
  table that fits them.
- The re-application uses **stated conditions**: "a group of 1,000 young men in which one in five
  is in that band". Not the NFHS-4 figure. 200 in the band, 172 flagged; 800 not, 208 flagged;
  172 of 380, about 45 per cent.
- Youden's index goes, everywhere.

**M2 · The Food Security Act ceiling (D1-3, D2-4, D2-5).** Section 3(2) sets coverage for the rural
population *of the country*, and section 9 has the Central Government fix each State's share. So
"at most 0.75" holds only for one person picked at random from all of rural India. Never apply it
to a block, district, State or "here". The household point in D2 stays (entitlement runs through
eligible households, so two people from one household are not independent draws), but no bound on
a household of four may be derived from a ceiling on persons.

**M3 · Odds (D1 odds defects).** A new anchor is held: `openstax_contemporary_math`
(`sources/openstax_contemporary_math_7_7.txt`, OpenStax *Contemporary Mathematics* s.7.7). Quote
it for the definition of odds and for "odds as a ratio of probabilities". Correct the false
sentences: odds and probability are close for rare events and pull apart as the probability grows;
odds of one means the event and its absence are equally likely. Delete the must-know point on
converting case-control or logistic-regression figures; odds ratios are not taught, and the most
D1 may say is that later subjects meet ratios of odds.

**M4 · Negative numbers (D5).** After the Part C close-out merges, A1 (`B0-R0-C01`) teaches negative
numbers and the order of operations; point back to "the section on counting" for them. A1 is not
known to teach a negative times a negative, so D5 shows that step in full the first time it squares
a deviation below the mean, with a one-line reason, and a worked line (`-3 times -3 = 9`).

**M5 · Sample and population (D5-13, D6).** D5 meets them first. It teaches them at first use in
these plain words, and D6 reuses them unchanged and adds parameter, statistic and estimate:
- **population** — the whole group a question is about
- **sample** — the part of that group that was actually measured

**M6 · Range and the interquartile range (D4, D5).** As C18 teaches: the statistical range is one
number, the largest value minus the smallest. The interquartile range is one number, the third
quartile minus the first. "The middle half lies between 16.7 and 28.8" is fine; calling the
interval itself "the range" or "the interquartile range" is not.

**M7 · Shape from bands (D4-2).** Band counts depend on where the band edges fall, and the WHO bands
are not centred on this group. Nothing in Table 2 shows a tail. Rewrite the shape lesson so it says
exactly that, and teach shape on the bare-number sets instead.

**M8 · Relative frequency.** First met in D1 inside the anchor's phrase. D1 glosses it at that point
as **the fraction of all the tries in which it happened**; D4 reuses those words.

**M9 · Bias.** D6 teaches **sampling bias** from the anchor's s.1.2 words, plainly: a sample that
leans one way because some members of the population were more likely to be picked than others.
D7 teaches **measurement bias** from VIM 2.18 and says it is the same word for the same shape of
problem — an error that points one way and does not shrink when you collect more.

**M10 · Precision (D7).** The glossary row "how tightly a measurement pins the number down" is the
loose sense the earlier sections used (how many digits a figure can defend). D7 quotes those words,
then narrows: the VIM's precision is how closely repeated readings agree with each other; the
smallest step a display can show is *resolution*. Both named, neither contradicting the glossary.

**M11 · D7's bioimpedance passage (D7 gold-standard defect).** Verified: the paper names "DEXA Scan
and body composition analysis using BIA machines" together as the gold standard. Delete every
sentence implying the study used a lesser method. The inventory's D7 row is corrected by the main
thread.

**M12 · D6 and the national figure (D6 most serious).** 20 per cent was the authors' planning figure
for sizing the study, taken from NFHS-4 as the paper reports it. It is not a true value and not a
figure for "young Indian adults". Do not quote NFHS figures as facts about India at all (they reach
us second-hand through the paper). Do not assert any cause for the gap. The sample cannot say
whether the gap comes from who volunteered, from the college, or from anything else, and that is
the lesson. Use Table 2 (83 plus 15 = 98 of 282). The abstract's "83 (29.4%) were overweight" under
a "BMI >=25" definition is now listed in the source header as the paper's seventh inconsistency and
may be used.

**M13 · Derived numbers.** Every figure the prose computes from the paper (52, 39.7 per cent, 98,
34.8 per cent, the D3 cells, and so on) is registered in `numbers[]` with `derived:` saying how,
e.g. `derived: '42 overweight plus 10 obese, Table 2, men'`. The `quote` on a derived entry is the
passage it was counted from. A non-derived entry's quote must **state** the number, in digits or
words. The `derived` field arrives with the Part C close-out (`0beba57`); the working copy carries
a local schema patch so it validates here, and Part D must be committed after `0beba57`.

**M14 · Scope of the transfer band.** A level 9 or 10 problem starts from a claim in words, computes
something, and then says what the answer does not establish. One that computes nothing fails §7a.

**M15 · Style warnings.** The fix pass also clears the sentence-length and reading-grade warnings on
C24, C25 and C26 (99 of them at the draft), splitting at natural joints without changing meaning.
