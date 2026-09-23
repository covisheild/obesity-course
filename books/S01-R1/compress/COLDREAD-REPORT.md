# Cold-read report: S01-R1-C01 to C10 (pass 1)

Reader: an intelligent adult with no background in the subject, who has read the twenty `-released.md` files (A3 to F4) and then C01 to C10 once, in order. Nothing else.

## Global findings (apply to several files)

- **GL-1. The Book 0 codes do not map to anything I was given.** The new book cites `B0-R0-C12`, `B0-R0-C32`, `B0-R0-C33` and `B0-R0-C42`. The earlier book's sections are labelled A3, A4, B4, E2, E3, F4 and so on, and no `B0-R0-Cnn` label appears anywhere in them. I *guessed* C12 = B4 (energy units), C32 = E2 (Atwater and the cascade), C33 = E3 (conservation and the boundary) and C42 = F4 (argument). Each guess was driven by content, and none was confirmed.
- **GL-2. The words for a unit of the book shift and are never defined.** It says "record" (C02, C03, C04, C05), "concept" (C07, C10), "section" (C08, C09), "booklet" (C10), "rung" / "this rung's build target" / "the gate this rung sets" / "later rungs of this subject" (C10), "this subject" / "this subject's held sources" (C02, C07, C08), and "held sources". I could not tell whether a record, a concept and a section are the same thing. "Rung", "build target" and "gate" have no referent anywhere.
- **GL-3. "Identity", "accounting identity" and "first law" are new names for E3's "balance line", and the text never says so.** Book 0 never used "identity" or "first law (of thermodynamics)". C06's title is "The first law for a body", and C07 has a "dynamic model, built from the first law of thermodynamics". I inferred that the first law means conservation of energy.
- **GL-4. Six of the ten files have no practice set.** C01, C03, C04, C06, C09 and C10 have no numbered problems. C01, C03 and C04 have no exercises either. So the sharpest gap detector is missing on exactly the files that make the most unsupported empirical claims (C03, C04, C09).
- **GL-5. Sources get thinner through the book.** C01 to C04 give a URL and a search string for each quote. C07's "*Lancet* paper by Hall and colleagues", C07/C08's "Thomas and colleagues", C07's "Wishnofsky (1958)" and C09's trial have no URL, no year (except Wishnofsky), no authors (C09) and no search string. I could not check any figure from them.

---

## C01: Body fat as stored chemical energy; fat mass and fat-free mass

**Exercises / practice.** There are none, so there was nothing to work. The illustration's "90 kilograms" is set up and never used in any calculation.

**What it changed for me**
- I will not read a weight change as a fat change without a statement of composition.
- I will stop assuming that a heavier person carries fat *instead of* lean tissue. The text says they carry more of both.
- I will refuse a fat-mass or fat-free-mass number that comes without a method.
- I now take body fat to be the largest energy store (Hall and Guo quote).

**Gaps**
- **C01-G1.** "Fat mass is the triglyceride held in adipose tissue." This defines fat mass as the triglyceride, not the tissue. Nowhere in C01 does it say that adipose tissue is *not* pure fat, yet C02 relies on exactly that ("Adipose tissue is not pure fat, `S01-R1-C01` already established"). C01 also never says which compartment the non-triglyceride part of adipose tissue (water, cells) belongs to. By the definition it must be fat-free mass, but a reader has to work that out alone.
- **C01-G2.** "A person carrying more body fat is not simply carrying fat mass in place of fat-free mass. They carry more of both." This is asserted with no source. The quote that follows is about fat-free mass driving REE, not about heavier people carrying more fat-free mass. It becomes a Must-know and is reused in C04, so the claim rests on nothing shown to me.
- **C01-G3.** The quote "contributes more to REE than body fat" uses "REE", which is not expanded here and is never expanded anywhere (C04 says "resting energy expenditure" but never ties it to the letters REE). "Metabolically active tissues" is not explained either. I could not say what the quote contributes to C01's point.
- **C01-G4.** "Body fat represents the vast majority of energy stores in the body compared with the energy content of body protein and glycogen." Book 0 (E6) taught that "The stores are glycogen and triglyceride". Body protein as an energy store is new and is not explained.
- **C01-G5.** "It is a large store." The pronoun has no clear referent. The sentence before it is "Naming a change in body weight is not yet naming a change in fat". I read it twice to settle on "fat in adipose tissue".
- **C01-G6.** "Ask for a method before you accept a number for either compartment." No method for measuring either compartment is named, anywhere in the book. I could ask for "a method" but could not judge any answer I got.
- **C01-G7.** Three terms are used for one thing: "body fat", "fat mass" and adipose tissue. C01 says "a person carrying more body fat" and defines "fat mass" as triglyceride. C02 later says "A kilogram of body fat lost or gained ... is adipose tissue". So "body fat" means triglyceride in one place and whole tissue in another (see C02-G2).

---

## C02: How much energy a kilogram of body fat holds

