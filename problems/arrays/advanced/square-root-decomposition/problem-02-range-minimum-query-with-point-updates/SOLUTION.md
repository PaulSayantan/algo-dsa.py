# Range Minimum Query with Point Updates — Solution

## Brute Force

Keep the array. `update` overwrites one cell in `O(1)`; `query` scans the range
and tracks the smallest value in `O(n)`.

```python
def query(self, left, right):
    return min(self.nums[left:right + 1])
```

With up to `10^5` queries over `10^5` elements this is `O(q * n) = 10^{10}`
operations worst case — far too slow.

Note that unlike sums, **minimum is not invertible**: you cannot get the min of
`[left, right]` by "subtracting" prefixes, so a prefix-style trick that supports
updates does not exist for min. Sparse tables give `O(1)` queries but assume the
array is immutable, so they break under updates. We need a structure tolerant of
both.

## Optimal Approach (Square Root Decomposition)

Cut the array into blocks of size `b ≈ sqrt(n)`; element `i` lives in block
`i // b`. Maintain `block_min[k]` = the minimum of block `k`.

**Build** — one linear pass sets each `block_min[k]` to the minimum of its
members: `O(n)`.

**update(index, val)** — assign `nums[index] = val`, then refresh the one block
that owns `index`. The cheap and robust way is to recompute that block's minimum
from its (at most `b`) elements:

```python
def update(self, index, val):
    self.nums[index] = val
    k = index // self.b
    start = k * self.b
    end = min(start + self.b, self.n)
    self.block_min[k] = min(self.nums[start:end])
```

This is `O(b) = O(sqrt(n))`. (An `O(1)` update is possible only when `val` is
not larger than the old minimum; a decrease that removes the current minimum
forces a rescan, so `O(sqrt(n))` per update is the clean worst-case bound.)

**query(left, right)** — combine three parts, seeding the answer with `+inf`:

1. **Partial left block:** compare elements from `left` to the end of its block
   (or `right`).
2. **Whole interior blocks:** fold in each `block_min[k]` directly.
3. **Partial right block:** compare its in-range elements.

```python
def query(self, left, right):
    b = self.b
    lb, rb = left // b, right // b
    best = float("inf")
    if lb == rb:
        return min(self.nums[left:right + 1])
    for i in range(left, (lb + 1) * b):        # partial left block
        best = min(best, self.nums[i])
    for k in range(lb + 1, rb):                # whole interior blocks
        best = min(best, self.block_min[k])
    for i in range(rb * b, right + 1):         # partial right block
        best = min(best, self.nums[i])
    return best
```

**Why it is correct.** The true minimum lies in some index of `[left, right]`.
That index is either in a boundary block (covered element-by-element by the two
partial loops) or in a fully-contained block (whose `block_min` is `<=` that
index's value and is folded into `best`). Because `min` is **associative and
idempotent**, combining partial elements with whole-block minima yields the
minimum over the entire range. `block_min` stays consistent because every
`update` recomputes the touched block.

**Complexity.** Each query touches `< b` elements on each side and `< n / b`
block minima. With `b ≈ sqrt(n)` that is `O(sqrt(n))` per query and per update.
Overall `O(n + q * sqrt(n))` time, `O(n)` space.

## Key Insights & Edge Cases

- **Min is associative + idempotent**, so block precomputation is valid — the
  same template works for max, gcd, or any associative monoid.
- **Min is not invertible**, which is exactly why a difference-based prefix
  approach fails here and sqrt decomposition (or a segment tree) is needed.
- **Update recomputes the whole block** rather than trying to patch the stored
  minimum; patching is wrong when you overwrite the current minimum with a
  larger value.
- **Single-block ranges** (`lb == rb`) must be special-cased so the two partial
  loops do not overlap.
- **Seed with `+inf`** (or the first element) so an all-negative range still
  returns the correct value.
- A segment tree does this in `O(log n)` per op; sqrt decomposition trades a bit
  of asymptotic speed for a much simpler, easy-to-reason-about implementation.
