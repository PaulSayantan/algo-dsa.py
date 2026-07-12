# Build & Evaluate an Expression Tree

**Difficulty:** Medium

**Source:** Classic — expression tree from postfix

## Description

Given `postfix` tokens (integer operands and operators `+ - * /`), build the expression tree using a stack of subtrees, then evaluate it and return the integer result. Division truncates toward zero.

## Examples

### Example 1

```
Input:  postfix = ["3","4","+","2","*"]
Output: 14
```

**Explanation:** (3+4)*2 = 14

## Hint

Push operand nodes; on an operator pop right then left, attach, push. Evaluate recursively.
