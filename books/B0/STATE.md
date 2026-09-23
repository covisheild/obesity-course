# Book 0 — finishing state

Chat: session_01KfRHN8FLF6Qq7KUNTJgL9a, branch `book/B0-finish` from `25d2ed8`, 23 Sep 2026.
**Done. Book 0 is frozen** (tag `book0-frozen`).

| Step | D1–D7 | E1–E8 | F1–F5 |
| --- | --- | --- | --- |
| 5a cut + validate | done | done | done |
| 5b cold read | 73 gaps | 98 gaps | 53 gaps |
| 5c restore (final cut) | 32–48% | 35–50% | 35–51% |
| holes the original did not fill | 39 | 48 | 41 |
| triage: errors / gaps / not defects / Harsh | 7/21/10/1 (+10 new) | 9/22/16/1 (+11 new) | 6/20/14/1 (+4 new) |
| fix + verify | closed | closed | closed |

Verification: round 1 closed 106 of 110; round 2 closed 10 of 11; the conductor fixed the rest
directly (C38, C25, C41 amendment year, C30, C36 ADP). `books/B0/defects/VERIFY-*.md`.
Harsh's decisions (23 Sep): F2 reworded, not C5; near/far store → small/large store; D1 "per cent"
without the statute's stop; F3 Ex 2 "a paper, report or guideline you have to hand".

Tooling: `restore.py` dropped every kept bullet, quote and table row — fixed; A7, C2, C9 repaired.
Glossary: 260 rows, Parts A–F, sorted. 16 A–C consistency items listed, not fixed
(`books/B0/GLOSSARY-MERGE-REPORT.md` §5). Build: blocking 0, warnings 49.
