# Prefix to Infix Conversion

**Difficulty:** Easy

**Source:** Classic — prefix (Polish) to infix conversion

## Description

Given a string `expr` holding a valid prefix (Polish) arithmetic expression, convert it to its fully-parenthesized infix form. Operators are `+ - * /` and every operand is a single character (a letter or digit). In prefix notation the operator precedes its two operands, so scan **right to left** with a stack: push operands, and on an operator pop the top two — the **first** popped is the left operand — combine them as `(left op right)`, and push the result. The final stack entry is the answer.

Constraints: `expr` is a valid prefix expression, every operator is binary, `1 <= len(expr) <= 10^4`.

## Examples

### Example 1

```
Input:  expr = "*+AB-CD"
Output: ((A+B)*(C-D))
```

**Explanation:** `+AB` is `(A+B)`, `-CD` is `(C-D)`, and the outer `*` joins them.

## Hint

Walk the tokens reversed on a stack; on an operator pop left then right and push `(left op right)`.
