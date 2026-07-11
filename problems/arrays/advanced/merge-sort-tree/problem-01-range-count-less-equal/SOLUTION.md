# Solution — Range Count of Elements ≤ X

## Brute Force

For each query `(l, r, x)`, scan the subarray `nums[l..r]` and count how many elements
are `<= x`.

```python
def count_at_most(nums, l, r, x):
    return sum(1 for i in range(l, r + 1) if nums[i] <= x)
```

- **Time:** `O(q * n)` — up to `10^5 * 10^5 = 10^10` operations. Far too slow.
- **Space:** `O(1)` extra.

A better-than-naive but still limited idea is to sort the whole array once and binary
search, but that only works for the *entire* array, not for arbitrary subranges — the
threshold count depends on which indices fall inside `[l, r]`.

## Optimal Approach (Merge Sort Tree)

### Structure

Build a segment tree over the indices `0..n-1`. Each node covers a contiguous index
range `[lo, hi]` and stores the **sorted list of the values** `nums[lo..hi]`.

- A leaf `[i, i]` stores the single-element list `[nums[i]]`.
- An internal node's sorted list is the **merge** of its two children's sorted lists
  (exactly the merge step of merge sort). Since the children are already sorted, the
  merge is linear in the node size.

Across one level of the tree the node sizes sum to `n`, and there are `log n` levels,
so building costs `O(n log n)` time and the stored lists occupy `O(n log n)` space.

### Answering a query

To count elements `<= x` in `nums[l..r]`:

1. Descend the segment tree. The range `[l, r]` is covered by `O(log n)` **canonical
   nodes** whose ranges are fully inside `[l, r]`.
2. For each such node, its stored list is sorted, so the count of elements `<= x` is
   `upper_bound(list, x)` — the number of elements less than or equal to `x`, found by
   binary search in `O(log n)`.
3. Sum these per-node counts.

There are `O(log n)` canonical nodes and each costs `O(log n)` for the binary search,
so a query is `O(log^2 n)`.

### Why it is correct

The canonical decomposition of the segment tree partitions `[l, r]` into disjoint index
ranges whose union is exactly `[l, r]`. Counting `<= x` is additive over a partition, so
summing each node's `upper_bound` count gives the exact total. Within a node, the values
are the same multiset as the original indices (merging preserves the multiset), so the
binary search counts precisely the qualifying elements.

### Reference implementation

```python
from bisect import bisect_right
from typing import List


class RangeCountSolver:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.tree = [[] for _ in range(4 * self.n)]
        if self.n:
            self._build(1, 0, self.n - 1, nums)

    def _build(self, node: int, lo: int, hi: int, nums: List[int]) -> None:
        if lo == hi:
            self.tree[node] = [nums[lo]]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, nums)
        self._build(2 * node + 1, mid + 1, hi, nums)
        # merge the two sorted child lists
        left, right = self.tree[2 * node], self.tree[2 * node + 1]
        merged, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        merged.extend(left[i:]); merged.extend(right[j:])
        self.tree[node] = merged

    def count_at_most(self, l: int, r: int, x: int) -> int:
        return self._query(1, 0, self.n - 1, l, r, x)

    def _query(self, node, lo, hi, l, r, x) -> int:
        if r < lo or hi < l:                 # disjoint
            return 0
        if l <= lo and hi <= r:              # fully inside -> binary search
            return bisect_right(self.tree[node], x)
        mid = (lo + hi) // 2
        return (self._query(2 * node, lo, mid, l, r, x)
                + self._query(2 * node + 1, mid + 1, hi, l, r, x))


def range_count_queries(nums, queries):
    solver = RangeCountSolver(nums)
    return [solver.count_at_most(l, r, x) for l, r, x in queries]
```

- **Build:** `O(n log n)` time, `O(n log n)` space.
- **Per query:** `O(log^2 n)`.

Merging with Python's built-in `sorted(left + right)` also works and is often just as
fast in practice, but the explicit two-pointer merge keeps the `O(node size)` guarantee.

## Key Insights & Edge Cases

- **`<= x` vs `< x`:** use `bisect_right` for `<= x` and `bisect_left` for `< x`. To count
  elements in `[a, b]`, compute `bisect_right(list, b) - bisect_left(list, a)`.
- **Static array only.** The sorted lists cannot be cheaply updated. If values change,
  use a different structure (wavelet tree, BIT of sorted arrays, or offline sorting).
- **Negative values and duplicates** are handled naturally — the tree stores raw values
  and binary search respects duplicates.
- **Single-element / degenerate ranges** (`l == r`) fall out correctly: the recursion
  reaches a leaf whose one-element list is binary searched.
- **`x` smaller than all / larger than all**: `upper_bound` returns `0` or the node size
  respectively, so the sum is `0` or the full range length — both correct.
- **Memory:** for `n = 10^5`, the tree stores about `n * log2(n) ≈ 1.7 * 10^6` integers,
  which is fine. Using `4 * n` slots for the tree array is a safe upper bound.
