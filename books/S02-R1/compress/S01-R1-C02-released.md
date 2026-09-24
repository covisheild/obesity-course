# S01-R1-C02 · How much energy a kilogram of body fat holds

**Definition.** A kilojoule (kJ), from `B0-R0-C12`, is a thousand joules; kilo means 10^3. The prefix this
section adds is mega, meaning 10^6, a million. A megajoule (MJ) is a million joules.

The Atwater general factor for fat, from `B0-R0-C32`, is 9.0 kilocalories (kcal) a gram. The
Food and Agriculture Organization (FAO) prints 37 kilojoules beside it. That is a rounded
value, and the two do not convert exactly. For a kilogram: 9,000 kilocalories, or 37
megajoules.

FAO's factors are corrected for what is lost in digestion, absorption and urine. They describe
fat eaten. Fat already stored in the body is not digested again. Hall (2008) gives fat in the
body 39.5 megajoules a kilogram. For body fat, use 39.5.

Adipose tissue is not pure fat, `S01-R1-C01` already established. Counting only its fat, its
energy per gram is its lipid fraction, the proportion of its mass that is fat, times fat's own
energy per gram.

A deficit is expenditure larger than intake; a surplus is the reverse. The static rule,
defined in `S01-R1-C07`, says a deficit of 3,500 kilocalories removes a pound of weight.
A pound is exactly 0.453 592 37 kilogram. Hall (2008) states that the rule "can be traced
back to a calculation that assumes exclusive loss of adipose tissue consisting of 87% fat."
That 87% is the rule's own assumption, not a measurement Hall reports.

A kilogram of lean mass lost or gained carries far less energy than a kilogram of fat.

**In plain terms.** Ask a simple question: how much energy does a kilogram of "fat" gained or lost hold? There are
two different honest answers, and mixing them up is the whole trap.

The first answer is about pure fat, the triglyceride itself. Fat in food carries about 9
kilocalories a gram, which is 9,000 a kilogram, or about 37 megajoules. Fat stored in the body
carries 39.5 megajoules a kilogram.

The second answer is about adipose tissue, the actual stuff that is gained or lost. It is not
pure fat — `S01-R1-C01` already told you that. By how much depends on what fraction of it is
fat, and here the honesty runs out: the only figure for that fraction in the sources this book
cites is 87%, and it is not a measurement.

Do the sum anyway, to see the size of the effect. Multiply 0.87 by fat's 37 kilojoules a gram.
You get 32.19 megajoules a kilogram, close to the famous rule's 32.2, but partly by luck.
Start from 9,000 kilocalories instead and the same sum gives 7,830, not the rule's 7,700.

That is arithmetic on an assumption.

**Illustration.** Open the table of prefixes kept by the International Bureau of Weights and Measures (BIPM),
"The International System of Units (SI): Prefixes", at
https://www.bipm.org/en/measurement-units/si-prefixes, and search the table for mega.

> mega | M | 106

The page prints 10 with a small raised 6. Copied as plain text it can come out as 106. Read
it as ten to the sixth, a million. A megajoule is a million joules, a thousand kilojoules.

Open FAO Food and Nutrition Paper 77, chapter 3, at https://www.fao.org/4/y5022e/y5022e04.htm,
and search for the word Atwater.

> The energy values are 17 kJ/g (4.0 kcal/g) for protein, 37 kJ/g (9.0 kcal/g) for fat and
> 17 kJ/g (4.0 kcal/g) for carbohydrates.

Fat: 37 kilojoules a gram. Scale that to a kilogram.

```working
    37 kJ/g times 1000 g/kg = 37000 kJ/kg
    37000 kJ/kg divided by 1000 kJ/MJ = 37 MJ/kg
```

37 megajoules a kilogram. The multiplication and the division cancel: a kilojoule-per-gram
figure is already a megajoule-per-kilogram figure.

Open Hall, "What is the required energy deficit per unit weight loss?", *International
Journal of Obesity* 2008, at https://pmc.ncbi.nlm.nih.gov/articles/PMC2376744/, and search for
the word respectively.

> the metabolizable energy densities of body glycogen, protein and fat are 17.6, 19.7, and
> 39.5 MJ/kg, respectively

39.5 megajoules a kilogram for fat in the body, against FAO's 37 for fat in food.

Now search the same paper for 87%.

> The origin of this rule can be traced back to a calculation that assumes exclusive loss of
> adipose tissue consisting of 87% fat

It says a calculation assumes 87%. It does not say a measurement found 87%. Search on for the word
variable.

> the change of body fat,ΔF, is not equivalent to the loss adipose tissue, which includes a
> variable contribution of fluid and protein in addition to triglyceride

Run the assumed fraction through the arithmetic once.

```working
    0.87 times 37 = 32.19
```

Search the same paper, near the start, for MJ per kg.

> a cumulative energy deficit of 3500 kcal is required to lose 1 pound of body weight, or
> equivalently 32.2 MJ per kg

32.19 lands close to 32.2. That is partly luck. FAO's footnote gives fat's precise value as
37.4 kilojoules a gram; 37 is its rounding. Try 37.4, Hall's 39.5, and 9,000 kilocalories.

```working
    0.87 times 37.4 = 32.538
    0.87 times 39.5 = 34.365
    0.87 times 9000 = 7830
```

