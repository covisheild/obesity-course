# Cold-read report — /tmp/coldread/

Read in filename order: B1, B2, B3, B4, B5, B6. Nothing read before them. Arithmetic done on a
calculator. Where I say "I had to supply this", I mean the page did not contain it.

Three-way key used throughout:

- **[OUTRIGHT]** — done using only what these files gave me.
- **[SUPPLIED]** — I produced an answer, but only by reaching for something the text never gave.
  This is the category that matters; a fluent read hides it.
- **[BLOCKED]** — could not attempt.

---

## B1 · What a unit is, and the SI base and derived units

### Exercises

**Exercise 1 (retrieval).** [OUTRIGHT]
Seven base units: second, metre, kilogram, ampere, kelvin, mole, candela.
A derived unit is one built as a product of powers of base units, by multiplying and dividing
them. Two built by me: speed = length ÷ time = **m/s**; area = length × length = **m²**.

**Exercise 2 (critique).** [SUPPLIED — and the text contradicts itself here]
What I would ask for: the unit on the column header. "Rice: 250, 180, 4.2, 300" is four bare
numbers, so by the section's own definition it is not four measurements and I would send the
register back before using any of it.

What the 4.2 tells me: I wrote "it tells you the column is not all in one unit — 4.2 is
probably a sack in kilograms while the others are packets in grams." Then I noticed that this
is exactly the move the section forbids in its own must-know list: *"Never work out which unit
was meant from how big the number looks."* Following that instruction literally, the honest
answer is that **4.2 tells me nothing at all** — and then the exercise has no content.
I could not tell which of those two answers was wanted. The section never discusses what a
spread of magnitudes inside one column signifies, so I had to invent a rule for it.

**Exercise 3 (teaching).** [SUPPLIED — this one I substantially could not do from the page]
The resident's problem is remembering whether the joule is kg m² s⁻² or kg m s⁻². The exercise
asks me to teach them "so that the question stops arising" — i.e. so they can reconstruct it,
not recite it. The only tools B1 gives me are: (a) look it up on the BIPM page, and (b) say it
out loud as a sentence. Neither stops the question arising; both are rote.

To actually make it reconstructible I wrote: energy is a force acting over a distance; a force
is a mass times an acceleration; acceleration is m/s²; so kg·(m/s²)·m = kg m² s⁻². **Every
term in that chain — force, acceleration, work, the newton — is absent from B1.** A reader with
no prior background has no route to it and can only tell the resident to look it up, which is
the answer the exercise is written to exclude.

### What B1 changed about what I would do

- I would refuse to act on a bare number. A strip labelled "500" is not a dose; I send it back.
- I would read the unit before the number, on a label or a report, rather than after.
- I would stop reading `m` as one thing: standing alone it is the metre, in front of another
  unit it is milli.
- I would treat an unfamiliar quantity in a paper by reading its unit first, as a recipe telling
  me what kind of thing it is.
- I would **not** accept "the units are right" as evidence that a machine or a report is
  accurate.

### Gaps

1. **"Seven base units keep their role inside that system."** (Definition, para 2.)
   *That system* has no antecedent. The Definition's first paragraph is about measurements
   having units; no system has been named. A reader without prior background does not know what
   "that system" refers to until the plain-terms section, two blocks later, mentions the SI.
   **Needed:** the sentence that introduced the SI, which has evidently been cut from the
   Definition.

2. **"SI" is never expanded and never defined.** It is used as a proper noun throughout six
   files. I never learned what the letters stand for or what kind of body the SI is (a standard?
   a treaty? an organisation?). The BIPM is named only as a publisher of a web page.

3. **"The SI fixes every unit through seven constants with exact values. One of them is the
   speed of light in vacuum..."** (Must-know.)
   This is the only mention of the seven constants in the whole set of files. Six of them are
   never named, and the mechanism — how fixing a constant fixes a unit — is asserted and never
   demonstrated. I cannot do anything with this bullet. It reads as the residue of a paragraph
   that was removed.

4. **"Now go and read the SI's own words... Open it and search inside the page for 'J ='."**
   The section hands the reader a task that requires internet access. It then prints the answer
   anyway, so the exercise is decorative. A reader offline is told to do something they cannot
   do, with no statement of what they would find.

5. **`J = kg m2 s-2`** in the working block is written without carets, while the Definition and
   the must-know bullets write `kg m^2 s^-2`. Two notations for one thing, unremarked. I read
   this twice to confirm they were the same expression.

6. **"One minute is 60 seconds. One hour is 3,600 seconds."**
   Dropped in with no connective, no relation to anything around it, and no statement that there
   are 60 minutes in an hour. B2 problem 3 then requires exactly that missing figure (below).

7. **Must-know bullet 1: "It is not a measurement at all. Send it back for the unit."**
   *It* has no antecedent. The bullet begins with a pronoun answering a question that is not on
   the page. (Same structural fault in B2 bullet 1 — see below.) These bullets look like the
   answer halves of a Q&A whose questions were deleted.

8. **The prefix table gives only kilo, centi, milli, micro.** `deci` is never listed — and B5
   is built entirely on the decilitre. `mega`, `nano` etc. are absent too, but deci is the one
   that is load-bearing later.

9. **The litre is never introduced anywhere in B1–B6.** B1 says volume is m³. B2 uses
   millilitres. B5 uses litres and decilitres as its whole subject. No file ever says what a
   litre is, whether it is SI, or how it relates to m³. I had to supply that a millilitre is a
   thousandth of a litre by analogy with milligram, which the text never licenses.

10. **"mole" appears in the base-unit list with no statement of what it measures.** Five files
    later B5 says "a mole is a fixed count of things". In B1 it is a word with no content.

11. **"And all of this is decided, not discovered."** No antecedent for *all of this* — the
    units? the seven constants? the derived-unit recipes? I read the paragraph twice and still
    picked by guess.

---

## B2 · Converting units as multiplication by one

### Exercises

**Exercise 1 (calculation).** [OUTRIGHT]
Height: 96 cm × (1 m / 100 cm) = **0.96 m**. The cm cancelled. (I got 100 cm = 1 m from B1's
prefix table: centi = 10⁻², one centimetre is 0.01 metres.)
Sack: 0.4 kg/packet × 25 packets = 10 kg; 10 kg × (1,000 g / 1 kg) = **10,000 g**. The kg
cancelled. (The packets cancelled too, which the question did not ask about.)

