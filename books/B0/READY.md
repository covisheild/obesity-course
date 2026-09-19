# Source gate · Book 0 Part A (A1–A8)

Checked against `sources/` on 2026-09-20. The rule in `claude.md`: a book only enters the
pipeline when its source pack is complete, and a line saying **no** stops the pipeline.

## The gate

| Needed for | Instrument or text | Kind | In `sources/`? | Obtained |
| --- | --- | --- | --- | --- |
| A1 illustration — the lakh grouping, in a real document | Food Safety and Standards Act, 2006, ss. 50–53 | instrument | `fss_act_2006.txt` | **yes** |
| A2, A4, A8 illustrations — real meal standards | National Food Security Act, 2013, Schedule II | instrument | `nfsa_2013.txt` | **yes** |
| A3, A5 illustrations — a real per-person-per-month entitlement | National Food Security Act, 2013, s. 3(1) | instrument | `nfsa_2013.txt` | **yes** |
| A7 illustration — a real ladder of numbers spanning powers of ten | Food Safety and Standards Act, 2006, ss. 50–53 | instrument | `fss_act_2006.txt` | **yes** |
| A1–A8 definitions — the canonical anchor every derivable concept needs | a school-level text on arithmetic, ratio, index notation and logarithms | textbook | — | **no** |

## The one **no**, and why the pipeline ran anyway

The missing line is a `textbook` anchor, and it is missing for the same reason it is missing in
three of the four records in `done/`: **no textbook is reachable from this authoring
environment.** `plan/INVENTORY-PILOT.md` established this before any authoring started, and
recorded it as structural rather than incidental.

A textbook anchor for a derivable concept is not the evidence for the concept. The evidence is
the derivation, which the reader can check line by line with a calculator. The anchor is the
canonical text a specialist would be pointed at, and the specification requires one. So the
eight records carry it as `opened: false`, with a locator naming the chapter to find and a note
in `verified.note`, and the build warns on all eight. They cannot reach `verified`, and
therefore cannot reach `released`, until someone with library access opens one text and fills
in eight locators.

**That is the whole citation backlog for Part A: one textbook, eight locators.** It is listed
again in `HANDOVER.md`.

## What was checked and found not to be needed

Anticipated before the inventory and then dropped, so nobody goes looking for them:

- **Census or NFHS population figures**, for A8. Not needed and deliberately not used. A8's
  worked example takes its one real figure from the National Food Security Act and requires the
  reader to supply the rest as *their own labelled guesses*, which is the method A8 teaches. A
  sourced population figure would teach the wrong lesson as well as needing a source nobody here
  can open.
- **ICMR-NIN recommended dietary allowances**, for A4 and A5. Not in `sources/`, and not needed:
  the National Food Security Act's own Schedule II carries statutory meal standards that are
  already opened and clause-located.