32.5, 34.4, and 7,830 kilocalories. The rule is 3,500 kilocalories a pound, about 7,700 a
kilogram (`S01-R1-C07` works that out). Hall does not say which figure for fat the original
calculation used. What the sum shows is the size of the effect an 87% assumption has, not how
the rule was built.

Search the same paper for 7.6.

> This results in a calculated energy density for lean body mass changes of ρL = 7.6 MJ/kg.

ρL is the paper's symbol for it: the energy in a kilogram of lean mass lost or gained.

```table
| quantity | value | source |
| fat in food, FAO Atwater factor | 9.0 kcal/g; 37 MJ/kg | FAO 2003 |
| fat in the body | 39.5 MJ/kg | Hall 2008 |
| adipose tissue, the rule's assumption | 32.2 MJ/kg (about 7,700 kcal/kg) | Hall 2008 (the rule, not a measurement) |
| lean mass change | 7.6 MJ/kg | Hall 2008 |
```

**Where this picture breaks.** The third row is different in kind, not just in size. It is one assumption, 87% fat, carried
through one piece of arithmetic; the paper that reports the assumption also says the true
figure is variable.

The closeness of 32.19 to Hall's 32.2 MJ/kg is not a confirmation. With 37.4 or 39.5 for fat,
the same 87% lands elsewhere. And `S01-R1-C07`'s pound conversion restates the rule; it does
not check the 87%.

The fourth row is named, not explained.

**Figure.** Energy in a kilogram, in megajoules: fat in food 37 (FAO); fat in the body 39.5 (Hall 2008); adipose tissue 32.2 only under the static rule's assumed 87% fat; a lean-mass change 7.6. Hall's body-fat figure is about 5.2 times the lean figure.

*What the figure shows:* Four bars in megajoules a kilogram: 37 for fat in food, 39.5 for fat in the body, 32.2 for adipose tissue under the rule's assumption, and a much shorter 7.6 for lean mass change.

**Figure.** Counting only the fat in adipose tissue, its energy per kilogram is the lipid fraction times the 39.5 megajoules a kilogram of fat in the body. At the rule's assumed 0.87 that gives 34.4, above the rule's own 32.2. The points at 0.60 and 0.80 are arbitrary, drawn to show the line, not a measured range. Hall (2008) calls the real composition variable.

*What the figure shows:* A straight line rising from 23.7 megajoules a kilogram at a lipid fraction of 0.60 to 39.5 at a fraction of 1, with the rule's assumed fraction marked at 0.87 and 34.4.

**Must know points for you.**

- Pure fat holds about 9 kilocalories a gram (9,000 a kilogram), or 37 to 39.5 megajoules a kilogram: 37 for fat in food (FAO), 39.5 for fat stored in the body (Hall 2008).
- A kilogram of adipose tissue lost or gained is not a kilogram of pure fat. It is a mixture, and it holds less energy per kilogram than pure fat does. Never quote 9,000 kilocalories or 37-39.5 megajoules a kilogram for a kilogram of weight a patient has lost or gained.
- The figure of about 32 megajoules, or 7,700 kilocalories, for a kilogram of adipose tissue is the static rule's own number, which Hall (2008) traces to an assumed 87% lipid fraction that no source this book cites measures. Say "the rule assumes" when you use it, never "adipose tissue is".
- A sum that lands near the rule's 32.2, like 0.87 times 37, does not confirm the rule. Use 37.4 or 39.5 for fat and the same 87% lands elsewhere.
- A kilogram of lean mass lost or gained carries about 7.6 megajoules (Hall 2008), about a fifth of fat's figure. That is the energy of the change, not of lean tissue as a whole; Hall warns the two "are not equivalent".
- Because fat and lean tissue differ this much, and `S01-R1-C01` already showed a scale cannot tell you which compartment moved, no single kilocalories-per-kilogram figure is safe to apply to a patient's weight change without separately knowing, or reasonably assuming, what that change was made of.

**1.** A tissue's energy per gram (counting only the fat) is found by multiplying its lipid fraction
by 9.0. Work out the result for a lipid fraction of 0.80, and separately for a lipid fraction of 0.60.

**2.** Convert 34,000 kilojoules into megajoules. Then convert 2.5 megajoules into kilojoules.

**3.** Two energy densities are quoted for two different tissues: 39.5 and 7.6, in the same units.
Work out how many times larger the first is than the second.

**4.** FAO Food and Nutrition Paper 77 gives the Atwater general factor for fat as 9.0 kilocalories
a gram. Work out how many kilocalories that is for one kilogram of pure fat, then convert to
megajoules using 1 kilocalorie = 0.004184 megajoules.

**5.** Hall (2008) gives the metabolizable energy density of body fat as 39.5 megajoules a kilogram.
Convert this to kilocalories a kilogram, using 1 kilocalorie = 4.184 kilojoules.

**6.** Hall (2008) traces the static rule to a calculation assuming adipose tissue is
87% fat. Take FAO's 37 kilojoules a gram for fat and work out the adipose-tissue energy
density in kilojoules a gram this assumption produces, and say how it compares with Hall's own statement of the rule as "32.2 MJ per kg".

**7.** Here is a worked answer. Find the step that broke.

```working
    pure fat holds 39.5 MJ/kg, Hall (2008)
    a patient's weight falls by 4 kg over a diet
    4 times 39.5 = 158
    so the deficit responsible for the loss was 158 MJ
```

**8.** Here is a worked answer. Find the step that broke.

```working
    the static rule's adipose figure is about 7,700 kcal/kg
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

