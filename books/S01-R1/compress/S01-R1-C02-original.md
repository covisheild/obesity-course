# S01-R1-C02 · How much energy a kilogram of body fat holds

**Definition.** A kilojoule, from `B0-R0-C12`, is a thousand joules; kilo means 10^3. The prefix this record
adds is mega, meaning 10^6, a million. A megajoule is a thousand kilojoules, and the figures
in this record run to tens of megajoules for each kilogram of tissue, which is why megajoules
is the unit used from here on.

Pure fat's own energy content is well established. The Atwater general factor for fat, from
`B0-R0-C32`, is 9.0 kilocalories, or 37 kilojoules, for each gram: 9,000 kilocalories, or 37
megajoules, for each kilogram. Hall (2008) gives an independent figure for the same
quantity, the metabolizable energy density of body fat, at 39.5 megajoules for each kilogram.
The two are the same order, both close to 9 kilocalories a gram, and neither is in dispute.

Adipose tissue is not pure fat, `S01-R1-C01` already established. So a kilogram of adipose
tissue holds less energy than a kilogram of pure fat, by however much of that kilogram is not
triglyceride. How much less depends on the tissue's lipid fraction, the proportion of its
mass that is fat, multiplied by fat's own energy per gram.

Here is where this record has to be exact about what its one held source does and does not
give. Hall (2008) states that the classic weight-loss rule "can be traced back to a
calculation that assumes exclusive loss of adipose tissue consisting of 87% fat." That 87% is
the rule's own assumption, not a measurement Hall reports of any adipose tissue. The same
paper goes on to warn that the change in body fat is "not equivalent to the loss of adipose
tissue, which includes a variable contribution of fluid and protein in addition to
triglyceride" — variable, not fixed at 87% or any other number. No source this subject holds
gives an independently measured lipid fraction for adipose tissue.

Run the rule's own assumption through the arithmetic anyway, once, to see where its number
comes from: lipid fraction times energy per gram.

```working
    0.87 times 37 = 32.19
```

32.19 megajoules for each kilogram of the rule's assumed adipose tissue, matching Hall's own
statement of the same rule as "equivalently 32.2 MJ per kg." In kilocalories a kilogram that
is about 7,700, the same figure `S01-R1-C07` reaches from the pound side of the rule. The two
routes agree because they are the same one assumption, carried through two different pieces
of arithmetic — not two independent confirmations of it.

Lean tissue's own energy density is far lower than fat's. Hall (2008) gives 17.6 and 19.7
megajoules a kilogram for glycogen and protein separately, and a combined figure, once the
water that moves with them is counted, of 7.6 megajoules for each kilogram of lean mass
change. That number is named here only; what it is built from is rung 2's work.

**In plain terms.** Ask a simple question: how many kilocalories does a kilogram of body fat hold? There are two
different honest answers, and mixing them up is the whole trap.

The first answer is about pure fat, the triglyceride itself. That number is solid. It is about
9 kilocalories a gram, which is 9,000 a kilogram, or in the unit this record is built on, about
37 to 39.5 megajoules a kilogram. Two sources agree on it from two different directions, and
neither is arguing.

The second answer is about adipose tissue, the actual stuff that is gained or lost. It is not
pure fat — `S01-R1-C01` already told you that. So its energy per kilogram has to be lower. By
how much depends on what fraction of it is fat, and here the honesty runs out: the only figure
for that fraction in this subject's held sources is 87%, and it is not a measurement. It is the
number a much older rule assumed, and the paper that reports it goes out of its way to say the
real figure is variable, not fixed.

Do the sum anyway, because it shows you where the famous 32.2-megajoules-a-kilogram, or roughly
7,700-kilocalories-a-kilogram, figure comes from. Take the fraction, 0.87, and multiply by fat's
own energy per gram.

```working
    the assumed energy per gram of adipose tissue = the assumed lipid fraction, times fat's
    energy per gram
```

That is arithmetic on an assumption. It is not a second, independent measurement, even though
two different routes to it — this one, and the pound conversion `S01-R1-C07` uses — land on the
same number. They agree because they are the same assumption, not because two people measured
the same thing twice.

One more figure, named and set aside. Lean tissue holds far less energy for each kilogram than
fat does — a small fraction of fat's own figure, once its glycogen, protein and the water that
travels with them are counted. What that number is built from is not this record's job.