**Practice (worked)**
1. 0.80 × 9.0 = **7.2** kcal/g; 0.60 × 9.0 = **5.4** kcal/g. The unit is implied rather than stated.
2. 34,000 kJ = **34 MJ**; 2.5 MJ = **2,500 kJ**.
3. 39.5 / 7.6 = **5.2 times**.
4. 9.0 × 1,000 = 9,000 kcal/kg; 9,000 × 0.004184 = **37.656 MJ/kg**. That is not quite the "37" the text uses. E2 had warned that the two columns are rounded independently, so I let it go.
5. 39.5 MJ = 39,500 kJ; 39,500 / 4.184 = **9,441 kcal/kg**.
6. 0.87 × 37 = **32.19 kJ/g**, which equals 32.19 MJ/kg. It matches "32.2 MJ per kg" to rounding, and the match is the rule reproducing its own assumption, not a confirmation.
7. Broken step: "4 times 39.5". It applies the pure-fat density to a *weight* change. Weight is not all fat, and adipose tissue is not pure fat.
8. Broken step: "so the two figures confirm each other". The 7,700 was built by taking a fraction of the 9,000, so the two are not independent. The roughly 14% gap is the assumed non-fat fraction itself, which contradicts "essentially pure fat".
9. 5 × 9,000 = 45,000 kcal, and the arithmetic is right. It uses pure fat, though. Using the rule's 7,700 gives about 38,500 kcal. What it does not establish: what the 5 kg was made of, and so what deficit was actually needed.
10. 0.87 × 37 = 32.19 MJ/kg ≈ 7,690 kcal/kg. Hall *reports* 7,700 as the rule's assumption and does not confirm it. What it does not establish: any measured composition of adipose tissue. **But** doing the same sum in kcal (0.87 × 9.0) gives **7,830**, not 7,700 (see C02-G5).

**What it changed for me**
- I will never quote 9 kcal/g (37 to 39.5 MJ/kg) for a kilogram a patient lost or gained.
- I will say "the rule assumes 7,700 kcal/kg", never "adipose tissue is".
- I will treat two routes to one number that share an assumption as one confirmation, not two.
- I now know lean mass change is far lower in energy per kg (7.6 MJ/kg) than fat.
- I now know mega = 10^6.

**Gaps**
- **C02-G1.** "Adipose tissue is not pure fat, `S01-R1-C01` already established." It did not (see C01-G1). The same false back-reference appears again at "It is not pure fat — `S01-R1-C01` already told you that."
- **C02-G2.** "Pure fat holds about 9 kilocalories, or 37 to 39.5 megajoules, for each kilogram." This is **wrong by a factor of 1,000**: it is 9 kcal per *gram*. The Must-know that follows repeats the error: "Never quote 9 kilocalories or 37-39.5 megajoules a kilogram." A reader who memorises the Must-know points memorises a false figure.
- **C02-G3.** "It is about 9 kilocalories a gram, which is 9,000 a kilogram, or ... about 37 to 39.5 megajoules a kilogram." 9 kcal/g converts to about 37.7 MJ/kg. 39.5 MJ/kg is about 9.44 kcal/g, so the sentence equates 9 kcal/g with a range that runs past it. The text also never says *why* Hall's "metabolizable energy density" (39.5) is higher than FAO's Atwater figure (37), when E2 taught that the Atwater factors are themselves metabolizable, and E2's footnote gave fat's precise value as 37.4. The table calls Hall's figure "physiological" without defining the word. I could not say which figure to use when.
- **C02-G4.** "Hall (2008) states that the classic weight-loss rule 'can be traced back to...'" This uses "the classic weight-loss rule" before saying what the rule is. Its content (3,500 kcal a pound) first appears 75 lines later, and it is not properly introduced until C07.
- **C02-G5.** "Take the fraction, 0.87, and multiply by fat's own energy per gram." The "In plain terms" part works in kcal, and in kcal 0.87 × 9.0 = 7.83 kcal/g, which is **7,830 kcal/kg, not "roughly 7,700"**. The text reaches 7,700 only by using 37 kJ/g and converting. Practice problem 1 then tells me to multiply by 9.0. A reader who follows the kcal route gets the "wrong" answer and is not told why (the rounded 9.0/37 columns from E2).
- **C02-G6.** "the source's own extraction note says the superscript formatting is lost in the fetch." There is no extraction note visible to me, and "the fetch" is not something I did. This is a production artefact leaking into the text.
- **C02-G7.** The working "37 times 1000 = 37000 / 37000 divided by 1000 = 37" has no units on any line, and the gloss says "the two divisions and multiplications cancel" when there is one of each. I had to work out the units myself (kJ/g × g/kg, then ÷ kJ/MJ).
- **C02-G8.** "lean mass change 7.6 MJ/kg — hall_2008_ijo" / "The fourth row is named, not explained." The figure has no quote and no search string, so I cannot verify it. It also appears right after a quote giving *protein* as 19.7 MJ/kg, with nothing to say how lean tissue comes out lower than its own protein (water is my guess, and it is not in the text). It is still used in practice problem 3 and in a Must-know.
- **C02-G9.** "the paper that reports the assumption also says the true figure is variable." This is asserted with no quote.
- **C02-G10.** "the same figure `S01-R1-C07` reaches by converting 3,500 kcal a pound directly. Two routes, one assumption: the fraction 0.87 is what both calculations are built on." This is a forward reference to a file I had not yet read. And C07 then attributes the 3,500 figure to Wishnofsky's "estimation of the energy content of weight lost", not to an 87% calculation. So I could not see that the pound route rests on 0.87 (see C07-G3).
- **C02-G11.** "the only figure for that fraction in this subject's held sources". "Held sources" is undefined jargon (GL-2). The table's source column ("fao_food_energy_2003", "hall_2008_ijo") uses internal keys that are never explained.
- **C02-G12.** "The near-exact match ... is not two confirmations." The sentence says what the match is not and stops. The Must-know supplies the rest, but at this point I had to infer "it is one assumption seen twice".

