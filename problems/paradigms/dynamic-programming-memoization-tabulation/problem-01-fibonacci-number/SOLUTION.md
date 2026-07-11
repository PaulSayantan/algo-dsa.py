# Solution — Fibonacci Number

## Brute Force

Translate the definition directly into recursion:

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

This is correct but disastrously slow. Computing `fib(n)` calls `fib(n - 1)` and
`fib(n - 2)`, which each spawn their own two calls, and so on. The recursion tree has
roughly `F(n)` leaves, so the number of calls grows like the golden ratio raised to `n`.

- **Time:** `O(phi^n)` ≈ `O(1.618^n)` — exponential.
- **Space:** `O(n)` for the recursion stack depth.

The key observation: `fib(k)` is recomputed an exponential number of times. Those are
**overlapping subproblems** — exactly the signal to apply DP.

## Optimal Approach (Dynamic Programming)

There are only `n + 1` distinct subproblems (`F(0)` through `F(n)`), and each depends
only on the two before it. Solve each once.

### Top-down (memoization)

```python
from functools import lru_cache

class Solution:
    def fib(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def f(k):
            if k < 2:
                return k
            return f(k - 1) + f(k - 2)
        return f(n)
```

The cache guarantees each `f(k)` is computed at most once; every later request is an
`O(1)` lookup.

### Bottom-up (tabulation)

```python
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for k in range(2, n + 1):
            dp[k] = dp[k - 1] + dp[k - 2]
        return dp[n]
```

We fill the table in increasing order, so `dp[k - 1]` and `dp[k - 2]` are always ready
before `dp[k]`.

### Space-optimized (rolling variables)

Because `dp[k]` needs only the previous two entries, keep just those two:

```python
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr
```

**Why it is correct:** The recurrence `F(k) = F(k-1) + F(k-2)` is the problem's
definition, and we always evaluate a state only after its dependencies are known. Base
cases `F(0)=0`, `F(1)=1` seed the process.

- **Time:** `O(n)` — a constant amount of work per state.
- **Space:** `O(n)` for the table, or `O(1)` with rolling variables.

## Key Insights & Edge Cases

- **Overlapping subproblems** is the trigger: the same `F(k)` is requested repeatedly.
  Caching converts exponential to linear.
- **Base cases first:** handle `n = 0` (→ 0) and `n = 1` (→ 1) before the loop; forgetting
  them is the most common bug.
- **Memoization vs. tabulation:** both are `O(n)` time. Memoization mirrors the math
  most directly; tabulation avoids recursion depth and has a smaller constant. For very
  large `n`, tabulation (or rolling variables) sidesteps Python's recursion limit.
- With the given constraint `n <= 30` the answer fits easily in a machine integer, and
  Python integers are arbitrary precision anyway, so overflow is a non-issue here.
