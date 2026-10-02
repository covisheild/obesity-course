# Draft notes · S47-R1 batch b2 (C04, C05, C06)

Drafted 2026-10-02 to `books/S47-R1/DRAFT-BRIEF.md`; exemplars S37-R1-C09 and C11.

## Records written

- `check/records/S47/S47-R1-C04.yml` · Union, State or local: whose subject is it (institutional)
- `check/records/S47/S47-R1-C05.yml` · Inside the Union government: Cabinet, ministries, departments (institutional)
- `check/records/S47/S47-R1-C06.yml` · How an Act is made (institutional)

`python check/build.py --check`: blocking 0 for the whole tree at hand-back; my three records carry
no warnings. 86 quotes re-checked by a separate script against the held files (whitespace-normalised,
case-folded): 0 missing; every number's quote states its number. Arithmetic recomputed (264 + 160 = 424;
14 + 11 = 25). Each record has a retrieval exercise (skill_ref S47-R1-K01) and retrieval_items.

## Anything unsourced

Nothing written as fact without a held quote. Gaps handled by saying so in the text, not by claiming:

- **Chhattisgarh's own instruments are not held**: its Panchayat Raj and municipal Acts (what it has
  devolved under Arts 243G/243W), its business rules under Art. 166(3), and its Assembly's rules of
  procedure. Each section says "not read in this book; open it before naming a body".
- **Which entry governs a canteen rule** (State 6, Concurrent 18/25/33(b), Union 52 via FSS s.2) is left
  open, as the brief asks; C04 names every entry and says the lists cannot settle it. Consistent with
  C11's canteen trace. C04 also says the FSS Act does not name entry 52 (the match is a reading), as C11 does.
- **Whether a subordinate rule counts as "legislation"** under ToB Second Schedule (a) is not asserted.
- **"15th Lok Sabha" = PRS's "current term of Parliament" (2012)**: the number's quote is "At the beginning
  of the 15th Lok Sabha"; PRS does not say in one sentence that the current term is the 15th. The auditor
  may prefer the prose to say "the term of Parliament running in 2012" only.
- The Standing Committee's evidence-taking is not claimed: the RS booklet says only Select/Joint
  Committees "take evidence of associations, public bodies or experts", and C06 says so.

## Reference kinds (for the conductor)

- `plcp_2014` entered as **guideline** (a Committee of Secretaries decision, not an instrument).
- `rajyasabha_2005_legislative` entered as **guideline** (the Secretariat's procedural guide).
- `prs_2012_parliament60` appears only in illustration numbers and must-know refs, not as a definition reference.
- `pib_1797203` as **instrument**, following S37's treatment of PIB releases. Each concept also has the
  Constitution or a Business Rules order as its instrument anchor, so no kind was stretched to pass the build.

## Practice-set size

None of C04–C06 is quantitative; no `practice[]`.

## Figures

- C06: `s47-r1-c06-private-members-bills.png`. Grouped bars, Private Members' Bills introduced against
  discussed, Lok Sabha 264/14 and Rajya Sabha 160/11 (PRS 2012). Checks 424 and 25. Drawn and looked at.
- C04 `figure_note`. Wanted diagram, which the tool cannot draw: three tiers (Union, State, panchayat or
  municipality), with the canteen, tax and label proposals drawn as arrows to the entries they touch
  (State 6; Concurrent 18, 25, 33(b); Union 52 via FSS s.2; Art. 246A for the tax; Eleventh/Twelfth
  Schedules shown dashed, as "only if the State Act hands it down").
- C05 `figure_note`. Wanted diagram: one proposal (the sugary-drinks tax) fanning out to four departments
  (Revenue 18A/21(a); Food Processing 6; Health and Family Welfare 3(a); Consumer Affairs 6), joined by
  a ToB rule 4(1) "all concur, or Cabinet" box.
- A flow diagram for C06 would also help (department → consultation → Law Ministry → Cabinet →
  House 1 three readings → House 2 → assent → commencement), with the two "doors" marked.

## Glossary rows (proposed; GLOSSARY.md not edited)

| Term | Plain words it gets at first use | First taught in |
| --- | --- | --- |
| Union List, State List, Concurrent List | Lists I, II and III of the Seventh Schedule: subjects on which Parliament alone, each State Legislature alone, or both may make law (Article 246) | `S47-R1-C04` |
| entry (of a Seventh Schedule list) | one numbered subject in a list, named in a few words, such as State List entry 6, public health | `S47-R1-C04` |
| repugnant (of a State law) | clashing with a law Parliament made on a Concurrent subject; the State law is void to that extent (Article 254(1)) | `S47-R1-C04` |
| Allocation of Business Rules | the Union government's rulebook (1961, amended) saying which department owns which subject: departments in its First Schedule, subjects in its Second | `S47-R1-C05` |
| Transaction of Business Rules | the Union government's rulebook (1961, amended) saying who decides a case and which cases go to the Cabinet | `S47-R1-C05` |
| Cabinet | the Prime Minister and the other Ministers of Cabinet rank (Article 352(3)'s words) | `S47-R1-C05` |
| Bill | a statute in draft | `S47-R1-C06` |
| Private Member's Bill | a Bill introduced by a member of Parliament who is not a Minister | `S47-R1-C06` |
| Money Bill | a Bill containing only provisions on the matters in Article 110(1), such as imposing or altering a tax; it starts in the Lok Sabha, and the Rajya Sabha may only recommend changes within fourteen days | `S47-R1-C06` |
| assent | the President's signature that turns a passed Bill into an Act (Article 111) | `S47-R1-C06` |
| Pre-legislative Consultation Policy | the Union's 2014 policy, a decision of senior civil servants and not a law, asking departments to put draft laws in public for at least thirty days | `S47-R1-C06` |

## Numbers keys

C06 uses `{{n:plcp_comment_days}}`. No new keys proposed: the Private Members' Bill counts and the
fourteen-day Money Bill period appear only in C06.

## Notes for other batches

None needed. Checked for consistency with C03 (the ladder image, "executive decision"), C07 (same name,
"Pre-legislative Consultation Policy"; its PLCP passage restates C06 for rules, which is fine) and C11
(its canteen trace matches C04's entries and its Allocation of Business Rules items match C05's).
