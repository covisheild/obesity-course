# S36-R1 glossary merge report

CONDUCTOR step 8. Checked against the final text as built by `python check/build.py --subject S36-R1`
(`check/_build/S36-R1.md`, 24 September 2026), not against the draft notes. Section n is record
`S36-R1-C0n` or `S36-R1-Cn`. No record was edited. No existing row of `prose/GLOSSARY.md` was changed;
new rows were inserted in their alphabetical places, as the file's header asks. The five batches'
proposals were merged into one definition per term, in the final text's words.

## 1. Rows added to `prose/GLOSSARY.md` (45)

cherry-picking (C13); cleaned transcription (intelligent verbatim) (C10); closed question (C05);
closing question (in a topic guide) (C06); code (in a transcript) (C12); conceptual generalisation
(C02); confidentiality (C07); deviant case (negative case) (C12); double question (C05); ethics
committee (EC) (C07); field notes (C08); focus group (C04); full verbatim (C10); group interview
(C04); in-depth interview (C03); informed consent (C07); leading question (C05); main question (in a
topic guide) (C06); mean share (of talk) (C11); memo (C12); moderator (C04); open question (C03, C05);
passage (of a transcript) (C12); pilot interview (C14); pooled share (of talk) (C11); power
calculation (C02); privacy (C07); probe (C08); prompt (in a topic guide) (C06); qualitative research
(C01); quantitative research (C01); quotation (in a qualitative report) (C13); randomised controlled
trial (C01); reflexivity (C09); research interview (C03); respondent (C02); respondent-to-interviewer
ratio (C11); semi-structured interview (C03); speaker label (C07); structured interview (C03); talk
share (C11); topic guide (C06); transcript (C10); turn (C11); warm-up question (C06).

Six of these were in no batch's proposals but are taught in a Definition or "In plain terms" of the
final text: closing question, mean share, passage, quotation, respondent-to-interviewer ratio and
speaker label. b1's and b2's two open question proposals were merged into one row.

## 2. Draft-note proposals not added, or changed

- **evidence-based medicine, evidence hierarchy, mixed methods, statistically representative** (b1):
  not in the final text (C01 and C02 were compressed).
- **NCD (non-communicable disease)** (b1): expanded only (C01, C03, C04, C07); the proposed gloss
  "a long-lasting condition that does not pass from person to person" is not in the text. The only
  gloss is C07's "non-communicable diseases such as diabetes". No row.
- **code, sense (1)** (b5: "the label R1 that stands in for a respondent's name", C07): the final C07
  calls R1 a **speaker label**, never a code. So "code" has one sense in this book; the R1 sense went
  into a separate "speaker label" row. No numbered senses were needed.
- **Definitions corrected to the final text**: double question (b2's "so an answer cannot be assigned
  to either" is gone); moderator (b2's "keeps the talk going without taking it over" is gone; C04 says
  only "the person who runs the group", Kitzinger's "facilitator"); main question ("grand tour" and
  "core question" wording: C06 keeps only "core question", in a Must-know point); warm-up question
  (the "grand tour" name is gone); transcript (b4's "made by someone who chose what went in" is gone;
  C10 says "made by a person or a program ... the text that analysis works on"); reflexivity (Mays and
  Pope's words, "sensitivity to the ways...", not b3's "showing how"); field notes (C08's list: what
  happened, where, how it felt, what surprised you; same day, before listening again); informed consent
  and ethics committee (C07's final wording); in-depth interview, structured interview (C03's final
  plain terms).
- **word (for the talk-share count)** (C11: "whatever stands between two spaces"): a counting
  convention for one exercise, not a term of art. No row.
- **Existing rows used in the same sense, not re-added**: sample, random sample, convenience sample
  (C02: "takes whoever is available"), population, premise, inference, conclusion, checking a
  reference (C13's four acts), systematic error and measurement bias (C09, see §5), mean, ratio.

## 3. Conflicts with existing rows (existing rows unchanged)

None of the terms the brief flagged (code, label, probe, interview, sample) has an existing row with
a different sense: code, label, probe and interview have no row, and sample is used in the row's
sense. So no row needed numbered senses. Two existing rows meet a second sense in this book:

1. **instrument.** Row (`B0-R0-C43`) has only the legal sense. C09's Illustration uses the measuring
   sense ("more readings on the same instrument do not remove") without a gloss, as does the existing
   `B0-R0-C30` zero error row. b1 avoided "instrument" for the interview, and the final text keeps that.
   The row needs a sense (2), measuring, from `B0-R0-C30`: a between-rounds decision.
2. **premise.** Row (`B0-R0-C42`): "a reason offered". C05: "a premise is a statement an argument
   rests on". The sense is the same; the words differ. Optional fix: C05 should reuse the row's words.

## 4. Drift inside S36-R1, and terms used before they are defined

1. **memo, two senses.** C08 (In plain terms and a Must-know point) says field notes are what "DeJonckheere
   and Vaughn call them memos". C12 defines a memo as a note written while reading a transcript. The
   row follows C12. Fix: C08 should drop the alias, or say it is not C12's memo.
2. **leading, two senses.** C05 and C08 both warn that DeJonckheere and Vaughn's probe called
   "leading" is not a leading question. The text keeps them apart; no fix needed.
3. **label.** "Label" means a speaker label (C03, C07, C11, C14) and a code ("a short label", C12).
   The text never confuses them; the two rows keep them apart.
4. **Used before the defining section.**
   - transcript: used in C04 (the focus-group illustration), defined in C10.
   - turn: used in C04's figure caption ("respondent's turn"), defined in C11.
   - closed question: used in C03's illustration, defined in C05.
   - probe: glossed briefly in C05 ("short follow-ups that ask for more"), defined in C08. The words
     agree.
   - pilot interview: named in C06's Definition, taught in C14. The row gives C14.
   - speaker label: "the labels R1, R2" in C03's illustration; named "speaker label" in C07.
   - EC: `build.py --subject` reports EC "used before anything expands them". C07 writes "an ethics
     committee, or EC", which the build's expansion check does not recognise. Fix: "ethics committee
     (EC)" in C07.
5. **No inconsistency** found for open question (C03 plain terms and C05 Definition agree), talk share
   and pooled or mean share (C11 and C14), or privacy and confidentiality (C07 Definition and plain
   terms).

## 5. Cross-book notes (existing rows, same sense, no fix required)

- **bias**: C09 says "it is bias: an error that points one way and does not shrink when you collect
  more", the words of the **measurement bias** row (`B0-R0-C30`), and cites Book 0's systematic error.
  No new row.
- **convenience sample, random sample** (`B0-R0-C29`): C02 recalls both in the row senses and sets
  the qualitative study's choice on purpose against them.
- **checking a reference** (`B0-R0-C41`): C13 uses the same four acts on a quotation.
- **statute, legislature** (`B0-R0-C43`): C07 says the ICMR guidelines are not a statute because no
  legislature passed them. Consistent.

## 6. Build

`python check/build.py --check`: 0 blocking, 137 warnings, the same as before the merge.
`python check/parallel.py registries`: 0 problems.
