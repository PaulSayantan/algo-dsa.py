# Solution — Range Sum Query 2D - Mutable

## Brute Force

- Store the raw matrix.
- `update` is `O(1)`: assign the cell.
- `sumRegion` loops over the whole rectangle: `O(m · n)` worst case.

With up to 5000 mixed calls on a `200 × 200` grid, worst-case query work is
`5000 · 40000 = 2 × 10^8` — borderline and clearly wasteful.

An alternative brute force is a **static 2D prefix-sum** array: `sumRegion`
becomes `O(1)`, but every `update` forces an `O(m · n)` rebuild of the prefix
sums, which is just as bad when updates are frequent.

- **Time:** `O(mn)` per query (raw) or per update (prefix sums).
- **Space:** `O(mn)`.

## Optimal Approach — 2D Binary Indexed Tree

A **2D BIT** gives `O(log m · log n)` for *both* operations, striking the
balance the two brute forces cannot.

### The 1D idea, recalled

A 1D Fenwick tree stores partial sums indexed 1..n. Index `i` is responsible for
the range `(i - lowbit(i), i]`, where `lowbit(i) = i & (-i)`.
- To add to index `i`: `while i <= n: tree[i] += delta; i += lowbit(i)`.
- Prefix sum up to `i`: `while i > 0: s += tree[i]; i -= lowbit(i)`.

### Lifting to 2D

Make each Fenwick node hold *another* Fenwick tree along the second axis. Use
**1-indexed** internal coordinates (add 1 to the incoming 0-indexed row/col).

```
def _add(self, r, c, delta):        # point update
    i = r + 1
    while i <= self.rows:
        j = c + 1
        while j <= self.cols:
            self.tree[i][j] += delta
            j += j & (-j)
        i += i & (-i)

def _prefix(self, r, c):            # sum of [0..r] x [0..c] (0-indexed inclusive)
    total = 0
    i = r + 1
    while i > 0:
        j = c + 1
        while j > 0:
            total += self.tree[i][j]
            j -= j & (-j)
        i -= i & (-i)
    return total
```

### update

We must apply a **delta**, not overwrite, so keep a shadow copy `nums`:

```
def update(self, row, col, val):
    delta = val - self.nums[row][col]
    self.nums[row][col] = val
    self._add(row, col, delta)
```

### sumRegion — inclusion–exclusion

A rectangle sum is four prefix sums:

```
sum(r1..r2, c1..c2)
   = P(r2, c2) - P(r1-1, c2) - P(r2, c1-1) + P(r1-1, c1-1)
```

With 1-indexing internally, `r1-1 = -1` maps to prefix `0` (loop simply does not
execute), so no special-casing is needed.

### Why it is correct

The nested loops enumerate exactly the same set of canonical Fenwick ranges the
1D structure would, once per axis. Because each cell's contribution is added to
precisely the nodes that cover it (and subtracted symmetrically in queries), the
prefix sum equals the true rectangle sum. Deltas keep the tree consistent after
arbitrary overwrites.

### Building

Two options:
1. Start all-zero and call `_add` for every cell: `O(mn · log m · log n)` — fine
   for `200 × 200`.
2. An `O(mn)` linear build (propagate each node to its Fenwick parent along both
   axes). Overkill here but good to know for large grids.

- **Time:** build `O(mn log m log n)`; `update` and `sumRegion` each
  `O(log m · log n)`.
- **Space:** `O(mn)` for the tree plus `O(mn)` for the shadow copy.

## Key Insights & Edge Cases

- **Delta, not assignment.** A BIT can only add. Track current values to derive
  the delta on `update`; forgetting this double-counts.
- **1-indexing.** BIT indices must start at 1 (`lowbit(0) = 0` would loop
  forever). Convert on the way in and out.
- **Negative values / net-zero deltas** are fine — the structure never assumes
  positivity. A `val` equal to the existing value produces `delta = 0`, a no-op.
- **Rectangle degenerates to a row, column, or single cell** — inclusion–
  exclusion still holds; the `r1-1`/`c1-1 = -1` prefixes evaluate to 0.
- A **2D segment tree** also solves this, but for pure sums the BIT is smaller,
  faster in practice, and far less code — prefer it here.