---

## C03: A day of intake and a day of expenditure: the sizes

**Exercises / practice.** There are none. I could not test myself on the three-kinds distinction.

**What it changed for me**
- Before I repeat a daily energy figure, I will name which kind it is: measured expenditure, adopted requirement, or survey estimate.
- ICMR 2020: sedentary man 2,110 kcal, sedentary woman 1,660 kcal.
- NSS rural all-India 2022-23: 2,233 kcal per person per day.
- I will treat self-reported intake as unreliable.
- I will not use a population figure as an individual's prescription.

**Gaps**
- **C03-G1.** "the number came out between about 8 and 16 megajoules a day." This contradicts the definition two paragraphs earlier ("a few megajoules to about ten of them"): 16 is not "about ten". It is also unsourced, because "In three groups it measured" names no groups and gives no quote.
- **C03-G2.** "There is a way to measure this directly, called doubly labelled water." The method is only named. Nothing says what is labelled, how it measures anything, or why it counts as "direct". I could not have told anyone what it is.
- **C03-G3.** "A measured group of sedentary or lightly active women averaged 1,975 kilocalories a day." The quote it rests on begins "**If** this PAL was from a female population ... TEE = 1.53 x 5.40". That is a hypothetical calculation (a multiplier times a BMR), not a measurement of a group. So in the section whose whole point is naming the kind of number, the number is given the wrong kind. The problem carries over to C05 practice problems 3 and 4 ("a measured total energy expenditure of 8.26").
- **C03-G4.** "PAL", "BMR" and "TEE" in that quote are never expanded. I could not follow the one calculation shown.
- **C03-G5.** "The first row is men, the second women, and the number under ICMR 2020 is the one to use." The quoted rows ("2110 2320 -210") carry no column headings. I had to take on trust which column is ICMR 2020 and guess that 2320 is an older figure and -210 the difference.
- **C03-G6.** "The first figure, 2,233 kilocalories a day, is what an average Indian household's recorded food purchases convert to per person, rural, 2022-23." The row has eight numbers and no headings, and "rural, 2022-23" cannot be checked from what is shown. The phrase "food purchases" also contradicts the earlier "food bought or grown by their household".
- **C03-G7.** "the number under ICMR 2020 is the one to use: 2,110 kilocalories a day for him, 1,660 for her." This applies an adopted population requirement to two individual patients. It directly contradicts the Must-know "Do not use a population figure as an individual's prescription." I did not know which of the two instructions to follow.
- **C03-G8.** "roughly 1,660 to 2,720 kilocalories a day for a woman, sedentary to heavy work, and 2,110 to 3,470 for a man." The heavy-work figures (2,720 and 3,470) appear only in the Must-know. They were never shown or sourced in the body.
- **C03-G9.** "Ask somebody to report what they ate and the answer is known to be unreliable." This is asserted with no source and no direction: does self-report run under, over, or both? It is also a fourth kind of number next to "three kinds".
- **C03-G10.** "converted to energy through a nutrient conversion table." The term is not defined. E6's "food composition tables" is presumably the same thing, but the text does not say so.
- **C03-G11.** "for the same activity band." The text asserts that FAO's "sedentary or light activity" and ICMR's "sedentary work" are the same band, and never shows it. The FAO women (55 kg, 30 to 50 years, nationality unstated) are called "a comparable population" with no reason given.

---

## C04: What expenditure is made of, and why a bigger body spends more

**Exercises / practice.** There are none. The illustration's own question, "Ask which of them has the higher daily energy expenditure", I answer as the 95 kg patient.

**What it changed for me**
- Expenditure has three parts: resting, thermic effect of food and activity.
- Resting is the largest, and REE rises linearly with fat-free mass and with fat.
- Activity cost scales with body weight.
- I will not assume a person with obesity has a "slow metabolism". Their absolute expenditure is generally higher.
- I will expect expenditure to fall as weight falls, and will not call that a failure.

