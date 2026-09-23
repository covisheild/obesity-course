> Archived brief given to the four amendment drafters on 23 Sep 2026. Paths under `/home/claude/` were that session's working copies; the files now live beside this one in `map/audit-2026-09/`.

# Brief for amendment drafters (map v3 → v3.1)

## What this is
Harsh (MD Community Medicine resident, AIIMS Raipur) is building a 196-book self-study course that makes
him an obesity expert who attacks obesity at every level, from the clinic to policy, aiming to eliminate
or substantially reduce obesity in India. The course is generated book by book from a frozen subject map:
`/home/claude/obesity-course/map/subject-map-v3-FROZEN.md` (61 subjects, 195 rungs). An external audit
found verified gaps. Harsh approved closing ALL of them. The map stays frozen; you are drafting lines for
`map/AMENDMENTS-v3.1.yml`, which each book's inventory step will read as part of its rung's terminal
requirements (outcomes, skills, build target, gate).

Read first:
- The audit: `/home/claude/audit/curriculum-audit-2026-09.md` (tiers, gaps, recommended rungs).
- Verified evidence: `/home/claude/audit/V-map.md` (what exists, with map line numbers, and where each gap
  should go) and `/home/claude/audit/V-facts.md` (verified external facts with URLs).
- Raw audits for detail: `/home/claude/audit/{A-clinical,B-policy,C-system,D-profession,E-india,F-blind}.md`.
- The map's front matter (lines 1–60) for the level rubric, and the full text of every rung you touch.

Harsh's decisions (apply them):
1. Tier 1 and Tier 2 gaps: close them all.
2. Persona widened, no new books: leadership, people/project/budget management, negotiation with
   ministries, states and industry, institution building, community engagement and mobilisation, and
   sustaining oneself over decades go into existing rungs whose build targets already need them, plus a
   leadership thread through S57. Campaign and social-marketing design goes into S34-R3, keeping the map's
   rule that structural levers come first and a campaign must earn its place. The map's
   "administrative capture" warning stays as a caution, not a ban.
3. GLP-1 prescribing: a CDSCO approval condition restricts prescription of these drugs to
   endocrinologists and internal medicine specialists (cardiologists for some indications); Community
   Medicine is not on the list (see V-facts claim 1). Keep all clinical knowledge. Hands-on build
   targets/gates that have Harsh initiate or prescribe become a clinic co-run with an eligible physician
   in which Harsh writes the protocol, assesses, counsels and monitors, and the physician holds the
   prescription. Add a regulatory-literacy item on prescriber conditions.

## Rules for every amendment line
- **Form.** Same voice as the map. A concept states an idea to understand. A skill is an observable action
  "written so someone else could watch you do them and judge". A build is an artefact. A gate is one
  observable pass/fail test.
- **Level fit.** R1 Introductory = recognise and route (no execution). R2 Intermediate = read, critique,
  commission. R3 Advanced = execute and defend. R4 Expert = originate and adjudicate. Put each line at the
  rung whose level it matches; never add execution to an R1.
- **Chain rule.** A line at rung n may only presuppose what is taught at rungs below it in the same subject,
  in its prerequisite subjects, or in Book 0. If your R3 line needs a concept nobody teaches, add that
  concept at R1 or R2 too. Remember: every R1 book is a bridge that must carry the reader to everything R2
  presupposes, so an R2 addition lands in the R1 book as well.
- **No duplicates.** Grep the full map before adding; if it is already there, don't add it. If an existing
  line is nearly right, prefer a `revise` of that line over a new one.
- **Minimum lines.** Close the gap with the fewest lines that do it. One line may close several items.
  Don't pad rungs; if a rung would take more than 4 additions, say so in `note`.
- **The one rule.** An amendment line must not assert a volatile fact (a number, a date, a legal status,
  a price). Name the instrument or dataset and let the book source it at intake. Where a line names a
  specific instrument, programme, dataset or body, give a verified URL in `sources` (from V-facts or the
  raw audits, only if that audit says it opened it) or set `verify_at_intake: true`.
- **Revisions.** `kind: revise` replaces the text of an existing map line. Give `target` = the existing line
  quoted exactly and `map_line` = its line number in the frozen map.
- **S61** (recognise-and-route directory, target Introductory, 1 rung) takes routing items: a field, who
  owns it, and the question you would ask them.

## Output format
Write YAML to your own file only (named in your task), a list of entries:

```yaml
- rung: S26-R3            # subject-rung this line belongs to
  kind: concept           # concept | skill | build | gate | revise
  text: "..."             # the line, in the map's voice
  target: "..."           # revise only: existing line, quoted exactly
  map_line: 2045          # revise only
  gap: "1.1"              # audit gap id(s) it closes, e.g. "1.1, 2.4"
  why: "..."              # one line: which verified finding this answers (cite V-map/V-facts)
  sources: []             # URLs, only for lines naming a specific instrument/programme/dataset/body
  verify_at_intake: false
  note: ""                # optional
```

End with a YAML comment block `# COVERAGE:` listing every gap/sub-item in your scope and the entry
(rung + first words) that closes it, or `ROUTED to S61` / `NOT CLOSED: reason`.

Reply to the conductor in ≤150 words: number of entries per rung, anything you could not close, and any
place where you had to add a lower-rung prerequisite.
