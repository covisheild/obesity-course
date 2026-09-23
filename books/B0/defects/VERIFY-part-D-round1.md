# VERIFY — Book 0 Part D, round 1 (Task 4b, C24–C30)

Verifier: fresh context; did not audit or fix. Scope: each CONFIRMED-ERROR, CONFIRMED-GAP or NEW item in B0-R0-C24..C30-compression.md, checked against check/records/B0/*.yml as they now stand. Numbers recomputed in Python; quotes searched in sources/*.txt.

| record | defect id | verdict |
|---|---|---|
| B0-R0-C24 | C24-K1 | closed |
| B0-R0-C24 | C24-K2 | closed |
| B0-R0-C24 | C24-K3 | closed |
| B0-R0-C25 | C25-K1 | closed |
| B0-R0-C25 | C25-K2 | closed |
| B0-R0-C25 | C25-K3 | open |
| B0-R0-C25 | C25-K4 | closed |
| B0-R0-C25 | C25-K5 | closed |
| B0-R0-C25 | C25-K6 | closed |
| B0-R0-C25 | C25-K7 | closed |
| B0-R0-C26 | C26-K1 | closed |
| B0-R0-C26 | C26-K2 | closed |
| B0-R0-C26 | C26-K3 | closed |
| B0-R0-C26 | C26-K4 | closed |
| B0-R0-C26 | C26-K5 | closed |
| B0-R0-C26 | C26-K6 | closed |
| B0-R0-C26 | C26-K7 | closed |
| B0-R0-C27 | C27-K1 | closed |
| B0-R0-C27 | C27-K2 | closed |
| B0-R0-C27 | C27-K3 | closed |
| B0-R0-C27 | C27-K4 | closed |
| B0-R0-C27 | C27-K5 | closed |
| B0-R0-C27 | C27-K6 | closed |
| B0-R0-C28 | C28-K1 | closed |
| B0-R0-C28 | C28-K2 | closed |
| B0-R0-C28 | C28-K3 | closed |
| B0-R0-C28 | C28-K4 | closed |
| B0-R0-C28 | C28-K5 | closed |
| B0-R0-C28 | C28-K6 | closed |
| B0-R0-C28 | C28-K7 | closed |
| B0-R0-C28 | C28-K8 | closed |
| B0-R0-C28 | C28-K9 | closed |
| B0-R0-C29 | C29-K1 | closed |
| B0-R0-C29 | C29-K2 | closed |
| B0-R0-C29 | C29-K3 | closed |
| B0-R0-C30 | C30-K1 | closed |
| B0-R0-C30 | C30-K2 | closed |
| B0-R0-C30 | C30-K3 | closed |
| B0-R0-C30 | C30-K4 | closed |

Open: 1 of 39.

- B0-R0-C25 / C25-K3: P13 answer now says the chance is "at least 0.25, a floor", but the person is known to be in a household of four and the s.3(2) ceiling bounds the rural population as a whole, not that subgroup; the floor does not follow.

Note (closed, not a defect of the fix as specified): C29-K3 removed the 0.633 and 0.317 numbers entries, but the d6-sample-means.png caption still states both values, so they now have no numbers entry (the fixer flagged this). Both match the square-root law (2/√10 ≈ 0.632, 2/√40 ≈ 0.316).
