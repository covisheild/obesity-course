# Defects · Book 0 Part A (A1–A8)

Audit of `check/records/B0/B0-R0-C01.yml` to `B0-R0-C08.yml`, run 2026-09-20 against the files in
`sources/` and against the arithmetic itself. Every claim that names a statute was located by
searching the file; every calculation was recomputed.

The audit is against files, not a read-through. Five of the fourteen below read perfectly well and
are wrong or unsupported, and none of them would have been caught by reading the draft.

---

## 1 · C01 · `illustration.body` · the first search hit is not the section

**The claim.** "Search inside it for 'misleading advertisement'. Section 53 comes up. Read what it
says the penalty may extend to."

**What the file has.** `fss_act_2006.txt` gives two hits. The first, at line 183, is the entry in
the ARRANGEMENT OF SECTIONS at the top of the Act: `53. Penalty for misleading advertisement.` It
carries no penalty figure at all. The operative section is the second hit, at line 2911.

**Why it matters.** A reader who follows the instruction lands on a line that names section 53 and
contains nothing to read, and has no way of knowing they have not arrived. This is the exact
failure mode Book 0 F3 is about, arriving thirty-five sections earlier and unremarked.

**Smallest fix.** Say that the first hit is the list of section names at the top, and that the
reader keeps going to the second.

---

## 2 · C01 · `exercises[1].prompt` · who the proviso to section 50 covers

**The claim.** "A proviso lowers it to twenty-five thousand rupees for one group of sellers."

**What the file has.** The proviso at line 2891 applies to "the persons covered under sub-section
(2) of section 31". Section 31(2), at line 2049, covers a petty manufacturer, a petty retailer,
hawker, itinerant vendor, temporary stall holder, small scale or cottage industry and tiny food
business operator. Manufacturers are in it, so "sellers" is the wrong noun.

**Smallest fix.** "for small food businesses — petty retailers, hawkers, temporary stalls and the
like".

---

## 3 · C02 · `illustration.body` · a standard reported as what a child receives

**The claim.** "A child in lower primary classes gets a hot cooked meal of 450 calories and 12
grams of protein."

**What the file has.** Schedule II of `nfsa_2013.txt`, line 1428, sets "nutritional standards …
required to be met by providing" the meal. It fixes what a meal has to deliver. It says nothing
about what any child receives.

**Why it matters.** The section's own lesson is that a fraction has to know what its whole was, and
this sentence quietly converts a statutory standard into a delivered quantity in the first line of
the illustration. It is the same substitution the illustration goes on to criticise.

**Smallest fix.** "The standard for a lower primary hot cooked meal is 450 calories and 12 grams of
protein."

---

## 4 · C02 · `exercises[1].prompt` · the malnourished row covers a wider age band

**The claim.** "a take-home ration for children aged six months to three years of 500 calories. For
a malnourished child of the same age it gives 800 calories."

**What the file has.** Schedule II row 1 is "Children (6 months to 3 years)", 500 calories. Row 3 is
"Children (6 months to 6 years) who are malnourished", 800 calories. The bands are not the same.

**Smallest fix.** "For a malnourished child aged six months to six years it gives 800 calories."
The worked answer's closing sentence needs the same correction.

---

## 5 · C03 · `illustration.body` · the tenth decimal place is not a ten-thousandth of a gram

**The claim.** "Count the digits after the point. Ten of them. The last one is claiming to pin the
daily ration down to a ten-thousandth of a gram."

**What the arithmetic gives.** The tenth decimal place of a figure in kilograms is 10^-10 kg. A
kilogram is a thousand grams, so that is 10^-7 g — a ten-millionth of a gram, not a
ten-thousandth. The claim is out by a factor of a thousand.

**Why it matters.** It is a section about false precision, making a slip of three orders of
magnitude, in the sentence that names the problem.

**Smallest fix.** "a ten-millionth of a gram".

---

## 6 · C05 · `illustration.body` · "out by a factor of forty" is wrong

**The claim.** "About seventeen per cent, not seven hundred. The first answer was out by a factor
of forty."

**What the arithmetic gives.** The false claim was a ratio: thirty-five divided by five is seven,
so "seven times as much". The true ratio for a household of six is 35 ÷ 30 = 1.17. The false claim
overstates by 7 ÷ 1.17 = 6, not 40.

