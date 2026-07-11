# Sort an Array — Solution

## Brute Force

The "brute force" baseline is any simple O(n^2) sort — for example selection sort or
insertion sort — which repeatedly finds the next element to place.

- **Time:** O(n^2) for selection/insertion sort in the average and worst case.
- **Space:** O(1) auxiliary.

This passes small inputs but times out on the upper constraint (`n = 5 * 10^4`).

## Optimal Approach (Quick Sort)

Quick Sort is divide-and-conquer built on a single subroutine, **partition**:

1. Choose a **pivot**. A fixed pivot (e.g. `nums[hi]`) is simplest but gives O(n^2)
   on already-sorted input. Swap a **random** index into `hi` first to make the
   expected cost O(n log n) regardless of input order.
2. **Partition** `nums[lo..hi]` around the pivot value so that every element `< pivot`
   comes before it and every element `> pivot` comes after. The pivot lands at some
   final index `p`.
3. Recurse on `nums[lo..p-1]` and `nums[p+1..hi]`. The pivot itself is already in its
   correct, final sorted spot, so it is never touched again.

### Why it is correct

Each `partition` call establishes a loop invariant: at index `p`, everything to the
left is `<= pivot` and everything to the right is `>= pivot`, so the pivot is in its
final position. Recursion then sorts each side independently. Since the sub-arrays are
disjoint and the pivot is fixed, combining them yields a fully sorted array. The
recursion terminates because each call strictly shrinks the range (`p` is excluded
from both recursive calls).

### Reference implementation (Lomuto partition, randomized pivot)

```python
import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(lo: int, hi: int) -> int:
            rand = random.randint(lo, hi)
            nums[rand], nums[hi] = nums[hi], nums[rand]  # random pivot -> hi
            pivot = nums[hi]
            i = lo                       # boundary of the "< pivot" region
            for j in range(lo, hi):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[hi] = nums[hi], nums[i]        # pivot to its slot
            return i

        def quicksort(lo: int, hi: int) -> None:
            if lo >= hi:
                return
            p = partition(lo, hi)
            quicksort(lo, p - 1)
            quicksort(p + 1, hi)

        quicksort(0, len(nums) - 1)
        return nums
```

### Complexity

- **Time:** O(n log n) expected (each level does O(n) partition work across
  ~log n levels). Worst case O(n^2) if pivots are consistently extreme, made
  vanishingly unlikely by randomization.
- **Space:** O(log n) expected recursion-stack depth; O(n) worst case. No auxiliary
  array — the sort is in place.

## Key Insights & Edge Cases

- **Randomize the pivot** (or use median-of-three). LeetCode's test set includes a
  large sorted array specifically to break fixed-pivot Lomuto partition into O(n^2).
- **Duplicate-heavy input** (e.g. all equal values) is the pathological case for the
  simple two-way Lomuto scheme, which still hits O(n^2). Using **3-way partitioning**
  (see Problem 2, Dutch National Flag) groups equal elements and restores O(n log n)
  on such inputs.
- **Base case:** `lo >= hi` covers both empty and single-element ranges.
- **In-place swaps** mean the returned list is the same object that was passed in.
- Negative numbers need no special handling — comparisons work unchanged.
