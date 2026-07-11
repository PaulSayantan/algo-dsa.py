# Solution — Smallest Subarrays With Maximum Bitwise OR

## Brute Force

For each start `i`, compute the target `full = OR(nums[i..n-1])`, then extend `j` from
`i` accumulating the running OR until it equals `full`; record `j - i + 1`.

- **Time:** O(n^2) — every start may scan to the end.
- **Space:** O(1) extra.

For `n = 10^5` this is up to `10^10` operations.

## Optimal Approach (Sparse Table + binary search)

> There is a well-known O(n) two-pointer / bit-counting solution scanning right to
> left. We present the **Sparse Table** approach because it is the technique of this
> folder and cleanly exploits OR's idempotency.

### Key facts about OR on a window

1. **Monotone growth:** extending a window to the right can only set more bits, so
   `OR(nums[i..j])` is non-decreasing in `j`. Hence the maximum OR achievable from
   start `i` is exactly the suffix OR `OR(nums[i..n-1])`.
2. **Idempotent:** `x | x = x`, so a Sparse Table answers `OR(nums[l..r])` in O(1) with
   two overlapping blocks.

### Algorithm

1. Build a Sparse Table `stOr` with `stOr[j][i] = OR(nums[i .. i+2^j-1])`.
2. For each `i`, the target is `full = stOr.query(i, n - 1)`.
3. Because `OR(nums[i..j])` is non-decreasing and eventually equals `full`, the set of
   `j` with `OR(nums[i..j]) == full` is a suffix `[j*, n-1]`. **Binary search** the
   smallest such `j*` in `[i, n-1]`: for a candidate `mid`, if
   `stOr.query(i, mid) == full` search left, else search right.
4. `answer[i] = j* - i + 1`.

### Why it is correct

The predicate `P(j) = (OR(nums[i..j]) == full)` is monotone: once true at some `j` it
stays true for all larger `j` (bits only accumulate and cannot exceed `full`, which is
the OR of the whole suffix). Binary search therefore finds the exact first `j*`. The
O(1) queries are exact because OR is idempotent, so overlapping blocks never
over-count.

### Reference implementation

```python
from typing import List


class SparseTableOr:
    def __init__(self, nums: List[int]) -> None:
        n = len(nums)
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1
        K = self.log[n] + 1 if n else 1
        self.sp = [[0] * n for _ in range(K)]
        self.sp[0] = nums[:]
        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                self.sp[j][i] = self.sp[j - 1][i] | self.sp[j - 1][i + half]
            j += 1

    def query(self, l: int, r: int) -> int:
        k = self.log[r - l + 1]
        return self.sp[k][l] | self.sp[k][r - (1 << k) + 1]


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = SparseTableOr(nums)
        ans = [1] * n
        for i in range(n):
            full = st.query(i, n - 1)
            lo, hi, j_star = i, n - 1, n - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if st.query(i, mid) == full:
                    j_star = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            ans[i] = j_star - i + 1
        return ans
```

- **Build:** O(n log n). **Per start:** O(log n) queries. **Total:** O(n log n).
  **Space:** O(n log n).

## Key Insights & Edge Cases

- **Idempotency + monotonicity** are both used: idempotency validates the O(1) query,
  monotonicity validates the binary search.
- **Last index:** `answer[n-1] = 1` because the only subarray from the last index is a
  single element, which already equals its own suffix OR.
- **Zeros / duplicate bits:** OR handles them naturally — extra zeros never change the
  target, and duplicated bits are absorbed by idempotency.
- **`answer[i] >= 1` always**, since a start's own element contributes to the OR.
- **No updates.** The array is treated as immutable; a change requires a rebuild.