**Exercise 2 (critique).** [OUTRIGHT, with one borrowed assumption]
40 packets × 250 mL/packet = **10,000 mL**, i.e. 10 litres — not 10 millilitres. The size check
fails immediately: 40 packets must hold more than one packet, not a twenty-fifth of one. They
appear to have divided by 1,000 and then kept the small unit as well, so they went wrong twice
in the same direction.
What I would change in how they work, not in the line: write the unit beside every line while
working, and run the size check (bigger unit → smaller number) before the answer leaves the
desk. Both are the section's own prescriptions.
*Borrowed:* that 1,000 mL = 1 L, which the text never states.

### Numbered problems

**1.** [OUTRIGHT] 3 km = **3,000 m**; 4,500 g = **4.5 kg**; 2.5 m = **250 cm**.

**2.** [OUTRIGHT] The two orientations: 1,000 g / 1 kg, and 1 kg / 1,000 g.
**1 kg / 1,000 g** turns grams into kilograms, because it puts g on the bottom where it cancels
the g you are holding. The other one does not: it leaves kg² / g, which is not a mass.

**3.** [SUPPLIED — one factor is missing from the text]
2 hours → seconds, *in two factors*: 2 h × (60 min / 1 h) × (60 s / 1 min) = **7,200 s**.
The problem explicitly demands two factors. B1 gives me "one minute is 60 seconds" and "one
hour is 3,600 seconds". **It never gives 60 minutes = 1 hour.** With only what is on the page I
can do this in *one* factor (2 × 3,600) but not in the two the problem asks for. I recovered
60 min/h by dividing 3,600 by 60 — an inference the text never models.
0.75 kg → mg: 0.75 kg × (1,000 g / 1 kg) × (1,000 mg / 1 g) = **750,000 mg**. [OUTRIGHT]

