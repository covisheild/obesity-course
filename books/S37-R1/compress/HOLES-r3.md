# S37-R1 holes found by the compression pass, batch r3 (C13 to C18)

These are the holes the restorer could not close from the original. The original does not fill
them either, or they are errors or contradictions. They go to the audit and the fixer. Each
entry gives the gap id(s), the section and field, the sentence as it stands in
`-final-prose.yml`, what is wrong or missing, and what would close it. The numbering matches
`RESTORE-DECISIONS-r3.md`.

## C13

**H1 · B-C13-1 (H) · C13 `definition.text`, `must_know[2].point`**
- As it stands: "IFCT converts them to kilocalories with 1 kcal = 4.18 kJ." and "The Indian tables
  use 4.18, not Book 0's 4.184."
- Wrong or missing: Book 0 (B4) taught 4.184 and 4.1868, both exact by definition. The text never
  says whether 4.18 is a rounding of 4.184 or a separate convention. It also never says whether
  the Schedule II norms (450 kcal, 700 kcal) were written in the same calorie. So the reader
  cannot tell whether "1,881 kJ = 450 kcal" compares like with like.
- What closes it: check the IFCT 2017 introduction for what its 4.18 is. Then add one sentence
  saying it is a rounding of the thermochemical calorie (if so), and that the difference is below
  0.1 per cent, so it never changes a verdict against a norm.

**H2 · B-C13-2 (L, residual) · C13 `definition.text`**
- As it stands: "... 1660 kcal a day for a sedentary reference woman of 55 kg and 2110 kcal for a
  sedentary reference man of 65 kg."
- Wrong or missing: "sedentary" and "reference" are undefined. ICMR-NIN is now expanded by the
  restored IFCT sentence.
- What closes it: one sentence from the ICMR-NIN 2020 report defining the reference adult and the
  sedentary activity level.

**H3 · B-C13-3 (M) · C13 figure caption**
- As it stands: "A primary school meal built to the PM POSHAN food norms ... The 100 g of raw milled
  rice gives 1,491, the 20 g of tur dal 276.8, and the 5 g of oil at most 185."
- Wrong or missing: the primary-class food norms (100 g grain, 20 g pulses, 50 g vegetables, 5 g
  oil) appear only in a caption, with no source. The text never says whether they are raw
  weights.
- What closes it: state the primary norms in the text, cited to the PM POSHAN guidelines. Say
  that the gram norms are raw, uncooked weights, if the source confirms it.

**H4 · B-C13-5 (L) · C13 figure caption**
- As it stands: "the 5 g of oil at most 185. The 50 g of vegetables is not counted."
- Wrong or missing: neither "at most" (oil taken as pure fat at 37 kJ/g) nor the vegetables'
  exclusion (no single IFCT composition for "vegetables") is explained.
- What closes it: a short clause for each reason, or a note under the figure.

**H5 · B-C13-6 (L) · C13 `must_know[1].point`**
- As it stands: "That uses the 2017 tables' average and a 30-day month."
- Wrong or missing: "average" of what is not said (varieties? samples?).
- What closes it: name what IFCT averages over for raw milled rice, from the table's own notes.

## C14

**H6 · B-C14-1 (M, number) · C14 figure spec and `must_know[2].point`**
- As it stands: the text gives the table's 607.40 lakh tonnes, and the report's text says 595.05.
  The figure's bars are PHH 428.63, AAY 99.39, tide over 26.09, WBNP 23.05, PM POSHAN 22.31,
  hostels 5.83 and adolescent girls 0.58.
- Wrong or missing: the bars sum to 605.88, not 607.40. Either a row of the DFPD table is missing
  from the figure (1.52 lakh tonnes), or a figure is wrong.
- What closes it: re-open the DFPD annual report table, add the missing row, or correct the
  total. This is a figure-spec fix, not a restoration.

**H7 · B-C14-2 (M, residual) · C14 figure**
- As it stands: bars "tide over 26.09" and "adolescent girls 0.58".
- Wrong or missing: neither scheme is explained anywhere in C14. The hostels bar is now explained
  by a restored sentence.
- What closes it: one clause each from the DFPD table's notes (what "tide over" allocation is,
  and which scheme for adolescent girls), or drop them into an "other" bar with a note.

