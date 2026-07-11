# Solution — Gorgeous Sequence (Range chmin / Max / Sum)

## Brute Force

Store the array. For `chmin [0, l, r, x]`, loop over `[l, r]` and set
`nums[i] = min(nums[i], x)`. For max/sum queries, loop over the range.

- **Time:** `O(q * n)` — a chmin can touch the whole array, and there can be `q`
  of them. With `n, q` up to `10^6` this is `10^12`, hopelessly slow.
- **Space:** `O(n)`.

A normal lazy segment tree does **not** rescue this. `chmin(x)` affects only the
elements greater than `x`, so there is no uniform lazy tag (like "add" or
"assign") you can push down a whole subtree. This is exactly the gap Segment Tree
Beats fills.

## Optimal Approach (Segment Tree Beats)

Each node stores four aggregates over its sub-range:

- `mx`   — the maximum value,
- `mxc`  — how many elements equal `mx`,
- `se`   — the **strict** second maximum (the largest value `< mx`; use `-1` or
  `-inf` if all elements are equal),
- `sum`  — the sum of the sub-range.

**Merge (pull up)** of two children `L` and `R`:

```
sum = L.sum + R.sum
mx  = max(L.mx, R.mx)
if L.mx == R.mx:
    mxc = L.mxc + R.mxc
    se  = max(L.se, R.se)
elif L.mx > R.mx:
    mxc = L.mxc
    se  = max(L.se, R.mx)      # R's max is a candidate second-max
else:
    mxc = R.mxc
    se  = max(R.se, L.mx)
```

**Applying `chmin(x)` to a whole node** (the "tag") is only valid when
`se < x < mx`. In that case exactly the `mxc` maximum elements drop from `mx` to
`x` and nothing else changes:

```
def apply_min(node, x):        # precondition: node.se < x < node.mx
    node.sum -= (node.mx - x) * node.mxc
    node.mx = x                # (second-max se and count mxc are unchanged)
```

Store `mx` itself as the pending "chmin tag": pushing down means calling
`apply_min(child, parent.mx)` on each child whose current `mx` exceeds it.

**The chmin update** on range `[l, r]` with value `x`:

```python
def update_min(k, lo, hi, l, r, x):
    if r < lo or hi < l or x >= mx[k]:      # disjoint OR no element exceeds x
        return                              # -> break condition, stop
    if l <= lo and hi <= r and x > se[k]:   # fully covered AND tag-applicable
        apply_min(k, x)                     # -> O(1) tag, stop
        return
    push_down(k)                            # "beaten": must recurse
    mid = (lo + hi) // 2
    update_min(2*k, lo, mid, l, r, x)
    update_min(2*k+1, mid+1, hi, l, r, x)
    pull_up(k)
```

`query_max` and `query_sum` are standard segment-tree range queries over `mx`
and `sum`.

Reference implementation core:

