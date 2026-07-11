# Solution — Range GCD Queries

## Brute Force

For each query `(l, r)`, fold `gcd` across `nums[l..r]`.

- **Time:** O(q · n · log M) where `M` is the max value (each `gcd` is `O(log M)`).
- **Space:** O(1) extra.

Too slow for `n = 10^5`, `q = 2 * 10^5`.

Unlike sum, gcd has **no inverse** — you cannot derive `gcd(l..r)` from prefix gcds by
"removing" the prefix `gcd(0..l-1)`. So prefix aggregation does not help, but a Sparse
Table does.

## Optimal Approach (Sparse Table)

### Structure

`sparse[j][i] = gcd(nums[i .. i + 2^j - 1])`.

- **Base:** `sparse[0][i] = nums[i]`.
- **Transition:** `sparse[j][i] = gcd(sparse[j-1][i], sparse[j-1][i + 2^(j-1)])`.

### Query

Let `k = floor(log2(r - l + 1))`. Then

```
answer = gcd( sparse[k][l], sparse[k][r - 2^k + 1] )
```

### Why overlap is fine

The two blocks may overlap in the middle. gcd is **idempotent**:
`gcd(x, x) = x`, and more generally combining a value with itself (or with something it
already divides) does not change the result. Formally, gcd is associative,
commutative, and idempotent, so the gcd over a set of blocks equals the gcd over their
union regardless of overlaps. Every index in `[l, r]` is covered by at least one block,
and neither block reaches outside `[l, r]`, so the answer is exactly `gcd(nums[l..r])`.

### Reference implementation

```python
from math import gcd
from typing import List


class SparseTableGCD:
    def __init__(self, nums: List[int]) -> None:
        n = len(nums)
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

        K = self.log[n] + 1 if n else 1
        self.sparse = [[0] * n for _ in range(K)]
        self.sparse[0] = nums[:]
        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                self.sparse[j][i] = gcd(self.sparse[j - 1][i],
                                        self.sparse[j - 1][i + half])
            j += 1

    def query(self, left: int, right: int) -> int:
        k = self.log[right - left + 1]
        return gcd(self.sparse[k][left], self.sparse[k][right - (1 << k) + 1])


def range_gcd_queries(nums: List[int], queries: List[List[int]]) -> List[int]:
    st = SparseTableGCD(nums)
    return [st.query(l, r) for l, r in queries]
```

- **Build:** O(n log n · log M). **Query:** O(log M) for the single top-level `gcd`
  (effectively O(1) in the number of array reads). **Space:** O(n log n).

## Key Insights & Edge Cases

- **gcd is idempotent and associative**, which is precisely why the two-overlapping-
  blocks O(1) query is valid. The identical template works for min/max/AND/OR.
- **Single element:** `gcd(x) = x`; handled because `l == r` gives `k = 0`.
- **Values up to 10^9** fit in native ints; each `gcd` costs `O(log M)`. This factor is
  usually treated as a constant but is worth noting for tight time limits.
- **All positive inputs** avoid `gcd(0, ...)` subtleties; if zeros were allowed,
  `gcd(0, x) = x` still behaves correctly with Python's `math.gcd`.
- **No updates.** Changing any element invalidates the table.
