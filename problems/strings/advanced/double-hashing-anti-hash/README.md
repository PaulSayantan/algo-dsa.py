# Double Hashing / Anti-Hash

## What it is

**Polynomial string hashing** maps a string to an integer so that two equal
substrings share the same value and (usually) two different substrings do not.
A single substring `s[l..r]` is hashed as

```
H(s[l..r]) = ( s[l]*B^0 + s[l+1]*B^1 + ... + s[r]*B^(r-l) ) mod M
```

for a base `B` and modulus `M`. With a **prefix hash** array plus precomputed
powers of `B`, the hash of any substring is retrieved in `O(1)`, which is what
makes techniques like Rabin-Karp, "compare substrings by hash", and
"binary-search the answer length" run fast.

The catch: any single modulus `M` is vulnerable. There are always pairs of
different strings that collide (`H(a) == H(b)` while `a != b`). On competitive
judges, adversaries craft **anti-hash tests** — inputs engineered so that a
popular `(B, M)` pair produces a collision — and a single-hash solution then
returns a wrong answer. The classic example is the **Thue-Morse string**, which
forces collisions for any base modulo `2^k`.

**Double hashing** defends against this. Compute two *independent* hashes with
different moduli (and often different bases): `h = (h1, h2)`. Two substrings are
treated as equal only when **both** components match. If each modulus is around
`10^9`, a random collision on both simultaneously has probability about
`1 / 10^18`, which is negligible even across billions of comparisons. It is far
harder for an adversary to break two secret/large moduli at once, especially if
the base is randomized at runtime.

## When to reach for it

- Rabin-Karp substring search and multi-pattern matching.
- Comparing many substrings for equality in `O(1)` (dedup, counting distinct
  substrings, longest common substring, palindrome checks).
- **Binary searching a length** `L` and hashing all windows of that length —
  a workhorse pattern for "longest duplicate / common substring" problems.
- Any hashing solution submitted to a judge with adversarial tests, or any
  problem where a single hash gives *wrong answers* rather than TLE.

## Complexity

- Build prefix hashes and power tables: `O(n)` time, `O(n)` space (per modulus).
- Query any substring hash: `O(1)`.
- Collision probability with two `~10^9` moduli: `~q^2 / M1 / M2` for `q`
  comparisons — effectively zero for `q` up to `~10^7`.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Find First Occurrence in a String](problem-01-first-occurrence-in-string/PROBLEM.md) | Rabin-Karp rolling hash | Easy |
| 2 | [Longest Happy Prefix](problem-02-longest-happy-prefix/PROBLEM.md) | Prefix-hash equality of prefix vs suffix | Medium |
| 3 | [Distinct Echo Substrings](problem-03-distinct-echo-substrings/PROBLEM.md) | O(1) substring hash + dedup with hash sets | Medium/Hard |
| 4 | [Longest Duplicate Substring](problem-04-longest-duplicate-substring/PROBLEM.md) | Binary search on length + double hashing | Hard |
| 5 | [Longest Common Subpath](problem-05-longest-common-subpath/PROBLEM.md) | Binary search + double hashing across many arrays | Hard |
