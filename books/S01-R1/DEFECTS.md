# S01-R1 defects

# Found by the compression pass

Run 23 September 2026, step 5c of PIPELINE.md Task 5. The cold reader's report is
`compress/COLDREAD-REPORT.md` (gap ids such as C03-G4). The restorer could not close the holes
below because the full-length original does not fill them either, or because they are errors
rather than missing text. They go back through the audit. Gap-by-gap decisions, including what
was restored, are in `compress/RESTORE-DECISIONS.md`.

Each item gives the section and field, the sentence as it stands, what is wrong or missing,
whether the original also had it, and the smallest fix. **error** means something false or
contradictory. **gap** means missing teaching.

Not recorded, on instruction: the Book 0 code mapping (GL-1, C05-G5, the code half of C08-G6).
The renderer now prints those ids as "Book 0, B4" and "section 3".

## Across the book

1. **gap** · All sections (GL-2, also C02-G11, C10-G5). The unit of the book is called "record",
   "concept", "section" and "booklet", and "rung", "this rung's build target", "the gate this
   rung sets" and "this subject's held sources" are used and never defined. The reader could not
   tell whether a record, a concept and a section are the same thing, or check C10 exercise 2
   against a target it cannot see. Original: same. Fix: use "section" throughout the prose. Either
   define "rung", "build target" and "gate" once in the book's opening, or replace them in C10 with
   the plain task ("write a one-page explanation that ..."). Replace "held sources" with "the
   sources this book cites".
2. **gap** · C05, C06 (title), C07 `illustration.body` (GL-3, C06-G2). The book says "identity",
   "accounting identity" and "the first law (of thermodynamics)" and never ties them to Book 0
   E3's "balance line" or to conservation of energy. The restored C05 sentence now ties
   "identity" to the balance line. "First law" is still never defined. Original: same. Fix: one
   sentence in C06's definition: "The first law of thermodynamics is the physicist's name for
   conservation of energy, the rule Book 0 E3 teaches."
3. **gap** · C01, C03, C04, C06, C09, C10 (GL-4). Six sections have no practice set, and C01,
   C03 and C04 have no exercise either. So the sections that make the most empirical claims have
   no problems to test them. Original: same, because the compression pass does not touch
   exercises. Fix: send these sections back for a practice set under the practice-set rule.

## S01-R1-C01

