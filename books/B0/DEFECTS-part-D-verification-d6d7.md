# Verification · Book 0 Part D fix pass, D6–D7 (`B0-R0-C29`, `B0-R0-C30`)

Audit of the fix pass, 2026-09-23. What was checked:

- The current records (HEAD `a9f8bfd`, working tree clean) against `DEFECTS-part-D-d6d7.md`, the
  fixer's appended "Resolution (fix pass)" section, and `DECISIONS-part-D-fix.md` (M5, M9–M14).
- Every number in every `working` block and in prose, and every `derived:` value, recomputed in
  python, including the seed-110 simulation and both scales' twenty readings.
- Every `quote` (21 in C29, 8 in C30), searched in its mapped file with the build's normalisation
  (whitespace collapsed, lower-cased), with line numbers. Every VIM and Kiran quotation inside the
  prose was compared by eye with `jcgm_vim3.txt` and `kiran_2022_muac_nc.txt`.
- The two figures: `check/figures/draw.py` (`d6_sample_means`, `d7_two_scales`) was run into a
  scratch folder. Both images are byte-identical to the committed PNGs and were compared with their
  captions and alt text.
- `python check/build.py --check` was run. It regenerates `check/_build/check_report.md`.
- Where the build places figures (`concept_md` in `check/build.py`): after "In plain terms" and
  before the Illustration.

No record was edited.

## Headline

**The fixer's "49 of 49 closed" is not true.** 34 of the 49 are closed, 15 are partly closed and
none is untouched. There are 32 new or still-open defects, listed in section 3: 15 in C29 and 17 in
C30.

- **M12 is not met in C29.** The two sentences the main thread found are there: L8 answer lines
  737–738 and L9 answer lines 778–779. The same problem is in four more places:
  - the illustration: "That figure is for India as a whole" (221), in the book's own voice;
  - the L9 answer: "NFHS-4's rounded planning figure for adults generally" (791–792);
  - the unit of the `19 and 21` number: "all adults";
  - five places that treat the study as a sample of India's adults, or treat 20 per cent as their
    true figure: 226, 234, 331–333 ("the survey's own 20 per cent"), 339, and L8's line 4 left
    undiagnosed.
- **The main thread's premise needs one correction.** The paper does give a place: "Prevalence of
  overweight in India was 19% in men and 21% in women in the National Family Health Survey—4"
  (source line 73). What it gives is **no age range and no population**. "As a whole", "generally"
  and "all adults" are the record's additions. The defect stands, but the fix wording has to allow
  "India".
- **Issue (b) is confirmed in C30.** "Sixty and a half kilograms, close to reading by reading" does
  not parse. The sentence after it, "an error of exactly the same size the whole way through", is
  false: scale A's errors run from 0.4 to 0.6 (V7-1).
- **The fixer's claims about its own work are wrong in three places:**
  - D6-4: it says a sentence explaining the abstract's 29.4 per cent was added. No such sentence
    exists.
  - D6-10: it says the prompt reads "a country of more than a billion people". The prompt says "a
    whole country".
  - Warnings: it says there are none. The build names C29 in one style warning.
- **Three of the fixer's new problems carry errors of their own:**
  - C29 L7 applies the square-root law to Kiran's volunteer men (V6-6).
  - C30's new L7 vouches for the trueness-as-accuracy line it was written to catch (V7-4).
  - C30 L10 calls invented data "real" (V7-7).
- **The arithmetic is clean.** Every working line and every derived value recomputes correctly.

---

## 1. Status of every original defect

