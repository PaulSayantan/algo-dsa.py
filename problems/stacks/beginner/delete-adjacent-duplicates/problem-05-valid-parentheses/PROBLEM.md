# Valid Parentheses

**Difficulty:** Easy

**Source:** LeetCode 20 — Valid Parentheses

## Description

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, return `True` if the string is valid. A string is valid when every open bracket is closed by a matching bracket of the same type and brackets close in the correct order (each closing bracket cancels the most recently opened, still-unmatched one).

## Examples

### Example 1

```
Input:  s = "()[]{}"
Output: true
```

**Explanation:** Each closing bracket cancels the open bracket immediately before it, so the whole string collapses to empty.

## Hint

Push openers; when a closer matches the stack top, they form a canceling adjacent pair — pop it. Valid iff the stack empties.
