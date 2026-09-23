# Book 0 — finishing state

Chat: session_01KfRHN8FLF6Qq7KUNTJgL9a, branch `book/B0-finish` from `25d2ed8`, started 23 Sep 2026.
Unit of work: handover §4.1 — compress D, E, F1–F5; merge glossary inboxes; render docx; tag frozen.

| Step | D1–D7 | E1–E8 | F1–F5 |
| --- | --- | --- | --- |
| extract | done | done | done |
| 5a cut + validate (re-validated by conductor) | done | done | done |
| 5b cold read (against released earlier Parts) | done, 73 gaps | done, 98 gaps | done, 53 gaps |
| 5c restore + validate | done, 32–48% cut | done, 35–50% | done, 35–51% |
| writeback + build (0 blocking) | done `317a94e` | done `4b69bd6` | done `df6a7bf` |
| holes the original did not fill | 39 | 48 | 41 |

Tooling fix `df6a7bf`: `restore.py` dropped every kept bullet, block quote and table row. D–F
unaffected (verified byte-identical after the fix); A7, C2 (C16), C9 (C23) had lost lines since
their compression and were put back.

## Open

1. Triage the 128 holes (`books/B0/compress/HOLES-part-{D,E,F}.md`): one auditor per Part →
   `books/B0/defects/<RECORD-ID>-compression.md`, each item CONFIRMED (error, or a gap that blocks
   an exercise/problem) or NOT A DEFECT with reason.
2. Fix confirmed items, one fixer per section; fresh verifier; two rounds, then conductor.
3. Glossary merge (inboxes D, F2, plus E/F terms); settle "whisker" vs "error bar".
4. Render docx; merge to main; tag `book0-frozen`; bundle.
