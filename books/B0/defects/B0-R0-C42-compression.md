# B0-R0-C42 (F4, Argument): compression-pass holes, audit triage

Auditor: Opus, Task 3. This record has no held source (pending_logic_text, not obtained).

1. **C42-K1**. Class: CONFIRMED-GAP. Fields: simplified_explanation and illustration.body. Ex 1, Ex 2 and must_know[3] all depend on it.
   Sentences: "It does not." must_know[3]: "Grant every premise aloud, then show the conclusion still does not follow."
   What is wrong: no general way of showing that an inference fails is taught. The illustration points at the "chosen" / "freely chosen" swap, but the reader is never given a method they can reuse. The Ex 1 answer also relies on two ideas that appear nowhere in A to F. One is a common cause moving both things. The other is that a pattern in country averages need not hold for people.
   Fix: add to simplified_explanation: "To show an inference fails, describe a case where every premise is true and the conclusion is false. If you can, the inference does not carry." Add to the illustration: "Picture a person who eats more than they use, and who chooses what to eat, but chooses from what is cheap and on the nearest shelf. Both premises hold, and 'a matter of personal choice' does not." For Ex 1, either add one sentence ("Two things that move together may both be moved by a third, and a pattern across countries need not hold for the people in them") or point to F3's "two things move together" line, and add B0-R0-C41 to concept_deps.
   Source: none needed (logic).
   Fix: added the counterexample method (two sentences) to simplified_explanation; added the cheap-nearest-shelf case to illustration.body; added "Two things that move together may both be moved by a third. And a pattern across countries need not hold for the people in them." to simplified_explanation, so Ex 1 rests on taught ideas. concept_deps left unchanged (the pointer option was not used).
   Verify: closed

2. **C42-K2**. Class: CONFIRMED-GAP, unsupported claim, **recurring** (SELFCHECK 3 and 4). Field: must_know[2] (india_deviation).
   Sentence: "In Indian food policy debate, the commonest unspoken premise is that people already know what is in their food."
   What is wrong: "commonest" is an empirical claim about the debate. It has no citekey, no source is held, and no example argument shows where the premise hides.
   Fix: reword so it is not a ranking: "A premise that often goes unspoken in Indian food policy debate is that people already know what is in their food. Look for it in any argument that leaves the choice to the buyer." Or cite a source (none held).
   Fix: must_know[2] reworded to "In Indian food policy debate, look for an unspoken premise that people already know what is in their food. Check for it in any argument that leaves the choice to the buyer." No ranking or frequency is asserted, so no source is needed.
   Verify: closed
