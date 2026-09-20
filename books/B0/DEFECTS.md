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

---

# Second pass · the practice sets

Added 2026-09-20, after `claude.md` §7a made ten practice problems mandatory on every quantitative
concept and eighty were written for A1 to A8. Same method: every statutory figure located by
searching the file, every one of the eighty answers recomputed rather than read.

## 15 · C02 · `practice[5]` · a protein figure taken off the bottom of a range

**The claim.** "The same schedule sets protein at 12 grams for a lower primary meal, 20 for an
upper primary meal and 18 for a take-home ration." The worked answer then divided 12 by 18 to get
two thirds.

**What the file has.** Schedule II of `nfsa_2013.txt` gives the protein column as a **range** in
four of its six rows: 12–15 for children aged six months to three years, 12–15 for three to six
years, 20–25 for a malnourished child, and **18–20** for a pregnant woman or lactating mother.
Only rows 4 and 5 — lower primary at 12 and upper primary at 20 — give a single figure.

**Why it matters.** The problem silently picked the bottom of a range and then did exact
arithmetic on it. The answer, two thirds, is arithmetically right and rests on a choice the reader
was never told had been made. In a section whose whole lesson is that a fraction must know what
its whole was, this is the same defect one level down.

**Fix applied.** The problem now uses only single-figure entries — protein 12 against 20, and
calories 450 against 500 — and the worked answer ends by pointing out that four of the six protein
rows are ranges, so those are the only two that can be divided without declaring which end of a
range was taken.

## What was checked in the eighty answers and is correct

- **Every numeric step in all eighty answers was recomputed**, including the four logarithms in A7
  (log 4,800 = 3.681; log 25,000 = 4.398; log 3,00,000 = 5.477; 10^1.1 = 12.589), the compound
  percentage in A4 level 8 (100 → 80 → 96), the order-of-magnitude chains in A8, and the
  spreadsheet conversions in A6. All correct.
- **Every statutory figure newly quoted was located.** Consumer Protection Act, 2019: s.21(2) ten
  lakh and its proviso fifty lakh, at lines 1443 and 1447; s.34(1) one crore, at 1687; s.47 ten
  crore, at 2223. National Food Security Act, 2013: s.3(2) "up to seventy-five per cent of the
  rural population and up to fifty per cent of the urban population", at line 421; Schedule II
  600 calories for a pregnant woman or lactating mother, at 1482.
- **The "up to" in s.3(2) is carried into the answer rather than dropped.** A4 level 4 works out a
  ceiling and its answer says so in as many words: these are the most who may be covered, not a
  count and not a target. That qualifier is the same class of thing as defect 7 above, and it was
  written in rather than found missing.
- **`consumer_prot_2019.txt` was checked for vintage** the same way as the other two and cites no
  amending Act anywhere in it, so it reads as the Act as enacted in 2019. The row in
  `sources/SOURCES.md` that said "not yet checked this way" has been filled in.
- **Invented figures.** Three practice problems supply numbers that are not from any source: the
  household and population figures in A5 level 10, the district population in A8 level 5, and the
  population of India in A8 level 10. Each is marked in the working as a guess, or named in the
  answer as made up to show the move, following `B0-R0-C39`. None appears in
  `illustration.numbers` and none is presented as a fact. A8's entire method is labelled
  assumptions, so a marked guess there is the content rather than a lapse.
- **Problem conditions that are neither sourced nor guesses** — 250 households, 2,400 respondents,
  196 school days, 1,850 kilograms — are stated conditions of a made-up problem, in the way a
  textbook question states its own numbers. They make no claim about the world.

## One gap this audit cannot close, recorded rather than fixed

The numbers register, `check/_build/numbers_register.csv`, is built from `illustration.numbers`
only. A real figure quoted inside a practice problem names its citekey in `refs`, which the build
checks against `library.bib`, but it does not reach the register with a value and a unit. So the
register under-reports what the corpus quotes, by eighteen figures in Part A alone.

Two ways to close it, neither taken here because `check/build.py` is a between-rounds file and this
pass was already changing it once: give `practice[].refs` the same shape as
`illustration.numbers`, or have `reports()` walk practice refs and emit a row without a value. The
second is cheaper and honest about what it knows. Carried in `HANDOVER.md`.

---

# Found by the compression pass

Third pass, 20 September 2026. These came out of the cold read at step 5b and **none of them was
closable at step 5c**, because the full-length original does not fill them either. Restoring text
cannot fix a hole that was always there. They go back through the audit.

They are the class of defect the audit cannot see on its own. The audit checks claims against
sources; these are gaps *between* claims — a rule stated and never demonstrated, a term used and
never defined, a move an exercise requires that the text nowhere performs.

