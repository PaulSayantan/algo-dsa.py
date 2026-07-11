# Minimum of the Upper Envelope of Parabolas

**Difficulty:** Medium

**Source:** Classic competitive-programming problem (convex upper-envelope minimization)

## Description

You are given `n` upward-opening parabolas. Parabola `i` is described by three
coefficients `[a_i, b_i, c_i]` with `a_i > 0` and represents the function

```
f_i(x) = a_i * x^2 + b_i * x + c_i
```

Define the **upper envelope**

```
g(x) = max( f_1(x), f_2(x), ..., f_n(x) )
```

Given a closed interval `[lo, hi]`, return the **minimum value** of `g(x)` for
`x` in `[lo, hi]`, i.e. `min_{x in [lo, hi]} g(x)`.

Each `f_i` is convex (because `a_i > 0`), and the pointwise maximum of convex
functions is convex — so `g` is **convex**, hence **unimodal** with a single minimum.
Answers within an absolute or relative error of `1e-6` are accepted.

## Constraints

- `1 <= n <= 10^5`
- `1 <= a_i <= 100`, `-1000 <= b_i, c_i <= 1000`
- `-10^4 <= lo < hi <= 10^4`
- The answer is a real number; tolerance `1e-6`.

## Examples

### Example 1

```
Input:  parabolas = [[1, 0, 0]], lo = -10, hi = 10
Output: 0.000000
```

Explanation: The envelope is just `g(x) = x^2`, whose minimum on `[-10, 10]` is at
`x = 0` with value `0`.

### Example 2

```
Input:  parabolas = [[1, -2, 1], [1, 2, 1]], lo = -5, hi = 5
Output: 1.000000
```

Explanation: The two parabolas are `(x - 1)^2` and `(x + 1)^2`. They cross at `x = 0`,
where both equal `1`. Left of `0` the envelope follows `(x - 1)^2` (falling toward
`0`); right of `0` it follows `(x + 1)^2` (rising). The lowest point of the envelope is
therefore `g(0) = 1`.

### Example 3

```
Input:  parabolas = [[1, 0, 0], [1, -8, 16]], lo = 0, hi = 4
Output: 4.000000
```

Explanation: The parabolas are `x^2` and `(x - 4)^2`. They cross at `x = 2`, where both
equal `4`. The envelope's minimum on `[0, 4]` is `g(2) = 4`.

## Hint

`g` is convex, so it is unimodal. Use **Ternary Search** on the real interval
`[lo, hi]`: probe `m1` and `m2` at the one-third points, evaluate `g` (an `O(n)` max
over the parabolas) at each, and keep shrinking toward the valley.