| id | status | note |
| --- | --- | --- |
| D6-1 | partly | "Meant to estimate" is gone and no cause is asserted. The illustration still frames the study as a sample of India's adults: "They could not measure every adult in India. So they measured a sample instead" (226); "any one adult in India" (234); 331–339 (V6-2). |
| D6-2 | partly | "Planning figure" and "NFHS is itself a sample survey" are in. "The true 20 per cent" became "the survey's own 20 per cent" (333), but the survey printed 19 and 21, not 20. The population is still asserted in four places (V6-1, V6-2). |
| D6-3 | closed | NFHS-4 is dated 2015-16 at first mention. The NFHS-5 sentence was removed afterwards under M12, which overrides this part of the audit's fix. The study's own year is now missing (V6-12). |
| D6-4 | partly | The 83 quote is now Table 2's row. The explanatory sentence about the abstract's 29.4 per cent, which the fixer says it added, does not exist: `29.4` and `abstract` appear only inside quotes (V6-7). |
| D6-5 | closed | 98, 34.8, 14.8, 0.633 and 0.317 are registered as derived. The quote behind the simulation outputs does not say what the `derived:` field claims it says (V6-8). |
| D6-6 | partly | "Very unlikely", "plausibly" and "fairly close" are gone. The L9 answer still says "The gap between the two is real" and "the arithmetic supports a real difference" (V6-3). |
| D6-7 | partly | Line 1 is now called "worked out from Table 2". Line 2's diagnosis says "across India generally", which breaks M12. Line 4's "true national 20%" is never diagnosed (V6-1, V6-2). |
| D6-8 | closed | "Never squared" is stated, and the 3.407 → 11.607649 → 1520.602 working is shown. |
| D6-9 | closed | L5 and L6 now open with "Suppose", and L6 carries `refs`. The new L7 brings the same misuse back (V6-6). |
| D6-10 | partly | The prompt says "a whole country". The answer puts "A country of more than a billion" in quotation marks. That phrase is not in the prompt, and it carries an unsourced population figure (V6-14). |
| D6-11 | closed | The wording is as the audit gave it. The term "the anchor" reaches the reader (V6-10). |
| D6-12 | closed | |
| D6-13 | closed | 2 ÷ √10 and 2 ÷ √40 are shown. The generator, seed and draw order are in the `derived:` fields, and `draw.py` reproduces 0.633 and 0.317 from them. |
| D6-14 | partly | The population-size quote now backs a definition sentence. The two bias quotes were added. The standard-error quote is still a fragment with no subject, "is an example of a standard error…". The fixer calls it "the full sentence"; the subject was dropped because the file puts it in bold (V6-8). |
| D6-15 | closed | The definition matches M9. The glossary row is still for the main thread. |
| D6-16 | closed | |
| D6-17 | partly | Fixed in the illustration. The L9 answer still opens with `83 plus 15 = 98` and no sentence saying what 83 and 15 are (V6-13). |
| D6-18 | closed | |
| D6-19 | partly | The 1,128 figure was cut. The illustration still gives L8's diagnosis in words at 336–339: quadrupling shrinks the spread but moves the answer no closer. L9 repeats the illustration's 83 + 15 and 98 ÷ 282 (V6-13). |
| D6-20 | closed | |
| D6-21 | closed | There are now six points. The four-times rule is added and the clinical tag is corrected. |
| D6-22 | closed | |
| D6-23 | closed | |
| D6-24 | closed | |
| D6-25 | closed | The problem was added. It has an error of its own (V6-6). |
| D7-1 | closed | The DEXA and bioimpedance material and old `must_know[5]` are gone. Neither "gold" nor "DEXA" occurs anywhere in C30. |
| D7-2 | partly | Most places are fixed. "Accurate" is still made equal to "true on average" at 169 and 251–252. Definition 52 says "a reading … is called true on average". The new L7 vouches for "close average, so accurate" (V7-3, V7-4). |
| D7-3 | closed | All three sentences are fixed as the audit asked. A new false description of scale A replaced part of the text (V7-1). |
| D7-4 | partly | The body now says "Say the cause is a zero error". It still says "the error does not vary from reading to reading" (208–209). `numbers[2].unit` still says "the same on every reading, a zero error" (V7-2). |
| D7-5 | partly | The illustration, `must_know[2]` and L8 are fixed. `numbers[0].unit` still calls 100 g "the weighing scale's stated resolution" (V7-8). |
| D7-6 | closed | |
| D7-7 | closed | The term "the anchor" reaches the reader (V7-11). |
| D7-8 | closed | 2.13 is quoted whole, through "of a measurand". 2.16 uses the VIM's own "reference quantity value". 4.28 is named. All are verbatim against `jcgm_vim3.txt`. |
| D7-9 | closed | |
| D7-10 | partly | The "true weight" wording is gone and the break is named. The answer still says the rule "is stated correctly in the third line", which is the contradiction D7-10 was raised for (V7-5). |
| D7-11 | closed | Done differently, and it meets M10. The definition says "This section's glossary" (V7-14). |
| D7-12 | closed | C01 now teaches adding and subtracting negatives (C01 line 184). The one-line reason sits after the working rather than before it. |
| D7-13 | partly | °C and mmHg are fixed. "Calibrated" and "calibration" appear three times before the dash gloss, and that gloss defines "calibration weight", not "calibrate" (V7-10). |
| D7-14 | closed | |
| D7-15 | closed | L9 and L10 now compute, and L3 is at level 4. L9's "does not establish" paragraph is weak (V7-13). |
| D7-16 | partly | L3, L7, L8 and L10 are fixed. L6 still asks "on its own", which the audit named as the answer's shape (V7-12). |
| D7-17 | closed | |
| D7-18 | closed | 604.9 + 605.1 and 598.5 + 600.0 are correct row subtotals. |
| D7-19 | closed | The correction appears in `simplified_explanation` and `must_know[5]`, not in `definition.text` as the fixer says. That placement is fine. |
| D7-20 | closed | |
| D7-21 | closed | |
| D7-22 | closed | |
| D7-23 | closed | |
| D7-24 | closed | Two problems were added. The level-7 one has an error of its own (V7-4). |

**Totals:** 34 closed, 15 partly, 0 not closed (D6: 16 / 9 / 0; D7: 18 / 6 / 0).

---

## 2. Re-audit of what changed

**Arithmetic.** Every working line was recomputed in python and is correct.

