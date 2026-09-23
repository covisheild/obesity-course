# Compression-pass holes, triaged · B0-R0-C38 (E8)

Auditor: Task 3, fresh context. Full per-hole verdicts: `books/B0/compress/TRIAGE-part-E.md`.

## What the held OpenStax source actually says (A&P 2e §17.9, `sources/openstax_anatphys_2e.txt` lines 296–300)

> "The primary function of insulin is to facilitate the uptake of glucose into body cells. Red blood cells, as well as cells of the brain, liver, kidneys, and the lining of the small intestine, do not have insulin receptors on their cell membranes and do not require insulin for glucose uptake. Although all other body cells do require insulin if they are to take glucose from the bloodstream, skeletal muscle cells and adipose cells are the primary targets of insulin."

> "Insulin triggers the rapid movement of a pool of glucose transporter vesicles to the cell membrane, where they fuse and expose the glucose transporters to the extracellular fluid. The transporters then move glucose by facilitated diffusion into the cell interior."

> "Insulin also reduces blood glucose levels by stimulating glycolysis, the metabolism of glucose for generation of ATP. Moreover, it stimulates the liver to convert excess glucose into glycogen for storage, and it inhibits enzymes involved in glycogenolysis and gluconeogenesis."

So the held source makes two claims about the liver, and they cannot both hold: (1) no insulin receptors on the cell membrane, and (2) insulin stimulates the liver's glycogen storage and inhibits its glycogenolysis and gluconeogenesis. The source names no transporter type (no "GLUT"). It says only "glucose transporters", and only for the insulin-driven mechanism. The one statement it supports without internal conflict is the second half of the sentence: these cells "do not require insulin for glucose uptake". That liver cells in fact carry insulin receptors is domain knowledge. It was not checked against a held source, and no web fetch was made.

---

