# Solution — Range Square-Root and Range Sum

## Brute Force

For each square-root update `[1, l, r]`, loop over every index `i` in `[l, r]`
and set `nums[i] = isqrt(nums[i])`. For each sum query `[2, l, r]`, loop over the
range and add up the values (or keep a prefix-sum array, rebuilt after each
update).

- **Time:** `O(q * n)` — each update can touch the whole array. With
  `n, q = 2 * 10^5` this is `4 * 10^10` operations, far too slow.
- **Space:** `O(n)`.

The brute force is wasteful because it keeps re-applying `sqrt` to values that
have already reached `0` or `1`, where `floor(sqrt(x)) == x`. Those elements
never change again.

## Optimal Approach (Segment Tree Beats break condition)

Build a segment tree over `nums` where each node stores:

- `sum` — the sum of its sub-range,
- `mx`  — the maximum value in its sub-range.

**Sum query** is the standard segment-tree range sum: split `[l, r]` across the
children and add the stored `sum` of fully-covered nodes. `O(log n)` per query.

**Square-root update** on `[l, r]` is the Beats-style part:

1. If the node's range is disjoint from `[l, r]`, return.
2. **Break condition:** if the node is fully inside `[l, r]` **and** `mx <= 1`,
   every value in the node is `0` or `1`, so `floor(sqrt(x)) == x`. The node is
   already at its fixed point — return without recursing. This is the pruning
   that makes the algorithm fast.
3. Otherwise recurse into both children, then pull up (`sum` and `mx` from the
   children). We keep descending until we reach individual leaves (or a node
   that hit the break condition), applying `isqrt` at the leaves.

Reference sketch:

```python
import math

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

    def sqrt_update(self, k, lo, hi, l, r):
        if r < lo or hi < l or self.mx[k] <= 1:   # disjoint OR already stable
            return
        if lo == hi:                               # leaf: apply the sqrt
            v = math.isqrt(self.sum[k])
            self.sum[k] = self.mx[k] = v
            return
        mid = (lo + hi) // 2
        self.sqrt_update(2 * k, lo, mid, l, r)
        self.sqrt_update(2 * k + 1, mid + 1, hi, l, r)
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

Then translate each 1-indexed query `[l, r]` to 0-indexed `[l-1, r-1]`, call
`sqrt_update` for type 1, and record `query` for type 2.

**Why it is fast (amortized analysis).** A value `x <= 10^18` reaches `1` after
about `6` square-root applications (`10^18 -> 10^9 -> ~31623 -> 177 -> 13 -> 3 ->
1`). Once a whole node's maximum is `<= 1`, the break condition prunes it forever.
Define a potential equal to the total number of remaining "useful" sqrt steps
across all elements; it starts at `O(n log log(maxV))` and each unit of recursion
work discharges it. So over the whole run the tree descends to leaves only
`O(n log log(maxV))` times, each descent costing `O(log n)`.

- **Time:** `O((n + q) log n * log log(maxV))`, effectively near-linear — the
  `log log(maxV)` factor is at most ~6 here.
- **Space:** `O(n)` for the tree arrays.

## Key Insights & Edge Cases

- **The fixed point is `{0, 1}`, not just `1`.** `floor(sqrt(0)) = 0` and
  `floor(sqrt(1)) = 1`, so the correct break condition is `mx <= 1`. Using
  `mx == 1` or `mx == 0` alone would either loop forever on `0`s or fail to
  prune ranges that mix `0`s and `1`s.
- **Use exact integer square root.** `math.isqrt` avoids floating-point error;
  `int(math.sqrt(x))` can be off by one for large `x` near a perfect square.
- **1-indexed vs 0-indexed.** The queries are 1-indexed; convert before calling
  into a 0-indexed tree.
- **Big sums.** Sums of up to `2 * 10^5` values of size `10^18` reach `~10^23`,
  which overflows 64-bit integers in other languages — Python handles it, but
  note it for portability.
- **This is the gateway to Beats.** The general Segment Tree Beats extends this
  exact "recurse until a break condition, then a tag condition" pattern to
  `chmin`/`chmax` operations (see the later problems), where a node stores the
  largest value, the second-largest value, and the count of the largest.
