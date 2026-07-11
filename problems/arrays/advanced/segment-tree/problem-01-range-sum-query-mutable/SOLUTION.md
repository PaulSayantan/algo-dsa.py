# Range Sum Query - Mutable — Solution

## Brute Force

Keep the raw array.

- `update(i, v)`: assign `nums[i] = v` — `O(1)`.
- `sumRange(l, r)`: loop and add — `O(n)`.

With up to `3 * 10^4` interleaved queries over an array of size `3 * 10^4`, this is
`O(q * n) = ~9 * 10^8` in the worst case — too slow.

The "prefix sum" alternative flips the tradeoff: `sumRange` is `O(1)` but each
`update` forces rebuilding the suffix of the prefix array in `O(n)`. Still `O(q*n)`
when updates are frequent. We need **both** operations to be sublinear.

- Brute force time: `O(1)` update, `O(n)` query.
- Prefix sum time: `O(n)` update, `O(1)` query.
- Space: `O(n)`.

## Optimal Approach — Segment Tree

Build a segment tree where each node stores the **sum** of its range. The root
covers `[0, n-1]`; each node splits into two halves; leaves are single elements.

### Why it is correct

Sum is associative, so the value of any node equals the merge (here, addition) of
its two children. A range `[l, r]` can be decomposed into `O(log n)` disjoint node
ranges that exactly tile `[l, r]`; summing those node values gives the answer. An
update changes exactly one leaf and every ancestor's sum on the path to the root —
`O(log n)` nodes — so the invariant is restored everywhere.

### Step by step (iterative array layout, size `2n`)

1. **Build:** place the `n` leaves at positions `[n, 2n)`. For `i` from `n-1` down
   to `1`, set `tree[i] = tree[2i] + tree[2i+1]`. `O(n)`.
2. **Update `index -> val`:** move to leaf `pos = index + n`, set it, then walk up
   `pos //= 2`, refreshing `tree[pos] = tree[2*pos] + tree[2*pos+1]`. `O(log n)`.
3. **Query `[l, r]`:** set `l += n`, `r += n + 1` (half-open). While `l < r`: if `l`
   is a right child (`l & 1`) add `tree[l]` and `l += 1`; if `r` is a right child
   (`r & 1`) do `r -= 1` and add `tree[r]`; then `l //= 2`, `r //= 2`. `O(log n)`.

### Reference implementation

```python
from typing import List


class NumArray:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        # leaves
        for i, v in enumerate(nums):
            self.tree[self.n + i] = v
        # internal nodes
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        pos = index + self.n
        self.tree[pos] = val
        pos //= 2
        while pos >= 1:
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
            pos //= 2

    def sumRange(self, left: int, right: int) -> int:
        l, r = left + self.n, right + self.n + 1  # [l, r)
        total = 0
        while l < r:
            if l & 1:
                total += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                total += self.tree[r]
            l //= 2
            r //= 2
        return total
```

A recursive implementation over a `4n` array is equally valid and often easier to
adapt to other aggregates or lazy propagation.

### Complexity

- Build: `O(n)` time, `O(n)` space.
- `update`: `O(log n)`.
- `sumRange`: `O(log n)`.

## Key Insights & Edge Cases

- **Half-open trick.** The iterative query uses `[l, r)`. The `+ n + 1` on `right`
  converts the inclusive right bound to exclusive — a common off-by-one source.
- **Single-element range** (`left == right`) must return exactly that element; the
  half-open loop handles it because the range still has width 1.
- **Negative values / net-zero sums** are fine — the merge is plain addition; there
  is no assumption of positivity (unlike some Fenwick-tree tricks).
- **Update to the same value** still costs `O(log n)`; that is expected and fine.
- **`n == 1`** works: the single leaf is at index 1 (`n`), the root and leaf
  coincide in the iterative layout, and queries/updates degenerate correctly.
- This is the base template. Swap the merge from `+` to `min`/`max`/`gcd` and you
  solve a whole family of range-aggregate problems (see problem 2).
