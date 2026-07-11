# Solution — Maximum Sum Circular Subarray

## Brute Force

Simulate the circle by considering every start index and every length up to `n`,
summing with modular indexing.

```python
n = len(nums)
best = nums[0]
for i in range(n):
    running = 0
    for length in range(1, n + 1):
        running += nums[(i + length - 1) % n]
        best = max(best, running)
return best
```

- **Time:** O(n^2).
- **Space:** O(1).

## Optimal Approach — two Kadane passes

Any optimal subarray falls into exactly one of two cases:

1. **Non-wrapping** — it lies within the array without crossing the seam. This is
   the ordinary maximum subarray, `max_kadane`.
2. **Wrapping** — it uses a suffix and a prefix, wrapping across the seam. The
   elements it *excludes* form a contiguous middle block. To maximize the
   included sum we must **minimize the excluded block**. So a wrapping maximum
   equals `total - min_kadane`, where `min_kadane` is the minimum subarray sum.

The answer is `max(max_kadane, total - min_kadane)`.

**Critical special case.** If every element is negative, the minimum subarray is
the *entire* array, so `total - min_kadane = 0`, which corresponds to choosing an
**empty** subarray — not allowed. Detect this by checking `max_kadane < 0`
(true iff all elements are negative) and return `max_kadane` directly.

### Reference implementation

```python
def maxSubarraySumCircular(nums):
    total = 0
    cur_max = best_max = nums[0]
    cur_min = best_min = nums[0]
    total = nums[0]
    for x in nums[1:]:
        total += x
        cur_max = max(x, cur_max + x)
        best_max = max(best_max, cur_max)
        cur_min = min(x, cur_min + x)
        best_min = min(best_min, cur_min)
    if best_max < 0:            # all negative -> wrap would be empty
        return best_max
    return max(best_max, total - best_min)
```

### Why it is correct

`best_max` is the best non-wrapping sum. For the wrapping case, note the seam is
crossed iff the *complement* (the removed middle) is a normal contiguous
subarray; minimizing that complement with `best_min` maximizes the wrapping sum
`total - best_min`. Taking the max of the two cases covers all subarrays. The
all-negative guard prevents the degenerate empty-subarray answer.

### Step-by-step on `[5, -3, 5]`

| x  | cur_max | best_max | cur_min | best_min | total |
| -- | ------- | -------- | ------- | -------- | ----- |
| 5  | 5       | 5        | 5       | 5        | 5     |
| -3 | 2       | 5        | -3      | -3       | 2     |
| 5  | 7       | 7        | 2       | -3       | 7     |

`best_max = 7`, `total - best_min = 7 - (-3) = 10`. Since `best_max >= 0`, the
answer is `max(7, 10) = 10`.

- **Time:** O(n) — a single combined pass.
- **Space:** O(1).

## Key Insights & Edge Cases

- **All-negative array** (Example 3): `best_max = -2` is negative, so return it
  directly; the `total - best_min` branch would incorrectly yield `0`.
- **No wrap needed** (Example 1): the non-wrapping `best_max` wins.
- **Complement intuition:** a wrapping subarray = whole array minus a contiguous
  chunk; minimizing that chunk is itself a min-subarray Kadane problem.
- **Single element:** loop skipped; returns `nums[0]`.
- Both Kadane passes run together in one loop, so despite "two passes"
  conceptually, it is one traversal in practice.
