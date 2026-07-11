# Solution — Maximum Subarray

## Brute Force

Try every start index `i` and every end index `j >= i`, sum `nums[i..j]`, and
track the maximum. Reusing a running inner sum avoids a third loop.

```python
best = float("-inf")
for i in range(len(nums)):
    running = 0
    for j in range(i, len(nums)):
        running += nums[j]
        best = max(best, running)
return best
```

- **Time:** O(n^2) — two nested loops.
- **Space:** O(1).

Correct but too slow when `n` approaches 10^5.

## Optimal Approach — Kadane's Algorithm

Define `cur` as the **maximum sum of a subarray that ends exactly at the
current index**. When we move to element `x`, a subarray ending at `x` either:

- **extends** the best subarray ending at the previous index (`cur + x`), or
- **starts fresh** at `x` (just `x`).

We always take whichever is larger, then update a global `best`:

```python
def maxSubArray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```

### Why it is correct

Every non-empty subarray ends at *some* index `j`. `cur` is, by construction,
the best sum among subarrays ending at `j`. Because `best` takes the maximum of
`cur` over all `j`, it equals the best over all subarrays. The recurrence is
optimal because a subarray ending at `j` is completely determined by whether it
also includes `j-1`: if the best run ending at `j-1` was negative, carrying it
forward can only hurt, so we restart.

### Step by step on `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| x  | cur = max(x, cur+x) | best |
|----|---------------------|------|
| -2 | -2                  | -2   |
| 1  | max(1, -1) = 1      | 1    |
| -3 | max(-3, -2) = -2    | 1    |
| 4  | max(4, 2) = 4       | 4    |
| -1 | max(-1, 3) = 3      | 4    |
| 2  | max(2, 5) = 5       | 5    |
| 1  | max(1, 6) = 6       | 6    |
| -5 | max(-5, 1) = 1      | 6    |
| 4  | max(4, 5) = 5       | 6    |

Result: **6** ✓ (the subarray `[4, -1, 2, 1]`).

- **Time:** O(n) — a single pass.
- **Space:** O(1) — two scalars.

## Key Insights & Edge Cases

- **Seed with `nums[0]`, not `0`.** Initializing `cur`/`best` to `0` breaks
  all-negative inputs (it would return `0`, which is an empty subarray). Since
  the subarray must be non-empty, start from the first element.
- **All-negative arrays** return the largest (closest to zero) element, e.g.
  `[-3, -2, -5] -> -2`. Kadane handles this automatically once seeded with
  `nums[0]`.
- **Restart intuition:** you drop the prefix precisely when the running sum has
  gone negative, because a negative prefix can never help a later subarray.
- This linear Kadane is the exact subroutine reused (twice, once mirrored) by
  every circular variant in this folder — internalize it before continuing.
