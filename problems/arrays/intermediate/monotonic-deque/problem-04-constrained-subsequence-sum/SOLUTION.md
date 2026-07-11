# Constrained Subsequence Sum — Solution

## Brute Force

Let `dp[i]` be the maximum sum of a valid subsequence that **ends at** index `i`
(so `nums[i]` is included). To extend a subsequence into `i`, the previous chosen
element must be some `j` with `i - k <= j < i`, and we take the best such `dp[j]`
— or start fresh at `i` if no earlier element helps:

```
dp[i] = nums[i] + max(0, max(dp[i-k], ..., dp[i-1]))
```

The answer is `max(dp)`. Computing the inner max by scanning is the brute force:

```python
def brute(nums, k):
    n = len(nums)
    dp = [0] * n
    for i in range(n):
        best_prev = 0
        for j in range(max(0, i - k), i):
            best_prev = max(best_prev, dp[j])
        dp[i] = nums[i] + best_prev
    return max(dp)
```

- **Time:** `O(n * k)`.
- **Space:** `O(n)`.

Too slow for `n = 10^5` with large `k`.

## Optimal Approach (Monotonic Deque)

The `max(dp[i-k], ..., dp[i-1])` term is a **sliding-window maximum** over the
`dp` array. Maintain a deque of **indices** whose `dp` values are **decreasing**
front to back:

1. Expire the front while `dq[0] < i - k` (out of the window `[i-k, i-1]`).
2. `best_prev = max(0, dp[dq[0]]) if dq else 0`. The `max(0, ...)` lets us start a
   brand-new subsequence at `i` instead of dragging along a negative prefix.
3. `dp[i] = nums[i] + best_prev`.
4. Push `i`: pop from the back while `dp[dq[-1]] <= dp[i]`, then append.

Track a running `answer = max(answer, dp[i])`.

```python
from collections import deque

def optimal(nums, k):
    n = len(nums)
    dp = [0] * n
    dq = deque()   # indices, dp[...] decreasing front -> back
    answer = float("-inf")
    for i in range(n):
        while dq and dq[0] < i - k:
            dq.popleft()
        best_prev = dp[dq[0]] if dq else 0
        dp[i] = nums[i] + max(0, best_prev)
        answer = max(answer, dp[i])
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        dq.append(i)
    return answer
```

### Why it is correct

`dp[i]` correctly captures the best subsequence ending at `i`: either `nums[i]`
alone (`best_prev` clamped to `0`) or `nums[i]` appended to the best valid
subsequence ending in the last `k` positions. The deque supplies that windowed
max in amortized `O(1)`, keeping only non-dominated candidates in decreasing
order. Because a subsequence can end at any index, the final answer is the
maximum over all `dp[i]`, not just `dp[n-1]`.

### Step-by-step on `nums = [10, 2, -10, 5, 20], k = 2`

Window for `dp[i]` is `[i-2, i-1]`; `best_prev = max(0, dp[front])`.

| i | nums[i] | window idx | dp[front] | best_prev | dp[i]       | dq after |
|---|---------|------------|-----------|-----------|-------------|----------|
| 0 | 10      | —          | —         | 0         | 10          | [0]      |
| 1 | 2       | [0]        | dp[0]=10  | 10        | 2+10 = 12   | [1]      |
| 2 | -10     | [0,1]      | dp[1]=12  | 12        | -10+12 = 2  | [1,2]    |
| 3 | 5       | [1,2]      | dp[1]=12  | 12        | 5+12 = 17   | [3]      |
| 4 | 20      | [2,3]      | dp[3]=17  | 17        | 20+17 = 37  | [4]      |

Running max: `10, 12, 12, 17, 37` -> answer `37`, matching Example 1.

- **Time:** `O(n)` — each index is pushed and popped from the deque at most once.
- **Space:** `O(n)` for `dp` (the deque is `O(k)`).

## Key Insights & Edge Cases

- The `max(0, ...)` clamp is what makes this a *subsequence* (you may skip a bad
  stretch and restart) rather than a contiguous-subarray problem.
- The answer is `max(dp)`, **not** `dp[n-1]` — a subsequence can end anywhere.
- When all values are negative (Example 2), every `best_prev` clamps to `0`, so
  `dp[i] = nums[i]` and the answer is the single largest element.
- Always expire the deque front *before* reading it, so you never use a `dp[j]`
  with `j < i - k`.
- Storing indices (not `dp` values) is essential for the front-expiry test.
