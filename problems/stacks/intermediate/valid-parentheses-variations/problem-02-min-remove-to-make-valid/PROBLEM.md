# Minimum Remove to Make Valid Parentheses

**Difficulty:** Medium

**Source:** LeetCode 1249 — Minimum Remove to Make Valid Parentheses

## Description

Given a string `s` of `(`, `)`, and lowercase letters, remove the minimum number of parentheses so the result is valid, and return any valid result. (This reference removes unmatched parens deterministically, left to right.)

## Examples

### Example 1

```
Input:  s = "a)b(c)d"
Output: "ab(c)d"
```

## Hint

Stack the indices of unmatched '('; mark unmatched ')' for removal; drop leftover '(' indices.
