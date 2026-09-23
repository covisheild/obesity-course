# B0-R0-C43 (F5, How government works): compression-pass holes, audit triage

Auditor: Opus, Task 3. Checked against sources/fss_act_2006.txt (citekey `fss_act_2006`), sources/constitution_current.txt (`constitution`) and sources/fssai_labelling_2020.txt.

1. **C43-K1**. Class: CONFIRMED-ERROR (the record contradicts itself), **recurring** (SELFCHECK 7). Field: illustration.body.
   Sentence: "The detail sits in a regulation — a rule written by a body, not by Parliament."
   What is wrong: definition.text separates the two: "The Central Government may make rules. A body that the statute creates may make regulations." The gloss then calls a regulation "a rule".
   Fix: "The detail sits in a regulation — an instrument written by a body the statute set up, not by Parliament."
   Support: FSS Act s.3(zj): "'prescribed' means prescribed by rules made by the Central Government or the State Government". s.92(1): "The Food Authority may … make regulations".
   Fix: illustration.body now reads "an instrument written by a body the statute set up, not by Parliament".
   Verify: closed

2. **C43-K2**. Class: CONFIRMED-ERROR. Field: must_know[0]. Ex 3 depends on it.
   Sentence: "A regulation needs a meeting and a notification in the Gazette — the government's official newspaper."
   What is wrong: the Act does not ask for "a meeting". It asks for the Central Government's prior approval, prior publication of a draft, and notification. Every regulation is then laid before Parliament. The Ex 3 answer ("drafting an amendment, taking comments, notifying it in the Gazette and laying it before Parliament") relies on steps the text never gives. Ex 3's "next week" needs only these steps; no timescale is needed.
   Fix: "A statute needs a legislature and a debate. A regulation under the Food Safety and Standards Act needs a draft published for comment, the Central Government's approval and a notification in the Gazette (the government's official newspaper). It is then laid before Parliament." Cite `fss_act_2006`, ss. 92(1) and 93.
   Support: s.92(1): "The Food Authority may, with the previous approval of the Central Government and after previous publication, by notification, make regulations". s.93: "Every rule and every regulation made under this Act shall be laid, as soon as may be after it is made, before each House of Parliament".
   Fix: must_know[0] replaced with the draft-for-comment / Central Government approval / Gazette / laid before Parliament wording, refs fss_act_2006; Ex 3 answer changed to the same steps; s.92(1) and s.93 quotes added as definition references.
   Verify: open, because 'a draft published for comment' (must_know[0]) and 'publishing a draft amendment for comment' (Ex 3 answer) go beyond the cited s.92(1), which says only 'after previous publication'; nothing in fss_act_2006.txt mentions comments, objections or suggestions. Either drop 'for comment' or cite a held source for it (General Clauses Act s.23 is not held). The rest of the defect is gone and the s.92(1) and s.93 quotes match the source.

3. **C43-K3**. Class: CONFIRMED-GAP. Field: must_know[1].
   Sentence: "Four levels, hardest to easiest to change: the Constitution, a statute, a rule or regulation, a notification."
   What is wrong: "notification" is used in two senses. In must_know[0] it is the act of publishing. Here it is the lowest instrument, and that sense is never defined. "A rule or regulation" can also be read as two levels, which makes five.
   Fix: "…a rule or a regulation (one level), and a notification: an order the government issues under a power a statute gives it, which takes effect when published in the Gazette."
   Support: held. FSS Act s.3(zg): "'notification' means a notification published in the Official Gazette". Example of such an order, s.3(1)(j) proviso: "the Central Government may declare, by notification in the Official Gazette, any other article as food".
   Fix: must_know[1] now says "a rule or a regulation (one level)" and defines a notification as an order issued under a power a statute gives, published in the Gazette ("takes effect when published" not asserted); s.3(1)(zg) and s.3(1)(j) proviso quotes added; Ex 1 answer says a notification is issued by whoever the statute gave that power to.
   Verify: closed

4. **C43-K4**. Class: CONFIRMED-GAP. Field: must_know[1] or simplified_explanation. This blocks Ex 1 for two of the four levels.
   Sentence: Ex 1 prompt: "For each, say who is able to change it."
   What is wrong: the text never says who amends the Constitution, or why it is the hardest. It never says who issues a notification. The Ex 1 answer supplies both.
   Fix: "Parliament amends the Constitution only by a special majority in each House. Changes to some parts, among them the Seventh Schedule's lists, must also be ratified by at least half the State Legislatures." The notification half is closed by K3. Cite `constitution`, Art. 368(2).
   Support: held. Art. 368(2): "passed in each House by a majority of the total membership of that House and by a majority of not less than two-thirds of the members of that House present and voting", and the proviso: "(c) any of the Lists in the Seventh Schedule … the amendment shall also require to be ratified by the Legislatures of not less than one-half of the States".
   Fix: simplified_explanation gains a paragraph on amendment by special majority (defined) plus ratification by at least half the State Legislatures for some parts incl. the Seventh Schedule lists; three Art. 368(2) quotes added as constitution references (the proviso is split by a page break in the source, so quoted in three pieces).
   Verify: closed

