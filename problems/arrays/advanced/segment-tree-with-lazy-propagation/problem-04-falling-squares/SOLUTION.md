# Solution — Falling Squares

## Brute Force

Maintain a list of landed squares, each stored as `(left, right, top)` where
`right = left + side` and `top` is its top-edge height.

For a new square `[l, r)`:

1. Scan all previously landed squares; find `base = max(top of every square whose
   interval overlaps [l, r) with positive length)`, or `0` if none.
2. Its new top is `base + side`.
3. Record `running_max = max(running_max, base + side)`.

With `m` squares, step 1 is `O(m)` per drop, giving `O(m^2)` overall. For
`m ≤ 1000` this is `~10^6` and actually passes — but it does not generalize, and
it is exactly the workload a lazy segment tree turns into `O(m log m)`.

- **Time:** `O(m^2)`. **Space:** `O(m)`.

## Optimal Approach — Segment Tree with Lazy Propagation

The interval a square covers is continuous, but only the `2m` interval endpoints
matter. Compress them, then run a **range-assign + range-max** lazy segment tree
over the compressed cells.

### Coordinate compression with half-open intervals

Each square occupies `[left, left + side]`. To make "touching at a point" *not*
count as overlap, treat each square as a **half-open** interval and index the gaps
*between* consecutive distinct coordinates rather than the coordinates themselves.

Concretely: collect every `left` and every `left + side`, sort and dedupe into
`xs`. A square `[l, r]` maps to the compressed cell range `[idx(l), idx(r) - 1]`
(inclusive over cells). Because `r` maps to the boundary and we stop at
`idx(r) - 1`, a square starting exactly where another ends shares no cell — which
is the desired "touch at a point does not stack" behavior (Example 2).

### The segment tree: range assign + range max

Each node over compressed cells `[lo, hi]` stores:

- `mx` — the maximum top-height over its cells, reflecting its own pending
  assignment;
- `lazy` — a pending assignment value, or `None` for "nothing pending".

`apply(node, val)`: the whole covered range becomes height `val`, so `mx = val`
and `lazy = val` (overwrite; assignment, like Problem 2, does *not* combine).
`push_down` overwrites both children and clears the tag. `query` combines children
by `max` and uses `0` as the neutral element (ground level).

### Per-square procedure

```
for (left, side) in positions:
    l = idx(left); r = idx(left + side) - 1     # compressed cell range
    base = query_max(l, r)                       # highest surface under the square
    top  = base + side
    assign(l, r, top)                            # the square now sits at height `top`
    running_max = max(running_max, top)
    ans.append(running_max)
```

### Why it is correct

`query_max(l, r)` returns the highest existing top edge over the cells the new
square covers — that is precisely the surface it lands on. Assigning `top` across
`[l, r]` records that those cells are now capped by this square (an *overwrite*,
because the new square is strictly above everything under it). The two lazy
invariants (Problem 2) guarantee the assign/query pair is `O(log m)`. The half-open
mapping ensures point-touching squares occupy disjoint cell ranges, so they never
stack.

### Reference implementation

```python
from typing import List, Optional
from bisect import bisect_left


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        xs = sorted({x for l, s in positions for x in (l, l + s)})
        idx = {x: i for i, x in enumerate(xs)}
        n = len(xs)                       # cells 0 .. n-2 are the gaps; n leaves is safe
        mx = [0] * (4 * n)
        lazy: List[Optional[int]] = [None] * (4 * n)

        def apply(node, val):
            mx[node] = val
            lazy[node] = val

        def push_down(node):
            if lazy[node] is not None:
                apply(2 * node, lazy[node])
                apply(2 * node + 1, lazy[node])
                lazy[node] = None

        def assign(node, lo, hi, l, r, val):
            if r < lo or hi < l:
                return
            if l <= lo and hi <= r:
                apply(node, val)
                return
            mid = (lo + hi) // 2
            push_down(node)
            assign(2 * node, lo, mid, l, r, val)
            assign(2 * node + 1, mid + 1, hi, l, r, val)
            mx[node] = max(mx[2 * node], mx[2 * node + 1])

        def query(node, lo, hi, l, r):
            if r < lo or hi < l:
                return 0
            if l <= lo and hi <= r:
                return mx[node]
            mid = (lo + hi) // 2
            push_down(node)
            return max(query(2 * node, lo, mid, l, r),
                       query(2 * node + 1, mid + 1, hi, l, r))

        ans, best = [], 0
        for left, side in positions:
            l = idx[left]
            r = idx[left + side] - 1          # half-open: exclude the right boundary
            base = query(1, 0, n - 1, l, r)
            top = base + side
            assign(1, 0, n - 1, l, r, top)
            best = max(best, top)
            ans.append(best)
        return ans
```

- **Time:** `O(m log m)` — sort/compress `O(m log m)`, then `O(log m)` per query
  and per assign over `m` squares. **Space:** `O(m)`.

## Key Insights & Edge Cases

- **Half-open intervals are the crux.** Mapping `[l, r]` to cells `[idx(l),
  idx(r) - 1]` is what makes point-touching squares (Example 2) *not* stack. Using
  the closed range `[idx(l), idx(r)]` would incorrectly merge them.
- **Assignment tag, not additive.** A landing square rests strictly above whatever
  is beneath it, so its cells are *overwritten* to `top` (`max`-aggregate with an
  assign lazy tag), exactly like Problem 2. A `None` sentinel distinguishes "no
  pending assign".
- **Neutral element for max is `0`** (ground level), returned on non-overlap.
- **Running maximum, not per-square top.** The answer is the max top edge seen *so
  far*, so a later short square (Example 1's third drop) keeps the previous, larger
  value.
- **Coordinates are large but few** (`left` up to `10^8`); compression shrinks the
  index space to `O(m)` so `4n` node arrays stay tiny.
- **A single square** works: it queries `0`, lands at height `side`.
