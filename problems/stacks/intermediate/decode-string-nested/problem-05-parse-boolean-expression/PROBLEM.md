# Parse Boolean Expression

**Difficulty:** Medium

**Source:** LeetCode 1106 — Parsing A Boolean Expression

## Description

Given a valid boolean `expression`, evaluate it and return its boolean value.

The grammar uses these tokens:

- `'t'` evaluates to `True`; `'f'` evaluates to `False`.
- `!(expr)` is the logical NOT of the inner expression.
- `&(expr1, expr2, ...)` is the logical AND of two or more inner expressions.
- `|(expr1, expr2, ...)` is the logical OR of two or more inner expressions.

Expressions may be nested arbitrarily. The input is always valid.

## Examples

### Example 1

```
Input:  expression = "|(&(t,f,t),!(t))"
Output: False
```

**Explanation:** `&(t,f,t)` is `False` (an `f` is present) and `!(t)` is `False`, so the OR of the two is `False`.

## Hint

Push tokens on a stack; on `)` pop operands back to the matching `(`, read the operator beneath, apply `!`/`&`/`|`, and push the resulting `t`/`f` — the nested-bracket fold pattern.
