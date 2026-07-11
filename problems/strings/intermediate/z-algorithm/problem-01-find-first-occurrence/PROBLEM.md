# Find the Index of the First Occurrence in a String

**Difficulty:** Easy

**Source:** LeetCode 28 — "Find the Index of the First Occurrence in a String" (classic `strStr()`).

## Description

Given two strings `haystack` and `needle`, return the index of the **first
occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of
`haystack`.

This is the canonical substring-search problem. A naive scan is `O(n * m)`; the
goal here is to solve it in linear `O(n + m)` time. The idiomatic linear
approach with the Z-Algorithm is to build one combined string
`needle + separator + haystack` (the separator being a character that appears in
neither input), compute its Z-array, and look for any position whose Z-value
equals `len(needle)` — that means the full needle re-appears there as a prefix.

## Constraints

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English letters.

## Examples

### Example 1

```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and also at index 6. The first occurrence
is at index 0, so we return 0.
```

### Example 2

```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" never appears as a contiguous substring of "leetcode", so
we return -1.
```

### Example 3

```
Input:  haystack = "abcabcabca", needle = "abcabca"
Output: 0
Explanation: The needle matches starting at index 0 (it also has an overlapping
match starting at index 3, but 0 is first).
```

## Hint

Use the **Z-Algorithm**. Concatenate `needle + '#' + haystack` (with a
separator absent from both), compute the Z-array, and scan for a Z-value equal
to the needle's length.
