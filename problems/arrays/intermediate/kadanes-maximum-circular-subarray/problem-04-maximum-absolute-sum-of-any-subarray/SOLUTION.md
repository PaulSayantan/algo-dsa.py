# Solution — Maximum Absolute Sum of Any Subarray

## Brute Force

Enumerate every subarray, accumulate its sum with a running inner loop, and
track the maximum absolute value.

```python
best = 0
for i in range(len(nums)):
    running = 0
    for j in range(i, len(nums)):
        running += nums[j]
        best = max(best, abs(running))
return best
```

- **Time:** O(n^2).
- **Space:** O(1).

## Optimal Approach — Simultaneous Max-Kadane and Min-Kadane

`abs(S)` is large exactly when `S` is very **positive** or very **negative**.
So the maximum absolute subarray sum is:

```
answer = max( maxSubarraySum, -minSubarraySum )
```

where `maxSubarraySum` is the most-positive subarray sum (maximizing Kadane)
and `minSubarraySum` is the most-negative subarray sum (minimizing Kadane).
Run both in a single pass. Because the empty subarray (sum `0`) is allowed,
seeding the running accumulators at `0` is fine and guarantees the answer is
non-negative.

```python
def maxAbsoluteSum(nums):
    cur_max = cur_min = 0
    best_max = best_min = 0
    for x in nums:
        cur_max = max(0, cur_max + x)   # empty subarray allowed -> floor at 0
        cur_min = min(0, cur_min + x)   # empty subarray allowed -> cap at 0
        best_max = max(best_max, cur_max)
        best_min = min(best_min, cur_min)
    return max(best_max, -best_min)
```

An equivalent and elegant reformulation uses prefix sums: with
`P[i] = nums[0] + ... + nums[i-1]` (and `P[0] = 0`), any subarray sum is
`P[r] - P[l]`, so the maximum absolute subarray sum equals
`max(P) - min(P)`. Both views are O(n).

### Why it is correct

Every subarray sum lies between the minimum subarray sum and the maximum
subarray sum. The value with the largest magnitude is therefore attained at one
of those two extremes, so taking `max(best_max, -best_min)` cannot miss the
optimum. The maximizing and minimizing Kadanes are independent and both correct
by the standard Kadane argument (see Problem 1).

### Step by step on `nums = [2, -5, 1, -4, 3, -2]`

Maximizing side (floor at 0): running maxes give `best_max = 3` (subarray `[3]`).
Minimizing side (cap at 0): `cur_min` reaches its lowest at `2 - 5 + 1 - 4 = -6`
after index 3, i.e. subarray `[-5, 1, -4]` with sum `-8` when measured from the
start of that run — the minimizing Kadane yields `best_min = -8`.

Answer = `max(3, -(-8))` = `max(3, 8)` = **8** ✓.

- **Time:** O(n) — one pass maintaining both Kadanes.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Two extremes, one answer.** The largest `abs` is always `max(most positive,
  |most negative|)`; you never need any subarray in between.
- **Empty subarray allowed** here (unlike the circular problems), so flooring
  `cur_max` at `0` and capping `cur_min` at `0` is exactly right and the answer
  is never negative.
- **All-negative** (e.g. `[-1, -2, -3]`) is driven entirely by the minimizing
  Kadane: `-best_min = 6`.
- **This is the reusable core** of the circular technique: carrying a
  max-Kadane and a min-Kadane together is precisely what Problems 2 and 3 do —
  here you simply combine them with `abs` instead of a wrap identity.