**Gaps**
- **C04-G1.** "Resting energy expenditure ... is the largest of the three." And in the Must-know: "the thermic effect of food, the smallest". Neither ranking has a figure or a source, and "the smallest" first appears in the Must-know. "By a wide margin" is also unsourced.
- **C04-G2.** "Protein takes more effort to process than carbohydrate, and carbohydrate takes more than fat." This is asserted with no source.
- **C04-G3.** "Ask which of them has the higher daily energy expenditure, before checking anything." The question is never answered, and no number is put on either patient. I inferred the answer from the quotes.
- **C04-G4.** "The other weighs 95 kilograms, of which a larger fat-free mass is part." It does not say larger than what. I read it twice before settling on "larger than the 55 kg patient's".
- **C04-G5.** The quotes use "REE". The text never states that REE = resting energy expenditure (see also C01-G3).
- **C04-G6.** "Expect the number that once held their weight steady to fall as their weight falls." Neither "the number" nor "their" has a referent in that bullet or the one before it. I guessed "the patient's energy requirement".
- **C04-G7.** "Do not use it to compute a patient's requirement; use it to say what a computed requirement would have to account for." "It" has no referent (this section? the pattern? the three-part split?).
- **C04-G8.** "The thermic effect of food is the energy spent digesting, absorbing and processing what was eaten." E2 taught that *net* metabolizable energy "takes off the energy the body itself spends on digesting the food". The text does not say whether the thermic effect is that same quantity. If it is, I cannot tell whether counting it as expenditure double-counts it. C05 later says intake is *metabolisable*, not net metabolisable, which suggests no double count, but a reader has to work this out alone.
- **C04-G9.** "a person carrying more body fat generally carries more fat-free mass too." This Must-know inherits C01-G2's unsupported claim.

---

## C05: The accounting identity for a body

**Exercise 1.** 540 + 10 × (8.9 − 9.4) = 540 − 5 = **535 MJ**. For the part about body mass, I could only say that the mass lost must hold 5 MJ. Using C02 that is about 0.16 kg if it is adipose tissue at the rule's 32.2 MJ/kg, or about 0.66 kg if it is lean mass at 7.6, and either could be hidden by day-to-day water swings. C05 itself says it "does not supply" that fact.

**Practice (worked)**
1. 380 − 410 = **−30**.
2. Row 1: 30. Row 2: expenditure 520 (500 − 520 = −20). Row 3: intake 495. Row 4: 0.
3. 8.80 − 8.26 = **+0.54 MJ**, so stores rose. (The 8.26 is again called "measured"; see C03-G3.)
4. 14 × 8.26 = 115.64; 115.64 − 9.8 = 105.84; ÷ 14 = **7.56 MJ/day**.
5. Broken step: "so 1,800 kilojoules crosses into their energy stores". A bomb calorimeter gives gross energy, and the identity needs metabolisable intake.
6. Broken step: "−0.4 minus −0.6". Changes over consecutive days add: −0.4 + (−0.6) = −1.0, so stores *fell* by 1.0 MJ.
7. A flat weight over three months shows only that mass in matched mass out *over the interval* (C9). It does not show that energy matched (composition can shift), and it says nothing about "every single day".
8. 8.0 − 8.5 = −0.5 MJ/day while both hold. What it does not establish: that "supplying" 8.0 MJ is metabolisable intake actually eaten, or that expenditure stays at 8.5 as she loses weight (C04 says it falls).

**What it changed for me**
- I will state the interval before quoting any figure built from the identity.
- Intake means metabolisable intake, not gross energy.
- A mismatch means a missing route, not a failed identity.
- A flat scale is not biological quiet.
- The identity answers no causal question.

**Gaps**
- **C05-G1.** "Whenever the two sides are computed correctly for the same boundary." The section never says *which* boundary is drawn round the body. E3's Must-know insisted: "Two lines are both in use. One is at the mouth and skin ... The other is at the gut wall ... Say which one you mean." Then "metabolisable intake" nets off urinary and surface losses, which fits neither of E3's two lines. I could not state the boundary this identity uses.
- **C05-G2.** "A person's energy stores are measured at the start of the week: 620 megajoules." The section itself says "Body energy stores are not measured directly day to day." The illustration's starting point is something the text says cannot be done, and unlike Book 0's convention it is not flagged as made up.
- **C05-G3.** "A day-to-day mismatch is usually a sign the interval is too short for food still in the gut and water shifts to average out, not a sign the identity has failed." Mismatch between what and what? The definition says the two sides match "with no exception and no remainder". Presumably the mismatch is between the identity and a *mass* reading. But water shifts carry no energy, so they cannot unbalance an energy identity. I read this twice and still had to supply "they mean the scale".
- **C05-G4.** The section is titled "The accounting identity", and "Identity" is never defined as a term (GL-3). The link to E3's "balance line" and C9's "stock now = starting stock + in − out" is only implied by "a stock, in the sense Book 0 gives that word".
- **C05-G5.** "the figure that survives the losses `B0-R0-C32` names." The code mapping is unresolved (GL-1).
- **C05-G6.** "say in words what has to be true of their body mass for that change to show up on a scale." Exercise 1 asks for exactly the energy-to-mass fact the section says it "does not supply". I could only start it by reaching back to C02.
- **C05-G7.** "A reference sedentary or lightly active adult woman has a measured total energy expenditure of 8.26 megajoules a day." "Reference" is undefined, and "measured" repeats C03-G3.

