# Commando

**Difficulty:** Medium-Hard

Source: APIO 2010, Problem "Commando".

## Description

You command an army of `N` soldiers standing in a fixed line. Soldier `i` has combat
strength `w[i] > 0`. You must partition the soldiers into **consecutive squads**
(each squad is a contiguous block of one or more soldiers, and every soldier belongs
to exactly one squad).

If a squad's soldiers have combined strength `x` (the sum of `w` over that block),
its adjusted combat value is

```
a * x^2 + b * x + c
```

where `a < 0`, and `b`, `c` are given integers. The total effectiveness is the sum of
the adjusted values over all squads. Because `a < 0`, splitting cleverly can raise
the total. **Maximize** the total effectiveness over all consecutive partitions.

Let `S[i] = w[1] + ... + w[i]` be prefix sums (`S[0] = 0`). With `dp[i]` = maximum
total effectiveness using the first `i` soldiers,

```
dp[0] = 0
dp[i] = max over 0 <= j < i of ( dp[j] + a*(S[i]-S[j])^2 + b*(S[i]-S[j]) + c )
```

and the answer is `dp[N]`. The direct DP is `O(N^2)`.

## Constraints

- `1 <= N <= 10^6`
- `-5 <= a <= -1` (so `a` is strictly negative; the parabola opens downward)
- `|b| <= 10^7`, `|c| <= 10^7`
- `1 <= w[i] <= 100`
- The answer fits in a 64-bit signed integer.

## Examples

### Example 1

```
Input:  N = 4, a = -1, b = 10, c = -20, w = [2, 2, 3, 4]
Output: 9
```

Explanation: The squad value function is `f(x) = -x^2 + 10x - 20`, so
`f(3) = -9+30-20 = 1`, `f(4) = -16+40-20 = 4`, `f(7) = -49+70-20 = 1`,
`f(11) = -121+110-20 = -31`. One big squad `[2,2,3,4]` scores `f(11) = -31`. The
optimal partition is `[2,2], [3], [4]` with strengths `4, 3, 4`:
`f(4) + f(3) + f(4) = 4 + 1 + 4 = 9`. No partition does better, so the answer is `9`.

### Example 2

```
Input:  N = 5, a = -1, b = 10, c = -20, w = [1, 7, 6, 2, 1]
Output: 1
```

Explanation: With `f(x) = -x^2 + 10x - 20` (peak value `5` at `x = 5`), the optimal
partition is `[1,7], [6], [2,1]` with strengths `8, 6, 3`:
`f(8) + f(6) + f(3) = (-64+80-20) + (-36+60-20) + (-9+30-20) = -4 + 4 + 1 = 1`. That
is the maximum achievable total effectiveness, so the answer is `1`.

## Hint

Expand `a*(S_i - S_j)^2` to obtain
`dp[i] = (a*S_i^2 + b*S_i + c) + max_j ( (-2a*S_j) * S_i + (a*S_j^2 - b*S_j + dp[j]) )`.
This is a **maximum** over lines evaluated at `x = S_i`. Since `a < 0`, the slopes
`-2a*S_j` are non-decreasing and the queries `S_i` are non-decreasing, so maintain
the **upper hull** with a monotonic Convex Hull Trick (a maximization CHT) in `O(N)`.
