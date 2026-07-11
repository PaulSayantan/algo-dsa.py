# Count of Range Sum — Solution

## Brute Force

Compute prefix sums, then for every pair `(i, j)` check whether `S(i, j)` is in
`[lower, upper]`.

- Time: `O(n^2)` — `~10^10` at `n = 10^5`. Too slow.
- Space: `O(n)` for prefix sums.

## Optimal Approach — Prefix Sums + Segment Tree over Value Domain

Define prefix sums `P[0] = 0` and `P[k] = nums[0] + ... + nums[k-1]` for
`k = 1 .. n`. Then any range sum is a difference of two prefixes:

```
S(i, j) = P[j + 1] - P[i]
```

so the condition `lower <= S(i, j) <= upper` becomes, fixing the right endpoint
`p = P[j+1]` and letting `q = P[i]` be an earlier prefix (`i <= j` ⇔ `i < j+1`):

```
lower <= p - q <= upper   ⇔   p - upper <= q <= p - lower
```

So as we scan the prefix array left to right, for each new prefix `p = P[k]` we must
count how many **already-inserted** earlier prefixes `q` fall in the value window
`[p - upper, p - lower]`. That is a range-count query over the *value domain of
prefix sums* — exactly what a count segment tree does.

### Coordinate compression

Prefix sums can be as large as `~10^5 * 2^31`, far too big to index directly. But
there are only `n + 1` of them. Collect every value we will ever query or insert —
that is, each `P[k]`, each `P[k] - lower`, and each `P[k] - upper` — sort the distinct
values, and map each to a compact rank. Now the tree needs only `O(n)` buckets.

### Step by step

1. Build `P[0..n]` with `P[0] = 0`.
2. Gather candidate coordinates: all `P[k]`, all `P[k] - lower`, all `P[k] - upper`.
   Sort + dedupe → `sorted_vals`, and map value → rank by binary search.
3. Count segment tree over `m = len(sorted_vals)` buckets, all zero.
4. For `k` from `0` to `n`:
   - `p = P[k]`.
   - answer += number of inserted prefixes `q` with
     `p - upper <= q <= p - lower` → `query(rank(p - upper) low side, rank(p - lower) high side)`.
   - insert `p`: `update(rank(p), +1)`.
5. Return the accumulated answer.

Inserting `P[k]` **after** querying with it guarantees we only count pairs with
`i < k` (strictly earlier prefixes), matching `i <= j`.

### Why it is correct

The transformation `S(i,j) = P[j+1] - P[i]` is exact. Processing prefixes in index
order and inserting after querying ensures that when we query with `p = P[k]`, the
tree contains exactly `P[0], ..., P[k-1]` — all valid left endpoints `q = P[i]` with
`i < k`. The window `[p - upper, p - lower]` is precisely the set of `q` making the
range sum land in `[lower, upper]`.

### Reference implementation

```python
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for k in range(n):
            prefix[k + 1] = prefix[k] + nums[k]

        # candidate coordinates for both queries and insertions
        coords = set()
        for p in prefix:
            coords.add(p)
            coords.add(p - lower)
            coords.add(p - upper)
        sorted_vals = sorted(coords)
        m = len(sorted_vals)
        tree = [0] * (2 * m)

        def update(pos: int) -> None:
            i = pos + m
            while i >= 1:
                tree[i] += 1
                i //= 2

        def query(l: int, r: int) -> int:      # inclusive count over ranks [l, r]
            if l > r:
                return 0
            res, l, r = 0, l + m, r + m + 1
            while l < r:
                if l & 1:
                    res += tree[l]; l += 1
                if r & 1:
                    r -= 1; res += tree[r]
                l //= 2; r //= 2
            return res

        ans = 0
        for p in prefix:
            lo_rank = bisect_left(sorted_vals, p - upper)          # first >= p-upper
            hi_rank = bisect_right(sorted_vals, p - lower) - 1     # last  <= p-lower
            ans += query(lo_rank, hi_rank)
            update(bisect_left(sorted_vals, p))                    # insert p
        return ans
```

### Complexity

- Time: `O(n log n)` — sorting the `O(n)` coordinates plus one `query` and one
  `update` (each `O(log n)`) per prefix.
- Space: `O(n)` for prefix sums, coordinate table, and the tree.

## Key Insights & Edge Cases

- **Difference-of-prefixes reframing** turns a 2-D "count pairs" problem into a 1-D
  "count earlier values in a window" sweep — the standard trick for range-sum
  counting.
- **Include the `P[0] = 0` prefix.** Sub-arrays that start at index 0 correspond to
  `q = P[0] = 0`; forgetting it undercounts.
- **Query-then-insert order** enforces `i < k`; inserting first would wrongly let a
  prefix pair with itself (a zero-length "range").
- **Compress query bounds too.** `p - lower` and `p - upper` must be in the coordinate
  set (or found via `bisect`), otherwise the window ranks are wrong. Using
  `bisect_left` for the low bound and `bisect_right - 1` for the high bound correctly
  handles values not present in the array.
- **64-bit prefix sums.** With `nums[i]` up to `2^31 - 1` and `n = 10^5`, prefixes can
  overflow 32 bits — fine in Python, but in C++/Java use `long long`. Coordinate
  compression sidesteps ever indexing by these huge values.
- **Empty window** (`lo_rank > hi_rank`) returns `0` — guard it.