4. **gap** · `definition.text` / `simplified_explanation` (C01-G7, remainder of C01-G1). "Fat
   mass is the triglyceride held in adipose tissue." Elsewhere "body fat" means the triglyceride
   (C01) or the whole tissue (C02: "A kilogram of body fat lost or gained ... is adipose
   tissue"). The section never says which compartment adipose tissue's water and cells belong
   to. The restored caveat now says adipose tissue is not all fat. Original: same. Fix: one
   sentence after the fat-mass definition: "The water and cells of adipose tissue count as
   fat-free mass." Also fix one meaning for "body fat" and use it in both sections.
5. **gap** · `illustration.body` quote (C01-G3). "...comprises the metabolically active tissues
   of the body and therefore contributes more to REE than body fat." The section does not say
   what "metabolically active" means. Original: same. Fix: gloss it in one sentence, for example
   as the tissue that spends most of the energy the body uses at rest.
6. **gap** · `illustration.body` quote (C01-G4). "Body fat represents the vast majority of energy
   stores in the body compared with the energy content of body protein and glycogen." Book 0 E6
   named only glycogen and triglyceride as stores, and body protein as an energy store is never
   introduced. Original: same. Fix: one sentence saying that body protein can be broken down for
   energy, although it is not held as a store the way fat is.
7. **gap** · `must_know[2].point` (C01-G6). "Ask for a method before you accept a number for
   either compartment." No method is named anywhere in the book, so the reader cannot judge an
   answer. Original: same ("by a method this section does not give you"). Fix: name one or two
   methods (for example DXA and bioimpedance) and point forward to where they are taught.
8. **gap** · abbreviations (C01-G3). REE is used in a quote and never expanded. Original: same.
   Fix: "REE (resting energy expenditure)" on first use.

## S01-R1-C02

9. **error** · `must_know[0].point`, `must_know[1].point` (C02-G2). "Pure fat holds about 9
   kilocalories, or 37 to 39.5 megajoules, for each kilogram." and "Never quote 9 kilocalories or
   37-39.5 megajoules a kilogram ..." The 9 kilocalories figure is per gram, so this is wrong by a
   factor of 1,000, in the lines a reader memorises. Original: same. Fix: "9 kilocalories a gram
   (9,000 a kilogram), or 37 to 39.5 megajoules a kilogram", and the same in must_know[1].
10. **error** · `simplified_explanation`, table (C02-G3). "It is about 9 kilocalories a gram, which
    is 9,000 a kilogram, or ... about 37 to 39.5 megajoules a kilogram." 9 kcal/g is 37.7 MJ/kg,
    and 39.5 MJ/kg is 9.4 kcal/g, so the sentence treats a range as equal to one of its ends.
    Nothing says why Hall's metabolizable figure (39.5) is above FAO's Atwater figure (37), when
    Book 0 E2 taught that Atwater factors are themselves metabolizable (fat 37.4). The table calls
    Hall's figure "physiological" and never defines the word. The original's only explanation
    ("Close, not identical — ... a general dietary factor against a physiological energy density
    ...") is a 56-word sentence. Restoring it raised the mean sentence length past the original's,
    so validation refused it. Original: same error. Fix: "about 9 kilocalories a gram, 37 to 39.5
    megajoules a kilogram depending on the source". Add one short sentence on why the two sources
    differ, and say which figure to use.
11. **gap** · `definition.text` (C02-G4). "Hall (2008) states that the classic weight-loss rule
    'can be traced back to ...'" The rule (3,500 kcal a pound) is not stated until the end of the
    illustration and is only introduced properly in C07. Original: same. Fix: state the rule in a
    clause at first mention ("the classic rule, 3,500 kcal for each pound lost").
12. **error** · `simplified_explanation` (C02-G5). "Take the fraction, 0.87, and multiply by fat's
    own energy per gram." In the kilocalorie framing of that passage, 0.87 × 9.0 = 7.83, which is
    7,830 kcal/kg and not "roughly 7,700". Practice problem 1 then has the reader multiply by 9.0.
    Original: same. Fix: say "fat's 37 kilojoules a gram", or add one sentence saying the kcal
    route gives about 7,800 because 9.0 and 37 are rounded separately (Book 0 E2).
13. **error** · `illustration.body` (C02-G6). "Read the exponent as ten to the sixth, a million —
    the source's own extraction note says the superscript formatting is lost in the fetch." This
    is a production artefact. The reader never sees an extraction note and fetched nothing.
    Original: same. Fix: "The page shows 10 with a raised 6; here it prints as 106. Read it as ten
    to the sixth."
14. **error** · `illustration.body` working and gloss (C02-G7). "37 times 1000 = 37000 / 37000
    divided by 1000 = 37" has no units on any line, and the gloss says "the two divisions and
    multiplications cancel" when there is one of each. Original: same. Fix: add units to the
    working (kJ/g × 1,000 g/kg = kJ/kg; ÷ 1,000 kJ/MJ = MJ/kg) and say "the multiplication and the
    division cancel".
15. **gap** · `definition.text` (restored), `must_know[4].point` (remainder of C02-G8). The 7.6
    MJ/kg lean-mass figure is now attributed to Hall (2008), with the water that moves with
    glycogen and protein. It still has no quote and no search string, unlike every other figure
    in the section. Original: same. Fix: add the quote and a search phrase from Hall 2008.
16. **gap** · abbreviations. BIPM, FAO and the symbol MJ are never expanded. SI is expanded in
    the BIPM page title. Original: same. Fix: expand BIPM (International Bureau of Weights and
    Measures) and FAO (Food and Agriculture Organization) on first use, and write "megajoules
    (MJ)" once.

(C02-G10, where two origin stories are given for the 3,500 rule, is item 41.)

## S01-R1-C03

17. **error** · `simplified_explanation` vs `definition.text` (C03-G1). "In three groups it
    measured, the number came out between about 8 and 16 megajoules a day." The definition says "a
    few megajoules to about ten of them", and 16 is not about ten. Original: same. Fix: change the
    definition to "a few megajoules to about fifteen", or drop the vigorously active example from
    the range.
18. **gap** · `simplified_explanation` (C03-G2). "There is a way to measure this directly, called
    doubly labelled water ..." The method is only named. Nothing says what is labelled, how it
    measures anything, or why it counts as direct. Original: same ("measures total energy
    expenditure directly, over ten to fourteen days"). Fix: two sentences on how it works (water
    with traceable hydrogen and oxygen; the difference in how fast they leave the body gives the
    carbon dioxide produced, and from that the energy spent).
19. **error** · `illustration.body`, `definition.text` (C03-G3). "A measured group of sedentary or
    lightly active women averaged 1,975 kilocalories a day." The quote it rests on is a
    hypothetical ("If this PAL was from a female population ... TEE = 1.53 x 5.40"). That is a
    multiplier times a BMR, not a measurement. The restored definition sentence itself calls the
    figures "worked examples", while the paragraph around it calls them "a measurement of what a
    group of people actually spent". In the section about naming the kind of number, the number
    is given the wrong kind. Original: same. Fix: call it "a worked example in the FAO/WHO/UNU
    report: a typical activity multiplier times a typical resting rate". Move it out of "the first
    kind", or find a real doubly-labelled-water mean for the first kind. (Carries into C05, item
    36.)
20. **gap** · `illustration.body` (C03-G5). "The first row is men, the second women, and the
    number under ICMR 2020 is the one to use ..." The quoted rows ("2110 2320 -210") have no
    column headings, so the reader has to take on trust which column is 2020. Original: same.
    Fix: quote or state the headings (ICMR 2020, ICMR 2010, difference).
21. **error** · `illustration.body` vs `simplified_explanation` (remainder of C03-G6). "... what an
    average Indian household's recorded food purchases convert to ..." The simplified explanation
    says "food bought or grown by their household". Original: same. Fix: "recorded food
    acquisition (bought, grown or received)" in both places. The restored definition sentence now
    gives the rural/urban and year mapping for the NSS row.
22. **error** · `illustration.body` vs `must_know[3].point` (C03-G7). "... the number under ICMR 2020
    is the one to use: 2,110 kilocalories a day for him, 1,660 for her." The Must-know says "Do not
    use a population figure as an individual's prescription." Original: same. Fix: "the number
    under ICMR 2020 is the committee's figure for a man and a woman like them", which makes no
    claim that it is the one to use for these two patients.
23. **gap** · `simplified_explanation`, `must_know[2].point` (remainder of C03-G9). "Ask somebody to
    report what they ate and the answer is known to be unreliable." There is no source and no
    direction (under, over, or both). The restored "There is a fourth thing worth knowing ..." now
    explains why it sits beside the three kinds. Original: same (no source, no direction). Fix:
    add the direction (typically under-reported) and a source.
24. **gap** · `definition.text` (C03-G10). "... converted to energy through a nutrient conversion
    table." The term is not defined or tied to Book 0 E6's "food composition tables". Original:
    same. Fix: "a nutrient conversion table (a food composition table, as in Book 0 E6)".
25. **gap** · `illustration.body` (C03-G11). "... within about three hundred kilocalories of the
    Indian committee's 1,660 for the same activity band." Nothing shows that FAO's "sedentary or
    light activity" and ICMR's "sedentary work" are the same band, or why 55 kg women aged 30 to
    50 are "a comparable population". Original: same. Fix: say what makes them comparable (the
    activity multiplier range each uses), or say "a roughly similar band".
26. **gap** · abbreviations (C03-G4). PAL, BMR and TEE in the FAO quote, and FAO, WHO and UNU in
    the source line, are never expanded, so the one calculation shown cannot be followed.
    ("Basal metabolic rate" appears in the original's Must-know but is never tied to BMR.)
    Original: same. Fix: gloss after the quote: "PAL is the physical activity level, a
    multiplier; BMR is basal metabolic rate; TEE is total energy expenditure". Expand FAO, WHO and
    UNU once.

## S01-R1-C04

27. **gap** · `definition.text`, `simplified_explanation`, `must_know[0].point` (C04-G1). "...
    is the largest of the three", "the biggest of the three by a wide margin", "This is the
    smallest of the three shares." No figure or source is given for either ranking. Original:
    same. Fix: give typical shares with a source (for example Hall and Guo 2017).
28. **gap** · `simplified_explanation` (C04-G2). "Protein takes more effort to process than
    carbohydrate, and carbohydrate takes more than fat." No source is given. Original: same. Fix:
    add a quote and search string.
29. **gap** · `illustration.body` (C04-G4). "The other weighs 95 kilograms, of which a larger
    fat-free mass is part." The sentence does not say larger than what. Original: same. Fix:
    "... and carries more fat-free mass than the first patient does."
30. **gap** · `definition.text` (C04-G8). "The thermic effect of food is the energy spent
    digesting, absorbing and processing what was eaten." Book 0 E2's *net* metabolizable energy
    already subtracts digestion cost, and the text does not say whether counting the thermic
    effect as expenditure double-counts it. Original: same. Fix: one sentence: intake here is
    metabolizable (not net), so the cost of digestion is counted once, on the expenditure side.
31. **gap** · abbreviations (C04-G5). REE is used in the quotes and never tied to "resting energy
    expenditure". Original: same. Fix: "resting energy expenditure (REE)" at the definition.

## S01-R1-C05

32. **error** · `illustration.body` vs `illustration.analogy_breaks_when` (C05-G2). "A person's
    energy stores are measured at the start of the week: 620 megajoules." The section itself says
    "Body energy stores are not measured directly day to day." The restored "Take a made-up week"
    now flags the week as invented. The verb is still "measured". Original: same. Fix: "Suppose
    a person's energy stores stand at 620 megajoules at the start of the week."
33. **error** · `must_know[3].point` (C05-G3). "A day-to-day mismatch is usually a sign the interval
    is too short for food still in the gut and water shifts to average out ..." Water shifts carry
    no energy, so they cannot unbalance an energy identity. The mismatch meant is between the
    identity and a scale reading, and the text does not say so. Original: same (and the original's
    `simplified_explanation` makes the same slide). Fix: "A day on which the scale seems to
    disagree with the identity usually reflects food still in the gut and water shifts, which move
    mass without moving stored energy."
34. **gap** · exercise 1 (C05-G6). "... say in words what has to be true of their body mass for
    that change to show up on a scale." The section says it "does not supply" the energy-to-mass
    fact the exercise needs. Original: same. Fix: point the exercise to C02 ("using C02's
    figures"), or reword it to ask only what the identity does not tell you about mass.
35. **gap** · abbreviations. FAO, WHO and UNU in the practice-problem source lines are never
    expanded. Original: same. Fix: expand them, or refer back to C03 once C03 expands them.
36. **error** · practice problems 3 and 4 (C05-G7). "A reference sedentary or lightly active adult
    woman has a measured total energy expenditure of 8.26 megajoules a day." This inherits
    C03's mislabel (item 19): 8.26 is a worked example, not a measurement. "Reference" is not
    defined. Original: same. Fix: "The FAO/WHO/UNU worked example for a sedentary woman puts total
    energy expenditure at 8.26 megajoules a day."

## S01-R1-C06

37. **gap** · title, `illustration.analogy_breaks_when` (C06-G1). "without a lever" and "a direction
    of control the identity never supplied". "Lever" is never explained. Original: same. Fix: one
    clause in the definition: "a lever, a handle that controls the outcome".
38. **gap** · `definition.text` (C06-G3). "It needs a further premise, about what happens to
    expenditure and appetite when intake changes ..." This is the book's first use of "appetite",
    which is undefined. The illustration's missing premise is only about expenditure, and the text
    does not say why appetite belongs in it. Original: same. Fix: define appetite in a clause and
    add "and whether the cut in intake can be held" to the illustration's missing premise, or drop
    appetite from this sentence.
39. **gap** · `must_know[2].point`, exercise 1 (C06-G6). "The identity is consistent with every
    serious account of why weight changes ..." The identity is about energy stores, and Book 0 C9
    separates energy from mass. The section slides from one to the other without comment.
    Original: same. Fix: "... why energy stores, and with them weight, change". Add one sentence
    that turning stores into weight needs the composition facts of C01 and C02.

## S01-R1-C07

40. **error** · `definition.text` (C07-G2). "... converts into a change in fat mass at that fixed
    rate." The common form is "for each pound of body weight changed", and the worked cases are
    weight. C01 and C02 teach that weight is not fat. Original: same. Fix: say what the rule
    predicts ("the rule is stated for body weight but assumes all of it is fat").
41. **error** · `definition.text` vs C02 `definition.text` (C07-G3, C02-G10). C07: "... a figure this
    subject's held sources trace to Wishnofsky (1958) and describe as 'derived by estimation of
    the energy content of weight lost'." C02: the rule "can be traced back to a calculation that
    assumes exclusive loss of adipose tissue consisting of 87% fat", and C02 says C07's pound
    route rests on that 0.87. The two origin stories are never reconciled. "Estimation of the
    energy content of weight lost" also sits badly with "It is not a fact anybody measured about
    fat." Original: same. Fix: one sentence in C07: "Wishnofsky's estimate is the calculation C02
    describes: 87% fat, times fat's energy per gram." Check this against Hall 2008 first.
42. **error** · `illustration.body` (remainder of C07-G4). "What they actually lost, measured, was
    20.1 pounds: '7.4±12.6 lb less than the 27.6±16.0 lbs predicted ...'" 27.6 − 7.4 = 20.2, not
    20.1. Original: same. Fix: check the paper for the mean loss. If it reports 20.1, add a clause
    saying the gap is rounding.
43. **gap** · `illustration.body` (C07-G5). "7.4±12.6 lb" and "27.6±16.0". The ± notation and
    standard deviation are not taught in Book 0 or here. Original: same. Fix: one sentence: "The
    number after ± is the spread between people. Many lost more than predicted, and many lost
    less."
44. **gap** · `illustration.analogy_breaks_when`, `must_know[3].point` (C07-G9). "The straight-line
    projection is reliable only over an interval short enough that intake and expenditure have
    not yet responded ..." No interval is given, and Thomas already shows a large miss at 64.8
    days. The Must-know tells the reader to "say over what interval it holds", and practice
    problem 8 needs one. Original: same (its "for the first few months" example also conflicts with
    Thomas). Fix: give a sourced rough interval, or say plainly that no source here fixes one.
45. **error** · practice problem 1 (C07-G10). "A rule states that 3,500 removes one unit of weight
    for every 0.45359237 of a different unit that measures the same thing." The sentence does not
    parse. Original: same. Fix: "A rule says 3,500 kcal removes one pound. One pound is 0.45359237
    kilogram. How many kcal per kilogram is that?"
46. **error** · `illustration.analogy_breaks_when` (C07-G11). "... both sources here agree that
    response starts working against the deficit within the first year ..." The Thomas material
    shown says nothing about timing or mechanism, only the size of the shortfall. Original: same.
    Fix: "the Hall model puts half the eventual loss in the first year, and Thomas's cohort already
    fell short of the rule within about nine weeks".
47. **gap** · `definition.text`, `illustration.body` (GL-5, remainder of C07-G6). "the *Lancet*
    paper by Hall and colleagues", "Thomas and colleagues", "Wishnofsky (1958)". None has a URL or
    a search string, and the first two have no year, unlike C01 to C04. Original: same. Fix: add
    year, URL and search string for each, in the C01 to C04 pattern.

## S01-R1-C08

48. **error** · `illustration.body` and table (C08-G1). "The largest average deficit anyone in that
    pooled group sustained, across the whole cohort ... was 1,439 kilocalories a day." and
    "roughly five times the biggest deficit ever measured in that supervised cohort". C07 gives
    1,439 as the cohort's *average*. An average is not the largest, and individuals ran bigger
    deficits. Original: same. Fix: "The cohort's average deficit, under total dietary control, was
    1,439 kilocalories a day", and "roughly five times the average deficit that cohort managed".
49. **error** · `definition.text`, `simplified_explanation` (C08-G2). "A claim whose required energy
    exceeds every plausible deficit ... is impossible on energy grounds alone." The ceiling that
    makes a claim impossible is total expenditure. Exceeding a *plausible* deficit makes it
    implausible. Original: same. Fix: "... exceeds the person's total expenditure over the interval
    is impossible; one that exceeds any plausible deficit is implausible."
50. **gap** · `illustration.body` (C08-G3). The illustration tests the 7,000 kcal/day claim only
    against Thomas's 1,439, never against the hard ceiling the section defines (total expenditure,
    which C03 puts at about 2,000 to 4,000 kcal). Original: same. Fix: add one line comparing
    7,000 with a day's total expenditure from C03.
51. **gap** · `definition.text` (C08-G4). "Second, put a number on the claimed fat change, using the
    static rule's own conversion from this subject's C07 ..." C02 and C07 have just taught the
    reader to distrust this figure. Nothing says why it is acceptable here (it is lower than pure
    fat's 9,000, so it is lenient to the claim), or when to use 9,000. Original: same. Fix: one
    sentence giving that reason.
52. **gap** · `definition.text` (remainder of C08-G5). "... a different substance leaving the
    boundary, at a different energy cost per kilogram than fat." No figure is given for glycogen
    plus its water, and no water-to-glycogen ratio, so practice problem 6 can be answered only in
    words. The restored Hall quote now sources "glycogen is stored with water". Original: same (no
    figure). Fix: give a sourced energy per kilogram of glycogen with its water.
53. **error** · `must_know[1].point` (C08-G6, wording only). "... which this subject's B0-R0-C33
    already rules out ..." Book 0 is not this subject. Original: same. Fix: "which Book 0's
    section on conservation already rules out".
54. **gap** · practice problem 8 (C08-G7). "A bariatric patient of mine dropped 12 kg in the first
    three weeks after surgery ..." "Bariatric" is defined in neither book, and the reader could not
    use the fact of surgery. Original: same. Fix: "after weight-loss (bariatric) surgery", and give
    or point to an expenditure figure.
55. **error** · `definition.text` (C08-G8). "... compare that required amount with the largest
    deficit that has plausibly crossed the person's boundary ..." A deficit is a difference between
    two crossings, not something that crosses. Original: same. Fix: "... the largest deficit the
    person could plausibly have run over that time".

## S01-R1-C09

56. **error** · `definition.text` (C09-G1). "That pull is more than three times the size of the
    matching fall in expenditure ..." The section's own numbers give about 800 against 300 to 400,
    which is 2 to 2.7 times. They also compare an 8 kg loss with a 10% loss, which match only at
    80 kg, and that is not stated. "Matching" is undefined. Original: same (and the original's
    illustration attributes "more than three times" to Polidori). Fix: check Polidori's comparison
    and state its basis. Otherwise say "two to three times, for a person of about 80 kg".
57. **error** · `illustration.body` (C09-G3). "The expenditure fall for a person who lost a full 10%
    of body weight sits at 300 to 400 kcal a day." The restored definition makes 300 to 400 the
    *extra* (adaptive) part, not the whole fall. Original: same. Fix: "The extra, adaptive fall in
    expenditure ... sits at 300 to 400 kcal a day."
58. **gap** · `illustration.body` (GL-5, remainder of C09-G4). "Take the trial the appetite figure
    above comes from." The trial has no authors, year, URL or quote. (Polidori is named only in a
    sentence the cut removed and that was not restored, because it repeats item 56.) Original: no
    URL, year or quote either. Fix: cite Polidori et al. with year, URL and a search string.
59. **gap** · `illustration.body` (C09-G5). "... in 153 people with type 2 diabetes ..." Type 2
    diabetes is defined in neither book. Original: same. Fix: a one-clause gloss.
60. **gap** · `definition.text` (remainder of C09-G6). "They are outputs of a system that senses
    body weight, or a signal that tracks it, and pushes back when weight falls." There is no
    source. The restored Rosenbaum and Leibel sentence now names a source for the expenditure
    figure. Original: same (no source for the sensing claim). Fix: cite Hall and Guo 2017 (already
    held) for the sensing claim.
61. **error** · `illustration.body` (C09-G7). "The appetite pull is about 8 times 100 kcal, close to
    800 kcal a day of extra wanting to eat." The trial estimated intake (eating), and "wanting to
    eat" is a different quantity. Original: same. Fix: "... close to 800 kcal a day of extra
    eating".
62. **error** · `must_know[0].point` (C09-G8). "'Cut intake and only fat is lost' is incomplete."
    The section is about push-back, not about what tissue is lost. Original: same. Fix: "'Cut
    intake and weight keeps falling' is incomplete."
63. **gap** · `must_know[4].point` (C09-G10). "It does not teach the neuroendocrine mechanism ..."
    "Neuroendocrine" is not defined. Original: same. Fix: "the nerve-and-hormone
    (neuroendocrine) mechanism".

## S01-R1-C10

64. **error** · `simplified_explanation` vs C06 (C10-G1). "So cut intake, or raise expenditure,
    and stores must fall." C06 teaches that this inference "does not follow ... not on the premise
    alone". C10 then locates the fault in "stores keep falling on their own", a different claim.
    Original: same (and adds "That much is arithmetic"). Fix: "So cut intake, *with expenditure
    unchanged*, and stores must fall." That matches C06.
65. **error** · `definition.text` (restored premises), `illustration.body` (C10-G2, remainder of
    C10-G4). "The inference fails, and it fails at premise two's hidden clause." In Book 0 F4's
    terms, what fails here is premise two's *truth*, not the inference. The argument is valid, and
    the illustration itself says the premise "is not true". The restored definition makes premise
    two "arithmetic and true" (with expenditure held fixed). The illustration makes it "left
    unsaid" and false ("expenditure and appetite do not move"). The same label covers two
    different statements. "Exactly as an earlier concept establishes" does not name C09. Original:
    same. Fix: use one premise two in both places ("once intake is cut, expenditure and appetite
    stay where they were"), say the argument is valid but premise two is false, and name C09.
66. **error** · `illustration.body` (C10-G3). "The evidence in this booklet says premise two is
    false: expenditure falls further than the lost mass explains, and appetite rises by more
    again." If rising appetite leads a person to eat more, they have indeed not kept intake cut,
    and the doctor's conclusion is literally true. Only the expenditure half defeats the doctor.
    Original: same. Its extra sentence ("A person can cut intake exactly as instructed and still
    see the scale stall, because the two physiological responses ... close most of a modest
    deficit") repeats the flaw, so it was not restored. Fix: rest the rebuttal on expenditure, and
    treat appetite as the reason a cut is hard to hold, not a reason the scale stalls while it is
    held.
67. **error** · `definition.text` vs C09 (C10-G6). "... they move in response to the fall in stored
    energy ..." C09 says the system "senses body weight, or a signal that tracks it". Original:
    same. Fix: use one wording in both sections.
68. **gap** · `illustration.body` (C10-G7). Premise one is about stored energy, and the conclusion
    is about a person "not losing weight". The argument needs a premise joining stores to weight
    (Book 0 C9), and the text does not name it. Original: same. Fix: add it as a stated premise, or
    phrase the conclusion in stored energy.

Totals: 68 items, 29 errors and 39 gaps.
