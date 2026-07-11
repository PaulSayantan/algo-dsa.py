# Solution — Count Values ≤ K in a Range

## Brute Force

For each query, scan `arr[l..r)` and count elements `<= x`. `O(n)` per query,
`O(nq)` overall — up to `10^10`, too slow.

A common intermediate approach is a **merge-sort tree**: a segment tree over
positions where each node stores its sorted subarray. A query decomposes `[l, r)`
into `O(log n)` nodes and binary-searches each, giving `O(log^2 n)` per query and
`O(n log n)` space. That passes here but is a log factor slower than the Wavelet
Tree and is what the Wavelet Tree improves upon.

## Optimal Approach (Wavelet Tree)

### Structure (same as Problem 1)

Coordinate-compress values to `[0, sigma)`. Each node covers a value range
`[lo, hi]`; with `mid = (lo + hi) // 2`, an element goes **left** iff its value
`<= mid`. Store `pref[k]` = number of left-going elements among the node's first
`k` elements (`pref[0] = 0`). A window `[l, r)` maps to the left child as
`[pref[l], pref[r])` and to the right child as `[l - pref[l], r - pref[r])`.

### rangeCountLeq(l, r, x)

Route the window `[l, r)` down the tree, accumulating an answer:

- At a node with range `[lo, hi]`, `mid = (lo+hi)//2`:
  - Compute `lc = pref[l]`, `rc = pref[r]`; the number of left-going elements in
    the window is `leftCount = rc - lc`.
  - **If `x <= mid`**, all qualifying elements (`<= x <= mid`) live in the left
    child. Recurse into the left child with window `[lc, rc)`.
  - **Else (`x > mid`)**, every left-child element is `<= mid <= x`, so it
    qualifies: add `leftCount` to the answer, then recurse into the right child
    with window `[l - lc, r - rc)` to count the remaining qualifiers `> mid`.
- **Base pruning**: if `x < lo` for the current node, answer contribution is `0`
  (stop); if `x >= hi`, every element in the window qualifies, add `r - l`
  (stop). At a leaf (`lo == hi`), add `r - l` iff `lo <= x`.

Only one root-to-leaf path is traversed with O(1) work per level, so each query
is `O(log sigma)`.

```python
def range_count_leq(self, l, r, x):
    if x < self.root.lo:
        return 0
    if x >= self.root.hi:
        return r - l
    return self._go(self.root, l, r, x)

def _go(self, node, l, r, x):
    if l >= r:
        return 0
    if node.lo == node.hi:
        return (r - l) if node.lo <= x else 0
    mid = (node.lo + node.hi) // 2
    lc, rc = node.pref[l], node.pref[r]
    if x <= mid:
        return self._go(node.left, lc, rc, x)
    return (rc - lc) + self._go(node.right, l - lc, r - rc, x)
```

### Derived queries

- `count(< x)  = range_count_leq(l, r, x - 1)`
- `count(== x) = range_count_leq(l, r, x) - range_count_leq(l, r, x - 1)`
- `count(a <= v <= b) = range_count_leq(l, r, b) - range_count_leq(l, r, a - 1)`

`range_count_between` in `solution.py` is exactly the last identity.

### Correctness

By induction on depth: the mapping is order-preserving, so the elements of the
window that fall in the left child are precisely those with value `<= mid`
occupying window `[pref[l], pref[r])` in the child, and the rest map to
`[l - pref[l], r - pref[r])` in the right child. When `x > mid`, all left-child
elements are `<= x` (add them all) and remaining qualifiers are exactly those
`> mid`, handled by the right recursion. When `x <= mid`, no right-child element
can be `<= x`, so recursing left suffices.

**Complexity:** build `O(n log sigma)`; each query `O(log sigma)`; space
`O(n log sigma)`.

## Key Insights & Edge Cases

- **Half-open ranges** (`[l, r)`) make the prefix arithmetic clean: the answer
  for `[l, r)` is `count(0, r) - count(0, l)` if you prefer a prefix formulation.
- **`x` outside the alphabet**: `x < min` → `0`; `x >= max` → `r - l`. Handle
  these before recursing (the pruning above does).
- **Empty window** (`l == r`) → `0`.
- **No compression pitfalls**: when mapping `x`, use a `<=`-aware lookup (e.g.
  `bisect_right` on the sorted distinct values minus 1) so that thresholds that
  fall *between* two present values still count correctly. Compressing only the
  array values and comparing on the original scale inside the tree (as in the
  snippet, which compares raw `mid`/`x`) sidesteps this entirely.
- This primitive is the workhorse for Problems 4, 5, and 6.