**Where the level numbers come from.** The cold reader worked all eighty practice problems, not
just the sixteen exercises, and reported each one as worked, worked-with-a-guess or
could-not-attempt. A hole in the teaching therefore shows up as a problem you cannot start, at a
known level. That is what the level numbers below are: the band of the §7a ladder where the
teaching actually failed, not an impression of difficulty.

| File | Practice verdict |
| --- | --- |
| A1 | worked 1–7, 9; guessed 8, 10 |
| A2 | worked 1, 4, 5, 6, 8; guessed 2, 3, 7, 9, 10 |
| A3 | worked 1, 4, 7; guessed 2, 3, 5, 6, 8, 9, 10 |
| A4 | worked 3, 5, 7, 8, 9, 10; guessed 1, 2, 4, 6 |
| A5 | worked 1–10 |
| A6 | worked 1, 3, 4, 7, 9, 10; guessed 2, 5, 6, 8 |
| A7 | worked 1–4, 6–10; **could not attempt 5** |
| A8 | worked 1, 3, 4, 5, 7, 8; guessed 2, 6, 9, 10 |

Read "guessed" as the dangerous verdict rather than the mild one. Exactly one problem in eighty
stopped the reader outright. Everywhere else a rule was imported that the text had not given, and
a correct-looking answer came out. A reader who could not import it produces a confident wrong
answer, not a blank — which is why a gap report is worth more than a completion rate.

## 16 · C07 · no inverse operation, and A6's definition of a power forbids one

**The only outright blockage in eighty problems: A7-P05, level 5.** It also makes the second half
of exercise E2 unanswerable and the section's own headline finding unverifiable by the reader.

`illustration.body` says *"That is a span of 1.6, and 1.6 powers of ten is a factor of about
forty."* Turning a difference of logarithms back into a multiplying factor needs ten raised to a
power that is not a whole number. C06 defines an exponent as a count of copies of the base being
multiplied together, under which `10^1.6` means nothing at all. C07 neither extends that
definition, nor names the inverse operation, nor says which calculator key performs it.

The reader can subtract to 1.08 on P05 and then has nowhere to go. Fix in C06 or C07, not by
deleting the claim: the "about forty" is what the whole illustration is for.

## 17 · C02 · the section tells the reader to compare and add fractions and never does either

**Blocks A2-P02 (2), P03 (3), P07 (7), P09 (9) and P10 (10) — half the set, spanning the ladder.**

`definition.text` carries *"To compare or add two, put them over the same denominator first."* The
illustration only ever simplifies. Nowhere in the section is there a worked instance of choosing a
common denominator, of multiplying each fraction up to it, or of what happens to the numerators
once they match.

P07 is the sharpest case and it is close to self-refuting: it is a find-the-broken-step problem
about an addition of fractions whose correct procedure the reader has never been shown.

A related, smaller hole in the same record: finding a common divisor is performed three times and
never taught. The illustration's two cues are *"both ended in a zero"* and *"both are in the five
times table"*; P01 offers 36/48, which fits neither. **"Times table" is itself used as a known
term** and nothing in C01 or C02 explains it.

## 18 · C03 · the significant-figure rule says where to start counting and never where to stop

**Blocks A3-P02 (2) outright and contaminates P05 (5), P06 (6) and P08 (8).**

`definition.text`: *"The significant figures of a number are the digits that carry information
about the quantity, counted from the first digit that is not zero."* Trailing zeros — the entire
difficulty — are never mentioned. Read literally the rule gives 450 → three figures and 1,200 →
four, which contradicts how the section itself treats 450 elsewhere.

Two more in the same record:

- **Rounding to a number of significant figures is never demonstrated**, only rounding to decimal
  places. **A3-P03 (3)** asks for three significant figures and P05 asks how many the answer
  deserves. The operation appears in the section only inside P07, which is the deliberately broken
  worked answer.
- **The exact-versus-measured rule and the significant-figure rule contradict each other**, and the
  section does not notice. *"Five kilograms in an Act is exactly five"* against *"a quantity
  calculated from other quantities cannot carry more significant figures than the least precise of
  them."* **A3-P05 (5)** sits exactly on the seam: 450 is an Act figure, so by the first rule the
  answer is exactly 88,200 and the question does not arise.
- **The exactly-five rounding edge is raised and abandoned.** *"When the digit you are dropping is
  exactly five and nothing follows it, the rule above always pushes up."* No alternative is given.
  **A3-P01 (1)** contains 7.2950, which lands on it. (The restore put back the original's
  statement of *why* that bias matters; it still does not say what to do instead.)

## 19 · C03 and the ordering of Part A · per cent is used three sections before it is defined

**Removes the whole top band of A3: P08 (8), P09 (9) and P10 (10) for a reader taking the sections
in order.** All three require computing or checking a percentage, and percentages are not defined
until C04.

