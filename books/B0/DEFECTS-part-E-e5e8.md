# Defects · Book 0 Part E, sections E5–E8

Audit of `B0-R0-C35` (E5, the cell), `B0-R0-C36` (E6, metabolism), `B0-R0-C37` (E7, genes) and
`B0-R0-C38` (E8, organs). Run 23 September 2026 against `claude.md` (§4, §5, §7b, §8, §9, §10, §11),
`books/B0/READY-part-E.md`, `books/B0/INVENTORY-part-E.md` and the files in `sources/` that
`sources/INDEX.yml` maps the citekeys to.

All four are `empirical` and none is `quantitative`, so no practice answers were recomputed. The
weight of this audit is sourcing and §9.

**Counts.** 3 blocking, 9 major, 10 minor. 22 total.

**Method note on check 1.** Every `definition.references[].quote` in all four records — 70 of them —
was searched for in the file `INDEX.yml` maps its citekey to, after normalising whitespace and
curly quotation marks. **All 70 are present, verbatim.** No quote is missing, no reference lacks a
`quote`, and no citekey resolves to a `do_not_cite` file. None of the four records has an
`illustration.numbers` block, and the build's numbers register carries zero rows for all four. So
every defect below is a defect of *support* — of what a passage that is genuinely in the source was
made to stand behind — or of scope, sequence or language. That is the intended shape of this audit
and it is where every failure found actually sits.

---

## Blocking

### 1. C37 — `simplified_explanation` defines a gene, from nowhere, in a record whose own audit trail says the source pack cannot support it

**Field.** `simplified_explanation`, the paragraph beginning "Next, a gene."

**The claim as the record makes it.**

> Next, a gene. A gene is a piece of that inherited material, carried on a chromosome — one of the
> long packages the DNA is kept in.

**What the source actually says.** Nothing. `sources/openstax_biology_2e.txt` contains no sentence
defining a gene as a length of DNA or as a piece of inherited material, and the record knows it.
`definition.references[6].verified.note` states in plain words:

> No sentence in the pack defines a gene as a length of DNA; see the handover note. This record
> therefore says what a gene determines and does not state its physical extent.

`definition.text` honours that — it says only "The gene that encodes a protein determines the order
of amino acids in that protein", which is sourced to Biology 2e §3.4 and is exact.
`simplified_explanation` then supplies the physical extent anyway, unsourced. "Chromosome — one of
the long packages the DNA is kept in" is likewise nowhere in the pack; §12.2 uses the word
throughout and never defines it.

This is §7b's named defect in its purest form: a claim written from what the model knew, sitting in
the field the reader actually reads, in a record where the audit trail two fields above says the
claim cannot be made. It also destroys the illustration. The whole of C37's illustration is the
story of going to §14.2 for a definition of a gene, not finding one, and drawing the lesson *search
the page for the word before you cite it*. A reader who has already been handed a crisp definition
of a gene two fields earlier cannot feel that dead end, because for them it is not a dead end.

**Smallest fix.** Delete the two definitional clauses and let the simplified explanation say what
the sourced `definition.text` says: *Next, a gene. What a gene does is this: it fixes the order of
the building blocks in one protein.* Keep "carried on a chromosome" only if a reference is added for
it — §12.2's "Physical characteristics are expressed through genes carried on chromosomes"
(`openstax_biology_2e.txt`) carries exactly that and nothing more, and is one line to add.

---

### 2. C38 — `simplified_explanation` defines a hormone, and the record's `verified.note` states that it does not

**Field.** `simplified_explanation`, the paragraph beginning "A chemical that one part of the body
puts into the blood".

**The claim as the record makes it.**

> A chemical that one part of the body puts into the blood, so that it can act somewhere else, is
> called a hormone.

**What the source actually says.** `definition.references[19].verified.note` reads:

> Section 17.1 contains no definition sentence for the word hormone. The word appears only as the
> appositive inside this sentence, between two dashes. […] This record therefore states what an
> endocrine organ secretes, where it goes and what it does when it arrives, all of which 17.1
> carries, and it does not offer a dictionary definition the source cannot support.

The first half of that note is correct and was verified: `openstax_anatphys_2e.txt` §17.1 carries
only "the endocrine organs, which secrete chemicals—the hormone—into the extracellular fluid", and
the file's own `[NOTE]` records the same finding. The last clause of the note is false. The record
does offer a dictionary definition, in `simplified_explanation`. It is also not quite 17.1's
account: 17.1 has hormones secreted into the *extracellular fluid*, which then drains to blood, not
put "into the blood"; and "so that it can act somewhere else" is a purposive gloss 17.1 nowhere
makes.