- **C29, illustration:**
  - 83 + 15 = 98, and 98 ÷ 282 = 0.3475177305;
  - the gap is 14.75, printed as 14.8;
  - the population: sum 40, mean 5, squared deviations 32, 32 ÷ 8 = 4, √4 = 2;
  - the hand samples: 18/4.5, 15/3.75, 17/4.25;
  - 2 ÷ √10 = 0.63246 and 2 ÷ √40 = 0.31623;
  - 0.633 ÷ 2 = 0.3165.
- **C29, simulation.** `random.seed(110)`, one `random.choice` per draw, the 10s then the 40s:
  - population standard deviations 0.63304 and 0.31652, which round to the printed 0.633 and 0.317;
  - with n − 1, 0.63310 and 0.31655, the same to three places;
  - the means range from 3.0 to 7.6 for samples of 10 and from 4.0 to 6.175 for samples of 40, as
    the alt text says.
- **C29, practice:**
  - L1 5; L2 2 and 1; L3 5 and 25; L4 0.78;
  - L5 √131 = 11.4455, 0.3407 and 0.17035;
  - L6 39, 1521, 3.407, 11.607649 and 1520.602;
  - L7 (standard deviation misread) 20.3, 28.1, 0.3407, 23.86 and 24.54;
  - L7 (doubling) 14.142, 3.5355, and 71 per cent (0.7071);
  - L8 1,128 = 4 × 282;
  - L10 44.7214, 0.8944, 1414.2136 and 0.0283, a ratio of 31.62 ("about thirty-two").
- **C30, scales:**
  - A: rows 604.9 and 605.1, sum 1210.0, mean 60.5, readings 60.4 to 60.6, all within 0.1 of 60.5;
  - B: rows 598.5 and 600.0, sum 1198.5, mean 59.925, readings 58.7 to 60.7;
  - B has exactly two readings of 60.0, and 18 of its 20 readings are more than 0.1 from 60.0;
  - 0.075, 1.3, and A's largest single error of 0.6 are all as stated.
- **C30, the plain-terms example:** 61.2 − 60.5 = 0.7.
- **C30, practice:**
  - L1 −6; L2 3, 2, 4, 1, 5; L3 15, 3, 4, −3, −0.6, 9;
  - L4 0.3, 0.2, 0.4, 0.3, 0.3, sum 1.5, mean 0.3;
  - L5 −0.6, 0.6, −0.1, 0.3, 0.0, sum 0.2, mean 0.04, range 1.2;
  - L6 0.3; L7 (thermometer) 100.0;
  - L7 (40.05) 0.05, 200.25, 40.05;
  - L8 61.7, and 62.5 − 61.7 = 0.8, twice 0.4;
  - L9 250.1, 50.02, 0.02, 253.1, 50.62, 0.62. The ratio is **31**, which the prose calls "thirty
    times" (V7-13);
  - L10 differences 0.4, 0.4, 0.5, 0.3, 0.3, sum 1.9, mean 0.38.

**Quotes.** All 29 are present exactly once in the mapped file, and none matches only the Kiran
file's curator header.

- C29 definition quotes are at OpenStax lines 111, 123, 126, 604, 701, 885, 1053, 731, 896, 5022
  and 2599. Every locator names the right section.
- The C29 Kiran numbers are at lines 102, 42, 73, 295 and 303.
- The C30 quotes are at OpenStax 723 and 725, Kiran 115, and VIM 67, 179 and 102.
- VIM quotations inside the prose are verbatim: 2.13 (whole), 2.14, 2.15, 2.16, 2.17, 2.19 and
  4.14. Also verbatim are the Kiran quotations "Weight and height were recorded with accuracy of
  100 g and 0.1 cm" and "was single observer measurements with minimum inter-observer variation".
  The "1 mm precision" in C30 L8 is a fair paraphrase of line 125.

**States-the-number rule (M13).**

- Every non-derived entry with a numeric value states its number: 20, 282, 83, 15 and 100.
- `19 and 21` is not numeric, so the build does not test it. Its quote does state both numbers, but
  it drops "NFHS-4" and the 2015–16 date that the prose rests on it (V6-8).
- Every derived entry names its derivation.
- Two problems remain:
  - The simulation outputs quote an OpenStax passage that does not state the law their `derived:`
    field says it states (V6-8).
  - C30's five stated-case numbers are registered under `jcgm_vim3`. The build therefore tells the
    reader these figures come from the VIM (V7-9).

**Build.** 0 blocking, 73 warnings.

- C29 is named 6 times:
  - one real style warning, a 32-word sentence at "The figure below was made that way…" (V6-11);
  - five derived-number notices, which report as designed.
- C30 is named 5 times, all derived-number notices.
- C30 L10 prompt reads at grade 8.9, under the limit.
- No acronym warning names either record:
  - NFHS is expanded at 219–220;
  - VIM is expanded at first use, in the definition;
  - mmHg and °C are spelled out in words.

**The main thread's post-fix edits.**

- **NFHS-5 removed.** It is gone from both prose and numbers, cleanly. The "different year"
  candidate now has no study year beside it (V6-12).
