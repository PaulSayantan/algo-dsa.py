# GCD Stack

**Difficulty:** Medium

**Source:** Classic — Stack with O(1) GCD of all elements

## Description

Design a stack that supports `push(x)`, `pop()`, `top()`, and `gcd()`, where
`gcd()` returns the greatest common divisor of ALL values currently on the
stack, in O(1) time. Values are positive integers, and `gcd()` assumes the
stack is non-empty.

A running GCD cannot simply be "undone" on `pop` (GCD is not invertible), so
carry the GCD-so-far alongside each element the same way a min-stack carries its
running minimum.

## Examples

### Example 1

```
Input:  push 12,18; gcd; push 9; gcd; pop; gcd
Output: 6, 3, 6
```

**Explanation:** `gcd(12,18)=6`; after pushing `9`, `gcd(12,18,9)=3`; popping
`9` restores `gcd(12,18)=6`.

## Hint

Store `(value, gcd-so-far)` pairs; `gcd()` reads the top pair's second field.