A `verified` block asserting that a record avoided a claim it did not avoid is the one failure mode
§8 exists to stop — "never set because the citation looks right". An auditor trusting this note
passes the record.

**What makes this worse, and cheaper to fix than the drafter thought.** The gap was avoidable. The
source pack already holds two sentences that define a hormone, both in a citekey already in
`INDEX.yml`, and one of them is in a section C35 already cites:

- `openstax_biology_2e.txt` §9.1: "The ligands released in endocrine signaling are called hormones,
  signaling molecules that are produced in one part of the body but affect other body regions some
  distance away."
- `openstax_biology_2e.txt` §3.4: "Hormones are chemical-signaling molecules, usually small proteins
  or steroids, secreted by endocrine cells that act to control or regulate specific physiological
  processes, including growth, development, metabolism, and reproduction."

**Smallest fix.** Add one reference to `openstax_biology_2e` §9.1 with the first quote above, and
correct the closing clause of `references[19].verified.note` to say that the definition is taken
from Biology 2e §9.1 because A&P §17.2 is out of pack. Then align the simplified sentence to the
sourced words: *A chemical made in one part of the body that affects other parts some distance away
is called a hormone.* No prose is lost and the record stops contradicting itself.

---

### 3. C37 — a general rule about protein synthesis, resting on a quote that states it only for one signalling route

**Field.** `definition.text`, final paragraph; repeated verbatim in `must_know[0]`,
`illustration.body`, `exercises[1].answer`, `exercises[2].answer` and `retrieval_items[3]`.

**The claim as the record makes it.**

> A gene fixes the order of amino acids in a protein. Whether that protein is made at a given moment
> is regulated by signals arriving at the cell […]

**What the source actually says.** The quote attached to it (`references[8]`, Biology 2e §9.1) is:

> many of these molecules bind to proteins that act as regulators of mRNA synthesis (transcription)
> to mediate gene expression. Gene expression is the cellular process of transforming the
> information in a cell's DNA into a sequence of amino acids, which ultimately forms a protein.

Read in place, "these molecules" are hydrophobic ligands that have crossed the membrane and bound an
**internal** receptor. The passage establishes that *one* signalling route regulates transcription
of *some* genes. It does not say, and §9.1 nowhere says, that whether any given protein is made is
in general regulated by signals arriving at the cell. The record states the special case as a
general rule.

This is the defect the audit was set to hunt: the quote is genuinely in the source, the prose reads
as unimpeachable, and the passage does not say what it was cited for. It matters more than most
because this sentence is the load-bearing plank of C37's §9 work — it is what the record uses, five
separate times, to refuse the move from "it is genetic" to "so nothing can be done". The course's
best anti-fatalism move should not rest on an over-reading.

**Smallest fix.** Narrow the claim to what §9.1 carries and let the mechanism do the work, e.g.
*A gene fixes the order of amino acids in a protein. It does not by itself decide when that protein
gets made: a signal arriving at a cell can bind a receptor inside it and switch the making of a
protein on, which is one route among others.* The same narrowing applied to the five repeats. The
teaching point survives intact.

---

## Major

### 4. C36 — the refusal of the kcal-per-kilogram figure is attributed to the wrong section

**Field.** `illustration.body`.

**The claim as the record makes it.**

> The section on stocks and flows has already told you why Book 0 will not give you a figure of that
> kind.