**C38-K1** · CONFIRMED-ERROR (serious; contradicts the record and the source's own next paragraph)
- **Field:** `simplified_explanation`, `must_know[0]`, `exercises[2]` answer, `retrieval_items[3]`, `illustration.body`
- **Sentences:** "Neither do red blood cells, the liver, the kidneys or the lining of the gut. They carry no insulin receptors at all, and they take glucose straight out of the blood." / must_know[0]: "The brain, the liver, the kidneys, red blood cells and the lining of the gut carry no insulin receptors and take glucose without it." / teaching answer: "carry no insulin receptors. They need no insulin to take glucose in." / "only one of them has a lock" / retrieval[3]: "…have no insulin receptors and take glucose without it."
- **What is wrong:** the same record says "Insulin also stimulates the liver to convert excess glucose into glycogen for storage" (definition) and "The liver packs spare sugar away as glycogen" (illustration, under insulin). It also states the rule "It does something only where there is a receptor shaped to hold it." Under the record's own rule, a liver with no insulin receptors could not respond to insulin. The receptor claim is also false for the liver (domain knowledge; see above).
- **Fix:** in every reader-facing sentence, replace the receptor claim with the uptake claim the source supports cleanly. Plain terms: "The brain does not need insulin to take glucose in. Neither do red blood cells, the liver, the kidneys or the lining of the gut. They take glucose out of the blood whether insulin is there or not." must_know[0]: "…do not need insulin to take glucose in. So make any claim about insulin name its tissue, and say whether it is about uptake or about something else." Teaching answer: "They need no insulin to take glucose in. The liver still answers to insulin in other ways: insulin makes it store glycogen." Change "only one of them has a lock" to "only one of them needs the key to let sugar in". In the illustration, keep the quote and add after "The brain is on it. So is the liver.": "Read to the end of the sentence: 'do not require insulin for glucose uptake'. That is the half to keep. The same page says insulin makes the liver store glycogen, so the liver is not deaf to insulin. What it does not need insulin for is taking glucose in." `analogy_breaks_when` already has "The brain not needing insulin does not mean the brain is untouched by insulin" — extend it to "the brain or the liver".
- **Support:** held, A&P §17.9 lines 296 and 300 as quoted above. Harsh may prefer to drop "liver" from the list altogether instead of adding the caveat. Either works. The caveat keeps the quote verbatim.
- Fix: receptor claim replaced by the uptake claim in simplified_explanation, must_know[0] (now also asks uptake-or-else), teaching answer ("Ask whether the brain needs insulin to take glucose in", a liver-still-answers-to-insulin line, "needs the key to let sugar in") and retrieval[3]; illustration keeps the quote and adds the read-to-the-end paragraph; analogy_breaks_when now says "the brain or the liver". Liver kept in the list.

**C38-K2** · CONFIRMED-ERROR
- **Field:** `simplified_explanation`
- **Sentence:** "Glucagon does the opposite job in the same places."
- **What is wrong:** the sentence before names the places as "Muscle cells and fat cells are the ones insulin acts on most". The sentences after send glucagon to the liver. The held source gives glucagon three actions: liver glycogen to glucose, liver amino acids to glucose, and lipolysis. Nothing is said about muscle. So "the same places" is false as read.
- **Fix:** "Glucagon runs the other way, and mostly at the liver."
- **Support:** held. A&P §17.9: "It stimulates the liver to convert its stores of glycogen back into glucose." / "It stimulates the liver to take up amino acids from the blood and convert them into glucose." / "It stimulates lipolysis…"
- Fix: sentence now reads "Glucagon runs the other way, and mostly at the liver."

**C38-K3** · CONFIRMED-ERROR (minor; internal)
- **Field:** `simplified_explanation`
- **Sentences:** "It is covered in tiny fingers, and the pieces cross into the blood vessels inside those fingers." then "Whatever dissolves in fat takes a different road and joins the blood further along." and "Every drop of blood leaving the gut goes through the liver…"
- **What is wrong:** the first sentence sends every piece into blood vessels, which contradicts the fat route (lacteals, which are lymph vessels) given in the definition. The fat route is never named as lymph, so "every drop of blood … goes through the liver" and "fat reaches the rest of the body before the liver" reconcile only if the reader already knows that lymph is not blood.
- **Fix:** "…and the pieces cross into the vessels inside those fingers." Then: "Whatever dissolves in fat goes into a different set of vessels, the lymph vessels, which empty into the blood further along, past the liver."
- **Support:** held. A&P §23.7: "…enter the lacteals of the villi to be transported by lymphatic vessels to the systemic circulation via the thoracic duct". A&P §24.3: "Chylomicrons … enter the lymphatic system via lacteals in the villi of the intestine. From the lymphatic system, the chylomicrons are transported to the circulatory system."
- Fix: "cross into the vessels inside those fingers"; fat route now named as lymph vessels that empty into the blood further along, past the liver.

**C38-K4** · CONFIRMED-GAP
- **Field:** `definition.text`, `retrieval_items[0]`
- **Terms:** villi, capillary, hepatic portal vein, lacteals, lymphatic vessels, general circulation.
- **What is wrong:** none is defined. The plain terms use "tiny fingers" and "a different road" and never attach the words, yet retrieval[0] answers with "hepatic portal circulation" and "general circulation".
- **Fix:** attach the words in the plain layer: "tiny fingers, called villi", "the smallest blood vessels (capillaries)", "that blood runs straight to the liver, along a vein called the hepatic portal vein", "the lymph vessels (in the villi they are called lacteals)", "the general circulation, the blood that goes round the whole body".
- **Support:** held, the same A&P 23.7 quotes. No new claim is made.
- Fix: villi, capillaries, hepatic portal vein, lacteals, lymph vessels, general circulation and hepatic portal circulation attached in the plain layer; short glosses added in definition.text.

**C38-K5** · CONFIRMED-GAP (minor)
- **Field:** `definition.text`, `retrieval_items[0]` and `[2]`
- **Terms:** "alimentary canal", "duodenum".
- **Fix:** "alimentary canal (the gut tube from mouth to anus)". For duodenum: "the first part of the small intestine". No held sentence defines the duodenum, so either add a source or replace it in reader-facing answers with "the small intestine".
- **Support:** partly held. Nothing held for the duodenum.
- Fix: "Its proper name is the alimentary canal" in plain layer and "(the gut tube)" in definition (no "mouth to anus": not in a held source). Duodenum replaced by "the small intestine" in definition.text (bile and pancreatic juice) and retrieval[2], since no held sentence defines it; reference quotes keep "duodenum" verbatim.

**C38-K6** · CONFIRMED-GAP (minor)
- **Field:** `definition.text`
- **Terms:** "extracellular fluid", "interstitial fluid".
- **Fix:** plain terms: "The gland lets it out into the fluid around its own cells, called the extracellular fluid. The part of it between cells is the interstitial fluid."
- **Support:** held. A&P §17.1 (in the record): "The interstitial fluid and the blood vessels then transport the hormones throughout the body."
- Fix: plain layer names the fluid around the gland's cells "the extracellular fluid" (also glossed in definition) and says "the interstitial fluid and the blood carry it on", dropping the unsourced "drains into the blood". Interstitial fluid is named but not defined as "between cells": no held sentence defines it.

**C38-N1** · NEW · CONFIRMED-GAP
- **Field:** `exercises[0]` answer
- **Sentence:** "It also makes bile, which breaks large blobs of fat into tiny ones."
- **What is wrong:** what bile does is in the references only. Neither the definition nor the plain terms say it, so the model answer asks for something the section did not teach.
- **Fix:** plain terms: "And it makes bile, which it sends down into the gut, where it breaks large blobs of fat into tiny ones."
- **Support:** held. A&P §23.6 (in the record): "Bile is a mixture secreted by the liver to accomplish the emulsification of lipids in the small intestine." and "This results in the large lipid globules being pulled apart into many tiny lipid fragments".
- Fix: plain layer now says bile is sent into the gut, "where it breaks large blobs of fat into tiny ones".

**C38-N2** · NEW · CONFIRMED-ERROR (minor, support)
- **Field:** `simplified_explanation`
- **Sentence:** "Muscle and fat wait for insulin. The brain does not, and it takes what it needs first."
- **What is wrong:** "first" asserts an order of priority between tissues. No held sentence carries it. The source says only that the brain does not require insulin for uptake and can use only glucose.
- **Fix:** "…The brain does not wait."
- **Support:** held. A&P §17.9 and §24.2 as quoted in the record carry no priority claim.
- Fix: now "Muscle and fat wait for insulin. The brain does not wait."
