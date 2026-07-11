# Solution — Range GCD Query

## Brute Force

Fold `gcd` across `l..r` per query.

```python
from math import gcd
def query(nums, l, r):
    g = nums[l]
    for i in range(l + 1, r + 1):
        g = gcd(g, nums[i])
    return g
```

- **Time:** O((r - l) · log A) per query (each `gcd` is O(log A) for values up to `A`),
  O(q · n · log A) total.
- **Space:** O(1) extra.

## Optimal Approach (Sqrt Tree)

Same Sqrt Tree as before with `op = gcd`. Per layer we keep prefix gcds, suffix gcds, and
the gcd over every pair of whole blocks. A query is
`gcd(suf[l], between[inner blocks], pref[r])`, an O(1) combine of at most three values (plus
the two special cases `l == r` and `l + 1 == r`).

### Why it is correct

gcd is **associative and commutative**:
`gcd(a, b, c, d) = gcd(gcd(a, b), gcd(c, d))`. So the gcd of the range equals the gcd of
(gcd of the suffix of `l`'s block) with (gcd of the whole between-blocks) with (gcd of the
prefix of `r`'s block). Each partial gcd is precomputed. As with min, the pieces are disjoint
and cover `[l, r]` exactly, so no double counting occurs — and even if they did overlap, gcd
is idempotent so it would not matter. The value of the Sqrt Tree here is illustrating
**non-invertibility**: there is no operation that recovers `gcd(l..r)` from `gcd(0..r)` and
`gcd(0..l-1)`, so the prefix-array approach that works for sums is impossible.

### Reference implementation (answer key)

Reuse the generic Sqrt Tree from Problem 1 with `op = math.gcd`:

```python
from math import gcd
class RangeGCD(SqrtTree):     # SqrtTree = generic class from problem 1
    def __init__(self, nums):
        super().__init__(nums, op=gcd)
```

- **Build:** O(n log log n · log A) time (the `log A` from each gcd call),
  O(n log log n) space.
- **Query:** O(1) combines, i.e. O(log A) counting the gcd cost; O(1) if treating gcd as a
  unit-cost op.

## Key Insights & Edge Cases

- **gcd of a single element** is the element itself — handled by the `l == r` base case.
- **All-equal ranges** return that value; **coprime ranges** return `1`.
- Values up to 1e9 fit comfortably in 32-bit, but intermediate gcds only shrink, so no
  overflow risk.
- **Why not prefix arrays?** gcd has no inverse: from `gcd(0..r)` and `gcd(0..l-1)` you
  cannot reconstruct `gcd(l..r)` (e.g. arrays `[6, 10]` and `[6, 15]` can share prefix
  patterns yet differ on suffixes). This is the same wall you hit for product-mod (Problem 4)
  and composition (Problem 5) — but those are also non-idempotent, so even a sparse table
  fails there and Sqrt Tree becomes the *only* simple O(1) option.
- A **Sparse Table** also solves range-gcd in O(1) query; choose it if you prefer simpler
  code and don't need the non-idempotent generality.
