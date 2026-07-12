# Validate a Prefix Expression

**Difficulty:** Easy

**Source:** Classic — prefix (Polish) expression validation

## Description

Given a string `expr`, decide whether it is a **valid** prefix (Polish) arithmetic expression and return a `bool`. Operators are the binary symbols `+ - * /`; every other character is a single-character operand. A string is valid when evaluating it as prefix notation consumes exactly one final value with no operand ever missing. Reuse the prefix-evaluation idea but track only *arity*: scan **right to left** with a stack — push `1` for each operand, and on an operator you must be able to pop two items, after which you push one back. The string is valid iff no operator ever underflows the stack and exactly one item remains at the end.

Constraints: `expr` consists of operator symbols `+ - * /` and single-character operands, `0 <= len(expr) <= 10^4`.

## Examples

### Example 1

```
Input:  expr = "*+AB-CD"
Output: True
```

**Explanation:** Every operator finds its two operands and a single result is left, so it is a well-formed prefix expression.

## Hint

Scan reversed, push a marker per operand, and require two pops per operator; valid iff nothing underflows and exactly one marker remains.