- **The "run Python" paragraph replaced.** The new text says "The figure below". The build renders
  figures before the Illustration, so the figure is **above** that sentence. That sentence also
  causes the only real C29 warning (V6-11).
- **Figures.**
  - `d6_sample_means` reads the population from the record and stops if its draw departs from the
    registered 0.633 and 0.317.
  - `d7_two_scales` reads both tables from the record.
  - Image, caption and alt text agree with the record, except the C30 caption's "all of it half a
    kilogram too high" (V7-1).
- **Acronym expansions.** Correct. They introduce no new defect.

**§9.** No breach in either record. C29 L9 uses the weight adjective only inside the claim the
reader takes apart, and the answer restates it with body-mass index.

---

## 3. New or still-open defects

### C29

**V6-1**
- **Fields:**
  - `illustration.body` 221–222;
  - `practice[L8].answer` 737–738;
  - `practice[L9].answer` 778–779 and 790–792;
  - `illustration.numbers[2].unit`.
- **Claim:**
  - "That figure is for India as a whole, with no age group named";
  - "for men and women across India generally" (twice);
  - "NFHS-4's rounded planning figure for adults generally";
  - the unit: "all adults, no age group named".
- **What the source says:** "Prevalence of overweight in India was 19% in men and 21% in women in
  the National Family Health Survey—4 (NFHS-4, 2015–16)" (Kiran, line 73). It names the country but
  gives no ages and no population. M12 forbids presenting any NFHS figure as a fact about India.
  "As a whole", "generally" and "all adults" add a population the paper never states. Line 221 says
  it in the book's own voice. At 791 the rounding is also given to NFHS-4, when it was the authors'.
- **Smallest fix.** In each place, write "which the paper reports as NFHS-4's figures for India,
  without saying which ages or which people they cover". At 791–792, write "…than the 20 per cent
  the authors rounded from the paper's NFHS-4 figures". Unit: "per cent, NFHS-4's prevalence of
  overweight in men and in women, as the paper reports it; no age group or population given".
- **Severity:** error.

**V6-2**
- **Fields:** `illustration.body` 226, 234, 331–333 and 339; `practice[L8].answer`.
- **Claim:**
  - "They could not measure every adult in India. So they measured a sample instead";
  - "chance of including any one adult in India";
  - "how close a sample this size sits to the survey's own 20 per cent";
  - "closer to the adults of India who never had a chance of being asked";
  - L8's line 4, "the true national 20%", is left undiagnosed.
- **What the source says:** the paper's objective was cut-offs "in young adults". Its 20 per cent is
  the authors' planning value; NFHS printed 19 and 21. Under D6-1 and M12 it is neither a true value
  nor a figure for India's adults. These sentences still cast the study as a sample of India's
  adults and cast 20 per cent as their true figure.
- **Smallest fix:**
  - 226: "They measured a sample: 282 medical students…" (drop the first sentence).
  - 234: "…chance of including any one young adult, the group the paper set out to study, is neither
    equal nor known."
  - 333: "…how close a sample this size sits to the figure for the population it was drawn from."
  - 339: "…closer to people who never had a chance of being asked."
  - In the L8 answer, add: "Line 4 also calls 20 per cent the true national figure. It is the
    authors' rounded planning number, not a true value."
- **Severity:** error.

**V6-3**
- **Field:** `practice[L9].answer`.
- **Claim:** "The gap between the two is real: about fifteen percentage points." Also: "So the
  arithmetic supports a real difference between this sample's figure and NFHS-4's."
- **Problem:** "Real" says the gap is more than sampling variation. Judging that needs the spread of
  a proportion, which the audit showed is not taught (D6-6). It is also the same kind of judgement
  D6-6 removed from the rest of the record.
- **Smallest fix:** "The two printed figures differ by about fifteen percentage points." Then: "So
  the arithmetic shows a difference between this sample's figure and the planning figure."
- **Severity:** error.

**V6-4**
- **Field:** `practice[L8].answer`, 747–748.
- **Claim:** "It could be the rounding in the second line." This is offered as one possible cause of
  the 14.8-point gap.
- **Arithmetic:** Rounding 19 and 21 to 20 moves the comparison by at most one point. 34.8 − 21 =
  13.8 and 34.8 − 19 = 15.8. Rounding cannot produce the gap.
- **Smallest fix:** delete the sentence. Or write: "The rounding in the second line moves it by at
  most a point either way."
- **Severity:** error.

**V6-5**
- **Field:** `practice[L9].answer`, 796.
- **Claim:** "People who volunteer for a free health check may differ from those who do not."
- **What the source says:** nothing about a health check, free or otherwise. "The study objectives
  were disseminated in the campus and the participants were invited to come to a designated
  anthropometric measurement room" (line 103ff).
- **Smallest fix:** "People who choose to come forward for a study may differ from those who do
  not."
- **Severity:** error (sourcing).

**V6-6**
- **Field:** `practice[L7, standard deviation read as the spread of the mean]`, new under D6-25.
- **Claim:**
  - "A different question is how far the sample's own mean, 24.2, might sit from the true mean of
    the wider population. … The square-root law gives that from the same two numbers."
  - "An interval built from that figure would run from about 23.86 to about 24.54."
