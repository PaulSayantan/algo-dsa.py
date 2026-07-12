# Evaluate Boolean Postfix Expression

**Difficulty:** Easy

**Source:** Classic — boolean (logical) postfix evaluation

## Description

Evaluate a boolean expression written in postfix notation. You are given a string `tokens` with no spaces where each character is one of:

- `T` — the literal **true**.
- `F` — the literal **false**.
- `&` — logical **AND** of the previous two operands.
- `|` — logical **OR** of the previous two operands.
- `!` — logical **NOT** of the previous single operand (a unary operator).

Return the resulting boolean value (`True` or `False`). The input is guaranteed to be a valid postfix boolean expression.

## Examples

### Example 1

```
Input:  tokens = "TF&"
Output: False
```

**Explanation:** `&` pops `T` and `F`; `T AND F` is `False`.

### Example 2

```
Input:  tokens = "TF|!"
Output: False
```

**Explanation:** `TF|` is `T OR F = True`; then `!` negates it to `False`.

## Hint

Use a stack of booleans: push `T`/`F` as `True`/`False`; for `&`/`|` pop two and push the result, and for the unary `!` pop just one and push its negation.
