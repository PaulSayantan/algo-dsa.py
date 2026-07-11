# Burst Balloons — Solution

## Brute Force

Try every possible **burst order**. At each step choose one of the remaining
balloons to burst, collect its coins (which depend on current neighbors), and
recurse on the smaller set. There are `n!` orders.

- **Time:** `O(n!)`.
- **Space:** `O(n)` recursion depth.

Even memoizing on the *set* of remaining balloons gives `O(2^n * n)`, still far
too slow for `n = 300`.

## Optimal Approach (Range / Interval DP — "burst last")

The naive "which balloon do I burst **first**?" formulation fails because after a
burst the neighbors change, so subintervals are **not independent** — the two
sides can influence each other through the removed balloon's former neighbors.

The trick is to reverse the question: **which balloon `k` do I burst LAST inside
an interval?** If `k` is burst last among the balloons strictly between `left`
and `right`, then at the moment `k` bursts, its neighbors are exactly `left` and
`right` (everything else inside is already gone). Crucially, the balloons in
`(left, k)` and `(k, right)` are burst *before* `k` and never interact across
`k`, so the two sides become **independent** subproblems bounded by fixed walls.

Pad the array with virtual `1`s: `arr = [1] + nums + [1]`, so real balloons live
at indices `1 … n`.

> `dp[left][right]` = max coins from bursting **all** balloons strictly between
> indices `left` and `right` (exclusive), with `arr[left]` and `arr[right]`
> remaining as intact walls.

**Recurrence** (choose the last-burst balloon `k`):
```
dp[left][right] = max over k in (left, right) of
                  dp[left][k] + dp[k][right]
                  + arr[left] * arr[k] * arr[right]
```
The term `arr[left]*arr[k]*arr[right]` is the coins from bursting `k` last, when
its neighbors are the walls `left` and `right`.

**Base case:** `dp[left][right] = 0` whenever `right <= left + 1` (no balloon
between the walls).

**Why it is correct.** For any interval, *some* balloon is burst last; fixing it
as `k` makes the left and right regions fully independent (they can never be a
neighbor of each other's balloons because `k` sits between them until the very
end). Maximizing over every choice of `k` explores all valid orders, and each
subproblem is a strictly smaller interval.

**Iteration order.** Increasing interval length, `length = right - left`.

```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):            # distance between walls
            for left in range(0, n - length):
                right = left + length
                best = 0
                for k in range(left + 1, right):
                    best = max(best,
                               dp[left][k] + dp[k][right]
                               + arr[left] * arr[k] * arr[right])
                dp[left][right] = best
        return dp[0][n - 1]
```

- **Time:** `O(n^3)` — `O(n^2)` intervals times `O(n)` choices of last balloon.
- **Space:** `O(n^2)`.

### Trace intuition for `nums = [3, 1, 5, 8]`

`arr = [1, 3, 1, 5, 8, 1]`. The full answer `dp[0][5]` tries each `k` as the
last balloon between walls `arr[0]=1` and `arr[5]=1`. The optimal choice bursts
balloon `8` (index 4) last: `dp[0][4] + dp[4][5] + 1*8*1`, and `dp[0][4]`
recursively resolves to bursting `3` last among `{3,1,5}`, matching the
`15 + 120 + 24 + 8 = 167` order in the statement.

## Key Insights & Edge Cases

- **"Last, not first"** is the whole game: it converts a problem with coupled
  subproblems into a clean split-point interval DP. This same reframing appears
  in "Remove Boxes" and other removal problems.
- **Padding with `1`s** removes all boundary special-casing — a real balloon at
  the array edge simply sees a wall of value `1`.
- The split index `k` is the **special (last-burst) element**, contrasted with
  matrix-chain where `k` is a *cut point*. Both are interval DP, different roles.
- **Single balloon** `[x]` -> `arr = [1, x, 1]`, answer `1*x*1 = x`.
- **Zeros** in `nums` are handled naturally; bursting a `0` balloon contributes
  `0` from itself but its position still matters for neighbors.
