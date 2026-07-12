# FKS Two-Level Perfect Hashing

**Difficulty:** Hard

**Source:** Classic — Fredman, Komlos & Szemeredi (FKS)

## Description

Build an FKS two-level perfect hash over a static set of integer keys. The first level hashes each key into one of `n` buckets; each bucket of size `b` is rehashed into `b*b` slots, retrying the second-level hash until it is collision-free. Seed the RNG with a **fixed** integer so construction is reproducible. Expose `lookup(key)` (True iff the key is present), `verify_all(keys)` (True iff every original key resolves to itself), and `total_slots()` (the total number of second-level slots allocated).

## Hint

Universal hash (a*k+b) mod p mod size. For each bucket of size b, use b*b slots and re-draw (a,b) until injective. Fixed random.seed(...) at the top makes the whole build deterministic.
