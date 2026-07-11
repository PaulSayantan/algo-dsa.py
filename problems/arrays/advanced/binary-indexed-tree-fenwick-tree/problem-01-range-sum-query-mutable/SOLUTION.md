# Range Sum Query - Mutable — Solution

## Brute Force

Keep the raw array. `update` writes `nums[index] = val` in O(1). `sumRange(l, r)` loops
from `l` to `r` and adds, which is O(n) per query.

- **Time:** O(1) per update, O(n) per query. With up to 3·10⁴ interleaved queries on an
  array of 3·10⁴ elements this is ~9·10⁸ operations worst case — too slow.
- **Space:** O(n).

A symmetric alternative — a precomputed prefix-sum array — gives O(1) queries but O(n)
updates because every element after `index` shifts. Either way one operation is linear.

## Optimal Approach (Binary Indexed Tree / Fenwick Tree)

A Fenwick Tree makes **both** operations O(log n).

Represent the array 1-indexed inside a tree array `tree[1..n]`. Index `i` stores the sum of
the `lowbit(i) = i & (-i)` elements ending at position `i`.

**Point add.** To add `delta` at position `i`, update `tree[i]`, then jump to the next
index responsible for `i` by adding `i & (-i)`, repeating until you pass `n`:

```
def add(i, delta):        # i is 1-based
    while i <= n:
        tree[i] += delta
        i += i & (-i)
```

**Prefix sum.** To sum `nums[1..i]`, accumulate `tree[i]` then strip the lowest set bit by
subtracting `i & (-i)`, repeating until `i` hits 0:

```
def prefix(i):            # sum of first i elements, i is 1-based
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & (-i)
    return s
```

**Range sum.** `sumRange(l, r) = prefix(r + 1) - prefix(l)` (shift 0-based indices by +1 to
become 1-based).

**Update to an absolute value.** The BIT stores deltas, so setting `nums[index] = val`
means adding `val - current[index]` and remembering the new value:

```
def update(index, val):
    add(index + 1, val - vals[index])
    vals[index] = val
```

**Why it is correct.** Each `add` walk touches exactly the tree cells whose responsibility
range covers position `i`, and each `prefix` walk decomposes `[1..i]` into disjoint blocks
(one per set bit of `i`). Because addition is associative and invertible, the difference
`prefix(r+1) - prefix(l)` is exactly the sum of the half-open range `[l, r]` in 0-based
terms. Both walks follow the binary representation of the index, so they take at most
⌊log₂ n⌋ + 1 steps.

**Reference implementation:**

```python
class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.vals = [0] * self.n
        self.tree = [0] * (self.n + 1)
        for i, v in enumerate(nums):
            self.update(i, v)

    def _add(self, i, delta):     # i is 1-based
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def _prefix(self, i):         # sum of nums[0..i-1]
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def update(self, index, val):
        self._add(index + 1, val - self.vals[index])
        self.vals[index] = val

    def sumRange(self, left, right):
        return self._prefix(right + 1) - self._prefix(left)
```

- **Time:** O(n log n) to build via `n` updates (or O(n) with a linear build), O(log n) per
  `update` and per `sumRange`.
- **Space:** O(n) for `tree` plus O(n) for the cached values.

## Key Insights & Edge Cases

- **1-based indexing is mandatory.** `i & (-i)` is 0 when `i == 0`, which would loop
  forever in `add`. Always shift 0-based external indices by +1.
- **Store the current values** so `update` can compute the delta `val - vals[index]`; the
  tree itself only knows sums, not individual elements.
- **`sumRange(l, r) = prefix(r+1) - prefix(l)`** — mixing 0-based and 1-based off-by-one is
  the most common bug here.
- **Negative values are fine.** Sum is an invertible group operation; nothing about the BIT
  assumes non-negative entries.
- **Linear build:** add each `nums[i]` to `tree[i]`, then push `tree[i]` into its parent
  `tree[i + (i & -i)]`. This builds in O(n) instead of O(n log n) — handy for large arrays.
