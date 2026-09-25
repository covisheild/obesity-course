# S37-R1 compression pass, batch r1 (C01 to C06): holes for the fixer

Holes the restore could not close. The full-length original does not fill them either, or they are
errors or contradictions, or (H6, H7) the original fills them but the restore failed the
mean-sentence check. "As it stands" quotes the final text (`<S>-final-prose.yml`); fields are the
prose-file keys. Gap ids from `COLD-READ-GAPS.md` are given in brackets. They are for the audit,
not for the compression pass.

## Across sections

**H5** [A-C01-6, A-C02-11, A-C03-9, A-C05-6]. C01, C02, C03 and C05 have no Illustration and no
practice set. Their key methods are never run once on numbers or on a single food: the eight
stages (C01), the loss figures and the 55 kg (C02), "together they may outrank the first
ingredient" (C03), the four questions (C05). To close: add an Illustration to each, and a practice
set as `claude.md` requires, through the drafting and audit route rather than this pass.

## C01

**H1** [A-C01-2] `definition.text`. "This book reads the system as eight stages: production,
storage, processing, distribution, retail, preparation, consumption and waste. The list is this
book's reading of HLPE's sentences, not a list HLPE prints." Missing: why eight, why storage
comes before processing when HLPE pairs "storage and distribution", and why waste is a stage when
HLPE speaks of outputs. To close: one or two sentences deriving each stage from a phrase of HLPE's
definition or supply-chain list, and a rule for a step that fits two stages.

**H2** [A-C01-3] `simplified_explanation`. "Each step is done by somebody, such as a farmer, a
trader, a mill owner, a shopkeeper or the person who cooks. Call each of them an actor ..."
Missing: who the actor is at the waste stage, and whether the state counts as an actor (C05 later
says the state decides). Ex 1 needs an actor at every stage. To close: name an actor for waste and
say whether the state is an actor.

**H3** [A-C01-4] Exercise 1. "Then mark each line 'checked' or 'guessed'." C01 names no kind of
source that could check a stage, so every line can only be "guessed". To close: name, in the
must-know or plain terms, the kinds of source that check a stage (a trade study, a label, a
government table), or move the checked/guessed step to C02, whose Ex 3 asks for it.