**What is actually the case.** Stocks and flows is `B0-R0-C23`. It contains no refusal of that figure
and no discussion of what a kilogram of change in a body is made of — searched for
`kilogram of body`, `per kilogram of body`, `made of`, `composition`, `linear`, `extrapolat`, `3500`,
`7700`: nothing. The refusal lives in `B0-R0-C33` (E3, "Conservation of energy, and a system with a
boundary"), three sections earlier in this same Part, where `must_know` carries *"This section gives
you no way to turn joules into kilograms of a body […] How much energy a kilogram of change holds
depends on what the change is made of"*, and the teaching answer carries *"What not to offer: a
figure for how many kilocalories make a kilogram."*

A reader who takes the instruction and goes back to the stocks-and-flows section will not find the
reasoning. §10 rule 5 asks a section to say in ordinary words what it stands on; naming the wrong
one is worse than naming none.

Note for whoever fixes this: `books/B0/INVENTORY-part-E.md` carries the same error twice ("E3 stands
on Book 0 C9, not on E1" and "Book 0 C9 has already taught stocks and flows"). `B0-R0-C09` is "What
a unit is, and the SI base and derived units". The inventory is where the mis-numbering entered.

**Smallest fix.** Replace with *The section on conservation of energy and the boundary has already
told you why Book 0 will not give you a figure of that kind.* And correct the two lines in
`INVENTORY-part-E.md`.

---

### 5. C36 — the §24.7 claim has no reference behind it, and the reason given for refusing §24.7 is the weaker of the two available

**Field.** `illustration.body`.

**The claim as the record makes it.**

> Section 24.7 of the same book, *Nutrition and Diet*, will hand you a figure for how many calories
> make a pound of body weight. It is the most repeated number in this whole subject. It is stated
> the same way, with no study behind it.

**What the source actually says.** `openstax_anatphys_2e.txt` §24.7:

> The accumulation of an extra 3500 calories adds one pound of weight. If an excess of 200 calories
> per day is ingested, one extra pound of body weight will be gained every 18 days. At that rate, an
> extra 20 pounds can be gained over the course of a year.

Two problems.

**(a) No audit trail.** This is the only claim about a source in any of the four records that carries
no `definition.references` entry at all. Every other source-claim in the four — the missing
"selectively permeable" in Biology §5.1, the percent sentence in A&P §24.1, the missing definition of
a gene in Biology §14.2, the insulin-receptor list in A&P §17.9 — is recorded either as a `quote` or
in a `verified.note`. This one is asserted in the reader's field and nowhere else. The one page in
Part E that most needs to be on record as refused is the one page with nothing on record.

**(b) The stated reason licences the figure.** The record's objection is "no study behind it", with
the composition argument following. Both are right and both are survivable: produce a primary source
and a composition assumption, and the reasoning as written admits the number. But §24.7 does not
merely state 3,500 flat. It compounds it — 200 kcal/day → one pound per 18 days → 20 pounds a year —
and that linear extrapolation is refused by this course whatever source stands behind it. The
illustration teaches the reader a rule that would let the extrapolation back in.

**Smallest fix.** Add a reference entry for `openstax_anatphys_2e` §24.7 carrying the quote above
with a `verified.note` recording it as refused, and add one sentence to the illustration after "with
no study behind it": *And look at what the page does with it next. It multiplies the figure out to a
pound every eighteen days and twenty pounds a year. That second step is the one this course refuses
outright, and it would still refuse it if a study were produced tomorrow, because a body is not a
bank account that compounds.*

**Where the do-not-cite note should live.** Three places, and each does a different job:

1. **`sources/openstax_anatphys_2e.txt`, inline under the §24.7 paragraph**, as a
   `[NOTE] DO NOT CITE` line in the same style as the file's existing `NOT OBTAINED VERBATIM`
   blocks. This is the only place a drafter is certain to read before quoting, and the file's
   existing notes demonstrably work — four records correctly avoided numbers because of them.
2. **`sources/INDEX.yml`**, under the `openstax_anatphys_2e` entry. The existing `do_not_cite` block
   is keyed by file and cannot express a clause, so this needs a sibling field — e.g.
   `do_not_cite_clauses:` naming §24.7's extrapolation sentences and the reason. Whatever the build
   reads for `do_not_cite` must read this too, or it blocks nothing.
3. **`books/B0/READY-part-E.md`**, in "One source deliberately not used". That section currently
   makes only the general statement that A&P's numbers are unusable. It should name §24.7 by clause
   and record the *second*, stronger reason: not unsourced, but structurally refused.

---

### 6. C37 — the opening sentence names the wrong preceding section

**Field.** `simplified_explanation`, first sentence.

**The claim as the record makes it.**

> The section before this one gave you a cell, its outer skin, the proteins in it and what a receptor
> does.

**What is actually the case.** C37 is sequence 37. The section before it is sequence 36, E6,
metabolism. The section described — cell, membrane, proteins, receptor — is E5, sequence 35, two back.
The record's own `concept_deps` correctly name `B0-R0-C35`; the prose then calls E5 "the section
before this one". §10 rule 5 makes this sentence load-bearing and it is wrong.

**Smallest fix.** *The section on the cell gave you a cell, its plasma membrane, the proteins in it
and what a receptor does.* This also repairs defect 22.

---

### 7. C38 — the opening sentence names the wrong two preceding sections

**Field.** `simplified_explanation`, first sentence.

**The claim as the record makes it.**

> The last two sections gave you a cell, and then the chemistry that goes on inside it.

**What is actually the case.** C38 is sequence 38. The last two sections are 37 (genes) and 36
(metabolism). "A cell, and then the chemistry that goes on inside it" is 35 and 36. Off by one, the
same way as defect 6 and for the same reason: both drafters wrote to the dependency graph in
`INVENTORY-part-E.md` rather than to document order, and E7 branches off E5 while E8 depends on E5
and E6.

**Smallest fix.** *The section on the cell and the section on metabolism gave you a cell, and then
the chemistry that goes on inside it.*

---

### 8. C37 — "inference" is used five sections before the section that teaches it

**Field.** `must_know[2]`.

**The claim as the record makes it.**

> Refuse any inference that runs from an observed trait back to a specific genetic make-up without a
> test that looked.

**What is actually the case.** The build's own terms-of-art table names `B0-R0-C37` as the corpus's
first use of *inference*, with the plain words it owes the reader: "the move from the reasons to the
conclusion". The section that teaches it is `B0-R0-C42`, "Argument: premise, inference, conclusion",
five sections later. §10 rule 1 forbids the forward reference; §11 rule 8 and §8's `teach_once` list
require the word to be given in plain words where the reader first meets it.

**Smallest fix.** Use the plain words here and let C42 keep the term: *Refuse any move that runs from
an observed trait back to a specific genetic make-up without a test that looked.*

---

### 9. C35, C37, C38 — one `quote` made to carry two or three claims, with the extra sentences parked in `verified.note` where the build cannot search for them

**Field.** `definition.references[].quote` / `.verified.note`, systematically.

**What §8 requires.** "`quote` […] is the field that makes the audit real. Copy the exact words the
claim rests on; the build searches the file for them and blocks if they are not there." A claim whose
supporting sentence lives only in a prose note is not machine-checked, and the whole point of the
`quote` field is that the last audit's assurance is not the artefact.

**Instances, worst first.** In each, the sentence named in the note *is* in the source — this is a
defect of audit mechanics, not of truth.

- **C37 `references[1]`.** Quote is the base-pairing sentence alone. Its note claims the reference
  "carries the two strands, the right-handed helix, the A-T and C-G pairing and the word
  complementary". The quote carries only the pairing. The helix and "complementary" are in adjacent
  sentences of the same paragraph and are not quoted.
- **C35 `references[8]`.** Quote is "To move substances against a concentration or electrochemical
  gradient, the cell must use energy." The claim attached adds "and specific carrier proteins, also
  called pumps, carry out that movement", which sits only in the note. The source reads "specific
  carrier proteins **or** pumps"; "also called pumps" over-reads it into a synonym.
- **C35 `references[4]`.** Quote is the ribosome sentence. The claim attached includes "The nucleus
  houses the cell's DNA", which sits only in the note.
- **C38 `references[21]`.** Quote is the specificity sentence alone. The record's attached sentence
  also asserts "Endocrine signalling is slower than neural signalling", which §17.1 does say —
  "endocrine signaling requires more time than neural signaling" — in a different paragraph, not
  quoted.
- **C38 `references[11]`, `[14]`, `[15]`, `[16]`.** Each parks a second sourced sentence in the note.

C36 does this too but always reproduces the extra sentence verbatim in the note, which is the best
practice of the four and the right model.

**Smallest fix.** Promote each note-held sentence into its own reference entry with its own `quote`
and locator. Roughly a dozen entries across the three records; no prose changes.

---

### 10. C37 — a `verified.note` makes a false statement about the source, which the same record's illustration contradicts

**Field.** `definition.references[6].verified.note`.

**The claim as the record makes it.**

> Section 14.2, which is the section on DNA structure, never uses the word gene at all.

**What the source actually says.** `openstax_biology_2e.txt`, §14.2 `NOT OBTAINED VERBATIM` note:

> The word "gene" occurs on the page only twice, both times in passing (the RUNX2 gene in a feature
> box, and "gene expression" in a note on histone research); the page defines neither.

And C37's own `illustration.body` says the same: "You will find it twice and neither one is a
definition." The note's substance (§14.2 defines no gene) is right; its absolute is wrong, and it is
wrong against a note the drafter demonstrably read.

**Smallest fix.** *Section 14.2 uses the word gene twice, both in passing, and defines it nowhere.*

---

### 11. C35 — a must-know point rests on a circulation fact neither the section nor its source pack supplies, and which E8 supplies three sections later

**Field.** `must_know[0]`.

**The claim as the record makes it.**

> A drug in the blood reaches nearly every organ, and that is not the same as acting on them.

**What the source actually says.** Nothing. All thirteen of C35's references are Biology 2e §§3.4,
4.1, 4.3, 5.1, 5.3 and 9.1 — cell structure, membrane, proteins, transport and signalling. None
mentions the circulation. The claim is sourced three sections later, in C38, from A&P §17.1
("Hormones are transported primarily via the bloodstream throughout the body"), which C38 duly
quotes. C35 has empty `concept_deps` and `ground_floor_deps`, so the reader has been given nothing to
build it from either. §10 rule 1: a section may assume everything before it and nothing after it.

**Smallest fix.** Recast the point so it turns on what C35 does establish — receptor specificity —
rather than on distribution: *A substance being present in a tissue is not the same as it acting
there. It acts where something binds it, so ask which cells carry the receptor before you accept any
claim about where a medicine works.* Or move the distribution half of the point into C38, which
already makes it (`must_know[1]`).

---

### 12. C37 — a broken sentence in a must-know point

**Field.** `must_know[7]`.

**The claim as the record makes it.**

> Made them separate on the page, the second and third are visibly unsupported.

This is not English. §11 rule 3 and §5's "one point, one paragraph, consequence inside the sentence"
both fail on it, and it is in the field §5 calls the one place meant to survive after the section is
forgotten.

**Smallest fix.** *Set out separately on the page, the second and third are visibly unsupported.*

---

## Minor

### 13. C35 — an uncited number, which the source itself declines to state as closed

**Field.** `simplified_explanation`.

> A protein is a chain. The links of the chain are called amino acids, and there are twenty kinds of
> link.

`openstax_biology_2e.txt` §3.4 carries the figure — "Different arrangements of the same 20 types of
amino acids comprise all proteins" — and then immediately qualifies it: "Two rare new amino acids
were discovered recently (selenocysteine and pyrrolysine), and additional new discoveries may be
added to the list." The record states it flat and cites nothing for it.

This is the only number in reader-facing prose in any of the four records, and because it sits in
`simplified_explanation` rather than in `illustration.numbers`, the numbers register cannot see it —
the register shows zero rows for all four. It is a count of a biochemical set rather than a measured
quantity, so it is not a §4 breach; it is a §8 one.

**Smallest fix.** Drop the count — *The links of the chain are called amino acids, and there is a
small fixed set of kinds* — or add the reference with the quote and carry the source's own
qualification.

### 14. C35 — a `boundary` point whose subject is the section

**Field.** `must_know[4]`.

> This section gives you no size, no speed and no dose. It tells you what can happen and never how
> much, so it can never settle whether an effect is large enough to matter.

§5: "a sentence whose subject is *this section* almost never passes it." This one survives on its
second clause, which is a genuine limit on what the reader may conclude — but it is framed as scope
and it is the only one of the four records' three boundary points that is. C36's and C38's both open
on a refusal ("Refuse any sum that…", "Refuse any argument that…") and are unambiguous.

**Smallest fix.** Open on the refusal, as its siblings do: *Refuse any claim that a mechanism settles
whether an effect is big enough to matter. A mechanism tells you what can happen and never how much,
and only measurement tells a real mechanism from one that changes an outcome.*

### 15. C35 — an unsourced detail in `analogy_breaks_when`

> …it is fluid, so the molecules in it slide about and proteins move within it.

Biology 2e §5.1 supports the fluid character ("gives the membrane a fluid character") but nowhere
says proteins move within it. **Fix:** cut the last clause, or cite §5.1's fluid-mosaic sentence.

### 16. C36 — "the last section but one" reads as two sections back

**Field.** `simplified_explanation`, first sentence.

> The last section but one gave you a cell and the small parts inside it.

C36 is sequence 36; the cell is sequence 35, immediately before it. On the ordinary reading, "the
last but one" is the penultimate — sequence 34, heat and temperature. Same family as defects 6 and
7, but ambiguous idiom rather than a plain mis-count. **Fix:** *The section on the cell gave you…*

### 17. C38 — an unsourced size comparison

**Field.** `simplified_explanation`.

> That makes it an organ of the same kind as the pancreas, doing a smaller version of the same thing.

A&P §17.1 says only "adipose tissue has long been known to produce hormones". Nothing in the pack
compares adipose endocrine output with the pancreas's, in scale or otherwise, and "a smaller version"
is a quantitative comparison in a record that closes by saying it carries no quantities. **Fix:** cut
"doing a smaller version of the same thing".

### 18. C38 — regain is named without the mechanism the section already holds

**Field.** `must_know[4]`.

> When weight comes back after it fell, the sentence to say names stores and signals. This section
> does not tell you which signals or by how much […]

This is the only mention of regain in the four records, and on §9's moral test it passes cleanly —
it explicitly refuses a sentence about the person's character. But §9 asks for regain "described as a
physiological outcome with a mechanism", and this names a mechanism *class* and then withdraws it.
The section has the mechanism: a store that fills under one signal and empties under another, running
in every person every day, which is the illustration's own closing line.

**Smallest fix.** *When weight comes back after it fell, say what the section has given you: a store
that fills under one signal and empties under another, running the same way in every person. This
section does not tell you which signals or by how much, and it never licenses a sentence about the
person's character.*

### 19. C37 — `quantitative` is out of field order

`quantitative: false` sits at line 512, between `exercises` and `retrieval_items`. The other three
records, and the schema example, put it after `review`. YAML-valid and harmless, and it is the
fingerprint of a session that stopped mid-write. **Fix:** move it.

### 20. C35 and C37 carry almost all of Part E's plain-language warnings

The build reports 11 warnings on C35 and 16 on C37, against **zero on C36** and one on C38 — and
C38's single warning is a quoted source sentence, so it is unavoidable. C37 holds both of the
corpus's two worst reading-grade breaches: `must_know[3]` at 12.0 and `must_know[0]` at 9.8, against
a limit of 9. Nothing else in Part E exceeds the limit. **Fix:** a §11 pass on C37's must-know
points, which is where every one of its grade failures sits.

### 21. C37 — pronoun drift in the teaching answer

The resident is "they" throughout, then: "That is not what **he** said and it is what she has taken
home." **Fix:** "That is not what they said".

### 22. C37 — synonym drift from E5

> The section before this one gave you a cell, its **outer skin**, the proteins in it…

C35 introduces the term as "the plasma membrane" and uses it consistently. §10 rule 2: a term is
introduced once and afterwards used in the same words. **Fix:** "its plasma membrane" — folded into
defect 6's fix.

---

## Checked and held

Recorded so nobody re-runs these.

**§4's number rule — the rule this audit most expected to catch, and it held.** Every number was
searched for, in digits and in words, across all four records and all reader-facing fields. No
percentage, no rate, no prevalence, no organ's share of energy expenditure, no ATP yield, no
concentration, no absorption fraction and no blood-glucose range appears anywhere. The numbers
register carries zero rows for all four. More than that, the four records **actively record the
refusals** in eleven separate `verified.note` entries, each naming the figure it declined and why:

- **C36 (5)** — the 40/60 split of catabolic energy between ATP and heat (§24.1), twice; the
  percentage absorption figures for lipid and protein (§23.7); the rate figure in the carbohydrate
  absorption paragraph (§23.7); the daily-litre volumes and the water and electrolyte percentages
  (§23.7); the "more than twice the energy per unit mass" claim (§24.3).
- **C38 (5)** — the daily volume and percentage absorption figures (§23.7); the liver's weight in
  pounds (§23.6); the bile-fragment diameter (§23.6); the alpha- and beta-cell islet percentages
  (§17.9); the 70–100 mg/dL blood-glucose range (§17.9), which the note correctly reclassifies as a
  clinical cut-point needing an instrument.
- **C37 (1)** — the helix's measured dimensions (§14.2).

C35 carries none, and needs none: the Biology 2e sections it cites contain almost no figures. The
widening of §4 has not been exploited here. The single number in reader-facing prose is C35's
"twenty kinds of link" (defect 13), which is a count of a biochemical set, not a measured quantity.

**No kilocalories-per-kilogram-of-body figure appears anywhere.** C36's `must_know[3]` and C33's
`must_know` and teaching answer all refuse it explicitly, by name, without stating it. C36's
illustration points at §24.7 as an instance of the figure and states no number. The refusal holds;
only its cross-reference and its stated reason are defective (defects 4 and 5).

**Nothing cites §24.7 for anything quantitative.** §24.7 appears in exactly one place across the four
records — C36's illustration, as a negative example — and carries no figure and no reference. C35,
C37 and C38 do not mention it. The defect is the missing audit trail and the incomplete reason, not a
quantitative citation.

**All 70 quotes verified.** Every `definition.references[].quote` in all four records was searched
for in the file `INDEX.yml` maps its citekey to, normalising whitespace and curly quotation marks.
All 70 are present verbatim. No reference is missing its `quote`. No citekey resolves to a
`do_not_cite` file. Beyond the support failures at defects 3 and 9, every quote says what it was
cited for.

**The inventory's deliberate cuts have held.** *Glycolysis*, *citric acid cycle*, *Krebs*, *electron
transport*, *oxidative phosphorylation*, *pyruvate*, *NADH*, *FADH* appear in reader-facing prose in
none of the four; the only occurrences are in C36's `references[8].verified.note`, which records them
as deliberately not used. *Acetyl CoA* occurs once, inside a source quote in the audit trail, never in
prose. *Enzyme kinetics* is absent entirely — C35 goes exactly as far as "Every enzyme speeds its
reaction up. That is as far as this book goes with enzymes, and it is enough." *Punnett square*,
*3:1* and *1:2:1* appear only in C37's `references[5].verified.note` as explicit non-use; the
illustration's three-row table states genotype-to-phenotype and computes no ratio. Mendel is named
once, for attribution, with no arithmetic attached.

**E6 and E8 do not re-teach E5, and all three dependants use E5's words.** C36 hands ATP back to the
reader as something already met; C38 refers the reader to "the section on the cell gave you a
membrane with a greasy middle and two wet faces", which is C35's exact phrasing, and to the receptor
and the shape change in C35's exact terms. Neither redefines the cell, the membrane, the protein or
the receptor. The only drift found is C37's "outer skin" (defect 22).

**§9 vocabulary is clean in all four.** Searched for *obese*, *overweight*, *cheat*, *indulge*,
*guilt*, *good/bad food*, *lazy*, *willpower*, *discipline*, *lapse*, *self-control*, *temptation*,
*before and after*, *blame*, *fault*, *defect*, *motivation*, *compliance*, *adherence*. Every hit is
either technical (a prediction that fails, a molecule that slips through) or explicitly corrective —
C37's `must_know[4]` exists precisely to forbid calling a variant "a defect or a fault", and C38's
illustration exists precisely to say "Neither one is a failure, and neither one is a success."
People-first construction holds throughout: C37's critique exercise says "living with obesity"; the
string "obese person" appears nowhere. No example in any of the four turns on a person's willpower.
There is no before-and-after framing in any field. C38's critique exercise dismantles a stigmatising
leaflet on exactly §9 grounds and names the word doing the damage.

**The two places §9 was most at risk both hold.** C36's `must_know[1]` — "Adipose tissue holds
triglyceride until it is needed. That is a job, in the same way that making bile is the liver's job"
— is the strongest §9 sentence in Part E and it is sourced, to §24.3's own closing "until they are
needed". C38's illustration closes on "The store filling and the store emptying are both the
mechanism working. Neither one is a failure, and neither one is a success", and its simplified
explanation carries "Neither half is the good half. A store that only ever filled would not be a
store." C37's fatalism risk is handled across four separate fields and a replacement sentence the
resident is made to say out loud. The only §9 weakness found is defect 18, and it is a
missing mechanism, not a moral framing.

**§5's admission test.** All 31 must-know points across the four records were tested. Every one names
something the reader would do, say, accept or refuse. The three `boundary` points in C36, C37 and
C38 all name a limit on what may be concluded, not the scope of the section; C36's and C38's open on
a refusal. No Part-A-style table-of-contents point was found. The single borderline is C35's
(defect 14), which is framed as scope and rescued by its second clause. Every record carries at
least one `misconception` and at least one `trap`, so none trips the build's warning.

**Flagged item 1 — "OpenStax A&P §17.1 never defines hormone."** **Confirmed as to the source; the
conclusion drawn from it is wrong.** §17.1 genuinely carries no definition sentence — the word
appears only as the appositive "which secrete chemicals—the hormone—into the extracellular fluid",
and the source file's own `[NOTE]` records the same. §17.2 is genuinely out of pack. But the drafter's
claim that E8 "was written to make only the claims §17.1 carries" is false: `definition.text` honours
it, and `simplified_explanation` then supplies a full definition anyway (defect 2). So: does the
result teach the reader what a hormone is? **Yes, and rather well** — the operational account in
`definition.text` (what secretes it, where it goes, what it does on arrival) plus the simplified
explanation's "it does not travel to a destination, it goes everywhere, it acts only where there is a
receptor shaped to hold it" is better teaching than a dictionary line would have been, and it sets up
the record's two best must-know points. The defect is not that the reader is under-taught. It is that
the sentence doing the teaching is unsourced, the audit trail says it does not exist, and the source
pack already held two usable definitions that nothing cites. The fix is one reference entry.

**Flagged item 2 — §24.2's missing uptake signal and §24.3's missing lipase.** **Both confirmed
deliberate, both recorded, and neither reads as a gap.** The insulin omission is recorded in C36
`references[14].verified.note`: "The paragraph also states that cells take up glucose in response to
insulin; insulin is taught in the next section and is deliberately not used here, because a section
may assume what is before it and nothing after it." The lipase omission is recorded in
`references[18].verified.note`: "The sentence before this one names the pancreatic lipases and the
bile salts as what breaks the triglyceride. The pancreas is established in the next section, so this
record states that fat is broken before it crosses and does not name what breaks it." Both notes
match the source exactly. **The prose does not limp.** "Triglycerides are broken into free fatty
acids, which cross the intestinal membrane" is an ordinary agentless passive that no reader will
stumble on; "A cell that takes glucose in breaks it down and makes coins" makes no claim about what
lets it in. Both omissions are then repaired in C38, which supplies insulin's uptake mechanism in
full and supplies bile and pancreatic juice as what takes fat apart. **One recommendation, not a
defect:** neither omission is signalled anywhere above the individual reference note, so an auditor
who reads `definition.text` and `simplified_explanation` and then goes looking would have to dig for
them. One line in the Part E handover naming both, and a half-clause in C38 saying that this is where
the thing E6 left unnamed gets its name, would close the loop for nothing.

**Flagged item 3 — §24.7.** **Confirmed: nothing in any of the four records cites §24.7 for anything
quantitative.** See defect 5 for the two things that are wrong about how C36 handles it, and for the
three places the do-not-cite note should live. The substantive point for whoever writes that note:
§24.7's defect is not that its 3,500-calorie figure is unsourced. It is that the page compounds the
figure into a linear extrapolation — one pound every 18 days, 20 pounds a year — and that
extrapolation is refused by this course whatever evidence is produced for it. A note that says only
"not usable for any number", which is what `sources/SOURCES.md` currently says, does not carry that
and would not stop a future drafter who found a study.

---

## Are C35 and C37 in worse shape than C36 and C38?

**Yes, and measurably, and C37 is the worst record of the four by a clear margin.**

| Record | Reviewed by its drafter | Blocking | Major | Minor | Build warnings |
| --- | --- | ---: | ---: | ---: | ---: |
| C35 (E5) | **no** | 0 | 2 | 3 | 11 |
| C36 (E6) | yes | 0 | 2 | 1 | **0** |
| C37 (E7) | **no** | 2 | 5 | 4 | 16 |
| C38 (E8) | yes | 1 | 2 | 2 | 1 (a source quote) |

Defect 9 spans C35, C37 and C38 and defect 20 spans C35 and C37, so the columns count more than the
22 numbered items.

C37 carries two of the three blocking defects, five of the nine major ones, both of the corpus's two
reading-grade breaches, the only broken sentence, the only false statement in an audit trail, the
only forward use of a term of art, and a mis-numbered opening. C35 is cleaner in substance than its
warning count suggests — its sourcing is careful and its `verified` notes are honest and useful — but
it holds the only uncited number in the four and the only must-know point resting on a fact its
section does not have.

C36 is the strongest record in Part E and should be the model for the fixes: it is the only one of
the four that reproduces every note-held sentence verbatim, the only one with zero build warnings,
and the only one whose illustration is built on a source failure it also records in its references.
Its two defects are both in one paragraph of one field.

C38 is close behind C36 on sourcing and is the best of the four on §9, and its one blocking defect is
a self-contradiction with a free fix.

The pattern is consistent with what the brief predicted: the two records nobody looked at fail in the
ways a drafter catches on their own second pass — a first sentence that names the wrong section, a
note that contradicts the illustration two fields below it, a definition that slipped into the
simplified explanation after the definition field had carefully refused it, and a sentence left
half-written.
