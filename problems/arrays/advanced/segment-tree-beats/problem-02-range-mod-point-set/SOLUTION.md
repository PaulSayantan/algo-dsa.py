# Solution — Range Modulo, Point Assignment, Range Sum

## Brute Force

Keep the array as-is. For a range-modulo `[2, l, r, x]`, loop over `[l, r]` and
set `nums[i] %= x`. For a point assignment `[3, k, x]`, set `nums[k] = x`. For a
sum query `[1, l, r]`, loop and add (or maintain a Fenwick/segment tree for the
sum only, but still loop for the modulo).

- **Time:** `O(q * n)` worst case — a modulo over the whole array is `O(n)`, and
  there can be `q` of them. With `n, q = 10^5` this is `10^10`, too slow.
- **Space:** `O(n)`.

The waste: a modulo re-touches elements that are already smaller than `x`, where
`nums[i] % x == nums[i]` is a no-op.

## Optimal Approach (Segment Tree Beats break condition)

Build a segment tree where each node stores:

- `sum` — sum of the sub-range,
- `mx`  — maximum of the sub-range.

**Sum query** and **point assignment** are the standard segment-tree operations
(`O(log n)` each): point assignment updates a single leaf and pulls up.

**Range modulo** on `[l, r]` with modulus `x` uses the Beats break condition:

1. If the node's range is disjoint from `[l, r]`, return.
2. **Break condition:** if the node is (relevantly) covered and `mx < x`, then
   every element in the node is `< x`, so `% x` changes nothing — return without
   recursing. This is the pruning that makes it fast.
3. Otherwise recurse into both children; at a leaf actually apply
   `nums[leaf] %= x`. Pull up `sum` and `mx` afterward.

Reference sketch:

```python
class Beats:
    def __init__(self, a):
        self.n = len(a)
        self.sum = [0] * (4 * self.n)
        self.mx = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, a)

    def _pull(self, k):
        self.sum[k] = self.sum[2 * k] + self.sum[2 * k + 1]
        self.mx[k] = max(self.mx[2 * k], self.mx[2 * k + 1])

    def _build(self, k, lo, hi, a):
        if lo == hi:
            self.sum[k] = self.mx[k] = a[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * k, lo, mid, a)
        self._build(2 * k + 1, mid + 1, hi, a)
        self._pull(k)

    def mod_update(self, k, lo, hi, l, r, x):
        if r < lo or hi < l or self.mx[k] < x:   # disjoint OR nothing can change
            return
        if lo == hi:                              # leaf: apply the modulo
            self.sum[k] %= x
            self.mx[k] = self.sum[k]
            return
        mid = (lo + hi) // 2
        self.mod_update(2 * k, lo, mid, l, r, x)
        self.mod_update(2 * k + 1, mid + 1, hi, l, r, x)
        self._pull(k)

    def assign(self, k, lo, hi, pos, val):
        if lo == hi:
            self.sum[k] = self.mx[k] = val
            return
        mid = (lo + hi) // 2
        if pos <= mid:
            self.assign(2 * k, lo, mid, pos, val)
        else:
            self.assign(2 * k + 1, mid + 1, hi, pos, val)
        self._pull(k)

    def query(self, k, lo, hi, l, r):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self.sum[k]
        mid = (lo + hi) // 2
        return (self.query(2 * k, lo, mid, l, r)
                + self.query(2 * k + 1, mid + 1, hi, l, r))
```

Convert 1-indexed inputs to 0-indexed before calling into the tree.

**Why it is fast (amortized analysis).** When a modulo actually changes an
element (`nums[i] >= x`), the result `nums[i] % x` is strictly less than `x`, and
since `x <= nums[i]` we get `nums[i] % x < nums[i] / 2` — the value **more than
halves**. So each element can be reduced by a "real" modulo at most
`O(log(maxV))` times. Point assignments can raise a value again, but each
assignment adds at most `O(log(maxV))` future reductions. Charge each unit of
recursion work to one of these reductions (there are `O((n + q) log(maxV))` of
them); every descent to a leaf costs `O(log n)`.

- **Time:** `O((n + q) log n * log(maxV))`, effectively near-linear for the given
  bounds.
- **Space:** `O(n)`.

## Key Insights & Edge Cases

- **Break condition uses strict `<`.** If `mx < x`, no element can change. If
  `mx == x`, at least one element equals `x` and `x % x = 0` is a real change, so
  you must recurse. Using `mx <= x` as the prune would be a correctness bug.
- **`x == 1`.** Everything becomes `0`; the tree correctly reduces every element
  to `0` and then future modulos prune (since `mx = 0 < 1`).
- **Point assignment resets the potential.** After `[3, k, x]`, the element can
  be large again — that is fine; it just contributes another `O(log(maxV))`
  future reductions, which the amortized bound already accounts for.
- **1-indexed conversion** must be applied consistently to both range and point
  operations.
- **Relation to full Beats.** Here the break condition (`mx < x`) is enough
  because reductions halve values. Full Segment Tree Beats generalizes this to
  `chmin`/`chmax` by additionally tracking the *second* maximum so it knows
  exactly when a tag can be applied to a whole node instead of recursing.
