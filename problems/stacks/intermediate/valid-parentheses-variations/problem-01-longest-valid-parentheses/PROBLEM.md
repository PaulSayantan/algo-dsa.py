# Longest Valid Parentheses

**Difficulty:** Hard

**Source:** LeetCode 32 — Longest Valid Parentheses

## Description

Given a string `s` containing just `(` and `)`, return the length of the longest valid (well-formed) parentheses substring.

## Examples

### Example 1

```
Input:  s = ")()())"
Output: 4
```

## Hint

Stack of indices seeded with -1; push '(' indices, on ')' pop and measure i - new-top.
