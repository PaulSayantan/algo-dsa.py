# Find the Index of the First Occurrence in a String

**Difficulty:** Easy

**Source:** LeetCode 28 — "Find the Index of the First Occurrence in a String" (classic `strStr` / substring search)

## Description

Given two strings `haystack` and `needle`, return the index of the **first
occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of
`haystack`.

This is the canonical substring-search problem. A naive scan compares `needle`
against every starting position of `haystack`, costing `O(n·m)` in the worst
case. Rabin–Karp instead compares the hash of `needle` against the rolling hash
of each length-`m` window of `haystack`, giving expected `O(n + m)` time.

Note: if `needle` is the empty string, return `0` (the empty string occurs at
index 0 by convention).

## Constraints

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

## Examples

### Example 1

```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and also at index 6. The first occurrence is at index 0.
```

### Example 2

```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" never occurs in "leetcode", so the answer is -1.
```

### Example 3

```
Input:  haystack = "hello", needle = "ll"
Output: 2
Explanation: "ll" starts at index 2 in "hello".
```

## Hint

Compute a polynomial **rolling hash** of `needle` once, then slide a length-`m`
window across `haystack`, updating its hash in `O(1)` per step. Only when a
window's hash equals the pattern's hash do you verify the characters — this is
**Rabin–Karp**.
