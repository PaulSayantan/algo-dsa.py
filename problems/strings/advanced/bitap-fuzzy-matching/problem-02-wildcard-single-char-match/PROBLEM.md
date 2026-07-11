# Wildcard Single-Character Match

**Difficulty:** Easy

**Source:** Classic pattern-matching exercise (the single-character wildcard subset of glob / `fnmatch`,
solvable with Bitap). Related to LeetCode 44 "Wildcard Matching" restricted to the `?` operator.

## Description

You are given a text `text` and a pattern `pattern`. The pattern may contain the wildcard character `?`, which
matches **any single character**. Every other character in the pattern must match literally. There is no `*`
(multi-character) wildcard in this problem — each pattern position consumes exactly one text character.

Return a list of all **start indices** `i` (in increasing order) such that `pattern` matches the substring
`text[i : i + len(pattern)]`, where each `?` matches whatever character sits at that position.

The Bitap angle: a `?` at pattern position `j` should *always* be considered a match at bit `j`, regardless of
the incoming text character. You achieve this by folding a "wildcard mask" (bits for every `?` position) into the
per-character mask, so the AND step never clears those bits.

## Constraints

- `1 <= text.length <= 10^5`
- `1 <= pattern.length <= 64` (the pattern fits in a single 64-bit machine word).
- `text` consists of lowercase English letters.
- `pattern` consists of lowercase English letters and the wildcard character `?`.
- Return the start indices in ascending order; return an empty list if there is no match.

## Examples

### Example 1
```
Input:  text = "abcabcabc", pattern = "a?c"
Output: [0, 3, 6]
```
Explanation: `a?c` matches `"abc"` at index 0, `"abc"` at index 3, and `"abc"` at index 6 — the middle `?`
absorbs the `b` each time.

### Example 2
```
Input:  text = "mississippi", pattern = "?ss"
Output: [1, 4]
```
Explanation: Indexing `text` as `m(0) i(1) s(2) s(3) i(4) s(5) s(6) i(7) p(8) p(9) i(10)`, the pattern `?ss`
requires two consecutive `s` characters at positions `i+1` and `i+2`. That happens at start index `1`
(`text[1:4] = "iss"`, `?`→`i`) and start index `4` (`text[4:7] = "iss"`, `?`→`i`). No other start position has
`ss` in its last two slots, so the answer is `[1, 4]`.

### Example 3
```
Input:  text = "abcde", pattern = "x?z"
Output: []
```
Explanation: The literal `x` and `z` never line up with the text, so despite the wildcard there is no match
anywhere.

## Hint

Reuse the **Bitap / Fuzzy Matching** shift-and register, but precompute a `wildcard` mask with a bit set for every
`?` position and OR it into `peq[c]` on every step: `R = ((R << 1) | 1) & (peq[c] | wildcard)`.
