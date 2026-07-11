# Implement strStr()

**Difficulty:** Easy

**Source:** LeetCode 28 — Find the Index of the First Occurrence in a String

## Description

Given two strings `haystack` and `needle`, return the index of the **first occurrence**
of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

This is the canonical string-search problem: you must locate where one string appears
inside another and report the starting index of the earliest match.

## Constraints

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English letters.

## Examples

### Example 1

```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
```

**Explanation:** `"sad"` occurs at index `0` and again at index `6`. The first
occurrence is at index `0`, so we return `0`.

### Example 2

```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
```

**Explanation:** `"leeto"` never appears in `"leetcode"` (the run `"leet"` matches but
the following character is `'c'`, not `'o'`), so we return `-1`.

### Example 3

```
Input:  haystack = "hello", needle = "ll"
Output: 2
```

**Explanation:** Sliding `"ll"` over `"hello"`, the first full match starts at index `2`
(`h e [l l] o`).

## Hint

Use **Naive Pattern Matching**: try aligning `needle` at each starting index of
`haystack` and compare character by character. Return the first alignment that matches
all `len(needle)` characters.
