# Bloom Filter

A **Bloom filter** is a space-efficient probabilistic set: a bit array of size `m` plus `k` independent hash functions. `add(x)` sets the `k` bits `h_1(x)..h_k(x)`; `contains(x)` returns true iff **all** those bits are set. It has **no false negatives** (anything added always tests present) but tunable **false positives** (an unadded item can collide on all `k` bits). Here the `k` hashes are computed arithmetically with fixed seeds so every test is deterministic and hand-traceable.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Design a Bloom Filter](problem-01-design-bloom-filter/PROBLEM.md) | Bit array + k hashes | Medium |
| 2 | [Counting Bloom Filter with Delete](problem-02-counting-bloom-filter/PROBLEM.md) | Counters enable delete | Medium |
