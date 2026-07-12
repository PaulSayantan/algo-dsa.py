# Bitwise-AND Stack

**Difficulty:** Medium

**Source:** Classic — Stack with O(1) bitwise-AND of all elements

## Description

Design a stack that supports `push(x)`, `pop()`, `top()`, and `andAll()`, where
`andAll()` returns the bitwise AND (`&`) of ALL values currently on the stack,
in O(1) time. Values are non-negative integers, and `andAll()` assumes the stack
is non-empty.

Like min or GCD, a running bitwise AND is not invertible — clearing a bit on
`pop` is impossible — so carry the AND-so-far alongside each pushed element.

## Examples

### Example 1

```
Input:  push 7,6,4; andAll; pop; andAll
Output: 4, 6
```

**Explanation:** `7 & 6 & 4 = 4`; popping `4` leaves `[7,6]`, and `7 & 6 = 6`.

## Hint

Store `(value, and-so-far)` pairs; `andAll()` reads the top pair's second field.
