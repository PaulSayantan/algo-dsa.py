# Solution — Range Add and Range Sum Query

## Brute Force

Keep the array as-is.

- `update(l, r, val)`: loop `i` from `l` to `r`, `arr[i] += val`. `O(n)`.
- `sumRange(l, r)`: loop and accumulate. `O(n)`.

With up to `10^5` operations each touching up to `10^5` elements, this is
`O(q * n) ≈ 10^10` — far too slow.

A prefix-sum array makes `sumRange` `O(1)` but forces every `update` to rebuild
the prefix sums in `O(n)`, so it does not help a mixed workload.

- **Time:** `O(n)` per operation. **Space:** `O(n)`.

## Optimal Approach — Segment Tree with Lazy Propagation

Each node covers a range `[lo, hi]` and stores:

- `sum` — the sum of the covered elements, **already reflecting** this node's own
  pending add;
- `lazy` — an additive amount that has **not yet been pushed** to the children.

### Core operations

**apply(node, add, length):** applying an add of `add` to a node covering
`length` elements increases its sum by `add * length` and accumulates the tag:
`sum += add * length; lazy += add`.

**push_down(node, left_len, right_len):** if `lazy != 0`, apply it to both
children and reset `lazy = 0`.

**update(l, r, val):** standard three-case recursion —
- no overlap → return;
- full cover → `apply` and stop (this is where laziness saves work);
- partial → `push_down`, recurse both children, then `sum = left.sum + right.sum`.

**query(l, r):** same three cases; on partial overlap `push_down` first so the
children are consistent before you read them.

### Why it is correct

The two invariants hold at all times:

1. A node's `sum` includes its own lazy tag, so a *fully covered* node can be read
   or updated without touching children.
2. A node's lazy tag is *not* yet in its children, so before descending on a
   partial overlap we `push_down`, restoring consistency for the sub-recursions.
   Add is associative and commutative, so accumulating tags (`lazy += add`) and
   pushing them later yields the same result as applying them immediately.

Because each of update/query visits `O(log n)` nodes (at most two per level that
partially overlap the query range) and does `O(1)` work per node, both run in
`O(log n)`.

### Reference implementation

```python
from typing import List


class RangeAddRangeSum:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.sum = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, nums)

    def _build(self, node: int, lo: int, hi: int, nums: List[int]) -> None:
        if lo == hi:
            self.sum[node] = nums[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, nums)
        self._build(2 * node + 1, mid + 1, hi, nums)
        self.sum[node] = self.sum[2 * node] + self.sum[2 * node + 1]

    def _apply(self, node: int, lo: int, hi: int, val: int) -> None:
        self.sum[node] += val * (hi - lo + 1)
        self.lazy[node] += val

    def _push_down(self, node: int, lo: int, mid: int, hi: int) -> None:
        if self.lazy[node]:
            self._apply(2 * node, lo, mid, self.lazy[node])
            self._apply(2 * node + 1, mid + 1, hi, self.lazy[node])
            self.lazy[node] = 0

    def update(self, left: int, right: int, val: int) -> None:
        self._update(1, 0, self.n - 1, left, right, val)

    def _update(self, node, lo, hi, l, r, val) -> None:
        if r < lo or hi < l:
            return
        if l <= lo and hi <= r:
            self._apply(node, lo, hi, val)
            return
        mid = (lo + hi) // 2
        self._push_down(node, lo, mid, hi)
        self._update(2 * node, lo, mid, l, r, val)
        self._update(2 * node + 1, mid + 1, hi, l, r, val)
        self.sum[node] = self.sum[2 * node] + self.sum[2 * node + 1]

    def sumRange(self, left: int, right: int) -> int:
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node, lo, hi, l, r) -> int:
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self.sum[node]
        mid = (lo + hi) // 2
        self._push_down(node, lo, mid, hi)
        return (self._query(2 * node, lo, mid, l, r)
                + self._query(2 * node + 1, mid + 1, hi, l, r))
```

- **Time:** `O(n)` build, `O(log n)` per update/query. **Space:** `O(n)`.

## Key Insights & Edge Cases

- **Store `sum`, tag `add`.** The aggregate is a sum; the natural range delta is
  an additive value scaled by the range length. Forgetting the `* length` factor
  is the most common bug.
- **`lazy += val`, never `lazy = val`.** Adds *compose*; overwriting would drop an
  earlier pending add. (Contrast with the assignment tag in Problem 2.)
- **Push down before every partial descent** — both in `update` and in `query`.
- **Recombine after recursing** (`sum = left + right`) so ancestors stay correct.
- **Single-element arrays** (`n = 1`) and **`left == right`** queries must work;
  the `lo == hi` base case handles them.
- **Overflow:** with `10^5` elements up to `~10^9` after many adds, use 64-bit
  sums (Python integers are unbounded, but note this when porting to C++/Java).
