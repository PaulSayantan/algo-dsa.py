# Valid Parentheses

**Difficulty:** Easy

**Source:** LeetCode 20 — Valid Parentheses

## Description

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine whether the input string is valid.

A string is valid when every open bracket is closed by the *same* type of bracket, and brackets close in the correct (last-opened-first-closed) order. Return `True` if `s` is valid, otherwise `False`. An empty string is valid.

## Examples

### Example 1

```
Input:  s = "()"
Output: true
```

**Explanation:** The single pair matches.

### Example 2

```
Input:  s = "([)]"
Output: false
```

**Explanation:** `)` closes before the inner `[` is closed, violating LIFO order.

## Hint

Push each opening bracket onto an array-based stack; on a closing bracket, pop and check it matches the most recent open.
