# Solution — House Robber

## Brute Force

Try every subset of houses that contains no two adjacent indices and keep the best sum.
Recursively, at each house choose to rob it (then skip the next) or skip it:

```python
def best(i):
    if i >= len(nums):
        return 0
    return max(nums[i] + best(i + 2),   # rob house i
               best(i + 1))             # skip house i
```

Two branches per house gives an exponential number of calls.

- **Time:** `O(2^n)`.
- **Space:** `O(n)` recursion depth.

`best(i)` is recomputed from many callers — overlapping subproblems — so cache it.

## Optimal Approach (Dynamic Programming)

**State:** `dp[i]` = the maximum money robbable considering only houses `0..i-1` (the
first `i` houses).

**Recurrence:** for house index `i` (1-based count), the last house either is or isn't
robbed:

```
dp[i] = max(dp[i - 1],                # skip house i-1
            dp[i - 2] + nums[i - 1])  # rob house i-1, add best up to i-2
```

**Base cases:** `dp[0] = 0` (no houses), `dp[1] = nums[0]`.

### Bottom-up (tabulation)

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[n]
```

### Space-optimized (rolling variables)

Only the previous two answers matter:

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0   # best up to i-2, best up to i-1
        for money in nums:
            prev, curr = curr, max(curr, prev + money)
        return curr
```

**Why it is correct:** Any optimal robbery of the first `i` houses either excludes house
`i-1` (so it is optimal for the first `i-1`) or includes it (so houses `i-1` and `i-2`
can't both be robbed, and the rest is optimal for the first `i-2`). Taking the max over
these two mutually exclusive, exhaustive cases yields the optimum, and induction from the
base cases finishes it.

### Trace on `[2, 7, 9, 3, 1]`

| i | house money | dp[i] = max(dp[i-1], dp[i-2] + money) |
|---|-------------|----------------------------------------|
| 0 | —           | 0                                       |
| 1 | 2           | 2                                       |
| 2 | 7           | max(2, 0 + 7) = 7                       |
| 3 | 9           | max(7, 2 + 9) = 11                      |
| 4 | 3           | max(11, 7 + 3) = 11                     |
| 5 | 1           | max(11, 11 + 1) = 12                    |

Answer: `dp[5] = 12`. ✔

- **Time:** `O(n)`.
- **Space:** `O(n)` for the table, or `O(1)` with rolling variables.

## Key Insights & Edge Cases

- The per-element **take / skip** decision is the archetype for a large family of
  1D DP problems (subsequence-with-constraint problems).
- **Non-negative values** guarantee that skipping is never forced; if values could be
  negative you would clamp with an extra `max(..., 0)`.
- **Edge cases:** length-1 array returns its only element; an all-zeros array returns 0.
- This is the linear-street version. The follow-up *House Robber II* arranges houses in a
  circle, solved by running this DP twice (excluding either the first or the last house).
