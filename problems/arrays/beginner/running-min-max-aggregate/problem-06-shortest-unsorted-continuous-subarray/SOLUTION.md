# Solution — Shortest Unsorted Continuous Subarray

## Brute Force

Sort a copy of the array, then compare element by element. The first index from
the left that differs and the last index from the right that differs bound the
window.

```python
sorted_nums = sorted(nums)
lo, hi = 0, len(nums) - 1
while lo <= hi and nums[lo] == sorted_nums[lo]:
    lo += 1
while hi >= lo and nums[hi] == sorted_nums[hi]:
    hi -= 1
return hi - lo + 1 if hi >= lo else 0
```

- **Time:** O(n log n) — dominated by the sort.
- **Space:** O(n) — the sorted copy.

Correct and simple, but we can do better without sorting.

## Optimal Approach (Running Max Forward, Running Min Backward)

Two observations pin down the boundaries:

- **Right boundary `end`.** Scan left to right maintaining `running_max`, the
  maximum of everything seen so far. If `nums[i] < running_max`, then `nums[i]`
  is smaller than something to its left, so it is out of order — the window must
  extend at least to `i`. The *last* such `i` is the right boundary.
- **Left boundary `begin`.** Scan right to left maintaining `running_min`, the
  minimum of everything seen so far (from the right). If `nums[i] > running_min`,
  then `nums[i]` is larger than something to its right, so it is out of order.
  The *last* such `i` encountered scanning leftward (i.e. the smallest index) is
  the left boundary.

The answer is `end - begin + 1`, or `0` if no element was ever out of order.

Reference implementation (single loop doing both directions at once):

```python
def findUnsortedSubarray(nums):
    n = len(nums)
    begin, end = -1, -2          # so end - begin + 1 == 0 when already sorted
    running_max, running_min = nums[0], nums[-1]
    for i in range(n):
        j = n - 1 - i            # mirror index for the backward scan
        running_max = max(running_max, nums[i])
        running_min = min(running_min, nums[j])
        if nums[i] < running_max:
            end = i              # last index below the running max
        if nums[j] > running_min:
            begin = j            # smallest index above the running min
    return end - begin + 1
```

**Why it is correct.** In a fully sorted array, every element is `>=` all
elements to its left, so `nums[i] >= running_max` always holds — no `end` is
recorded. Any element with something larger before it (`nums[i] < running_max`)
*must* move, and everything up to the farthest such position must be inside the
window; the last violation defines the right edge. Symmetrically, `running_min`
from the right catches every element that has something smaller after it, and
the leftmost such position defines the left edge. Sorting exactly the window
`[begin, end]` fixes all out-of-order elements while leaving the already-correct
prefix and suffix untouched. Initializing `begin = -1, end = -2` makes the
returned length `0` when the array is sorted.

**Step-by-step** on `[2, 6, 4, 8, 10, 9, 15]` (forward pass for `end`):

| i | nums[i] | running_max | nums[i] < running_max? | end |
| - | ------- | ----------- | ---------------------- | --- |
| 0 | 2  | 2  | no  | -2 |
| 1 | 6  | 6  | no  | -2 |
| 2 | 4  | 6  | yes | 2  |
| 3 | 8  | 8  | no  | 2  |
| 4 | 10 | 10 | no  | 2  |
| 5 | 9  | 10 | yes | 5  |
| 6 | 15 | 15 | no  | 5  |

Backward pass for `begin` gives `begin = 1` (element 6 is greater than the
running min of the suffix). Answer: `end - begin + 1 = 5 - 1 + 1 = 5`.

- **Time:** O(n) — one combined pass (or two simple passes).
- **Space:** O(1).

## Key Insights & Edge Cases

- This problem needs **two** running aggregates in opposite directions: a
  running max from the left finds where things are "too small," and a running
  min from the right finds where things are "too big."
- Already-sorted input returns `0`; the sentinel initialization `begin=-1,
  end=-2` yields length `0` without a special branch.
- Duplicates are fine: the comparisons use strict `<` / `>`, so equal neighbors
  never expand the window (the array `[1, 1, 1]` returns `0`).
- A single-element or empty-ish array is trivially sorted and returns `0`.
- The window is *inclusive* of both boundaries, hence the `+ 1` in the length.
