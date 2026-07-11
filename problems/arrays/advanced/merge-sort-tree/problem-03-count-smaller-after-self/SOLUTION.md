# Solution — Count of Smaller Numbers After Self

## Brute Force

For every index `i`, scan the suffix to its right and count strictly smaller elements.

```python
def countSmaller(nums):
    n = len(nums)
    return [sum(1 for j in range(i + 1, n) if nums[j] < nums[i]) for i in range(n)]
```

- **Time:** `O(n^2)` — `~10^10` for `n = 10^5`. Too slow.
- **Space:** `O(1)` extra (besides the output).

## Optimal Approach (Merge Sort Tree)

### Reframe as range queries

`counts[i]` asks: *how many elements in the suffix `nums[i+1 .. n-1]` are strictly less
than `nums[i]`?* That is exactly a "count values `< x` over an index range" query on a
static array — the Merge Sort Tree's home turf.

### Build the tree

Build a segment tree over indices `0..n-1`; each node stores the sorted list of its
range's values, formed by merging its children. Build cost: `O(n log n)`.

### Answer each index

For each `i`, query the range `[i+1, n-1]` with threshold `x = nums[i]`, counting
elements strictly `< x`. In each of the `O(log n)` canonical nodes, the count of
elements `< x` is `bisect_left(node_list, x)`. Sum across the nodes. If `i == n-1` the
range is empty and the answer is `0`.

- **Total time:** `O(n log^2 n)` — `n` queries, each `O(log^2 n)`.
- **Space:** `O(n log n)` for the tree.

### Why it is correct

The suffix `[i+1, n-1]` is decomposed into disjoint canonical index ranges by the
segment tree; `bisect_left(list, nums[i])` in each returns the count of values strictly
below `nums[i]` in that node, and strict-less counting is additive over the partition,
so the sum is exact. Using `bisect_left` (not `bisect_right`) is what enforces the
**strict** `<` — equal values to the right are correctly excluded.

### Reference implementation

```python
from bisect import bisect_left
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        tree = [[] for _ in range(4 * n)]

        def build(node, lo, hi):
            if lo == hi:
                tree[node] = [nums[lo]]
                return
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            a, b = tree[2 * node], tree[2 * node + 1]
            merged, p, q = [], 0, 0
            while p < len(a) and q < len(b):
                if a[p] <= b[q]:
                    merged.append(a[p]); p += 1
                else:
                    merged.append(b[q]); q += 1
            merged.extend(a[p:]); merged.extend(b[q:])
            tree[node] = merged

        def query(node, lo, hi, l, r, x):
            if r < l or r < lo or hi < l:      # empty or disjoint
                return 0
            if l <= lo and hi <= r:
                return bisect_left(tree[node], x)   # count of elements < x
            mid = (lo + hi) // 2
            return (query(2 * node, lo, mid, l, r, x)
                    + query(2 * node + 1, mid + 1, hi, l, r, x))

        build(1, 0, n - 1)
        return [query(1, 0, n - 1, i + 1, n - 1, nums[i]) for i in range(n)]
```

## Key Insights & Edge Cases

- **Strict `<`:** use `bisect_left`. Using `bisect_right` would wrongly count equal
  elements (see Example 2, where two `-1`s must both yield `0`).
- **Empty suffix:** for `i == n-1`, `[i+1, n-1]` is empty; guard with `r < l -> 0`.
- **Negative values / duplicates:** handled directly; the tree stores raw values.
- **Alternative canonical solutions:** a modified merge sort that counts cross-pair
  inversions, or a Fenwick tree over coordinate-compressed values, both run in
  `O(n log n)`. The Merge Sort Tree is a `log` factor slower but generalizes instantly
  to *arbitrary* ranges (not just suffixes) and to online queries.
- **Recursion depth:** the tree has depth `O(log n)`; per-index queries do not deepen it.
  For very large `n` in Python, an iterative or `sys.setrecursionlimit`-guarded build is
  advisable.
