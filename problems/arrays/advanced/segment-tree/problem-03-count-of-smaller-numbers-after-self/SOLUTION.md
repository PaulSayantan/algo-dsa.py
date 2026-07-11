# Count of Smaller Numbers After Self — Solution

## Brute Force

For each `i`, scan every `j > i` and count `nums[j] < nums[i]`.

- Time: `O(n^2)` — up to `~10^10` at `n = 10^5`. Too slow.
- Space: `O(1)` beyond the output.

## Optimal Approach — Frequency Segment Tree over the Value Domain

Key reframing: "how many earlier-processed elements are smaller than `x`?" is a
**prefix-count query over values**. If we process elements from **right to left** and
keep a running multiset of values we've already seen (those strictly to the right),
then `counts[i]` is exactly the number of seen values in the range
`[min_value, nums[i] - 1]`.

A segment tree indexed by **value** (not by array position) supports:
- **point update:** increment the frequency bucket of a value by 1 — `O(log V)`.
- **range query:** sum of frequencies over a value range — `O(log V)`.

### Coordinate compression

Values lie in `[-10^4, 10^4]`, so we could offset by `10^4` and use a tree of size
`20001`. More generally, compress: sort the distinct values, map each to its rank in
`[0, m)`. Then the "strictly smaller" query becomes "sum over ranks `[0, rank-1]`".

### Step by step

1. Build the sorted list of distinct values; map value → rank via binary search.
2. Create a count segment tree over `m = #distinct` buckets, all zero.
3. Iterate `i` from `n - 1` down to `0`:
   - let `r = rank(nums[i])`.
   - `counts[i] = query(0, r - 1)` — number of already-inserted values with a smaller
     rank (== strictly smaller value).
   - `update(r, +1)` — record `nums[i]` as seen.
4. Return `counts`.

### Why it is correct

When we reach index `i`, the tree holds precisely the values at indices `i+1 .. n-1`
(everything to the right, because we go right-to-left and insert *after* querying).
`query(0, r-1)` counts those with rank `< r`, i.e. value strictly less than `nums[i]`.
Equal values share the same rank and fall **outside** `[0, r-1]`, correctly excluded
by the "strictly smaller" requirement.

### Reference implementation

```python
from bisect import bisect_left
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_vals = sorted(set(nums))
        m = len(sorted_vals)
        tree = [0] * (2 * m)              # iterative count segment tree

        def update(pos: int) -> None:     # add 1 at value-rank `pos`
            i = pos + m
            while i >= 1:
                tree[i] += 1
                i //= 2

        def query(l: int, r: int) -> int: # inclusive sum over ranks [l, r]
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

        counts = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            rank = bisect_left(sorted_vals, nums[i])
            counts[i] = query(0, rank - 1)
            update(rank)
        return counts
```

### Complexity

- Time: `O(n log n)` — one `update` + one `query` (each `O(log m)`) per element, plus
  `O(n log n)` for sorting / compression.
- Space: `O(n)` for the tree and the compression arrays.

## Key Insights & Edge Cases

- **Value-domain, not index-domain.** The tree is indexed by (compressed) value; the
  frequency stored at a bucket is how many times that value has appeared so far. This
  "count segment tree" pattern powers many inversion / rank problems.
- **Right-to-left sweep** guarantees the tree only ever contains elements to the right
  of the current index — the crux of correctness.
- **Strictly smaller** → query `[0, rank - 1]`, excluding equal values. If the problem
  asked for `<=`, query `[0, rank]` instead. Duplicates (Example 2) are handled because
  equal values share a rank.
- **`rank == 0`** makes the query range `[0, -1]`, which is empty → returns `0`. Guard
  `l > r` explicitly.
- A **Binary Indexed Tree (Fenwick)** solves this identically and with less code; the
  segment tree version generalizes more readily (e.g. to "count in an arbitrary value
  range" as in problem 4).
- **Negative values** are absorbed by coordinate compression, so no offset arithmetic
  is required.
