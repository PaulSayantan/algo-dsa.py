# Rabin–Karp (Rolling Hash)

**Rabin–Karp** is a string-matching algorithm that uses **hashing** to find a
pattern inside a text. Instead of comparing the pattern against every window of
the text character by character, it compares a single integer **hash** of the
pattern against the hash of each window. To make hashing every window cheap, it
uses a **rolling hash**: when the window slides one position to the right, the
new hash is computed from the old one in `O(1)` by removing the contribution of
the outgoing character and adding the contribution of the incoming character.

Because two different strings can share the same hash (a **collision**),
Rabin–Karp treats a hash match only as a *candidate*. It then either verifies
the candidate character-by-character (deterministic Rabin–Karp) or relies on a
carefully chosen large modulus / double hashing so that collisions are
astronomically unlikely (probabilistic / Monte-Carlo Rabin–Karp).

## The rolling hash (polynomial hash)

Treat a length-`L` window `s[i..i+L-1]` as a base-`B` number modulo a large
prime `M`:

```
hash(s[i..i+L-1]) = (s[i]*B^(L-1) + s[i+1]*B^(L-2) + ... + s[i+L-1]*B^0) mod M
```

Sliding the window from `i` to `i+1`:

```
new = ( (old - s[i]*B^(L-1)) * B + s[i+L] ) mod M
```

Every step is `O(1)`, so scanning the whole text is `O(n)`.

## When to reach for it

- **Single-pattern search** where you want simple average-case linear time.
- **Multiple-pattern search**: hash all patterns into a set, then hash each
  window once and check set membership — one pass finds all of them.
- **"Does substring X appear / repeat?"** style problems, especially combined
  with **binary search on the answer length** (e.g. longest duplicate substring).
- **Counting / deduplicating substrings** by storing their hashes in a set.

## Complexity

| | Time | Space |
|---|---|---|
| Preprocessing (pattern hash + powers) | `O(m)` | `O(1)` (or `O(k)` for `k` patterns) |
| Average / expected search | `O(n + m)` | `O(1)` |
| Worst case (adversarial, all hashes collide) | `O(n·m)` | `O(1)` |

Using a random base and a large prime modulus (or two moduli — "double hashing")
makes the worst case effectively unreachable in practice.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Find the Index of the First Occurrence in a String](problem-01-find-first-occurrence/PROBLEM.md) | Classic single-pattern rolling-hash search | Easy |
| 2 | [Repeated DNA Sequences](problem-02-repeated-dna-sequences/PROBLEM.md) | Hash every fixed-length window into a set | Medium |
| 3 | [Longest Happy Prefix](problem-03-longest-happy-prefix/PROBLEM.md) | Compare prefix hashes against suffix hashes | Hard |
| 4 | [Distinct Echo Substrings](problem-04-distinct-echo-substrings/PROBLEM.md) | Precompute prefix hashes; test `a+a` equality in `O(1)` | Hard |
| 5 | [Longest Duplicate Substring](problem-05-longest-duplicate-substring/PROBLEM.md) | Binary search on length + Rabin–Karp membership | Hard |