**Illustration.** Start with the unit. `B0-R0-C12` gave you the kilojoule: kilo means 10^3, a thousand. Open
BIPM's own table of SI prefixes, "The International System of Units (SI): Prefixes", at
https://www.bipm.org/en/measurement-units/si-prefixes, and search the table for mega.

> mega | M | 106

Read the exponent as ten to the sixth, a million — the source's own extraction note says the
superscript formatting is lost in the fetch. A megajoule is a million joules, a thousand
kilojoules.

Now the two solid figures for pure fat, from two directions.

Open FAO Food and Nutrition Paper 77, chapter 3, at https://www.fao.org/4/y5022e/y5022e04.htm,
and search for the word Atwater.

> The energy values are 17 kJ/g (4.0 kcal/g) for protein, 37 kJ/g (9.0 kcal/g) for fat and
> 17 kJ/g (4.0 kcal/g) for carbohydrates.

Fat: 37 kilojoules a gram. Scale that to a kilogram.

```working
    37 times 1000 = 37000
    37000 divided by 1000 = 37
```

37 megajoules a kilogram (the two divisions and multiplications cancel; a kilojoule-per-gram
figure is already a megajoule-per-kilogram figure, because both the numerator and the
denominator scale by a thousand together).

Open Hall, "What is the required energy deficit per unit weight loss?", *International
Journal of Obesity* 2008, at https://pmc.ncbi.nlm.nih.gov/articles/PMC2376744/, and search for
the word respectively.

> the metabolizable energy densities of body glycogen, protein and fat are 17.6, 19.7, and
> 39.5 MJ/kg, respectively

39.5 megajoules a kilogram for fat, against FAO's 37. Close, not identical — the two sources
are measuring slightly different things (a general dietary factor against a physiological
energy density), and this record does not need them to match exactly to trust either one for
what it says: pure fat is worth roughly 9 kilocalories, or somewhere from 37 to 39.5
megajoules, for a kilogram.

Now search the same paper for 87%.

> The origin of this rule can be traced back to a calculation that assumes exclusive loss of
> adipose tissue consisting of 87% fat

Read the sentence again and notice what it does not say. It says a calculation assumes 87%.
It does not say a measurement found 87%. Search on for the word variable.

> the change of body fat,ΔF, is not equivalent to the loss adipose tissue, which includes a
> variable contribution of fluid and protein in addition to triglyceride

Variable. Not 87%, not any other fixed number. That is everything this held source gives you
about adipose tissue's own composition.

Run the assumed fraction through the arithmetic once, to see the classic rule's number
appear.

```working
    0.87 times 37 = 32.19
```

Search the same paper, near the start, for MJ per kg.

> a cumulative energy deficit of 3500 kcal is required to lose 1 pound of body weight, or
> equivalently 32.2 MJ per kg

32.19 against 32.2. The small gap is rounding; the arithmetic reproduces the paper's own
statement of the rule. In kilocalories a kilogram that is about 7,700 — the same figure
`S01-R1-C07` reaches by converting 3,500 kcal a pound directly. Two routes, one assumption:
the fraction 0.87 is what both calculations are built on, and neither route checks it against
a measurement.

```table
quantity                              value                 source
pure fat, FAO Atwater factor          9.0 kcal/g, 37 MJ/kg  fao_food_energy_2003
pure fat, Hall's physiological figure 39.5 MJ/kg            hall_2008_ijo
adipose tissue, the rule's assumption 32.2 MJ/kg (≈7,700 kcal/kg)  hall_2008_ijo (rule, not a measurement)
lean mass change                      7.6 MJ/kg             hall_2008_ijo
```

Read the third row with the parenthetical attached every time you use it. Drop the
parenthetical and the row reads like a measured property of a tissue; it is not one.

**Where this picture breaks.** The first two rows of the table are not in dispute in this subject's held sources: pure fat's
own energy content is well established from two independent directions. The third row is
different in kind, not just in size. It is one assumption, 87% fat, carried through one piece
of arithmetic; the paper that reports the assumption also says the true figure is variable.
Nothing here gives a range for that variation, a method for measuring it in a person, or a
reason to expect 87% over some other number for any particular patient's adipose tissue.

