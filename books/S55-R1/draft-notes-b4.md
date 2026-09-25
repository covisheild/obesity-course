# S55-R1 draft notes, batch b4 (C07, C08)

## Records written

- `check/records/S55/S55-R1-C07.yml`: Who is waiting for this answer, and what will they do differently. Derivable, not quantitative. Three exercises (critique, design, teaching), all `skill_ref: S55-R1-K02`.
- `check/records/S55/S55-R1-C08.yml`: Ten candidates, one score each, nine rejections. Derivable, quantitative, 9 practice problems. Build exercise (K02) and a critique of rejection lines (K01).

`python check/build.py --check`: blocking 0 for the book as it stood at hand-back. Remaining warnings on my records are three long sentences, each a one-sentence research question quoted whole (splitting it would break the thing being taught).

## Sources

Every quote is from a held file and passed the build's quote check: `jhangiani_2019_methods` and `blackstone_2012` (ch. 4 only, blocks 15 and 17) as textbooks; `ratan_2019`, `ioannidis_2016_useful`, `ioannidis_2014_waste` as primary. No number is cited from any quote. Ioannidis 2014 is fair use only, so each quote is one sentence.

Nothing unsourced is stated as fact. Not stated anywhere: the Companies Act or CSR rules (C07 names CSR funds, programme grants and government tenders as names only and says this book says nothing about their rules), NMC thesis rules ("your degree does need a thesis" is said as the reader's circumstance, with no rule attached), the 85% waste figure, and any Chalmers paper.

**Decision for the conductor (C08 rule).** The brief says a zero on who-is-waiting rejects. The sheet applies the rule to item 4 **or** item 5, because C07 defines the test as two parts and says a question with the same action for every answer has nobody waiting. The sheet also says a 0 on item 4 forces a 0 on item 5, so in practice the item 5 score carries every rule rejection. If the conductor wants the rule on item 4 alone, change the definition, the simplified explanation, the illustration verdicts for A, C and G, practice 3, 4, 7 and 9, and the figure caption.

The scoring sheet is presented as the course's working tool. It is not tested, and it borrows no published checklist's name. FINERMAPS is named only as Ratan's list, in a reference note.

## Practice-set size

C08: 9 problems (levels 1, 2, 3, 4, 5, 7, 8, 9, 10). Five moves compose: scoring an item, totalling, applying the rule, breaking a tie, and writing the rejection line. Each move gets a mechanical or applied problem. Level 5 runs the other way (finding a smudged item from the total). Each diagnostic covers one of the two ways a sheet goes wrong: a total that hides a zero, and a 2 given on the scorer's own guess. Nine climbs the ladder without padding. `practice_note` in the record says the same.

All arithmetic was recomputed in `/home/claude/scratch-b4/recompute.py`: totals, the 50% and 20% rule shares, the tie-breaks, the smudged items, and 2/7 = 28.57%. The line "2 divided by 7 is about 0.2857" is written in words because the build's checker compares an unrounded left side at full precision.

## Figures

- C08: `s55-r1-c08-totals-and-item-5.png`, a bar chart drawn from the illustration's scored table (block 1): total and item 5 score for each candidate A to J. Drawn, 0 problems. The PNG has been looked at, and its bars match the table.
- C07: `figure_note` only. **Figure wanted** if the planner adds a diagram kind: a two-step flow showing Part 1 (name the waiting party), then Part 2 (action if the answer is high, action if it is low), then "different? pass / same? fail". Show both cases from the illustration: the school survey (same school plan both ways, fails) and the camp waist question (adds tape measures, or leaves the checklist, passes). No numbers except the officer's made-up "about one in ten".

Running `draw.py --book S55-R1` also redrew the C02 and C06 figures from their own specs. Nothing in their specs was touched.

## Glossary rows

None of these is in `prose/GLOSSARY.md` now. `value question` belongs to C04, and I use it in C04's sense.

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| conflict of interest | having something to gain from one result of a study | `S55-R1-C07` |
| CSR (corporate social responsibility) funds | a name for money companies spend on programmes; named only, the rules not taught here | `S55-R1-C07` |
| implementation money | money that pays to carry a programme out, as against money to find out an answer | `S55-R1-C07` |
| research money | money that pays to find out an answer | `S55-R1-C07` |
| scoring sheet (for candidate questions) | this course's five-item sheet, 0 to 2 points each, used to put candidate questions in order; not a tested scale | `S55-R1-C08` |
| who-is-waiting test | name the person or body who needs the answer for a decision; then say what they will do for each possible answer; it passes only if the actions differ | `S55-R1-C07` |

## Other caveats

- The candidates use the running setting (Raipur, Bilaspur, Durg, Korba, Bhilai, the district NCD camp and clinic). Every one is marked as made up. No real programme or school plan is described.
- G's note says "suppose your look found a recent national survey report that already gives a figure". It is framed as supposed, and no survey is named.
- C07's `concept_deps` are C02, C05 and C06. C08's are C01, C02, C04, C05 and C07. The cross-references ("the section on population, exposure and outcome", "the section on questions worth answering") were checked against those drafts as they stood.
