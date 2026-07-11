# Solution — Maximum Subarray

## Brute Force

Try every possible subarray. For each start index `i`, extend an inner loop to
each end index `j >= i`, accumulate the running sum, and track the global
maximum.

```python
best = nums[0]
for i in range(len(nums)):
    running = 0
    for j in range(i, len(nums)):
        running += nums[j]
        best = max(best, running)
return best
```

- **Time:** O(n^2) — two nested loops over the array.
- **Space:** O(1).

(Enumerating all subarrays and re-summing each from scratch would be O(n^3);
the accumulating inner loop above already trims that to O(n^2).)

## Optimal Approach — Kadane's Algorithm

**Key observation.** The maximum subarray ending at index `i` is either:

1. just `nums[i]` on its own, or
2. `nums[i]` appended to the maximum subarray ending at `i - 1`.

If the best sum ending at `i - 1` is negative, it can only drag `nums[i]` down,
so we discard it and start a new subarray at `i`. This gives the recurrence:

```
cur = max(nums[i], cur + nums[i])
best = max(best, cur)
```

`cur` is the best sum of a subarray ending exactly at the current index; `best`
is the best over all positions seen so far.

### Reference implementation

```python
def maxSubArray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```

### Why it is correct

`cur` correctly maintains the invariant "maximum sum of a subarray ending at the
current element." Any optimal subarray ends at *some* index `k`; when the loop
reaches `k`, `cur` equals that subarray's sum (because extending the best prefix
or restarting is exactly the optimal local choice), and `best` has captured it.
Since every index is considered as a possible endpoint, the global optimum is
found.

### Step-by-step on `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| x  | cur = max(x, cur+x) | best |
| -- | ------------------- | ---- |
| -2 | -2                  | -2   |
| 1  | max(1, -1) = 1      | 1    |
| -3 | max(-3, -2) = -2    | 1    |
| 4  | max(4, 2) = 4       | 4    |
| -1 | max(-1, 3) = 3      | 4    |
| 2  | max(2, 5) = 5       | 5    |
| 1  | max(1, 6) = 6       | 6    |
| -5 | max(-5, 1) = 1      | 6    |
| 4  | max(4, 5) = 5       | 6    |

Answer: **6**.

- **Time:** O(n) — single pass.
- **Space:** O(1) — two scalars.

## Key Insights & Edge Cases

- **All negatives:** initialize `cur` and `best` to `nums[0]` (not `0`). Seeding
  with `0` would wrongly return `0` for an all-negative array, but the subarray
  must be non-empty, so the answer is the largest element.
- **Single element:** the loop body never runs; `best = nums[0]` is returned.
- **Restart condition:** `cur + x < x` exactly when `cur < 0`, so "reset when the
  running sum goes negative" and `max(x, cur + x)` describe the same rule.
- If you also need the *indices* of the subarray, record a candidate start when
  you restart and commit `(start, i)` whenever `cur` becomes the new `best`.
