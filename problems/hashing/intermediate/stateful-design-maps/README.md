# Design: Stateful Hash-Map Systems

Real systems keep per-key histories or aggregates in a Hash Map: a time-keyed store binds each key to a timestamped version list, a transit system accumulates (start, end) → (total time, count), a token manager maps ids to expiry times, and a feed maps users to tweets and follow sets. The map holds the mutable state; a small amount of ordering (binary search or a sort) answers the query.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Time Based Key-Value Store](problem-01-time-based-key-value-store/PROBLEM.md) | Versioned map + binary search | Medium |
| 2 | [Design Underground System](problem-02-design-underground-system/PROBLEM.md) | Aggregate map (sum, count) | Medium |
| 3 | [Design Authentication Manager](problem-03-authentication-manager/PROBLEM.md) | Id -> expiry map | Medium |
| 4 | [Snapshot Array](problem-04-snapshot-array/PROBLEM.md) | Per-index version history | Medium |
| 5 | [Design Twitter](problem-05-design-twitter/PROBLEM.md) | Maps: tweets + follow sets | Medium |