---

## C06: The first law for a body in one sentence, without a lever

**Exercise 1.** Premise: calories in minus calories out equals weight change. Conclusion: weight change is entirely under a person's control. The inference fails because the premise says nothing about control. It needs hidden premises: that intake is freely chosen (F4) and that expenditure does not respond to a cut. The premise is itself wrong as stated, since the identity is about energy, not weight (C9).

**What it changed for me**
- "Energy in minus energy out" is a premise, not a conclusion.
- When someone derives "eat less" from it, I will ask what they assumed about expenditure.
- The identity is compatible with every causal account, so it cannot choose between them.
- A good line for a journalist: "the arithmetic is real and settles nothing about cause".

**Gaps**
- **C06-G1.** The title says "without a lever", and the text later refers to "a direction of control the identity never supplied". "Lever" is never explained. I guessed "a handle you can pull to control the outcome".
- **C06-G2.** "The one-sentence statement: a person's energy stores change only by the energy..." The title calls this "the first law", and the first law is never defined (GL-3).
- **C06-G3.** "It needs a further premise, about what happens to expenditure and appetite when intake changes." This is the first appearance of "appetite" in the new book, and it is undefined. The illustration's missing premise is only about expenditure ("and expenditure does not change when intake does"). So why appetite belongs in the premise is not explained: appetite acts on intake, which the argument holds as the thing being cut.
- **C06-G4.** "Watch for the sentence doing the work of an inference nobody has actually made." Which sentence? I read it twice and could not turn it into an action.
- **C06-G5.** "Do not let the identity stand in for an account of why it changed, which you may not have." "It" has no referent (weight? stores?).
- **C06-G6.** "The identity is consistent with every serious account of why weight changes." The identity is about *energy stores*, and C9 warned that energy and weight are two separate balances. C06 slides from one to the other here and in the exercise's pamphlet without comment.
- **C06-G7.** "the way `B0-R0-C42`'s own illustration does it". F4's illustration never actually writes its missing premise out as a sentence. It describes it ("Nobody ... says out loud that eating sits untouched by price"). This is a small mismatch, and it again depends on GL-1.

---

## C07: Sizing an imbalance, and the static rule

**Exercises (worked)**
- Exercise 1: 600 × 40 = 24,000 kcal; ÷ 7,716.18 = **3.11 kg**.
- Exercise 2: No, not as a long-run promise. It is roughly right only at the start. Weight loss slows because expenditure and appetite respond. For a 2 MJ/day cut, the modelled year-one loss is about half the rule's figure.

**Practice (worked)**
1. 3,500 / 0.45359237 = **7,716.18** per whole unit.
2. **17,500**; **42,000**.
3. 1,439 × 64.8 = 93,247.2; ÷ 3,500 = **26.64 lb**; × 0.45359237 = **12.09 kg**.
4. 2 / 0.004184 = 478.01 kcal/day; × 365 = 174,473.65; ÷ 7,716.18 = **22.6 kg**. This matches the paper's "22 kg".
5. Broken step: "every year, forever". A heavier body spends more (C04), so a fixed 200 kcal surplus shrinks as weight rises, and the straight line does not continue.
6. Broken step: "8 times 3500". It applies the per-*pound* rate to kilograms. It should be 8 × 7,716 ≈ 61,700 kcal (or 17.6 lb × 3,500).
7. 500 × 7 = 3,500 kcal = 1 lb a week; 26 weeks gives 26 lb (11.8 kg). What it does not establish: that loss stays linear. Thomas found about 27% less than predicted within about 9 weeks, and Hall's model roughly halves year one. It also says nothing about the loss's composition.
8. Same arithmetic. "Reliably" is what is not established: the rule overpredicts, and individual responses vary.

**What it changed for me**
- Convert pounds to kilograms first (1 lb = 0.45359237 kg exactly).
- A rule that holds a daily amount fixed always draws a straight line.
- I will state the interval whenever I use the rule.
- A widely printed figure is not thereby a measured one.
- A kilogram of fat is several days of total expenditure.

