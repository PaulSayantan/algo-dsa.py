# Solution — Maximum Subarray

## Brute Force

Consider every start index `i` and every end index `j >= i`, sum the slice, and
keep the maximum.

```python
best = float("-inf")
for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total += nums[j]          # extend the current window's sum
        best = max(best, total)
return best
```

- **Time:** O(n^2). (A naive triple loop that re-sums each slice is O(n^3);
  reusing `total` as above trims it to O(n^2).)
- **Space:** O(1).

Too slow for `n = 10^5`.

## Optimal Approach (Kadane — Running Best-Ending-Here)

Define `cur` = the maximum sum of a subarray that **ends exactly at the current
index**. There are only two choices for such a subarray at index `i`:

1. Extend the best subarray ending at `i-1`: `cur_prev + nums[i]`.
2. Start a brand-new subarray at `i`: `nums[i]`.

So `cur = max(nums[i], cur_prev + nums[i])`. The global answer is the maximum of
`cur` over all indices, since every subarray ends *somewhere*.

Reference implementation:

```python
def maxSubArray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)     # best subarray ending here
        best = max(best, cur)     # best subarray seen anywhere
    return best
```

**Why it is correct.** By induction `cur` correctly equals the max sum of a
subarray ending at the current index: extending is optimal when the previous
running sum is positive, and restarting is optimal when it is negative (dropping
a negative prefix can only help). Equivalently, `cur = nums[i] + max(cur_prev, 0)`.
Every non-empty subarray has some right endpoint `i`, and its sum is at most the
best subarray ending at `i`, which is `cur` at step `i`; taking the max of all
`cur` therefore finds the global optimum. Because we seed both variables with
`nums[0]` (never with `0`), all-negative inputs correctly return their largest
element rather than an empty-subarray sum of 0.

**Step-by-step** on `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`:

| i | x  | cur = max(x, cur+x) | best |
| - | -- | ------------------- | ---- |
| 0 | -2 | -2                  | -2   |
| 1 |  1 | max(1, -1) = 1      | 1    |
| 2 | -3 | max(-3, -2) = -2    | 1    |
| 3 |  4 | max(4, 2) = 4       | 4    |
| 4 | -1 | max(-1, 3) = 3      | 4    |
| 5 |  2 | max(2, 5) = 5       | 5    |
| 6 |  1 | max(1, 6) = 6       | 6    |
| 7 | -5 | max(-5, 1) = 1      | 6    |
| 8 |  4 | max(4, 5) = 5       | 6    |

Result: **6** (the subarray `[4, -1, 2, 1]`).

- **Time:** O(n) — single pass.
- **Space:** O(1).

## Key Insights & Edge Cases

- Kadane is the "running best-ending-here" pattern: the DP state is a single
  running scalar, and the answer is the running max of that scalar.
- **Never** seed `cur`/`best` to `0`. Doing so silently allows the empty
  subarray and returns `0` for all-negative arrays; this problem forbids empty
  subarrays, so seed with `nums[0]`.
- Single element returns itself.
- To also recover the subarray's boundaries, record a tentative start whenever
  you *restart* (`cur == x`), and capture `[start, i]` whenever `cur` sets a new
  `best`.
- The equivalent form `cur = x + max(cur, 0)` makes the "drop a negative
  prefix" intuition explicit.
