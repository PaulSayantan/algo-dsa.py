# Build & Evaluate a Prefix Expression Tree

**Difficulty:** Medium

**Source:** Classic — expression tree from prefix (Polish notation)

## Description

Given `prefix` tokens (integer operands and operators `+ - * /`) in prefix (Polish) notation, build the binary expression tree with a stack of subtrees by scanning the tokens right to left, then evaluate the tree and return the integer result. Division truncates toward zero.

When scanning right to left, push a leaf for each operand; on an operator pop two subtrees — the first popped is the left child, the second popped is the right child — attach them, and push the new subtree.

Constraints: `prefix` is a valid prefix expression; `1 <= len(prefix)`; no division by zero.

## Examples

### Example 1

```
Input:  prefix = ["*","+","3","4","2"]
Output: 14
```

**Explanation:** The tree is `*( +(3,4), 2)` = `(3+4)*2 = 14`.

## Hint

Scan right to left over an ordinary subtree stack; the operand nearest the operator on the right becomes its left child.
