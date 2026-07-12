# Infix to Prefix Conversion

**Difficulty:** Medium

**Source:** Classic — Shunting-Yard (prefix variant)

## Description

Given `tokens` of a valid infix expression over single-letter/number operands and operators `+ - * /` with parentheses `( )`, return the equivalent prefix (Polish) token list. `*` and `/` bind tighter than `+` and `-`; all four are left-associative.

## Examples

### Example 1

```
Input:  ["a","+","b","*","c"]
Output: ['+', 'a', '*', 'b', 'c']
```

**Explanation:** `*` binds first, so `b*c` is one operand of `+`; prefix puts each operator before its two operands.

## Hint

Reverse the tokens and swap parentheses, run shunting-yard popping only *strictly* higher precedence (to preserve left-associativity across the reversal), then reverse the output.
