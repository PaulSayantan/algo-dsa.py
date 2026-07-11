# Solution — Submatrix Maximum with Point Updates

## Brute Force

- `update`: `O(1)`, assign the cell.
- `query`: scan the whole submatrix, `O(n · m)` worst case.

With `q = 10^5` queries on a `1000 × 1000` grid, a single full-grid query is
`10^6`, so the worst case approaches `10^11`. Too slow.

- **Time:** `O(q · n · m)`.
- **Space:** `O(n · m)`.

## Optimal Approach — 2D Segment Tree

A BIT is out: **`max` is not invertible**, so we cannot recover the max of an
inner rectangle from the max of an enclosing one. A segment tree stores an
explicit aggregate for every canonical range, so it does not need invertibility.

### Structure: a tree of trees

- **Outer segment tree** is built over the **rows** `[0, n)`. Each outer node
  covers a contiguous band of rows.
- Each outer node owns an **inner segment tree** over the **columns** `[0, m)`.
  The inner tree at an outer node stores, for every column-range, the **max over
  that column-range across all rows in the outer node's row-band**.
- Store as `tree[4n][4m]` (four-times sizing for both segment trees).

### Build — `O(n · m)`

- Outer **leaf** (a single row `x`): its inner tree is just a 1D segment tree of
  that row's values.
- Outer **internal** node: its inner tree is the **element-wise max** of its two
  children's inner trees (merge two 1D max-trees node by node). This "pull"
  keeps every internal band consistent with its rows.

Building bottom-up costs `O(nm)` because each of the `O(n)` outer nodes does
`O(m)` inner work.

### update(r, c, v) — `O(log n · log m)`

Recurse the outer tree toward the leaf row `r`. This touches `O(log n)` outer
nodes on the path (leaf plus its ancestors). At each such node, the row `r` lies
inside its band, so column `c`'s max may change:

- At the **outer leaf** for row `r`: point-update column `c` to `v` in its inner
  tree.
- At each **outer ancestor**: recompute column `c` as
  `max(left child's inner value at c, right child's inner value at c)` and
  point-update it in this node's inner tree.

Each inner update is `O(log m)`, giving `O(log n · log m)` overall.

### query(r1, c1, r2, c2) — `O(log n · log m)`

Descend the outer tree to collect the `O(log n)` **canonical row-bands** that
exactly tile `[r1, r2]` (standard segment-tree range decomposition — never
recurse into bands fully inside or fully outside). For each such outer node, run
an inner column-range query over `[c1, c2]` (`O(log m)`), and combine all the
partial maxima with `max`.

Because the outer bands are disjoint and cover `[r1, r2]` exactly, and each
inner query returns the true max of its band over the columns, the overall
maximum is correct.

### Reference sketch (recursive, max-aggregate)

```
def _inner_update(node_row, col, lo, hi, node_col, val):
    if lo == hi:
        tree[node_row][node_col] = val; return
    mid = (lo + hi) // 2
    if col <= mid: _inner_update(node_row, col, lo, mid, 2*node_col, val)
    else:          _inner_update(node_row, col, mid+1, hi, 2*node_col+1, val)
    tree[node_row][node_col] = max(tree[node_row][2*node_col],
                                   tree[node_row][2*node_col+1])

def _outer_update(node, rlo, rhi, r, c, val):
    if rlo != rhi:
        mid = (rlo + rhi) // 2
        if r <= mid: _outer_update(2*node, rlo, mid, r, c, val)
        else:        _outer_update(2*node+1, mid+1, rhi, r, c, val)
    if rlo == rhi:
        _inner_update(node, c, 0, m-1, 1, val)          # leaf: raw value
    else:
        merged = max(inner_point(2*node, c), inner_point(2*node+1, c))
        _inner_update(node, c, 0, m-1, 1, merged)       # internal: pull-up
```

- **Time:** build `O(nm)`; `update` and `query` each `O(log n · log m)`.
- **Space:** `O(nm)` (constant factor ≈ 4× from the segment-tree sizing on each
  axis; for `1000 × 1000` prefer an iterative or array-sized-to-power-of-two
  build, or use `O(nm)` iterative segment trees to keep memory in check).

## Key Insights & Edge Cases

- **Why not a BIT:** BIT range queries rely on prefix subtraction, which needs an
  invertible group operation (sum, XOR). `max`/`min` have no inverse, so a BIT
  only supports *prefix-max with monotone updates* — not this problem's arbitrary
  point updates. The segment tree is required.
- **Initialize the identity to `-inf`**, not `0`. Example 2 has all-negative
  values; a `0` identity would wrongly report `0` as the max.
- **Internal nodes are element-wise merges,** not stored ranges — update must
  pull up column `c` at every ancestor, or stale maxima leak into queries.
- **Single-cell query** (`r1=r2, c1=c2`, as in Example 2's last query) reduces to
  reading one leaf — the range decomposition returns exactly one band of one
  column.
- **Memory for `1000 × 1000`:** a naive `4n × 4m` = `16 × 10^6` cell tree is
  large but feasible; an iterative segment tree sized to the next power of two on
  each axis roughly halves the constant and is the usual competitive choice.
- The same skeleton with `+` instead of `max` gives submatrix-sum with point
  updates — but for sums the 2D BIT (Problem 1) is smaller and faster, so reserve
  the 2D segment tree for non-invertible aggregates.