- **Problems:**
  - The 131 men volunteered. The record's own boundary point, `must_know[3]`, and the D6-9 fix say
    the law describes only a random sample.
  - 3.9 is a sample standard deviation, used here as the population's with no "suppose".
  - The answer replaces the colleague's wrong interval with another unqualified one. A reader will
    take 23.86–24.54 as "where the true mean lies", which is the same mistake made narrower. That is
    also S03 material.
- **Smallest fix:**
  - Open the working with: "Suppose, for the moment, that these 131 men were a random sample from a
    population whose spread is 3.9."
  - Replace the interval sentence with: "That 0.34 describes random samples. These men volunteered,
    so it says nothing about how far 24.2 sits from any wider population's mean."
- **Severity:** error.

**V6-7**
- **Field:** `illustration.body`, the remainder of D6-4.
- **Claim:** the fixer says "a sentence explains the abstract's 29.4 per cent versus the 34.8 per
  cent". There is no such sentence.
- **What the source says:** the abstract reads "Of the 282 participants, 83 (29.4%) were overweight"
  under a "BMI ≥25" definition. A reader who opens the paper meets that first. M12 allows the record
  to say so.
- **Smallest fix:** after the Table 2 working, add: "The paper's abstract calls these 83, 29.4 per
  cent, 'overweight', having defined overweight as 25 or more. Table 2 shows the 83 are only the 25
  to 29.9 band."
- **Severity:** sourcing.

**V6-8**
- **Fields:**
  - `illustration.numbers[2]` (19 and 21);
  - `numbers[8]` and `numbers[9]` (0.633 and 0.317);
  - `definition.references[11]`.
