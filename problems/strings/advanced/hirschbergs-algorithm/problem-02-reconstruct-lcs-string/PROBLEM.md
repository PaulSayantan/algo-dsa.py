# Reconstruct the Longest Common Subsequence String

**Difficulty:** Medium

**Source:** Classic (CLRS 15.4 "Longest Common Subsequence"; the linear-space variant is Hirschberg 1975)

## Description

Given two strings `a` and `b`, return **an actual longest common subsequence string**
(not merely its length). If several LCS strings tie for the maximum length, returning any
one of them is acceptable. If the strings share no characters, return the empty string.

The catch: you must reconstruct the subsequence using only **`O(min(len(a), len(b)))`
extra space**. The usual trick — build the full `O(n·m)` table and walk backwards through
it — is disallowed, because for very long strings the table does not fit in memory.

This is the canonical problem Hirschberg's algorithm was designed for: recovering the
alignment itself, in linear space, by divide and conquer.

## Constraints

- `0 <= len(a), len(b) <= 5000`
- `a` and `b` consist of printable ASCII characters.
- Extra space (beyond the inputs and the returned string) must be
  `O(min(len(a), len(b)))`. You may **not** materialise the full 2-D DP table.

## Examples

### Example 1
```
Input:  a = "abcde", b = "ace"
Output: "ace"
Explanation: "ace" appears in both strings in order and has length 3, the maximum
possible. No length-4 common subsequence exists.
```

### Example 2
```
Input:  a = "AGGTAB", b = "GXTXAYB"
Output: "GTAB"
Explanation: G, T, A, B appear in that relative order in both strings. Length 4 is
optimal; there is no length-5 common subsequence.
```

### Example 3
```
Input:  a = "abc", b = "def"
Output: ""
Explanation: The strings share no characters, so the only common subsequence is empty.
```

## Hint

Compute forward LCS-length scores for the top half of `a` and backward scores for the
bottom half; the column where the two score rows sum to a maximum tells you where an
optimal subsequence crosses the middle row. Split there and recurse — this divide-and-
conquer reconstruction is **Hirschberg's Algorithm**.
