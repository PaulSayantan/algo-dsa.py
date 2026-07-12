# Minimal Perfect Hash (CHD-lite)

**Difficulty:** Hard

**Source:** Classic — Belazzougui, Botelho & Dietzfelbinger (CHD)

## Description

Build a **minimal** perfect hash over a small static integer set: the `n` keys must map bijectively onto exactly `0..n-1`. Split keys into buckets with one universal hash, then process buckets largest-first, assigning each a displacement `d` so that a second hash plus `d` places every key in that bucket into a distinct still-free slot. Seed the RNG with a fixed integer. Expose `hash(key)`, `all_hashes()` (in insertion order), and `is_minimal_perfect()`.

## Hint

Two universal hashes f (bucket) and h (placement) plus a per-bucket displacement array g. Greedily pick the smallest d that avoids taken slots. Fixed seed => reproducible g.
