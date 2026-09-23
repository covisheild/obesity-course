# The Notion build tracker

Harsh follows the build in Notion, not in the repository. The conductor (`CONDUCTOR.md`) keeps it
current; nobody else writes to it. Standing instruction from Harsh, 23 September 2026: no chat
needs telling this again.

## What it is

| | |
| --- | --- |
| Dashboard page | "Obesity Expert Course · Build Dashboard", https://app.notion.com/p/3e0e211880e28124b6d0ff389421243c |
| Database | "Build Tracker", data source `collection://21657754-2f96-4821-942c-86f85790cc00` |
| One row per unit | Unit ID `B0`, `S01-R1`, `S02-R1`, ... (the ids in `map/BOOKS.yml`) |
| Child database | "Book 0 · sections", one row per Book 0 section. Book 0 is frozen; touch it only when a new Book 0 version changes a section |

Properties of a unit's row:

- **Stage**: Not started, Source gate, Inventory done, Drafted, Audited, Build clean, Compressed,
  Reader pass, Released.
- **Citations**: n/a, Unopened, Partly verified, Verified.
- **Concepts**: the number of sections (records) in the unit.
- **Blocker**: what is stopping the unit, in one line; empty when nothing is.
- **Notes**: the latest phase line, and at finish the main commit.

## When the conductor updates it

At **every phase boundary**, the same moments it sends Harsh a one-line progress message, and at
**finish**. The row gets the same line as the message, so Notion and the chat never disagree. If the
dashboard page carries a status line (a "now building" or "last updated" line), update it at the
same moments.

The option order of Stage is historical: compression now runs **before** the audit
(`PIPELINE.md`, Task 5), so a unit goes Drafted → Compressed → Audited → Build clean. Set the stage
the unit has reached; never skip back to match the option order.

| Pipeline step (`PIPELINE.md`) | Stage | Citations | Also set |
| --- | --- | --- | --- |
| Claimed (`CONDUCTOR.md` §0) | Not started | n/a until the inventory | Notes: "claimed, branch book/<ID>" |
| Task 1 done, `READY.md` has a **no** | Source gate | Unopened | Concepts; Blocker: the missing files, named |
| Task 1 done and every source obtained (intake checklist done) | Inventory done | Unopened | Concepts; Blocker empty |
| Task 2: every section drafted | Drafted | Unopened, or Partly verified if drafters quoted sources | |
| Task 5: cut, cold read, restore done | Compressed | unchanged | |
| Figure plan: figures drawn from the final text and looked at | Compressed (no stage of its own) | unchanged | Notes: "figures: n drawn, m sections with figure_note" |
| Task 3, 4 and 4b: every defect closed | Audited | Partly verified, or Verified if no reference is `opened: false` | Blocker: any defect still open |
| `check/build.py --check` at zero blocking, docx and PDF built | Build clean | Verified | Notes: warning count |
| Task 6, if Harsh ran a reader pass | Reader pass | unchanged | |
| Finish (`CONDUCTOR.md` §3) | Released | Verified | Notes: the main merge commit (short hash) and version; Blocker empty |

A stop to ask Harsh (`CONDUCTOR.md` §2) puts the reason in **Blocker** at the moment the message is
sent, and clears it when the stop ends.

## How

Through the Notion connector: find the unit's row in the data source above by Unit ID and update
its properties; if the row does not exist, create it in that data source. Read the row back once
after the first write of a chat to confirm the property names still match this file; if they have
changed, update this file in the same commit as the book.

If Notion is unreachable, never block the book on it: write "Notion not updated: <step>" in
`books/<ID>/STATE.md`, carry on, and bring the row up to date at the next boundary that can reach
it. Say so in the finish report if it was never brought up to date.
