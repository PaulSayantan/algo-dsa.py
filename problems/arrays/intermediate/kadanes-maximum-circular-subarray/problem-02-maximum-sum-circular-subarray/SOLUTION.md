# Solution — Maximum Sum Circular Subarray

## Brute Force

A circular subarray is defined by a start index `i` and a length `L` from `1`
to `n`. Try all of them, summing with modular indexing.

```python
n = len(nums)
best = float("-inf")
for i in range(n):
    running = 0
    for L in range(1, n + 1):
        running += nums[(i + L - 1) % n]
        best = max(best, running)
return best
```

- **Time:** O(n^2) — `n` start points × up to `n` lengths.
- **Space:** O(1).

Too slow when `n` reaches 3 * 10^4.

## Optimal Approach — Two Kadanes: `max(maxKadane, total − minKadane)`

Every candidate subarray is exactly one of two shapes:

1. **Non-wrapping** — an ordinary slice `nums[i..j]`. The best such sum is
   plain Kadane (maximum), call it `maxK`.
2. **Wrapping** — it takes a prefix and a suffix, skipping a contiguous
   **middle** block. Its sum is `total - (sum of the middle)`. To maximize it,
   the middle must be as small as possible: the **minimum-sum subarray**,
   `minK`. So the best wrapping sum is `total - minK`.

Therefore:

```
answer = max( maxK, total - minK )
```

### The all-negative guard (the one tricky case)

If every element is negative, the minimum-sum subarray is the *entire* array,
so `total - minK == total - total == 0`. That `0` corresponds to skipping the
whole array — an **empty** subarray, which is not allowed. Detect this with the
sign of `maxK`: if `maxK < 0`, the array is all negative, and the answer is
simply `maxK` (the least-negative single element).

```python
def maxSubarraySumCircular(nums):
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
    if best_max < 0:                 # all elements negative
        return best_max
    return max(best_max, total - best_min)
```

### Why the wrapping identity is correct

Fix any wrapping subarray. The indices it does **not** use form a single
contiguous block (the "middle"), because a wrap consists of a suffix plus a
prefix, and the leftover indices between them are contiguous. Its sum is
`total - middle`. Conversely, removing any contiguous middle (of length
`0 <= m < n`) leaves a valid wrapping (or full-array) subarray. Maximizing
`total - middle` over non-empty results means minimizing `middle`, which is
what `minK` computes — with the empty-middle case (`m = 0`, giving the whole
array) already covered by `maxK`.

### Step by step on `nums = [5, -3, 5]`

Max-Kadane run: `cur_max`: 5 → max(-3, 2)=2 → max(5, 7)=7, so `maxK = 7`
(subarray `[5,-3,5]`).
Min-Kadane run: `cur_min`: 5 → min(-3, 2)=-3 → min(5, 2)=2, so `minK = -3`
(subarray `[-3]`). `total = 7`.

- Non-wrapping best = `maxK` = 7.
- Wrapping best = `total - minK` = `7 - (-3)` = **10** (subarray `[5, 5]`).
- `maxK = 7 >= 0`, so no all-negative guard. Answer = `max(7, 10)` = **10** ✓.

- **Time:** O(n) — max-Kadane, min-Kadane, and the sum fused into one pass.
- **Space:** O(1).

## Key Insights & Edge Cases

- **All-negative is the whole trap.** Without the `if best_max < 0` guard you
  would return `0` (an empty subarray) instead of the correct least-negative
  element. Always test an input like `[-3, -2, -3] -> -2`.
- **`total - minK` encodes wrapping** by *excluding* the worst middle chunk —
  the recurring "answer = total − best_middle" identity.
- **Single fused pass.** You do not need three separate loops; carry
  `cur_max`, `best_max`, `cur_min`, `best_min`, and `total` together.
- **Length cap is automatic.** Because `minK` is over a *non-empty* subarray,
  the excluded middle has length >= 1, so the wrapping subarray has length
  <= n − 1; the full array itself is still covered by `maxK`.
- **Single element** (`n = 1`) returns that element from `maxK`.
