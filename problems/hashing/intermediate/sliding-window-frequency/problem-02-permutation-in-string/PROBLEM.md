# Permutation in String

**Difficulty:** Medium

**Source:** LeetCode 567 — Permutation in String

## Description

Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1` as a contiguous substring, otherwise `False`. Equivalently, some length-`len(s1)` window of `s2` has the same character frequencies as `s1`.

## Examples

### Example 1

```
Input:  s1 = "ab", s2 = "eidbaooo"
Output: true
```

**Explanation:** s2 contains "ba", a permutation of "ab".

### Example 2

```
Input:  s1 = "ab", s2 = "eidboaoo"
Output: false
```

## Hint

Fixed window of len(s1); return True as soon as the window Counter equals Counter(s1).
