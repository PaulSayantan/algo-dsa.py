# Pratt-Parse and Evaluate (with Power)

**Difficulty:** Hard

**Source:** Classic — Pratt / precedence-climbing parser

## Description

Evaluate an infix expression over non-negative integers with `+ - * /` (left-associative) and `^` (exponentiation, **right**-associative, highest precedence), plus parentheses. Use precedence-climbing / Pratt parsing. Division truncates toward zero. Return the integer result.

## Examples

### Example 1

```
Input:  s = "2 ^ 3 ^ 2"
Output: 512
```

**Explanation:** Right-assoc: 2^(3^2)=2^9=512.

## Hint

Recurse with a min-binding-power; '^' has higher power and recurses with a lower right-bp (right-assoc).
