# Implement strStr()

**Difficulty:** Easy

**Source:** LeetCode 28 — "Find the Index of the First Occurrence in a String"

## Description

Given two strings `haystack` and `needle`, return the index of the **first
occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of
`haystack`.

This is the canonical substring-search problem. A brute-force scan is
`O(n * m)` in the worst case (for example a haystack of all `a`s and a needle
of many `a`s followed by a `b`). Your job is to match in linear time.

Note the standard convention: if `needle` is the empty string, the answer is
`0` (the empty string occurs at index 0 of any string).

## Constraints

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

## Examples

### Example 1

```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and also at index 6.
             The first occurrence is at index 0.
```

### Example 2

```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" never occurs in "leetcode", so we return -1.
```

### Example 3

```
Input:  haystack = "hello", needle = "ll"
Output: 2
Explanation: "ll" starts at index 2 of "hello".
```

## Hint

Precompute a failure function (the **LPS array**) for `needle`, then scan
`haystack` once without ever moving the text pointer backward. This is exactly
**KMP (Knuth–Morris–Pratt)**.
