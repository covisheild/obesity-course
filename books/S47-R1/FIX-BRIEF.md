# Fixer brief · S47-R1 (Task 4 of PIPELINE.md)

Repository `/home/claude/obesity-course`, branch `book/S47-R1`. Do not commit, push or switch
branches. **No `rm` in the repository**; absolute paths; scratch in `/home/claude/scratch-fix-<batch>/`.
Other fixers work on other sections at the same time: edit only your own records
(`check/records/S47/<RECORD-ID>.yml`), their figure specs (PNGs are redrawn, never edited), and your
defect files. Never edit `sources/`, `sources/INDEX.yml`, `check/references/library.bib`,
`prose/GLOSSARY.md`, anything under `check/` other than your records, or another record; never fetch
from the web. `books/S47-R1/numbers.yml`: you may add a key (value read from a held source, citekey
given) but never change an existing key's value; if a key's value is wrong, leave the defect `Partly:`
and say so.

Read `books/S47-R1/defects/<RECORD-ID>.md` and the record. Read the parts of `claude.md` the defects
cite (and "The one rule that matters"), `check/SELFCHECK.md`, and the book-wide decisions below. For
a defect that depends on what a source says, open the held file and check it yourself: auditors can
be wrong.

Apply every item, or reject it with the source's words. Rules while fixing: a claim without an
opened source is not written down as a fact; every number's `quote` must state that number; keep the
second person; one idea per sentence; the compression pass is done, so fix with the fewest words that
close the defect, and prefer deleting a false sentence to adding a qualifying one. Cite other
sections as `S47-R1-Cnn` / Book 0 as `B0-R0-Cnn` in backticks (the renderer prints them). Expand every
abbreviation at first use in the section (PIB = Press Information Bureau; FSSAI = Food Safety and
Standards Authority of India; PRS = PRS Legislative Research; G.S.R. = General Statutory Rules;
S.O. = Statutory Order; GST = goods and services tax; CGST = central goods and services tax; COTPA;
FCTC; PLCP; CBIC = Central Board of Indirect Taxes and Customs). If a fix changes a number a figure
uses, update the spec, run `python books/S47-R1/draw_figures.py` (it applies the numbers registry),
and look at the PNG with the Read tool.

Run `python check/build.py --check` until blocking is zero for your records. Re-derive every practice
and exercise answer you touched. Then read your section as the reader meets it in
`check/_build/S47-R1.md` (run `python check/build.py --subject S47-R1` first; if another fixer is
rendering at the same moment, rerun): every sentence you must read twice is a defect — fix it.

**Disposition format (checked by `check/defects.py`).** Under each numbered defect write exactly one
line starting `Fixed: <what changed>`, or `Partly: <what changed, and what remains and who owns it>`,
or `Rejected: <why the text was right, with the source's words>`. Leave the `Verified:` line to the
verifier. Return at most 150 words: fixed / partly / rejected counts, and anything left.

## Book-wide decisions (conductor, 2 Oct 2026) — apply wherever your defects touch them

1. **One addressee rule.** A note is addressed to the body that holds the decision job for the
   instrument the proposal needs (`S47-R1-C02`). Where several bodies must act, the note names all of
   them and says which one moves first (`S47-R1-C09`). For the sugary-drinks GST: the GST Council
   recommends; the Central Government notifies the central rate under CGST s.9(1); the note is
   addressed to the GST Council as the body that moves first. C02, C09, C11 and C18 state and apply
   this one rule, and C18's own worked note obeys it.
2. **GST, as held.** The Council recommends (Art. 279A; PIB 2163555). CGST s.9(1) caps the central rate
   at 20%; heading 2202 drinks are in Schedule III - 20% of 9/2025-CT(Rate), entries re-stated by
   01/2026-CT(Rate), in force 1 May 2026 (19/2025 not held; the held 01/2026 is CBIC's pre-Gazette
   copy). The 40% is the combined rate in PIB's words. **Nothing about State GST Acts or State
   notifications** beyond PIB 2163555's words; delete "each State notifies under its own Act" unless a
   held source says it. A cess figure only if a held source states it. Vote arithmetic only as Art.
   279A states it.
3. **Rule-making.** General Clauses Act s.23 governs "rules or bye-laws" made after previous
   publication; do not say it governs FSSAI regulations. FSSAI's own procedure comes from the FSS Act
   (ss.92–93) and the 2018 packaging notification. State food-safety rules are laid before the State
   Legislature (FSS Act s.94(3)).
4. **The school-canteen case** is never resolved beyond what held sources carry; no Chhattisgarh body
   is named as fact.
5. **Informing and campaigning.** Both are legitimate jobs (`S47-R1-C17`); C16 says the researcher's
   job *as analyst* is to state options with their evidence and uncertainty, not that it is the only
   job. "Honest broker" against "issue advocate" only as Oliver & Cairney 2019 state it; no second
   sense examined, no Pielke four roles.
6. **No exercise answered in advance.** Where a drill or exercise is already answered by another
   section's text, change the drill to another held text (or a made-up one, marked), not the other
   section.
7. **Framing evidence** carries country, years, sample and design; Entman's four functions "as
   reported by Koon et al."; Barry's findings stay within what Barry tested (no "disease" frame he did
   not test); no Gollust, Pielke or Varghese claims (Varghese only as Summan reports it).
8. **Figure notes** may name the diagram a reader would want (the brief asks for that); not a defect.
9. **Unsourced claims** are deleted or reduced to what a held source says; the book's own reasoning
   reads as reasoning ("because..."), not as a finding.
10. **References:** a source already in `library.bib` may be added to your record; a source not held
    stays open (`Partly:`). Never relabel a `kind` to pass a gate.
