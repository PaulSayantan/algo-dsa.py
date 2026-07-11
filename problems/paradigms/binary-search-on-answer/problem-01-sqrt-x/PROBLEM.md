# Sqrt(x)

**Difficulty:** Easy

**Source:** LeetCode 69 (Sqrt(x))

## Description

Given a non-negative integer `x`, return the **square root of `x` rounded down to
the nearest integer**. The returned integer should be **non-negative** as well.

You **must not** use any built-in exponent function or operator such as
`pow(x, 0.5)` or `x ** 0.5` or `math.sqrt`.

In other words, return the largest integer `k` such that `k * k <= x`.

## Constraints

- `0 <= x <= 2^31 - 1`

## Examples

### Example 1

```
Input:  x = 4
Output: 2
```

Explanation: The square root of `4` is `2`, and `2 * 2 = 4 <= 4`.

### Example 2

```
Input:  x = 8
Output: 2
```

Explanation: The square root of `8` is about `2.828...`. Rounded down, the answer
is `2`, because `2 * 2 = 4 <= 8` but `3 * 3 = 9 > 8`.

### Example 3

```
Input:  x = 0
Output: 0
```

Explanation: The square root of `0` is `0`. The answer `0` satisfies
`0 * 0 = 0 <= 0`.

## Hint

You do not need to search the number line one integer at a time. The predicate
"`k * k <= x`" is `True` for small `k` and flips to `False` once `k` gets too
big, so it is **monotonic**. Use **Binary Search on Answer** to find the boundary
— the largest `k` for which the predicate still holds.
