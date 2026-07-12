# Prefix to Postfix Conversion

**Difficulty:** Easy

**Source:** Classic — prefix (Polish) to postfix (Reverse Polish) conversion

## Description

Given a string `expr` holding a valid prefix (Polish) arithmetic expression, convert it to postfix (Reverse Polish) notation. Operators are `+ - * /` and every operand is a single character. In prefix notation the operator comes before its two operands, so scan **right to left** with a stack: push operands, and on an operator pop the top two — the **first** popped is the left operand — and push the combined string `left + right + op`. The final stack entry is the postfix form.

Constraints: `expr` is a valid prefix expression, every operator is binary, `1 <= len(expr) <= 10^4`.

## Examples

### Example 1

```
Input:  expr = "*-AB/CD"
Output: AB-CD/*
```

**Explanation:** `-AB` becomes `AB-`, `/CD` becomes `CD/`, and the outer `*` appends to both to give `AB-CD/*`.

## Hint

Scan the tokens reversed; on an operator pop left then right and push `left + right + op` (operator last).
