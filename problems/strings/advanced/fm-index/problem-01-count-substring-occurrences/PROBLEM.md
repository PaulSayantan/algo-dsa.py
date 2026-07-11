# Count Substring Occurrences

**Difficulty:** Medium

Source: Classic full-text indexing problem (Ferragina–Manzini FM-Index; SPOJ-style
"substring count" queries)

## Description

You are given a fixed text `T` of length `n` and a list of query patterns. For
each pattern `P`, return the number of times `P` occurs in `T` as a contiguous
substring. Occurrences may **overlap** (in `"aaaa"` the pattern `"aa"` occurs 3
times, at indices 0, 1, and 2).

The text is fixed and there can be **many** queries, so you should build one
index over `T` first and then answer each query in time proportional to the
pattern length — independent of `n`. This is exactly what an **FM-Index**
supports through *backward search*.

Design a class that is constructed once from `T` and exposes a `count(P)` method.

## Constraints

- `1 <= n <= 2 * 10^5`
- The total length of all query patterns is at most `2 * 10^5`.
- `T` and every `P` consist of lowercase English letters (or a small alphabet).
- A pattern that is longer than `T`, or that never appears, has a count of `0`.
- The empty pattern is not queried.

## Examples

### Example 1
```
Input:
  T = "mississippi"
  queries = ["issi", "ss", "i", "ppi", "ab"]
Output:
  [2, 2, 4, 1, 0]
Explanation:
  "issi" starts at indices 1 and 4  -> 2
  "ss"   starts at indices 2 and 5  -> 2
  "i"    appears at indices 1,4,7,10 -> 4
  "ppi"  starts at index 8          -> 1
  "ab"   never appears              -> 0
```

### Example 2
```
Input:
  T = "banana"
  queries = ["ana", "na", "a", "x"]
Output:
  [2, 2, 3, 0]
Explanation:
  "ana" occurs at indices 1 and 3 (overlapping) -> 2
  "na"  occurs at indices 2 and 4               -> 2
  "a"   occurs at indices 1, 3, 5               -> 3
  "x"   is not in the text                      -> 0
```

## Hint

Build the **FM-Index**: append a sentinel `$`, take the **Burrows–Wheeler
Transform**, and precompute the `C[]` table and the rank (`Occ`) table. Then run
**backward search**, scanning the pattern right to left and shrinking a suffix
interval `[sp, ep)`. The answer is `ep - sp` at the end.