The 40 comes from setting "700 per cent" against "17 per cent", which mixes a ratio with a
percentage-more. And "seven times as much" is 600 per cent more, not 700, so even that comparison
is built on the wrong figure. Two errors of exactly the kind the section teaches the reader to
catch, inside the section.

**Smallest fix.** Delete both sentences and write: "Seventeen per cent more, not seven times as
much."

---

## 7 · C05 · `illustration.body` · the Antyodaya proviso is conditional and is quoted as flat

**The claim.** "A proviso just below sets a different figure for households covered by the
Antyodaya Anna Yojana: thirty-five kilograms of foodgrains per household per month."

**What the file has.** Lines 399 to 403 of `nfsa_2013.txt`: households under Antyodaya Anna Yojana shall,
"to such extent as may be specified by the Central Government for each State in the said scheme",
be entitled to thirty-five kilograms per household per month.

**Why it matters.** The qualifier is the difference between an entitlement the Act fixes and one
the Central Government fixes per State within the scheme. Dropping it makes a statement about
Indian food policy that the Act does not make, and the whole illustration is built on the figure.

**Smallest fix.** One clause: "thirty-five kilograms of foodgrains per household per month, to the
extent the Central Government specifies for each State under that scheme."

---

## 8 · C06 · `illustration.body` · the powers-of-ten ladder has a stranded annotation

**What is there.** The first row of the block reads
`10^1   10                one thousand is 10^3 in both`. The annotation belongs against 10^3 and
is sitting against 10^1, where it is simply false.

**Smallest fix.** Rebuild the block with each name against its own row and no floating annotation.

---

## 9 · C07 · `illustration.body` · three of the four search strings are not unique

**The claim.** "Now search for 'three lakh', then 'five lakh', then 'ten lakh'. Sections 52, 51 and
53 give you three more ceilings."

**What the file has.** In `fss_act_2006.txt`: "three lakh" has four hits and section 52's is the
second, at line 2905. "five lakh" has five hits and section 51's is the second, at 2899 — the
first, at 2889, is section 50's main ceiling, which is also five lakh. "ten lakh" has three hits.
Only "twenty-five thousand" is unique, with one hit at 2893.

**Why it matters.** A reader following the instruction will take the first hit and, for "five
lakh", will take section 50's figure while believing it is section 51's. Both are five lakh, so
nothing looks wrong. That is the whole problem.

**Smallest fix.** Have the reader search the section headings — "Penalty for misbranded food",
"Penalty for sub-standard food", "Penalty for misleading advertisement" — and warn, as in defect 1,
that the first hit is the contents list.

---

## 10 · C07 · `illustration.body` · "the whole ladder" and "this part of the Act" overstate

**The claims.** "The whole ladder of penalties, from the smallest to the largest, runs from 4.4 to
6.0." And: "The heaviest penalty in this part of the Act is about forty times the lightest."

**What the file has.** Chapter IX of `fss_act_2006.txt` carries penalties outside the four chosen,
including a fine of "not less than ten lakh rupees" at line 3004 and the compensation figures at
3081 to 3083. Four figures were selected; they are not the range of the chapter.

**Smallest fix.** Scope both sentences to the four figures written down: "The four you wrote down
run from 4.4 to 6.0", and "The heaviest of your four is about forty times the lightest."

---

## 11 · All eight records, currency · the source copies are of unstated and different vintage

**What the files have.** `fss_act_2006.txt` cites exactly one amending Act anywhere in it — Act 13
of 2008, with effect from 7 February 2008 — and nothing later. `nfsa_2013.txt` cites no amendment
at all. Neither file says on its face how current it is, and `sources/SOURCES.md` records the
enactment date of each and not the consolidation date.

**Why it matters.** Every penalty figure in C01 and C07 and every schedule figure in C02, C03, C04,
C05 and C08 is an institutional number taken out of a copy of unknown currency. This is precisely
the failure the finished record `B0-R0-C41` is built around, reproduced in Part A. It is not
repaired by opening the file, because opening it is what produced the figures.

**Three-part fix, and none of the parts is optional.**

