# Evaluate a Prefix Expression

**Difficulty:** Medium

**Source:** Classic — prefix (Polish) evaluation

## Description

Given `tokens` of a valid prefix arithmetic expression with operators `+ - * /` and integer operands, evaluate it and return the integer result. Scan right to left; on an operator the **first** value popped is the left operand. Division truncates toward zero.

## Examples

### Example 1

```
Input:  tokens = ["*","+","2","3","4"]
Output: 20
```

**Explanation:** (2+3)*4 = 20

## Hint

Iterate tokens reversed. On operator pop a (left) then b (right); push a∘b.
