# Rolling Hash / Polynomial Hashing

**Polynomial hashing** maps a string to a single integer by treating its
characters as the digits of a base-`B` number taken modulo a large prime `M`:

```
hash(s) = ( s[0]·B^(L-1) + s[1]·B^(L-2) + ... + s[L-1]·B^0 ) mod M
```

Two things make this idea powerful:

1. **Rolling** — when a fixed-width window slides one step to the right you can
   update its hash in `O(1)` by dropping the outgoing character's weighted
   contribution and folding in the incoming one. This is what Rabin–Karp uses
   for pattern search.

2. **Prefix hashes** — precompute `H[i] = hash(s[0..i-1])` for every prefix in
   `O(n)`. Then the hash of *any* substring `s[l..r]` is obtained in `O(1)`:

   ```
   hash(s[l..r]) = ( H[r+1] - H[l]·B^(r-l+1) ) mod M
   ```

   With prefix hashes you get an **O(1) equality test for any two substrings**,
   which unlocks a family of problems that plain rolling-window Rabin–Karp does
   not naturally cover.

## When to reach for it

- **O(1) "are these two substrings equal?" queries** after `O(n)` preprocessing.
- **Deduplicating substrings** (count/collect distinct substrings) by storing
  their hashes in a set instead of the substrings themselves — `O(1)` per
  substring instead of `O(length)`.
- **Binary search on an answer length** `L`: "does a good substring of length
  `L` exist?" is monotone, and each check hashes all length-`L` windows in
  `O(n)`. Total `O(n log n)`. This is the standard route for *longest duplicate
  substring*, *longest common substring of two strings*, and similar.
- **Palindrome checks in O(1)**: hash the string forward and reversed; a
  substring is a palindrome iff its forward hash equals its reverse hash.

## Complexity

| Operation | Cost |
| --- | --- |
| Build prefix hashes | `O(n)` time, `O(n)` space |
| Hash of one substring `s[l..r]` | `O(1)` |
| Compare two substrings | `O(1)` (probabilistic) |
| Binary search on length + per-check hashing | `O(n log n)` |

Because distinct strings can share a hash (a **collision**), a single 64-bit
prime gives a tiny but nonzero error probability. In practice use a large prime
(e.g. `2^61 - 1`) or **double hashing** (two independent `(B, M)` pairs, compare
the pair) to drive the collision probability to negligible, and verify
character-by-character when exact correctness is required.

## Problems

| # | Problem | Technique focus | Difficulty |
| --- | --- | --- | --- |
| 1 | [Substring Equality Queries](problem-01-substring-equality-queries/PROBLEM.md) | Prefix hashes → O(1) substring equality | Easy |
| 2 | [Count Distinct Substrings](problem-02-count-distinct-substrings/PROBLEM.md) | Hash-set dedup over all substrings | Medium |
| 3 | [Maximum Length of Repeated Subarray](problem-03-maximum-length-of-repeated-subarray/PROBLEM.md) | Binary search on length + hashing | Medium |
| 4 | [Shortest Palindrome](problem-04-shortest-palindrome/PROBLEM.md) | Forward vs. reverse rolling hash | Hard |
| 5 | [Longest Duplicate Substring](problem-05-longest-duplicate-substring/PROBLEM.md) | Binary search on length + prefix-hash dedup | Hard |
