# Infix to Postfix with Right-Associative Exponent

**Difficulty:** Medium

**Source:** Classic — Shunting-Yard with associativity

## Description

Given `tokens` of a valid infix expression over single-letter/number operands, the operators `+ - * /` and the exponent operator `^`, plus parentheses `( )`, return the equivalent postfix (RPN) token list. Precedence is `^` (highest) > `* /` > `+ -`. The operators `+ - * /` are left-associative, but `^` is **right-associative** (so `a^b^c` means `a^(b^c)`).

## Examples

### Example 1

```
Input:  ["a","^","b","^","c"]
Output: ['a', 'b', 'c', '^', '^']
```

**Explanation:** `^` is right-associative, so the rightmost `b^c` is grouped first and its operator emitted last.

## Hint

Pop the operator stack while the top has strictly greater precedence, OR equal precedence AND the current operator is left-associative; a right-associative `^` never pops another `^`.
