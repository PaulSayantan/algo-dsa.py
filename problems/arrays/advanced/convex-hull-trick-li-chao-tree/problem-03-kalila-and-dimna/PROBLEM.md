# Kalila and Dimna in the Forest

**Difficulty:** Medium

Source: Codeforces Round 189, Problem 319C ("Kalila and Dimna in the Forest").

## Description

There are `N` trees to cut down, indexed `1 .. N`. Tree `i` has an initial height
`a[i]` and a per-use recharge cost `b[i]`. The chainsaw must be recharged before each
tree is cut. The cost of one recharge equals `b[k] * (current height of the tallest
tree you can currently cut)` — but for this problem the recurrence is given directly
below; you only need to optimize it.

The heights `a` are given in **strictly increasing** order and the costs `b` in
**non-increasing** order, with `a[1] = 1` and `b[N] = 0` (so the process can always
finish). Define

```
dp[1] = 0
dp[i] = min over 1 <= j < i of ( dp[j] + b[j] * a[i] )
```

The answer — the minimum total cost to cut all trees — is `dp[N]`.

Each transition is already a product `b[j] * a[i]` plus a base cost `dp[j]`, so this
is the purest possible Convex Hull Trick setup. The direct DP is `O(N^2)`.

## Constraints

- `1 <= N <= 10^5`
- `1 <= a[i], b[i] <= 10^9`
- `a[1] < a[2] < ... < a[N]` (strictly increasing) and `a[1] = 1`
- `b[1] >= b[2] >= ... >= b[N]` (non-increasing) and `b[N] = 0`
- The answer fits in a 64-bit signed integer.

## Examples

### Example 1

```
Input:  N = 5, a = [1, 2, 3, 4, 5], b = [5, 4, 3, 2, 0]
Output: 25
```

Explanation: `dp[1]=0`. `dp[2] = dp[1] + b[1]*a[2] = 0 + 5*2 = 10`.
`dp[3] = min(dp[1]+5*3, dp[2]+4*3) = min(15, 22) = 15`.
`dp[4] = min(0+5*4, 10+4*4, 15+3*4) = min(20, 26, 27) = 20`.
`dp[5] = min(0+5*5, 10+4*5, 15+3*5, 20+2*5) = min(25, 30, 30, 30) = 25`. Answer `25`.

### Example 2

```
Input:  N = 6, a = [1, 2, 3, 10, 20, 30], b = [6, 5, 4, 3, 2, 0]
Output: 138
```

Explanation: Following the same recurrence (1-indexed), `dp[2]=12`, `dp[3]=18`,
`dp[4]=58`, `dp[5]=98`, and
`dp[6] = min(0+6*30, 12+5*30, 18+4*30, 58+3*30, 98+2*30) =
min(180, 162, 138, 148, 158) = 138`. Answer `138`.

## Hint

Read `dp[j] + b[j] * a[i]` as a line `line_j(x) = b[j] * x + dp[j]` evaluated at
`x = a[i]`. Because slopes `b[j]` are non-increasing and query points `a[i]` are
strictly increasing, maintain the lower hull with a **monotonic Convex Hull Trick**
and answer each `dp[i]` in amortized `O(1)`.
