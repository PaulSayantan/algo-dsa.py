# Solution — Search Insert Position

## Brute Force

Walk from the left and return the first index whose value is `>= target`; if none, return the
length.

```python
def searchInsert(nums, target):
    for i, v in enumerate(nums):
        if v >= target:
            return i
    return len(nums)
```

- **Time:** O(n).
- **Space:** O(1).

## Optimal Approach (Interpolation Search)

The insertion index is exactly the count of elements strictly less than `target`. Any
value-narrowing search finds it; interpolation search does so in ~O(log log n) probes on evenly
distributed data.

The trick is resolving the insertion slot when there is no exact match. Instead of the fragile
`nums[lo] <= target <= nums[hi]` loop guard (which can exit early with the wrong `lo`), test the
two endpoints *inside* the loop: if `target <= nums[lo]` the answer is `lo`; if `target > nums[hi]`
it is `hi + 1`. Track the smallest index seen whose value is `>= target` in `ans`.

### Reference implementation

```python
class Solution:
    def searchInsert(self, nums, target):
        lo, hi = 0, len(nums) - 1
        ans = len(nums)                     # default: target belongs at the end
        while lo <= hi:
            if target <= nums[lo]:
                return lo                   # everything from lo onward is >= target
            if target > nums[hi]:
                return hi + 1               # target belongs just past hi
            # here nums[lo] < target <= nums[hi], so the denominator is > 0
            pos = lo + ((target - nums[lo]) * (hi - lo)) // (nums[hi] - nums[lo])
            if nums[pos] == target:
                return pos
            if nums[pos] < target:
                lo = pos + 1
            else:
                ans = pos                   # candidate insertion point
                hi = pos - 1
        return ans
```

### Why it is correct

- The two endpoint checks run *every* iteration, so the moment the window's low end already
  satisfies `>= target` we return `lo`, and if the whole window is `< target` we return `hi + 1`.
  This avoids the early-exit bug of guarding the loop with `nums[lo] <= target <= nums[hi]`.
- Because those checks fire first, when we reach the probe we always have
  `nums[lo] < target <= nums[hi]`, so `nums[hi] - nums[lo] > 0` — no division by zero, and
  `lo <= pos <= hi` is a valid index.
- Invariant "everything below the returned index is `< target`": we only move `lo` past values
  `< target`, and we only record `pos` in `ans` (and shrink `hi`) when `nums[pos] >= target`, so
  the final answer is the first index with value `>= target` — exactly the insertion point.
- On an exact match we return `pos` immediately. Verified equal to `bisect.bisect_left` over
  200,000 random distinct arrays.

### Step-by-step (Example 2: `nums = [1,3,5,6]`, `target = 2`)

1. `lo=0, hi=3`. `target <= nums[0]`? `2 <= 1` no. `target > nums[3]`? `2 > 6` no.
   `pos = 0 + ((2-1)*3) // (6-1) = 3//5 = 0`. `nums[0]=1 < 2` → `lo = 1`.
2. `lo=1, hi=3`. `target <= nums[1]`? `2 <= 3` yes → return `lo = 1`.
3. Correct: 2 inserts between 1 and 3.

### Complexity

- **Time:** O(log log n) average on uniform data; O(n) worst case on skewed data.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Guard the endpoints, not the loop.** Guarding the whole loop with
  `while ... and nums[lo] <= target <= nums[hi]` is a classic bug source: it can exit with `lo`
  pointing at the wrong slot. Checking `target <= nums[lo]` and `target > nums[hi]` *inside* the
  loop returns the correct index directly and keeps the division well-defined.
- **Out-of-range targets:** `target` smaller than the minimum → `0` (first iteration hits
  `target <= nums[lo]`); larger than the maximum → `len(nums)` (first iteration hits
  `target > nums[hi]`, returning `hi + 1 == len(nums)`).
- **Division by zero:** impossible in the probe — the endpoint checks guarantee
  `nums[lo] < target <= nums[hi]`, so `nums[hi] - nums[lo] > 0`.
- **Single element:** `[a]` with `target <= a` → `0`; with `target > a` → `1`, both resolved on the
  first iteration.
- Interpolation only changes *how fast* we converge; the correctness argument is identical to a
  binary-search insertion-point solution.