The same fault, smaller, in three exercises: *"Record your confidence as a percentage before
turning to the answer"* appears on A1-E1, A2-E1 and A3-E1. It is the first instruction the reader
is given after the first exercise in the book, and it uses a term the course does not introduce for
three more sections.

This is a sequencing defect, not a content one. Swapping A3 and A4 fixes the practice problems and
leaves the confidence line, which wants rewording or moving.

## 20 · C04 · a percentage is never taken *of* anything

**Blocks A4-P02 (2), P04 (4) and the second half of P06 (6), and is needed for P08 and for E2.**

The only multiplication in C04 is a percentage of a percentage — *"0.40 times 0.30 is 0.12"* — where
both factors are percentages and the product is reported as a percentage. Turning a percentage into
a count of things is the commonest use there is and it appears nowhere in the section.

**Expressing one quantity as a percentage of another is missing in the same way.** The section
teaches percentage *change* — change over starting value — and nothing else. A4-P02 asks for 840 as
a percentage of 1,200, which is a different operation.

Two smaller ones in C04:

- **Percentages above 100 and below 1 are never mentioned**, and under C02's definition of a
  numerator as a count of parts of the whole, neither 125 per cent nor 0.5 per cent can be written
  at all. **Hits A4-P01 (1)** on two of its four items.
- **No must-know point carries the restriction on multiplying percentages.** The illustration is
  careful — *"Of those who do"* — but the point as stated is just that a percentage of a percentage
  multiplies, which would equally authorise multiplying two unrelated percentages.

## 21 · C01 · four holes under "count the digits", three of them at the bottom of the ladder

None blocked the cold reader outright and all four were filled by importing something. They sit at
levels 1, 3, 6 and 10, which is the shape of a section whose test set is harder than its teaching.

- **The place-name ladder below a lakh is never listed.** The reader is told each place is ten times
  the one to its right and is shown "five hundred" and "five". **A1-P01 (1)** asks what each digit
  of 90,807 is worth and the names have to be built by the reader.
- **Comparing two numbers of equal digit length is never demonstrated.** The section's whole method
  is counting digits, which ties for **A1-P03 (3)**.
- **Compound naming is never shown.** The section names single rungs and never composes one.
  **A1-P06 (6)** wants 45,000,000 as "four crore fifty lakh".