**H4** [A-C01-5] Exercise 3. "A first-year resident asks why this book says 'food system' rather
than 'diet'." C01 never gives the reason and never mentions diet or obesity. To close: a sentence
giving the reason (the shelf others filled, C05's argument), or re-point the exercise to C05.

**H6** [A-C01-7] `definition.text` / must_know[3]. The must-know asks "Household waste in or out?"
while waste is one of the book's fixed eight stages. The original closes this: "Which stages,
places and flows count as inside is fixed by a boundary, chosen by whoever is doing the
accounting, as for any system." (24 words). Restoring it raises C01's mean sentence above the
original's (13.63) in every combination with the two dangling-antecedent restores. To close:
the fixer decides whether to restore it and cut elsewhere, or split it on the audit route.

## C02

**H7** [A-C02-2] `must_know[1].point`. "That is the NABCONS study for 2020-22, as the ministry reported it
in 2025." NABCONS is never identified and "the ministry" never named. The original's Definition
sentence names both ("a study by the consultancy NABCONS for the Ministry of Food Processing
Industries (reference years 2020-22)", 32 words) but could not be restored alongside the RBI source
sentence without raising the mean above 14.50. To close: restore it on the audit route, or name the
ministry in the figure caption.

**H8** [A-C02-3] Figure caption and `must_know[1].point`. "Per cent lost after harvest, in farm
operations and at market level." Per cent of what is never said; the two may be on different
bases. To close: state the base of each percentage from the NABCONS study.

**H9** [A-C02-4] `definition.text` against the figure. UNEP's loss is "up to, and excluding, the
retail level"; the figure has a "market level" row. Whether market-level loss is UNEP loss is not
said. To close: one sentence placing NABCONS's market level against UNEP's retail line.

**H10** [A-C02-5] `must_know[1].point`. "never add them as if that were the study's own total." No
reason is given (different bases? percentage of a percentage?). To close: give the reason, and say
what a correct combined figure would need.

**H11** [A-C02-6] `must_know[2].point`. "India's household food waste of 55 kg per person a year is
UNEP's 'medium confidence' estimate." What "medium confidence" means in UNEP's scheme is never
said. To close: one sentence on UNEP's confidence levels.

**H12** [A-C02-8] Exercise 2. "Indian households throw away 78 million tonnes of food every year."
C02 gives no population, so the reader cannot check the 78 (55 kg × C06's population is about
76.6 Mt, and the year differs). To close: give the population UNEP used, or say in the exercise
that the check uses C06.

**H13** [A-C02-9] `simplified_explanation`. "A trader buys it, helped by a commission agent — a
middleman paid a percentage for arranging the sale." A percentage of what, and paid by whom, is not
said (the restored "The trader pays a fee to the mandi and a commission to the agent" settles who
pays). C04's farm-gate price depends on it. To close: state the commission's base.

**H14** [A-C02-10] `simplified_explanation`. The onion route (grow, mandi, truck, city mandi, shop)
is never mapped onto C01's eight stages. The restored "Potatoes often sit for months in a cold store
on the way." shows storage for potato only. To close: one sentence saying which stages a fresh
onion passes through and which it skips.

## C03

**H15** [A-C03-2] `definition.text`. "It states an ingredient's percentage only where regulation
5(2)(g) requires one, for example where the label emphasises that ingredient in words or
pictures." "For example" leaves the triggers open; Ex 2 turns on whether its case triggers it. To
close: state 5(2)(g)'s triggers in full, or say this is the only one the exercises use.

**H16** [A-C03-3] `definition.text`. 'milk products as "Milk solids", with the source optional.'
"Source" (animal? origin? supplier?) is unclear. To close: quote or paraphrase what the regulation
makes optional.

**H17** [A-C03-4] `must_know[1].point`. "Sugar and invert sugar syrup are listed as two lines." Invert
sugar syrup is never defined, and that it counts as sugar is assumed. To close: a definition in a
few words.

**H18** [A-C03-5] `definition.text`. "... only the manufacturer's licence number must appear
(regulation 5(7)(b))." FSSAI licences are never introduced. To close: say what the licence is and
who issues it.

**H19** [A-C03-6] `must_know[3].point`. "A compound ingredient under 5 per cent of the food need not
list its own ingredients, apart from additives." "Compound ingredient" is undefined and the rule
has no regulation number, in the original too. To close: define it and cite the sub-regulation.

**H20** [A-C03-7] `definition.text` against `simplified_explanation`. Definition: "descending order
... by weight or volume". Plain terms: "in order of weight when the food was made, heaviest
first". For a liquid, "heaviest first" may be wrong. To close: plain terms says "by weight, or by
volume for liquids".

**H21** [A-C03-8] Exercise 1. "Which ingredient hides more than one chain behind a single name, and
which rule lets it?" The only class titles given are Sugar and Milk solids; whether "Spices and
condiments" is an allowed class title is never stated. To close: name the class title that covers
spices, with its regulation.

## C04

**H22** [A-C04-1, serious] Figure 1 caption. "Grouped bars for ten stages. Gram: farmer 53, then 2,
2, 1, 2, 1, 1, 1, 2 and retailer 6." Eight stages are unnamed, so Ex 1 ("Name the hands ... in
order"; "The rows are the same stages as for gram and tur") cannot be done; P6 and P10 cite "the
RBI table" the reader has only seen as numbers. The restored plain-terms list (market-yard fee,
commission, lorry, mill, packet, wholesaler, shopkeeper) is seven items, not ten. To close: name
all ten stages from RBI WP 07/2024 in the caption or a table.

**H23** [A-C04-2, serious] `must_know[0].point`. "In the RBI's tomato chain, traders' mark-up was 21.3
per cent and their margin 5.3 per cent." No base (breaks the section's own rule) and no cost
breakdown; cannot be reconciled with the 66.5 per cent after the farm gate. P12 cannot be finished
with numbers. To close: give the base and the paper's cost components between 21.3 and 5.3.

**H24** [A-C04-3] Practice 6. "Say which of the two the table prints." The figure prints rupees; the
base of the table's percentages is never stated (inferable only from P10, which comes later). To
close: state the base the RBI table uses.

**H25** [A-C04-4] Figure 2 against practice 9. "milk 70" against 35/49 = 71.4 per cent. Same paper,
cooperative and month is not said. To close: say what the 70 is, or reconcile.

**H26** [A-C04-5] Figure 2 caption. "Foods that spoil sit near a third; foods that keep sit near
two-thirds or more." "Spoil" is undefined, and milk (70) and eggs (75.2) sit on the "keep" side.
The restored "The RBI papers tie the low farmer's share of vegetables to perishability." sources the
vegetable half only. To close: define the grouping, or narrow the caption to vegetables.

**H27** [A-C04-6] `definition.text`. "what is left after those costs is the actor's margin." Never
worked with numbers. To close: one worked split of a mark-up into costs and margin.

**H28** [A-C04-7] Figure 1 caption and practice 5. "Indore and Latur to Delhi"; "tur sold at the
mandi for Rs 72". Which pulse comes from which origin is not stated, and that the mandi price is
the farm-gate price (fees not deducted) must be assumed. To close: state both.

**H29** [A-C04-9] Practice 8. "Give the farmer's share at the low end and at the high end of both
ranges." Pairing is ambiguous (14/30 and 16/35, or all four). To close: reword the problem.

**H30** [A-C04-10] Figure 1 caption. "ten stages" in the pulse chain against C01's "eight stages".
The same word means a food-system stage and a hand in a price chain. To close: call the price-chain
units something else, or say how they sit in C01's stages.

**H31** [A-C04-11] Figure 2 caption and `must_know[4].point`. "four RBI working papers of 2024";
"The RBI's poultry-meat figure of 56 per cent". Only WP 07/2024 (and C02's WP 08/2024) are
identified; the poultry figure is in no figure or table. To close: list all four papers by number.

## C05

**H32** [A-C05-4] `simplified_explanation`. No actor is named for food safety (the restored trader's
grade covers quality). Ex 1 asks for one per element. To close: name the regulator (FSSAI, from
C03) as the actor for safety.

**H33** [A-C05-5] `definition.text`. "The food environment is the part of the food system where a
person meets it." Not mapped onto C01's eight stages. To close: say which stages it spans.

**H34** [A-C05-7] `definition.text`. The state is a decider, but the only state instruments taught
are market fees, MSP and label rules. Taxes are never mentioned, so a price instrument such as a
tax on sugar-sweetened drinks cannot be placed (cold read Part 2). To close: name tax as a state
instrument on affordability, here or in C10.

## C06

**H35** [A-C06-2] Figure 1 caption. "Net production plus net imports, minus the rise in stocks".
"Net production" appears only in the figure and exercises; the Definition gives it only as a
formula. To close: name "net production" (gross production less seed, feed and wastage).

**H36** [A-C06-3] `definition.text`. "Its self-sufficiency ratio (SSR) is production divided by the
same total". Gross or net production? Figure 2's 111.1 uses gross (303,628/273,276). To close:
say "gross production".

**H37** [A-C06-5, serious] Exercise 1 and `must_know[5].point`. Wheat: 97,177 − 4,682 + 10,645 =
103,140 against 103,142 printed. "If a row does not close, say so and do not build a trend on it"
gives no rounding tolerance. To close: give a tolerance, or say the 2 is rounding in the source.

**H38** [A-C06-6] Figure 2 caption against practice 8. Edible oil self-sufficiency "43.75 (PIB ...)"
against "the release's own figures of 56.25 and 43.74". To close: print one figure, as the source
gives it.

**H39** [A-C06-7] `must_know[3].point`. "India imported 56.25 per cent of its edible oil supply".
Here "supply" is production plus imports, not the Definition's supply; why the FAO ratios ignore
stocks is not said. To close: say "of production plus imports" and one line on stocks in the
ratios.

**H40** [A-C06-8] Practice 9. "per capita domestic consumption of edible oils". Whether this PIB
figure is availability or survey intake is not said, after the section insists they differ. To
close: state what the PIB figure measures.

**H41** [A-C06-9] Practice 14. "Using Table 1.19, decide what to compute". The 2021-22 row and the
foodgrain stock changes are not shown, so the stock part of the rise can be estimated only for
wheat. To close: give the 2021-22 row and stock change.

**H42** [A-C06-10] Figure 2 caption. "(PIB, exports left out)". Zero, or unknown and ignored? P8's
answer depends on it. To close: say which.
