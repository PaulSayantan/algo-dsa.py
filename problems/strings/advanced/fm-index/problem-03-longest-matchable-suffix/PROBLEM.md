# Longest Matchable Suffix

**Difficulty:** Medium

Source: Classic FM-Index application (partial backward search; the same idea
underlies "backward matching statistics" used in read alignment)

## Description

You are given a fixed text `T` and query patterns. Backward search naturally
processes a pattern **right to left**, one character at a time, and it keeps
matching as long as the current suffix of the pattern still occurs somewhere in
`T`.

For each query `P`, return the length of the **longest suffix of `P` that occurs
as a substring of `T`**. Formally, return the largest `L` such that
`P[len(P)-L : len(P)]` occurs in `T`. If not even the last character of `P`
appears in `T`, return `0`.

This is a single **partial backward search**: keep extending the match to the
left until the FM-Index interval would become empty, and report how many
characters you managed to match.

## Constraints

- `1 <= len(T) <= 2 * 10^5`
- `1 <= len(P) <= 2 * 10^5` per query; total query length `<= 2 * 10^5`.
- `T` and every `P` consist of lowercase English letters (or a small alphabet).
- The answer is an integer in `[0, len(P)]`.

## Examples

### Example 1
```
Input:
  T = "mississippi"
  P = "xsip"
Output:
  3
Explanation:
  Backward search from the right: "p" occurs, "ip" occurs, "sip" occurs, but
  "xsip" does not (there is no 'x' in T). The longest matchable suffix is "sip",
  of length 3.
```

### Example 2
```
Input:
  T = "mississippi"
  P = "ssis"
Output:
  4
Explanation:
  The entire pattern "ssis" occurs in T (starting at index 2: "ss i s" -> chars
  s,s,i,s), so its longest matchable suffix is the whole string, length 4.
```

### Example 3
```
Input:
  T = "mississippi"
  P = "xyz"
Output:
  0
Explanation:
  The last character 'z' does not occur in T at all, so backward search matches
  nothing. The longest matchable suffix has length 0.
```

## Hint

Run **FM-Index backward search** but do not stop at a failed full match. Process
`P` right to left, updating the interval `[sp, ep)`; each successful character
extends the matched suffix by one. Stop when the interval would become empty and
return the number of characters matched so far. This is a partial application of
the same LF-mapping used for counting.
