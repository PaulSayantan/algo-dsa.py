# Postfix to Infix Conversion

**Difficulty:** Easy

**Source:** Classic — postfix (RPN) to fully parenthesized infix

## Description

Given a valid postfix expression as a string `expression`, convert it to its **fully parenthesized infix** form. Each operand is a single character (a letter or digit) and the valid operators are `+`, `-`, `*`, `/`. In the result, every operator combines its two operands wrapped in a single pair of parentheses, e.g. `a` and `b` combined with `*` become `(a*b)`.

The input is guaranteed to be a well-formed postfix expression with no spaces. A lone operand converts to itself (no parentheses).

## Examples

### Example 1

```
Input:  expression = "ab+"
Output: "(a+b)"
```

**Explanation:** `+` pops `a` and `b` and forms `(a+b)`.

### Example 2

```
Input:  expression = "abc*+"
Output: "(a+(b*c))"
```

**Explanation:** `*` forms `(b*c)`; then `+` combines `a` with `(b*c)` to give `(a+(b*c))`.

## Hint

Evaluate the postfix stream with a stack, but push partial infix strings instead of numbers: on an operator pop `b` then `a` and push `"(" + a + op + b + ")"`.
