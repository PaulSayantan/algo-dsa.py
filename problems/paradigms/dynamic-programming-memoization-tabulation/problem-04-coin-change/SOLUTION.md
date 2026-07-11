# Solution — Coin Change

## Brute Force

Recursively try every coin at every step and take the minimum count:

```python
def fewest(rem):
    if rem == 0:
        return 0
    if rem < 0:
        return float('inf')
    return 1 + min(fewest(rem - c) for c in coins)
```

Without caching, the same remaining amount is explored along exponentially many coin
sequences.

- **Time:** `O(amount^len(coins))` in the worst case — exponential.
- **Space:** `O(amount)` recursion depth.

The remaining-amount subproblem repeats constantly — overlapping subproblems — so DP
applies. This is the *unbounded knapsack* / *minimum-cost* pattern (coins may repeat).

## Optimal Approach (Dynamic Programming)

**State:** `dp[a]` = the minimum number of coins needed to make amount `a`.

**Recurrence:** the last coin used is some `c <= a`; before it we needed `dp[a - c]`
coins. Take the best final coin:

```
dp[a] = min(dp[a - c] + 1)  over all coins c with c <= a
```

**Base case:** `dp[0] = 0`. Unreachable amounts stay at `infinity` (sentinel).

### Bottom-up (tabulation)

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1                       # larger than any real answer
        dp = [0] + [INF] * amount
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        return dp[amount] if dp[amount] != INF else -1
```

### Top-down (memoization)

```python
from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize=None)
        def fewest(rem):
            if rem == 0:
                return 0
            best = float('inf')
            for c in coins:
                if c <= rem:
                    best = min(best, fewest(rem - c) + 1)
            return best
        ans = fewest(amount)
        return ans if ans != float('inf') else -1
```

**Why it is correct:** Any optimal solution for amount `a` uses some last coin `c`;
removing it leaves an optimal solution for `a - c` (optimal substructure — if the
remainder weren't optimal we could improve the whole). Minimizing over all valid last
coins covers every possibility, and we fill amounts in increasing order so `dp[a - c]` is
finalized before `dp[a]`.

### Trace on `coins = [1, 2, 5], amount = 11` (selected states)

```
dp[0]=0  dp[1]=1  dp[2]=1  dp[3]=2  dp[4]=2  dp[5]=1
dp[6]=2  dp[7]=2  dp[8]=3  dp[9]=3  dp[10]=2 dp[11]=3
```

`dp[11] = min(dp[10]+1, dp[9]+1, dp[6]+1) = min(3, 4, 3) = 3`. ✔

- **Time:** `O(amount * len(coins))`.
- **Space:** `O(amount)`.

## Key Insights & Edge Cases

- **Minimization needs an infinity sentinel:** unreachable states must not masquerade as
  valid small answers. Using `amount + 1` as "infinity" works because any real answer
  needs at most `amount` coins (all 1s if a coin of value 1 exists).
- **`amount = 0` returns 0**, not -1 — handled by the base case `dp[0] = 0`.
- **Unbounded reuse:** because a coin can be used repeatedly, the inner loop reads
  `dp[a - c]` for the *current* row (same array), unlike the 0/1 knapsack which iterates
  the capacity in reverse.
- **Return -1 for impossible amounts** (e.g., `coins=[2], amount=3`): check the sentinel
  at the end.
- This DP finds the *minimum count*. A closely related variant (LeetCode 518) counts the
  *number of ways* to make the amount — same states, different transition (sum instead of
  min) and a different loop order to avoid counting permutations.
