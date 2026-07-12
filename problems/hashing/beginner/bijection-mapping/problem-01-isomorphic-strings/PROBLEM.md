# Isomorphic Strings

**Difficulty:** Easy

**Source:** LeetCode 205 — Isomorphic Strings

## Description

Given two strings `s` and `t`, determine if they are isomorphic. They are isomorphic if the characters in `s` can be replaced to get `t`, where each character maps to exactly one character and no two characters map to the same character (order is preserved).

## Examples

### Example 1

```
Input:  s = "egg", t = "add"
Output: true
```

### Example 2

```
Input:  s = "foo", t = "bar"
Output: false
```

## Hint

Keep forward and backward maps; a new pair is only valid if it agrees with both.
