# Solution — Maximum Subarray

## Brute Force

Try every pair of start/end indices and sum the slice between them.

```python
best = float("-inf")
for i in range(n):
    running = 0
    for j in range(i, n):
        running += nums[j]        # extend the current window's end
        best = max(best, running)
return best
```

- **Time:** `O(n²)` — `O(n)` starts times `O(n)` ends (with the inner running
  sum this is `O(n²)`; a naive re-sum would be `O(n³)`).
- **Space:** `O(1)`.

## Optimal Approach — 1D Kadane

The key observation is that the maximum-sum subarray *ending at index `j`* is
either:

1. just `nums[j]` on its own, or
2. `nums[j]` appended to the best subarray ending at `j - 1`.

So if we let `cur` be the best sum of a subarray ending at the current index,
the transition is:

```
cur = max(nums[j], cur + nums[j])
```

Whenever `cur + nums[j] < nums[j]` — i.e. the running prefix has gone negative
— we "restart" the window at `j`. We track the global best `ans` separately so
a later restart never erases an earlier peak.

```python
def maxSubArray(nums):
    cur = ans = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)     # extend or restart
        ans = max(ans, cur)       # remember the best seen so far
    return ans
```

**Why it is correct.** Every subarray has some end index `j`. By induction,
after processing index `j` the variable `cur` equals the maximum sum among all
subarrays ending exactly at `j` (the transition covers the only two candidates:
start fresh, or extend the optimal subarray ending at `j-1`). The global answer
is the maximum over all end indices, which `ans` accumulates. Initializing both
to `nums[0]` guarantees a non-empty subarray is always returned, which is what
makes the all-negative case yield the single largest element rather than `0`.

- **Time:** `O(n)` — one pass.
- **Space:** `O(1)`.

### Connection to Kadane 2D

In the matrix problems that follow, you fix a top and bottom row and collapse
every column in that band into a single number, producing a 1D array
`colSum`. Running exactly this routine on `colSum` gives the best rectangle for
that row band. Iterating over all `O(n²)` row bands and taking the max is the
whole Kadane 2D algorithm.

## Key Insights & Edge Cases

- **Non-empty requirement:** Initialize `cur` and `ans` to `nums[0]` (not `0`).
  Starting `ans` at `0` breaks the all-negative case, returning `0` instead of
  the largest (least negative) element.
- **Single element:** Returns that element directly — the loop body never runs.
- **All negatives:** `cur` restarts at each element, so `ans` ends up as the
  maximum single element, e.g. `[-3, -1, -2] -> -1`.
- **Overflow:** Not a concern in Python, but in fixed-width languages the
  running sum can exceed 32-bit range for long arrays; use 64-bit accumulators.
- **Extension:** To also recover the subarray *indices*, record a tentative
  start pointer that resets whenever you restart (`cur = x`), and capture
  `[start, j]` each time `ans` improves.
