# Infix to Postfix Conversion

**Difficulty:** Medium

**Source:** Classic — Shunting-Yard algorithm

## Description

Given `tokens` of a valid infix expression over single-letter/number operands and operators `+ - * /` with parentheses `( )`, return the equivalent postfix (RPN) token list. `*` and `/` bind tighter than `+` and `-`; all four are left-associative.

## Examples

### Example 1

```
Input:  ["a","+","b","*","c"]
Output: ["a","b","c","*","+"]
```

## Hint

Output operands immediately; pop higher/equal-precedence operators before pushing; parentheses gate popping.
