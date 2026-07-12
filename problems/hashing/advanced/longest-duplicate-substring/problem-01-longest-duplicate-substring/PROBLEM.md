# Longest Duplicate Substring

**Difficulty:** Hard

**Source:** LeetCode 1044 — Longest Duplicate Substring

## Description

Given a string `s`, a duplicated substring is a (contiguous) substring that occurs at least twice, possibly overlapping. Return the **length** of the longest duplicated substring (return `0` if none exists). The length is unique even though the substring achieving it may not be.

## Examples

### Example 1

```
Input:  s = "banana"
Output: 3
```

**Explanation:** "ana" (length 3) occurs twice

### Example 2

```
Input:  s = "abcd"
Output: 0
```

**Explanation:** no repeated substring

## Hint

Binary-search the length; for a fixed length, use rolling hashes to detect a repeat.
