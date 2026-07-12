# Postfix to Fully Parenthesized Infix

**Difficulty:** Medium

**Source:** Classic — postfix to fully-parenthesized infix

## Description

Given `postfix` tokens (integer operands and operators `+ - * /`), build the expression tree with a stack of subtrees, then return the fully parenthesized `infix` string produced by an inorder walk. Render each operand as its integer text; render every operator node as `(` + left + operator + right + `)`. A lone operand (no operators) is returned without parentheses.

Constraints: `postfix` is a valid postfix expression with `1 <= len(postfix)`; operands fit in an `int`.

## Examples

### Example 1

```
Input:  postfix = ["3","4","+","2","*"]
Output: "((3+4)*2)"
```

**Explanation:** Push `3` and `4`; on `+` pop both and form `(3+4)`; push `2`; on `*` pop `(3+4)` and `2` to form `((3+4)*2)`.

## Hint

Push a leaf string per operand; on an operator pop right then left, wrap as `(left op right)`, and push the combined subtree string.
