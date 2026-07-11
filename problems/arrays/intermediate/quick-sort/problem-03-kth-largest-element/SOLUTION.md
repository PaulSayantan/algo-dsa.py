# Kth Largest Element in an Array — Solution

## Brute Force

**Sort and index.** Sort `nums` ascending and return `nums[len(nums) - k]`.

```python
nums.sort()
return nums[len(nums) - k]
```

- **Time:** O(n log n) for the sort.
- **Space:** O(1) to O(n) depending on the sort implementation.

A heap of size `k` improves this to O(n log k) time and O(k) space, which is a common
alternative answer. But we can do better on average with Quickselect.

## Optimal Approach (Quickselect)

The k-th **largest** element equals the element at **ascending** index
`target = len(nums) - k`. Quickselect reuses Quick Sort's partition but recurses into
only **one** side:

1. Pick a random pivot in `nums[lo..hi]` and partition. The pivot lands at final index
   `p`, with everything `< pivot` to its left and everything `>= pivot` to its right.
2. If `p == target`, the pivot is the answer — return it.
3. If `p < target`, the target is in the right half — recurse on `nums[p+1..hi]`.
4. If `p > target`, the target is in the left half — recurse on `nums[lo..p-1]`.

Because we throw away one side each step, the expected work is `n + n/2 + n/4 + ... =
O(n)` rather than the O(n log n) of sorting both sides.

### Why it is correct

After a partition, index `p` holds an element in its final sorted position. So if
`p == target` we have found the value that belongs at the target rank. Otherwise the
target rank must lie strictly in the sub-array on the side we recurse into, and its
relative order there is unchanged — the same argument applies recursively until the
partition point coincides with `target`.

### Reference implementation

```python
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k  # ascending index of the k-th largest

        def partition(lo: int, hi: int) -> int:
            r = random.randint(lo, hi)
            nums[r], nums[hi] = nums[hi], nums[r]
            pivot = nums[hi]
            i = lo
            for j in range(lo, hi):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[hi] = nums[hi], nums[i]
            return i

        lo, hi = 0, len(nums) - 1
        while True:
            p = partition(lo, hi)
            if p == target:
                return nums[p]
            elif p < target:
                lo = p + 1
            else:
                hi = p - 1
```

### Complexity

- **Time:** O(n) expected, O(n^2) worst case (mitigated by the random pivot).
- **Space:** O(1) with the iterative loop above (O(log n) if written recursively).

## Key Insights & Edge Cases

- **Index conversion:** the classic bug is confusing "largest" with "smallest".
  Convert once: k-th largest -> ascending index `len(nums) - k`.
- **Randomize the pivot.** LeetCode 215 includes large inputs (`n` up to 10^5) plus
  sorted arrays designed to force O(n^2) on a fixed-pivot Lomuto partition.
- **Duplicates count individually** — the k-th largest is a positional rank, not a
  distinct-value rank (see Example 2).
- **Iterative loop** avoids recursion-depth issues and keeps space at O(1).
- **Single element** (`n == 1, k == 1`) returns immediately after one partition where
  `p == target == 0`.
