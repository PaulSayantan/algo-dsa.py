# Solution — Count of Range Sum

## Brute Force

Compute prefix sums, then test every pair of prefix indices.

```python
def countRangeSum_brute(nums, lower, upper):
    n = len(nums)
    P = [0] * (n + 1)
    for k in range(n):
        P[k + 1] = P[k] + nums[k]
    count = 0
    for a in range(n + 1):
        for b in range(a + 1, n + 1):
            if lower <= P[b] - P[a] <= upper:
                count += 1
    return count
```

- **Time:** `O(n^2)`.
- **Space:** `O(n)` for the prefix array.

Too slow at `n = 10^5`.

## Optimal Approach — Count Inversions (Merge Sort)

**Step 1 — prefix sums.** With `P[0] = 0` and `P[k] = nums[0] + ... + nums[k-1]`,
a subarray sum `S(i, j) = P[j+1] - P[i]`. So counting subarrays with sum in
`[lower, upper]` equals counting prefix-index pairs `a < b` (indices `0..n`) with

```
lower <= P[b] - P[a] <= upper.
```

This is a **two-sided** cross-pair count over `P` — the inversion-counting merge
generalized from one inequality to a range.

**Step 2 — count during merge.** Merge-sort the prefix array `P`. In a merge the
left block holds the smaller prefix indices `a` and the right block the larger
indices `b`, so `a < b` holds for every cross pair automatically. Both blocks are
sorted ascending by value. For each left value `P[a]`, the right values `P[b]`
that satisfy the range are those with

```
P[a] + lower <= P[b] <= P[a] + upper,
```

i.e. a contiguous window of the sorted right block. Maintain two pointers `k1`
(first right index with `P[b] >= P[a] + lower`) and `k2` (first right index with
`P[b] > P[a] + upper`); the window size is `k2 - k1`. As `P[a]` increases (left
block is sorted), both bounds increase, so `k1` and `k2` only move forward —
monotone two-pointers, linear per level. Then perform the ordinary merge to keep
`P` sorted for the parent.

### Why it is correct

Left indices are all `< mid` and right indices `>= mid`, so `a < b` for every
counted cross pair — the `a < b` requirement is satisfied structurally and no
pair is counted twice. For a fixed `a`, the valid `b` values form a contiguous
range of the sorted right block, so `k2 - k1` counts them exactly. Pairs with
both indices in the same block are handled by recursion; the left-only,
right-only, and cross groups partition all pairs `a < b`.

### Step-by-step on `nums = [-2, 5, -1]`, `lower = -2`, `upper = 2`

- `P = [0, -2, 3, 2]` (indices 0..3).
- The recursion sorts `P` while counting. Consider the cross pairs by level; the
  qualifying prefix pairs `(a, b)` with `a < b` and `-2 <= P[b]-P[a] <= 2` are:
  - `(0, 1)`: `-2 - 0 = -2`  ✓  (subarray `[-2]`)
  - `(0, 3)`: `2 - 0 = 2`    ✓  (subarray `[-2, 5, -1]`)
  - `(2, 3)`: `2 - 3 = -1`   ✓  (subarray `[-1]`)
  - non-qualifying: `(0,2)=3`, `(1,2)=5`, `(1,3)=4` all fall outside `[-2, 2]`.
- Total qualifying pairs = `3`. ✓

### Reference implementation

```python
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        for k in range(n):
            P[k + 1] = P[k] + nums[k]

        def sort_count(lo: int, hi: int) -> int:
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            cnt = sort_count(lo, mid) + sort_count(mid, hi)

            # counting phase: P[lo:mid] and P[mid:hi] are each sorted ascending
            k1 = k2 = mid
            for a in range(lo, mid):
                while k1 < hi and P[k1] - P[a] < lower:
                    k1 += 1
                while k2 < hi and P[k2] - P[a] <= upper:
                    k2 += 1
                cnt += k2 - k1

            # merge phase (keep P[lo:hi] sorted)
            P[lo:hi] = sorted(P[lo:hi])
            return cnt

        return sort_count(0, n + 1)
```

The `sorted(P[lo:hi])` line can be replaced by an explicit linear two-pointer
merge into a buffer to keep the whole algorithm strictly `O(n log n)`; it is
written this way for clarity of the counting logic.

- **Time:** `O(n log n)` with a linear merge; the counting sweep is `O(n)` per
  level over `log n` levels.
- **Space:** `O(n)` for the prefix array and merge buffer, plus `O(log n)` stack.

## Key Insights & Edge Cases

- **Prefix sums include `P[0] = 0`.** The array has length `n + 1`; forgetting
  the leading zero drops all subarrays that start at index 0.
- **Two-sided window.** Unlike single-inequality inversion counting, you track
  *two* monotone pointers (`>= P[a]+lower` and `> P[a]+upper`) and count the gap.
- **Inclusive bounds.** Use `< lower` to skip and `<= upper` to include so both
  endpoints of `[lower, upper]` are counted (Example 1's `-2` and `2` both count).
- **Overflow.** Prefix sums of up to `10^5` values near `±2^31` reach `~2^46`;
  use 64-bit accumulators outside Python. `P[b] - P[a]` and the bounds must use
  the same wide type.
- **Single element / zeros.** `nums = [0]`, `lower = upper = 0` → `P = [0, 0]`,
  one qualifying pair → `1`. The base case `hi - lo <= 1` returns 0 correctly.
- Alternatives: a Binary Indexed Tree or balanced BST over coordinate-compressed
  prefix sums also give `O(n log n)`; the merge-sort version avoids compression.
