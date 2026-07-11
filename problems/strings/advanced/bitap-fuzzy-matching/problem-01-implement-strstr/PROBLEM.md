# Implement strStr()

**Difficulty:** Easy

**Source:** LeetCode 28 — "Find the Index of the First Occurrence in a String" (classic substring search)

## Description

Given two strings `haystack` and `needle`, return the index of the **first** occurrence of `needle` in
`haystack`, or `-1` if `needle` is not part of `haystack`.

This is the exact-matching warm-up for the Bitap family. Instead of the usual naive scan or KMP, solve it with the
**shift-or** formulation of Bitap: encode "which pattern prefixes currently match a suffix of the text read so
far" as the bits of a single integer, and advance that integer one text character at a time with a shift, an OR,
and an AND against a precomputed character mask. When the bit corresponding to the last pattern position turns on,
you have found a full occurrence ending at the current index.

If `needle` is the empty string, return `0` (an empty needle occurs at position `0`).

## Constraints

- `0 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English letters.
- You should aim for `O(n)` search time when `|needle|` fits in a machine word (which it does for these limits on
  a 64-bit machine only for very short needles; for the general case a multi-word register or the standard
  `O(n·⌈m/w⌉)` bound applies).

## Examples

### Example 1
```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
```
Explanation: `"sad"` occurs at index `0` and again at index `6`. The first occurrence is index `0`, so the shift-or
register lights its top bit for the first time when the text position reaches the end of the first `"sad"`.

### Example 2
```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
```
Explanation: `"leeto"` never appears; the register's top bit is never set, so we return `-1`.

### Example 3
```
Input:  haystack = "mississippi", needle = "issip"
Output: 4
```
Explanation: `"issip"` matches starting at index `4` (`m i s s [i s s i p] p i`). The match ends at index `8`, so
the reported start index is `8 - 5 + 1 = 4`.

## Hint

Use the **Bitap / Fuzzy Matching** shift-or idea: build a bitmask `peq[c]` per character, keep one register `R`,
and update `R = ((R << 1) | 1) & peq[c]` for each text character. A full match is signalled by the top bit
(`1 << (m-1)`) of `R`.
