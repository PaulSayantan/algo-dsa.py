# Maximum Sum Circular Subarray — Solution

## Brute Force

Every circular subarray starts at some index `i` and extends up to `n` elements.
Try all start/length pairs, summing modulo `n`.

```python
def brute(nums):
    n = len(nums)
    best = nums[0]
    for i in range(n):
        running = 0
        for length in range(1, n + 1):       # at most n elements
            running += nums[(i + length - 1) % n]
            best = max(best, running)
    return best
```

- **Time:** `O(n^2)`.
- **Space:** `O(1)`.

## Optimal Approach (Divide & Conquer)

The key observation splits the answer into two cases:

1. **Non-wrapping** best = ordinary maximum subarray. Solve with the standard
   divide & conquer recursion (problem 1): best of left, right, and the crossing
   subarray (best suffix of left + best prefix of right).
2. **Wrapping** best = `total(nums) - (minimum subarray)`. A wrapping subarray
   keeps a prefix and a suffix and drops a contiguous interior chunk; to maximize
   what we keep, we drop the interior chunk with the **smallest** sum. The minimum
   subarray is found with the *same* merge, mirrored: at every level take the best
   of left-min, right-min, and the crossing **minimum** (worst suffix of left +
   worst prefix of right).

The answer is `max(non_wrapping, wrapping)`, with one guard (below).

```python
def maxSubarraySumCircular(nums):
    def merge_solve(a, pick):
        # pick = max -> maximum subarray; pick = min -> minimum subarray
        def crossing(lo, mid, hi):
            s, left = 0, None
            for i in range(mid, lo - 1, -1):
                s += a[i]
                left = s if left is None else pick(left, s)
            s, right = 0, None
            for j in range(mid + 1, hi + 1):
                s += a[j]
                right = s if right is None else pick(right, s)
            return left + right

        def solve(lo, hi):
            if lo == hi:
                return a[lo]
            mid = (lo + hi) // 2
            return pick(solve(lo, mid), solve(mid + 1, hi), crossing(lo, mid, hi))

        return solve(0, len(a) - 1)

    total = sum(nums)
    best_max = merge_solve(nums, max)
    best_min = merge_solve(nums, min)
    if best_max < 0:                 # every element negative -> all-negative array
        return best_max              # wrapping would remove everything; disallowed
    return max(best_max, total - best_min)
```

**Why it is correct.**

- The maximum subarray via divide & conquer is correct by the three-case argument
  from problem 1.
- For a wrapping subarray, the *removed* middle is a non-empty ordinary subarray,
  so `wrapping_sum = total - interior_sum` is maximized when `interior_sum` is
  minimized — exactly the minimum subarray, which the mirrored merge computes.
- **All-negative guard:** if `best_max < 0`, every element is negative, so the
  minimum subarray is the entire array and `total - best_min = 0` would correspond
  to removing *everything* — an empty subarray, which is not allowed. In that case
  the true answer is simply `best_max` (the least-negative single element).

**Step by step on `[5, -3, 5]`:**

- `total = 7`.
- Maximum subarray = `5` (either single 5; the middle `-3` blocks a non-wrapping
  join). `best_max = 5`.
- Minimum subarray = `[-3] = -3`. `best_min = -3`.
- Wrapping = `total - best_min = 7 - (-3) = 10`, corresponding to keeping the two
  `5`s and dropping `-3`.
- `max(5, 10) = 10`. ✓

**Complexity.** Two independent divide & conquer passes, each `T(n) = 2T(n/2) +
O(n) = O(n log n)`. Total time `O(n log n)`, space `O(log n)` recursion depth.

## Key Insights & Edge Cases

- **`total - min_subarray` is the whole wrapping trick.** Keeping a
  suffix+prefix is the complement of removing one interior slice.
- **All-negative arrays are the classic trap.** Without the `best_max < 0` guard,
  the wrapping branch returns `0` (removing everything) and you would wrongly
  report `0` for `[-3, -2, -3]` instead of `-2`.
- **Both merges reuse identical structure** — pass `max` or `min` as the combine
  operator. This is the point of the exercise: the crossing-combine generalizes.
- **`min` crossing uses the *worst* suffix/prefix**, i.e. the smallest running
  sums, mirroring the max version.
- **Kadane note:** LeetCode solutions usually do this with two Kadane passes in
  `O(n)`; the divide & conquer version is the paradigm-focused equivalent.
