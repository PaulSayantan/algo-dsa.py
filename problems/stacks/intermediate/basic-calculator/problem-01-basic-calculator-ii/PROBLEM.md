# Basic Calculator II

**Difficulty:** Medium

**Source:** LeetCode 227 — Basic Calculator II

## Description

Given a string `s` representing a valid expression with non-negative integers and the operators `+ - * /` (no parentheses), evaluate it. Multiplication and division have higher precedence; integer division truncates toward zero. Spaces may appear.

## Examples

### Example 1

```
Input:  s = "3+2*2"
Output: 7
```

### Example 2

```
Input:  s = " 3+5 / 2 "
Output: 5
```

## Hint

Track last-number and a pending op; on * and / update the top of a stack, then sum.
