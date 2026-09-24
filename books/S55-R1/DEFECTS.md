# S55-R1 defects

## Found by the compression pass

Holes from the cold read (books/S55-R1/compress/COLD-READ-GAPS.md) that the original did not fill either, or errors/contradictions. Full entries:

# S55-R1 step 5c, batch r1 (C01 to C04): holes for the fixer

These gaps could not be closed by restoring the original's own sentences. For each, the original either
has the same gap or has an error, or restoring it broke a constraint. Gap ids refer to `COLD-READ-GAPS.md`.
"As it stands" quotes the final text (`<S>-final-prose.yml`). Nothing here has been fixed.

## C01

**H1 · A-C01-5 · C01 `illustration.body` (first use of NCD)**
As it stands: "What share of patients at the district hospital's NCD clinic know their own weight?" (table)
What is wrong: NCD is never expanded in the final text of any S55 section, but it recurs in every one.
The original expands it: "There is also a district programme officer for non-communicable diseases (NCDs) — long-term
illnesses that do not pass from one person to another." That 23-word sentence raised C01's mean sentence length
from 12.27 to 12.46 (validation fail).
To close: expand NCD at first use in a sentence no longer than the section mean, for example in the table row or in a
short separate gloss.

## C02

**H2 · A-C02-1 (and A-X-1) · C02 `figure` caption**
As it stands: "The five made-up first drafts and their rewrites in the second illustration, counted by which part each names."
What is wrong: C02 has no illustration in the original either, let alone a second one. The figure's counts
(1 → 5 fenced; exposures 3 → 4; comparisons 0 → 4) cannot be checked, and the worked rewrite of a draft that the
practice set leans on is missing.
To close: write the illustration (the five drafts and their rewrites) the figure describes, or redraw the figure from
material in the text.

**H3 · A-C02-2 · C02 (no `illustration.analogy_breaks_when`)**
As it stands: there is no "Where this picture breaks" block. The limit sits in the last must-know point.
What is missing: the section's limits block, which the released sections all have.
To close: add one when the illustration (H2) is written.

**H4 · A-C02-3 (residual) · C02 `definition.text` / `must_know[5].point`**
As it stands: "The exposure is what differs between the people being compared: something they have, do or meet."
What is missing: nowhere does the text say a question has one main exposure (it says one main outcome). "Risk factor"
is never defined. Ex 2 asks the reader to teach why "risk factors" is not an exposure.
To close: define "risk factor" and state the one-exposure rule next to the one-outcome rule.

**H5 · A-C02-5 · C02 `simplified_explanation` ("Obesity judged from measured weight and height is an outcome."); Practice 4**
What is missing: no cut-off for obesity or overweight is given for adults or children, and neither is the difference
between them (used in C07 and C08). B6 declines to give a cut-off. Practice 4 asks "say how the outcome is judged".
To close: give or point to a named, dated cut-off for adults and for children, with whose it is. Also say what
separates overweight from obesity.

**H6 · A-C02-7 · C02 `definition.text`**
As it stands: "It is bounded by place, by person (age, and any other trait that decides who is in) and by time."
What is wrong: it is ambiguous whether ages are required, or whether a trait such as "patients of one clinic" completes
the person fence (Practice 2b).
To close: say whether age is always required.

**H7 · A-C02-8 (residual) · C02 `simplified_explanation`**
As it stands: "The four parts have short names made from their first letters."
What is wrong: PICO and PECO are names for the whole set, not short names for each part. The original has the same
wording here, and the clearer "known by their initials" is in its definition.
To close: reword (minor).

**H8 · A-C02-9 · C02 Practice 6 (exercise)**
As it stands: "Say which part the report leaves unfenced."
What is wrong: both time and person (no ages) are unfenced, so the singular prompt does not fit its answer.
To close: make the prompt plural, or fence the person in the report sentence. This is an exercise, so it is outside
the compression pass.

## C03

**H9 · A-C03-2 · C03 `definition.text`**
As it stands: "A descriptive question asks how common an outcome is ... and in which people it is commoner. It names no exposure."
What is wrong: C02 defines exposure as "something they have", so a trait such as an age group could be read as an
exposure. Ex 1 Q4 and Q5 turn on where describe ends and relate begins.
To close: say that describing by personal traits (age, sex) is descriptive, and when a trait becomes an exposure.

**H10 · A-C03-4 · C03 `definition.text`**
As it stands: "This is the design that answers a causal question directly, wherever the exposure can be assigned."
What is missing: nothing for a cause question whose exposure cannot be assigned (night shifts, short sleep).
To close: say what evidence is used then, for example a cohort with time order and a way of handling third things,
and that it answers the question less directly.

