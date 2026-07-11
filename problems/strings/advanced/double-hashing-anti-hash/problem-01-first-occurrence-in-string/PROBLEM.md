# Find the Index of the First Occurrence in a String

**Difficulty:** Easy

**Source:** LeetCode 28 — Find the Index of the First Occurrence in a String (classic Rabin-Karp string matching)

## Description

Given two strings `haystack` and `needle`, return the index of the first
occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of
`haystack`.

While this can be solved with the naive `O(n*m)` scan or the KMP automaton, the
goal here is to practice **Rabin-Karp**: slide a window of length `len(needle)`
across `haystack`, keep a rolling polynomial hash of the window, and compare it
against the hash of `needle`. Because a single modulus can be forced to collide,
use a hash strong enough (two moduli) that a hash match reliably means a real
match — optionally verify a raw character comparison only when the hashes agree.

## Constraints

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

## Examples

**Example 1**

```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and index 6. The first occurrence is at index 0.
```

**Example 2**

```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" never occurs in "leetcode", so we return -1.
```

**Example 3**

```
Input:  haystack = "hello", needle = "ll"
Output: 2
Explanation: "ll" first appears starting at index 2.
```

## Hint

Use **Double Hashing / Anti-Hash**: hash the needle once, then roll a
two-modulus polynomial hash across every window of `haystack` and report the
first window whose hash pair equals the needle's.
