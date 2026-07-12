# Postfix to Prefix Conversion

**Difficulty:** Easy

**Source:** Classic — postfix (RPN) to prefix (Polish notation)

## Description

Given a valid postfix expression as a string `expression`, convert it to its equivalent **prefix** (Polish) form. Each operand is a single character (a letter or digit) and the valid operators are `+`, `-`, `*`, `/`.

In prefix notation the operator is written **before** its two operands with no parentheses. So operands `a` and `b` combined with operator `op` become the string `op + a + b`. The input is guaranteed to be a well-formed postfix expression with no spaces.

## Examples

### Example 1

```
Input:  expression = "ab+"
Output: "+ab"
```

**Explanation:** `+` pops `a` and `b`; the prefix form places the operator first: `+ab`.

### Example 2

```
Input:  expression = "ab+cd-*"
Output: "*+ab-cd"
```

**Explanation:** `ab+` becomes `+ab`, `cd-` becomes `-cd`, and `*` prepends onto their concatenation: `*` + `+ab` + `-cd`.

## Hint

Run the postfix stack sweep but push partial **strings**: on an operator pop `b` then `a` and push `op + a + b` (operator first).
