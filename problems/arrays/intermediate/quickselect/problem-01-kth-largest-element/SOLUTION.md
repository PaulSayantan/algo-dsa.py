# Solution — Kth Largest Element in an Array

## Brute Force

Sort the array in ascending order and index directly.

```python
def findKthLargest(self, nums, k):
    nums.sort()
    return nums[len(nums) - k]
```

- **Time:** `O(n log n)` for the sort.
- **Space:** `O(1)` extra (or `O(n)` depending on the sort implementation).

A slightly better classic alternative is a **min-heap of size k**: push all elements,
keep only the k largest, and the heap root is the answer — `O(n log k)` time,
`O(k)` space. This is the go-to when you cannot mutate the input or need an online/streaming
solution.

## Optimal Approach (Quickselect)

The k-th **largest** element sits at index `target = n - k` when the array is sorted
**ascending**. Quickselect finds the element at a given index in expected `O(n)` without
sorting the whole array.

### Why it is correct

The partition step places the chosen pivot into its **final sorted position** `p`:
every element left of `p` is `<= pivot` and every element right of `p` is `>= pivot`.
Therefore:

- If `p == target`, `nums[p]` is exactly the element that belongs at `target` in the
  sorted array — the answer.
- If `p < target`, all indices `<= p` are settled and too small; the answer must be to
  the right, so we search `[p + 1, hi]`.
- If `p > target`, the answer must be to the left, so we search `[lo, p - 1]`.

Each iteration keeps the invariant "the element that belongs at `target` lies within
`[lo, hi]`", so when the search narrows to the pivot at `target` we have the correct value.

### Step-by-step

1. Set `target = n - k`, `lo = 0`, `hi = n - 1`.
2. Choose a **random** pivot index in `[lo, hi]` and partition `[lo, hi]` around it
   (Lomuto or Hoare scheme). Let `p` be the pivot's final index.
3. Compare `p` with `target` and shrink `[lo, hi]` to the correct side (or return if equal).
4. Repeat until the pivot lands on `target`.

### Reference implementation

```python
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k          # index in ascending-sorted order
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            p = self._partition(nums, lo, hi)
            if p == target:
                return nums[p]
            elif p < target:
                lo = p + 1
            else:
                hi = p - 1
        return nums[lo]                 # unreachable for valid input

    def _partition(self, nums: List[int], lo: int, hi: int) -> int:
        # Randomized pivot avoids O(n^2) on sorted / adversarial input.
        rand = random.randint(lo, hi)
        nums[rand], nums[hi] = nums[hi], nums[rand]
        pivot = nums[hi]
        i = lo
        for j in range(lo, hi):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]
        return i
```

- **Time:** expected `O(n)`; worst case `O(n^2)` (mitigated by the random pivot).
- **Space:** `O(1)` — the loop is iterative and partitions in place.

## Key Insights & Edge Cases

- **Rank conversion:** the k-th *largest* = index `n - k` when sorted ascending. Off-by-one
  here is the most common bug. Sanity check: `k = 1` -> `target = n - 1` (the maximum).
- **Duplicates are counted, not deduplicated.** `[3,3,3]`, `k = 2` returns `3`. Because
  partition uses `<=`, equal elements are handled naturally.
- **Randomize the pivot.** A fixed last-element pivot degrades to `O(n^2)` on sorted input;
  a random pivot makes worst cases astronomically unlikely.
- **Single element / k == n:** `nums = [x]`, `k = 1` returns `x`; `k == n` returns the
  minimum. Both fall out of the same logic with no special casing.
- **In-place mutation:** Quickselect reorders `nums`. If the caller needs the original order,
  operate on a copy.
