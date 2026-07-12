# Determine if Two Strings Are Close

**Difficulty:** Medium

**Source:** LeetCode 1657 — Determine if Two Strings Are Close

## Description

Two strings are *close* if you can turn one into the other using: (1) swapping any two existing characters, and (2) transforming every occurrence of one existing character into another existing character (and vice versa). Given `word1` and `word2`, return whether they are close.

## Examples

### Example 1

```
Input:  word1 = "cabbba", word2 = "abbccc"
Output: true
```

### Example 2

```
Input:  word1 = "a", word2 = "aa"
Output: false
```

## Hint

Close iff they use exactly the same set of characters AND the sorted lists of their frequencies match.
