# Solution — K-Query (Count Elements Greater Than K)

## Brute Force

For each query `(i, j, k)`, scan `nums[i..j]` and count elements strictly greater than `k`.

```python
def count_greater(nums, i, j, k):
    return sum(1 for p in range(i, j + 1) if nums[p] > k)
```

- **Time:** `O(q * n)`. With `q = 2*10^5` and `n = 3*10^4` that is `6*10^9` — too slow.
- **Space:** `O(1)` extra.

## Optimal Approach (Merge Sort Tree)

This is the same tree as the canonical "count `<= x`" problem, only the per-node
accounting flips. Build a segment tree over the indices where each node stores the
**sorted list of its range's values** (parent list = merge of the two child lists).

To answer "how many elements `> k` in `nums[i..j]`":

1. Decompose `[i, j]` into `O(log n)` canonical nodes.
2. For a node whose sorted list has length `L`, the number of elements `<= k` is
   `upper_bound(list, k)` (i.e. `bisect_right`). Therefore the number of elements
   **strictly greater than** `k` is `L - upper_bound(list, k)`. Equivalently, it is
   `L - lower_bound(list, k+1)`; both agree because with integer values
   `upper_bound(k) == lower_bound(k+1)`.
3. Sum the per-node "greater than" counts.

Each of the `O(log n)` nodes costs `O(log n)` for the binary search, so a query is
`O(log^2 n)`. Building is `O(n log n)`.

### Why it is correct

Within a canonical node the stored multiset equals the original values at those indices,
so `L - upper_bound(list, k)` is exactly the count of values `> k` in that node. The
canonical nodes partition `[i, j]`, and "count of elements `> k`" is additive over a
partition, so summing gives the exact answer.

### Reference implementation

```python
from bisect import bisect_right
from typing import List


class KQuerySolver:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.tree = [[] for _ in range(4 * max(self.n, 1))]
        if self.n:
            self._build(1, 0, self.n - 1, nums)

    def _build(self, node, lo, hi, nums):
        if lo == hi:
            self.tree[node] = [nums[lo]]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, nums)
        self._build(2 * node + 1, mid + 1, hi, nums)
        a, b = self.tree[2 * node], self.tree[2 * node + 1]
        merged, i, j = [], 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                merged.append(a[i]); i += 1
            else:
                merged.append(b[j]); j += 1
        merged.extend(a[i:]); merged.extend(b[j:])
        self.tree[node] = merged

    def count_greater(self, i, j, k):
        return self._query(1, 0, self.n - 1, i, j, k)

    def _query(self, node, lo, hi, l, r, k):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            lst = self.tree[node]
            return len(lst) - bisect_right(lst, k)   # count of elements > k
        mid = (lo + hi) // 2
        return (self._query(2 * node, lo, mid, l, r, k)
                + self._query(2 * node + 1, mid + 1, hi, l, r, k))


def kquery(nums, queries):
    solver = KQuerySolver(nums)
    return [solver.count_greater(i, j, k) for i, j, k in queries]
```

- **Build:** `O(n log n)` time and space.
- **Per query:** `O(log^2 n)`.

## Key Insights & Edge Cases

- **Strict vs non-strict:** `> k` uses `len - bisect_right(list, k)`; `>= k` uses
  `len - bisect_left(list, k)`. Mixing these up is the most common bug here.
- **Offline alternative:** The original SPOJ KQUERY is often solved offline with a BIT by
  sorting both the array and the queries by value in decreasing order. The Merge Sort
  Tree solves it **online** with no need to know all queries in advance.
- **Large `q`:** with up to `2*10^5` queries, read input fast; the per-query cost is the
  bottleneck, not the build.
- **All elements equal:** if every value is `v`, a query with `k >= v` returns `0` and
  with `k < v` returns the full range length — the binary search handles both.
- **Values up to `10^9`:** no coordinate compression is required because the tree stores
  raw values and only compares against `k`.
