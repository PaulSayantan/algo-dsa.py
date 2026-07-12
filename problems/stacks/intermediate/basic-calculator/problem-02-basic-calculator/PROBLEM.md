# Basic Calculator

**Difficulty:** Hard

**Source:** LeetCode 224 — Basic Calculator

## Description

Given a string `s` representing a valid expression with non-negative integers, `+`, `-`, and parentheses `( )` (no `*`/`/`), evaluate it. Spaces may appear. Parentheses may be nested.

## Examples

### Example 1

```
Input:  s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

## Hint

Keep a running result and sign; on '(' push (result, sign) and reset; on ')' pop and combine.
