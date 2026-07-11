# Solution — Rank & Select over a Sequence

## Brute Force

- **`rank(c, i)`**: scan `arr[0..i)` and count matches. `O(n)` per query.
- **`select(c, j)`**: scan left to right, counting occurrences of `c` until the
  `j`-th. `O(n)` per query.

With `q` queries this is `O(nq)` — up to `10^10` for the constraints, too slow.

A first improvement is a hash map from value → sorted list of its indices. Then
`rank(c, i)` is a binary search (`bisect_left` for `i`) and `select(c, j)` is a
direct list lookup — both `O(log n)`. This is actually optimal for *these two
primitives alone* and worth knowing. The Wavelet Tree matters because the **same
structure** also answers range order-statistic and range-count queries
(Problems 2–6) that the per-value index lists cannot.

## Optimal Approach (Wavelet Tree)

### Structure

Coordinate-compress values to `[0, sigma)`. The root holds all `n` positions and
represents value range `[lo, hi] = [0, sigma-1]`. For a node with range
`[lo, hi]` and `mid = (lo + hi) // 2`:

- Every element with value `<= mid` conceptually stores a `0` (goes **left**);
  every element with value `> mid` stores a `1` (goes **right**).
- Store `pref[k]` = number of `0`s (left-going elements) among the node's first
  `k` elements. This is a prefix sum of the "goes-left" bitmap, with
  `pref[0] = 0`.
- Recurse: the left child gets the subsequence of left-going elements (range
  `[lo, mid]`), the right child gets the right-going ones (range `[mid+1, hi]`).

Leaves have `lo == hi` (a single value). Building costs `O(n log sigma)`.

The key routing fact: if a node's current window is positions `[l, r)`, then
- `pref[l]` and `pref[r]` give the count of left-going elements before `l` and
  before `r`;
- the window maps to the **left** child as `[pref[l], pref[r])`;
- and to the **right** child as `[l - pref[l], r - pref[r])`.

### rank(c, i)

Walk from the root to the leaf for value `c`, maintaining the mapped prefix
bound. Start with `i` (and implicitly `l = 0`). At each internal node with
`mid`:
- if `c <= mid`, go left: `i <- pref[i]`;
- else go right: `i <- i - pref[i]`.

When you reach the leaf for `c`, the current `i` equals the number of `c`s in the
original prefix `arr[0..i)`. `O(log sigma)`.

```python
def rank(self, c, i):
    node = self.root
    while node.lo != node.hi:
        mid = (node.lo + node.hi) // 2
        if c <= mid:
            i = node.pref[i]
            node = node.left
        else:
            i = i - node.pref[i]
            node = node.right
    return i  # position within the leaf == count of c in prefix
```

An equally valid implementation reuses `rangeCountLeq`:
`rank(c, i) = rangeCountLeq(0, i, c) - rangeCountLeq(0, i, c - 1)` (see Problem 2).

### select(c, j)

`select` runs the routing **in reverse**. First descend to the leaf for `c`
(same branching as `rank`, but tracking the full window `[l, r)`), which tells
you how many `c`s exist. If `j` exceeds that count, return `-1`. Otherwise the
target is position `j - 1` within the leaf's element list; walk back **up** the
recorded path, inverting each mapping:
- coming up from a **left** child, the position that maps to left-index `k` is
  the index of the `(k+1)`-th left-going (`0`) element in the parent;
- coming up from a **right** child, invert against the right-going (`1`)
  elements.

Each inverse step is a "find the p-th 0/1" which is itself a `select` on the
node's bitmap; with `pref` it is a single binary search, so the whole operation
is `O(log sigma * log n)`, or `O(log sigma)` with an O(1)-select bitmap. For the
given constraints even a linear scan per level (`O(n log sigma)` overall for
`select`) passes, but binary search on `pref` is clean:

```python
# inverse of "left" mapping: smallest p with pref[p+1] == k+1 and element goes left
# inverse of "right" mapping: smallest p with (p+1 - pref[p+1]) == k+1
```

### Correctness

The routing is a bijection between a node's element list and the union of its
children's lists that **preserves left-to-right order** within each child
(stable partition). Therefore the count of left-going elements before position
`x` (`pref[x]`) is exactly the mapped position in the left child, and
`x - pref[x]` the mapped position in the right child. Iterating this invariant
from root to the leaf of `c` yields the number of `c`s before the bound —
i.e. `rank`. `select` inverts the same bijection.

**Complexity:** build `O(n log sigma)` time and space; `rank` `O(log sigma)`;
`select` `O(log sigma)` (with binary-searchable prefix sums).

## Key Insights & Edge Cases

- **Coordinate compression** keeps `sigma <= n`, so per-query cost is
  `O(log n)`. Map query value `c` through the same compression; if `c` is not a
  present value, `rank` still returns a well-defined count of `0` for it only if
  you keep it in the alphabet — simplest is to treat absent `c` via
  `rangeCountLeq` subtraction, which returns `0` naturally.
- **Prefix bounds are exclusive**: `rank(c, 0) == 0` and `rank(c, n)` is the
  total count of `c`.
- **`select` out of range** must return `-1` — always compare `j` against the
  leaf's element count before mapping back up.
- **1-based `j` vs 0-based index**: the `j`-th occurrence lives at leaf position
  `j - 1`.
- `rank`/`select` are inverses: `rank(c, select(c, j) + 1) == j` for valid `j` —
  a handy self-check when debugging.
