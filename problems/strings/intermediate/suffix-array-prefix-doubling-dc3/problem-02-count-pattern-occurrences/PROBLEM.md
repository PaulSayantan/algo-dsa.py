# Count Pattern Occurrences

**Difficulty:** Medium

**Source:** Classic string-matching task (CP-Algorithms "Applications of Suffix Array"; equivalent to many "count substring occurrences" judge problems).

## Description

You are given a text `S` of length `n` and then `q` query patterns
`P_1, P_2, ..., P_q`. For each pattern `P`, return the number of times `P` occurs
in `S` as a (possibly overlapping) contiguous substring.

The point is that `S` is **fixed** and there are **many** queries, so you should
preprocess `S` once (build its suffix array) and then answer each query quickly.

**Key observation.** Every occurrence of `P` in `S` is the prefix of exactly one
suffix of `S`. In the suffix array the suffixes are sorted, so all suffixes that
start with `P` form a **contiguous block**. The count for `P` is the size of that
block, which you can find with two binary searches (lower and upper bound).

Return a list with one integer per query, in the same order.

## Constraints

- `1 <= n <= 2 * 10^5`
- `1 <= q <= 2 * 10^5`
- `1 <= len(P_i) <= n`
- Total length of all patterns fits comfortably in memory.
- Occurrences may overlap and each is counted.

## Examples

### Example 1
```
Input:  S = "banana", queries = ["ana", "na", "x"]
Output: [2, 2, 0]
Explanation:
  "ana" occurs at indices 1 and 3 ("b[ana]na" and "ban[ana]") -> 2 (they overlap, both counted).
  "na"  occurs at indices 2 and 4 -> 2.
  "x"   does not occur -> 0.
```

### Example 2
```
Input:  S = "mississippi", queries = ["issi", "ss", "i"]
Output: [2, 2, 4]
Explanation:
  "issi" occurs at indices 1 and 4 -> 2 (overlapping: "m[issi]ssippi" and "miss[issi]ppi").
  "ss"   occurs at indices 2 and 5 -> 2.
  "i"    occurs at indices 1, 4, 7, 10 -> 4.
```

### Example 3
```
Input:  S = "aaaa", queries = ["aa", "aaaa", "aaaaa"]
Output: [3, 1, 0]
Explanation:
  "aa"    starts at indices 0, 1, 2 -> 3.
  "aaaa"  starts only at index 0 -> 1.
  "aaaaa" is longer than S -> 0.
```

## Hint

Use **Suffix Array (prefix-doubling / DC3)**. Because sorted suffixes that share
the prefix `P` are contiguous, binary-search for the first and last suffix whose
prefix equals `P`; the count is `upper - lower`.