**H8 · B-C14-3 (M) · C14 `definition.text`; Exercise 1**
- As it stands: "The DFPD allocated it 22.31 lakh tonnes of foodgrains for 2025-26." (of PM POSHAN).
  Exercise 1 asks for the ministry that runs each channel.
- Wrong or missing: PM POSHAN's ministry (Ministry of Education) is given only in C16, and
  "The DFPD allocated it" invites the wrong answer.
- What closes it: name the Ministry of Education where C14 introduces PM POSHAN.

**H9 · B-C14-6 (L, cross-file) · C14 `definition.text` against C12**
- As it stands: "The DFPD's grain for it runs through the Wheat Based Nutrition Programme (WBNP),
  23.05 lakh tonnes for 2025-26." C12 says: "The 2022 guidelines forbid raw rice, wheat or dal as a
  take-home ration."
- Wrong or missing: nothing says how allocated grain becomes the prepared food the guidelines
  require, so the two read as a contradiction.
- What closes it: one sentence, sourced to the Poshan 2.0 guidelines, saying that the grain is
  cooked or processed into meals or fortified mixes before distribution.

**H10 · B-C14-8, B-C15-5, B-C16-8, B-C17-5 (L, structure) · C14, C15, C16, C17**
- As it stands: exercises only, and no numbered practice set.
- Wrong or missing: there is no drill set for the cold read to test against. The original has
  none either.
- What closes it: a decision on whether these conceptual sections need a practice set under
  `claude/practice-set-rule.md`. If they do, the fixer writes one. The compression pass does
  not.

**H13 · B-C14-5 (L) · C14 `definition.text`**
- As it stands: "The DFPD allocated it 22.31 lakh tonnes ..." and "The DFPD's grain for it runs
  through ...". DFPD is never expanded in C14 as it now stands.
- Wrong or missing: the original's expansion ("The grain goes out through fair price shops, of
  which the Department of Food and Public Distribution (DFPD) counts 5.51 lakh (551,000).") could
  not come back. It raised the mean sentence length from 15.26 to 15.28, so validation failed.
- What closes it: the fixer adds "(DFPD)" at the full name's first use in the book (C08), or
  expands DFPD at its first use in C14.

## C15

**H11 · B-C15-2 (H) · C15 `definition.text`, `must_know[7].point`; Exercise 1**
- As it stands: "A single-duty change acts on one burden and neither aims at nor checks the other.
  A change working against the other burden acts on one and raises the risk of the other."
- Wrong or missing:
  - The categories are not exhaustive. There is no label for a change that was checked, passes
    do-no-harm and acts on one burden, which is Ex 1(b).
  - Nothing maps the WHO's three levels onto double-duty, single-duty and working against.
  - Whether a change "raises the risk" needs evidence the book never gives.
  - So Ex 1 and the R2 Task 2 turn on the reader's judgement.
- What closes it: name the missing category (or fold it into "single-duty, checked"). State how the
  WHO levels relate to the book's words. Say what evidence would show that a change raises the
  other burden's risk.

**H12 · B-C15-3 (M) · C15 `must_know[5].point`**
- As it stands: "A change that adds energy and nothing else, in a population where overweight is
  rising, fails that check."
- Wrong or missing: the rule is asserted with no source, and "population" is unspecified.
  Overweight is shown rising in women aged 15 to 49 and in children under five. The proposals
  target toddlers, schoolchildren (no data) or households.
- What closes it: source the rule (the WHO double-duty brief), and state which population's trend
  it must be read against. Add school-age overweight data if C15 is to judge school meals.

**H14 · B-C15-4 (L) · C15 `definition.text`**
- As it stands: "An adult aged 15 to 49 has a below-normal body mass index (BMI) below 18.5
  kg/m^2, and is overweight or obese at 25.0 kg/m^2 or more."
- Wrong or missing: 15-year-olds are called adults, and the cut-offs are not attributed (B6 says
  always say whose cut-offs).
- What closes it: "A woman or man aged 15 to 49", and say that these are the WHO cut-offs as
  NFHS-5 applies them.

**H15 · B-C15-5 (L) · C15 `definition.text`**
- As it stands: "A double-duty action, in the WHO's words, is an intervention, programme or policy
  with the potential to reduce the risk or burden of both at once."
