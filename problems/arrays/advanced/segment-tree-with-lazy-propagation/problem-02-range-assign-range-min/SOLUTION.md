# Solution — Range Assign and Range Minimum Query

## Brute Force

Keep the raw array.

- `assign(l, r, val)`: loop `i` from `l` to `r`, set `arr[i] = val`. `O(n)`.
- `minRange(l, r)`: scan the range for the minimum. `O(n)`.

With `10^5` operations over ranges of size up to `10^5`, this is `O(q * n)` ≈
`10^10` — too slow.

- **Time:** `O(n)` per operation. **Space:** `O(n)`.

## Optimal Approach — Segment Tree with Lazy Propagation

Each node covering `[lo, hi]` stores:

- `mn` — the minimum of the covered elements, **already reflecting** any pending
  assignment on this node;
- `lazy` — a pending *assignment* value, or a sentinel `None` meaning "nothing
  pending".

### The crucial difference from range-add: overwrite semantics

For an **assignment**, the value that will ultimately sit in the range is `val`,
regardless of history. So:

- `apply(node, val)`: the whole covered range becomes `val`, hence its minimum is
  also `val`: `mn = val; lazy = val`. Note there is **no `* length`** factor — the
  min of a constant range is just that constant.
- When we push an assignment tag to a child, we **overwrite** the child's `mn` and
  the child's `lazy` (we do *not* combine). This is why a later assignment on a
  parent correctly erases an earlier, smaller-range assignment stored below it —
  the earlier one gets pushed down first, then immediately clobbered when the
  parent's newer tag reaches the same node.

### Operations

**push_down(node):** if `lazy is not None`, `apply` it to both children, then set
`lazy = None`.

**assign(l, r, val):** three-case recursion — no overlap → return; full cover →
`apply(node, val)`; partial → `push_down`, recurse, then `mn = min(left.mn,
right.mn)`.

**minRange(l, r):** three-case recursion; on partial overlap `push_down` first,
then combine children with `min`. A non-overlapping branch returns `+∞`.

### Why it is correct

Invariant 1: a node's `mn` already reflects its own pending assignment, so a fully
covered node is answered/updated without descending. Invariant 2: a node's `lazy`
is not yet in its children, so we `push_down` before any partial descent.
Assignment is *idempotent and overriding* — the last writer wins — so pushing a
tag down and then overwriting it with a newer one from above reproduces exactly
the effect of applying the operations in order.

### Reference implementation

```python
from typing import List, Optional

INF = float("inf")


class RangeAssignRangeMin:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.mn = [0] * (4 * self.n)
        self.lazy: List[Optional[int]] = [None] * (4 * self.n)
        self._build(1, 0, self.n - 1, nums)

    def _build(self, node, lo, hi, nums) -> None:
        if lo == hi:
            self.mn[node] = nums[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, nums)
        self._build(2 * node + 1, mid + 1, hi, nums)
        self.mn[node] = min(self.mn[2 * node], self.mn[2 * node + 1])

    def _apply(self, node, val) -> None:
        self.mn[node] = val       # min of a constant range is the constant
        self.lazy[node] = val     # overwrite, do NOT combine

    def _push_down(self, node) -> None:
        if self.lazy[node] is not None:
            self._apply(2 * node, self.lazy[node])
            self._apply(2 * node + 1, self.lazy[node])
            self.lazy[node] = None

    def assign(self, left, right, val) -> None:
        self._assign(1, 0, self.n - 1, left, right, val)

    def _assign(self, node, lo, hi, l, r, val) -> None:
        if r < lo or hi < l:
            return
        if l <= lo and hi <= r:
            self._apply(node, val)
            return
        mid = (lo + hi) // 2
        self._push_down(node)
        self._assign(2 * node, lo, mid, l, r, val)
        self._assign(2 * node + 1, mid + 1, hi, l, r, val)
        self.mn[node] = min(self.mn[2 * node], self.mn[2 * node + 1])

    def minRange(self, left, right) -> int:
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node, lo, hi, l, r) -> int:
        if r < lo or hi < l:
            return INF
        if l <= lo and hi <= r:
            return self.mn[node]
        mid = (lo + hi) // 2
        self._push_down(node)
        return min(self._query(2 * node, lo, mid, l, r),
                   self._query(2 * node + 1, mid + 1, hi, l, r))
```

- **Time:** `O(n)` build, `O(log n)` per assign/query. **Space:** `O(n)`.

## Key Insights & Edge Cases

- **Sentinel matters.** You must distinguish "assign to 0" from "no pending
  assignment". Using `0` as the empty tag is a classic bug; use `None` (or a
  boolean `has_lazy` flag alongside the value).
- **No length factor.** Unlike sum, the min of a constant range is just the
  constant — do *not* multiply by range length.
- **Overwrite, don't accumulate.** `apply` sets `lazy = val`; it never adds. A
  newer assignment fully supersedes an older one on the same subtree.
- **Neutral element for min is `+∞`**, returned on the no-overlap branch so it
  never wins a `min`.
- **Single element / `left == right`** works via the `lo == hi` base case.
- If you later need *both* assign and add (see Problem 5), the tag algebra gets
  more involved: an assign must clear any pending add, while an add composes on
  top of an assign.