- **Problems:**
  1. The 19-and-21 quote, "was 19% in men and 21% in women in the National Family Health", leaves
     out "NFHS-4", "overweight" and "2015–16". Those are what the illustration uses it for ("NFHS-4,
     run in 2015-16").
  2. The simulation entries say "verifies the square-root law this citation states". The quoted 2.7
     passage defines the standard error and does not state the law; the 7.1 quote does. Also,
     because both carry `citekey: openstax_intro_stats_2e`, the build prints "Figures quoted in this
     illustration are from [OpenStax]" for a simulation output (`mark_numbers`).
  3. D6-14 remainder: reference 11 is still a subject-less fragment. The subject is missing because
     the file bolds it.
- **Smallest fix** (each quote below passes the normalised search exactly once):
  1. Quote `Prevalence of overweight in India was 19% in men and 21% in women in the National Family
     Health Survey—4 (NFHS-4, 2015–16)`.
  2. Either quote the 7.1 sentence and reword to "checks the square-root law stated at 7.1", or,
     better, drop the two simulation outputs from `numbers[]`. They are not figures from any source.
     This wants a main-thread ruling under M13 (see also V7-9).
  3. Quote `The **standard error of the mean** is an example of a standard error. It is a special
     standard deviation and is known as the standard deviation of the sampling distribution of the
     mean.` with the asterisks, as they are in the file.
- **Severity:** sourcing.

**V6-9**
- **Field:** `illustration.body` 223–224.
- **Claim:** "NFHS is itself a sample survey, so its own figure is an estimate."
- **Problem:** No held source says how NFHS chooses its people. The paper gives only the survey's name
  and a reference to the IIPS report. The claim is true in fact, but it comes from model knowledge
  (§7b). It was added at the audit's suggestion.
- **Smallest fix:** "Its figure is itself a survey result that reaches this book second-hand, through
  the paper, not a fixed truth." Or hold the IIPS NFHS-4 report in `sources/` and cite it.
- **Severity:** sourcing.

**V6-10**
- **Field:** `illustration.body` 232.
- **Claim:** "which the anchor calls a self-selected sample".
- **Problem:** "The anchor" is pipeline vocabulary. The reader has never been told what it is. This
  is the same defect as V5-4 in the D4–D5 verification.
- **Smallest fix:** "which the statistics textbook this book follows calls a self-selected sample".
- **Severity:** floor.

**V6-11**
- **Field:** `illustration.body` 305–307, from the main thread's edit.
- **Claim:** "The figure below was made that way: 5,000 samples of size 10 from this same
  eight-number population, each number put back after it is drawn, and then 5,000 samples of size
  40."
- **Problems:**
  - `concept_md` renders `figures` after "In plain terms" and **before** the Illustration, so the
    figure is above this sentence.
  - The sentence is 32 words long, and it is the build's only real warning on C29. The fixer
    reported none.
- **Smallest fix:** "The figure above the illustration was made that way. It shows 5,000 samples of
  size 10 from this same eight-number population, each number put back after it is drawn. Then it
  shows 5,000 samples of size 40."
- **Severity:** floor.

**V6-12**
- **Fields:** `illustration.body` 342–344; `practice[L8].answer` 748.
- **Claim:** "the years between when the study ran and when NFHS-4 was measured"; "the years between
  the two surveys".
- **Problems:**
  - Since NFHS-5 was removed, C29 never says when the study ran: July–September 2019, source line
    100.
  - The study is not a survey.
- **Smallest fix:** after "run in 2015-16", add "The study itself ran in July to September 2019."
  In L8, write "the years between NFHS-4 and this study".
- **Severity:** style.

**V6-13**
- **Fields:** `illustration.body` 336–339; `practice[L9].answer` 772–775. This is what remains of
  D6-17 and D6-19.
- **Problems:**
  - The illustration still gives L8's diagnosis in words: "Multiplying the invitation by four would
    shrink the spread … It would not move that answer one step closer".
  - L9 repeats the illustration's 83 + 15 and 98 ÷ 282. Its working comes before any sentence saying
    what 83 and 15 are.
- **Smallest fix:**
  - Cut the two sentences at 337–339 from the illustration. L8's answer already makes the point.
  - In L9, put "Table 2 puts 83 students at 25 to 29.9 and 15 at 30 or more." before the working.
- **Severity:** style.

**V6-14**
- **Field:** `practice[L10].answer` 842.
- **Claim:** "'A country of more than a billion' sounds like it should demand a bigger sample."
- **Problem:** The prompt says "a whole country". The phrase in quotation marks appears nowhere, and
  it reintroduces an unsourced population figure. The fixer's resolution misreports the prompt
  wording.
- **Smallest fix:** "'A whole country' sounds like it should demand a bigger sample."
- **Severity:** style.

**V6-15**
- **Field:** `exercises[0].answer`.
- **Claim:** "They are more engaged, more online, probably younger and more urban than the
  hospital's whole patient population."
- **Problem:** This asserts facts about a group with no source. Only "probably" is hedged. The audit
  did not touch this line.
- **Smallest fix:** "They may be more engaged, more online, younger or more urban than the
  hospital's whole patient population."
- **Severity:** style.

### C30

**V7-1**
- **Fields:** `illustration.body` 198–199; `figures[0].caption`.
- **Claim:**
  - "Sixty and a half kilograms, close to reading by reading." This is the main thread's issue (b).
  - "Against the known 60.0 kilograms, that is an error of exactly the same size the whole way
    through."
  - Caption: "all of it half a kilogram too high".
- **Arithmetic:**
  - The first sentence does not parse.
  - The second is false. Scale A's errors are 0.4 twice, 0.6 twice and 0.5 sixteen times.
  - The caption overstates in the same way.
- **Smallest fix:**
  - Body: "Sixty and a half kilograms, and no single reading is more than a tenth of a kilogram from
    it. Against the known 60.0 kilograms, every reading is 0.4 to 0.6 kilograms high, and the
    average is 0.5 high."
  - Caption: "about half a kilogram too high".
- **Severity:** error.

**V7-2**
- **Fields:**
  - `illustration.body` 208–209;
  - `illustration.numbers[2]` (0.5), `unit` and `derived`.
  This is what remains of D7-4.
- **Claim:**
  - "No amount of repeating the weighing removes it, because the error does not vary from reading to
    reading."
  - Unit: "the same on every reading, a zero error".
  - Derived: "illustrates VIM 4.28 zero error".
- **Problems:**
  - The error does vary, by ±0.1.
  - VIM 4.28 is the error "where the specified measured quantity value is zero". These readings are
    at 60 kg, and the body now says rightly that they "could not show that by themselves".
- **Smallest fix:**
  - Body: "because this part of the error does not vary from reading to reading".
  - Unit: "kilograms, scale A's average error against the stated 60.0 kilogram reference".
  - Derived: "…; illustrates a systematic error (VIM 2.17)". Change the quote to match:
    `component of measurement error that in replicate measurements remains constant or varies in a
    predictable manner`.
- **Severity:** error.

**V7-3**
- **Fields:** `illustration.body` 169; `illustration.analogy_breaks_when` 251–252; `definition.text`
  52. This is what remains of D7-2.
- **Claim:**
  - "Was the scale also accurate — did it read true, on average, against a correctly calibrated
    reference?"
  - "You check an instrument's accuracy once … using exactly this arithmetic". That arithmetic is an
    average error, which is trueness.
  - "A reading, or a set of readings, is called true on average". A single reading has no average.
- **What the source says:** VIM 2.13 Note 2 and 2.14 Note 3 forbid using "accuracy" for trueness.
- **Smallest fix:**
  - 169: "Was the scale also true on average, against a correctly calibrated reference?"
  - 252: "check an instrument's trueness once, in advance…"
  - 52: "A set of readings is called true on average…"
- **Severity:** error.

**V7-4**
- **Field:** `practice[L7, 40.05 kg]`, new under D7-24.
- **Claim:** The prompt's line 3 is "the average is close to the true weight, so the scale is
  accurate". The answer says "The first three lines are fine".
- **Problems:**
  - Line 3 is exactly the trueness-called-accuracy error this problem was added to drill (D7-24,
    failure mode 1).
  - The answer vouches for line 3, then admits in "why it looks reasonable" that "accurate" is used
    loosely there.
  - The answer's opening working line comes before any sentence.
- **Smallest fix:** "The first two lines are fine: an average 0.05 kg from the truth is good
  trueness (VIM 2.14). Line 3 is where it starts to break: a close average shows trueness, not
  accuracy. Line 4 then draws the conclusion that the mislabel invites."
- **Severity:** error.

**V7-5**
- **Field:** `practice[L7, thermometer].answer` 582–583. This is what remains of D7-10.
- **Claim:** "'averaging reduces error' is a true and useful rule, and it is stated correctly in the
  third line." The same answer has already named line 3 as the break.
- **Smallest fix:** "'averaging reduces error' is true of random error, and the third line states it
  as if it were true of all error."
- **Severity:** error.

**V7-6**
- **Field:** `practice[L8, neck circumference].answer` 640–641.
- **Claim:** "The paper's methods describe one measurement per participant, taken by a tape marked in
  millimetres."
- **What the source says:**
  - The methods name no instrument for neck circumference. The SECA 201 tape is named for arm
    circumference (line 122).
  - The methods do not say how many times the neck was measured.
  - The discussion calls for "standardized neck tapes" (line 719).
- **Smallest fix:** "The paper's methods do not name the instrument used on the neck, and report no
  repeat measurement." Then keep "'With 1 mm precision' most likely names the step…".
- **Severity:** error (sourcing).

**V7-7**
- **Field:** `practice[L10]` prompt and answer.
- **Claim:** The prompt says "A second observer now measures the same five people", with no
  "suppose". The answer says "It shows that two real observers, measuring the same real necks, can
  disagree…".
- **Problem:** The ten readings are invented for the problem. They are not in the paper, yet the
  problem carries `refs: kiran_2022_muac_nc`. §7a requires real figures or none. Calling stated data
  "real" is the defect §7a names.
- **Smallest fix:**
  - Prompt: "Suppose a second observer measures five people, and both observers measure neck
    circumference in cm."
  - Answer: "It shows that two observers, measuring the same necks, can disagree…".
- **Severity:** error.

**V7-8**
- **Field:** `illustration.numbers[0].unit`. This is what remains of D7-5.
- **Claim:** "grams, the weighing scale's stated resolution (called 'accuracy' in the paper's own
  words)".
