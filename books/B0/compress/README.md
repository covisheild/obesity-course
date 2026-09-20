# The compression pass on Part A · working files

Run 20 September 2026, all three steps in one task, per `claude.md` §12 and `PIPELINE.md` Task 5.
Kept so the pass can be audited rather than believed.

| File | What it is |
| --- | --- |
| `<SEC>-prose.yml` | the five reader-facing prose fields, extracted from the record |
| `<SEC>-original.md` | the section as the booklet prints it — what step 5a read |
| `<SEC>-pass1-prose.yml` | step 5a's cut |
| `<SEC>-pass1.md` | the cut section, assembled — what went into the scratch directory |
| `COLDREAD-REPORT.md` | step 5b's gap report |
| `RESTORE.yml` | step 5c's decisions, each keyed to the gap that justifies it |
| `<SEC>-final-prose.yml` | what was written back into the record |
| `LEAST-SURE-CUTS.md` | the cut each cutter was least sure about, written before the test |
| `validate.py` | the mechanical check on a cut or a restore |

**The one thing worth knowing before running this again.** The cutters never touched the
exercises or the practice problems, and could not have: `<SEC>-pass1.md` is assembled from the
cutter's prose plus the exercises and the ten prompts copied out of the record, so the test set is
byte-identical to the original's by construction rather than by instruction. `validate.py` closes
the other half — it fails a cut whose surviving sentences are not the original's word for word,
which is how "delete, never compress" is enforced rather than hoped for.

`<SEC>-final-prose.yml` is built by walking the *original* and keeping a sentence if the cut kept
it or `RESTORE.yml` names it. Nothing new can enter a restore, because nothing new is ever in the
input.
