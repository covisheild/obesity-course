# S47-R1 handover (v1.0, 2 Oct 2026)

Book 5, *Policy process, framing and advocacy craft · Rung 1*. 18 sections, 30 practice problems (C11, C15, C17:
10 each), 13 figures + 9 figure_notes, 59 glossary rows, PDF ~178 pages (page_budget 160). 191 audit defects
(22 errors), all with a disposition and verified closed; 51 rendered-page faults triaged (29 fixed in records,
2 rejected, 20 renderer/series). Build blocking 0. First book through the source-collection stop: released
2 Oct 2026, `sources-provided` (Harsh supplied 7 PDFs).

## Decisions taken in this book
- **One addressee rule** (C02, C09, C11, C18): a note goes to the body holding the decision job; where several must
  act, it names all and says which moves first. The sugary-drinks note is addressed to the GST Council.
- **GST as held**: the Council recommends (Art. 279A; PIB 2163555, "special de-merit rate of 40%"); CGST s.9(1)
  caps the central rate at 20%; heading 2202 drinks are in Schedule III - 20% of 9/2025-CT(Rate), entries re-stated
  by 01/2026-CT(Rate) (in force 1 May 2026). Nothing is said about State GST Acts (not held). 19/2025 not held.
- **General Clauses Act s.23** is taught for "rules or bye-laws"; FSSAI's own procedure comes from FSS Act ss.92-93
  and the 2018 Packaging Regulations' preamble. State food-safety rules go before the State Legislature (s.94(3)).
- **School-canteen case** deliberately unresolved: no held source settles whether FSSAI or the State decides.
- **Pielke not held**: C17 teaches only "honest broker" against "issue advocate" as Oliver & Cairney 2019 state it.
- **Entman** cited "as reported by Koon et al."; Gollust 2013 and Varghese 2024 not held (Varghese only via Summan).
- PIB releases: kind `instrument` where an institutional record uses them for decisions, `primary` where an
  empirical record studies their framing.
- Lok Sabha USQ 2110 withdrawn at intake (sansad.in terms unreadable).
- `books/S47-R1/draw_figures.py`: `check/figures/draw.py` does not apply the numbers registry, so figures whose
  numbers the prose writes as `{{n:key}}` are redrawn with this book-local wrapper (the build checks them correctly).

## Open for Harsh / later
- Coverage gaps proposed as map amendments, not decided: SWOT analysis (NMC); power as a concept (S47-R2 P1).
- Book is ~178 pages against a 160-page budget.
- Sources to tidy: 19/2025-CT(Rate) and a Gazette copy of 01/2026; an official copy of the 2008 Smoking Rules
  (held from Indian Kanoon); confirm the download sites of the PLCP and the 2018 Packaging notification PDFs.
- Currency: the GST rate (any notification after 01/2026), the DPDP Rules' stages (C03), the Business Rules'
  amendment series (AoB no. 386, 22 Jul 2026; ToB no. 75, 13 Jan 2025), PRS private members' Bill counts (2012).
- Contract-change items (check/** frozen mid-flight): `draw.py` and `prepare.py extract/assemble` should apply the
  numbers registry; `_block()` corrupts a prompt/answer that begins with a table or list (worked round by a lead
  line; earlier books' appendices may be affected: S55-R1 C02/C08, S36-R1 C05, B0); the abbreviation scan misses
  dotted forms (G.S.R., S.O.); the new-reader series text promises a Symbols page and calculators to a book with
  neither; table headers do not repeat after a page break; narrow first columns break words.
