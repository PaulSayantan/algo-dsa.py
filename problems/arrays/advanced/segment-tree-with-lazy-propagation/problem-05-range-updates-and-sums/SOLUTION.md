# Solution — Range Updates and Sums

## Brute Force

Keep the raw array.

- `add(l, r, x)`: loop and `arr[i] += x`. `O(n)`.
- `assign(l, r, x)`: loop and `arr[i] = x`. `O(n)`.
- `sum(l, r)`: scan and accumulate. `O(n)`.

With `n, q` up to `2 * 10^5` and ranges up to size `n`, this is `O(q * n) ≈
4 * 10^10` — far too slow.

- **Time:** `O(n)` per operation. **Space:** `O(n)`.

## Optimal Approach — Segment Tree with Lazy Propagation (two tags)

This problem combines Problem 1 (range add + sum) and Problem 2 (range assign),
so a node must hold **both** kinds of pending update. Each node over `[lo, hi]`
stores:

- `sum` — the subtree sum, already reflecting *both* of this node's tags;
- `assign_tag` — a pending assignment value, or `None` if none is pending;
- `add_tag` — a pending additive amount (`0` means none).

### The tag algebra (the whole game)

The semantics of a *single element* under a pending assign `A` then a pending add
`D` is: value becomes `A + D` if an assign is pending, else `old + D`. The two
tags interact as follows.

**apply_assign(node, val):** an assignment wipes history on this range.
```
sum        = val * length
assign_tag = val
add_tag    = 0            # <-- crucial: the assign cancels any pending add
```

**apply_add(node, val):** an add composes on top of whatever is there (including a
pending assign, since we keep `assign_tag` untouched and just grow `add_tag`).
```
sum      += val * length
add_tag  += val
```

**push_down(node):** push the **assign first, then the add** to each child:
```
if assign_tag is not None:
    apply_assign(left,  assign_tag);  apply_assign(right, assign_tag)
    assign_tag = None
if add_tag != 0:
    apply_add(left,  add_tag);  apply_add(right, add_tag)
    add_tag = 0
```
Order matters: a child might itself carry an older assign+add. Pushing the
parent's *assign* first correctly clears that child's stale `add_tag` (via
`apply_assign`), and then the parent's *add* is layered on top — reproducing "the
add happened after the assign", which is exactly the order in which the parent
accumulated them.

### Why this order is correct

The parent's own tags were built by `apply_assign` / `apply_add` calls in *time
order*. Because `apply_assign` always zeroes `add_tag`, at any moment the parent's
`(assign_tag, add_tag)` encodes "optionally assign to `assign_tag`, then add
`add_tag`" — the add is always the *later* action. Replaying that on the children
in the same order (assign then add) is faithful. Together with the two standard
lazy invariants (a node's `sum` includes its own tags; a node's tags are not yet
in its children), every `add` / `assign` / `sum` visits `O(log n)` nodes.

### Reference implementation

```python
from typing import List, Optional


class RangeUpdatesAndSums:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        size = 4 * self.n
        self.sum = [0] * size
        self.add_tag = [0] * size
        self.assign_tag: List[Optional[int]] = [None] * size
        self._build(1, 0, self.n - 1, nums)

    def _build(self, node, lo, hi, nums):
        if lo == hi:
            self.sum[node] = nums[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, nums)
        self._build(2 * node + 1, mid + 1, hi, nums)
        self.sum[node] = self.sum[2 * node] + self.sum[2 * node + 1]

    def _apply_assign(self, node, lo, hi, val):
        self.sum[node] = val * (hi - lo + 1)
        self.assign_tag[node] = val
        self.add_tag[node] = 0            # assign cancels pending add

    def _apply_add(self, node, lo, hi, val):
        self.sum[node] += val * (hi - lo + 1)
        self.add_tag[node] += val

    def _push_down(self, node, lo, mid, hi):
        if self.assign_tag[node] is not None:
            self._apply_assign(2 * node, lo, mid, self.assign_tag[node])
            self._apply_assign(2 * node + 1, mid + 1, hi, self.assign_tag[node])
            self.assign_tag[node] = None
        if self.add_tag[node]:
            self._apply_add(2 * node, lo, mid, self.add_tag[node])
            self._apply_add(2 * node + 1, mid + 1, hi, self.add_tag[node])
            self.add_tag[node] = 0

    def add(self, left, right, x):
        self._add(1, 0, self.n - 1, left, right, x)

    def _add(self, node, lo, hi, l, r, x):
        if r < lo or hi < l:
            return
        if l <= lo and hi <= r:
            self._apply_add(node, lo, hi, x)
            return
        mid = (lo + hi) // 2
        self._push_down(node, lo, mid, hi)
        self._add(2 * node, lo, mid, l, r, x)
        self._add(2 * node + 1, mid + 1, hi, l, r, x)
        self.sum[node] = self.sum[2 * node] + self.sum[2 * node + 1]

    def assign(self, left, right, x):
        self._assign(1, 0, self.n - 1, left, right, x)

    def _assign(self, node, lo, hi, l, r, x):
        if r < lo or hi < l:
            return
        if l <= lo and hi <= r:
            self._apply_assign(node, lo, hi, x)
            return
        mid = (lo + hi) // 2
        self._push_down(node, lo, mid, hi)
        self._assign(2 * node, lo, mid, l, r, x)
        self._assign(2 * node + 1, mid + 1, hi, l, r, x)
        self.sum[node] = self.sum[2 * node] + self.sum[2 * node + 1]

    def sum(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node, lo, hi, l, r):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self.sum[node]
        mid = (lo + hi) // 2
        self._push_down(node, lo, mid, hi)
        return (self._query(2 * node, lo, mid, l, r)
                + self._query(2 * node + 1, mid + 1, hi, l, r))
```

- **Time:** `O(n)` build, `O(log n)` per operation → `O((n + q) log n)` overall.
  **Space:** `O(n)`.

## Key Insights & Edge Cases

- **Assign must zero the add tag.** The single most common bug: forgetting
  `add_tag = 0` inside `apply_assign` leaves a stale add that resurrects after the
  overwrite. Example 2 catches exactly this — the earlier `add(0,2,3)` must not
  survive the `assign(1,2,0)` on indices 1–2.
- **Push assign before add.** Reverse the order and you apply the parent's add
  *before* clearing the child's older tags, corrupting the child.
- **`None` sentinel for assign**, distinct from `0` — you can legitimately assign
  `0` (Example 2 does).
- **Both tags need the `* length` factor for the sum** aggregate.
- **64-bit sums.** With `2 * 10^5` elements and values up to `~10^9` after many
  adds, sums reach `~10^{14}` — use 64-bit integers when porting (Python's ints
  are unbounded).
- **This pattern generalizes:** whenever two range operations must coexist, define
  `apply` for each tag, decide how a new tag *composes into* an existing node, and
  push tags in the correct dependency order.
