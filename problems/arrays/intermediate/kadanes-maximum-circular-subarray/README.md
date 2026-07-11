# Kadane's — Maximum Circular Subarray

## What it is

**Kadane's algorithm** finds the maximum-sum contiguous subarray of a linear
array in a single O(n) pass. The **Maximum Circular Subarray** technique
extends Kadane to arrays that *wrap around* — where a subarray may run off the
right end and continue from index `0` (imagine the array bent into a ring).

The key realization is that any circular-array subarray is exactly one of two
shapes:

1. **Non-wrapping** — an ordinary contiguous slice `nums[i..j]`. The best such
   sum is plain Kadane on the array.
2. **Wrapping** — it uses a prefix `nums[0..i]` *and* a suffix `nums[j..n-1]`,
   skipping a middle chunk `nums[i+1..j-1]`. Its sum equals
   `total - (sum of the skipped middle)`. To make the wrapping sum as large as
   possible, we make the skipped middle as small as possible — i.e. the
   **minimum-sum subarray** (also found by a mirrored Kadane).

Putting the two together:

```
answer = max( maxKadane(nums),           # best non-wrapping
              total - minKadane(nums) )   # best wrapping = total - min middle
```

## The all-negative gotcha

The formula has one famous trap. If every element is negative, the
minimum-sum subarray is the entire array, so `total - minKadane(nums) == 0`,
which corresponds to choosing an **empty** middle — i.e. an empty subarray.
When subarrays must be non-empty, that `0` is invalid. The fix is a single
guard: if `maxKadane(nums) < 0` (all numbers negative), just return
`maxKadane(nums)`.

## When to reach for it

Reach for this technique whenever a problem involves **best/worst contiguous
sum on a ring**, or more generally whenever "the optimal window might wrap
around the ends":

- Maximum (or minimum) sum subarray in a **circular** array.
- Problems that decompose the answer into "a middle piece I want to *exclude*"
  — `total - best_middle` is the recurring identity.
- Maximum **absolute** sum of any subarray (need both the max-Kadane and the
  min-Kadane running values).
- Wrap-around over a **repeated/concatenated** array (`k` copies), where the
  cross-copy join is captured by running Kadane over two concatenated copies.

## Typical complexity

- **Time:** O(n) — a constant number of linear scans (max-Kadane, min-Kadane,
  and a sum), so O(n) overall regardless of how they are fused.
- **Space:** O(1) — only a handful of running accumulators.

## The two-Kadane skeleton

```python
def max_circular(nums):
    total = 0
    cur_max = best_max = nums[0]   # standard Kadane (maximum)
    cur_min = best_min = nums[0]   # mirrored Kadane (minimum)
    for i, x in enumerate(nums):
        total += x
        if i == 0:
            continue
        cur_max = max(x, cur_max + x); best_max = max(best_max, cur_max)
        cur_min = min(x, cur_min + x); best_min = min(best_min, cur_min)
    if best_max < 0:              # all elements negative -> no wrap allowed
        return best_max
    return max(best_max, total - best_min)
```

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Maximum Subarray](problem-01-maximum-subarray/PROBLEM.md) | Plain Kadane — largest sum of a contiguous (non-circular) subarray. The base case you must master first. | Easy |
| 2 | [Maximum Sum Circular Subarray](problem-02-maximum-sum-circular-subarray/PROBLEM.md) | The core technique: `max(maxKadane, total − minKadane)` with the all-negative guard. | Medium |
| 3 | [Minimum Sum Circular Subarray](problem-03-minimum-sum-circular-subarray/PROBLEM.md) | The mirror image: `min(minKadane, total − maxKadane)` with an all-positive guard. | Medium |
| 4 | [Maximum Absolute Sum of Any Subarray](problem-04-maximum-absolute-sum-of-any-subarray/PROBLEM.md) | Run max-Kadane and min-Kadane together; answer is `max(maxKadane, −minKadane)`. | Medium |
| 5 | [K-Concatenation Maximum Sum](problem-05-k-concatenation-maximum-sum/PROBLEM.md) | Wrap-around over `k` repeated copies; combine Kadane on two copies with `(k−2)·total`. | Hard |
