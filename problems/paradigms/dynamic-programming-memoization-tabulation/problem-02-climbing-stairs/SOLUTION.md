# Solution — Climbing Stairs

## Brute Force

Enumerate every sequence of moves by recursing on the number of steps remaining:

```python
def climb(n):
    if n < 0:
        return 0
    if n == 0:
        return 1          # one valid way: take no more steps
    return climb(n - 1) + climb(n - 2)
```

Each call branches into two, so the recursion tree size is proportional to the answer
itself, which grows like the golden ratio to the `n`.

- **Time:** `O(phi^n)` — exponential.
- **Space:** `O(n)` recursion depth.

The subproblem `climb(k)` is evaluated many times over — overlapping subproblems — so DP
applies.

## Optimal Approach (Dynamic Programming)

**State:** `dp[i]` = number of distinct ways to reach step `i`.

**Recurrence:** To stand on step `i`, your last move was either a single step from
`i - 1` or a double step from `i - 2`. These paths are disjoint and together exhaustive,
so:

```
dp[i] = dp[i - 1] + dp[i - 2]
```

**Base cases:** `dp[0] = 1` (the empty sequence reaches the ground), `dp[1] = 1`.

### Bottom-up (tabulation)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
```

### Space-optimized

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        one_back, two_back = 1, 1   # ways(1), ways(0)
        for _ in range(2, n + 1):
            one_back, two_back = one_back + two_back, one_back
        return one_back
```

**Why it is correct:** Every path to the top ends in exactly one final move (size 1 or
2), partitioning all paths into two non-overlapping groups counted by `dp[i-1]` and
`dp[i-2]`. Induction from the base cases gives the exact count.

- **Time:** `O(n)`.
- **Space:** `O(n)` for the table, or `O(1)` with rolling variables.

## Key Insights & Edge Cases

- This is **Fibonacci in disguise**: `climbStairs(n) = F(n + 1)`. Recognizing the shape
  of a recurrence is a core DP skill.
- **Why counts add (not multiply):** the last move splits the outcomes into mutually
  exclusive cases; the sum rule applies, not the product rule.
- **Edge cases:** `n = 1` → 1, `n = 2` → 2. Make sure the base cases are seeded before
  the loop starts at `i = 3`.
- Because moves are ordered, `1 + 2` and `2 + 1` are counted separately — this is why the
  answer is larger than a partition count.
