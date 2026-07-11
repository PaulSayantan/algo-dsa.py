# Solution — Static Range Minimum Query

## Brute Force

For each query `(l, r)`, scan `nums[l..r]` and track the minimum.

- **Time:** O(q · n) — a single query can touch the whole array.
- **Space:** O(1) extra.

With `n = 10^5` and `q = 2 * 10^5` this is up to `2 * 10^10` operations — far too slow.

A prefix-based trick does **not** work for min the way prefix sums work for sum,
because min has no inverse (you cannot "subtract" the prefix before `l`). That is
exactly the gap a Sparse Table fills.

## Optimal Approach (Sparse Table)

### Structure

Precompute `sparse[j][i] = min(nums[i .. i + 2^j - 1])`, the minimum of the block of
length `2^j` that starts at index `i`.

- **Base level** (`j = 0`): blocks of length 1, so `sparse[0][i] = nums[i]`.
- **Transition:** a block of length `2^j` is two adjacent blocks of length `2^(j-1)`:

```
sparse[j][i] = min( sparse[j-1][i], sparse[j-1][i + 2^(j-1)] )
```

Build levels in increasing `j`; each of the O(n log n) entries costs O(1).

### Answering a query in O(1)

Let `length = r - l + 1` and `k = floor(log2(length))`, the largest exponent with
`2^k <= length`. Two blocks of length `2^k` cover `[l, r]`:

- one starting at `l`, covering `[l, l + 2^k - 1]`
- one ending at `r`, starting at `r - 2^k + 1`

These two blocks **together cover every index** in `[l, r]`, and they may **overlap**
in the middle. That overlap is harmless because `min` is **idempotent**:
`min(x, x) = x`. So

```
answer = min( sparse[k][l], sparse[k][r - 2^k + 1] )
```

### Why it is correct

Every index in `[l, r]` lies in at least one of the two chosen blocks (the left block
reaches at least the midpoint, the right block reaches back to at least the midpoint
because `2 * 2^k >= length`). Since both blocks are entirely inside `[l, r]`, no index
outside the range is ever considered. Taking the min of the two block minima therefore
equals the min over `[l, r]`.

### Reference implementation

```python
from typing import List


class SparseTable:
    def __init__(self, nums: List[int]) -> None:
        n = len(nums)
        # log2[i] = floor(log2(i)) for i >= 1
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

        K = self.log[n] + 1 if n else 1
        self.sparse = [[0] * n for _ in range(K)]
        self.sparse[0] = nums[:]                       # blocks of length 1
        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                self.sparse[j][i] = min(self.sparse[j - 1][i],
                                        self.sparse[j - 1][i + half])
            j += 1

    def query(self, left: int, right: int) -> int:
        k = self.log[right - left + 1]
        return min(self.sparse[k][left], self.sparse[k][right - (1 << k) + 1])


def range_min_queries(nums: List[int], queries: List[List[int]]) -> List[int]:
    st = SparseTable(nums)
    return [st.query(l, r) for l, r in queries]
```

- **Build time:** O(n log n). **Query time:** O(1). **Space:** O(n log n).

## Key Insights & Edge Cases

- **Idempotency is the whole trick.** Overlapping blocks are only allowed because
  `min(x, x) = x`. The same code works verbatim for `max`, `gcd`, bitwise AND/OR.
- **Precompute `log2`** in O(n) so each query stays O(1). Computing `log2` per query
  with floating point risks off-by-one errors near powers of two.
- **Single-element / full-array queries** are handled uniformly: for `l == r`,
  `length = 1`, `k = 0`, and both blocks are `nums[l]`.
- **No updates.** If any element changes, the whole table must be rebuilt. Use a
  Segment Tree when updates are required.
- **Negative numbers** are fine — the operation is a comparison, not an aggregation.