- Wrong or missing: the WHO text is quoted with no document name, date or link, so F3's check is
  impossible.
- What closes it: cite the WHO policy brief (title, year, URL) in the text or the references.

## C16

**H16 · B-C16-1 (H) · C16 `definition.text` table, Stage column**
- As it stands: stages "Production", "Storage", "Storage and trade inside India", "Trade across the
  border", "Processing and retail", "Provision", "Tax".
- Wrong or missing: these are not C01's eight stages (production, storage, processing,
  distribution, retail, preparation, consumption, waste). "Provision" and "Tax" have no
  counterpart. The R2 Task 1 and C17's "stage" question need a mapping.
- What closes it: relabel the column with C01's stages, or add one sentence mapping each label.
  For example: provision acts at distribution and preparation; tax acts on price at retail.

**H17 · B-C16-2 (M) · C16 table**
- As it stands: "India's main food policy tools, placed at the stage of the food system where each
  acts" (the map).
- Wrong or missing: the APMC mandi, its auction and fees are left out, though C02 and C05 teach
  them.
- What closes it: add a Distribution row for APMC market fees and auction, run by State
  agricultural produce market committees under State Acts. Source it from the State Act or C05's
  source.

**H18 · B-C16-3 (M, number) · C16 figure; `must_know[2].point`**
- As it stands: "A Cabinet release of 3 October 2024 put the duty on edible oils at 20%. The basic
  customs duty on crude palm oil was 10% from June 2025, and 5% ..." The figure calls them "the
  same tool, three values".
- Wrong or missing: whether the 2024 20% is basic or effective duty is not said. The same section
  warns that the two differ, so the bars may not be comparable.
- What closes it: re-open the 3 October 2024 release. State which duty it gives, and relabel or
  split the figure's first group to match.

**H19 · B-C16-4 (M) · C16 Exercise 2**
- As it stands: "Using the release of 24 September 2026, say what the release does and does not
  support in that line."
- Wrong or missing: the release's own words are never quoted, only the book's paraphrase ("wants
  cheaper oil in the shop"). "Does not support" cannot be checked.
- What closes it: quote the release's stated purpose, with a link, in the text or the must-know
  point on the duty.

**H20 · B-C16-6 (L) · C16 `simplified_explanation`**
- As it stands: "Obesity turns up in these texts only as a theme of two awareness campaigns in
  2025."
- Wrong or missing: the two campaigns are not named. C17 mentions Poshan 2.0's "campaign on less
  sugar" and an oilseeds-mission campaign on oil, but it never confirms they are the same two.
- What closes it: name both campaigns (and their source) in C16 so that C17's references resolve.

**H21 · B-C16-7 (L) · C16 table, MSP row, against C09**
- As it stands: "Minimum support price (MSP) ... | a decision announced each season". C09: "Section
  2(10) of the National Food Security Act, 2013 defines the minimum support price".
- Wrong or missing: whether MSP rests on a statute is ambiguous between the two sections.
- What closes it: say in C16 that the NFSA defines MSP but does not set it, and that each season's
  figure rests on a Cabinet decision.

## C17

**H22 · B-C17-1 (H) · C17 `definition.text`, against C05**
- As it stands: "A proposal acts on the person when the only decision it changes is the eater's
  own, made from an offer left as it was: advice, counselling, an awareness campaign. It then
  moves no element of the food environment." C17's list of elements: "availability, price,
  promotion or quality".
- Wrong or missing: C05's HLPE definition lists "promotion, advertising and information" as one
  element. An awareness campaign and a front-of-pack warning are information. So C17 contradicts
  C05, and C17's shortening to "promotion" hides the clash. Ex 1(b) and (c) cannot be answered
  consistently.
- What closes it: name the element as C05 does. Say that a campaign moves the information element
  while leaving what is on offer unchanged, and restate "on the person" on that basis. Or change
  "moves no element" to "changes nothing on offer".

**H23 · B-C17-2 (M) · C17 Exercise 2**
- As it stands: "a Poshan Maah rally, the anganwadi rule on jaggery, and school nutrition
  gardens."
- Wrong or missing: none of the three is introduced anywhere. The text's rule is "white sugar
  should not be used", not a jaggery rule.
- What closes it: introduce Poshan Maah and nutrition gardens (one clause each, sourced), and
  either quote the guideline's jaggery wording or reword the exercise to match the white-sugar
  rule. The exercise wording is the fixer's call, not the compression pass's.

**H24 · B-C17-3 (M) · C17 Exercise 1(d); `definition.text`**
- As it stands: "(d) A tax on sugared drinks."
- Wrong or missing: a tax is not one of C01's stages, and whose decision it changes (maker,
  retailer, buyer) depends on who bears the tax. That is never taught.