**Gaps**
- **C07-G1.** "The rule fails for two separate reasons, and only the second is this concept's subject. Second, and the reason a straight line is the wrong shape..." **The first reason is never stated.** I had to guess it, probably that the energy per kg is not fixed or known (C02). This is the most visible hole in the book.
- **C07-G2.** The definition converts a deficit "into a change in fat mass". The common form is "for each pound of body weight changed". The comparison table is headed "weight change", and Thomas's outcome is "lost 20.1 pounds" (weight). C01 and C02 drilled that weight is not fat, yet here fat mass and body weight are swapped without comment. I could not tell which quantity the rule predicts.
- **C07-G3.** "a figure this subject's held sources trace to Wishnofsky (1958) and describe as 'derived by estimation of the energy content of weight lost'." C02 traced the same figure to "a calculation that assumes exclusive loss of adipose tissue consisting of 87% fat". Two origin stories are given and never reconciled. "Estimation of the energy content of weight lost" also sits awkwardly with "It is not a fact anybody measured about fat."
- **C07-G4.** The working "1439 times 64.8 = 93247.2 / 93247.2 divided by 3500 = 26.64" is followed by the quote "the 27.6±16.0 lbs predicted by the 3500 kcal rule". My own prediction (26.64 lb) does not match the paper's (27.6 lb), and the text is silent about it. I could not tell whether I had made an error. Also, 27.6 − 7.4 = 20.2, not the stated 20.1.
- **C07-G5.** "7.4±12.6 lb" and "27.6±16.0". The ± notation was never taught, and standard deviation or spread is not in Book 0. I could not read what ±12.6 means, or notice that it implies many people lost *more* than predicted.
- **C07-G6.** "The paper's own dynamic model, built from the first law of thermodynamics rather than from a fixed rate, predicts something different." The dynamic model is not explained at all. The static rule also obeys conservation, so "built from the first law rather than a fixed rate" is not a contrast I can understand. The paper has no year, URL or search string (GL-5).
- **C07-G7.** "Second, and the reason a straight line is the wrong shape". "Straight line" is used before the plain-terms part introduces plotting the rule. C6 from Book 0 lets me guess.
- **C07-G8.** "Nobody's daily intake and daily expenditure sit still while they lose weight." In the illustration, intake is cut "and keeps it cut", which is held fixed by assumption. So in that scenario only expenditure moves, and the text never makes that distinction.
- **C07-G9.** "The straight-line projection is reliable only over an interval short enough that intake and expenditure have not yet responded." No interval is given. Thomas already shows a large miss at 64.8 days. The Must-knows say "The straight line from the static rule is not wrong on day one" and "say over what interval it holds", but I cannot supply any interval. Practice problem 8 ("reliably ... a pound a week") needs one.
- **C07-G10.** "A rule states that 3,500 removes one unit of weight for every 0.45359237 of a different unit that measures the same thing." Practice problem 1 is garbled: "removes one unit ... for every 0.4536 of a different unit" does not parse. I read it three times and answered it by pattern-matching to the text's own working.
- **C07-G11.** "both sources here agree that response starts working against the deficit within the first year." The Thomas material shown says nothing about timing or mechanism. Only the size of the shortfall is quoted.
- **C07-G12.** "It has the wrong shape. It says every year should look like the first." "It" follows a two-row table and has to be resolved as "the static rule".

---

## C08: Spotting a claim that breaks conservation

**Exercises (worked)**
- Exercise 1: 1 lb/day × 10 = 10 lb = 35,000 kcal, or 3,500 kcal a day, with "no change to diet or exercise". No route is named for the energy. The claim needs a daily deficit about the size of a whole day's expenditure (C03). I would ask for the measured composition of the loss (fat or water), the method of measurement, the individual data, and the route.
- Exercise 2: 5 kg of *pure* fat is 5 × 9,000 = 45,000 kcal (C02 says use pure fat for pure fat). Over 7 days that is about 6,400 kcal a day of deficit while eating normally. That is above any whole-day expenditure in C03 (at most about 16 MJ ≈ 3,800 kcal), so it is impossible as fat. Ask about water and glycogen.

**Practice (worked)**
1. 6 × 3,500 = **21,000**.
2. 24,500 / 3,500 = **7 units**.
3. 2 × 3,500 = **7,000 kcal/day**.
4. 7,000 / 1,439 = 4.86, which is **4.9 times**.
5. Broken step: "therefore the claim must be true". Conservation rules claims out and never rules them in (E3). On water only, the most the deficit can be is a week's total expenditure (about 14,000 to 28,000 kcal). Against 4 × 7,716 ≈ 30,900 kcal the claim is implausible or impossible for most people.
6. Broken step: "so the reported loss must be fabricated". It assumes the loss was fat. Glycogen and water explain a fast early loss. I could not put a number on the glycogen-plus-water energy (C08-G5).
7. 8 kg × 7,716 = 61,730 kcal (or × 9,000 = 72,000 if "pure fat"), over 10 days that is about 6,200 to 7,200 kcal a day. That is above any total expenditure in C03, so it is impossible as fat. And "calories don't matter" does not follow from anything. What it does not establish: what the 8 kg actually was.
8. 12 × 7,716 = 92,600 kcal over 21 days ≈ 4,400 kcal a day. That is near or above even a large person's total expenditure, so the loss is probably not all fat. The identity holding says nothing about "nothing else going on". I could not finish this one: "bariatric" and "after surgery" are never explained, and I have no expenditure figure for a heavy post-surgery patient.

