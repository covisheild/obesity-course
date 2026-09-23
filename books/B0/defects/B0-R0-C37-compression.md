# Compression-pass holes, triaged · B0-R0-C37 (E7)

Auditor: Task 3, fresh context. Full per-hole verdicts: `books/B0/compress/TRIAGE-part-E.md`.

---

**C37-K1** · CONFIRMED-GAP
- **Field:** `simplified_explanation` (and `definition.text`)
- **Sentences:** "Genes are carried on chromosomes." (definition only) / plain: "You get two copies of each chromosome … So you carry two copies of each gene, not one."
- **What is wrong:** the plain terms never say that genes sit on chromosomes, so the "So" does not follow for a reader of that layer. Chromosome is never described. The reference note says the plain words given for it are "a thing that carries its genes in a fixed order along it", but those words are no longer in the text. How gene and DNA relate is never stated, although a held sentence gives it.
- **Fix:** before "You get two copies…", add: "Genes sit along structures called chromosomes, in a fixed order. The information a gene carries is written in the DNA: the cell turns the information in its DNA into the order of amino acids in a protein." This defines the relation without claiming what a gene physically is, so the illustration's point about 14.2 stands.
- **Support:** held. Biology 2e §12.2: "Physical characteristics are expressed through genes carried on chromosomes." and "Each pair of homologous chromosomes has the same linear order of genes." Biology 2e §9.1 (quoted in the record): "Gene expression is the cellular process of transforming the information in a cell's DNA into a sequence of amino acids".
- Fix: added the auditor's two sentences as their own paragraph before "You get two copies…" in the plain terms; updated the 12.2 linear-order reference note to match the new plain words. Definition already said genes are carried on chromosomes, left as is.
Verify: closed

**C37-K2** · CONFIRMED-ERROR (scope misstated)
- **Field:** `definition.text`, `simplified_explanation`
- **Sentences:** "Everything above describes the case in which a single gene controls a single characteristic." / "Everything above is about one gene controlling one characteristic."
- **What is wrong:** "everything above" includes the structure of DNA, base pairing and copying. None of that is a single-gene case claim, and the source's "For cases in which a single gene controls a single characteristic" introduces alleles and dominance only. Dominance is also absent from the definition, so there the sentence points at nothing single-gene except alleles, genotype and phenotype.
- **Fix:** definition: "The account of alleles, genotype and phenotype above describes the case in which a single gene controls a single characteristic." Plain terms: "The dominant-and-recessive picture is about one gene controlling one characteristic."
- **Support:** held. Biology 2e §12.2: "For cases in which a single gene controls a single characteristic".
- Fix: replaced both sentences with the auditor's wording (definition rewrapped).
Verify: closed

**C37-K3** · CONFIRMED-GAP
- **Field:** `simplified_explanation`
- **Sentence:** "Inside, it lands on a receptor, exactly as the section on the cell showed you. The receptor then sets the making of a protein going."
- **What is wrong:** E5 showed an internal receptor binding a ligand. It never showed a receptor starting protein-making. "Exactly as" makes the new step read as revision.
- **Fix:** "Inside, it lands on a receptor, as the section on the cell showed you. What is new here is what some of these receptors then do: they set the making of a protein going."
- **Support:** held. Biology 2e §9.1 (in the record): "many of these molecules bind to proteins that act as regulators of mRNA synthesis (transcription) to mediate gene expression".
- Fix: replaced with the auditor's wording ("as the section on the cell showed you. What is new here is what some of these receptors then do: they set the making of a protein going.").
Verify: closed

**C37-K4** · CONFIRMED-GAP
- **Field:** `simplified_explanation`
- **Sentence:** "…and it is how a copy gets into an egg and a sperm." against "You get two copies of each chromosome, one from your mother and one from your father."
- **What is wrong:** it never says that an egg or a sperm carries one copy of each chromosome, not two. Read literally, each parent passes on "a copy" of everything they hold and the child would have four.
- **Fix:** after "…one from your father." add: "An egg or a sperm carries only one copy of each chromosome, so when they join, the child has two."
- **Support:** held. Biology 2e §12.2, the same paragraph as the record's diploid quote: "Diploid organisms produce haploid gametes, which contain one copy of each homologous chromosome that unite at fertilization to create a diploid zygote." Add it as a reference.
- Fix: added the sentence after "…one from your father." and added the gametes sentence as a new 12.2 reference (quote confirmed in the held source).
Verify: closed
