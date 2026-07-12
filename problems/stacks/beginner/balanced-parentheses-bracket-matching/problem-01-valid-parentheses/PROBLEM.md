# Valid Parentheses

**Difficulty:** Easy

**Source:** LeetCode 20 — Valid Parentheses

## Description

Given a string `s` containing just the characters `()[]{}`, determine if the input string is valid. Brackets must be closed by the same type and in the correct order, and every closer must match an opener.

## Examples

### Example 1

```
Input:  s = "()[]{}"
Output: true
```

### Example 2

```
Input:  s = "(]"
Output: false
```

## Hint

Push openers; on a closer, the popped top must be the matching opener. Empty stack at end = valid.