- **Billion is never given a value.** C01 uses the word twice and defines lakh, crore and million
  only. **A1-P10 (10)** turns entirely on that one conversion. The corpus does define it — in C06's
  ladder, five sections later. (That sentence had been cut and the restore put it back, so the
  definition now exists again at C06; the ordering problem is C01's and is not fixable there.)
- **A1-E2 asks the reader to say which step an error happened at**, and the section never decomposes
  a claim into steps in front of them. The illustration shows the error as a single wrong belief.

## 22 · C06 · roots are in the title and nowhere in the section's test set

The cut removed square roots entirely — the definition, the plain-terms paragraph, and the
"most square roots are not whole numbers" passage. **The cold read came back with nothing blocked
by their absence**, because not one exercise and not one of the ten practice problems touches a
root.

That is the finding, and it is not an argument for restoring them. A third of the section's title
has no test behind it. Either roots need an exercise and a place in the practice ladder, or they
belong in a different section. The restore left them out deliberately, so this is a live decision
rather than a description of the text: **C06 as it now stands does not teach roots at all.**

Smaller, in the same record:

- **Multiplying two numbers in scientific notation is never demonstrated.** Every worked instance
  multiplies or divides bare powers of ten, with the mantissa always 1. **Blocks A6-P05 (5) and
  P06 (6)**, and is needed to check E2. The reader is shown how to write 35,000 as 3.5 × 10^4 and
  never shown what to do with the 3.5 afterwards.
- **Arithmetic with negative numbers is taught nowhere in A1–A6.** C06 introduces negative
  exponents and then needs them added and ordered. **Hits A6-P02 (2)**, which needs 3 + (−1), and
  **P08 (8)**, which needs a larger exponent to mean a larger number when both are negative.
- **Converting a small decimal to scientific notation is not demonstrated.** The only worked case
  runs the other way. **A6-P03 (3)** includes 0.0047.
- **A6-E2 cannot be checked from what A6-E2 gives.** The multiplier between daily and annual
  production is never stated, so the reader must supply 365, or 360, or a count of working days, to
  check a step the exercise instructs them to check. Whether the intended fault is the arithmetic or
  the every-day-of-the-year assumption cannot be told from the wording.

## 23 · C08 · the method's load-bearing step needs a stock of known quantities the course never gives

**This is what stopped the reader on A8-P09 (9) and P10 (10), the two problems where the comparison
is the whole task.**

`illustration.analogy_breaks_when` is explicit that *"the method only works if the thing you compare
against is one you actually know."* Across all eight sections the reader is given almost nothing to
know: no population of India, no population of a typical state or district, no price of anything.
P09 needs the price of a glass of milk and P10 needs the population of India, and neither appears
anywhere in Part A.

C08 teaches the procedure and withholds the reference points that make the procedure work. The fix
is a short table of quantities a reader may hold — and it is a Book 0 decision, not a C08 one,
because the same table would sharpen A1-P10, A5-P10 and A6-P10 too.

Also in C08:

- **A tonne is never defined in any of the eight sections**, although tonnes appear in A5-E2 and
  A5-P09 and are required as an *output* by **A8-P06 (6)**.
- **The mixed-rounding case is never handled.** The section says *"round three numbers down and your
  answer is low"*. **A8-P02 (2)** asks whether an estimate is above or below the truth when one
  input was rounded down and one up, which needs the relative size of each rounding — a step the
  section never performs.
- **The definition of an order of magnitude and the estimating procedure are different operations
  and the text slides between them.** *"The power of ten nearest to it"* makes 450 into 10^3; the
  illustration writes *"450 calories, to one digit: 5 times 10^2"*. **A8-P01 (1)** asks for one and
  **P03 (3)** for the other, and the difference is never named.
- **A8-P04 tells the reader to "mark every input you were not given" and then gives every input.**
  Either it is a null case or the intended answer is the attendance assumption hidden in the word
  "receives", which nothing in the wording signals.

## 24 · C05 · three assertions the section never performs

A5 was the only section where every one of the ten problems was reachable from the text. These cost
the reader nothing and are still real.

- **Reducing a ratio is asserted, never performed.** *"Twelve grams against twenty grams is a ratio
  of twelve to twenty, or three to five."* The "or" does all the work. **A5-P01 (1)** is nothing but
  ratio reduction, and it only worked because C02 had shown the same operation on fractions — which
  C05 never says is the same operation.
- **A part-to-part ratio is never formed from a total.** **A5-P02 (2)** wants "lifting to not
  lifting" from "90 of 250"; every ratio in the section is between two quantities handed over
  directly.
- **A proportion is defined as running from zero to one and then never used.** No proportion appears
  in the illustration at all. **A5-P02 (2)** asks for one.
- **The numerator of a rate is never required to carry a label.** **A5-P06 (6)** says "48 events in
  a year" and never says what an event is. The section's whole discipline is interrogating the
  bottom of a rate; C02 established that a number with its label stripped off is not a number, and
  this problem strips the top.
- **A5-E1 requires the move the section warns against, without acknowledging it.** The record says
  converting per-household to per-person with an average assumes every household is average; E1 then
  hands the reader an average household size and asks for the entitlement. The right answer flags
  the assumption and nothing in the wording invites it.

## 25 · C02 · terms borrowed from the scheme vocabulary and never introduced

*Anganwadi*, *take-home ration*, *lactating mother* and *hot cooked meal* all arrive in C02's
illustration as though already defined, and *anganwadi* is needed to read **A2-P09 (9)**. C02 also
uses "a half" in P09 and P10 and never writes it as a fraction.

Under §11 rule 8 these are either terms of art that belong in `teach_once` with plain words at
first use, or decoration. They are currently neither.

## Two artefacts of the isolation method, recorded so nobody files them as defects

The cold reader worked from a directory holding the eight cut sections and nothing else, which is
what `claude.md` §12 requires. Two of its findings are consequences of that and not faults in the
corpus:

1. **"There is no appendix."** Every section ends by pointing at the appendix of worked answers,
   and the appendix is not in the scratch directory — deliberately, so that the reader had to work
   the eighty problems rather than read them back. It exists in the assembled booklet.
2. **"The source files do not exist."** A1, A2, A3, A5 and A7 instruct the reader to open and search
   `sources/fss_act_2006.txt` and `sources/nfsa_2013.txt`, and A1-P09 states flatly *"You have the
   Food Safety and Standards Act, 2006 open."* The checker did not. In every case the figure needed
   was also restated in the prose, so nothing was blocked — but the verification habit these
   sections are built around could not be performed, and no cold read run this way ever will be
   able to perform it. That is a limit on what step 5b can test, not a defect in the sections.

## One question for the contract, not a defect in the text

`claude.md` §12 says a compression pass that raised the mean sentence length has failed whatever
its word count says, and `PIPELINE.md` Task 5c repeats it as a check to run at the end. On A2 the
restore raised it, from 12.18 words to 12.35, while every surviving sentence is still the
original's own, word for word — which is checked mechanically and passes.

The rule is written against step 5a, where a rise means sentences were fused. At step 5c a rise can
also mean that the sentences the test proved load-bearing were long ones, which is what happened
here: C02's equivalence rule and the roti passage's missing step both run to 23 words. Part A as a
whole still falls, 12.54 to 12.13.

Someone has to decide whether the rule binds per section or per Part, and whether it binds 5c at
all. Left here rather than answered, because it is a change to the contract.
