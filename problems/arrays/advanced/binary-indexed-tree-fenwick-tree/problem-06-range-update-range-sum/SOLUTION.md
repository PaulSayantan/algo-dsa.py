# Range Update Range Sum — Solution

## Brute Force

Keep the raw array. `rangeUpdate(l, r, delta)` loops over `[l, r]` adding `delta`
(O(r - l + 1)); `rangeSum(l, r)` loops adding values (O(r - l + 1)). Both are O(n) worst
case.

- **Time:** O(n) per operation → up to O(q · n) ≈ 4·10¹⁰ for n = q = 2·10⁵ — far too slow.
- **Space:** O(n).

A single Fenwick Tree solves *point-update + range-query*, and a **difference-array** BIT
solves *range-update + point-query*, but neither alone gives *range-update + range-query*.

## Optimal Approach (Two Fenwick Trees: the B1 / B2 trick)

The idea is to represent range updates as a **difference array** and then derive a closed
form for the prefix sum that is *linear in the index* `i`. That linear form needs two
accumulators, hence two Fenwick Trees, `B1` and `B2`.

**Step 1 — range-add via a difference array.** To add `x` to `[l, r]`, do the classic
difference update: `+x` at `l` and `-x` at `r + 1`. If `D` is that difference array, then the
value at position `i` is `A[i] = sum_{k=1..i} D[k]`, and the prefix sum is:

```
prefixSum(i) = sum_{j=1..i} A[j]
             = sum_{j=1..i} sum_{k=1..j} D[k]
             = sum_{k=1..i} D[k] * (i - k + 1)
             = (i + 1) * sum_{k=1..i} D[k]  -  sum_{k=1..i} D[k] * k
```

**Step 2 — two trees.** Let

- `B1` accumulate `D[k]` (the difference values),
- `B2` accumulate `D[k] * (k - 1)`.

Then

```
prefixSum(i) = B1.prefix(i) * i  -  B2.prefix(i)
```

(Using `(k - 1)` in `B2` instead of `k` folds the `+1` into the `i` coefficient — you get the
same result whether you store `D[k]*k` and use `(i+1)*B1 - B2`, or store `D[k]*(k-1)` and use
`i*B1 - B2`. The implementation below uses the `(k-1)` / `i*B1 - B2` form.)

**Step 3 — apply an update to both trees.** A `rangeUpdate(l, r, x)` performs the difference
update `+x` at `l` and `-x` at `r + 1` on **both** trees, weighted appropriately:

```
B1.add(l, x);        B1.add(r + 1, -x)
B2.add(l, x*(l-1));  B2.add(r + 1, -x*r)      # note: -x*(r+1-1) = -x*r
```

**Step 4 — range sum.** `rangeSum(l, r) = prefixSum(r) - prefixSum(l - 1)`.

**Why it is correct.** The difference update makes `sum_{k<=i} D[k]` equal the true value
`A[i]` at every position, so the algebra in Step 1 is an exact identity, not an
approximation. `B1` and `B2` are ordinary Fenwick Trees, so each `prefix` and `add` is
O(log n); we simply evaluate the linear combination `B1.prefix(i)*i - B2.prefix(i)`. The two
weighted updates on `B2` encode the `D[k]*(k-1)` term consistently with the `+x` / `-x`
boundaries used on `B1`.

**Reference implementation** (verified against both examples: outputs `[6, 13, 2]` and
`[11, 1]`):

```python
class BIT:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 2)          # +2 keeps r+1 in range

    def add(self, i, v):
        while i <= self.n:
            self.t[i] += v
            i += i & (-i)

    def prefix(self, i):
        s = 0
        while i > 0:
            s += self.t[i]
            i -= i & (-i)
        return s


class RangeBIT:
    def __init__(self, n):
        self.n = n
        self.b1 = BIT(n)
        self.b2 = BIT(n)

    def _prefix(self, i):               # sum of A[1..i]
        return self.b1.prefix(i) * i - self.b2.prefix(i)

    def rangeUpdate(self, l, r, x):
        self.b1.add(l, x)
        self.b1.add(r + 1, -x)
        self.b2.add(l, x * (l - 1))
        self.b2.add(r + 1, -x * r)

    def rangeSum(self, l, r):
        return self._prefix(r) - self._prefix(l - 1)


def process(n, ops):
    bit = RangeBIT(n)
    out = []
    for op in ops:
        if op[0] == "rangeUpdate":
            _, l, r, x = op
            bit.rangeUpdate(l, r, x)
        else:
            _, l, r = op
            out.append(bit.rangeSum(l, r))
    return out
```

- **Time:** O(log n) per `rangeUpdate` and per `rangeSum` (a constant number of BIT walks
  each). Total O((n + q) log n).
- **Space:** O(n) for the two trees.

## Key Insights & Edge Cases

- **Why two trees?** The prefix sum of a range-added array is *linear* in the index `i`
  (`c1 * i + c0`). `B1` supplies the coefficient `c1` and `B2` supplies the constant `c0`;
  one tree cannot represent both without recomputation.
- **`r + 1` boundary.** The difference update touches index `r + 1`; size the trees to at
  least `n + 1` (here `n + 2`) so `add(r + 1, ...)` never overflows the array. If `r == n`,
  `add(n + 1, ...)` simply does nothing useful but must not crash.
- **Weight consistency.** `B2` uses `x*(l-1)` at `l` and `-x*r` at `r+1`. Mixing this with an
  `(i+1)*B1 - B2` prefix formula (which pairs with `x*l` / `-x*(r+1)` weights) gives wrong
  answers — pick one convention and keep it throughout.
- **Overflow.** With `delta` up to 10⁹ and `n` up to 2·10⁵, `B2` entries and prefix sums can
  reach ~10^14; use 64-bit integers (Python is safe automatically).
- **Point update / point query fall out for free:** `rangeUpdate(i, i, x)` is a point add and
  `rangeSum(i, i)` is a point read, so this structure subsumes the 1D LeetCode 307 problem.
