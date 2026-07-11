# Range Minimum Query (Mutable) — Solution

## Brute Force

Keep the array; `query(l, r)` scans `arr[l..r]` and returns the running minimum.

- `update`: `O(1)`.
- `query`: `O(n)`.
- Overall `O(q * n)` — up to `~2 * 10^10` operations at the constraint limits. Too slow.

A **sparse table** answers static RMQ in `O(1)` after `O(n log n)` preprocessing, but
it does **not** support updates (rebuilding is `O(n log n)` per update). Because this
problem interleaves updates, we need a structure that updates cheaply too.

- Brute force time: `O(1)` update, `O(n)` query. Space `O(n)`.

## Optimal Approach — Segment Tree

Identical structure to range-sum, but each node stores the **minimum** of its range,
and the merge is `min` instead of `+`.

### Why it is correct

`min` is associative and has identity `+infinity`. For any node,
`value = min(left_child, right_child)`. A query range `[l, r]` decomposes into
`O(log n)` node ranges that tile it exactly; the min of those node values is the min
of the whole range. An update rewrites one leaf and re-mins every ancestor, so the
invariant holds throughout.

### Step by step (recursive, `4n` array)

1. **Build(node, lo, hi):** if `lo == hi`, `tree[node] = arr[lo]`; else build both
   halves and set `tree[node] = min(children)`. `O(n)`.
2. **Update(node, lo, hi, idx, val):** recurse into the half containing `idx`; on the
   way back set `tree[node] = min(children)`. `O(log n)`.
3. **Query(node, lo, hi, l, r):**
   - if `[lo, hi]` is disjoint from `[l, r]`: return `+infinity` (identity),
   - if `[lo, hi] ⊆ [l, r]`: return `tree[node]`,
   - else return `min(query(left), query(right))`. `O(log n)`.

### Reference implementation

```python
from typing import List


class RangeMin:
    def __init__(self, arr: List[int]) -> None:
        self.n = len(arr)
        self.arr = arr[:]
        self.tree = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1)

    def _build(self, node: int, lo: int, hi: int) -> None:
        if lo == hi:
            self.tree[node] = self.arr[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid)
        self._build(2 * node + 1, mid + 1, hi)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, index: int, val: int) -> None:
        self._update(1, 0, self.n - 1, index, val)

    def _update(self, node: int, lo: int, hi: int, idx: int, val: int) -> None:
        if lo == hi:
            self.tree[node] = val
            return
        mid = (lo + hi) // 2
        if idx <= mid:
            self._update(2 * node, lo, mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, hi, idx, val)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, left: int, right: int) -> int:
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node: int, lo: int, hi: int, l: int, r: int) -> int:
        if r < lo or hi < l:            # disjoint
            return float("inf")
        if l <= lo and hi <= r:         # fully covered
            return self.tree[node]
        mid = (lo + hi) // 2
        return min(self._query(2 * node, lo, mid, l, r),
                   self._query(2 * node + 1, mid + 1, hi, l, r))
```

### Complexity

- Build `O(n)`; `update` `O(log n)`; `query` `O(log n)`; space `O(n)` (the `4n`
  array is a constant factor).

## Key Insights & Edge Cases

- **Identity element matters.** For `min` the identity is `+infinity`, so a fully
  disjoint node contributes nothing. For `max` use `-infinity`, for `sum` use `0`,
  for `gcd` use `0`. Choosing the wrong identity is the most common bug.
- **Only the merge changes.** The traversal skeleton is identical to range-sum; this
  is why a segment tree is best learned once and reused for many aggregates.
- **Large / negative values** are handled directly — no offset tricks needed.
- **Single-element query** returns that element (the "fully covered" base case fires
  at the leaf).
- **`n == 1`** is fine: the root is also the only leaf.
- Segment tree beats a sparse table here purely because of the interleaved updates;
  if the array were static, the sparse table's `O(1)` query would win.
