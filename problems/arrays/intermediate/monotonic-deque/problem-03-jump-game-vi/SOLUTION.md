# Jump Game VI — Solution

## Brute Force

Define `dp[i]` = maximum score to reach index `i`. Base case `dp[0] = nums[0]`.
Transition: `dp[i] = nums[i] + max(dp[i-k], ..., dp[i-1])`. Compute it directly
by scanning the previous `k` cells for each `i`.

```python
def brute(nums, k):
    n = len(nums)
    dp = [float("-inf")] * n
    dp[0] = nums[0]
    for i in range(1, n):
        best_prev = max(dp[max(0, i - k):i])
        dp[i] = nums[i] + best_prev
    return dp[-1]
```

- **Time:** `O(n * k)` — an `O(k)` scan per index.
- **Space:** `O(n)` for the `dp` array.

At `n = 10^5` and `k` up to `10^5` this is far too slow.

## Optimal Approach (Monotonic Deque)

The only expensive part is `max(dp[i-k], ..., dp[i-1])` — a **sliding-window
maximum over the `dp` array**. Maintain a deque of **indices** whose `dp` values
are **decreasing** front to back:

1. Before computing `dp[i]`, expire the front while `dq[0] < i - k` (it left the
   window `[i-k, i-1]`).
2. `dp[i] = nums[i] + dp[dq[0]]` — the front is the best reachable predecessor.
3. Push `i`: pop from the back while `dp[dq[-1]] <= dp[i]`, then append `i`.

The answer is `dp[n-1]`.

```python
from collections import deque

def optimal(nums, k):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dq = deque([0])   # indices, dp[...] decreasing front -> back
    for i in range(1, n):
        while dq[0] < i - k:      # front slid out of [i-k, i-1]
            dq.popleft()
        dp[i] = nums[i] + dp[dq[0]]
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        dq.append(i)
    return dp[-1]
```

### Why it is correct

The recurrence is exact: to land on `i` you must have jumped from some `j` in
`[i-k, i-1]`, and you want the best such `dp[j]`. The deque holds precisely the
indices in that window that are not dominated by a later, larger `dp` value, kept
in decreasing order — so its front is the window maximum. Expiring the front by
`dq[0] < i - k` keeps the window correct; because `i` increases by one each step,
the window slides by one and the amortized cost stays `O(1)`.

### Step-by-step on `nums = [1, -1, -2, 4, -7, 3], k = 2`

The window feeding `dp[i]` is `[i-2, i-1]`; the deque front is the index of the
**maximum** `dp` value in that window. "dq after" shows the deque once index `i`
has been pushed (values decreasing front to back).

| i | nums[i] | front used | dp[i]      | dq after   |
|---|---------|------------|------------|------------|
| 0 | 1       | —          | 1          | [0]        |
| 1 | -1      | dp[0]=1    | -1+1 = 0   | [0,1]      |
| 2 | -2      | dp[0]=1    | -2+1 = -1  | [0,1,2]    |
| 3 | 4       | dp[1]=0    | 4+0 = 4    | [3]        |
| 4 | -7      | dp[3]=4    | -7+4 = -3  | [3,4]      |
| 5 | 3       | dp[3]=4    | 3+4 = 7    | [5]        |

Two steps show the invariant at work:

- At `i = 2`, pushing index `2` compares `dp[dq[-1]] = dp[1] = 0` with
  `dp[2] = -1`. Since `0 <= -1` is false, index `1` stays, so `dq = [0, 1, 2]`.
- At `i = 3`, front-expiry drops index `0` because `0 < 3 - 2 = 1`, leaving
  window `[1, 2]`; the front is index `1` (`dp[1] = 0 > dp[2] = -1`), so
  `dp[3] = 4 + 0 = 4`. Pushing index `3` then pops both `2` and `1` (their `dp`
  values are `<= 4`), leaving `dq = [3]`.

The final answer is `dp[5] = 7`, matching the expected output.

- **Time:** `O(n)` — each index enters and leaves the deque at most once.
- **Space:** `O(n)` for `dp` (the deque itself is `O(k)`).

## Key Insights & Edge Cases

- This is a **DP-optimization** use of the deque: the window slides over the `dp`
  array itself, not over the raw input.
- The deque front is the max over `[i-k, i-1]`; **always expire the front before
  reading it**, or you may include an out-of-range predecessor.
- Negative values matter — you cannot skip indices, only jump forward by up to
  `k`, so the "max previous `dp`" can be negative (Example 3 lands on `0`).
- You can drop the full `dp` array and store `dp` values only inside the deque
  (as `(index, value)` pairs) for `O(k)` extra space if desired.
- `k >= n - 1` means you can jump straight from `0` to `n-1`; the deque handles
  this naturally since the window covers all earlier indices.
