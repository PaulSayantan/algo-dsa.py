# Evaluate Reverse Polish Notation

**Difficulty:** Medium

**Source:** LeetCode 150 — Evaluate Reverse Polish Notation

## Description

Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are `+`, `-`, `*`, `/`. Each operand is an integer. Division between two integers **truncates toward zero**. The input `tokens` is guaranteed to be a valid RPN expression.

## Examples

### Example 1

```
Input:  tokens = ["2","1","+","3","*"]
Output: 9
```

**Explanation:** ((2 + 1) * 3) = 9

### Example 2

```
Input:  tokens = ["4","13","5","/","+"]
Output: 6
```

**Explanation:** (4 + (13 / 5)) = 6

## Hint

Push integer tokens; on an operator, pop b then a, push a∘b. Use int(a/b) to truncate toward zero.