1. Append a vintage note to `sources/SOURCES.md` recording the newest amendment each copy cites.
   `sources/` is append-only, so this is a new section under the table, not an edit to the rows.
2. Add one sentence to `analogy_breaks_when` in C01 and in C07 saying that these figures are what
   this copy of the Act says, and that a later section of this book teaches how to check whether a
   copy is up to date. A forward pointer is allowed; a silent dependency is not.
3. Record both files, with their vintage and a re-check trigger, in `HANDOVER.md`.

---

## 12 · C02 and C04 · the glossary's recorded words for "denominator" are never used

**What the corpus has.** `prose/GLOSSARY.md` records *denominator* as "the number a percentage is a
percentage of", first taught in `B0-R0-C39`. `PARALLEL.md` requires that a term already in the
glossary is taught in the words recorded there.

**What the records do.** C02 glosses it as "how many equal parts the whole was cut into", which is
right for a fraction and does not match the recorded words. C04 does not gloss it at all. So the
recorded wording appears nowhere in Part A, and a reader meets two unconnected senses.

**Smallest fix.** Keep C02's fraction gloss, which is where the reader first meets the word, and
add the recorded wording to C04 at the point the percentage sense arrives, so the two senses are
visibly the same word. The glossary row's "First taught in" column now points at the wrong record
and that is a between-rounds correction, not a mid-flight one: it goes to `HANDOVER.md`.

---

## 13 · C02 and C03 · first use of two glossary terms has moved

**What changed.** With Part A written, document order puts the first use of *denominator* in
`B0-R0-C02` and of *precision* in `B0-R0-C03`. `prose/GLOSSARY.md` records both against
`B0-R0-C39`, which is now the fourth section in which each appears.

**Smallest fix.** Nothing in the records. Both rows are corrected between rounds, per `PARALLEL.md`,
and the item is carried in `HANDOVER.md`. Recorded here so the next audit does not treat it as new.

---

## 14 · C08 · the build reports GUESS as an unexpanded acronym

**What the build says.** `python check/build.py --subject B0` prints: `[B0] used before anything
expands them: GUESS`. The word is the marker on the assumed inputs in C08's worked estimate, and
the acronym check reads any run of two to six capitals as an acronym.

**Why it matters, a little.** It is a false positive, and a false positive in a check is worse than
a missing check, because the next chat learns to skim that line.

**Smallest fix.** Mark the assumed inputs in lower case — `<- a guess` — which loses nothing and
clears the report.

---

## What was checked and is correct

Recorded so the next audit does not repeat it.

- Every arithmetic step in all eight records was recomputed. Apart from defects 5 and 6, all are
  correct, including the four logarithms in C07 (4.398, 5.477, 5.699, 6.000, shown to one place),
  the factor of forty from 6.0 − 1.6, √90 = 9.4868, 2.4 × 10^5 × 365 = 8.76 × 10^7, and every step
  of both order-of-magnitude estimates in C08.
- The Schedule II figures are in `nfsa_2013.txt` exactly as quoted: 450 and 12 for lower primary
  at line 1478, 700 and 20 for upper primary at line 1480, 500 for a take-home ration at six months
  to three years, and 800 for a malnourished child at six months to six years.
- Section 3(1) of the National Food Security Act, 2013 does give five kilograms per person per
  month to a person in a priority household, at line 388.
- The penalty ceilings quoted — five lakh at section 50 and section 51, three lakh at section 52,
  ten lakh at section 53, twenty-five thousand in the proviso to section 50 — are all present at
  the lines named, subject to defect 11.
- The search strings "NUTRITIONAL STANDARDS" (two hits, both in Schedule II) and "five kilograms"
  (two hits, both in section 3) do land where the records say they do.
- Schedule I of the National Food Security Act, 2013 fixes rice, wheat and coarse grain prices for
  three years from commencement and leaves the price after that to the Central Government. Those
  figures were deliberately not used anywhere in Part A, and should not be: the three-year window
  closed in 2016 and the file carries nothing later.
- No figure in Part A that is not in `illustration.numbers` is presented as a measurement. The
  teaching examples in C04 and C08 are named as made up in the text, following the precedent of the
  two-state table in `B0-R0-C39`, whose `numbers` list is likewise empty.
