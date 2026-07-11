# Pow(x, n)

**Difficulty:** Medium

**Source:** LeetCode 50 (Pow(x, n))

## Description

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`).

You must not use the language's built-in exponentiation operator or library function.

A naive solution multiplies `x` by itself `n` times — `O(n)`. But exponentiation is
self-similar in a much stronger way: `x^n = (x^(n/2))^2`. Computing `x^(n/2)` **once**
and squaring it halves the problem on every step, giving a recursion of depth
`O(log n)`. This is known as **fast exponentiation** (exponentiation by squaring).

## Constraints

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1` — note that `n` can be negative.
- `-10^4 <= x^n <= 10^4`

## Examples

### Example 1

```
Input:  x = 2.00000, n = 10
Output: 1024.00000
```

Explanation: `2^10 = 1024`.

### Example 2

```
Input:  x = 2.10000, n = 3
Output: 9.26100
```

Explanation: `2.1^3 = 9.261`.

### Example 3

```
Input:  x = 2.00000, n = -2
Output: 0.25000
```

Explanation: `2^-2 = 1 / 2^2 = 1 / 4 = 0.25`.

## Hint

Use **Recursion** with the identity `x^n = (x^(n/2))^2`. Compute the half power once,
square it, and multiply by an extra `x` when `n` is odd. Handle negative `n` by taking
the reciprocal, and use `n = 0` as the base case (`x^0 = 1`).
