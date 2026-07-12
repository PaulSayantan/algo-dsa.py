# Fully Parenthesize an Infix Expression

**Difficulty:** Medium

**Source:** Classic — Shunting-Yard parenthesization

## Description

Given `tokens` of a valid infix expression over single-letter/number operands and operators `+ - * /` with parentheses `( )`, return a single string that is the **fully parenthesized** equivalent: every binary operation is wrapped in its own `( ... )` so precedence and associativity are explicit and no ambiguity remains. Operands and operators are concatenated with no spaces. `*` and `/` bind tighter than `+` and `-`; all four are left-associative.

## Examples

### Example 1

```
Input:  ["a","+","b","*","c"]
Output: '(a+(b*c))'
```

**Explanation:** `b*c` binds first, so it is parenthesized before being added to `a`.

## Hint

Run shunting-yard to postfix, but rebuild instead of emit: on each operator pop two operand *strings* `a`, `b` and push `"(a op b)"`; the single remaining string is the answer.