**H11 · A-C03-5 (residual) · C03 `simplified_explanation`**
As it stands: "Chance does the deciding, not anything about the people. So no third thing can decide who is exposed."
What is missing: whether chance itself can leave the groups unequal, and what makes that unlikely (group size). There
is no worked case.
To close: one sentence on chance imbalance and group size, or a worked case.

**H12 · A-C03-6 (residual) · C03 `definition.text` and `simplified_explanation`**
As it stands: "A systematic review is a study of studies." appears in both fields. The final plain-terms text adds "It
collects and combines the results of all the studies already done on one question."
What is missing: which kind of question a review answers, and where it fits in the table. It is not linked to C05's
"reviews" or C06's "meta-analysis".
To close: remove the repetition, and link review and meta-analysis to the three kinds.

**H13 · A-C03-8 · C03 `simplified_explanation` (error)**
As it stands: "The count is the prevalence — how many people in a group have the condition."
What is wrong: every example asks for a share. Prevalence as a proportion is the usual definition, and A4 keeps counts
and percentages apart. The original has the same wording.
To close: define prevalence as the share (proportion) of the group with the condition at that time. Check the source.

**H14 · A-C03-9 (and A-X-1) · C03 (no illustration, no limits block)**
What is missing: no design is shown on a worked case. Nothing says a cohort starts with people who do not yet have the
outcome, which Ex 1 Q2 ("develop obesity") depends on.
To close: add a worked illustration, and state the outcome-free start of a cohort.

## C04

**H15 · A-C04-1 · C04 `definition.text`**
As it stands: "FINER is one published checklist ... credited to Hulley and colleagues."
What is missing: no title, year or source, so the reader cannot check the citation. I, N and R are never explained.
The original is no fuller ("Aslam and Emmanuel credit it to Hulley and colleagues").
To close: cite the work (author, title, year). Say what I, N and R mean, or say that later sections cover them (C05,
C07).

**H16 · A-C04-4 · C04 `simplified_explanation`**
As it stands: "People you can reach, in enough number."
What is missing: how to judge "enough". D6's square-root law is not connected here.
To close: point to how sample size is judged (D6, or a later rung).

**H17 · A-C04-5 · C04 `simplified_explanation`**
As it stands: "A way to measure the outcome."
What is missing: a way to measure the exposure. C04 Ex 2 and C08 Practice 3 (screen time) need it.
To close: add the exposure to the list line and to the definition.

**H18 · A-C04-6 · C04 `must_know[4].point`**
As it stands: "Before the main study, run a small trial of the hardest line, usually the measurement."
What is wrong: "trial" was just used in C03 for a randomised controlled trial. A pilot study is never named.
To close: call it a pilot, and define it in one line.

**H19 · A-C04-7 (residual, and A-X-1) · C04 `must_know[3].point`; Ex 3**
As it stands: "When narrowing turns a cause question into a relate question, say so in the protocol." Ex 3: "Reply as
you would to a health secretary".
What is missing: "protocol" and "health secretary" are never defined, and there is no illustration or limits block.
To close: gloss "protocol" at first use. Add a worked illustration running the two tests on one candidate.

## Across files

**H20 · A-X-1 · C02, C03, C04**
What is missing: no worked illustration in any of the three, in the original either (see H2, H3, H14, H19).
To close: an illustration per section on the running setting.

**H21 · A-X-2 · C01 to C04 (with C05 to C08)**
What is missing: nothing assembles what happens to the kept question: match it to a design (C03), pilot (C04), note
any narrowing in the protocol (C04), re-run the tests (C05), and ask again before writing up (C07). No sentence in the
C01 to C04 originals does this. The batch holding C08 may record the same hole.
To close: one closing list in C08 that names the next steps in order.

**H22 · A-X-3 (residual) · C02 `simplified_explanation`; C05, C06**
As it stands (restored): "When you search for what others have already found, you build the search from these same parts."
What is missing: a search method: where to search, how to turn the four parts into search terms, when to stop, and
how to tell a good existing answer from a weak one.
To close: a short worked search, in C05 or at a later rung, with a pointer from here.

# S55-R1 holes found by the compression pass, batch r2 (C05 to C08)

For the fixer and the audit. Each hole is absent from, or wrong in, the full-length original too,
so the restorer could not close it. Text quoted is as it stands in `-final-prose.yml` (or the
exercise/table in the record where noted).

**H1. C05 must_know[2] / definition.text; C08 table item 3; A-C05-1, A-C08-5, A-X-3.**
"Look for studies and reviews that have asked it before, and for counts that someone already holds."
Missing: how to look (which databases, what search terms, when to stop) and what makes an existing
answer "good" or "weak" (item 3 depends on it). Close with a short search method and two or three
criteria for "answered well".