```python
class Beats:
    NEG = -1  # values are >= 0, so -1 is a safe "no second max" sentinel

    def __init__(self, a):
        self.n = len(a)
        self.mx  = [0] * (4 * self.n)
        self.mxc = [0] * (4 * self.n)
        self.se  = [self.NEG] * (4 * self.n)
        self.sm  = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, a)

    def _pull(self, k):
        l, r = 2 * k, 2 * k + 1
        self.sm[k] = self.sm[l] + self.sm[r]
        if self.mx[l] == self.mx[r]:
            self.mx[k] = self.mx[l]
            self.mxc[k] = self.mxc[l] + self.mxc[r]
            self.se[k] = max(self.se[l], self.se[r])
        elif self.mx[l] > self.mx[r]:
            self.mx[k] = self.mx[l]; self.mxc[k] = self.mxc[l]
            self.se[k] = max(self.se[l], self.mx[r])
        else:
            self.mx[k] = self.mx[r]; self.mxc[k] = self.mxc[r]
            self.se[k] = max(self.se[r], self.mx[l])

    def _apply(self, k, x):          # precondition: se[k] < x < mx[k]
        if x < self.mx[k]:
            self.sm[k] -= (self.mx[k] - x) * self.mxc[k]
            self.mx[k] = x

    def _push(self, k):
        self._apply(2 * k, self.mx[k])
        self._apply(2 * k + 1, self.mx[k])

    def _build(self, k, lo, hi, a):
        if lo == hi:
            self.mx[k] = self.sm[k] = a[lo]
            self.mxc[k] = 1
            self.se[k] = self.NEG
            return
        mid = (lo + hi) // 2
        self._build(2 * k, lo, mid, a)
        self._build(2 * k + 1, mid + 1, hi, a)
        self._pull(k)

    def chmin(self, k, lo, hi, l, r, x):
        if r < lo or hi < l or x >= self.mx[k]:
            return
        if l <= lo and hi <= r and x > self.se[k]:
            self._apply(k, x)
            return
        self._push(k)
        mid = (lo + hi) // 2
        self.chmin(2 * k, lo, mid, l, r, x)
        self.chmin(2 * k + 1, mid + 1, hi, l, r, x)
        self._pull(k)

    def qmax(self, k, lo, hi, l, r):
        if r < lo or hi < l:
            return self.NEG
        if l <= lo and hi <= r:
            return self.mx[k]
        self._push(k)
        mid = (lo + hi) // 2
        return max(self.qmax(2 * k, lo, mid, l, r),
                   self.qmax(2 * k + 1, mid + 1, hi, l, r))

    def qsum(self, k, lo, hi, l, r):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self.sm[k]
        self._push(k)
        mid = (lo + hi) // 2
        return (self.qsum(2 * k, lo, mid, l, r)
                + self.qsum(2 * k + 1, mid + 1, hi, l, r))
```

**Correctness of the three cases.**
- `x >= mx`: no element in the node exceeds `x`, so `min(·, x)` is the identity.
- `se < x < mx`: the only elements `> x` are exactly the `mxc` copies of `mx`
  (everything else is `<= se < x`). Each drops to `x`; the count and second-max
  are unchanged, so the `O(1)` update is exact.
- `x <= se`: at least two distinct values exceed `x`, so a single tag cannot
  describe the result — we must recurse.

**Why it is fast (potential argument).** Define the potential as the total number
of *distinct values* summed over all tree nodes' subtrees (equivalently, the sum
over nodes of the depth of an auxiliary "value tree"). A recursion happens only in
the `x <= se` case, and each such recursion strictly *decreases* the number of
distinct values in the affected subtrees. Each chmin can only *increase* the
potential by `O(log n)` (along the `O(log n)` nodes on the decomposition), while
every "beaten" recursion consumes potential. Summing over all `q` operations
gives a total of `O((n + q) log n)` work. (For the more general chmin+chmax+add
variant the bound becomes `O((n + q) log^2 n)`.)

- **Time:** `O((n + q) log n)` amortized.
- **Space:** `O(n)`.

## Key Insights & Edge Cases

- **`se` must be the STRICT second maximum** (largest value strictly below `mx`).
  If you accidentally let `se == mx`, the tag condition `x > se` becomes wrong and
  the tree either applies an invalid `O(1)` tag or never terminates.
- **Sentinel for a uniform node.** When every element equals `mx` (e.g. a leaf),
  `se` must be a value strictly less than any real element. Since values are
  `>= 0`, `-1` works; use a large negative sentinel if values can be negative.
- **Push down before recursing and before descending in queries.** The pending
  chmin lives in the parent's `mx`; children must be brought up to date first, or
  queries and further updates read stale aggregates.
- **The `_apply` guard `if x < mx[k]`** makes push-down idempotent and safe even
  when a child's max is already `<= x`.
- **64-bit sums.** With `n = 10^6` values up to `2^31 - 1`, sums reach `~2^51`;
  fine in Python, but use 64-bit integers in C++/Java.
- **This is the template.** Adding range-`chmax` and range-`add` (next problems)
  just means also tracking the *minimum*, *second minimum*, min-count, and an add
  lazy tag, and being careful about the interaction of tags.
