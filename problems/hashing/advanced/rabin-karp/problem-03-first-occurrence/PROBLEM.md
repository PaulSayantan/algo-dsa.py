# Find the Index of the First Occurrence in a String

**Difficulty:** Easy

**Source:** LeetCode 28 — Find the Index of the First Occurrence in a String

## Description

Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`. By convention an empty `needle` returns `0`. Solve it with the Rabin-Karp rolling hash.

## Examples

### Example 1

```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
```

### Example 2

```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
```

## Hint

Return the first index from the rolling-hash match scan; empty needle -> 0.
