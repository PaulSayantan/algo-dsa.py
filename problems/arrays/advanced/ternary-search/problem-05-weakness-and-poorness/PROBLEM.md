# Weakness and Poorness

**Difficulty:** Hard

**Source:** Codeforces 578C — Weakness and Poorness

## Description

You are given an array `a` of `n` numbers. For a real number `x`, form the shifted
array `b_i = a_i - x`. The **poorness** of a contiguous subarray is the **absolute
value of its sum** of `b` values. The **weakness** of the whole sequence for a given
`x` is the maximum poorness over **all** non-empty contiguous subarrays:

```
weakness(x) = max over subarrays [l, r] of | sum_{i=l..r} (a_i - x) |
```

Choose the real number `x` that **minimizes** `weakness(x)`, and return that minimum
weakness.

For a fixed `x`, `weakness(x)` can be computed in `O(n)`: it equals
`max( maxSubarraySum(b), -minSubarraySum(b) )`, both found by Kadane's algorithm. As a
function of `x`, each subarray's poorness `|sum - k·x|` is a V-shaped (convex) function
of `x`, and `weakness(x)` is the **pointwise maximum** of these convex functions —
hence **convex**, therefore **unimodal**. Answers within `1e-6` are accepted.

## Constraints

- `1 <= n <= 200000`
- `|a_i| <= 10^4`
- The answer is a real number; absolute or relative error up to `1e-6` is accepted.

## Examples

### Example 1

```
Input:  a = [1, 2, 3]
Output: 1.000000000
```

Explanation: The best shift is `x = 2` (the middle value). Then `b = [-1, 0, 1]`, and
the largest absolute subarray sum is `1` (from `[-1]` or `[1]`). No other `x` does
better, so the minimum weakness is `1`.

### Example 2

```
Input:  a = [1, 2, 3, 4]
Output: 2.000000000
```

Explanation: The optimal shift is `x = 2.5`, giving `b = [-1.5, -0.5, 0.5, 1.5]`. The
maximum absolute subarray sum is `|-1.5 - 0.5| = 2` (prefix `[1, 2]`) — matched by the
suffix `[3, 4]`. The minimum weakness is `2`.

### Example 3

```
Input:  a = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
Output: 4.500000000
```

Explanation: The optimal shift balances the largest positive and negative subarray
sums; the minimized weakness works out to `4.5`.

## Hint

`weakness(x)` is the pointwise maximum of convex functions of `x`, so it is convex —
unimodal with a single minimum. Use **Ternary Search** on `x` over a real interval,
where each probe evaluates `weakness(x)` in `O(n)` with Kadane's algorithm (run twice:
for the max-sum and the min-sum subarrays).
