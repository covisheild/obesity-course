# B0-R0-C41 (F3, Checking a reference): compression-pass holes, audit triage

Auditor: Opus, Task 3. Checked against sources/constitution_current.txt (citekey `constitution`).

1. **C41-K1**. Class: NEW, CONFIRMED-ERROR, **recurring** (SELFCHECK 1 and 3). Field: illustration.body.
   Sentence: "The Council is the body that sets goods and services tax rates."
   What is wrong: the Council recommends rates. It does not set them. The sentence also has no citekey.
   Fix: "The Council is the body that recommends goods and services tax rates to the Union and the States." Cite `constitution`, Article 279A(4).
   Support: constitution_current.txt, Art. 279A(4): "The Goods and Services Tax Council shall make recommendations to the Union and the States on— … (e) the rates including floor rates with bands of goods and services tax".
   Fix: sentence now reads "recommends goods and services tax rates to the Union and the States (Constitution of India, Article 279A(4))"; added a `constitution` reference, locator Article 279A(4)(e), with the clause (4) quote (build found it).
   Verify: closed

2. **C41-K2**. Class: CONFIRMED-GAP. Fields: illustration.body and exercises[0].answer. This blocks Ex 1.
   Sentence: "A second copy sits on the same website, marked as up to date, and that one does hold Article 279A."
   What is wrong: the worked check stops at act three. Act four, reading the passage, is never done, so the claim is never settled. The Ex 1 answer ("To settle it: … search it for Article 279A") also stops at locating, which the section says is not enough.
   Fix: add to the illustration: "Fourth, read it. Article 279A(1) says the President 'shall … by order, constitute a Council to be called the Goods and Services Tax Council.' So the claim holds, with one correction that only reading could give you. The Article does not set up the Council itself. It requires the President to, by order." Add to the Ex 1 answer: "Then read clause (1), and check that it says what the draft claims."
   Support: held. constitution_current.txt, Art. 279A(1), quoted above.
   Fix: added the fourth act to the illustration (reads clause (1), quoting "shall ... by order, constitute a Council", split into two sentences to clear the sentence-length warning) and the correction that the President constitutes the Council by order; added "Then read clause (1), and check that it says what the draft claims." to the Ex 1 answer. Added a `constitution` reference, Article 279A(1), with its quote.
   Verify: closed

3. **C41-K3**. Class: CONFIRMED-GAP. Field: illustration.body.
   Sentence: "Article 279A was written into the Constitution in 2016, thirteen years after that."
   What is wrong: the diagnosis rests on this date, and the reader is not told how to find it.
   Fix: "The up-to-date copy says when, in the footnote under the Article: 'Ins. by the Constitution (One Hundred and First Amendment) Act, 2016'." Cite `constitution`.
   Support: held. constitution_current.txt, the footnote to 279A: "Ins. by the Constitution (One Hundred and First Amendment) Act, 2016, s. 12 (w.e.f. 12-9-2016)."
   Fix: added the footnote sentence quoting "Ins. by the Constitution (One Hundred and First Amendment) Act, 2016", with a gloss "Ins." means inserted; added a `constitution` reference, locator Article 279A footnote 1, with its quote.
   Verify: closed

4. **C41-K4**. Class: CONFIRMED-GAP (the cold reader called it an ERROR; downgraded here). Field: illustration.analogy_breaks_when.
   Sentence: "An old copy can pass finding, confirming and locating, then fail at reading."
   What is wrong: as the text now stands, this is true in general: an article that exists but has since been amended passes locating. But the only example in the section, the old copy, failed at locating. The original's contradicting sentence ("That is exactly what happened above") was cut, yet the reader still links the two.
   Fix: add: "That happens when the article was there but has since been amended. Above, the Article did not yet exist in the old copy, so it failed earlier, at locating."
   Source: none needed.
   Fix: added the two sentences as given, as a separate paragraph of analogy_breaks_when.
   Verify: closed

5. **C41-K5**. Class: CONFIRMED-GAP. Fields: illustration.analogy_breaks_when, compared with definition.text and retrieval_items[2].
   Sentence: "For a law there is a fifth question the four acts never ask on their own: is this copy up to date?"
   What is wrong: four acts or five? And where does the currency check go? The section never settles it. In the illustration it does the work of act two.
   Fix: "It belongs with the second act. The source named is the law as it now stands, and an outdated copy is not that source." (If Harsh prefers a separate fifth act, say where it sits in the order.)
   Source: none needed.
   Fix: added "It is not a fifth act. It belongs with the second act. The source named is the law as it now stands, and an outdated copy is not that source." (Harsh may still prefer a separate fifth act.)
   Verify: open, because the added sentences contradict the next paragraph of analogy_breaks_when: if currency belongs with the second act and 'an outdated copy is not that source', an old copy cannot 'pass finding, confirming and locating', and the K4 line 'it failed earlier, at locating' should then say it failed at confirming (the illustration's act two also says 'Nothing looks wrong yet'). The two fixes need reconciling, or Harsh's choice of a separate fifth act.

6. **C41-K6**. Class: NEW (minor), **recurring** (SELFCHECK 7). Field: retrieval_items.
   Sentences: "Resolve the pointer, confirm the object is what is named…"; "They stop at resolving…"; "Is this version current…"
   What is wrong: the retrieval answers use "resolve", "object" and "version". The text says "find", "source" and "copy".
   Fix: "Find the source, confirm it is the source named, find the exact passage, read whether it supports the claim." "They stop at finding." "Is this copy up to date?"
   Fix: retrieval answers now say "Find the source, confirm it is the source named, find the exact passage, ...", "They stop at finding", and "Is this copy up to date, or has the law been amended since?"
   Verify: closed


## Round 2 (23 Sep 2026)

- **C41-R2a** · reopens C41-K5 (verifier): the new line says an out-of-date copy fails at act two; the next paragraph still says an old copy can pass that act and that the example failed at act three. Reconcile so the section says one thing throughout, keeping the up-to-date check inside act two (Harsh did not ask for a fifth act).

- **C41-R2b** · HARSH DECISION (23 Sep): Exercise 2's 'something you have written' becomes 'a paper, report or guideline you have to hand'. Adjust its answer to match.