- **What the source says:** "recorded with accuracy of 100 g". That is a recording step. The paper
  states no resolution, which is the distinction D7-5 made and the body now makes correctly.
- **Smallest fix:** "grams, the step weights were recorded in (the paper calls it 'accuracy')".
- **Severity:** sourcing.

**V7-9**
- **Field:** `illustration.numbers[1..5]` (60.5, 0.5, 59.925, 0.075, 1.3).
- **Problem:** These are stated-case numbers, "from the stated worked example", registered under
  `citekey: jcgm_vim3`. `mark_numbers` in `build.py` then prints "Figures quoted in this illustration
  are from [Kiran, VIM]". The reader is told the VIM supplied figures that the record made up. No
  other record registers stated-case numbers this way.
- **Smallest fix:** remove the five entries. §7a: stated numbers say nothing about the world and need
  no source. Only 100 g is a real figure. Or have the main thread rule under M13 how stated and
  simulated numbers are handled (with V6-8, item 2).
- **Severity:** sourcing.

**V7-10**
- **Fields:** `simplified_explanation` 133; `illustration.body` 169, 174–175. This is what remains of
  D7-13.
- **Problems:**
  - "Badly calibrated instrument" (133), "correctly calibrated reference" (169) and "calibration
    readings" (174) all come before the dash gloss at 175.
  - That gloss defines "calibration weight", not "calibrate".
  - `prose/GLOSSARY.md` already has "calibration | measuring a machine against something already
    known, so its readings mean something". It gives the first use as C32, but C30 is earlier in
    document order.
- **Smallest fix:** at 133, "…on a badly calibrated instrument (calibration is measuring a machine
  against something already known, so its readings mean something)…". Tell the main thread the
  glossary row's first-use record should be C30.
- **Severity:** floor.

**V7-11**
- **Field:** `definition.text` 19.
- **Claim:** "the anchor calls this a nonsampling error".
- **Problem:** Same as V6-10.
- **Smallest fix:** "the statistics textbook this book follows calls this a nonsampling error".
- **Severity:** floor.

**V7-12**
- **Field:** `practice[L6].prompt`. This is what remains of D7-16.
- **Claim:** "Can knowing how the scale records its weights, on its own, tell you whether this error
  is systematic or random?"
- **Problem:** "On its own" is the answer's shape. The audit named it.
- **Smallest fix:** drop ", on its own,".
- **Severity:** style.

**V7-13**
- **Field:** `practice[L9].answer`.
- **Problems:**
  - "Thirty times the old scale's": 0.62 ÷ 0.02 = 31.
  - The "does not establish" paragraph only refutes the colleague. It never names a limit of the
    reader's own computation (M14).
  - The new scale's readings actually agree more closely than the old scale's: range 0.16 kg against
    0.30 kg.
  - Five readings at one weight say nothing about other loads.
