# Solution — Longest Subarray With Absolute Diff ≤ Limit

## Brute Force

Try every start `l`, extend `r` while tracking the running max and min; stop when
`max - min > limit`.

- **Time:** O(n^2) in the worst case (e.g. a strictly small-variation array).
- **Space:** O(1).

For `n = 10^5` this is up to `10^10` operations — too slow.

## Optimal Approach (two Sparse Tables + binary search)

> The canonical O(n) solution uses two monotonic deques (a sliding window). Here we
> present the **Sparse Table** solution, which is the reason this problem lives in this
> folder: it turns any window's `max - min` into an O(1) query and pairs that with a
> binary search on the answer length.

### Step 1 — Make window extremes O(1)

Both **max** and **min** are idempotent, so build **two** Sparse Tables:

- `stMax[j][i] = max(nums[i .. i + 2^j - 1])`
- `stMin[j][i] = min(nums[i .. i + 2^j - 1])`

For a window `[l, r]`, `qMax(l, r) - qMin(l, r)` is the window's spread in O(1).

### Step 2 — Monotonic feasibility

Define `feasible(L)` = "some window of length `L` has spread `<= limit`". This is
**monotone**: if a length-`L` window `[l, l+L-1]` is valid, then its length-`(L-1)`
prefix `[l, l+L-2]` is also valid (dropping an element cannot increase the spread).
So there is a threshold `Lmax`: feasible for all `L <= Lmax`, infeasible above it.

That monotonicity lets us **binary search** on `L` in `[1, n]`. For a candidate `L`,
`check(L)` scans all `n - L + 1` windows and returns True if any has spread `<= limit`,
each check being O(1) via the Sparse Tables — so `check` is O(n).

### Step 3 — Combine

Binary search over `L` performs `O(log n)` calls to `check`, each `O(n)`, giving
`O(n log n)` after the `O(n log n)` build.

### Why it is correct

`check(L)` is exact because window spread is computed exactly. Binary search returns
the largest `L` with `check(L) == True`, which is precisely the longest valid subarray
length. Idempotency of max and min guarantees the overlapping-block queries are exact.

### Reference implementation

```python
from typing import List


class SparseTable:
    def __init__(self, nums, func):
        n = len(nums)
        self.func = func
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1
        K = self.log[n] + 1 if n else 1
        self.sp = [[0] * n for _ in range(K)]
        self.sp[0] = nums[:]
        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                self.sp[j][i] = func(self.sp[j - 1][i], self.sp[j - 1][i + half])
            j += 1

    def query(self, l, r):
        k = self.log[r - l + 1]
        return self.func(self.sp[k][l], self.sp[k][r - (1 << k) + 1])


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        st_max = SparseTable(nums, max)
        st_min = SparseTable(nums, min)

        def check(L: int) -> bool:
            for l in range(0, n - L + 1):
                r = l + L - 1
                if st_max.query(l, r) - st_min.query(l, r) <= limit:
                    return True
            return False

        lo, hi, best = 1, n, 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                best = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return best
```

- **Build:** O(n log n). **Search:** O(n log n). **Space:** O(n log n).

## Key Insights & Edge Cases

- **Two idempotent tables.** Max and min are both idempotent, so each supports the O(1)
  overlapping-block query independently.
- **Monotonicity justifies binary search.** Without it you could not skip lengths.
- **`limit = 0`** forces all-equal windows; the tables still work (spread 0 means every
  element equals both the max and min).
- **Answer is at least 1** — a single element always has spread 0, so `best` starts at 1.
- **Comparison vs. deque solution.** The two-deque sliding window is O(n) and lighter on
  memory; the Sparse Table approach is O(n log n) but demonstrates how idempotent range
  queries plus a monotone predicate solve the problem — and generalizes to offline
  variants where windows are queried arbitrarily.
