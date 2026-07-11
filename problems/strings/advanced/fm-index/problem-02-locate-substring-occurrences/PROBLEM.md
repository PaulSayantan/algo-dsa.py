# Locate Substring Occurrences

**Difficulty:** Medium

Source: Classic full-text indexing problem (FM-Index `locate` query; equivalent
to "find all occurrences of a pattern in a text")

## Description

You are given a fixed text `T` of length `n` and query patterns. For each pattern
`P`, return the **sorted list of every start index** where `P` occurs in `T`.
Occurrences may overlap.

As with counting, the text is fixed and queries are many, so build one index over
`T` and answer each query in time proportional to the pattern length plus the
number of reported occurrences. An **FM-Index** does this: backward search gives
the contiguous block of suffix-array rows matching `P`, and the suffix array
converts those rows into text positions.

Design a class constructed once from `T` that exposes a `locate(P)` method
returning start indices in ascending order.

## Constraints

- `1 <= n <= 2 * 10^5`
- The total length of all query patterns is at most `2 * 10^5`.
- `T` and every `P` consist of lowercase English letters (or a small alphabet).
- Indices are 0-based.
- If `P` does not occur, return an empty list.

## Examples

### Example 1
```
Input:
  T = "mississippi"
  queries = ["issi", "ss", "i", "ppi"]
Output:
  [[1, 4], [2, 5], [1, 4, 7, 10], [8]]
Explanation:
  "issi" starts at 1 and 4.
  "ss"   starts at 2 and 5.
  "i"    appears at 1, 4, 7, 10.
  "ppi"  starts at 8.
```

### Example 2
```
Input:
  T = "aaaa"
  queries = ["aa", "aaa", "b"]
Output:
  [[0, 1, 2], [0, 1], []]
Explanation:
  "aa"  occurs (overlapping) at 0, 1, 2.
  "aaa" occurs at 0 and 1.
  "b"   never occurs, so the list is empty.
```

## Hint

Run **FM-Index backward search** to obtain the suffix-array interval `[sp, ep)`
matching `P`. Every row `i` in that interval gives a start position `SA[i]`.
Collect `SA[sp..ep)` and sort. (In a space-optimized index you would store only a
sampled suffix array and walk the **LF-mapping** until you hit a sampled row.)
