# HyperLogLog / Cardinality Estimation

Cardinality estimators guess the number of **distinct** items in a stream from the bit patterns of hashed values, in tiny space. Flajolet-Martin watches the longest run of trailing zeros in any hash (a run of length `r` suggests ~`2^r` distinct items); linear counting tracks how many of `m` buckets stay empty. The full estimators are approximate, so here we verify the **exact, deterministic register mechanics** — max trailing-zero count and empty-bucket count — rather than a fuzzy cardinality.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Flajolet-Martin Trailing-Zero Register](problem-01-flajolet-martin-register/PROBLEM.md) | Max trailing zeros | Medium |
| 2 | [Linear Counting: Empty Buckets](problem-02-linear-counting-empty-buckets/PROBLEM.md) | Empty-bucket count | Medium |
