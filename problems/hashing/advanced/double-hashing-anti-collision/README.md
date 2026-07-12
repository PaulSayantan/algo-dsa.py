# Double Hashing (Anti-Collision)

A single polynomial hash can be fooled: an adversary (or just bad luck) can produce two different strings with the same hash modulo one prime. **Double hashing** computes the value under two *independent* (base, modulus) pairs and uses the **pair** of hashes as the key. For two strings to collide they must collide under both moduli simultaneously, which happens with probability on the order of `1/(M1*M2)` — astronomically unlikely for `M ~ 10^9`. This makes hash-based equality effectively exact without verifying slices.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Count Distinct Substrings of Length L (Double Hash)](problem-01-count-distinct-double-hash/PROBLEM.md) | Two-channel distinct count | Medium |
| 2 | [Detect a Repeated Substring of Length L (Double Hash)](problem-02-detect-repeat-double-hash/PROBLEM.md) | Two-channel repeat detection | Medium |
| 3 | [Compare Two Strings via Double Hash](problem-03-compare-strings-double-hash/PROBLEM.md) | Two-channel equality | Easy |
