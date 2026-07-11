# Sqrt(x)

**Difficulty:** Easy

**Source:** LeetCode 69 — Sqrt(x)

## Description

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be **non-negative** as well.

You must **not** use any built-in exponent function or operator such as `pow(x, 0.5)` in Python or `x ** 0.5`.

In other words, return the largest integer `k` such that `k * k <= x`.

## Constraints

- `0 <= x <= 2^31 - 1`

## Examples

### Example 1

```
Input:  x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
```

### Example 2

```
Input:  x = 8
Output: 2
Explanation: The square root of 8 is 2.828..., and since we round it down to
the nearest integer, 2 is returned. Note that 3 * 3 = 9 > 8, so 3 is too big.
```

### Example 3

```
Input:  x = 0
Output: 0
Explanation: The square root of 0 is 0.
```

## Hint

The answer `k` lives in the range `[0, x]`, and the predicate `k * k <= x` is monotonic: once a value `k` becomes too large, every larger value is also too large. Use **Binary Search on Answer** to find the last `k` that satisfies the predicate.
