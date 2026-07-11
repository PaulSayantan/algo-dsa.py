# Solution — Range Sum of Elements ≤ K

## Brute Force

For each query `(l, r, k)`, scan `nums[l..r]` and add up the elements that are `<= k`.

```python
def sum_at_most(nums, l, r, k):
    return sum(v for v in nums[l:r + 1] if v <= k)
```

- **Time:** `O(q * n)` — up to `10^{10}`. Too slow.
- **Space:** `O(1)` extra.

## Optimal Approach (Augmented Merge Sort Tree)

### Augment each node with prefix sums

A plain Merge Sort Tree can *count* elements `<= k`, but here we need their **sum**.
Store in every node:

- `sorted_vals` — the sorted list of the node's range values (merge of children), and
- `prefix` — a prefix-sum array of `sorted_vals`, where `prefix[t] = sorted_vals[0] + ...
  + sorted_vals[t-1]` and `prefix[0] = 0`.

Building both still costs `O(n log n)` time and `O(n log n)` space (each node holds two
arrays of its own size).

### Answer a query

To compute the sum of elements `<= k` in `nums[l..r]`:

1. Decompose `[l, r]` into `O(log n)` canonical nodes.
2. In a node, let `c = upper_bound(sorted_vals, k)` (`bisect_right`) — the number of
   elements `<= k`. Their sum is `prefix[c]`, read in `O(1)`.
3. Add `prefix[c]` from every canonical node.

Each node costs `O(log n)` for the binary search plus `O(1)` for the prefix lookup, so a
query is `O(log^2 n)`.

### Why it is correct

`sorted_vals` is a permutation of the node's original values, so its first `c` entries
(after sorting) are exactly the elements `<= k`, and `prefix[c]` is precisely their sum.
The canonical nodes partition `[l, r]`, and "sum of qualifying elements" is additive over
a partition, so summing the per-node contributions yields the exact total. Negative
values are handled correctly because the prefix sums simply accumulate signed values.

### Reference implementation

```python
from bisect import bisect_right
from typing import List


class RangeSumAtMostSolver:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.vals = [[] for _ in range(4 * max(self.n, 1))]
        self.pref = [[] for _ in range(4 * max(self.n, 1))]
        if self.n:
            self._build(1, 0, self.n - 1, nums)

    def _build(self, node, lo, hi, nums):
        if lo == hi:
            self.vals[node] = [nums[lo]]
            self.pref[node] = [0, nums[lo]]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, nums)
        self._build(2 * node + 1, mid + 1, hi, nums)
        a, b = self.vals[2 * node], self.vals[2 * node + 1]
        merged, i, j = [], 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                merged.append(a[i]); i += 1
            else:
                merged.append(b[j]); j += 1
        merged.extend(a[i:]); merged.extend(b[j:])
        self.vals[node] = merged
        pref = [0] * (len(merged) + 1)
        for t, v in enumerate(merged):
            pref[t + 1] = pref[t] + v
        self.pref[node] = pref

    def sum_at_most(self, l, r, k):
        return self._query(1, 0, self.n - 1, l, r, k)

    def _query(self, node, lo, hi, l, r, k):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            c = bisect_right(self.vals[node], k)   # count of elements <= k
            return self.pref[node][c]              # sum of those c elements
        mid = (lo + hi) // 2
        return (self._query(2 * node, lo, mid, l, r, k)
                + self._query(2 * node + 1, mid + 1, hi, l, r, k))


def range_sum_at_most_queries(nums, queries):
    solver = RangeSumAtMostSolver(nums)
    return [solver.sum_at_most(l, r, k) for l, r, k in queries]
```

- **Build:** `O(n log n)` time and space.
- **Per query:** `O(log^2 n)`.

## Key Insights & Edge Cases

- **Prefix array is 1 longer than the value list:** `prefix[0] = 0` so that a count of `0`
  (nothing `<= k`) reads `prefix[0] = 0`, and a count equal to the node size reads the
  full node sum. This off-by-one is the classic bug to avoid.
- **`<= k` vs `< k`:** use `bisect_right` for `<= k`; switch to `bisect_left` for `< k`.
  For a band `a <= v <= b`, subtract two prefix reads:
  `prefix[bisect_right(vals, b)] - prefix[bisect_left(vals, a)]`.
- **Negative numbers:** fully supported; the prefix sums store signed cumulative totals
  (see Example 2, sum `-4`).
- **Overflow:** Python integers are unbounded, but in C++/Java use 64-bit accumulators —
  with `n = 10^5` and values up to `10^9`, a range sum can reach `~10^{14}`.
- **Empty result:** if `k` is below the node minimum, `bisect_right` returns `0` and the
  contribution is `prefix[0] = 0` — correct.
- **Static only:** as with all Merge Sort Trees, the sorted lists and their prefix sums
  cannot be updated cheaply; rebuild is `O(n log n)`.