**4.** [SUPPLIED — months per year is never stated]
35 kg/household/month = **35,000 g per household per month**.
Per year: 35 kg/hh/month × 12 months/year = **420 kg per household per year**.
**Nowhere in B1 or B2 does the text say a year has 12 months.** I supplied it. This is
conspicuous because the section makes a point, twice, that the 30-day month is a choice the
reader must make and declare — so the text is alert to calendar assumptions and then silently
relies on an undeclared one. (B3's illustration does use "times 12", but B3 comes after B2.)
The two limits: the entitlement runs only to the extent the Central Government specifies for
each State, and the grain comes at Schedule I prices. So the 35 kg figure **does not let me say
what any one household actually receives**, and does not let me say the grain is free.

**5.** [SUPPLIED — prefix-to-prefix conversion is never demonstrated]
0.25 mg × (1,000 µg / 1 mg) = **250 µg**; mg on the bottom, cancelling.
4,000 µg × (1 mg / 1,000 µg) = **4 mg**; µg on the bottom, cancelling.
**Every worked conversion in B2 runs between a prefixed unit and its base unit** (km↔m, kg↔g,
month↔day). The milligram-to-microgram step is prefix-to-prefix and is never worked anywhere.
I got the 1,000 by subtracting exponents in B1's table (10⁻³ vs 10⁻⁶). The text never shows
that step and never says it is allowed.

**6.** [OUTRIGHT] The break is line 3: the factor is upside down. It should be
0.5 g × (1,000 mg / 1 g) = **500 mg**. Two tells: the unit falling out of their version is
g²/mg, not mg; and the size check fails, since a milligram is smaller than a gram so the number
must get bigger.

**7.** [SUPPLIED — the required technique is not in the text at this point]
12,000 m² → km². Correct answer **0.012 km²**, via (1 km / 1,000 m)² = 1 km² / 1,000,000 m².
The break is that they applied a *length* factor, once, to an *area*.
**Squaring a conversion factor is never taught in B1 or B2.** B1 introduces m² as a derived
unit and stops. B2's entire method — write the factor, cancel the unit — gives no account of
what happens when the unit carries a power. Working it their way with units attached gives
12,000 m² × (1 km / 1,000 m) = 12 m·km, which is not an area at all, so the *unit check* does
catch it — but the check is a B3 idea and B3 has not been read yet. I could say "wrong" from
B2; I could only say "0.012" by supplying the squaring rule myself. B6 eventually demonstrates
a squared conversion (100 × 100 = 10,000), four sections too late.

**8.** [OUTRIGHT] 0.5 mg × 1,000 = 500 µg. The two strengths are **the same amount**. The new
tablet is not a thousand times anything; the speaker converted in the wrong direction, or not
at all.
What this does not establish: nothing about whether the two tablets act the same in a person,
nothing about formulation, and nothing about whether either label is accurate. I have compared
two printed numbers, not two medicines.

### What B2 changed about what I would do

- Given a conversion, I would now write the factor as a fraction and choose the orientation by
  which unit needs to cancel, instead of deciding between multiply and divide by feel.
- I would run the size check on any converted dose or dispensed amount **before acting on it**:
  bigger unit, smaller number.
- I would refuse to produce a conversion between kilograms and litres, or grams and rupees —
  there is no factor between units of different kinds.
- I would not hand over a daily figure derived from a monthly entitlement without saying which
  number of days I chose, because no statute chooses it.

### Gaps

1. **Must-know bullet 1: "It is a fraction equal to one, and which way up you write it is
   settled by which unit you want to cancel."**
   *It* has no antecedent — the bullet never names the conversion factor. Same deleted-question
   structure as B1.

2. **"5 kg times 1 kg over 1,000 g = 0.005 kg squared per gram."**
   The result is stated; the cancellation that produces kg²/g is not shown. A reader who does
   not already handle units as algebra cannot see where the square came from. This is the one
   place in the section where the units are *not* written beside each line, which is the very
   discipline the section is prescribing.

3. **The millilitre is used in Exercise 2 and never introduced.** Neither the litre nor its
   relation to any other unit appears in B1 or B2.

4. **"There is no agreed number of days in a month, so you have to choose one and say so."**
   Good, and clearly deliberate. But the section then leaves 12 months = 1 year completely
   unmentioned while setting a problem that needs it (problem 4). The asymmetry is unexplained
   and I had to guess whether it too was a choice I should declare.

5. **No worked example converts a unit that carries a power**, yet problem 7 requires one.
   **Needed:** one demonstration of (factor)², or a sentence saying a squared unit takes a
   squared factor.

6. **"Section 3(1) of the National Food Security Act, 2013"** is quoted as a fact about the
   world with no statement of what the Act is, which country's it is, or whether the reader is
   expected to have it open. The files assume an Indian reader throughout without ever saying so.

---

## B3 · Dimensional analysis as an error check

### Exercises

**Exercise 1 (critique).** [OUTRIGHT]
"Units match, so the formula is correct" does not follow, because the check throws away the
numbers. Any dimensionless factor — ½, 2, π — changes the answer and changes no unit, so a
formula can pass and still be wrong by any multiple.
My example: area of a rectangle given as `area = 3 × length × width`. Units come out m², which
is correct; the areas come out three times too big.

**Exercise 2 (teaching).** [OUTRIGHT]
I would give them the four steps (strip the numbers, write every unit both sides, cancel top
against bottom, compare), work the 12 km ÷ 40 km/h example with them, then hand them a formula
they have never seen and have them reject it. Closing point: this tells you when to stop, not
what to write instead — and matching units are never a certificate.

### Numbered problems

**1.** [OUTRIGHT] m/s × s = **m**. m × m × m = **m³**. (kg/m³) × m³ = **kg**.

**2.** [OUTRIGHT]
3 m + 4 m — add as they stand, = 7 m.
3 m + 4 s — cannot be added at all; different dimensions.
3 kg + 4 g — after conversion; 3 kg = 3,000 g, so 3,004 g.
3 m² + 4 m — cannot be added at all; an area and a length are different dimensions even though
the letter is the same.

**3.** [OUTRIGHT] mass ÷ volume = **kg/m³**. length ÷ time = **m/s**. length ÷ time ÷ time =
**m/s²**. people ÷ area = **persons per m²** — and as the section itself notes, the person is
not an SI unit, so this one is not in base units at all.

**4.** [OUTRIGHT] kg m² s⁻² ÷ kg = **m² s⁻²**. kg m² s⁻² ÷ s = **kg m² s⁻³**. m² ÷ m = **m**.

**5.** [OUTRIGHT] J/kg = **m² s⁻²**. J·s²/m² = **kg**. J/s = **kg m² s⁻³**.

**6.** [OUTRIGHT] (mg/mL) × mL = **mg**. The millilitres cancel; the total amount is a mass.

**7.** [OUTRIGHT] 360 kg/household/year ÷ 6 persons ÷ 12 months = **5 kg per person per month**.
Cancelled: households against the household count, and years against months via 12 months/year.
Yes — that is the rate section 3(1) states.
(Here the text does supply "times 12" in its own illustration, so the months-per-year figure is
in-text at B3, unlike B2.)

**8.** [OUTRIGHT] time ÷ distance = min/km: 30/18 = **1.67 min/km**. That is a time per unit
distance, not a speed; a speed is a distance per unit time, so their arrangement is inverted.
Correct arrangement is distance ÷ time = 18 km / 30 min = **0.6 km/min**, or with 30 min = 0.5 h,
**36 km/h**.

**9.** [OUTRIGHT] Their volume ÷ mass gives m³/kg — a volume in every unit of mass, the
opposite of a density. Correct: 2,400 kg ÷ 1.2 m³ = **2,000 kg/m³**.

**10.** [SUPPLIED — partly]
The break is line 2: 30 × 20 gives m², an area, and fencing is a length. The unit check rejects
it without my knowing the right formula, exactly as advertised.
To give the *right* answer — 2 × (30 + 20) = **100 m** — I had to supply that fencing follows
the perimeter and how a perimeter is computed. **Neither perimeter nor the word is anywhere in
these files.** The problem only asks for the broken step, so strictly I was inside the text;
but I would have been stranded if asked for the number.

**11.** [OUTRIGHT] The break is line 2–3: they multiplied a *per-month* rate by a number of
*days*. The units give kg·day per person per month, which is nothing. Correct:
5 kg/person/month × 12 months/year = **60 kg per person per year**.

**12.** [OUTRIGHT] The break is the second-to-last line: "contains kg, m and s, and so does
kg m² s⁻²". The same letters are not the same units — kg m s⁻¹ and kg m² s⁻² differ in the
powers of both m and s. The units do not match and the formula is rejected.

**13.** [SUPPLIED — this one I could not do from the files at all]
4.5 crore litres/day ÷ 30 lakh people. **Neither "crore" nor "lakh" is defined anywhere in
B1–B6.** I supplied crore = 10⁷ and lakh = 10⁵ from outside the text.
45,000,000 L/day ÷ 3,000,000 persons = **15 litres per person per day**, not 135. The press
note is out by a factor of nine.
What this does not establish: nothing about whether 15 L/person/day is enough, nothing about
whether the plant is the city's only supply, and nothing about whether either of the two input
figures is correct. I have checked one division, not a water supply.
*Without the two words, a reader can write the arrangement — litres per day ÷ persons gives
litres per person per day — and cannot produce a single digit.*

**14.** [OUTRIGHT] 2 mg/L × 5,000 L = 10,000 mg = **10 g per fill**. The brochure divided where
it should have multiplied; their arrangement gives mg per litre squared, which is not an amount
of anything. The litres cancel only under multiplication.
What this does not establish: nothing about what the tank *should* be dosed at — the problem
says so explicitly, and the 2 mg/L is not to be carried away as a dose.

### What B3 changed about what I would do

- I can now reject a formula in a paper, a protocol or a spreadsheet **without being able to
  write the right one**, and I would do that rather than defer to whoever wrote it.
- I would read the unit that falls out of a calculated dose before acting on the number.
- I would refuse to take a logarithm of, or exponentiate, a quantity carrying a unit.
- I would stop treating "kg, m and s appear on both sides" as agreement, and read the powers.
- I would not accept a unit check as endorsement of a formula, and I would say so out loud when
  someone offers one as proof.

### Gaps

1. **"A logarithm, and any quantity used as an exponent, takes a plain number with no unit on
   it."** (Definition; repeated twice more.)
   The logarithm is never explained, never defined, never used in any worked example, and never
   appears in any of the fourteen problems. A reader with no background does not know what a
   logarithm is and is being given a rule about an object they cannot identify. **Needed:**
   either a definition, or the removal of a rule that no problem exercises.

2. **"It cannot confirm a formula, because a wrong dimensionless factor changes no unit."**
   (Definition, last line.)
   *It* has no antecedent — nothing in the Definition block has yet been named as a check or a
   procedure. The Definition describes dimensions; then a pronoun arrives referring to a method
   that is only introduced in the next block. I read this sentence three times. Also
   "dimensionless" is used here before the idea of a quantity with no dimension is explained;
   it never is, properly.

3. **"as you did in the section before this one"** — a live cross-reference, and the only one
   in these six files that actually resolves. Noted because B6 contains one that does not.

4. **"And the persons in the working above are not an SI unit."**
   Asserted and then dropped. If persons are not an SI unit, what is their status in a
   dimensional check? Can I cancel them or not? The illustration *does* cancel them, and
   problem 3 asks me to produce persons per area as an answer. The text gives a warning and no
   rule to go with it. I had to decide for myself that non-SI labels still cancel.

5. **"Three metres plus four seconds is not seven of anything."** Fine. But the four-step check
   is stated for *equations between quantities*, and then every worked example and eleven of the
   fourteen problems are about a single expression, not an equation with two sides. Step 4 —
   "compare the two sides" — has nothing to compare in most of the problems. I had to
   reinterpret the procedure as "see what unit falls out", which is not what step 4 says.

6. **Problem 13's "crore" and "lakh" — see above.** The single hardest blocker in the file.

7. **The Illustration begins with a block-quoted line ("The stretch is 12 km...") with no lead-in
   sentence**, immediately after the heading. Something introducing the speaker has been cut; the
   quote arrives unattached.

---

## B4 · Energy units: joule, kilojoule, calorie, kilocalorie

### Exercises

**Exercise 1 (critique).** [OUTRIGHT]
Wrong because nothing was measured. The calorie's size in joules was fixed by agreement, so
4.184 is exact by definition, not established by careful measurement — and there are two such
agreements in use.
Replacement: *"One thermochemical calorie is defined as exactly 4.184 joules; a second
definition, the International Table calorie, is exactly 4.1868 joules, and you should say which
one you are using."*

**Exercise 2 (teaching).** [OUTRIGHT]
Plain version: the number on the packet is not weighed out of the food — it is worked out from
how many grams of carbohydrate, protein and fat are in it, each multiplied by a fixed factor and
added up. Quotable sentence: *"That number is a calculation, not a measurement."*
How much the two-calorie business matters to a reader: **almost none** — the two definitions
differ in the fourth digit, which is far below anything a food label is good to.

### Numbered problems

**1.** [OUTRIGHT] 1,000 J = **1 kJ**; 2.5 kJ = **2,500 J**; 3 kcal = **3,000 cal**;
7,000 cal = **7 kcal**.

**2.** [OUTRIGHT] ×4.184: 1 → **4.184 J**; 10 → **41.84 J**; 250 → **1,046 J**;
1,500 → **6,276 J**.

**3.** [OUTRIGHT] ÷4.184: 8.368 → **2 cal**; 2,092 → **500 cal**; 4,184 → **1,000 cal**.

**4.** [SUPPLIED on the second half]
450 kcal × 4.184 = **1,882.8 kJ**.
"Then say how many digits you would write down." I wrote **1,880 kJ** (three digits, matching
the three in 450), on the strength of the must-know line that a conversion never improves a
number. **But the text never gives a rule for choosing digits.** It gives one example in B5
(5.5506 → 5.55) and nothing else. I could not tell whether the wanted answer was 1,883, 1,880,
or "about 1,900". See the gap list.

**5.** [OUTRIGHT] 700 × 4.184 = **2,928.8 kJ**; 700 × 4.1868 = **2,930.76 kJ**.
Apart by **1.96 kJ**, which is **0.067 %** of either figure — about seven parts in ten thousand.
(The problem says "as a share of the figure" without saying which figure; they agree to three
digits either way.)

**6.** [OUTRIGHT, after reading the question three times]
2,000 kJ ÷ 4.184 = **478.0 kcal**; with the International Table calorie, 477.7 kcal.
Which definition could have changed the answer at two digits: **neither**. The two results
differ by 0.3 kcal, in the fourth digit; at two digits both are 480 kcal. The choice of calorie
cannot reach two digits at this size of number.

**7.** [OUTRIGHT] 8,400 ÷ 4.184 = **2,007.6 kcal**. Back: 2,007.6 × 4.184 = 8,399.8 ≈ 8,400 —
yes, I get the number I started with, **provided I do not round in between**. If I write down
2,008 kcal and convert that back I get 8,401.5 kJ, and I have lost the original. So the round
trip survives the arithmetic and not the rounding.

**8.** [OUTRIGHT] (60 × 4) + (8 × 4) + (22 × 9) = 240 + 32 + 198 = **470 kcal per 100 g**.
In kilojoules: 470 × 4.184 = **1,966.5 kJ per 100 g** (I would write 1,970 kJ).

**9.** [OUTRIGHT] The break is line 3: they divided where they should have multiplied. Correct:
450 × 4.184 = **1,882.8 kJ**. The size check catches it — a kilojoule is smaller than a
kilocalorie, so the number must get bigger, not smaller.

**10.** [OUTRIGHT] The arithmetic is right and the **unit is wrong**. 250 kcal × 4.184 = 1,046
**kilojoules**, not joules. In joules it is 1,046,000 J. The break is the last line.

**11.** [OUTRIGHT] 600 kcal × 4.184 = **2,510.4 kJ**. The two papers agree; they are the same
quantity written in two units, and neither is wrong.
What this does not establish: nothing about whether either paper measured the food correctly,
nothing about whether they measured the same food, and nothing about which calorie the second
paper used — though at this size that last one cannot matter.

**12.** [OUTRIGHT] Compute the conversion: any kilojoule figure ÷ 4.184 is a kilocalorie figure.
The datasets are comparable and **nobody has to collect anything again**.
What this does not establish: that the two datasets are comparable *in any other respect* —
same population, same method, same period, same definition of what was being measured. I have
removed one obstacle, not shown the comparison is sound.

### What B4 changed about what I would do

- I would stop saying the calorie was measured, and I would correct anyone who writes that it was.
- I would ask which calorie somebody used before telling them their number is wrong, and I would
  not open a disagreement over a difference in the fourth digit.
- Reading "calories" on a packet, a paper or a scheme document, I would read it as kilocalories
  and then check the size of the number to confirm.
- Given grams of carbohydrate, protein, fat and alcohol I can now produce the declared energy
  myself (4, 4, 9, 7 kcal/g), and I would treat a printed Indian label energy as **calculated,
  not measured**, and say so.
- I would refuse to hand back a two-digit figure written out to six digits after a conversion.

### Gaps

1. **"If their kilojoule figure and yours part company in the fourth digit, neither of you has
   slipped. You used different calories."**
   ***Their.* There is no antecedent anywhere in this section.** No other party has been
   introduced — the illustration is the reader converting a Schedule II figure alone. A sentence
   setting up a colleague or a second paper has plainly been cut, and the paragraph now opens
   mid-thought with a pronoun. This is the clearest deletion scar in the six files. I read the
   paragraph four times before concluding the referent was simply absent.
   The line break in the source ("If\ntheir...") suggests text was removed from in front of it.

2. **"Regulation 5(3)(e)(i) of the same regulations fixes the factors by which the declared
   energy is calculated rather than measured."** (Definition, last line.)
   Factors for *what*? The Definition never says what the factors do, what they multiply, or
   what they produce. **The actual factors — 4, 4, 9, 7 kcal/g — appear only in the last
   must-know bullet**, after the Illustration, and are never demonstrated in a worked example.
   Problem 8 is the first and only place the method is exercised, and it re-states the factors
   itself rather than relying on the section. A reader who skips must-know bullets cannot do
   problem 8 from the body of the section.

3. **"4,50,000" and "18,82,800".**
   Indian digit grouping, used without a word of explanation, in the section's single most
   important worked example. A reader who groups in threes will read 4,50,000 as forty-five
   thousand or be unable to parse it at all, and the whole point of the example — that the
   digits are the same and the unit is not — is lost. **Needed:** either Western grouping or one
   sentence on the convention. This compounds gap B3-6: the files assume familiarity with
   lakh/crore notation twice and explain it never.

4. **"Say how many digits you would write down"** (problem 4) and its twins in B5 (problems 5
   and 6), plus **"write the answer to four digits"** (B5 problems 2, 3, 4).
   **No file ever states a rule for choosing digits.** There is one worked instance (5.5506 →
   5.55) and one slogan ("a conversion never adds a digit"). Worse, "four digits" is ambiguous
   and the text never disambiguates it: for 13.876554 do I write 13.88 (four significant
   figures) or 13.8766 (four decimal places)? I chose significant figures because 5.551 and
   5.107 read that way, but that is my inference from two examples. **Needed:** a definition of
   "digit" as used here, and a rule for how many to keep.

5. **"Open the National Food Security Act, 2013, and go to Schedule II. Find the row for lower
   primary classes. The hot cooked meal is set at 450."**
   A second instruction requiring an external document. The numbers are given anyway (450, 700),
   so the trip is unnecessary, but "read the head of the column instead of the number under it"
   — the pedagogical point of the whole illustration — depends on a table the reader is not
   shown. I have to take on trust that the column head reads "Calories (Kcal)".

6. **"lower primary classes" / "upper primary"** are used as if familiar. Never explained.

7. **The Fifth International Conference on the Properties of Steam, July 1956** is given with a
   precision that suggests it matters, and nothing is ever done with it. Meanwhile the
   thermochemical calorie's origin — who fixed it, when — is not given at all. The asymmetry is
   unexplained.

8. **"A meal in the hundreds is kilocalories."** (Must-know.) This is a magnitude heuristic —
   precisely the move B1's must-know forbids ("Never work out which unit was meant from how big
   the number looks"). The two sections give directly opposing instructions and neither
   acknowledges the other. I had to decide which one governs. I do not know.

---

## B5 · Concentration units: mg/dL, mmol/L, and converting between them

### Exercises

**Exercise 1 (critique).** [OUTRIGHT]
Wrong because there is no single factor between mg/dL and mmol/L. The factor is built from the
substance's molar mass, so it belongs to the substance, not to the pair of units. 18 is the
glucose divisor (and even for glucose it is a rounding of 18.016); it is wrong on everything
else, and a figure that is a mixture reported as one total has no molar mass at all.
Replacement: *"To convert a laboratory value from mg/dL to mmol/L, identify the substance, look
up its molar mass in g/mol, multiply the mg/dL figure by ten, and divide by the molar mass. If
you do not hold the molar mass, do not convert."*

**Exercise 2 (teaching).** [OUTRIGHT]
92 mg/dL → (92 × 10) ÷ 180.16 = **5.11 mmol/L**. So 92 and 5.1 are the same blood sugar in two
different units, and neither paper is wrong.
Quotable: *"They are not disagreeing — they are speaking two languages about one number."*
Confidence: high for the conversion itself; I would add that I have not checked that the two
papers measured the same thing in the same conditions.

### Numbered problems

**1.** [OUTRIGHT] 5/dL → **50/L**; 0.7/dL → **7/L**; 120/L → **12/dL**; 96/L → **9.6/dL**.

**2.** [OUTRIGHT, with the "four digits" ambiguity noted above]
1,000 ÷ 180.16 = **5.551**; 920 ÷ 180.16 = **5.107**; 2,500 ÷ 180.16 = **13.88**.

**3.** [OUTRIGHT] 72 → **3.996**; 110 → **6.106**; 45 → **2.498**.

**4.** [OUTRIGHT] 4 → **72.06**; 6.5 → **117.1**; 9 → **162.1**.

**5.** [OUTRIGHT on the arithmetic, SUPPLIED on the digits]
92 mg/dL → 920 ÷ 180.16 = 5.1066 → **5.11 mmol/L**. Digits: three, matching the laboratory's
two-to-three-digit input. Again, no rule was given; I copied the section's one example.

**6.** [OUTRIGHT] 7.2 mmol/L × 180.16 = 1,297.15 mg/L, ÷ 10 = **129.7 mg/dL**. Three digits,
matching the two in 7.2 — I would write 130 mg/dL and I am not sure the text agrees.

**7.** [OUTRIGHT] Exact divisor = 180.16 ÷ 10 = **18.016**.
180 mg/dL ÷ 18.016 = **9.991 mmol/L**; ÷ 18 = **10.00 mmol/L**.
Apart by 0.0089, which is **0.089 %** of the answer — under a tenth of one per cent. So the
shortcut is harmless *for glucose* and catastrophic for anything else, which is the point.

**8.** [PARTLY BLOCKED — and correctly so]
Glucose: 110 mg/dL → 1,100 ÷ 180.16 = **6.11 mmol/L**. Done.
Cholesterol: **cannot be done.** I have the substance and the method and the formula C₂₇H₄₆O,
and I do not have cholesterol's molar mass. I cannot compute it from the formula — the text
never gives atomic masses, never says a formula determines a molar mass, and never shows that
calculation. I cannot reuse 180.16, because that belongs to D-glucose and to nothing else, and
the section says so explicitly.
What I would do: record the conversion as pending, name what is needed — cholesterol's molar
mass in g/mol — and go and read it off PubChem compound 5997.

**9.** [OUTRIGHT] Two breaks. Line 2 asserts a universal divisor that does not exist, and 18 is
the glucose divisor being applied to cholesterol. Line 4 then presents a result that cannot be
produced at all: without cholesterol's molar mass the conversion is not available, so the right
output is "pending", not 11.1.

**10.** [OUTRIGHT] The break is line 3: the ×10 for decilitres to litres was dropped. Correct:
90 × 10 = 900; 900 ÷ 180.16 = **4.996 mmol/L**. Their answer is exactly a tenth of the truth.

**11.** [OUTRIGHT] Every line of arithmetic is right; the break is the last line. 5.550621670
claims nine digits of knowledge about a value the laboratory gave to three. Write **5.55
mmol/L**. The conversion renamed the amount; it did not measure it again.

**12.** [OUTRIGHT] Compute: their mmol/L figures convert to mg/dL by ×180.16 ÷ 10, or ours the
other way. The sets **can** be pooled on units and **nobody re-samples anybody**.
What this does not establish: that the two sets are otherwise poolable — fasting state, assay
method, population, timing. Unit compatibility is a precondition, not a licence.

**13.** [BLOCKED — deliberately, and I am confident it is deliberate]
To check whether 4.5 mmol/L and 210 mg/dL are the same figure I need cholesterol's molar mass,
and I do not have it. The one number the check requires is exactly the number this section
withheld. So the correct answer is: **I cannot verify the claim, and I would say so and stop.**
What I can say: the speaker has asserted an equivalence without showing the conversion, and
the implied divisor is 210 ÷ 4.5 = 46.7, which is not 18 and not anything the section supplied
— so whatever they did, they did not use a factor this course can source.
And even if the two figures did match, that would not establish that the two groups are
comparable: one mean cholesterol agreeing says nothing about the rest of the two populations.

### What B5 changed about what I would do

- I would **refuse** to convert mg/dL to mmol/L without first naming the substance and sourcing
  its molar mass — and I would say "pending" out loud rather than produce a number.
- I would stop treating "divide by 18" as a conversion rule; it is a glucose move.
- I would read the row label before the number on any laboratory report, and carry the substance
  name with every converted value I pass on.
- I would refuse to put a mixture reported as a single total into mmol/L at all.
- I would cut a converted value back to the digits the laboratory gave me.
- Given cholesterol's molar mass, I could now finish the cholesterol conversion in four steps —
  so the withholding is recoverable, not a dead end.

### Gaps

1. **"Do the glucose one first. The record is compound 5793."**
   ***The record* has no antecedent.** No record has been mentioned. PubChem has not been named.
   Nothing has told the reader to go anywhere or look anything up. Two paragraphs later the text
   says *"**Go back** to PubChem and search for cholesterol"* — which presupposes a first visit
   that the page never describes. **A sentence sending the reader to PubChem for glucose has
   been cut**, and its removal orphans both the first reference and the "go back". This is the
   second clear deletion scar, and structurally the same fault as B4's "their".

2. **PubChem is never explained.** What it is, who runs it, why its numbers are usable, whether
   "compound 5793" is a stable identifier — none of it. It is simply a proper noun that four
   problems depend on.

3. **"molecular weight" and "molar mass" are used as if interchangeable and never equated.**
   The Definition says *molar mass*, in g/mol. Every quotation from PubChem, and five of the
   problems, say *molecular weight* — "PubChem gives the molecular weight of D-glucose as 180.16
   g/mol". The text never says these are the same quantity. I inferred it from the shared unit.
   A reader who did not would not know that problem 5 supplies what step 2 of the method asks for.

4. **"one mole weighs 180.16 grams, so one millimole weighs 180.16 milligrams"** — asserted,
   never demonstrated. The move (divide both sides by a thousand) is the crux of why step 3's
   ×10 and step 4's division produce mmol/L rather than something else, and it is given as a
   single clause.

5. **Step 4 of the method — "Divide by the molar mass. That gives millimoles per litre" — is
   never unit-checked.** Milligrams per litre divided by grams per mole does not visibly give
   millimoles per litre; making it come out requires the mg↔g and mol↔mmol bookkeeping that the
   previous clause compressed into nothing. **This is the one place in six files where the
   discipline B3 spent a whole section installing is not applied**, and it is applied nowhere in
   B5's worked example either — the 100 → 1,000 → 5.5506 working carries no units on any line.
   I followed it by pattern-matching the numbers, not by understanding it.

6. **The mole is defined as "a fixed count of things, molecules here" and the count is never
   given.** Not needed for any problem, but a reader is told a base unit is a count and not told
   of what size. Also "amount of substance" is used in the Definition before "a mole is a fixed
   count" arrives in the plain-terms block — term used before explanation.

7. **The decilitre.** "A litre holds ten decilitres" is given, so the sum works. But `deci` is
   not in B1's prefix table, the litre is never defined anywhere in these files, and the
   relation of either to the SI's m³ is never stated. The section's entire arithmetic rests on a
   unit that no section introduces.

8. **"A molar mass is measured and computed, not decided, so it can be revised."** (Definition.)
   *Computed* from what? This is the only hint that a molar mass might be derivable from a
   molecular formula — which would make problem 8's cholesterol half doable — and it is never
   followed up. I read it twice to check whether it was licensing me to compute C₂₇H₄₆O myself.
   It is not, because no atomic masses are given. But it dangles the possibility.

9. **The withheld number — see the separate section below.**

---

## B6 · Body-size units: kg, m, cm and kg/m²

### Exercises

**Exercise 1 (calculation).** [OUTRIGHT]
Height conversion as its own line: 155 ÷ 100 = 1.55 m.
1.55 × 1.55 = 2.4025. 64 ÷ 2.4025 = **26.6 kg/m²**.
What it does not tell me: **nothing about whether 26.6 is high or low.** The arithmetic stops at
the number and its unit; where any line falls between one value and another is a decision
somebody made, and this section does not make it.

**Exercise 2 (teaching).** [PARTLY BLOCKED — and the section admits it]
Why the answer is in kilograms per metre squared: I can teach that — the unit falls out of the
division, kilograms on top, metres times metres underneath, and it is the unit that tells you
the centimetre version was never an answer at all. The error to watch for: a height in
centimetres, which gives a result ten thousand times too small because the denominator squares
the error.
**Why the height is squared: I cannot teach this, and neither can the section.** The text's only
statement is that "a squared denominator is a choice somebody made rather than a law you can
check" — and its doubling argument actually shows the square *fails* at the job you would assume
it was for, since the index rises by 2 when every length doubles. So the honest ten-minute
answer is "it is a convention, and here is a demonstration that it does not do what you would
expect". That is a defensible thing to teach, but the exercise asks "why is the height squared"
as though an answer exists, and the section supplies none. I could not tell whether the intended
answer was "it is a convention" or something the page dropped.

### Numbered problems

**1.** [OUTRIGHT] 72 ÷ 1.8² = 72 ÷ 3.24 = **22.2**. 81 ÷ 1.5² = 81 ÷ 2.25 = **36.0**.
45 ÷ 2.25 = **20.0**.

**2.** [OUTRIGHT] **1.68 m, 1.55 m, 1.80 m, 0.96 m.**

**3.** [OUTRIGHT] The answer is wrong by a factor of **10,000, too small**. The step that
produces it: the conversion is 100 cm to the metre, and the length is squared, so the factor is
squared too — 100 × 100 = 10,000 — and it sits in the denominator, so the result is divided by
10,000.

**4.** [OUTRIGHT] 1.52 × 1.52 = 2.3104. 58 ÷ 2.3104 = **25.1 kg/m²**.

**5.** [SUPPLIED — the technique is never taught]
1.60 × 1.60 = 2.56. 27.0 × 2.56 = **69.1 kg**.
**No section in these files ever rearranges a relation to solve for a missing quantity.** Every
worked example and every other problem runs forwards: given the inputs, divide. This problem
requires running it backwards, and the move — multiply instead of divide, because the missing
quantity was the numerator — is mine, not the text's. B2's cancelling method does not cover it,
because there is no unit to cancel; it is algebra, and algebra is absent from all six files.

**6.** [OUTRIGHT] The break is line 3: they converted the height and then **forgot to square
it**. Correct: 1.7 × 1.7 = 2.89; 65 ÷ 2.89 = **22.5 kg/m²**. The unit is the tell — 65 ÷ 1.7
gives kilograms per metre, not per metre squared, so 38.2 was never a kg/m² figure.

**7.** [OUTRIGHT] The break is line 4, "that is far too small, so multiply by 100". Two faults:
they fixed a number by feel rather than by fixing the method, and the factor is wrong anyway —
a centimetre height needs 10,000, not 100. Correct: 1.58 × 1.58 = 2.4964; 62 ÷ 2.4964 =
**24.8 kg/m²**. (Their 0.00248 × 10,000 would have got there; × 100 gets a tenth of nowhere.)

**8.** [OUTRIGHT] Compute the factor: the height sits in a squared denominator, so a
centimetres-for-metres substitution divides every value by 100 × 100 = **10,000**. Multiplying
the column by 100 leaves it a hundred times too small. The right multiplier is 10,000 — or
better, recompute the column from the source heights.
What this does not establish: that the height column is uniformly in centimetres. If some rows
were entered in metres and some in centimetres, no single multiplier fixes the column and
multiplying makes the metre rows wrong by 10,000 in the other direction. It also does not
establish that the heights or the masses are themselves correct — rescaling a column validates
nothing about what is in it.

### What B6 changed about what I would do

- Before computing a single row of a dataset, I would find out which unit the height column was
  collected in — and I would treat a centimetre height as a factor-of-10,000 error, not a
  rounding nuisance.
- I would convert the height to metres on its own line, before anything else, and say the unit
  out loud with the number.
- I would refuse to repair a bad index column by multiplying it by a number chosen to make the
  values look right.
- I would stop saying that dividing by the square of the height takes size out of the number,
  and could demonstrate with the doubling argument that it does not.
- I would refuse to quote a cut-off without saying whose it is and when it was set — **though,
  see below, this section gives me no cut-off and no body to attribute one to, so in practice
  this instruction leaves me with nothing to say at all.**

### Gaps

1. **"which is the squaring you met in the section on powers."**
   **There is no section on powers.** B1 through B5 contain no section on powers, no treatment
   of squaring, and no explanation of what `^2` means beyond its appearance in unit symbols.
   This is a live cross-reference to material that is not in the set. A reader who does not
   already know what squaring is has been told they met it and they did not.
   This is the most concrete evidence that something load-bearing was removed from the sequence.

2. **The index is never named and never given a purpose.**
   "The index is a number together with its unit." (Definition, para 4.) ***The index* has no
   antecedent** — the preceding paragraph describes dividing a mass by a squared length but
   never calls the result an index. The noun arrives already definite. And across the whole
   section the reader is never told **what the index is called, what it is used for, who
   computes it, or why anybody would**. I computed it eleven times without knowing what it was.

3. **"A length entered in centimetres rather than metres therefore divides the value by 10⁴."**
   (Definition, para 3.) *The value* of what? Nothing has been named as having a value.
   *Therefore* — following from what? The preceding sentence states a unit, not a mechanism. The
   reasoning (that the denominator squares the conversion factor) appears only in the
   Illustration. In the Definition it is a conclusion with no premise.

4. **The Illustration's first working block is incomplete.**
   "A person weighs 70 kg and stands 168 cm tall. Square it as it stands and divide." The block
   shows only `168 times 168 = 28,224`. **The division is never shown.** The next sentence simply
   asserts "The answer is 0.00248". I checked it — 70 ÷ 28,224 = 0.0024802 — but the reader is
   given a number with no working, in a section whose whole method is to show every line, and in
   a set of files that repeatedly instructs the reader to show every line. Problem 4 asks the
   reader to show "every line"; the Illustration does not.

5. **"Square it as it stands"** — *it* is the height, three words after "weighs 70 kg", and I had
   to read the sentence twice to be sure I was not squaring the mass.

6. **"Take a shape and make every length twice as long, keeping everything else the same. Mass
   goes with volume, and volume has three lengths in it..."**
   "Mass goes with volume" is asserted and never justified in the body — it silently assumes
   constant density. The "Where this picture breaks" block does rescue it ("holds only while the
   shape and the density stay the same"), but density has not been established as a concept that
   links mass to volume anywhere in B6, and the reader has to carry it from B1's single passing
   line (density is mass divided by volume). The argument is given before its assumption.

7. **"So the index itself goes up."** Up *by a factor of two*, which the following block shows
   (8 ÷ 4 = 2) but the sentence does not say. Minor, but the conclusion and its size are split
   across two elements.

8. **"a squared denominator is a choice somebody made rather than a law you can check."**
   Who? When? Never said. Combined with must-know bullet 6 — *"Quote a cut-off only with whose
   it is and when it was set"* — the section instructs the reader to do something it gives them
   no material to do. **Not one cut-off, not one body, not one date appears in the section.** I
   was told to attribute, and given nothing to attribute.

9. **"the squaring squares the mistake as well"** and "the mistake is squared too" — the word
   *mistake* is used where *conversion factor* is meant. It took a second reading to see that
   what is squared is the factor 100, not an error in the measurement.

---

## The deliberately withheld number

**It is in B5, and yes — it reads as deliberate.** The section signals it three times before it
happens and twice after:

- *"Start with the sum you cannot do, because that is the one this section is really about."*
  — the very first sentence of the Illustration, before any working. This is unambiguous
  staging. I knew a wall was coming.
- *"Now the cholesterol, and watch it stop."*
- *"And you still cannot do the sum."*
- *"You know the method. You know the substance. None of that is enough."*
- And a prescription for what to do instead: write down that the conversion is pending, name
  what you need, go and read it off PubChem 5997.

So as a reader I was never left thinking the page had simply stopped. It read as constructed,
and the construction worked on me: at problem 8 and again at problem 13 I reached for a divisor,
found I had none, checked whether 180.16 could be borrowed, and stopped — which is exactly the
behaviour the section is trying to install. The payoff lands.

**But there is a real wrinkle in *why* it is withheld, and it is worth knowing about.**
The stated reason is:

> *"The molecular weight was not captured when that page was read for this course. So the
> course can hand you glucose's molar mass and cannot hand you cholesterol's."*

That is not a pedagogical reason. That is the course reporting **its own data-capture failure**
and then building a lesson on the wreckage. The staging around it is deliberate; the *cause* is
narrated as an accident. As a reader this produced a specific and slightly corrosive reaction:
if this number went missing because somebody did not copy it down, **how many of the other
numbers in these files are in the same position and not flagged?** I now hold 180.16, 4.184,
4.1868 and 299 792 458 slightly more loosely than I did an hour ago.

There is a clean version of this available — "this number is withheld so that you practise
stopping" — and the text does not use it. I would flag that as a choice worth revisiting, not
because the exercise fails, but because the reason given undermines the reader's trust in every
other figure in the set.

**A second, unflagged withholding — which does read as "the page stopped".**
Five problems (B4-4, B5-2, B5-3, B5-4, B5-5, B5-6) ask how many digits to write down, or demand
an answer "to four digits". **No rule for choosing digits is given anywhere in the six files**,
and "digit" is never defined — significant figure or decimal place is left open, and the two
give different answers (13.88 vs 13.8766 for B5 problem 2). Here there is no staging, no signal,
no "you cannot do this and here is why". It simply is not there. That one did feel like the page
stopped, and unlike the cholesterol gap it is not recoverable by going and looking something up,
because what is missing is a convention the course was supposed to set.

---

## Summary table of attempts

| File | Outright | Supplied (guessed at something absent) | Blocked |
|---|---|---|---|
| B1 | 1 of 3 | 2 of 3 (Ex 2, Ex 3) | 0 |
| B2 | 6 of 10 | 4 of 10 (Ex 2 partly, P3, P4, P5, P7) | 0 |
| B3 | 14 of 16 | 2 of 16 (P10 partly, P13) | 0 |
| B4 | 13 of 14 | 1 of 14 (P4's digit question) | 0 |
| B5 | 13 of 15 | 2 of 15 (digit questions) | 2 partial (P8 half, P13 — both intended) |
| B6 | 7 of 10 | 2 of 10 (Ex 2 partly, P5) | 0 |

## Ranking of the gaps by how badly they strand a reader

1. **B6: "the section on powers" does not exist.** A cross-reference to absent material,
   carrying the one concept (squaring) the entire section depends on.
2. **B6: the index is never named or explained.** Eleven computations of an unnamed thing with
   an unstated purpose, plus an instruction to attribute cut-offs and no cut-off to attribute.
3. **B3: "crore" and "lakh" are never defined**, and problem 13 cannot produce a digit without
   them. B4 then uses Indian digit grouping (4,50,000) in its central worked example, also
   unexplained.
4. **B5: the missing PubChem lead-in.** "The record is compound 5793" and "**Go back** to
   PubChem" both point at a sentence that is not on the page.
5. **B4: "If *their* kilojoule figure and yours..."** — a pronoun with no antecedent anywhere in
   the section, at the punchline of the two-calorie lesson.
6. **The digit rule, absent across B4 and B5** while six problems demand it.
7. **B2 problem 7 requires squaring a conversion factor**, four sections before any file shows one.
8. **B5 step 4 is never unit-checked**, in the one section where B3's method most needed applying.
9. **The litre and the decilitre are never defined**, though B5 is built on them.
10. **B1's must-know bullet 1 and B2's must-know bullet 1 both open with an orphan "It"** — the
    question halves of a Q&A appear to have been deleted.
