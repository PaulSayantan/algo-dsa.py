# Solution — K-th Smallest Number in Range

## Brute Force

For each query, copy `nums[l..r]`, sort it, and index position `k-1`.

```python
def kth_smallest(nums, l, r, k):
    return sorted(nums[l:r + 1])[k - 1]
```

- **Time:** `O(q * n log n)` — sorting per query. Far too slow for `q, n = 10^5`.
- **Space:** `O(n)` per query for the copy.

## Optimal Approach (Merge Sort Tree + binary search on the answer)

### Core query the tree supports

Build a Merge Sort Tree that answers `count_le(l, r, v)` = "how many elements in
`nums[l..r]` are `<= v`" in `O(log^2 n)` (each node stores its sorted list; count via
`bisect_right`). This is exactly Problem 1.

### Reduce k-th smallest to counting

`count_le(l, r, v)` is **monotonically non-decreasing** in `v`. The k-th smallest value of
the subarray is the **smallest value `v` present in the array** such that
`count_le(l, r, v) >= k`. So:

1. Let `sorted_distinct` be the sorted array of distinct values of `nums` (built once).
2. Binary search over `sorted_distinct` for the smallest `v` with `count_le(l, r, v) >= k`.
3. That `v` is the answer.

The outer binary search runs `O(log n)` iterations (over the distinct values), and each
iteration performs one `O(log^2 n)` count query, giving `O(log^3 n)` per query and
`O(q log^3 n)` overall — comfortably fast for the limits.

### Why it is correct

If the subarray were sorted, the k-th smallest is the value at rank `k`. For a value `v`,
`count_le(l, r, v)` is the number of subarray elements at or below `v`. The k-th smallest
is the least `v` for which at least `k` elements are `<= v`; any smaller candidate has a
count `< k` (not enough elements below it), and this `v` itself is attained by some
element (so it is a real array value, not a gap). Restricting the search to values that
actually occur guarantees we return an element that exists in the range. Duplicates are
handled because the count includes equal values (see Example 2: 3rd smallest of
`[2,2,4,4]` is `4`).

### Reference implementation

```python
from bisect import bisect_right, bisect_left
from typing import List


class KthSmallestSolver:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.tree = [[] for _ in range(4 * max(self.n, 1))]
        self.sorted_distinct = sorted(set(nums))
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

    def _count_le(self, node, lo, hi, l, r, v):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return bisect_right(self.tree[node], v)
        mid = (lo + hi) // 2
        return (self._count_le(2 * node, lo, mid, l, r, v)
                + self._count_le(2 * node + 1, mid + 1, hi, l, r, v))

    def kth_smallest(self, l, r, k):
        # binary search over distinct values for smallest v with count_le >= k
        vals = self.sorted_distinct
        blo, bhi = 0, len(vals) - 1
        ans = vals[bhi]
        while blo <= bhi:
            mid = (blo + bhi) // 2
            if self._count_le(1, 0, self.n - 1, l, r, vals[mid]) >= k:
                ans = vals[mid]
                bhi = mid - 1
            else:
                blo = mid + 1
        return ans


def kth_smallest_queries(nums, queries):
    solver = KthSmallestSolver(nums)
    return [solver.kth_smallest(l, r, k) for l, r, k in queries]
```

- **Build:** `O(n log n)` time and space.
- **Per query:** `O(log^3 n)` (value binary search x count query).

### Faster `O(log n)` per query (the "walk down" trick)

Instead of binary searching on the value, select directly. At the root, the sorted list
covers everything. Descend: at a node split at `mid`, compute `t` = the number of range
elements that fall in the **left child** (via two binary searches on the left child's list
for the range boundaries, or by precomputed positions). If `t >= k`, recurse left;
otherwise recurse right with `k -= t`. This reaches a leaf in `O(log n)` node steps, each
doing `O(log n)` work — `O(log^2 n)`; with the persistent segment tree variant it is a
clean `O(log n)`. The binary-search-on-answer version above is simpler and usually fast
enough.

## Key Insights & Edge Cases

- **1-based `k`:** the problem uses `k = 1` for the minimum. Guard your indexing so that
  `k = r - l + 1` returns the maximum of the range.
- **Search over occurring values only:** binary searching the *distinct sorted values*
  (not the raw integer range `[-10^9, 10^9]`) guarantees the returned value is an actual
  element and keeps the search to `O(log n)` steps. Searching the integer range also works
  but does more iterations.
- **Duplicates** are counted with multiplicity by `count_le`, so ranks land on the correct
  repeated value (Example 2).
- **Monotonicity is the whole trick:** `count_le(l, r, v)` never decreases as `v` grows,
  which is what makes the binary search valid.
- **Static array only** — like every Merge Sort Tree, values may not change between
  queries. For updates, use a BIT/segment tree of sorted structures, sqrt-decomposition,
  or an offline approach.
- **Negative values / large magnitudes** need no special handling; comparisons and
  `bisect` work on raw values.
