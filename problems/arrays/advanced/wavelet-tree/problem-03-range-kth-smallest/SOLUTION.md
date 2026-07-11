# Solution — Range K-th Smallest (MKTHNUM)

## Brute Force

For each query, copy `arr[l..r)`, sort it, and index position `k-1`. Sorting is
`O(m log m)` where `m = r - l`, so worst case `O(n log n)` per query and
`O(q n log n)` overall — far too slow for `n, q up to 10^5 / 5*10^4`.

A `nth_element`/quickselect brings a single query to `O(m)` average, still `O(nq)`
overall in the worst case.

## Optimal Approach (Wavelet Tree)

This is the query the Wavelet Tree was made for: a single root-to-leaf descent.

### Structure (same as Problems 1–2)

Coordinate-compress values to `[0, sigma)`. Node range `[lo, hi]`,
`mid = (lo+hi)//2`; element goes left iff value `<= mid`. `pref[k]` = number of
left-going elements among the node's first `k` elements. A window `[l, r)` maps
to the left child as `[pref[l], pref[r])` and to the right child as
`[l - pref[l], r - pref[r])`.

### kthSmallest(l, r, k)

Descend from the root, always narrowing the window and the value range:

```python
def kth_smallest(self, l, r, k):
    node = self.root
    while node.lo != node.hi:
        lc, rc = node.pref[l], node.pref[r]
        left_count = rc - lc            # window elements that went left
        if k <= left_count:
            # the k-th smallest is among the smaller half -> go left
            l, r = lc, rc
            node = node.left
        else:
            # skip all left_count smaller elements, go right
            k -= left_count
            l, r = l - lc, r - rc
            node = node.right
    return node.lo   # leaf value == the answer (map back to original scale)
```

**Why it works.** At any node, `left_count = pref[r] - pref[l]` is exactly how
many elements of the current window have value `<= mid` — i.e. how many are
"smaller" (they occupy the first `left_count` slots of the window's sorted
order). So:

- If `k <= left_count`, the `k`-th smallest is one of those lower-half elements;
  recurse into the left child, where the window becomes `[pref[l], pref[r])` and
  the rank `k` is unchanged.
- Otherwise the `k`-th smallest is in the upper half; the `left_count` smaller
  elements are skipped, so its rank within the right child is `k - left_count`,
  and the window maps to `[l - pref[l], r - pref[r])`.

Because the value range halves each level, after `O(log sigma)` steps we reach a
leaf whose single value is the answer. Map that compressed value back to the
original integer.

### Correctness

Invariant maintained at every level: **the value we seek is the element of rank
`k` among the elements currently in window `[l, r)` of this node.** Splitting the
window by the `<= mid` predicate is a stable partition that preserves order
statistics — the smallest `left_count` elements are precisely the left-going
ones — so choosing the correct child and adjusting `k` keeps the invariant. When
`lo == hi`, the window is nonempty and every element equals `lo`, which is
therefore the rank-`k` element.

**Complexity:** build `O(n log sigma)` time and space; each query `O(log sigma)`
time, `O(1)` extra space. With compression, `O(log n)` per query.

## Key Insights & Edge Cases

- **1-based `k`**: `k = 1` is the minimum, `k = r - l` is the maximum of the
  range. Guard callers so `1 <= k <= r - l`.
- **Right-exclusive window**: `arr[l..r)` has `r - l` elements; this keeps the
  prefix subtraction `pref[r] - pref[l]` exact.
- **Duplicates** are handled naturally — equal values funnel down the same path
  and stack at the same leaf; `left_count` counts them correctly.
- **Related queries with the same descent**: `k`-th *largest* is
  `kthSmallest(l, r, (r - l) - k + 1)`; the **range median** is
  `kthSmallest(l, r, ((r - l) // 2) + 1)`.
- **Coordinate compression is essential** to bound `sigma <= n`; remember to
  translate the returned leaf value back to the original domain.
- This descent is the primitive that powers Problem 6's majority candidate.
