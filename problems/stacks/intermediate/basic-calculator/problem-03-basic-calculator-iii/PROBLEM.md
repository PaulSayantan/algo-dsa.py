# Basic Calculator III

**Difficulty:** Medium

**Source:** LeetCode 772 — Basic Calculator III

## Description

Given a string `s` representing a valid arithmetic expression, evaluate it and return its integer value. The expression may contain non-negative integers, the operators `+`, `-`, `*`, `/`, and parentheses `( )`. Multiplication and division have higher precedence than addition and subtraction, integer division truncates toward zero, and parentheses may be nested. Spaces may appear anywhere in the string.

This combines the precedence handling of Basic Calculator II with the nested parentheses of Basic Calculator.

## Examples

### Example 1

```
Input:  s = "6-4/2"
Output: 4
```

**Explanation:** `4 / 2 = 2` binds first, then `6 - 2 = 4`.

### Example 2

```
Input:  s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
```

**Explanation:** The parenthesized groups evaluate to `15` and `11`; `2 * 15 / 3 = 10`, then `10 + 11 = 21`.

## Hint

Reuse the term-stack calculator, but when you hit `(` recurse (or push context) to evaluate the sub-expression first, treating its result as a single operand for the pending operator.
