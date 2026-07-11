# Bitap / Fuzzy Matching

**Bitap** (also called the **shift-or / shift-and algorithm**, or the **Baeza-Yates–Gonnet algorithm**) is a
string-matching technique that encodes the *state of the search* as the bits of a machine word and advances the
whole search one text character at a time using a handful of bitwise operations. Because a single CPU word holds
`w` bits (typically 32 or 64), the algorithm processes up to `w` pattern positions **in parallel** — this trick is
called **bit-parallelism**.

The reason Bitap matters is its **approximate (fuzzy) matching** extension, due to Wu and Manber: with a small
constant factor of extra work it finds every place where the pattern occurs allowing up to `k` **errors**
(substitutions for Hamming distance, or insertions/deletions/substitutions for Levenshtein/edit distance). This is
exactly what tools like GNU `agrep` and many "did you mean?" / fuzzy-find features are built on.

## Core idea

Precompute, for each alphabet symbol `c`, a bitmask `peq[c]` whose bit `j` is set iff `pattern[j] == c`.
Maintain a state register `R` where bit `j` being "active" means *the pattern prefix of length `j+1` currently
matches a suffix of the text read so far*. For **shift-and** the update per text character `c` is:

```
R = ((R << 1) | 1) & peq[c]
```

A full match ends at the current position whenever the top bit (bit `m-1`) of `R` is set. For `k`-error matching
you keep `k+1` registers `R[0..k]`, where `R[d]` tracks matches using at most `d` errors, and combine them with a
recurrence that models substitution, insertion, and deletion as bit shifts/ORs.

## When to reach for it

- You need **approximate** substring search with a small edit bound `k` (spell-check, DNA reads, fuzzy find).
- The pattern is short — ideally `m <= w` (one machine word). Longer patterns need multi-word simulation.
- The alphabet is modest so the `peq` table is cheap to build.
- You want simple, cache-friendly code with no heavy preprocessing (unlike suffix automata / KMP failure tables).

## Complexity

Let `n = |text|`, `m = |pattern|`, `k = max errors`, `w = word size`, `σ = alphabet size`.

| Variant | Preprocessing | Search time | Extra space |
|---|---|---|---|
| Exact (shift-or/shift-and) | `O(m + σ)` | `O(n · ⌈m/w⌉)` → `O(n)` when `m ≤ w` | `O(σ · ⌈m/w⌉)` |
| Wildcard (`?` = any char) | `O(m + σ)` | `O(n)` when `m ≤ w` | `O(σ)` |
| `k`-mismatch (Hamming) | `O(m + σ)` | `O(n · k · ⌈m/w⌉)` → `O(n · k)` | `O(σ + k)` |
| `k`-edit (Levenshtein, Wu–Manber) | `O(m + σ)` | `O(n · k · ⌈m/w⌉)` → `O(n · k)` | `O(σ + k)` |

The classic dynamic-programming approach to the same problems costs `O(n · m)`; Bitap wins by packing a whole
column of the DP table into one word.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Implement strStr()](problem-01-implement-strstr/PROBLEM.md) | Exact match via shift-or (warm-up) | Easy |
| 2 | [Wildcard single-character match](problem-02-wildcard-single-char-match/PROBLEM.md) | `?`-wildcards folded into the bitmask | Easy |
| 3 | [k-mismatch substring search](problem-03-k-mismatch-substring-search/PROBLEM.md) | Bitap under Hamming distance | Medium |
| 4 | [Approximate search within k edits](problem-04-approximate-search-k-edits/PROBLEM.md) | Wu–Manber Levenshtein Bitap | Hard |
| 5 | [Best fuzzy match (minimum edits)](problem-05-best-fuzzy-match-min-edits/PROBLEM.md) | Bitap as an edit-distance oracle | Hard |

Work through them in order — each layers one more idea onto the register update of the previous one.
