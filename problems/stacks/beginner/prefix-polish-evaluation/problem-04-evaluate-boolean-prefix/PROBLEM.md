# Evaluate a Boolean Prefix Expression

**Difficulty:** Easy

**Source:** Classic — boolean prefix (Polish) evaluation

## Description

Given a string `expr` holding a valid boolean prefix (Polish) expression, evaluate it and return a `bool`. Operands are the single characters `T` (true) and `F` (false); the binary operators are `&` (logical AND) and `|` (logical OR). As with arithmetic prefix notation the operator precedes its two operands, so scan **right to left** with a stack: push each operand's boolean value, and on an operator pop the top two and push their combined result. The final stack entry is the answer.

Constraints: `expr` is a valid boolean prefix expression, every operator is binary, `1 <= len(expr) <= 10^4`.

## Examples

### Example 1

```
Input:  expr = "&T|FT"
Output: True
```

**Explanation:** `|FT` is `F OR T = True`, then `& T True = True`.

## Hint

Scan the tokens reversed on a stack; map `T`/`F` to booleans and apply `&`/`|` when you pop two.
