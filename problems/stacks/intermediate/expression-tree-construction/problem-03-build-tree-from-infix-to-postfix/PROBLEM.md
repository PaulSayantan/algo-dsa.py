# Infix to Postfix via Expression Tree

**Difficulty:** Medium

**Source:** Classic — infix to postfix (expression tree)

## Description

Given `infix` tokens (integer operands, binary operators `+ - * /`, and parentheses `(` `)`), build the binary expression tree that respects operator precedence (`* /` bind tighter than `+ -`) and parentheses, then return the equivalent `postfix` token list from a postorder walk of the tree.

Use two stacks while scanning: one holds operator tokens, the other holds completed subtree nodes. On a closing paren, or when the incoming operator has precedence not greater than the stack's top, pop the operator and combine the two top subtrees. Left-to-right scan yields left-associative operators.

Constraints: `infix` is a well-formed expression; `1 <= len(infix)`.

## Examples

### Example 1

```
Input:  infix = ["3","+","4","*","2"]
Output: ["3","4","2","*","+"]
```

**Explanation:** `*` binds tighter than `+`, so `4*2` forms first; the tree is `+(3, *(4,2))`, whose postorder is `3 4 2 * +`.

## Hint

Keep an operator stack and a subtree stack; each time you pop an operator, pop two subtrees, attach them, and push the new subtree. Postorder-walk the final root.
