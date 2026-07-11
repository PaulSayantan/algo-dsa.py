# Solution — Maximum Absolute Sum of Any Subarray

## Brute Force

Enumerate every subarray, compute its sum, take the maximum absolute value.

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

## Optimal Approach — Kadane's Algorithm (twice)

**Key observation.** For any subarray with sum `S`, `abs(S)` is large exactly
when `S` is very positive or very negative. So

```
answer = max( maximum subarray sum , -(minimum subarray sum) )
```

- The **maximum** subarray sum is found by standard Kadane.
- The **minimum** subarray sum is found by "min-Kadane": replace every `max`
  with `min`.

Because the empty subarray (sum `0`) is allowed, we seed the accumulators at `0`
so the result is never negative.

### Reference implementation

```python
def maxAbsoluteSum(nums):
    cur_max = cur_min = 0
    best_max = best_min = 0
    for x in nums:
        cur_max = max(0, cur_max + x)
        cur_min = min(0, cur_min + x)
        best_max = max(best_max, cur_max)
        best_min = min(best_min, cur_min)
    return max(best_max, -best_min)
```

You can fold both passes into one loop (as above) since they are independent.

### Why it is correct

`best_max` is the largest achievable subarray sum and `best_min` the smallest
(most negative). Any subarray's absolute sum is bounded by these two extremes,
and both extremes are themselves achievable subarrays, so
`max(best_max, -best_min)` is exactly the maximum absolute sum.

### Step-by-step on `[2, -5, 1, -4, 3, -2]`

| x  | cur_max | best_max | cur_min | best_min |
| -- | ------- | -------- | ------- | -------- |
| 2  | 2       | 2        | 0       | 0        |
| -5 | 0       | 2        | -5      | -5       |
| 1  | 1       | 2        | -4      | -5       |
| -4 | 0       | 2        | -8      | -8       |
| 3  | 3       | 3        | 0       | -8       |
| -2 | 1       | 3        | -2      | -8       |

`max(best_max, -best_min) = max(3, 8) = 8`. Answer: **8**.

- **Time:** O(n) — one combined pass.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Empty subarray allowed:** seeding at `0` (rather than `nums[0]`) means the
  answer is `>= 0`, matching the problem's "possibly empty" wording.
- **All positive:** `best_min` stays `0`, so the answer is the total sum
  (the whole array is the max subarray).
- **All negative:** `best_max` stays `0`, so the answer is `-best_min`, the
  magnitude of the entire-array sum.
- **Elegant one-liner identity:** for prefix sums `P`, the answer equals
  `max(P) - min(P)` (including the empty prefix `0`). Kadane is just an O(1)-space
  way of computing that spread without storing all prefixes.