**What it changed for me**
- A deficit can be no bigger than total expenditure.
- A claim that names no route fails E3.
- A fast early loss on a low-carbohydrate diet is often glycogen and water.
- I will ask for the time period first, and say what the check did not do.

**Gaps**
- **C08-G1.** "The largest average deficit anyone in that pooled group sustained, across the whole cohort ... was 1,439 kilocalories a day." And later: "roughly five times the biggest deficit ever measured in that supervised cohort". C07 says the cohort was "averaging a 1,439 kcal per day deficit". An average is not the largest, and "largest average ... anyone sustained" does not make sense. The comparison is therefore wrong: individuals ran bigger deficits (C07's ±).
- **C08-G2.** "A claim whose required energy exceeds every plausible deficit ... is impossible on energy grounds alone." And: "biggest possible deficit ... whole expenditure ... So if the energy the claim requires is bigger than any plausible deficit ... the claim cannot be true." This slides from *possible* (a hard ceiling equal to total expenditure) to *plausible* (a soft one). Exceeding a plausible deficit makes a claim implausible, not impossible.
- **C08-G3.** The illustration tests the 7,000 kcal/day claim against Thomas's 1,439, never against the hard ceiling the section just defined (total expenditure, which C03 puts at about 2,000 to 4,000 kcal). A reader copying the illustration never learns to do the decisive comparison.
- **C08-G4.** "using the static rule's own conversion from this subject's C07". C07 and C02 have just taught me to distrust this figure ("never 'adipose tissue is'"). The text does not say why it is acceptable here (it is conservative, being lower than pure fat's 9,000, so it makes a claim *easier* to pass). I had to reason that out myself, and I was unsure whether to use 7,716 or 9,000 for "pure fat" claims (Exercise 2, problem 7).
- **C08-G5.** "it is a different substance leaving the boundary, at a different energy cost per kilogram than fat." No figure is given for glycogen plus its water, and no ratio of water to glycogen. C02's quote gave glycogen alone as 17.6 MJ/kg. So practice problem 6 and the low-carbohydrate example can only be answered qualitatively. "Glycogen is stored together with water" is asserted without a source.
- **C08-G6.** "which this subject's B0-R0-C33 already rules out". B0 is Book 0, not "this subject", and the code does not map (GL-1).
- **C08-G7.** "A bariatric patient of mine dropped 12 kg in the first three weeks after surgery". "Bariatric" is undefined in either book, and I could not use the fact that the patient had surgery.
- **C08-G8.** "compare that required amount with the largest deficit that has plausibly crossed the person's boundary". A deficit is a difference between two crossings, not something that crosses. The wording made me stop.

---

## C09: Intake and expenditure are outputs of a regulated system

**Exercise 1.** The colleague's argument hides a premise: that expenditure and appetite are unchanged. The arithmetic has not changed, but its inputs have. A smaller body spends less (C04). Expenditure falls further still, adaptively. Appetite rises by about 100 kcal/day per kg lost. So the same intake can now match a lower expenditure, and a plateau is the expected result, not proof of non-adherence.

**What it changed for me**
- A weight plateau is the expected output of a loop, not a lapse by the patient.
- Rising appetite is the larger push-back, so I will talk about hunger, not only "slow metabolism".
- A formerly heavier person needs roughly 300 to 400 kcal/day less.
- I will not quote those figures to a patient as their personal forecast.
- None of this is about character.

**Gaps**
- **C09-G1.** "That pull is more than three times the size of the matching fall in expenditure." The illustration's own numbers give 800 against 300 to 400, which is **2 to 2.7 times, not "more than three"**. They also compare an 8 kg loss with a 10%-of-body-weight loss, which are only equal for an 80 kg person, and that is not stated. "Matching" is never defined.
- **C09-G2.** "The rest, about 10 to 15% of the total, is extra." Total what? Total expenditure, or the total drop? I read it twice. Only by back-solving from 300 to 400 kcal did I conclude that it is 10 to 15% of total daily expenditure.
- **C09-G3.** "The expenditure fall for a person who lost a full 10% of body weight sits at 300 to 400 kcal a day." Here 300 to 400 is called *the* fall, but the plain terms (a fall of a fifth to a quarter) and the Must-know ("300 to 400 fewer calories than someone who was always that weight") make it the *extra* part only. The appetite comparison in C09-G1 depends on which one is meant.
- **C09-G4.** "Take the trial the appetite figure above comes from ... They found intake climbing." The trial has no authors, year, URL or quote, and "They" has no referent (GL-5).
- **C09-G5.** "in 153 people with type 2 diabetes". Type 2 diabetes is not defined in either book. E8 taught insulin and glucagon but never the disease.
- **C09-G6.** "Expenditure falls by more than the loss of fat and lean mass alone accounts for." "a system that senses body weight, or a signal that tracks it". Both are asserted in the definition with no source anywhere in the section.
- **C09-G7.** "close to 100 kcal a day of extra eating ... close to 800 kcal a day of extra wanting to eat". The text slides from measured intake to appetite ("wanting"). They are not the same quantity, and the text treats them as one.
- **C09-G8.** "'Cut intake and only fat is lost' is incomplete." The section never discusses what is lost. It is about push-back, so this Must-know does not match the content. I guessed that "only fat is lost" was meant to be "weight keeps falling".
- **C09-G9.** "They are outputs of a system..." The first word of the definition has no antecedent in the body. It relies on the title.
- **C09-G10.** "the neuroendocrine mechanism". "Neuroendocrine" is not defined. E8 gives "endocrine", and "neuro-" I had to guess.

---

## C10: Arithmetically true, practically insufficient

**Exercises.**
- Exercise 1: answer first. The calories-in-calories-out arithmetic is true, but it does not make obesity simple. When intake is cut, the body spends less and appetite rises, so a fixed instruction produces a stall and not a steady loss. Then one sentence on the hidden premise.
- Exercise 2: I could write the page, but I cannot check it against the "build target" or the "gate" (C10-G5).

**What it changed for me**
- I will state the identity and the instruction as two separate claims.
- "They must not be sticking to it" invents a premise.
- The three-minute argument: the accounting is true, the instruction adds an assumption, the assumption is false, and the difficulty is physiological.
- The instruction can still work for some people.

**Gaps**
- **C10-G1.** "So cut intake, or raise expenditure, and stores must fall." This states as fact the very inference C06 said "does not follow ... not on the premise alone". C10 then moves the fault to "stores keep falling on their own", which is a different claim from C06's. I could not reconcile the two sections.
- **C10-G2.** "The inference fails, and it fails at premise two's hidden clause." In F4's terms, a false premise and a failed inference are the two *independent* failure modes. The illustration's argument is valid (if expenditure and appetite are fixed and intake is cut, a failure to lose does imply intake was not cut). What fails is premise two's *truth*. Line 23 says as much: "adding a premise that was never checked and is not true". The section uses the wrong one of the two failure modes it says Book 0 taught.
- **C10-G3.** Premise two: "once a person cuts intake, expenditure and appetite do not move". The conclusion is "a person not losing weight has not really cut intake". If rising appetite leads the person to eat more, then they have indeed not kept intake cut, and the doctor's conclusion is literally true. The text does not deal with this. Only the expenditure half of the rebuttal clearly defeats the doctor, and I had to work that out myself.
- **C10-G4.** "it fails at premise two's hidden clause: 'with expenditure held fixed'." Premise two is cited before it is laid out, and the definition's wording (expenditure only) differs from the illustration's (expenditure *and* appetite). "Exactly as an earlier concept establishes" does not say which concept.
- **C10-G5.** "Write the one-page explanation this rung's build target asks for", "that is the gate this rung sets", "a plan needs the later rungs of this subject". "Rung", "build target" and "gate" appear nowhere else. I could not see the target I am meant to meet (GL-2).
- **C10-G6.** "they move in response to the fall in stored energy". C09 said the system "senses body weight, or a signal that tracks it", not stored energy. A small inconsistency, but the two sections name different signals.
- **C10-G7.** Premise one reads "stored energy changes at a rate equal to intake minus expenditure", and the conclusion is about a person "not losing weight". The argument needs a further premise joining energy stores to weight (C9, C05-G3), and the text does not name it.

---

## Gap counts

| File | Gaps |
|---|---|
| Global | 5 |
| C01 | 7 |
| C02 | 12 |
| C03 | 11 |
| C04 | 9 |
| C05 | 7 |
| C06 | 7 |
| C07 | 12 |
| C08 | 8 |
| C09 | 10 |
| C10 | 7 |
| **Total** | **95** |

## Three most serious

1. **C02-G2.** The Must-know says pure fat holds "about 9 kilocalories ... for each **kilogram**". That is wrong by 1,000×, and the error sits in the line a reader memorises.
2. **C07-G1.** "The rule fails for two separate reasons": the first reason is missing entirely. Close behind are C07-G2 (fat mass and body weight used interchangeably) and C07-G4 (my computed 26.64 lb against the quoted 27.6 lb, with no comment).
3. **C03-G3 / C03-G7.** The "measured" 1,975 kcal is a hypothetical PAL × BMR calculation, mislabelled as a kind of number in the section about kinds of number, and the error carries into C05's practice problems. The same section applies a population requirement to two individual patients and then forbids doing so.

Next in severity: C08-G1 (an average called "the largest"), C09-G1 ("more than three times" when its own numbers give 2 to 2.7), C10-G1/G2 (contradicts C06, and misnames the failure mode), and C01-G1/C02-G1 (C02 relies on a fact C01 never gave).
