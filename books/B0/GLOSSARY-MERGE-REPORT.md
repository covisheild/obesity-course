# Book 0 · glossary merge report (CONDUCTOR step 7)

23 September 2026. Merged `prose/glossary-inbox-D.md`, `prose/glossary-inbox-F2.md`, and the terms
Parts E, F1, F3, F4 and F5 teach into `prose/GLOSSARY.md`. The new section is at the end of that file,
headed "Added at the Book 0 glossary merge". Only `prose/GLOSSARY.md` and this report were edited. No
record was touched.

**Snapshot warning.** Records C24 to C28, C33, C37, C38, C40 and C42 had uncommitted edits in the
working tree while this ran, because another agent is editing them. Every quote below is from the
working tree as it stood during this run. Re-read each quote before applying an edit.

`python check/build.py --check`: 43 records, 0 blocking, 48 warnings, the same as before the merge.

## 1. Terms added

**103 rows: D 52, E 34, F 17.** Every row gives the record's own words, shortened, and the record
that first teaches the term. Existing rows were left alone because the file is append-only
(`PARALLEL.md`). Section 3 lists what needs changing in them.

| Part | Rows | Records |
| --- | --- | --- |
| D (inbox, rechecked) | 52 | C24 8 · C25 2 · C26 9 · C27 6 · C28 9 · C29 8 · C30 10 |
| E | 34 | C31 4 (energy, work, electron, ion) · C32 1 (net metabolizable energy) · C33 1 (energy balance) · C35 7 (cytoplasm, phospholipid, hydrophilic, hydrophobic, enzyme, ligand, signal transduction) · C36 6 (free energy, starch, monosaccharide, polysaccharide, small store, large store) · C37 4 (nucleotide, diploid, dominant, recessive) · C38 11 (capillaries, villi, hepatic portal vein, lacteals, general circulation, alimentary canal, hepatic portal circulation, gallbladder, pancreatic islets, extracellular fluid, lipolysis) |
| F1 | 1 | C39 table |
| F2 (inbox, rechecked) | 7 | C40 mark, value axis, pie chart, scale factor, bin, window, infographic |
| F3 | 2 | C41 reference, checking a reference |
| F4 | 2 | C42 argument, conclusion |
| F5 | 5 | C43 Constitution, Act, legislature, special majority, rule |

C34 adds no new term. Its terms were already in the glossary. "small store" and "large store" use
the 23 September wording. "near store" and "far store" appear in no record.

**Changes from the inboxes.** Compression and the fix rounds changed the records after the inboxes
were written, so the inbox wording was checked against each record again.