**H2. C05 must_know[4].** "Design the study so that it is useful whichever answer comes back."
Asserted, never shown. Close with one worked line: two answers, and what each is used for.

**H3. C05 simplified_explanation.** "Beside each, write what someone would decide or do if that
answer came back." "Someone" is only made concrete in C07. Close with a forward pointer to C07 or
a named example.

**H4. C05 Exercise 1 item 2.** "Book 0 defined it as ..." No earlier book calls itself Book 0 to
the reader. Use the earlier book's reader-facing name, or the section.

**H5. C05, C06, C08 (no Illustration or "Where this picture breaks"); A-X-1, A-C05-5, A-C06-10.**
The tests of C05, the uncited-count reading of C06, and the ten-candidate sheet of C08 are never
run on a worked case. Close with a worked case in each.

**H6. C08 definition.text and table; A-C05-6, A-C08-2.** The five items omit C05's "in doubt" test,
C03's question–design match, and C04's money and equipment lines. Say whether this is deliberate,
or add them.

**H7. C06 definition.text.** "A 1990 report in Science found 55% of items ..." The database is not
named, so the three-labels rule cannot be applied to the headline error.

**H8. C06 definition.text and must_know[7].** "A 1990 report in Science", "a news feature in
Nature", "a peer-reviewed count". No authors, titles or issues (F3 cannot run); Science and Nature
not said to be journals; "peer-reviewed" undefined; the section asks for peer review while leaning
on a news feature. Give full references and one line on peer review.

**H9. C06 definition.text and must_know[5].** "One study held for this course" / "no held
measurement". "Held" is course-internal jargon. Replace with what was searched and found.

**H10. C06 must_know[3].** "Web of Science shows papers by Indian authors as less often cited than
papers from the United States and Europe." No figure and no source.

**H11. C06 Exercise 3.** "with your confidence stated". Stating confidence is taught nowhere.

**H12. C06 must_know[1].** "The belief that more than half of all papers are never cited ... goes
back to a 1990 count ... over only 5 years." The history of the belief is asserted without a
source.

**H13. C07 illustration.body.** "what share have a waist measurement above the camp's cut-off?"
The camp is deciding whether to start measuring waists, so it has no waist data and no waist cut-off.
The passing example fails feasibility. Rewrite the candidate (e.g. a pilot sample measured for the
study) or say where the waist data come from.

**H14. C07 illustration.body.** "if more than about one in ten are missed". Why a low-BMI,
large-waist adult counts as missed, and what the waist measure and its cut-off are, is never taught.

**H15. C07 illustration.analogy_breaks_when.** "A guideline group rarely acts on one study."
"Guideline group" undefined; not linked to systematic review or meta-analysis.

**H16. C07 must_know[6].** "Treat money from a party who gains from one answer with care." No
concrete action; deferred to the next book. Give one action (declare it, keep analysis independent).

**H17. C07 illustration.body; A-C07-7 with A-C02-5.** "have overweight or obesity". Overweight is
never distinguished from obesity, and it is unclear whether this is one outcome or two.

**H18. C08 table rows 4 and 5 against C07.** Item 4 = 1 for "a kind of body you cannot reach, such
as 'policy makers'" and item 5 = 1 for "different actions, but your guess" let a question survive
that C07 fails ("Name a role you could go and talk to"; "Do not guess Part 2"). Decide which binds.

**H19. C08 Figure.** "The ten made-up candidates, A to J". The candidates are never shown; the B/I
tie-break cannot be checked because item 4 scores are not given.

**H20. C08 table row 5.** Item 5 = 0 includes "nobody to ask"; item 5 = 1 is "your guess". An
unreachable body (item 4 = 1) always has nobody to ask, so item 5 = 1 can never arise with it.
Practice 2c and 7 turn on this.

**H21. C08 simplified_explanation.** "For each, write one line that names the item that decided
it." A rank rejection is decided by a total, not one item. Say what the line names then.

**H22. C08 simplified_explanation.** "If two totals tie, the one with more points on items 4 and 5
together goes first." No rule if that ties too.

**H23. C08 must_know[4].** "A percentage change between them measures nothing". Why ordered scores
cannot be divided is not explained.

**H24. C08 definition.text.** "This book's build" is course jargon.

**H25. C08 definition.text, item 4; Practice 2d.** "a decision in front of them". Unclear whether a
settled plan ("Dinner stays at 9 pm whatever you find") counts as a decision.

**H26. C08 (A-X-2, remainder).** After "Keep the top one." and the pointer to the next book, no
version says what a protocol is, who approves the kept question, or that a design is matched next.
