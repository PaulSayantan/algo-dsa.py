# Frog Jump III

**Difficulty:** Easy (introductory CHT)

Source: AtCoder Educational DP Contest, Problem Z ("Frog 3").

## Description

There are `N` stones numbered `1, 2, ..., N`. Stone `i` has a height `h[i]`, and the
heights are **strictly increasing**: `h[1] < h[2] < ... < h[N]`.

A frog starts on stone `1` and wants to reach stone `N`. When the frog is on stone
`i`, it can jump to any stone `j` with `i < j`. The cost of jumping from stone `i`
to stone `j` is

```
(h[i] - h[j])^2 + C
```

where `C` is a given non-negative constant.

Find the **minimum total cost** for the frog to reach stone `N` from stone `1`.

The natural recurrence is

```
dp[1] = 0
dp[j] = min over i < j of ( dp[i] + (h[i] - h[j])^2 + C )
```

and the answer is `dp[N]`. A direct evaluation is `O(N^2)`; you must do better.

## Constraints

- `2 <= N <= 2 * 10^5`
- `1 <= C <= 10^12`
- `1 <= h[1] < h[2] < ... < h[N] <= 10^6`
- The answer fits in a 64-bit signed integer.

## Examples

### Example 1

```
Input:  N = 5, C = 6, h = [1, 2, 4, 5, 7]
Output: 30
```

Explanation: One optimal route is `1 -> 5` directly (a single jump):
`(1 - 7)^2 + 6 = 36 + 6 = 42`. Better is `1 -> 3 -> 5`:
`((1-4)^2 + 6) + ((4-7)^2 + 6) = (9 + 6) + (9 + 6) = 15 + 15 = 30`. No route costs
less, so the answer is `30`.

### Example 2

```
Input:  N = 2, C = 1000000000000, h = [500000, 1000000]
Output: 1250000000000
```

Explanation: The only route is the single jump `1 -> 2`:
`(500000 - 1000000)^2 + C = 250000000000 + 1000000000000 = 1250000000000`. This
example shows why 64-bit arithmetic is required.

### Example 3

```
Input:  N = 8, C = 5, h = [1, 3, 4, 5, 10, 11, 12, 13]
Output: 62
```

Explanation: An optimal route is `1 -> 2 -> 4 -> 5 -> 8` (heights `1, 3, 5, 10, 13`):
`(1-3)^2+5 + (3-5)^2+5 + (5-10)^2+5 + (10-13)^2+5 = 9 + 9 + 30 + 14 = 62`. Short
jumps keep the squared gaps small; the minimum achievable total is `62`.

## Hint

Expand `(h[i] - h[j])^2 = h[i]^2 - 2 h[i] h[j] + h[j]^2`. Then
`dp[j] = h[j]^2 + C + min_i ( (-2 h[i]) * h[j] + (dp[i] + h[i]^2) )`, which is a
minimum over lines `m_i * x + b_i` evaluated at `x = h[j]`. Because slopes
`-2 h[i]` are strictly decreasing and query points `h[j]` are strictly increasing,
you can maintain the lower hull with a **monotonic Convex Hull Trick** in `O(N)`.
