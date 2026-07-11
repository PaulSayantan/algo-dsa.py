# Bit-mask / Bitset String Matching (Shift-And / Shift-Or)

**Category:** Strings / Intermediate

## What it is

Shift-And and Shift-Or are **bit-parallel** string-matching algorithms. Instead of
comparing characters one at a time, they pack the "matching state" of a pattern into
the bits of a single machine word and advance *all* prefixes of the pattern
simultaneously using a shift, an OR/AND, and a table lookup per text character.

The core object is a **state bitmask** `D` of `m` bits (where `m = len(pattern)`).
Bit `j` of `D` is set when the first `j+1` characters of the pattern currently match
the text ending at the current position. Reading a text character `c` updates the
whole word at once:

```
Shift-And:  D = ((D << 1) | 1) & B[c]      # match reported when bit (m-1) is set
Shift-Or:   D = (D << 1) | B[c]            # (complemented bits) match when bit (m-1) is 0
```

`B[c]` is a precomputed **character mask**: bit `j` is set iff `pattern[j] == c`
(Shift-And convention). The `| 1` (Shift-And) seeds a new potential match starting at
every position. When the highest bit reaches the "match bit" `1 << (m-1)`, a full
occurrence has been found ending at the current index.

## When to reach for it

- The pattern is **short** — it fits in one (or a few) machine words, i.e. `m <= 64`
  (or `m <= word_size`). This is the sweet spot; Python big-ints extend it painlessly.
- You want **simple, branch-light** code that is easy to extend.
- You need **flexible matching**, which is where it truly shines and beats KMP/Z:
  - single-character **wildcards** (`?`) — just OR the wildcard positions into every mask,
  - **character classes** (`[a-c]`) — set multiple bits in the masks,
  - **approximate matching**: `k` mismatches (Hamming) via a stack of `k+1` bitmasks,
    or `k` edits (insert/delete/substitute) via the **Wu-Manber** recurrence.

For very long patterns or when only exact matching is needed on large alphabets,
KMP / Aho-Corasick / suffix automata are the more standard tools.

## Complexity

Let `n = len(text)`, `m = len(pattern)`, `sigma = alphabet size`, `w = machine word bits`.

| Task | Time | Space |
|------|------|-------|
| Preprocess masks | `O(m + sigma)` | `O(sigma * ceil(m/w))` |
| Exact match (Shift-And/Or) | `O(n * ceil(m/w))` | `O(sigma * ceil(m/w))` |
| Wildcard `?` / classes | `O(n * ceil(m/w))` | same |
| `k`-mismatch (Hamming) | `O(n * k * ceil(m/w))` | `O(k * ceil(m/w))` |
| `k`-edit (Wu-Manber) | `O(n * k * ceil(m/w))` | `O(k * ceil(m/w))` |

When `m <= w` (the common case) every per-character update is `O(1)`, so exact
matching runs in `O(n)` time overall after `O(m + sigma)` preprocessing.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Implement strStr()](problem-01-implement-strstr/PROBLEM.md) | Find the first index where a pattern occurs in a text | Easy |
| 2 | [Count All Occurrences](problem-02-count-all-occurrences/PROBLEM.md) | Report every (possibly overlapping) start index of a pattern | Easy |
| 3 | [Wildcard `?` Pattern Search](problem-03-wildcard-question-matching/PROBLEM.md) | Substring search where `?` matches any single character | Medium |
| 4 | [k-Mismatch Search (Hamming)](problem-04-k-mismatch-search/PROBLEM.md) | Find windows equal to the pattern up to `k` substitutions | Medium |
| 5 | [Fuzzy Substring Search (Wu-Manber)](problem-05-fuzzy-search-wu-manber/PROBLEM.md) | Find substrings within edit distance `k` of the pattern | Hard |
