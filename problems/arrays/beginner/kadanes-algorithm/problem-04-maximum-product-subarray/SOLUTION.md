# Solution — Maximum Product Subarray

## Brute Force

Compute the product of every subarray and keep the maximum.

```python
best = nums[0]
for i in range(len(nums)):
    prod = 1
    for j in range(i, len(nums)):
        prod *= nums[j]
        best = max(best, prod)
return best
```

- **Time:** O(n^2).
- **Space:** O(1).

## Optimal Approach — Kadane variant (track max AND min)

**Why plain Kadane fails.** For sums, extending a negative prefix never helps.
For products, a negative running product is *valuable*: multiply it by another
negative and it becomes a large positive. So the best product ending at `i` may
come from the **smallest** (most negative) product ending at `i - 1`.

Maintain two running values ending at the current index:

- `cur_max` — the largest product of a subarray ending here.
- `cur_min` — the smallest (most negative) product of a subarray ending here.

At each element `x` the new candidates are `x`, `cur_max * x`, and `cur_min * x`:

```
new_max = max(x, cur_max * x, cur_min * x)
new_min = min(x, cur_max * x, cur_min * x)
```

The `x`-by-itself option restarts the subarray, which also handles zeros: after
a `0`, both `cur_max` and `cur_min` reset because `x` dominates the products.

### Reference implementation

```python
def maxProduct(nums):
    cur_max = cur_min = best = nums[0]
    for x in nums[1:]:
        cands = (x, cur_max * x, cur_min * x)
        cur_max = max(cands)
        cur_min = min(cands)
        best = max(best, cur_max)
    return best
```

### Why it is correct

By induction, after processing index `i`, `cur_max` and `cur_min` are the true
maximum and minimum products of subarrays ending at `i`. The optimal subarray
ends at some index `k`; at that step it equals `cur_max`, and `best` records it.
Tracking `cur_min` is essential because a future negative multiplier turns the
minimum into the next maximum.

### Step-by-step on `[-2, 3, -4]`

| x  | candidates (x, max*x, min*x) | cur_max | cur_min | best |
| -- | ---------------------------- | ------- | ------- | ---- |
| -2 | (init)                       | -2      | -2      | -2   |
| 3  | (3, -6, -6)                  | 3       | -6      | 3    |
| -4 | (-4, -12, 24)                | 24      | -12     | 24   |

Answer: **24** (the whole array, since two negatives make a positive).

- **Time:** O(n).
- **Space:** O(1).

## Key Insights & Edge Cases

- **Swap on negatives:** multiplying by a negative flips max and min, which is
  exactly why computing both from the *same* previous pair (before overwriting)
  matters. Recompute `cur_min` from the old `cur_max`, not the new one.
- **Zeros reset the run:** when `x == 0`, all three candidates are `0`, so both
  accumulators become `0` and the next element starts a fresh subarray.
- **Non-empty requirement:** seed `best`, `cur_max`, `cur_min` with `nums[0]` so
  an all-negative array like `[-3]` correctly returns `-3` rather than `0`.
- **Single element:** loop body is skipped; `best = nums[0]`.