The near-exact match between 32.19 and Hall's own 32.2 MJ/kg, and between this record's route
and `S01-R1-C07`'s pound-conversion route, is not two confirmations. It is the same 87%
reappearing wherever the same rule is computed. Treat one appearance of it as evidence and the
second stops being independent evidence.

The fourth row is named, not explained. It says lean tissue holds far less energy for each
kilogram than fat does, and nothing here says how the 7.6 splits between glycogen, protein and
water, or how it was measured.

**Must know points for you.**

- Pure fat holds about 9 kilocalories, or 37 to 39.5 megajoules, for each kilogram. This figure is well established from two independent sources and is safe to quote on its own, without the caution the next point requires.
- A kilogram of body fat lost or gained is not a kilogram of pure fat; it is adipose tissue, a mixture, and holds less energy per kilogram than pure fat does. Never quote 9 kilocalories or 37-39.5 megajoules a kilogram for a kilogram of weight a patient has lost or gained.
- The figure of about 32 megajoules, or 7,700 kilocalories, for a kilogram of adipose tissue is the classic rule's own assumed number, built from an assumed 87% lipid fraction that no held source measures. It is not an established property of adipose tissue. Say "the rule assumes" when you use it, never "adipose tissue is".
- Reaching the same ~7,700 or ~32.2 figure by two different pieces of arithmetic, as this record and `S01-R1-C07` both do, is not two independent confirmations of it. Both routes carry the same 87% assumption through different unit conversions. Check what a figure is built on before counting a second appearance of it as new evidence.
- Lean tissue's energy density, about 7.6 megajoules for a kilogram of lean mass change, is far lower than fat's. This record names the number and does not build it; ask what it is made of before using it for anything beyond "much lower than fat".
- Because fat and lean tissue differ this much, and `S01-R1-C01` already showed a scale cannot tell you which compartment moved, no single kilocalories-per-kilogram figure is safe to apply to a patient's weight change without separately knowing, or reasonably assuming, what that change was made of.

**1.** A tissue's energy per gram is found by multiplying its lipid fraction by 9.0. Work out the
result for a lipid fraction of 0.80, and separately for a lipid fraction of 0.60.

**2.** Convert 34,000 kilojoules into megajoules. Then convert 2.5 megajoules into kilojoules.

**3.** Two energy densities are quoted for two different tissues: 39.5 and 7.6, in the same units.
Work out how many times larger the first is than the second.

**4.** FAO Food and Nutrition Paper 77 gives the Atwater general factor for fat as 9.0 kilocalories
a gram. Work out how many kilocalories that is for one kilogram of pure fat, then convert to
megajoules using 1 kilocalorie = 0.004184 megajoules.

**5.** Hall (2008) gives the metabolizable energy density of body fat as 39.5 megajoules a kilogram.
Convert this to kilocalories a kilogram, using 1 kilocalorie = 4.184 kilojoules.

**6.** Hall (2008) traces the classic weight-loss rule to a calculation assuming adipose tissue is
87% fat, using an energy-per-gram figure for fat of 37 kilojoules a gram (FAO's Atwater
factor). Work out the adipose-tissue energy density in kilojoules a gram this assumption
produces, and say how it compares with Hall's own statement of the rule as "32.2 MJ per kg".

**7.** Here is a worked answer. Find the step that broke.

```working
    pure fat holds 39.5 MJ/kg, Hall (2008)
    a patient's weight falls by 4 kg over a diet
    4 times 39.5 = 158
    so the deficit responsible for the loss was 158 MJ
```

**8.** Here is a worked answer. Find the step that broke.

```working
    the classic rule's adipose figure is about 7,700 kcal/kg
    FAO's Atwater factor for fat is 9.0 kcal/g, or 9,000 kcal/kg
    7,700 is close to 9,000
    so the two figures confirm each other, and adipose tissue is essentially pure fat
```

**9.** A colleague says: "A kilogram of fat is worth about 9,000 kilocalories, so losing 5 kilograms
needs a 45,000-kilocalorie deficit." Decide what to compute, compute it, and say what your
answer does not establish.

**10.** A slimming clinic's brochure says: "Body fat holds 7,700 kilocalories per kilogram, a figure
confirmed by peer-reviewed research (Hall, 2008)." Decide what to compute, compute it, and
say what your answer does not establish.