- What closes it: one sentence in C17 locating a tax, for example at retail, changing the price
  element and the seller's pricing decision. Note that who bears it is left to rung 2.

**H25 · B-C17-4 (L) · C17 `must_know[3].point`**
- As it stands: "its awareness campaign on dietary guidelines for oil".
- Wrong or missing: "dietary guidelines" (ICMR-NIN's Dietary Guidelines for Indians) are never
  introduced.
- What closes it: name the guidelines in a clause, with year.

## C18

**H26 · B-C18-2 (M) · C18 `illustration.body`; Exercise 1**
- As it stands: "Take the first three ingredients, and milk solids and salt as well."
- Wrong or missing: the fourth ingredient, invert sugar syrup, is skipped. That breaks C03's rule
  to add up sugar under its several names. Exercise 1 asks for the first four.
- What closes it: say that invert sugar syrup is sugar under another name and counts with sugar
  (from sugarcane). Then the worked example follows C03 and matches the exercise.

**H27 · B-C18-3 (M) · C18 `illustration.body` table, palm oil row**
- As it stands: "Palm oil | oil palm | Basic customs duty on crude palm oil 5% ... | tools checked;
  origin unknown".
- Wrong or missing: a biscuit's palm oil is refined, or of unknown form. The refined-oil duty is
  never given, so "checked" overstates the link.
- What closes it: give the refined palm oil duty from the same release, or mark the tool "crude oil
  duty checked; whether it applies to this oil unknown".

**H28 · B-C18-4 (L) · C18 `illustration.body` table, sugar row**
- As it stands: "Rs 365 per quintal at 10.25% recovery, sugar season 2026-27".
- Wrong or missing: "recovery" (sugar recovered from cane, by weight) and "sugar season" (October
  to September) are undefined.
- What closes it: one clause each, from the CCEA release.

**H29 · B-C18-5 (L, cross-file) · C18 `illustration.body`, against C03**
- As it stands: "Mark the brand owner as seen, and the factory as unknown unless the pack names it."
  C03: "If the maker is someone else, the label shows the maker's licence number, not its name."
- Wrong or missing: whether the FSSAI licence number can be looked up to make the maker "checked"
  is never addressed.
- What closes it: one sentence saying whether the licence number identifies the maker (and where
  to look it up), or that this book does not use it.

**H30 · B-C18-6 (L, cross-file) · C05 and C09/C10, not C18**
- As it stands: C18 defines "a kirana, a small neighbourhood shop" and "A quintal is 100 kg".
- Wrong or missing: both terms are used earlier without definition, kirana in C05 ("a kirana
  shelf") and quintal from C09 on (see B-C10-2).
- What closes it: move each definition to its first use (C05, C09), and keep or drop the C18
  repeat.

**H31 · B-C18-7 (M) · C18 `illustration.body` table, wheat row**
- As it stands: "Support price for wheat, Rs 2,585 per quintal ...; bought into the central pool by
  the Food Corporation of India (FCI) | tools checked; this flour's wheat unknown".
- Wrong or missing: nothing shows how MSP or central-pool buying acts on a flour miller's wheat or
  its price. C09 says a farmer "may sell to them or in the open market".
- What closes it: one sentence on the route. MSP sets a floor that shapes the open-market price
  millers pay, and FCI open-market sales supply millers. Source it, or mark the link "asserted,
  not checked".

**H32 · B-C18-8 (L) · C18 `definition.text`; table**
- As it stands: the sketch traces "the policy tools that act on that crop".
- Wrong or missing: the tools that act on the product itself, FSSAI labelling and GST (both on
  C16's map), are left out. No GST rate is given anywhere, so the price side cannot start.
- What closes it: add a product row (FSSAI labelling: seen; GST rate on biscuits with its
  notification date: checked), or say that product-level tools are rung 2's.