5. **C43-K5**. Class: CONFIRMED-GAP. Field: definition.text.
   Sentences: "In India the Constitution divides the power to make law from the power to apply it." Compare simplified_explanation: "Three different jobs, done by three different sets of people."
   What is wrong: the definition counts two powers and never mentions the courts, yet it cites Articles 32 and 226 (the courts' writ powers) as a locator. The simplified explanation counts three.
   Fix: add to the definition: "The courts read statutes and decide whether the executive has acted within them."
   Support: already in the record's locator (Arts. 32 and 226, constitution_current.txt).
   Fix: definition.text gains "The courts read statutes and decide whether the executive has acted within them."
   Verify: closed

6. **C43-K6**. Class: CONFIRMED-GAP, unsupported claim, **recurring** (SELFCHECK 3). Fields: illustration.analogy_breaks_when and must_know[5].
   Sentence: "Some of the largest programmes shaping health in India rest on nothing but an executive decision and a budget line."
   What is wrong: this is a claim about the world with no example and no citekey, so the reader cannot check it.
   Fix: name one programme and cite the scheme document that shows it has no statutory basis (not held; would need fetching). Or drop "largest" and say plainly that it is a possibility to check: "A programme may rest on nothing but an executive decision and a budget line. Look for the statute; if there is none, that is what it rests on."
   Source: none held.
   Fix: took the second option. analogy_breaks_when drops "largest" and says a programme may rest on a decision and budget line, and to look for the statute; must_know[5] rewritten as "Before relying on a programme, look for the statute behind it...". No programme named, no new claim about the world.
   Verify: closed

7. **C43-K7**. Class: CONFIRMED-GAP. Field: must_know[2].
   Sentence: "Before repeating a label rule to anyone, open the regulation itself."
   What is wrong: the regulation is never named. B4 (B0-R0-C12) named it, but the text leaves the reader to make that link.
   Fix: add: "For the energy figure, that is regulation 5(3)(b) of the Food Safety and Standards (Labelling and Display) Regulations, 2020, which the section on energy units used." Add B0-R0-C12 to concept_deps.
   Support: held (fssai_labelling_2020). B4-released line 16.
   Fix: sentence added to must_know[2] as proposed (refs fss_act_2006, fssai_labelling_2020); B0-R0-C12 added to concept_deps; reg 5(3)(b) quote "(i) energy value (kcal);" added as a reference.
   Verify: closed

8. **C43-K8**. Class: CONFIRMED-GAP (minor). Field: definition.text.
   Sentence: "Parliament and the State Legislatures enact statutes."
   What is wrong: A to E say "Act" throughout, and the illustration says "the Act". Nothing says an Act is a statute, or what the Constitution is.
   Fix: "Parliament and the State Legislatures enact statutes, each called an Act. The Constitution is the founding law that every statute must fit."
   Source: none needed.
   Fix: definition.text now reads "...enact statutes, each called an Act. The Constitution is the founding law that every statute must fit."
   Verify: closed

9. **C43-K9**. Class: NEW, CONFIRMED-ERROR, **recurring** (SELFCHECK 1 and 3). Fields: illustration.body and references.
   Sentences: "Now read section 23(1) of the Act. It says no one may sell a packaged food that is not labelled 'in the manner as may be specified by regulations'." "Section 4 sets up the body…" "Section 92 gives that body the power to make regulations."
   What is wrong: three claims about the FSS Act, one of them a direct quote, carry no citekey. The record's only reference is `constitution`. The source is held, and the claims are accurate.
   Fix: add a `fss_act_2006` reference with these quotes. s.23(1): "any packaged food products which are not marked and labelled in the manner as may be specified by regulations". s.4(1): "The Central Government shall, by notification, establish a body to be known as the Food Safety and Standards Authority of India". s.92(1): "The Food Authority may, with the previous approval of the Central Government and after previous publication, by notification, make regulations".
   Fix: fss_act_2006 references added to definition.references for s.4(1), s.23(1) and s.92(1) (plus s.93, s.3(1)(zg), s.3(1)(zj), s.3(1)(j) proviso), each quote found by the build.
   Verify: closed


## Round 2 (23 Sep 2026)

- **C43-R2a** · reopens C43-K2 (verifier): 'published for comment' goes beyond s.92(1), which says only 'after previous publication'. Drop 'for comment' (no source for it is held); keep the rest. Check the Ex 1 and Ex 3 answers for the same phrase.
