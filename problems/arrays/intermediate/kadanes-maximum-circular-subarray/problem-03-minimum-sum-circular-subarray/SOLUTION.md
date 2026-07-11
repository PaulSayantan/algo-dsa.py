# Solution — Minimum Sum Circular Subarray

## Brute Force

Try every circular start index `i` and length `L` from `1` to `n`, summing
with modular indexing, and keep the minimum.

```python
n = len(nums)
best = float("inf")
for i in range(n):
    running = 0
    for L in range(1, n + 1):
        running += nums[(i + L - 1) % n]
        best = min(best, running)
return best
```

- **Time:** O(n^2).
- **Space:** O(1).

## Optimal Approach — Two Kadanes: `min(minKadane, total − maxKadane)`

This is the exact mirror of the maximum-circular problem. A minimum-sum
subarray is one of two shapes:

1. **Non-wrapping** — an ordinary slice. The best (smallest) such sum is a
   minimizing Kadane, `minK`.
2. **Wrapping** — a prefix plus a suffix, skipping a contiguous **middle**.
   Its sum is `total - middle`. To make it as *small* as possible, the skipped
   middle must be as *large* as possible: the **maximum-sum subarray**, `maxK`.
   So the best wrapping sum is `total - maxK`.

Therefore:

```
answer = min( minK, total - maxK )
```

### The all-positive guard (mirror of all-negative)

If every element is positive, the maximum-sum subarray is the entire array, so
`total - maxK == 0`, corresponding to an **empty** subarray — not allowed.
Detect it by the sign of `minK`: if `minK > 0`, the array is all positive, and
the answer is simply `minK` (the smallest single element).

```python
def minSubarraySumCircular(nums):
    total = 0
    cur_max = best_max = nums[0]
    cur_min = best_min = nums[0]
    for i, x in enumerate(nums):
        total += x
        if i == 0:
            continue
        cur_max = max(x, cur_max + x)
        best_max = max(best_max, cur_max)
        cur_min = min(x, cur_min + x)
        best_min = min(best_min, cur_min)
    if best_min > 0:                 # all elements positive
        return best_min
    return min(best_min, total - best_max)
```

### Step by step on `nums = [-5, 3, 4, -2]`

Min-Kadane run: `cur_min`: -5 → min(3, -2)=-2 → min(4, 2)=2 → min(-2, 0)=-2,
so `minK = -5` (subarray `[-5]`).
Max-Kadane run: `cur_max`: -5 → max(3, -2)=3 → max(4, 7)=7 → max(-2, 5)=5,
so `maxK = 7` (subarray `[3, 4]`). `total = 0`.

- Non-wrapping best = `minK` = -5.
- Wrapping best = `total - maxK` = `0 - 7` = **-7** (subarray `[-2, -5]`).
- `minK = -5 <= 0`, so no all-positive guard. Answer = `min(-5, -7)` = **-7** ✓.

- **Time:** O(n) — all four running values fused into one pass.
- **Space:** O(1).

## Key Insights & Edge Cases

- **All-positive is the mirror trap.** Without `if best_min > 0` you would
  return `0` (empty subarray) instead of the smallest element. Test
  `[1, 2, 3] -> 1`.
- **Duality:** replace every `max` with `min` (and vice-versa) relative to the
  maximum-circular solution; `total - maxK` replaces `total - minK`. Deriving
  one from the other is a great way to confirm you truly understand both.
- **Equivalent trick:** min-subarray of `nums` equals `-` (max-subarray of
  `-nums`). Negating the array and reusing the maximum-circular routine is a
  valid alternative implementation.
- **Single fused pass** over `cur_max, best_max, cur_min, best_min, total`.
