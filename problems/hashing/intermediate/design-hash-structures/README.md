# Design: Hash-Backed Structures

Implementing the ADTs themselves cements how hashing works: a HashMap/HashSet is a bucket array plus a hash and collision chaining; a RandomizedSet pairs a value→index map with a dynamic array for O(1) insert/delete via swap-with-last; a rate limiter and a Two-Sum store keep just enough per-key state in a map. Each is an op-sequence: replay the calls, observe the deterministic returns.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Design HashMap](problem-01-design-hashmap/PROBLEM.md) | Buckets + chaining | Easy |
| 2 | [Design HashSet](problem-02-design-hashset/PROBLEM.md) | Buckets, membership | Easy |
| 3 | [Insert Delete GetRandom O(1)](problem-03-randomized-set/PROBLEM.md) | Map + array swap-delete | Medium |
| 4 | [Logger Rate Limiter](problem-04-logger-rate-limiter/PROBLEM.md) | Message -> last-time map | Easy |
| 5 | [Two Sum III — Data Structure Design](problem-05-two-sum-design/PROBLEM.md) | Frequency map pair check | Easy |
