# Book 0 C24–C43: final verification (Task 4b)

Verifier: a fresh session that made none of the edits. Scope: `git diff c7ac0fe^ HEAD` plus the uncommitted changes to B0-R0-C36 (`git diff HEAD`). Nothing was edited except this file.

Result: **2 open**, everything else closed. `python check/build.py --check`: records 43, blocking 0, warnings 49.

## 1. Conductor items

- **C25-C1: closed.** Practice answer now reads "A household of four is covered or not covered as one draw". The double negative is gone and the sense matches the section 3(1) point beside it.
- **C38-R2a (conductor fix): closed.** simplified_explanation now reads "It also holds part of the small store." C36 defines the small store as glycogen "kept in the liver and in the muscles", so the liver holds part of it, not all of it. The next sentence ("packed away there as glycogen") still follows.
- **C41-C1: closed.** In `sources/constitution.txt`, every "Amendment) Act, 20.." footnote is from 2000–2006. That includes the entries split across two lines (lines 13034 and 13088 are 2003). The newest is the Ninety-fourth Amendment Act, 2006 (line 5162), and the Ninety-third Amendment Act, 2005 is at line 443. No Act from 2007 or later appears. 2016 − 2006 = 10, so the text reads "from 2006 … ten years after that". The file header, INDEX.yml (comment and do_not_cite `why`), SOURCES.md (both rows), claude.md and library.bib all now say "newest amendment it names: 2006", or the same thing in other words. B0-R0-C43's verified.note was also changed from 2003 to 2006. That change is correct but not listed in the C41 item. Stale "2003" wording is left only in history files: plan/S48-VERIFICATION.md and books/B0/compress/F3-*. They are not live text.
- **C36-C1: closed.** The restored sentence matches books/B0/compress/E6-prose.yml line 25 word for word. It sits right after the ATP sentences, so "its" refers to ATP. Two things support it. The record's openstax_biology_2e §7.1 quote covers terminal-phosphate removal, and the verified.note covers the released phosphate activating the molecule it binds.

## 2. STYLE-TIDY.md (22 pairs)

**All 22 closed.** Each pair matches the diff. Each split keeps the same claims, numbers and quotations.
- #4 and #11 add reader-address words only ("Check it yourself:", "yourself"). They add no claim.
- #7 (C33) leaves a verbless list sentence ("The flame, the air, …"). This is style only and does not change meaning.
- One small discrepancy: the file says there are 48 warnings after the tidy. The build now reports 49, both at HEAD and with the C36 change. This does not block.

## 3. GLOSSARY-EDITS.md (14 lines)

Every line matches the record. Status of each:

- C20 "careful statement": closed.
- C28 "That is the mean, which everyday speech calls the average.": closed. The record's own quote says "mean" and "average" are often used interchangeably.
- C31 atom sentence: closed. It is still grammatical. No later plain-layer text uses "nucleus", so nothing depends on the cut word.
- C37 "amino acids": closed. The next sentence already uses the term.
- C30 must_know "…as a biased sample: an error that…": closed.
- **C30 "an instrument never checked against something already known": OPEN.** The sentence still ends "It is a more confident wrong one." "Badly calibrated" meant the instrument was known to be off. "Never checked" only means nobody knows. The new sentence therefore claims that every unchecked instrument reads wrong, and neither the record nor its sources support that. Suggested fix: "on an instrument that reads off and was never checked against something already known". Another option: keep the idea of being off but gloss it differently.
- C35 "water-loving"/"water-hating" in definition.text: closed. openstax_biology_2e §5.1 uses both words. Deleting the illustration line loses nothing, because the definition, which comes first, now carries the gloss.
- C43 regulation sentence: closed.
- C39 "A number on its own": closed. It fits the "Forty-five could be…" line that follows.
- C38 "called islets" and "The same islets": closed.
- C38 "The islets notice. Blood sugar, meaning the glucose in the blood, is high, and … a beta cell, releases insulin.": closed, with one note. The rule ("when … is high") has become a narrative step ("is high, and"). It sits in the eat → rise → fall story, next to "Blood sugar falls.", so the meaning holds and the claim still rests on the "Elevated blood glucose levels stimulate the release of insulin" quote. A later style pass could restore "When".
- C38 "Adipose tissue, the large store from the section on metabolism": closed. C36 says "The large store is fat… The store is a tissue, and its name is adipose tissue." C38 depends on C36, and C38 uses "small store" and "large store" the same way C36 does.

## 4. prose/GLOSSARY.md: 25 rows (random.seed(7); random.sample of the 260 body rows)

Rows checked: origin, error, ribosome, blood sugar, checking a reference, sampling variation, logarithmic axis, work, gallbladder, molar mass, atom, starch, lacteals, crore, amino acid, bile, hydrophobic, hepatic portal circulation, average rate of change, deviation, bin, mean, hepatic portal vein, ATP, saturating.

- **24 closed.** Each named record exists, uses the term, and teaches what the row's plain words say.
- **atom (B0-R0-C31): OPEN.** The row says "the smallest piece of an element". C31 never teaches that. Its own verified.note says the source has no "An atom is …" sentence and describes only what an atom contains. Suggested fix: cut the row to "a tiny heavy centre with much lighter electrons around it", which is what C31 line 245 says.

## 5. Build

`python check/build.py --check`: records 43 | clusters 9 | blocking 0 | warnings 49. **Closed.**


## Conductor, closing VERIFY-final

- C30: "an instrument never checked against something already known" → "an instrument with a systematic error" (the sentence claims it reads wrong; only a systematic error licenses that; the term is taught in this section).
- GLOSSARY atom row: dropped "the smallest piece of an element", which C31 does not teach.
