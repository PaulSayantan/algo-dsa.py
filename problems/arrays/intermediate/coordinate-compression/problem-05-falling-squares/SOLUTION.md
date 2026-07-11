# Falling Squares — Solution

## Brute Force

Keep a list of landed squares as `(left, right, height)` intervals. For each new square,
scan all previously landed squares; if their X-ranges overlap (strictly, not just touching),
the new square must rest above them. Its base height is the max top of every overlapping
square, and its new top is that base plus its side length.

```python
def fallingSquares(positions):
    intervals = []       # (left, right, top_height)
    res = []
    best = 0
    for left, side in positions:
        right = left + side
        base = 0
        for l, r, h in intervals:
            if left < r and l < right:      # strict overlap (touching edges excluded)
                base = max(base, h)
        top = base + side
        intervals.append((left, right, top))
        best = max(best, top)
        res.append(best)
    return res
```

- **Time:** `O(n^2)` — each drop scans all earlier squares. With `n <= 1000` this is only
  ~10^6 operations and actually passes, but it does not generalize to larger `n`.
- **Space:** `O(n)`.

## Optimal Approach (Coordinate Compression + Segment Tree)

Think of the X-axis as a set of intervals. Dropping a square over `[left, right)` means:

1. **Query** the maximum current height over `[left, right)` — that is the surface it lands
   on; its new top is `queryMax + side`.
2. **Update** the whole interval `[left, right)` to that new top (a range assignment, since
   the entire footprint now sits at the same height).

A segment tree with *range-assign* (lazy) and *range-max* does both in `O(log k)`. The catch
is that `left`/`right` reach `10^8`. But there are at most `2n <= 2000` distinct edges, so we
**compress** the edges into indices `0 .. k-1` and build the tree over those `k` positions.

We index by the **gaps between consecutive edges** (half-open intervals), which correctly
models that two squares merely touching at a shared edge do not overlap.

```python
def fallingSquares(positions):
    # 1. collect and compress edges
    xs = sorted({x for l, s in positions for x in (l, l + s)})
    idx = {x: i for i, x in enumerate(xs)}
    n = len(xs)                       # number of distinct edges

    # segment tree over the n edge-indices; a square [l, r) maps to indices
    # [idx[l], idx[r] - 1]  (the gaps strictly inside), so touching edges don't overlap.
    seg = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def push_down(node):
        if lazy[node]:
            for child in (2 * node, 2 * node + 1):
                seg[child] = max(seg[child], lazy[node])
                lazy[child] = max(lazy[child], lazy[node])
            lazy[node] = 0

    def update(node, lo, hi, ql, qr, val):
        if qr < lo or hi < ql:
            return
        if ql <= lo and hi <= qr:
            seg[node] = max(seg[node], val)
            lazy[node] = max(lazy[node], val)
            return
        push_down(node)
        mid = (lo + hi) // 2
        update(2 * node, lo, mid, ql, qr, val)
        update(2 * node + 1, mid + 1, hi, ql, qr, val)
        seg[node] = max(seg[2 * node], seg[2 * node + 1])

    def query(node, lo, hi, ql, qr):
        if qr < lo or hi < ql:
            return 0
        if ql <= lo and hi <= qr:
            return seg[node]
        push_down(node)
        mid = (lo + hi) // 2
        return max(query(2 * node, lo, mid, ql, qr),
                   query(2 * node + 1, mid + 1, hi, ql, qr))

    res = []
    best = 0
    for l, s in positions:
        ql, qr = idx[l], idx[l + s] - 1      # half-open -> inclusive gap indices
        cur = query(1, 0, n - 1, ql, qr)
        top = cur + s
        update(1, 0, n - 1, ql, qr, top)
        best = max(best, top)
        res.append(best)
    return res
```

**Why it is correct.**

- Compression keeps only the coordinates that matter (the edges); nothing between two
  consecutive edges ever changes independently, so representing each gap by one tree slot
  loses no information.
- Mapping `[l, l+s)` to inclusive indices `[idx[l], idx[l+s] - 1]` uses the *gap* between
  edges, so a square starting exactly where another ends shares no gap index — modeling the
  "touching does not stack" rule (Example 2).
- `query` returns the highest surface under the footprint; `update` raises the whole
  footprint to the new top so later squares landing here see the correct height.

**Step by step** on `[[1, 2], [2, 3], [6, 1]]`:

- Edges: squares cover `[1,3), [2,5), [6,7)` -> `xs = [1, 2, 3, 5, 6, 7]`,
  `idx = {1:0, 2:1, 3:2, 5:3, 6:4, 7:5}`.
- Square `[1,3)` -> indices `[0, 1]`: query max = 0, top = 2, assign 2. best = 2.
- Square `[2,5)` -> indices `[1, 2]`: query max = 2 (index 1 overlaps square 1), top = 5,
  assign 5. best = 5.
- Square `[6,7)` -> indices `[4, 4]`: query max = 0, top = 1, assign 1. best stays 5.
- Result `[2, 5, 5]`.

- **Time:** `O(n log n)` — sort/compress plus `n` segment-tree operations at `O(log n)`.
- **Space:** `O(n)` for the compressed edges and the segment tree.

## Key Insights & Edge Cases

- **Half-open intervals / the touching rule:** map `[l, r)` to gap indices
  `[idx[l], idx[r] - 1]`. If you instead used `[idx[l], idx[r]]` you would incorrectly stack
  squares that merely touch (Example 2 would return `[100, 200]`).
- **Running maximum:** `ans[i]` is the max over *all* drops so far, not just the current
  square, so carry a `best` accumulator.
- **Compression is what makes the segment tree feasible:** with `left` up to `10^8` a direct
  tree is impossible; there are only `<= 2n` distinct edges to compress.
- The `O(n^2)` interval scan is acceptable here because `n <= 1000`, but the compressed
  segment tree is the technique the problem is designed to teach and scales to large `n`.
- Deduplicate edges with a `set` before sorting so identical edges from different squares map
  to the same index.
