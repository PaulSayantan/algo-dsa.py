# Evaluate Infix Arithmetic Expression

**Difficulty:** Medium

**Source:** Classic — Shunting-Yard two-stack evaluation

## Description

Given a string `expr` holding a valid arithmetic expression of non-negative integers, the binary operators `+ - * /`, parentheses `( )`, and optional spaces, evaluate it and return the integer result. `*` and `/` bind tighter than `+` and `-`; all four are left-associative. Division truncates toward zero (Python `int(a / b)` semantics). The expression is guaranteed well-formed and never divides by zero.

## Examples

### Example 1

```
Input:  expr = "3+4*2"
Output: 11
```

**Explanation:** `4*2` evaluates first (higher precedence), then `3+8`.

## Hint

Run shunting-yard but instead of emitting tokens, keep a value stack alongside the operator stack: whenever you would pop an operator, apply it to the top two values.
