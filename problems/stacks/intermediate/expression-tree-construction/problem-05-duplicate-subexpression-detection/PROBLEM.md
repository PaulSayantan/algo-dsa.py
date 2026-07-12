# Detect a Duplicate Subexpression

**Difficulty:** Medium

**Source:** Classic — duplicate subtree / common subexpression detection

## Description

Given `postfix` tokens (integer operands and operators `+ - * /`), build the binary expression tree with a stack of subtrees, then return `True` if the tree contains a duplicate **subexpression** — two distinct operator nodes whose entire subtrees are structurally identical (same operators and operands in the same shape) — and `False` otherwise. A single operand by itself is not a subexpression, so repeated bare operands do not count; only repeated operator subtrees do.

Serialize each subtree to a canonical signature and detect when the same operator-node signature appears more than once.

Constraints: `postfix` is a valid postfix expression; `1 <= len(postfix)`.

## Examples

### Example 1

```
Input:  postfix = ["3","4","+","3","4","+","*"]
Output: True
```

**Explanation:** The tree is `*( +(3,4), +(3,4) )`; the subexpression `(3+4)` appears twice.

## Hint

Give every subtree a canonical signature (operator plus child signatures); the tree has a duplicate if any operator-node signature is produced more than once.
