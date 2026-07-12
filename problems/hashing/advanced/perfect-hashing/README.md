# Perfect Hashing (FKS / Minimal)

For a **static** key set you can build a hash function with *no* collisions, giving O(1) worst-case lookup instead of the amortized/average guarantee of a chained hash table. The **FKS scheme** uses two levels: a first hash spreads the keys into buckets, and each bucket of size b gets its own hash into b^2 slots — quadratic size makes a collision-free second-level hash easy to find, keeping total space O(n). A **minimal perfect hash** goes further, mapping the n keys bijectively onto exactly `0..n-1` with no empty slots; the CHD displacement method finds it fast. Construction is randomized, so a FIXED seed makes it reproducible.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [FKS Two-Level Perfect Hashing](problem-01-fks-two-level/PROBLEM.md) | Two-level, O(1) worst case | Hard |
| 2 | [Minimal Perfect Hash (CHD-lite)](problem-02-minimal-perfect-displacement/PROBLEM.md) | Displacement, bijective 0..n-1 | Hard |
