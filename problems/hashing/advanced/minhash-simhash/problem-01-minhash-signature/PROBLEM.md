# MinHash Signature

**Difficulty:** Medium

**Source:** Classic — Broder MinHash

## Description

Implement MinHash with a **fixed** family of `k` universal hash functions `(a*x+b) mod p` (seed the RNG with a fixed integer in the constructor). `signature(elements)` returns the length-`k` list whose i-th entry is the minimum of the i-th hash over the set. Because the hash family is fixed, the signature is identical every run — the reproducible sketch you store per set.

## Hint

For each (a, b) take min((a*x+b) mod p for x in the set). Fixed seed => fixed signature.
