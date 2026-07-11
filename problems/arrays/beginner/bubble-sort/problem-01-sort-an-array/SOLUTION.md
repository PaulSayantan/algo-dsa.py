# Solution — Sort an Array

## Brute Force

The most naive "correct" approach is **selection by repeated scanning**: repeatedly scan the
unsorted portion, find the minimum, and append it to an output list (removing it from the
input). Removing from a Python list is `O(n)`, and we do it `n` times, so this is `O(n^2)`
time and `O(n)` extra space for the output list. It works but wastes memory and is clumsy.

- Time: `O(n^2)`
- Space: `O(n)`

## Optimal Approach (Bubble Sort)

Bubble sort sorts **in place** with only `O(1)` extra space. The idea:

1. Make repeated passes over the array from left to right.
2. On each pass, compare every adjacent pair `nums[j]` and `nums[j+1]`. If `nums[j] > nums[j+1]`,
   swap them.
3. After the first pass, the single largest element has "bubbled" to the last slot. After the
   second pass, the two largest occupy the last two slots, and so on. So on pass `i` we only
   need to scan the first `n - 1 - i` pairs.

**Why it is correct.** Loop invariant: *after `i` completed passes, the last `i` positions
contain the `i` largest elements in sorted order, and no smaller element lies to their right.*
Each pass moves the largest element of the still-unsorted prefix to the boundary, extending the
sorted suffix by one. After `n - 1` passes the whole array is sorted.

**Stability.** We swap only when `nums[j] > nums[j+1]` (strict), so equal elements never jump
past each other — their relative order is preserved.

```python
def sortArray(self, nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:      # already sorted -> stop early
            break
    return nums
```

- Time: `O(n^2)` average and worst case; `O(n)` best case (already sorted, thanks to the
  `swapped` early-exit flag).
- Space: `O(1)` — in place.

## Key Insights & Edge Cases

- **Bounds shrink each pass.** Using `range(n - 1 - i)` avoids re-comparing the already-sorted
  tail. Forgetting the `-i` still produces a correct result but does needless work.
- **Early exit.** The `swapped` flag turns an already-sorted input into a single `O(n)` pass.
- **Negatives and duplicates** need no special handling — comparisons work the same.
- **Single element / empty prefix.** With `n <= 1`, the outer loop body never runs and the
  array is returned unchanged.
- **In place vs. copy.** If the caller must keep the original untouched, operate on
  `nums = list(nums)` first.
