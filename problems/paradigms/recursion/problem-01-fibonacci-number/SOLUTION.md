# Fibonacci Number — Solution

## Brute Force

The most literal translation of the definition is a two-branch recursion: `fib(n)`
calls `fib(n-1)` and `fib(n-2)` and adds the results.

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

- **Time:** `O(φ^n)` ≈ `O(1.618^n)` — exponential. The recursion tree recomputes the
  same subproblems many times (`fib(n-2)` is computed by both `fib(n-1)` and the
  direct call, and so on down the tree).
- **Space:** `O(n)` for the recursion stack (the tree's maximum depth is `n`).

This is the textbook example of **overlapping subproblems**: pure recursion is correct
but wastefully slow. For `n <= 30` it still runs instantly, so it is a fine answer for
this problem — but it is the perfect motivator for memoization.

## Optimal Approach (Recursion + Memoization)

The exponential blowup comes entirely from recomputing identical subproblems. Cache
each `F(k)` the first time it is computed and reuse it thereafter. This keeps the clean
recursive structure but makes each of the `n + 1` distinct subproblems compute exactly
once.

```python
from functools import lru_cache

class Solution:
    def fib(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def rec(k):
            if k < 2:            # base cases: F(0)=0, F(1)=1
                return k
            return rec(k - 1) + rec(k - 2)
        return rec(n)
```

**Why it is correct:** the recurrence and base cases are exactly the mathematical
definition of the Fibonacci sequence, so by induction the function returns `F(n)`. The
cache does not change *which* value is returned for any `k`; it only avoids
recomputing it — so correctness is preserved while the running time collapses.

**Step by step for `n = 4`:**

1. `rec(4)` needs `rec(3)` and `rec(2)`.
2. `rec(3)` needs `rec(2)` and `rec(1)`. `rec(2)` needs `rec(1)` and `rec(0)`.
3. Base cases return `rec(1) = 1`, `rec(0) = 0`; these get cached.
4. Unwinding: `rec(2) = 1 + 0 = 1`, `rec(3) = 1 + 1 = 2`, and the second `rec(2)` is a
   cache hit returning `1`. Finally `rec(4) = 2 + 1 = 3`.

- **Time:** `O(n)` — each of the `n + 1` subproblems is evaluated once.
- **Space:** `O(n)` for the cache plus `O(n)` recursion stack.

(An iterative bottom-up version reaches `O(n)` time and `O(1)` space, but the point of
this problem is the recursion.)

## Key Insights & Edge Cases

- **Base cases first:** `F(0) = 0` and `F(1) = 1` are what stop the recursion.
  Returning `n` directly when `n < 2` handles both in one line.
- **Overlapping subproblems** are the defining weakness of naive branching recursion —
  recognizing them is the trigger to memoize (this is the bridge from plain recursion
  to dynamic programming).
- **`n = 0` and `n = 1`** must return `0` and `1` respectively; make sure the base-case
  guard is `n < 2`, not `n <= 2` (which would wrongly short-circuit `F(2)`).
- The recursion depth reaches `n`, which is safely within Python's default limit for
  `n <= 30`; for very large `n` you would prefer the iterative or matrix-power form.