- **Smallest fix:**
  - Write "thirty-one times".
  - Add: "What this does not establish: the new scale is not worse in every way, since its readings
    agree more closely with each other (a range of 0.16 kg against 0.3 kg). And five readings at
    50 kg say nothing about either scale at other weights."
- **Severity:** style.

**V7-14**
- **Field:** `definition.text` 56.
- **Claim:** "This section's glossary calls precision…"
- **Problem:** The glossary belongs to the book, and `simplified_explanation` 142 says "This book's
  glossary".
- **Smallest fix:** "This book's glossary".
- **Severity:** style.

**V7-15**
- **Field:** `practice[L7, thermometer].answer` 579–580.
- **Claim:** "the best estimate is 100.0 °C, water's boiling point at sea level". The answer also says
  the zero error "adds the same 0.3 °C to every single reading".
- **Problems:**
  - This is an unsourced fact about the world, and it holds only at standard pressure.
  - Applying an error found in ice to readings at 100 °C assumes it does not change with
    temperature. That is the assumption the illustration warns about for scale A at 60 kg.
- **Smallest fix:** delete "water's boiling point at sea level". Add "if the 0.3 °C error is the same
  at every temperature".
- **Severity:** style.

**V7-16**
- **Field:** `simplified_explanation` 141 and 147.
- **Problems:**
  - "Papers mix them up often" is a frequency claim with no source. VIM 2.15 Note 4 says
    "Sometimes".
  - "A scale that reads 61.4, 61.4, 61.4 and 61.4 kilograms … is very precise" commits the
    coarse-display failure (D7-24, mode 2). The fixer said the illustration now covers that failure.
    Identical readings on a 0.1 kg display can hide scatter smaller than one step.
- **Smallest fix:**
  - "and papers sometimes mix them up, as the VIM itself notes (2.15)".
  - "…agrees with itself to the last digit it shows".
- **Severity:** style.

**V7-17**
- **Field:** `illustration.body` 222–223.
- **Claim:** "a few more readings would bring the average closer still".
- **Problem:** With random error this is a tendency, not a certainty. B's −0.075 is well inside one
  standard error of its mean (0.115).
- **Smallest fix:** "would tend to bring the average closer still".
- **Severity:** style.

---

## Counts

**Original 49:** 34 closed, 15 partly, 0 not closed.

- D6: 16 closed, 9 partly (D6-1, 2, 4, 6, 7, 10, 14, 17, 19).
- D7: 18 closed, 6 partly (D7-2, 4, 5, 10, 13, 16).

**New or still-open items:** 32.

| severity | C29 | C30 | items |
| --- | --- | --- | --- |
| error | 6 | 7 | V6-1, V6-2, V6-3, V6-4, V6-5, V6-6; V7-1, V7-2, V7-3, V7-4, V7-5, V7-6, V7-7 |
| sourcing | 3 | 2 | V6-7, V6-8, V6-9; V7-8, V7-9 |
| floor | 2 | 2 | V6-10, V6-11; V7-10, V7-11 |
| style | 4 | 6 | V6-12, V6-13, V6-14, V6-15; V7-12, V7-13, V7-14, V7-15, V7-16, V7-17 |
| **total** | **15** | **17** | 32 |

**For the main thread:**

- **M13 does not say how simulated or stated-case numbers are registered.** V6-8 (item 2) and V7-9
  need a ruling. Today they make the reader's reference marks attribute made-up figures to OpenStax
  and the VIM.
- **Glossary rows** still to add or correct:
  - *bias*, both senses (D6-15);
  - *calibration*, first use C30 not C32 (V7-10);
  - *precision*, first use C03 (already carried in the glossary's own note).
- **M10 and the VIM.** M10 sets resolution as "the smallest step a display can show", and C30
  attaches "VIM 4.14" to that gloss in six places. VIM 4.14 defines resolution by the measured
  quantity. The display's step is VIM 4.15, which is not held. This is not counted against the
  fixer, because M10 rules it, but the citation is looser than the words it cites.

## Verdicts

**B0-R0-C29:** The square-root law teaching, the simulation and every sum are right. The figure is
exactly reproducible from the record. M12 is the ruling that mattered most for this section, and it
is not met. The NFHS figure is still given a population the paper never states, in six places, one
of them in the book's own voice. The study is still framed as a sample of India's adults, with 20
per cent as their figure. L9 still calls the gap "real". The fixer's new L7 applies the square-root
law to the volunteer men, which the section exists to forbid. It needs another fix pass on the
Kiran passages, and a re-check of every sentence that mentions NFHS, India or 20 per cent.

**B0-R0-C30:** The DEXA misreading, the definition's references, the zero-error inference in the
body, the transfer band and the VIM quotations are all fixed properly. The central distinction
still leaks: "accurate" is made equal to "true on average" in two places. The new L7 vouches for
the very line it was written to catch. Scale A is misdescribed again, in a sentence that does not
parse and one that is false. Two practice answers state things the paper or the problem does not
support: the neck tape, and "real" observers. It needs one more short fix pass.