- **Dropped, because no record teaches the term now:** sampling bias (C29 keeps it only inside a
  source quote), self-selected sample, nonsampling error and measurand (both only in C30's
  references), true on average (used once in C30 practice and never glossed), contingency table
  (C26 now says only "two-way table"), whisker (cut from C40 in commit `df6a7bf`), and square law
  (C40's prose now says "scale factor squared", and "square law" survives only in `practice_note`).
- **Moved to a different record:** relative frequency now goes to **C27**. C24 no longer teaches
  it, so ruling M8's arrangement no longer holds.
- **Reworded to match the record:** independent, two-way table, cell, grand total, conditional
  probability, quartile, random error, resolution, scale factor and window. "mean (also average)"
  is now plain "mean", because C28 no longer says they are the same thing (conflict 3).
- **Added from F2's record:** value axis and pie chart. C40 defines both, and the F2 inbox did not
  list them.
- **zero error and correction** are taught only in C30's practice set, at lines 505 and 524. They
  are kept, and the rows point to C30.

## 2. Conflicts: one term, one thing

Each conflict below gives the record, the field, the quoted sentence and a proposed edit. None of
these edits has been applied.

**1. "nucleus" names two different things.** C31 `simplified_explanation`: "An atom has a tiny
heavy centre, called the nucleus, and a cloud of much lighter particles around it, called
electrons." C35 and the glossary use *nucleus* for the part of a cell that holds the DNA. The atom
sense is never used again.
*Edit C31:* "An atom has a tiny heavy centre, and a cloud of much lighter particles around it,
called electrons." This also stops the sentence introducing two terms at once (§10 rule 4).

**2. "cell" names two different things.** C26 `simplified_explanation`: "Where a row meets a column
is a count of people who are both — that count is a cell." C39 `simplified_explanation`: "A cell on
its own tells you nothing." C35 `definition`: "A cell is the smallest unit of a living thing".
Both senses are standard and C26's exercises depend on the table sense, so the glossary now carries
both, labelled. *Edit C39:* "A number on its own tells you nothing." That removes the one use that
is not needed. **Harsh to decide** whether to live with the two senses.

**3. "mean" and "average" name one thing, and nothing says so.** C28 `simplified_explanation`:
"Add them and divide by how many there are for the mean." C29 then uses "average" for the same
quantity throughout, in its `definition` ("Take the average of a random sample") and its
`simplified_explanation` ("work out its average"). C28's own name is "Average and spread".
*Edit C28:* "Add them and divide by how many there are. That is the mean, which everyday speech
calls the average."

**4. C30 points back to a term that C29 no longer teaches.** C30 `must_know`: "Measurement bias is
the VIM's own word (entry 2.18) for the same shape of problem." The "same shape" is sampling bias,
which C29 now shows only as "biased" ("A bigger sample is not a repair for a biased one.", in
`must_know`), and never glosses.
*Edit C30:* "Measurement bias is the VIM's own word (entry 2.18) for the same shape of problem as a
biased sample: an error that points one way and does not shrink when you collect more." Keep the
second sentence of that point, or merge it into this one.

**5. "calibrated" has two senses, and one use comes before the gloss.** C20 `exercises`: "Then give
them the calibrated statement." Here it means a claim sized to the evidence. C30
`simplified_explanation`: "A very careful, very repeated measurement on a badly calibrated
instrument is not a truer measurement." This comes before C32 glosses calibration, which it does
in `simplified_explanation`: "Doing this is called calibrating the machine".
*Edit C20:* "Then give them the careful statement." *Edit C30:* "…on an instrument never checked
against something already known is not a truer measurement." The existing **calibration** row
keeps `B0-R0-C32`. The D inbox wanted it moved to C30, but C30 no longer glosses the word.

**6. "building blocks" names two different things.** C37 `simplified_explanation`: "it fixes the
order of the building blocks in one protein". The glossary's **gene** row repeats this wording.
C35 calls the same things "links" ("The links of the chain are called amino acids"), and C35
`definition` uses "building blocks" for cells ("cells are the basic building blocks of all
organisms").
*Edit C37:* "it fixes the order of the amino acids in one protein". Change the gene row to match
in the between-rounds pass.

**7. "islands" and "islets" name one thing.** C38 `definition` says "pancreatic islets".
`simplified_explanation` says "Scattered through the pancreas are small islands of another kind of
cell.", then "The islands notice." and "The same islands notice that too." The glossary's **alpha
cell** and **beta cell** rows say "the islet cell".
*Edit C38:* "…small islands of another kind of cell, called islets." Then "The islets notice." and
"The same islets notice that too."

**8. "blood sugar" and "blood glucose" name one thing.** C38 `definition`: "Elevated blood glucose
stimulates the release of insulin." `simplified_explanation`: "When blood sugar is high, one kind
of cell in them, called a beta cell, releases insulin." The glossary's insulin and glucagon rows
use "blood sugar".
*Edit C38 simplified_explanation,* at the first use: "The islets notice. Blood sugar, meaning the
glucose in the blood, is high, and one kind of cell in them…". Or accept the split, since the
definition layer quotes the source. Low priority.

**9. adipose tissue is taught twice.** C36 `simplified_explanation`: "The store is a tissue, and its
name is adipose tissue." C38 `simplified_explanation` presents it as new: "Fat tissue has a proper
name: adipose tissue."
*Edit C38:* "Adipose tissue, the large store from the section on metabolism, makes hormones of its
own and puts them into the blood."

**10. "regulation", "rule" and "instrument" drift, the case §10 rule 2 names.** The glossary's
**regulation** row says "a rule written by a body that a statute gave the power to write rules",
using *rule* generically. C43 `definition` makes *rule* a different thing: "The Central Government
may make rules. A body that the statute creates may make regulations." C43 `illustration` uses
*instrument* before `must_know` glosses it: "The detail sits in a regulation — an instrument
written by a body the statute set up, not by Parliament." `must_know` then says: "Lawyers call any
one of them an instrument."
*Row change (between rounds):* regulation → "what a body the statute set up may make, not
Parliament". *Edit C43 illustration:* "The detail sits in a regulation, written by a body the
statute set up, not by Parliament." This leaves *instrument* to its gloss in `must_know`.

**11. "statute" and "Act" name one thing.** C43 `definition`: "Parliament and the State
Legislatures enact statutes, each called an Act." The record says the two are the same, and the
reader meets *Act* in every title. **No edit is recommended.** Both are listed, and the Act row
points to the statute.

**12. "energy equivalent" and "heat capacity" name one thing.** C34 `simplified_explanation`: "The
energy equivalent from that section is the calorimeter's heat capacity." The record reconciles the
two on purpose. **No edit.**

**13. "hydrophilic"/"hydrophobic" and "water-loving"/"water-hating" name the same things.** C35
`definition`: "hydrophilic, meaning it mixes with water". `simplified_explanation`: "The water-hating
ends turn inwards". The `illustration` joins them: "Hydrophilic means water-loving, and
hydrophobic means water-hating." That is two glosses for each term, against M20. *Edit C35
definition:* "hydrophilic, meaning water-loving: it mixes with water … hydrophobic, meaning
water-hating: it does not". Low priority.

## 3. Existing rows that are now wrong (for the between-rounds pass)

| Row | Problem | Proposed |
| --- | --- | --- |
| denominator | first used in C02, not C39. Two senses (A2 and A4), already noted in the file | point to `B0-R0-C02` and give both senses |
| precision | first used in C03, not C39 | point to `B0-R0-C03`. The measurement sense is now its own row |
| statute | C41 does not contain the word. C43 teaches it, and C01 ("Indian statutes") and C10 ("no statute makes it for you") use it before any gloss | point to `B0-R0-C43`, and gloss it at C01 or reword C01/C10 |
| regulation | C41 does not contain the word. C43 teaches it, and C12 uses "regulations" unglossed | point to `B0-R0-C43` and reword (conflict 10) |
| thermal equilibrium | C34 no longer teaches it. It appears only in a source note | delete the row, or restore the term to C34 |
| bilayer | C35's prose no longer uses the word ("a sheet two molecules thick") | delete the row |
| amino acid | C35 no longer says "twenty". It says "a small fixed set of kinds" | "one of a small fixed set of kinds of link a protein chain is built from" |
| consolidated, locator | C41 now uses them only in `exercises`, and neither is glossed | delete both rows, or gloss them in C41 |
| amendment | C41 `illustration` says "later changes stitched into the law" | take that wording |
| receptor | the row says "signalling molecule". C35 now calls it the ligand | "the protein a ligand fits into, which changes shape when it does" |
| hormone | the row says "puts into the blood". C38: "A chemical made in one part of the body that affects other parts some distance away", released into the extracellular fluid first | take C38's words |
| executive | the row says "the people who run the country day to day". C43: "the executive — the day-to-day running of government" | take C43's words |
| notification | the row says "an announcement in the Gazette that makes something take effect". C43 `must_know`: "an order issued under a power a statute gives, and published in the Gazette" | take C43's words |
| gene | "building blocks" | see conflict 6 |

**Outside this task's scope, but found.** The user brief says Parts A to C are already in the
glossary. **Parts B and C have no rows at all.** For example, C19 teaches slope, rise, run and
intercept, C20 teaches ceiling, C22 teaches running total, and C23 teaches stock, flow and net flow.
That harvest still needs doing.

## 4. whisker or error bar: ruling

**What the records say now: no record uses either term.** A search of `check/records/` for
"whisker", "error bar" and "error-bar" finds nothing, in either the working tree or HEAD. C40 used
to say "A point sometimes carries a short line through it, called a whisker. It shows either a
spread or an uncertainty, and the caption should say which. Read the caption for that. If the
caption does not say, you cannot read the whisker." Compression cut that paragraph in `df6a7bf`.
The copy in `books/B0/compress/F2-prose.yml` still has it. Part D never used "error bar", as the D
inbox confirmed, and Part D teaches no box plot.

**Ruling: use "error bar". Do not add a whisker row.**

- "Error bar" is the usual name for a line through a point that shows a spread or an uncertainty,
  and it is what the reader will meet in the papers this course prepares them for.
- In statistics, "whisker" means the lines of a box plot. The book's own source uses it that way
  (`sources/openstax_intro_stats_2e.txt` line 2896: "The long left whisker in the box plot…").
  Using it for an error bar would give one word two things as soon as a later rung teaches box
  plots.

**Record edits that make the book consistent: none are required.** Neither word appears anywhere,
so nothing is inconsistent. The F2 inbox's whisker row was not merged. **Harsh to decide:** whether
C40 should get the sentence back, since cold readers may meet error bars in the F2 figures and in
Part D's standard error. If it goes back, put it in C40 `simplified_explanation`, directly after
"Only then look at the shape.":

> A point sometimes carries a short line through it, called an error bar. It shows either a spread
> or an uncertainty, and the caption should say which. If the caption does not say, you cannot read
> the error bar.

If it goes back, also add this row to the glossary: `error bar | a short line through a point,
showing a spread or an uncertainty, which the caption should name | B0-R0-C40`. "Uncertainty" is
still never glossed in any record. C29 uses it only in its everyday sense.
