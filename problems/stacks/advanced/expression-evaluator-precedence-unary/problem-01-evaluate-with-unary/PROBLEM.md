# Evaluate Expression with Unary Minus

**Difficulty:** Hard

**Source:** Classic — two-stack calculator with unary operators

## Description

Evaluate an infix arithmetic expression string with `+ - * /`, parentheses, non-negative integer literals, spaces, and **unary minus** (e.g. `-3`, `2*(-4)`, `-(3+4)`). Division truncates toward zero. Return the integer result.

## Hint

Two stacks (values, ops); precedence-driven apply; treat '-' as unary at start/after '('/after an operator by pushing a 0 operand.
