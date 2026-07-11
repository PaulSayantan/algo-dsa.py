# Maximum Subarray — Solution

## Brute Force

Try every pair of endpoints `(i, j)` and sum the subarray between them, tracking the
maximum.

- **Time:** `O(n^2)` if you extend a running sum for each start `i`; `O(n^3)` if you
  re-sum each subarray from scratch.
- **Space:** `O(1)`.

Correct but too slow at `n = 10^5`.

## Optimal Approach (Divide and Conquer)

**Idea:** For a range `[lo, hi]`, split at `mid`. Any contiguous subarray falls into
exactly one of three categories:

1. **Entirely in the left half** `[lo, mid]` — solved recursively.
2. **Entirely in the right half** `[mid+1, hi]` — solved recursively.
3. **Crossing the midpoint** — it must include `nums[mid]` and `nums[mid+1]`. Compute
   the best sum extending *leftward* from `mid` and the best sum extending *rightward*
   from `mid+1`, then add them. This is the **combine** step, and it is where the
   left and right pieces get stitched into a single subarray.

The answer for the range is the maximum of these three.

```python
def maxSubArray(nums):
    def rec(lo, hi):
        if lo == hi:                       # base case: single element
            return nums[lo]
        mid = (lo + hi) // 2

        best_left = rec(lo, mid)
        best_right = rec(mid + 1, hi)

        # best crossing sum: must touch both nums[mid] and nums[mid+1]
        s, left_part = 0, float("-inf")
        for i in range(mid, lo - 1, -1):   # extend left from mid
            s += nums[i]
            left_part = max(left_part, s)
        s, right_part = 0, float("-inf")
        for i in range(mid + 1, hi + 1):   # extend right from mid+1
            s += nums[i]
            right_part = max(right_part, s)
        cross = left_part + right_part

        return max(best_left, best_right, cross)

    return rec(0, len(nums) - 1)
```

**Why it is correct:** every non-empty subarray is either confined to one half or
spans the split point; those cases are exhaustive and mutually exclusive. The
recursion handles the confined cases; the crossing scan is guaranteed to find the best
midpoint-spanning subarray because it independently maximizes the left extension and
the right extension, and a crossing subarray's sum is exactly `left_ext + right_ext`.

**Recurrence:** `T(n) = 2T(n/2) + O(n)` — the crossing scan is linear → `O(n log n)`.

- **Time:** `O(n log n)`.
- **Space:** `O(log n)` recursion stack.

## Key Insights & Edge Cases

- **The three-way split is the core idea:** left, right, or crossing. Forgetting the
  crossing case is the classic bug — it is the only case that actually needs the two
  halves' data combined.
- **Crossing sums must be seeded from the midpoint outward** (starting sums at `mid`
  and `mid+1`), not from `lo`/`hi`, so that the two extensions are forced to meet at
  the split and together form one contiguous subarray.
- **All-negative arrays** (example 3): because subarrays must be non-empty and the base
  case returns the single element, the answer is the largest single element (`-1`),
  never `0`.
- **Initialize crossing parts to `-inf`,** not `0`, so a forced-negative extension is
  still counted (the subarray must include the boundary element).
- **Kadane's `O(n)` DP is strictly faster** here, but the D&C formulation is the CLRS
  teaching example and generalizes to settings without a linear scan (e.g. segment
  trees storing prefix/suffix/best/total per node use exactly this crossing-combine).
